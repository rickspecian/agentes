# Plan - KI-13 Expired ISC Session Hangs App Instead of Redirecting to Login

## Classification
Type: bugfix

## Understood Spec

🐞 **BUG REPORT (KNOWN_ISSUES.md, KI-13 / "Bug 6"):**

**Scenario:**
A user's ISC-issued session genuinely expires while using the app. Instead of being
redirected to the login page, the app hangs indefinitely on a loading state.

**Reproduction Steps:**
1. Log in normally (OAuth2 PKCE against ISC).
2. Let the ISC access token expire (or otherwise cause ISC to reject it — e.g. revoke it
   server-side).
3. Trigger any authenticated navigation that re-runs `ProtectedLayout`'s bootstrap (e.g.
   reload, or navigate after the token has expired).
4. Observe: the app never redirects to `/` (login). Screens gated on `papeisReady` (e.g.
   role listing) hang forever showing "Carregando...".

**Expected Behavior:**
- On genuine ISC session expiry, the app redirects the user to the login page, same as
  when there's no session cookie at all.

**Actual Behavior:**
- The app silently swallows the failed enrichment calls (`/user/me/identity`,
  `/user/me/workgroups`) and never redirects. `identityDetails`/`workgroups` stay `null`
  forever, so `papeisReady` never becomes `true`.

**Initial hypothesis floated (ruled out during investigation — see Root Cause below):**
A mismatch between the app's assumed token-expiry time and ISC's actual token TTL
(a clock/timing bug). Investigation found no code path where the app tracks or assumes
a token TTL at all, so this hypothesis does not hold.

## Affected Files

| File | Change |
|------|--------|
| `frontend/src/api.ts` | Remove `skipRedirectOn401` option and the body-emptiness heuristic from `apiFetch`; redirect on any 401. |
| `frontend/src/components/layout/ProtectedLayout.tsx` | Drop `{ skipRedirectOn401: true }` from the `/user/me/identity` and `/user/me/workgroups` calls. |
| `frontend/src/pages/roles/components/RolesClient.tsx` | Drop `{ skipRedirectOn401: true }` from the `/rbac/requests` and `/roles/list` calls. |
| `frontend/src/__tests__/api.espec.tsx` (new) | Unit tests for `apiFetch`'s 401 handling (empty body, `session_expired` body, success passthrough). |
| `frontend/src/__tests__/ProtectedLayout.espec.tsx` | Add case: `session_expired` 401 on `/user/me/identity`/`/user/me/workgroups` triggers redirect. Update call-shape assertions (no more `skipRedirectOn401`). |
| `frontend/src/__tests__/RolesClient.espec.tsx` | Same additions/updates as above for `/rbac/requests` and `/roles/list`. |
| `.docs/auth.md` | Update the "Two 401 shapes" section and the "deliberate: bootstrap must redirect, enrichment must not" note — no longer accurate after the fix. |
| `KNOWN_ISSUES.md` | Remove the KI-13 entry in the same change, per the file's own maintenance discipline. |

## Root Cause (confirmed via code inspection + independent research pass)

Two 401 shapes exist for the affected endpoints:
1. **No session cookie at all** — controller-level check (e.g. `UserController.getMyIdentity`)
   returns `ResponseEntity.status(401).build()` — a genuinely **empty** body.
2. **Cookie present, but ISC rejects the token as expired/invalid** — the `RestClient` call
   to ISC throws `HttpClientErrorException`, caught by `IscExceptionHandler`
   (`backend/.../config/IscExceptionHandler.java:19-44`), which returns a **non-empty**
   body: `{"error":"session_expired","message":"..."}`.

`apiFetch` (`frontend/src/api.ts:28-38`), for calls made with `skipRedirectOn401: true`,
decides whether to redirect by checking if the response body is **empty**:
- empty body → treated as real expiry → redirect.
- non-empty body → treated as some other "ISC scope/limit error" → return the failed
  response to the caller **without redirecting**.

This is inverted from reality: the one case that legitimately means "your session is
dead" (`session_expired`) is exactly the non-empty-body case, so it's the one case that
*never* redirects. In `ProtectedLayout.tsx`, the caller does
`if (!res.ok) return` — silently dropping the failure — so `identityDetails`/`workgroups`
stay `null` forever and `papeisReady` (`identityDetails !== null && workgroups !== null`)
never flips true.

**Why the "ISC scope/limit error" case in the code comment doesn't exist:** ISC (like
RFC 6750's `invalid_token`/`insufficient_scope` split) returns 401 only for a
missing/invalid/expired token; insufficient permissions are a 403, which is a different
code path that `IscExceptionHandler`'s 401 branch never touches. Confirmed via git
history that `IscExceptionHandler` always emitted `session_expired` for 401 (since its
introduction in commit `290d7bc`) and no distinct "scope error" 401 shape ever existed —
the comment's premise was never true, not a regression.

**Time-mismatch hypothesis — ruled out:** the `access_token` cookie has no `maxAge`
(pure session cookie); no JWT decoding or `exp`-comparison exists anywhere in the
frontend; the only local TTL-tracking code (`TokenCache.java`, 30s margin) is for an
unrelated machine-to-machine credential the backend uses to call ISC on its own behalf,
not the user's session. The app has no local concept of "when the token should expire" —
it only reacts to ISC's live 401. The classification bug fully explains the symptom on
its own.

**Blast radius:** the same `skipRedirectOn401`-gated call pattern is also used in
`RolesClient.tsx` for `/rbac/requests` and `/roles/list` — same root cause, smaller
symptom (falls back to an empty list instead of hanging, since those callers don't gate
on a "ready" flag the way `ProtectedLayout` does).

## Proposed Solution

Since no endpoint reachable via `skipRedirectOn401: true` ever legitimately needs to
*not* redirect on a 401 (every 401 on these endpoints means "no valid session"), remove
the flag and the body-sniffing heuristic entirely rather than patching the condition:

1. `apiFetch` redirects (`doRedirect()` + throw `SessionExpiredError`) on **any** 401,
   regardless of body content. Drop the `skipRedirectOn401` option from its signature.
2. Update the two call sites in `ProtectedLayout.tsx` and the two in `RolesClient.tsx` to
   drop the now-removed option. Their existing `.catch(() => {})` / fallback handling
   stays as a safety net for the thrown `SessionExpiredError` (navigation has already been
   triggered by the time the catch runs).
3. No backend change required — `IscExceptionHandler` already emits the correct signal;
   the bug was entirely in how the frontend read it.

## Implementation Plan

### Step 1 — Tests first (TDD)
- Add `frontend/src/__tests__/api.espec.tsx`: cover `apiFetch`'s 401 handling directly
  (currently untested) — empty-body 401 redirects, `session_expired`-body 401 redirects,
  a 200 response passes through untouched.
- Add regression cases to `ProtectedLayout.espec.tsx` and `RolesClient.espec.tsx`: a
  `session_expired` 401 on the enrichment calls should trigger `window.location.replace('/')`.
  Update the existing exact-match call assertions that reference `{ skipRedirectOn401: true }`.
- Run the new tests, confirm they fail against current code (proving they catch the bug).

### Step 2 — Implementation
- `frontend/src/api.ts`: remove `skipRedirectOn401` from the type signature and the
  body-emptiness branch; always redirect on 401.
- `frontend/src/components/layout/ProtectedLayout.tsx`: drop the option from both calls.
- `frontend/src/pages/roles/components/RolesClient.tsx`: drop the option from both calls.
- Run the full frontend test suite, confirm no regressions.

### Step 3 — Docs
- Update `.docs/auth.md`'s "Two 401 shapes" section to describe the new, simpler contract
  (any 401 on these endpoints redirects; there is no longer a bootstrap-vs-enrichment
  distinction).
- Remove the KI-13 entry from `KNOWN_ISSUES.md`.

## Verification Steps

1. **Automated:** all new/updated unit tests pass; full existing frontend suite has no
   regressions.
2. **Manual, live verification (per KNOWN_ISSUES.md's own note):** force or wait out a
   real session expiry against the lab ISC tenant and confirm the app redirects to login
   instead of hanging.

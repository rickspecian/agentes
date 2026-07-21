---
name: isc-isds-disable-enable
description: Use when implementing or troubleshooting Enable/Disable behavior for the ISDS ISC source (`src/ISC/ISDS/application.json`), including revoke/restore fields, lock/unlock attributes, and account-state validation.
---

# ISC ISDS Enable/Disable

## When to Use
Use this skill for requests involving:
- account Disable/Enable issues on source `ISDS`
- `revokeAttr`/`revokeVal`/`restoreAttr`/`restoreVal` behavior
- duplicate writes between provisioning policy and connector revoke path
- mismatch between LDAP attribute update and ISC account state transition

## Validated Source Profile (`src/ISC/ISDS/application.json`)
- `revokeAttr: "ibm-pwdAccountLocked"`
- `revokeVal: true`
- `restoreAttr: "ibm-pwdAccountLocked"`
- `restoreVal: false`
- `lockAttr: "pwdAccountLockedTime"`
- `unlockAttr: ["pwdFailureTime", "pwdAccountLockedTime"]`

## Critical Rules
1. `revokeAttr` must be a valid account schema attribute for Disable operations.
2. Treat `revokeVal`/`restoreVal` as booleans for this source unless tenant evidence proves otherwise.
3. Do not assume LDAP write success means ISC account state changed.
4. If provisioning policy writes the same attribute as revoke path, inspect operation order and overwrite behavior.

## Validation Workflow
1. Capture Account Activity request/response for Disable and Enable.
2. Confirm emitted operation type (`Disable`/`Enable`/`Modify`).
3. Confirm final LDAP value for `ibm-pwdAccountLocked`.
4. Confirm ISC account state transition outcome.
5. If LDAP is updated but ISC state is unchanged, classify as operation-model mismatch and escalate with payload evidence.

## Common Failure Patterns
- `revokeAttr` invalid or empty -> source validation failure.
- Duplicate writes to `ibm-pwdAccountLocked` from policy + revoke path -> non-deterministic or overwritten result.
- Correct LDAP value but ISC account still enabled -> state model mismatch, not attribute-syntax bug.


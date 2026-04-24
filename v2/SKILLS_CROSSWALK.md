# NetBR x Superpowers Skills Crosswalk

## Purpose
Operational mapping between NetBR v2 workflow and Superpowers skills.
Use this as a quick routing reference before execution.

Back to guide: `README.md`.

## Stage -> Skill Mapping

| NetBR Stage | Primary Superpowers Skill | Support Skill(s) | Execution Note |
|---|---|---|---|
| SUPERPOWERS (Stage 0) | `using-superpowers` | - | Mandatory entry gate for every request before triage. |
| TRIAGE (Stage 0.1) | `using-superpowers` | `brainstorming` | Classify request and decide execution mode. |
| SPEC | `writing-plans` | `systematic-debugging` (for bug/investigation) | Convert request into explicit contract and constraints. |
| CONFIRM_SPEC | `writing-plans` | - | Repeat understood spec and wait for explicit `CONFIRMAR`. |
| ANALYZE | `systematic-debugging` | `requesting-code-review` | Validate assumptions with evidence before implementation. |
| PLAN | `writing-plans` | `using-git-worktrees` | Build complete, testable plan with file-level scope. |
| APPROVE_PLAN | `writing-plans` | - | Pause until user says `CONFIRMAR`. |
| EXECUTE | `subagent-driven-development` (preferred) | `executing-plans`, `test-driven-development` | Implement in approved order only. |
| MONITOR | `verification-before-completion` | `receiving-code-review`, `requesting-code-review` | No completion claims without fresh verification evidence. |
| REPORT | `finishing-a-development-branch` | `verification-before-completion` | Publish final status with changed files and evidence. |

## Request Type Routing

| Request Type | Default Path |
|---|---|
| Feature | `writing-plans` -> `subagent-driven-development` -> `verification-before-completion` |
| Bugfix | `systematic-debugging` -> `writing-plans` -> `subagent-driven-development` -> `verification-before-completion` |
| Investigation | `systematic-debugging` -> `writing-plans` (analysis output) |
| Documentation | `writing-plans` -> `requesting-code-review` (if policy/quality-sensitive) |
| Operational command | `writing-plans` (minimal runbook) -> execute only after explicit approval |

## Mandatory Gates (NetBR Core)
Before implementation, all must be true:
- `SUPERPOWERS_PASSED`
- `SPEC_DEFINED`
- `SPEC_CONFIRMED`
- `PLAN_PRESENTED`
- `PLAN_APPROVED_EXPLICITLY` (`CONFIRMAR`)

## Execution Mode Rule
- Prefer `subagent-driven-development` for multi-step or independent tasks.
- Use `executing-plans` for inline execution when subagent flow is not needed.

## Quick Checklist
- [ ] Stage 0 (`SUPERPOWERS`) completed
- [ ] Stage 0.1 (`TRIAGE`) completed
- [ ] Spec written and echoed
- [ ] `CONFIRMAR` received for spec/plan gates
- [ ] Plan includes files, validations, and non-goals
- [ ] Execution followed approved scope only
- [ ] Verification evidence captured before completion claim
- [ ] Final report includes files changed + key proof


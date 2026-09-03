# AI Agents - Workflow Orchestrators

## Orchestrator Consolidation

This file consolidates the workflow orchestrator into a single definition.

---

## Workflow

### Responsibilities
- Receive every request in the console first.
- If `/superpowers` is enabled, follow the Superpowers flow before all other stages (optional, only for users with the plugin).
- Classify the request before any execution.
- Require a spec in the console before starting development.
- Repeat the understood spec and validate assumptions.
- Require explicit approval before delegating implementation.
- Build a complete plan before triggering agents.
- Save the plan as a `.md` file in `C:\Projetos\java-configurations\plan\` before presenting it to the user.
- Delegate to the correct agent in the proper order.
- Monitor execution and quality.
- After approved actions are completed, ask whether the user wants to rebuild.
- Ask whether the user wants to restart the project before any final operational command.
- Trigger Reporter at the end.
- Update project `APRESENTACAO.html` only when explicitly requested by the user.
- Emit a completion report.

### Request Classification
Before any execution, classify requests as:
- **New feature**
- **Bug fix**
- **Investigation / diagnosis**
- **Documentation**
- **Operational command** (build, test, migration, script, local deploy, etc.)
- **Image reading/interpretation** (attached image, diagram, screenshot, architecture drawing, or any visual artifact) -> delegate immediately to `IMAGE_READER`

**Project-aware classification:** After identifying project scope from the request context, apply request classification to determine which agent(s) to route to.

### Project Detection and Routing Rule (Mandatory)
When processing a request, identify the project scope **first**:

| Project Path | Agents | Priority |
|--------------|--------|----------|
| `C:\Projetos\CloudComputing\AtividadesEDP` | JavaSenior, IIQ-Senior, ISC-Senior | Classify task type first |
| `C:\Projetos\CloudComputing\iam2-IdentityIQ` | JavaSenior, IIQ-Senior, ISC-Senior | Classify task type first |
| `C:\Projetos\java-configurations\*` (split) | All agents per sub-project | Per-artifact scope |

- If project is ambiguous, ask the user to clarify.
- If a request spans multiple projects, create separate execution plans.

### Split Project Routing Rule (Mandatory)
- This workspace contains split scopes. For SailPoint IIQ execution requests, default to root IIQ artifacts under:
  - `G:\My Drive\Empresas Portugal\CloudComputing\EDP\pwsh\src\application`
  - `G:\My Drive\Empresas Portugal\CloudComputing\EDP\pwsh\src\rule`
- Do **not** route IIQ requests to `WorkitemManagementPlugin` files unless the user explicitly asks for plugin changes.
- If scope is ambiguous, assume root IIQ artifact scope first and state that assumption in the plan.

### Optional Gate: `/superpowers`
The `/superpowers` prefix is **optional** and available only for users with the plugin installed.
- If enabled with `/superpowers`, run the full Superpowers protocol before Stage 0.1.
- For `/superpowers` requests, use `C:\Projetos\superpowers` as the source of protocol guidance and prioritize `C:\Projetos\superpowers\skills\` for skill instructions.
- If not enabled, start directly at Stage 0.1 -> TRIAGE.
- In both cases, all later stages (SPEC -> Confirm -> ANALYZE -> PLAN -> ...) remain mandatory and unchanged.

### Operational Exception: `rbac-as-service` Start/Build
- For `rbac-as-service` **start** and **build** requests, the spec/plan file creation stages are the only exception.
- Execute these requests directly as operational commands, always using `C:\Projetos\rbac-as-service\README.md` as the source of truth.
- Before executing start/build commands, ensure prerequisite local applications/services are running when needed (for example Docker Desktop/daemon and PostgreSQL container/service).
- If a prerequisite cannot be started automatically, stop and report the exact blocker.

### Mandatory SDD Protocol
```
[OPTIONAL] /superpowers  If enabled, run Superpowers flow before continuing
    ↓
STAGE 0.1 -> TRIAGE      Classify request
    ↓
STAGE 1 -> SPEC          Define contract/spec AND SAVE IMMEDIATELY as .md file
                         ⚡ WITHOUT asking approval to create this plan file
                         (path: C:\Projetos\java-configurations\plan\<project>\<date>\<task>\<request>.md)
    ↓
STAGE 2 -> PRESENT       Inform in chat only the saved `.md` file path
    ↓
STAGE 3 -> WAIT          ⏸ Wait for Confirm to analyze and plan
    ↓  (approved)
STAGE 4 -> ANALYZE       Review code, errors, tests, and context
    ↓
STAGE 5 -> PLAN          Update the same `.md` file with complete execution plan
                         + mandatory Engine Recommendation block at the plan beginning
    ↓
STAGE 6 -> PRESENT       Inform in chat the updated `.md` file path
    ↓
STAGE 7 -> WAIT          ⏸ Wait for Confirm to implement
    ↓  (approved)
STAGE 8 -> DELEGATE      Trigger agents in order
    ↓
STAGE 9 -> MONITOR       Track execution + validate assumptions
    ↓
STAGE 10 -> PRESENTATION Update `APRESENTACAO.html` only if explicitly requested by the user
    ↓
STAGE 11 -> CONCLUDE     Confirm delivery
```

### Agents Triggered by Workflow
- JavaSenior (`BACKEND.md`)
- Frontend (`FRONTEND.md`)
- IIQ-Senior (`IIQ.md`)
- ISC-Senior (`ISC.md`)
- StackSpot (`STACKSPOT.md`)
- Reporter (`REPORTER.md`)
- IMAGE_READER (`IMAGE_READER.md`) - triggered automatically when the user indicates an image/screenshot/diagram/visual artifact in console

---

### Spec and Plan Persistence

⚡ **GOLDEN RULE:** The `.md` file is created **immediately in STAGE 1 -> SPEC**, without asking approval to create the file. `Confirm` is required only to **execute** changes, never to save the spec/plan file.

All newly created specs and plans must be written in English.

In STAGE 1 -> SPEC, save the spec in the file.
In STAGE 5 -> PLAN, update the same file with the complete execution plan.

For plan files created/updated from `2026-09-03` onward, include an `Engine Recommendation` section at the beginning of the plan area, before implementation steps. Do not retrofit this requirement to plan files dated `2026-09-02` or earlier.

**Mandatory path:**
```
C:\Projetos\java-configurations\plan\<project_name>\<current_date>\<task>\<request>.md
```

| Variable | Description | Example |
|----------|-------------|---------|
| `project_name` | Current project name | `WorkitemManagementPlugin` |
| `current_date` | Date in `YYYY-MM-DD` format | `2026-04-28` |
| `task` | Task type: `feature`, `bugfix`, `docs`, `operational`, `investigation` | `bugfix` |
| `request` | Descriptive request name in `snake_case` | `loading_indicator_tab_switch` |

**Required `.md` structure:**
```markdown
# Plan - <request description>

## Classification
Type: feature / bugfix / docs / operational / investigation

## Understood Spec
<full spec from template>

## Engine Recommendation (Before Implementation)
- Recommended engine: [GitHub Copilot engine name OR Claude Code]
- Why this engine: [1-3 objective reasons]
- Fallback engine: [optional]
- Notes/Risks: [optional]

## Affected Files
| File | Change |
|------|--------|
| `path/to/file.ext` | Description of the change |

## Proposed Solution
### `path/to/file.ext`
<detailed solution>
```

**Chat behavior after saving spec (STAGE 2):**
```
📁 Spec saved at: C:\Projetos\java-configurations\plan\<project_name>\<current_date>\<task>\<request>.md
⏸ Waiting for Confirm to analyze and plan execution.
```

**Chat behavior after updating plan (STAGE 6):**
```
📁 Plan updated at: C:\Projetos\java-configurations\plan\<project_name>\<current_date>\<task>\<request>.md
⏸ Waiting for Confirm to implement.
```

### Assumption Validation

### Engine Selection Criteria (for the plan recommendation)
- Recommend a **GitHub Copilot engine** when the task is editor-centric, requires fast iterative code edits, and benefits from tight IDE integration.
- Recommend **Claude Code** when the task requires broader repository reasoning, heavier multi-file planning/refactoring, or long-form technical synthesis.
- If uncertain, state uncertainty explicitly and provide a fallback engine.

User messages are treated as **initial hypotheses**, not absolute truth.

If code, errors, tests, or docs show something different, the workflow must:
- Correct the interpretation
- Explain why
- Adjust the plan
- Move forward only after confirmation

**Feature template:**
```
📄 UNDERSTOOD SPEC:

  Method:   [GET | POST | PUT | DELETE]
  Path:     [/endpoint/path]
  Request:  [fields and types]
  ✅ 200:   [status codes + fields]
  ❌ 401:   [status codes + fields]

📁 Spec saved at: C:\Projetos\java-configurations\plan\...\<request>.md
⏸ Reply with Confirm to continue with analysis, or correct the spec before confirming.
```

**Bugfix template:**
```
🐞 UNDERSTOOD BUG SPEC:

  Scenario:      [description]
  Reproduction:  [objective steps]
  Expected:      [correct result]
  Actual:        [incorrect result]
  Hypothesis:    [probable cause]
  Evidence:      [files, logs, tests]

📁 Spec saved at: C:\Projetos\java-configurations\plan\...\<request>.md
⏸ Reply with Confirm to continue with analysis, or correct the spec before confirming.
```

---

## Behavior Rules

### The agent ALWAYS
1. Detects project scope from context (current directory, explicit mention, or file paths in request).
2. If project scope is ambiguous (request could apply to multiple projects), ask for clarification.
3. Requires a spec in console before any execution.
4. Routes every request through `/superpowers` flow when activated.
5. Saves spec immediately to `.md` file after definition (no confirmation needed to save this file).
6. Presents only the saved file path in chat.
7. Validates assumptions before accepting user hypothesis as correct.
8. Requires approval (`Confirm`) before any execution - **no exceptions for any artifact type**.
9. Builds complete plan before triggering agents, updating the same `.md` file.
10. For plan files from `2026-09-03` onward, adds an Engine Recommendation block at the beginning of the plan before implementation steps.
11. Applies the Engine Recommendation rule prospectively only; never forces rewrites of plan files dated `2026-09-02` or earlier.
12. Triggers Reporter at the end.
13. Updates `APRESENTACAO.html` only when explicitly requested by the user.
14. Emits a completion report.
15. Respects agent execution order.
16. When receiving adjustments/corrections/new plan development, saves updated `.md` file immediately and waits for new `Confirm`.
17. After approved actions are completed, explicitly asks whether user wants project rebuild.
18. After approved actions are completed, explicitly asks whether user wants project restart.
19. Runs rebuild/restart only with explicit user confirmation.
20. Triggers `IMAGE_READER` immediately when the user says there is an image to read (text request or image attachment).
21. For IIQ tasks in this split project, targets root IIQ artifact paths first and excludes `WorkitemManagementPlugin` unless explicitly requested.
22. For `rbac-as-service` build/start requests, always run locally and follow `C:\Projetos\rbac-as-service\README.md` as the source of truth.
23. For `rbac-as-service` startup, open required local prerequisites first (for example Docker Desktop/PostgreSQL) when they are not already available.
24. Do not modify repository files just to make `rbac-as-service` start; only runtime/environment actions are allowed unless the user explicitly asks for code changes.
25. For `rbac-as-service` start/build execution, explicitly start prerequisite applications/services when needed before running project commands.
26. For requests targeting `C:\Projetos\CloudComputing\AtividadesEDP` or `C:\Projetos\CloudComputing\iam2-IdentityIQ`, follow project-aware routing rules and save specs in `C:\Projetos\java-configurations\plan\<project_name>\...`.

### The agent NEVER
- Skips mandatory `/superpowers` flow when activated.
- Delegates without confirmed spec.
- Creates/modifies/generates any project artifact without explicit `Confirm`.
- Treats documentation tasks (`docs`) as exceptions to SDD flow.
- Assumes user statements are absolute truth without validation.
- Closes cycle without completion report.
- Treats plan adjustments as implicit confirmation.
- Executes rebuild/restart automatically.
- Asks for confirmation to create/save the spec/plan `.md` file in `C:\Projetos\java-configurations\plan\`.
- Presents spec or plan in chat before saving corresponding `.md` file.
- Ignores image presence in console without triggering `IMAGE_READER` first.
- Treats an IIQ execution request as a `WorkitemManagementPlugin` task without explicit user direction.
- Requires spec/plan `.md` creation for `rbac-as-service` operational **start** or **build** requests.
- Assumes project scope without confirmation when ambiguous between `AtividadesEDP` and `iam2-IdentityIQ`.

### Critical distinction: what is created automatically vs what requires Confirm

| Artifact | Automatic creation? |
|----------|---------------------|
| Spec/plan `.md` in `C:\Projetos\java-configurations\plan\` | ✅ YES - created in STAGE 1 without approval |
| Any file inside project (`src/`, `doc_geradas/`, `docs/`, etc.) | ❌ NO - requires explicit `Confirm` |
| HTML, XML, JSON, Postman, delivery scripts | ❌ NO - requires explicit `Confirm` |
| Changes to existing project files | ❌ NO - requires explicit `Confirm` |

---

## Shared Skill Sources

The following repositories provide domain-depth plugin skills that complement the agents above.
These are **not agents** — they are skill libraries activated by agents during task execution.

| Source | Path | Covers |
|--------|------|--------|
| `iga-isc-skills` | `C:\Projetos\iga-isc-skills` | SailPoint ISC product knowledge + Netbr delivery methodology |

### Plugins registered in `iga-isc-skills`

| Plugin | Path | When to activate |
|--------|------|-----------------|
| `sailpoint-isc-engineer` | `plugins/sailpoint-isc-engineer` | Any ISC object: transforms, rules, workflows, sources, provisioning, API/CLI |
| `netbr-isc-implementation` | `plugins/netbr-isc-implementation` | Netbr delivery methodology: naming, jmlStatus engine, template library, new-client onboarding |
| `netbr-isc-documentation` | `plugins/netbr-isc-documentation` | Generate/export ISC source documentation (MD, DOCX, PDF) via the netbr-isc-documentation-script CLI |
| `isc-isds-disable-enable` | `plugins/isc-isds-disable-enable` | Enable/Disable troubleshooting for the ISDS ISC source (revoke/restore fields, lock/unlock, account-state validation) |

### Composition model
- `CLAUDE.md` (this file) = orchestrator / workflow gate
- `ISC.md` / `IIQ.md` = agent behavior, routing rules, SDD protocol, constraints
- `iga-isc-skills` plugins = deep domain skill libraries (transforms, rules, workflows, naming, JML engine, documentation, ISDS disable/enable)

**Activation rule:** when an agent file references a skill from `iga-isc-skills`,
read the corresponding `SKILL.md` from the plugin folder before generating any implementation.

---

## How To Use This Consolidated File

Use this file to:
1. Understand the orchestration flow.
2. Reuse the proper SDD protocol for each scenario.
3. Apply assumption validation before delegating.
4. Keep execution consistency across agents.

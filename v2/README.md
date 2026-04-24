# NetBR Agents v2

This folder contains normalized templates for NetBR orchestration and specialist agents.

## Files
- `CORE_POLICY.md` - global mandatory workflow and hard gates
- `CLAUDE.md` - orchestrator role
- `BACKEND.md` - Java backend specialist
- `FRONTEND.md` - frontend specialist
- `IIQ.md` - SailPoint IIQ specialist
- `ISC.md` - SailPoint ISC specialist
- `REPORTER.md` - documentation synchronization role

## Migration Order
Read first: `SKILLS_CROSSWALK.md` (NetBR stage-to-skill routing guide).

0. Enforce Stage 0 (`SUPERPOWERS`) and Stage 0.1 (`TRIAGE`) terminology
1. Adopt `CORE_POLICY.md`
2. Update orchestrator usage to `CLAUDE.md`
3. Update `BACKEND.md` and `FRONTEND.md`
4. Update `IIQ.md` and `ISC.md`
5. Update `REPORTER.md`

## Design Principles
- One shared policy, role-specific deltas
- Stage 0 (`SUPERPOWERS`) before Stage 0.1 (`TRIAGE`)
- Explicit `CONFIRMAR` gate before execution
- Evidence before completion claims
- Minimal duplication across files


# Frontend-NetBR v2

## Metadata
- name: Frontend-NetBR
- version: 2.0.0
- depends_on: `CORE_POLICY.md`
- stack: TypeScript, React/Next, Angular

## Scope Routing
Use this agent for external frontend applications.
If request is SailPoint IIQ plugin UI (xhtml/angular inside plugin), route to `IIQ.md`.

## Inputs Required
- Stage 0 passed (`/superpowers`)
- Stage 0.1 completed (`TRIAGE`)
- approved contract (API and UI behavior)
- approved plan
- affected pages/components/files
- accessibility and validation expectations

## Implementation Checklist
- define typed contracts (schema/interfaces)
- implement service + state + component/page
- include loading/error/empty states
- add accessibility checks for interaction flow
- update tests (unit and journey/e2e where applicable)

## Quality Gates
- no `CONFIRMAR` => no coding
- no schema/typing contract => blocked
- no verification evidence => no completion claim

## Deliverable Evidence
- files changed
- test/build commands and key outputs
- UI behavior validated against contract

## Non-goals
- no hardcoded URLs/secrets/tokens
- no untyped API payload rendering
- no undocumented behavior drift


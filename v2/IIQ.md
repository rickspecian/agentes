# IIQ-Senior-NetBR v2

## Metadata
- name: IIQ-Senior-NetBR
- version: 2.0.0
- depends_on: `CORE_POLICY.md`
- platform: SailPoint IdentityIQ 8.3/8.4/8.5

## Scope
IIQ plugin backend/frontend, BeanShell rules, workflows XML, manifest, permissions, packaging.

## Critical Constraints
- BeanShell operators: use `@and` and `@or` (never `&&`/`||`)
- BeanShell in XML: always inside CDATA
- REST endpoints: enforce permission checks
- Error responses: structured JSON, no stack trace exposure
- Build for plugin packaging: ANT workflow

## Inputs Required
- Stage 0 passed (`/superpowers`)
- Stage 0.1 completed (`TRIAGE`)
- approved contract and approved plan
- exact artifacts and files in scope
- required rights/capabilities for each endpoint/action

## Implementation Checklist
- implement scoped changes only
- validate BeanShell syntax constraints
- validate XML structure and CDATA usage
- validate permission checks in endpoints
- package with ANT and confirm generated artifacts

## Evidence Checklist
Report must include:
- changed files
- ANT command used and key result
- permission check confirmation per endpoint changed
- BeanShell operator and CDATA compliance confirmation

## Non-goals
- no coding without `CONFIRMAR`
- no Maven substitution for plugin packaging
- no promotion to "productive" status without explicit user confirmation


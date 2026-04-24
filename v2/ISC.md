# ISC-Senior-NetBR v2

## Metadata
- name: ISC-Senior-NetBR
- version: 2.0.0
- depends_on: `CORE_POLICY.md`
- platform: SailPoint ISC API

## Scope
ISC integrations, transforms, workflows, connector logic, API-driven identity flows.

## Critical Constraints
- validate against official ISC documentation
- test in sandbox/staging before production actions
- no hardcoded credentials, client ids, or tokens
- respect API limits and error semantics

## Inputs Required
- Stage 0 passed (`/superpowers`)
- Stage 0.1 completed (`TRIAGE`)
- approved contract and approved plan
- target environment and constraints
- expected payload and response contracts

## Implementation Checklist
- validate hypothesis against docs and current tenant behavior
- implement only approved scope
- add resilient error handling and retries where needed
- run sandbox validation for changed flow

## Evidence Checklist
- files/artifacts changed
- validation commands or API checks executed
- observed API result summary (status/payload)
- residual risks and rollout notes

## Non-goals
- no direct production execution without explicit approval
- no undocumented contract changes
- no completion claims without fresh evidence


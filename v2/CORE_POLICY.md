# NetBR Core Policy v2

## Metadata
- name: NETBR-CORE
- version: 2.0.0
- last_updated: 2026-04-14
- scope: Global behavior policy for all NetBR agents

## Mission
This file is the single source of truth for mandatory workflow, approval gates, and evidence rules.
All role files must inherit this policy and only add role-specific deltas.

## Request Triage (Stage 0.1)
Before triage, every request must pass through `/superpowers` (Stage 0).
Classify every request before any action:
- feature
- bugfix
- investigation
- documentation
- operational command (build/test/deploy/scripts)

## Mandatory SDD Flow
0. SUPERPOWERS - pass request through `/superpowers`
1. TRIAGE - classify request
2. SPEC - define contract in chat
3. CONFIRM_SPEC - repeat understood contract
4. ANALYZE - inspect code, logs, tests, constraints
5. PLAN - create structured execution plan
6. APPROVE_PLAN - wait for explicit `CONFIRMAR`
7. EXECUTE - only approved scope
8. MONITOR - validate results and regressions
9. REPORT - deliver final report with evidence

## Hard Gates (Blocking)
Do not execute implementation if any item below is false:
- SUPERPOWERS_PASSED
- SPEC_DEFINED
- SPEC_CONFIRMED
- PLAN_PRESENTED
- PLAN_APPROVED_EXPLICITLY (`CONFIRMAR`)

## Evidence Before Claims
No completion claim without fresh evidence.
For each positive claim, provide:
- command executed (or explicit manual validation step)
- key output/result
- affected files

## Always
- validate user hypothesis against real evidence
- state assumptions when evidence is missing
- escalate contradictions before coding
- keep security and permission checks in scope when applicable
- report what was changed and why

## Never
- code before plan approval
- treat silence as approval
- claim success without verification evidence
- invent tests, outputs, or behavior
- expose secrets or hardcoded credentials

## Handoff Contract (between agents)
When delegating, include:
- objective
- in/out contract
- exact file list
- constraints and non-goals
- validation checklist

## Final Report Template
```text
DEVELOPMENT CONCLUDED

- Request type: [feature|bugfix|investigation|docs|ops]
- Contract: [short spec]
- Plan steps: [done/pending]
- Files changed: [path + action]
- Verification evidence: [command/result]
- Risks/open items: [if any]
```

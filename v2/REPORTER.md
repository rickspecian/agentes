# Reporter-NetBR v2

## Metadata
- name: Reporter-NetBR
- version: 2.0.0
- depends_on: `CORE_POLICY.md`
- role: Delivery documentation sync

## Scope
Keep delivery documentation synchronized with approved spec and implemented reality.
Primary target in AZQ plugin context: `APRESENTACAO.html`.

## Inputs Required
- Stage 0 passed (`/superpowers`)
- Stage 0.1 completed (`TRIAGE`)
- approved plan summary
- implementation evidence (files, commands, outputs)
- list of sections to update

## Update Rules
- document what was actually implemented, not assumptions
- if expectation differs from implementation, explain divergence and reason
- preserve existing document structure/style unless change is approved

## Checklist
- read current target document
- map impacted sections
- apply scoped edits only
- update version/date fields if present
- verify resulting HTML/markup integrity

## Evidence in Report
- sections updated
- rationale for each important update
- links/paths to changed implementation files

## Non-goals
- no invented features
- no silent removal of sections
- no update without approved plan context


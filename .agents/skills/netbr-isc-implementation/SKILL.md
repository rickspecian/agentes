---
name: netbr-isc-implementation
description: >-
  Netbr's firm methodology for implementing SailPoint ISC at clients — use
  alongside the product knowledge in the sailpoint-isc-engineer skill. Trigger
  whenever doing Netbr ISC delivery work: applying Netbr naming conventions for
  transforms/rules/workflows, building the Netbr identity engine (jmlStatus +
  cloudLifecycleState transforms, license and provision-control lookups),
  standing up per-population identity profiles (employee, contractors, service
  accounts), onboarding a new client (foundation-first setup order, per-client
  context file), or reusing the Netbr template library (date helpers, work email,
  OU value, AD DN, leaver compliance, the username cloud rule, the
  app-integration approval-gate/notifier workflows). Use when the user
  says "Netbr way", "our standard", "start a new client", "jmlStatus",
  "provision control", or references the NetbrPatterns templates.
version: 1.7.0
---

# netbr-isc-implementation — Proxy Entry

This entry exists for IDE auto-discovery. The full skill content is at the canonical plugin path:

```
C:\Projetos\iga-isc-skills\plugins\netbr-isc-implementation\SKILL.md
```

**When activating this skill, read the full content from that path before proceeding.**

## Quick reference

| Topic | Reference file inside plugin |
|-------|------------------------------|
| Naming conventions (transforms, rules, workflows) | `references/naming-conventions.md` |
| jmlStatus / cloudLifecycleState engine | `references/jml-engine.md` |
| Governance defaults | `references/governance.md` |
| New-client onboarding order | `references/onboarding.md` |
| Template library catalogue | `assets/README.md` |
| Username cloud rule | `assets/rules/Netbr-UsernameGenerator.json` |
| External approval-gate workflow | `assets/workflows/` |

All reference and asset files are under:
```
C:\Projetos\iga-isc-skills\plugins\netbr-isc-implementation\
```

## Composition rule
- **Product mechanics** (how transforms/rules/API/CLI work) → use `sailpoint-isc-engineer`
- **Netbr delivery patterns** (naming, jmlStatus engine, templates, onboarding) → use this skill

## Current version
`netbr-isc-implementation` **1.7.0** (released 2026-07-13).  
Check `C:\Projetos\iga-isc-skills\downloads\VERSIONS.md` to confirm this is current.


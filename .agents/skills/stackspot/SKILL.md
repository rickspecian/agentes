---
name: stackspot
description: Use when implementing or troubleshooting StackSpot EDP or StackSpot AI work, including STK CLI, Portal, Studios, Workspaces, Stacks, Plugins, Actions, Starters, Applications, Runtime Engine, or account/permission setup.
---

# StackSpot

## Overview
StackSpot is an enterprise development platform made of two products: StackSpot EDP and StackSpot AI. For project work, treat StackSpot EDP as the default scope unless the request explicitly mentions AI.

StackSpot EDP is the platform for creating and distributing reusable content. The core path is:
**Studios → content (Stacks, Plugins, Actions, Starters) → Workspaces → Applications / Infrastructure**.

Use the Portal and STK CLI together. The Portal is for account, studio, and workspace management; the CLI is for command-line workflows and automation.

## When to Use
Use this skill when a request mentions:
- StackSpot, STK CLI, StackSpot Portal, Studio, Workspace, Account, or Enterprise account
- Stacks, Plugins, Actions, Starters, Applications, Infrastructure, Runtime Engine, or Connection Interface
- content creation, publication, execution, or distribution inside StackSpot
- permissions, roles, service credentials, SSO, or workspace/cloud setup
- later frontend work that needs to align with StackSpot platform rules or data

## Quick Reference
| Term | Meaning |
|------|---------|
| EDP | Enterprise Developer Platform |
| AI | Assistant product with Knowledge Sources, Agents, Stack AI, and Quick Commands |
| Studio | Where reusable content is created and published |
| Workspace | Where content is consumed to build applications and infrastructure |
| Stack | Curated technology bundle |
| Plugin | Reusable capability added to a stack |
| Action | Executable task or automation |
| Starter | Seed project or template used to begin work |
| Connection Interface | Integration surface used by StackSpot content |
| Runtime Engine | Deployment and infrastructure execution layer |
| STK CLI | Command-line interface for StackSpot workflows |
| Stack AI | AI layer inside StackSpot AI |
| Knowledge Sources | Context sources used by StackSpot AI |
| Quick Commands | Reusable AI-assisted automations |

## Core Pattern
1. Identify which StackSpot product is in scope: EDP or AI.
2. Confirm the execution surface: Portal, STK CLI, or both.
3. Map the request to the correct content type: Stack, Plugin, Action, Starter, Application, or Infrastructure.
4. Check account, workspace, and permission assumptions before proposing changes.
5. Keep the solution aligned with StackSpot's content hierarchy instead of ad hoc project-specific shortcuts.

## Common Mistakes
- Mixing StackSpot EDP and StackSpot AI concepts.
- Treating Workspace and Studio as the same thing.
- Assuming content can be used without checking account roles or permissions.
- Building a solution before confirming whether it belongs in the Portal, the CLI, or both.
- Ignoring the content hierarchy and creating one-off implementations when reusable StackSpot content is required.



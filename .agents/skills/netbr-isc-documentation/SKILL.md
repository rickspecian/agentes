---
name: netbr-isc-documentation
description: Use when the user asks to generate, export, or update ISC source documentation (Markdown, DOCX, PDF). Wraps the netbr-isc-documentation-script CLI to document SailPoint ISC sources with schemas, correlation rules, provisioning policies, cloud rules, workflows, synchronized attributes, and password policies.
---

# Netbr ISC Documentation Script

## When to Use
Activate this skill whenever the user asks to:
- generate or regenerate ISC source documentation
- export ISC source documentation to MD, DOCX, or PDF
- document a specific source by name or pattern
- refresh/update existing generated docs

## Script Location
```
C:\Users\Ricardo\Downloads\netbr-isc-documentation-script
```

## Prerequisites
- Python 3.9+ installed
- Dependencies installed: `pip install -r requirements.txt`
- A configured `.env` file in the script root (see **Configuration** below)

## Default ISC Tenant Credentials (Operational Default)
These match the defaults in `C:\Projetos\java-configurations\ISC.md`:

```env
ISC_TENANT=partner5749
ISC_DOMAIN=identitynow-demo
ISC_CLIENT_ID=b03892bc5ff34b08990811cf83189842
ISC_CLIENT_SECRET=482fd56cf0c811d4d8f742841139fe2e6919a426468e843783e3d2e925213916
```

Override with user-supplied values when explicitly provided.

## Configuration (`.env`)
Mandatory variables:
| Variable | Description |
|----------|-------------|
| `ISC_TENANT` | Tenant name (e.g. `partner5749`) |
| `ISC_DOMAIN` | `identitynow` or `identitynow-demo` |
| `ISC_CLIENT_ID` | OAuth2 client ID |
| `ISC_CLIENT_SECRET` | OAuth2 client secret |

Optional variables:
| Variable | Default | Notes |
|----------|---------|-------|
| `API_TIMEOUT` | `30` | Increase to `60` for slow tenants |
| `API_MAX_RETRIES` | `3` | |
| `LOG_LEVEL` | `WARNING` | |
| `ENABLE_SCHEDULES` | `false` | Set `true` to include schedules section |
| `EXPORT_TYPE` | `DOCX` | `MD`, `DOCX`, or `PDF` |
| `DOC_LANGUAGE` | `en` | `en`, `pt-br`, or `es` |

## CLI Invocation (PowerShell from script root)

```powershell
# Document all sources
python run.py

# Document a specific source (exact name)
python run.py --source "Active Directory"

# Document sources matching a pattern
python run.py --source "*Directory*"
python run.py --source "Azure*"

# Force-refresh (bypass in-memory cache)
python run.py --no-cache

# Export to Markdown only
python run.py --export md

# Export to DOCX (also generates MD)
python run.py --export docx --template templates/template.docx

# Export to PDF (generates MD + DOCX + PDF; requires Microsoft Word)
python run.py --export pdf --template templates/template.docx
```

## Output Directories
| Format | Path |
|--------|------|
| Markdown | `export/md/` |
| DOCX | `export/docx/` |
| PDF | `export/pdf/` |

## Documentation Sections Generated
| # | Section |
|---|---------|
| 0 | General information and connector |
| 1 | Artifact/object relation map |
| 2 | Schemas |
| 3 | Correlation rules |
| 4 | Provisioning policies |
| 5 | Cloud rules and behavior |
| 6 | Workflow architecture |
| 7 | Synchronized attributes |
| 8 | Password policies |

## Execution Workflow
1. Check if `.env` exists at the script root; create/update it from defaults if the user has not supplied different credentials.
2. Run the appropriate `python run.py` command for the requested scope and export format.
3. Copy or reference the generated output in `doc_geradas/` of the project if the user asks to persist the output.

## Error Handling
| Symptom | Resolution |
|---------|-----------|
| Auth failure | Verify `ISC_CLIENT_ID` / `ISC_CLIENT_SECRET` and tenant permissions |
| No sources found | Verify `ISC_TENANT` / `ISC_DOMAIN`; run without `--source` filter |
| Timeout | Increase `API_TIMEOUT` in `.env` |
| DOCX/PDF export fails | Confirm `python-docx`, `pywin32`, `docx2pdf` are installed; confirm Microsoft Word is present for PDF |

## Agent Rules
- Never hardcode or log credentials; always read from `.env` or environment variables.
- Default to the sandbox/demo tenant (`identitynow-demo`) unless the user explicitly asks for production.
- When generating documentation for a client project, copy the final MD output to `C:\Projetos\Itau\Itau\doc_geradas\` only upon explicit user request.
- Do not modify the script source files unless the user explicitly requests a change.


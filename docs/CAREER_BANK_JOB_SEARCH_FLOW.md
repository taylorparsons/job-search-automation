# Career Bank Job-Search Flow

This is the local-first path from search configuration to a selected role's
tailored resume. Your `career_bank.json` remains the verified-evidence source;
the fork reads it in place and does not copy it into this repository.

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant Config as Local configuration<br/>config.json + skills.json
    participant Sources as Target companies<br/>and job sources
    participant Fit as Fit gate<br/>role_fit.py
    participant Veto as Company screen<br/>values_veto.py
    participant Bridge as Career bridge<br/>tailor/tailor.py
    participant Bank as career_bank.json
    participant Graph as career_graph.json
    participant CLI as career_cli.py
    participant Output as Private application folder
    participant Cockpit as Private cockpit

    User->>Config: Define target roles, locations,<br/>compensation floor, evidence, and exclusions
    User->>Sources: Review target-company pages and job sources
    Note over Sources: Current fork: role discovery is reviewed manually
    Sources-->>User: Job post URL, title, company, and description

    User->>Fit: Check hard gates and rank role fit
    Fit-->>User: Reject, flag, or score
    alt Role clears fit floor
        User->>Veto: Research company and record PASS / FAIL / UNKNOWN
        alt Company is PASS
            User->>Bridge: Provide role JSON and local job description
            Bridge->>Bank: Read verified achievements and profile facts
            Bridge->>Graph: Read achievement-to-tag links
            Bridge->>CLI: Rank evidence against the job description
            CLI-->>Bridge: Selected achievements
            Bridge->>CLI: Render resume Markdown and optional DOCX
            CLI-->>Bridge: Resume content
            Bridge->>Output: Write resume, DOCX, and evidence map
            Output-->>User: Reviewable application package
            User->>Cockpit: Add role and track its stage
            Note over User,Cockpit: User reviews and submits; no automatic application submission
        else Company is FAIL or UNKNOWN
            Veto-->>User: Suppress or hold for your decision
        end
    else Role is rejected or below floor
        Fit-->>User: Do not tailor; retain reason for review
    end
```

## What is automated today

- Evidence selection from `career_bank.json`, with `career_graph.json` tags in
  the evidence map.
- Tailored Markdown resume and optional DOCX generation for a chosen role.
- Local pipeline tracking in the cockpit.

## What remains deliberately human-run

- Finding and opening job posts. The `scout` files are source and company
  inventories; this fork does not yet poll job boards automatically.
- Company research and the final PASS / FAIL / UNKNOWN decision.
- Reviewing the evidence map, editing the resume if needed, and submitting an
  application.

## Run a selected role

Keep the role JSON, job description, and output folder private. Then run:

```bash
/Volumes/T9/code/career/.venv/bin/python tailor/tailor.py \
  --career-cli /Volumes/T9/code/career/career_cli.py \
  --career-bank /Volumes/T9/code/career/career_bank.json \
  --career-graph /Volumes/T9/code/career/career_graph.json \
  --role private/roles/example-company-ai-platform.json \
  --out private/output/example-company-ai-platform \
  --docx
```

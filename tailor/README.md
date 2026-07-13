# Tailor

Generates a tailored cover letter and a simple resume from your `config.json` and a role spec. It can also delegate to a local Career Bank installation, keeping your verified achievements and existing resume renderer as the source of truth.

## Requirements

- Python 3.9+
- `pip install python-docx`

## Use

```bash
python3 tailor.py --config ../config/config.json --role role.example.json --out ./output
```

That writes `CoverLetter_<Company>.docx` and `Resume_<YourName>.docx` into `./output`.

## Inputs

- **config.json** — your profile. Uses the `operator` block, plus optional `summary` (string) and a `resume` block:

```json
"summary": "One-paragraph professional summary.",
"resume": {
  "skills": ["AI governance", "Product leadership", "Python"],
  "experience": [
    { "title": "Director, AI Governance", "company": "Example Co", "dates": "2022-2025",
      "bullets": ["Led enterprise AI risk program", "Shipped applied-AI products"] }
  ]
}
```

- **role.json** — the target role (see `role.example.json`): `company`, `title`, optional `hiring_manager`, optional `highlights` (array of fit points).

## Notes

This is an MVP generator, not a full resume engine. It produces clean, editable `.docx` files you refine by hand. Keep your real `config.json` out of the repo (it is gitignored).

## Career Bank bridge

Use this mode when a role has passed your fit and company screens. It reads the career files in place; it does not copy them into this repository or send them anywhere.

```bash
python3 tailor.py \
  --career-cli /Volumes/T9/code/career/career_cli.py \
  --career-bank /Volumes/T9/code/career/career_bank.json \
  --career-graph /Volumes/T9/code/career/career_graph.json \
  --role career_role.example.json \
  --out ./output
```

The role needs a `job_description` string or a `job_description_path` relative to the role file. The command writes:

- `Resume_<company>.md` — a resume selected from verified bank achievements
- `Evidence_<company>.md` — the selected achievements and graph tags for review

Add `--docx` to ask your existing Career Bank renderer for an editable DOCX. This requires `python-docx` in the Python environment that runs `career_cli.py`.

Career mode does not create accounts, enter credentials, submit an application, or modify the bank or graph. Review the evidence map and generated resume before proceeding with any application.

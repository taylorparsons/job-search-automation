# AI-Assisted Setup

Prefer to be walked through setup by an AI assistant instead of editing files? Copy the prompt below into an AI assistant that can read and write files in this folder (for example a Cowork-style session), and answer its questions one at a time.

---

## Paste this prompt

> You are helping me set up the Reverse-Recruiter Job Search System in this folder. Do it conversationally — ask me one question at a time, then generate the local-only files. Do not submit applications, create accounts, or enter credentials. Steps:
>
> 1. Ask me for: my full name, email, phone (optional), LinkedIn URL, location preference, compensation floor, weekly application target, and weekly outreach target. Suggest 6-8 quality applications and 5 outreach actions per week.
> 2. Present these starting target-position tracks and ask me to confirm, remove, rename, or reprioritize each one:
>    - **Primary:** Senior or Principal Product Manager, Program Manager, or Technical Program Manager — AI platform, applied AI, generative AI, RAG, agent, and AI-enabled workflow roles.
>    - **Secondary:** Senior or Principal Product Manager, Program Manager, or Technical Program Manager — internal tools, support operations, self-service, and workflow-automation roles.
>    - **Selective:** Senior or Principal Product Manager, Program Manager, or Technical Program Manager — platform, marketplace operations, fulfillment, returns, and product reliability roles.
>    - **Engineering-management extension:** Software Engineering Manager, Engineering Manager, or Software Development Manager roles when the scope centers on technical delivery, platform or operational outcomes, cross-functional execution, and team leadership.
>    - **Optional stretch:** Product Lead, Group Product Manager, Director of Product, or Head of Product roles when the scope is hands-on product leadership rather than people management alone.
> 3. Explain that title is not enough: keep Program Manager roles when they own product-like strategy, prioritization, roadmap, customer or operational outcomes, and cross-functional delivery. Keep software-management roles when their scope matches the engineering-management extension; flag pure people-management or hands-on coding roles for review rather than assuming they are a fit.
> 4. From `config/config.example.json`, create `config/config.json` with the operator details and confirmed tracks. Do not include the `_comment` fields. Update `search.target_role_types`, `criteria.tracks`, `criteria.intersection`, `criteria.mission_signals`, `criteria.comp_floor`, `criteria.location_ok`, and `criteria.level_words`. Ensure the level list includes Senior PM, Principal PM, Program Manager, Technical Program Manager, Engineering Manager, Software Engineering Manager, and Software Development Manager language; do not leave the default director-only filter in place.
> 5. Copy `fit/skills.example.json` to `fit/skills.json`. Ask for the local path to my career bank (if available), then use only verified bank evidence to create an inventory of relevant skills. Favor AI product leadership, AI-enabled workflow design, internal knowledge/RAG copilots, internal and operational tooling, marketplace/returns, reliability, agent workflows, program delivery, and engineering leadership. Do not invent tools, metrics, titles, or ownership. Do not describe me as having led GenAI governance; the accurate framing is enterprise GPT-4 access, partnership with the GenAI governance team, and an internal-knowledge RAG copilot.
> 6. Copy `scout/scout_targets.example.json` to `scout/scout_targets.json`. Ask for target companies and careers URLs, then organize them by high, medium, or watch priority. Also copy `scout/scout_boards.example.json` to `scout/scout_boards.json` and ask for job boards, communities, and recruiter sources to monitor. These are local inventories, not permission to auto-apply.
> 7. Ask me for my current roles — for each: company, role title, stage (Sourced, Applying, Applied, Screening, Interview, Offer, Closed), source, and any job-description path. Keep the fit rating as a review field, not an unsupported claim.
> 8. Create `cockpit/Job_Search_Cockpit.local.html` by copying the shipped cockpit. Add that local filename to `.git/info/exclude`, then update only the local copy's `SEED` cards, recruiter list, network list, `updated`, and `updatedAt` values. Never place my personal pipeline data into the tracked `cockpit/Job_Search_Cockpit.html` source file.
> 9. For every promising role, ask me to save the job description locally and create a role JSON file. Use the Career Bank bridge to produce a resume Markdown file, an evidence map, and (when requested) a DOCX. Require me to review the evidence map and resume before any application action.
> 10. Show me a summary of the confirmed target tracks, configured local files, any unresolved company verdicts, and the first actions in the cockpit.
>
> Ask me the first question now.

---

## Notes

- The assistant only edits your local copies. Nothing is sent anywhere.
- `config/config.json`, `fit/skills.json`, and the scout inventories are gitignored. The shipped cockpit HTML is tracked, so use the `.local.html` copy for personal pipeline data.
- `bash setup.sh` only captures basic profile and weekly-target information. Use this prompt when you also want tailored role tracks, evidence inventory, source lists, and a private cockpit board.

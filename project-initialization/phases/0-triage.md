# Phase 0: Triage

## Purpose

Produce the plan file that all subsequent phase commands rely on. Write the Phase Roadmap, Artifact Roadmap, and initial Project Facts. Do not produce any canonical documentation.

## Precheck

If `docs/superpowers/plans/*-project-initialization.md` already exists, stop: "An initialization plan already exists. Run `/init` to continue, revisit a completed item, or delete the plan file and re-run `/init` to start over."

## Step 1 — Routing questions

Ask these five questions in order. Do not skip any.

1. **Project type** (pick one): product, internal tool, library/utility, platform/regulated, other (describe).
2. **AI involvement** (pick one): none — no AI features in the product itself; consumer — calls third-party AI APIs; core — AI model behavior is central to the product.
3. **Regulatory posture** (pick one): none — standard software product; light — general data privacy (GDPR, CCPA); heavy — industry-specific regulation (HIPAA, PCI, financial services, government).
4. **Team shape** (pick one): solo, small team (2-5 people), multi-team.
5. **Existing description** (free text, optional): "If you have anything written about this project — a README draft, a requirements doc, an email thread, a design note — paste it here. The more you share, the fewer questions I'll need to ask in later phases. Or leave blank."

## Step 2 — Profile selection

Map type + posture to profile:

| Project type | Regulatory posture | Profile |
| --- | --- | --- |
| product | any | product |
| internal tool | none or light | internal-tool |
| internal tool | heavy | platform |
| library/utility | none or light | library |
| library/utility | heavy | platform |
| platform/regulated | any | platform |
| other | none or light | internal-tool (note the edge case) |
| other | heavy | platform |

Read the chosen profile from `project-initialization/profiles/<profile>.md`.

## Step 3 — Fact extraction

If the user pasted a project description, run an extraction pass:
- Pull project name, one-line summary, primary users, deployment hints, stack hints, integration hints into `Project Facts`.
- Pull architecture or stack details into `Future-Phase Facts / Phase 3 — solution-design`.
- Pull governance or compliance mentions into `Future-Phase Facts / Phase 4 — security-baseline` or `Phase 4 — ai-use-policy`.
- Pull testing mentions into `Future-Phase Facts / Phase 4 — test-strategy`.
- Ignore content that does not fit any artifact.

## Step 4 — Artifact Roadmap construction

Start from the profile's artifact defaults. Apply rule-based prunes:

- AI involvement = none → skip `ai-use-policy` regardless of profile.
- Regulatory posture = none → skip `security-baseline` and `delivery-plan` if profile = library.
- Team shape = solo → skip `delivery-plan` unless profile = product or platform.
- Any artifact for which all required content was extracted → set initial mode to `confirm` or `extract` per these rules:
  - `extract`: sufficient facts captured to draft the artifact without questions.
  - `confirm`: partial facts; command will show extracted content and ask targeted gap questions.
  - `interview`: no usable facts; full question flow.

Show the proposed Artifact Roadmap to the user with one-line mode reasoning per artifact. Example: "PRD is `confirm` because the pasted description gave us users and goals but not scope boundaries."

Ask: "Any artifact you want to activate, deactivate, or change the mode for?" Apply changes and record them under `Overrides applied` in the plan.

## Step 5 — Write the plan file

Initialize `docs/superpowers/plans/YYYY-MM-DD-project-initialization.md` from `project-initialization/plan-template.md`. Populate:
- `Goal` — one sentence from project name and summary.
- `Profile` — selected profile and rationale.
- `Phase Roadmap` — all phases as `pending` (Phase 0 = `done`).
- `Artifact Roadmap` — all rows with initial and effective mode (same at this point), status `pending` or `skipped`, and `Last Revisited` blank.
- `Project Facts` — everything extracted in Step 3.
- `Future-Phase Facts` — sub-sections for any future-phase facts extracted in Step 3.

## Output

```text
Stage Completed: Phase 0 — Triage
Docs Updated: docs/superpowers/plans/YYYY-MM-DD-project-initialization.md
Review Fixes Applied: none
Concerns And Recommendations: <list or "none">
Parked Questions: <list or "none">
Next Recommended Step: Run `/init` to continue to Phase 1 (Intent).
```

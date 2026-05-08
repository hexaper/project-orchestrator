---
description: "Run the consolidated project initialization workflow — start triage, resume the next phase, or revisit a completed phase or artifact."
---

You are running the consolidated `/init` workflow for this repository.

## Argument handling

- No argument: inspect `docs/superpowers/plans/*-project-initialization.md`.
  - If no plan exists, announce `No initialization plan found — running Phase 0 (Triage).` and follow `project-initialization/phases/0-triage.md` exactly.
  - If a plan exists and at least one phase is not `done`, render the status block below, then wait for `[Enter] continue · revisit · show plan · q`.
  - If all phases are `done`, print `Project initialization is complete.` and offer the revisit menu.
- One argument: resolve it against phase names (`triage`, `intent`, `spec`, `design`, `govern`, `adapt`, `review`) and artifact names from `project-initialization/artifacts/`. A phase argument runs the corresponding phase rubric; an artifact argument runs only that artifact in revisit mode.
- Unknown argument: print the supported phase names plus the artifact catalog and stop.

## Status block template

Render this format from the plan's Phase Roadmap:

```text
Project initialization — <plan date>
  ✓ Phase 0  Triage          done  <date or blank>
  ✓ Phase 1  Intent          done  <date or blank>
  ▶ Phase 2  Specification   next
    Phase 3  Design
    Phase 4  Govern & Operate
    Phase 5  Adapt
    Phase 6  Final review

Next action: run Phase <N> — <Phase Name> (<artifacts summary>).

[Enter] continue · revisit · show plan · q
```

## Revisit menu template

If the user chooses `revisit`, render completed phases and their artifacts in a flat menu:

```text
Revisit a completed item:
  1. Phase 0 — Triage (whole phase)
  2. Phase 1 — Intent (whole phase)
     a. project-brief        last revisited: never
     b. business-case        last revisited: 2026-05-06
Enter number (e.g. 2a) or q to cancel:
```

Selecting a whole phase runs that phase rubric in revisit mode. Selecting an artifact runs only that artifact's rubric in append/extend mode and updates `Last Revisited` in the Artifact Roadmap when the artifact run completes.

## Routing rules

- Always treat `project-initialization/plan-template.md` and the active plan file as the only state source.
- Always follow `project-initialization/contract.md` for per-run stop rules.
- Always route into `project-initialization/phases/<N>-*.md` for full-phase work.
- Always route into `project-initialization/artifacts/<name>.md` for artifact-only revisits.
- Never duplicate phase interview logic in this wrapper.
- If the existing plan lacks the `Last Revisited` column, treat it as blank for every artifact.

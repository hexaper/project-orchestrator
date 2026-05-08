---
title: Project Initialization
status: active
record_class: supporting
audience: [internal]
owner: Template maintainers
capability: knowledge
phase: n/a
cadence: ad-hoc
last_reviewed: 2026-05-08
---

# Project Initialization

> **Purpose**: serve as the entrypoint and contract summary for the tool-neutral project initialization workflow.
> **Audience**: contributors maintaining the initialization workflow; AI agents reading phase content.
> **When to update**: update when the phase catalog, artifact list, or shared contract rules change.

## How initialization works

A fresh clone of this template is unspecialized. To initialize it for a specific project, run `/init` in your AI tool's command surface.

Tool-specific `/init` wrappers live outside this directory. This directory remains tool-neutral and defines the shared workflow contract they must all follow.

The command reads `docs/superpowers/plans/YYYY-MM-DD-project-initialization.md` as its sole source of truth.

- If no plan exists, `/init` starts Phase 0 (Triage).
- If a plan exists and phases remain incomplete, `/init` shows the current roadmap, names the next phase, and lets the user continue, revisit completed work, or show the plan.
- If all phases are complete, `/init` reports completion and offers revisit options.
- Power users can jump directly with `/init <phase-or-artifact-name>`.

## Phases

| Phase | Routed by `/init` to | Purpose |
| --- | --- | --- |
| 0. Triage | `project-initialization/phases/0-triage.md` | Routing questions, profile selection, artifact roadmap |
| 1. Intent | `project-initialization/phases/1-intent.md` | Project brief, optional business case |
| 2. Specification | `project-initialization/phases/2-specification.md` | PRD, requirements catalog, user journeys, acceptance catalog |
| 3. Design | `project-initialization/phases/3-design.md` | Solution design, ADRs, optional C4 views |
| 4. Govern & Operate | `project-initialization/phases/4-govern-operate.md` | AI policy, test strategy, security baseline, delivery plan |
| 5. Adapt | `project-initialization/phases/5-adapt.md` | Language adaptation, repository sync |
| 6. Final review | `project-initialization/phases/6-review.md` | Cross-doc coherence, entry-doc parity, standards pass |

### Status and revisit behavior

`/init` without arguments renders a status block derived from the plan file, then offers:

```text
[Enter] continue · revisit · show plan · q
```

- `continue` runs the next incomplete phase.
- `revisit` opens the completed-phase and artifact menu.
- `show plan` prints the plan path plus the roadmap and resume sections.
- `q` exits without changes.

Revisiting a completed artifact updates `Last Revisited` in the Artifact Roadmap but keeps both artifact and phase status as `done`.

### SessionStart visibility

Each tool's SessionStart hook checks for an in-progress project initialization plan on session open.

- No plan file: hook stays silent.
- In-progress plan: hook prints the status block and `Run /init to continue.`
- All phases done: hook stays silent.

## This directory

| Path | Responsibility |
| --- | --- |
| `contract.md` | Stop rules, concern framing, output format — all commands follow this |
| `plan-template.md` | Scaffold for the plan file created by triage |
| `review-checklist.md` | Standards + coherence rubric used by `init-reviewer` |
| `phases/` | Per-phase orchestration files |
| `artifacts/` | Per-artifact question rubrics, gating criteria, review hooks |
| `profiles/` | Default artifact activations per project type |

# Artifact Rubric: Delivery Plan

- Phase: 4 (Govern & Operate)
- Output path: `docs/07_delivery/01_delivery_plan.md`
- Template: `docs/07_delivery/` (use first TEMPLATE file found)
- Prerequisites: prd, solution-design

## Gating criteria

The delivery plan is complete when:
- At least two phases or milestones are defined.
- Each milestone has a measurable success criterion.
- Team responsibilities are stated (who owns what).
- Dependencies between milestones are noted.

## Interview mode

1. "How do you plan to deliver this: iterative sprints, phased releases, big-bang, or another approach?"
2. "What are the key milestones? For each: what does 'done' mean?"
3. "Who owns each delivery area? Name teams or roles, not individuals."
4. "What are the critical dependencies — things that must happen before a milestone can start?"

## Confirm mode

Present scope and timeline hints from PRD and Future-Phase Facts. Ask for milestone structure and ownership.

## Extract mode

Fill the delivery plan template from captured facts. Add `[NEEDS-REVIEW: describe what is missing]` for any required section lacking source material. Files with `[NEEDS-REVIEW]` markers do not pass the phase gate — resolve every marker before marking the artifact complete.

## Review hooks

- Milestone success criteria are measurable — not "the feature is complete" but a named, verifiable outcome.
- All PRD MUST requirements are covered by at least one milestone.
- Dependencies are stated directionally (A before B), not implied.
- Output path `docs/07_delivery/01_delivery_plan.md` exists and is the file that was written.
- Frontmatter complete per schema (`docs/00_operating_model/04_frontmatter_schema.md`).

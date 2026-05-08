# Artifact Rubric: User Journeys

- Phase: 2 (Specification)
- Output path: `docs/02_product/03_user_journeys.md`
- Template: `docs/02_product/03_user_journeys_TEMPLATE.md`
- Prerequisites: prd

## Gating criteria

The user journeys artifact is complete when:
- At least one complete journey exists per primary user type named in the PRD.
- Each journey has a defined start point, at least three steps (a step = one atomic action by one actor with one observable result), and a success outcome.
- Each step names actor, action, and result.
- No step contains implementation detail (no UI element names, API calls, or database terms).

## Interview mode

1. "Who are the distinct user types performing meaningful actions? List them."
2. "For [primary user type]: walk me through the most important thing they do in this system, from start to success."
3. "Where does that journey break down today? What is the failure mode we are trying to eliminate?"
4. "Are there secondary journeys — less frequent but important — for the same user type?"

Repeat questions 2-4 for each user type.

## Confirm mode

Present extracted user types and any journey fragments from Future-Phase Facts. For each step presented, confirm it has the form: Actor → Action → Observable result. Ask for missing steps, user types, or missing result statements.

## Extract mode

Build journeys from PRD user descriptions and any source material provided. Mark incomplete journeys with `[NEEDS-REVIEW: missing steps]`. Flag any step containing implementation detail (UI element names, API names, database terms) with `[NEEDS-REVIEW: remove implementation detail]`. Files with `[NEEDS-REVIEW]` markers do not pass the phase gate — resolve every marker before marking the artifact complete.

## Review hooks

- Actor names in journeys match the PRD's user descriptions.
- No implementation detail: no UI component names, no API endpoint names, no database terms.
- Each journey ends with a named success outcome, not an open-ended state.
- Output path `docs/02_product/03_user_journeys.md` exists and is the file that was written.
- Frontmatter complete per schema (`docs/00_operating_model/04_frontmatter_schema.md`).

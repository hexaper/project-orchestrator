# Artifact Rubric: PRD

- Phase: 2 (Specification)
- Output path: `docs/02_product/01_prd.md`
- Template: `docs/02_product/01_prd_TEMPLATE.md`
- Prerequisites: project-brief

## Gating criteria

The PRD is complete when:
- Problem statement and target users are named and non-generic.
- Scope section has an explicit out-of-scope list with at least three items.
- At least one measurable success metric is defined.
- No `[TBD]` markers remain in required sections.

## Interview mode

1. "The brief names [problem] and [users]. Does the PRD scope match exactly? If there are differences — different problem framing, expanded users, or narrowed scope — state them explicitly so the PRD is self-contained."
2. "What is explicitly out of scope for the first release? List at least three things we are not building."
3. "What does success look like in three to six months? Name at least one outcome you could measure."
4. "Are there competing or related products the PRD should acknowledge for differentiation?"
5. "Are there release constraints — regulatory approval, partner dependencies, platform certification — that define hard deadlines?"

## Confirm mode

Present extracted problem, users, scope hints, and metrics. Ask only for what is missing per the gating criteria.

## Extract mode

Fill `docs/02_product/01_prd_TEMPLATE.md` from `Project Facts` and Future-Phase Facts tagged for this artifact. Add `[NEEDS-REVIEW: ...]` where content is absent. Files with `[NEEDS-REVIEW]` markers do not pass the phase gate — present the draft and resolve every marker before marking the artifact complete.

## Review hooks

- Problem statement matches the brief's problem — no scope creep introduced in the PRD.
- Out-of-scope list exists and is not empty.
- Success metrics are measurable: not "improve UX" but "reduce time-to-first-action by 30%".
- Target users in PRD match the brief's user description, or any differences are intentional and explained in the PRD scope section.
- Output path `docs/02_product/01_prd.md` exists and is the file that was written.
- Frontmatter complete per schema (`docs/00_operating_model/04_frontmatter_schema.md`).

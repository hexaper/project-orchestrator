# Artifact Rubric: Requirements Catalog

- Phase: 2 (Specification)
- Output path: `docs/02_product/02_requirements_catalog.md`
- Template: `docs/02_product/02_requirements_catalog_TEMPLATE.md`
- Prerequisites: prd

## Gating criteria

The requirements catalog is complete when:
- At least five functional requirements are listed.
- Each requirement has a priority: MUST, SHOULD, COULD, or WON'T.
- No requirement restates a PRD out-of-scope item as a positive requirement (scope inversion).
- No requirement contains implementation detail (how, not what).

## Interview mode

1. "List the functional things the system must do — start with MUST requirements, then SHOULD."
2. "Review the requirements you just listed: does any of them describe *how* the system should work rather than *what* it should do? Implementation detail should be moved to ADRs, not requirements."
3. "For each MUST requirement: what would you observe if it were NOT met? These failure descriptions will define acceptance criteria — confirm they are observable, not subjective."
4. "Are there non-functional requirements (performance, availability, data retention) the architecture must respect?"
5. "What requirements did you consider and explicitly decide not to include in this release?"

## Confirm mode

Show extracted requirements from PRD and Future-Phase Facts. Ask the user to confirm priority and completeness.

## Extract mode

Pull requirements from PRD scope section and Future-Phase Facts. Structure into the catalog template. Flag any requirement that is vague enough to be unverifiable with `[NEEDS-REVIEW: make testable]`. Files with `[NEEDS-REVIEW]` markers do not pass the phase gate — resolve every marker before marking the artifact complete.

## Review hooks

- Each requirement is testable: a person reading it can say "this is met" or "this is not met" unambiguously.
- No requirement says "should be easy to use" or similar subjective statements.
- Priority labels are present on every row.
- Output path `docs/02_product/02_requirements_catalog.md` exists and is the file that was written.
- Frontmatter complete per schema (`docs/00_operating_model/04_frontmatter_schema.md`).

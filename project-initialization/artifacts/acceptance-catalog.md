# Artifact Rubric: Acceptance Catalog

- Phase: 2 (Specification)
- Output path: `docs/02_product/05_acceptance_catalog.md`
- Template: `docs/02_product/05_acceptance_catalog_TEMPLATE.md`
- Prerequisites: prd, requirements-catalog (if active)

## Gating criteria

The acceptance catalog is complete when:
- Every MUST requirement from the requirements catalog (or the PRD scope if requirements-catalog was skipped) has at least one acceptance criterion.
- Each criterion is binary: it is either met or not.
- No criterion requires subjective judgment to evaluate.
- No criterion restates a PRD out-of-scope item as a verifiable gate (out-of-scope items cannot be accepted, only excluded).

## Interview mode

Work through MUST requirements one at a time. For each:
1. "How would you verify that [requirement] is satisfied? Describe a specific test or observable outcome."
2. "What would you see if this requirement is NOT met? Name the observable failure."

Repeat for every MUST requirement before moving to SHOULD requirements.

## Confirm mode

Present requirements and ask the user to confirm or add acceptance criteria for each.

## Extract mode

Derive criteria from requirements and any source material. Flag ambiguous criteria with `[NEEDS-REVIEW: not binary — rephrase as pass/fail]`. Files with `[NEEDS-REVIEW]` markers do not pass the phase gate — resolve every marker before marking the artifact complete.

## Review hooks

- Every MUST requirement has at least one criterion.
- Criteria are binary: no "should feel fast" or "should look clean".
- Criteria do not duplicate the PRD's out-of-scope list (anti-requirements are not acceptance criteria).
- Output path `docs/02_product/05_acceptance_catalog.md` exists and is the file that was written.
- Frontmatter complete per schema (`docs/00_operating_model/04_frontmatter_schema.md`).

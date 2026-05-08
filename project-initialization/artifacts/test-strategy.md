# Artifact Rubric: Test Strategy

- Phase: 4 (Govern & Operate)
- Output path: `docs/05_testing_acceptance/01_test_strategy.md`
- Template: `docs/05_testing_acceptance/` (use first TEMPLATE file found)
- Prerequisites: solution-design, requirements-catalog (if active)

## Gating criteria

The test strategy is complete when:
- Testing levels are defined per component type (unit, integration, E2E, contract, performance as applicable).
- Automated vs. manual split is stated.
- At least one quality gate for CI/CD is named.
- Coverage expectation is stated (even if directional, e.g., "unit coverage for all business logic").

## Interview mode

1. "What types of testing are most important for this project: unit, integration, end-to-end, contract, performance, security?"
2. "Which tests will be automated and run in CI? Which will remain manual?"
3. "What are the quality gates — what must pass before a PR merges? Before a release?"
4. "Are there components where testing is difficult or expensive? How will you handle them?"

## Confirm mode

Present testing approach facts captured from solution design and Future-Phase Facts. Ask only for missing gating criteria.

## Extract mode

Fill the test strategy template from captured facts. Add `[NEEDS-REVIEW: describe what is missing]` for any required section lacking source material. Files with `[NEEDS-REVIEW]` markers do not pass the phase gate — resolve every marker before marking the artifact complete.

## Review hooks

- Testing levels named in the strategy match the component types in the solution design.
- At least one CI gate is named.
- Manual test scope is explicitly bounded — not "everything not automated".
- Output path `docs/05_testing_acceptance/01_test_strategy.md` exists and is the file that was written.
- Frontmatter complete per schema (`docs/00_operating_model/04_frontmatter_schema.md`).

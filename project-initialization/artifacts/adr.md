# Artifact Rubric: ADR

- Phase: 3 (Design) — created on demand as decisions arise
- Output path: `docs/adr/ADR-NNN-<decision-slug>.md`
- Template: `docs/adr/ADR-000-template.md`
- Prerequisites: none (created as decisions are made)

## When to create an ADR

Create an ADR whenever a durable decision is made during Design (or any phase) that:
- Cannot easily be reversed once implemented.
- Affects how the codebase or system is structured.
- Would surprise a future contributor if it were changed without explanation.

Common triggers: language choice, framework choice, data store choice, deployment model, auth model, security posture, external service commitment.

## Gating criteria

An ADR is complete when:
- Status is `accepted` or `proposed` (never blank).
- Exactly one decision outcome is stated.
- At least two options were considered.
- Consequences (positive and negative) are listed.

## Interview mode

For each decision identified during the Design phase:
1. "What is the decision in one sentence?"
2. "What options did you consider? List at least two."
3. "What drove the choice — constraint, preference, evidence, or prior art?"
4. "What does this decision cost or risk?"

## ADR index update

After writing each ADR, add a row to `docs/adr/INDEX.md`. Format:

```text
| [ADR-NNN](ADR-NNN-slug.md) | Short title | Accepted | YYYY-MM-DD | One-line summary. |
```

## Review hooks

- ADR slug matches the decision (not generic like "ADR-001-tech-choice").
- Status is explicitly set to `accepted` or `proposed`.
- Exactly one decision outcome in the "Decision outcome" section.
- `docs/adr/INDEX.md` row is present.
- Output path `docs/adr/ADR-NNN-<decision-slug>.md` exists and is the file that was written.
- Frontmatter complete per schema (`docs/00_operating_model/04_frontmatter_schema.md`).

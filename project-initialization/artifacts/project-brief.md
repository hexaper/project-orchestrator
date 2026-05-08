# Artifact Rubric: Project Brief

- Phase: 1 (Intent)
- Output path: `docs/00_governance/00_project_brief.md`
- Template: `docs/00_governance/00_project_brief_TEMPLATE.md`
- Prerequisites: none (first artifact)

## Gating criteria

The project brief is complete when:
- Project name is present and not a placeholder.
- Problem statement is specific: names the problem, not the solution.
- Target users are identified: a qualified description, not "users" or "developers".
- A one-line project summary exists (usable as the `Goal` in the plan file).
- No `[TBD: ...]` markers remain in the executive summary, problem statement, or any scope section (what is in scope, what is out of scope).

## Interview mode

Ask in order. Stop when gating criteria are met.

1. "What is the name of this project?"
2. "In one or two sentences: what problem does this project solve, and why does it matter to the people experiencing it?"
3. "Who are the primary users or beneficiaries? Describe them specifically — not 'users' but a qualified group."
4. "What do those people do today, without this project? What makes that inadequate?"
5. "Are there hard constraints — timeline, budget, regulatory, integration, or technical — you must acknowledge upfront?"

If any answer is a placeholder ("TBD", "not sure yet"), ask a follow-up: "What's your best current hypothesis for [that item]? We can capture it as provisional, but we'll need to confirm it before this phase closes."

## Confirm mode

Present to the user:

```text
From what you've shared, here's the draft project brief context:
- Name: [extracted]
- Problem: [extracted]
- Users: [extracted]
- Constraints: [extracted or "none captured yet"]

Anything wrong or missing?
```

Then ask only the questions whose gating criteria are not met.

## Extract mode

Fill `docs/00_governance/00_project_brief_TEMPLATE.md` using `Project Facts` and the current phase's `Future-Phase Facts` sub-section. Where required sections lack captured content, add `[NEEDS-REVIEW: describe what is missing]` so the user can spot gaps at review time. Files with `[NEEDS-REVIEW]` markers do not pass the phase gate — present them to the user and resolve every marker before marking the artifact complete.

## Review hooks

Pass to `init-reviewer`:
- Problem statement names a real problem, not a solution or a category ("build an API" is a solution; "teams cannot track X without manual effort" is a problem).
- Target users are specific enough to derive requirements from (not "developers" or "the business").
- No `[TBD]` or `[NEEDS-REVIEW]` remains in the executive summary, problem statement, or primary users sections.
- Frontmatter is complete per `docs/00_operating_model/04_frontmatter_schema.md`.
- Output path `docs/00_governance/00_project_brief.md` exists and is the file that was written.
- No `[TBD]` or `[NEEDS-REVIEW]` remains in any scope section of the brief.

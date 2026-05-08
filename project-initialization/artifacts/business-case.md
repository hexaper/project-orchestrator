# Artifact Rubric: Business Case

- Phase: 1 (Intent)
- Output path: `docs/00_governance/01_business_case.md`
- Template: `docs/00_governance/01_business_case_TEMPLATE.md`
- Prerequisites: project-brief (must be done)

## Gating criteria

The business case is complete when:
- Executive summary exists and is specific to this project (not generic: "improve efficiency", "enable better collaboration"; specific: "reduce manual reporting time for X by eliminating Y" or "enable Z team to deploy independently without coordinating with W").
- Primary benefit or value driver is named and at least directionally quantified or described.
- Strategic fit is stated (why this project, why now).
- Key investment or cost acknowledgment is present (even if approximate).

## Interview mode

Ask in order:
1. "Who commissioned or is sponsoring this project, and what outcome are they accountable for?"
2. "What is the primary benefit — describe it in terms of time saved, risk reduced, revenue enabled, or cost avoided. Even a rough estimate is useful."
3. "Why is this the right time to build this? What has changed that makes this possible or urgent?"
4. "What is the rough investment expected — team size, duration, or budget range? Approximate is fine."

## Confirm mode

Present to the user:

```text
From what you've shared, here's the draft business case context:
- Sponsor: [extracted]
- Primary benefit: [extracted]
- Why now: [extracted]
- Investment: [extracted or "not captured yet"]

Anything wrong or missing?
```

Then ask only the questions whose gating criteria are not met.

## Extract mode

Fill `docs/00_governance/01_business_case_TEMPLATE.md` from captured facts. Add `[NEEDS-REVIEW: describe what is missing]` for any required section lacking source material. Files with `[NEEDS-REVIEW]` markers do not pass the phase gate — resolve every marker before marking the artifact complete.

## Review hooks

- Benefit is directionally quantified: a direction and magnitude, not "improve efficiency" or "reduce overhead".
- Strategic fit names the organizational context, not just the project.
- Frontmatter complete per schema.
- Output path `docs/00_governance/01_business_case.md` exists and is the file that was written.
- Schema ref: `docs/00_operating_model/04_frontmatter_schema.md`.

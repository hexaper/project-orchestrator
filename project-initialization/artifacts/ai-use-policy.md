# Artifact Rubric: AI Use Policy

- Phase: 4 (Govern & Operate)
- Output path: `docs/04_ai_governance/01_ai_use_policy.md`
- Template: `docs/04_ai_governance/` (use first TEMPLATE file found)
- Prerequisites: solution-design

## Gating criteria

The AI use policy is complete when:
- Allowed AI use cases are listed (at minimum: which AI capabilities are used).
- Prohibited uses or limitations are stated.
- Human-in-the-loop requirements are described for any AI-driven decisions.
- Data handling: which user data, if any, is sent to external AI providers.

## Interview mode

1. "Which AI capabilities does this project use — generation, classification, retrieval, or other?"
2. "What data is sent to AI providers? Does it include PII, business-sensitive, or regulated data?"
3. "For AI-driven decisions: which decisions require human review or approval before acting?"
4. "What uses of AI are explicitly prohibited in this project (to prevent misuse or scope creep)?"

## Confirm mode

Present extracted AI involvement facts from triage and Future-Phase Facts. Ask only for policy gaps.

## Extract mode

Fill the AI use policy template from captured facts. Add `[NEEDS-REVIEW: describe what is missing]` for any required section lacking source material. Files with `[NEEDS-REVIEW]` markers do not pass the phase gate — resolve every marker before marking the artifact complete.

## Review hooks

- Data handling statement covers PII and regulated data — not silent on what is sent externally.
- Prohibited use list exists and is non-empty.
- Human-in-the-loop requirements are named for any decision affecting users.
- Policy aligns with regulatory posture selected at triage.
- Output path `docs/04_ai_governance/01_ai_use_policy.md` exists and is the file that was written.
- Frontmatter complete per schema (`docs/00_operating_model/04_frontmatter_schema.md`).

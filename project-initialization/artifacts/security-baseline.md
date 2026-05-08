# Artifact Rubric: Security Baseline

- Phase: 4 (Govern & Operate)
- Output path: `docs/06_security_operations/01_security_baseline.md`
- Template: `docs/06_security_operations/` (use first TEMPLATE file found)
- Prerequisites: solution-design

## Gating criteria

The security baseline is complete when:
- Threat surface is identified (what attack vectors are in scope).
- At least three controls are named.
- Data classification is stated (what data is processed and its sensitivity level).
- Incident response owner is named.

## Interview mode

1. "Who are the likely threat actors — external attackers, internal misuse, supply chain?"
2. "What data does this system process? Classify: public, internal, confidential, regulated."
3. "What are the three most important security controls for this system?"
4. "Who is responsible for security incidents — is there an on-call rotation, a security team, or a named owner?"

## Confirm mode

Present data handling and regulatory posture facts from triage and captured tech stack. Ask for controls and ownership.

## Extract mode

Fill the security baseline template from captured facts. Add `[NEEDS-REVIEW: describe what is missing]` for any required section lacking source material. Files with `[NEEDS-REVIEW]` markers do not pass the phase gate — resolve every marker before marking the artifact complete.

## Review hooks

- Controls are specific enough to verify (not "follow OWASP" but "input validation on all user-submitted fields").
- Data classification aligns with regulatory posture selected at triage.
- Incident response owner is a role or team, not anonymous.
- Output path `docs/06_security_operations/01_security_baseline.md` exists and is the file that was written.
- Frontmatter complete per schema (`docs/00_operating_model/04_frontmatter_schema.md`).

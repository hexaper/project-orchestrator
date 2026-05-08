# Phase 4: Govern & Operate

## Purpose

Make operational, quality, and risk decisions traceable. Produce the active govern & operate artifacts per the profile.

## Artifact walk order

1. `ai-use-policy` (if active)
2. `test-strategy`
3. `security-baseline` (if active)
4. `delivery-plan` (if active)

For each, load `project-initialization/artifacts/<name>.md` and follow the mode assigned in the plan.

## Phase-specific guidance

- Check Future-Phase Facts for this phase first. Facts from Specification (data classification, compliance requirements) and Design (deployment target, tech stack) are often pre-populated here.
- If the user says "we don't need a test strategy," raise a concern (five-part frame). Test strategy is always active in non-library profiles.
- If security baseline is skipped but regulatory posture is light or heavy, raise a concern.

## Future-phase fact scope

Route to:
- Stack-specific test tooling choices → `Future-Phase Facts / Phase 5 — language-adaptation`
- Deployment and infra specifics → `Future-Phase Facts / Phase 5 — language-adaptation`

## End-of-phase review

Dispatch `init-reviewer` with all govern & operate artifacts produced and phase number 4.

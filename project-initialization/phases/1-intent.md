# Phase 1: Intent

## Purpose

Produce the project brief and, if activated, the business case. Establish the "why" before moving to specifications.

## Artifact walk order

1. `project-brief` (always active)
2. `business-case` (if active in Artifact Roadmap)

For each, load `project-initialization/artifacts/<name>.md` and follow the mode assigned in the plan.

## Phase-specific guidance

- Do not discuss technical stack, architecture, or implementation in this phase. If the user raises them, capture as Future-Phase Facts for Phase 3 and redirect: "That's a great design decision — I've noted it for Phase 3 (Design). For now, let's focus on the problem and who it's for."
- After producing the project brief, update `Project Facts` with confirmed project name and one-line summary before moving to the business case.

## Future-phase fact scope

Route captured statements to:
- Specification hints (requirements, scope, user needs) → `Future-Phase Facts / Phase 2 — prd`
- Stack, architecture, deployment → `Future-Phase Facts / Phase 3 — solution-design`
- Compliance, security, AI use → `Future-Phase Facts / Phase 4` (appropriate artifact)
- Testing approach → `Future-Phase Facts / Phase 4 — test-strategy`

## End-of-phase review

Dispatch `init-reviewer` with:
- Files produced: `docs/00_governance/00_project_brief.md` and `docs/00_governance/01_business_case.md` (if produced)
- Phase number: 1
- Checklist: `project-initialization/review-checklist.md`

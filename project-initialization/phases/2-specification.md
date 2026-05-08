# Phase 2: Specification

## Purpose

Produce the PRD and active specification artifacts. Define what the product does and for whom, verifiably.

## Prerequisite check

Before starting, read `docs/00_governance/00_project_brief.md`. If it has unresolved `[TBD]` or `[NEEDS-REVIEW]` markers in the problem statement, users, or one-line summary sections, stop and tell the user: "The project brief has unresolved gaps that will create ambiguity in the PRD. Resolve them first, or override to continue anyway."

## Artifact walk order

1. `prd` (always active)
2. `requirements-catalog` (if active)
3. `journeys` (if active)
4. `acceptance-catalog` (if active)

For each, load `project-initialization/artifacts/<name>.md` and follow the mode assigned in the plan.

## Phase-specific guidance

- Architecture choices that emerge here belong in Future-Phase Facts for Phase 3, not in the PRD itself.
- If the user describes a solution in answer to a requirements question, gently redirect: "That sounds like an architectural choice — I've noted it for Phase 3. In the requirements, let's describe what the system must do, not how."
- The PRD's out-of-scope list is load-bearing. If the user is reluctant to define it, raise a concern using the five-part frame.

## Future-phase fact scope

Route to:
- Architecture choices → `Future-Phase Facts / Phase 3 — solution-design`
- Security or compliance specifics → `Future-Phase Facts / Phase 4 — security-baseline`
- AI use specifics → `Future-Phase Facts / Phase 4 — ai-use-policy`
- Delivery timeline hints → `Future-Phase Facts / Phase 4 — delivery-plan`

## End-of-phase review

Dispatch `init-reviewer` with all specification files produced and phase number 2.

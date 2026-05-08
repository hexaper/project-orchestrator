# Phase 3: Design

## Purpose

Make durable technical decisions traceable and documented. Produce the solution design and ADRs for every durable decision.

## Artifact walk order

1. `solution-design`
2. `adr` (created on demand as decisions arise during solution-design — multiple ADRs may result)
3. `c4` (if active — run after solution-design is complete)

For each, load `project-initialization/artifacts/<name>.md` and follow the mode assigned in the plan.

## Phase-specific guidance

- Before running `solution-design` in interview mode, invoke `superpowers:brainstorming` to explore 2-3 architectural approaches. Present approaches with trade-offs and a recommendation. Wait for the user to choose before writing the solution design.
- Every time a durable decision is made during solution-design — language, framework, data store, auth model, deployment target, external service commitment — immediately create an ADR for it using `project-initialization/artifacts/adr.md`. Do not defer ADR creation to end-of-phase.
- Update `docs/adr/INDEX.md` after each ADR is written.
- Check Future-Phase Facts for this phase before starting. Any architecture, stack, or deployment facts captured in earlier phases should be acknowledged: "I see we noted [X] during Phase 1 — confirming this before including it in the solution design."

## Future-phase fact scope

Route to:
- Test approach from design decisions → `Future-Phase Facts / Phase 4 — test-strategy`
- Security implications of architectural choices → `Future-Phase Facts / Phase 4 — security-baseline`
- Deployment decisions relevant to language adaptation → `Future-Phase Facts / Phase 5 — language-adaptation`

## End-of-phase review

Dispatch `init-reviewer` with solution design, all ADRs produced, C4 files (if produced), updated `docs/adr/INDEX.md`, and phase number 3.

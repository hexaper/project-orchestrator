# Artifact Rubric: Solution Design

- Phase: 3 (Design)
- Output path: `docs/03_architecture/01_solution_design.md`
- Template: `docs/03_architecture/01_solution_design_TEMPLATE.md`
- Prerequisites: prd (and requirements-catalog if active)

## Gating criteria

The solution design is complete when:
- System shape is decided (monolith / services / hybrid) and an ADR exists for it.
- Primary data store is chosen and an ADR exists for it.
- Deployment target is chosen and an ADR exists for it.
- Non-functional requirements from the PRD are addressed (scale, latency, reliability).
- No `[TBD]` in core sections (context, constraints, solution strategy, building blocks).

## Interview mode

Before asking questions, invoke `superpowers:brainstorming` to explore 2-3 architectural approaches. Present the approaches with trade-offs and a recommendation before asking the user to decide.

After the user chooses an approach, ask:
1. "What language and primary framework will you use? If already decided by an ADR, confirm."
2. "What is your primary data store? Relational, document, or other — and which specific technology?"
3. "Where will this system run? Cloud provider and service type (container, serverless, VM, managed service)."
4. "What are the scale characteristics: expected concurrent users, request volume, data volume?"
5. "Are there integration constraints — existing systems, partner APIs, internal platforms this must connect to?"

## Confirm mode

Present extracted stack, deployment, and scale facts. Show which questions were pre-answered. Ask only for missing gating criteria.

## Extract mode

Build the solution design from all captured architecture facts. Mark undecided areas as `[NEEDS-REVIEW: decision required]` rather than silently choosing. Files with `[NEEDS-REVIEW]` markers do not pass the phase gate — resolve every marker before marking the artifact complete.

## Review hooks

- Every durable decision (language, framework, data store, deployment target, auth approach) has a corresponding ADR in `docs/adr/`.
- Non-functional requirements from the PRD are addressed — not ignored.
- No implementation code, version pins, or module names appear in the design (those belong in ADRs or implementation docs).
- Scale characteristics match what the PRD implies.
- Output path `docs/03_architecture/01_solution_design.md` exists and is the file that was written.
- Frontmatter complete per schema (`docs/00_operating_model/04_frontmatter_schema.md`).

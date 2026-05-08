---
title: ADR-006 Phase-Gate and Plan-Update Invariants
status: active
record_class: canonical
audience: [internal]
owner: architecture-maintainer
capability: architecture
phase: planning
cadence: per-stage
last_reviewed: 2026-05-08
---

# ADR-006: Enforce phase-gate blocking and one-batch plan updates as contract invariants

- Status: Accepted
- Date: 2026-05-08
- Deciders: Project Initiator
- Consulted: none
- Informed: future contributors and reviewers
- Tags: [Architecture, Operations, Delivery]
- Supersedes: None
- Superseded by: None
- Related documents: [../03_architecture/01_solution_design.md](../03_architecture/01_solution_design.md), [../superpowers/plans/2026-05-08-project-initialization.md](../superpowers/plans/2026-05-08-project-initialization.md), [../../project-initialization/contract.md](../../project-initialization/contract.md)

## Context and problem statement

The workflow already applies two durable operational rules: a phase cannot close while critical or important findings remain unresolved, and plan-state updates occur once at end-of-run in a single batch. These rules are cross-cutting and directly shape correctness, traceability, and resume behavior. Without an ADR, they remain implicit guidance and can drift across implementations.

## Decision drivers

- Deterministic and auditable phase closure behavior.
- Consistent resumability after interruptions.
- Reduced partial-state drift from incremental plan writes.
- Stable governance semantics across agent adapters.

## Considered options

### Option 1: ADR-backed invariants

- What it is: formalize both rules as binding architecture invariants.
- Pros: explicit authority, consistent implementation target, strong review traceability.
- Cons: less flexibility for ad-hoc workflow experimentation.

### Option 2: Keep as implementation guidance only

- What it is: document behavior in phase rubrics/contract without ADR authority.
- Pros: easier to iterate informally.
- Cons: higher drift risk and weaker cross-phase governance consistency.

## Decision outcome

Choose Option 1. The following are binding invariants for initialization workflow implementations:

1. Phase-gate blocking invariant: a phase remains open until all critical and important findings are resolved.
2. One-batch plan-update invariant: phase status, artifact status, and run metadata updates are applied in one end-of-run write operation.

## Consequences

- Improves reliability of phase progression and resume semantics.
- Strengthens reviewer confidence that gating behavior is consistent across adapters.
- Requires any future deviation to be explicitly superseded via a new ADR.

## Pros and cons of the options

- Chosen option: preserves correctness and traceability for a documentation-gated workflow.
- Rejected option: informal guidance is too easy to diverge and weakens governance guarantees.

## More information

Implementation-level details continue to live in the initialization contract and phase rubrics; this ADR captures the durable architectural authority for those rules.

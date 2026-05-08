---
title: ADR-003 Modular Monolith Architecture
status: active
record_class: canonical
audience: [internal]
owner: architecture-maintainer
capability: architecture
phase: planning
cadence: per-stage
last_reviewed: 2026-05-08
---

# ADR-003: Adopt modular monolith architecture for v1 workflow engine

- Status: Accepted
- Date: 2026-05-08
- Deciders: Project Initiator
- Consulted: none
- Informed: future contributors and reviewers
- Tags: [Architecture]
- Supersedes: None
- Superseded by: None
- Related documents: [../03_architecture/01_solution_design.md](../03_architecture/01_solution_design.md)

## Context and problem statement

project--orchestrator needs a design that can deliver quickly for a solo-to-small-team setting while keeping clear boundaries for future evolution. The system must coordinate multi-phase documentation workflows, enforce review gates, and support adapters for different agent ecosystems without adding avoidable operational burden.

## Decision drivers

- Fast time-to-usability for current team shape.
- Strong internal separation for orchestration, state, and adapters.
- Low operational overhead in v1.
- Future ability to extract boundaries if usage grows.

## Considered options

### Option 1: Modular monolith

- What it is: one deployable runtime with explicit internal modules and interface boundaries.
- Pros: simpler deployment, rapid iteration, centralized traceability, lower ops burden.
- Cons: independent scaling is limited; boundary discipline must be maintained in code.

### Option 2: Service-oriented split from day one

- What it is: separate services for orchestration, state, review, and adapters.
- Pros: independent scaling and isolated deployment domains.
- Cons: higher complexity, higher operational cost, and slower initial delivery.

### Option 3: External workflow-engine-first architecture

- What it is: workflow control delegated to an external orchestration platform.
- Pros: explicit state machine tooling and built-in run controls.
- Cons: dependency and portability risk, steeper setup for early stage.

## Decision outcome

Choose Option 1: modular monolith for v1, with explicit internal module boundaries that permit future extraction.

### Consequences

- Faster delivery for current constraints.
- Reduced deployment and debugging complexity during early adoption.
- Requires deliberate interface discipline to avoid monolith entanglement over time.

## Pros and cons of the options

- Chosen option: balances speed, maintainability, and portability for current scale.
- Rejected option: service split is premature for solo/small-team operation and raises operating cost.
- Rejected option: external workflow engine introduces avoidable dependency risk in v1.

## More information

This decision is reflected in the solution design building-block and deployment sections.

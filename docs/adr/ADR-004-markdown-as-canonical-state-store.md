---
title: ADR-004 Markdown as Canonical State Store
status: active
record_class: canonical
audience: [internal]
owner: architecture-maintainer
capability: architecture
phase: planning
cadence: per-stage
last_reviewed: 2026-05-08
---

# ADR-004: Use Markdown files as canonical workflow state and artifact store

- Status: Accepted
- Date: 2026-05-08
- Deciders: Project Initiator
- Consulted: none
- Informed: future contributors and reviewers
- Tags: [Architecture, Data]
- Supersedes: None
- Superseded by: None
- Related documents: [../03_architecture/01_solution_design.md](../03_architecture/01_solution_design.md)

## Context and problem statement

The workflow is primarily driven by instruction, skill, and artifact documents. The user explicitly prioritizes Markdown as the best working format for agent-guided process control. The state model must remain easy to inspect, diff, review, and port across agent ecosystems.

## Decision drivers

- Human-readable and agent-readable state.
- Native compatibility with repository workflows and reviews.
- Minimal setup burden for local-first execution.
- Portability across different tooling environments.

## Considered options

### Option 1: Markdown files as canonical state

- What it is: plan, artifacts, and decision records stored as repository Markdown files.
- Pros: transparent history, easy collaboration via version control, no separate infrastructure.
- Cons: concurrent edits can produce merge conflicts; structured querying is limited.

### Option 2: Embedded database plus document exports

- What it is: operational state in a local database with generated Markdown artifacts.
- Pros: stronger query/update semantics and conflict handling options.
- Cons: increased complexity, reduced transparency, and added migration concerns.

### Option 3: External managed database

- What it is: centralized state service outside repository files.
- Pros: stronger multi-user concurrency support and centralized control.
- Cons: infrastructure overhead, reduced offline usability, lower portability.

## Decision outcome

Choose Option 1: Markdown files are the canonical state and output format for v1.

### Consequences

- Aligns directly with user workflow and repository-native process.
- Keeps startup and operational requirements minimal.
- Requires explicit merge/conflict guidance and disciplined update patterns for concurrent usage.

## Pros and cons of the options

- Chosen option: best fit for transparency, portability, and low-friction adoption.
- Rejected option: embedded database adds complexity without clear v1 necessity.
- Rejected option: external database conflicts with local-first and portability goals.

## More information

The plan and artifact roadmap remain the single state source across runs.

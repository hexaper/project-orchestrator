---
title: ADR-005 Local-First CLI Runtime
status: active
record_class: canonical
audience: [internal]
owner: architecture-maintainer
capability: architecture
phase: planning
cadence: per-stage
last_reviewed: 2026-05-08
---

# ADR-005: Use local-first CLI runtime with adapter-compatible deployment path

- Status: Accepted
- Date: 2026-05-08
- Deciders: Project Initiator
- Consulted: none
- Informed: future contributors and reviewers
- Tags: [Architecture, Delivery, Operations]
- Supersedes: None
- Superseded by: None
- Related documents: [../03_architecture/01_solution_design.md](../03_architecture/01_solution_design.md)

## Context and problem statement

The user selected local-first execution as the initial deployment model and requested flexibility to run in other agent deployments in the future. The runtime decision must preserve quick local usability while avoiding lock-in to a single execution environment.

## Decision drivers

- Immediate usability on contributor machines.
- Low operational overhead for v1.
- Portability to CI and other agent-hosted contexts.
- Compatibility with Markdown-based canonical state.

## Considered options

### Option 1: Local-first CLI runtime

- What it is: workflow runs locally in repository context via command invocation.
- Pros: fastest onboarding, offline-friendly, straightforward debugging.
- Cons: collaboration requires git-based coordination; environment differences can affect behavior.

### Option 2: GitHub Actions-first runtime

- What it is: workflow primarily executed through hosted CI automation.
- Pros: consistent execution environment and centralized logs.
- Cons: slower interaction cycle and reduced conversational flexibility.

### Option 3: Managed cloud runtime from day one

- What it is: hosted service executes orchestration for all users.
- Pros: centralized control and potential multi-user scaling.
- Cons: highest setup/operations burden and stronger platform coupling.

## Decision outcome

Choose Option 1: local-first CLI runtime for v1, with architecture boundaries that allow CI/hosted adapters later.

### Consequences

- Supports rapid iteration and immediate practical usage.
- Keeps v1 operations lightweight.
- Requires adapter and environment-conformance work before broader deployment targets are production-ready.

## Pros and cons of the options

- Chosen option: optimizes speed-to-usability while preserving extension paths.
- Rejected option: CI-first impairs interactive workflow quality for early phases.
- Rejected option: cloud-first is disproportionate to current scale and constraints.

## More information

Future deployment expansion should reuse the same orchestration contract and Markdown state model.

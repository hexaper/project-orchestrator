---
title: Solution Design — project--orchestrator
status: active
record_class: canonical
audience: [internal, manager]
owner: architecture-maintainer
capability: architecture
phase: planning
cadence: per-stage
last_reviewed: 2026-05-08
---

# Solution Design — project--orchestrator

## 1. Introduction and goals

project--orchestrator provides a guided initialization workflow that helps teams produce complete, review-ready documentation before implementation planning. The architecture goal is to deliver a local-first workflow that is reliable for a small team, preserves traceability across phases, and remains portable across multiple agent ecosystems.

Primary success conditions for this design:

- End-to-end phase progression is deterministic and resumable.
- Artifacts remain canonical Markdown-first outputs in repository paths.
- Architecture enables integration with agent instruction/skill/plugin surfaces as the primary process-control mechanism.

## 2. Constraints

- Repository-native Markdown artifacts are the primary state format.
- The system must run local-first for v1 and remain usable in non-interactive environments later.
- The workflow must support cross-agent portability (Copilot, Claude Code, and similar environments).
- Human and agent review loops are mandatory before phase closure.
- Team shape is currently solo-to-small-team, so operational complexity must stay low.

## 3. Context and scope

In scope:

- Phase orchestration logic for initialization and revisits.
- Artifact routing to phase/artifact rubrics and template-backed outputs.
- Plan-state management and captured-fact propagation across phases.
- End-of-phase review dispatch and findings enforcement.

Out of scope:

- Production application code generation.
- Organization-wide governance replacement.
- External PM-tool synchronization.

Neighboring systems and actors:

- Project Initiator interacting through a local agent-capable environment.
- Reviewer role (automated agent and/or human) for phase gates.
- Repository file system and version control as authoritative storage boundary.

## 4. Solution strategy

The system uses a modular monolith architecture with explicit internal boundaries around orchestration, artifact processing, review coordination, and adapter integration. This preserves fast local iteration while retaining clear seams for future extraction.

The strategy is contract-first and adapter-driven:

- Core workflow contract defines phase lifecycle, stop rules, artifact execution modes, and review invariants.
- Agent adapters translate this contract to environment-specific instruction and plugin surfaces.
- Markdown artifact and plan files remain canonical state to maximize portability and auditability.

Decision references:

- [ADR-003](../adr/ADR-003-modular-monolith-architecture.md)
- [ADR-004](../adr/ADR-004-markdown-as-canonical-state-store.md)
- [ADR-005](../adr/ADR-005-local-first-cli-runtime.md)
- [ADR-006](../adr/ADR-006-phase-gate-and-plan-update-invariants.md)

## 5. Building block view

Primary building blocks and responsibilities:

- Workflow Orchestrator: resolves active phase/artifact, enforces sequencing, and applies per-run stop rules.
- Artifact Engine: executes phase/artifact rubrics in interview/confirm/extract modes and writes outputs.
- Plan State Manager: reads/writes the initialization plan, roadmap status, facts, concerns, and run metadata.
- Review Coordinator: invokes review agents, classifies findings, and blocks completion when critical or important findings remain.
- Adapter Layer: maps core workflow operations to host agent ecosystems and plugin interfaces.
- Validation Layer: runs documentation schema/quality checks and reports gate status.

This decomposition supports small-team maintainability and cross-agent portability without distributed-systems overhead.

## 6. Runtime view

Primary flow (happy path):

1. User invokes initialization command.
2. Workflow Orchestrator resolves phase status and active artifact from plan state.
3. Artifact Engine runs rubric-driven interaction and writes artifact updates.
4. Plan State Manager records captured facts and artifact outcomes.
5. Review Coordinator dispatches end-of-phase review.
6. Critical/important findings are resolved and artifacts are updated.
7. Plan State Manager performs one-batch phase update and sets next recommended step.

Failure and recovery behavior:

- Interrupted run: next invocation resumes from plan state and active artifact context.
- Invalid artifact output: validation blocks closure until corrected.
- Review failure: phase remains open until required severities are resolved.
- Adapter-level mismatch: adapter returns bounded error; core contract remains unchanged.

## 7. Deployment view

v1 deployment model is local-first CLI execution on contributor machines.

- Primary runtime: local command execution inside repository working copy.
- Data boundary: repository files (plan + artifacts + ADRs).
- Collaboration model: team members coordinate through version control workflows.
- Future extension path: same contract can run in CI or hosted agents by reusing adapter boundary rather than rewriting orchestration core.

## 8. Cross-cutting concepts

- Traceability: every phase transition, artifact status change, and review finding is recorded in plan history.
- Portability: contract-first workflow with adapter translation for agent-specific instruction/plugin formats.
- Review governance: no phase closure when unresolved critical or important findings exist.
- Data integrity: one-batch plan updates at end-of-run prevent partial state drift.
- Resumability: state-driven execution supports continuation after interruption.

## 9. Architectural decisions

- [ADR-003](../adr/ADR-003-modular-monolith-architecture.md) — Adopt modular monolith architecture.
- [ADR-004](../adr/ADR-004-markdown-as-canonical-state-store.md) — Use Markdown files as canonical state store.
- [ADR-005](../adr/ADR-005-local-first-cli-runtime.md) — Use local-first CLI runtime with adapter-compatible extension path.
- [ADR-006](../adr/ADR-006-phase-gate-and-plan-update-invariants.md) — Enforce phase-gate blocking and one-batch plan updates as workflow invariants.

## 10. Quality requirements

Design response to PRD non-functional requirements:

- NFR-001 Documentation completeness: Artifact Engine and Validation Layer enforce template/frontmatter conformance and marker-free phase gates.
- NFR-002 Workflow continuability: Plan State Manager persists resumable state and active context between runs.
- NFR-003 Output conformance: Validation Layer includes docs schema and quality checks as closure prerequisites.
- NFR-004 Differentiator completeness: in a fresh clone, first run setup requires no manual pre-configuration steps and initialization can reach the next incomplete phase or revisit target in one command invocation after interruption.

Scale assumptions for v1:

- Target: small team (3-10 users) with occasional concurrent runs.
- Contention model: repository-level coordination through version control and merge resolution.

## 11. Risks and technical debt

- Runtime implementation risk: the reference runtime is now Node.js 22+ with TypeScript, but adapter and contract boundaries must remain runtime-agnostic to preserve cross-agent portability.
- Cross-agent drift risk: adapter behavior may diverge across ecosystems without shared conformance checks.
- Concurrent plan edits: file-based state can conflict when multiple users edit same phase concurrently.
- Review dependency: quality relies on reviewer availability and rubric quality.

Mitigation direction:

- Add adapter conformance scenarios in testing strategy.
- Add plan-write conflict guidelines in operations documentation.
- Keep architecture seams explicit to enable selective extraction if team/scale grows.

## 12. Glossary

- Project Initiator: IT-adjacent person running initialization and producing artifacts.
- Phase gate: closure checkpoint requiring satisfied criteria and resolved high-severity findings.
- Artifact mode: rubric execution mode (`interview`, `confirm`, `extract`, `skipped`).
- Future-phase fact: out-of-phase insight captured for later artifact execution.
- Adapter: integration boundary translating core workflow contract to a specific agent ecosystem.

## Related documents

- [Product Requirements Document](../02_product/01_prd.md)
- [User Journeys](../02_product/03_user_journeys.md)
- [ADR Index](../adr/INDEX.md)

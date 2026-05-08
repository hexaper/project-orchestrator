---
title: ADR Index
status: active
record_class: canonical
audience: [internal]
owner: architecture-maintainer
capability: architecture
phase: planning
cadence: monthly
last_reviewed: 2026-05-07
---

# ADR Index

> **Purpose**: provide the maintained list of architecture decision records and their current status.
> **Audience**: architects, engineers, reviewers, and delivery leads who need the canonical ADR map.
> **When to update**: update when ADRs are created, accepted, superseded, or archived.

## How to use this template

- Keep this index current as the canonical navigation page for `docs/adr/`.
- One row per ADR; link directly to the source file.
- Keep durable decision authority in the ADR files themselves.

## ADR list

| ADR | Title | Status | Date | Notes |
| --- | --- | --- | --- | --- |
| [ADR-006](ADR-006-phase-gate-and-plan-update-invariants.md) | Phase-Gate and Plan-Update Invariants | Accepted | 2026-05-08 | Makes phase-gate blocking and one-batch plan updates binding architecture invariants. |
| [ADR-005](ADR-005-local-first-cli-runtime.md) | Local-First CLI Runtime | Accepted | 2026-05-08 | Establishes local-first execution with adapter-compatible extension path. |
| [ADR-004](ADR-004-markdown-as-canonical-state-store.md) | Markdown as Canonical State Store | Accepted | 2026-05-08 | Keeps plan and artifact state repository-native and portable. |
| [ADR-003](ADR-003-modular-monolith-architecture.md) | Modular Monolith Architecture | Accepted | 2026-05-08 | Adopts modular monolith shape for v1 workflow engine. |
| [ADR-002](../99_archive/repo/adr/ADR-002-prompt-adoption-with-tracked-assistant-tooling.md) | Prompt-Based Template Adoption with Tracked Assistant-Native Tooling | Archived | 2026-05-07 | Archived repository bootstrap ADR retained for traceability. |
| [ADR-001](../99_archive/repo/adr/ADR-001-skill-first-template-adoption.md) | Command-First Template Adoption | Archived | 2026-05-07 | Archived repository bootstrap ADR retained for traceability. |
| [ADR-000](ADR-000-template.md) | Template | Draft | 2026-05-07 | Starting point for new decisions. |

## Status notes

- Proposed: under review and not yet binding.
- Accepted: approved and binding until superseded.
- Superseded: replaced by a newer decision.
- Archived: retained for history without active authority.

## Related documents

- [README.md](README.md) — ADR policy, lifecycle, and authority rules.
- [ADR-000-template.md](ADR-000-template.md) — default ADR authoring template.
- [../99_archive/repo/adr/README.md](../99_archive/repo/adr/README.md) — archived repository ADR history.
- [../03_architecture/11_adr_index_TEMPLATE.md](../03_architecture/11_adr_index_TEMPLATE.md) — architecture-side ADR snapshot template.
- [../03_architecture/01_solution_design_TEMPLATE.md](../03_architecture/01_solution_design_TEMPLATE.md) — links architecture baseline sections to ADRs.

---
title: Project Initialization Plan
status: active
record_class: historical
audience: [internal]
owner: initialization workflow
capability: knowledge
phase: planning
cadence: ad-hoc
last_reviewed: 2026-05-08
---

# Project Initialization Plan

## Goal

Initialize project--orchestrator as an internal AI-centric tooling repository.

## Profile

- Selected profile: internal-tool
- Profile rationale: Project type is internal tool with regulatory posture none, which maps to the internal-tool profile.
- Overrides applied: none

## Phase Roadmap

| Phase | Status | Notes |
| --- | --- | --- |
| 0. Triage | done | 2026-05-08 |
| 1. Intent | done | 2026-05-08 |
| 2. Specification | done | 2026-05-08 |
| 3. Design | done | 2026-05-08 |
| 4. Govern & Operate | pending | |
| 5. Adapt | pending | |
| 6. Final review | pending | |

## Artifact Roadmap

| Phase | Artifact | Status | Mode (initial) | Mode (effective) | Output path | Last Revisited |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | project-brief | done | interview | interview | docs/00_governance/00_project_brief.md | |
| 1 | business-case | skipped | skipped | skipped | docs/00_governance/01_business_case.md | |
| 2 | prd | done | interview | interview | docs/02_product/01_prd.md | |
| 2 | requirements-catalog | skipped | skipped | skipped | docs/02_product/02_requirements_catalog.md | |
| 2 | journeys | done | interview | interview | docs/02_product/03_user_journeys.md | |
| 2 | acceptance-catalog | skipped | skipped | skipped | docs/02_product/05_acceptance_catalog.md | |
| 3 | solution-design | done | interview | interview | docs/03_architecture/01_solution_design.md | |
| 3 | adr | done | interview | interview | docs/adr/ADR-NNN-<decision-slug>.md | |
| 3 | c4 | skipped | skipped | skipped | docs/03_architecture/c4/*.mmd | |
| 4 | ai-use-policy | pending | interview | interview | docs/04_ai_governance/01_ai_use_policy.md | |
| 4 | test-strategy | pending | interview | interview | docs/05_testing_acceptance/01_test_strategy.md | |
| 4 | security-baseline | skipped | skipped | skipped | docs/06_security_operations/01_security_baseline.md | |
| 4 | delivery-plan | skipped | skipped | skipped | docs/07_delivery/01_delivery_plan.md | |
| 5 | language-adaptation | pending | interview | interview | src/, tests/, config/, .gitignore, .editorconfig, src/AGENTS.md | |
| 5 | repo-sync | pending | extract | extract | README.md, AGENTS.md, bin/README.md, diagrams/README.md, examples/README.md | |

## Project Facts

- Project name: project--orchestrator.
- One-line summary: guide teams to produce comprehensive, review-ready project documentation before implementation planning.
- Project type: internal tool.
- AI involvement: core (AI model behavior is central to the product).
- Regulatory posture: none (standard software product).
- Team shape: solo.

## Future-Phase Facts

### Phase 2 — prd

- (captured during Phase 1, 2026-05-08): "It aims to guide the user in creating comprehensive project documentation and streamline the process with best-practice outputs."
- (captured during Phase 1, 2026-05-08): "Documentation should pass strict acceptance gates before implementation planning starts."
- (captured during Phase 2, 2026-05-08): "Root cause is absence of stable, repeatable process for completeness — not user incompetence."
- (captured during Phase 2, 2026-05-08): "Differentiator: bundled repository scaffold + doc templates + conversational AI-guided execution in one seamless package."
- (captured during Phase 2, 2026-05-08): "Speed-to-usability is a priority; author is also primary user."
- (captured during Phase 2, 2026-05-08): "Out of scope: code generation for production software; eliminating human review in governance decisions; template customization (Phase 2+)."

### Phase 3 — solution-design

- (captured during Phase 2, 2026-05-08): "Primary personas are IT-adjacent: team leads, architects, project managers, solo developers — treated as a single Project Initiator persona in journeys."
- (captured during Phase 1, 2026-05-08): "Documentation should undergo an extensive review sequence until acceptance gates pass."
- (captured during Phase 3, 2026-05-08): "Selected architecture shape is modular monolith for v1."
- (captured during Phase 3, 2026-05-08): "Instruction, skill, agent, and plugin files are the primary mechanism directing the workflow."
- (captured during Phase 3, 2026-05-08): "Primary state/output store remains Markdown files in repository paths."
- (captured during Phase 3, 2026-05-08): "Initial runtime is local-first CLI, with compatibility goals for other agent deployments."
- (captured during Phase 3, 2026-05-08): "v1 scale target is small team usage (3-10 users) with occasional concurrent runs."

### Phase 4 — test-strategy

- (captured during Phase 3, 2026-05-08): "Test strategy should include adapter conformance scenarios across agent ecosystems and resumability checks for interrupted runs."
- (captured during Phase 3, 2026-05-08): "Review gating must verify no unresolved critical/important findings before phase closure."

### Phase 4 — security-baseline

- (captured during Phase 3, 2026-05-08): "Markdown/file-based workflow state introduces repository-integrity and concurrent-edit conflict considerations that require guardrails."

### Phase 5 — language-adaptation

- (captured during Phase 3, 2026-05-08): "Support tooling language remains open between Python and JavaScript/TypeScript, but adapter contract must stay runtime-agnostic."

### Phase 5 — repo-sync

- (captured during Phase 1, 2026-05-08): "The app should be based on this repository and its documentation templates."

## Open Questions For Current Phase

none

## Parked Questions For Later

none

## Concerns And Recommendations

- **Concern (Phase 3, 2026-05-08):** The implementation language/framework remains undecided while cross-agent portability is a core requirement.
	- **Why it matters here:** Language choices shape adapter boundaries, testing approach, and maintenance cost in a small-team environment.
	- **Stronger option:** Commit in Phase 5 to one reference runtime for core adapter implementation and keep the workflow contract language-agnostic.
	- **Trade-off:** Faster implementation focus now may reduce early parity across secondary runtimes.
	- **Acceptable if intentional:** yes, if the contract-first adapter boundary remains explicit and portability checks are added to test strategy.

## Files Updated This Run

- docs/03_architecture/01_solution_design.md
- docs/adr/ADR-003-modular-monolith-architecture.md
- docs/adr/ADR-004-markdown-as-canonical-state-store.md
- docs/adr/ADR-005-local-first-cli-runtime.md
- docs/adr/INDEX.md
- docs/00-source-of-truth.md
- docs/superpowers/plans/2026-05-08-project-initialization.md

## Review Findings

- [fixed] important: project name mismatch between project brief and plan goal (docs/00_governance/00_project_brief.md, docs/superpowers/plans/2026-05-08-project-initialization.md)
- [fixed] important: Phase 1 and project-brief status were pending after artifact production (docs/superpowers/plans/2026-05-08-project-initialization.md)
- [fixed — Phase 2] critical: PRD related-documents linked to non-existent solution_design.md; replaced with template link
- [fixed — Phase 2] important: PRD and journeys used single-hyphen project name; normalised to project--orchestrator
- [fixed — Phase 2] important: NFR-004 was non-measurable; rewritten with verifiable criterion
- [fixed — Phase 2] important: source-of-truth map missing active PRD and active user journeys entries; added
- [advisory — Phase 2] minor: J-001 and J-002 journey steps reference /init command name rather than abstract action; noted for future revision
- [fixed — Phase 3] important: Phase 3 and its artifacts remained pending in plan roadmap after artifact production
- [fixed — Phase 3] important: Phase 3 confirmed decisions and produced files were not recorded in plan
- [fixed — Phase 3] important: source-of-truth map lacked explicit active solution design ownership
- [fixed — Phase 3] minor: ADR-000 row in ADR index was unlinked and inconsistent with linked-row convention

## Next Recommended Step

Run `/init` to continue to Phase 4 (Govern & Operate).

## Resume Context

- Active phase: 3 (Design)
- Active artifact: ai-use-policy
- Last user input: "the ai agents skills/instuctions/agents/plugins files will be the main way direct the process, these files will be heavily used as a one complete workflow"
- Outstanding clarifications: none

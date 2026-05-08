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
| 4. Govern & Operate | done | 2026-05-08 |
| 5. Adapt | done | 2026-05-08 |
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
| 3 | adr | done | interview | interview | docs/adr/ADR-003-modular-monolith-architecture.md; docs/adr/ADR-004-markdown-as-canonical-state-store.md; docs/adr/ADR-005-local-first-cli-runtime.md; docs/adr/ADR-006-phase-gate-and-plan-update-invariants.md | |
| 3 | c4 | skipped | skipped | skipped | docs/03_architecture/c4/*.mmd | |
| 4 | ai-use-policy | done | interview | interview | docs/04_ai_governance/01_ai_use_policy.md | 2026-05-08 |
| 4 | test-strategy | done | interview | interview | docs/05_testing_acceptance/01_test_strategy.md | 2026-05-08 |
| 4 | security-baseline | skipped | skipped | skipped | docs/06_security_operations/01_security_baseline.md | |
| 4 | delivery-plan | skipped | skipped | skipped | docs/07_delivery/01_delivery_plan.md | |
| 5 | language-adaptation | done | interview | interview | src/, tests/, config/, .gitignore, .editorconfig, src/AGENTS.md | 2026-05-08 |
| 5 | repo-sync | done | extract | extract | README.md, AGENTS.md, bin/README.md, diagrams/README.md, examples/README.md | 2026-05-08 |

## Project Facts

- Project name: project--orchestrator.
- One-line summary: guide teams to produce comprehensive, review-ready project documentation before implementation planning.
- Project type: internal tool.
- AI involvement: core (AI model behavior is central to the product).
- Regulatory posture: none (standard software product).
- Team shape: solo.
- Naming decision: keep project--orchestrator unchanged for now.
- Workflow scope: provide a full end-to-end workflow to generate complete project documentation.
- Input expectation: workflow accepts company and project context as user-provided input.
- Output expectation: structured, decision-complete documentation with no open items and no revisit loops unless a major change is introduced.
- Major-change policy: significant changes are handled as a mini-project.
- Assistant ecosystem expectation: Claude, Copilot, Codex, and OpenCode should be interchangeable, with the best option still under evaluation.
- UX constraint: workflow should remain friendly and guided for non-expert users.
- Governance constraint: strict review gates are mandatory and cannot be bypassed without documented exception handling.
- Reference runtime decision: Node.js 22+ with TypeScript.
- Framework style decision: prompt-driven instruction executor with adapter modules and contract-first boundaries.
- Test framework decision: Vitest.
- Package manager decision: npm/pnpm.
- CI decision: GitHub Actions for linting, formatting, link checks, and documentation drift controls.

## Future-Phase Facts

### Phase 2 — prd

- (captured during Phase 1, 2026-05-08): "It aims to guide the user in creating comprehensive project documentation and streamline the process with best-practice outputs."
- (captured during Phase 1, 2026-05-08): "Documentation should pass strict acceptance gates before implementation planning starts."
- (captured during Phase 0, 2026-05-08): "Output quality bar is decision-complete documentation with no open items and no revisit unless there is a major change."
- (captured during Phase 2, 2026-05-08): "Root cause is absence of stable, repeatable process for completeness — not user incompetence."
- (captured during Phase 2, 2026-05-08): "Differentiator: bundled repository scaffold + doc templates + conversational AI-guided execution in one seamless package."
- (captured during Phase 2, 2026-05-08): "Speed-to-usability is a priority; author is also primary user."
- (captured during Phase 2, 2026-05-08): "Out of scope for this release: code generation for production software; eliminating human review in governance decisions; template customization (deferred to a later release)."

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
- (captured during Phase 4, 2026-05-08): "Primary validation approach is real-project documentation runs from start to finish."
- (captured during Phase 4, 2026-05-08): "Automated CI checks include markdown lint, docs schema/frontmatter validation, link checks, consistency checks, and scripted review-agent checks."
- (captured during Phase 4, 2026-05-08): "Final acceptance remains human-reviewed, with agent collaboration grounded in standards and document evidence."
- (captured during Phase 4, 2026-05-08): "PR merge requires full documentation validation so only standards-compliant current-best docs land in main."
- (captured during Phase 4, 2026-05-08): "Implementation planning is blocked until complete and traceable end-to-end documentation workflow knowledge is accepted."
- (captured during Phase 4, 2026-05-08): "AI testing is cost-constrained; workflow and checks should be optimized for token usage."

### Phase 4 — security-baseline

- (captured during Phase 3, 2026-05-08): "Markdown/file-based workflow state introduces repository-integrity and concurrent-edit conflict considerations that require guardrails."

### Phase 5 — language-adaptation

- (captured during Phase 3, 2026-05-08): "Support tooling language remains open between Python and JavaScript/TypeScript, but adapter contract must stay runtime-agnostic."
- (captured during Phase 4, 2026-05-08): "Language adaptation should include low-cost deterministic checks first and targeted high-cost agent checks to control token spend."
- (captured during Phase 4, 2026-05-08): "Model/runtime choices should be compared with quality-per-token evidence during adaptation."
- (captured during Phase 0, 2026-05-08): "Claude, Copilot, Codex, and OpenCode should remain interchangeable while the best option is evaluated."

### Phase 5 — repo-sync

- (captured during Phase 1, 2026-05-08): "The app should be based on this repository and its documentation templates."
- (captured during Phase 0, 2026-05-08): "Workflow goal is complete end-to-end documentation generation from provided company/project context."

## Open Questions For Current Phase

none

## Parked Questions For Later

none

## Concerns And Recommendations

- **Concern (Phase 4, 2026-05-08):** AI-agent evaluation depth is constrained by runtime cost.
	- **Why it matters here:** Insufficient high-value review coverage can allow alignment and quality regressions across documentation artifacts.
	- **Stronger option:** Enforce tiered validation where deterministic checks run first and budgeted agent reviews target highest-risk areas.
	- **Trade-off:** Some low-risk areas may receive less frequent deep AI review.
	- **Acceptable if intentional:** yes, if cost-aware coverage thresholds and escalation triggers are documented and followed.

## Files Updated This Run

- src/AGENTS.md
- src/README.md
- tests/README.md
- config/README.md
- .gitignore
- README.md
- AGENTS.md
- bin/README.md
- diagrams/README.md
- examples/README.md
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
- [fixed — Phase 4] important: Phase 4 and active artifacts were pending after artifact production; reconciled to done with revisit dates
- [fixed — Phase 4] important: Phase 4 governance/testing decisions and files-updated traceability were missing from plan
- [fixed — Phase 5] important: language/runtime, testing stack, package manager, and CI choices were unresolved for adaptation
- [fixed — Phase 5] important: repository entry surfaces still used template-centric wording instead of project-specific guidance

## Next Recommended Step

Run `/init` to continue to Phase 6 (Final review).

## Resume Context

- Active phase: 6 (Final review)
- Active artifact: final-review
- Last user input: "continue"
- Outstanding clarifications: none

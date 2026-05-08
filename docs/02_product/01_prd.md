---
title: Product Requirements Document — project--orchestrator
status: active
record_class: canonical
audience: [internal, manager]
owner: product-owner
capability: product
phase: planning
cadence: per-release
last_reviewed: 2026-05-08
---

# Product Requirements Document — project--orchestrator

## Problem

Teams initiating software projects frequently produce incomplete or inconsistent documentation before implementation begins — not because of incompetence, but because no stable, repeatable process exists to tell them what completeness looks like. Without a structured completeness contract, critical framing decisions (scope, users, architecture constraints) are deferred or missed, causing rework downstream when gaps surface during build or review.

`project--orchestrator` exists to close that process gap: a guided, conversational workflow that surfaces exactly what each documentation artifact needs, helps the user capture it correctly, and enforces acceptance gates before allowing progression to implementation planning.

## Users

### Primary

- Solo developers and small teams initiating a new software project who need structured documentation guidance without a dedicated project manager or documentation specialist.
- The product author, who is also a primary user and uses the tool to bootstrap their own projects.

### Secondary

- Reviewers and approvers who validate documentation quality and phase-gate readiness before implementation may proceed.

### Out-of-scope users (this release)

- Enterprise multi-team rollouts with centralized governance tooling.
- Non-technical stakeholders who do not interact with the repository directly.

## Goals

- A user can complete a full documentation set (from project brief to implementation-ready artifact suite) without prior knowledge of what each document requires.
- All documentation phase gates pass before implementation planning begins — measurable as zero unresolved `[NEEDS-REVIEW]` markers and a passing `init-reviewer` run across all phases.
- The author can use the tool on their own project within the current release window and reach implementation phase.

## Non-goals

- Acting as a code generation platform for production software implementation.
- Eliminating human review and approval in governance-critical decisions.
- Template customization: parameter substitution, frontmatter overrides, or custom markers (deferred to a future release).
- Providing a roadmap or multi-project portfolio tracking capability.
- Replacing organization-wide governance policies outside this repository's framework.

## User stories

| ID | User story | Priority | Notes |
| --- | --- | --- | --- |
| US-001 | As a developer starting a new project, I want to be guided through each documentation artifact with contextual questions, so that I produce a complete, reviewable document without needing to know the template structure in advance. | Must | Core guided workflow. |
| US-002 | As a user completing a phase, I want an automated quality review to flag gaps before I move on, so that documentation defects are caught early rather than at implementation. | Must | Phase-gate enforcement. |
| US-003 | As a user revisiting a prior phase, I want to update a specific artifact without restarting the whole workflow, so that corrections are low-friction and targeted. | Must | Revisit mode. |
| US-004 | As a reviewer, I want to inspect phase artifacts and see structured findings classified by severity, so that I can approve progression with confidence. | Should | Reviewer use case. |
| US-005 | As a user, I want the workflow to capture architectural and governance facts I mention out of context and surface them in the right phase, so that nothing falls through the cracks during a long session. | Should | Cross-phase fact capture. |

## Functional requirements

| ID | Requirement | Priority | Acceptance reference |
| --- | --- | --- | --- |
| FR-001 | The system shall guide users through each documentation artifact via a structured interview, asking only relevant questions based on prior answers and captured project facts. | Must | [J-001 Step 3](03_user_journeys.md), [J-001 Step 5](03_user_journeys.md) |
| FR-002 | The system shall enforce phase-gate acceptance criteria before marking a phase as complete, blocking progression if criteria are unmet. | Must | [J-003 Step 5](03_user_journeys.md), [Acceptance criteria](#acceptance-criteria) |
| FR-003 | The system shall capture out-of-context facts (future-phase facts) during any artifact interview and surface them in the correct phase. | Must | [US-005](#user-stories), [J-001 Step 2](03_user_journeys.md) |
| FR-004 | The system shall support revisiting any completed phase or individual artifact without resetting downstream work. | Must | [J-002 Step 5](03_user_journeys.md), [Acceptance criteria](#acceptance-criteria) |
| FR-005 | The system shall dispatch an automated reviewer at the end of each phase and apply critical and important findings before closing the run. | Must | [J-003 Step 1](03_user_journeys.md), [J-003 Step 4](03_user_journeys.md) |
| FR-006 | The system shall produce documentation outputs that conform to this repository's template structure and frontmatter schema. | Must | [NFR-003](#non-functional-requirements), [Acceptance criteria](#acceptance-criteria) |
| FR-007 | The system shall support at least three artifact modes: interview (guided questions), confirm (validate extracted content), and extract (auto-fill from captured facts). | Should | [US-001](#user-stories), [J-001 Step 3](03_user_journeys.md) |
| FR-008 | The system shall maintain a persistent plan file that records phase status, artifact status, captured facts, concerns, and review findings across sessions. | Must | [NFR-002](#non-functional-requirements), [J-001 Step 7](03_user_journeys.md) |

## Non-functional requirements

| ID | Requirement | Measure or constraint | Acceptance reference |
| --- | --- | --- | --- |
| NFR-001 | Documentation completeness | All required frontmatter fields present; no `[TBD]` or `[NEEDS-REVIEW]` markers in any active artifact at phase gate. | [Acceptance criteria](#acceptance-criteria) |
| NFR-002 | Workflow continuability | A session interrupted at any point resumes to the next incomplete phase or selected revisit target in one `/init` invocation, with no field loss in the plan file. | [J-001 Step 7](03_user_journeys.md), [J-002 Step 5](03_user_journeys.md) |
| NFR-003 | Output conformance | All produced documents must pass the `docs_validator` CLI with zero errors. | [Acceptance criteria](#acceptance-criteria) |
| NFR-004 | Differentiator completeness | Running the initialization workflow in a fresh clone with no pre-installed dependencies produces all active documentation artifacts in one logical run, allowing resumptions when interrupted, with no separate installation or configuration step required. | [Acceptance criteria](#acceptance-criteria), [NFR-002](#non-functional-requirements) |

## Out of scope

- Production code generation or application scaffolding beyond repository structure.
- Automated human decision replacement in governance-critical approvals.
- Template customization engine (marker substitution, frontmatter overrides) — deferred to a future release.
- Multi-project or portfolio-level tracking.
- Non-repository-based documentation export (e.g., Confluence sync, PDF generation).
- Integrations with external project management tools (Jira, Linear, Asana).

## Acceptance criteria

- All phase gates (Phases 0–6) complete with zero unresolved `[NEEDS-REVIEW]` markers.
- `init-reviewer` passes for every phase with no critical or important findings outstanding.
- All produced documents pass `docs_validator` with zero errors.
- The author has used the tool end-to-end on at least one real project (this repository) and reached the implementation phase.
- Revisit flow navigates to and updates a completed artifact without corrupting plan state.

## Release plan

No hard external deadlines. Priority is speed-to-usability: the author is also the primary user and intends to use the tool on this project immediately. The release is complete when all documentation phase gates pass and implementation planning can begin. No staged rollout or rollback plan is required for this solo-use first release.

## Related documents

- [00_project_brief.md](../00_governance/00_project_brief.md) — upstream project brief this PRD extends.
- [03_user_journeys.md](03_user_journeys.md) — user journeys for the primary user types named here.
- [01_solution_design.md](../03_architecture/01_solution_design.md) — active solution design for project--orchestrator.
- [02_requirements_catalog_TEMPLATE.md](02_requirements_catalog_TEMPLATE.md) — requirements catalog template for future expansion.
- [05_acceptance_catalog_TEMPLATE.md](05_acceptance_catalog_TEMPLATE.md) — acceptance catalog template for detailed scenarios.

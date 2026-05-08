---
title: AI Use Policy — project--orchestrator
status: active
record_class: canonical
audience: [internal, manager]
owner: ai-governance
capability: ai_governance
phase: planning
cadence: monthly
last_reviewed: 2026-05-08
---

# AI Use Policy — project--orchestrator

## Scope

This policy applies to AI-assisted documentation workflows in project--orchestrator, including drafting documentation artifacts, guiding users through initialization phases, and reviewing documentation quality and consistency.

In scope:

- AI-assisted document drafting and refinement.
- AI-guided phase execution support in the initialization workflow.
- AI-assisted review of documentation completeness, consistency, and standards conformance.

Out of scope:

- Autonomous production-code generation for deployment without human review.
- AI-only final approvals for phase gates or implementation readiness.

## Approved use cases

| ID | Use case | Owner | Notes |
| --- | --- | --- | --- |
| AI-001 | Draft and improve project documentation artifacts | Project Initiator | Must preserve canonical template structure and frontmatter requirements. |
| AI-002 | Guide users through project execution phases and rubric-driven steps | Project Initiator | Guidance must follow documented workflow rules and stop gates. |
| AI-003 | Review documentation for completeness, detail, alignment, and standards compliance | Project Initiator | Findings must be traceable and resolved before phase closure where required. |
| AI-004 | Evaluate alternative AI models for documentation quality and workflow fit | Project Initiator | Model selection must be evidence-driven and revisitable. |

## Restricted or prohibited use cases

| ID | Restriction | Reason | Notes |
| --- | --- | --- | --- |
| AI-R-001 | Sending secrets, credentials, or private data to external AI providers | Security and privacy risk | Never expose confidential secrets or personal private data. |
| AI-R-002 | Generating production code without human review | Quality and governance risk | Any code output requires explicit human review and acceptance. |
| AI-R-003 | Silent documentation changes without review or traceability | Auditability and trust risk | All material changes must be reviewable and leave a visible history. |
| AI-R-004 | Modifying documentation standards through AI output without explicit review trail | Governance drift risk | Standards changes require intentional review and traceable acceptance. |
| AI-R-005 | Proceeding to implementation planning before documentation is fully accepted | Process integrity risk | Implementation planning is blocked until documentation acceptance gates pass. |

## Data and model boundaries

Data sent to AI providers may include full repository content relevant to documentation work:

- Repository Markdown/document content.
- Project planning notes and metadata.
- Source code and scripts present in repository scope.

Data boundary requirements:

- Do not send secrets, credentials, or private data to external providers.
- Handle business-sensitive content with minimum-disclosure practices and explicit user awareness.
- Keep prompts and outputs scoped to task-relevant content to reduce leakage and token cost.

Approved provider and deployment boundaries:

- Approved AI assistant surfaces for this workflow: Claude, Copilot, Codex, and OpenCode.
- Approved deployment modes: local-first execution and approved provider-hosted assistant sessions used for repository documentation work.
- Model/runtime selection remains interchangeable across approved surfaces while best option is evaluated using quality-per-token evidence.

Retention and audit requirements:

- Retention default: keep no separate prompt/output archive outside normal repository artifacts and required tool logs.
- Any AI-assisted material documentation change must remain traceable through repository history and/or phase review records.
- Minimum audit fields for material AI-assisted edits: actor, timestamp, artifact path, and review disposition.

## Approval workflow

- AI may propose draft content, edits, and review findings.
- Human review is required before accepting or merging documentation changes.
- Human review is required before phase-gate advancement.
- Human review is required for architectural and governance decisions.
- Human review is required before implementation planning begins.

Approval trace requirements:

- Accepted changes must be visible in repository history.
- Review outcomes must be documented in plan/review artifacts where phase rules require it.
- Decisions that change durable behavior must be captured in ADRs.

## Evaluation and safety

Minimum safety and quality controls:

- Use AI review passes to challenge weak assumptions and detect cross-document inconsistencies.
- Treat model outputs as non-authoritative until validated against project standards and source documents.
- Require iterative correction when findings identify gaps in detail, alignment, or traceability.
- Optimize token usage by constraining scope and reusing structured workflow context.

## Compliance and external references

- Repository documentation standards and source-of-truth ownership rules.
- Initialization contract and per-phase stop/gate requirements.
- ADR process for durable technical and workflow decisions.

## Owners and approvers

- Policy owner: Project Initiator
- Technical approver: Project Initiator
- Governance approver: Project Initiator
- Review cadence: monthly or when workflow/governance constraints change

## Related documents

- [Solution Design](../03_architecture/01_solution_design.md)
- [Project Initialization Plan](../superpowers/plans/2026-05-08-project-initialization.md)
- [ADR Index](../adr/INDEX.md)
- [Test Strategy](../05_testing_acceptance/01_test_strategy.md)

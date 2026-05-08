---
title: Project Brief
status: active
record_class: canonical
audience: [internal, manager]
owner: product-owner
capability: governance
phase: initiation
cadence: one-shot
last_reviewed: 2026-05-08
---

# Project Brief

## Summary

Project `project--orchestrator` is an internal initiative to guide teams through creating comprehensive, review-ready project documentation using this repository's documentation model and templates. The project exists to reduce downstream rework caused by incomplete or inconsistent project framing before implementation.

## Goals and success measures

- At phase-gate review, 100% of required canonical documentation artifacts are present, have valid frontmatter, and contain no unresolved required-section placeholders.
- Before any phase is closed, there are 0 unresolved critical or important review findings.
- Revisit loops are avoided in normal flow; re-opening completed outputs is limited to major changes handled as a mini-project.

## Scope (in/out)

### In scope

- A guided workflow that asks contextual questions and helps users capture clear project intent and scope.
- Documentation outputs aligned to this repository's templates and governance structure.
- A review sequence that checks completeness and quality before allowing progression.

### Out of scope

- Implementing product runtime features unrelated to documentation orchestration.
- Replacing organization-wide governance policies outside this repository's framework.
- Defining final technical architecture decisions in this phase.

## Stakeholders

- Primary stakeholder persona for v1: Project Initiator (solo developer, technical lead, or project manager).
- Decision owner for scope and gate exceptions: product-owner role.
- Software developers who initiate and execute projects.
- Project managers and team leads responsible for planning quality and delivery readiness.
- Reviewers and approvers who validate documentation quality and phase-gate readiness.

## Constraints and assumptions

### Constraints

- The workflow must be based on this repository and its documentation templates.
- The user experience should remain friendly and guided while preserving strict review gate quality.

### Assumptions

- Users can provide enough project context during guided intake to produce usable first-pass documents.
- Teams will follow the review sequence before implementation planning and architecture lock-in.

## Risks and dependencies

### Risks

- Broad user personas may lead to inconsistent depth or quality if guidance is not sufficiently specific by context.
- Strict gates may increase early effort if criteria are not explained clearly to users.

### Dependencies

- Continued availability and quality of repository templates and governance documentation.
- Alignment of future phase artifacts with the intent captured in this brief.

## Governance and approval

- Phase progression is controlled by documented acceptance gates and review outcomes.
- Project-level scope and quality decisions are approved by the responsible project lead role.
- Escalation follows the repository's governance model and decision records in the documentation tree.
- Until a project-specific board terms document is instantiated, escalation authority references [Board Terms of Reference Template](03_board_terms_of_reference_TEMPLATE.md).

## Related documents

- [Business Case Template](01_business_case_TEMPLATE.md)
- [Project Initiation Document Template](02_project_initiation_document_TEMPLATE.md)
- [Delivery Plan Template](../07_delivery/01_delivery_plan_TEMPLATE.md)

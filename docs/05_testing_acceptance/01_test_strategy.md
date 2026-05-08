---
title: Test Strategy — project--orchestrator
status: active
record_class: canonical
audience: [internal, manager]
owner: quality-lead
capability: quality
phase: planning
cadence: per-stage
last_reviewed: 2026-05-08
source_of_truth: repo
---

# Test Strategy — project--orchestrator

## Scope

This strategy covers validation of the complete documentation-creation workflow from initialization start through documentation acceptance gates required before implementation planning.

In scope:

- Documentation artifact generation and updates across active phases.
- Documentation standards compliance and frontmatter/schema conformance.
- Cross-document consistency and alignment checks.
- AI-assisted review quality, model fit, and workflow traceability.

Out of scope:

- Production software feature verification outside documentation workflow tooling.

## Testing scope (functional/NFR/security/AI eval)

Functional scope:

- Correct phase/artifact routing and stop-rule behavior.
- Correct enforcement of documentation acceptance gates.
- Correct traceability capture for decisions, reviews, and updates.

Non-functional scope:

- Consistency and repeatability of outputs across repeated workflow runs.
- Token-efficiency awareness in workflow execution and review passes.

Security and governance scope:

- Validation that prohibited AI uses are not permitted by process.
- Validation that implementation planning does not begin before documentation acceptance.

AI evaluation scope:

- Practical model evaluation based on real documentation outcomes.
- Comparative review quality for identifying gaps and alignment issues.
- Continuous process improvement using each documentation run as feedback.

Priority conformance scenarios (must run):

- Adapter conformance matrix across Claude, Copilot, Codex, and OpenCode for phase routing, artifact mode behavior, and end-of-phase review dispatch.
- Resumability at phase boundary: interrupted run resumes to the next incomplete phase in one command invocation with no plan-state loss.
- Resumability at artifact boundary: interrupted artifact run resumes to the selected artifact/revisit target in one command invocation with no plan-state loss.
- Resumability after review-before-plan-update boundary: interruption after review does not produce partial plan updates; closure requires one-batch plan write semantics.

## Levels (unit/integration/E2E/UAT)

- Unit: validate discrete rules for document checks and workflow state transitions where tooling code exists.
- Integration: validate interactions between workflow orchestration, validation tooling, and review steps.
- End-to-end: run full documentation workflows on real project docs to confirm start-to-finish behavior.
- UAT/collaborative review: user and agent jointly determine if quality/detail is sufficient, with agent rationale grounded in standards and source docs.

## Environments

- Local environment for iterative authoring and workflow dry runs.
- CI environment for automated quality gates and repeatable checks.
- Repository mainline context for final acceptance decisions based on traceable review evidence.

## Tools

Automated quality tools and checks include:

- Markdown lint checks.
- Documentation schema/frontmatter validation.
- Link checks.
- Cross-document consistency checks.
- Scripted review-agent checks.

Manual validation tools include:

- Human review of AI findings and proposed document updates.
- Standards-based judgment on documentation sufficiency with explicit rationale.

Baseline verification commands (mandatory):

- `git ls-files '*.md' | xargs -r npx --yes markdownlint-cli2` returns zero markdownlint errors.
- `python3 -m docs_validator.cli <active-doc-paths...>` returns zero validation errors for active artifacts in scope.
- `python3 scripts/check-init-parity.py` exits successfully.
- `lychee --config lychee.toml --offline --no-progress './**/*.md'` reports zero broken offline-checkable links.

## Entry/exit criteria

Entry criteria:

- Active templates and phase rubrics are available.
- Workflow scope and acceptance expectations are defined.
- Validation tooling commands are runnable in local/CI contexts.

Exit criteria:

- All required automated checks pass with no blocking errors.
- Review-agent checks run and no unresolved critical or important findings remain.
- Documentation changes are traceable and reviewed.
- Documentation workflow is fully documented end-to-end and accepted as sufficient to begin implementation planning.
- Priority conformance scenarios complete with pass outcomes recorded in review evidence.

## Quality gates

Before PR merge:

- Full documentation validation passes.
- Cross-document consistency checks pass.
- No unresolved critical or important findings are allowed.
- Main branch receives only standards-compliant, current-best documentation versions.

Before implementation planning:

- Documentation for the entire docs-creation workflow exists from start to finish.
- Traceability is present for key decisions, edits, and review outcomes.
- Documentation is accepted as complete and aligned by human reviewer with AI-assisted validation.

## Difficult/expensive testing areas and mitigations

Difficult area:

- Extensive AI-agent evaluation can be costly.

Mitigations:

- Use risk-based sampling for expensive agent runs.
- Run low-cost deterministic checks first; reserve agent-heavy checks for targeted gaps.
- Reuse structured context and constrain review scope to reduce token spend.
- Track model-performance-to-cost trade-offs and prioritize models that deliver adequate review quality per token.

## Defect-management cross-link

Defects and quality findings should be tracked and resolved with severity awareness before closure of gated workflow steps. High-severity defects block merge or phase completion until resolved or explicitly accepted as conditional risk by the designated approver.

## Related documents

- [Product Requirements Document](../02_product/01_prd.md)
- [User Journeys](../02_product/03_user_journeys.md)
- [Solution Design](../03_architecture/01_solution_design.md)
- [AI Use Policy](../04_ai_governance/01_ai_use_policy.md)
- [Project Initialization Plan](../superpowers/plans/2026-05-08-project-initialization.md)

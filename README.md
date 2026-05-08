# project--orchestrator

project--orchestrator is an internal initiative to guide teams through creating comprehensive, review-ready project documentation using this repository's documentation model and templates.

The core principle is simple: decisions about purpose, scope, and architecture belong in active documents before code is written.

## Goals

- Guide teams through capturing project intent, scope, requirements, architecture, and governance in canonical docs before implementation.
- Enforce a decision-complete documentation standard with explicit review gates and traceable evidence.
- Reduce rework by removing ambiguity about what must be documented and accepted before implementation planning starts.
- Provide one resumable initialization workflow that supports both first-pass execution and targeted revisits.

## What this project provides

| Asset | Description |
| --- | --- |
| `/init` command | The orchestration entrypoint that runs the seven-phase documentation workflow and supports resumable progress and revisits. |
| Documentation tree (`docs/`) | A structured, role-tagged documentation system with templates covering governance, strategy, product, architecture, testing, delivery, and operations. |
| AI agent integration | Tracked assistant-native assets for Claude, Copilot, Codex, and OpenCode with interoperable workflow semantics. |
| Governance baseline | ADR system, frontmatter validator, markdown linting, and link checking included and wired to CI. |
| Lifecycle templates | Dozens of `_TEMPLATE.md` starters across every project artifact type, with worked examples and role-based reading paths. |

More agentic tooling is in development — the roadmap includes commands that handle common cross-cutting tasks without manual coordination.

## Initialization workflow

The repository uses a seven-phase workflow before implementation begins. The user runs `/init` to start, continue, or revisit work. State is tracked in `docs/superpowers/plans/YYYY-MM-DD-project-initialization.md`.

`/init` routes into these phases:

| Phase | Routed target | Output |
| --- | --- | --- |
| 0 | `project-initialization/phases/0-triage.md` | plan file in `docs/superpowers/plans/` |
| 1 | `project-initialization/phases/1-intent.md` | `docs/00_governance/00_project_brief.md` and optional `01_business_case.md` |
| 2 | `project-initialization/phases/2-specification.md` | active specification artifacts |
| 3 | `project-initialization/phases/3-design.md` | `docs/03_architecture/01_solution_design.md`, ADRs, optional C4 views |
| 4 | `project-initialization/phases/4-govern-operate.md` | govern and operate artifacts per profile |
| 5 | `project-initialization/phases/5-adapt.md` | language-specific scaffold and repository sync updates |
| 6 | `project-initialization/phases/6-review.md` | final review pass and completed plan |

## Get started

Run `/init` in Claude Code, GitHub Copilot Chat, Codex, or any AI tool that supports per-project slash commands:

1. Run `/init` to continue from the next incomplete phase in the active plan.
2. Use `/init <phase-or-artifact-name>` to revisit a completed phase or artifact.
3. Keep machine-specific overrides local-only. The assistant directories `.claude/`, `.copilot/`, `.codex/`, and `.opencode/` are tracked assets; only local machine overrides should stay untracked.

`/init` behavior at a glance:

- Starts triage if no plan exists.
- Shows a status block and resumes the next phase when initialization is in progress.
- Supports direct jumps with `/init <phase-or-artifact-name>`.

See [`project-initialization/README.md`](project-initialization/README.md) for the full phase catalog and shared contract.

## Top-level layout

| Path | Purpose |
| --- | --- |
| `src/` | Implementation code and reusable modules. |
| `tests/` | Automated verification, ideally mirroring `src/` by scope. |
| `config/` | Environment, runtime, and deployment configuration templates. |
| `scripts/` | Maintainer automation for development, CI, release, and migration tasks. |
| `bin/` | Thin user-facing entrypoints or wrappers for runtime commands. |
| `tools/` | Repository-maintained utilities such as documentation validators and maintenance helpers. |
| `examples/` | Copyable examples for implemented features only. |
| `diagrams/` | Source diagrams that support active architecture docs and ADRs. |
| `.agents/` | Repo-native Codex skill discovery surface. |
| `.claude/` | Tracked Claude Code skills, hooks, and repo-local defaults. |
| `.copilot/` | Tracked Copilot-oriented Superpowers assets kept in parity with other harnesses. |
| `.codex/` | Tracked Codex hook wiring and vendored Superpowers mirror assets. |
| `.opencode/` | Tracked OpenCode skills and plugin bootstrap assets. |
| `project-initialization/` | Phase orchestration content, artifact rubrics, and profiles for the init workflow. |
| `docs/` | Canonical documentation tree and governance structure. |

## Documentation model

- `docs/README.md`, `docs/Architecture.md`, `docs/00-documentation-standards.md`, `docs/00-source-of-truth.md`, and `docs/INDEX.md` form the control spine, the source of truth for how documentation is structured in this project.
- `docs/adr/` holds durable architecture and implementation decisions.
- `docs/superpowers/` holds dated specs and plans as historical working records, not canonical guidance.
- `docs/99_archive/` is for retired material, not active guidance.
- `tools/docs_validator/` holds the Python frontmatter validator used by docs-focused local checks and GitHub workflows.

## Assistant-native tooling

The repository ships tracked assistant-native assets in `.claude/`, `.copilot/`, `.codex/`, and `.opencode/`. Each directory contains skills, hooks, and context files that keep assistants aligned to the same workflow contract.

The `/init` command is the primary orchestration surface for documentation initialization and revisit operations.

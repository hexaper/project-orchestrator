# Universal Repository Template

A documentation-first project template with custom agentic tooling for a structured, repeatable path from blank repository to implementation-ready state.

The core principle is simple: decisions about purpose, scope, and architecture belong in active documents *before* code is written. This template creates that structure upfront — giving your codebase, docs, and AI agent context a shared foundation from day one.

## Goals

- Provide a clean, consistent engineering scaffold that any project can adopt without reinventing its structure.
- Establish a comprehensive documentation tree that AI agents can read and act on throughout the project lifecycle.
- Remove the "how should this project be organized?" question before the first commit.
- Deliver a single-command initialization workflow that adapts to any project type, from solo experiments to team products.

## What this template gives you today

| Asset | Description |
| --- | --- |
| `/init` command | A custom agentic tool that walks you through seven initialization phases. One command, fully resumable at any point. |
| Documentation tree (`docs/`) | A structured, role-tagged documentation system with templates covering governance, strategy, product, architecture, testing, delivery, and operations. |
| AI agent integration | Tracked assistant-native assets for Claude, Copilot, Codex, and OpenCode — so your AI tool has the right context from the start. |
| Governance baseline | ADR system, frontmatter validator, markdown linting, and link checking included and wired to CI. |
| Lifecycle templates | Dozens of `_TEMPLATE.md` starters across every project artifact type, with worked examples and role-based reading paths. |

More agentic tooling is in development — the roadmap includes commands that handle common cross-cutting tasks without manual coordination.

## Initialization workflow

A new project goes through seven structured phases before implementation begins. The user only needs to remember one command: `/init`.

```text
Clone
  │
  ▼
/init
  Starts Phase 0 (Triage) if no plan exists.
  Otherwise shows status, resumes the next phase,
  or lets the user revisit a completed phase or artifact.
  State lives in docs/superpowers/plans/YYYY-MM-DD-project-initialization.md
```

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

1. Clone this repository.
2. Run `/init` to start Phase 0 (Triage) and generate your initialization plan.
3. Run `/init` again to continue — it resumes the next incomplete phase automatically.
4. Use `/init <phase-or-artifact-name>` to revisit any completed phase or artifact.
5. Replace the placeholder [`LICENSE`](LICENSE) with your chosen license before publishing.
6. Keep machine-specific overrides local-only. The assistant directories `.claude/`, `.copilot/`, `.codex/`, and `.opencode/` are tracked template assets; only `settings.local.json` and similar machine-specific files should stay untracked.
7. Commit the bootstrap state as one or two clean commits before starting feature work.

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

The template ships tracked assistant-native assets in `.claude/`, `.copilot/`, `.codex/`, and `.opencode/`. Each directory contains the skills, hooks, and context files that give the corresponding AI tool a working understanding of this project's conventions without manual setup.

The `/init` command is the first of these agentic tools. Additional tools covering common cross-cutting development tasks are planned for future releases.

# Contributing

## Workflow

- Work in small, reviewable increments.
- Keep changes scoped to approved requirements.
- Update documentation in the same change when behavior or policy changes.

## Change process by scope

Calibrate the process to the change size. Heavier changes need heavier records.

### Trivial changes

Typo fixes, link repairs, copy edits, and other documentation polish.

- A clear PR description is sufficient.
- No ADR, spec, or plan required.

### Substantive changes

New features, refactors, structural moves, or behavior changes that are not durable architecture decisions.

- Create or update a spec in `docs/superpowers/specs/` describing intent and acceptance.
- Create or update a plan in `docs/superpowers/plans/` describing the steps.
- Link both from the PR description.
- Run verification relevant to the change and record outcomes.

### Durable decisions

Architecture, security, governance, contract, or policy changes that should be discoverable later.

- Update or add an ADR in `docs/adr/` _before_ implementation begins.
- Follow the substantive-change steps above for the implementation work that follows.
- Link the ADR from the PR description.

A planning workflow such as Superpowers can be used to drive substantive and durable changes, but it is not required by this template.

## Local development setup

### Pre-commit hooks

The repository ships a `.pre-commit-config.yaml` that auto-fixes Markdown lint
issues before every commit and reports frontmatter and link errors immediately.

```bash
pip install pre-commit
pre-commit install
```

**Hook requirements** (system-level, installed once):

| Hook | Requirement |
|------|-------------|
| `markdownlint-fix` | Node.js (hook installs `markdownlint-cli2` automatically) |
| `lychee-offline` | `lychee` on PATH — see <https://lychee.cli.rs> |
| `docs-validator` | `pip install -e ./tools/docs_validator` |

The `markdownlint-fix` hook auto-fixes staged files. The other two hooks are
detection-only; they print errors so you can fix them before the commit lands.

- Include a concise rationale and impact summary.
- Link changed ADR, spec, or plan docs.
- Keep branch protections and required checks intact.

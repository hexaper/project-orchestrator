# Copilot repository instructions

Read [`AGENTS.md`](../AGENTS.md) before any non-trivial work. It defines pre-work checks, ADR rules, global workflow, and the routing map for all subdirectory `AGENTS.md` files.

## Initialization

This repository is an unspecialized template. Run `/init` to start Phase 0 (Triage). See [`project-initialization/README.md`](../project-initialization/README.md) for the full phase catalog and [`project-initialization/contract.md`](../project-initialization/contract.md) for per-run execution rules. Initialization state lives in `docs/superpowers/plans/YYYY-MM-DD-project-initialization.md`.

## Local verification commands

```bash
# Markdown lint (tracked files only)
git ls-files '*.md' | xargs -r npx --yes markdownlint-cli2

# Documentation frontmatter validation
python -m pip install -e "./tools/docs_validator[dev]"
python -m docs_validator.cli <doc-paths...>

# Init workflow parity check
python3 scripts/check-init-parity.py

# Link checking (offline)
lychee --config lychee.toml --offline --no-progress './**/*.md'
```

## Documentation frontmatter

All `docs/` files require these frontmatter fields: `title`, `status`, `record_class`, `audience`, `owner`, `capability`. Full schema and allowed values: [`docs/00_operating_model/04_frontmatter_schema.md`](../docs/00_operating_model/04_frontmatter_schema.md).

## Asset directories

- `.copilot/commands/init.md` — consolidated `/init` command; keep in parity with `.claude/`, `.codex/`, `.opencode/`
- `.copilot/skills/` — vendored Superpowers 5.1.0 skills; only edit when updating the vendor version across all assistant directories
- Shared workflow guidance belongs in root docs first; sync assistant-specific notes afterward

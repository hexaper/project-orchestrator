# scripts

Purpose: Operational automation scripts used by maintainers.

## Available scripts

### `bump-last-reviewed.py`

Bumps the `last_reviewed` frontmatter field to today's date in one or more
Markdown files.

```bash
# Update a single file:
python scripts/bump-last-reviewed.py docs/README.md

# Update all docs in a directory:
python scripts/bump-last-reviewed.py docs/

# Preview changes without writing (dry-run):
python scripts/bump-last-reviewed.py --dry-run docs/
```

Run this after reviewing a document to keep the `last_reviewed` date current.
It skips files that lack a `last_reviewed` field.

### `check-init-parity.py`

Validates that the consolidated init workflow and bootstrap wiring exist across
all tracked tool surfaces (`.claude`, `.copilot`, `.codex`, `.opencode`). Run
from the repo root.

```bash
python scripts/check-init-parity.py
```

## Recommended categories for future scripts

- `scripts/dev/` for local development helpers
- `scripts/ci/` for verification and CI entrypoints
- `scripts/release/` for packaging, release, or deployment automation
- `scripts/migrate/` for one-off or repeatable data/schema migrations

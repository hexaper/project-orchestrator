#!/usr/bin/env python3
"""Bump the last_reviewed date in Markdown frontmatter to today.

Usage:
    python scripts/bump-last-reviewed.py <file_or_directory> [...]

Examples:
    # Update a single file:
    python scripts/bump-last-reviewed.py docs/README.md

    # Update all docs in a directory:
    python scripts/bump-last-reviewed.py docs/

    # Update several specific files:
    python scripts/bump-last-reviewed.py docs/INDEX.md docs/Architecture.md

The script only modifies files that already have a last_reviewed field in their
YAML frontmatter. Files without frontmatter or without a last_reviewed field
are skipped with a warning.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
LAST_REVIEWED_RE = re.compile(r"^(last_reviewed:\s*)(.+)$", re.MULTILINE)

# Mirrors the skip list used by docs_validator CLI so behaviour is consistent.
SKIP_DIRECTORIES = {".git", "node_modules", ".venv", "__pycache__", "dist", "build"}
# AGENTS.md files contain agent instructions, not canonical docs; skip them.
SKIP_FILENAMES = {"AGENTS.md"}


def discover_markdown(paths: list[str]) -> list[Path]:
    files: list[Path] = []
    seen: set[Path] = set()

    for raw_path in paths:
        path = Path(raw_path)
        if path.is_file() and path.suffix == ".md":
            if path.name in SKIP_FILENAMES:
                continue
            resolved = path.resolve()
            if resolved not in seen:
                seen.add(resolved)
                files.append(path)
            continue

        if not path.is_dir():
            print(f"warning: {raw_path}: not a file or directory — skipping", file=sys.stderr)
            continue

        for candidate in sorted(path.rglob("*.md")):
            if any(part in SKIP_DIRECTORIES for part in candidate.parts):
                continue
            if candidate.name in SKIP_FILENAMES:
                continue
            resolved = candidate.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            files.append(candidate)

    return files


def bump_file(path: Path, today: date) -> bool:
    """Return True if the file was updated, False if skipped."""
    raw = path.read_text(encoding="utf-8")

    fm_match = FRONTMATTER_RE.match(raw)
    if not fm_match:
        print(f"warning: {path}: no frontmatter block — skipping", file=sys.stderr)
        return False

    fm_block = fm_match.group(0)
    if "last_reviewed" not in fm_block:
        print(f"warning: {path}: no last_reviewed field — skipping", file=sys.stderr)
        return False

    today_str = today.isoformat()
    new_fm = LAST_REVIEWED_RE.sub(rf"\g<1>{today_str}", fm_block)

    if new_fm == fm_block:
        # Date is already today.
        print(f"{path}: already up to date ({today_str})")
        return False

    new_content = raw.replace(fm_block, new_fm, 1)
    path.write_text(new_content, encoding="utf-8")
    print(f"{path}: updated last_reviewed → {today_str}")
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="bump-last-reviewed",
        description="Bump last_reviewed frontmatter to today in Markdown files.",
    )
    parser.add_argument(
        "paths",
        nargs="+",
        help="Markdown files or directories to update",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change without writing files",
    )
    args = parser.parse_args(argv)

    today = date.today()
    files = discover_markdown(args.paths)

    if not files:
        print("No Markdown files found.")
        return 0

    updated = 0
    for file_path in files:
        if args.dry_run:
            raw = file_path.read_text(encoding="utf-8")
            fm_match = FRONTMATTER_RE.match(raw)
            if fm_match and "last_reviewed" in fm_match.group(0):
                print(f"{file_path}: would update last_reviewed → {today.isoformat()}")
                updated += 1
        else:
            if bump_file(file_path, today):
                updated += 1

    action = "would update" if args.dry_run else "updated"
    print(f"\nDone: {action} {updated} of {len(files)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

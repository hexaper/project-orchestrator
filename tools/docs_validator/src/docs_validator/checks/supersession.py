"""Supersession link validation."""
from __future__ import annotations

from pathlib import Path

from docs_validator.parser import ParseResult


def check_supersession_links(parsed: list[ParseResult], root: Path) -> list[str]:
    errors: list[str] = []

    for result in parsed:
        target = result.frontmatter.superseded_by
        if not target:
            continue

        candidate = (result.path.parent / target).resolve()
        fallback = (root / target).resolve()
        if candidate.exists() or fallback.exists():
            continue

        errors.append(
            f"{result.path.name}: superseded_by target not found: {target}"
        )

    return errors

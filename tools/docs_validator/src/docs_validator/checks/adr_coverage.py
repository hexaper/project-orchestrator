"""ADR coverage scanning."""
from __future__ import annotations

from pathlib import Path


def find_orphan_adrs(root: Path, adr_dir: Path) -> list[Path]:
    if not adr_dir.exists():
        return []

    markdown_files = [
        path for path in root.rglob("*.md") if path.is_file() and path.parent != adr_dir
    ]
    contents = [path.read_text(encoding="utf-8") for path in markdown_files]

    orphans: list[Path] = []
    for adr_path in sorted(adr_dir.glob("*.md")):
        relative_to_root = adr_path.relative_to(root).as_posix()
        relative_to_parent = adr_path.relative_to(adr_dir.parent).as_posix()
        if any(
            relative_to_root in content or relative_to_parent in content
            for content in contents
        ):
            continue
        orphans.append(adr_path)

    return orphans

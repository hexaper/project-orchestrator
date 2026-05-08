"""Tests for ADR coverage scanning."""
from pathlib import Path

from docs_validator.checks.adr_coverage import find_orphan_adrs


def test_find_orphan_adrs_returns_unreferenced_adr_files(tmp_path):
    docs_root = tmp_path / "docs"
    adr_dir = docs_root / "adr"
    adr_dir.mkdir(parents=True)

    referenced = adr_dir / "ADR-001-first.md"
    referenced.write_text("# ADR 1\n", encoding="utf-8")
    orphan = adr_dir / "ADR-002-second.md"
    orphan.write_text("# ADR 2\n", encoding="utf-8")

    (docs_root / "README.md").write_text(
        "[Decision](adr/ADR-001-first.md)\n",
        encoding="utf-8",
    )

    orphans = find_orphan_adrs(docs_root, adr_dir)

    assert orphans == [orphan]


def test_find_orphan_adrs_returns_empty_when_no_adr_directory(tmp_path):
    docs_root = tmp_path / "docs"
    docs_root.mkdir()

    assert find_orphan_adrs(docs_root, docs_root / "adr") == []

"""CLI integration tests for docs-validator."""
from pathlib import Path

from docs_validator.cli import main


FIXTURES = Path(__file__).parent / "fixtures"


def test_cli_exits_zero_on_valid_file(capsys):
    exit_code = main([str(FIXTURES / "valid.md")])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert "checked 1 file(s); 0 error(s)" in captured.out


def test_cli_exits_one_on_schema_invalid_file(capsys):
    exit_code = main([str(FIXTURES / "invalid_missing_audience.md")])

    captured = capsys.readouterr()
    assert exit_code == 1
    assert "invalid_missing_audience.md" in captured.err
    assert "audience" in captured.err
    assert "checked 1 file(s); 1 error(s)" in captured.out


def test_cli_exits_one_on_missing_frontmatter(capsys):
    exit_code = main([str(FIXTURES / "no_frontmatter.md")])

    captured = capsys.readouterr()
    assert exit_code == 1
    assert "no frontmatter block found" in captured.err


def test_cli_recurses_directories_and_reports_multiple_errors(capsys):
    exit_code = main([str(FIXTURES)])

    captured = capsys.readouterr()
    assert exit_code == 1
    assert "checked 7 file(s); 4 error(s)" in captured.out
    assert "invalid_missing_audience.md" in captured.err
    assert "malformed_yaml.md" in captured.err
    assert "no_frontmatter.md" in captured.err
    assert "superseded_dangling.md" in captured.err


def test_cli_strict_staleness_turns_warning_into_error(tmp_path, capsys):
    stale_file = tmp_path / "stale.md"
    stale_file.write_text(
        """---
title: Stale Fixture
status: active
record_class: canonical
audience: [internal]
owner: Docs
capability: governance
cadence: weekly
last_reviewed: 2024-01-01
---

# Stale Fixture
""",
        encoding="utf-8",
    )

    exit_code = main(["--strict-staleness", str(stale_file)])

    captured = capsys.readouterr()
    assert exit_code == 1
    assert "stale.md" in captured.err
    assert "stale" in captured.err


def test_cli_ignores_agents_routing_files(tmp_path, capsys):
    agents_file = tmp_path / "AGENTS.md"
    agents_file.write_text(
        """---
name: Test Routing Rules
description: Not a canonical docs artifact.
applyTo: \"docs/**\"
---

# Test Routing Rules
""",
        encoding="utf-8",
    )

    valid_file = tmp_path / "valid.md"
    valid_file.write_text(
        """---
title: Valid Fixture
status: active
record_class: canonical
audience: [internal]
owner: Docs
capability: governance
---

# Valid Fixture
""",
        encoding="utf-8",
    )

    exit_code = main([str(tmp_path)])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert "checked 1 file(s); 0 error(s)" in captured.out
    assert "AGENTS.md" not in captured.err

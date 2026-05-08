"""Tests for supersession link checks."""
from pathlib import Path

from docs_validator.checks.supersession import check_supersession_links
from docs_validator.parser import parse_file


FIXTURES = Path(__file__).parent / "fixtures"


def test_superseded_by_resolves_relative_to_document_directory():
    parsed = [parse_file(FIXTURES / "superseded_ok.md")]

    errors = check_supersession_links(parsed, FIXTURES)

    assert errors == []


def test_superseded_by_reports_missing_target():
    parsed = [parse_file(FIXTURES / "superseded_dangling.md")]

    errors = check_supersession_links(parsed, FIXTURES)

    assert len(errors) == 1
    assert "superseded_dangling.md" in errors[0]
    assert "missing-replacement.md" in errors[0]

"""Tests for Markdown frontmatter parsing."""
from pathlib import Path

import pytest

from docs_validator.parser import (
    MalformedFrontmatterError,
    NoFrontmatterError,
    parse_file,
)


FIXTURES = Path(__file__).parent / "fixtures"


def test_parse_file_returns_metadata_and_body():
    result = parse_file(FIXTURES / "valid.md")

    assert result.path == FIXTURES / "valid.md"
    assert result.frontmatter.title == "Valid Fixture"
    assert "Fixture body" in result.body


def test_parse_file_without_frontmatter_raises_error():
    with pytest.raises(NoFrontmatterError):
        parse_file(FIXTURES / "no_frontmatter.md")


def test_parse_file_with_malformed_yaml_raises_error():
    with pytest.raises(MalformedFrontmatterError):
        parse_file(FIXTURES / "malformed_yaml.md")


def test_parse_file_missing_path_raises_file_not_found():
    with pytest.raises(FileNotFoundError):
        parse_file(FIXTURES / "missing.md")

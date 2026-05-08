"""Markdown frontmatter parsing helpers."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import frontmatter
from pydantic import ValidationError
from yaml.error import YAMLError

from docs_validator.schema import Frontmatter


class ParserError(Exception):
    """Base parser error."""


class NoFrontmatterError(ParserError):
    """Raised when a Markdown file lacks a frontmatter block."""


class MalformedFrontmatterError(ParserError):
    """Raised when YAML frontmatter cannot be parsed."""


@dataclass(slots=True)
class ParseResult:
    path: Path
    frontmatter: Frontmatter
    body: str


def parse_file(path: str | Path) -> ParseResult:
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(file_path)

    raw = file_path.read_text(encoding="utf-8")
    if not raw.startswith("---\n") and raw != "---":
        raise NoFrontmatterError("no frontmatter block found")

    try:
        post = frontmatter.loads(raw)
    except YAMLError as exc:
        raise MalformedFrontmatterError(str(exc)) from exc

    if not post.metadata:
        raise NoFrontmatterError("no frontmatter block found")

    try:
        metadata = Frontmatter.model_validate(post.metadata)
    except ValidationError:
        raise

    return ParseResult(path=file_path, frontmatter=metadata, body=post.content)

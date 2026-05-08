"""CLI entry point for docs-validator."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from pydantic import ValidationError

from docs_validator.checks.adr_coverage import find_orphan_adrs
from docs_validator.checks.staleness import find_stale
from docs_validator.checks.supersession import check_supersession_links
from docs_validator.parser import (
    MalformedFrontmatterError,
    NoFrontmatterError,
    ParseResult,
    parse_file,
)


SKIP_DIRECTORIES = {".git", "node_modules", ".venv", "__pycache__", "dist", "build"}
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


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="docs-validator")
    parser.add_argument("paths", nargs="+", help="Markdown files or directories to validate")
    parser.add_argument(
        "--strict-staleness",
        action="store_true",
        help="Treat stale review warnings as validation errors",
    )
    return parser


def determine_root(discovered_files: list[Path], original_paths: list[str]) -> Path:
    directory_inputs = [Path(path) for path in original_paths if Path(path).is_dir()]
    if directory_inputs:
        return directory_inputs[0]
    if not discovered_files:
        return Path.cwd()
    return discovered_files[0].parent


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    files = discover_markdown(args.paths)
    root = determine_root(files, args.paths)

    errors: list[str] = []
    warnings: list[str] = []
    parsed: list[ParseResult] = []

    for file_path in files:
        try:
            parsed.append(parse_file(file_path))
        except FileNotFoundError:
            errors.append(f"{file_path}: file not found")
        except NoFrontmatterError as exc:
            errors.append(f"{file_path}: {exc}")
        except MalformedFrontmatterError as exc:
            errors.append(f"{file_path}: malformed frontmatter: {exc}")
        except ValidationError as exc:
            errors.append(f"{file_path}: {exc}")

    errors.extend(check_supersession_links(parsed, root))

    stale_messages = find_stale(parsed)
    if args.strict_staleness:
        errors.extend(stale_messages)
    else:
        warnings.extend(stale_messages)

    adr_dir = root / "adr"
    for orphan in find_orphan_adrs(root, adr_dir):
        warnings.append(f"{orphan.name}: ADR is not referenced by any other Markdown file")

    for message in errors:
        print(message, file=sys.stderr)
    for message in warnings:
        print(f"warning: {message}", file=sys.stderr)

    print(f"checked {len(files)} file(s); {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

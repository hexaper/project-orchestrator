"""Tests for document staleness checks."""
from datetime import date
from pathlib import Path

from docs_validator.checks.staleness import find_stale, is_stale
from docs_validator.parser import parse_file


FIXTURES = Path(__file__).parent / "fixtures"


def test_weekly_documents_become_stale_after_fourteen_days():
    assert is_stale("weekly", date(2026, 5, 1), today=date(2026, 5, 16)) is True
    assert is_stale("weekly", date(2026, 5, 1), today=date(2026, 5, 14)) is False


def test_monthly_documents_become_stale_after_sixty_days():
    assert is_stale("monthly", date(2026, 1, 1), today=date(2026, 3, 3)) is True
    assert is_stale("monthly", date(2026, 1, 1), today=date(2026, 2, 15)) is False


def test_per_release_and_one_shot_are_not_time_based():
    assert is_stale("per-release", date(2024, 1, 1), today=date(2026, 5, 7)) is False
    assert is_stale("one-shot", date(2024, 1, 1), today=date(2026, 5, 7)) is False


def test_find_stale_returns_readable_messages(tmp_path):
    stale_file = tmp_path / "weekly-status.md"
    stale_file.write_text(
        """---
title: Weekly Status
status: active
record_class: canonical
audience: [internal, manager]
owner: PM
capability: governance
cadence: weekly
last_reviewed: 2026-01-01
---

# Weekly Status
""",
        encoding="utf-8",
    )

    warnings = find_stale([parse_file(stale_file)], today=date(2026, 2, 1))

    assert len(warnings) == 1
    assert "weekly-status.md" in warnings[0]
    assert "weekly" in warnings[0]

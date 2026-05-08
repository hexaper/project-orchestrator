"""Document staleness checks."""
from __future__ import annotations

from datetime import date

from docs_validator.parser import ParseResult


STALE_THRESHOLDS = {
    "weekly": 14,
    "monthly": 60,
    "per-stage": 90,
    "ad-hoc": 365,
}


def is_stale(cadence: str, last_reviewed: date, *, today: date | None = None) -> bool:
    current_day = today or date.today()
    threshold = STALE_THRESHOLDS.get(cadence)
    if threshold is None:
        return False
    return (current_day - last_reviewed).days > threshold


def find_stale(
    parsed: list[ParseResult], *, today: date | None = None
) -> list[str]:
    warnings: list[str] = []

    for result in parsed:
        cadence = result.frontmatter.cadence
        last_reviewed = result.frontmatter.last_reviewed
        if not cadence or not last_reviewed:
            continue
        if not is_stale(cadence.value, last_reviewed, today=today):
            continue

        warnings.append(
            f"{result.path.name}: stale for cadence '{cadence.value}' "
            f"(last reviewed {last_reviewed.isoformat()})"
        )

    return warnings

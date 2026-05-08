"""Tests for docs_validator.schema.Frontmatter model."""
from datetime import date

import pytest
from pydantic import ValidationError

from docs_validator.schema import Frontmatter


MINIMAL_VALID = {
    "title": "My Document",
    "status": "draft",
    "record_class": "canonical",
    "audience": ["internal"],
    "owner": "team-a",
    "capability": "governance",
}


def make(**overrides):
    data = {**MINIMAL_VALID, **overrides}
    return data


# ---------------------------------------------------------------------------
# Basic valid / invalid cases
# ---------------------------------------------------------------------------


def test_minimal_valid_frontmatter_parses():
    fm = Frontmatter.model_validate(make())
    assert fm.title == "My Document"
    assert fm.status.value == "draft"


def test_missing_required_field_rejects():
    data = {k: v for k, v in MINIMAL_VALID.items() if k != "audience"}
    with pytest.raises(ValidationError):
        Frontmatter.model_validate(data)


def test_empty_audience_list_rejects():
    with pytest.raises(ValidationError):
        Frontmatter.model_validate(make(audience=[]))


def test_unknown_audience_value_rejects():
    with pytest.raises(ValidationError):
        Frontmatter.model_validate(make(audience=["public"]))


# ---------------------------------------------------------------------------
# Conditional: superseded requires superseded_by
# ---------------------------------------------------------------------------


def test_superseded_requires_superseded_by():
    with pytest.raises(ValidationError) as exc_info:
        Frontmatter.model_validate(make(status="superseded"))
    assert "superseded_by" in str(exc_info.value)


def test_superseded_with_superseded_by_passes():
    fm = Frontmatter.model_validate(make(status="superseded", superseded_by="new.md"))
    assert fm.superseded_by == "new.md"


# ---------------------------------------------------------------------------
# Conditional: execution capability requires cadence and source_of_truth
# ---------------------------------------------------------------------------


def test_execution_capability_requires_cadence_and_source_of_truth():
    with pytest.raises(ValidationError):
        Frontmatter.model_validate(make(capability="execution"))


def test_execution_capability_with_required_fields_passes():
    fm = Frontmatter.model_validate(
        make(capability="execution", cadence="weekly", source_of_truth="repo")
    )
    assert fm.cadence.value == "weekly"
    assert fm.source_of_truth == "repo"


# ---------------------------------------------------------------------------
# Optional fields
# ---------------------------------------------------------------------------


def test_last_reviewed_parses_iso_date():
    fm = Frontmatter.model_validate(make(last_reviewed="2026-05-07"))
    assert fm.last_reviewed == date(2026, 5, 7)


def test_supporting_record_class_works():
    fm = Frontmatter.model_validate(make(record_class="supporting", audience=["internal"]))
    assert fm.record_class.value == "supporting"


# ---------------------------------------------------------------------------
# New capability enum values
# ---------------------------------------------------------------------------


def test_strategy_capability_is_accepted():
    fm = Frontmatter.model_validate(make(capability="strategy"))
    assert fm.capability.value == "strategy"


def test_ai_governance_capability_is_accepted():
    fm = Frontmatter.model_validate(make(capability="ai_governance"))
    assert fm.capability.value == "ai_governance"


# ---------------------------------------------------------------------------
# Extra field rejection
# ---------------------------------------------------------------------------


def test_extra_field_rejected():
    with pytest.raises(ValidationError):
        Frontmatter.model_validate(make(unknown_field="oops"))

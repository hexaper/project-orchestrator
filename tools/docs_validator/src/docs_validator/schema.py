"""Pydantic v2 model for validating Markdown documentation frontmatter."""
from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Any

from pydantic import BaseModel, ConfigDict, field_validator, model_validator


class Status(str, Enum):
    draft = "draft"
    proposed = "proposed"
    accepted = "accepted"
    active = "active"
    superseded = "superseded"
    archived = "archived"


class RecordClass(str, Enum):
    canonical = "canonical"
    supporting = "supporting"
    historical = "historical"


class Audience(str, Enum):
    internal = "internal"
    manager = "manager"
    client = "client"
    end_user = "end_user"
    auditor = "auditor"


class Capability(str, Enum):
    governance = "governance"
    product = "product"
    architecture = "architecture"
    execution = "execution"
    quality = "quality"
    operations = "operations"
    knowledge = "knowledge"
    references = "references"
    user_docs = "user_docs"
    operating_model = "operating_model"
    strategy = "strategy"
    ai_governance = "ai_governance"


class Phase(str, Enum):
    initiation = "initiation"
    planning = "planning"
    execution = "execution"
    monitoring = "monitoring"
    closure = "closure"
    na = "n/a"


class Cadence(str, Enum):
    ad_hoc = "ad-hoc"
    weekly = "weekly"
    monthly = "monthly"
    per_stage = "per-stage"
    per_release = "per-release"
    one_shot = "one-shot"


class Frontmatter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    # Required fields
    title: str
    status: Status
    record_class: RecordClass
    audience: list[Audience]
    owner: str
    capability: Capability

    # Optional fields
    phase: Phase | None = None
    cadence: Cadence | None = None
    last_reviewed: date | None = None
    supersedes: list[str] | None = None
    superseded_by: str | None = None
    source_of_truth: str | None = None
    tags: list[str] | None = None

    @field_validator("title", "owner", mode="before")
    @classmethod
    def non_empty_string(cls, v: Any) -> Any:
        if isinstance(v, str) and not v.strip():
            raise ValueError("must not be empty")
        return v

    @field_validator("audience", mode="before")
    @classmethod
    def coerce_audience_to_list(cls, v: Any) -> Any:
        if isinstance(v, str):
            return [v]
        return v

    @field_validator("audience", mode="after")
    @classmethod
    def audience_non_empty(cls, v: list[Audience]) -> list[Audience]:
        if len(v) < 1:
            raise ValueError("audience must have at least one entry")
        return v

    @model_validator(mode="after")
    def check_conditional_requirements(self) -> "Frontmatter":
        errors: list[str] = []

        if self.status == Status.superseded and not self.superseded_by:
            errors.append(
                "superseded_by is required when status is 'superseded'"
            )

        if self.capability == Capability.execution:
            if not self.cadence:
                errors.append(
                    "cadence is required when capability is 'execution'"
                )
            if not self.source_of_truth:
                errors.append(
                    "source_of_truth is required when capability is 'execution'"
                )

        if errors:
            raise ValueError("; ".join(errors))

        return self

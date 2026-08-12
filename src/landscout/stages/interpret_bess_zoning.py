"""Apply a source-locked, evidence-backed BESS zoning precheck policy."""

from __future__ import annotations

import json
import math
import re
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, replace
from datetime import date, datetime
from hashlib import sha256
from numbers import Integral, Real
from pathlib import Path
from typing import Literal

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
import yaml  # type: ignore[import-untyped]
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, model_validator
from pyproj import CRS
from shapely import to_wkb  # type: ignore[import-untyped]
from shapely.geometry.base import BaseGeometry  # type: ignore[import-untyped]

from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    validate_planning_regulation_index,
)
from landscout.stages.planning_overlay import technical_overlay_tolerance
from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    validate_planning_regulation_structure_with_fragments,
)

__all__ = [
    "BessZoningPolicyConfig",
    "BessZoningPrecheckError",
    "BessZoningPrecheckResult",
    "interpret_bess_zoning",
    "load_bess_zoning_policy_config",
    "validate_bess_zoning_precheck",
]

POLICY_SCHEMA_VERSION = 4
RESULT_HASH_SCHEMA_VERSION = 4
PLANNING_PRECHECK_SCOPE = "WRITTEN_ZONING_REGULATION_ONLY"
REVIEW_SCOPE = "CONFIGURED_USE_CONTROL_ARTICLES_ONLY"

ChapterStatus = Literal[
    "POTENTIALLY_COMPATIBLE",
    "CONDITIONAL_REVIEW",
    "LIKELY_DIFFICULT",
    "UNKNOWN",
]
Confidence = Literal["HIGH", "MEDIUM", "LOW"]
ReviewCompleteness = Literal[
    "COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES", "INCOMPLETE"
]
RouteKind = Literal[
    "DIRECT_ROUTE",
    "CONDITIONAL_ROUTE",
    "RESTRICTION_EXCEPTION_ROUTE",
    "DIFFICULTY_ONLY",
]
EvidenceKind = Literal[
    "USE_PERMISSION",
    "USE_RESTRICTION",
    "PUBLIC_INTEREST_EXCEPTION",
    "TECHNICAL_EQUIPMENT_RULE",
    "ICPE_RULE",
    "RISK_OR_NUISANCE_CONDITION",
    "ACCESS_OR_NETWORK_CONDITION",
    "OTHER_RELEVANT_RULE",
]
EvidenceDirection = Literal[
    "SUPPORTS_POTENTIAL_COMPATIBILITY",
    "SUPPORTS_DIFFICULTY",
    "CONDITION",
    "CONTEXT_ONLY",
]

_CHAPTER_STATUSES = frozenset(
    {"POTENTIALLY_COMPATIBLE", "CONDITIONAL_REVIEW", "LIKELY_DIFFICULT", "UNKNOWN"}
)
_PARCEL_STATUSES = _CHAPTER_STATUSES | {"MIXED_REVIEW_REQUIRED"}
_CONFIDENCES = frozenset({"HIGH", "MEDIUM", "LOW"})
_RESOLVED_MAPPING_STATUSES = frozenset({"EXACT", "CONFIG_ALIAS"})

CHAPTER_POLICY_COLUMNS = (
    "resolved_zone_chapter_label",
    "chapter_section_id",
    "review_completeness",
    "review_scope",
    "reviewed_section_ids",
    "missing_required_section_ids",
    "review_note",
    "zoning_precheck_status",
    "zoning_precheck_confidence",
    "evidence_count",
    "evidence_ids",
    "decision_evidence_ids",
    "context_evidence_ids",
    "rationale",
    "missing_information",
    "planning_precheck_scope",
    "policy_profile",
    "policy_sha256",
    "document_id",
    "archive_sha256",
    "pdf_sha256",
    "index_content_sha256",
    "structure_result_content_sha256",
    "structure_profile",
)
EVIDENCE_CATALOG_COLUMNS = (
    "evidence_id",
    "resolved_zone_chapter_label",
    "section_id",
    "page_number",
    "evidence_kind",
    "evidence_direction",
    "linked_route_ids",
    "linked_route_roles",
    "decision_linked",
    "exact_raw_excerpt",
    "excerpt_sha256",
    "section_page_fragment_sha256",
    "excerpt_start",
    "excerpt_end",
    "source_rule_id",
    "source_rule_excerpt",
    "source_rule_sha256",
    "source_rule_start",
    "source_rule_end",
    "interpretation_note",
    "review_completeness",
    "review_scope",
    "policy_profile",
    "policy_sha256",
    "document_id",
    "archive_sha256",
    "pdf_sha256",
    "index_content_sha256",
    "structure_result_content_sha256",
    "structure_profile",
)
ROUTE_ASSESSMENT_COLUMNS = (
    "route_id",
    "resolved_zone_chapter_label",
    "route_kind",
    "derived_route_status",
    "positive_evidence_ids",
    "condition_evidence_ids",
    "difficulty_evidence_ids",
    "applicability_note",
    "review_completeness",
    "review_scope",
    "policy_profile",
    "policy_sha256",
    "document_id",
    "archive_sha256",
    "pdf_sha256",
    "index_content_sha256",
    "structure_result_content_sha256",
    "structure_profile",
)
EVIDENCE_ROUTE_LINK_COLUMNS = (
    "route_id",
    "resolved_zone_chapter_label",
    "route_kind",
    "evidence_id",
    "route_role",
    "evidence_direction",
    "review_completeness",
    "review_scope",
    "policy_profile",
    "policy_sha256",
    "document_id",
    "archive_sha256",
    "pdf_sha256",
    "index_content_sha256",
    "structure_result_content_sha256",
    "structure_profile",
)
SOURCE_ZONE_POLICY_COLUMNS = (
    "source_zone_label_raw",
    "resolved_zone_chapter_label",
    "mapping_status",
    "matched_section_id",
    "source_layer",
    "zoning_precheck_status",
    "zoning_precheck_confidence",
    "evidence_ids",
    "decision_evidence_ids",
    "context_evidence_ids",
    "review_scope",
    "planning_precheck_scope",
    "policy_profile",
    "policy_sha256",
    "document_id",
    "archive_sha256",
    "pdf_sha256",
    "index_content_sha256",
    "structure_result_content_sha256",
    "structure_profile",
)
PARCEL_ZONE_POLICY_COLUMNS = (
    "parcel_id",
    "planning_zone_id",
    "source_zone_id",
    "source_zone_label_raw",
    "resolved_zone_chapter_label",
    "intersection_area_m2",
    "parcel_share_pct",
    "zoning_precheck_status",
    "zoning_precheck_confidence",
    "evidence_ids",
    "decision_evidence_ids",
    "context_evidence_ids",
    "review_scope",
    "planning_precheck_scope",
    "policy_profile",
    "policy_sha256",
    "document_id",
    "archive_sha256",
    "pdf_sha256",
    "index_content_sha256",
    "structure_result_content_sha256",
    "structure_profile",
    "source_layer",
)
PARCEL_PRECHECK_COLUMNS = (
    "zoning_precheck_status",
    "dominant_zone_precheck_status",
    "dominant_zone_precheck_confidence",
    "positive_area_zone_count",
    "distinct_zone_status_count",
    "non_dominant_different_status_count",
    "touch_only_zone_count",
    "zoning_precheck_evidence_ids",
    "zoning_precheck_context_evidence_ids",
    "zoning_precheck_requires_formal_review",
    "planning_precheck_scope",
    "review_scope",
    "non_zoning_planning_features_interpreted",
    "zoning_precheck_policy_profile",
    "zoning_precheck_policy_sha256",
)


class BessZoningPrecheckError(ValueError):
    """Raised when the preliminary zoning interpretation cannot be proven."""


class _StrictConfigModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class PolicySourceLock(_StrictConfigModel):
    document_id: StrictStr = Field(min_length=1)
    archive_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    pdf_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    index_content_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    structure_result_content_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    structure_profile: StrictStr = Field(min_length=1)


class PolicyEvidence(_StrictConfigModel):
    evidence_id: StrictStr = Field(min_length=1)
    section_id: StrictStr = Field(min_length=1)
    page_number: StrictInt = Field(ge=1)
    evidence_kind: EvidenceKind
    evidence_direction: EvidenceDirection
    exact_raw_excerpt: StrictStr = Field(min_length=1, max_length=600)
    excerpt_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    section_page_fragment_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    excerpt_start: StrictInt = Field(ge=0)
    excerpt_end: StrictInt = Field(ge=1)
    source_rule_id: StrictStr = Field(min_length=1)
    source_rule_excerpt: StrictStr = Field(min_length=1)
    source_rule_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    source_rule_start: StrictInt = Field(ge=0)
    source_rule_end: StrictInt = Field(ge=1)
    interpretation_note: StrictStr = Field(min_length=1)

    @model_validator(mode="after")
    def _validate_exact_strings(self) -> PolicyEvidence:
        for value, label in (
            (self.evidence_id, "evidence ID"),
            (self.section_id, "evidence section ID"),
            (self.exact_raw_excerpt, "exact raw excerpt"),
            (self.source_rule_id, "source rule ID"),
            (self.source_rule_excerpt, "source rule excerpt"),
            (self.interpretation_note, "interpretation note"),
        ):
            _config_string(value, label)
        if sha256(self.exact_raw_excerpt.encode("utf-8")).hexdigest() != self.excerpt_sha256:
            raise ValueError("evidence excerpt SHA256 differs from exact_raw_excerpt")
        if self.excerpt_end <= self.excerpt_start:
            raise ValueError("evidence excerpt offsets must be ordered")
        if sha256(self.source_rule_excerpt.encode("utf-8")).hexdigest() != (
            self.source_rule_sha256
        ):
            raise ValueError("source rule SHA256 differs from source_rule_excerpt")
        if self.source_rule_end <= self.source_rule_start:
            raise ValueError("source rule offsets must be ordered")
        if not (
            self.source_rule_start <= self.excerpt_start
            and self.excerpt_end <= self.source_rule_end
        ):
            raise ValueError("evidence excerpt must lie inside its source rule")
        allowed_directions: dict[str, frozenset[str]] = {
            "USE_PERMISSION": frozenset(
                {"SUPPORTS_POTENTIAL_COMPATIBILITY", "CONTEXT_ONLY"}
            ),
            "USE_RESTRICTION": frozenset({"SUPPORTS_DIFFICULTY", "CONTEXT_ONLY"}),
            "PUBLIC_INTEREST_EXCEPTION": frozenset(
                {
                    "SUPPORTS_POTENTIAL_COMPATIBILITY",
                    "CONDITION",
                    "CONTEXT_ONLY",
                }
            ),
            "TECHNICAL_EQUIPMENT_RULE": frozenset(
                {
                    "SUPPORTS_POTENTIAL_COMPATIBILITY",
                    "SUPPORTS_DIFFICULTY",
                    "CONDITION",
                    "CONTEXT_ONLY",
                }
            ),
            "ICPE_RULE": frozenset(
                {
                    "SUPPORTS_POTENTIAL_COMPATIBILITY",
                    "SUPPORTS_DIFFICULTY",
                    "CONDITION",
                    "CONTEXT_ONLY",
                }
            ),
            "RISK_OR_NUISANCE_CONDITION": frozenset(
                {"SUPPORTS_DIFFICULTY", "CONDITION", "CONTEXT_ONLY"}
            ),
            "ACCESS_OR_NETWORK_CONDITION": frozenset(
                {"SUPPORTS_DIFFICULTY", "CONDITION", "CONTEXT_ONLY"}
            ),
            "OTHER_RELEVANT_RULE": frozenset(
                {"SUPPORTS_DIFFICULTY", "CONDITION", "CONTEXT_ONLY"}
            ),
        }
        allowed = allowed_directions[self.evidence_kind]
        if self.evidence_direction not in allowed:
            raise ValueError("evidence kind and direction are incompatible")
        return self


class RouteAssessment(_StrictConfigModel):
    route_id: StrictStr = Field(min_length=1)
    route_kind: RouteKind
    positive_evidence_ids: tuple[StrictStr, ...] = ()
    condition_evidence_ids: tuple[StrictStr, ...] = ()
    difficulty_evidence_ids: tuple[StrictStr, ...] = ()
    applicability_note: StrictStr = Field(min_length=1)

    @model_validator(mode="after")
    def _validate_route_shape(self) -> RouteAssessment:
        _config_string(self.route_id, "route ID")
        _config_string(self.applicability_note, "route applicability note")
        roles = {
            "positive": self.positive_evidence_ids,
            "condition": self.condition_evidence_ids,
            "difficulty": self.difficulty_evidence_ids,
        }
        combined: list[str] = []
        for role, values in roles.items():
            normalized = [_config_string(value, f"{role} evidence ID") for value in values]
            if len(set(normalized)) != len(normalized):
                raise ValueError(f"{role} evidence IDs must be unique within a route")
            combined.extend(normalized)
        if len(set(combined)) != len(combined):
            raise ValueError("one evidence ID cannot occupy incompatible route roles")
        positive = bool(self.positive_evidence_ids)
        condition = bool(self.condition_evidence_ids)
        difficulty = bool(self.difficulty_evidence_ids)
        expected = {
            "DIRECT_ROUTE": (True, False, False),
            "CONDITIONAL_ROUTE": (True, True, False),
            "RESTRICTION_EXCEPTION_ROUTE": (True, False, True),
            "DIFFICULTY_ONLY": (False, False, True),
        }[self.route_kind]
        if (positive, condition, difficulty) != expected:
            raise ValueError(
                f"{self.route_kind} has incompatible evidence-role membership"
            )
        return self


def _derived_chapter_status(
    review_completeness: ReviewCompleteness,
    routes: Sequence[RouteAssessment],
) -> ChapterStatus:
    if review_completeness == "INCOMPLETE":
        return "UNKNOWN"
    kinds = {route.route_kind for route in routes}
    if kinds.intersection({"CONDITIONAL_ROUTE", "RESTRICTION_EXCEPTION_ROUTE"}):
        return "CONDITIONAL_REVIEW"
    if "DIRECT_ROUTE" in kinds:
        return "UNKNOWN" if "DIFFICULTY_ONLY" in kinds else "POTENTIALLY_COMPATIBLE"
    if "DIFFICULTY_ONLY" in kinds:
        return "LIKELY_DIFFICULT"
    return "UNKNOWN"


class ChapterPolicy(_StrictConfigModel):
    resolved_zone_chapter_label: StrictStr = Field(min_length=1)
    review_completeness: ReviewCompleteness
    reviewed_section_ids: tuple[StrictStr, ...] = ()
    review_note: StrictStr = Field(min_length=1)
    zoning_precheck_status: ChapterStatus
    zoning_precheck_confidence: Confidence
    rationale: StrictStr = Field(min_length=1)
    missing_information: StrictStr = Field(min_length=1)
    evidence: tuple[PolicyEvidence, ...] = ()
    route_assessments: tuple[RouteAssessment, ...] = ()

    @model_validator(mode="after")
    def _validate_evidence_semantics(self) -> ChapterPolicy:
        _config_string(self.resolved_zone_chapter_label, "chapter label")
        _config_string(self.review_note, "chapter review note")
        _config_string(self.rationale, "chapter rationale")
        _config_string(self.missing_information, "chapter missing information")
        reviewed = [
            _config_string(value, "reviewed section ID")
            for value in self.reviewed_section_ids
        ]
        if len(set(reviewed)) != len(reviewed):
            raise ValueError("reviewed section IDs must be unique")
        if self.review_completeness == "INCOMPLETE" and (
            self.zoning_precheck_status != "UNKNOWN"
            or self.zoning_precheck_confidence != "LOW"
        ):
            raise ValueError("incomplete review requires UNKNOWN / LOW")
        route_ids = [route.route_id for route in self.route_assessments]
        if len(set(route_ids)) != len(route_ids):
            raise ValueError("route IDs must be unique within a chapter")
        expected_status = _derived_chapter_status(
            self.review_completeness,
            self.route_assessments,
        )
        if self.zoning_precheck_status != expected_status:
            raise ValueError(
                "declared chapter status differs from coherent linked route assessments"
            )
        return self


class BessZoningPolicyConfig(_StrictConfigModel):
    """Strict source-locked interpretation policy."""

    schema_version: StrictInt
    policy_profile: StrictStr = Field(min_length=1)
    planning_precheck_scope: Literal["WRITTEN_ZONING_REGULATION_ONLY"]
    review_scope: Literal["CONFIGURED_USE_CONTROL_ARTICLES_ONLY"]
    source_lock: PolicySourceLock
    required_zone_article_numbers: tuple[StrictStr, ...] = Field(min_length=1)
    chapters: tuple[ChapterPolicy, ...] = Field(min_length=1)

    @model_validator(mode="after")
    def _validate_policy(self) -> BessZoningPolicyConfig:
        if self.schema_version != POLICY_SCHEMA_VERSION:
            raise ValueError(f"unsupported BESS zoning policy schema: {self.schema_version}")
        _config_string(self.policy_profile, "policy profile")
        _config_string(self.source_lock.document_id, "policy document ID")
        _config_string(self.source_lock.structure_profile, "policy structure profile")
        article_numbers = [
            _config_string(value, "required zone article number")
            for value in self.required_zone_article_numbers
        ]
        if len(set(article_numbers)) != len(article_numbers):
            raise ValueError("required zone article numbers must be unique")
        labels = [chapter.resolved_zone_chapter_label for chapter in self.chapters]
        if len(set(labels)) != len(labels):
            raise ValueError("chapter policy labels must be unique")
        evidence_ids: set[str] = set()
        route_ids: set[str] = set()
        excerpt_directions: dict[tuple[str, int, str, int, int], str] = {}
        source_rules: dict[str, tuple[object, ...]] = {}
        source_rule_occurrences: dict[tuple[object, ...], str] = {}
        source_rule_ranges: dict[tuple[str, int, str], list[tuple[int, int, str]]] = {}
        for chapter in self.chapters:
            chapter_evidence = {
                evidence.evidence_id: evidence for evidence in chapter.evidence
            }
            linked_evidence_ids: set[str] = set()
            for evidence in chapter.evidence:
                if evidence.evidence_id in evidence_ids:
                    raise ValueError("evidence IDs must be globally unique")
                evidence_ids.add(evidence.evidence_id)
                key = (
                    evidence.section_id,
                    evidence.page_number,
                    evidence.section_page_fragment_sha256,
                    evidence.excerpt_start,
                    evidence.excerpt_end,
                )
                previous = excerpt_directions.get(key)
                if previous is not None and previous != evidence.evidence_direction:
                    raise ValueError(
                        "one exact evidence occurrence cannot use contradictory directions"
                    )
                excerpt_directions[key] = evidence.evidence_direction
                rule_identity = (
                    evidence.section_id,
                    evidence.page_number,
                    evidence.section_page_fragment_sha256,
                    evidence.source_rule_start,
                    evidence.source_rule_end,
                    evidence.source_rule_sha256,
                    evidence.source_rule_excerpt,
                )
                prior_rule = source_rules.get(evidence.source_rule_id)
                if prior_rule is not None and prior_rule != rule_identity:
                    raise ValueError(
                        "one source rule ID must resolve to one exact occurrence"
                    )
                source_rules[evidence.source_rule_id] = rule_identity
                occurrence = rule_identity[:5]
                prior_rule_id = source_rule_occurrences.get(occurrence)
                if prior_rule_id is not None and prior_rule_id != evidence.source_rule_id:
                    raise ValueError(
                        "one exact source-rule occurrence must use one source rule ID"
                    )
                source_rule_occurrences[occurrence] = evidence.source_rule_id
                range_key = (
                    evidence.section_id,
                    evidence.page_number,
                    evidence.section_page_fragment_sha256,
                )
                ranges = source_rule_ranges.setdefault(range_key, [])
                current = (
                    evidence.source_rule_start,
                    evidence.source_rule_end,
                    evidence.source_rule_id,
                )
                for start, end, rule_id in ranges:
                    overlaps = max(start, current[0]) < min(end, current[1])
                    identical = start == current[0] and end == current[1]
                    if overlaps and not identical:
                        raise ValueError(
                            f"source rule {evidence.source_rule_id!r} partially overlaps {rule_id!r}"
                        )
                if current not in ranges:
                    ranges.append(current)
            for route in chapter.route_assessments:
                if route.route_id in route_ids:
                    raise ValueError("route IDs must be globally unique")
                route_ids.add(route.route_id)
                roles = (
                    (
                        route.positive_evidence_ids,
                        "SUPPORTS_POTENTIAL_COMPATIBILITY",
                        "positive",
                    ),
                    (route.condition_evidence_ids, "CONDITION", "condition"),
                    (
                        route.difficulty_evidence_ids,
                        "SUPPORTS_DIFFICULTY",
                        "difficulty",
                    ),
                )
                for identifiers, expected_direction, role in roles:
                    for evidence_id in identifiers:
                        referenced_evidence = chapter_evidence.get(evidence_id)
                        if referenced_evidence is None:
                            raise ValueError(
                                f"route references unknown or another-chapter evidence ID {evidence_id!r}"
                            )
                        if referenced_evidence.evidence_direction != expected_direction:
                            raise ValueError(
                                f"route assigns evidence ID {evidence_id!r} to an incompatible {role} role"
                            )
                        linked_evidence_ids.add(evidence_id)
            for evidence in chapter.evidence:
                is_linked = evidence.evidence_id in linked_evidence_ids
                if evidence.evidence_direction == "CONTEXT_ONLY" and is_linked:
                    raise ValueError("CONTEXT_ONLY evidence must not be linked to a route")
                if evidence.evidence_direction != "CONTEXT_ONLY" and not is_linked:
                    raise ValueError(
                        "decision evidence must be linked to at least one route"
                    )
        return self


@dataclass(frozen=True)
class BessZoningPrecheckResult:
    """Immutable envelope around the conservative written-zoning precheck."""

    result_hash_schema_version: int
    policy_schema_version: int
    policy_profile: str
    planning_precheck_scope: str
    review_scope: str
    document_id: str
    archive_sha256: str
    pdf_sha256: str
    index_content_sha256: str
    structure_result_content_sha256: str
    structure_profile: str
    policy_config_sha256: str
    factual_structure_content_sha256: str
    zone_mapping_input_sha256: str
    zoning_relation_hash_columns: tuple[str, ...]
    zoning_relations_input_sha256: str
    evidence_catalog_content_sha256: str
    evidence_route_links_content_sha256: str
    route_assessments_content_sha256: str
    chapter_policy_content_sha256: str
    source_zone_policy_content_sha256: str
    parcel_zone_policy_content_sha256: str
    parcel_output_content_sha256: str
    complete_result_content_sha256: str
    touch_only_relation_count: int
    evidence_catalog: pd.DataFrame
    evidence_route_links: pd.DataFrame
    route_assessments: pd.DataFrame
    chapter_policy: pd.DataFrame
    source_zone_policy: pd.DataFrame
    parcel_zone_interpretations: pd.DataFrame
    parcels: gpd.GeoDataFrame


class _UniqueKeyLoader(yaml.SafeLoader):
    pass


def _construct_unique_mapping(
    loader: yaml.SafeLoader,
    node: yaml.MappingNode,
    deep: bool = False,
) -> dict[object, object]:
    result: dict[object, object] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise BessZoningPrecheckError(f"Duplicate YAML policy key: {key!r}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


_UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_unique_mapping,
)


def _config_string(value: str, label: str) -> str:
    if not value or value != value.strip():
        raise ValueError(f"{label} must be a non-empty exact string")
    return value


def load_bess_zoning_policy_config(path: str | Path) -> BessZoningPolicyConfig:
    """Load a strict policy while rejecting duplicate YAML keys."""

    try:
        payload = yaml.load(Path(path).read_text(encoding="utf-8"), Loader=_UniqueKeyLoader)
        if not isinstance(payload, Mapping):
            raise BessZoningPrecheckError("BESS zoning policy must be a mapping")
        return BessZoningPolicyConfig.model_validate(payload)
    except BessZoningPrecheckError:
        raise
    except Exception as error:
        raise BessZoningPrecheckError("BESS zoning policy is invalid") from error


def _strict_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise BessZoningPrecheckError(f"{label} must be a non-empty exact string")
    return value


def _strict_nonnegative_integer(value: object, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, Integral):
        raise BessZoningPrecheckError(f"{label} must be an integer")
    result = int(value)
    if result < 0:
        raise BessZoningPrecheckError(f"{label} must be non-negative")
    return result


def _strict_positive_integer(value: object, label: str) -> int:
    result = _strict_nonnegative_integer(value, label)
    if result < 1:
        raise BessZoningPrecheckError(f"{label} must be positive")
    return result


def _validated_sha256(value: object, label: str) -> str:
    checksum = _strict_string(value, label)
    if re.fullmatch(r"[0-9a-f]{64}", checksum) is None:
        raise BessZoningPrecheckError(
            f"{label} must be exactly 64 lowercase hexadecimal characters"
        )
    return checksum


def _strict_nonnegative_number(value: object, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise BessZoningPrecheckError(f"{label} must be numeric")
    try:
        result = float(value)
    except (TypeError, ValueError, OverflowError) as error:
        raise BessZoningPrecheckError(f"{label} must be finite") from error
    if not math.isfinite(result) or result < 0:
        raise BessZoningPrecheckError(f"{label} must be finite and non-negative")
    return result


def _canonical_value(value: object) -> object:
    if value is None or value is pd.NA:
        return None
    if isinstance(value, np.generic):
        return _canonical_value(value.item())
    if isinstance(value, BaseGeometry):
        return to_wkb(value, hex=True, include_srid=False)
    if isinstance(value, (pd.Timestamp, datetime, date)):
        return value.isoformat()
    if isinstance(value, bytes):
        return value.hex()
    if isinstance(value, (tuple, list, np.ndarray)):
        return [_canonical_value(item) for item in value]
    if isinstance(value, Mapping):
        return {str(key): _canonical_value(item) for key, item in value.items()}
    if isinstance(value, float) and math.isnan(value):
        return None
    if isinstance(value, (str, int, float, bool)):
        return value
    raise BessZoningPrecheckError(
        f"Value of type {type(value).__name__} cannot be canonically serialized"
    )


def _canonical_sha256(value: object) -> str:
    try:
        serialized = json.dumps(
            _canonical_value(value),
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except BessZoningPrecheckError:
        raise
    except Exception as error:
        raise BessZoningPrecheckError("Canonical integrity serialization failed") from error
    return sha256(serialized).hexdigest()


def _frame_payload(frame: pd.DataFrame, columns: Sequence[str]) -> dict[str, object]:
    try:
        if frame.columns.has_duplicates:
            raise BessZoningPrecheckError("DataFrame columns must be unique")
        missing = [column for column in columns if column not in frame.columns]
        if missing:
            raise BessZoningPrecheckError(f"DataFrame is missing columns: {missing}")
        payload: dict[str, object] = {
            "columns": list(columns),
            "index_names": list(frame.index.names),
            "index": [_canonical_value(value) for value in frame.index.tolist()],
            "rows": frame.loc[:, columns].to_dict("records"),
        }
        if isinstance(frame, gpd.GeoDataFrame):
            if frame.crs is None:
                raise BessZoningPrecheckError("GeoDataFrame CRS is required")
            payload["crs"] = CRS.from_user_input(frame.crs).to_json_dict()
            payload["geometry_column"] = frame.geometry.name
        return payload
    except BessZoningPrecheckError:
        raise
    except Exception as error:
        raise BessZoningPrecheckError("DataFrame integrity serialization failed") from error


def _frame_sha256(domain: str, frame: pd.DataFrame, columns: Sequence[str]) -> str:
    return _canonical_sha256({"domain": domain, **_frame_payload(frame, columns)})


def _policy_sha256(config: BessZoningPolicyConfig) -> str:
    return _canonical_sha256(
        {
            "domain": "landscout.bess_zoning.policy_config",
            "config": config.model_dump(mode="json"),
        }
    )


def _factual_structure_sha256(
    structure: PlanningRegulationStructureResult,
) -> str:
    return _canonical_sha256(
        {
            "domain": "landscout.bess_zoning.factual_structure_input",
            "structure_result_content_sha256": structure.structure_result_content_sha256,
            "section_hash_schema_version": structure.section_hash_schema_version,
            "structure_config_sha256": structure.structure_config_sha256,
            "sections_content_sha256": structure.sections_content_sha256,
            "zone_map_content_sha256": structure.zone_map_content_sha256,
            "topic_evidence_content_sha256": structure.topic_evidence_content_sha256,
        }
    )


def _resolved_policy(
    policy: BessZoningPolicyConfig | str | Path,
) -> BessZoningPolicyConfig:
    if isinstance(policy, BessZoningPolicyConfig):
        try:
            return BessZoningPolicyConfig.model_validate(
                policy.model_dump(mode="python")
            )
        except Exception as error:
            raise BessZoningPrecheckError("BESS zoning policy is invalid") from error
    return load_bess_zoning_policy_config(policy)


def _validate_policy_lock(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
) -> None:
    lock = policy.source_lock
    comparisons = (
        (lock.document_id, index.document_id, "document ID"),
        (lock.archive_sha256, index.archive_sha256, "archive SHA256"),
        (lock.pdf_sha256, index.pdf_sha256, "PDF SHA256"),
        (lock.index_content_sha256, index.index_content_sha256, "index SHA256"),
        (
            lock.structure_result_content_sha256,
            structure.structure_result_content_sha256,
            "structure result SHA256",
        ),
        (lock.structure_profile, structure.structure_profile, "structure profile"),
    )
    for actual, expected, label in comparisons:
        if actual != expected:
            raise BessZoningPrecheckError(
                f"BESS zoning policy {label} differs from factual source"
            )


def _exact_id_series(series: pd.Series, label: str, *, unique: bool) -> tuple[str, ...]:
    values: list[str] = []
    for value in series.tolist():
        values.append(_strict_string(value, label))
    if unique and len(set(values)) != len(values):
        raise BessZoningPrecheckError(f"{label} values must be unique")
    return tuple(values)


def _validate_parcels(
    index: PlanningRegulationIndex,
    parcels: gpd.GeoDataFrame,
) -> gpd.GeoDataFrame:
    if not isinstance(parcels, gpd.GeoDataFrame):
        raise BessZoningPrecheckError("parcels must be a GeoDataFrame")
    if parcels.columns.has_duplicates:
        raise BessZoningPrecheckError("Parcel columns must be unique")
    required = {
        "parcel_id",
        "geometry",
        "dominant_planning_zone_id",
        "planning_surface_relation_count",
        "prescription_surface_relation_count",
        "information_surface_relation_count",
        "planning_line_relation_count",
        "planning_point_relation_count",
        "planning_feature_document_id",
        "planning_feature_archive_sha256",
        "planning_document_id",
        "planning_archive_sha256",
    }
    missing = sorted(required.difference(parcels.columns))
    if missing:
        raise BessZoningPrecheckError(f"Parcel input is missing columns: {missing}")
    collisions = sorted(set(PARCEL_PRECHECK_COLUMNS).intersection(parcels.columns))
    if collisions:
        raise BessZoningPrecheckError(
            f"Parcel input already contains precheck columns: {collisions}"
        )
    if parcels.crs is None:
        raise BessZoningPrecheckError("Parcel CRS is required")
    try:
        CRS.from_user_input(parcels.crs)
        if parcels.geometry.name != "geometry":
            raise BessZoningPrecheckError("Parcel geometry must be active")
    except BessZoningPrecheckError:
        raise
    except Exception as error:
        raise BessZoningPrecheckError("Parcel CRS or geometry is invalid") from error
    _exact_id_series(parcels["parcel_id"], "parcel ID", unique=True)
    geometry = parcels.geometry
    if geometry.isna().any() or geometry.is_empty.any() or (~geometry.is_valid).any():
        raise BessZoningPrecheckError(
            "Parcel geometry must be non-null, non-empty, and valid"
        )
    if not geometry.geom_type.isin({"Polygon", "MultiPolygon"}).all():
        raise BessZoningPrecheckError("Parcel geometry must be Polygon or MultiPolygon")
    for column in (
        "planning_surface_relation_count",
        "prescription_surface_relation_count",
        "information_surface_relation_count",
        "planning_line_relation_count",
        "planning_point_relation_count",
    ):
        for value in parcels[column].tolist():
            _strict_nonnegative_integer(value, column)
    for document_column in ("planning_document_id", "planning_feature_document_id"):
        if not parcels[document_column].eq(index.document_id).all():
            raise BessZoningPrecheckError(
                f"Parcel {document_column} lineage differs from the regulation"
            )
    for archive_column in (
        "planning_archive_sha256",
        "planning_feature_archive_sha256",
    ):
        if not parcels[archive_column].eq(index.archive_sha256).all():
            raise BessZoningPrecheckError(
                f"Parcel {archive_column} lineage differs from the regulation"
            )
    return parcels.copy(deep=True)


def _validate_zones(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
) -> pd.DataFrame:
    if not isinstance(zones, pd.DataFrame) or zones.columns.has_duplicates:
        raise BessZoningPrecheckError("zones must be a DataFrame with unique columns")
    required = (
        "planning_zone_id",
        "source_zone_id",
        "zone_label_raw",
        "source_document_id",
        "source_archive_sha256",
        "source_layer",
    )
    missing = [column for column in required if column not in zones.columns]
    if missing:
        raise BessZoningPrecheckError(f"Zone catalog is missing columns: {missing}")
    result = zones.copy(deep=True)
    _exact_id_series(result["planning_zone_id"], "planning zone ID", unique=True)
    _exact_id_series(result["source_zone_id"], "source zone ID", unique=True)
    _exact_id_series(result["zone_label_raw"], "raw zone label", unique=False)
    if not result["source_document_id"].eq(index.document_id).all():
        raise BessZoningPrecheckError("Zone catalog document lineage differs")
    if not result["source_archive_sha256"].eq(index.archive_sha256).all():
        raise BessZoningPrecheckError("Zone catalog archive lineage differs")
    for value in result["source_layer"].tolist():
        _strict_string(value, "zone source layer")
    return result


def _validate_relations(
    index: PlanningRegulationIndex,
    parcels: gpd.GeoDataFrame,
    zones: pd.DataFrame,
    relations: pd.DataFrame,
) -> pd.DataFrame:
    if not isinstance(relations, pd.DataFrame) or relations.columns.has_duplicates:
        raise BessZoningPrecheckError(
            "zoning_intersections must be a DataFrame with unique columns"
        )
    required = (
        "parcel_id",
        "planning_zone_id",
        "source_zone_id",
        "zone_label_raw",
        "relation_type",
        "intersection_area_m2",
        "parcel_metric_area_m2",
        "zone_area_m2",
        "parcel_share_pct",
        "zone_share_pct",
        "source_document_id",
        "source_archive_sha256",
        "source_layer",
    )
    missing = [column for column in required if column not in relations.columns]
    if missing:
        raise BessZoningPrecheckError(f"Zoning relations are missing columns: {missing}")
    result = relations.copy(deep=True)
    if result.duplicated(["parcel_id", "planning_zone_id"]).any():
        raise BessZoningPrecheckError("Parcel/zone relations must be unique")
    parcel_ids = set(_exact_id_series(parcels["parcel_id"], "parcel ID", unique=True))
    if not set(_exact_id_series(result["parcel_id"], "relation parcel ID", unique=False)).issubset(parcel_ids):
        raise BessZoningPrecheckError("Zoning relation references an unknown parcel")
    zone_records = zones.set_index("planning_zone_id")[
        ["source_zone_id", "zone_label_raw", "source_layer"]
    ].to_dict("index")
    for row in result.to_dict("records"):
        planning_id = _strict_string(row["planning_zone_id"], "relation planning zone ID")
        source_id = _strict_string(row["source_zone_id"], "relation source zone ID")
        label = _strict_string(row["zone_label_raw"], "relation raw zone label")
        expected_zone = zone_records.get(planning_id)
        if expected_zone is None:
            raise BessZoningPrecheckError("Zoning relation references an unknown zone")
        if source_id != expected_zone["source_zone_id"] or label != expected_zone["zone_label_raw"]:
            raise BessZoningPrecheckError("Zoning relation zone identity is inconsistent")
        if row["source_layer"] != expected_zone["source_layer"]:
            raise BessZoningPrecheckError("Zoning relation source layer is inconsistent")
        relation_type = _strict_string(row["relation_type"], "zoning relation type")
        area = _strict_nonnegative_number(row["intersection_area_m2"], "intersection area")
        if relation_type == "AREA_OVERLAP" and area <= 0:
            raise BessZoningPrecheckError("AREA_OVERLAP requires positive area")
        if relation_type == "TOUCH_ONLY" and area != 0:
            raise BessZoningPrecheckError("TOUCH_ONLY requires zero area")
        if relation_type not in {"AREA_OVERLAP", "TOUCH_ONLY"}:
            raise BessZoningPrecheckError("Zoning relation type is invalid")
        for upper_column in ("parcel_metric_area_m2", "zone_area_m2"):
            upper = _strict_nonnegative_number(row[upper_column], upper_column)
            if upper <= 0:
                raise BessZoningPrecheckError(
                    f"{upper_column} must be positive for a zoning relation"
                )
            if area - upper > technical_overlay_tolerance(upper):
                raise BessZoningPrecheckError(
                    f"Intersection area exceeds {upper_column}"
                )
        percentage_checks = (
            ("parcel_metric_area_m2", "parcel_share_pct"),
            ("zone_area_m2", "zone_share_pct"),
        )
        for area_column, percentage_column in percentage_checks:
            reference_area = _strict_nonnegative_number(
                row[area_column], area_column
            )
            observed_percentage = _strict_nonnegative_number(
                row[percentage_column], percentage_column
            )
            if reference_area <= 0:
                raise BessZoningPrecheckError(
                    f"{area_column} must be positive for a zoning relation"
                )
            percentage_area = observed_percentage * reference_area / 100.0
            if abs(percentage_area - area) > technical_overlay_tolerance(
                reference_area
            ):
                raise BessZoningPrecheckError(
                    f"{percentage_column} is inconsistent with factual areas"
                )
        if row["source_document_id"] != index.document_id:
            raise BessZoningPrecheckError("Zoning relation document lineage differs")
        if row["source_archive_sha256"] != index.archive_sha256:
            raise BessZoningPrecheckError("Zoning relation archive lineage differs")
        _strict_string(row["source_layer"], "zoning relation source layer")
    return result


def _zone_mapping_input_sha256(
    zones: pd.DataFrame,
    structure: PlanningRegulationStructureResult,
) -> str:
    zone_columns = (
        "planning_zone_id",
        "source_zone_id",
        "zone_label_raw",
        "source_document_id",
        "source_archive_sha256",
        "source_layer",
    )
    return _canonical_sha256(
        {
            "domain": "landscout.bess_zoning.zone_mapping_input",
            "zones": _frame_payload(zones, zone_columns),
            "mapping": _frame_payload(
                structure.zone_mapping,
                tuple(str(column) for column in structure.zone_mapping.columns),
            ),
        }
    )


def _zone_chapter_rows(
    structure: PlanningRegulationStructureResult,
) -> list[dict[str, object]]:
    rows = structure.sections.loc[
        structure.sections["section_type"].eq("ZONE_CHAPTER")
    ].to_dict("records")
    labels = [
        _strict_string(row["zone_chapter_label"], "zone chapter label")
        for row in rows
    ]
    section_ids = [
        _strict_string(row["section_id"], "zone chapter section ID") for row in rows
    ]
    if len(set(labels)) != len(labels):
        raise BessZoningPrecheckError(
            "Regulation zone chapter labels must be unique"
        )
    if len(set(section_ids)) != len(section_ids):
        raise BessZoningPrecheckError(
            "Regulation zone chapter section IDs must be unique"
        )
    return rows


def _required_section_ids_by_chapter(
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
) -> dict[str, tuple[str, ...]]:
    required_numbers = set(policy.required_zone_article_numbers)
    chapter_ids = {
        row["zone_chapter_label"]: row["section_id"]
        for row in _zone_chapter_rows(structure)
    }
    result: dict[str, tuple[str, ...]] = {}
    section_rows = structure.sections.to_dict("records")
    for label, chapter_id in chapter_ids.items():
        result[str(label)] = tuple(
            str(row["section_id"])
            for row in section_rows
            if row["section_type"] == "ARTICLE"
            and row["parent_section_id"] == chapter_id
            and row["article_number_raw"] in required_numbers
        )
    return result


def _validate_policy_evidence(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    fragments: pd.DataFrame,
    policy_hash: str,
    evidence_route_links: pd.DataFrame,
) -> tuple[dict[str, dict[str, object]], pd.DataFrame]:
    sections = {
        _strict_string(row["section_id"], "section ID"): row
        for row in structure.sections.to_dict("records")
    }
    fragment_records = {
        (
            _strict_string(row["section_id"], "fragment section ID"),
            _strict_positive_integer(row["page_number"], "fragment page number"),
        ): row
        for row in fragments.to_dict("records")
    }
    chapters = {
        _strict_string(row["zone_chapter_label"], "zone chapter label"): row
        for row in _zone_chapter_rows(structure)
    }
    policy_labels = {chapter.resolved_zone_chapter_label for chapter in policy.chapters}
    if policy_labels != set(chapters):
        missing = sorted(set(chapters).difference(policy_labels))
        extra = sorted(policy_labels.difference(chapters))
        raise BessZoningPrecheckError(
            f"Chapter policy completeness differs; missing={missing}, extra={extra}"
        )
    catalog_rows: list[dict[str, object]] = []
    links_by_evidence: dict[str, list[tuple[str, str]]] = {}
    for link in evidence_route_links.to_dict("records"):
        evidence_id = _strict_string(link["evidence_id"], "linked evidence ID")
        links_by_evidence.setdefault(evidence_id, []).append(
            (
                _strict_string(link["route_id"], "linked route ID"),
                _strict_string(link["route_role"], "route role"),
            )
        )
    required_by_chapter = _required_section_ids_by_chapter(structure, policy)
    for chapter in policy.chapters:
        chapter_row = chapters[chapter.resolved_zone_chapter_label]
        chapter_id = chapter_row["section_id"]
        reviewed_ids = set(chapter.reviewed_section_ids)
        for reviewed_id in chapter.reviewed_section_ids:
            reviewed = sections.get(reviewed_id)
            if reviewed is None:
                raise BessZoningPrecheckError(
                    f"Reviewed section {reviewed_id!r} is unknown"
                )
            if reviewed["section_type"] == "GENERAL":
                continue
            if reviewed["section_type"] not in {"ZONE_CHAPTER", "ARTICLE"}:
                raise BessZoningPrecheckError(
                    f"Reviewed section {reviewed_id!r} is not a zone/general section"
                )
            if reviewed["zone_chapter_label"] != chapter.resolved_zone_chapter_label:
                raise BessZoningPrecheckError(
                    f"Reviewed section {reviewed_id!r} belongs to another chapter"
                )
            if (
                reviewed["section_type"] == "ARTICLE"
                and reviewed["parent_section_id"] != chapter_id
            ):
                raise BessZoningPrecheckError(
                    f"Reviewed section {reviewed_id!r} has another chapter parent"
                )
        required_ids = set(required_by_chapter[chapter.resolved_zone_chapter_label])
        missing_required = sorted(required_ids.difference(reviewed_ids))
        if (
            chapter.review_completeness
            == "COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"
            and missing_required
        ):
            raise BessZoningPrecheckError(
                f"Chapter {chapter.resolved_zone_chapter_label} omits required reviewed articles: {missing_required}"
            )
        for evidence in chapter.evidence:
            reverse_links = tuple(
                sorted(links_by_evidence.get(evidence.evidence_id, []))
            )
            section = sections.get(evidence.section_id)
            if section is None:
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} references an unknown section"
                )
            section_type = section["section_type"]
            if section_type == "GENERAL":
                pass
            elif section["zone_chapter_label"] != chapter.resolved_zone_chapter_label:
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} belongs to another zone chapter"
                )
            if section_type == "ARTICLE" and section["parent_section_id"] != chapter_id:
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} has the wrong chapter parent"
                )
            if evidence.section_id not in reviewed_ids:
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} is outside reviewed sections"
                )
            fragment = fragment_records.get((evidence.section_id, evidence.page_number))
            if fragment is None:
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} has no factual section/page fragment"
                )
            excerpt = evidence.exact_raw_excerpt
            raw_fragment = fragment["raw_text"]
            if not isinstance(raw_fragment, str):
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} fragment text is invalid"
                )
            if fragment["section_page_fragment_sha256"] != evidence.section_page_fragment_sha256:
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} fragment SHA256 differs"
                )
            if evidence.excerpt_end > len(raw_fragment) or raw_fragment[
                evidence.excerpt_start : evidence.excerpt_end
            ] != excerpt:
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} offsets do not identify its exact excerpt"
                )
            if sha256(excerpt.encode("utf-8")).hexdigest() != evidence.excerpt_sha256:
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} excerpt SHA256 differs"
                )
            rule = evidence.source_rule_excerpt
            if evidence.source_rule_end > len(raw_fragment) or raw_fragment[
                evidence.source_rule_start : evidence.source_rule_end
            ] != rule:
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} source-rule offsets differ"
                )
            if sha256(rule.encode("utf-8")).hexdigest() != evidence.source_rule_sha256:
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} source-rule SHA256 differs"
                )
            relative_start = evidence.excerpt_start - evidence.source_rule_start
            relative_end = evidence.excerpt_end - evidence.source_rule_start
            if rule[relative_start:relative_end] != excerpt:
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} is outside its source rule"
                )
            catalog_rows.append(
                {
                    "evidence_id": evidence.evidence_id,
                    "resolved_zone_chapter_label": (
                        chapter.resolved_zone_chapter_label
                    ),
                    "section_id": evidence.section_id,
                    "page_number": evidence.page_number,
                    "evidence_kind": evidence.evidence_kind,
                    "evidence_direction": evidence.evidence_direction,
                    "linked_route_ids": tuple(item[0] for item in reverse_links),
                    "linked_route_roles": tuple(item[1] for item in reverse_links),
                    "decision_linked": bool(reverse_links),
                    "exact_raw_excerpt": excerpt,
                    "excerpt_sha256": evidence.excerpt_sha256,
                    "section_page_fragment_sha256": (
                        evidence.section_page_fragment_sha256
                    ),
                    "excerpt_start": evidence.excerpt_start,
                    "excerpt_end": evidence.excerpt_end,
                    "source_rule_id": evidence.source_rule_id,
                    "source_rule_excerpt": rule,
                    "source_rule_sha256": evidence.source_rule_sha256,
                    "source_rule_start": evidence.source_rule_start,
                    "source_rule_end": evidence.source_rule_end,
                    "interpretation_note": evidence.interpretation_note,
                    "review_completeness": chapter.review_completeness,
                    "review_scope": policy.review_scope,
                    "policy_profile": policy.policy_profile,
                    "policy_sha256": policy_hash,
                    "document_id": index.document_id,
                    "archive_sha256": index.archive_sha256,
                    "pdf_sha256": index.pdf_sha256,
                    "index_content_sha256": index.index_content_sha256,
                    "structure_result_content_sha256": (
                        structure.structure_result_content_sha256
                    ),
                    "structure_profile": structure.structure_profile,
                }
            )
    catalog = pd.DataFrame(catalog_rows, columns=EVIDENCE_CATALOG_COLUMNS)
    for column in (
        "page_number",
        "excerpt_start",
        "excerpt_end",
        "source_rule_start",
        "source_rule_end",
    ):
        catalog[column] = catalog[column].astype("int64")
    catalog["decision_linked"] = catalog["decision_linked"].astype("bool")
    if catalog["evidence_id"].duplicated().any():
        raise BessZoningPrecheckError("Evidence catalog IDs must be unique")
    return chapters, catalog


def _validate_mapping(
    structure: PlanningRegulationStructureResult,
    zones: pd.DataFrame,
) -> pd.DataFrame:
    mapping = structure.zone_mapping.copy(deep=True)
    source_labels = set(
        _exact_id_series(zones["zone_label_raw"], "raw zone label", unique=False)
    )
    mapped_labels = set(
        _exact_id_series(
            mapping["source_zone_label_raw"],
            "mapped source zone label",
            unique=True,
        )
    )
    if mapped_labels != source_labels:
        raise BessZoningPrecheckError("Factual zone mapping is incomplete or has extras")
    chapters = {
        row["zone_chapter_label"]: row["section_id"]
        for row in _zone_chapter_rows(structure)
    }
    for row in mapping.to_dict("records"):
        _strict_string(row["source_zone_label_raw"], "mapped source zone label")
        status = _strict_string(row["mapping_status"], "mapping status")
        if status not in _RESOLVED_MAPPING_STATUSES:
            raise BessZoningPrecheckError(
                f"Source zone {row['source_zone_label_raw']!r} is not resolved"
            )
        resolved = _strict_string(
            row["resolved_zone_chapter_label"], "resolved zone chapter"
        )
        if chapters.get(resolved) != row["matched_section_id"]:
            raise BessZoningPrecheckError("Zone mapping chapter identity is inconsistent")
    return mapping


def _lineage(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> dict[str, object]:
    return {
        "planning_precheck_scope": PLANNING_PRECHECK_SCOPE,
        "review_scope": REVIEW_SCOPE,
        "policy_profile": policy.policy_profile,
        "policy_sha256": policy_hash,
        "document_id": index.document_id,
        "archive_sha256": index.archive_sha256,
        "pdf_sha256": index.pdf_sha256,
        "index_content_sha256": index.index_content_sha256,
        "structure_result_content_sha256": structure.structure_result_content_sha256,
        "structure_profile": structure.structure_profile,
    }


def _build_chapter_policy(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> pd.DataFrame:
    by_label = {
        chapter.resolved_zone_chapter_label: chapter for chapter in policy.chapters
    }
    rows: list[dict[str, object]] = []
    lineage = _lineage(index, structure, policy, policy_hash)
    chapters = _zone_chapter_rows(structure)
    required_by_chapter = _required_section_ids_by_chapter(structure, policy)
    for source in chapters:
        label = _strict_string(source["zone_chapter_label"], "zone chapter label")
        chapter_section_id = _strict_string(
            source["section_id"], "zone chapter section ID"
        )
        chapter = by_label[label]
        evidence_ids = tuple(item.evidence_id for item in chapter.evidence)
        decision_evidence_ids = tuple(
            item.evidence_id
            for item in chapter.evidence
            if item.evidence_direction != "CONTEXT_ONLY"
        )
        context_evidence_ids = tuple(
            item.evidence_id
            for item in chapter.evidence
            if item.evidence_direction == "CONTEXT_ONLY"
        )
        rows.append(
            {
                "resolved_zone_chapter_label": label,
                "chapter_section_id": chapter_section_id,
                "review_completeness": chapter.review_completeness,
                "review_scope": policy.review_scope,
                "reviewed_section_ids": tuple(chapter.reviewed_section_ids),
                "missing_required_section_ids": tuple(
                    section_id
                    for section_id in required_by_chapter[label]
                    if section_id not in set(chapter.reviewed_section_ids)
                ),
                "review_note": chapter.review_note,
                "zoning_precheck_status": chapter.zoning_precheck_status,
                "zoning_precheck_confidence": chapter.zoning_precheck_confidence,
                "evidence_count": len(evidence_ids),
                "evidence_ids": evidence_ids,
                "decision_evidence_ids": decision_evidence_ids,
                "context_evidence_ids": context_evidence_ids,
                "rationale": chapter.rationale,
                "missing_information": chapter.missing_information,
                **lineage,
            }
        )
    frame = pd.DataFrame(rows, columns=CHAPTER_POLICY_COLUMNS)
    frame["evidence_count"] = frame["evidence_count"].astype("int64")
    return frame


def _route_status(route_kind: RouteKind) -> ChapterStatus:
    statuses: dict[RouteKind, ChapterStatus] = {
        "DIRECT_ROUTE": "POTENTIALLY_COMPATIBLE",
        "CONDITIONAL_ROUTE": "CONDITIONAL_REVIEW",
        "RESTRICTION_EXCEPTION_ROUTE": "CONDITIONAL_REVIEW",
        "DIFFICULTY_ONLY": "LIKELY_DIFFICULT",
    }
    return statuses[route_kind]


def _build_route_assessments(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> pd.DataFrame:
    lineage = _lineage(index, structure, policy, policy_hash)
    rows = [
        {
            "route_id": route.route_id,
            "resolved_zone_chapter_label": chapter.resolved_zone_chapter_label,
            "route_kind": route.route_kind,
            "derived_route_status": _route_status(route.route_kind),
            "positive_evidence_ids": tuple(route.positive_evidence_ids),
            "condition_evidence_ids": tuple(route.condition_evidence_ids),
            "difficulty_evidence_ids": tuple(route.difficulty_evidence_ids),
            "applicability_note": route.applicability_note,
            "review_completeness": chapter.review_completeness,
            "review_scope": policy.review_scope,
            **lineage,
        }
        for chapter in policy.chapters
        for route in chapter.route_assessments
    ]
    frame = pd.DataFrame(rows, columns=ROUTE_ASSESSMENT_COLUMNS)
    if frame["route_id"].duplicated().any():
        raise BessZoningPrecheckError("Normalized route IDs must be unique")
    return frame


def _build_evidence_route_links(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> pd.DataFrame:
    lineage = _lineage(index, structure, policy, policy_hash)
    rows: list[dict[str, object]] = []
    role_fields = (
        ("positive_evidence_ids", "POSITIVE", "SUPPORTS_POTENTIAL_COMPATIBILITY"),
        ("condition_evidence_ids", "CONDITION", "CONDITION"),
        ("difficulty_evidence_ids", "DIFFICULTY", "SUPPORTS_DIFFICULTY"),
    )
    for chapter in policy.chapters:
        for route in chapter.route_assessments:
            for field, role, direction in role_fields:
                for evidence_id in getattr(route, field):
                    rows.append(
                        {
                            "route_id": route.route_id,
                            "resolved_zone_chapter_label": (
                                chapter.resolved_zone_chapter_label
                            ),
                            "route_kind": route.route_kind,
                            "evidence_id": evidence_id,
                            "route_role": role,
                            "evidence_direction": direction,
                            "review_completeness": chapter.review_completeness,
                            "review_scope": policy.review_scope,
                            **lineage,
                        }
                    )
    frame = pd.DataFrame(rows, columns=EVIDENCE_ROUTE_LINK_COLUMNS)
    if not frame.empty:
        frame = frame.sort_values(
            ["route_id", "evidence_id"], kind="mergesort"
        ).reset_index(drop=True)
    if frame.duplicated(["route_id", "evidence_id"]).any():
        raise BessZoningPrecheckError(
            "Evidence-route links must be unique by route and evidence"
        )
    return frame


def _build_source_zone_policy(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
    zones: pd.DataFrame,
    mapping: pd.DataFrame,
    chapter_policy: pd.DataFrame,
) -> pd.DataFrame:
    policies = chapter_policy.set_index("resolved_zone_chapter_label").to_dict("index")
    lineage = _lineage(index, structure, policy, policy_hash)
    layers_by_label: dict[str, str] = {}
    for label, group in zones.groupby("zone_label_raw", sort=False):
        layers = tuple(dict.fromkeys(group["source_layer"].tolist()))
        if len(layers) != 1:
            raise BessZoningPrecheckError(
                f"Source zone label {label!r} has ambiguous source-layer lineage"
            )
        layers_by_label[str(label)] = _strict_string(layers[0], "zone source layer")
    rows: list[dict[str, object]] = []
    for source in mapping.to_dict("records"):
        chapter = policies[source["resolved_zone_chapter_label"]]
        rows.append(
            {
                "source_zone_label_raw": source["source_zone_label_raw"],
                "resolved_zone_chapter_label": source[
                    "resolved_zone_chapter_label"
                ],
                "mapping_status": source["mapping_status"],
                "matched_section_id": source["matched_section_id"],
                "source_layer": layers_by_label[source["source_zone_label_raw"]],
                "zoning_precheck_status": chapter["zoning_precheck_status"],
                "zoning_precheck_confidence": chapter[
                    "zoning_precheck_confidence"
                ],
                "evidence_ids": tuple(chapter["evidence_ids"]),
                "decision_evidence_ids": tuple(chapter["decision_evidence_ids"]),
                "context_evidence_ids": tuple(chapter["context_evidence_ids"]),
                **lineage,
            }
        )
    return pd.DataFrame(rows, columns=SOURCE_ZONE_POLICY_COLUMNS)


def _build_parcel_zone_interpretations(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
    relations: pd.DataFrame,
    source_policy: pd.DataFrame,
) -> pd.DataFrame:
    policies = source_policy.set_index("source_zone_label_raw").to_dict("index")
    lineage = _lineage(index, structure, policy, policy_hash)
    rows: list[dict[str, object]] = []
    positive = relations.loc[relations["relation_type"].eq("AREA_OVERLAP")]
    for source in positive.to_dict("records"):
        item = policies[source["zone_label_raw"]]
        rows.append(
            {
                "parcel_id": source["parcel_id"],
                "planning_zone_id": source["planning_zone_id"],
                "source_zone_id": source["source_zone_id"],
                "source_zone_label_raw": source["zone_label_raw"],
                "resolved_zone_chapter_label": item[
                    "resolved_zone_chapter_label"
                ],
                "intersection_area_m2": float(source["intersection_area_m2"]),
                "parcel_share_pct": float(source["parcel_share_pct"]),
                "zoning_precheck_status": item["zoning_precheck_status"],
                "zoning_precheck_confidence": item[
                    "zoning_precheck_confidence"
                ],
                "evidence_ids": tuple(item["evidence_ids"]),
                "decision_evidence_ids": tuple(item["decision_evidence_ids"]),
                "context_evidence_ids": tuple(item["context_evidence_ids"]),
                **lineage,
                "source_layer": source["source_layer"],
            }
        )
    frame = pd.DataFrame(rows, columns=PARCEL_ZONE_POLICY_COLUMNS)
    if frame.empty:
        frame = pd.DataFrame(
            {
                column: pd.Series(
                    dtype=(
                        "float64"
                        if column in {"intersection_area_m2", "parcel_share_pct"}
                        else "object"
                    )
                )
                for column in PARCEL_ZONE_POLICY_COLUMNS
            }
        )
    return frame


def _is_null(value: object) -> bool:
    if value is None or value is pd.NA:
        return True
    try:
        null = pd.isna(value)
    except (TypeError, ValueError):
        return False
    return isinstance(null, (bool, np.bool_)) and bool(null)


def _build_parcel_output(
    parcels: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    interpretations: pd.DataFrame,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> gpd.GeoDataFrame:
    output = parcels.copy(deep=True)
    positive_by_parcel = {
        parcel_id: group.copy()
        for parcel_id, group in interpretations.groupby("parcel_id", sort=False)
    }
    touch_counts = (
        relations.loc[relations["relation_type"].eq("TOUCH_ONLY")]
        .groupby("parcel_id", sort=False)
        .size()
        .to_dict()
    )
    summary: dict[str, list[object]] = {column: [] for column in PARCEL_PRECHECK_COLUMNS}
    for parcel in parcels.to_dict("records"):
        parcel_id = parcel["parcel_id"]
        group = positive_by_parcel.get(parcel_id)
        dominant_id = parcel["dominant_planning_zone_id"]
        if group is None or group.empty:
            if not _is_null(dominant_id):
                raise BessZoningPrecheckError(
                    "Parcel dominant zone exists without a positive-area relation"
                )
            overall_status = "UNKNOWN"
            dominant_status: object = None
            dominant_confidence: object = None
            positive_count = 0
            distinct_count = 0
            non_dominant_different = 0
            evidence_ids: tuple[str, ...] = ()
            context_evidence_ids: tuple[str, ...] = ()
        else:
            ordered = group.sort_values(
                ["intersection_area_m2", "planning_zone_id"],
                ascending=[False, True],
                kind="mergesort",
            )
            expected_dominant = ordered.iloc[0]["planning_zone_id"]
            if dominant_id != expected_dominant:
                raise BessZoningPrecheckError(
                    "Parcel dominant zone differs from factual positive-area relations"
                )
            dominant = ordered.iloc[0]
            dominant_status = dominant["zoning_precheck_status"]
            dominant_confidence = dominant["zoning_precheck_confidence"]
            statuses = tuple(group["zoning_precheck_status"].tolist())
            distinct_statuses = set(statuses)
            overall_status = (
                statuses[0]
                if len(distinct_statuses) == 1
                else "MIXED_REVIEW_REQUIRED"
            )
            positive_count = len(group)
            distinct_count = len(distinct_statuses)
            non_dominant_different = int(
                (
                    group.loc[
                        ~group["planning_zone_id"].eq(expected_dominant),
                        "zoning_precheck_status",
                    ]
                    != dominant_status
                ).sum()
            )
            evidence_ids = tuple(
                sorted(
                    {
                        _strict_string(evidence_id, "parcel evidence ID")
                        for values in group["decision_evidence_ids"].tolist()
                        for evidence_id in values
                    }
                )
            )
            context_evidence_ids = tuple(
                sorted(
                    {
                        _strict_string(evidence_id, "parcel context evidence ID")
                        for values in group["context_evidence_ids"].tolist()
                        for evidence_id in values
                    }
                )
            )
        summary["zoning_precheck_status"].append(overall_status)
        summary["dominant_zone_precheck_status"].append(dominant_status)
        summary["dominant_zone_precheck_confidence"].append(dominant_confidence)
        summary["positive_area_zone_count"].append(positive_count)
        summary["distinct_zone_status_count"].append(distinct_count)
        summary["non_dominant_different_status_count"].append(
            non_dominant_different
        )
        summary["touch_only_zone_count"].append(int(touch_counts.get(parcel_id, 0)))
        summary["zoning_precheck_evidence_ids"].append(evidence_ids)
        summary["zoning_precheck_context_evidence_ids"].append(
            context_evidence_ids
        )
        summary["zoning_precheck_requires_formal_review"].append(True)
        summary["planning_precheck_scope"].append(PLANNING_PRECHECK_SCOPE)
        summary["review_scope"].append(REVIEW_SCOPE)
        summary["non_zoning_planning_features_interpreted"].append(False)
        summary["zoning_precheck_policy_profile"].append(policy.policy_profile)
        summary["zoning_precheck_policy_sha256"].append(policy_hash)
    for column in PARCEL_PRECHECK_COLUMNS:
        values = np.empty(len(summary[column]), dtype=object)
        values[:] = summary[column]
        output[column] = values
    for column in (
        "positive_area_zone_count",
        "distinct_zone_status_count",
        "non_dominant_different_status_count",
        "touch_only_zone_count",
    ):
        output[column] = output[column].astype("int64")
    for column in (
        "zoning_precheck_requires_formal_review",
        "non_zoning_planning_features_interpreted",
    ):
        output[column] = output[column].astype("bool")
    return output


def _result_component_metadata(result: BessZoningPrecheckResult) -> dict[str, object]:
    return {
        "result_hash_schema_version": result.result_hash_schema_version,
        "policy_schema_version": result.policy_schema_version,
        "policy_profile": result.policy_profile,
        "planning_precheck_scope": result.planning_precheck_scope,
        "review_scope": result.review_scope,
        "document_id": result.document_id,
        "archive_sha256": result.archive_sha256,
        "pdf_sha256": result.pdf_sha256,
        "index_content_sha256": result.index_content_sha256,
        "structure_result_content_sha256": result.structure_result_content_sha256,
        "structure_profile": result.structure_profile,
        "policy_config_sha256": result.policy_config_sha256,
        "factual_structure_content_sha256": result.factual_structure_content_sha256,
        "zone_mapping_input_sha256": result.zone_mapping_input_sha256,
        "zoning_relation_hash_columns": list(result.zoning_relation_hash_columns),
        "zoning_relations_input_sha256": result.zoning_relations_input_sha256,
        "touch_only_relation_count": result.touch_only_relation_count,
    }


def _result_frame_sha256(
    domain: str,
    result: BessZoningPrecheckResult,
    frame: pd.DataFrame,
    columns: Sequence[str],
) -> str:
    return _canonical_sha256(
        {
            "domain": domain,
            **_result_component_metadata(result),
            "frame": _frame_payload(frame, columns),
        }
    )


def _complete_result_sha256(result: BessZoningPrecheckResult) -> str:
    return _canonical_sha256(
        {
            "domain": "landscout.bess_zoning.precheck_result",
            **_result_component_metadata(result),
            "evidence_catalog_content_sha256": (
                result.evidence_catalog_content_sha256
            ),
            "evidence_route_links_content_sha256": (
                result.evidence_route_links_content_sha256
            ),
            "route_assessments_content_sha256": (
                result.route_assessments_content_sha256
            ),
            "chapter_policy_content_sha256": result.chapter_policy_content_sha256,
            "source_zone_policy_content_sha256": (
                result.source_zone_policy_content_sha256
            ),
            "parcel_zone_policy_content_sha256": (
                result.parcel_zone_policy_content_sha256
            ),
            "parcel_output_content_sha256": result.parcel_output_content_sha256,
        }
    )


def _result_with_hashes(
    result: BessZoningPrecheckResult,
) -> BessZoningPrecheckResult:
    component = replace(
        result,
        evidence_catalog_content_sha256=_result_frame_sha256(
            "landscout.bess_zoning.evidence_catalog",
            result,
            result.evidence_catalog,
            EVIDENCE_CATALOG_COLUMNS,
        ),
        evidence_route_links_content_sha256=_result_frame_sha256(
            "landscout.bess_zoning.evidence_route_links",
            result,
            result.evidence_route_links,
            EVIDENCE_ROUTE_LINK_COLUMNS,
        ),
        route_assessments_content_sha256=_result_frame_sha256(
            "landscout.bess_zoning.route_assessments",
            result,
            result.route_assessments,
            ROUTE_ASSESSMENT_COLUMNS,
        ),
        chapter_policy_content_sha256=_result_frame_sha256(
            "landscout.bess_zoning.chapter_policy",
            result,
            result.chapter_policy,
            CHAPTER_POLICY_COLUMNS,
        ),
        source_zone_policy_content_sha256=_result_frame_sha256(
            "landscout.bess_zoning.source_zone_policy",
            result,
            result.source_zone_policy,
            SOURCE_ZONE_POLICY_COLUMNS,
        ),
        parcel_zone_policy_content_sha256=_result_frame_sha256(
            "landscout.bess_zoning.parcel_zone_policy",
            result,
            result.parcel_zone_interpretations,
            PARCEL_ZONE_POLICY_COLUMNS,
        ),
        parcel_output_content_sha256=_result_frame_sha256(
            "landscout.bess_zoning.parcel_output",
            result,
            result.parcels,
            tuple(result.parcels.columns),
        ),
    )
    return replace(
        component,
        complete_result_content_sha256=_complete_result_sha256(component),
    )


def _build_result(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    structure_config: PlanningRegulationStructureConfig | str | Path,
    zones: pd.DataFrame,
    zoning_intersections: pd.DataFrame,
    parcels: gpd.GeoDataFrame,
    policy: BessZoningPolicyConfig,
) -> BessZoningPrecheckResult:
    validate_planning_regulation_index(index)
    fragments = validate_planning_regulation_structure_with_fragments(
        index,
        zones,
        zoning_intersections,
        structure_config,
        structure,
    )
    _validate_policy_lock(index, structure, policy)
    parcel_copy = _validate_parcels(index, parcels)
    zone_copy = _validate_zones(index, zones)
    relation_copy = _validate_relations(
        index, parcel_copy, zone_copy, zoning_intersections
    )
    mapping = _validate_mapping(structure, zone_copy)
    policy_hash = _policy_sha256(policy)
    route_assessments = _build_route_assessments(
        index, structure, policy, policy_hash
    )
    evidence_route_links = _build_evidence_route_links(
        index, structure, policy, policy_hash
    )
    _, evidence_catalog = _validate_policy_evidence(
        index,
        structure,
        policy,
        fragments,
        policy_hash,
        evidence_route_links,
    )
    chapter_policy = _build_chapter_policy(
        index, structure, policy, policy_hash
    )
    source_policy = _build_source_zone_policy(
        index,
        structure,
        policy,
        policy_hash,
        zone_copy,
        mapping,
        chapter_policy,
    )
    interpretations = _build_parcel_zone_interpretations(
        index,
        structure,
        policy,
        policy_hash,
        relation_copy,
        source_policy,
    )
    parcel_output = _build_parcel_output(
        parcel_copy,
        relation_copy,
        interpretations,
        policy,
        policy_hash,
    )
    relation_columns = tuple(str(column) for column in relation_copy.columns)
    result = BessZoningPrecheckResult(
        result_hash_schema_version=RESULT_HASH_SCHEMA_VERSION,
        policy_schema_version=policy.schema_version,
        policy_profile=policy.policy_profile,
        planning_precheck_scope=PLANNING_PRECHECK_SCOPE,
        review_scope=REVIEW_SCOPE,
        document_id=index.document_id,
        archive_sha256=index.archive_sha256,
        pdf_sha256=index.pdf_sha256,
        index_content_sha256=index.index_content_sha256,
        structure_result_content_sha256=structure.structure_result_content_sha256,
        structure_profile=structure.structure_profile,
        policy_config_sha256=policy_hash,
        factual_structure_content_sha256=_factual_structure_sha256(structure),
        zone_mapping_input_sha256=_zone_mapping_input_sha256(zone_copy, structure),
        zoning_relation_hash_columns=relation_columns,
        zoning_relations_input_sha256=_frame_sha256(
            "landscout.bess_zoning.zoning_relations_input",
            relation_copy,
            relation_columns,
        ),
        evidence_catalog_content_sha256="",
        evidence_route_links_content_sha256="",
        route_assessments_content_sha256="",
        chapter_policy_content_sha256="",
        source_zone_policy_content_sha256="",
        parcel_zone_policy_content_sha256="",
        parcel_output_content_sha256="",
        complete_result_content_sha256="",
        touch_only_relation_count=int(
            relation_copy["relation_type"].eq("TOUCH_ONLY").sum()
        ),
        evidence_catalog=evidence_catalog,
        evidence_route_links=evidence_route_links,
        route_assessments=route_assessments,
        chapter_policy=chapter_policy,
        source_zone_policy=source_policy,
        parcel_zone_interpretations=interpretations,
        parcels=parcel_output,
    )
    return _result_with_hashes(result)


def _compare_frames(
    actual: pd.DataFrame,
    expected: pd.DataFrame,
    columns: Sequence[str],
    label: str,
) -> None:
    if tuple(actual.columns) != tuple(expected.columns) or tuple(actual.columns) != tuple(columns):
        raise BessZoningPrecheckError(f"{label} schema differs from rebuilt result")
    if _canonical_value(_frame_payload(actual, columns)) != _canonical_value(
        _frame_payload(expected, columns)
    ):
        raise BessZoningPrecheckError(f"{label} differs from rebuilt source evidence")


def _compare_results(
    result: BessZoningPrecheckResult,
    expected: BessZoningPrecheckResult,
    original_parcels: gpd.GeoDataFrame,
) -> None:
    if not isinstance(result, BessZoningPrecheckResult):
        raise BessZoningPrecheckError("result must be a BessZoningPrecheckResult")
    scalar_fields = (
        "result_hash_schema_version",
        "policy_schema_version",
        "policy_profile",
        "planning_precheck_scope",
        "review_scope",
        "document_id",
        "archive_sha256",
        "pdf_sha256",
        "index_content_sha256",
        "structure_result_content_sha256",
        "structure_profile",
        "policy_config_sha256",
        "factual_structure_content_sha256",
        "zone_mapping_input_sha256",
        "zoning_relation_hash_columns",
        "zoning_relations_input_sha256",
        "evidence_catalog_content_sha256",
        "evidence_route_links_content_sha256",
        "route_assessments_content_sha256",
        "chapter_policy_content_sha256",
        "source_zone_policy_content_sha256",
        "parcel_zone_policy_content_sha256",
        "parcel_output_content_sha256",
        "complete_result_content_sha256",
        "touch_only_relation_count",
    )
    for field in scalar_fields:
        if getattr(result, field) != getattr(expected, field):
            raise BessZoningPrecheckError(
                f"BESS zoning result {field} differs from rebuilt source evidence"
            )
    if (
        _strict_positive_integer(
            result.result_hash_schema_version,
            "precheck result hash schema version",
        )
        != RESULT_HASH_SCHEMA_VERSION
    ):
        raise BessZoningPrecheckError("Unsupported precheck result hash schema")
    if (
        _strict_positive_integer(
            result.policy_schema_version,
            "precheck policy schema version",
        )
        != POLICY_SCHEMA_VERSION
    ):
        raise BessZoningPrecheckError("Unsupported precheck policy schema")
    _strict_nonnegative_integer(
        result.touch_only_relation_count,
        "touch-only relation count",
    )
    if type(result.zoning_relation_hash_columns) is not tuple or not all(
        isinstance(column, str) and column and column == column.strip()
        for column in result.zoning_relation_hash_columns
    ):
        raise BessZoningPrecheckError(
            "Zoning relation hash columns must be an exact string tuple"
        )
    for field in (
        "archive_sha256",
        "pdf_sha256",
        "index_content_sha256",
        "structure_result_content_sha256",
        "policy_config_sha256",
        "factual_structure_content_sha256",
        "zone_mapping_input_sha256",
        "zoning_relations_input_sha256",
        "evidence_catalog_content_sha256",
        "evidence_route_links_content_sha256",
        "route_assessments_content_sha256",
        "chapter_policy_content_sha256",
        "source_zone_policy_content_sha256",
        "parcel_zone_policy_content_sha256",
        "parcel_output_content_sha256",
        "complete_result_content_sha256",
    ):
        _validated_sha256(getattr(result, field), field)
    _compare_frames(
        result.evidence_catalog,
        expected.evidence_catalog,
        EVIDENCE_CATALOG_COLUMNS,
        "evidence catalog",
    )
    _compare_frames(
        result.evidence_route_links,
        expected.evidence_route_links,
        EVIDENCE_ROUTE_LINK_COLUMNS,
        "evidence-route links",
    )
    _compare_frames(
        result.route_assessments,
        expected.route_assessments,
        ROUTE_ASSESSMENT_COLUMNS,
        "route assessments",
    )
    _compare_frames(
        result.chapter_policy,
        expected.chapter_policy,
        CHAPTER_POLICY_COLUMNS,
        "chapter policy",
    )
    _compare_frames(
        result.source_zone_policy,
        expected.source_zone_policy,
        SOURCE_ZONE_POLICY_COLUMNS,
        "source-zone policy",
    )
    _compare_frames(
        result.parcel_zone_interpretations,
        expected.parcel_zone_interpretations,
        PARCEL_ZONE_POLICY_COLUMNS,
        "parcel/zone policy",
    )
    _compare_frames(
        result.parcels,
        expected.parcels,
        tuple(expected.parcels.columns),
        "parcel precheck",
    )
    original_columns = tuple(original_parcels.columns)
    if tuple(result.parcels.columns[: len(original_columns)]) != original_columns:
        raise BessZoningPrecheckError("Existing parcel columns are not preserved")
    if _canonical_value(_frame_payload(result.parcels, original_columns)) != _canonical_value(
        _frame_payload(original_parcels, original_columns)
    ):
        raise BessZoningPrecheckError(
            "Parcel count, IDs, order, index, geometry, CRS, or prior fields changed"
        )
    statuses = set(result.chapter_policy["zoning_precheck_status"].tolist())
    parcel_statuses = set(result.parcels["zoning_precheck_status"].tolist())
    confidences = set(
        result.chapter_policy["zoning_precheck_confidence"].tolist()
    )
    if not statuses.issubset(_CHAPTER_STATUSES):
        raise BessZoningPrecheckError("Chapter policy status is invalid")
    if not parcel_statuses.issubset(_PARCEL_STATUSES):
        raise BessZoningPrecheckError("Parcel precheck status is invalid")
    if not confidences.issubset(_CONFIDENCES):
        raise BessZoningPrecheckError("Chapter policy confidence is invalid")
    evidence_ids = set(
        _exact_id_series(
            result.evidence_catalog["evidence_id"],
            "catalog evidence ID",
            unique=True,
        )
    )
    catalog_by_id = result.evidence_catalog.set_index("evidence_id").to_dict("index")
    expected_links: set[tuple[str, str, str, str]] = set()
    role_fields = (
        ("positive_evidence_ids", "POSITIVE", "SUPPORTS_POTENTIAL_COMPATIBILITY"),
        ("condition_evidence_ids", "CONDITION", "CONDITION"),
        ("difficulty_evidence_ids", "DIFFICULTY", "SUPPORTS_DIFFICULTY"),
    )
    for route in result.route_assessments.to_dict("records"):
        for field, role, direction in role_fields:
            values = route[field]
            if not isinstance(values, (tuple, list, np.ndarray)):
                raise BessZoningPrecheckError("Route evidence IDs must be arrays")
            for evidence_id in values:
                expected_links.add((route["route_id"], evidence_id, role, direction))
    actual_links = {
        (
            row["route_id"],
            row["evidence_id"],
            row["route_role"],
            row["evidence_direction"],
        )
        for row in result.evidence_route_links.to_dict("records")
    }
    if len(actual_links) != len(result.evidence_route_links) or actual_links != expected_links:
        raise BessZoningPrecheckError(
            "Evidence-route links do not exactly reproduce route evidence arrays"
        )
    reverse_links: dict[str, list[tuple[str, str]]] = {}
    for route_id, evidence_id, role, _ in actual_links:
        if evidence_id not in catalog_by_id:
            raise BessZoningPrecheckError(
                "Evidence-route link references unknown evidence"
            )
        reverse_links.setdefault(evidence_id, []).append((route_id, role))
    decision_ids: set[str] = set()
    context_ids: set[str] = set()
    for evidence_id, row in catalog_by_id.items():
        links = tuple(sorted(reverse_links.get(evidence_id, [])))
        if tuple(row["linked_route_ids"]) != tuple(item[0] for item in links):
            raise BessZoningPrecheckError("Evidence reverse route IDs are inconsistent")
        if tuple(row["linked_route_roles"]) != tuple(item[1] for item in links):
            raise BessZoningPrecheckError("Evidence reverse route roles are inconsistent")
        if bool(row["decision_linked"]) != bool(links):
            raise BessZoningPrecheckError("Evidence reverse decision link is inconsistent")
        if row["evidence_direction"] == "CONTEXT_ONLY":
            context_ids.add(evidence_id)
            if links:
                raise BessZoningPrecheckError(
                    "CONTEXT_ONLY evidence must not influence a route"
                )
        else:
            decision_ids.add(evidence_id)
            if not links:
                raise BessZoningPrecheckError(
                    "Decision evidence must be linked to a route"
                )
    for frame, column in (
        (result.chapter_policy, "evidence_ids"),
        (result.source_zone_policy, "evidence_ids"),
        (result.parcel_zone_interpretations, "evidence_ids"),
        (result.parcels, "zoning_precheck_evidence_ids"),
    ):
        for values in frame[column].tolist():
            if not isinstance(values, (tuple, list, np.ndarray)):
                raise BessZoningPrecheckError("Evidence references must be arrays")
            if not set(values).issubset(evidence_ids):
                raise BessZoningPrecheckError(
                    "An output evidence ID is absent from the evidence catalog"
                )
    for frame in (
        result.chapter_policy,
        result.source_zone_policy,
        result.parcel_zone_interpretations,
    ):
        for row in frame.to_dict("records"):
            retained = set(row["evidence_ids"])
            if set(row["decision_evidence_ids"]) != retained.intersection(decision_ids):
                raise BessZoningPrecheckError("Decision evidence output is inconsistent")
            if set(row["context_evidence_ids"]) != retained.intersection(context_ids):
                raise BessZoningPrecheckError("Context evidence output is inconsistent")
    for row in result.parcels.to_dict("records"):
        if not set(row["zoning_precheck_evidence_ids"]).issubset(decision_ids):
            raise BessZoningPrecheckError("Parcel decision evidence includes context")
        if not set(row["zoning_precheck_context_evidence_ids"]).issubset(context_ids):
            raise BessZoningPrecheckError("Parcel context evidence includes a decision")
    if not result.parcels["zoning_precheck_requires_formal_review"].eq(True).all():
        raise BessZoningPrecheckError("Every parcel must require formal review")
    if not result.parcels["non_zoning_planning_features_interpreted"].eq(False).all():
        raise BessZoningPrecheckError(
            "Non-zoning planning features must remain uninterpreted"
        )
    if not result.parcels["review_scope"].eq(REVIEW_SCOPE).all():
        raise BessZoningPrecheckError("Parcel review scope is invalid")


def validate_bess_zoning_precheck(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    structure_config: PlanningRegulationStructureConfig | str | Path,
    zones: pd.DataFrame,
    zoning_intersections: pd.DataFrame,
    parcels: gpd.GeoDataFrame,
    policy: BessZoningPolicyConfig | str | Path,
    result: BessZoningPrecheckResult,
) -> None:
    """Rebuild and validate the precheck from every factual and policy input."""

    try:
        resolved_policy = _resolved_policy(policy)
        expected = _build_result(
            index,
            structure,
            structure_config,
            zones,
            zoning_intersections,
            parcels,
            resolved_policy,
        )
        _compare_results(result, expected, parcels)
    except BessZoningPrecheckError:
        raise
    except PlanningRegulationStructureError as error:
        raise BessZoningPrecheckError(
            f"Factual regulation structure validation failed: {error}"
        ) from error
    except Exception as error:
        raise BessZoningPrecheckError(
            "BESS zoning precheck validation failed safely"
        ) from error


def interpret_bess_zoning(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    structure_config: PlanningRegulationStructureConfig | str | Path,
    zones: pd.DataFrame,
    zoning_intersections: pd.DataFrame,
    parcels: gpd.GeoDataFrame,
    policy: BessZoningPolicyConfig | str | Path,
) -> BessZoningPrecheckResult:
    """Build a conservative written-zoning precheck without rejecting parcels."""

    try:
        resolved_policy = _resolved_policy(policy)
        result = _build_result(
            index,
            structure,
            structure_config,
            zones,
            zoning_intersections,
            parcels,
            resolved_policy,
        )
        validate_bess_zoning_precheck(
            index,
            structure,
            structure_config,
            zones,
            zoning_intersections,
            parcels,
            resolved_policy,
            result,
        )
        return result
    except BessZoningPrecheckError:
        raise
    except PlanningRegulationStructureError as error:
        raise BessZoningPrecheckError(
            f"Factual regulation structure validation failed: {error}"
        ) from error
    except Exception as error:
        raise BessZoningPrecheckError(
            "BESS zoning precheck could not be built safely"
        ) from error

"""Apply a source-locked, evidence-backed BESS zoning precheck policy."""

from __future__ import annotations

import json
import math
import re
from collections import Counter
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
    PlanningRegulationStructureResult,
)

__all__ = [
    "BessZoningPolicyConfig",
    "BessZoningPrecheckError",
    "BessZoningPrecheckResult",
    "interpret_bess_zoning",
    "load_bess_zoning_policy_config",
    "validate_bess_zoning_precheck",
]

POLICY_SCHEMA_VERSION = 1
RESULT_HASH_SCHEMA_VERSION = 1
PLANNING_PRECHECK_SCOPE = "WRITTEN_ZONING_REGULATION_ONLY"

ChapterStatus = Literal[
    "POTENTIALLY_COMPATIBLE",
    "CONDITIONAL_REVIEW",
    "LIKELY_DIFFICULT",
    "UNKNOWN",
]
Confidence = Literal["HIGH", "MEDIUM", "LOW"]
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

_STRUCTURE_SECTION_COLUMNS = (
    "section_id",
    "parent_section_id",
    "section_type",
    "heading_raw",
    "heading_normalized",
    "zone_chapter_label",
    "article_number_raw",
    "article_title_raw",
    "start_record_id",
    "end_record_id",
    "source_record_count",
    "source_records_sha256",
    "start_page",
    "end_page",
    "page_numbers",
    "raw_text",
    "normalized_text",
    "character_count",
    "section_content_sha256",
    "document_id",
    "archive_sha256",
    "pdf_sha256",
    "index_content_sha256",
    "structure_profile",
)
_STRUCTURE_ZONE_MAPPING_COLUMNS = (
    "source_zone_label_raw",
    "resolved_zone_chapter_label",
    "mapping_status",
    "mapping_method",
    "matched_section_id",
    "zone_polygon_count",
    "candidate_parcel_count",
    "candidate_intersection_count",
    "dominant_candidate_count",
    "document_id",
    "archive_sha256",
    "pdf_sha256",
    "index_content_sha256",
    "structure_profile",
)
_STRUCTURE_TOPIC_COLUMNS = (
    "topic",
    "search_term",
    "normalized_search_term",
    "match_policy",
    "section_id",
    "evidence_scope",
    "zone_chapter_label",
    "article_number_raw",
    "page_number",
    "occurrence_count",
    "first_match_normalized_start",
    "first_match_normalized_end",
    "first_match_raw_start",
    "first_match_raw_end",
    "raw_context",
    "normalized_context",
    "document_id",
    "archive_sha256",
    "pdf_sha256",
    "index_content_sha256",
    "structure_profile",
)

CHAPTER_POLICY_COLUMNS = (
    "resolved_zone_chapter_label",
    "chapter_section_id",
    "zoning_precheck_status",
    "zoning_precheck_confidence",
    "evidence_count",
    "evidence_ids",
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
SOURCE_ZONE_POLICY_COLUMNS = (
    "source_zone_label_raw",
    "resolved_zone_chapter_label",
    "mapping_status",
    "matched_section_id",
    "source_layer",
    "zoning_precheck_status",
    "zoning_precheck_confidence",
    "evidence_ids",
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
    "zoning_precheck_requires_formal_review",
    "planning_precheck_scope",
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
    interpretation_note: StrictStr = Field(min_length=1)

    @model_validator(mode="after")
    def _validate_exact_strings(self) -> PolicyEvidence:
        for value, label in (
            (self.evidence_id, "evidence ID"),
            (self.section_id, "evidence section ID"),
            (self.exact_raw_excerpt, "exact raw excerpt"),
            (self.interpretation_note, "interpretation note"),
        ):
            _config_string(value, label)
        if sha256(self.exact_raw_excerpt.encode("utf-8")).hexdigest() != self.excerpt_sha256:
            raise ValueError("evidence excerpt SHA256 differs from exact_raw_excerpt")
        return self


class ChapterPolicy(_StrictConfigModel):
    resolved_zone_chapter_label: StrictStr = Field(min_length=1)
    zoning_precheck_status: ChapterStatus
    zoning_precheck_confidence: Confidence
    rationale: StrictStr = Field(min_length=1)
    missing_information: StrictStr = Field(min_length=1)
    evidence: tuple[PolicyEvidence, ...] = ()

    @model_validator(mode="after")
    def _validate_evidence_semantics(self) -> ChapterPolicy:
        _config_string(self.resolved_zone_chapter_label, "chapter label")
        _config_string(self.rationale, "chapter rationale")
        _config_string(self.missing_information, "chapter missing information")
        directions = {item.evidence_direction for item in self.evidence}
        status = self.zoning_precheck_status
        if status == "POTENTIALLY_COMPATIBLE" and "SUPPORTS_POTENTIAL_COMPATIBILITY" not in directions:
            raise ValueError("POTENTIALLY_COMPATIBLE requires positive evidence")
        if status == "LIKELY_DIFFICULT" and "SUPPORTS_DIFFICULTY" not in directions:
            raise ValueError("LIKELY_DIFFICULT requires difficulty evidence")
        if status == "CONDITIONAL_REVIEW" and not (
            "CONDITION" in directions
            or {
                "SUPPORTS_POTENTIAL_COMPATIBILITY",
                "SUPPORTS_DIFFICULTY",
            }.issubset(directions)
        ):
            raise ValueError("CONDITIONAL_REVIEW requires a condition or conflicting evidence")
        if status == "UNKNOWN" and directions.difference({"CONTEXT_ONLY"}):
            raise ValueError("UNKNOWN may contain only contextual evidence")
        return self


class BessZoningPolicyConfig(_StrictConfigModel):
    """Strict source-locked interpretation policy."""

    schema_version: StrictInt
    policy_profile: StrictStr = Field(min_length=1)
    planning_precheck_scope: Literal["WRITTEN_ZONING_REGULATION_ONLY"]
    source_lock: PolicySourceLock
    chapters: tuple[ChapterPolicy, ...] = Field(min_length=1)

    @model_validator(mode="after")
    def _validate_policy(self) -> BessZoningPolicyConfig:
        if self.schema_version != POLICY_SCHEMA_VERSION:
            raise ValueError(f"unsupported BESS zoning policy schema: {self.schema_version}")
        _config_string(self.policy_profile, "policy profile")
        _config_string(self.source_lock.document_id, "policy document ID")
        _config_string(self.source_lock.structure_profile, "policy structure profile")
        labels = [chapter.resolved_zone_chapter_label for chapter in self.chapters]
        if len(set(labels)) != len(labels):
            raise ValueError("chapter policy labels must be unique")
        evidence_ids: set[str] = set()
        excerpt_directions: dict[tuple[str, str, int], str] = {}
        for chapter in self.chapters:
            for evidence in chapter.evidence:
                if evidence.evidence_id in evidence_ids:
                    raise ValueError("evidence IDs must be globally unique")
                evidence_ids.add(evidence.evidence_id)
                key = (evidence.excerpt_sha256, evidence.section_id, evidence.page_number)
                previous = excerpt_directions.get(key)
                if previous is not None and previous != evidence.evidence_direction:
                    raise ValueError("one evidence excerpt cannot use contradictory directions")
                excerpt_directions[key] = evidence.evidence_direction
        return self


@dataclass(frozen=True)
class BessZoningPrecheckResult:
    """Immutable envelope around the conservative written-zoning precheck."""

    result_hash_schema_version: int
    policy_schema_version: int
    policy_profile: str
    planning_precheck_scope: str
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
    chapter_policy_content_sha256: str
    source_zone_policy_content_sha256: str
    parcel_zone_policy_content_sha256: str
    parcel_output_content_sha256: str
    complete_result_content_sha256: str
    touch_only_relation_count: int
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


def _structure_component_payload(
    structure: PlanningRegulationStructureResult,
) -> dict[str, object]:
    return {
        "section_hash_schema_version": structure.section_hash_schema_version,
        "document_id": structure.document_id,
        "archive_sha256": structure.archive_sha256,
        "pdf_sha256": structure.pdf_sha256,
        "index_content_sha256": structure.index_content_sha256,
        "structure_profile": structure.structure_profile,
        "structure_config_schema_version": structure.structure_config_schema_version,
        "structure_config_sha256": structure.structure_config_sha256,
        "zones_content_sha256": structure.zones_content_sha256,
        "zoning_intersection_hash_columns": list(
            structure.zoning_intersection_hash_columns
        ),
        "zoning_intersections_content_sha256": (
            structure.zoning_intersections_content_sha256
        ),
        "source_records_sha256": structure.source_records_sha256,
    }


def _structure_component_sha256(
    domain: str,
    structure: PlanningRegulationStructureResult,
    frame: pd.DataFrame,
    columns: Sequence[str],
) -> str:
    return _canonical_sha256(
        {
            "domain": domain,
            **_structure_component_payload(structure),
            "rows": frame.loc[:, columns].to_dict("records"),
        }
    )


def _validate_structure_self(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
) -> None:
    if not isinstance(structure, PlanningRegulationStructureResult):
        raise BessZoningPrecheckError(
            "structure must be a PlanningRegulationStructureResult"
        )
    if structure.section_hash_schema_version != 3:
        raise BessZoningPrecheckError("Unsupported factual structure schema")
    comparisons = (
        (structure.document_id, index.document_id, "document ID"),
        (structure.archive_sha256, index.archive_sha256, "archive SHA256"),
        (structure.pdf_sha256, index.pdf_sha256, "PDF SHA256"),
        (structure.index_content_sha256, index.index_content_sha256, "index hash"),
    )
    for actual, expected, label in comparisons:
        if actual != expected:
            raise BessZoningPrecheckError(f"Factual structure {label} differs from index")
    for value, label in (
        (structure.archive_sha256, "structure archive SHA256"),
        (structure.pdf_sha256, "structure PDF SHA256"),
        (structure.index_content_sha256, "structure index SHA256"),
        (structure.structure_config_sha256, "structure config SHA256"),
        (structure.zones_content_sha256, "structure zones SHA256"),
        (
            structure.zoning_intersections_content_sha256,
            "structure intersections SHA256",
        ),
        (structure.source_records_sha256, "structure records SHA256"),
    ):
        _validated_sha256(value, label)
    frames = (
        (
            structure.sections,
            _STRUCTURE_SECTION_COLUMNS,
            "landscout.planning_regulation.sections",
            structure.sections_content_sha256,
            "sections",
        ),
        (
            structure.zone_mapping,
            _STRUCTURE_ZONE_MAPPING_COLUMNS,
            "landscout.planning_regulation.zone_map",
            structure.zone_map_content_sha256,
            "zone map",
        ),
        (
            structure.topic_evidence,
            _STRUCTURE_TOPIC_COLUMNS,
            "landscout.planning_regulation.topic_evidence",
            structure.topic_evidence_content_sha256,
            "topic evidence",
        ),
    )
    for frame, columns, domain, actual_hash, label in frames:
        if not isinstance(frame, pd.DataFrame) or tuple(frame.columns) != tuple(columns):
            raise BessZoningPrecheckError(f"Factual structure {label} schema differs")
        expected_hash = _structure_component_sha256(domain, structure, frame, columns)
        if _validated_sha256(actual_hash, f"{label} SHA256") != expected_hash:
            raise BessZoningPrecheckError(f"Factual structure {label} hash differs")
    for row in structure.sections.to_dict("records"):
        content = {
            column: row[column]
            for column in _STRUCTURE_SECTION_COLUMNS
            if column != "section_content_sha256"
        }
        expected = _canonical_sha256(
            {
                "domain": "landscout.planning_regulation.section",
                "section_hash_schema_version": structure.section_hash_schema_version,
                "section": content,
            }
        )
        if row["section_content_sha256"] != expected:
            raise BessZoningPrecheckError("Factual section content hash differs")
    expected_complete = _canonical_sha256(
        {
            "domain": "landscout.planning_regulation.structure_result",
            "document_id": structure.document_id,
            "archive_sha256": structure.archive_sha256,
            "pdf_sha256": structure.pdf_sha256,
            "index_content_sha256": structure.index_content_sha256,
            "structure_profile": structure.structure_profile,
            "structure_config_schema_version": structure.structure_config_schema_version,
            "structure_config_sha256": structure.structure_config_sha256,
            "zones_content_sha256": structure.zones_content_sha256,
            "zoning_intersection_hash_columns": list(
                structure.zoning_intersection_hash_columns
            ),
            "zoning_intersections_content_sha256": (
                structure.zoning_intersections_content_sha256
            ),
            "source_records_sha256": structure.source_records_sha256,
            "section_hash_schema_version": structure.section_hash_schema_version,
            "sections_content_sha256": structure.sections_content_sha256,
            "zone_map_content_sha256": structure.zone_map_content_sha256,
            "topic_evidence_content_sha256": structure.topic_evidence_content_sha256,
        }
    )
    if structure.structure_result_content_sha256 != expected_complete:
        raise BessZoningPrecheckError("Complete factual structure hash differs")


def _factual_structure_sha256(
    structure: PlanningRegulationStructureResult,
) -> str:
    return _canonical_sha256(
        {
            "domain": "landscout.bess_zoning.factual_structure_input",
            "structure_result_content_sha256": structure.structure_result_content_sha256,
            "section_hash_schema_version": structure.section_hash_schema_version,
            "sections": structure.sections.loc[
                :, _STRUCTURE_SECTION_COLUMNS
            ].to_dict("records"),
            "zone_mapping": structure.zone_mapping.loc[
                :, _STRUCTURE_ZONE_MAPPING_COLUMNS
            ].to_dict("records"),
            "topic_evidence": structure.topic_evidence.loc[
                :, _STRUCTURE_TOPIC_COLUMNS
            ].to_dict("records"),
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
        "parcel_share_pct",
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
        share = _strict_nonnegative_number(row["parcel_share_pct"], "parcel share")
        if share > 100.0 + 1e-9:
            raise BessZoningPrecheckError("Parcel share exceeds 100 percent")
        if relation_type == "AREA_OVERLAP" and area <= 0:
            raise BessZoningPrecheckError("AREA_OVERLAP requires positive area")
        if relation_type == "TOUCH_ONLY" and area != 0:
            raise BessZoningPrecheckError("TOUCH_ONLY requires zero area")
        if relation_type not in {"AREA_OVERLAP", "TOUCH_ONLY"}:
            raise BessZoningPrecheckError("Zoning relation type is invalid")
        for upper_column in ("parcel_metric_area_m2", "zone_area_m2"):
            if upper_column in result.columns:
                upper = _strict_nonnegative_number(row[upper_column], upper_column)
                if area - upper > technical_overlay_tolerance(upper):
                    raise BessZoningPrecheckError(
                        f"Intersection area exceeds {upper_column}"
                    )
        percentage_checks = (
            ("parcel_metric_area_m2", "parcel_share_pct"),
            ("zone_area_m2", "zone_share_pct"),
        )
        for area_column, percentage_column in percentage_checks:
            if area_column not in result.columns or percentage_column not in result.columns:
                continue
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
            expected_percentage = 100.0 * area / reference_area
            if not math.isclose(
                observed_percentage,
                expected_percentage,
                rel_tol=1e-12,
                abs_tol=1e-9,
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
                _STRUCTURE_ZONE_MAPPING_COLUMNS,
            ),
        }
    )


def _validate_structure_factual_inputs(
    structure: PlanningRegulationStructureResult,
    zones: pd.DataFrame,
    relations: pd.DataFrame,
) -> None:
    zone_columns = (
        "planning_zone_id",
        "source_zone_id",
        "zone_label_raw",
        "source_document_id",
        "source_archive_sha256",
    )
    expected_zones = _canonical_sha256(
        {
            "domain": "landscout.planning_regulation.zones_input",
            "columns": list(zone_columns),
            "rows": zones.loc[:, zone_columns].to_dict("records"),
        }
    )
    required_relation_columns = (
        "parcel_id",
        "planning_zone_id",
        "source_zone_id",
        "zone_label_raw",
        "relation_type",
        "intersection_area_m2",
        "source_document_id",
        "source_archive_sha256",
    )
    optional_relation_columns = tuple(
        column
        for column in ("parcel_metric_area_m2", "zone_area_m2")
        if column in relations.columns
    )
    relation_columns = required_relation_columns + optional_relation_columns
    expected_relations = _canonical_sha256(
        {
            "domain": "landscout.planning_regulation.intersections_input",
            "columns": list(relation_columns),
            "rows": relations.loc[:, relation_columns].to_dict("records"),
        }
    )
    if structure.zones_content_sha256 != expected_zones:
        raise BessZoningPrecheckError(
            "Zone catalog differs from the validated factual structure input"
        )
    if structure.zoning_intersection_hash_columns != relation_columns:
        raise BessZoningPrecheckError(
            "Zoning relation hash columns differ from the factual structure input"
        )
    if structure.zoning_intersections_content_sha256 != expected_relations:
        raise BessZoningPrecheckError(
            "Zoning relations differ from the validated factual structure input"
        )


def _page_numbers(value: object) -> tuple[int, ...]:
    if not isinstance(value, (tuple, list, np.ndarray)):
        raise BessZoningPrecheckError("Section page_numbers must be an array")
    return tuple(_strict_positive_integer(item, "section page number") for item in value)


def _validate_policy_evidence(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
) -> tuple[dict[str, dict[str, object]], dict[int, str]]:
    sections = {
        _strict_string(row["section_id"], "section ID"): row
        for row in structure.sections.to_dict("records")
    }
    pages = {
        _strict_positive_integer(row["page_number"], "page number"): row["raw_text"]
        for row in index.pages.to_dict("records")
    }
    chapters = {
        _strict_string(row["zone_chapter_label"], "zone chapter label"): row
        for row in structure.sections.loc[
            structure.sections["section_type"].eq("ZONE_CHAPTER")
        ].to_dict("records")
    }
    policy_labels = {chapter.resolved_zone_chapter_label for chapter in policy.chapters}
    if policy_labels != set(chapters):
        missing = sorted(set(chapters).difference(policy_labels))
        extra = sorted(policy_labels.difference(chapters))
        raise BessZoningPrecheckError(
            f"Chapter policy completeness differs; missing={missing}, extra={extra}"
        )
    for chapter in policy.chapters:
        chapter_row = chapters[chapter.resolved_zone_chapter_label]
        chapter_id = chapter_row["section_id"]
        for evidence in chapter.evidence:
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
            if evidence.page_number not in _page_numbers(section["page_numbers"]):
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} page differs from its section"
                )
            page_text = pages.get(evidence.page_number)
            if not isinstance(page_text, str):
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} references an unknown page"
                )
            excerpt = evidence.exact_raw_excerpt
            if excerpt not in page_text or excerpt not in section["raw_text"]:
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} excerpt is absent from source text"
                )
            if sha256(excerpt.encode("utf-8")).hexdigest() != evidence.excerpt_sha256:
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} excerpt SHA256 differs"
                )
    return chapters, pages


def _validate_mapping(
    structure: PlanningRegulationStructureResult,
    zones: pd.DataFrame,
    relations: pd.DataFrame,
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
        for row in structure.sections.loc[
            structure.sections["section_type"].eq("ZONE_CHAPTER")
        ].to_dict("records")
    }
    zone_polygon_counts = Counter(zones["zone_label_raw"].tolist())
    candidate_parcel_counts = (
        relations.groupby("zone_label_raw", sort=False)["parcel_id"].nunique().to_dict()
    )
    candidate_intersection_counts = Counter(relations["zone_label_raw"].tolist())
    positive = relations.loc[
        relations["intersection_area_m2"].gt(0),
        ["parcel_id", "planning_zone_id", "zone_label_raw", "intersection_area_m2"],
    ].copy()
    if positive.empty:
        dominant_counts: Counter[str] = Counter()
    else:
        positive = positive.sort_values(
            ["parcel_id", "intersection_area_m2", "planning_zone_id"],
            ascending=[True, False, True],
            kind="mergesort",
        )
        dominant_counts = Counter(
            positive.drop_duplicates("parcel_id", keep="first")[
                "zone_label_raw"
            ].tolist()
        )
    for row in mapping.to_dict("records"):
        label = _strict_string(row["source_zone_label_raw"], "mapped source zone label")
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
        expected_counts = {
            "zone_polygon_count": zone_polygon_counts[label],
            "candidate_parcel_count": int(candidate_parcel_counts.get(label, 0)),
            "candidate_intersection_count": candidate_intersection_counts[label],
            "dominant_candidate_count": dominant_counts[label],
        }
        for column, expected in expected_counts.items():
            observed = _strict_nonnegative_integer(row[column], column)
            if observed != expected:
                raise BessZoningPrecheckError(
                    f"Zone mapping {column} differs from factual inputs"
                )
    return mapping


def _lineage(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> dict[str, object]:
    return {
        "planning_precheck_scope": PLANNING_PRECHECK_SCOPE,
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
    chapters = structure.sections.loc[
        structure.sections["section_type"].eq("ZONE_CHAPTER")
    ]
    for source in chapters.to_dict("records"):
        label = source["zone_chapter_label"]
        chapter = by_label[label]
        evidence_ids = tuple(item.evidence_id for item in chapter.evidence)
        rows.append(
            {
                "resolved_zone_chapter_label": label,
                "chapter_section_id": source["section_id"],
                "zoning_precheck_status": chapter.zoning_precheck_status,
                "zoning_precheck_confidence": chapter.zoning_precheck_confidence,
                "evidence_count": len(evidence_ids),
                "evidence_ids": evidence_ids,
                "rationale": chapter.rationale,
                "missing_information": chapter.missing_information,
                **lineage,
            }
        )
    frame = pd.DataFrame(rows, columns=CHAPTER_POLICY_COLUMNS)
    frame["evidence_count"] = frame["evidence_count"].astype("int64")
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
                        for values in group["evidence_ids"].tolist()
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
        summary["zoning_precheck_requires_formal_review"].append(True)
        summary["planning_precheck_scope"].append(PLANNING_PRECHECK_SCOPE)
        summary["non_zoning_planning_features_interpreted"].append(False)
        summary["zoning_precheck_policy_profile"].append(policy.policy_profile)
        summary["zoning_precheck_policy_sha256"].append(policy_hash)
    for column in PARCEL_PRECHECK_COLUMNS:
        output[column] = np.asarray(summary[column], dtype=object)
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
    zones: pd.DataFrame,
    zoning_intersections: pd.DataFrame,
    parcels: gpd.GeoDataFrame,
    policy: BessZoningPolicyConfig,
) -> BessZoningPrecheckResult:
    validate_planning_regulation_index(index)
    _validate_structure_self(index, structure)
    _validate_policy_lock(index, structure, policy)
    parcel_copy = _validate_parcels(index, parcels)
    zone_copy = _validate_zones(index, zones)
    relation_copy = _validate_relations(
        index, parcel_copy, zone_copy, zoning_intersections
    )
    _validate_structure_factual_inputs(structure, zone_copy, relation_copy)
    _validate_policy_evidence(index, structure, policy)
    mapping = _validate_mapping(structure, zone_copy, relation_copy)
    policy_hash = _policy_sha256(policy)
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
        chapter_policy_content_sha256="",
        source_zone_policy_content_sha256="",
        parcel_zone_policy_content_sha256="",
        parcel_output_content_sha256="",
        complete_result_content_sha256="",
        touch_only_relation_count=int(
            relation_copy["relation_type"].eq("TOUCH_ONLY").sum()
        ),
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
        "chapter_policy_content_sha256",
        "source_zone_policy_content_sha256",
        "parcel_zone_policy_content_sha256",
        "parcel_output_content_sha256",
        "complete_result_content_sha256",
    ):
        _validated_sha256(getattr(result, field), field)
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
    if not result.parcels["zoning_precheck_requires_formal_review"].eq(True).all():
        raise BessZoningPrecheckError("Every parcel must require formal review")
    if not result.parcels["non_zoning_planning_features_interpreted"].eq(False).all():
        raise BessZoningPrecheckError(
            "Non-zoning planning features must remain uninterpreted"
        )


def validate_bess_zoning_precheck(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
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
            zones,
            zoning_intersections,
            parcels,
            resolved_policy,
        )
        _compare_results(result, expected, parcels)
    except BessZoningPrecheckError:
        raise
    except Exception as error:
        raise BessZoningPrecheckError(
            "BESS zoning precheck validation failed safely"
        ) from error


def interpret_bess_zoning(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
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
            zones,
            zoning_intersections,
            parcels,
            resolved_policy,
        )
        validate_bess_zoning_precheck(
            index,
            structure,
            zones,
            zoning_intersections,
            parcels,
            resolved_policy,
            result,
        )
        return result
    except BessZoningPrecheckError:
        raise
    except Exception as error:
        raise BessZoningPrecheckError(
            "BESS zoning precheck could not be built safely"
        ) from error

"""Aggregate exact BESS CNIG feature-policy relations to preserved parcels."""

from __future__ import annotations

import json
import math
import re
from dataclasses import dataclass, replace
from datetime import date, datetime
from hashlib import sha256
from io import BytesIO
from numbers import Integral, Real
from pathlib import Path, PurePosixPath, PureWindowsPath
from typing import Literal

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
from pydantic import (
    BaseModel,
    ConfigDict,
    StrictBool,
    StrictInt,
    StrictStr,
    model_validator,
)
from pyproj import CRS
from shapely import get_coordinate_dimension, to_wkb  # type: ignore[import-untyped]
from shapely.geometry.base import BaseGeometry  # type: ignore[import-untyped]

from landscout.common.bess_application_contract import (
    ALLOWED_CONFIDENCES,
    ALLOWED_PRECHECK_STATUSES,
    NULL_LITERALS,
    POLICY_SCOPE,
    validate_bess_application_relation_frame,
)
from landscout.common.frame_integrity import deterministic_frame_schema_signature
from landscout.sources.gpu_fr import GpuPlanningDocument
from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationResult,
    validate_bess_planning_feature_application_result,
)
from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
)
from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
)

__all__ = [
    "BessPlanningFeatureParcelAggregationArtifactManifest",
    "BessPlanningFeatureParcelAggregationError",
    "BessPlanningFeatureParcelAggregationResult",
    "aggregate_bess_planning_feature_policy_to_parcels",
    "load_bess_planning_feature_parcel_aggregation_artifacts",
    "validate_bess_planning_feature_parcel_aggregation_result",
]

RESULT_HASH_SCHEMA_VERSION = 1
ARTIFACT_MANIFEST_SCHEMA_VERSION = 1
APPLICATION_RESULT_HASH_SCHEMA_VERSION = 2
AGGREGATION_SCOPE = "PARCEL_POLICY_AGGREGATION_ONLY"
CONFIDENCE_METHOD = "LOWEST_CONFIDENCE_FOR_SELECTED_STATUS"
ARTIFACT_KIND = "BESS_PLANNING_FEATURE_PARCEL_AGGREGATION_RESULT"

CONTROLLING_RELATION_TYPES = frozenset({"AREA_OVERLAP", "LENGTH_OVERLAP", "INSIDE"})
CONTEXT_RELATION_TYPES = frozenset({"TOUCH_ONLY", "BOUNDARY_TOUCH"})
AGGREGATION_STATUSES = frozenset(
    {
        "AGGREGATED_EXACT_POLICY",
        "UNRESOLVED_CONTROLLING_CODE_PAIR",
        "TOUCH_ONLY_RELATIONS_ONLY",
        "NO_PLANNING_FEATURE_RELATION",
    }
)
RELATION_ROLES = frozenset(
    {
        "SELECTED_CONTROLLING",
        "LOWER_PRIORITY_CONTROLLING",
        "DEFERRED_BY_UNRESOLVED_CONTROLLING",
        "UNRESOLVED_CONTROLLING",
        "TOUCH_ONLY_CONTEXT",
    }
)
CONFIDENCE_RANK = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}
SHA_PATTERN = re.compile(r"[0-9a-f]{64}")

PARCEL_COLUMNS = (
    "bess_cnig_parcel_aggregation_status",
    "bess_cnig_parcel_precheck_status",
    "bess_cnig_parcel_precheck_confidence",
    "bess_cnig_parcel_status_priority",
    "bess_cnig_controlling_relation_count",
    "bess_cnig_exact_controlling_relation_count",
    "bess_cnig_unresolved_controlling_relation_count",
    "bess_cnig_touch_only_relation_count",
    "bess_cnig_selected_relation_count",
    "bess_cnig_lower_priority_controlling_relation_count",
    "bess_cnig_distinct_exact_status_count",
    "bess_cnig_multiple_exact_statuses",
    "bess_cnig_selected_feature_ids_json",
    "bess_cnig_unresolved_feature_ids_json",
    "bess_cnig_touch_only_feature_ids_json",
    "bess_cnig_confidence_aggregation_method",
    "bess_cnig_formal_review_required",
    "bess_cnig_aggregation_scope",
    "bess_cnig_policy_scope",
    "bess_cnig_local_feature_text_interpreted",
    "bess_cnig_local_regulation_content_interpreted",
    "bess_cnig_legal_conclusion_produced",
    "bess_cnig_parcel_status_aggregated",
    "bess_cnig_parcel_rejection_performed",
    "bess_cnig_score_calculated",
    "bess_cnig_policy_profile",
    "bess_cnig_policy_sha256",
    "bess_cnig_policy_result_sha256",
    "bess_cnig_application_result_sha256",
)
RELATION_COLUMNS = (
    "bess_cnig_parcel_relation_role",
    "bess_cnig_selected_for_parcel_status",
    "bess_cnig_resulting_parcel_aggregation_status",
    "bess_cnig_resulting_parcel_precheck_status",
    "bess_cnig_resulting_parcel_precheck_confidence",
    "bess_cnig_resulting_parcel_status_priority",
)
PARCEL_STRING_COLUMNS = (
    "bess_cnig_parcel_aggregation_status",
    "bess_cnig_parcel_precheck_status",
    "bess_cnig_parcel_precheck_confidence",
    "bess_cnig_selected_feature_ids_json",
    "bess_cnig_unresolved_feature_ids_json",
    "bess_cnig_touch_only_feature_ids_json",
    "bess_cnig_confidence_aggregation_method",
    "bess_cnig_aggregation_scope",
    "bess_cnig_policy_scope",
    "bess_cnig_policy_profile",
    "bess_cnig_policy_sha256",
    "bess_cnig_policy_result_sha256",
    "bess_cnig_application_result_sha256",
)
PARCEL_INTEGER_COLUMNS = (
    "bess_cnig_parcel_status_priority",
    "bess_cnig_controlling_relation_count",
    "bess_cnig_exact_controlling_relation_count",
    "bess_cnig_unresolved_controlling_relation_count",
    "bess_cnig_touch_only_relation_count",
    "bess_cnig_selected_relation_count",
    "bess_cnig_lower_priority_controlling_relation_count",
    "bess_cnig_distinct_exact_status_count",
)
PARCEL_BOOL_COLUMNS = (
    "bess_cnig_multiple_exact_statuses",
    "bess_cnig_formal_review_required",
    "bess_cnig_local_feature_text_interpreted",
    "bess_cnig_local_regulation_content_interpreted",
    "bess_cnig_legal_conclusion_produced",
    "bess_cnig_parcel_status_aggregated",
    "bess_cnig_parcel_rejection_performed",
    "bess_cnig_score_calculated",
)
RELATION_STRING_COLUMNS = (
    "bess_cnig_parcel_relation_role",
    "bess_cnig_resulting_parcel_aggregation_status",
    "bess_cnig_resulting_parcel_precheck_status",
    "bess_cnig_resulting_parcel_precheck_confidence",
)

ArtifactRole = Literal["PARCELS", "RELATION_ASSESSMENTS"]
ARTIFACT_ROLES: tuple[ArtifactRole, ...] = ("PARCELS", "RELATION_ASSESSMENTS")


class BessPlanningFeatureParcelAggregationError(ValueError):
    """Raised when parcel aggregation integrity cannot be proven."""


@dataclass(frozen=True)
class _ApplicationLineage:
    policy_profile: str
    policy_sha256: str
    policy_complete_result_content_sha256: str
    complete_result_content_sha256: str


class _StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


def _exact_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise ValueError(f"{label} must be an exact non-empty string")
    return value


def _sha256_string(value: object, label: str) -> str:
    text = _exact_string(value, label)
    if SHA_PATTERN.fullmatch(text) is None:
        raise ValueError(f"{label} must be a lowercase SHA256")
    return text


class BessPlanningFeatureParcelAggregationArtifactRecord(_StrictModel):
    artifact_role: ArtifactRole
    filename: StrictStr
    row_count: StrictInt
    size_bytes: StrictInt
    sha256: StrictStr
    frame_schema_signature: dict[StrictStr, object]
    geospatial: StrictBool
    crs: dict[StrictStr, object] | None

    @model_validator(mode="after")
    def _validate_record(self) -> BessPlanningFeatureParcelAggregationArtifactRecord:
        _exact_string(self.filename, "artifact filename")
        path = Path(self.filename)
        if (
            path.is_absolute()
            or path.name != self.filename
            or path.suffix.lower() != ".parquet"
        ):
            raise ValueError("artifact filename must be one local Parquet filename")
        if type(self.row_count) is not int or self.row_count < 0:
            raise ValueError("artifact row_count must be non-negative")
        if type(self.size_bytes) is not int or self.size_bytes < 1:
            raise ValueError("artifact size_bytes must be positive")
        _sha256_string(self.sha256, "artifact SHA256")
        expected_geo = self.artifact_role == "PARCELS"
        if self.geospatial is not expected_geo:
            raise ValueError("artifact geospatial flag differs from its role")
        signature_crs = self.frame_schema_signature.get("crs")
        if expected_geo:
            if self.crs is None or signature_crs != self.crs:
                raise ValueError("parcel artifact CRS is missing or inconsistent")
        elif self.crs is not None or signature_crs is not None:
            raise ValueError("relation artifact must not declare CRS")
        return self


@dataclass(frozen=True)
class BessPlanningFeatureParcelAggregationResult:
    result_hash_schema_version: int
    aggregation_scope: str
    policy_scope: str
    local_feature_text_interpreted: bool
    local_regulation_content_interpreted: bool
    legal_conclusion_produced: bool
    parcel_status_aggregated: bool
    parcel_rejection_performed: bool
    score_calculated: bool
    source_document_id: str
    source_archive_sha256: str
    cnig_profile: str
    cnig_profile_sha256: str
    cnig_complete_result_content_sha256: str
    policy_profile: str
    policy_sha256: str
    policy_complete_result_content_sha256: str
    application_result_hash_schema_version: int
    application_complete_result_content_sha256: str
    source_parcels_content_sha256: str
    source_application_relations_content_sha256: str
    relation_assessments_content_sha256: str
    parcels_content_sha256: str
    complete_result_content_sha256: str
    relation_assessments: pd.DataFrame
    parcels: gpd.GeoDataFrame


RESULT_FRAME_FIELDS = ("relation_assessments", "parcels")
RESULT_SCALAR_FIELDS = tuple(
    field
    for field in BessPlanningFeatureParcelAggregationResult.__dataclass_fields__
    if field not in RESULT_FRAME_FIELDS
)


class BessPlanningFeatureParcelAggregationArtifactManifest(_StrictModel):
    schema_version: StrictInt
    artifact_kind: Literal["BESS_PLANNING_FEATURE_PARCEL_AGGREGATION_RESULT"]
    result_hash_schema_version: StrictInt
    aggregation_scope: Literal["PARCEL_POLICY_AGGREGATION_ONLY"]
    policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]
    local_feature_text_interpreted: StrictBool
    local_regulation_content_interpreted: StrictBool
    legal_conclusion_produced: StrictBool
    parcel_status_aggregated: StrictBool
    parcel_rejection_performed: StrictBool
    score_calculated: StrictBool
    source_document_id: StrictStr
    source_archive_sha256: StrictStr
    cnig_profile: StrictStr
    cnig_profile_sha256: StrictStr
    cnig_complete_result_content_sha256: StrictStr
    policy_profile: StrictStr
    policy_sha256: StrictStr
    policy_complete_result_content_sha256: StrictStr
    application_result_hash_schema_version: StrictInt
    application_complete_result_content_sha256: StrictStr
    source_parcels_content_sha256: StrictStr
    source_application_relations_content_sha256: StrictStr
    relation_assessments_content_sha256: StrictStr
    parcels_content_sha256: StrictStr
    complete_result_content_sha256: StrictStr
    artifacts: tuple[BessPlanningFeatureParcelAggregationArtifactRecord, ...]

    @model_validator(mode="after")
    def _validate_manifest(
        self,
    ) -> BessPlanningFeatureParcelAggregationArtifactManifest:
        if (
            type(self.schema_version) is not int
            or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION
        ):
            raise ValueError("unsupported parcel aggregation artifact schema")
        if (
            type(self.result_hash_schema_version) is not int
            or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION
        ):
            raise ValueError("unsupported parcel aggregation result schema")
        if any(
            value is not expected
            for value, expected in (
                (self.local_feature_text_interpreted, False),
                (self.local_regulation_content_interpreted, False),
                (self.legal_conclusion_produced, False),
                (self.parcel_status_aggregated, True),
                (self.parcel_rejection_performed, False),
                (self.score_calculated, False),
            )
        ):
            raise ValueError("parcel aggregation boundary flags are invalid")
        for field in RESULT_SCALAR_FIELDS:
            value = getattr(self, field)
            if field.endswith("sha256"):
                _sha256_string(value, field)
        if (
            type(self.application_result_hash_schema_version) is not int
            or self.application_result_hash_schema_version
            != APPLICATION_RESULT_HASH_SCHEMA_VERSION
        ):
            raise ValueError("application result schema must be exactly 2")
        roles = tuple(record.artifact_role for record in self.artifacts)
        if roles != ARTIFACT_ROLES:
            raise ValueError("parcel aggregation artifact roles differ")
        filenames = tuple(record.filename for record in self.artifacts)
        if len(filenames) != len(set(filenames)):
            raise ValueError("parcel aggregation artifact filename is duplicated")
        return self


def _null_value(value: object) -> object:
    if value is None or value is pd.NA:
        return None
    try:
        missing = pd.isna(value)
    except (TypeError, ValueError):
        missing = False
    if isinstance(missing, (bool, np.bool_)) and bool(missing):
        return None
    return value


def _canonical_value(value: object) -> object:
    value = _null_value(value)
    if value is None:
        return None
    if isinstance(value, BaseGeometry):
        dimension = int(get_coordinate_dimension(value))
        if dimension != 2:
            raise BessPlanningFeatureParcelAggregationError(
                "Parcel aggregation geometry must be canonical 2D"
            )
        return {
            "coordinate_dimension": dimension,
            "wkb_hex": to_wkb(
                value, hex=True, output_dimension=2, byte_order=1, include_srid=False
            ),
        }
    if isinstance(value, (datetime, date, pd.Timestamp)):
        return value.isoformat()
    if isinstance(value, np.generic):
        return _canonical_value(value.item())
    if isinstance(value, bool):
        return value
    if isinstance(value, Integral):
        return int(value)
    if isinstance(value, Real):
        number = float(value)
        if not math.isfinite(number):
            raise BessPlanningFeatureParcelAggregationError(
                "Aggregation payload contains non-finite data"
            )
        return number
    if isinstance(value, str):
        return value
    raise BessPlanningFeatureParcelAggregationError(
        f"Unsupported aggregation integrity value {type(value).__name__}"
    )


def _frame_payload(frame: pd.DataFrame) -> dict[str, object]:
    return {
        "schema": deterministic_frame_schema_signature(frame),
        "index": [_canonical_value(value) for value in frame.index.tolist()],
        "rows": [
            [_canonical_value(value) for value in row]
            for row in frame.itertuples(index=False, name=None)
        ],
    }


def _canonical_sha256(value: object) -> str:
    try:
        payload = json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except (TypeError, ValueError) as error:
        raise BessPlanningFeatureParcelAggregationError(
            "Aggregation payload is not canonical JSON"
        ) from error
    return sha256(payload).hexdigest()


def _frame_sha256(frame: pd.DataFrame, domain: str) -> str:
    return _canonical_sha256(
        {
            "domain": domain,
            "result_hash_schema_version": RESULT_HASH_SCHEMA_VERSION,
            "frame": _frame_payload(frame),
        }
    )


def _validate_feature_id(value: object) -> str:
    if (
        not isinstance(value, str)
        or not value
        or value != value.strip()
        or value in NULL_LITERALS
        or PurePosixPath(value).is_absolute()
        or PureWindowsPath(value).is_absolute()
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "Feature ID is not an exact portable string"
        )
    return value


def _json_ids(values: list[object]) -> str:
    ids = sorted({_validate_feature_id(value) for value in values})
    return json.dumps(ids, ensure_ascii=False, allow_nan=False, separators=(",", ":"))


def _validate_json_ids(value: object, label: str) -> None:
    if not isinstance(value, str):
        raise BessPlanningFeatureParcelAggregationError(
            f"{label} must be canonical JSON"
        )
    try:
        parsed = json.loads(value)
    except (TypeError, ValueError) as error:
        raise BessPlanningFeatureParcelAggregationError(
            f"{label} must be canonical JSON"
        ) from error
    if not isinstance(parsed, list):
        raise BessPlanningFeatureParcelAggregationError(f"{label} must be a JSON array")
    ids = [_validate_feature_id(item) for item in parsed]
    canonical = json.dumps(
        sorted(set(ids)),
        ensure_ascii=False,
        allow_nan=False,
        separators=(",", ":"),
    )
    if len(ids) != len(set(ids)) or ids != sorted(ids) or value != canonical:
        raise BessPlanningFeatureParcelAggregationError(f"{label} is not canonical")


def _validate_parcel_frame(frame: object, label: str) -> gpd.GeoDataFrame:
    if not isinstance(frame, gpd.GeoDataFrame):
        raise BessPlanningFeatureParcelAggregationError(
            f"{label} must be a GeoDataFrame"
        )
    if frame.columns.duplicated().any():
        raise BessPlanningFeatureParcelAggregationError(
            f"{label} contains duplicate columns"
        )
    if "parcel_id" not in frame.columns:
        raise BessPlanningFeatureParcelAggregationError(f"{label} lacks parcel_id")
    try:
        geometry_name = frame.geometry.name
        if geometry_name not in frame.columns:
            raise ValueError("active geometry column is absent")
        if frame.crs is None:
            raise ValueError("CRS is absent")
        CRS.from_user_input(frame.crs)
    except Exception as error:
        raise BessPlanningFeatureParcelAggregationError(
            f"{label} geometry or CRS contract is invalid"
        ) from error
    parcel_ids = frame["parcel_id"]
    if (
        parcel_ids.isna().any()
        or parcel_ids.duplicated().any()
        or any(
            not isinstance(value, str) or not value or value != value.strip()
            for value in parcel_ids
        )
    ):
        raise BessPlanningFeatureParcelAggregationError(
            f"{label} parcel IDs must be unique exact strings"
        )
    for geometry in frame.geometry.array:
        if (
            geometry is None
            or geometry.is_empty
            or not geometry.is_valid
            or geometry.geom_type not in {"Polygon", "MultiPolygon"}
            or int(get_coordinate_dimension(geometry)) != 2
        ):
            raise BessPlanningFeatureParcelAggregationError(
                f"{label} requires valid canonical 2D polygon geometry"
            )
    return frame


def _validate_application_relations(
    frame: object,
    application: BessPlanningFeatureApplicationResult | _ApplicationLineage,
) -> pd.DataFrame:
    if not isinstance(frame, pd.DataFrame) or isinstance(frame, gpd.GeoDataFrame):
        raise BessPlanningFeatureParcelAggregationError(
            "Application relations must be a DataFrame"
        )
    try:
        validate_bess_application_relation_frame(
            frame,
            label="application relations",
            policy_profile=application.policy_profile,
            policy_sha256=application.policy_sha256,
            policy_result_sha256=application.policy_complete_result_content_sha256,
        )
    except ValueError as error:
        raise BessPlanningFeatureParcelAggregationError(str(error)) from error
    return frame


def _validate_local_domains(parcels: gpd.GeoDataFrame, relations: pd.DataFrame) -> None:
    for row in parcels.to_dict("records"):
        aggregation_status = row["bess_cnig_parcel_aggregation_status"]
        if aggregation_status not in AGGREGATION_STATUSES:
            raise BessPlanningFeatureParcelAggregationError(
                "parcel aggregation status is outside the allowed domain"
            )
        status = _null_value(row["bess_cnig_parcel_precheck_status"])
        confidence = _null_value(row["bess_cnig_parcel_precheck_confidence"])
        priority = _null_value(row["bess_cnig_parcel_status_priority"])
        if aggregation_status == "AGGREGATED_EXACT_POLICY":
            if status not in ALLOWED_PRECHECK_STATUSES:
                raise BessPlanningFeatureParcelAggregationError(
                    "parcel precheck status is outside the allowed domain"
                )
            if confidence not in ALLOWED_CONFIDENCES:
                raise BessPlanningFeatureParcelAggregationError(
                    "parcel confidence is outside the allowed domain"
                )
            if (
                isinstance(priority, bool)
                or not isinstance(priority, Integral)
                or int(priority) <= 0
            ):
                raise BessPlanningFeatureParcelAggregationError(
                    "parcel status priority must be a positive integer"
                )
        elif any(value is not None for value in (status, confidence, priority)):
            raise BessPlanningFeatureParcelAggregationError(
                "non-decision parcel contains an invented decision"
            )
        for column in (
            "bess_cnig_selected_feature_ids_json",
            "bess_cnig_unresolved_feature_ids_json",
            "bess_cnig_touch_only_feature_ids_json",
        ):
            _validate_json_ids(row[column], column)
    for row in relations.to_dict("records"):
        role = row["bess_cnig_parcel_relation_role"]
        if role not in RELATION_ROLES:
            raise BessPlanningFeatureParcelAggregationError(
                "parcel relation role is outside the allowed domain"
            )
        selected = row["bess_cnig_selected_for_parcel_status"]
        if selected is not (role == "SELECTED_CONTROLLING"):
            raise BessPlanningFeatureParcelAggregationError(
                "parcel relation selected flag contradicts its role"
            )
        aggregation_status = row["bess_cnig_resulting_parcel_aggregation_status"]
        if aggregation_status not in AGGREGATION_STATUSES:
            raise BessPlanningFeatureParcelAggregationError(
                "relation aggregation status is outside the allowed domain"
            )
        status = _null_value(row["bess_cnig_resulting_parcel_precheck_status"])
        confidence = _null_value(row["bess_cnig_resulting_parcel_precheck_confidence"])
        priority = _null_value(row["bess_cnig_resulting_parcel_status_priority"])
        if aggregation_status == "AGGREGATED_EXACT_POLICY":
            if status not in ALLOWED_PRECHECK_STATUSES:
                raise BessPlanningFeatureParcelAggregationError(
                    "relation parcel status is outside the allowed domain"
                )
            if confidence not in ALLOWED_CONFIDENCES:
                raise BessPlanningFeatureParcelAggregationError(
                    "relation parcel confidence is outside the allowed domain"
                )
            if (
                isinstance(priority, bool)
                or not isinstance(priority, Integral)
                or int(priority) <= 0
            ):
                raise BessPlanningFeatureParcelAggregationError(
                    "relation parcel priority must be a positive integer"
                )
        elif any(value is not None for value in (status, confidence, priority)):
            raise BessPlanningFeatureParcelAggregationError(
                "non-decision relation contains an invented parcel decision"
            )


def _relation_priority(row: dict[str, object]) -> int:
    value = row["bess_cnig_status_priority"]
    if isinstance(value, bool) or not isinstance(value, Integral) or int(value) <= 0:
        raise BessPlanningFeatureParcelAggregationError(
            "Applied relation priority must be a positive integer"
        )
    return int(value)


def _parcel_summary(
    parcel_relations: list[dict[str, object]],
    application: BessPlanningFeatureApplicationResult | _ApplicationLineage,
) -> tuple[dict[str, object], list[dict[str, object]]]:
    controlling = [
        row
        for row in parcel_relations
        if row["relation_type"] in CONTROLLING_RELATION_TYPES
    ]
    contextual = [
        row
        for row in parcel_relations
        if row["relation_type"] in CONTEXT_RELATION_TYPES
    ]
    if len(controlling) + len(contextual) != len(parcel_relations):
        raise BessPlanningFeatureParcelAggregationError(
            "Relation type is outside the aggregation contract"
        )
    exact = [
        row
        for row in controlling
        if row["bess_cnig_policy_application_status"] == "APPLIED_EXACT_POLICY"
    ]
    unresolved = [
        row
        for row in controlling
        if row["bess_cnig_policy_application_status"] == "UNRESOLVED_CODE_PAIR"
    ]
    if len(exact) + len(unresolved) != len(controlling):
        raise BessPlanningFeatureParcelAggregationError(
            "Controlling application status is invalid"
        )
    selected_status: str | None = None
    selected_confidence: str | None = None
    selected_priority: int | None = None
    priorities: list[int] = []
    priority_statuses: dict[int, set[str]] = {}
    status_priorities: dict[str, set[int]] = {}
    for row in exact:
        priority = row["bess_cnig_status_priority"]
        status = row["bess_cnig_precheck_status"]
        if (
            isinstance(priority, bool)
            or not isinstance(priority, Integral)
            or int(priority) <= 0
            or not isinstance(status, str)
        ):
            raise BessPlanningFeatureParcelAggregationError(
                "Applied relation status and priority are invalid"
            )
        normalized_priority = int(priority)
        priorities.append(normalized_priority)
        priority_statuses.setdefault(normalized_priority, set()).add(status)
        status_priorities.setdefault(status, set()).add(normalized_priority)
    if any(len(statuses) != 1 for statuses in priority_statuses.values()) or any(
        len(priority_values) != 1 for priority_values in status_priorities.values()
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "Applied relation status and priority mapping is not one-to-one"
        )
    if unresolved:
        aggregation_status = "UNRESOLVED_CONTROLLING_CODE_PAIR"
    elif controlling:
        aggregation_status = "AGGREGATED_EXACT_POLICY"
        selected_priority = max(priorities)
        selected_status = next(iter(priority_statuses[selected_priority]))
        confidences = [
            str(row["bess_cnig_precheck_confidence"])
            for row in exact
            if row["bess_cnig_precheck_status"] == selected_status
            and _relation_priority(row) == selected_priority
        ]
        if any(value not in CONFIDENCE_RANK for value in confidences):
            raise BessPlanningFeatureParcelAggregationError(
                "Selected relation confidence is invalid"
            )
        selected_confidence = min(confidences, key=CONFIDENCE_RANK.__getitem__)
    elif parcel_relations:
        aggregation_status = "TOUCH_ONLY_RELATIONS_ONLY"
    else:
        aggregation_status = "NO_PLANNING_FEATURE_RELATION"

    assessed: list[dict[str, object]] = []
    for row in parcel_relations:
        if row["relation_type"] in CONTEXT_RELATION_TYPES:
            role = "TOUCH_ONLY_CONTEXT"
        elif aggregation_status == "UNRESOLVED_CONTROLLING_CODE_PAIR":
            role = (
                "UNRESOLVED_CONTROLLING"
                if row["bess_cnig_policy_application_status"] == "UNRESOLVED_CODE_PAIR"
                else "DEFERRED_BY_UNRESOLVED_CONTROLLING"
            )
        else:
            role = (
                "SELECTED_CONTROLLING"
                if row["bess_cnig_precheck_status"] == selected_status
                and _relation_priority(row) == selected_priority
                else "LOWER_PRIORITY_CONTROLLING"
            )
        assessed.append(
            {
                **row,
                "bess_cnig_parcel_relation_role": role,
                "bess_cnig_selected_for_parcel_status": role == "SELECTED_CONTROLLING",
                "bess_cnig_resulting_parcel_aggregation_status": aggregation_status,
                "bess_cnig_resulting_parcel_precheck_status": selected_status,
                "bess_cnig_resulting_parcel_precheck_confidence": selected_confidence,
                "bess_cnig_resulting_parcel_status_priority": selected_priority,
            }
        )
    roles = [row["bess_cnig_parcel_relation_role"] for row in assessed]
    exact_statuses = {str(row["bess_cnig_precheck_status"]) for row in exact}
    summary: dict[str, object] = {
        "bess_cnig_parcel_aggregation_status": aggregation_status,
        "bess_cnig_parcel_precheck_status": selected_status,
        "bess_cnig_parcel_precheck_confidence": selected_confidence,
        "bess_cnig_parcel_status_priority": selected_priority,
        "bess_cnig_controlling_relation_count": len(controlling),
        "bess_cnig_exact_controlling_relation_count": len(exact),
        "bess_cnig_unresolved_controlling_relation_count": len(unresolved),
        "bess_cnig_touch_only_relation_count": len(contextual),
        "bess_cnig_selected_relation_count": roles.count("SELECTED_CONTROLLING"),
        "bess_cnig_lower_priority_controlling_relation_count": roles.count(
            "LOWER_PRIORITY_CONTROLLING"
        ),
        "bess_cnig_distinct_exact_status_count": len(exact_statuses),
        "bess_cnig_multiple_exact_statuses": len(exact_statuses) > 1,
        "bess_cnig_selected_feature_ids_json": _json_ids(
            [
                row["planning_feature_id"]
                for row in assessed
                if row["bess_cnig_parcel_relation_role"] == "SELECTED_CONTROLLING"
            ]
        ),
        "bess_cnig_unresolved_feature_ids_json": _json_ids(
            [
                row["planning_feature_id"]
                for row in assessed
                if row["bess_cnig_parcel_relation_role"] == "UNRESOLVED_CONTROLLING"
            ]
        ),
        "bess_cnig_touch_only_feature_ids_json": _json_ids(
            [
                row["planning_feature_id"]
                for row in assessed
                if row["bess_cnig_parcel_relation_role"] == "TOUCH_ONLY_CONTEXT"
            ]
        ),
        "bess_cnig_confidence_aggregation_method": CONFIDENCE_METHOD,
        "bess_cnig_formal_review_required": True,
        "bess_cnig_aggregation_scope": AGGREGATION_SCOPE,
        "bess_cnig_policy_scope": POLICY_SCOPE,
        "bess_cnig_local_feature_text_interpreted": False,
        "bess_cnig_local_regulation_content_interpreted": False,
        "bess_cnig_legal_conclusion_produced": False,
        "bess_cnig_parcel_status_aggregated": True,
        "bess_cnig_parcel_rejection_performed": False,
        "bess_cnig_score_calculated": False,
        "bess_cnig_policy_profile": application.policy_profile,
        "bess_cnig_policy_sha256": application.policy_sha256,
        "bess_cnig_policy_result_sha256": application.policy_complete_result_content_sha256,
        "bess_cnig_application_result_sha256": application.complete_result_content_sha256,
    }
    return summary, assessed


def _assign_columns(
    frame: pd.DataFrame, rows: list[dict[str, object]], columns: tuple[str, ...]
) -> pd.DataFrame:
    for column in columns:
        values = [row[column] for row in rows]
        if (
            column in PARCEL_INTEGER_COLUMNS
            or column == "bess_cnig_resulting_parcel_status_priority"
        ):
            frame[column] = pd.array(values, dtype="Int64")
        elif (
            column in PARCEL_BOOL_COLUMNS
            or column == "bess_cnig_selected_for_parcel_status"
        ):
            frame[column] = pd.array(values, dtype="bool")
        else:
            frame[column] = pd.array(values, dtype="str")
    return frame


def _aggregate_frames(
    source_parcels: gpd.GeoDataFrame,
    source_relations: pd.DataFrame,
    application: BessPlanningFeatureApplicationResult | _ApplicationLineage,
) -> tuple[gpd.GeoDataFrame, pd.DataFrame]:
    _validate_parcel_frame(source_parcels, "source parcels")
    _validate_application_relations(source_relations, application)
    if any(column in source_parcels.columns for column in PARCEL_COLUMNS) or any(
        column in source_relations.columns for column in RELATION_COLUMNS
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "Aggregation columns already exist on source inputs"
        )
    if "parcel_id" not in source_parcels or "parcel_id" not in source_relations:
        raise BessPlanningFeatureParcelAggregationError(
            "Aggregation inputs lack parcel_id"
        )
    parcel_ids = source_parcels["parcel_id"]
    known = set(parcel_ids.tolist())
    if any(value not in known for value in source_relations["parcel_id"]):
        raise BessPlanningFeatureParcelAggregationError(
            "Relation references an unknown parcel"
        )
    relation_rows = source_relations.to_dict("records")
    grouped: dict[str, list[dict[str, object]]] = {
        value: [] for value in parcel_ids.tolist()
    }
    for row in relation_rows:
        grouped[str(row["parcel_id"])].append(row)
    summaries: list[dict[str, object]] = []
    assessment_rows: list[dict[str, object]] = []
    for parcel_id in parcel_ids.tolist():
        summary, assessed = _parcel_summary(grouped[parcel_id], application)
        summaries.append(summary)
        assessment_rows.extend(assessed)
    parcels = source_parcels.copy(deep=True)
    _assign_columns(parcels, summaries, PARCEL_COLUMNS)
    parcels = gpd.GeoDataFrame(
        parcels, geometry=source_parcels.geometry.name, crs=source_parcels.crs
    )
    assessments = source_relations.copy(deep=True)
    # assessed rows were grouped by parcel; restore exact source relation order by stable source position.
    cursor: dict[str, int] = {parcel_id: 0 for parcel_id in grouped}
    assessed_by_parcel: dict[str, list[dict[str, object]]] = {
        parcel_id: [] for parcel_id in grouped
    }
    for row in assessment_rows:
        assessed_by_parcel[str(row["parcel_id"])].append(row)
    ordered_assessed: list[dict[str, object]] = []
    for source_row in relation_rows:
        parcel_id = str(source_row["parcel_id"])
        item = assessed_by_parcel[parcel_id][cursor[parcel_id]]
        cursor[parcel_id] += 1
        ordered_assessed.append(item)
    _assign_columns(assessments, ordered_assessed, RELATION_COLUMNS)
    return parcels, assessments


def _component_metadata(
    result: BessPlanningFeatureParcelAggregationResult,
) -> dict[str, object]:
    return {
        field: getattr(result, field)
        for field in RESULT_SCALAR_FIELDS
        if field
        not in {
            "relation_assessments_content_sha256",
            "parcels_content_sha256",
            "complete_result_content_sha256",
        }
    }


def _result_with_hashes(
    result: BessPlanningFeatureParcelAggregationResult,
) -> BessPlanningFeatureParcelAggregationResult:
    metadata = _component_metadata(result)
    relations_hash = _canonical_sha256(
        {
            "domain": "landscout.bess_cnig_parcel_aggregation.relation_assessments",
            **metadata,
            "frame": _frame_payload(result.relation_assessments),
        }
    )
    parcels_hash = _canonical_sha256(
        {
            "domain": "landscout.bess_cnig_parcel_aggregation.parcels",
            **metadata,
            "frame": _frame_payload(result.parcels),
        }
    )
    components = replace(
        result,
        relation_assessments_content_sha256=relations_hash,
        parcels_content_sha256=parcels_hash,
    )
    complete = _canonical_sha256(
        {
            "domain": "landscout.bess_cnig_parcel_aggregation.result",
            **metadata,
            "relation_assessments_content_sha256": relations_hash,
            "parcels_content_sha256": parcels_hash,
        }
    )
    return replace(components, complete_result_content_sha256=complete)


def _build_result(
    source_parcels: gpd.GeoDataFrame,
    application: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureParcelAggregationResult:
    parcels, assessments = _aggregate_frames(
        source_parcels, application.relations, application
    )
    result = BessPlanningFeatureParcelAggregationResult(
        result_hash_schema_version=RESULT_HASH_SCHEMA_VERSION,
        aggregation_scope=AGGREGATION_SCOPE,
        policy_scope=POLICY_SCOPE,
        local_feature_text_interpreted=False,
        local_regulation_content_interpreted=False,
        legal_conclusion_produced=False,
        parcel_status_aggregated=True,
        parcel_rejection_performed=False,
        score_calculated=False,
        source_document_id=application.source_document_id,
        source_archive_sha256=application.source_archive_sha256,
        cnig_profile=application.cnig_profile,
        cnig_profile_sha256=application.cnig_profile_sha256,
        cnig_complete_result_content_sha256=application.cnig_complete_result_content_sha256,
        policy_profile=application.policy_profile,
        policy_sha256=application.policy_sha256,
        policy_complete_result_content_sha256=application.policy_complete_result_content_sha256,
        application_result_hash_schema_version=application.result_hash_schema_version,
        application_complete_result_content_sha256=application.complete_result_content_sha256,
        source_parcels_content_sha256=_frame_sha256(
            source_parcels, "landscout.bess_cnig_parcel_aggregation.source_parcels"
        ),
        source_application_relations_content_sha256=_frame_sha256(
            application.relations,
            "landscout.bess_cnig_parcel_aggregation.source_application_relations",
        ),
        relation_assessments_content_sha256="",
        parcels_content_sha256="",
        complete_result_content_sha256="",
        relation_assessments=assessments,
        parcels=parcels,
    )
    return _result_with_hashes(result)


def _compare_frame(actual: pd.DataFrame, expected: pd.DataFrame, label: str) -> None:
    if _frame_payload(actual) != _frame_payload(expected):
        raise BessPlanningFeatureParcelAggregationError(
            f"{label} differs from deterministic aggregation"
        )


def _validate_result_envelope(
    result: BessPlanningFeatureParcelAggregationResult,
) -> None:
    if not isinstance(result, BessPlanningFeatureParcelAggregationResult):
        raise BessPlanningFeatureParcelAggregationError("result has the wrong type")
    if (
        type(result.result_hash_schema_version) is not int
        or result.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "unsupported parcel aggregation result schema"
        )
    if (
        result.aggregation_scope != AGGREGATION_SCOPE
        or result.policy_scope != POLICY_SCOPE
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "parcel aggregation scope is invalid"
        )
    for field in RESULT_SCALAR_FIELDS:
        if field.endswith("sha256"):
            try:
                _sha256_string(getattr(result, field), field)
            except ValueError as error:
                raise BessPlanningFeatureParcelAggregationError(str(error)) from error
    for value, label in (
        (result.source_document_id, "source_document_id"),
        (result.cnig_profile, "cnig_profile"),
        (result.policy_profile, "policy_profile"),
    ):
        try:
            _exact_string(value, label)
        except ValueError as error:
            raise BessPlanningFeatureParcelAggregationError(str(error)) from error
    if (
        type(result.application_result_hash_schema_version) is not int
        or result.application_result_hash_schema_version
        != APPLICATION_RESULT_HASH_SCHEMA_VERSION
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "application result schema must be exactly 2"
        )
    if any(
        value is not expected
        for value, expected in (
            (result.local_feature_text_interpreted, False),
            (result.local_regulation_content_interpreted, False),
            (result.legal_conclusion_produced, False),
            (result.parcel_status_aggregated, True),
            (result.parcel_rejection_performed, False),
            (result.score_calculated, False),
        )
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "parcel aggregation flags are invalid"
        )
    if (
        not isinstance(result.parcels, gpd.GeoDataFrame)
        or not isinstance(result.relation_assessments, pd.DataFrame)
        or isinstance(result.relation_assessments, gpd.GeoDataFrame)
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "aggregation output frame types are invalid"
        )
    if result.parcels.columns.duplicated().any():
        raise BessPlanningFeatureParcelAggregationError(
            "parcel output contains duplicate columns"
        )
    if result.relation_assessments.columns.duplicated().any():
        raise BessPlanningFeatureParcelAggregationError(
            "relation assessments contain duplicate columns"
        )
    if (
        tuple(result.parcels.columns[-len(PARCEL_COLUMNS) :]) != PARCEL_COLUMNS
        or tuple(result.relation_assessments.columns[-len(RELATION_COLUMNS) :])
        != RELATION_COLUMNS
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "aggregation output suffix schema is invalid"
        )
    for column in PARCEL_STRING_COLUMNS:
        if str(result.parcels[column].dtype) != "str":
            raise BessPlanningFeatureParcelAggregationError(
                "parcel aggregation string dtype is invalid"
            )
    for column in PARCEL_INTEGER_COLUMNS:
        if str(result.parcels[column].dtype) != "Int64":
            raise BessPlanningFeatureParcelAggregationError(
                "parcel aggregation integer dtype is invalid"
            )
    for column in PARCEL_BOOL_COLUMNS:
        if str(result.parcels[column].dtype) != "bool":
            raise BessPlanningFeatureParcelAggregationError(
                "parcel aggregation bool dtype is invalid"
            )
    for column in RELATION_STRING_COLUMNS:
        if str(result.relation_assessments[column].dtype) != "str":
            raise BessPlanningFeatureParcelAggregationError(
                "relation assessment string dtype is invalid"
            )
    if (
        str(result.relation_assessments["bess_cnig_selected_for_parcel_status"].dtype)
        != "bool"
        or str(
            result.relation_assessments[
                "bess_cnig_resulting_parcel_status_priority"
            ].dtype
        )
        != "Int64"
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "relation assessment dtype is invalid"
        )
    _validate_parcel_frame(result.parcels, "parcel output")
    _validate_local_domains(result.parcels, result.relation_assessments)
    source_parcels = result.parcels.drop(columns=list(PARCEL_COLUMNS))
    source_parcels = gpd.GeoDataFrame(
        source_parcels, geometry=result.parcels.geometry.name, crs=result.parcels.crs
    )
    source_relations = result.relation_assessments.drop(columns=list(RELATION_COLUMNS))
    if result.source_parcels_content_sha256 != _frame_sha256(
        source_parcels, "landscout.bess_cnig_parcel_aggregation.source_parcels"
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "source parcel content SHA256 is invalid"
        )
    if result.source_application_relations_content_sha256 != _frame_sha256(
        source_relations,
        "landscout.bess_cnig_parcel_aggregation.source_application_relations",
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "source application relation content SHA256 is invalid"
        )
    lineage = _ApplicationLineage(
        policy_profile=result.policy_profile,
        policy_sha256=result.policy_sha256,
        policy_complete_result_content_sha256=result.policy_complete_result_content_sha256,
        complete_result_content_sha256=result.application_complete_result_content_sha256,
    )
    _validate_application_relations(source_relations, lineage)
    expected_parcels, expected_relations = _aggregate_frames(
        source_parcels, source_relations, lineage
    )
    _compare_frame(result.parcels, expected_parcels, "parcel output")
    _compare_frame(
        result.relation_assessments, expected_relations, "relation assessments"
    )
    rebuilt = _result_with_hashes(result)
    for field in (
        "relation_assessments_content_sha256",
        "parcels_content_sha256",
        "complete_result_content_sha256",
    ):
        if getattr(result, field) != getattr(rebuilt, field):
            raise BessPlanningFeatureParcelAggregationError(f"{field} is invalid")


def _validate_source_locks(
    result: BessPlanningFeatureParcelAggregationResult,
    source_parcels: gpd.GeoDataFrame,
    application: BessPlanningFeatureApplicationResult,
) -> None:
    comparisons = (
        (result.source_document_id, application.source_document_id),
        (result.source_archive_sha256, application.source_archive_sha256),
        (result.cnig_profile, application.cnig_profile),
        (result.cnig_profile_sha256, application.cnig_profile_sha256),
        (
            result.cnig_complete_result_content_sha256,
            application.cnig_complete_result_content_sha256,
        ),
        (result.policy_profile, application.policy_profile),
        (result.policy_sha256, application.policy_sha256),
        (
            result.policy_complete_result_content_sha256,
            application.policy_complete_result_content_sha256,
        ),
        (
            result.application_result_hash_schema_version,
            application.result_hash_schema_version,
        ),
        (
            result.application_complete_result_content_sha256,
            application.complete_result_content_sha256,
        ),
        (
            result.source_application_relations_content_sha256,
            _frame_sha256(
                application.relations,
                "landscout.bess_cnig_parcel_aggregation.source_application_relations",
            ),
        ),
        (
            result.source_parcels_content_sha256,
            _frame_sha256(
                source_parcels, "landscout.bess_cnig_parcel_aggregation.source_parcels"
            ),
        ),
    )
    if any(actual != expected for actual, expected in comparisons):
        raise BessPlanningFeatureParcelAggregationError(
            "parcel aggregation source lock differs"
        )


def _validate_application_source(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
    policy_config: BessPlanningFeaturePolicyConfig | str | Path,
    policy_result: BessPlanningFeaturePolicyResult,
    application_result: BessPlanningFeatureApplicationResult,
) -> None:
    try:
        validate_bess_planning_feature_application_result(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
            code_profile,
            coded_result,
            policy_config,
            policy_result,
            application_result,
        )
    except Exception as error:
        raise BessPlanningFeatureParcelAggregationError(
            "Source-complete application validation failed"
        ) from error


def aggregate_bess_planning_feature_policy_to_parcels(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
    policy_config: BessPlanningFeaturePolicyConfig | str | Path,
    policy_result: BessPlanningFeaturePolicyResult,
    application_result: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureParcelAggregationResult:
    """Validate the application once and aggregate its relations to every parcel."""
    try:
        _validate_application_source(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
            code_profile,
            coded_result,
            policy_config,
            policy_result,
            application_result,
        )
        result = _build_result(parcels, application_result)
        _validate_result_envelope(result)
        return result
    except BessPlanningFeatureParcelAggregationError:
        raise
    except Exception as error:
        raise BessPlanningFeatureParcelAggregationError(
            "Parcel aggregation failed safely"
        ) from error


def validate_bess_planning_feature_parcel_aggregation_result(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
    policy_config: BessPlanningFeaturePolicyConfig | str | Path,
    policy_result: BessPlanningFeaturePolicyResult,
    application_result: BessPlanningFeatureApplicationResult,
    result: BessPlanningFeatureParcelAggregationResult,
) -> None:
    """Independently validate and rebuild one persisted parcel aggregation result."""
    try:
        _validate_result_envelope(result)
        _validate_source_locks(result, parcels, application_result)
        _validate_application_source(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
            code_profile,
            coded_result,
            policy_config,
            policy_result,
            application_result,
        )
        expected = _build_result(parcels, application_result)
        for field in RESULT_SCALAR_FIELDS:
            if getattr(result, field) != getattr(expected, field):
                raise BessPlanningFeatureParcelAggregationError(
                    f"Aggregation {field} differs"
                )
        _compare_frame(result.parcels, expected.parcels, "parcels")
        _compare_frame(
            result.relation_assessments, expected.relation_assessments, "relations"
        )
    except BessPlanningFeatureParcelAggregationError:
        raise
    except Exception as error:
        raise BessPlanningFeatureParcelAggregationError(
            "Parcel aggregation result validation failed safely"
        ) from error


def _unique_json_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    output: dict[str, object] = {}
    for key, value in pairs:
        if key in output:
            raise BessPlanningFeatureParcelAggregationError(
                f"Duplicate JSON aggregation artifact key: {key!r}"
            )
        output[key] = value
    return output


def _read_verified_artifact(
    path: Path, record: BessPlanningFeatureParcelAggregationArtifactRecord
) -> pd.DataFrame:
    if path.name != record.filename:
        raise BessPlanningFeatureParcelAggregationError(
            "Aggregation artifact filename differs"
        )
    payload = path.read_bytes()
    if len(payload) != record.size_bytes:
        raise BessPlanningFeatureParcelAggregationError(
            "Aggregation artifact byte size differs"
        )
    if sha256(payload).hexdigest() != record.sha256:
        raise BessPlanningFeatureParcelAggregationError(
            "Aggregation artifact SHA256 differs"
        )
    buffer = BytesIO(payload)
    frame: pd.DataFrame = (
        gpd.read_parquet(buffer) if record.geospatial else pd.read_parquet(buffer)
    )
    if len(frame) != record.row_count:
        raise BessPlanningFeatureParcelAggregationError(
            "Aggregation artifact row count differs"
        )
    if deterministic_frame_schema_signature(frame) != record.frame_schema_signature:
        raise BessPlanningFeatureParcelAggregationError(
            "Aggregation artifact frame schema differs"
        )
    if record.geospatial:
        if (
            not isinstance(frame, gpd.GeoDataFrame)
            or frame.crs is None
            or CRS.from_user_input(frame.crs).to_json_dict() != record.crs
        ):
            raise BessPlanningFeatureParcelAggregationError(
                "Aggregation parcel artifact CRS differs"
            )
    elif isinstance(frame, gpd.GeoDataFrame):
        raise BessPlanningFeatureParcelAggregationError(
            "Relation assessment artifact is unexpectedly geospatial"
        )
    return frame


def load_bess_planning_feature_parcel_aggregation_artifacts(
    manifest_path: str | Path,
    parcels_path: str | Path,
    relation_assessments_path: str | Path,
) -> BessPlanningFeatureParcelAggregationResult:
    """Load the two byte-verified aggregation artifacts and validate locally."""
    try:
        payload = json.loads(
            Path(manifest_path).read_text(encoding="utf-8"),
            object_pairs_hook=_unique_json_object,
        )
        manifest = BessPlanningFeatureParcelAggregationArtifactManifest.model_validate(
            payload
        )
        records = {record.artifact_role: record for record in manifest.artifacts}
        loaded_parcels = _read_verified_artifact(Path(parcels_path), records["PARCELS"])
        loaded_relations = _read_verified_artifact(
            Path(relation_assessments_path), records["RELATION_ASSESSMENTS"]
        )
        if not isinstance(loaded_parcels, gpd.GeoDataFrame):
            raise BessPlanningFeatureParcelAggregationError(
                "Parcel artifact is not geospatial"
            )
        result = BessPlanningFeatureParcelAggregationResult(
            **{field: getattr(manifest, field) for field in RESULT_SCALAR_FIELDS},
            parcels=loaded_parcels,
            relation_assessments=loaded_relations,
        )
        _validate_result_envelope(result)
        return result
    except BessPlanningFeatureParcelAggregationError:
        raise
    except Exception as error:
        raise BessPlanningFeatureParcelAggregationError(
            f"Parcel aggregation artifacts are invalid: {error}"
        ) from error

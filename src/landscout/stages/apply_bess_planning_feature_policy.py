"""Apply a validated BESS CNIG policy exactly to coded features and relations."""

from __future__ import annotations

import json
import math
import re
from dataclasses import dataclass, replace
from datetime import date, datetime
from hashlib import sha256
from io import BytesIO
from numbers import Integral, Real
from pathlib import Path
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
    APPLICATION_SCOPE,
    FLAG_COLUMNS,
    POLICY_COLUMNS,
    POLICY_SCOPE,
    STRING_POLICY_COLUMNS,
    ApplicationStatus,
    validate_bess_application_feature_catalogs,
    validate_bess_application_relation_frame,
)
from landscout.common.frame_integrity import deterministic_frame_schema_signature
from landscout.common.planning_overlay import technical_overlay_tolerance
from landscout.sources.gpu_fr import GpuPlanningDocument
from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
    validate_bess_planning_feature_policy_result,
)
from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
)

__all__ = [
    "BessPlanningFeatureApplicationArtifactManifest",
    "BessPlanningFeatureApplicationError",
    "BessPlanningFeatureApplicationResult",
    "apply_bess_planning_feature_policy",
    "load_bess_planning_feature_application_artifacts",
    "validate_bess_planning_feature_application_result",
]

RESULT_HASH_SCHEMA_VERSION = 2
ARTIFACT_MANIFEST_SCHEMA_VERSION = 2
ARTIFACT_KIND = "BESS_PLANNING_FEATURE_POLICY_APPLICATION_RESULT"

ArtifactRole = Literal[
    "SURFACE_FEATURES",
    "LINE_FEATURES",
    "POINT_FEATURES",
    "RELATIONS",
]

ARTIFACT_ROLES: tuple[ArtifactRole, ...] = (
    "SURFACE_FEATURES",
    "LINE_FEATURES",
    "POINT_FEATURES",
    "RELATIONS",
)
RELATION_FEATURE_AGREEMENT_COLUMNS = (
    "source_feature_id",
    "source_identity_kind",
    "source_identity_field",
    "logical_layer",
    "feature_family",
    "geometry_kind",
    "type_code_raw",
    "subtype_code_raw",
    "label_raw",
    "text_raw",
    "source_document_id",
    "source_archive_sha256",
    "source_layer",
    "source_validity_date_raw",
    "regulation_filename_raw",
    "official_code_status",
    "official_code_label",
    "official_legal_reference",
    "official_regulation_reference",
    "official_code_source_url",
    "official_code_profile",
    "official_code_profile_sha256",
)
SHA_PATTERN = re.compile(r"[0-9a-f]{64}")
CODE_PATTERN = re.compile(r"[0-9]{2}")


class BessPlanningFeatureApplicationError(ValueError):
    """Raised when exact feature-policy propagation cannot be proven."""


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


class BessPlanningFeatureApplicationArtifactRecord(_StrictModel):
    """One physical output record within the application manifest."""

    artifact_role: ArtifactRole
    filename: StrictStr
    row_count: StrictInt
    size_bytes: StrictInt
    sha256: StrictStr
    frame_schema_signature: dict[StrictStr, object]
    geospatial: StrictBool
    crs: dict[StrictStr, object] | None

    @model_validator(mode="after")
    def _validate_record(self) -> BessPlanningFeatureApplicationArtifactRecord:
        _exact_string(self.filename, "artifact filename")
        path = Path(self.filename)
        if (
            path.is_absolute()
            or path.name != self.filename
            or path.suffix.lower() != ".parquet"
        ):
            raise ValueError("artifact filename must be one local Parquet filename")
        if type(self.row_count) is not int or self.row_count < 0:
            raise ValueError("artifact row_count must be a non-negative integer")
        if type(self.size_bytes) is not int or self.size_bytes < 1:
            raise ValueError("artifact size_bytes must be a positive integer")
        _sha256_string(self.sha256, "artifact SHA256")
        expected_geospatial = self.artifact_role != "RELATIONS"
        if self.geospatial is not expected_geospatial:
            raise ValueError("artifact geospatial flag differs from its role")
        signature_crs = self.frame_schema_signature.get("crs")
        signature_geometry = self.frame_schema_signature.get("geometry_column")
        if expected_geospatial:
            if self.crs is None or signature_crs != self.crs:
                raise ValueError("geospatial artifact CRS is missing or inconsistent")
            if not isinstance(signature_geometry, str) or not signature_geometry:
                raise ValueError("geospatial artifact geometry column is missing")
        elif self.crs is not None or signature_crs is not None:
            raise ValueError("non-geospatial artifact must not declare a CRS")
        return self


@dataclass(frozen=True)
class BessPlanningFeatureApplicationResult:
    """Immutable exact policy propagation over coded features and relations."""

    result_hash_schema_version: int
    application_scope: str
    policy_scope: str
    local_feature_text_interpreted: bool
    local_regulation_content_interpreted: bool
    legal_conclusion_produced: bool
    parcel_status_aggregated: bool
    parcel_rejection_performed: bool
    score_calculated: bool
    policy_profile: str
    policy_sha256: str
    policy_result_hash_schema_version: int
    policy_complete_result_content_sha256: str
    cnig_profile: str
    cnig_profile_sha256: str
    cnig_result_hash_schema_version: int
    cnig_complete_result_content_sha256: str
    source_document_id: str
    source_archive_sha256: str
    cnig_surface_features_content_sha256: str
    cnig_line_features_content_sha256: str
    cnig_point_features_content_sha256: str
    cnig_relations_content_sha256: str
    surface_features_content_sha256: str
    line_features_content_sha256: str
    point_features_content_sha256: str
    relations_content_sha256: str
    complete_result_content_sha256: str
    surface_features: gpd.GeoDataFrame
    line_features: gpd.GeoDataFrame
    point_features: gpd.GeoDataFrame
    relations: pd.DataFrame


RESULT_FRAME_FIELDS = (
    "surface_features",
    "line_features",
    "point_features",
    "relations",
)
RESULT_SCALAR_FIELDS = tuple(
    field
    for field in BessPlanningFeatureApplicationResult.__dataclass_fields__
    if field not in RESULT_FRAME_FIELDS
)


class BessPlanningFeatureApplicationArtifactManifest(_StrictModel):
    """Strict four-file physical artifact envelope."""

    schema_version: StrictInt
    artifact_kind: Literal["BESS_PLANNING_FEATURE_POLICY_APPLICATION_RESULT"]
    result_hash_schema_version: StrictInt
    application_scope: Literal["FEATURE_AND_RELATION_POLICY_PROPAGATION_ONLY"]
    policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]
    local_feature_text_interpreted: StrictBool
    local_regulation_content_interpreted: StrictBool
    legal_conclusion_produced: StrictBool
    parcel_status_aggregated: StrictBool
    parcel_rejection_performed: StrictBool
    score_calculated: StrictBool
    policy_profile: StrictStr
    policy_sha256: StrictStr
    policy_result_hash_schema_version: StrictInt
    policy_complete_result_content_sha256: StrictStr
    cnig_profile: StrictStr
    cnig_profile_sha256: StrictStr
    cnig_result_hash_schema_version: StrictInt
    cnig_complete_result_content_sha256: StrictStr
    source_document_id: StrictStr
    source_archive_sha256: StrictStr
    cnig_surface_features_content_sha256: StrictStr
    cnig_line_features_content_sha256: StrictStr
    cnig_point_features_content_sha256: StrictStr
    cnig_relations_content_sha256: StrictStr
    surface_features_content_sha256: StrictStr
    line_features_content_sha256: StrictStr
    point_features_content_sha256: StrictStr
    relations_content_sha256: StrictStr
    complete_result_content_sha256: StrictStr
    artifacts: tuple[BessPlanningFeatureApplicationArtifactRecord, ...]

    @model_validator(mode="after")
    def _validate_manifest(self) -> BessPlanningFeatureApplicationArtifactManifest:
        if (
            type(self.schema_version) is not int
            or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION
        ):
            raise ValueError("unsupported application artifact manifest schema")
        if (
            type(self.result_hash_schema_version) is not int
            or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION
        ):
            raise ValueError("unsupported application result hash schema")
        if any(
            value is not False
            for value in (
                self.local_feature_text_interpreted,
                self.local_regulation_content_interpreted,
                self.legal_conclusion_produced,
                self.parcel_status_aggregated,
                self.parcel_rejection_performed,
                self.score_calculated,
            )
        ):
            raise ValueError("application boundary flags must all be false")
        for exact_value, label in (
            (self.policy_profile, "policy_profile"),
            (self.cnig_profile, "cnig_profile"),
            (self.source_document_id, "source_document_id"),
        ):
            _exact_string(exact_value, label)
        if self.policy_result_hash_schema_version != 1:
            raise ValueError("policy result hash schema must be exactly 1")
        if self.cnig_result_hash_schema_version != 5:
            raise ValueError("CNIG result hash schema must be exactly 5")
        for field in RESULT_SCALAR_FIELDS:
            if field.endswith("sha256"):
                _sha256_string(getattr(self, field), field)
        roles = tuple(record.artifact_role for record in self.artifacts)
        if roles != ARTIFACT_ROLES:
            raise ValueError(
                "application artifact roles are missing, extra, or unordered"
            )
        filenames = tuple(record.filename for record in self.artifacts)
        if len(filenames) != len(set(filenames)):
            raise ValueError("application artifact filenames contain a duplicate")
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
        coordinate_dimension = int(get_coordinate_dimension(value))
        if coordinate_dimension != 2:
            raise BessPlanningFeatureApplicationError(
                "Application geometry coordinate dimension must be exactly 2D"
            )
        return {
            "coordinate_dimension": coordinate_dimension,
            "wkb_hex": to_wkb(
                value,
                hex=True,
                output_dimension=2,
                byte_order=1,
                include_srid=False,
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
            raise BessPlanningFeatureApplicationError(
                "Application integrity payload contains non-finite data"
            )
        return number
    if isinstance(value, str):
        return value
    raise BessPlanningFeatureApplicationError(
        f"Unsupported application integrity value {type(value).__name__}"
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


def _validate_application_geometry(frame: gpd.GeoDataFrame, label: str) -> None:
    """Require supplied application geometry to remain canonical two-dimensional."""

    try:
        geometry_name = frame.geometry.name
        if geometry_name not in frame.columns:
            raise BessPlanningFeatureApplicationError(
                f"{label} active geometry column is missing"
            )
        for position, geometry in enumerate(frame.geometry.array):
            if not isinstance(geometry, BaseGeometry):
                raise BessPlanningFeatureApplicationError(
                    f"{label} geometry at row {position} is missing or invalid"
                )
            if int(get_coordinate_dimension(geometry)) != 2:
                raise BessPlanningFeatureApplicationError(
                    f"{label} geometry at row {position} must be canonical 2D"
                )
    except BessPlanningFeatureApplicationError:
        raise
    except Exception as error:
        raise BessPlanningFeatureApplicationError(
            f"{label} geometry contract is invalid"
        ) from error


def _canonical_json_sha256(value: object) -> str:
    try:
        encoded = json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except (TypeError, ValueError) as error:
        raise BessPlanningFeatureApplicationError(
            "Application integrity payload is not canonical JSON"
        ) from error
    return sha256(encoded).hexdigest()


def _null_safe_equal(left: object, right: object) -> bool:
    left = _null_value(left)
    right = _null_value(right)
    if left is None or right is None:
        return left is None and right is None
    try:
        return bool(left == right)
    except (TypeError, ValueError):
        return False


def _policy_lookup(
    policy: BessPlanningFeaturePolicyResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
    lookup: dict[tuple[str, str, str], dict[str, object]] = {}
    for row in policy.policy_table.to_dict("records"):
        key = (
            str(row["feature_family"]),
            str(row["type_code"]),
            str(row["subtype_code"]),
        )
        if key in lookup:
            raise BessPlanningFeatureApplicationError(
                "Compiled policy contains a duplicate exact code pair"
            )
        lookup[key] = row
    return lookup


def _policy_values(
    row: dict[str, object] | None,
    application_status: ApplicationStatus,
    policy: BessPlanningFeaturePolicyResult,
) -> dict[str, object]:
    return {
        "bess_cnig_policy_application_status": application_status,
        "bess_cnig_precheck_status": None if row is None else row["precheck_status"],
        "bess_cnig_precheck_confidence": None if row is None else row["confidence"],
        "bess_cnig_status_priority": None if row is None else row["status_priority"],
        "bess_cnig_rationale": None if row is None else row["rationale"],
        "bess_cnig_required_human_action": (
            None if row is None else row["required_human_action"]
        ),
        "bess_cnig_limitations": None if row is None else row["limitations"],
        "bess_cnig_application_scope": APPLICATION_SCOPE,
        "bess_cnig_policy_scope": policy.policy_scope,
        "bess_cnig_local_feature_text_interpreted": False,
        "bess_cnig_local_regulation_content_interpreted": False,
        "bess_cnig_legal_conclusion_produced": False,
        "bess_cnig_parcel_status_aggregated": False,
        "bess_cnig_parcel_rejection_performed": False,
        "bess_cnig_score_calculated": False,
        "bess_cnig_policy_profile": policy.policy_profile,
        "bess_cnig_policy_sha256": policy.policy_sha256,
        "bess_cnig_policy_result_sha256": policy.complete_result_content_sha256,
    }


def _assign_policy_columns(
    frame: pd.DataFrame,
    rows: list[dict[str, object]],
) -> pd.DataFrame:
    values: dict[str, object] = {}
    for column in STRING_POLICY_COLUMNS:
        values[column] = pd.array([row[column] for row in rows], dtype="str")
    values["bess_cnig_status_priority"] = pd.array(
        [row["bess_cnig_status_priority"] for row in rows], dtype="Int64"
    )
    for column in FLAG_COLUMNS:
        values[column] = pd.array([row[column] for row in rows], dtype="bool")
    for column in POLICY_COLUMNS:
        frame[column] = values[column]
    return frame


def _apply_feature_catalog(
    catalog: gpd.GeoDataFrame,
    policy: BessPlanningFeaturePolicyResult,
) -> gpd.GeoDataFrame:
    """Apply exact family/type/subtype policy to one already-coded catalog."""

    if not isinstance(catalog, gpd.GeoDataFrame):
        raise BessPlanningFeatureApplicationError(
            "Coded feature catalog is not geospatial"
        )
    if any(column in catalog.columns for column in POLICY_COLUMNS):
        raise BessPlanningFeatureApplicationError(
            "Coded feature catalog already contains BESS policy columns"
        )
    required = {
        "planning_feature_id",
        "feature_family",
        "type_code_raw",
        "subtype_code_raw",
        "official_code_status",
    }
    if not required.issubset(catalog.columns):
        raise BessPlanningFeatureApplicationError(
            "Coded feature catalog lacks exact policy lookup fields"
        )
    lookup = _policy_lookup(policy)
    policy_rows: list[dict[str, object]] = []
    for row in catalog.to_dict("records"):
        type_code = row["type_code_raw"]
        subtype_code = row["subtype_code_raw"]
        if not isinstance(type_code, str) or CODE_PATTERN.fullmatch(type_code) is None:
            raise BessPlanningFeatureApplicationError(
                "Feature type code is not an exact two-character string"
            )
        if (
            not isinstance(subtype_code, str)
            or CODE_PATTERN.fullmatch(subtype_code) is None
        ):
            raise BessPlanningFeatureApplicationError(
                "Feature subtype code is not an exact two-character string"
            )
        key = (str(row["feature_family"]), type_code, subtype_code)
        official_status = row["official_code_status"]
        policy_row = lookup.get(key)
        if official_status == "RESOLVED_OFFICIAL":
            if policy_row is None:
                raise BessPlanningFeatureApplicationError(
                    f"Resolved official feature has no exact policy row: {key}"
                )
            application_status: ApplicationStatus = "APPLIED_EXACT_POLICY"
        elif official_status == "UNKNOWN_CODE_PAIR":
            if policy_row is not None:
                raise BessPlanningFeatureApplicationError(
                    f"Unknown official feature unexpectedly matches policy row: {key}"
                )
            application_status = "UNRESOLVED_CODE_PAIR"
        else:
            raise BessPlanningFeatureApplicationError(
                "Feature official-code status is invalid"
            )
        policy_rows.append(_policy_values(policy_row, application_status, policy))
    output = catalog.copy(deep=True)
    _assign_policy_columns(output, policy_rows)
    applied = gpd.GeoDataFrame(output, geometry=catalog.geometry.name, crs=catalog.crs)
    _validate_application_geometry(applied, "applied feature catalog")
    return applied


def _feature_rows_by_id(
    *catalogs: gpd.GeoDataFrame,
) -> dict[str, dict[str, object]]:
    indexed: dict[str, dict[str, object]] = {}
    for catalog in catalogs:
        for row in catalog.to_dict("records"):
            feature_id = row["planning_feature_id"]
            if not isinstance(feature_id, str) or not feature_id:
                raise BessPlanningFeatureApplicationError(
                    "Enriched feature ID must be an exact string"
                )
            if feature_id in indexed:
                raise BessPlanningFeatureApplicationError(
                    "Enriched planning feature ID is not globally unique"
                )
            indexed[feature_id] = row
    return indexed


def _apply_relations(
    relations: pd.DataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
) -> pd.DataFrame:
    """Propagate feature policy to relations only through planning_feature_id."""

    if not isinstance(relations, pd.DataFrame) or isinstance(
        relations, gpd.GeoDataFrame
    ):
        raise BessPlanningFeatureApplicationError("Coded relations must be a DataFrame")
    if any(column in relations.columns for column in POLICY_COLUMNS):
        raise BessPlanningFeatureApplicationError(
            "Coded relations already contain BESS policy columns"
        )
    required = {"planning_feature_id", *RELATION_FEATURE_AGREEMENT_COLUMNS}
    if not required.issubset(relations.columns):
        raise BessPlanningFeatureApplicationError(
            "Coded relations lack feature-policy agreement fields"
        )
    features = _feature_rows_by_id(surface_features, line_features, point_features)
    policy_rows: list[dict[str, object]] = []
    for relation in relations.to_dict("records"):
        feature_id = relation["planning_feature_id"]
        feature = features.get(str(feature_id))
        if feature is None:
            raise BessPlanningFeatureApplicationError(
                f"Relation references unknown planning feature ID: {feature_id!r}"
            )
        for column in RELATION_FEATURE_AGREEMENT_COLUMNS:
            if not _null_safe_equal(relation[column], feature[column]):
                raise BessPlanningFeatureApplicationError(
                    f"Relation {column} differs from referenced feature"
                )
        policy_rows.append({column: feature[column] for column in POLICY_COLUMNS})
    output = relations.copy(deep=True)
    return _assign_policy_columns(output, policy_rows)


def _component_metadata(
    result: BessPlanningFeatureApplicationResult,
) -> dict[str, object]:
    return {
        "result_hash_schema_version": result.result_hash_schema_version,
        "application_scope": result.application_scope,
        "policy_scope": result.policy_scope,
        "local_feature_text_interpreted": result.local_feature_text_interpreted,
        "local_regulation_content_interpreted": (
            result.local_regulation_content_interpreted
        ),
        "legal_conclusion_produced": result.legal_conclusion_produced,
        "parcel_status_aggregated": result.parcel_status_aggregated,
        "parcel_rejection_performed": result.parcel_rejection_performed,
        "score_calculated": result.score_calculated,
        "policy_profile": result.policy_profile,
        "policy_sha256": result.policy_sha256,
        "policy_result_hash_schema_version": (result.policy_result_hash_schema_version),
        "policy_complete_result_content_sha256": (
            result.policy_complete_result_content_sha256
        ),
        "cnig_profile": result.cnig_profile,
        "cnig_profile_sha256": result.cnig_profile_sha256,
        "cnig_result_hash_schema_version": result.cnig_result_hash_schema_version,
        "cnig_complete_result_content_sha256": (
            result.cnig_complete_result_content_sha256
        ),
        "source_document_id": result.source_document_id,
        "source_archive_sha256": result.source_archive_sha256,
        "cnig_surface_features_content_sha256": (
            result.cnig_surface_features_content_sha256
        ),
        "cnig_line_features_content_sha256": result.cnig_line_features_content_sha256,
        "cnig_point_features_content_sha256": (
            result.cnig_point_features_content_sha256
        ),
        "cnig_relations_content_sha256": result.cnig_relations_content_sha256,
    }


def _component_sha256(
    result: BessPlanningFeatureApplicationResult,
    frame: pd.DataFrame,
    role: str,
) -> str:
    return _canonical_json_sha256(
        {
            "domain": f"landscout.bess_planning_feature_application.{role}",
            **_component_metadata(result),
            "frame": _frame_payload(frame),
        }
    )


def _complete_result_sha256(result: BessPlanningFeatureApplicationResult) -> str:
    return _canonical_json_sha256(
        {
            "domain": "landscout.bess_planning_feature_application.result",
            **_component_metadata(result),
            "surface_features_content_sha256": (result.surface_features_content_sha256),
            "line_features_content_sha256": result.line_features_content_sha256,
            "point_features_content_sha256": result.point_features_content_sha256,
            "relations_content_sha256": result.relations_content_sha256,
        }
    )


def _result_with_hashes(
    result: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureApplicationResult:
    components = replace(
        result,
        surface_features_content_sha256=_component_sha256(
            result, result.surface_features, "surface_features"
        ),
        line_features_content_sha256=_component_sha256(
            result, result.line_features, "line_features"
        ),
        point_features_content_sha256=_component_sha256(
            result, result.point_features, "point_features"
        ),
        relations_content_sha256=_component_sha256(
            result, result.relations, "relations"
        ),
    )
    return replace(
        components,
        complete_result_content_sha256=_complete_result_sha256(components),
    )


def _build_result(
    coded: PlanningFeatureCodeResult,
    policy: BessPlanningFeaturePolicyResult,
) -> BessPlanningFeatureApplicationResult:
    surface = _apply_feature_catalog(coded.surface_features, policy)
    line = _apply_feature_catalog(coded.line_features, policy)
    point = _apply_feature_catalog(coded.point_features, policy)
    relations = _apply_relations(coded.relations, surface, line, point)
    result = BessPlanningFeatureApplicationResult(
        result_hash_schema_version=RESULT_HASH_SCHEMA_VERSION,
        application_scope=APPLICATION_SCOPE,
        policy_scope=policy.policy_scope,
        local_feature_text_interpreted=False,
        local_regulation_content_interpreted=False,
        legal_conclusion_produced=False,
        parcel_status_aggregated=False,
        parcel_rejection_performed=False,
        score_calculated=False,
        policy_profile=policy.policy_profile,
        policy_sha256=policy.policy_sha256,
        policy_result_hash_schema_version=policy.result_hash_schema_version,
        policy_complete_result_content_sha256=policy.complete_result_content_sha256,
        cnig_profile=coded.profile,
        cnig_profile_sha256=coded.profile_sha256,
        cnig_result_hash_schema_version=coded.result_hash_schema_version,
        cnig_complete_result_content_sha256=coded.complete_result_content_sha256,
        source_document_id=coded.source_document_id,
        source_archive_sha256=coded.source_archive_sha256,
        cnig_surface_features_content_sha256=coded.surface_features_content_sha256,
        cnig_line_features_content_sha256=coded.line_features_content_sha256,
        cnig_point_features_content_sha256=coded.point_features_content_sha256,
        cnig_relations_content_sha256=coded.relations_content_sha256,
        surface_features_content_sha256="",
        line_features_content_sha256="",
        point_features_content_sha256="",
        relations_content_sha256="",
        complete_result_content_sha256="",
        surface_features=surface,
        line_features=line,
        point_features=point,
        relations=relations,
    )
    return _result_with_hashes(result)


def _validate_relation_rows(
    frame: pd.DataFrame,
    label: str,
    result: BessPlanningFeatureApplicationResult,
) -> tuple[dict[int, str], dict[str, int]]:
    try:
        return validate_bess_application_relation_frame(
            frame,
            label=label,
            policy_profile=result.policy_profile,
            policy_sha256=result.policy_sha256,
            policy_result_sha256=result.policy_complete_result_content_sha256,
            source_document_id=result.source_document_id,
            source_archive_sha256=result.source_archive_sha256,
            cnig_profile=result.cnig_profile,
            cnig_profile_sha256=result.cnig_profile_sha256,
        )
    except (TypeError, ValueError) as error:
        raise BessPlanningFeatureApplicationError(str(error)) from error


def _validate_result_envelope(result: BessPlanningFeatureApplicationResult) -> None:
    if not isinstance(result, BessPlanningFeatureApplicationResult):
        raise BessPlanningFeatureApplicationError(
            "result must be a BessPlanningFeatureApplicationResult"
        )
    if (
        type(result.result_hash_schema_version) is not int
        or result.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION
    ):
        raise BessPlanningFeatureApplicationError("unsupported result hash schema")
    if (
        result.application_scope != APPLICATION_SCOPE
        or result.policy_scope != POLICY_SCOPE
    ):
        raise BessPlanningFeatureApplicationError("application result scope is invalid")
    for exact_value, label in (
        (result.policy_profile, "policy_profile"),
        (result.cnig_profile, "cnig_profile"),
        (result.source_document_id, "source_document_id"),
    ):
        try:
            _exact_string(exact_value, label)
        except ValueError as error:
            raise BessPlanningFeatureApplicationError(str(error)) from error
    if result.policy_result_hash_schema_version != 1:
        raise BessPlanningFeatureApplicationError(
            "policy result hash schema must be exactly 1"
        )
    if result.cnig_result_hash_schema_version != 5:
        raise BessPlanningFeatureApplicationError(
            "CNIG result hash schema must be exactly 5"
        )
    if any(
        value is not False
        for value in (
            result.local_feature_text_interpreted,
            result.local_regulation_content_interpreted,
            result.legal_conclusion_produced,
            result.parcel_status_aggregated,
            result.parcel_rejection_performed,
            result.score_calculated,
        )
    ):
        raise BessPlanningFeatureApplicationError(
            "application result boundary flags must all be false"
        )
    for frame, label in (
        (result.surface_features, "surface features"),
        (result.line_features, "line features"),
        (result.point_features, "point features"),
    ):
        if not isinstance(frame, gpd.GeoDataFrame):
            raise BessPlanningFeatureApplicationError(f"{label} must be geospatial")
        if frame.columns.duplicated().any():
            raise BessPlanningFeatureApplicationError(
                f"{label} policy schema is invalid"
            )
        deterministic_frame_schema_signature(frame)
    try:
        feature_mapping = validate_bess_application_feature_catalogs(
            result.surface_features,
            result.line_features,
            result.point_features,
            policy_profile=result.policy_profile,
            policy_sha256=result.policy_sha256,
            policy_result_sha256=result.policy_complete_result_content_sha256,
            source_document_id=result.source_document_id,
            source_archive_sha256=result.source_archive_sha256,
            cnig_profile=result.cnig_profile,
            cnig_profile_sha256=result.cnig_profile_sha256,
        )
    except (TypeError, ValueError) as error:
        raise BessPlanningFeatureApplicationError(str(error)) from error
    if not isinstance(result.relations, pd.DataFrame) or isinstance(
        result.relations, gpd.GeoDataFrame
    ):
        raise BessPlanningFeatureApplicationError("relations must be a DataFrame")
    if result.relations.columns.duplicated().any():
        raise BessPlanningFeatureApplicationError("relations policy schema is invalid")
    relation_mapping = _validate_relation_rows(result.relations, "relations", result)
    if any(
        feature_mapping[0].get(priority) != status
        for priority, status in relation_mapping[0].items()
    ) or any(
        feature_mapping[1].get(status) != priority
        for status, priority in relation_mapping[1].items()
    ):
        raise BessPlanningFeatureApplicationError(
            "relation policy mapping differs from the feature mapping"
        )
    feature_rows = _feature_rows_by_id(
        result.surface_features, result.line_features, result.point_features
    )
    for relation in result.relations.to_dict("records"):
        feature = feature_rows.get(str(relation["planning_feature_id"]))
        if feature is None:
            raise BessPlanningFeatureApplicationError(
                "Application relation references an unknown feature"
            )
        for column in (*RELATION_FEATURE_AGREEMENT_COLUMNS, *POLICY_COLUMNS):
            if not _null_safe_equal(relation[column], feature[column]):
                raise BessPlanningFeatureApplicationError(
                    f"Application relation {column} differs from its feature"
                )
        kind = relation["geometry_kind"]
        relation_metric, feature_metric = {
            "SURFACE": ("feature_area_m2", "feature_area_m2"),
            "LINE": ("source_line_length_m", "feature_length_m"),
            "POINT": ("point_member_count", "point_member_count"),
        }[kind]
        if kind == "POINT":
            metric_equal = _null_safe_equal(
                relation[relation_metric], feature[feature_metric]
            )
        else:
            actual_value = relation[relation_metric]
            expected_value = feature[feature_metric]
            if (
                isinstance(actual_value, bool)
                or not isinstance(actual_value, Real)
                or isinstance(expected_value, bool)
                or not isinstance(expected_value, Real)
            ):
                raise BessPlanningFeatureApplicationError(
                    "Application relation feature metric is not numeric"
                )
            actual = float(actual_value)
            expected = float(expected_value)
            metric_equal = abs(actual - expected) <= technical_overlay_tolerance(
                max(abs(actual), abs(expected))
            )
        if not metric_equal:
            raise BessPlanningFeatureApplicationError(
                "Application relation feature metric differs from its feature"
            )
    for field in RESULT_SCALAR_FIELDS:
        if field.endswith("sha256"):
            try:
                _sha256_string(getattr(result, field), field)
            except ValueError as error:
                raise BessPlanningFeatureApplicationError(str(error)) from error
    rebuilt = _result_with_hashes(result)
    for field in (
        "surface_features_content_sha256",
        "line_features_content_sha256",
        "point_features_content_sha256",
        "relations_content_sha256",
        "complete_result_content_sha256",
    ):
        if getattr(result, field) != getattr(rebuilt, field):
            raise BessPlanningFeatureApplicationError(f"{field} is invalid")


def _validate_source_locks(
    result: BessPlanningFeatureApplicationResult,
    coded: PlanningFeatureCodeResult,
    policy: BessPlanningFeaturePolicyResult,
) -> None:
    comparisons = (
        (result.policy_profile, policy.policy_profile, "policy profile"),
        (result.policy_sha256, policy.policy_sha256, "policy SHA256"),
        (
            result.policy_result_hash_schema_version,
            policy.result_hash_schema_version,
            "policy result hash schema",
        ),
        (
            result.policy_complete_result_content_sha256,
            policy.complete_result_content_sha256,
            "policy result SHA256",
        ),
        (result.cnig_profile, coded.profile, "CNIG profile"),
        (result.cnig_profile_sha256, coded.profile_sha256, "CNIG profile SHA256"),
        (
            result.cnig_result_hash_schema_version,
            coded.result_hash_schema_version,
            "CNIG result hash schema",
        ),
        (
            result.cnig_complete_result_content_sha256,
            coded.complete_result_content_sha256,
            "CNIG result SHA256",
        ),
        (result.source_document_id, coded.source_document_id, "document ID"),
        (result.source_archive_sha256, coded.source_archive_sha256, "archive SHA256"),
        (
            result.cnig_surface_features_content_sha256,
            coded.surface_features_content_sha256,
            "coded surface SHA256",
        ),
        (
            result.cnig_line_features_content_sha256,
            coded.line_features_content_sha256,
            "coded line SHA256",
        ),
        (
            result.cnig_point_features_content_sha256,
            coded.point_features_content_sha256,
            "coded point SHA256",
        ),
        (
            result.cnig_relations_content_sha256,
            coded.relations_content_sha256,
            "coded relations SHA256",
        ),
    )
    for actual, expected, label in comparisons:
        if actual != expected:
            raise BessPlanningFeatureApplicationError(
                f"Application source lock differs for {label}"
            )


def _validate_policy_source(
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
) -> None:
    try:
        validate_bess_planning_feature_policy_result(
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
        )
    except Exception as error:
        raise BessPlanningFeatureApplicationError(
            "Source-complete BESS planning-feature policy validation failed"
        ) from error


def apply_bess_planning_feature_policy(
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
) -> BessPlanningFeatureApplicationResult:
    """Validate once, then propagate exact compiled policy to features and relations."""

    try:
        _validate_policy_source(
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
        )
        result = _build_result(coded_result, policy_result)
        _validate_result_envelope(result)
        return result
    except BessPlanningFeatureApplicationError:
        raise
    except Exception as error:
        raise BessPlanningFeatureApplicationError(
            "BESS planning-feature policy application failed safely"
        ) from error


def _compare_frame(actual: pd.DataFrame, expected: pd.DataFrame, label: str) -> None:
    if _frame_payload(actual) != _frame_payload(expected):
        raise BessPlanningFeatureApplicationError(
            f"Application {label} differs from rebuilt result"
        )


def validate_bess_planning_feature_application_result(
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
    result: BessPlanningFeatureApplicationResult,
) -> None:
    """Independently rebuild exact policy propagation from every source input."""

    try:
        _validate_result_envelope(result)
        _validate_source_locks(result, coded_result, policy_result)
        _validate_policy_source(
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
        )
        expected = _build_result(coded_result, policy_result)
        for field in RESULT_SCALAR_FIELDS:
            if getattr(result, field) != getattr(expected, field):
                raise BessPlanningFeatureApplicationError(
                    f"Application {field} differs from rebuilt result"
                )
        for actual, rebuilt, label in (
            (result.surface_features, expected.surface_features, "surface features"),
            (result.line_features, expected.line_features, "line features"),
            (result.point_features, expected.point_features, "point features"),
            (result.relations, expected.relations, "relations"),
        ):
            _compare_frame(actual, rebuilt, label)
    except BessPlanningFeatureApplicationError:
        raise
    except Exception as error:
        raise BessPlanningFeatureApplicationError(
            "BESS planning-feature application result validation failed safely"
        ) from error


def _unique_json_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    output: dict[str, object] = {}
    for key, value in pairs:
        if key in output:
            raise BessPlanningFeatureApplicationError(
                f"Duplicate JSON application artifact key: {key!r}"
            )
        output[key] = value
    return output


def _read_verified_artifact(
    path: Path,
    record: BessPlanningFeatureApplicationArtifactRecord,
) -> pd.DataFrame:
    if path.name != record.filename:
        raise BessPlanningFeatureApplicationError(
            f"Artifact {record.artifact_role} filename differs"
        )
    payload = path.read_bytes()
    if len(payload) != record.size_bytes:
        raise BessPlanningFeatureApplicationError(
            f"Artifact {record.artifact_role} byte size differs"
        )
    if sha256(payload).hexdigest() != record.sha256:
        raise BessPlanningFeatureApplicationError(
            f"Artifact {record.artifact_role} SHA256 differs"
        )
    buffer = BytesIO(payload)
    frame: pd.DataFrame
    if record.geospatial:
        frame = gpd.read_parquet(buffer)
    else:
        frame = pd.read_parquet(buffer)
    if len(frame) != record.row_count:
        raise BessPlanningFeatureApplicationError(
            f"Artifact {record.artifact_role} row count differs"
        )
    signature = deterministic_frame_schema_signature(frame)
    if signature != record.frame_schema_signature:
        raise BessPlanningFeatureApplicationError(
            f"Artifact {record.artifact_role} frame schema differs"
        )
    if record.geospatial:
        if not isinstance(frame, gpd.GeoDataFrame) or frame.crs is None:
            raise BessPlanningFeatureApplicationError(
                f"Artifact {record.artifact_role} geospatial contract differs"
            )
        if CRS.from_user_input(frame.crs).to_json_dict() != record.crs:
            raise BessPlanningFeatureApplicationError(
                f"Artifact {record.artifact_role} CRS differs"
            )
    elif isinstance(frame, gpd.GeoDataFrame):
        raise BessPlanningFeatureApplicationError(
            "Relations artifact unexpectedly loaded as geospatial"
        )
    return frame


def load_bess_planning_feature_application_artifacts(
    manifest_path: str | Path,
    surface_features_path: str | Path,
    line_features_path: str | Path,
    point_features_path: str | Path,
    relations_path: str | Path,
) -> BessPlanningFeatureApplicationResult:
    """Load four byte-sealed application outputs and validate their local envelope."""

    try:
        payload = json.loads(
            Path(manifest_path).read_text(encoding="utf-8"),
            object_pairs_hook=_unique_json_object,
        )
        manifest = BessPlanningFeatureApplicationArtifactManifest.model_validate(
            payload
        )
        paths = {
            "SURFACE_FEATURES": Path(surface_features_path),
            "LINE_FEATURES": Path(line_features_path),
            "POINT_FEATURES": Path(point_features_path),
            "RELATIONS": Path(relations_path),
        }
        records = {record.artifact_role: record for record in manifest.artifacts}
        loaded = {
            role: _read_verified_artifact(paths[role], records[role])
            for role in ARTIFACT_ROLES
        }
        result = BessPlanningFeatureApplicationResult(
            **{field: getattr(manifest, field) for field in RESULT_SCALAR_FIELDS},
            surface_features=loaded["SURFACE_FEATURES"],
            line_features=loaded["LINE_FEATURES"],
            point_features=loaded["POINT_FEATURES"],
            relations=loaded["RELATIONS"],
        )
        _validate_result_envelope(result)
        return result
    except BessPlanningFeatureApplicationError:
        raise
    except Exception as error:
        raise BessPlanningFeatureApplicationError(
            f"BESS planning-feature application artifacts are invalid: {error}"
        ) from error

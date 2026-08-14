"""Internal intrinsic contracts for BESS CNIG application rows."""

from __future__ import annotations

import math
import re
from numbers import Integral, Real
from pathlib import PurePosixPath, PureWindowsPath
from typing import Literal

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd  # type: ignore[import-untyped]
from pyproj import CRS
from shapely import get_coordinate_dimension, get_parts  # type: ignore[import-untyped]
from shapely.geometry.base import BaseGeometry  # type: ignore[import-untyped]

from landscout.common.planning_feature_contract import (
    validate_intrinsic_planning_feature_relations,
)
from landscout.stages.planning_overlay import technical_overlay_tolerance

APPLICATION_SCOPE = "FEATURE_AND_RELATION_POLICY_PROPAGATION_ONLY"
POLICY_SCOPE = "OFFICIAL_CNIG_CODE_MEANING_ONLY"

ApplicationStatus = Literal["APPLIED_EXACT_POLICY", "UNRESOLVED_CODE_PAIR"]

POLICY_COLUMNS = (
    "bess_cnig_policy_application_status",
    "bess_cnig_precheck_status",
    "bess_cnig_precheck_confidence",
    "bess_cnig_status_priority",
    "bess_cnig_rationale",
    "bess_cnig_required_human_action",
    "bess_cnig_limitations",
    "bess_cnig_application_scope",
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
)
DECISION_COLUMNS = (
    "bess_cnig_precheck_status",
    "bess_cnig_precheck_confidence",
    "bess_cnig_status_priority",
    "bess_cnig_rationale",
    "bess_cnig_required_human_action",
    "bess_cnig_limitations",
)
FLAG_COLUMNS = (
    "bess_cnig_local_feature_text_interpreted",
    "bess_cnig_local_regulation_content_interpreted",
    "bess_cnig_legal_conclusion_produced",
    "bess_cnig_parcel_status_aggregated",
    "bess_cnig_parcel_rejection_performed",
    "bess_cnig_score_calculated",
)
STRING_POLICY_COLUMNS = tuple(
    column
    for column in POLICY_COLUMNS
    if column not in {"bess_cnig_status_priority", *FLAG_COLUMNS}
)
POLICY_SUFFIX_DTYPES = {
    **{column: "str" for column in STRING_POLICY_COLUMNS},
    "bess_cnig_status_priority": "Int64",
    **{column: "bool" for column in FLAG_COLUMNS},
}
ALLOWED_PRECHECK_STATUSES = frozenset(
    {
        "LIKELY_MATERIAL_CONSTRAINT",
        "MATERIAL_REVIEW_REQUIRED",
        "DESIGN_REVIEW_REQUIRED",
        "CONTEXT_REVIEW_REQUIRED",
        "UNKNOWN",
    }
)
ALLOWED_CONFIDENCES = frozenset({"HIGH", "MEDIUM", "LOW"})
ALLOWED_FEATURE_FAMILIES = frozenset({"PRESCRIPTION", "INFORMATION"})
NULL_LITERALS = frozenset({"None", "nan", "<NA>"})
CODE_PATTERN = re.compile(r"[0-9]{2}")
_FEATURE_SPECS = {
    "SURFACE": (
        frozenset({"prescription_surface", "information_surface"}),
        frozenset({"Polygon", "MultiPolygon"}),
        "feature_area_m2",
    ),
    "LINE": (
        frozenset({"prescription_line", "information_line"}),
        frozenset({"LineString", "MultiLineString"}),
        "feature_length_m",
    ),
    "POINT": (
        frozenset({"prescription_point", "information_point"}),
        frozenset({"Point", "MultiPoint"}),
        "point_member_count",
    ),
}


def _null_value(value: object) -> object:
    if value is None or value is pd.NA:
        return None
    if isinstance(value, float) and math.isnan(value):
        return None
    return value


def _exact_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise ValueError(f"{label} must be an exact non-empty string")
    return value


def validate_bess_application_policy_frame(
    frame: pd.DataFrame,
    *,
    label: str,
    policy_profile: str,
    policy_sha256: str,
    policy_result_sha256: str,
) -> None:
    """Validate the complete canonical application suffix and every row."""

    if not isinstance(frame, pd.DataFrame):
        raise TypeError(f"{label} must be a DataFrame")
    if frame.columns.duplicated().any():
        raise ValueError(f"{label} contains duplicate columns")
    if tuple(frame.columns[-len(POLICY_COLUMNS) :]) != POLICY_COLUMNS:
        raise ValueError(f"{label} policy schema is invalid")
    for column, expected_dtype in POLICY_SUFFIX_DTYPES.items():
        if str(frame[column].dtype) != expected_dtype:
            raise ValueError(f"{label} policy dtype is invalid for {column}")
    required = {
        "feature_family",
        "type_code_raw",
        "subtype_code_raw",
        "official_code_status",
        *POLICY_COLUMNS,
    }
    if not required.issubset(frame.columns):
        raise ValueError(f"{label} application identity schema is incomplete")
    for row in frame.to_dict("records"):
        if row["feature_family"] not in ALLOWED_FEATURE_FAMILIES:
            raise ValueError(f"{label} feature family is invalid")
        for column in ("type_code_raw", "subtype_code_raw"):
            value = row[column]
            if not isinstance(value, str) or CODE_PATTERN.fullmatch(value) is None:
                raise ValueError(f"{label} {column} is not an exact two-digit code")
        application_status = row["bess_cnig_policy_application_status"]
        official_status = row["official_code_status"]
        if application_status == "APPLIED_EXACT_POLICY":
            if official_status != "RESOLVED_OFFICIAL":
                raise ValueError(
                    f"{label} official status contradicts its application status"
                )
            if any(_null_value(row[column]) is None for column in DECISION_COLUMNS):
                raise ValueError(f"{label} applied policy row has a missing decision")
            if row["bess_cnig_precheck_status"] not in ALLOWED_PRECHECK_STATUSES:
                raise ValueError(f"{label} precheck status is outside the domain")
            if row["bess_cnig_precheck_confidence"] not in ALLOWED_CONFIDENCES:
                raise ValueError(f"{label} confidence is outside the domain")
            priority = row["bess_cnig_status_priority"]
            if (
                isinstance(priority, bool)
                or not isinstance(priority, Integral)
                or int(priority) <= 0
            ):
                raise ValueError(f"{label} priority must be a positive integer")
            for column in (
                "bess_cnig_rationale",
                "bess_cnig_required_human_action",
                "bess_cnig_limitations",
            ):
                _exact_string(row[column], f"{label} {column}")
        elif application_status == "UNRESOLVED_CODE_PAIR":
            if official_status != "UNKNOWN_CODE_PAIR":
                raise ValueError(
                    f"{label} official status contradicts its application status"
                )
            if any(_null_value(row[column]) is not None for column in DECISION_COLUMNS):
                raise ValueError(f"{label} unresolved row has an invented decision")
        else:
            raise ValueError(f"{label} application status is invalid")
        for column in STRING_POLICY_COLUMNS:
            value = row[column]
            if isinstance(value, str) and value in NULL_LITERALS:
                raise ValueError(
                    f"{label} contains a literal missing-value replacement"
                )
        if row["bess_cnig_application_scope"] != APPLICATION_SCOPE:
            raise ValueError(f"{label} application scope is invalid")
        if row["bess_cnig_policy_scope"] != POLICY_SCOPE:
            raise ValueError(f"{label} policy scope is invalid")
        if any(row[column] is not False for column in FLAG_COLUMNS):
            raise ValueError(f"{label} boundary flags must be false")
        for actual, expected, lineage_label in (
            (row["bess_cnig_policy_profile"], policy_profile, "policy profile"),
            (row["bess_cnig_policy_sha256"], policy_sha256, "policy SHA256"),
            (
                row["bess_cnig_policy_result_sha256"],
                policy_result_sha256,
                "policy result SHA256",
            ),
        ):
            if actual != expected:
                raise ValueError(f"{label} {lineage_label} lineage is invalid")


def _relation_identity_string(value: object, label: str) -> str:
    exact = _exact_string(value, label)
    if exact in NULL_LITERALS:
        raise ValueError(f"{label} must not be a textual null sentinel")
    return exact


def _portable_feature_id(value: object, label: str) -> str:
    feature_id = _relation_identity_string(value, label)
    if (
        PurePosixPath(feature_id).is_absolute()
        or PureWindowsPath(feature_id).is_absolute()
    ):
        raise ValueError(f"{label} must not be an absolute path")
    return feature_id


def _status_priority_mapping(
    frame: pd.DataFrame, label: str
) -> tuple[dict[int, str], dict[str, int]]:
    priority_to_statuses: dict[int, set[str]] = {}
    status_to_priorities: dict[str, set[int]] = {}
    applied = frame[
        frame["bess_cnig_policy_application_status"] == "APPLIED_EXACT_POLICY"
    ]
    for row in applied.to_dict("records"):
        priority = int(row["bess_cnig_status_priority"])
        status = str(row["bess_cnig_precheck_status"])
        priority_to_statuses.setdefault(priority, set()).add(status)
        status_to_priorities.setdefault(status, set()).add(priority)
    if any(len(statuses) != 1 for statuses in priority_to_statuses.values()) or any(
        len(priorities) != 1 for priorities in status_to_priorities.values()
    ):
        raise ValueError(f"{label} status/priority mapping is not one-to-one")
    return (
        {
            priority: next(iter(statuses))
            for priority, statuses in priority_to_statuses.items()
        },
        {
            status: next(iter(priorities))
            for status, priorities in status_to_priorities.items()
        },
    )


def _feature_metric(value: object, expected: float, label: str) -> None:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise TypeError(f"{label} must be numeric")
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise ValueError(f"{label} must be finite and positive")
    if abs(number - expected) > technical_overlay_tolerance(
        max(abs(number), abs(expected))
    ):
        raise ValueError(f"{label} is inconsistent with feature geometry")


def validate_bess_application_feature_catalogs(
    surface: gpd.GeoDataFrame,
    line: gpd.GeoDataFrame,
    point: gpd.GeoDataFrame,
    *,
    policy_profile: str,
    policy_sha256: str,
    policy_result_sha256: str,
) -> tuple[dict[int, str], dict[str, int]]:
    """Validate all intrinsic feature facts, identities, geometry, and mappings."""

    feature_ids: list[str] = []
    applied_frames: list[pd.DataFrame] = []
    for frame, kind, label in (
        (surface, "SURFACE", "surface features"),
        (line, "LINE", "line features"),
        (point, "POINT", "point features"),
    ):
        if not isinstance(frame, gpd.GeoDataFrame):
            raise TypeError(f"{label} must be a GeoDataFrame")
        validate_bess_application_policy_frame(
            frame,
            label=label,
            policy_profile=policy_profile,
            policy_sha256=policy_sha256,
            policy_result_sha256=policy_result_sha256,
        )
        required = {
            "planning_feature_id",
            "source_feature_id",
            "source_document_id",
            "logical_layer",
            "feature_family",
            "geometry_kind",
            "geometry",
            _FEATURE_SPECS[kind][2],
        }
        if not required.issubset(frame.columns):
            raise ValueError(f"{label} factual schema is incomplete")
        try:
            if frame.geometry.name != "geometry" or frame.crs is None:
                raise ValueError("active geometry or CRS is missing")
            if not CRS.from_user_input(frame.crs).equals(CRS.from_epsg(2154)):
                raise ValueError("CRS is not EPSG:2154")
        except Exception as error:
            raise ValueError(
                f"{label} must use active geometry and EPSG:2154"
            ) from error
        allowed_layers, geometry_types, metric_column = _FEATURE_SPECS[kind]
        for row in frame.to_dict("records"):
            feature_id = _portable_feature_id(
                row["planning_feature_id"], f"{label} planning feature identity"
            )
            source_id = _relation_identity_string(
                row["source_feature_id"], f"{label} source feature identity"
            )
            document_id = _relation_identity_string(
                row["source_document_id"], f"{label} source document identity"
            )
            logical_layer = row["logical_layer"]
            if logical_layer not in allowed_layers:
                raise ValueError(f"{label} logical layer is invalid")
            expected_family = (
                "PRESCRIPTION"
                if str(logical_layer).startswith("prescription_")
                else "INFORMATION"
            )
            if row["feature_family"] != expected_family:
                raise ValueError(f"{label} family and logical layer are inconsistent")
            if row["geometry_kind"] != kind:
                raise ValueError(f"{label} geometry kind is invalid")
            expected_id = f"GPU:{document_id}:{logical_layer}:{source_id}"
            if feature_id != expected_id:
                raise ValueError(
                    f"{label} planning feature identity differs from GPU namespace"
                )
            geometry = row["geometry"]
            if (
                not isinstance(geometry, BaseGeometry)
                or geometry.is_empty
                or not geometry.is_valid
                or geometry.geom_type not in geometry_types
            ):
                raise ValueError(f"{label} geometry is invalid for {kind}")
            if int(get_coordinate_dimension(geometry)) != 2:
                raise ValueError(f"{label} geometry must be canonical 2D")
            if kind == "SURFACE":
                _feature_metric(row[metric_column], float(geometry.area), metric_column)
            elif kind == "LINE":
                _feature_metric(
                    row[metric_column], float(geometry.length), metric_column
                )
            else:
                count = row[metric_column]
                if (
                    isinstance(count, bool)
                    or not isinstance(count, Integral)
                    or int(count) <= 0
                    or int(count) != len(get_parts(geometry))
                ):
                    raise ValueError(
                        "point member count is inconsistent with feature geometry"
                    )
            feature_ids.append(feature_id)
        applied_frames.append(frame)
    if len(feature_ids) != len(set(feature_ids)):
        raise ValueError("planning feature identity must be globally unique")
    combined = pd.concat(applied_frames, ignore_index=True)
    return _status_priority_mapping(combined, "feature document-wide")


def validate_bess_application_relation_frame(
    frame: pd.DataFrame,
    *,
    label: str,
    policy_profile: str,
    policy_sha256: str,
    policy_result_sha256: str,
) -> None:
    """Validate canonical application rows and the complete relation identity."""

    validate_bess_application_policy_frame(
        frame,
        label=label,
        policy_profile=policy_profile,
        policy_sha256=policy_sha256,
        policy_result_sha256=policy_result_sha256,
    )
    required = {"parcel_id", "planning_feature_id", "relation_type"}
    if not required.issubset(frame.columns):
        raise ValueError(f"{label} relation identity schema is incomplete")
    for row in frame.to_dict("records"):
        _relation_identity_string(row["parcel_id"], f"{label} parcel identity")
        feature_id = _portable_feature_id(
            row["planning_feature_id"], f"{label} Feature ID identity"
        )
        assert feature_id
    if frame.duplicated(["parcel_id", "planning_feature_id"]).any():
        raise ValueError(f"{label} contains a duplicate parcel/feature relation pair")
    validate_intrinsic_planning_feature_relations(frame)
    _status_priority_mapping(frame, f"{label} document-wide")

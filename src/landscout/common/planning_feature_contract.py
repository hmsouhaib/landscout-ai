"""Internal intrinsic contracts for stored normalized planning-feature facts."""

from __future__ import annotations

import math
from numbers import Integral, Real

import numpy as np
import pandas as pd  # type: ignore[import-untyped]

from landscout.stages.planning_overlay import technical_overlay_tolerance

RELATION_FLOAT_COLUMNS = frozenset(
    {
        "parcel_metric_area_m2",
        "feature_area_m2",
        "source_line_length_m",
        "intersection_area_m2",
        "intersection_length_m",
        "parcel_share_pct",
        "feature_share_pct",
    }
)
RELATION_COUNT_COLUMNS = frozenset(
    {
        "point_member_count",
        "point_members_inside_count",
        "point_members_boundary_count",
    }
)
REQUIRED_RELATION_COLUMNS = frozenset(
    {"geometry_kind", "relation_type"} | RELATION_FLOAT_COLUMNS | RELATION_COUNT_COLUMNS
)
RELATION_TYPES_BY_GEOMETRY_KIND = {
    "SURFACE": frozenset({"AREA_OVERLAP", "TOUCH_ONLY"}),
    "LINE": frozenset({"LENGTH_OVERLAP", "TOUCH_ONLY"}),
    "POINT": frozenset({"INSIDE", "BOUNDARY_TOUCH"}),
}


def _missing(value: object) -> bool:
    try:
        missing = pd.isna(value)
    except (TypeError, ValueError):
        return False
    return isinstance(missing, (bool, np.bool_)) and bool(missing)


def _number(value: object, label: str, *, required: bool) -> float | None:
    if _missing(value):
        if required:
            raise ValueError(f"{label} must not be null")
        return None
    if isinstance(value, bool) or not isinstance(value, Real):
        raise TypeError(f"{label} must be numeric")
    number = float(value)
    if not math.isfinite(number) or number < 0:
        raise ValueError(f"{label} must be finite and non-negative")
    return number


def _count(value: object, label: str, *, required: bool) -> int | None:
    if _missing(value):
        if required:
            raise ValueError(f"{label} must not be null")
        return None
    if isinstance(value, bool) or not isinstance(value, Integral) or int(value) < 0:
        raise ValueError(f"{label} must be a strict non-negative integer")
    return int(value)


def _require_null(row: dict[str, object], columns: tuple[str, ...], kind: str) -> None:
    if any(not _missing(row[column]) for column in columns):
        raise ValueError(f"{kind} relation populated an unrelated metric")


def validate_intrinsic_planning_feature_relations(frame: pd.DataFrame) -> None:
    """Validate stored relation types, metrics, nulls, and count semantics locally."""

    if not isinstance(frame, pd.DataFrame):
        raise TypeError("planning relations must be a DataFrame")
    if frame.columns.duplicated().any():
        raise ValueError("planning relations contain duplicate columns")
    if not REQUIRED_RELATION_COLUMNS.issubset(frame.columns):
        raise ValueError("planning relation factual metric schema is incomplete")
    for column in RELATION_FLOAT_COLUMNS:
        for value in frame[column].tolist():
            _number(value, f"relation {column}", required=False)
    for column in RELATION_COUNT_COLUMNS:
        for value in frame[column].tolist():
            _count(value, f"relation {column}", required=False)

    for row in frame.to_dict("records"):
        kind = row["geometry_kind"]
        relation_type = row["relation_type"]
        allowed = RELATION_TYPES_BY_GEOMETRY_KIND.get(kind)
        if allowed is None:
            raise ValueError("planning relation geometry kind is invalid")
        if not isinstance(relation_type, str) or relation_type not in allowed:
            raise ValueError(
                f"{kind} relation type is incompatible with its geometry kind"
            )
        parcel_area = _number(
            row["parcel_metric_area_m2"],
            "relation parcel metric area",
            required=True,
        )
        assert parcel_area is not None
        if parcel_area <= 0:
            raise ValueError("relation parcel metric area must be positive")

        if kind == "SURFACE":
            feature_area = _number(
                row["feature_area_m2"], "surface feature area", required=True
            )
            area = _number(
                row["intersection_area_m2"],
                "surface intersection area",
                required=True,
            )
            parcel_pct = _number(
                row["parcel_share_pct"], "surface parcel share", required=True
            )
            feature_pct = _number(
                row["feature_share_pct"], "surface feature share", required=True
            )
            assert None not in (feature_area, area, parcel_pct, feature_pct)
            assert feature_area is not None and area is not None
            assert parcel_pct is not None and feature_pct is not None
            if feature_area <= 0:
                raise ValueError("surface feature area must be positive")
            expected_type = "AREA_OVERLAP" if area > 0 else "TOUCH_ONLY"
            if relation_type != expected_type:
                raise ValueError("surface relation type is inconsistent with its area")
            if area - parcel_area > technical_overlay_tolerance(parcel_area):
                raise ValueError("surface intersection exceeds parcel area")
            if area - feature_area > technical_overlay_tolerance(feature_area):
                raise ValueError("surface intersection exceeds feature area")
            expected_parcel_pct = 100.0 * area / parcel_area
            expected_feature_pct = 100.0 * area / feature_area
            pct_tolerance = max(
                100.0 * technical_overlay_tolerance(parcel_area) / parcel_area,
                100.0 * technical_overlay_tolerance(feature_area) / feature_area,
            )
            if (
                abs(parcel_pct - expected_parcel_pct) > pct_tolerance
                or abs(feature_pct - expected_feature_pct) > pct_tolerance
            ):
                raise ValueError("surface relation percentages are inconsistent")
            _require_null(
                row,
                (
                    "source_line_length_m",
                    "intersection_length_m",
                    *RELATION_COUNT_COLUMNS,
                ),
                kind,
            )
        elif kind == "LINE":
            source_length = _number(
                row["source_line_length_m"], "source line length", required=True
            )
            length = _number(
                row["intersection_length_m"],
                "line intersection length",
                required=True,
            )
            assert source_length is not None and length is not None
            if source_length <= 0:
                raise ValueError("source line length must be positive")
            expected_type = "LENGTH_OVERLAP" if length > 0 else "TOUCH_ONLY"
            if relation_type != expected_type:
                raise ValueError("line relation type is inconsistent with its length")
            if length - source_length > technical_overlay_tolerance(source_length):
                raise ValueError("line intersection exceeds source line length")
            _require_null(
                row,
                (
                    "feature_area_m2",
                    "intersection_area_m2",
                    "parcel_share_pct",
                    "feature_share_pct",
                    *RELATION_COUNT_COLUMNS,
                ),
                kind,
            )
        else:
            member_count = _count(
                row["point_member_count"], "point member count", required=True
            )
            inside = _count(
                row["point_members_inside_count"],
                "point inside member count",
                required=True,
            )
            boundary = _count(
                row["point_members_boundary_count"],
                "point boundary member count",
                required=True,
            )
            assert (
                member_count is not None and inside is not None and boundary is not None
            )
            if member_count <= 0:
                raise ValueError("point member count must be positive")
            if inside + boundary > member_count:
                raise ValueError("point covered members exceed source members")
            if relation_type == "INSIDE" and inside < 1:
                raise ValueError("INSIDE relation type requires an inside point member")
            if relation_type == "BOUNDARY_TOUCH" and (inside != 0 or boundary < 1):
                raise ValueError(
                    "BOUNDARY_TOUCH relation type requires only boundary point members"
                )
            _require_null(
                row,
                (
                    "feature_area_m2",
                    "source_line_length_m",
                    "intersection_area_m2",
                    "intersection_length_m",
                    "parcel_share_pct",
                    "feature_share_pct",
                ),
                kind,
            )

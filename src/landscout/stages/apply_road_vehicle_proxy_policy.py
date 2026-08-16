"""Apply the checked-in IGN general-vehicle proxy policy to factual roads."""

from __future__ import annotations

import json
import math
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any, cast

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
from pandas.api.types import (  # type: ignore[import-untyped]
    is_bool_dtype,
    is_numeric_dtype,
)

from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
)
from landscout.stages.normalize_access_ign import (
    NormalizedIgnRoadData,
    normalize_ign_roads,
)
from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    load_ign_road_vehicle_proxy_policy,
)

__all__ = [
    "IgnRoadVehicleProxyApplicationError",
    "IgnRoadVehicleProxyApplicationResult",
    "apply_ign_road_vehicle_proxy_policy",
]

_GEOMETRY_STATUSES = frozenset({"VALID", "NULL", "EMPTY", "INVALID"})
_TECHNICAL_GEOMETRY_RULE = "SOURCE_GEOMETRY_NOT_VALID"
_CRITICAL_FIELDS = (
    "fictitious_raw",
    "asset_status_raw",
    "nature_raw",
    "light_vehicle_access_raw",
    "private_raw",
    "importance_raw",
)
_UNKNOWN_FIELD_ORDER = (
    *_CRITICAL_FIELDS,
    "carriageway_width_raw",
    "closure_period_raw",
    "restriction_nature_raw",
)
_REQUIRED_COLUMNS = frozenset(
    {
        "geometry_status",
        "geometry",
        *_UNKNOWN_FIELD_ORDER,
    }
)
_APPLICATION_COLUMNS = (
    "road_proxy_primary_rule",
    "road_proxy_class",
    "road_proxy_rule_trace_json",
    "road_proxy_unknown_fields_json",
    "road_proxy_toll_evidence",
    "road_proxy_policy_id",
    "road_proxy_policy_schema_version",
    "road_proxy_policy_config_sha256",
    "road_proxy_policy_scope",
    "road_proxy_policy_evidence_checked_on",
    "road_proxy_vehicle_scope",
    "road_proxy_heavy_vehicle_access",
)


class IgnRoadVehicleProxyApplicationError(ValueError):
    """Raised when factual roads cannot receive the approved policy safely."""


@dataclass(frozen=True)
class IgnRoadVehicleProxyApplicationResult:
    """Normalized factual roads plus deterministic general-car proxy evidence."""

    roads: gpd.GeoDataFrame


def _false_mask(index: pd.Index) -> pd.Series:
    return pd.Series(False, index=index, dtype="bool")


def _object_scalar_mask(
    series: pd.Series,
    predicate: Callable[[object], bool],
) -> pd.Series:
    """Apply a strict scalar type gate only for heterogeneous object fixtures."""

    function = np.frompyfunc(predicate, 1, 1)
    values = function(series.to_numpy(dtype=object))
    return pd.Series(np.asarray(values, dtype=bool), index=series.index)


def _is_strict_numeric_scalar(value: object) -> bool:
    return type(value) in {int, float} or (
        isinstance(value, (np.integer, np.floating))
        and not isinstance(value, np.bool_)
    )


def _is_strict_binary_numeric(value: object) -> bool:
    if not _is_strict_numeric_scalar(value):
        return False
    numeric = float(cast(Any, value))
    return math.isfinite(numeric) and numeric in {0.0, 1.0}


def _is_strict_positive_numeric(value: object) -> bool:
    if not _is_strict_numeric_scalar(value):
        return False
    numeric = float(cast(Any, value))
    return math.isfinite(numeric) and numeric > 0


def _strict_boolean_masks(
    series: pd.Series,
) -> tuple[pd.Series, pd.Series, pd.Series]:
    if is_bool_dtype(series.dtype):
        known = series.notna()
        true = known & series.eq(True)
        false = known & series.eq(False)
        return known, true, false

    if series.dtype == "object":
        known = _object_scalar_mask(
            series,
            lambda value: type(value) is bool or isinstance(value, np.bool_),
        )
        true = known & series.eq(True)
        false = known & series.eq(False)
        return known, true, false

    known = _false_mask(series.index)
    return known, known.copy(), known.copy()


def _strict_private_masks(
    series: pd.Series,
) -> tuple[pd.Series, pd.Series, pd.Series]:
    if is_bool_dtype(series.dtype):
        known = series.notna()
        return known, known & series.eq(True), known & series.eq(False)

    if is_numeric_dtype(series.dtype):
        numeric = pd.to_numeric(series, errors="raise")
        finite = pd.Series(
            np.isfinite(numeric.to_numpy(dtype="float64", na_value=np.nan)),
            index=series.index,
        )
        known = series.notna() & finite & (series.eq(0) | series.eq(1))
        return known, known & series.eq(1), known & series.eq(0)

    if series.dtype == "object":
        boolean = _object_scalar_mask(
            series,
            lambda value: type(value) is bool or isinstance(value, np.bool_),
        )
        numeric = _object_scalar_mask(
            series,
            _is_strict_binary_numeric,
        )
        known = boolean | numeric
        true = known & series.eq(1)
        false = known & series.eq(0)
        return known, true, false

    known = _false_mask(series.index)
    return known, known.copy(), known.copy()


def _exact_string_mask(series: pd.Series) -> pd.Series:
    if not (isinstance(series.dtype, pd.StringDtype) or series.dtype == "object"):
        return _false_mask(series.index)
    stripped = series.str.strip()
    return series.notna() & stripped.notna() & stripped.ne("") & series.eq(stripped)


def _known_string_masks(
    series: pd.Series,
    known_values: frozenset[str],
) -> tuple[pd.Series, pd.Series]:
    exact = _exact_string_mask(series)
    known = exact & series.isin(known_values)
    return known, ~known


def _optional_exact_string_masks(
    series: pd.Series,
) -> tuple[pd.Series, pd.Series]:
    missing = series.isna()
    exact_present = _exact_string_mask(series)
    invalid = ~missing & ~exact_present
    return exact_present, invalid


def _width_masks(
    series: pd.Series,
    threshold: float,
) -> tuple[pd.Series, pd.Series]:
    missing = series.isna()
    if is_numeric_dtype(series.dtype) and not is_bool_dtype(series.dtype):
        numeric = series.to_numpy(dtype="float64", na_value=np.nan)
        finite_positive = pd.Series(
            np.isfinite(numeric) & (numeric > 0),
            index=series.index,
        )
        valid = missing | finite_positive
        narrow = finite_positive & series.lt(threshold)
        return narrow, ~valid

    if series.dtype == "object":
        numeric = _object_scalar_mask(
            series,
            _is_strict_positive_numeric,
        )
        numeric_values = pd.to_numeric(series.where(numeric), errors="coerce")
        narrow = numeric & numeric_values.lt(threshold)
        return narrow, ~missing & ~numeric

    return _false_mask(series.index), ~missing


def _json_array_from_masks(
    index: pd.Index,
    ordered_masks: tuple[tuple[str, pd.Series], ...],
) -> pd.Series:
    output = pd.Series("[", index=index, dtype="object")
    populated = _false_mask(index)
    for value, raw_mask in ordered_masks:
        mask = raw_mask.fillna(False).astype(bool)
        token = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
        output.loc[mask & ~populated] += token
        output.loc[mask & populated] += f",{token}"
        populated |= mask
    return output + "]"


def _rule_outcomes(policy: IgnRoadVehicleProxyPolicy) -> Mapping[str, str]:
    outcomes = policy.decision_outcomes
    return {
        "FICTITIOUS_GEOMETRY": outcomes.fictitious_geometry,
        "PROJECT_GEOMETRY_NOT_SIGNIFICANT": (
            outcomes.project_geometry_not_significant
        ),
        "NOT_IN_SERVICE": outcomes.not_in_service,
        "PHYSICALLY_IMPOSSIBLE": outcomes.physically_impossible,
        "NON_GENERAL_VEHICLE_NATURE": outcomes.non_general_vehicle_nature,
        "RIGHTS_RESTRICTED": outcomes.rights_restricted,
        "PRIVATE_ROAD": outcomes.private_road,
        "TEMPORAL_CLOSURE": outcomes.temporal_closure,
        "KNOWN_RESTRICTION": outcomes.known_restriction,
        "OTHER_RECORDED_RESTRICTION": outcomes.other_recorded_restriction,
        "SPECIAL_NATURE": outcomes.special_nature,
        "LIMITED_NATURE": outcomes.limited_nature,
        "IMPORTANCE_6": outcomes.importance_6,
        "NARROW_CARRIAGEWAY": outcomes.narrow_carriageway,
        "OPEN_OR_TOLL": outcomes.open_or_toll,
        "UNKNOWN": outcomes.unknown,
    }


def _validate_normalized_frame(frame: object) -> gpd.GeoDataFrame:
    if not isinstance(frame, gpd.GeoDataFrame):
        raise IgnRoadVehicleProxyApplicationError(
            "Normalized IGN roads must be a GeoDataFrame"
        )
    if frame.columns.duplicated().any():
        raise IgnRoadVehicleProxyApplicationError(
            "Normalized IGN road columns must not contain duplicates"
        )
    missing = _REQUIRED_COLUMNS - set(frame.columns)
    if missing:
        raise IgnRoadVehicleProxyApplicationError(
            "Normalized IGN roads are missing policy input columns: "
            + ", ".join(sorted(missing))
        )
    if frame.active_geometry_name != "geometry" or frame.crs is None:
        raise IgnRoadVehicleProxyApplicationError(
            "Normalized IGN roads require active geometry and CRS"
        )
    if not isinstance(frame.index, pd.RangeIndex):
        raise IgnRoadVehicleProxyApplicationError(
            "Normalized IGN roads must retain a RangeIndex"
        )
    statuses = frame["geometry_status"]
    if statuses.isna().any() or not set(statuses.unique()).issubset(
        _GEOMETRY_STATUSES
    ):
        raise IgnRoadVehicleProxyApplicationError(
            "Normalized IGN roads contain an impossible geometry_status"
        )
    return frame


def _classify_road_frame(
    normalized: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> gpd.GeoDataFrame:
    source = _validate_normalized_frame(normalized)
    output = source.copy(deep=True)
    index = output.index
    valid_geometry = output["geometry_status"].eq("VALID")
    technical_geometry = ~valid_geometry

    fictitious_known, fictitious_true, _ = _strict_boolean_masks(
        output["fictitious_raw"]
    )
    private_known, private_true, private_false = _strict_private_masks(
        output["private_raw"]
    )

    asset_values = policy.asset_state
    asset_domain = frozenset(
        {
            *asset_values.in_service,
            *asset_values.project_geometry_not_significant,
            *asset_values.under_construction,
        }
    )
    asset_known, asset_unknown = _known_string_masks(
        output["asset_status_raw"], asset_domain
    )

    nature_values = policy.nature
    nature_domain = frozenset(
        {
            *nature_values.general_motor_road,
            *nature_values.limited_motor_proxy,
            *nature_values.non_general_vehicle,
            *nature_values.special_review,
        }
    )
    nature_known, nature_unknown = _known_string_masks(
        output["nature_raw"], nature_domain
    )

    access_values = policy.light_vehicle_access
    access_domain = frozenset(
        {
            *access_values.open,
            *access_values.toll,
            *access_values.rights_restricted,
            *access_values.physically_impossible,
        }
    )
    access_known, access_unknown = _known_string_masks(
        output["light_vehicle_access_raw"], access_domain
    )
    importance_known, importance_unknown = _known_string_masks(
        output["importance_raw"], policy.importance.known
    )

    closure_present, closure_unknown = _optional_exact_string_masks(
        output["closure_period_raw"]
    )
    restriction_present, restriction_unknown = _optional_exact_string_masks(
        output["restriction_nature_raw"]
    )
    restriction_known = restriction_present & output[
        "restriction_nature_raw"
    ].isin(policy.known_restriction_review)
    restriction_other = restriction_present & ~restriction_known
    narrow, width_unknown = _width_masks(
        output["carriageway_width_raw"], policy.width_below_m
    )

    unknown_masks = {
        "fictitious_raw": ~fictitious_known,
        "asset_status_raw": asset_unknown,
        "nature_raw": nature_unknown,
        "light_vehicle_access_raw": access_unknown,
        "private_raw": ~private_known,
        "importance_raw": importance_unknown,
        "carriageway_width_raw": width_unknown,
        "closure_period_raw": closure_unknown,
        "restriction_nature_raw": restriction_unknown,
    }
    unknown_any = _false_mask(index)
    for mask in unknown_masks.values():
        unknown_any |= mask.fillna(False)

    rule_masks: dict[str, pd.Series] = {
        "FICTITIOUS_GEOMETRY": fictitious_true,
        "PROJECT_GEOMETRY_NOT_SIGNIFICANT": output["asset_status_raw"].isin(
            asset_values.project_geometry_not_significant
        ),
        "NOT_IN_SERVICE": output["asset_status_raw"].isin(
            asset_values.under_construction
        ),
        "PHYSICALLY_IMPOSSIBLE": output["light_vehicle_access_raw"].isin(
            access_values.physically_impossible
        ),
        "NON_GENERAL_VEHICLE_NATURE": output["nature_raw"].isin(
            nature_values.non_general_vehicle
        ),
        "RIGHTS_RESTRICTED": output["light_vehicle_access_raw"].isin(
            access_values.rights_restricted
        ),
        "PRIVATE_ROAD": private_true,
        "TEMPORAL_CLOSURE": closure_present,
        "KNOWN_RESTRICTION": restriction_known,
        "OTHER_RECORDED_RESTRICTION": restriction_other,
        "SPECIAL_NATURE": output["nature_raw"].isin(nature_values.special_review),
        "LIMITED_NATURE": output["nature_raw"].isin(
            nature_values.limited_motor_proxy
        ),
        "IMPORTANCE_6": output["importance_raw"].isin(policy.importance.limited),
        "NARROW_CARRIAGEWAY": narrow,
    }
    higher_rule = _false_mask(index)
    for mask in rule_masks.values():
        higher_rule |= mask.fillna(False)

    open_or_toll = (
        fictitious_known
        & ~fictitious_true
        & asset_known
        & output["asset_status_raw"].isin(asset_values.in_service)
        & nature_known
        & output["nature_raw"].isin(nature_values.general_motor_road)
        & access_known
        & output["light_vehicle_access_raw"].isin(
            access_values.open | access_values.toll
        )
        & private_known
        & private_false
        & importance_known
        & ~unknown_any
        & ~higher_rule
    )
    rule_masks["OPEN_OR_TOLL"] = open_or_toll
    determined = higher_rule | open_or_toll
    rule_masks["UNKNOWN"] = unknown_any | ~determined
    rule_masks = {
        rule: valid_geometry & mask.fillna(False).astype(bool)
        for rule, mask in rule_masks.items()
    }

    outcomes = _rule_outcomes(policy)
    if set(outcomes) != set(policy.decision_precedence):
        raise IgnRoadVehicleProxyApplicationError(
            "Compiled policy precedence and outcomes do not agree"
        )

    primary = pd.Series(pd.NA, index=index, dtype="string")
    proxy_class = pd.Series(pd.NA, index=index, dtype="string")
    primary.loc[technical_geometry] = _TECHNICAL_GEOMETRY_RULE
    proxy_class.loc[technical_geometry] = policy.classes.not_distance_proxy
    for rule in policy.decision_precedence:
        first = rule_masks[rule] & primary.isna()
        primary.loc[first] = rule
        proxy_class.loc[first] = outcomes[rule]
    if primary.isna().any() or proxy_class.isna().any():
        raise IgnRoadVehicleProxyApplicationError(
            "Every normalized IGN road must receive one primary policy result"
        )

    policy_trace_masks = tuple(
        (rule, rule_masks[rule]) for rule in policy.decision_precedence
    )
    trace = _json_array_from_masks(
        index,
        ((_TECHNICAL_GEOMETRY_RULE, technical_geometry), *policy_trace_masks),
    )
    unknown_fields = _json_array_from_masks(
        index,
        tuple((field, unknown_masks[field]) for field in _UNKNOWN_FIELD_ORDER),
    )

    output["road_proxy_primary_rule"] = primary
    output["road_proxy_class"] = proxy_class
    output["road_proxy_rule_trace_json"] = trace
    output["road_proxy_unknown_fields_json"] = unknown_fields
    output["road_proxy_toll_evidence"] = output[
        "light_vehicle_access_raw"
    ].isin(access_values.toll)
    output["road_proxy_policy_id"] = policy.policy_id
    output["road_proxy_policy_schema_version"] = policy.schema_version
    output["road_proxy_policy_config_sha256"] = policy.config_sha256
    output["road_proxy_policy_scope"] = policy.scope
    output["road_proxy_policy_evidence_checked_on"] = policy.evidence_checked_on
    output["road_proxy_vehicle_scope"] = policy.vehicle_scope
    output["road_proxy_heavy_vehicle_access"] = policy.heavy_vehicle_access

    result = gpd.GeoDataFrame(
        output.loc[:, [*source.columns, *_APPLICATION_COLUMNS]],
        geometry=source.active_geometry_name,
        crs=source.crs,
    )
    if len(result) != len(source) or not result.index.equals(source.index):
        raise IgnRoadVehicleProxyApplicationError(
            "IGN road policy application changed row count or order"
        )
    return result


def _apply_ign_road_vehicle_proxy_policy(
    source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None,
) -> IgnRoadVehicleProxyApplicationResult:
    normalized = normalize_ign_roads(source, source_config)
    if type(normalized) is not NormalizedIgnRoadData:
        raise IgnRoadVehicleProxyApplicationError(
            "IGN road normalization returned an invalid result type"
        )
    policy = (
        load_ign_road_vehicle_proxy_policy()
        if policy_path is None
        else load_ign_road_vehicle_proxy_policy(policy_path)
    )
    return IgnRoadVehicleProxyApplicationResult(
        roads=_classify_road_frame(normalized.road_segments, policy)
    )


def apply_ign_road_vehicle_proxy_policy(
    source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None = None,
) -> IgnRoadVehicleProxyApplicationResult:
    """Source-completely normalize roads and apply the exact policy bytes once."""

    try:
        if type(source) is not IgnBdTopoRoadData:
            raise TypeError("source must be an IgnBdTopoRoadData")
        if type(source_config) is not IgnBdTopoSourceConfig:
            raise TypeError("source_config must be an IgnBdTopoSourceConfig")
        if policy_path is not None and not isinstance(policy_path, Path):
            raise TypeError("policy_path must be a pathlib.Path or None")
        return _apply_ign_road_vehicle_proxy_policy(
            source, source_config, policy_path
        )
    except IgnRoadVehicleProxyApplicationError:
        raise
    except Exception as error:
        raise IgnRoadVehicleProxyApplicationError(
            "IGN road vehicle-proxy policy cannot be applied safely"
        ) from error

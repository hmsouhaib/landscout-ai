"""Compute threshold-free parcel proximity by IGN road proxy class."""

from __future__ import annotations

from dataclasses import dataclass
from numbers import Integral
from pathlib import Path

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
from pandas.api.types import (  # type: ignore[import-untyped]
    is_bool_dtype,
    is_numeric_dtype,
)
from pyproj import CRS
from shapely import STRtree, force_2d  # type: ignore[import-untyped]

from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
)
from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationResult,
    apply_ign_road_vehicle_proxy_policy,
)
from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    load_ign_road_vehicle_proxy_policy,
)

__all__ = [
    "ParcelRoadProximityResult",
    "RoadProximityError",
    "RoadProxyClassCoverage",
    "enrich_parcel_road_proximity",
]

_PARCEL_STORAGE_CRS = "EPSG:4326"
_CALCULATION_CRS = "EPSG:2154"
_PROXIMITY_SCOPE = "WITHIN_VERIFIED_SOURCE_PACKAGE"
_PARCEL_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})
_ROAD_GEOMETRY_TYPES = frozenset({"LineString", "MultiLineString"})
_ROAD_GEOMETRY_STATUSES = frozenset({"VALID", "NULL", "EMPTY", "INVALID"})

_ROAD_MATCH_COLUMNS = (
    "road_feature_id",
    "source_feature_id",
    "road_proxy_primary_rule",
    "road_proxy_rule_trace_json",
    "road_proxy_unknown_fields_json",
    "road_proxy_toll_evidence",
    "nature_raw",
    "importance_raw",
    "asset_status_raw",
    "private_raw",
    "light_vehicle_access_raw",
    "carriageway_width_raw",
    "closure_period_raw",
    "restriction_nature_raw",
    "source_layer",
    "source_department_code",
    "source_edition",
    "source_archive_sha256",
)
_ROAD_REQUIRED_COLUMNS = frozenset(
    {
        *_ROAD_MATCH_COLUMNS,
        "geometry_status",
        "road_proxy_class",
        "road_proxy_policy_id",
        "road_proxy_policy_schema_version",
        "road_proxy_policy_config_sha256",
        "road_proxy_policy_scope",
        "road_proxy_heavy_vehicle_access",
        "geometry",
    }
)
_MATCH_OUTPUT_MAPPING = {
    "distance_m": "nearest_road_proxy_distance_m",
    "road_feature_id": "nearest_road_feature_id",
    "source_feature_id": "nearest_source_feature_id",
    "tie_count": "nearest_road_tie_count",
    "road_proxy_primary_rule": "nearest_road_primary_rule",
    "road_proxy_rule_trace_json": "nearest_road_rule_trace_json",
    "road_proxy_unknown_fields_json": "nearest_road_unknown_fields_json",
    "road_proxy_toll_evidence": "nearest_road_toll_evidence",
    "nature_raw": "nearest_nature_raw",
    "importance_raw": "nearest_importance_raw",
    "asset_status_raw": "nearest_asset_status_raw",
    "private_raw": "nearest_private_raw",
    "light_vehicle_access_raw": "nearest_light_vehicle_access_raw",
    "carriageway_width_raw": "nearest_carriageway_width_raw",
    "closure_period_raw": "nearest_closure_period_raw",
    "restriction_nature_raw": "nearest_restriction_nature_raw",
    "source_layer": "nearest_source_layer",
    "source_department_code": "nearest_source_department_code",
    "source_edition": "nearest_source_edition",
    "source_archive_sha256": "nearest_source_archive_sha256",
}

CLASS_PROXIMITY_COLUMNS = (
    "parcel_id",
    "road_proxy_class",
    "nearest_road_proxy_distance_m",
    "nearest_road_feature_id",
    "nearest_source_feature_id",
    "nearest_road_tie_count",
    "nearest_road_primary_rule",
    "nearest_road_rule_trace_json",
    "nearest_road_unknown_fields_json",
    "nearest_road_toll_evidence",
    "nearest_nature_raw",
    "nearest_importance_raw",
    "nearest_asset_status_raw",
    "nearest_private_raw",
    "nearest_light_vehicle_access_raw",
    "nearest_carriageway_width_raw",
    "nearest_closure_period_raw",
    "nearest_restriction_nature_raw",
    "nearest_source_layer",
    "nearest_source_department_code",
    "nearest_source_edition",
    "nearest_source_archive_sha256",
    "road_proxy_policy_id",
    "road_proxy_policy_schema_version",
    "road_proxy_policy_config_sha256",
    "road_proxy_heavy_vehicle_access",
    "proximity_scope",
)


class RoadProximityError(ValueError):
    """Raised when parcel-to-road proximity cannot be proven safely."""


@dataclass(frozen=True)
class RoadProxyClassCoverage:
    """Source coverage and distance eligibility for one policy class."""

    road_proxy_class: str
    feature_count: int
    distance_eligible: bool


@dataclass(frozen=True)
class ParcelRoadProximityResult:
    """Unchanged parcels plus class-specific factual road proximity."""

    parcels: gpd.GeoDataFrame
    class_proximity: pd.DataFrame
    class_coverage: tuple[RoadProxyClassCoverage, ...]


def _validated_crs(value: object, label: str) -> CRS:
    if value is None:
        raise RoadProximityError(f"{label} CRS is required")
    try:
        return CRS.from_user_input(value)
    except Exception as error:
        raise RoadProximityError(f"{label} CRS is unreadable") from error


def _require_crs(value: object, expected_epsg: int, label: str) -> None:
    actual = _validated_crs(value, label)
    expected = CRS.from_epsg(expected_epsg)
    if not actual.equals(expected):
        raise RoadProximityError(f"{label} must use EPSG:{expected_epsg}")


def _validate_exact_ids(
    values: pd.Series,
    label: str,
    *,
    require_unique: bool,
) -> None:
    if values.isna().any():
        raise RoadProximityError(f"{label} values must not be null")
    raw = values.tolist()
    if any(not isinstance(value, str) for value in raw):
        raise RoadProximityError(f"{label} values must be exact strings")
    if any(not value.strip() for value in raw):
        raise RoadProximityError(f"{label} values must not be empty")
    if any(value != value.strip() for value in raw):
        raise RoadProximityError(f"{label} values must not have edge whitespace")
    if require_unique and values.duplicated().any():
        raise RoadProximityError(f"{label} values must be unique")


def _validate_parcels(parcels: object) -> gpd.GeoDataFrame:
    if not isinstance(parcels, gpd.GeoDataFrame):
        raise RoadProximityError("parcels must be a GeoDataFrame")
    if parcels.columns.duplicated().any():
        raise RoadProximityError("Parcel columns must not contain duplicates")
    missing = {"parcel_id", "geometry"} - set(parcels.columns)
    if missing:
        raise RoadProximityError(
            "Missing required parcel columns: " + ", ".join(sorted(missing))
        )
    if parcels.active_geometry_name != "geometry":
        raise RoadProximityError("Parcel geometry column must be active")
    _require_crs(parcels.crs, 4326, "Parcel storage")
    _validate_exact_ids(parcels["parcel_id"], "parcel_id", require_unique=True)
    if parcels.geometry.isna().any():
        raise RoadProximityError("Parcel geometries must not be null")
    if parcels.geometry.is_empty.any():
        raise RoadProximityError("Parcel geometries must not be empty")
    if not parcels.geometry.is_valid.all():
        raise RoadProximityError("Parcel geometries must be valid")
    unsupported = sorted(
        set(parcels.geometry.geom_type.dropna()) - _PARCEL_GEOMETRY_TYPES
    )
    if unsupported:
        raise RoadProximityError(
            "Parcel geometries must be Polygon or MultiPolygon; found: "
            + ", ".join(str(value) for value in unsupported)
        )
    return parcels


def _policy_classes(
    policy: IgnRoadVehicleProxyPolicy,
) -> tuple[tuple[str, ...], tuple[str, ...]]:
    all_classes = policy.classes.values
    if len(all_classes) != 6 or len(set(all_classes)) != 6:
        raise RoadProximityError("Compiled road policy class domain is invalid")
    non_distance = policy.classes.not_distance_proxy
    eligible = tuple(value for value in all_classes if value != non_distance)
    if len(eligible) != 5 or non_distance not in all_classes:
        raise RoadProximityError("Compiled road distance eligibility is invalid")
    return all_classes, eligible


def _require_row_lineage(
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> None:
    expected = {
        "road_proxy_policy_id": policy.policy_id,
        "road_proxy_policy_schema_version": policy.schema_version,
        "road_proxy_policy_config_sha256": policy.config_sha256,
        "road_proxy_policy_scope": policy.scope,
        "road_proxy_heavy_vehicle_access": policy.heavy_vehicle_access,
    }
    for column, value in expected.items():
        if roads[column].isna().any() or not roads[column].eq(value).all():
            raise RoadProximityError(
                f"Road application policy lineage differs in {column}"
            )


def _validate_application_roads(
    application: object,
    policy: IgnRoadVehicleProxyPolicy,
) -> gpd.GeoDataFrame:
    if type(application) is not IgnRoadVehicleProxyApplicationResult:
        raise RoadProximityError("Road application result type is invalid")
    roads = application.roads
    if not isinstance(roads, gpd.GeoDataFrame):
        raise RoadProximityError("Road application roads must be a GeoDataFrame")
    if roads.columns.duplicated().any():
        raise RoadProximityError("Road application columns must not be duplicated")
    missing = _ROAD_REQUIRED_COLUMNS - set(roads.columns)
    if missing:
        raise RoadProximityError(
            "Missing road application column or lineage: "
            + ", ".join(sorted(missing))
        )
    if roads.active_geometry_name != "geometry":
        raise RoadProximityError("Road application geometry must be active")
    _require_crs(roads.crs, 2154, "Road application")
    _validate_exact_ids(
        roads["road_feature_id"], "road_feature_id", require_unique=True
    )
    _validate_exact_ids(
        roads["source_feature_id"], "source_feature_id", require_unique=False
    )

    all_classes, eligible_classes = _policy_classes(policy)
    classes = roads["road_proxy_class"]
    if classes.isna().any() or not classes.isin(all_classes).all():
        raise RoadProximityError("Road application has an unknown proxy class")
    _require_row_lineage(roads, policy)

    statuses = roads["geometry_status"]
    if statuses.isna().any() or not statuses.isin(_ROAD_GEOMETRY_STATUSES).all():
        raise RoadProximityError("Road application geometry status is invalid")
    eligible = classes.isin(eligible_classes)
    if not statuses.loc[eligible].eq("VALID").all():
        raise RoadProximityError(
            "Distance-eligible roads must have VALID geometry status"
        )
    eligible_geometry = roads.loc[eligible, "geometry"]
    if eligible_geometry.isna().any():
        raise RoadProximityError("Distance-eligible road geometry must not be null")
    if eligible_geometry.is_empty.any():
        raise RoadProximityError("Distance-eligible road geometry must not be empty")
    if not eligible_geometry.is_valid.all():
        raise RoadProximityError("Distance-eligible road geometry must be valid")
    unsupported = sorted(
        set(eligible_geometry.geom_type.dropna()) - _ROAD_GEOMETRY_TYPES
    )
    if unsupported:
        raise RoadProximityError(
            "Distance-eligible geometry must be LineString or MultiLineString; found: "
            + ", ".join(str(value) for value in unsupported)
        )
    return roads


def _calculation_geometries(frame: gpd.GeoDataFrame) -> np.ndarray:
    values = np.asarray(frame.geometry.array, dtype=object)
    return np.asarray(force_2d(values), dtype=object)


def _empty_nearest_rows(parcel_count: int) -> pd.DataFrame:
    output = pd.DataFrame(index=pd.RangeIndex(parcel_count))
    output["distance_m"] = pd.Series(np.nan, index=output.index, dtype="float64")
    output["tie_count"] = pd.Series(pd.NA, index=output.index, dtype="Int64")
    for column in _ROAD_MATCH_COLUMNS:
        if column == "road_proxy_toll_evidence":
            output[column] = pd.Series(pd.NA, index=output.index, dtype="boolean")
        else:
            output[column] = pd.Series(pd.NA, index=output.index, dtype="object")
    return output


def _nearest_class_rows(
    parcel_geometries: np.ndarray,
    roads: gpd.GeoDataFrame,
) -> pd.DataFrame:
    parcel_count = len(parcel_geometries)
    if roads.empty:
        return _empty_nearest_rows(parcel_count)

    tree = STRtree(_calculation_geometries(roads))
    indices, distances = tree.query_nearest(
        parcel_geometries,
        all_matches=True,
        return_distance=True,
    )
    matches = pd.DataFrame(
        {
            "parcel_position": indices[0],
            "road_position": indices[1],
            "distance_m": distances,
        }
    )
    matches["road_feature_id"] = roads.iloc[
        matches["road_position"].to_numpy()
    ]["road_feature_id"].to_numpy()
    matches = matches.sort_values(
        ["parcel_position", "distance_m", "road_feature_id"],
        kind="mergesort",
    )
    ties = matches.groupby("parcel_position", sort=False).size()
    selected = matches.drop_duplicates("parcel_position", keep="first").sort_values(
        "parcel_position", kind="mergesort"
    )
    if selected["parcel_position"].tolist() != list(range(parcel_count)):
        raise RoadProximityError(
            "Nearest-road matching did not cover every parcel"
        )

    source_rows = roads.iloc[selected["road_position"].to_numpy()]
    output = source_rows.loc[:, list(_ROAD_MATCH_COLUMNS)].reset_index(drop=True)
    output.insert(
        0,
        "tie_count",
        pd.Series(ties.reindex(range(parcel_count)).to_numpy(), dtype="Int64"),
    )
    output.insert(
        0,
        "distance_m",
        selected["distance_m"].to_numpy(dtype="float64"),
    )
    return output


def _coverage(
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> tuple[RoadProxyClassCoverage, ...]:
    all_classes, eligible_classes = _policy_classes(policy)
    counts = roads["road_proxy_class"].value_counts()
    return tuple(
        RoadProxyClassCoverage(
            road_proxy_class=road_class,
            feature_count=int(counts.get(road_class, 0)),
            distance_eligible=road_class in eligible_classes,
        )
        for road_class in all_classes
    )


def _class_proximity_table(
    parcel_ids: pd.Series,
    parcel_geometries: np.ndarray,
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> pd.DataFrame:
    _, eligible_classes = _policy_classes(policy)
    tables: list[pd.DataFrame] = []
    for class_position, road_class in enumerate(eligible_classes):
        class_roads = roads.loc[
            roads["road_proxy_class"].eq(road_class)
        ].reset_index(drop=True)
        nearest = _nearest_class_rows(parcel_geometries, class_roads)
        _validate_distance_and_ties(
            nearest.rename(
                columns={
                    "distance_m": "nearest_road_proxy_distance_m",
                    "tie_count": "nearest_road_tie_count",
                }
            ),
            expect_matches=not class_roads.empty,
        )
        table = pd.DataFrame(
            {
                "_parcel_position": np.arange(len(parcel_ids), dtype="int64"),
                "_class_position": class_position,
                "parcel_id": parcel_ids.reset_index(drop=True),
                "road_proxy_class": road_class,
            }
        )
        for source_column, output_column in _MATCH_OUTPUT_MAPPING.items():
            table[output_column] = nearest[source_column].reset_index(drop=True)
        table["road_proxy_policy_id"] = policy.policy_id
        table["road_proxy_policy_schema_version"] = policy.schema_version
        table["road_proxy_policy_config_sha256"] = policy.config_sha256
        table["road_proxy_heavy_vehicle_access"] = policy.heavy_vehicle_access
        table["proximity_scope"] = _PROXIMITY_SCOPE
        tables.append(table)

    output = pd.concat(tables, ignore_index=True)
    output = output.sort_values(
        ["_parcel_position", "_class_position"], kind="mergesort"
    ).reset_index(drop=True)
    output = output.drop(columns=["_parcel_position", "_class_position"])
    output["nearest_road_proxy_distance_m"] = output[
        "nearest_road_proxy_distance_m"
    ].astype("float64")
    output["nearest_road_tie_count"] = output["nearest_road_tie_count"].astype(
        "Int64"
    )
    output["nearest_road_toll_evidence"] = output[
        "nearest_road_toll_evidence"
    ].astype("boolean")
    return output.loc[:, list(CLASS_PROXIMITY_COLUMNS)]


def _is_missing_scalar(value: object) -> bool:
    if value is None:
        return True
    try:
        return bool(pd.isna(value))
    except (TypeError, ValueError):
        return False


def _validate_distance_and_ties(
    rows: pd.DataFrame,
    *,
    expect_matches: bool,
) -> None:
    distances = rows["nearest_road_proxy_distance_m"]
    matched = distances.notna()
    if expect_matches and not matched.all():
        raise RoadProximityError("Non-empty road classes require parcel matches")
    if not expect_matches and matched.any():
        raise RoadProximityError("Empty road classes must not contain matches")
    if matched.any():
        if not is_numeric_dtype(distances.dtype) or is_bool_dtype(distances.dtype):
            raise RoadProximityError("Matched road distances must be numeric")
        numeric = distances.loc[matched].to_numpy(dtype="float64")
        if not np.isfinite(numeric).all() or (numeric < 0).any():
            raise RoadProximityError("Matched road distances must be finite and >= 0")

    ties = rows["nearest_road_tie_count"]
    for value, row_matched in zip(
        ties.tolist(), matched.to_numpy(dtype=bool), strict=True
    ):
        missing = _is_missing_scalar(value)
        if not row_matched:
            if not missing:
                raise RoadProximityError("Unmatched rows require null tie_count")
            continue
        if (
            missing
            or not isinstance(value, Integral)
            or isinstance(value, (bool, np.bool_))
            or int(value) < 1
        ):
            raise RoadProximityError(
                "Matched nearest_road_tie_count must be an integer >= 1"
            )


def _null_safe_equal(actual: pd.Series, expected: pd.Series) -> bool:
    left = actual.reset_index(drop=True)
    right = expected.reset_index(drop=True)
    if len(left) != len(right):
        return False
    both_null = left.isna() & right.isna()
    try:
        equal = left.eq(right).fillna(False)
    except (TypeError, ValueError):
        return False
    return bool((both_null | equal).all())


def _validate_selected_evidence(
    table: pd.DataFrame,
    roads: gpd.GeoDataFrame,
) -> None:
    matched = table["nearest_road_feature_id"].notna()
    selected = table.loc[matched].reset_index(drop=True)
    if selected.empty:
        return
    lookup = roads.set_index("road_feature_id", drop=False)
    positions = lookup.index.get_indexer(selected["nearest_road_feature_id"])
    if (positions < 0).any():
        raise RoadProximityError("Selected nearest road ID is absent from source")
    expected = lookup.iloc[positions].reset_index(drop=True)
    if not selected["road_proxy_class"].reset_index(drop=True).eq(
        expected["road_proxy_class"]
    ).all():
        raise RoadProximityError("Selected nearest road has the wrong proxy class")

    for source_column, output_column in _MATCH_OUTPUT_MAPPING.items():
        if source_column in {"distance_m", "tie_count"}:
            continue
        if not _null_safe_equal(selected[output_column], expected[source_column]):
            raise RoadProximityError(
                f"Selected nearest road evidence differs for {output_column}"
            )


def _validate_coverage(
    coverage: tuple[RoadProxyClassCoverage, ...],
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> tuple[str, ...]:
    all_classes, eligible_classes = _policy_classes(policy)
    if type(coverage) is not tuple or len(coverage) != len(all_classes):
        raise RoadProximityError("Road class coverage is incomplete")
    counts = roads["road_proxy_class"].value_counts()
    total = 0
    for position, item in enumerate(coverage):
        if type(item) is not RoadProxyClassCoverage:
            raise RoadProximityError("Road class coverage entry type is invalid")
        road_class = all_classes[position]
        if item.road_proxy_class != road_class:
            raise RoadProximityError("Road class coverage order is invalid")
        if type(item.feature_count) is not int or item.feature_count < 0:
            raise RoadProximityError("Road class feature_count must be an integer >= 0")
        if type(item.distance_eligible) is not bool:
            raise RoadProximityError("Road class distance_eligible must be Boolean")
        if item.distance_eligible != (road_class in eligible_classes):
            raise RoadProximityError("Road class distance eligibility is invalid")
        if item.feature_count != int(counts.get(road_class, 0)):
            raise RoadProximityError("Road class feature_count differs from source")
        total += item.feature_count
    if total != len(roads):
        raise RoadProximityError("Road class coverage does not sum to source rows")
    return eligible_classes


def _validate_parcel_preservation(
    source: gpd.GeoDataFrame,
    output: gpd.GeoDataFrame,
) -> None:
    if len(output) != len(source):
        raise RoadProximityError("Road proximity changed parcel count")
    if list(output.columns) != list(source.columns):
        raise RoadProximityError("Road proximity changed parcel columns")
    if not output.dtypes.equals(source.dtypes):
        raise RoadProximityError("Road proximity changed parcel dtypes")
    if (
        type(output.index) is not type(source.index)
        or output.index.names != source.index.names
        or str(output.index.dtype) != str(source.index.dtype)
        or not output.index.equals(source.index)
    ):
        raise RoadProximityError("Road proximity changed parcel index metadata")
    if not _validated_crs(output.crs, "Output parcel").equals(
        _validated_crs(source.crs, "Source parcel")
    ):
        raise RoadProximityError("Road proximity changed parcel CRS")
    if not output.geometry.to_wkb().equals(source.geometry.to_wkb()):
        raise RoadProximityError("Road proximity changed parcel geometry WKB")
    geometry_column = source.active_geometry_name
    if geometry_column is None or not output.drop(columns=geometry_column).equals(
        source.drop(columns=geometry_column)
    ):
        raise RoadProximityError("Road proximity changed parcel facts")


def _validate_result(
    source_parcels: gpd.GeoDataFrame,
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
    result: ParcelRoadProximityResult,
) -> None:
    if type(result) is not ParcelRoadProximityResult:
        raise RoadProximityError("Road proximity result type is invalid")
    if not isinstance(result.parcels, gpd.GeoDataFrame):
        raise RoadProximityError("Road proximity parcels must be a GeoDataFrame")
    if type(result.class_proximity) is not pd.DataFrame:
        raise RoadProximityError("Class proximity must be a plain DataFrame")
    _validate_parcel_preservation(source_parcels, result.parcels)
    eligible_classes = _validate_coverage(
        result.class_coverage, roads, policy
    )
    table = result.class_proximity
    if table.columns.duplicated().any() or list(table.columns) != list(
        CLASS_PROXIMITY_COLUMNS
    ):
        raise RoadProximityError("Class proximity schema is invalid")
    if len(table) != len(source_parcels) * len(eligible_classes):
        raise RoadProximityError("Class proximity row count is invalid")
    expected_ids = [
        parcel_id
        for parcel_id in source_parcels["parcel_id"].tolist()
        for _ in eligible_classes
    ]
    expected_classes = list(eligible_classes) * len(source_parcels)
    if table["parcel_id"].tolist() != expected_ids:
        raise RoadProximityError("Class proximity parcel order is invalid")
    if table["road_proxy_class"].tolist() != expected_classes:
        raise RoadProximityError("Class proximity class order is invalid")
    if policy.classes.not_distance_proxy in set(table["road_proxy_class"]):
        raise RoadProximityError("NOT_DISTANCE_PROXY cannot have distance rows")
    if table.duplicated(["parcel_id", "road_proxy_class"]).any():
        raise RoadProximityError("Class proximity parcel/class pairs must be unique")

    coverage = {item.road_proxy_class: item for item in result.class_coverage}
    required_match_values = (
        "nearest_road_feature_id",
        "nearest_source_feature_id",
        "nearest_road_primary_rule",
        "nearest_road_rule_trace_json",
        "nearest_road_unknown_fields_json",
        "nearest_road_toll_evidence",
        "nearest_source_layer",
        "nearest_source_department_code",
        "nearest_source_edition",
        "nearest_source_archive_sha256",
    )
    for road_class in eligible_classes:
        rows = table.loc[table["road_proxy_class"].eq(road_class)]
        expect_matches = coverage[road_class].feature_count > 0
        _validate_distance_and_ties(rows, expect_matches=expect_matches)
        if expect_matches:
            for column in required_match_values:
                if rows[column].isna().any():
                    raise RoadProximityError(
                        f"Matched class rows require {column}"
                    )
        elif rows.loc[:, list(_MATCH_OUTPUT_MAPPING.values())].notna().any().any():
            raise RoadProximityError(
                "Empty-class selected road evidence must be entirely null"
            )

    expected_lineage = {
        "road_proxy_policy_id": policy.policy_id,
        "road_proxy_policy_schema_version": policy.schema_version,
        "road_proxy_policy_config_sha256": policy.config_sha256,
        "road_proxy_heavy_vehicle_access": policy.heavy_vehicle_access,
        "proximity_scope": _PROXIMITY_SCOPE,
    }
    for column, value in expected_lineage.items():
        if table[column].isna().any() or not table[column].eq(value).all():
            raise RoadProximityError(
                f"Class proximity lineage differs in {column}"
            )
    _validate_selected_evidence(table, roads)


def _enrich_parcel_road_proximity(
    parcels: gpd.GeoDataFrame,
    road_source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None,
) -> ParcelRoadProximityResult:
    source_parcels = _validate_parcels(parcels)
    policy = (
        load_ign_road_vehicle_proxy_policy()
        if policy_path is None
        else load_ign_road_vehicle_proxy_policy(policy_path)
    )
    application = apply_ign_road_vehicle_proxy_policy(
        road_source, source_config, policy_path
    )
    roads = _validate_application_roads(application, policy)

    output_parcels = source_parcels.copy(deep=True)
    calculation_parcels = source_parcels.to_crs(_CALCULATION_CRS)
    parcel_geometries = _calculation_geometries(calculation_parcels)
    class_proximity = _class_proximity_table(
        source_parcels["parcel_id"], parcel_geometries, roads, policy
    )
    result = ParcelRoadProximityResult(
        parcels=output_parcels,
        class_proximity=class_proximity,
        class_coverage=_coverage(roads, policy),
    )
    _validate_result(source_parcels, roads, policy, result)
    return result


def enrich_parcel_road_proximity(
    parcels: gpd.GeoDataFrame,
    road_source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None = None,
) -> ParcelRoadProximityResult:
    """Compute exact class-specific distance within the verified source package."""

    try:
        if not isinstance(parcels, gpd.GeoDataFrame):
            raise RoadProximityError(
                "parcels must be a GeoDataFrame with active geometry"
            )
        if type(road_source) is not IgnBdTopoRoadData:
            raise RoadProximityError(
                "road_source must be an IgnBdTopoRoadData"
            )
        if type(source_config) is not IgnBdTopoSourceConfig:
            raise RoadProximityError(
                "source_config must be an IgnBdTopoSourceConfig"
            )
        if policy_path is not None and not isinstance(policy_path, Path):
            raise RoadProximityError(
                "policy_path must be a pathlib.Path or None"
            )
        return _enrich_parcel_road_proximity(
            parcels, road_source, source_config, policy_path
        )
    except RoadProximityError:
        raise
    except Exception as error:
        raise RoadProximityError(
            "Parcel-to-road proximity cannot be computed safely"
        ) from error

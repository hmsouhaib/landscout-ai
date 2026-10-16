"""Source-bound road evidence integration; no road-based parcel selection."""

import csv
from dataclasses import dataclass
from hashlib import sha256
from math import isfinite
from numbers import Integral, Real
from pathlib import Path

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]

from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_roads,
    validate_ign_bdtopo_archive,
)
from landscout.stages.assess_road_proximity_coverage import (
    RoadProximityCoverageAssessmentResult,
    assess_road_proximity_coverage,
)
from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    RoadProxyClassCoverage,
)
from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    load_ign_road_vehicle_proxy_policy,
)
from landscout.workflows import grid_screening as grid
from landscout.workflows.ign_screening import _IgnContext

# Explicit workflow contract, not imports of private assessment constants.
ROAD_EXPORT_COLUMNS = (
    *CLASS_PROXIMITY_COLUMNS,
    "road_source_boundary_distance_m",
    "road_source_coverage_position",
    "road_proximity_coverage_status",
    "road_source_coverage_provider",
    "road_source_coverage_product",
    "road_source_coverage_department_code",
    "road_source_coverage_edition",
    "road_source_coverage_product_version",
    "road_source_coverage_archive_sha256",
    "road_source_coverage_layer",
    "road_source_coverage_spatial_role",
)
_FLOAT_COLUMNS = frozenset(
    {
        "nearest_road_proxy_distance_m",
        "nearest_carriageway_width_raw",
        "road_source_boundary_distance_m",
    }
)
_INTEGER_COLUMNS = frozenset(
    {"nearest_road_tie_count", "road_proxy_policy_schema_version"}
)
RoadScalar = str | int | float | bool | None


class RoadScreeningError(ValueError):
    """Requested road evidence cannot be safely published."""


@dataclass(frozen=True)
class _RoadOptions:
    policy: IgnRoadVehicleProxyPolicy
    path: Path
    identity: dict[str, str | int]


@dataclass(frozen=True)
class _RoadRun:
    options: grid._GridOptions
    policy_options: _RoadOptions
    context: _IgnContext
    source: IgnBdTopoRoadData
    assessment: RoadProximityCoverageAssessmentResult


def _prepare_roads(root: Path, path: Path | None) -> _RoadOptions:
    # This workflow's default is scan-root-relative, unlike the historical loader.
    absolute = grid._checked_path(
        path
        if path is not None
        else Path("configs/access/ign_bdtopo_vehicle_proxy_policy.yaml"),
        root,
    )
    identity = grid._identity(absolute)
    policy = load_ign_road_vehicle_proxy_policy(absolute)
    if (
        grid._identity(absolute) != identity
        or policy.config_sha256 != identity["sha256"]
    ):
        raise RoadScreeningError("Road policy changed during loading")
    return _RoadOptions(policy, absolute, identity)


def _scalar(value: object, column: str) -> RoadScalar:
    if value is None or bool(pd.isna(value)):
        return None
    boolean = isinstance(value, (bool, np.bool_))
    if column == "nearest_road_toll_evidence":
        if not boolean:
            raise RoadScreeningError("Road toll evidence must be a nullable bool")
        return bool(value)
    if column == "nearest_private_raw":
        if boolean:
            return bool(value)
        if isinstance(value, str):
            return value
        if isinstance(value, Integral):
            return int(value)
        if isinstance(value, Real) and isfinite(float(value)):
            return float(value)
        raise RoadScreeningError("Unsupported private raw fact")
    if boolean:
        raise RoadScreeningError(f"Boolean is not a road numeric/text: {column}")
    if column in _INTEGER_COLUMNS:
        if not isinstance(value, Integral) or value < 1:
            raise RoadScreeningError(f"Road positive integer required: {column}")
        return int(value)
    if column in _FLOAT_COLUMNS:
        if not isinstance(value, Real) or not isfinite(float(value)):
            raise RoadScreeningError(f"Finite road numeric required: {column}")
        if column != "nearest_carriageway_width_raw" and value < 0:
            raise RoadScreeningError("Road distance must not be negative")
        return float(value)
    if not isinstance(value, str):
        raise RoadScreeningError(f"Road text required: {column}")
    return value


def _road_records(run: _RoadRun) -> list[dict[str, RoadScalar]]:
    result, policy = run.assessment, run.policy_options.policy
    classes = policy.classes.values
    coverage = result.class_coverage
    if type(coverage) is not tuple or len(coverage) != len(classes):
        raise RoadScreeningError("Incomplete road class coverage")
    for item, name in zip(coverage, classes, strict=True):
        if (
            type(item) is not RoadProxyClassCoverage
            or item.road_proxy_class != name
            or type(item.feature_count) is not int
            or item.feature_count < 0
            or type(item.distance_eligible) is not bool
            or item.distance_eligible != (name != policy.classes.not_distance_proxy)
        ):
            raise RoadScreeningError("Invalid road class coverage")
    if sum(item.feature_count for item in coverage) != len(run.source.road_segments):
        raise RoadScreeningError("Road class counts differ from the physical source")
    eligible = tuple(
        item.road_proxy_class for item in coverage if item.distance_eligible
    )
    table = result.class_proximity
    if (
        type(table) is not pd.DataFrame
        or table.columns.duplicated().any()
        or tuple(table.columns) != ROAD_EXPORT_COLUMNS
        or type(table.index) is not pd.RangeIndex
        or table.index.name is not None
        or not table.index.equals(pd.RangeIndex(len(table)))
    ):
        raise RoadScreeningError("Road table schema/index differs from public contract")
    ids = result.parcels["parcel_id"].tolist()
    if (
        table["parcel_id"].tolist() != [p for p in ids for _ in eligible]
        or table["road_proxy_class"].tolist() != list(eligible) * len(ids)
        or table.duplicated(["parcel_id", "road_proxy_class"]).any()
    ):
        raise RoadScreeningError(
            "Road table does not cover the exact ordered parcel/class domain"
        )
    lineage = {
        "road_proxy_policy_id": policy.policy_id,
        "road_proxy_policy_schema_version": policy.schema_version,
        "road_proxy_policy_config_sha256": policy.config_sha256,
        "road_proxy_heavy_vehicle_access": policy.heavy_vehicle_access,
    }
    for column, value in lineage.items():
        if table[column].isna().any() or not table[column].eq(value).all():
            raise RoadScreeningError(f"Road policy lineage differs: {column}")
    # Copies of scalar records only: no sorting or resetting of the public result.
    records = [
        {key: _scalar(row[key], key) for key in ROAD_EXPORT_COLUMNS}
        for _, row in table.iterrows()
    ]
    order = {name: position for position, name in enumerate(classes)}
    return sorted(
        records, key=lambda row: (row["parcel_id"], order[row["road_proxy_class"]])
    )


def _run_roads(
    retained: gpd.GeoDataFrame,
    options: grid._GridOptions,
    policy_options: _RoadOptions,
    context: _IgnContext,
) -> _RoadRun:
    before = retained.copy(deep=True)
    source = load_ign_bdtopo_roads(context.extraction, options.config)
    result = assess_road_proximity_coverage(
        retained, source, options.config, policy_options.path
    )
    if type(result) is not RoadProximityCoverageAssessmentResult:
        raise RoadScreeningError("Invalid road assessment result type")
    # Strict original index; unlike grid, roads has no restoration exception.
    grid._compare_frame(retained, before)
    grid._compare_frame(result.parcels, before)
    run = _RoadRun(options, policy_options, context, source, result)
    _road_records(run)
    return run


def _encoded(value: RoadScalar) -> str:
    if value is None:
        return ""
    if type(value) is bool:
        return "true" if value else "false"
    return str(value)


def _write_road_csv(path: Path, records: list[dict[str, RoadScalar]]) -> None:
    expected = [
        {key: _encoded(row[key]) for key in ROAD_EXPORT_COLUMNS} for row in records
    ]
    with path.open("x", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(
            stream, fieldnames=ROAD_EXPORT_COLUMNS, lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(expected)
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        if (
            tuple(reader.fieldnames or ()) != ROAD_EXPORT_COLUMNS
            or list(reader) != expected
        ):
            raise RoadScreeningError(
                "Written road table differs from public road result"
            )


def _final_road_check(run: _RoadRun) -> None:
    extraction = run.context.extraction
    archive = extraction.archive
    integrity = validate_ign_bdtopo_archive(archive.path, run.options.config)
    for key in (
        "file_size",
        "sha256",
        "official_checksum_algorithm",
        "official_checksum",
        "official_checksum_validated",
    ):
        if type(getattr(integrity, key)) is not type(getattr(archive, key)) or getattr(
            integrity, key
        ) != getattr(archive, key):
            raise RoadScreeningError("IGN archive changed after road calculation")
    fresh = load_ign_bdtopo_roads(extraction, run.options.config)
    source = run.source
    if (
        type(source) is not IgnBdTopoRoadData
        or type(fresh) is not IgnBdTopoRoadData
        or source.extraction is not extraction
        or fresh.extraction is not extraction
    ):
        raise RoadScreeningError("IGN road bundle/extraction identity differs")
    grid._compare_frame(source.road_segments, fresh.road_segments)
    grid._summary_equal(
        source.road_segments_summary, fresh.road_segments_summary, IgnBdTopoLayerSummary
    )
    if any(
        role != "PROXY_GEOMETRY"
        for role in (
            archive.spatial_role,
            extraction.spatial_role,
            source.road_segments_summary.spatial_role,
            fresh.road_segments_summary.spatial_role,
        )
    ):
        raise RoadScreeningError("IGN road spatial role differs")
    used = run.assessment.source_coverage
    fresh_coverage = load_ign_bdtopo_department_coverage(extraction, run.options.config)
    if (
        type(used) is not IgnBdTopoDepartmentCoverage
        or type(fresh_coverage) is not IgnBdTopoDepartmentCoverage
        or used.extraction is not extraction
        or fresh_coverage.extraction is not extraction
    ):
        raise RoadScreeningError("IGN road coverage extraction identity differs")
    grid._compare_frame(used.coverage, fresh_coverage.coverage)
    grid._summary_equal(
        used.summary, fresh_coverage.summary, IgnBdTopoCoverageLayerSummary
    )
    for key in (
        "source_provider",
        "source_product",
        "source_department_code",
        "source_edition",
        "source_product_version",
        "source_archive_sha256",
        "source_layer",
        "spatial_role",
    ):
        if type(getattr(used, key)) is not type(
            getattr(fresh_coverage, key)
        ) or getattr(used, key) != getattr(fresh_coverage, key):
            raise RoadScreeningError("IGN road coverage lineage differs")
    if (
        grid._identity(Path(run.context.marker_identity["path"]))
        != run.context.marker_identity
    ):
        raise RoadScreeningError("IGN extraction marker changed after road calculation")
    if grid._identity(run.policy_options.path) != run.policy_options.identity:
        raise RoadScreeningError("Road policy changed after calculation")


def _policy_provenance(options: _RoadOptions) -> dict[str, object]:
    policy = options.policy
    return {
        "binding": options.identity,
        "policy_id": policy.policy_id,
        "schema_version": policy.schema_version,
        "config_sha256": policy.config_sha256,
        "scope": policy.scope,
        "vehicle_scope": policy.vehicle_scope,
        "heavy_vehicle_access": policy.heavy_vehicle_access,
    }


def _provenance(run: _RoadRun) -> dict[str, object]:
    extraction, coverage = run.context.extraction, run.assessment.source_coverage
    archive = extraction.archive
    return {
        "status": "COMPLETE",
        "policy": _policy_provenance(run.policy_options),
        "archive": {
            key: getattr(archive, key)
            for key in (
                "provider",
                "product",
                "department_code",
                "edition",
                "product_version",
                "projection",
                "package_format",
                "archive_format",
                "source_url",
                "checksum_url",
                "download_timestamp",
                "filename",
                "file_size",
                "sha256",
                "official_checksum_algorithm",
                "official_checksum",
                "official_checksum_validated",
                "cache_hit",
                "spatial_role",
            )
        },
        "archive_path": str(archive.path),
        "extraction": {
            "path": str(extraction.extraction_path),
            "cache_hit": extraction.cache_hit,
            "marker": run.context.marker_identity,
            "spatial_role": extraction.spatial_role,
        },
        "geopackage": {
            "path": str(extraction.geopackage_path),
            "filename": extraction.geopackage_filename,
            "size_bytes": extraction.geopackage_size_bytes,
            "sha256": extraction.geopackage_sha256,
        },
        "layers": {
            "road_segments": run.source.road_segments_summary.source_layer_name,
            "electric_lines_inventory_only": extraction.electric_lines_layer,
            "transformation_posts_inventory_only": extraction.transformation_posts_layer,
            "department": extraction.department_layer,
            "inventory": list(extraction.all_layer_names),
        },
        "source_coverage": {
            "layer": coverage.source_layer,
            "department_code": coverage.source_department_code,
            "spatial_role": coverage.spatial_role,
            "crs": str(coverage.coverage.crs),
            "selected_feature_count": coverage.summary.selected_feature_count,
            "source_feature_count": coverage.summary.source_feature_count,
            "department_code_field": coverage.summary.department_code_field,
            "bounds": [float(v) for v in coverage.coverage.total_bounds],
            "geometry_wkb_sha256": sha256(
                coverage.coverage.geometry.iloc[0].wkb
            ).hexdigest(),
        },
        "class_coverage": [
            {
                "road_proxy_class": item.road_proxy_class,
                "feature_count": item.feature_count,
                "distance_eligible": item.distance_eligible,
            }
            for item in run.assessment.class_coverage
        ],
        "hash_authority": "LOCAL_BYTE_VERIFICATION; pinned official checksum only where configured",
    }

"""Internal source-bound IGN integration for the optional cadastre workflow."""

import subprocess
from dataclasses import dataclass, fields
from hashlib import sha256
from math import isfinite
from numbers import Integral, Real
from pathlib import Path
from urllib.parse import urlparse

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd  # type: ignore[import-untyped]

from landscout.sources.cadastre_fr import build_cadastre_parcelles_url
from landscout.sources.ign_bdtopo_fr import (
    DEFAULT_CACHE_DIR,
    DEFAULT_CONFIG_PATH,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoElectricityData,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)
from landscout.stages.assess_grid_coverage import (
    COVERAGE_LINEAGE_COLUMNS,
    PARCEL_DIAGNOSTIC_COLUMNS,
    VOLTAGE_DIAGNOSTIC_COLUMNS,
    GridCoverageAssessmentResult,
    assess_grid_coverage,
)
from landscout.stages.enrich_grid_proximity import VOLTAGE_PROXIMITY_COLUMNS

# Deliberate export allowlist; no private producer mapping or runtime wildcard.
NEAREST_COLUMNS = (
    "nearest_line_proxy_distance_m",
    "nearest_line_grid_feature_id",
    "nearest_line_source_feature_id",
    "nearest_line_tie_count",
    "nearest_line_voltage_raw",
    "nearest_line_voltage_status",
    "nearest_line_voltage_kv",
    "nearest_line_voltage_upper_bound_kv",
    "nearest_line_manager_name",
    "nearest_line_asset_status_raw",
    "nearest_line_source_department_code",
    "nearest_line_source_edition",
    "nearest_line_source_archive_sha256",
    "nearest_exact_line_proxy_distance_m",
    "nearest_exact_line_grid_feature_id",
    "nearest_exact_line_source_feature_id",
    "nearest_exact_line_tie_count",
    "nearest_exact_line_voltage_kv",
    "nearest_exact_line_manager_name",
    "nearest_exact_line_asset_status_raw",
    "nearest_exact_line_source_department_code",
    "nearest_exact_line_source_edition",
    "nearest_exact_line_source_archive_sha256",
    "nearest_post_proxy_distance_m",
    "nearest_post_grid_feature_id",
    "nearest_post_source_feature_id",
    "nearest_post_tie_count",
    "nearest_post_name",
    "nearest_post_importance_raw",
    "nearest_post_asset_status_raw",
    "nearest_post_source_department_code",
    "nearest_post_source_edition",
    "nearest_post_source_archive_sha256",
)
GRID_COLUMNS = (*NEAREST_COLUMNS, *PARCEL_DIAGNOSTIC_COLUMNS, *COVERAGE_LINEAGE_COLUMNS)
VOLTAGE_EXPORT_COLUMNS = (
    *VOLTAGE_PROXIMITY_COLUMNS,
    *VOLTAGE_DIAGNOSTIC_COLUMNS,
    *COVERAGE_LINEAGE_COLUMNS,
)
INTEGER_COLUMNS = frozenset(
    {
        "nearest_line_tie_count",
        "nearest_exact_line_tie_count",
        "nearest_post_tie_count",
        "tie_count",
    }
)
FLOAT_COLUMNS = frozenset(
    {
        "nearest_line_proxy_distance_m",
        "nearest_exact_line_proxy_distance_m",
        "nearest_post_proxy_distance_m",
        "nearest_line_voltage_kv",
        "nearest_line_voltage_upper_bound_kv",
        "nearest_exact_line_voltage_kv",
        "grid_source_boundary_distance_m",
        "source_boundary_distance_m",
        "voltage_kv",
    }
)


class GridScreeningError(ValueError):
    """The requested grid slice cannot be published safely."""


@dataclass(frozen=True)
class _GridOptions:
    config: IgnBdTopoSourceConfig
    config_path: Path
    config_identity: dict[str, str | int]
    cache_dir: Path
    extraction_dir: Path | None


@dataclass(frozen=True)
class _GridRun:
    options: _GridOptions
    electricity: IgnBdTopoElectricityData
    assessment: GridCoverageAssessmentResult
    parcels: gpd.GeoDataFrame
    marker_identity: dict[str, str | int]


def _identity(path: Path) -> dict[str, str | int]:
    raw = path.read_bytes()
    return {
        "path": str(path),
        "size_bytes": len(raw),
        "sha256": sha256(raw).hexdigest(),
    }


def _checked_path(path: Path, root: Path) -> Path:
    if not isinstance(path, Path):
        raise GridScreeningError("Grid paths must be pathlib.Path values")
    absolute = path if path.is_absolute() else root / path
    for part in (absolute, *absolute.parents):
        if part.is_symlink() or part.is_junction():
            raise GridScreeningError(f"Grid path contains a link or junction: {part}")
    return absolute.resolve()


def _overlaps(first: Path, second: Path) -> bool:
    return (
        first == second or first.is_relative_to(second) or second.is_relative_to(first)
    )


def _prepare_grid(
    root: Path,
    commune: str,
    cadastre_cache: Path,
    destination: Path,
    configurations: tuple[Path, ...],
    config_path: Path | None,
    cache_dir: Path | None,
    extraction_dir: Path | None,
) -> _GridOptions:
    path = _checked_path(
        config_path if config_path is not None else DEFAULT_CONFIG_PATH, root
    )
    identity = _identity(path)
    config = load_ign_bdtopo_source_config(path)
    if _identity(path) != identity:
        raise GridScreeningError("IGN configuration changed during loading")
    # Use the existing canonical commune/department contract, including Corsica/DOM.
    department = urlparse(build_cadastre_parcelles_url(commune)).path.rsplit("/", 3)[-3]
    if department != config.department_code:
        raise GridScreeningError(
            "Commune department differs from IGN source department"
        )
    cache = _checked_path(
        cache_dir if cache_dir is not None else DEFAULT_CACHE_DIR, root
    )
    cadastre = _checked_path(cadastre_cache, root)
    extraction = (
        _checked_path(extraction_dir, root) if extraction_dir is not None else None
    )
    output = _checked_path(destination, root)
    configs = (*configurations, path)
    directories = (cadastre, cache, *((extraction,) if extraction is not None else ()))
    if _overlaps(cadastre, cache) or any(_overlaps(output, p) for p in directories):
        raise GridScreeningError("Grid/cadastre caches and output paths collide")
    if extraction is not None and (
        _overlaps(extraction, cadastre)
        or cache == extraction
        or cache.is_relative_to(extraction)
    ):
        raise GridScreeningError("IGN extraction path collides with a cache")
    protected = [*configs, root / ".git"]
    if (root / ".git").exists():
        try:
            listed = subprocess.run(
                ["git", "-C", str(root), "ls-files", "--cached", "-z"],
                capture_output=True,
                check=True,
                timeout=15,
            )
        except (OSError, subprocess.SubprocessError) as error:
            raise GridScreeningError(
                "Cannot preflight grid paths against tracked files"
            ) from error
        protected.extend(
            root / p.decode("utf-8") for p in listed.stdout.split(b"\0") if p
        )
    if any(
        _overlaps(directory, target.resolve())
        for directory in directories
        for target in protected
    ):
        raise GridScreeningError(
            "Grid/cache/extraction path collides with configuration or tracked paths"
        )
    if any(_overlaps(output, target.resolve()) for target in configs):
        raise GridScreeningError("Grid output collides with configuration")
    return _GridOptions(config, path, identity, cache, extraction)


def _compare_frame(supplied: gpd.GeoDataFrame, expected: gpd.GeoDataFrame) -> None:
    """Full strict comparison, including index class and byte-level geometry."""
    try:
        if not isinstance(supplied, gpd.GeoDataFrame) or not isinstance(
            expected, gpd.GeoDataFrame
        ):
            raise TypeError("Expected GeoDataFrames")
        if tuple(supplied.columns) != tuple(
            expected.columns
        ) or not supplied.dtypes.equals(expected.dtypes):
            raise AssertionError("columns or dtypes differ")
        if (
            type(supplied.index) is not type(expected.index)
            or supplied.index.names != expected.index.names
            or not supplied.index.equals(expected.index)
        ):
            raise AssertionError("index differs")
        if (
            supplied.active_geometry_name != expected.active_geometry_name
            or supplied.crs != expected.crs
        ):
            raise AssertionError("active geometry or CRS differs")
        geometry = expected.active_geometry_name
        if geometry is None:
            raise AssertionError("geometry missing")
        pd.testing.assert_frame_equal(
            pd.DataFrame(supplied.drop(columns=geometry)),
            pd.DataFrame(expected.drop(columns=geometry)),
            check_dtype=True,
            check_index_type=True,
            check_column_type=True,
            check_names=True,
            check_exact=True,
        )
        if (
            supplied.geometry.to_wkb().tolist() != expected.geometry.to_wkb().tolist()
            or supplied.attrs != expected.attrs
        ):
            raise AssertionError("WKB or frame attributes differ")
    except (AssertionError, AttributeError, TypeError, ValueError) as error:
        raise GridScreeningError(
            "Grid frame differs from the expected complete frame"
        ) from error


def _restore_parcel_index(
    retained: gpd.GeoDataFrame, stage: gpd.GeoDataFrame
) -> gpd.GeoDataFrame:
    if (
        len(stage) != len(retained)
        or "parcel_id" not in stage
        or stage["parcel_id"].isna().any()
        or stage["parcel_id"].duplicated().any()
    ):
        raise GridScreeningError("Grid parcel IDs are missing or duplicated")
    if (
        retained["parcel_id"].isna().any()
        or retained["parcel_id"].duplicated().any()
        or stage["parcel_id"].tolist() != retained["parcel_id"].tolist()
    ):
        raise GridScreeningError(
            "Grid parcel ID sequence differs from retained parcels"
        )
    if tuple(stage.columns) != (*retained.columns, *GRID_COLUMNS):
        raise GridScreeningError(
            "Grid parcel export schema differs from the explicit allowlist"
        )
    output = stage.copy(deep=True)
    output.index = retained.index.copy(deep=True)
    _compare_frame(output.loc[:, list(retained.columns)], retained)
    return output


def _run_grid(retained: gpd.GeoDataFrame, options: _GridOptions) -> _GridRun:
    download = download_ign_bdtopo_archive(
        options.config, cache_dir=options.cache_dir, allow_download=False
    )
    extraction = extract_ign_bdtopo_archive(
        download,
        options.config,
        extraction_dir=options.extraction_dir,
        allow_extract=False,
    )
    # The extractor owns its default path selection; False forbids rebuilding it.
    actual_path = _checked_path(extraction.extraction_path, options.cache_dir)
    if actual_path == options.cache_dir or options.cache_dir.is_relative_to(
        actual_path
    ):
        raise GridScreeningError("IGN extraction target collides with archive cache")
    marker = _identity(actual_path / ".landscout-extraction.json")
    electricity = load_ign_bdtopo_electricity(extraction, options.config)
    result = assess_grid_coverage(retained, electricity, options.config)
    integrated = _restore_parcel_index(retained, result.parcels)
    run = _GridRun(options, electricity, result, integrated, marker)
    _voltage_records(run)
    return run


def _summary_equal(actual: object, fresh: object, expected_type: type) -> None:
    if type(actual) is not expected_type or type(fresh) is not expected_type:
        raise GridScreeningError("IGN summary type differs")
    for field in fields(expected_type):
        first, second = getattr(actual, field.name), getattr(fresh, field.name)
        if type(first) is not type(second) or first != second:
            raise GridScreeningError(f"IGN summary differs: {field.name}")


def _final_grid_check(run: _GridRun) -> None:
    source = run.electricity
    extraction = source.extraction
    download = extraction.archive
    integrity = validate_ign_bdtopo_archive(download.path, run.options.config)
    for key in (
        "file_size",
        "sha256",
        "official_checksum_algorithm",
        "official_checksum",
        "official_checksum_validated",
    ):
        if type(getattr(integrity, key)) is not type(getattr(download, key)) or getattr(
            integrity, key
        ) != getattr(download, key):
            raise GridScreeningError("IGN archive changed after grid calculation")
    # Authorized clarification: public reread plus full comparison, no private alias.
    fresh = load_ign_bdtopo_electricity(extraction, run.options.config)
    if (
        type(source) is not IgnBdTopoElectricityData
        or type(fresh) is not IgnBdTopoElectricityData
        or fresh.extraction is not extraction
    ):
        raise GridScreeningError("IGN electricity bundle/extraction identity differs")
    if (
        source.spatial_role != "PROXY_GEOMETRY"
        or fresh.spatial_role != source.spatial_role
    ):
        raise GridScreeningError("IGN electricity spatial role differs")
    _compare_frame(source.electric_lines, fresh.electric_lines)
    _compare_frame(source.transformation_posts, fresh.transformation_posts)
    _summary_equal(
        source.electric_lines_summary,
        fresh.electric_lines_summary,
        IgnBdTopoLayerSummary,
    )
    _summary_equal(
        source.transformation_posts_summary,
        fresh.transformation_posts_summary,
        IgnBdTopoLayerSummary,
    )
    used = run.assessment.source_coverage
    fresh_coverage = load_ign_bdtopo_department_coverage(extraction, run.options.config)
    if used.extraction is not extraction or fresh_coverage.extraction is not extraction:
        raise GridScreeningError("IGN coverage changed extraction identity")
    _compare_frame(used.coverage, fresh_coverage.coverage)
    _summary_equal(used.summary, fresh_coverage.summary, IgnBdTopoCoverageLayerSummary)
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
            raise GridScreeningError("IGN coverage lineage differs")
    if _identity(Path(run.marker_identity["path"])) != run.marker_identity:
        raise GridScreeningError("IGN extraction marker changed after grid calculation")


def _scalar(value: object, column: str) -> str | int | float | None:
    if value is None or bool(pd.isna(value)):
        return None
    if isinstance(value, bool):
        raise GridScreeningError(f"Boolean is not a grid scalar for {column}")
    if column in INTEGER_COLUMNS:
        if not isinstance(value, Integral):
            raise GridScreeningError(f"Grid integer required: {column}")
        return int(value)
    if column in FLOAT_COLUMNS:
        if not isinstance(value, Real) or not isfinite(float(value)):
            raise GridScreeningError(f"Finite grid numeric required: {column}")
        return float(value)
    if isinstance(value, str):
        return str(value)
    if isinstance(value, Integral):
        return int(value)
    if isinstance(value, Real) and isfinite(float(value)):
        return float(value)
    raise GridScreeningError(f"Unsupported grid scalar: {column}")


def _parcel_records(run: _GridRun) -> dict[str, dict[str, str | int | float | None]]:
    return {
        row["parcel_id"]: {key: _scalar(row[key], key) for key in GRID_COLUMNS}
        for _, row in run.parcels.iterrows()
    }


def _voltage_records(run: _GridRun) -> list[dict[str, str | int | float | None]]:
    table = run.assessment.voltage_level_proximity
    if (
        tuple(table.columns) != VOLTAGE_EXPORT_COLUMNS
        or table[["parcel_id", "voltage_kv"]].isna().any().any()
        or table.duplicated(["parcel_id", "voltage_kv"]).any()
    ):
        raise GridScreeningError("Grid voltage table schema or pair uniqueness differs")
    levels = tuple(item.voltage_kv for item in run.assessment.voltage_level_coverage)
    if len(levels) != len(set(levels)) or any(
        isinstance(v, bool)
        or not isinstance(v, Real)
        or not isfinite(float(v))
        or v <= 0
        for v in levels
    ):
        raise GridScreeningError("Invalid observed exact voltage coverage")
    expected = {(p, v) for p in run.parcels["parcel_id"] for v in levels}
    if set(
        zip(table["parcel_id"], table["voltage_kv"], strict=True)
    ) != expected or len(table) != len(expected):
        raise GridScreeningError(
            "Grid voltage table does not cover the exact parcel/voltage domain"
        )
    records = [
        {key: _scalar(row[key], key) for key in VOLTAGE_EXPORT_COLUMNS}
        for _, row in table.iterrows()
    ]
    return sorted(
        records, key=lambda row: (str(row["parcel_id"]), float(row["voltage_kv"]))
    )


def _provenance(run: _GridRun) -> dict[str, object]:
    extraction = run.electricity.extraction
    archive = extraction.archive
    coverage = run.assessment.source_coverage
    return {
        "status": "COMPLETE",
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
            "marker": run.marker_identity,
            "spatial_role": extraction.spatial_role,
        },
        "geopackage": {
            "path": str(extraction.geopackage_path),
            "filename": extraction.geopackage_filename,
            "size_bytes": extraction.geopackage_size_bytes,
            "sha256": extraction.geopackage_sha256,
        },
        "layers": {
            "electric_lines": extraction.electric_lines_layer,
            "transformation_posts": extraction.transformation_posts_layer,
            "road_segments_inventory_only": extraction.road_segments_layer,
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
        "voltage_level_coverage": [
            {
                "voltage_kv": float(item.voltage_kv),
                "line_feature_count": int(item.line_feature_count),
            }
            for item in run.assessment.voltage_level_coverage
        ],
        "hash_authority": "LOCAL_BYTE_VERIFICATION; pinned official checksum only where configured",
    }

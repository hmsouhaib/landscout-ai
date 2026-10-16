"""Verified cadastre -> existing area/shape filters -> a local completion marker."""

import csv
import json
import subprocess
from collections import Counter
from dataclasses import dataclass
from datetime import UTC, datetime
from hashlib import sha256
from math import isfinite
from numbers import Real
from pathlib import Path
from uuid import uuid4

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd  # type: ignore[import-untyped]
from shapely.geometry import mapping  # type: ignore[import-untyped]

from landscout.common.strict_json import loads_strict_json_object
from landscout.common.strict_yaml import loads_strict_yaml
from landscout.config import ScanConfig, load_scan_config
from landscout.sources.cadastre_fr import DEFAULT_CACHE_DIR, download_cadastre_parcelles
from landscout.sources.cadastre_loader_fr import (
    load_cadastre_parcels,
    revalidate_cadastre_parcel_source,
)
from landscout.stages.enrich_shape import enrich_parcel_shapes
from landscout.stages.filter_parcels import (
    filter_parcels_by_area,
    filter_parcels_by_shape,
)
from landscout.stages.normalize_cadastre import normalize_cadastre_parcels
from landscout.workflows import grid_screening as grid
from landscout.workflows import ign_screening as ign
from landscout.workflows import road_screening as roads

IDENTITY_COLUMNS = (
    "parcel_id",
    "commune_code",
    "section_prefix",
    "section",
    "parcel_number",
)
METRIC_COLUMNS = (
    "area_m2",
    "length_m",
    "width_m",
    "length_width_ratio",
    "compactness",
    "centroid_lat",
    "centroid_lon",
)
EXPORT_COLUMNS = (
    *IDENTITY_COLUMNS,
    "geometry_status",
    "area_m2",
    "shape_status",
    *METRIC_COLUMNS[1:],
    "screening_status",
    "screening_stage",
    "rejection_reason",
)


class CadastreScreeningRunError(RuntimeError):
    """A controlled failure; a directory without run.json is incomplete."""


@dataclass(frozen=True)
class CadastreScreeningRunResult:
    output_dir: Path
    candidates_csv: Path
    rejections_csv: Path
    candidates_geojson: Path
    manifest_path: Path
    normalized_count: int
    area_rejected_count: int
    shape_rejected_count: int
    retained_count: int
    voltage_proximity_csv: Path | None = None
    grid_status: str | None = None
    road_proximity_csv: Path | None = None
    roads_status: str | None = None


def _fingerprint(path: Path) -> dict[str, str | int]:
    content = path.read_bytes()
    return {
        "path": str(path),
        "size_bytes": len(content),
        "sha256": sha256(content).hexdigest(),
    }


def _check_config_identity(
    identities: tuple[tuple[Path, dict[str, str | int]], ...],
) -> None:
    for path, identity in identities:
        if _fingerprint(path) != identity:
            raise CadastreScreeningRunError(f"Configuration changed during run: {path}")


def _absolute(path: Path, root: Path) -> Path:
    if not isinstance(path, Path):
        raise CadastreScreeningRunError(
            "Cache/output paths must be pathlib.Path values"
        )
    return path if path.is_absolute() else root / path


def _check_output_path(
    path: Path,
    cache: Path,
    root: Path,
    configuration_paths: tuple[Path, ...],
    additional_paths: tuple[Path, ...] = (),
) -> Path:
    # Inspect the lexical path before resolve() can hide a link or junction.
    for ancestor in (path, *path.parents):
        if ancestor.is_symlink() or ancestor.is_junction():
            raise CadastreScreeningRunError(
                f"Output path contains a link or junction: {ancestor}"
            )
    if path.exists():
        raise CadastreScreeningRunError(f"Output directory already exists: {path}")
    resolved = path.resolve()
    if (
        resolved == cache
        or resolved.is_relative_to(cache)
        or cache.is_relative_to(resolved)
    ):
        raise CadastreScreeningRunError(
            "Output directory collides with the cadastre cache"
        )
    protected = [*configuration_paths, root / ".git", *additional_paths]
    if (root / ".git").exists():
        try:
            listing = subprocess.run(
                ["git", "-C", str(root), "ls-files", "--cached", "-z"],
                capture_output=True,
                check=True,
                timeout=15,
            )
        except (OSError, subprocess.SubprocessError) as error:
            raise CadastreScreeningRunError(
                "Cannot check output against tracked paths"
            ) from error
        protected.extend(
            root / name.decode("utf-8") for name in listing.stdout.split(b"\0") if name
        )
    for target in protected:
        target = target.resolve()
        if (
            resolved == target
            or target.is_relative_to(resolved)
            or resolved.is_relative_to(target)
        ):
            raise CadastreScreeningRunError(
                f"Output directory collides with protected path: {target}"
            )
    return resolved


def _check_partition(
    normalized: gpd.GeoDataFrame,
    area_candidates: gpd.GeoDataFrame,
    area_rejected: gpd.GeoDataFrame,
    enriched: gpd.GeoDataFrame,
    retained: gpd.GeoDataFrame,
    shape_rejected: gpd.GeoDataFrame,
) -> None:
    frames = (
        normalized,
        area_candidates,
        area_rejected,
        enriched,
        retained,
        shape_rejected,
    )
    for frame in frames:
        if frame["parcel_id"].duplicated().any():
            raise CadastreScreeningRunError("Partition contains duplicate parcel IDs")
    whole, area, rejected_area, measured, kept, rejected_shape = (
        set(frame["parcel_id"]) for frame in frames
    )
    if (
        area != measured
        or area != kept | rejected_shape
        or kept & rejected_shape
        or whole != kept | rejected_shape | rejected_area
        or rejected_area & (kept | rejected_shape)
        or len(normalized) != len(area_rejected) + len(shape_rejected) + len(retained)
    ):
        raise CadastreScreeningRunError(
            "Cadastre partition lost, overlapped or added parcel IDs"
        )


def _scalar(value: object, *, numeric: bool) -> str | float | None:
    if value is None or bool(pd.isna(value)):
        return None
    if numeric:
        if (
            isinstance(value, bool)
            or not isinstance(value, Real)
            or not isfinite(float(value))
        ):
            raise CadastreScreeningRunError(
                "Export metric must be finite numeric or null"
            )
        return float(value)
    if not isinstance(value, str):
        raise CadastreScreeningRunError("Export text must be a string or null")
    return str(value)


def _records(
    frame: gpd.GeoDataFrame,
    stage: str,
    reason_column: str | None = None,
) -> list[dict[str, str | float | None]]:
    records = []
    for _, row in frame.iterrows():
        record = {
            key: _scalar(row.get(key), numeric=key in METRIC_COLUMNS)
            for key in EXPORT_COLUMNS[:-3]
        }
        record["screening_status"] = (
            "REJECTED_BY_EXECUTED_FILTERS"
            if reason_column
            else "RETAINED_BY_EXECUTED_FILTERS"
        )
        record["screening_stage"] = stage
        record["rejection_reason"] = (
            _scalar(row[reason_column], numeric=False) if reason_column else None
        )
        records.append(record)
    return sorted(records, key=lambda row: str(row["parcel_id"]))


def _write_csv(
    path: Path,
    records: list[dict[str, str | float | None]],
    columns: tuple[str, ...] = EXPORT_COLUMNS,
) -> None:
    with path.open("x", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows(records)


def _json_bytes(value: object) -> bytes:
    return (
        json.dumps(value, ensure_ascii=False, allow_nan=False, indent=2) + "\n"
    ).encode("utf-8")


def _write_geojson(
    path: Path,
    retained: gpd.GeoDataFrame,
    records: list[dict[str, str | float | None]],
) -> None:
    geometries = dict(zip(retained["parcel_id"], retained.geometry, strict=True))
    features = [
        {
            "type": "Feature",
            "id": row["parcel_id"],
            "properties": row,
            "geometry": mapping(geometries[row["parcel_id"]]),
        }
        for row in records
    ]
    with path.open("xb") as stream:
        stream.write(_json_bytes({"type": "FeatureCollection", "features": features}))


def _verify_export_ids(
    candidates: Path,
    rejections: Path,
    geojson: Path,
    normalized: gpd.GeoDataFrame,
    retained: gpd.GeoDataFrame,
) -> None:
    with candidates.open(encoding="utf-8", newline="") as stream:
        kept = [row["parcel_id"] for row in csv.DictReader(stream)]
    with rejections.open(encoding="utf-8", newline="") as stream:
        rejected = [row["parcel_id"] for row in csv.DictReader(stream)]
    features = loads_strict_json_object(geojson.read_bytes())["features"]
    geo_ids = [row["properties"]["parcel_id"] for row in features]
    if (
        kept != geo_ids
        or kept != sorted(retained["parcel_id"])
        or len(rejected) != len(set(rejected))
        or set(kept) & set(rejected)
        or len(kept) + len(rejected) != len(normalized)
        or set(kept) | set(rejected) != set(normalized["parcel_id"])
    ):
        raise CadastreScreeningRunError(
            "Written exports do not preserve the parcel partition"
        )


def _publish_manifest(path: Path, manifest: dict[str, object]) -> None:
    temporary = path.with_suffix(".json.part")
    with temporary.open("xb") as stream:
        stream.write(_json_bytes(manifest))
    if path.exists() or path.is_symlink() or path.is_junction():
        raise CadastreScreeningRunError("Manifest destination already exists")
    temporary.rename(path)


def run_cadastre_screening(
    scan_path: Path,
    *,
    cache_dir: Path | None = None,
    output_dir: Path | None = None,
    allow_download: bool = False,
    max_cache_age_hours: float = 168.0,
    with_grid: bool = False,
    ign_config_path: Path | None = None,
    ign_cache_dir: Path | None = None,
    ign_extraction_dir: Path | None = None,
    with_roads: bool = False,
    road_policy_path: Path | None = None,
) -> CadastreScreeningRunResult:
    """Run one FR/BESS commune, retaining the existing physical trust boundaries.

    Relative cache/output paths use scan_path.resolve().parents[2], just like the
    configuration loader's relative profile path. Configuration byte checks detect
    persistent changes; they do not constitute an immutable source snapshot.
    """
    reserved: Path | None = None
    started = datetime.now(UTC).isoformat()
    try:
        if not isinstance(scan_path, Path):
            raise CadastreScreeningRunError("scan_path must be a pathlib.Path")
        if type(allow_download) is not bool:
            raise CadastreScreeningRunError("allow_download must be an exact bool")
        if type(with_grid) is not bool:
            raise CadastreScreeningRunError("with_grid must be an exact bool")
        if type(with_roads) is not bool:
            raise CadastreScreeningRunError("with_roads must be an exact bool")
        if road_policy_path is not None and not with_roads:
            raise CadastreScreeningRunError("road_policy_path requires with_roads=True")
        if not (with_grid or with_roads) and any(
            p is not None for p in (ign_config_path, ign_cache_dir, ign_extraction_dir)
        ):
            raise CadastreScreeningRunError(
                "IGN options require with_grid=True or with_roads=True"
            )
        scan_path = scan_path.resolve()
        if len(scan_path.parents) < 3:
            raise CadastreScreeningRunError(
                "Expected scan under configs/scans in a project root"
            )
        root = scan_path.parents[2]
        scan_identity = _fingerprint(scan_path)
        # Bind the profile before the public loader reads it, using the same convention.
        reference = ScanConfig.model_validate(loads_strict_yaml(scan_path.read_bytes()))
        profile_path = _absolute(reference.profile.path, root).resolve()
        identities = (
            (scan_path, scan_identity),
            (profile_path, _fingerprint(profile_path)),
        )
        loaded = load_scan_config(scan_path)
        _check_config_identity(identities)
        if loaded.profile_path.resolve() != profile_path:
            raise CadastreScreeningRunError("Loaded profile identity changed")
        scan = loaded.scan_config
        if (
            scan.scan.country != "FR"
            or scan.scan.technology != "BESS"
            or len(scan.aoi.commune_codes) != 1
        ):
            raise CadastreScreeningRunError(
                "This workflow requires FR/BESS and exactly one commune"
            )
        commune = scan.aoi.commune_codes[0]
        cache_path = _absolute(
            cache_dir if cache_dir is not None else DEFAULT_CACHE_DIR, root
        )
        cache = cache_path.resolve()
        destination = (
            _absolute(output_dir, root)
            if output_dir is not None
            else (
                _absolute(scan.output.directory, root)
                / f"cadastre-{commune}-{uuid4().hex}"
            )
        )
        destination = _check_output_path(
            destination, cache, root, (scan_path, profile_path)
        )
        grid_options = None
        road_options = None
        source_paths: tuple[Path, ...] = ()
        configuration_paths = (scan_path, profile_path)
        if with_roads:
            road_options = roads._prepare_roads(root, road_policy_path)
            identities = (*identities, (road_options.path, road_options.identity))
            configuration_paths = (*configuration_paths, road_options.path)
        if with_grid or with_roads:
            grid_options = grid._prepare_grid(
                root,
                commune,
                cache_path,
                destination,
                configuration_paths,
                ign_config_path,
                ign_cache_dir,
                ign_extraction_dir,
            )
            identities = (
                *identities,
                (grid_options.config_path, grid_options.config_identity),
            )
            configuration_paths = (*configuration_paths, grid_options.config_path)
            source_paths = (
                grid_options.cache_dir,
                *(
                    (grid_options.extraction_dir,)
                    if grid_options.extraction_dir is not None
                    else ()
                ),
            )
            _check_output_path(
                destination, cache, root, configuration_paths, source_paths
            )
        _check_config_identity(identities)
        download = download_cadastre_parcelles(
            commune,
            cache_dir=cache,
            max_cache_age_hours=max_cache_age_hours,
            allow_download=allow_download,
        )
        source = load_cadastre_parcels(download)
        normalized = normalize_cadastre_parcels(source)
        area_candidates, area_rejected = filter_parcels_by_area(
            normalized, loaded.profile.parcel
        )
        enriched = enrich_parcel_shapes(area_candidates)
        retained, shape_rejected = filter_parcels_by_shape(
            enriched, loaded.profile.shape_screening
        )
        _check_partition(
            normalized,
            area_candidates,
            area_rejected,
            enriched,
            retained,
            shape_rejected,
        )
        context = (
            ign._acquire_ign(
                grid_options.config, grid_options.cache_dir, grid_options.extraction_dir
            )
            if grid_options is not None and len(retained)
            else None
        )
        grid_run = (
            grid._run_grid(retained, grid_options, context)
            if with_grid and context is not None
            else None
        )
        road_run = (
            roads._run_roads(retained, grid_options, road_options, context)
            if with_roads and context is not None
            else None
        )
        retained_records = _records(
            retained, "AREA_SHAPE" if loaded.profile.shape_screening.enabled else "AREA"
        )
        if grid_run is not None:
            grid_records = grid._parcel_records(grid_run)
            retained_records = [
                {**row, **grid_records[row["parcel_id"]]} for row in retained_records
            ]
        candidate_columns = (
            (*EXPORT_COLUMNS, *grid.GRID_COLUMNS) if with_grid else EXPORT_COLUMNS
        )
        voltage_records = (
            grid._voltage_records(grid_run) if grid_run is not None else []
        )
        road_records = roads._road_records(road_run) if road_run is not None else []
        rejected_records = sorted(
            _records(area_rejected, "AREA", "rejection_reason")
            + _records(shape_rejected, "SHAPE", "shape_rejection_reason"),
            key=lambda row: str(row["parcel_id"]),
        )
        _check_config_identity(identities)
        _check_output_path(destination, cache, root, configuration_paths, source_paths)
        destination.mkdir(parents=True, exist_ok=False)
        reserved = destination
        candidates_csv = destination / "candidates.csv"
        rejections_csv = destination / "rejections.csv"
        candidates_geojson = destination / "candidates.geojson"
        _write_csv(candidates_csv, retained_records, candidate_columns)
        _write_csv(rejections_csv, rejected_records)
        _write_geojson(candidates_geojson, retained, retained_records)
        voltage_path = destination / "voltage_proximity.csv" if with_grid else None
        if voltage_path is not None:
            _write_csv(voltage_path, voltage_records, grid.VOLTAGE_EXPORT_COLUMNS)
            with voltage_path.open(encoding="utf-8", newline="") as stream:
                written = list(csv.DictReader(stream))
            expected = [
                {key: "" if value is None else str(value) for key, value in row.items()}
                for row in voltage_records
            ]
            if written != expected:
                raise CadastreScreeningRunError(
                    "Written voltage table differs from public grid result"
                )
        road_path = destination / "road_proximity.csv" if with_roads else None
        if road_path is not None:
            roads._write_road_csv(road_path, road_records)
        _verify_export_ids(
            candidates_csv, rejections_csv, candidates_geojson, normalized, retained
        )
        revalidate_cadastre_parcel_source(source)
        if grid_run is not None:
            grid._final_grid_check(grid_run)
        if road_run is not None:
            roads._final_road_check(road_run)
        _check_config_identity(identities)
        data_files = []
        for path in (
            candidates_csv,
            rejections_csv,
            candidates_geojson,
            *((voltage_path,) if voltage_path is not None else ()),
            *((road_path,) if road_path is not None else ()),
        ):
            identity = _fingerprint(path)
            data_files.append({**identity, "path": path.name})
        manifest: dict[str, object] = {
            "schema_version": 1,
            "status": "COMPLETE",
            "scope": "CADASTRE_AREA_SHAPE_ONLY",
            "commune_code": commune,
            "started_at_utc": started,
            "completed_at_utc": datetime.now(UTC).isoformat(),
            "configuration": {"scan": identities[0][1], "profile": identities[1][1]},
            "filters": {
                "area": loaded.profile.parcel.model_dump(mode="json"),
                "shape": loaded.profile.shape_screening.model_dump(mode="json"),
            },
            "max_cache_age_hours": float(max_cache_age_hours),
            "allow_download": allow_download,
            "source": {
                "archive_path": str(download.path),
                "filename": download.filename,
                "source_url": download.source_url,
                "size_bytes": download.file_size,
                "sha256": download.sha256,
                "download_timestamp": download.download_timestamp,
                "cache_hit": download.cache_hit,
                "hash_authority": "LOCAL_BYTE_VERIFICATION",
            },
            "counts": {
                "normalized": len(normalized),
                "area_candidates": len(area_candidates),
                "area_rejected": len(area_rejected),
                "shape_rejected": len(shape_rejected),
                "retained": len(retained),
                "rejection_reasons": {
                    "AREA": dict(
                        sorted(Counter(area_rejected["rejection_reason"]).items())
                    ),
                    "SHAPE": dict(
                        sorted(
                            Counter(
                                shape_rejected.get("shape_rejection_reason", [])
                            ).items()
                        )
                    ),
                },
            },
            "data_files": data_files,
            "not_run": {
                domain: "NOT_RUN"
                for domain in (
                    "grid",
                    "roads",
                    "planning",
                    "environment",
                    "scoring",
                    "owners",
                )
            },
            "presentation_order": "parcel_id ascending; intermediate frames unchanged",
        }
        manifest_path = destination / "run.json"
        if with_grid:
            manifest["schema_version"] = 2
            manifest["scope"] = "CADASTRE_AREA_SHAPE_WITH_GRID_PROXIES"
            manifest["configuration"]["ign"] = grid_options.config_identity
            manifest["grid"] = (
                grid._provenance(grid_run)
                if grid_run is not None
                else {"status": "NOT_RUN", "reason": "NO_RETAINED_PARCELS"}
            )
            if grid_run is not None:
                del manifest["not_run"]["grid"]
        if with_roads:
            manifest["schema_version"] = 3
            manifest["road_presentation_order"] = (
                "parcel_id ascending, then loaded policy class order; public table unchanged"
            )
            manifest["scope"] = (
                "CADASTRE_AREA_SHAPE_WITH_GRID_AND_ROAD_PROXIES"
                if with_grid
                else "CADASTRE_AREA_SHAPE_WITH_ROAD_PROXIES"
            )
            manifest["configuration"]["ign"] = grid_options.config_identity
            manifest["configuration"]["road_policy"] = road_options.identity
            manifest["roads"] = (
                roads._provenance(road_run)
                if road_run is not None
                else {
                    "status": "NOT_RUN",
                    "reason": "NO_RETAINED_PARCELS",
                    "policy": roads._policy_provenance(road_options),
                }
            )
            if road_run is not None:
                del manifest["not_run"]["roads"]
        _publish_manifest(manifest_path, manifest)
        return CadastreScreeningRunResult(
            destination,
            candidates_csv,
            rejections_csv,
            candidates_geojson,
            manifest_path,
            len(normalized),
            len(area_rejected),
            len(shape_rejected),
            len(retained),
            voltage_path,
            ("COMPLETE" if grid_run is not None else "NOT_RUN") if with_grid else None,
            road_path,
            ("COMPLETE" if road_run is not None else "NOT_RUN") if with_roads else None,
        )
    except (OSError, ValueError, TypeError, RuntimeError) as error:
        detail = str(error)
        if reserved is not None:
            detail += f"; incomplete output directory preserved: {reserved}"
        raise CadastreScreeningRunError(detail) from error

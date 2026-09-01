import json
import sys
from dataclasses import asdict, dataclass, replace
from datetime import UTC, datetime
from hashlib import sha256
from math import isfinite
from numbers import Real
from pathlib import Path
from shutil import copy2, copyfileobj
from typing import Annotated, Any, Literal, cast
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlsplit

from pydantic import (
    BaseModel,
    BeforeValidator,
    ConfigDict,
    Field,
    HttpUrl,
    StringConstraints,
    ValidationError,
    field_validator,
)
from pydantic_core import PydanticCustomError

from landscout.common.safe_http import open_safe_https
from landscout.common.strict_json import StrictJsonError, loads_strict_json_object
from landscout.common.strict_yaml import loads_strict_yaml

DEFAULT_CONFIG_PATH = Path("configs/sources/rte_odre_fr.yaml")
DEFAULT_CACHE_DIR = Path("data/cache/rte_odre")
DOWNLOAD_CHUNK_SIZE = 1024 * 1024
LOGICAL_DATASET_NAMES = ("sites", "overhead_lines", "underground_lines")
COORDINATE_GEOMETRY_TYPES = frozenset(
    {
        "Point",
        "MultiPoint",
        "LineString",
        "MultiLineString",
        "Polygon",
        "MultiPolygon",
    }
)
GEOJSON_GEOMETRY_TYPES = COORDINATE_GEOMETRY_TYPES | {"GeometryCollection"}

LogicalDatasetName = Literal["sites", "overhead_lines", "underground_lines"]
ExportFormat = Literal["geojson"]
GeometryPrecisionStatus = Literal[
    "EXACT_NOT_CLAIMED",
    "GENERALIZED_OR_RESTRICTED",
    "MISSING",
    "UNKNOWN",
]

NonEmptyString = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
DatasetIdentifier = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        min_length=1,
        pattern=r"^[A-Za-z0-9][A-Za-z0-9_-]*$",
    ),
]


def _strict_nonnegative_finite_number(value: object) -> object:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise PydanticCustomError(
            "strict_number",
            "value must be a strict finite non-negative number",
        )
    try:
        numeric_value = float(value)
    except (OverflowError, TypeError, ValueError) as error:
        raise ValueError("value must be a strict finite non-negative number") from error
    if not isfinite(numeric_value) or value < 0:
        raise ValueError("value must be a strict finite non-negative number")
    return value


StrictNonNegativeFloat = Annotated[
    float,
    BeforeValidator(_strict_nonnegative_finite_number),
    Field(ge=0, allow_inf_nan=False),
]


class RteDatasetConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    dataset_id: DatasetIdentifier
    preferred_format: ExportFormat


class RteDatasetsConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    sites: RteDatasetConfig
    overhead_lines: RteDatasetConfig
    underground_lines: RteDatasetConfig


class RteOdreApiConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    base_url: HttpUrl

    @field_validator("base_url")
    @classmethod
    def _official_api_origin(cls, value: HttpUrl) -> HttpUrl:
        parsed = urlsplit(str(value))
        if (
            parsed.scheme != "https"
            or parsed.hostname != "odre.opendatasoft.com"
            or parsed.port not in {None, 443}
            or parsed.username is not None
            or parsed.password is not None
            or parsed.path.rstrip("/") != "/api/explore/v2.1"
            or parsed.query
            or parsed.fragment
        ):
            raise ValueError("RTE/ODRE API must use the exact official HTTPS origin")
        return value


class RteOdreCacheConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    max_age_hours: StrictNonNegativeFloat


class RteOdreSourceConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    provider: Literal["RTE"]
    portal: Literal["ODRE"]
    api: RteOdreApiConfig
    datasets: RteDatasetsConfig
    cache: RteOdreCacheConfig


class RteOdreDownloadError(RuntimeError):
    """Raised when RTE/ODRE metadata or exports cannot be retrieved safely."""


@dataclass(frozen=True)
class RteOdreDatasetMetadata:
    dataset_id: str
    title: str | None
    publisher: str | None
    modified: str | None
    data_processed: str | None
    metadata_processed: str | None
    license: str | None
    records_count: int | None
    geometry_precision_status: GeometryPrecisionStatus

    def __post_init__(self) -> None:
        if self.records_count is not None and (
            not isinstance(self.records_count, int)
            or isinstance(self.records_count, bool)
            or self.records_count < 0
        ):
            raise ValueError("records_count must be a non-negative integer or None")


@dataclass(frozen=True)
class RteOdreExportSummary:
    feature_count: int
    null_geometry_count: int
    non_null_geometry_count: int
    geometry_types: tuple[str, ...]

    def __post_init__(self) -> None:
        counts = {
            "feature_count": self.feature_count,
            "null_geometry_count": self.null_geometry_count,
            "non_null_geometry_count": self.non_null_geometry_count,
        }
        for name, value in counts.items():
            if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                raise ValueError(f"{name} must be a non-negative integer")
        if (
            self.null_geometry_count + self.non_null_geometry_count
            != self.feature_count
        ):
            raise ValueError("Geometry counts must add up to feature_count")
        if not isinstance(self.geometry_types, tuple) or any(
            not isinstance(value, str) or not value for value in self.geometry_types
        ):
            raise TypeError("geometry_types must be a tuple of non-empty strings")


@dataclass(frozen=True)
class RteOdreDownload:
    logical_name: LogicalDatasetName
    dataset_id: str
    provider: str
    portal: str
    source_url: str
    export_format: ExportFormat
    download_timestamp: str
    filename: str
    file_size: int
    sha256: str
    path: Path
    cache_hit: bool
    dataset_metadata: RteOdreDatasetMetadata
    export_summary: RteOdreExportSummary


def load_rte_odre_source_config(
    path: Path = DEFAULT_CONFIG_PATH,
) -> RteOdreSourceConfig:
    content = loads_strict_yaml(path.read_bytes())
    if type(content) is not dict:
        raise TypeError(f"Expected a YAML mapping in {path}")
    return RteOdreSourceConfig.model_validate(content)


def _validated_source_config(config: object) -> RteOdreSourceConfig:
    try:
        if type(config) is not RteOdreSourceConfig:
            raise TypeError("RTE/ODRE source config type is invalid")
        return RteOdreSourceConfig.model_validate(config.model_dump(mode="python"))
    except (AttributeError, TypeError, ValidationError, ValueError) as error:
        raise RteOdreDownloadError(
            "RTE/ODRE source config no longer satisfies the official origin contract"
        ) from error


def _get_dataset_config(
    config: RteOdreSourceConfig, logical_name: LogicalDatasetName
) -> RteDatasetConfig:
    if logical_name not in LOGICAL_DATASET_NAMES:
        raise ValueError(f"Unsupported RTE/ODRE logical dataset: {logical_name}")
    return getattr(config.datasets, logical_name)


def _dataset_api_url(
    config: RteOdreSourceConfig,
    logical_name: LogicalDatasetName,
    suffix: str,
) -> str:
    dataset = _get_dataset_config(config, logical_name)
    encoded_dataset_id = quote(dataset.dataset_id, safe="")
    return (
        f"{str(config.api.base_url).rstrip('/')}/catalog/datasets/"
        f"{encoded_dataset_id}{suffix}"
    )


def build_rte_odre_metadata_url(
    config: RteOdreSourceConfig, logical_name: LogicalDatasetName
) -> str:
    validated_config = _validated_source_config(config)
    return _dataset_api_url(validated_config, logical_name, "")


def build_rte_odre_export_url(
    config: RteOdreSourceConfig, logical_name: LogicalDatasetName
) -> str:
    validated_config = _validated_source_config(config)
    dataset = _get_dataset_config(validated_config, logical_name)
    export_format = quote(dataset.preferred_format, safe="")
    return _dataset_api_url(validated_config, logical_name, f"/exports/{export_format}")


def _optional_string(mapping: dict[str, Any], key: str) -> str | None:
    value = mapping.get(key)
    if not isinstance(value, str):
        return None
    normalized = value.strip()
    return normalized or None


def _metadata_precision_status(description: str | None) -> GeometryPrecisionStatus:
    if description is None:
        return "UNKNOWN"
    normalized = description.casefold()
    if "données gps" in normalized and "sécurité publique" in normalized:
        return "GENERALIZED_OR_RESTRICTED"
    return "UNKNOWN"


def _read_response_json(source_url: str, timeout: float) -> dict[str, Any]:
    try:
        with open_safe_https(
            source_url,
            timeout=timeout,
            headers={"User-Agent": "LandScout-AI/0.1"},
        ) as response:
            payload = loads_strict_json_object(response.read())
    except (HTTPError, URLError, OSError, StrictJsonError) as error:
        raise RteOdreDownloadError(f"RTE/ODRE request failed: {source_url}") from error
    return payload


def fetch_rte_odre_dataset_metadata(
    config: RteOdreSourceConfig,
    logical_name: LogicalDatasetName,
    timeout: float = 60.0,
) -> RteOdreDatasetMetadata:
    validated_config = _validated_source_config(config)
    dataset = _get_dataset_config(validated_config, logical_name)
    metadata_url = _dataset_api_url(validated_config, logical_name, "")
    payload = _read_response_json(metadata_url, timeout)
    response_dataset_id = payload.get("dataset_id")
    if response_dataset_id != dataset.dataset_id:
        raise RteOdreDownloadError(
            f"Unexpected dataset metadata response for {dataset.dataset_id}"
        )

    metas = payload.get("metas")
    default_metas = metas.get("default") if isinstance(metas, dict) else None
    if not isinstance(default_metas, dict):
        default_metas = {}
    records_count_value = default_metas.get("records_count")
    if records_count_value is None:
        records_count = None
    elif not isinstance(records_count_value, int) or isinstance(
        records_count_value, bool
    ):
        raise RteOdreDownloadError("RTE/ODRE records_count must be an integer or null")
    elif records_count_value < 0:
        raise RteOdreDownloadError("RTE/ODRE records_count must not be negative")
    else:
        records_count = records_count_value
    description = _optional_string(default_metas, "description")
    return RteOdreDatasetMetadata(
        dataset_id=dataset.dataset_id,
        title=_optional_string(default_metas, "title"),
        publisher=_optional_string(default_metas, "publisher"),
        modified=_optional_string(default_metas, "modified"),
        data_processed=_optional_string(default_metas, "data_processed"),
        metadata_processed=_optional_string(default_metas, "metadata_processed"),
        license=_optional_string(default_metas, "license"),
        records_count=records_count,
        geometry_precision_status=_metadata_precision_status(description),
    )


def _sha256(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(DOWNLOAD_CHUNK_SIZE), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _validate_geojson(path: Path) -> RteOdreExportSummary:
    if not path.is_file() or path.stat().st_size == 0:
        raise RteOdreDownloadError(f"GeoJSON export is missing or empty: {path}")
    try:
        payload = loads_strict_json_object(path.read_bytes())
    except (OSError, StrictJsonError) as error:
        raise RteOdreDownloadError(
            f"GeoJSON export is not valid finite UTF-8 JSON: {path}"
        ) from error
    if payload.get("type") != "FeatureCollection":
        raise RteOdreDownloadError("GeoJSON export must be a FeatureCollection")
    features = payload.get("features")
    if not isinstance(features, list):
        raise RteOdreDownloadError(
            "GeoJSON FeatureCollection must contain a features list"
        )

    null_geometry_count = 0
    geometry_types: set[str] = set()
    for feature in features:
        if not isinstance(feature, dict) or feature.get("type") != "Feature":
            raise RteOdreDownloadError(
                "Every GeoJSON feature must be an object with type Feature"
            )
        geometry = feature.get("geometry")
        if geometry is None:
            null_geometry_count += 1
            continue
        if not isinstance(geometry, dict):
            raise RteOdreDownloadError(
                "GeoJSON feature geometry must be an object or null"
            )
        geometry_type = _validate_geojson_geometry(geometry)
        geometry_types.add(geometry_type)
    return RteOdreExportSummary(
        feature_count=len(features),
        null_geometry_count=null_geometry_count,
        non_null_geometry_count=len(features) - null_geometry_count,
        geometry_types=tuple(sorted(geometry_types)),
    )


def _validate_position(value: object, geometry_type: str) -> None:
    if not isinstance(value, list) or len(value) < 2:
        raise RteOdreDownloadError(
            f"GeoJSON {geometry_type} coordinates must contain an X/Y position"
        )
    if any(
        isinstance(coordinate, bool)
        or not isinstance(coordinate, Real)
        or not isfinite(float(coordinate))
        for coordinate in value
    ):
        raise RteOdreDownloadError(
            f"GeoJSON {geometry_type} coordinates must be finite numeric values"
        )


def _validate_nested_coordinates(
    value: object,
    *,
    depth: int,
    geometry_type: str,
) -> None:
    if not isinstance(value, list):
        raise RteOdreDownloadError(
            f"GeoJSON {geometry_type} coordinate structure must use JSON arrays"
        )
    if depth == 0:
        _validate_position(value, geometry_type)
        return
    for member in value:
        _validate_nested_coordinates(
            member,
            depth=depth - 1,
            geometry_type=geometry_type,
        )


def _validate_geojson_geometry(geometry: object) -> str:
    if not isinstance(geometry, dict):
        raise RteOdreDownloadError("GeoJSON geometry member must be an object")
    geometry_type = geometry.get("type")
    if geometry_type not in GEOJSON_GEOMETRY_TYPES:
        raise RteOdreDownloadError("GeoJSON feature has an unsupported geometry type")
    if geometry_type == "GeometryCollection":
        members = geometry.get("geometries")
        if not isinstance(members, list):
            raise RteOdreDownloadError(
                "GeoJSON GeometryCollection must contain a geometries list"
            )
        for member in members:
            _validate_geojson_geometry(member)
        return geometry_type

    if "coordinates" not in geometry:
        raise RteOdreDownloadError(
            f"GeoJSON {geometry_type} geometry must contain coordinates"
        )
    depth_by_type = {
        "Point": 0,
        "MultiPoint": 1,
        "LineString": 1,
        "MultiLineString": 2,
        "Polygon": 2,
        "MultiPolygon": 3,
    }
    _validate_nested_coordinates(
        geometry["coordinates"],
        depth=depth_by_type[geometry_type],
        geometry_type=geometry_type,
    )
    return geometry_type


def _metadata_from_dict(payload: Any) -> RteOdreDatasetMetadata:
    if type(payload) is not dict:
        raise TypeError("Missing cached dataset metadata")
    expected_keys = {
        "dataset_id",
        "title",
        "publisher",
        "modified",
        "data_processed",
        "metadata_processed",
        "license",
        "records_count",
        "geometry_precision_status",
    }
    if set(payload) != expected_keys:
        raise ValueError("Cached dataset metadata schema differs")
    dataset_id = payload["dataset_id"]
    if type(dataset_id) is not str or not dataset_id:
        raise TypeError("Invalid cached dataset ID")
    precision_status = payload["geometry_precision_status"]
    allowed_statuses = {
        "EXACT_NOT_CLAIMED",
        "GENERALIZED_OR_RESTRICTED",
        "MISSING",
        "UNKNOWN",
    }
    if type(precision_status) is not str or precision_status not in allowed_statuses:
        raise ValueError("Invalid cached geometry precision status")
    records_count = payload["records_count"]
    if records_count is not None and (type(records_count) is not int):
        raise TypeError("Invalid cached records count")
    optional_values: dict[str, str | None] = {}
    for field_name in (
        "title",
        "publisher",
        "modified",
        "data_processed",
        "metadata_processed",
        "license",
    ):
        value = payload[field_name]
        if value is not None and type(value) is not str:
            raise TypeError(f"Invalid cached metadata value: {field_name}")
        optional_values[field_name] = value
    return RteOdreDatasetMetadata(
        dataset_id=dataset_id,
        title=optional_values["title"],
        publisher=optional_values["publisher"],
        modified=optional_values["modified"],
        data_processed=optional_values["data_processed"],
        metadata_processed=optional_values["metadata_processed"],
        license=optional_values["license"],
        records_count=records_count,
        geometry_precision_status=cast(GeometryPrecisionStatus, precision_status),
    )


def _export_summary_from_dict(payload: Any) -> RteOdreExportSummary:
    if type(payload) is not dict:
        raise TypeError("Missing cached export summary")
    expected_keys = {
        "feature_count",
        "null_geometry_count",
        "non_null_geometry_count",
        "geometry_types",
    }
    if set(payload) != expected_keys:
        raise ValueError("Cached export summary schema differs")
    geometry_types = payload["geometry_types"]
    if type(geometry_types) is not list or any(
        type(value) is not str for value in geometry_types
    ):
        raise TypeError("Invalid cached geometry types")
    return RteOdreExportSummary(
        feature_count=payload["feature_count"],
        null_geometry_count=payload["null_geometry_count"],
        non_null_geometry_count=payload["non_null_geometry_count"],
        geometry_types=tuple(geometry_types),
    )


def _validate_records_count(
    dataset_metadata: RteOdreDatasetMetadata,
    export_summary: RteOdreExportSummary,
) -> None:
    records_count = dataset_metadata.records_count
    if records_count is not None and records_count != export_summary.feature_count:
        raise RteOdreDownloadError(
            "RTE/ODRE metadata records_count does not match export feature_count: "
            f"{records_count} != {export_summary.feature_count}"
        )


def _replace_file(source: Path, target: Path) -> None:
    source.replace(target)


def _is_link_or_junction(path: Path) -> bool:
    try:
        return path.is_symlink() or path.is_junction()
    except OSError:
        return True


def _cache_recovery_paths(
    archive_path: Path,
    metadata_path: Path,
) -> tuple[Path, Path]:
    return (
        archive_path.with_suffix(f"{archive_path.suffix}.bak"),
        metadata_path.with_suffix(f"{metadata_path.suffix}.bak"),
    )


def _require_no_cache_recovery_material(
    archive_path: Path,
    metadata_path: Path,
) -> None:
    if any(
        path.exists() or _is_link_or_junction(path)
        for path in _cache_recovery_paths(archive_path, metadata_path)
    ):
        raise RteOdreDownloadError(
            "RTE/ODRE cache recovery backup already exists; manual recovery is required"
        )


def _prepare_temporary_cache_file(path: Path) -> None:
    try:
        if _is_link_or_junction(path):
            raise RteOdreDownloadError(
                "RTE/ODRE cache temporary path is a link or junction"
            )
        if path.exists():
            if not path.is_file():
                raise RteOdreDownloadError(
                    "RTE/ODRE cache temporary path is not a regular file"
                )
            path.unlink()
    except RteOdreDownloadError:
        raise
    except OSError as error:
        raise RteOdreDownloadError(
            "RTE/ODRE cache temporary path cannot be prepared safely"
        ) from error


def _cleanup_temporary_cache_files(
    paths: tuple[Path, ...],
    primary_error: BaseException | None,
) -> None:
    cleanup_error: OSError | None = None
    for path in paths:
        try:
            path.unlink(missing_ok=True)
        except OSError as error:
            cleanup_error = cleanup_error or error
    if cleanup_error is not None and primary_error is None:
        raise RteOdreDownloadError(
            "RTE/ODRE cache temporary files could not be cleaned safely"
        ) from cleanup_error


def _publish_cache_pair(
    temporary_archive: Path,
    temporary_metadata: Path,
    archive_path: Path,
    metadata_path: Path,
) -> None:
    archive_backup, metadata_backup = _cache_recovery_paths(
        archive_path,
        metadata_path,
    )
    archive_existed = archive_path.is_file()
    metadata_existed = metadata_path.is_file()

    _require_no_cache_recovery_material(archive_path, metadata_path)
    try:
        if archive_existed:
            copy2(archive_path, archive_backup)
        if metadata_existed:
            copy2(metadata_path, metadata_backup)
    except OSError:
        archive_backup.unlink(missing_ok=True)
        metadata_backup.unlink(missing_ok=True)
        raise

    archive_published = False
    try:
        _replace_file(temporary_archive, archive_path)
        archive_published = True
        _replace_file(temporary_metadata, metadata_path)
    except OSError:
        try:
            if archive_published:
                if archive_existed:
                    _replace_file(archive_backup, archive_path)
                else:
                    archive_path.unlink(missing_ok=True)
        except OSError as rollback_error:
            raise RteOdreDownloadError(
                "RTE/ODRE cache publication and rollback both failed"
            ) from rollback_error
        archive_backup.unlink(missing_ok=True)
        metadata_backup.unlink(missing_ok=True)
        raise
    else:
        archive_backup.unlink(missing_ok=True)
        metadata_backup.unlink(missing_ok=True)


def _load_cached_download(
    archive_path: Path,
    metadata_path: Path,
    config: RteOdreSourceConfig,
    logical_name: LogicalDatasetName,
    source_url: str,
) -> RteOdreDownload | None:
    if not archive_path.is_file() or not metadata_path.is_file():
        return None
    dataset = _get_dataset_config(config, logical_name)
    try:
        metadata = loads_strict_json_object(metadata_path.read_bytes())
        expected_keys = {
            "logical_name",
            "dataset_id",
            "provider",
            "portal",
            "source_url",
            "export_format",
            "download_timestamp",
            "filename",
            "file_size",
            "sha256",
            "dataset_metadata",
            "export_summary",
        }
        if set(metadata) != expected_keys:
            return None
        string_fields = (
            "logical_name",
            "dataset_id",
            "provider",
            "portal",
            "source_url",
            "export_format",
            "download_timestamp",
            "filename",
            "sha256",
        )
        if any(type(metadata[field]) is not str for field in string_fields):
            return None
        if type(metadata["file_size"]) is not int:
            return None
        fresh_summary = _validate_geojson(archive_path)
        file_size = archive_path.stat().st_size
        checksum = _sha256(archive_path)
        download_timestamp = metadata["download_timestamp"]
        assert isinstance(download_timestamp, str)
        downloaded_at = datetime.fromisoformat(download_timestamp)
        if downloaded_at.tzinfo is None:
            return None
        age_seconds = (
            datetime.now(UTC) - downloaded_at.astimezone(UTC)
        ).total_seconds()
        valid = (
            0 <= age_seconds <= config.cache.max_age_hours * 3600
            and metadata["logical_name"] == logical_name
            and metadata["dataset_id"] == dataset.dataset_id
            and metadata["provider"] == config.provider
            and metadata["portal"] == config.portal
            and metadata["source_url"] == source_url
            and metadata["export_format"] == dataset.preferred_format
            and metadata["filename"] == archive_path.name
            and metadata["file_size"] == file_size
            and metadata["sha256"] == checksum
        )
        if not valid:
            return None
        dataset_metadata = _metadata_from_dict(metadata["dataset_metadata"])
        cached_summary = _export_summary_from_dict(metadata["export_summary"])
        if dataset_metadata.dataset_id != dataset.dataset_id:
            return None
        if fresh_summary != cached_summary:
            return None
        _validate_records_count(dataset_metadata, cached_summary)
        return RteOdreDownload(
            logical_name=logical_name,
            dataset_id=dataset.dataset_id,
            provider=config.provider,
            portal=config.portal,
            source_url=source_url,
            export_format=dataset.preferred_format,
            download_timestamp=download_timestamp,
            filename=archive_path.name,
            file_size=file_size,
            sha256=checksum,
            path=archive_path,
            cache_hit=True,
            dataset_metadata=dataset_metadata,
            export_summary=cached_summary,
        )
    except (
        KeyError,
        OSError,
        TypeError,
        ValueError,
        RteOdreDownloadError,
    ):
        return None


def download_rte_odre_dataset(
    logical_name: LogicalDatasetName,
    config: RteOdreSourceConfig,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    timeout: float = 60.0,
) -> RteOdreDownload:
    validated_config = _validated_source_config(config)
    dataset = _get_dataset_config(validated_config, logical_name)
    export_format = quote(dataset.preferred_format, safe="")
    source_url = _dataset_api_url(
        validated_config, logical_name, f"/exports/{export_format}"
    )
    filename = f"{dataset.dataset_id}.{dataset.preferred_format}"
    archive_path = cache_dir / filename
    metadata_path = cache_dir / f"{filename}.metadata.json"
    _require_no_cache_recovery_material(archive_path, metadata_path)
    cached = _load_cached_download(
        archive_path,
        metadata_path,
        validated_config,
        logical_name,
        source_url,
    )
    if cached is not None:
        return cached

    temporary_archive = archive_path.with_suffix(f"{archive_path.suffix}.part")
    temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
    try:
        cache_dir.mkdir(parents=True, exist_ok=True)
        _prepare_temporary_cache_file(temporary_archive)
        _prepare_temporary_cache_file(temporary_metadata)
    except RteOdreDownloadError:
        raise
    except OSError as error:
        raise RteOdreDownloadError(
            "RTE/ODRE cache paths cannot be prepared safely"
        ) from error
    try:
        dataset_metadata = fetch_rte_odre_dataset_metadata(
            validated_config, logical_name, timeout=timeout
        )
        with (
            open_safe_https(
                source_url,
                timeout=timeout,
                headers={"User-Agent": "LandScout-AI/0.1"},
            ) as response,
            temporary_archive.open("xb") as output,
        ):
            copyfileobj(response, output, length=DOWNLOAD_CHUNK_SIZE)
        summary = _validate_geojson(temporary_archive)
        _validate_records_count(dataset_metadata, summary)
        if summary.feature_count > 0 and summary.non_null_geometry_count == 0:
            dataset_metadata = replace(
                dataset_metadata, geometry_precision_status="MISSING"
            )

        result = RteOdreDownload(
            logical_name=logical_name,
            dataset_id=dataset.dataset_id,
            provider=validated_config.provider,
            portal=validated_config.portal,
            source_url=source_url,
            export_format=dataset.preferred_format,
            download_timestamp=datetime.now(UTC).isoformat(),
            filename=filename,
            file_size=temporary_archive.stat().st_size,
            sha256=_sha256(temporary_archive),
            path=archive_path,
            cache_hit=False,
            dataset_metadata=dataset_metadata,
            export_summary=summary,
        )
        lineage = asdict(result)
        lineage.pop("path")
        lineage.pop("cache_hit")
        with temporary_metadata.open("x", encoding="utf-8") as output:
            output.write(json.dumps(lineage, indent=2, sort_keys=True) + "\n")
        _publish_cache_pair(
            temporary_archive, temporary_metadata, archive_path, metadata_path
        )
        return result
    except RteOdreDownloadError:
        raise
    except (HTTPError, URLError, OSError) as error:
        raise RteOdreDownloadError(f"RTE/ODRE download failed: {source_url}") from error
    finally:
        _cleanup_temporary_cache_files(
            (temporary_archive, temporary_metadata),
            sys.exception(),
        )

"""Source-bound metadata-only catalog of verified INPN EP GeoPackages."""

from __future__ import annotations

import json
import math
import re
import unicodedata
import warnings
from collections.abc import Iterator, Mapping
from contextlib import contextmanager
from dataclasses import dataclass
from hashlib import sha256
from numbers import Real
from pathlib import Path, PurePosixPath, PureWindowsPath
from typing import SupportsFloat, cast

import pyogrio  # type: ignore[import-untyped]
from pyproj import CRS

from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    validate_inpn_protected_areas_extraction,
)

CATALOG_HASH_SCHEMA_VERSION = 2
_SHA_PATTERN = re.compile(r"[0-9a-f]{64}")
_PYOGRIO_BYTES_GPKG_WARNING = (
    r"^File /vsimem/pyogrio_[0-9a-f]+ has GPKG application_id, "
    r"but non conformant file extension$"
)


@contextmanager
def _suppress_pyogrio_bytes_gpkg_warning() -> Iterator[None]:
    """Suppress only Pyogrio's expected byte-backed GPKG extension warning."""

    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore",
            message=_PYOGRIO_BYTES_GPKG_WARNING,
            category=RuntimeWarning,
        )
        yield


class InpnProtectedAreasCatalogError(ValueError):
    """Raised when exact EP GeoPackage metadata cannot be proven safely."""


@dataclass(frozen=True)
class InpnProtectedAreasFieldCatalog:
    """One source-ordered physical attribute-field metadata record."""

    name: str
    source_dtype: str
    position: int


@dataclass(frozen=True)
class InpnProtectedAreasLayerCatalog:
    """One source-ordered OGR layer metadata record without feature rows."""

    layer_name: str
    layer_position: int
    feature_count: int
    geometry_type_raw: str | None
    is_spatial: bool
    crs_raw: str | None
    crs_authority_name: str | None
    crs_authority_code: str | None
    crs_wkt: str | None
    total_bounds: tuple[float, float, float, float] | None
    fields: tuple[InpnProtectedAreasFieldCatalog, ...]


@dataclass(frozen=True)
class InpnProtectedAreasGeoPackageCatalog:
    """One extraction-ordered verified GeoPackage and all of its OGR layers."""

    relative_path: str
    file_size: int
    file_sha256: str
    package_position: int
    driver_name: str
    layers: tuple[InpnProtectedAreasLayerCatalog, ...]


@dataclass(frozen=True)
class InpnProtectedAreasCatalog:
    """Portable factual metadata catalog bound to one verified INPN EP snapshot."""

    catalog_schema_version: int
    provider: str
    authority: str
    program: str
    dataset_id: str
    dataset_name: str
    declared_version: str
    reference_page_url: str
    archive_url: str
    archive_filename: str
    archive_size: int
    archive_sha256: str
    packages: tuple[InpnProtectedAreasGeoPackageCatalog, ...]
    package_count: int
    layer_count: int
    field_count: int
    total_feature_count: int
    complete_catalog_content_sha256: str


def _exact_text(value: object, label: str) -> str:
    if type(value) is not str or not value or value != value.strip():
        raise InpnProtectedAreasCatalogError(f"{label} must be an exact string")
    return value


def _identity_key(value: str) -> str:
    return unicodedata.normalize("NFKC", value).casefold()


def _require_unique_identities(values: tuple[str, ...], label: str) -> None:
    if len(set(values)) != len(values):
        raise InpnProtectedAreasCatalogError(f"{label} contains duplicate exact names")
    normalized = tuple(_identity_key(value) for value in values)
    if len(set(normalized)) != len(normalized):
        raise InpnProtectedAreasCatalogError(
            f"{label} contains Unicode-NFKC/casefold collisions"
        )


def _is_link_or_junction(path: Path) -> bool:
    try:
        return path.is_symlink() or path.is_junction()
    except OSError:
        return True


def _safe_package_path(
    extraction: InpnProtectedAreasExtraction,
    item: InpnProtectedAreasExtractedFile,
) -> Path:
    relative = PurePosixPath(item.relative_path)
    windows = PureWindowsPath(item.relative_path)
    if (
        relative.is_absolute()
        or windows.is_absolute()
        or bool(windows.drive)
        or ".." in relative.parts
        or relative.as_posix() != item.relative_path
    ):
        raise InpnProtectedAreasCatalogError(
            f"package {item.relative_path}: relative path is not canonical"
        )
    root = extraction.extraction_path
    if _is_link_or_junction(root) or not root.is_dir():
        raise InpnProtectedAreasCatalogError("extraction root is missing or unsafe")
    path = root.joinpath(*relative.parts)
    root_resolved = root.resolve(strict=True)
    path_resolved = path.resolve(strict=True)
    if path_resolved == root_resolved or not path_resolved.is_relative_to(
        root_resolved
    ):
        raise InpnProtectedAreasCatalogError(
            f"package {item.relative_path}: path escapes the extraction root"
        )
    current = root
    for component in relative.parts:
        current = current / component
        if _is_link_or_junction(current):
            raise InpnProtectedAreasCatalogError(
                f"package {item.relative_path}: links or junctions are forbidden"
            )
    if not path.is_file():
        raise InpnProtectedAreasCatalogError(
            f"package {item.relative_path}: source is not a regular file"
        )
    return path


def _read_verified_package_bytes(
    extraction: InpnProtectedAreasExtraction,
    item: InpnProtectedAreasExtractedFile,
) -> bytes:
    path = _safe_package_path(extraction, item)
    try:
        package_bytes = path.read_bytes()
    except OSError as error:
        raise InpnProtectedAreasCatalogError(
            f"package {item.relative_path}: cannot read physical byte snapshot"
        ) from error
    if (
        type(package_bytes) is not bytes
        or len(package_bytes) != item.file_size
        or sha256(package_bytes).hexdigest() != item.sha256
    ):
        raise InpnProtectedAreasCatalogError(
            f"package {item.relative_path}: physical byte identity changed"
        )
    return package_bytes


def _metadata_sequence(value: object, label: str) -> tuple[object, ...]:
    if isinstance(value, (str, bytes, bytearray, Mapping)):
        raise InpnProtectedAreasCatalogError(f"{label} metadata array is malformed")
    try:
        converted = value.tolist() if hasattr(value, "tolist") else value
        if type(converted) not in (list, tuple):
            raise TypeError
        return tuple(cast(list[object] | tuple[object, ...], converted))
    except (AttributeError, TypeError, ValueError) as error:
        raise InpnProtectedAreasCatalogError(
            f"{label} metadata array is malformed"
        ) from error


def _layer_enumeration(
    value: object, relative_path: str
) -> tuple[tuple[str, str | None], ...]:
    rows = _metadata_sequence(value, f"package {relative_path} layer enumeration")
    if not rows:
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path}: no OGR-visible layer"
        )
    result: list[tuple[str, str | None]] = []
    for position, raw_row in enumerate(rows):
        row = _metadata_sequence(
            raw_row,
            f"package {relative_path} layer {position}",
        )
        if len(row) != 2:
            raise InpnProtectedAreasCatalogError(
                f"package {relative_path}: layer enumeration row is malformed"
            )
        name = _exact_text(
            row[0],
            f"package {relative_path} layer name at position {position}",
        )
        raw_geometry = row[1]
        if raw_geometry is not None:
            raw_geometry = _exact_text(
                raw_geometry,
                f"package {relative_path} layer {name} geometry type",
            )
        result.append((name, raw_geometry))
    _require_unique_identities(
        tuple(name for name, _ in result),
        f"package {relative_path} layer identities",
    )
    return tuple(result)


def _metadata_mapping(
    value: object, relative_path: str, layer_name: str
) -> Mapping[object, object]:
    if not isinstance(value, Mapping):
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: metadata is not a mapping"
        )
    return value


def _required_metadata(
    metadata: Mapping[object, object],
    key: str,
    relative_path: str,
    layer_name: str,
) -> object:
    if key not in metadata:
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: missing {key} metadata"
        )
    return metadata[key]


def _field_catalogs(
    metadata: Mapping[object, object],
    relative_path: str,
    layer_name: str,
) -> tuple[InpnProtectedAreasFieldCatalog, ...]:
    names = _metadata_sequence(
        _required_metadata(metadata, "fields", relative_path, layer_name),
        f"package {relative_path} layer {layer_name} fields",
    )
    dtypes = _metadata_sequence(
        _required_metadata(metadata, "dtypes", relative_path, layer_name),
        f"package {relative_path} layer {layer_name} dtypes",
    )
    if len(names) != len(dtypes):
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: field/dtype lengths differ"
        )
    fields: list[InpnProtectedAreasFieldCatalog] = []
    for position, (raw_name, raw_dtype) in enumerate(zip(names, dtypes, strict=True)):
        name = _exact_text(
            raw_name,
            f"package {relative_path} layer {layer_name} field name at position {position}",
        )
        source_dtype = _exact_text(
            raw_dtype,
            f"package {relative_path} layer {layer_name} dtype for field {name}",
        )
        fields.append(
            InpnProtectedAreasFieldCatalog(
                name=name,
                source_dtype=source_dtype,
                position=position,
            )
        )
    _require_unique_identities(
        tuple(field.name for field in fields),
        f"package {relative_path} layer {layer_name} field identities",
    )
    return tuple(fields)


def _feature_count(value: object, relative_path: str, layer_name: str) -> int:
    if type(value) is not int or value < 0:
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: feature count must be "
            "an exact non-negative integer"
        )
    return value


def _missing_bound(value: object) -> bool:
    return value is None or (
        isinstance(value, Real)
        and not isinstance(value, bool)
        and math.isnan(float(value))
    )


def _bounds_sequence(
    value: object,
    relative_path: str,
    layer_name: str,
) -> tuple[object, object, object, object]:
    values = _metadata_sequence(
        value,
        f"package {relative_path} layer {layer_name} bounds",
    )
    if len(values) != 4:
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: bounds must have four values"
        )
    return values[0], values[1], values[2], values[3]


def _validated_bounds(
    value: object,
    *,
    is_spatial: bool,
    feature_count: int,
    relative_path: str,
    layer_name: str,
) -> tuple[float, float, float, float] | None:
    if not is_spatial:
        if value is not None:
            raise InpnProtectedAreasCatalogError(
                f"package {relative_path} layer {layer_name}: non-spatial bounds must be null"
            )
        return None
    if value is None:
        if feature_count == 0:
            return None
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: populated spatial bounds are missing"
        )
    values = _bounds_sequence(value, relative_path, layer_name)
    missing = tuple(_missing_bound(member) for member in values)
    if any(missing):
        if feature_count == 0 and all(missing):
            return None
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: bounds are partially missing"
        )
    if feature_count == 0:
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: empty spatial bounds must be null"
        )
    if any(
        isinstance(member, bool) or not isinstance(member, Real) for member in values
    ):
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: bounds must be numeric"
        )
    bounds = tuple(float(cast(SupportsFloat, member)) for member in values)
    if not all(math.isfinite(member) for member in bounds):
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: bounds must be finite"
        )
    min_x, min_y, max_x, max_y = bounds
    if min_x > max_x or min_y > max_y:
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: bounds are reversed"
        )
    return min_x, min_y, max_x, max_y


def _canonical_crs(
    value: object,
    relative_path: str,
    layer_name: str,
) -> tuple[str, str | None, str | None, str]:
    raw = _exact_text(
        value,
        f"package {relative_path} layer {layer_name} CRS",
    )
    try:
        crs = CRS.from_user_input(raw)
        wkt = crs.to_wkt(version="WKT2_2019", pretty=False)
        authority = crs.to_authority()
    except Exception as error:
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: CRS is not parseable"
        ) from error
    if type(wkt) is not str or not wkt:
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: canonical CRS WKT is missing"
        )
    if authority is None:
        return raw, None, None, wkt
    if (
        type(authority) is not tuple
        or len(authority) != 2
        or any(type(member) is not str or not member for member in authority)
    ):
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: CRS authority is malformed"
        )
    return raw, authority[0], authority[1], wkt


def _inspect_layer(
    package_bytes: bytes,
    relative_path: str,
    layer_name: str,
    layer_position: int,
    listed_geometry_type: str | None,
) -> tuple[InpnProtectedAreasLayerCatalog, str]:
    try:
        with _suppress_pyogrio_bytes_gpkg_warning():
            raw_metadata = pyogrio.read_info(
                package_bytes,
                layer=layer_name,
                force_feature_count=True,
                force_total_bounds=True,
            )
        metadata = _metadata_mapping(raw_metadata, relative_path, layer_name)
        driver_name = _exact_text(
            _required_metadata(metadata, "driver", relative_path, layer_name),
            f"package {relative_path} layer {layer_name} driver",
        )
        if driver_name != "GPKG":
            raise InpnProtectedAreasCatalogError(
                f"package {relative_path} layer {layer_name}: driver must be exact GPKG"
            )
        reported_name = _exact_text(
            _required_metadata(metadata, "layer_name", relative_path, layer_name),
            f"package {relative_path} layer {layer_name} reported name",
        )
        if reported_name != layer_name:
            raise InpnProtectedAreasCatalogError(
                f"package {relative_path} layer {layer_name}: reported layer name differs"
            )
        raw_geometry = _required_metadata(
            metadata,
            "geometry_type",
            relative_path,
            layer_name,
        )
        geometry_type = (
            None
            if raw_geometry is None
            else _exact_text(
                raw_geometry,
                f"package {relative_path} layer {layer_name} geometry type",
            )
        )
        if geometry_type != listed_geometry_type:
            raise InpnProtectedAreasCatalogError(
                f"package {relative_path} layer {layer_name}: layer enumeration and "
                "metadata geometry types differ"
            )
        is_spatial = geometry_type is not None
        count = _feature_count(
            _required_metadata(metadata, "features", relative_path, layer_name),
            relative_path,
            layer_name,
        )
        raw_crs = _required_metadata(metadata, "crs", relative_path, layer_name)
        crs_raw: str | None
        authority_name: str | None
        authority_code: str | None
        crs_wkt: str | None
        if is_spatial:
            crs_raw, authority_name, authority_code, crs_wkt = _canonical_crs(
                raw_crs,
                relative_path,
                layer_name,
            )
        else:
            if raw_crs is not None:
                raise InpnProtectedAreasCatalogError(
                    f"package {relative_path} layer {layer_name}: non-spatial CRS must be null"
                )
            crs_raw = authority_name = authority_code = crs_wkt = None
        bounds = _validated_bounds(
            _required_metadata(metadata, "total_bounds", relative_path, layer_name),
            is_spatial=is_spatial,
            feature_count=count,
            relative_path=relative_path,
            layer_name=layer_name,
        )
        return (
            InpnProtectedAreasLayerCatalog(
                layer_name=layer_name,
                layer_position=layer_position,
                feature_count=count,
                geometry_type_raw=geometry_type,
                is_spatial=is_spatial,
                crs_raw=crs_raw,
                crs_authority_name=authority_name,
                crs_authority_code=authority_code,
                crs_wkt=crs_wkt,
                total_bounds=bounds,
                fields=_field_catalogs(metadata, relative_path, layer_name),
            ),
            driver_name,
        )
    except InpnProtectedAreasCatalogError:
        raise
    except Exception as error:
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: metadata inspection failed"
        ) from error


def _inspect_package(
    extraction: InpnProtectedAreasExtraction,
    item: InpnProtectedAreasExtractedFile,
    package_position: int,
) -> InpnProtectedAreasGeoPackageCatalog:
    if PurePosixPath(item.relative_path).suffix.casefold() != ".gpkg":
        raise InpnProtectedAreasCatalogError(
            f"extracted file {item.relative_path} is not a GeoPackage and cannot be ignored"
        )
    try:
        package_bytes = _read_verified_package_bytes(extraction, item)
        try:
            with _suppress_pyogrio_bytes_gpkg_warning():
                raw_layers = pyogrio.list_layers(package_bytes)
            enumeration = _layer_enumeration(raw_layers, item.relative_path)
        except InpnProtectedAreasCatalogError:
            raise
        except Exception as error:
            raise InpnProtectedAreasCatalogError(
                f"package {item.relative_path}: OGR layer enumeration failed"
            ) from error
        inspected = tuple(
            _inspect_layer(
                package_bytes,
                item.relative_path,
                layer_name,
                layer_position,
                geometry_type,
            )
            for layer_position, (layer_name, geometry_type) in enumerate(enumeration)
        )
        layers = tuple(layer for layer, _ in inspected)
        drivers = tuple(driver for _, driver in inspected)
        if len(set(drivers)) != 1 or drivers[0] != "GPKG":
            raise InpnProtectedAreasCatalogError(
                f"package {item.relative_path}: layer driver metadata is inconsistent"
            )
        return InpnProtectedAreasGeoPackageCatalog(
            relative_path=item.relative_path,
            file_size=item.file_size,
            file_sha256=item.sha256,
            package_position=package_position,
            driver_name=drivers[0],
            layers=layers,
        )
    except InpnProtectedAreasCatalogError:
        raise
    except Exception as error:
        raise InpnProtectedAreasCatalogError(
            f"package {item.relative_path}: physical inspection failed"
        ) from error


def _field_payload(field: InpnProtectedAreasFieldCatalog) -> dict[str, object]:
    return {
        "name": field.name,
        "source_dtype": field.source_dtype,
        "position": field.position,
    }


def _layer_payload(layer: InpnProtectedAreasLayerCatalog) -> dict[str, object]:
    return {
        "layer_name": layer.layer_name,
        "layer_position": layer.layer_position,
        "feature_count": layer.feature_count,
        "geometry_type_raw": layer.geometry_type_raw,
        "is_spatial": layer.is_spatial,
        "crs_raw": layer.crs_raw,
        "crs_authority_name": layer.crs_authority_name,
        "crs_authority_code": layer.crs_authority_code,
        "crs_wkt": layer.crs_wkt,
        "total_bounds": layer.total_bounds,
        "fields": [_field_payload(field) for field in layer.fields],
    }


def _package_payload(package: InpnProtectedAreasGeoPackageCatalog) -> dict[str, object]:
    return {
        "relative_path": package.relative_path,
        "file_size": package.file_size,
        "file_sha256": package.file_sha256,
        "package_position": package.package_position,
        "driver_name": package.driver_name,
        "layers": [_layer_payload(layer) for layer in package.layers],
    }


def _catalog_payload(catalog: InpnProtectedAreasCatalog) -> dict[str, object]:
    return {
        "catalog_schema_version": catalog.catalog_schema_version,
        "provider": catalog.provider,
        "authority": catalog.authority,
        "program": catalog.program,
        "dataset_id": catalog.dataset_id,
        "dataset_name": catalog.dataset_name,
        "declared_version": catalog.declared_version,
        "reference_page_url": catalog.reference_page_url,
        "archive_url": catalog.archive_url,
        "archive_filename": catalog.archive_filename,
        "archive_size": catalog.archive_size,
        "archive_sha256": catalog.archive_sha256,
        "packages": [_package_payload(package) for package in catalog.packages],
        "package_count": catalog.package_count,
        "layer_count": catalog.layer_count,
        "field_count": catalog.field_count,
        "total_feature_count": catalog.total_feature_count,
    }


def _catalog_content_sha256(catalog: InpnProtectedAreasCatalog) -> str:
    try:
        encoded = json.dumps(
            _catalog_payload(catalog),
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
            allow_nan=False,
        ).encode("utf-8")
    except (TypeError, ValueError) as error:
        raise InpnProtectedAreasCatalogError(
            "catalog content is not canonical JSON"
        ) from error
    return sha256(encoded).hexdigest()


def _build_catalog(
    extraction: InpnProtectedAreasExtraction,
) -> InpnProtectedAreasCatalog:
    packages = tuple(
        _inspect_package(extraction, item, position)
        for position, item in enumerate(extraction.files)
    )
    download = extraction.download
    catalog = InpnProtectedAreasCatalog(
        catalog_schema_version=CATALOG_HASH_SCHEMA_VERSION,
        provider=download.provider,
        authority=download.authority,
        program=download.program,
        dataset_id=download.dataset_id,
        dataset_name=download.dataset_name,
        declared_version=download.declared_version,
        reference_page_url=download.reference_page_url,
        archive_url=download.archive_url,
        archive_filename=download.filename,
        archive_size=download.file_size,
        archive_sha256=download.sha256,
        packages=packages,
        package_count=len(packages),
        layer_count=sum(len(package.layers) for package in packages),
        field_count=sum(
            len(layer.fields) for package in packages for layer in package.layers
        ),
        total_feature_count=sum(
            layer.feature_count for package in packages for layer in package.layers
        ),
        complete_catalog_content_sha256="",
    )
    return InpnProtectedAreasCatalog(
        **{
            **catalog.__dict__,
            "complete_catalog_content_sha256": _catalog_content_sha256(catalog),
        }
    )


def _validate_catalog_intrinsic(catalog: object) -> InpnProtectedAreasCatalog:
    if type(catalog) is not InpnProtectedAreasCatalog:
        raise InpnProtectedAreasCatalogError(
            "catalog must be an exact InpnProtectedAreasCatalog"
        )
    if (
        type(catalog.catalog_schema_version) is not int
        or catalog.catalog_schema_version != CATALOG_HASH_SCHEMA_VERSION
    ):
        raise InpnProtectedAreasCatalogError("catalog schema version is invalid")
    for name in (
        "provider",
        "authority",
        "program",
        "dataset_id",
        "dataset_name",
        "declared_version",
        "reference_page_url",
        "archive_url",
        "archive_filename",
    ):
        _exact_text(getattr(catalog, name), f"catalog {name}")
    if type(catalog.archive_size) is not int or catalog.archive_size <= 0:
        raise InpnProtectedAreasCatalogError("catalog archive size is invalid")
    if (
        type(catalog.archive_sha256) is not str
        or _SHA_PATTERN.fullmatch(catalog.archive_sha256) is None
    ):
        raise InpnProtectedAreasCatalogError("catalog archive SHA256 is invalid")
    if type(catalog.packages) is not tuple or not catalog.packages:
        raise InpnProtectedAreasCatalogError(
            "catalog packages must be a non-empty tuple"
        )

    package_names: list[str] = []
    layer_count = 0
    field_count = 0
    feature_count = 0
    for package_position, package in enumerate(catalog.packages):
        if type(package) is not InpnProtectedAreasGeoPackageCatalog:
            raise InpnProtectedAreasCatalogError("catalog package type is invalid")
        relative_path = _exact_text(package.relative_path, "catalog package path")
        pure = PurePosixPath(relative_path)
        if (
            pure.as_posix() != relative_path
            or pure.is_absolute()
            or ".." in pure.parts
            or pure.suffix.casefold() != ".gpkg"
        ):
            raise InpnProtectedAreasCatalogError("catalog package path is invalid")
        package_names.append(relative_path)
        if type(package.package_position) is not int or (
            package.package_position != package_position
        ):
            raise InpnProtectedAreasCatalogError("catalog package order is invalid")
        if type(package.file_size) is not int or package.file_size <= 0:
            raise InpnProtectedAreasCatalogError("catalog package size is invalid")
        if (
            type(package.file_sha256) is not str
            or _SHA_PATTERN.fullmatch(package.file_sha256) is None
        ):
            raise InpnProtectedAreasCatalogError("catalog package SHA256 is invalid")
        driver_name = _exact_text(package.driver_name, "catalog package driver")
        if driver_name != "GPKG":
            raise InpnProtectedAreasCatalogError(
                "catalog package driver must be exact GPKG"
            )
        if type(package.layers) is not tuple or not package.layers:
            raise InpnProtectedAreasCatalogError("catalog package layers are invalid")
        layer_names: list[str] = []
        for layer_position, layer in enumerate(package.layers):
            if type(layer) is not InpnProtectedAreasLayerCatalog:
                raise InpnProtectedAreasCatalogError("catalog layer type is invalid")
            layer_name = _exact_text(layer.layer_name, "catalog layer name")
            layer_names.append(layer_name)
            if type(layer.layer_position) is not int or (
                layer.layer_position != layer_position
            ):
                raise InpnProtectedAreasCatalogError("catalog layer order is invalid")
            count = _feature_count(layer.feature_count, relative_path, layer_name)
            if type(layer.is_spatial) is not bool:
                raise InpnProtectedAreasCatalogError("catalog spatial flag is invalid")
            if layer.is_spatial:
                geometry_type = _exact_text(
                    layer.geometry_type_raw,
                    f"catalog layer {layer_name} geometry type",
                )
                if not geometry_type:
                    raise InpnProtectedAreasCatalogError(
                        "catalog spatial geometry type is invalid"
                    )
                _exact_text(layer.crs_raw, f"catalog layer {layer_name} CRS")
                if layer.crs_authority_name is not None:
                    _exact_text(
                        layer.crs_authority_name,
                        f"catalog layer {layer_name} CRS authority name",
                    )
                if layer.crs_authority_code is not None:
                    _exact_text(
                        layer.crs_authority_code,
                        f"catalog layer {layer_name} CRS authority code",
                    )
                _exact_text(layer.crs_wkt, f"catalog layer {layer_name} CRS WKT")
                expected_crs = _canonical_crs(
                    layer.crs_raw,
                    relative_path,
                    layer_name,
                )
                if expected_crs != (
                    layer.crs_raw,
                    layer.crs_authority_name,
                    layer.crs_authority_code,
                    layer.crs_wkt,
                ):
                    raise InpnProtectedAreasCatalogError(
                        "catalog CRS metadata is not canonical"
                    )
            elif any(
                value is not None
                for value in (
                    layer.geometry_type_raw,
                    layer.crs_raw,
                    layer.crs_authority_name,
                    layer.crs_authority_code,
                    layer.crs_wkt,
                )
            ):
                raise InpnProtectedAreasCatalogError(
                    "catalog non-spatial metadata is inconsistent"
                )
            if layer.total_bounds is not None and (
                type(layer.total_bounds) is not tuple
                or len(layer.total_bounds) != 4
                or any(type(member) is not float for member in layer.total_bounds)
            ):
                raise InpnProtectedAreasCatalogError(
                    "catalog bounds representation is not canonical"
                )
            bounds = _validated_bounds(
                layer.total_bounds,
                is_spatial=layer.is_spatial,
                feature_count=count,
                relative_path=relative_path,
                layer_name=layer_name,
            )
            if bounds != layer.total_bounds or (
                bounds is not None
                and any(type(member) is not float for member in bounds)
            ):
                raise InpnProtectedAreasCatalogError(
                    "catalog bounds representation is not canonical"
                )
            if type(layer.fields) is not tuple:
                raise InpnProtectedAreasCatalogError("catalog fields must be a tuple")
            field_names: list[str] = []
            for position, field in enumerate(layer.fields):
                if type(field) is not InpnProtectedAreasFieldCatalog:
                    raise InpnProtectedAreasCatalogError(
                        "catalog field type is invalid"
                    )
                field_names.append(_exact_text(field.name, "catalog field name"))
                _exact_text(field.source_dtype, "catalog source dtype")
                if type(field.position) is not int or field.position != position:
                    raise InpnProtectedAreasCatalogError(
                        "catalog field order is invalid"
                    )
            _require_unique_identities(tuple(field_names), "catalog field identities")
            field_count += len(layer.fields)
            feature_count += count
        _require_unique_identities(tuple(layer_names), "catalog layer identities")
        layer_count += len(package.layers)
    _require_unique_identities(tuple(package_names), "catalog package identities")
    if tuple(package_names) != tuple(sorted(package_names)):
        raise InpnProtectedAreasCatalogError("catalog package paths are not ordered")
    expected_counts = (
        len(catalog.packages),
        layer_count,
        field_count,
        feature_count,
    )
    actual_counts = (
        catalog.package_count,
        catalog.layer_count,
        catalog.field_count,
        catalog.total_feature_count,
    )
    if any(type(value) is not int or value < 0 for value in actual_counts) or (
        actual_counts != expected_counts
    ):
        raise InpnProtectedAreasCatalogError("catalog aggregate counts are invalid")
    if (
        type(catalog.complete_catalog_content_sha256) is not str
        or _SHA_PATTERN.fullmatch(catalog.complete_catalog_content_sha256) is None
        or _catalog_content_sha256(catalog) != catalog.complete_catalog_content_sha256
    ):
        raise InpnProtectedAreasCatalogError("catalog content SHA256 is invalid")
    return catalog


def _validate_source_locks(
    catalog: InpnProtectedAreasCatalog,
    extraction: InpnProtectedAreasExtraction,
) -> None:
    download = extraction.download
    expected = (
        download.provider,
        download.authority,
        download.program,
        download.dataset_id,
        download.dataset_name,
        download.declared_version,
        download.reference_page_url,
        download.archive_url,
        download.filename,
        download.file_size,
        download.sha256,
    )
    actual = (
        catalog.provider,
        catalog.authority,
        catalog.program,
        catalog.dataset_id,
        catalog.dataset_name,
        catalog.declared_version,
        catalog.reference_page_url,
        catalog.archive_url,
        catalog.archive_filename,
        catalog.archive_size,
        catalog.archive_sha256,
    )
    if actual != expected:
        raise InpnProtectedAreasCatalogError(
            "catalog source/archive lineage differs from the verified extraction"
        )


def build_inpn_protected_areas_catalog(
    extraction: InpnProtectedAreasExtraction,
    config: InpnProtectedAreasSourceConfig,
) -> InpnProtectedAreasCatalog:
    """Build a portable metadata-only catalog from one verified EP extraction."""

    try:
        fresh_before = validate_inpn_protected_areas_extraction(extraction, config)
        catalog = _build_catalog(fresh_before)
        fresh_after = validate_inpn_protected_areas_extraction(fresh_before, config)
        if fresh_after != fresh_before:
            raise InpnProtectedAreasCatalogError(
                "extraction physical inventory changed during metadata inspection"
            )
        return _validate_catalog_intrinsic(catalog)
    except InpnProtectedAreasCatalogError:
        raise
    except InpnProtectedAreasSourceError as error:
        raise InpnProtectedAreasCatalogError(
            "INPN extraction byte identity changed or failed source-complete "
            "catalog validation"
        ) from error
    except Exception as error:
        raise InpnProtectedAreasCatalogError(
            "INPN protected-areas metadata catalog cannot be built safely"
        ) from error


def validate_inpn_protected_areas_catalog(
    extraction: InpnProtectedAreasExtraction,
    config: InpnProtectedAreasSourceConfig,
    catalog: InpnProtectedAreasCatalog,
) -> None:
    """Independently rebuild and exact-compare one supplied physical catalog."""

    try:
        validated = _validate_catalog_intrinsic(catalog)
        fresh_extraction = validate_inpn_protected_areas_extraction(
            extraction,
            config,
        )
        _validate_source_locks(validated, fresh_extraction)
        rebuilt = build_inpn_protected_areas_catalog(fresh_extraction, config)
        if validated != rebuilt:
            raise InpnProtectedAreasCatalogError(
                "catalog differs from the independently rebuilt physical metadata"
            )
    except InpnProtectedAreasCatalogError:
        raise
    except InpnProtectedAreasSourceError as error:
        raise InpnProtectedAreasCatalogError(
            "INPN extraction failed catalog source-lock validation"
        ) from error
    except Exception as error:
        raise InpnProtectedAreasCatalogError(
            "INPN protected-areas catalog validation failed safely"
        ) from error


__all__ = [
    "InpnProtectedAreasCatalog",
    "InpnProtectedAreasCatalogError",
    "InpnProtectedAreasFieldCatalog",
    "InpnProtectedAreasGeoPackageCatalog",
    "InpnProtectedAreasLayerCatalog",
    "build_inpn_protected_areas_catalog",
    "validate_inpn_protected_areas_catalog",
]

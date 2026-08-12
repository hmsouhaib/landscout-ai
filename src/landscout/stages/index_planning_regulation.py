"""Build a factual, integrity-sealed text index for a GPU regulation PDF."""

from __future__ import annotations

import json
from collections.abc import Sequence
from dataclasses import dataclass, replace
from hashlib import sha256
from importlib.metadata import version
from numbers import Integral
from pathlib import Path, PurePosixPath
from re import escape, finditer, fullmatch, sub
from typing import Literal

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd  # type: ignore[import-untyped]
from pypdf import PdfReader
from pyproj import CRS

from landscout.common import planning_text
from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuPlanningDocument,
    GpuWrittenFile,
)

__all__ = [
    "PlanningRegulationIndex",
    "PlanningRegulationIndexError",
    "PlanningRegulationSearchResult",
    "index_planning_regulation",
    "search_planning_regulation",
    "validate_planning_regulation_index",
    "validate_planning_regulation_search_result",
]

SEARCH_NORMALIZATION_PROFILE = planning_text.SEARCH_NORMALIZATION_PROFILE
_normalize_search_text = planning_text.normalize_planning_search_text
_normalize_search_text_with_mapping = (
    planning_text.normalize_planning_search_text_with_mapping
)
_raw_context = planning_text.raw_context_from_spans

PAGE_HASH_SCHEMA_VERSION = 1
INDEX_HASH_SCHEMA_VERSION = 1
SEARCH_HASH_SCHEMA_VERSION = 1

PAGE_COLUMNS = (
    "page_number",
    "extraction_status",
    "raw_text",
    "normalized_search_text",
    "character_count",
    "extraction_error",
    "page_content_sha256",
)
SEARCH_HIT_COLUMNS = (
    "document_id",
    "archive_sha256",
    "pdf_sha256",
    "search_normalization_profile",
    "search_term",
    "normalized_search_term",
    "page_number",
    "occurrence_count",
    "raw_context",
    "normalized_context",
)

ExtractionStatus = Literal["TEXT", "EMPTY", "ERROR"]


class PlanningRegulationIndexError(ValueError):
    """Raised when regulation indexing or search integrity cannot be proven."""


@dataclass(frozen=True)
class PlanningRegulationIndex:
    """Immutable lineage envelope around a deterministic page text table."""

    document_id: str
    archive_sha256: str
    regulation_filename: str
    source_selection_method: str
    source_selection_sha256: str
    pdf_relative_path: str
    pdf_size_bytes: int
    pdf_sha256: str
    extraction_library: str
    extraction_library_version: str
    search_normalization_profile: str
    page_hash_schema_version: int
    index_hash_schema_version: int
    total_page_count: int
    pages_content_sha256: str
    index_content_sha256: str
    pages: pd.DataFrame


@dataclass(frozen=True)
class PlanningRegulationSearchResult:
    """Immutable lineage envelope around deterministic factual search hits."""

    document_id: str
    archive_sha256: str
    pdf_sha256: str
    search_normalization_profile: str
    search_hash_schema_version: int
    index_content_sha256: str
    requested_terms: tuple[str, ...]
    context_characters: int
    hit_count: int
    hits_content_sha256: str
    hits: pd.DataFrame


@dataclass(frozen=True)
class _ZoningSourceFileIntegrity:
    relative_path: str
    size_bytes: int
    sha256: str


@dataclass(frozen=True)
class _ZoningSourceEvidence:
    source_layer: str
    driver: str
    files: tuple[_ZoningSourceFileIntegrity, ...]


def _strict_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise PlanningRegulationIndexError(
            f"{label} must be a non-empty exact string"
        )
    return value


def _strict_nonnegative_integer(value: object, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, Integral):
        raise PlanningRegulationIndexError(f"{label} must be an integer")
    if value < 0:
        raise PlanningRegulationIndexError(f"{label} must be non-negative")
    return int(value)


def _strict_positive_integer(value: object, label: str) -> int:
    result = _strict_nonnegative_integer(value, label)
    if result == 0:
        raise PlanningRegulationIndexError(f"{label} must be positive")
    return result


def _supported_schema_version(value: object, supported: int, label: str) -> int:
    result = _strict_positive_integer(value, label)
    if result != supported:
        raise PlanningRegulationIndexError(
            f"Unsupported {label}: {result}; expected {supported}"
        )
    return result


def _validated_sha256(value: object, label: str) -> str:
    checksum = _strict_string(value, label)
    if fullmatch(r"[0-9a-f]{64}", checksum) is None:
        raise PlanningRegulationIndexError(
            f"{label} must contain exactly 64 lowercase hexadecimal characters"
        )
    return checksum


def _canonical_sha256(value: object) -> str:
    try:
        payload = json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except Exception as error:
        raise PlanningRegulationIndexError(
            "Canonical integrity payload cannot be serialized"
        ) from error
    return sha256(payload).hexdigest()


def _is_link_or_junction(path: Path) -> bool:
    try:
        return path.is_symlink() or path.is_junction()
    except OSError as error:
        raise PlanningRegulationIndexError(
            f"Cannot inspect GPU extraction path safely: {path}"
        ) from error


def _validated_relative_path(value: object) -> PurePosixPath:
    raw = _strict_string(value, "GPU inventory relative path")
    if "\\" in raw or "\x00" in raw:
        raise PlanningRegulationIndexError("GPU inventory path is unsafe")
    parts = raw.split("/")
    if any(part in {"", ".", ".."} for part in parts):
        raise PlanningRegulationIndexError("GPU inventory path is unsafe")
    relative = PurePosixPath(raw)
    if relative.is_absolute() or relative.as_posix() != raw:
        raise PlanningRegulationIndexError("GPU inventory path is unsafe")
    return relative


def _validated_pdf_basename(value: object) -> str:
    name = _strict_string(value, "regulation PDF filename")
    if (
        name in {".", ".."}
        or "/" in name
        or "\\" in name
        or Path(name).name != name
        or not name.casefold().endswith(".pdf")
        or any(ord(character) < 32 or ord(character) == 127 for character in name)
    ):
        raise PlanningRegulationIndexError(
            "regulation PDF filename must be one safe PDF basename"
        )
    return name


def _file_sha256(path: Path) -> str:
    digest = sha256()
    try:
        with path.open("rb") as stream:
            while chunk := stream.read(1024 * 1024):
                digest.update(chunk)
    except OSError as error:
        raise PlanningRegulationIndexError(
            "Regulation PDF checksum cannot be calculated"
        ) from error
    return digest.hexdigest()


def _validated_extraction_root(extraction: GpuExtraction) -> tuple[Path, Path]:
    root = extraction.extraction_root
    if not isinstance(root, Path) or _is_link_or_junction(root) or not root.is_dir():
        raise PlanningRegulationIndexError(
            "GPU extraction root must be a regular directory"
        )
    try:
        return root, root.resolve(strict=True)
    except OSError as error:
        raise PlanningRegulationIndexError(
            "GPU extraction root cannot be resolved safely"
        ) from error


def _inventory_by_relative_path(
    extraction: GpuExtraction,
) -> dict[str, GpuExtractedFile]:
    if type(extraction.files) is not tuple:
        raise PlanningRegulationIndexError(
            "GPU extraction inventory must be an immutable tuple"
        )
    inventory: dict[str, GpuExtractedFile] = {}
    for item in extraction.files:
        if not isinstance(item, GpuExtractedFile):
            raise PlanningRegulationIndexError("GPU extraction inventory is invalid")
        relative = _validated_relative_path(item.relative_path).as_posix()
        if relative in inventory:
            raise PlanningRegulationIndexError(
                "GPU extraction inventory contains duplicate paths"
            )
        inventory[relative] = item
    return inventory


def _contained_zoning_file(root: Path, root_resolved: Path, relative: str) -> Path:
    relative_path = _validated_relative_path(relative)
    path = root.joinpath(*relative_path.parts)
    current = root
    for part in relative_path.parts:
        current /= part
        if _is_link_or_junction(current):
            raise PlanningRegulationIndexError(
                "GPU zoning source path contains a symbolic link or junction"
            )
    try:
        resolved = path.resolve(strict=True)
        resolved.relative_to(root_resolved)
    except (OSError, ValueError) as error:
        raise PlanningRegulationIndexError(
            "GPU zoning source path escapes the verified extraction root"
        ) from error
    if not path.is_file():
        raise PlanningRegulationIndexError(
            "GPU zoning source must be an extracted regular file"
        )
    return path


def _zoning_dataset_relative_path(
    planning_document: GpuPlanningDocument,
    root_resolved: Path,
) -> str:
    dataset_path = planning_document.zoning.reference.dataset_path
    if not isinstance(dataset_path, Path) or _is_link_or_junction(dataset_path):
        raise PlanningRegulationIndexError("GPU zoning source path is invalid")
    try:
        relative = dataset_path.resolve(strict=True).relative_to(root_resolved)
    except (OSError, ValueError) as error:
        raise PlanningRegulationIndexError(
            "GPU zoning source path escapes the verified extraction root"
        ) from error
    return _validated_relative_path(relative.as_posix()).as_posix()


def _zoning_source_family(
    planning_document: GpuPlanningDocument,
    root: Path,
    root_resolved: Path,
    inventory: dict[str, GpuExtractedFile],
) -> tuple[tuple[Path, GpuExtractedFile], ...]:
    reference = planning_document.zoning.reference
    driver = _strict_string(reference.driver, "GPU zoning source driver")
    dataset_relative = _zoning_dataset_relative_path(
        planning_document, root_resolved
    )
    dataset_pure = PurePosixPath(dataset_relative)
    if driver == "GPKG":
        if dataset_pure.suffix.casefold() != ".gpkg":
            raise PlanningRegulationIndexError(
                "GPU zoning GeoPackage source has an inconsistent extension"
            )
        expected_paths = {dataset_relative}
    elif driver == "ESRI Shapefile":
        if dataset_pure.suffix.casefold() != ".shp":
            raise PlanningRegulationIndexError(
                "GPU zoning Shapefile source has an inconsistent extension"
            )
        if reference.source_layer != dataset_pure.stem:
            raise PlanningRegulationIndexError(
                "GPU zoning Shapefile layer name differs from its source basename"
            )
        family_prefix = f"{dataset_pure.stem}.".casefold()
        family_suffixes = {
            ".shp",
            ".shx",
            ".dbf",
            ".prj",
            ".cpg",
            ".qix",
            ".qmd",
            ".sbn",
            ".sbx",
        }
        expected_paths = {
            relative
            for relative in inventory
            if PurePosixPath(relative).parent == dataset_pure.parent
            and PurePosixPath(relative).name.casefold().startswith(family_prefix)
            and PurePosixPath(relative).suffix.casefold() in family_suffixes
        }
        required_suffixes = {".shp", ".shx", ".dbf"}
        if not required_suffixes.issubset(
            {
                PurePosixPath(relative).suffix.casefold()
                for relative in expected_paths
            }
        ):
            raise PlanningRegulationIndexError(
                "GPU zoning Shapefile inventory is missing a required family member"
            )
        parent = root.joinpath(*dataset_pure.parent.parts)
        try:
            actual_paths = {
                candidate.resolve(strict=True).relative_to(root_resolved).as_posix()
                for candidate in parent.iterdir()
                if candidate.name.casefold().startswith(family_prefix)
                and candidate.suffix.casefold() in family_suffixes
            }
        except (OSError, ValueError) as error:
            raise PlanningRegulationIndexError(
                "GPU zoning Shapefile family cannot be inventoried safely"
            ) from error
        if actual_paths != expected_paths:
            raise PlanningRegulationIndexError(
                "GPU zoning Shapefile family differs from the extraction inventory"
            )
    else:
        raise PlanningRegulationIndexError(
            "GPU zoning source driver must be GPKG or ESRI Shapefile"
        )

    if not expected_paths:
        raise PlanningRegulationIndexError(
            "GPU zoning source is absent from the extraction inventory"
        )
    family: list[tuple[Path, GpuExtractedFile]] = []
    for relative in sorted(expected_paths):
        item = inventory.get(relative)
        if item is None:
            raise PlanningRegulationIndexError(
                "GPU zoning source is absent from the extraction inventory"
            )
        expected_size = _strict_positive_integer(
            item.size_bytes, "GPU zoning source inventory size"
        )
        expected_sha = _validated_sha256(
            item.sha256, "GPU zoning source inventory SHA256"
        )
        path = _contained_zoning_file(root, root_resolved, relative)
        try:
            actual_size = path.stat().st_size
        except OSError as error:
            raise PlanningRegulationIndexError(
                "GPU zoning source size cannot be read"
            ) from error
        if actual_size != expected_size:
            raise PlanningRegulationIndexError(
                "GPU zoning source size differs from the extraction inventory"
            )
        if _file_sha256(path) != expected_sha:
            raise PlanningRegulationIndexError(
                "GPU zoning source SHA256 differs from the extraction inventory"
            )
        family.append((path, item))
    return tuple(family)


def _same_crs(left: object, right: object) -> bool:
    if left is None or right is None:
        return left is None and right is None
    try:
        return bool(CRS.from_user_input(left).equals(CRS.from_user_input(right)))
    except Exception as error:
        raise PlanningRegulationIndexError(
            "GPU zoning CRS cannot be validated"
        ) from error


def _compare_loaded_zoning(
    loaded: gpd.GeoDataFrame,
    reread: gpd.GeoDataFrame,
) -> None:
    try:
        if not isinstance(loaded, gpd.GeoDataFrame) or not isinstance(
            reread, gpd.GeoDataFrame
        ):
            raise PlanningRegulationIndexError(
                "GPU zoning source must be a GeoDataFrame"
            )
        if len(loaded) != len(reread):
            raise PlanningRegulationIndexError(
                "Loaded GPU zoning row count differs from its source"
            )
        if tuple(loaded.columns) != tuple(reread.columns):
            raise PlanningRegulationIndexError(
                "Loaded GPU zoning columns differ from its source"
            )
        if loaded.geometry.name != reread.geometry.name:
            raise PlanningRegulationIndexError(
                "Loaded GPU zoning active geometry differs from its source"
            )
        if not _same_crs(loaded.crs, reread.crs):
            raise PlanningRegulationIndexError(
                "Loaded GPU zoning CRS differs from its source"
            )
        geometry_column = reread.geometry.name
        attributes = [column for column in reread.columns if column != geometry_column]
        if not loaded[attributes].reset_index(drop=True).equals(
            reread[attributes].reset_index(drop=True)
        ):
            raise PlanningRegulationIndexError(
                "Loaded GPU zoning attributes or row order differ from its source"
            )
        if loaded.geometry.to_wkb().tolist() != reread.geometry.to_wkb().tolist():
            raise PlanningRegulationIndexError(
                "Loaded GPU zoning geometry or row order differs from its source"
            )
        if "NOMFIC" not in reread.columns:
            raise PlanningRegulationIndexError("GPU zoning is missing NOMFIC")
    except PlanningRegulationIndexError:
        raise
    except Exception as error:
        raise PlanningRegulationIndexError(
            "Loaded GPU zoning cannot be compared safely with its source"
        ) from error


def _revalidate_zoning_source(
    planning_document: GpuPlanningDocument,
) -> tuple[gpd.GeoDataFrame, _ZoningSourceEvidence]:
    """Re-read immutable zoning bytes before trusting source PDF references."""

    try:
        extraction = planning_document.extraction
        reference = planning_document.zoning.reference
        source_layer = _strict_string(
            reference.source_layer, "GPU zoning source layer"
        )
        root, root_resolved = _validated_extraction_root(extraction)
        family = _zoning_source_family(
            planning_document,
            root,
            root_resolved,
            _inventory_by_relative_path(extraction),
        )
        driver = _strict_string(reference.driver, "GPU zoning source driver")
        if driver == "GPKG":
            reread = gpd.read_file(
                reference.dataset_path, layer=source_layer, engine="pyogrio"
            )
        elif driver == "ESRI Shapefile":
            reread = gpd.read_file(reference.dataset_path, engine="pyogrio")
        else:  # already rejected by _zoning_source_family
            raise PlanningRegulationIndexError(
                "GPU zoning source driver must be GPKG or ESRI Shapefile"
            )
        _compare_loaded_zoning(planning_document.zoning.data, reread)
        return reread, _ZoningSourceEvidence(
            source_layer=source_layer,
            driver=driver,
            files=tuple(
                _ZoningSourceFileIntegrity(
                    relative_path=item.relative_path,
                    size_bytes=item.size_bytes,
                    sha256=item.sha256,
                )
                for _, item in family
            ),
        )
    except PlanningRegulationIndexError:
        raise
    except Exception as error:
        raise PlanningRegulationIndexError(
            "GPU zoning source cannot be revalidated"
        ) from error


def _validate_document_lineage(planning_document: GpuPlanningDocument) -> tuple[str, str]:
    if not isinstance(planning_document, GpuPlanningDocument):
        raise PlanningRegulationIndexError(
            "planning_document must be a GpuPlanningDocument"
        )
    extraction = planning_document.extraction
    if not isinstance(extraction, GpuExtraction):
        raise PlanningRegulationIndexError("GPU extraction lineage is invalid")
    archive = extraction.archive
    if not isinstance(archive, GpuArchiveDownload) or not isinstance(
        archive.document, GpuDocumentMetadata
    ):
        raise PlanningRegulationIndexError("GPU archive lineage is invalid")
    metadata = archive.document
    document_id = _strict_string(metadata.document_id, "GPU document ID")
    archive_sha = _validated_sha256(archive.sha256, "GPU archive SHA256")
    if not isinstance(archive.archive_format, str) or (
        archive.archive_format.casefold() != "zip"
    ):
        raise PlanningRegulationIndexError("GPU archive format must be zip")
    if (
        metadata.document_family != "DU"
        or metadata.status != "document.production"
        or metadata.legal_status != "APPROVED"
        or metadata.effective_status != "EN_VIGUEUR"
    ):
        raise PlanningRegulationIndexError(
            "GPU planning document is not the current effective DU"
        )
    if type(planning_document.related_layers) is not tuple or type(
        planning_document.all_spatial_layers
    ) is not tuple:
        raise PlanningRegulationIndexError("GPU spatial-layer lineage is invalid")
    if planning_document.zoning.logical_name != "zoning":
        raise PlanningRegulationIndexError("GPU zoning logical layer is invalid")
    if planning_document.zoning.reference not in planning_document.all_spatial_layers:
        raise PlanningRegulationIndexError(
            "GPU zoning reference is absent from discovered spatial layers"
        )
    for layer in (planning_document.zoning, *planning_document.related_layers):
        if (
            layer.summary.source_document_id != document_id
            or layer.summary.source_archive_sha256 != archive_sha
            or layer.summary.source_layer != layer.reference.source_layer
            or layer.summary.feature_count != len(layer.data)
        ):
            raise PlanningRegulationIndexError(
                "GPU spatial-layer lineage is inconsistent with the archive"
            )
    return document_id, archive_sha


def _zoning_regulation_filenames(zoning: gpd.GeoDataFrame) -> tuple[str, ...]:
    if "NOMFIC" not in zoning.columns:
        raise PlanningRegulationIndexError("GPU zoning is missing NOMFIC")
    values: set[str] = set()
    try:
        source_values = zoning["NOMFIC"].tolist()
        for value in source_values:
            if value is None or value is pd.NA or (
                isinstance(value, float) and pd.isna(value)
            ):
                continue
            values.add(_validated_pdf_basename(value))
    except PlanningRegulationIndexError:
        raise
    except Exception as error:
        raise PlanningRegulationIndexError(
            "GPU zoning NOMFIC values cannot be validated"
        ) from error
    if not values:
        raise PlanningRegulationIndexError(
            "GPU zoning NOMFIC contains no regulation filename"
        )
    return tuple(sorted(values, key=str.casefold))


def _written_file_matches(
    planning_document: GpuPlanningDocument, filename: str
) -> tuple[GpuWrittenFile, ...]:
    matches: list[GpuWrittenFile] = []
    written_files = planning_document.extraction.archive.document.written_files
    if type(written_files) is not tuple:
        raise PlanningRegulationIndexError(
            "GPU written-files metadata must be an immutable tuple"
        )
    for item in written_files:
        if not isinstance(item, GpuWrittenFile):
            raise PlanningRegulationIndexError("GPU written-files metadata is invalid")
        written_filename = _strict_string(item.filename, "GPU written filename")
        if written_filename == filename:
            matches.append(item)
    if not matches:
        raise PlanningRegulationIndexError(
            f"Regulation PDF is absent from official written_files: {filename}"
        )
    if len(matches) != 1:
        raise PlanningRegulationIndexError(
            f"Regulation PDF is duplicated in official written_files: {filename}"
        )
    return tuple(matches)


def _resolve_regulation_filename(
    planning_document: GpuPlanningDocument,
    regulation_filename: str | None,
) -> tuple[str, str, _ZoningSourceEvidence, GpuWrittenFile]:
    reread_zoning, zoning_evidence = _revalidate_zoning_source(planning_document)
    referenced = _zoning_regulation_filenames(reread_zoning)
    if regulation_filename is None:
        if len(referenced) != 1:
            raise PlanningRegulationIndexError(
                "GPU zoning NOMFIC regulation selection is ambiguous"
            )
        selected = referenced[0]
        method = "ZONING_NOMFIC"
    else:
        selected = _validated_pdf_basename(regulation_filename)
        if selected not in referenced:
            raise PlanningRegulationIndexError(
                "Explicit regulation filename is not referenced by zoning NOMFIC"
            )
        method = "EXPLICIT_ZONING_NOMFIC"
    written_file = _written_file_matches(planning_document, selected)[0]
    return selected, method, zoning_evidence, written_file


def _locate_regulation_pdf(
    planning_document: GpuPlanningDocument,
    pdf_basename: str,
) -> tuple[Path, GpuExtractedFile]:
    extraction = planning_document.extraction
    root = extraction.extraction_root
    if not isinstance(root, Path) or _is_link_or_junction(root) or not root.is_dir():
        raise PlanningRegulationIndexError(
            "GPU extraction root must be a regular directory"
        )
    inventory_paths: set[str] = set()
    matches: list[tuple[PurePosixPath, GpuExtractedFile]] = []
    for item in extraction.files:
        if not isinstance(item, GpuExtractedFile):
            raise PlanningRegulationIndexError("GPU extraction inventory is invalid")
        relative = _validated_relative_path(item.relative_path)
        if item.relative_path in inventory_paths:
            raise PlanningRegulationIndexError(
                "GPU extraction inventory contains duplicate paths"
            )
        inventory_paths.add(item.relative_path)
        if relative.name == pdf_basename:
            matches.append((relative, item))
    if not matches:
        raise PlanningRegulationIndexError(
            f"Regulation PDF is missing from GPU inventory: {pdf_basename}"
        )
    if len(matches) != 1:
        raise PlanningRegulationIndexError(
            f"Regulation PDF is ambiguous in GPU inventory: {pdf_basename}"
        )
    relative, item = matches[0]
    file_type = _strict_string(item.file_type, "PDF inventory file type")
    if file_type.casefold() != "pdf" or item.category != "WRITTEN_REGULATION":
        raise PlanningRegulationIndexError(
            "Regulation PDF inventory classification is inconsistent"
        )
    try:
        root_resolved = root.resolve(strict=True)
    except OSError as error:
        raise PlanningRegulationIndexError(
            "GPU extraction root cannot be resolved safely"
        ) from error
    path = root.joinpath(*relative.parts)
    try:
        resolved = path.resolve(strict=True)
        resolved.relative_to(root_resolved)
    except (OSError, ValueError) as error:
        raise PlanningRegulationIndexError(
            "Regulation PDF path escapes the GPU extraction root"
        ) from error
    current = root
    for part in relative.parts:
        current /= part
        if _is_link_or_junction(current):
            raise PlanningRegulationIndexError(
                "Regulation PDF path contains a symbolic link or junction"
            )
    if not path.is_file():
        raise PlanningRegulationIndexError(
            "Regulation PDF must be an extracted regular file"
        )
    expected_size = _strict_positive_integer(item.size_bytes, "PDF inventory size")
    try:
        actual_size = path.stat().st_size
    except OSError as error:
        raise PlanningRegulationIndexError(
            "Regulation PDF size cannot be read"
        ) from error
    if actual_size != expected_size:
        raise PlanningRegulationIndexError(
            "Regulation PDF size differs from extraction inventory"
        )
    expected_sha = _validated_sha256(item.sha256, "PDF inventory SHA256")
    if _file_sha256(path) != expected_sha:
        raise PlanningRegulationIndexError(
            "Regulation PDF SHA256 differs from extraction inventory"
        )
    return path, item


def _page_error(error: Exception) -> str:
    message = sub(r"\s+", " ", str(error)).strip()
    return f"{type(error).__name__}: {message}" if message else type(error).__name__


def _canonical_page_record(row: dict[str, object]) -> dict[str, object]:
    record = {
        key: row[key]
        for key in PAGE_COLUMNS
        if key != "page_content_sha256"
    }
    if bool(pd.isna(record["extraction_error"])):
        record["extraction_error"] = None
    return record


def _page_hash_payload(
    row: dict[str, object],
    page_hash_schema_version: int = PAGE_HASH_SCHEMA_VERSION,
    search_normalization_profile: str = SEARCH_NORMALIZATION_PROFILE,
) -> dict[str, object]:
    return {
        "schema_version": page_hash_schema_version,
        "search_normalization_profile": search_normalization_profile,
        "page": _canonical_page_record(row),
    }


def _page_content_sha256(
    row: dict[str, object],
    page_hash_schema_version: int = PAGE_HASH_SCHEMA_VERSION,
    search_normalization_profile: str = SEARCH_NORMALIZATION_PROFILE,
) -> str:
    return _canonical_sha256(
        _page_hash_payload(
            row,
            page_hash_schema_version,
            search_normalization_profile,
        )
    )


def _pages_content_sha256(
    frame: pd.DataFrame,
    page_hash_schema_version: int = PAGE_HASH_SCHEMA_VERSION,
    search_normalization_profile: str = SEARCH_NORMALIZATION_PROFILE,
) -> str:
    pages = []
    for row in frame.loc[:, PAGE_COLUMNS].to_dict("records"):
        canonical = _canonical_page_record(row)
        canonical["page_content_sha256"] = row["page_content_sha256"]
        pages.append(canonical)
    return _canonical_sha256(
        {
            "schema_version": page_hash_schema_version,
            "search_normalization_profile": search_normalization_profile,
            "pages": pages,
        }
    )


def _pages_frame(rows: list[dict[str, object]]) -> pd.DataFrame:
    frame = pd.DataFrame(rows, columns=PAGE_COLUMNS)
    frame["page_number"] = frame["page_number"].astype("int64")
    frame["character_count"] = frame["character_count"].astype("int64")
    return frame


def _index_hash_payload(index: PlanningRegulationIndex) -> dict[str, object]:
    return {
        "domain": "landscout.planning_regulation.index",
        "index_hash_schema_version": index.index_hash_schema_version,
        "document_id": index.document_id,
        "archive_sha256": index.archive_sha256,
        "regulation_filename": index.regulation_filename,
        "source_selection_method": index.source_selection_method,
        "source_selection_sha256": index.source_selection_sha256,
        "pdf_relative_path": index.pdf_relative_path,
        "pdf_size_bytes": index.pdf_size_bytes,
        "pdf_sha256": index.pdf_sha256,
        "extraction_library": index.extraction_library,
        "extraction_library_version": index.extraction_library_version,
        "search_normalization_profile": index.search_normalization_profile,
        "page_hash_schema_version": index.page_hash_schema_version,
        "total_page_count": index.total_page_count,
        "pages_content_sha256": index.pages_content_sha256,
    }


def _index_content_sha256(index: PlanningRegulationIndex) -> str:
    return _canonical_sha256(_index_hash_payload(index))


def _source_selection_sha256(
    filename: str,
    method: str,
    zoning_evidence: _ZoningSourceEvidence,
    written_file: GpuWrittenFile,
    pdf_inventory: GpuExtractedFile,
) -> str:
    return _canonical_sha256(
        {
            "domain": "landscout.planning_regulation.source_selection",
            "regulation_filename": filename,
            "source_selection_method": method,
            "zoning": {
                "source_layer": zoning_evidence.source_layer,
                "driver": zoning_evidence.driver,
                "source_files": [
                    {
                        "relative_path": item.relative_path,
                        "size_bytes": item.size_bytes,
                        "sha256": item.sha256,
                    }
                    for item in zoning_evidence.files
                ],
            },
            "written_file": {
                "filename": written_file.filename,
                "title": written_file.title,
                "document_path": written_file.document_path,
                "source_url": written_file.source_url,
            },
            "pdf_inventory": {
                "relative_path": pdf_inventory.relative_path,
                "size_bytes": pdf_inventory.size_bytes,
                "sha256": pdf_inventory.sha256,
                "file_type": pdf_inventory.file_type,
                "category": pdf_inventory.category,
            },
        }
    )


def _validate_pages(
    frame: pd.DataFrame,
    total_page_count: int,
    page_hash_schema_version: int,
    search_normalization_profile: str,
) -> None:
    if not isinstance(frame, pd.DataFrame):
        raise PlanningRegulationIndexError("Regulation pages must be a DataFrame")
    if tuple(frame.columns) != PAGE_COLUMNS:
        raise PlanningRegulationIndexError("Regulation page schema is not deterministic")
    if len(frame) != total_page_count:
        raise PlanningRegulationIndexError("Regulation page count is inconsistent")
    if frame["page_number"].tolist() != list(range(1, total_page_count + 1)):
        raise PlanningRegulationIndexError(
            "Regulation page numbers must be unique and ordered from 1"
        )
    if not frame["extraction_status"].isin({"TEXT", "EMPTY", "ERROR"}).all():
        raise PlanningRegulationIndexError("Regulation extraction status is invalid")
    for row in frame.to_dict("records"):
        _strict_positive_integer(row["page_number"], "page number")
        character_count = _strict_nonnegative_integer(
            row["character_count"], "character count"
        )
        raw_text = row["raw_text"]
        normalized = row["normalized_search_text"]
        status = row["extraction_status"]
        extraction_error = row["extraction_error"]
        error_is_null = bool(pd.isna(extraction_error))
        if not isinstance(raw_text, str) or not isinstance(normalized, str):
            raise PlanningRegulationIndexError("Regulation page text must be a string")
        if character_count != len(raw_text):
            raise PlanningRegulationIndexError(
                "Regulation page character count is inconsistent"
            )
        if normalized != _normalize_search_text(raw_text):
            raise PlanningRegulationIndexError(
                "Regulation normalized search text is inconsistent"
            )
        if status == "TEXT" and (not normalized or not error_is_null):
            raise PlanningRegulationIndexError("TEXT page state is inconsistent")
        if status == "EMPTY" and (normalized or not error_is_null):
            raise PlanningRegulationIndexError("EMPTY page state is inconsistent")
        if status == "ERROR" and (
            raw_text
            or normalized
            or not isinstance(extraction_error, str)
            or not extraction_error
        ):
            raise PlanningRegulationIndexError("ERROR page state is inconsistent")
        checksum = _validated_sha256(
            row["page_content_sha256"], "page content SHA256"
        )
        if checksum != _page_content_sha256(
            row,
            page_hash_schema_version,
            search_normalization_profile,
        ):
            raise PlanningRegulationIndexError("Regulation page content hash differs")


def _pypdf_version() -> str:
    try:
        return version("pypdf")
    except Exception as error:
        raise PlanningRegulationIndexError(
            "pypdf package version cannot be determined"
        ) from error


def _index_planning_regulation(
    planning_document: GpuPlanningDocument,
    regulation_filename: str | None = None,
) -> PlanningRegulationIndex:
    """Index the source-validated primary written regulation page by page."""

    document_id, archive_sha = _validate_document_lineage(planning_document)
    filename, selection_method, zoning_evidence, written_file = (
        _resolve_regulation_filename(planning_document, regulation_filename)
    )
    path, inventory = _locate_regulation_pdf(planning_document, filename)
    selection_sha = _source_selection_sha256(
        filename,
        selection_method,
        zoning_evidence,
        written_file,
        inventory,
    )
    rows: list[dict[str, object]] = []
    try:
        with path.open("rb") as stream:
            reader = PdfReader(stream, strict=False)
            if reader.is_encrypted:
                raise PlanningRegulationIndexError(
                    "Encrypted regulation PDFs are not supported"
                )
            total_page_count = len(reader.pages)
            if total_page_count == 0:
                raise PlanningRegulationIndexError(
                    "Regulation PDF must contain at least one page"
                )
            for page_index in range(total_page_count):
                try:
                    extracted = reader.pages[page_index].extract_text()
                    raw_text = "" if extracted is None else extracted
                    if not isinstance(raw_text, str):
                        raise TypeError("PDF page extractor returned non-text data")
                    normalized = _normalize_search_text(raw_text)
                    status: ExtractionStatus = "TEXT" if normalized else "EMPTY"
                    extraction_error: str | None = None
                except Exception as error:  # noqa: BLE001 - isolate one bad PDF page
                    raw_text = ""
                    normalized = ""
                    status = "ERROR"
                    extraction_error = _page_error(error)
                row: dict[str, object] = {
                    "page_number": page_index + 1,
                    "extraction_status": status,
                    "raw_text": raw_text,
                    "normalized_search_text": normalized,
                    "character_count": len(raw_text),
                    "extraction_error": extraction_error,
                }
                row["page_content_sha256"] = _page_content_sha256(row)
                rows.append(row)
    except PlanningRegulationIndexError:
        raise
    except Exception as error:
        raise PlanningRegulationIndexError(
            "Regulation PDF cannot be opened or parsed"
        ) from error
    try:
        final_size = path.stat().st_size
    except OSError as error:
        raise PlanningRegulationIndexError(
            "Regulation PDF size cannot be revalidated"
        ) from error
    final_sha = _file_sha256(path)
    if final_size != inventory.size_bytes or final_sha != inventory.sha256:
        raise PlanningRegulationIndexError(
            "Regulation PDF changed during text extraction"
        )
    pages = _pages_frame(rows)
    result = PlanningRegulationIndex(
        document_id=document_id,
        archive_sha256=archive_sha,
        regulation_filename=filename,
        source_selection_method=selection_method,
        source_selection_sha256=selection_sha,
        pdf_relative_path=inventory.relative_path,
        pdf_size_bytes=inventory.size_bytes,
        pdf_sha256=final_sha,
        extraction_library="pypdf",
        extraction_library_version=_pypdf_version(),
        search_normalization_profile=SEARCH_NORMALIZATION_PROFILE,
        page_hash_schema_version=PAGE_HASH_SCHEMA_VERSION,
        index_hash_schema_version=INDEX_HASH_SCHEMA_VERSION,
        total_page_count=total_page_count,
        pages_content_sha256=_pages_content_sha256(pages),
        index_content_sha256="",
        pages=pages,
    )
    result = replace(result, index_content_sha256=_index_content_sha256(result))
    validate_planning_regulation_index(result)
    return result


def index_planning_regulation(
    planning_document: GpuPlanningDocument,
    regulation_filename: str | None = None,
) -> PlanningRegulationIndex:
    """Index one source-validated written regulation with controlled failures."""

    try:
        return _index_planning_regulation(planning_document, regulation_filename)
    except PlanningRegulationIndexError:
        raise
    except Exception as error:
        raise PlanningRegulationIndexError(
            "Planning regulation indexing failed safely"
        ) from error


def _validate_planning_regulation_index(index: PlanningRegulationIndex) -> None:
    if not isinstance(index, PlanningRegulationIndex):
        raise PlanningRegulationIndexError(
            "index must be a PlanningRegulationIndex"
        )
    _strict_string(index.document_id, "regulation document ID")
    _validated_sha256(index.archive_sha256, "regulation archive SHA256")
    filename = _validated_pdf_basename(index.regulation_filename)
    if index.source_selection_method not in {
        "ZONING_NOMFIC",
        "EXPLICIT_ZONING_NOMFIC",
    }:
        raise PlanningRegulationIndexError(
            "Regulation source-selection method is unsupported"
        )
    _validated_sha256(index.source_selection_sha256, "source selection SHA256")
    relative_pdf = _validated_relative_path(index.pdf_relative_path)
    if relative_pdf.name != filename:
        raise PlanningRegulationIndexError(
            "Regulation filename differs from PDF relative path"
        )
    _strict_positive_integer(index.pdf_size_bytes, "regulation PDF size")
    _validated_sha256(index.pdf_sha256, "regulation PDF SHA256")
    if index.extraction_library != "pypdf":
        raise PlanningRegulationIndexError("Regulation extraction library differs")
    _strict_string(index.extraction_library_version, "extraction library version")
    if index.search_normalization_profile != SEARCH_NORMALIZATION_PROFILE:
        raise PlanningRegulationIndexError(
            "Regulation search normalization profile is unsupported"
        )
    page_schema = _supported_schema_version(
        index.page_hash_schema_version,
        PAGE_HASH_SCHEMA_VERSION,
        "page hash schema version",
    )
    _supported_schema_version(
        index.index_hash_schema_version,
        INDEX_HASH_SCHEMA_VERSION,
        "index hash schema version",
    )
    total = _strict_positive_integer(index.total_page_count, "total page count")
    _validate_pages(
        index.pages,
        total,
        page_schema,
        index.search_normalization_profile,
    )
    checksum = _validated_sha256(
        index.pages_content_sha256, "pages content SHA256"
    )
    if checksum != _pages_content_sha256(
        index.pages,
        page_schema,
        index.search_normalization_profile,
    ):
        raise PlanningRegulationIndexError("Regulation pages envelope hash differs")
    index_checksum = _validated_sha256(
        index.index_content_sha256, "index content SHA256"
    )
    if index_checksum != _index_content_sha256(index):
        raise PlanningRegulationIndexError("Regulation index envelope hash differs")


def validate_planning_regulation_index(index: PlanningRegulationIndex) -> None:
    """Validate all page, metadata, and complete index integrity contracts."""

    try:
        _validate_planning_regulation_index(index)
    except PlanningRegulationIndexError:
        raise
    except Exception as error:
        raise PlanningRegulationIndexError(
            "Regulation index validation failed safely"
        ) from error


_validate_index = validate_planning_regulation_index


def _validated_terms(terms: Sequence[str]) -> tuple[tuple[str, str], ...]:
    if isinstance(terms, (str, bytes)) or not isinstance(terms, Sequence):
        raise PlanningRegulationIndexError("Search terms must be a sequence of terms")
    result: list[tuple[str, str]] = []
    normalized_seen: set[str] = set()
    for term in terms:
        raw_term = _strict_string(term, "search term")
        normalized_term = _normalize_search_text(raw_term)
        if not normalized_term or normalized_term in normalized_seen:
            raise PlanningRegulationIndexError(
                "Search terms must be unique after normalization"
            )
        normalized_seen.add(normalized_term)
        result.append((raw_term, normalized_term))
    return tuple(result)


def _empty_hits() -> pd.DataFrame:
    return pd.DataFrame(
        {
            column: pd.Series(
                dtype=(
                    "int64"
                    if column in {"page_number", "occurrence_count"}
                    else "object"
                )
            )
            for column in SEARCH_HIT_COLUMNS
        }
    )


def _build_hits(
    index: PlanningRegulationIndex,
    terms: tuple[tuple[str, str], ...],
    context_characters: int,
) -> pd.DataFrame:
    hits: list[dict[str, object]] = []
    for raw_term, normalized_term in terms:
        pattern = escape(normalized_term)
        for page in index.pages.to_dict("records"):
            raw_text = page["raw_text"]
            normalized_text, raw_spans = _normalize_search_text_with_mapping(
                raw_text
            )
            matches = list(finditer(pattern, normalized_text))
            if not matches:
                continue
            first = matches[0]
            context_start = max(0, first.start() - context_characters)
            context_end = min(
                len(normalized_text), first.end() + context_characters
            )
            hits.append(
                {
                    "document_id": index.document_id,
                    "archive_sha256": index.archive_sha256,
                    "pdf_sha256": index.pdf_sha256,
                    "search_normalization_profile": SEARCH_NORMALIZATION_PROFILE,
                    "search_term": raw_term,
                    "normalized_search_term": normalized_term,
                    "page_number": page["page_number"],
                    "occurrence_count": len(matches),
                    "raw_context": _raw_context(
                        raw_text, raw_spans, context_start, context_end
                    ),
                    "normalized_context": normalized_text[
                        context_start:context_end
                    ],
                }
            )
    if not hits:
        return _empty_hits()
    frame = pd.DataFrame(hits, columns=SEARCH_HIT_COLUMNS)
    frame["page_number"] = frame["page_number"].astype("int64")
    frame["occurrence_count"] = frame["occurrence_count"].astype("int64")
    return frame


def _hits_content_sha256(
    index: PlanningRegulationIndex,
    requested_terms: tuple[str, ...],
    context_characters: int,
    hits: pd.DataFrame,
    search_hash_schema_version: int = SEARCH_HASH_SCHEMA_VERSION,
) -> str:
    return _canonical_sha256(
        {
            "domain": "landscout.planning_regulation.search",
            "search_hash_schema_version": search_hash_schema_version,
            "index_content_sha256": index.index_content_sha256,
            "document_id": index.document_id,
            "archive_sha256": index.archive_sha256,
            "pdf_sha256": index.pdf_sha256,
            "search_normalization_profile": index.search_normalization_profile,
            "requested_terms": list(requested_terms),
            "context_characters": context_characters,
            "hit_count": len(hits),
            "hits": hits.loc[:, SEARCH_HIT_COLUMNS].to_dict("records"),
        }
    )


def search_planning_regulation(
    index: PlanningRegulationIndex,
    terms: Sequence[str],
    *,
    context_characters: int = 80,
) -> PlanningRegulationSearchResult:
    """Return sealed literal search hits with raw and normalized contexts."""

    validate_planning_regulation_index(index)
    validated_terms = _validated_terms(terms)
    context = _strict_nonnegative_integer(context_characters, "context_characters")
    requested = tuple(raw for raw, _ in validated_terms)
    hits = _build_hits(index, validated_terms, context)
    result = PlanningRegulationSearchResult(
        document_id=index.document_id,
        archive_sha256=index.archive_sha256,
        pdf_sha256=index.pdf_sha256,
        search_normalization_profile=index.search_normalization_profile,
        search_hash_schema_version=SEARCH_HASH_SCHEMA_VERSION,
        index_content_sha256=index.index_content_sha256,
        requested_terms=requested,
        context_characters=context,
        hit_count=len(hits),
        hits_content_sha256=_hits_content_sha256(index, requested, context, hits),
        hits=hits,
    )
    validate_planning_regulation_search_result(index, result)
    return result


def _validate_planning_regulation_search_result(
    index: PlanningRegulationIndex,
    result: PlanningRegulationSearchResult,
) -> None:
    validate_planning_regulation_index(index)
    if not isinstance(result, PlanningRegulationSearchResult):
        raise PlanningRegulationIndexError(
            "result must be a PlanningRegulationSearchResult"
        )
    if (
        result.document_id != index.document_id
        or result.archive_sha256 != index.archive_sha256
        or result.pdf_sha256 != index.pdf_sha256
        or result.search_normalization_profile
        != index.search_normalization_profile
        or result.index_content_sha256 != index.index_content_sha256
    ):
        raise PlanningRegulationIndexError("Search-result lineage differs from index")
    search_schema = _supported_schema_version(
        result.search_hash_schema_version,
        SEARCH_HASH_SCHEMA_VERSION,
        "search hash schema version",
    )
    if type(result.requested_terms) is not tuple:
        raise PlanningRegulationIndexError(
            "Search-result requested_terms must be tuple[str, ...]"
        )
    validated_terms = _validated_terms(result.requested_terms)
    context = _strict_nonnegative_integer(
        result.context_characters, "context_characters"
    )
    if not isinstance(result.hits, pd.DataFrame) or tuple(result.hits.columns) != (
        SEARCH_HIT_COLUMNS
    ):
        raise PlanningRegulationIndexError("Search-hit schema is not deterministic")
    hit_count = _strict_nonnegative_integer(result.hit_count, "hit count")
    if hit_count != len(result.hits):
        raise PlanningRegulationIndexError("Search-result hit count differs")
    allowed_pages = set(index.pages["page_number"].tolist())
    allowed_terms = {normalized for _, normalized in validated_terms}
    seen: set[tuple[str, int]] = set()
    for row in result.hits.to_dict("records"):
        if (
            row["document_id"] != index.document_id
            or row["archive_sha256"] != index.archive_sha256
            or row["pdf_sha256"] != index.pdf_sha256
            or row["search_normalization_profile"]
            != index.search_normalization_profile
        ):
            raise PlanningRegulationIndexError("Search-hit lineage differs from index")
        normalized_term = _strict_string(
            row["normalized_search_term"], "normalized search term"
        )
        if normalized_term not in allowed_terms:
            raise PlanningRegulationIndexError("Search hit has an unrequested term")
        page_number = _strict_positive_integer(row["page_number"], "hit page number")
        if page_number not in allowed_pages:
            raise PlanningRegulationIndexError("Search hit references an unknown page")
        pair = (normalized_term, page_number)
        if pair in seen:
            raise PlanningRegulationIndexError("Search hit page/term pair is duplicated")
        seen.add(pair)
        _strict_positive_integer(row["occurrence_count"], "occurrence count")
        if not isinstance(row["raw_context"], str) or not isinstance(
            row["normalized_context"], str
        ):
            raise PlanningRegulationIndexError("Search contexts must be strings")
    requested = tuple(raw for raw, _ in validated_terms)
    checksum = _validated_sha256(
        result.hits_content_sha256, "hits content SHA256"
    )
    if checksum != _hits_content_sha256(
        index,
        requested,
        context,
        result.hits,
        search_schema,
    ):
        raise PlanningRegulationIndexError("Search-result content hash differs")
    expected = _build_hits(index, validated_terms, context)
    if not result.hits.reset_index(drop=True).equals(expected):
        raise PlanningRegulationIndexError(
            "Search-result rows differ from deterministic source search"
        )


def validate_planning_regulation_search_result(
    index: PlanningRegulationIndex,
    result: PlanningRegulationSearchResult,
) -> None:
    """Validate search lineage, schema, rows, hash, and source-derived contexts."""

    try:
        _validate_planning_regulation_search_result(index, result)
    except PlanningRegulationIndexError:
        raise
    except Exception as error:
        raise PlanningRegulationIndexError(
            "Regulation search-result validation failed safely"
        ) from error

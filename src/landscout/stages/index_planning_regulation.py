"""Build a factual page-level text index for an extracted GPU regulation PDF."""

from __future__ import annotations

import unicodedata
from collections.abc import Sequence
from dataclasses import dataclass
from hashlib import sha256
from importlib.metadata import version
from numbers import Integral
from pathlib import Path, PurePosixPath
from re import escape, finditer, fullmatch, sub
from typing import Literal

import pandas as pd  # type: ignore[import-untyped]
from pypdf import PdfReader

from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuPlanningDocument,
)

__all__ = [
    "PlanningRegulationIndex",
    "PlanningRegulationIndexError",
    "index_planning_regulation",
    "search_planning_regulation",
]

PAGE_COLUMNS = (
    "page_number",
    "extraction_status",
    "raw_text",
    "normalized_search_text",
    "character_count",
    "extraction_error",
)
SEARCH_HIT_COLUMNS = (
    "search_term",
    "page_number",
    "occurrence_count",
    "context",
)
MURET_REGULATION_PDF_BASENAME = "31395_reglement_20240215.pdf"

ExtractionStatus = Literal["TEXT", "EMPTY", "ERROR"]


class PlanningRegulationIndexError(ValueError):
    """Raised when a GPU regulation cannot be indexed without losing integrity."""


@dataclass(frozen=True)
class PlanningRegulationIndex:
    """Immutable lineage envelope around a deterministic page text table."""

    document_id: str
    archive_sha256: str
    pdf_relative_path: str
    pdf_size_bytes: int
    pdf_sha256: str
    extraction_library: str
    extraction_library_version: str
    total_page_count: int
    pages: pd.DataFrame


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


def _validated_sha256(value: object, label: str) -> str:
    checksum = _strict_string(value, label)
    if fullmatch(r"[0-9a-fA-F]{64}", checksum) is None:
        raise PlanningRegulationIndexError(
            f"{label} must contain exactly 64 hexadecimal characters"
        )
    return checksum


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
    name = _strict_string(value, "regulation PDF basename")
    if (
        name in {".", ".."}
        or "/" in name
        or "\\" in name
        or Path(name).name != name
        or not name.casefold().endswith(".pdf")
    ):
        raise PlanningRegulationIndexError(
            "regulation PDF basename must be one safe PDF filename"
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
    if archive.archive_format.casefold() != "zip":
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
    for layer in (planning_document.zoning, *planning_document.related_layers):
        if (
            layer.summary.source_document_id != document_id
            or layer.summary.source_archive_sha256 != archive_sha
        ):
            raise PlanningRegulationIndexError(
                "GPU spatial-layer lineage is inconsistent with the archive"
            )
    return document_id, archive_sha


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
    expected_size = _strict_nonnegative_integer(item.size_bytes, "PDF inventory size")
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
    if _file_sha256(path) != expected_sha.casefold():
        raise PlanningRegulationIndexError(
            "Regulation PDF SHA256 differs from extraction inventory"
        )
    return path, item


def _normalize_search_text(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value)
    accentless = "".join(
        character for character in decomposed if not unicodedata.combining(character)
    )
    return sub(r"\s+", " ", accentless.casefold()).strip()


def _page_error(error: Exception) -> str:
    message = sub(r"\s+", " ", str(error)).strip()
    return f"{type(error).__name__}: {message}" if message else type(error).__name__


def _pages_frame(rows: list[dict[str, object]]) -> pd.DataFrame:
    frame = pd.DataFrame(rows, columns=PAGE_COLUMNS)
    frame["page_number"] = frame["page_number"].astype("int64")
    frame["character_count"] = frame["character_count"].astype("int64")
    return frame


def _validate_pages(frame: pd.DataFrame, total_page_count: int) -> None:
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
    for _, row in frame.iterrows():
        _strict_nonnegative_integer(row["page_number"], "page number")
        _strict_nonnegative_integer(row["character_count"], "character count")
        raw_text = row["raw_text"]
        normalized = row["normalized_search_text"]
        character_count = row["character_count"]
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


def index_planning_regulation(
    planning_document: GpuPlanningDocument,
) -> PlanningRegulationIndex:
    """Extract raw and normalized text for every page of one inventoried PDF."""

    basename = _validated_pdf_basename(MURET_REGULATION_PDF_BASENAME)
    document_id, archive_sha = _validate_document_lineage(planning_document)
    path, inventory = _locate_regulation_pdf(planning_document, basename)
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
                rows.append(
                    {
                        "page_number": page_index + 1,
                        "extraction_status": status,
                        "raw_text": raw_text,
                        "normalized_search_text": normalized,
                        "character_count": len(raw_text),
                        "extraction_error": extraction_error,
                    }
                )
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
    if final_size != inventory.size_bytes or final_sha != inventory.sha256.casefold():
        raise PlanningRegulationIndexError(
            "Regulation PDF changed during text extraction"
        )
    pages = _pages_frame(rows)
    _validate_pages(pages, total_page_count)
    return PlanningRegulationIndex(
        document_id=document_id,
        archive_sha256=archive_sha,
        pdf_relative_path=inventory.relative_path,
        pdf_size_bytes=inventory.size_bytes,
        pdf_sha256=final_sha,
        extraction_library="pypdf",
        extraction_library_version=version("pypdf"),
        total_page_count=total_page_count,
        pages=pages,
    )


def _validate_index(index: PlanningRegulationIndex) -> None:
    if not isinstance(index, PlanningRegulationIndex):
        raise PlanningRegulationIndexError(
            "index must be a PlanningRegulationIndex"
        )
    _strict_string(index.document_id, "regulation document ID")
    _validated_sha256(index.archive_sha256, "regulation archive SHA256")
    _validated_relative_path(index.pdf_relative_path)
    _strict_nonnegative_integer(index.pdf_size_bytes, "regulation PDF size")
    if index.pdf_size_bytes == 0:
        raise PlanningRegulationIndexError("regulation PDF size must be positive")
    _validated_sha256(index.pdf_sha256, "regulation PDF SHA256")
    _strict_string(index.extraction_library, "extraction library")
    _strict_string(index.extraction_library_version, "extraction library version")
    total = _strict_nonnegative_integer(index.total_page_count, "total page count")
    if total == 0:
        raise PlanningRegulationIndexError("total page count must be positive")
    _validate_pages(index.pages, total)


def search_planning_regulation(
    index: PlanningRegulationIndex,
    terms: Sequence[str],
    *,
    context_characters: int = 80,
) -> pd.DataFrame:
    """Return literal, accent/case-insensitive page hits without interpretation."""

    _validate_index(index)
    if isinstance(terms, (str, bytes)) or not isinstance(terms, Sequence):
        raise PlanningRegulationIndexError("Search terms must be a sequence of terms")
    if (
        isinstance(context_characters, bool)
        or not isinstance(context_characters, int)
        or context_characters < 0
    ):
        raise PlanningRegulationIndexError(
            "context_characters must be a non-negative integer"
        )
    validated_terms: list[tuple[str, str]] = []
    normalized_seen: set[str] = set()
    for term in terms:
        raw_term = _strict_string(term, "search term")
        normalized_term = _normalize_search_text(raw_term)
        if not normalized_term or normalized_term in normalized_seen:
            raise PlanningRegulationIndexError(
                "Search terms must be unique after normalization"
            )
        normalized_seen.add(normalized_term)
        validated_terms.append((raw_term, normalized_term))

    hits: list[dict[str, object]] = []
    for raw_term, normalized_term in validated_terms:
        pattern = escape(normalized_term)
        for _, page in index.pages.iterrows():
            text = page["normalized_search_text"]
            matches = list(finditer(pattern, text))
            if not matches:
                continue
            first = matches[0]
            context_start = max(0, first.start() - context_characters)
            context_end = min(len(text), first.end() + context_characters)
            context = text[context_start:context_end]
            hits.append(
                {
                    "search_term": raw_term,
                    "page_number": int(page["page_number"]),
                    "occurrence_count": len(matches),
                    "context": context,
                }
            )
    result = pd.DataFrame(hits, columns=SEARCH_HIT_COLUMNS)
    if result.empty:
        return pd.DataFrame(
            {
                "search_term": pd.Series(dtype="object"),
                "page_number": pd.Series(dtype="int64"),
                "occurrence_count": pd.Series(dtype="int64"),
                "context": pd.Series(dtype="object"),
            }
        )
    result["page_number"] = result["page_number"].astype("int64")
    result["occurrence_count"] = result["occurrence_count"].astype("int64")
    return result

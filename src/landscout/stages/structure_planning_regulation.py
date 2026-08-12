"""Structure a validated planning regulation into factual, auditable evidence."""

from __future__ import annotations

import json
import math
import re
from collections import Counter
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, replace
from hashlib import sha256
from numbers import Integral, Real
from pathlib import Path
from typing import Literal

import numpy as np
import pandas as pd  # type: ignore[import-untyped]
import yaml  # type: ignore[import-untyped]
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, model_validator

from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    _normalize_search_text,
    _normalize_search_text_with_mapping,
    _raw_context,
    validate_planning_regulation_index,
)

__all__ = [
    "PlanningRegulationStructureConfig",
    "PlanningRegulationStructureError",
    "PlanningRegulationStructureResult",
    "load_planning_regulation_structure_config",
    "structure_planning_regulation",
    "validate_planning_regulation_structure",
]

SECTION_HASH_SCHEMA_VERSION = 1
_SUPPORTED_CONFIG_SCHEMA_VERSION = 1

_SECTION_TYPES = frozenset({"GENERAL", "ZONE_CHAPTER", "ARTICLE", "OTHER"})
_MAPPING_STATUSES = frozenset({"EXACT", "CONFIG_ALIAS", "UNMAPPED", "AMBIGUOUS"})
_MAPPING_METHODS = frozenset({"EXACT_HEADING", "CONFIG_ALIAS", "NONE", "AMBIGUOUS"})
_EVIDENCE_SCOPES = frozenset({"GENERAL_RULE", "ZONE_SPECIFIC_RULE"})

SECTION_COLUMNS = (
    "section_id",
    "parent_section_id",
    "section_type",
    "heading_raw",
    "heading_normalized",
    "zone_chapter_label",
    "article_number_raw",
    "article_title_raw",
    "start_page",
    "end_page",
    "page_numbers",
    "raw_text",
    "normalized_text",
    "character_count",
    "section_content_sha256",
    "document_id",
    "archive_sha256",
    "pdf_sha256",
    "index_content_sha256",
    "structure_profile",
)

ZONE_MAPPING_COLUMNS = (
    "source_zone_label_raw",
    "resolved_zone_chapter_label",
    "mapping_status",
    "mapping_method",
    "matched_section_id",
    "zone_polygon_count",
    "candidate_parcel_count",
    "candidate_intersection_count",
    "dominant_candidate_count",
    "document_id",
    "archive_sha256",
    "pdf_sha256",
    "index_content_sha256",
    "structure_profile",
)

TOPIC_EVIDENCE_COLUMNS = (
    "topic",
    "search_term",
    "normalized_search_term",
    "section_id",
    "evidence_scope",
    "zone_chapter_label",
    "article_number_raw",
    "page_number",
    "occurrence_count",
    "raw_context",
    "normalized_context",
    "document_id",
    "archive_sha256",
    "pdf_sha256",
    "index_content_sha256",
    "structure_profile",
)


class PlanningRegulationStructureError(ValueError):
    """Raised when factual regulation structure integrity cannot be proven."""


class _StrictConfigModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class DocumentLockConfig(_StrictConfigModel):
    document_id: StrictStr = Field(min_length=1)
    pdf_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    pages_content_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    index_content_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    normalization_profile: StrictStr = Field(min_length=1)


class DocumentLayoutConfig(_StrictConfigModel):
    body_start_page: StrictInt = Field(ge=1)
    table_of_contents_pages: tuple[StrictInt, ...] = ()
    max_heading_continuation_lines: StrictInt = Field(ge=0, le=10)

    @model_validator(mode="after")
    def _validate_pages(self) -> DocumentLayoutConfig:
        pages = self.table_of_contents_pages
        if any(page < 1 for page in pages) or tuple(sorted(set(pages))) != pages:
            raise ValueError(
                "table_of_contents_pages must contain unique ascending positive integers"
            )
        return self


class HeadingPatternsConfig(_StrictConfigModel):
    zone_chapter: tuple[StrictStr, ...] = Field(min_length=1)
    article: tuple[StrictStr, ...] = Field(min_length=1)
    general_section: tuple[StrictStr, ...] = Field(min_length=1)
    continuation: tuple[StrictStr, ...] = Field(min_length=1)


class IgnoredPatternsConfig(_StrictConfigModel):
    page_headers: tuple[StrictStr, ...] = Field(min_length=1)
    page_footers: tuple[StrictStr, ...] = Field(min_length=1)


class PlanningRegulationStructureConfig(_StrictConfigModel):
    """Strict, document-locked grammar for one factual regulation structure."""

    schema_version: StrictInt
    structure_profile: StrictStr = Field(min_length=1)
    document_lock: DocumentLockConfig
    document_layout: DocumentLayoutConfig
    heading_patterns: HeadingPatternsConfig
    ignored_patterns: IgnoredPatternsConfig
    zone_aliases: dict[StrictStr, StrictStr]
    topics: dict[StrictStr, tuple[StrictStr, ...]]
    topic_context_characters: StrictInt = Field(ge=0)

    @model_validator(mode="after")
    def _validate_grammar(self) -> PlanningRegulationStructureConfig:
        if self.schema_version != _SUPPORTED_CONFIG_SCHEMA_VERSION:
            raise ValueError(
                f"unsupported structure config schema: {self.schema_version}"
            )
        _exact_config_string(self.structure_profile, "structure_profile")
        _exact_config_string(self.document_lock.document_id, "document_id")
        _exact_config_string(
            self.document_lock.normalization_profile,
            "normalization_profile",
        )
        pattern_groups = (
            self.heading_patterns.zone_chapter,
            self.heading_patterns.article,
            self.heading_patterns.general_section,
            self.heading_patterns.continuation,
            self.ignored_patterns.page_headers,
            self.ignored_patterns.page_footers,
        )
        for patterns in pattern_groups:
            if len(set(patterns)) != len(patterns):
                raise ValueError("regular-expression patterns must be unique")
            for pattern in patterns:
                _exact_config_string(pattern, "regular-expression pattern")
                try:
                    re.compile(pattern)
                except re.error as error:
                    raise ValueError(f"invalid regular expression: {pattern}") from error
        for alias, target in self.zone_aliases.items():
            _exact_config_string(alias, "zone alias")
            _exact_config_string(target, "zone alias target")
        _validate_alias_cycles(self.zone_aliases)
        if not self.topics:
            raise ValueError("topics must not be empty")
        for topic, terms in self.topics.items():
            _exact_config_string(topic, "topic")
            if not terms:
                raise ValueError(f"topic {topic!r} must contain literal terms")
            normalized: set[str] = set()
            for term in terms:
                _exact_config_string(term, "topic search term")
                normalized_term = _normalize_search_text(term)
                if not normalized_term or normalized_term in normalized:
                    raise ValueError(
                        f"topic {topic!r} contains duplicate normalized terms"
                    )
                normalized.add(normalized_term)
        return self


@dataclass(frozen=True)
class PlanningRegulationStructureResult:
    """Immutable lineage envelope for regulation sections and factual evidence."""

    document_id: str
    archive_sha256: str
    pdf_sha256: str
    index_content_sha256: str
    structure_profile: str
    structure_config_sha256: str
    section_hash_schema_version: int
    sections_content_sha256: str
    zone_map_content_sha256: str
    topic_evidence_content_sha256: str
    sections: pd.DataFrame
    zone_mapping: pd.DataFrame
    topic_evidence: pd.DataFrame


@dataclass(frozen=True)
class _LineRecord:
    page_number: int
    raw: str


@dataclass(frozen=True)
class _HeadingEvent:
    record_position: int
    section_type: Literal["GENERAL", "ZONE_CHAPTER", "ARTICLE"]
    heading_raw: str
    heading_normalized: str
    zone_chapter_label: str | None
    article_number_raw: str | None
    article_title_raw: str | None


@dataclass(frozen=True)
class _SectionBuild:
    row: dict[str, object]
    page_fragments: tuple[tuple[int, str], ...]


class _UniqueKeyLoader(yaml.SafeLoader):
    pass


def _construct_unique_mapping(
    loader: yaml.SafeLoader,
    node: yaml.MappingNode,
    deep: bool = False,
) -> dict[object, object]:
    result: dict[object, object] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise PlanningRegulationStructureError(
                f"Duplicate YAML configuration key: {key!r}"
            )
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


_UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_unique_mapping,
)


def _exact_config_string(value: str, label: str) -> str:
    if not value or value != value.strip():
        raise ValueError(f"{label} must be a non-empty exact string")
    return value


def _validate_alias_cycles(aliases: Mapping[str, str]) -> None:
    for start in aliases:
        seen: set[str] = set()
        current = start
        while current in aliases:
            if current in seen:
                raise ValueError(f"zone alias cycle detected at {current!r}")
            seen.add(current)
            current = aliases[current]


def load_planning_regulation_structure_config(
    path: str | Path,
) -> PlanningRegulationStructureConfig:
    """Load and strictly validate a document-specific structure grammar."""

    try:
        config_path = Path(path)
        payload = yaml.load(config_path.read_text(encoding="utf-8"), Loader=_UniqueKeyLoader)
        if not isinstance(payload, Mapping):
            raise PlanningRegulationStructureError(
                "Planning structure configuration must be a mapping"
            )
        return PlanningRegulationStructureConfig.model_validate(payload)
    except PlanningRegulationStructureError:
        raise
    except Exception as error:
        raise PlanningRegulationStructureError(
            "Planning structure configuration is invalid"
        ) from error


def _strict_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise PlanningRegulationStructureError(
            f"{label} must be a non-empty exact string"
        )
    return value


def _strict_nonnegative_integer(value: object, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, Integral):
        raise PlanningRegulationStructureError(f"{label} must be an integer")
    result = int(value)
    if result < 0:
        raise PlanningRegulationStructureError(f"{label} must be non-negative")
    return result


def _strict_positive_integer(value: object, label: str) -> int:
    result = _strict_nonnegative_integer(value, label)
    if result == 0:
        raise PlanningRegulationStructureError(f"{label} must be positive")
    return result


def _validated_sha256(value: object, label: str) -> str:
    checksum = _strict_string(value, label)
    if re.fullmatch(r"[0-9a-f]{64}", checksum) is None:
        raise PlanningRegulationStructureError(
            f"{label} must be exactly 64 lowercase hexadecimal characters"
        )
    return checksum


def _canonical_value(value: object) -> object:
    if value is None or value is pd.NA:
        return None
    if isinstance(value, np.generic):
        return _canonical_value(value.item())
    if isinstance(value, (tuple, list, np.ndarray)):
        return [_canonical_value(item) for item in value]
    if isinstance(value, Mapping):
        return {str(key): _canonical_value(item) for key, item in value.items()}
    if isinstance(value, float) and math.isnan(value):
        return None
    if isinstance(value, (str, int, float, bool)):
        return value
    raise PlanningRegulationStructureError(
        f"Value of type {type(value).__name__} cannot be canonically serialized"
    )


def _canonical_sha256(value: object) -> str:
    try:
        serialized = json.dumps(
            _canonical_value(value),
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except PlanningRegulationStructureError:
        raise
    except Exception as error:
        raise PlanningRegulationStructureError(
            "Canonical integrity serialization failed"
        ) from error
    return sha256(serialized).hexdigest()


def _config_sha256(config: PlanningRegulationStructureConfig) -> str:
    return _canonical_sha256(
        {
            "domain": "landscout.planning_regulation.structure_config",
            "config": config.model_dump(mode="json"),
        }
    )


def _validate_document_lock(
    index: PlanningRegulationIndex,
    config: PlanningRegulationStructureConfig,
) -> None:
    validate_planning_regulation_index(index)
    lock = config.document_lock
    comparisons = (
        (index.document_id, lock.document_id, "document ID"),
        (index.pdf_sha256, lock.pdf_sha256, "PDF SHA256"),
        (
            index.pages_content_sha256,
            lock.pages_content_sha256,
            "pages content SHA256",
        ),
        (
            index.index_content_sha256,
            lock.index_content_sha256,
            "index content SHA256",
        ),
        (
            index.search_normalization_profile,
            lock.normalization_profile,
            "normalization profile",
        ),
    )
    for actual, expected, label in comparisons:
        if actual != expected:
            raise PlanningRegulationStructureError(
                f"Planning structure {label} differs from its document lock"
            )


def _compiled(patterns: Sequence[str]) -> tuple[re.Pattern[str], ...]:
    return tuple(re.compile(pattern) for pattern in patterns)


def _matches_any(value: str, patterns: Sequence[re.Pattern[str]]) -> bool:
    return any(pattern.fullmatch(value) is not None for pattern in patterns)


def _line_records(
    index: PlanningRegulationIndex,
    config: PlanningRegulationStructureConfig,
) -> list[_LineRecord]:
    headers = _compiled(config.ignored_patterns.page_headers)
    footers = _compiled(config.ignored_patterns.page_footers)
    records: list[_LineRecord] = []
    toc_pages = set(config.document_layout.table_of_contents_pages)
    for page in index.pages.to_dict("records"):
        page_number = _strict_positive_integer(page["page_number"], "page number")
        raw_text = page["raw_text"]
        if not isinstance(raw_text, str):
            raise PlanningRegulationStructureError("Page raw text must be a string")
        for raw_line in raw_text.splitlines():
            comparable = raw_line.strip()
            if _matches_any(comparable, headers) or _matches_any(comparable, footers):
                continue
            records.append(_LineRecord(page_number=page_number, raw=raw_line))
        if page_number in toc_pages:
            # Content remains auditable, while its repeated headings are suppressed later.
            continue
    if not records:
        raise PlanningRegulationStructureError("Regulation contains no structural text")
    return records


def _canonical_chapter_label(value: str) -> str:
    label = re.sub(r"\s+", "", value)
    return _strict_string(label, "zone chapter label")


def _first_match(
    value: str,
    patterns: Sequence[re.Pattern[str]],
) -> re.Match[str] | None:
    for pattern in patterns:
        match = pattern.fullmatch(value)
        if match is not None:
            return match
    return None


def _heading_events(
    records: Sequence[_LineRecord],
    config: PlanningRegulationStructureConfig,
) -> list[_HeadingEvent]:
    zones = _compiled(config.heading_patterns.zone_chapter)
    articles = _compiled(config.heading_patterns.article)
    generals = _compiled(config.heading_patterns.general_section)
    continuations = _compiled(config.heading_patterns.continuation)
    toc_pages = set(config.document_layout.table_of_contents_pages)
    events: list[_HeadingEvent] = []
    position = 0
    while position < len(records):
        record = records[position]
        comparable = record.raw.strip()
        if (
            not comparable
            or record.page_number < config.document_layout.body_start_page
            or record.page_number in toc_pages
        ):
            position += 1
            continue
        match = _first_match(comparable, zones)
        section_type: Literal["GENERAL", "ZONE_CHAPTER", "ARTICLE"] | None = None
        if match is not None:
            section_type = "ZONE_CHAPTER"
        else:
            match = _first_match(comparable, generals)
            if match is not None:
                section_type = "GENERAL"
            else:
                match = _first_match(comparable, articles)
                if match is not None:
                    section_type = "ARTICLE"
        if match is None or section_type is None:
            position += 1
            continue
        groups = match.groupdict()
        zone_label = groups.get("label") or groups.get("zone")
        chapter_label = (
            _canonical_chapter_label(zone_label) if zone_label is not None else None
        )
        article_number = groups.get("number")
        title = groups.get("title")
        heading_lines = [record.raw]
        if section_type != "ZONE_CHAPTER":
            cursor = position + 1
            while (
                cursor < len(records)
                and len(heading_lines)
                <= config.document_layout.max_heading_continuation_lines
                and records[cursor].page_number == record.page_number
            ):
                candidate = records[cursor].raw.strip()
                if not candidate or not _matches_any(candidate, continuations):
                    break
                if any(
                    _first_match(candidate, patterns) is not None
                    for patterns in (zones, generals, articles)
                ):
                    break
                heading_lines.append(records[cursor].raw)
                cursor += 1
        heading_raw = "\n".join(heading_lines)
        if title is not None:
            continuation_titles = [line.strip() for line in heading_lines[1:]]
            title = " ".join([title.strip(), *continuation_titles]).strip()
            title = title or None
        events.append(
            _HeadingEvent(
                record_position=position,
                section_type=section_type,
                heading_raw=heading_raw,
                heading_normalized=_normalize_search_text(heading_raw),
                zone_chapter_label=chapter_label,
                article_number_raw=article_number,
                article_title_raw=title,
            )
        )
        position += len(heading_lines)
    if not events:
        raise PlanningRegulationStructureError(
            "No regulation body headings matched the configured grammar"
        )
    return events


def _page_fragments(records: Sequence[_LineRecord]) -> tuple[tuple[int, str], ...]:
    fragments: list[tuple[int, str]] = []
    current_page: int | None = None
    lines: list[str] = []
    for record in records:
        if current_page is not None and record.page_number != current_page:
            fragments.append((current_page, "\n".join(lines)))
            lines = []
        current_page = record.page_number
        lines.append(record.raw)
    if current_page is not None:
        fragments.append((current_page, "\n".join(lines)))
    return tuple(fragments)


def _section_content_sha256(row: Mapping[str, object]) -> str:
    content = {column: row[column] for column in SECTION_COLUMNS if column != "section_content_sha256"}
    return _canonical_sha256(
        {
            "domain": "landscout.planning_regulation.section",
            "section_hash_schema_version": SECTION_HASH_SCHEMA_VERSION,
            "section": content,
        }
    )


def _build_sections(
    index: PlanningRegulationIndex,
    config: PlanningRegulationStructureConfig,
) -> tuple[pd.DataFrame, tuple[_SectionBuild, ...]]:
    records = _line_records(index, config)
    events = _heading_events(records, config)
    starts: list[tuple[int, _HeadingEvent | None]] = []
    if events[0].record_position > 0:
        starts.append((0, None))
    starts.extend((event.record_position, event) for event in events)
    builds: list[_SectionBuild] = []
    current_chapter_id: str | None = None
    current_chapter_label: str | None = None
    for sequence, (start, event) in enumerate(starts, start=1):
        end = starts[sequence][0] if sequence < len(starts) else len(records)
        segment = records[start:end]
        if not segment or not any(record.raw.strip() for record in segment):
            continue
        section_id = f"SECTION-{len(builds) + 1:04d}"
        if event is None:
            section_type = "OTHER"
            heading_raw = segment[0].raw
            heading_normalized = _normalize_search_text(heading_raw)
            zone_label = None
            article_number = None
            article_title = None
            parent_id = None
        else:
            section_type = event.section_type
            heading_raw = event.heading_raw
            heading_normalized = event.heading_normalized
            article_number = event.article_number_raw
            article_title = event.article_title_raw
            if section_type == "ZONE_CHAPTER":
                zone_label = event.zone_chapter_label
                current_chapter_label = zone_label
                current_chapter_id = section_id
                parent_id = None
            elif section_type == "ARTICLE":
                if current_chapter_id is None or current_chapter_label is None:
                    raise PlanningRegulationStructureError(
                        "Zone article has no preceding zone chapter"
                    )
                if (
                    event.zone_chapter_label is None
                    or event.zone_chapter_label.casefold()
                    != current_chapter_label.casefold()
                ):
                    raise PlanningRegulationStructureError(
                        "Zone article label differs from its active chapter"
                    )
                zone_label = current_chapter_label
                parent_id = current_chapter_id
            else:
                zone_label = None
                parent_id = None
                current_chapter_id = None
                current_chapter_label = None
        fragments = _page_fragments(segment)
        pages = tuple(page for page, _ in fragments)
        raw_text = "\n".join(record.raw for record in segment)
        row: dict[str, object] = {
            "section_id": section_id,
            "parent_section_id": parent_id,
            "section_type": section_type,
            "heading_raw": heading_raw,
            "heading_normalized": heading_normalized,
            "zone_chapter_label": zone_label,
            "article_number_raw": article_number,
            "article_title_raw": article_title,
            "start_page": pages[0],
            "end_page": pages[-1],
            "page_numbers": pages,
            "raw_text": raw_text,
            "normalized_text": _normalize_search_text(raw_text),
            "character_count": len(raw_text),
            "section_content_sha256": "",
            "document_id": index.document_id,
            "archive_sha256": index.archive_sha256,
            "pdf_sha256": index.pdf_sha256,
            "index_content_sha256": index.index_content_sha256,
            "structure_profile": config.structure_profile,
        }
        row["section_content_sha256"] = _section_content_sha256(row)
        builds.append(_SectionBuild(row=row, page_fragments=fragments))
    frame = pd.DataFrame([build.row for build in builds], columns=SECTION_COLUMNS)
    frame["start_page"] = frame["start_page"].astype("int64")
    frame["end_page"] = frame["end_page"].astype("int64")
    frame["character_count"] = frame["character_count"].astype("int64")
    return frame, tuple(builds)


def _validate_source_label_values(series: pd.Series, label: str) -> None:
    for value in series.tolist():
        _strict_string(value, label)


def _validated_zoning_inputs(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
    intersections: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    if not isinstance(zones, pd.DataFrame) or not isinstance(intersections, pd.DataFrame):
        raise PlanningRegulationStructureError(
            "Zones and zoning intersections must be DataFrames"
        )
    zone_required = {
        "planning_zone_id",
        "zone_label_raw",
        "source_document_id",
        "source_archive_sha256",
    }
    relation_required = {
        "parcel_id",
        "planning_zone_id",
        "source_zone_id",
        "zone_label_raw",
        "relation_type",
        "intersection_area_m2",
        "source_document_id",
        "source_archive_sha256",
    }
    missing_zones = sorted(zone_required.difference(zones.columns))
    missing_relations = sorted(relation_required.difference(intersections.columns))
    if missing_zones:
        raise PlanningRegulationStructureError(
            f"Zone catalog is missing required columns: {missing_zones}"
        )
    if missing_relations:
        raise PlanningRegulationStructureError(
            f"Zoning intersections are missing required columns: {missing_relations}"
        )
    zone_copy = zones.copy(deep=True)
    relation_copy = intersections.copy(deep=True)
    _validate_source_label_values(zone_copy["planning_zone_id"], "planning zone ID")
    _validate_source_label_values(zone_copy["zone_label_raw"], "zone label")
    if zone_copy["planning_zone_id"].duplicated().any():
        raise PlanningRegulationStructureError("Planning zone IDs must be unique")
    for column in ("source_document_id", "source_archive_sha256"):
        _validate_source_label_values(zone_copy[column], f"zone {column}")
    if not zone_copy["source_document_id"].eq(index.document_id).all():
        raise PlanningRegulationStructureError("Zone document lineage differs from index")
    if not zone_copy["source_archive_sha256"].eq(index.archive_sha256).all():
        raise PlanningRegulationStructureError("Zone archive lineage differs from index")
    for column in ("parcel_id", "planning_zone_id", "source_zone_id", "zone_label_raw"):
        _validate_source_label_values(relation_copy[column], f"intersection {column}")
    if relation_copy.duplicated(["parcel_id", "planning_zone_id"]).any():
        raise PlanningRegulationStructureError(
            "Parcel/zone intersection pairs must be unique"
        )
    known = set(zone_copy["planning_zone_id"].tolist())
    if not set(relation_copy["planning_zone_id"].tolist()).issubset(known):
        raise PlanningRegulationStructureError(
            "Zoning intersections reference an unknown planning zone"
        )
    label_by_id = zone_copy.set_index("planning_zone_id")["zone_label_raw"]
    expected_labels = relation_copy["planning_zone_id"].map(label_by_id)
    if not expected_labels.eq(relation_copy["zone_label_raw"]).all():
        raise PlanningRegulationStructureError(
            "Intersection zone labels differ from the zone catalog"
        )
    if not relation_copy["source_document_id"].eq(index.document_id).all():
        raise PlanningRegulationStructureError(
            "Intersection document lineage differs from index"
        )
    if not relation_copy["source_archive_sha256"].eq(index.archive_sha256).all():
        raise PlanningRegulationStructureError(
            "Intersection archive lineage differs from index"
        )
    allowed_relations = {"AREA_OVERLAP", "TOUCH_ONLY"}
    if not set(relation_copy["relation_type"].tolist()).issubset(allowed_relations):
        raise PlanningRegulationStructureError("Zoning relation type is invalid")
    metrics: list[float] = []
    for value in relation_copy["intersection_area_m2"].tolist():
        if isinstance(value, bool) or not isinstance(value, Real):
            raise PlanningRegulationStructureError(
                "Intersection areas must be numeric"
            )
        try:
            numeric = float(value)
        except (TypeError, ValueError, OverflowError) as error:
            raise PlanningRegulationStructureError(
                "Intersection areas must be finite"
            ) from error
        if not math.isfinite(numeric) or numeric < 0:
            raise PlanningRegulationStructureError(
                "Intersection areas must be finite and non-negative"
            )
        metrics.append(numeric)
    relation_copy["intersection_area_m2"] = pd.Series(
        metrics, index=relation_copy.index, dtype="float64"
    )
    positive = relation_copy["intersection_area_m2"].gt(0)
    if not relation_copy.loc[positive, "relation_type"].eq("AREA_OVERLAP").all():
        raise PlanningRegulationStructureError("Positive zoning relations must be AREA_OVERLAP")
    if not relation_copy.loc[~positive, "relation_type"].eq("TOUCH_ONLY").all():
        raise PlanningRegulationStructureError("Zero-area zoning relations must be TOUCH_ONLY")
    return zone_copy, relation_copy


def _resolved_alias(label: str, aliases: Mapping[str, str]) -> str | None:
    if label not in aliases:
        return None
    current = label
    visited: set[str] = set()
    while current in aliases:
        if current in visited:
            raise PlanningRegulationStructureError("Zone alias cycle is invalid")
        visited.add(current)
        current = aliases[current]
    return current


def _dominant_counts(intersections: pd.DataFrame) -> Counter[str]:
    positive = intersections.loc[
        intersections["intersection_area_m2"].gt(0),
        ["parcel_id", "planning_zone_id", "zone_label_raw", "intersection_area_m2"],
    ].copy()
    if positive.empty:
        return Counter()
    positive = positive.sort_values(
        ["parcel_id", "intersection_area_m2", "planning_zone_id"],
        ascending=[True, False, True],
        kind="mergesort",
    )
    selected = positive.drop_duplicates("parcel_id", keep="first")
    return Counter(selected["zone_label_raw"].tolist())


def _build_zone_mapping(
    index: PlanningRegulationIndex,
    config: PlanningRegulationStructureConfig,
    sections: pd.DataFrame,
    zones: pd.DataFrame,
    intersections: pd.DataFrame,
) -> pd.DataFrame:
    chapters = sections.loc[
        sections["section_type"].eq("ZONE_CHAPTER"),
        ["section_id", "zone_chapter_label"],
    ]
    chapters_by_label: dict[str, list[str]] = {}
    for row in chapters.to_dict("records"):
        label = _strict_string(row["zone_chapter_label"], "zone chapter label")
        chapters_by_label.setdefault(label, []).append(row["section_id"])
    zone_counts = Counter(zones["zone_label_raw"].tolist())
    parcel_counts = intersections.groupby("zone_label_raw", sort=False)["parcel_id"].nunique().to_dict()
    intersection_counts = Counter(intersections["zone_label_raw"].tolist())
    dominant_counts = _dominant_counts(intersections)
    rows: list[dict[str, object]] = []
    for label in sorted(zone_counts):
        exact_sections = chapters_by_label.get(label, [])
        resolved: str | None = None
        matched: str | None = None
        if len(exact_sections) == 1:
            status = "EXACT"
            method = "EXACT_HEADING"
            resolved = label
            matched = exact_sections[0]
        elif len(exact_sections) > 1:
            status = "AMBIGUOUS"
            method = "AMBIGUOUS"
        else:
            alias_target = _resolved_alias(label, config.zone_aliases)
            alias_sections = chapters_by_label.get(alias_target or "", [])
            if alias_target is not None and len(alias_sections) == 1:
                status = "CONFIG_ALIAS"
                method = "CONFIG_ALIAS"
                resolved = alias_target
                matched = alias_sections[0]
            elif alias_target is not None and len(alias_sections) > 1:
                status = "AMBIGUOUS"
                method = "AMBIGUOUS"
                resolved = alias_target
            else:
                status = "UNMAPPED"
                method = "NONE"
                resolved = alias_target
        rows.append(
            {
                "source_zone_label_raw": label,
                "resolved_zone_chapter_label": resolved,
                "mapping_status": status,
                "mapping_method": method,
                "matched_section_id": matched,
                "zone_polygon_count": zone_counts[label],
                "candidate_parcel_count": int(parcel_counts.get(label, 0)),
                "candidate_intersection_count": intersection_counts[label],
                "dominant_candidate_count": dominant_counts[label],
                "document_id": index.document_id,
                "archive_sha256": index.archive_sha256,
                "pdf_sha256": index.pdf_sha256,
                "index_content_sha256": index.index_content_sha256,
                "structure_profile": config.structure_profile,
            }
        )
    frame = pd.DataFrame(rows, columns=ZONE_MAPPING_COLUMNS)
    for column in (
        "zone_polygon_count",
        "candidate_parcel_count",
        "candidate_intersection_count",
        "dominant_candidate_count",
    ):
        frame[column] = frame[column].astype("int64")
    unresolved_dominant = frame.loc[
        frame["dominant_candidate_count"].gt(0)
        & ~frame["mapping_status"].isin({"EXACT", "CONFIG_ALIAS"}),
        "source_zone_label_raw",
    ].tolist()
    if unresolved_dominant:
        raise PlanningRegulationStructureError(
            "Dominant candidate zone labels lack an exact configured chapter mapping: "
            f"{unresolved_dominant}"
        )
    return frame


def _build_topic_evidence(
    index: PlanningRegulationIndex,
    config: PlanningRegulationStructureConfig,
    builds: Sequence[_SectionBuild],
) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    context_characters = config.topic_context_characters
    for topic, terms in config.topics.items():
        for search_term in terms:
            normalized_term = _normalize_search_text(search_term)
            pattern = re.compile(re.escape(normalized_term))
            for build in builds:
                section = build.row
                for page_number, raw_fragment in build.page_fragments:
                    normalized, spans = _normalize_search_text_with_mapping(raw_fragment)
                    matches = list(pattern.finditer(normalized))
                    if not matches:
                        continue
                    first = matches[0]
                    context_start = max(0, first.start() - context_characters)
                    context_end = min(len(normalized), first.end() + context_characters)
                    zone_label = section["zone_chapter_label"]
                    rows.append(
                        {
                            "topic": topic,
                            "search_term": search_term,
                            "normalized_search_term": normalized_term,
                            "section_id": section["section_id"],
                            "evidence_scope": (
                                "ZONE_SPECIFIC_RULE"
                                if zone_label is not None
                                else "GENERAL_RULE"
                            ),
                            "zone_chapter_label": zone_label,
                            "article_number_raw": section["article_number_raw"],
                            "page_number": page_number,
                            "occurrence_count": len(matches),
                            "raw_context": _raw_context(
                                raw_fragment, spans, context_start, context_end
                            ),
                            "normalized_context": normalized[context_start:context_end],
                            "document_id": index.document_id,
                            "archive_sha256": index.archive_sha256,
                            "pdf_sha256": index.pdf_sha256,
                            "index_content_sha256": index.index_content_sha256,
                            "structure_profile": config.structure_profile,
                        }
                    )
    if not rows:
        return pd.DataFrame(
            {
                column: pd.Series(
                    dtype=(
                        "int64"
                        if column in {"page_number", "occurrence_count"}
                        else "object"
                    )
                )
                for column in TOPIC_EVIDENCE_COLUMNS
            }
        )
    frame = pd.DataFrame(rows, columns=TOPIC_EVIDENCE_COLUMNS)
    frame["page_number"] = frame["page_number"].astype("int64")
    frame["occurrence_count"] = frame["occurrence_count"].astype("int64")
    return frame


def _frame_hash(
    domain: str,
    result: PlanningRegulationStructureResult,
    frame: pd.DataFrame,
    columns: Sequence[str],
) -> str:
    return _canonical_sha256(
        {
            "domain": domain,
            "section_hash_schema_version": result.section_hash_schema_version,
            "document_id": result.document_id,
            "archive_sha256": result.archive_sha256,
            "pdf_sha256": result.pdf_sha256,
            "index_content_sha256": result.index_content_sha256,
            "structure_profile": result.structure_profile,
            "structure_config_sha256": result.structure_config_sha256,
            "rows": frame.loc[:, columns].to_dict("records"),
        }
    )


def _result_with_hashes(result: PlanningRegulationStructureResult) -> PlanningRegulationStructureResult:
    return replace(
        result,
        sections_content_sha256=_frame_hash(
            "landscout.planning_regulation.sections",
            result,
            result.sections,
            SECTION_COLUMNS,
        ),
        zone_map_content_sha256=_frame_hash(
            "landscout.planning_regulation.zone_map",
            result,
            result.zone_mapping,
            ZONE_MAPPING_COLUMNS,
        ),
        topic_evidence_content_sha256=_frame_hash(
            "landscout.planning_regulation.topic_evidence",
            result,
            result.topic_evidence,
            TOPIC_EVIDENCE_COLUMNS,
        ),
    )


def _page_tuple(value: object) -> tuple[int, ...]:
    if not isinstance(value, (tuple, list, np.ndarray)):
        raise PlanningRegulationStructureError("Section page_numbers must be a sequence")
    return tuple(_strict_positive_integer(item, "section page number") for item in value)


def _validate_sections(
    index: PlanningRegulationIndex,
    result: PlanningRegulationStructureResult,
) -> None:
    frame = result.sections
    if not isinstance(frame, pd.DataFrame) or tuple(frame.columns) != SECTION_COLUMNS:
        raise PlanningRegulationStructureError("Section schema is not deterministic")
    if frame.empty:
        raise PlanningRegulationStructureError("Regulation sections must not be empty")
    known_pages = set(index.pages["page_number"].tolist())
    ids: list[str] = []
    previous_start = 0
    parents: dict[str, str] = {}
    for row in frame.to_dict("records"):
        section_id = _strict_string(row["section_id"], "section ID")
        ids.append(section_id)
        section_type = _strict_string(row["section_type"], "section type")
        if section_type not in _SECTION_TYPES:
            raise PlanningRegulationStructureError("Section type is invalid")
        for column in ("heading_raw", "heading_normalized", "raw_text", "normalized_text"):
            if not isinstance(row[column], str):
                raise PlanningRegulationStructureError(f"Section {column} must be a string")
        if row["heading_normalized"] != _normalize_search_text(row["heading_raw"]):
            raise PlanningRegulationStructureError("Section heading normalization differs")
        if row["normalized_text"] != _normalize_search_text(row["raw_text"]):
            raise PlanningRegulationStructureError("Section text normalization differs")
        if _strict_nonnegative_integer(row["character_count"], "character count") != len(row["raw_text"]):
            raise PlanningRegulationStructureError("Section character count differs")
        pages = _page_tuple(row["page_numbers"])
        if not pages or tuple(dict.fromkeys(pages)) != pages or not set(pages).issubset(known_pages):
            raise PlanningRegulationStructureError("Section page references are invalid")
        start = _strict_positive_integer(row["start_page"], "section start page")
        end = _strict_positive_integer(row["end_page"], "section end page")
        if start != pages[0] or end != pages[-1] or end < start or start < previous_start:
            raise PlanningRegulationStructureError("Section page range is invalid or unordered")
        previous_start = start
        for column, actual in (
            ("document_id", result.document_id),
            ("archive_sha256", result.archive_sha256),
            ("pdf_sha256", result.pdf_sha256),
            ("index_content_sha256", result.index_content_sha256),
            ("structure_profile", result.structure_profile),
        ):
            if row[column] != actual:
                raise PlanningRegulationStructureError("Section lineage differs")
        expected_hash = _section_content_sha256(row)
        if _validated_sha256(row["section_content_sha256"], "section content SHA256") != expected_hash:
            raise PlanningRegulationStructureError("Section content hash differs")
        parent = row["parent_section_id"]
        if parent is not None and not bool(pd.isna(parent)):
            parents[section_id] = _strict_string(parent, "parent section ID")
        if section_type in {"ZONE_CHAPTER", "ARTICLE"}:
            _strict_string(row["zone_chapter_label"], "zone chapter label")
        elif row["zone_chapter_label"] is not None and not bool(pd.isna(row["zone_chapter_label"])):
            raise PlanningRegulationStructureError("Non-zone section has a zone label")
    if len(set(ids)) != len(ids):
        raise PlanningRegulationStructureError("Section IDs must be unique")
    type_by_id = dict(zip(ids, frame["section_type"].tolist(), strict=True))
    for section_id, parent in parents.items():
        if parent not in type_by_id or type_by_id[parent] != "ZONE_CHAPTER":
            raise PlanningRegulationStructureError("Article parent section is invalid")
        section_type = type_by_id[section_id]
        if section_type != "ARTICLE":
            raise PlanningRegulationStructureError("Only articles may have a parent section")


def _validate_zone_mapping(result: PlanningRegulationStructureResult) -> None:
    frame = result.zone_mapping
    if not isinstance(frame, pd.DataFrame) or tuple(frame.columns) != ZONE_MAPPING_COLUMNS:
        raise PlanningRegulationStructureError("Zone mapping schema is not deterministic")
    labels: list[str] = []
    section_ids = set(result.sections["section_id"].tolist())
    for row in frame.to_dict("records"):
        label = _strict_string(row["source_zone_label_raw"], "source zone label")
        labels.append(label)
        status = _strict_string(row["mapping_status"], "mapping status")
        method = _strict_string(row["mapping_method"], "mapping method")
        if status not in _MAPPING_STATUSES or method not in _MAPPING_METHODS:
            raise PlanningRegulationStructureError("Zone mapping status or method is invalid")
        for column in (
            "zone_polygon_count",
            "candidate_parcel_count",
            "candidate_intersection_count",
            "dominant_candidate_count",
        ):
            count = _strict_nonnegative_integer(row[column], column)
            if column == "zone_polygon_count" and count == 0:
                raise PlanningRegulationStructureError("Zone polygon count must be positive")
        matched = row["matched_section_id"]
        if status in {"EXACT", "CONFIG_ALIAS"}:
            if _strict_string(matched, "matched section ID") not in section_ids:
                raise PlanningRegulationStructureError("Zone mapping section is unknown")
            _strict_string(row["resolved_zone_chapter_label"], "resolved chapter label")
        elif matched is not None and not bool(pd.isna(matched)):
            raise PlanningRegulationStructureError("Unresolved zone mapping has a section ID")
        if row["dominant_candidate_count"] > 0 and status not in {"EXACT", "CONFIG_ALIAS"}:
            raise PlanningRegulationStructureError("Dominant candidate zone is unresolved")
        for column, actual in (
            ("document_id", result.document_id),
            ("archive_sha256", result.archive_sha256),
            ("pdf_sha256", result.pdf_sha256),
            ("index_content_sha256", result.index_content_sha256),
            ("structure_profile", result.structure_profile),
        ):
            if row[column] != actual:
                raise PlanningRegulationStructureError("Zone mapping lineage differs")
    if labels != sorted(labels) or len(set(labels)) != len(labels):
        raise PlanningRegulationStructureError("Zone mappings must be unique and sorted")


def _validate_topic_evidence(
    index: PlanningRegulationIndex,
    result: PlanningRegulationStructureResult,
) -> None:
    frame = result.topic_evidence
    if not isinstance(frame, pd.DataFrame) or tuple(frame.columns) != TOPIC_EVIDENCE_COLUMNS:
        raise PlanningRegulationStructureError("Topic evidence schema is not deterministic")
    sections = result.sections.set_index("section_id", drop=False)
    page_set = set(index.pages["page_number"].tolist())
    keys: set[tuple[str, str, str, int]] = set()
    for row in frame.to_dict("records"):
        topic = _strict_string(row["topic"], "topic")
        term = _strict_string(row["search_term"], "search term")
        normalized = _strict_string(row["normalized_search_term"], "normalized search term")
        if normalized != _normalize_search_text(term):
            raise PlanningRegulationStructureError("Topic search normalization differs")
        section_id = _strict_string(row["section_id"], "topic section ID")
        if section_id not in sections.index:
            raise PlanningRegulationStructureError("Topic evidence references an unknown section")
        page = _strict_positive_integer(row["page_number"], "topic page number")
        if page not in page_set or page not in _page_tuple(sections.at[section_id, "page_numbers"]):
            raise PlanningRegulationStructureError("Topic evidence references an unknown page")
        count = _strict_positive_integer(row["occurrence_count"], "topic occurrence count")
        if count < 1:
            raise PlanningRegulationStructureError("Topic occurrence count is invalid")
        if not isinstance(row["raw_context"], str) or not isinstance(row["normalized_context"], str):
            raise PlanningRegulationStructureError("Topic contexts must be strings")
        scope = _strict_string(row["evidence_scope"], "evidence scope")
        if scope not in _EVIDENCE_SCOPES:
            raise PlanningRegulationStructureError("Evidence scope is invalid")
        key = (topic, normalized, section_id, page)
        if key in keys:
            raise PlanningRegulationStructureError("Topic evidence row is duplicated")
        keys.add(key)
        for column, actual in (
            ("document_id", result.document_id),
            ("archive_sha256", result.archive_sha256),
            ("pdf_sha256", result.pdf_sha256),
            ("index_content_sha256", result.index_content_sha256),
            ("structure_profile", result.structure_profile),
        ):
            if row[column] != actual:
                raise PlanningRegulationStructureError("Topic evidence lineage differs")


def _validate_result(
    index: PlanningRegulationIndex,
    result: PlanningRegulationStructureResult,
) -> None:
    validate_planning_regulation_index(index)
    if not isinstance(result, PlanningRegulationStructureResult):
        raise PlanningRegulationStructureError(
            "result must be a PlanningRegulationStructureResult"
        )
    for value, label in (
        (result.document_id, "document ID"),
        (result.archive_sha256, "archive SHA256"),
        (result.pdf_sha256, "PDF SHA256"),
        (result.index_content_sha256, "index content SHA256"),
        (result.structure_profile, "structure profile"),
    ):
        _strict_string(value, label)
    if (
        result.document_id != index.document_id
        or result.archive_sha256 != index.archive_sha256
        or result.pdf_sha256 != index.pdf_sha256
        or result.index_content_sha256 != index.index_content_sha256
    ):
        raise PlanningRegulationStructureError("Structure result lineage differs from index")
    _validated_sha256(result.archive_sha256, "archive SHA256")
    _validated_sha256(result.pdf_sha256, "PDF SHA256")
    _validated_sha256(result.index_content_sha256, "index content SHA256")
    _validated_sha256(result.structure_config_sha256, "structure config SHA256")
    schema = _strict_positive_integer(
        result.section_hash_schema_version, "section hash schema version"
    )
    if schema != SECTION_HASH_SCHEMA_VERSION:
        raise PlanningRegulationStructureError("Unsupported section hash schema version")
    _validate_sections(index, result)
    _validate_zone_mapping(result)
    _validate_topic_evidence(index, result)
    expected = _result_with_hashes(replace(
        result,
        sections_content_sha256="",
        zone_map_content_sha256="",
        topic_evidence_content_sha256="",
    ))
    for actual, wanted, label in (
        (result.sections_content_sha256, expected.sections_content_sha256, "sections"),
        (result.zone_map_content_sha256, expected.zone_map_content_sha256, "zone map"),
        (
            result.topic_evidence_content_sha256,
            expected.topic_evidence_content_sha256,
            "topic evidence",
        ),
    ):
        if _validated_sha256(actual, f"{label} content SHA256") != wanted:
            raise PlanningRegulationStructureError(f"{label} content hash differs")


def validate_planning_regulation_structure(
    index: PlanningRegulationIndex,
    result: PlanningRegulationStructureResult,
) -> None:
    """Validate source lineage, schemas, references, and all result hashes."""

    try:
        _validate_result(index, result)
    except PlanningRegulationStructureError:
        raise
    except Exception as error:
        raise PlanningRegulationStructureError(
            "Planning regulation structure validation failed safely"
        ) from error


def structure_planning_regulation(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
    zoning_intersections: pd.DataFrame,
    config: PlanningRegulationStructureConfig | str | Path,
) -> PlanningRegulationStructureResult:
    """Build source-locked sections, exact zone mappings, and literal topic evidence."""

    try:
        resolved_config = (
            config
            if isinstance(config, PlanningRegulationStructureConfig)
            else load_planning_regulation_structure_config(config)
        )
        _validate_document_lock(index, resolved_config)
        zones_copy, intersections_copy = _validated_zoning_inputs(
            index, zones, zoning_intersections
        )
        sections, builds = _build_sections(index, resolved_config)
        zone_mapping = _build_zone_mapping(
            index,
            resolved_config,
            sections,
            zones_copy,
            intersections_copy,
        )
        topic_evidence = _build_topic_evidence(index, resolved_config, builds)
        result = PlanningRegulationStructureResult(
            document_id=index.document_id,
            archive_sha256=index.archive_sha256,
            pdf_sha256=index.pdf_sha256,
            index_content_sha256=index.index_content_sha256,
            structure_profile=resolved_config.structure_profile,
            structure_config_sha256=_config_sha256(resolved_config),
            section_hash_schema_version=SECTION_HASH_SCHEMA_VERSION,
            sections_content_sha256="",
            zone_map_content_sha256="",
            topic_evidence_content_sha256="",
            sections=sections,
            zone_mapping=zone_mapping,
            topic_evidence=topic_evidence,
        )
        result = _result_with_hashes(result)
        validate_planning_regulation_structure(index, result)
        return result
    except PlanningRegulationStructureError:
        raise
    except Exception as error:
        raise PlanningRegulationStructureError(
            "Planning regulation structure could not be built safely"
        ) from error

"""Structure a validated planning regulation into factual, auditable evidence."""

from __future__ import annotations

import json
import math
import re
from collections import Counter
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, replace
from hashlib import sha256
from itertools import pairwise
from numbers import Integral, Real
from pathlib import Path
from typing import Literal

import numpy as np
import pandas as pd  # type: ignore[import-untyped]
import yaml  # type: ignore[import-untyped]
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictInt,
    StrictStr,
    model_validator,
)

from landscout.common.planning_text import (
    normalize_planning_search_text,
    normalize_planning_search_text_with_mapping,
    raw_context_from_spans,
)
from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    validate_planning_regulation_index,
)
from landscout.stages.planning_overlay import technical_overlay_tolerance

_normalize_search_text = normalize_planning_search_text
_normalize_search_text_with_mapping = normalize_planning_search_text_with_mapping
_raw_context = raw_context_from_spans

__all__ = [
    "PlanningRegulationStructureConfig",
    "PlanningRegulationStructureError",
    "PlanningRegulationStructureResult",
    "load_planning_regulation_structure_config",
    "planning_regulation_section_page_fragments",
    "structure_planning_regulation",
    "validate_planning_regulation_structure",
]

SECTION_HASH_SCHEMA_VERSION = 3
STRUCTURE_MANIFEST_SCHEMA_VERSION = 4
_SUPPORTED_CONFIG_SCHEMA_VERSION = 2

_SECTION_TYPES = frozenset({"GENERAL", "ZONE_CHAPTER", "ARTICLE", "OTHER"})
_MAPPING_STATUSES = frozenset({"EXACT", "CONFIG_ALIAS", "UNMAPPED", "AMBIGUOUS"})
_MAPPING_METHODS = frozenset({"EXACT_HEADING", "CONFIG_ALIAS", "NONE", "AMBIGUOUS"})
_EVIDENCE_SCOPES = frozenset(
    {"GENERAL_RULE", "ZONE_SPECIFIC_RULE", "OTHER_TEXT"}
)

_ZONE_INPUT_COLUMNS = (
    "planning_zone_id",
    "source_zone_id",
    "zone_label_raw",
    "source_document_id",
    "source_archive_sha256",
)
_REQUIRED_INTERSECTION_INPUT_COLUMNS = (
    "parcel_id",
    "planning_zone_id",
    "source_zone_id",
    "zone_label_raw",
    "relation_type",
    "intersection_area_m2",
    "source_document_id",
    "source_archive_sha256",
)
_OPTIONAL_INTERSECTION_INPUT_COLUMNS = (
    "parcel_metric_area_m2",
    "zone_area_m2",
)

SECTION_COLUMNS = (
    "section_id",
    "parent_section_id",
    "section_type",
    "heading_raw",
    "heading_normalized",
    "zone_chapter_label",
    "article_number_raw",
    "article_title_raw",
    "start_record_id",
    "end_record_id",
    "source_record_count",
    "source_records_sha256",
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
    "match_policy",
    "section_id",
    "evidence_scope",
    "zone_chapter_label",
    "article_number_raw",
    "page_number",
    "occurrence_count",
    "first_match_normalized_start",
    "first_match_normalized_end",
    "first_match_raw_start",
    "first_match_raw_end",
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
    include_table_of_contents_in_topic_evidence: StrictBool = False

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
    continuation: tuple[StrictStr, ...] = ()


class IgnoredPatternsConfig(_StrictConfigModel):
    page_headers: tuple[StrictStr, ...] = ()
    page_footers: tuple[StrictStr, ...] = ()


class TopicMatchPolicyConfig(_StrictConfigModel):
    boundary_mode: Literal["token"]
    overlap_resolution: Literal["longest_match"]

    @property
    def identifier(self) -> str:
        return f"{self.boundary_mode}_{self.overlap_resolution}"


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
    topic_match_policy: TopicMatchPolicyConfig
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
        structural_pattern_owners: dict[str, str] = {}
        for category, patterns in (
            ("ZONE_CHAPTER", self.heading_patterns.zone_chapter),
            ("GENERAL", self.heading_patterns.general_section),
            ("ARTICLE", self.heading_patterns.article),
        ):
            for pattern in patterns:
                previous = structural_pattern_owners.get(pattern)
                if previous is not None:
                    raise ValueError(
                        "identical structural heading regex is reused across "
                        f"groups {previous} and {category}"
                    )
                structural_pattern_owners[pattern] = category
        required_captures = (
            (self.heading_patterns.zone_chapter, {"label"}, "zone chapter"),
            (
                self.heading_patterns.article,
                {"zone", "number", "title"},
                "zone article",
            ),
            (
                self.heading_patterns.general_section,
                {"number", "title"},
                "general section",
            ),
        )
        for patterns, required, label in required_captures:
            for pattern in patterns:
                missing = required.difference(re.compile(pattern).groupindex)
                if missing:
                    raise ValueError(
                        f"{label} pattern lacks named captures: {sorted(missing)}"
                    )
        for alias, target in self.zone_aliases.items():
            _exact_config_string(alias, "zone alias")
            _exact_config_string(target, "zone alias target")
        _validate_alias_cycles(self.zone_aliases)
        if not self.topics:
            raise ValueError("topics must not be empty")
        for topic in sorted(self.topics):
            terms = self.topics[topic]
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
    structure_config_schema_version: int
    structure_config_sha256: str
    zones_content_sha256: str
    zoning_intersection_hash_columns: tuple[str, ...]
    zoning_intersections_content_sha256: str
    source_records_sha256: str
    section_hash_schema_version: int
    sections_content_sha256: str
    zone_map_content_sha256: str
    topic_evidence_content_sha256: str
    structure_result_content_sha256: str
    sections: pd.DataFrame
    zone_mapping: pd.DataFrame
    topic_evidence: pd.DataFrame


@dataclass(frozen=True)
class _LineRecord:
    record_id: str
    page_number: int
    page_line_number: int
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
class _StructuralHeadingMatch:
    section_type: Literal["GENERAL", "ZONE_CHAPTER", "ARTICLE"]
    pattern_index: int
    named_captures: tuple[tuple[str, str | None], ...]


@dataclass(frozen=True)
class _SectionBoundary:
    record_position: int
    event: _HeadingEvent | None
    forced_table_of_contents: bool


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
    payload = config.model_dump(mode="json")
    payload["topics"] = {
        topic: list(config.topics[topic]) for topic in sorted(config.topics)
    }
    return _canonical_sha256(
        {
            "domain": "landscout.planning_regulation.structure_config",
            "config": payload,
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
    indexed_pages = tuple(
        _strict_positive_integer(value, "indexed page number")
        for value in index.pages["page_number"].tolist()
    )
    indexed_page_set = set(indexed_pages)
    if config.document_layout.body_start_page not in indexed_page_set:
        raise PlanningRegulationStructureError(
            "body_start_page must reference a real indexed page"
        )
    missing_toc_pages = sorted(
        set(config.document_layout.table_of_contents_pages).difference(
            indexed_page_set
        )
    )
    if missing_toc_pages:
        raise PlanningRegulationStructureError(
            "table_of_contents_pages reference nonexistent indexed pages: "
            f"{missing_toc_pages}"
        )


def _compiled(patterns: Sequence[str]) -> tuple[re.Pattern[str], ...]:
    return tuple(re.compile(pattern) for pattern in patterns)


def _matches_any(value: str, patterns: Sequence[re.Pattern[str]]) -> bool:
    return any(pattern.fullmatch(value) is not None for pattern in patterns)


def _retained_page_lines(
    raw_text: str,
    headers: Sequence[re.Pattern[str]],
    footers: Sequence[re.Pattern[str]],
) -> list[tuple[int, str]]:
    lines = list(enumerate(raw_text.splitlines(), start=1))
    start = 0
    first_nonempty = next(
        (position for position, (_, line) in enumerate(lines) if line.strip()),
        None,
    )
    if (
        first_nonempty is not None
        and _matches_any(lines[first_nonempty][1].strip(), headers)
    ):
        cursor = first_nonempty
        while cursor < len(lines):
            comparable = lines[cursor][1].strip()
            if not comparable or _matches_any(comparable, headers):
                cursor += 1
                continue
            break
        start = cursor
    end = len(lines)
    last_nonempty = next(
        (
            position
            for position in range(len(lines) - 1, start - 1, -1)
            if lines[position][1].strip()
        ),
        None,
    )
    if (
        last_nonempty is not None
        and _matches_any(lines[last_nonempty][1].strip(), footers)
    ):
        cursor = last_nonempty
        while cursor >= start:
            comparable = lines[cursor][1].strip()
            if not comparable or _matches_any(comparable, footers):
                cursor -= 1
                continue
            break
        end = cursor + 1
    return lines[start:end]


def _line_records(
    index: PlanningRegulationIndex,
    config: PlanningRegulationStructureConfig,
) -> list[_LineRecord]:
    headers = _compiled(config.ignored_patterns.page_headers)
    footers = _compiled(config.ignored_patterns.page_footers)
    retained: list[tuple[int, int, str]] = []
    for page in index.pages.to_dict("records"):
        page_number = _strict_positive_integer(page["page_number"], "page number")
        raw_text = page["raw_text"]
        if not isinstance(raw_text, str):
            raise PlanningRegulationStructureError("Page raw text must be a string")
        retained.extend(
            (page_number, line_number, raw_line)
            for line_number, raw_line in _retained_page_lines(
                raw_text, headers, footers
            )
        )
    records = [
        _LineRecord(
            record_id=f"RECORD-{position:06d}",
            page_number=page_number,
            page_line_number=line_number,
            raw=raw_line,
        )
        for position, (page_number, line_number, raw_line) in enumerate(
            retained, start=1
        )
    ]
    if not records:
        raise PlanningRegulationStructureError("Regulation contains no structural text")
    return records


def _source_record_payload(record: _LineRecord) -> dict[str, object]:
    return {
        "record_id": record.record_id,
        "page_number": record.page_number,
        "page_line_number": record.page_line_number,
        "raw_text": record.raw,
    }


def _source_records_sha256(records: Sequence[_LineRecord]) -> str:
    return _canonical_sha256(
        {
            "domain": "landscout.planning_regulation.source_records",
            "section_hash_schema_version": SECTION_HASH_SCHEMA_VERSION,
            "records": [_source_record_payload(record) for record in records],
        }
    )


def _canonical_chapter_label(value: str) -> str:
    label = re.sub(r"\s+", "", value)
    return _strict_string(label, "zone chapter label")


def _classify_structural_heading(
    record: _LineRecord,
    value: str,
    pattern_groups: Sequence[
        tuple[
            Literal["GENERAL", "ZONE_CHAPTER", "ARTICLE"],
            Sequence[re.Pattern[str]],
        ]
    ],
) -> _StructuralHeadingMatch | None:
    matches: list[_StructuralHeadingMatch] = []
    for section_type, patterns in pattern_groups:
        for pattern_index, pattern in enumerate(patterns):
            match = pattern.fullmatch(value)
            if match is None:
                continue
            matches.append(
                _StructuralHeadingMatch(
                    section_type=section_type,
                    pattern_index=pattern_index,
                    named_captures=tuple(match.groupdict().items()),
                )
            )
    if len(matches) > 1:
        diagnostics = ", ".join(
            f"{match.section_type}[{match.pattern_index}]" for match in matches
        )
        raise PlanningRegulationStructureError(
            "Ambiguous structural heading at "
            f"{record.record_id}, page {record.page_number}, "
            f"line {record.page_line_number}: {diagnostics}"
        )
    return matches[0] if matches else None


def _heading_events(
    records: Sequence[_LineRecord],
    config: PlanningRegulationStructureConfig,
) -> list[_HeadingEvent]:
    zones = _compiled(config.heading_patterns.zone_chapter)
    articles = _compiled(config.heading_patterns.article)
    generals = _compiled(config.heading_patterns.general_section)
    continuations = _compiled(config.heading_patterns.continuation)
    structural_patterns: tuple[
        tuple[
            Literal["GENERAL", "ZONE_CHAPTER", "ARTICLE"],
            Sequence[re.Pattern[str]],
        ],
        ...,
    ] = (
        ("ZONE_CHAPTER", zones),
        ("GENERAL", generals),
        ("ARTICLE", articles),
    )
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
        structural_match = _classify_structural_heading(
            record,
            comparable,
            structural_patterns,
        )
        if structural_match is None:
            position += 1
            continue
        section_type = structural_match.section_type
        groups = dict(structural_match.named_captures)
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
                if not candidate:
                    break
                if (
                    _classify_structural_heading(
                        records[cursor],
                        candidate,
                        structural_patterns,
                    )
                    is not None
                ):
                    break
                if not _matches_any(candidate, continuations):
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


def _contiguous_page_blocks(pages: Sequence[int]) -> tuple[tuple[int, ...], ...]:
    if not pages:
        return ()
    blocks: list[list[int]] = [[pages[0]]]
    for page in pages[1:]:
        if page == blocks[-1][-1] + 1:
            blocks[-1].append(page)
        else:
            blocks.append([page])
    return tuple(tuple(block) for block in blocks)


def _section_starts(
    records: Sequence[_LineRecord],
    events: Sequence[_HeadingEvent],
    config: PlanningRegulationStructureConfig,
) -> list[_SectionBoundary]:
    starts_by_position: dict[int, _SectionBoundary] = {
        event.record_position: _SectionBoundary(
            record_position=event.record_position,
            event=event,
            forced_table_of_contents=False,
        )
        for event in events
    }
    record_positions_by_page: dict[int, list[int]] = {}
    for position, record in enumerate(records):
        record_positions_by_page.setdefault(record.page_number, []).append(position)
    for block in _contiguous_page_blocks(
        config.document_layout.table_of_contents_pages
    ):
        positions = [
            position
            for page in block
            for position in record_positions_by_page.get(page, [])
        ]
        if not positions:
            continue
        block_start = min(positions)
        block_end = max(positions) + 1
        starts_by_position[block_start] = _SectionBoundary(
            record_position=block_start,
            event=None,
            forced_table_of_contents=True,
        )
        if block_end < len(records) and block_end not in starts_by_position:
            starts_by_position[block_end] = _SectionBoundary(
                record_position=block_end,
                event=None,
                forced_table_of_contents=False,
            )
    ordered = sorted(
        starts_by_position.values(),
        key=lambda boundary: boundary.record_position,
    )
    toc_pages = set(config.document_layout.table_of_contents_pages)
    for boundary_index, boundary in enumerate(ordered):
        if boundary.event is None:
            continue
        minimum_position = (
            ordered[boundary_index - 1].record_position
            if boundary_index > 0
            else 0
        )
        shifted_position = boundary.record_position
        while (
            shifted_position > minimum_position
            and not records[shifted_position - 1].raw.strip()
            and records[shifted_position - 1].page_number not in toc_pages
        ):
            shifted_position -= 1
        ordered[boundary_index] = replace(
            boundary,
            record_position=shifted_position,
        )
    compacted: dict[int, _SectionBoundary] = {}
    for boundary in ordered:
        existing = compacted.get(boundary.record_position)
        if (
            existing is None
            or boundary.forced_table_of_contents
            or (
                not existing.forced_table_of_contents
                and boundary.event is not None
            )
        ):
            compacted[boundary.record_position] = boundary
    ordered = sorted(
        compacted.values(),
        key=lambda boundary: boundary.record_position,
    )
    if not ordered:
        raise PlanningRegulationStructureError(
            "No regulation section boundary could be established"
        )
    first_boundary = ordered[0]
    if first_boundary.record_position > 0:
        prefix = records[: first_boundary.record_position]
        if any(record.raw.strip() for record in prefix):
            ordered.insert(
                0,
                _SectionBoundary(
                    record_position=0,
                    event=None,
                    forced_table_of_contents=False,
                ),
            )
        else:
            ordered[0] = replace(first_boundary, record_position=0)
    coalesced: list[_SectionBoundary] = []
    for boundary_index, boundary in enumerate(ordered):
        start = boundary.record_position
        end = (
            ordered[boundary_index + 1].record_position
            if boundary_index + 1 < len(ordered)
            else len(records)
        )
        if (
            not boundary.forced_table_of_contents
            and boundary.event is None
            and not any(record.raw.strip() for record in records[start:end])
        ):
            if boundary_index + 1 < len(ordered):
                ordered[boundary_index + 1] = replace(
                    ordered[boundary_index + 1],
                    record_position=start,
                )
                continue
            if coalesced:
                continue
        coalesced.append(boundary)
    return coalesced


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
) -> tuple[pd.DataFrame, tuple[_SectionBuild, ...], tuple[_LineRecord, ...]]:
    records = _line_records(index, config)
    events = _heading_events(records, config)
    starts = _section_starts(records, events, config)
    builds: list[_SectionBuild] = []
    current_chapter_id: str | None = None
    current_chapter_label: str | None = None
    for start_index, boundary in enumerate(starts):
        start = boundary.record_position
        event = boundary.event
        end = (
            starts[start_index + 1].record_position
            if start_index + 1 < len(starts)
            else len(records)
        )
        segment = records[start:end]
        if not segment:
            continue
        section_id = f"SECTION-{len(builds) + 1:04d}"
        if event is None:
            section_type = "OTHER"
            heading_raw = next(
                (record.raw for record in segment if record.raw.strip()),
                "",
            )
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
            "start_record_id": segment[0].record_id,
            "end_record_id": segment[-1].record_id,
            "source_record_count": len(segment),
            "source_records_sha256": _source_records_sha256(segment),
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
    frame["source_record_count"] = frame["source_record_count"].astype("int64")
    frame["character_count"] = frame["character_count"].astype("int64")
    return frame, tuple(builds), tuple(records)


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
        "source_zone_id",
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
    _validate_source_label_values(zone_copy["source_zone_id"], "source zone ID")
    _validate_source_label_values(zone_copy["zone_label_raw"], "zone label")
    if zone_copy["planning_zone_id"].duplicated().any():
        raise PlanningRegulationStructureError("Planning zone IDs must be unique")
    if zone_copy["source_zone_id"].duplicated().any():
        raise PlanningRegulationStructureError("Source zone IDs must be unique")
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
    catalog_by_id = zone_copy.set_index("planning_zone_id")
    expected_labels = relation_copy["planning_zone_id"].map(
        catalog_by_id["zone_label_raw"]
    )
    if not expected_labels.eq(relation_copy["zone_label_raw"]).all():
        raise PlanningRegulationStructureError(
            "Intersection zone labels differ from the zone catalog"
        )
    expected_source_ids = relation_copy["planning_zone_id"].map(
        catalog_by_id["source_zone_id"]
    )
    if not expected_source_ids.eq(relation_copy["source_zone_id"]).all():
        raise PlanningRegulationStructureError(
            "Intersection source-zone IDs differ from the zone catalog"
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
    for upper_column in ("parcel_metric_area_m2", "zone_area_m2"):
        if upper_column not in relation_copy.columns:
            continue
        for area, upper in zip(
            relation_copy["intersection_area_m2"].tolist(),
            relation_copy[upper_column].tolist(),
            strict=True,
        ):
            if isinstance(upper, bool) or not isinstance(upper, Real):
                raise PlanningRegulationStructureError(
                    f"{upper_column} must be numeric"
                )
            try:
                numeric_upper = float(upper)
            except (TypeError, ValueError, OverflowError) as error:
                raise PlanningRegulationStructureError(
                    f"{upper_column} must be finite"
                ) from error
            if not math.isfinite(numeric_upper) or numeric_upper < 0:
                raise PlanningRegulationStructureError(
                    f"{upper_column} must be finite and non-negative"
                )
            if area - numeric_upper > technical_overlay_tolerance(numeric_upper):
                raise PlanningRegulationStructureError(
                    f"Intersection area exceeds {upper_column}"
                )
    return zone_copy, relation_copy


def _input_frame_sha256(
    domain: str,
    frame: pd.DataFrame,
    columns: Sequence[str],
) -> str:
    return _canonical_sha256(
        {
            "domain": domain,
            "columns": list(columns),
            "rows": frame.loc[:, columns].to_dict("records"),
        }
    )


def _intersection_hash_columns(frame: pd.DataFrame) -> tuple[str, ...]:
    return _REQUIRED_INTERSECTION_INPUT_COLUMNS + tuple(
        column
        for column in _OPTIONAL_INTERSECTION_INPUT_COLUMNS
        if column in frame.columns
    )


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
                resolved = None
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


@dataclass(frozen=True)
class _TopicMatch:
    term_index: int
    search_term: str
    normalized_term: str
    normalized_start: int
    normalized_end: int


def _is_token_character(value: str) -> bool:
    return value.isalnum() or value == "_"


def _literal_topic_matches(
    normalized_text: str,
    terms: Sequence[str],
) -> tuple[_TopicMatch, ...]:
    candidates: list[_TopicMatch] = []
    for term_index, search_term in enumerate(terms):
        normalized_term = _normalize_search_text(search_term)
        cursor = 0
        while True:
            start = normalized_text.find(normalized_term, cursor)
            if start < 0:
                break
            end = start + len(normalized_term)
            left_ok = start == 0 or not _is_token_character(normalized_text[start - 1])
            right_ok = end == len(normalized_text) or not _is_token_character(
                normalized_text[end]
            )
            if left_ok and right_ok:
                candidates.append(
                    _TopicMatch(
                        term_index=term_index,
                        search_term=search_term,
                        normalized_term=normalized_term,
                        normalized_start=start,
                        normalized_end=end,
                    )
                )
            cursor = start + 1
    selected: list[_TopicMatch] = []
    for candidate in sorted(
        candidates,
        key=lambda item: (
            -(item.normalized_end - item.normalized_start),
            item.term_index,
            item.normalized_start,
        ),
    ):
        if any(
            candidate.normalized_start < existing.normalized_end
            and existing.normalized_start < candidate.normalized_end
            for existing in selected
        ):
            continue
        selected.append(candidate)
    return tuple(
        sorted(
            selected,
            key=lambda item: (item.normalized_start, item.term_index),
        )
    )


def _evidence_scope(section_type: str) -> str:
    if section_type == "GENERAL":
        return "GENERAL_RULE"
    if section_type in {"ZONE_CHAPTER", "ARTICLE"}:
        return "ZONE_SPECIFIC_RULE"
    if section_type == "OTHER":
        return "OTHER_TEXT"
    raise PlanningRegulationStructureError(
        "Topic evidence references an unsupported section type"
    )


def _build_topic_evidence(
    index: PlanningRegulationIndex,
    config: PlanningRegulationStructureConfig,
    builds: Sequence[_SectionBuild],
) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    context_characters = config.topic_context_characters
    toc_pages = set(config.document_layout.table_of_contents_pages)
    for topic in sorted(config.topics):
        terms = config.topics[topic]
        for build in builds:
            section = build.row
            for page_number, raw_fragment in build.page_fragments:
                if (
                    page_number in toc_pages
                    and not config.document_layout.include_table_of_contents_in_topic_evidence
                ):
                    continue
                normalized, spans = _normalize_search_text_with_mapping(raw_fragment)
                matches = _literal_topic_matches(normalized, terms)
                by_term: dict[int, list[_TopicMatch]] = {}
                for match in matches:
                    by_term.setdefault(match.term_index, []).append(match)
                for term_index in range(len(terms)):
                    retained = by_term.get(term_index, [])
                    if not retained:
                        continue
                    first = retained[0]
                    context_start = max(
                        0, first.normalized_start - context_characters
                    )
                    context_end = min(
                        len(normalized),
                        first.normalized_end + context_characters,
                    )
                    raw_start = spans[first.normalized_start][0]
                    raw_end = spans[first.normalized_end - 1][1]
                    zone_label = section["zone_chapter_label"]
                    rows.append(
                        {
                            "topic": topic,
                            "search_term": first.search_term,
                            "normalized_search_term": first.normalized_term,
                            "match_policy": config.topic_match_policy.identifier,
                            "section_id": section["section_id"],
                            "evidence_scope": _evidence_scope(
                                str(section["section_type"])
                            ),
                            "zone_chapter_label": zone_label,
                            "article_number_raw": section["article_number_raw"],
                            "page_number": page_number,
                            "occurrence_count": len(retained),
                            "first_match_normalized_start": first.normalized_start,
                            "first_match_normalized_end": first.normalized_end,
                            "first_match_raw_start": raw_start,
                            "first_match_raw_end": raw_end,
                            "raw_context": _raw_context(
                                raw_fragment, spans, context_start, context_end
                            ),
                            "normalized_context": normalized[
                                context_start:context_end
                            ],
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
                        if column
                        in {
                            "page_number",
                            "occurrence_count",
                            "first_match_normalized_start",
                            "first_match_normalized_end",
                            "first_match_raw_start",
                            "first_match_raw_end",
                        }
                        else "object"
                    )
                )
                for column in TOPIC_EVIDENCE_COLUMNS
            }
        )
    frame = pd.DataFrame(rows, columns=TOPIC_EVIDENCE_COLUMNS)
    for column in (
        "page_number",
        "occurrence_count",
        "first_match_normalized_start",
        "first_match_normalized_end",
        "first_match_raw_start",
        "first_match_raw_end",
    ):
        frame[column] = frame[column].astype("int64")
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
            "structure_config_schema_version": result.structure_config_schema_version,
            "structure_config_sha256": result.structure_config_sha256,
            "zones_content_sha256": result.zones_content_sha256,
            "zoning_intersection_hash_columns": list(
                result.zoning_intersection_hash_columns
            ),
            "zoning_intersections_content_sha256": (
                result.zoning_intersections_content_sha256
            ),
            "source_records_sha256": result.source_records_sha256,
            "rows": frame.loc[:, columns].to_dict("records"),
        }
    )


def _structure_result_content_sha256(
    result: PlanningRegulationStructureResult,
) -> str:
    return _canonical_sha256(
        {
            "domain": "landscout.planning_regulation.structure_result",
            "document_id": result.document_id,
            "archive_sha256": result.archive_sha256,
            "pdf_sha256": result.pdf_sha256,
            "index_content_sha256": result.index_content_sha256,
            "structure_profile": result.structure_profile,
            "structure_config_schema_version": result.structure_config_schema_version,
            "structure_config_sha256": result.structure_config_sha256,
            "zones_content_sha256": result.zones_content_sha256,
            "zoning_intersection_hash_columns": list(
                result.zoning_intersection_hash_columns
            ),
            "zoning_intersections_content_sha256": (
                result.zoning_intersections_content_sha256
            ),
            "source_records_sha256": result.source_records_sha256,
            "section_hash_schema_version": result.section_hash_schema_version,
            "sections_content_sha256": result.sections_content_sha256,
            "zone_map_content_sha256": result.zone_map_content_sha256,
            "topic_evidence_content_sha256": result.topic_evidence_content_sha256,
        }
    )


def _result_with_hashes(
    result: PlanningRegulationStructureResult,
) -> PlanningRegulationStructureResult:
    component_result = replace(
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
    return replace(
        component_result,
        structure_result_content_sha256=_structure_result_content_sha256(
            component_result
        ),
    )


def _page_tuple(value: object) -> tuple[int, ...]:
    if not isinstance(value, (tuple, list, np.ndarray)):
        raise PlanningRegulationStructureError("Section page_numbers must be a sequence")
    return tuple(_strict_positive_integer(item, "section page number") for item in value)


def _validate_sections(
    index: PlanningRegulationIndex,
    result: PlanningRegulationStructureResult,
    records: Sequence[_LineRecord],
    config: PlanningRegulationStructureConfig,
) -> None:
    frame = result.sections
    if not isinstance(frame, pd.DataFrame) or tuple(frame.columns) != SECTION_COLUMNS:
        raise PlanningRegulationStructureError("Section schema is not deterministic")
    if frame.empty:
        raise PlanningRegulationStructureError("Regulation sections must not be empty")
    if result.source_records_sha256 != _source_records_sha256(records):
        raise PlanningRegulationStructureError("Retained source-record hash differs")
    known_pages = set(index.pages["page_number"].tolist())
    record_position = {record.record_id: position for position, record in enumerate(records)}
    ids: list[str] = []
    expected_record_start = 0
    parents: dict[str, str] = {}
    zone_by_id: dict[str, str | None] = {}
    for sequence, row in enumerate(frame.to_dict("records"), start=1):
        section_id = _strict_string(row["section_id"], "section ID")
        if section_id != f"SECTION-{sequence:04d}":
            raise PlanningRegulationStructureError(
                "Section IDs must be deterministic and sequential"
            )
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
        start_record_id = _strict_string(row["start_record_id"], "start record ID")
        end_record_id = _strict_string(row["end_record_id"], "end record ID")
        if start_record_id not in record_position or end_record_id not in record_position:
            raise PlanningRegulationStructureError("Section record boundary is unknown")
        start_record = record_position[start_record_id]
        end_record = record_position[end_record_id]
        if start_record != expected_record_start or end_record < start_record:
            raise PlanningRegulationStructureError(
                "Sections do not preserve the exact source-record partition"
            )
        segment = records[start_record : end_record + 1]
        expected_record_start = end_record + 1
        blank_toc_other = (
            section_type == "OTHER"
            and not row["raw_text"].strip()
            and any(
                record.page_number
                in config.document_layout.table_of_contents_pages
                for record in segment
            )
        )
        if not row["raw_text"].strip() and not blank_toc_other:
            raise PlanningRegulationStructureError(
                "Only an explicit TOC OTHER section may contain blank-only text"
            )
        if not row["heading_raw"].strip() and not blank_toc_other:
            raise PlanningRegulationStructureError(
                "Every nonblank section must retain a factual heading"
            )
        if _strict_positive_integer(
            row["source_record_count"], "source record count"
        ) != len(segment):
            raise PlanningRegulationStructureError("Section source-record count differs")
        if _validated_sha256(
            row["source_records_sha256"], "section source-record SHA256"
        ) != _source_records_sha256(segment):
            raise PlanningRegulationStructureError("Section source-record hash differs")
        if row["raw_text"] != "\n".join(record.raw for record in segment):
            raise PlanningRegulationStructureError(
                "Section raw text differs from its retained source records"
            )
        expected_pages = tuple(dict.fromkeys(record.page_number for record in segment))
        pages = _page_tuple(row["page_numbers"])
        if (
            not pages
            or any(right <= left for left, right in pairwise(pages))
            or not set(pages).issubset(known_pages)
            or pages != expected_pages
        ):
            raise PlanningRegulationStructureError("Section page references are invalid")
        start = _strict_positive_integer(row["start_page"], "section start page")
        end = _strict_positive_integer(row["end_page"], "section end page")
        if start != pages[0] or end != pages[-1] or end < start:
            raise PlanningRegulationStructureError("Section page range is invalid or unordered")
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
        zone_value = row["zone_chapter_label"]
        zone_label = (
            None
            if zone_value is None or bool(pd.isna(zone_value))
            else _strict_string(zone_value, "zone chapter label")
        )
        zone_by_id[section_id] = zone_label
        article_number = row["article_number_raw"]
        article_title = row["article_title_raw"]
        if section_type == "ARTICLE":
            if zone_label is None:
                raise PlanningRegulationStructureError("Article zone label is missing")
            _strict_string(article_number, "article number")
            _strict_string(article_title, "article title")
            if section_id not in parents:
                raise PlanningRegulationStructureError("Article parent is missing")
        elif section_type == "GENERAL":
            if zone_label is not None or section_id in parents:
                raise PlanningRegulationStructureError(
                    "General section cannot have a zone label or parent"
                )
            _strict_string(article_number, "general article number")
            _strict_string(article_title, "general article title")
        else:
            if section_id in parents:
                raise PlanningRegulationStructureError(
                    "Zone chapter or OTHER section cannot have a parent"
                )
            if section_type == "ZONE_CHAPTER":
                if zone_label is None:
                    raise PlanningRegulationStructureError(
                        "Zone chapter label is missing"
                    )
            elif zone_label is not None:
                raise PlanningRegulationStructureError(
                    "OTHER section cannot have a zone label"
                )
            for value, label in (
                (article_number, "article number"),
                (article_title, "article title"),
            ):
                if value is not None and not bool(pd.isna(value)):
                    raise PlanningRegulationStructureError(
                        f"{section_type} {label} must be null"
                    )
    if expected_record_start != len(records):
        raise PlanningRegulationStructureError(
            "Retained source records are omitted from the section partition"
        )
    if len(set(ids)) != len(ids):
        raise PlanningRegulationStructureError("Section IDs must be unique")
    type_by_id = dict(zip(ids, frame["section_type"].tolist(), strict=True))
    order_by_id = {section_id: position for position, section_id in enumerate(ids)}
    for section_id, parent in parents.items():
        if parent not in type_by_id or type_by_id[parent] != "ZONE_CHAPTER":
            raise PlanningRegulationStructureError("Article parent section is invalid")
        section_type = type_by_id[section_id]
        if section_type != "ARTICLE":
            raise PlanningRegulationStructureError("Only articles may have a parent section")
        if order_by_id[parent] >= order_by_id[section_id]:
            raise PlanningRegulationStructureError(
                "Article parent must occur earlier in source order"
            )
        if zone_by_id[parent] != zone_by_id[section_id]:
            raise PlanningRegulationStructureError(
                "Article zone label differs from its parent chapter"
            )


def _validate_zone_mapping(
    result: PlanningRegulationStructureResult,
    config: PlanningRegulationStructureConfig,
) -> None:
    frame = result.zone_mapping
    if not isinstance(frame, pd.DataFrame) or tuple(frame.columns) != ZONE_MAPPING_COLUMNS:
        raise PlanningRegulationStructureError("Zone mapping schema is not deterministic")
    labels: list[str] = []
    sections = result.sections.set_index("section_id", drop=False)
    exact_methods = {
        "EXACT": "EXACT_HEADING",
        "CONFIG_ALIAS": "CONFIG_ALIAS",
        "UNMAPPED": "NONE",
        "AMBIGUOUS": "AMBIGUOUS",
    }
    for row in frame.to_dict("records"):
        label = _strict_string(row["source_zone_label_raw"], "source zone label")
        labels.append(label)
        status = _strict_string(row["mapping_status"], "mapping status")
        method = _strict_string(row["mapping_method"], "mapping method")
        if status not in _MAPPING_STATUSES or method not in _MAPPING_METHODS:
            raise PlanningRegulationStructureError("Zone mapping status or method is invalid")
        if exact_methods[status] != method:
            raise PlanningRegulationStructureError(
                "Zone mapping status/method combination is invalid"
            )
        counts: dict[str, int] = {}
        for column in (
            "zone_polygon_count",
            "candidate_parcel_count",
            "candidate_intersection_count",
            "dominant_candidate_count",
        ):
            count = _strict_nonnegative_integer(row[column], column)
            counts[column] = count
            if column == "zone_polygon_count" and count == 0:
                raise PlanningRegulationStructureError("Zone polygon count must be positive")
        matched = row["matched_section_id"]
        if status in {"EXACT", "CONFIG_ALIAS"}:
            matched_id = _strict_string(matched, "matched section ID")
            if matched_id not in sections.index:
                raise PlanningRegulationStructureError("Zone mapping section is unknown")
            resolved = _strict_string(
                row["resolved_zone_chapter_label"], "resolved chapter label"
            )
            matched_section = sections.loc[matched_id]
            if matched_section["section_type"] != "ZONE_CHAPTER":
                raise PlanningRegulationStructureError(
                    "Resolved zone mapping must reference a zone chapter"
                )
            if matched_section["zone_chapter_label"] != resolved:
                raise PlanningRegulationStructureError(
                    "Resolved zone label differs from its matched chapter"
                )
            if status == "EXACT" and resolved != label:
                raise PlanningRegulationStructureError(
                    "Exact zone mapping must preserve the source label"
                )
            if status == "CONFIG_ALIAS" and resolved != _resolved_alias(
                label, config.zone_aliases
            ):
                raise PlanningRegulationStructureError(
                    "Configured zone mapping differs from its final alias target"
                )
        elif matched is not None and not bool(pd.isna(matched)):
            raise PlanningRegulationStructureError("Unresolved zone mapping has a section ID")
        elif status == "UNMAPPED" and row["resolved_zone_chapter_label"] is not None and not bool(
            pd.isna(row["resolved_zone_chapter_label"])
        ):
            raise PlanningRegulationStructureError(
                "Unmapped zone must not claim a resolved chapter label"
            )
        if row["dominant_candidate_count"] > 0 and status not in {"EXACT", "CONFIG_ALIAS"}:
            raise PlanningRegulationStructureError("Dominant candidate zone is unresolved")
        if not (
            counts["dominant_candidate_count"]
            <= counts["candidate_parcel_count"]
            <= counts["candidate_intersection_count"]
        ):
            raise PlanningRegulationStructureError(
                "Zone candidate coverage counts are mathematically inconsistent"
            )
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
    config: PlanningRegulationStructureConfig,
    builds: Sequence[_SectionBuild],
) -> None:
    frame = result.topic_evidence
    if not isinstance(frame, pd.DataFrame) or tuple(frame.columns) != TOPIC_EVIDENCE_COLUMNS:
        raise PlanningRegulationStructureError("Topic evidence schema is not deterministic")
    sections = result.sections.set_index("section_id", drop=False)
    fragments = {
        (str(build.row["section_id"]), page_number): raw_fragment
        for build in builds
        for page_number, raw_fragment in build.page_fragments
    }
    page_set = set(index.pages["page_number"].tolist())
    keys: set[tuple[str, str, str, int]] = set()
    for row in frame.to_dict("records"):
        topic = _strict_string(row["topic"], "topic")
        if topic not in config.topics:
            raise PlanningRegulationStructureError("Topic evidence topic is unconfigured")
        term = _strict_string(row["search_term"], "search term")
        if term not in config.topics[topic]:
            raise PlanningRegulationStructureError(
                "Topic evidence search term is unconfigured"
            )
        normalized = _strict_string(row["normalized_search_term"], "normalized search term")
        if normalized != _normalize_search_text(term):
            raise PlanningRegulationStructureError("Topic search normalization differs")
        section_id = _strict_string(row["section_id"], "topic section ID")
        if section_id not in sections.index:
            raise PlanningRegulationStructureError("Topic evidence references an unknown section")
        page = _strict_positive_integer(row["page_number"], "topic page number")
        if page not in page_set or page not in _page_tuple(sections.at[section_id, "page_numbers"]):
            raise PlanningRegulationStructureError("Topic evidence references an unknown page")
        if (section_id, page) not in fragments:
            raise PlanningRegulationStructureError(
                "Topic evidence page is absent from its retained section text"
            )
        count = _strict_positive_integer(row["occurrence_count"], "topic occurrence count")
        if count < 1:
            raise PlanningRegulationStructureError("Topic occurrence count is invalid")
        if not isinstance(row["raw_context"], str) or not isinstance(row["normalized_context"], str):
            raise PlanningRegulationStructureError("Topic contexts must be strings")
        scope = _strict_string(row["evidence_scope"], "evidence scope")
        if scope not in _EVIDENCE_SCOPES:
            raise PlanningRegulationStructureError("Evidence scope is invalid")
        section = sections.loc[section_id]
        expected_scope = _evidence_scope(str(section["section_type"]))
        if scope != expected_scope:
            raise PlanningRegulationStructureError(
                "Topic evidence scope differs from its section location"
            )
        for column in ("zone_chapter_label", "article_number_raw"):
            actual = row[column]
            expected = section[column]
            if (actual is None or bool(pd.isna(actual))) and (
                expected is None or bool(pd.isna(expected))
            ):
                continue
            if actual != expected:
                raise PlanningRegulationStructureError(
                    f"Topic evidence {column} differs from its section"
                )
        if row["match_policy"] != config.topic_match_policy.identifier:
            raise PlanningRegulationStructureError("Topic match policy differs")
        raw_fragment = fragments[(section_id, page)]
        normalized_fragment, spans = _normalize_search_text_with_mapping(raw_fragment)
        retained_matches = [
            match
            for match in _literal_topic_matches(
                normalized_fragment, config.topics[topic]
            )
            if match.search_term == term
        ]
        if not retained_matches:
            raise PlanningRegulationStructureError(
                "Topic evidence has no retained source-text match"
            )
        first = retained_matches[0]
        expected_positions = {
            "first_match_normalized_start": first.normalized_start,
            "first_match_normalized_end": first.normalized_end,
            "first_match_raw_start": spans[first.normalized_start][0],
            "first_match_raw_end": spans[first.normalized_end - 1][1],
        }
        for column, expected in expected_positions.items():
            if _strict_nonnegative_integer(row[column], column) != expected:
                raise PlanningRegulationStructureError(
                    "Topic match provenance differs from source text"
                )
        if count != len(retained_matches):
            raise PlanningRegulationStructureError(
                "Topic occurrence count differs from retained source spans"
            )
        context_start = max(
            0, first.normalized_start - config.topic_context_characters
        )
        context_end = min(
            len(normalized_fragment),
            first.normalized_end + config.topic_context_characters,
        )
        expected_raw_context = _raw_context(
            raw_fragment, spans, context_start, context_end
        )
        expected_normalized_context = normalized_fragment[context_start:context_end]
        if (
            row["raw_context"] != expected_raw_context
            or row["normalized_context"] != expected_normalized_context
            or row["raw_context"] not in raw_fragment
        ):
            raise PlanningRegulationStructureError(
                "Topic context differs from retained source text"
            )
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


def _build_structure_result(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
    intersections: pd.DataFrame,
    config: PlanningRegulationStructureConfig,
) -> tuple[
    PlanningRegulationStructureResult,
    tuple[_SectionBuild, ...],
    tuple[_LineRecord, ...],
]:
    sections, builds, records = _build_sections(index, config)
    zone_mapping = _build_zone_mapping(
        index,
        config,
        sections,
        zones,
        intersections,
    )
    topic_evidence = _build_topic_evidence(index, config, builds)
    intersection_hash_columns = _intersection_hash_columns(intersections)
    result = PlanningRegulationStructureResult(
        document_id=index.document_id,
        archive_sha256=index.archive_sha256,
        pdf_sha256=index.pdf_sha256,
        index_content_sha256=index.index_content_sha256,
        structure_profile=config.structure_profile,
        structure_config_schema_version=config.schema_version,
        structure_config_sha256=_config_sha256(config),
        zones_content_sha256=_input_frame_sha256(
            "landscout.planning_regulation.zones_input",
            zones,
            _ZONE_INPUT_COLUMNS,
        ),
        zoning_intersection_hash_columns=intersection_hash_columns,
        zoning_intersections_content_sha256=_input_frame_sha256(
            "landscout.planning_regulation.intersections_input",
            intersections,
            intersection_hash_columns,
        ),
        source_records_sha256=_source_records_sha256(records),
        section_hash_schema_version=SECTION_HASH_SCHEMA_VERSION,
        sections_content_sha256="",
        zone_map_content_sha256="",
        topic_evidence_content_sha256="",
        structure_result_content_sha256="",
        sections=sections,
        zone_mapping=zone_mapping,
        topic_evidence=topic_evidence,
    )
    return _result_with_hashes(result), builds, records


def _validate_result_self(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
    intersections: pd.DataFrame,
    config: PlanningRegulationStructureConfig,
    result: PlanningRegulationStructureResult,
    builds: Sequence[_SectionBuild],
    records: Sequence[_LineRecord],
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
    config_schema = _strict_positive_integer(
        result.structure_config_schema_version,
        "structure config schema version",
    )
    if config_schema != config.schema_version:
        raise PlanningRegulationStructureError(
            "Structure config schema version differs"
        )
    _validated_sha256(result.structure_config_sha256, "structure config SHA256")
    if result.structure_config_sha256 != _config_sha256(config):
        raise PlanningRegulationStructureError("Structure config hash differs")
    expected_zones_hash = _input_frame_sha256(
        "landscout.planning_regulation.zones_input",
        zones,
        _ZONE_INPUT_COLUMNS,
    )
    expected_intersections_hash = _input_frame_sha256(
        "landscout.planning_regulation.intersections_input",
        intersections,
        _intersection_hash_columns(intersections),
    )
    if result.zones_content_sha256 != expected_zones_hash:
        raise PlanningRegulationStructureError("Zone input hash differs")
    expected_intersection_columns = _intersection_hash_columns(intersections)
    if (
        type(result.zoning_intersection_hash_columns) is not tuple
        or not all(
            isinstance(column, str)
            for column in result.zoning_intersection_hash_columns
        )
        or result.zoning_intersection_hash_columns != expected_intersection_columns
    ):
        raise PlanningRegulationStructureError(
            "Intersection hash columns differ from the factual input schema"
        )
    if result.zoning_intersections_content_sha256 != expected_intersections_hash:
        raise PlanningRegulationStructureError("Intersection input hash differs")
    _validated_sha256(result.source_records_sha256, "source records SHA256")
    schema = _strict_positive_integer(
        result.section_hash_schema_version, "section hash schema version"
    )
    if schema != SECTION_HASH_SCHEMA_VERSION:
        raise PlanningRegulationStructureError("Unsupported section hash schema version")
    _validate_sections(index, result, records, config)
    _validate_zone_mapping(result, config)
    _validate_topic_evidence(index, result, config, builds)
    expected = _result_with_hashes(replace(
        result,
        sections_content_sha256="",
        zone_map_content_sha256="",
        topic_evidence_content_sha256="",
        structure_result_content_sha256="",
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
    if _validated_sha256(
        result.structure_result_content_sha256,
        "structure result content SHA256",
    ) != expected.structure_result_content_sha256:
        raise PlanningRegulationStructureError("Complete structure result hash differs")


def _resolved_config(
    config: PlanningRegulationStructureConfig | str | Path,
) -> PlanningRegulationStructureConfig:
    if isinstance(config, PlanningRegulationStructureConfig):
        try:
            return PlanningRegulationStructureConfig.model_validate(
                config.model_dump(mode="python")
            )
        except Exception as error:
            raise PlanningRegulationStructureError(
                "Planning structure configuration is invalid"
            ) from error
    return load_planning_regulation_structure_config(config)


def _canonical_frame_rows(frame: pd.DataFrame, columns: Sequence[str]) -> object:
    return _canonical_value(frame.loc[:, columns].to_dict("records"))


def _compare_expected_result(
    result: PlanningRegulationStructureResult,
    expected: PlanningRegulationStructureResult,
) -> None:
    scalar_fields = (
        "document_id",
        "archive_sha256",
        "pdf_sha256",
        "index_content_sha256",
        "structure_profile",
        "structure_config_schema_version",
        "structure_config_sha256",
        "zones_content_sha256",
        "zoning_intersection_hash_columns",
        "zoning_intersections_content_sha256",
        "source_records_sha256",
        "section_hash_schema_version",
        "sections_content_sha256",
        "zone_map_content_sha256",
        "topic_evidence_content_sha256",
        "structure_result_content_sha256",
    )
    for field in scalar_fields:
        if getattr(result, field) != getattr(expected, field):
            raise PlanningRegulationStructureError(
                f"Structure result {field} differs from rebuilt source evidence"
            )
    for name, columns in (
        ("sections", SECTION_COLUMNS),
        ("zone_mapping", ZONE_MAPPING_COLUMNS),
        ("topic_evidence", TOPIC_EVIDENCE_COLUMNS),
    ):
        actual_frame = getattr(result, name)
        expected_frame = getattr(expected, name)
        if tuple(actual_frame.columns) != tuple(columns):
            raise PlanningRegulationStructureError(
                f"{name} schema differs from rebuilt source evidence"
            )
        if _canonical_frame_rows(actual_frame, columns) != _canonical_frame_rows(
            expected_frame, columns
        ):
            raise PlanningRegulationStructureError(
                f"{name} differs from rebuilt source evidence"
            )


def validate_planning_regulation_structure(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
    zoning_intersections: pd.DataFrame,
    config: PlanningRegulationStructureConfig | str | Path,
    result: PlanningRegulationStructureResult,
) -> None:
    """Rebuild and validate the complete structure from all factual inputs."""

    try:
        resolved_config = _resolved_config(config)
        _validate_document_lock(index, resolved_config)
        zones_copy, intersections_copy = _validated_zoning_inputs(
            index, zones, zoning_intersections
        )
        expected, builds, records = _build_structure_result(
            index,
            zones_copy,
            intersections_copy,
            resolved_config,
        )
        _validate_result_self(
            index,
            zones_copy,
            intersections_copy,
            resolved_config,
            result,
            builds,
            records,
        )
        _compare_expected_result(result, expected)
    except PlanningRegulationStructureError:
        raise
    except Exception as error:
        raise PlanningRegulationStructureError(
            "Planning regulation structure validation failed safely"
        ) from error


def planning_regulation_section_page_fragments(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
    zoning_intersections: pd.DataFrame,
    config: PlanningRegulationStructureConfig | str | Path,
    result: PlanningRegulationStructureResult,
) -> pd.DataFrame:
    """Return validated retained raw text for every section and source page."""

    try:
        validate_planning_regulation_structure(
            index,
            zones,
            zoning_intersections,
            config,
            result,
        )
        resolved_config = _resolved_config(config)
        _, builds, _ = _build_structure_result(
            index,
            *_validated_zoning_inputs(index, zones, zoning_intersections),
            resolved_config,
        )
        rows = [
            {
                "section_id": build.row["section_id"],
                "page_number": page_number,
                "raw_text": raw_text,
                "section_page_fragment_sha256": sha256(
                    raw_text.encode("utf-8")
                ).hexdigest(),
                "document_id": result.document_id,
                "archive_sha256": result.archive_sha256,
                "pdf_sha256": result.pdf_sha256,
                "index_content_sha256": result.index_content_sha256,
                "structure_result_content_sha256": (
                    result.structure_result_content_sha256
                ),
                "structure_profile": result.structure_profile,
            }
            for build in builds
            for page_number, raw_text in build.page_fragments
        ]
        frame = pd.DataFrame(
            rows,
            columns=(
                "section_id",
                "page_number",
                "raw_text",
                "section_page_fragment_sha256",
                "document_id",
                "archive_sha256",
                "pdf_sha256",
                "index_content_sha256",
                "structure_result_content_sha256",
                "structure_profile",
            ),
        )
        frame["page_number"] = frame["page_number"].astype("int64")
        if frame.duplicated(["section_id", "page_number"]).any():
            raise PlanningRegulationStructureError(
                "Section/page fragment identity is not unique"
            )
        return frame
    except PlanningRegulationStructureError:
        raise
    except Exception as error:
        raise PlanningRegulationStructureError(
            "Planning regulation section/page fragments could not be rebuilt safely"
        ) from error


def structure_planning_regulation(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
    zoning_intersections: pd.DataFrame,
    config: PlanningRegulationStructureConfig | str | Path,
) -> PlanningRegulationStructureResult:
    """Build source-locked sections, exact zone mappings, and literal topic evidence."""

    try:
        resolved_config = _resolved_config(config)
        _validate_document_lock(index, resolved_config)
        zones_copy, intersections_copy = _validated_zoning_inputs(
            index, zones, zoning_intersections
        )
        result, _, _ = _build_structure_result(
            index,
            zones_copy,
            intersections_copy,
            resolved_config,
        )
        validate_planning_regulation_structure(
            index,
            zones_copy,
            intersections_copy,
            resolved_config,
            result,
        )
        return result
    except PlanningRegulationStructureError:
        raise
    except Exception as error:
        raise PlanningRegulationStructureError(
            "Planning regulation structure could not be built safely"
        ) from error

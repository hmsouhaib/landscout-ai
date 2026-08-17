# `src/landscout/stages/structure_planning_regulation.py`

## File identity

- Repository path: `src/landscout/stages/structure_planning_regulation.py`
- File type: Python source
- Primary responsibility: Partitions the indexed written regulation into deterministic source-bound sections, zone mappings, and topic evidence.
- Layer / domain: `stage` / `planning`
- Public or internal role: Contains an explicit module/package export surface; helpers prefixed with `_` remain internal unless re-exported elsewhere.
- Source SHA256: `46707b5077b1e122158b4ca6be3363ee8ad7808ac62e08106854bee1e89da45e`

## 1. Purpose

Partitions the indexed written regulation into deterministic source-bound sections, zone mappings, and topic evidence.

## 2. Position in LandScout architecture

This file is a `stage` artifact in the `planning` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import json` — required by the implementation paths and symbols documented below.
- `import math` — required by the implementation paths and symbols documented below.
- `import re` — required by the implementation paths and symbols documented below.
- `from collections import Counter` — required by the implementation paths and symbols documented below.
- `from collections.abc import Mapping, Sequence` — required by the implementation paths and symbols documented below.
- `from dataclasses import dataclass, replace` — required by the implementation paths and symbols documented below.
- `from hashlib import sha256` — required by the implementation paths and symbols documented below.
- `from numbers import Integral, Real` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.
- `from typing import Literal` — required by the implementation paths and symbols documented below.

### Third-party

- `from itertools import pairwise` — required by the implementation paths and symbols documented below.
- `import numpy as np` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `import yaml` — required by the implementation paths and symbols documented below.
- `from pydantic import ( BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, model_validator, )` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.common.planning_text import ( normalize_planning_search_text, normalize_planning_search_text_with_mapping, raw_context_from_spans, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.index_planning_regulation import ( PlanningRegulationIndex, validate_planning_regulation_index, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.planning_overlay import technical_overlay_tolerance` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `SECTION_HASH_SCHEMA_VERSION` | `3` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `STRUCTURE_MANIFEST_SCHEMA_VERSION` | `4` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_SUPPORTED_CONFIG_SCHEMA_VERSION` | `2` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_SECTION_TYPES` | `frozenset({"GENERAL", "ZONE_CHAPTER", "ARTICLE", "OTHER"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_MAPPING_STATUSES` | `frozenset({"EXACT", "CONFIG_ALIAS", "UNMAPPED", "AMBIGUOUS"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_MAPPING_METHODS` | `frozenset({"EXACT_HEADING", "CONFIG_ALIAS", "NONE", "AMBIGUOUS"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_EVIDENCE_SCOPES` | `frozenset( {"GENERAL_RULE", "ZONE_SPECIFIC_RULE", "OTHER_TEXT"} )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_ZONE_INPUT_COLUMNS` | `( "planning_zone_id", "source_zone_id", "zone_label_raw", "source_document_id", "source_archive_sha256", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_REQUIRED_INTERSECTION_INPUT_COLUMNS` | `( "parcel_id", "planning_zone_id", "source_zone_id", "zone_label_raw", "relation_type", "intersection_area_m2", "source_document_id", "source_archive_sha256", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_OPTIONAL_INTERSECTION_INPUT_COLUMNS` | `( "parcel_metric_area_m2", "zone_area_m2", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SECTION_COLUMNS` | `( "section_id", "parent_section_id", "section_type", "heading_raw", "heading_normalized", "zone_chapter_label", "article_number_raw", "article_title_raw", "start_record_id", "end_record_id", "source_record_count", "source_records_sha256", "start_page", "end_page", "page_numbers", "raw_text", "normalized_text", "character_count", "section_content_sha256", "document_id", "archive_sha256", "pdf_sha256", "index_content_sha256", "structure_profile", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ZONE_MAPPING_COLUMNS` | `( "source_zone_label_raw", "resolved_zone_chapter_label", "mapping_status", "mapping_method", "matched_section_id", "zone_polygon_count", "candidate_parcel_count", "candidate_intersection_count", "dominant_candidate_count", "document_id", "archive_sha256", "pdf_sha256", "index_content_sha256", "structure_profile", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `TOPIC_EVIDENCE_COLUMNS` | `( "topic", "search_term", "normalized_search_term", "match_policy", "section_id", "evidence_scope", "zone_chapter_label", "article_number_raw", "page_number", "occurrence_count", "first_match_normalized_start", "first_match_normalized_end", "first_match_raw_start", "first_match_raw_end", "raw_context", "normalized_context", "document_id", "archive_sha256", "pdf_sha256", "index_content_sha256", "structure_profile", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `PlanningRegulationStructureError`

**Purpose:** Raised when factual regulation structure integrity cannot be proven.

**Inheritance:** `ValueError`.

**Model form and mutability:** class inheriting from `ValueError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `_StrictConfigModel`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid", frozen=True)`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `DocumentLockConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `_StrictConfigModel`.

**Model form and mutability:** class inheriting from `_StrictConfigModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `document_id` | `StrictStr` | `Field(min_length=1)` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `pdf_sha256` | `StrictStr` | `Field(pattern='^[0-9a-f]{64}$')` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `pages_content_sha256` | `StrictStr` | `Field(pattern='^[0-9a-f]{64}$')` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `index_content_sha256` | `StrictStr` | `Field(pattern='^[0-9a-f]{64}$')` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `normalization_profile` | `StrictStr` | `Field(min_length=1)` | `StrictStr` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `DocumentLayoutConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `_StrictConfigModel`.

**Model form and mutability:** class inheriting from `_StrictConfigModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `body_start_page` | `StrictInt` | `Field(ge=1)` | `StrictInt` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `table_of_contents_pages` | `tuple[StrictInt, ...]` | `()` | `tuple[StrictInt, ...]` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `max_heading_continuation_lines` | `StrictInt` | `Field(ge=0, le=10)` | `StrictInt` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `include_table_of_contents_in_topic_evidence` | `StrictBool` | `False` | `StrictBool` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `_validate_pages` — `def _validate_pages(self) -> DocumentLayoutConfig:`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

### `HeadingPatternsConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `_StrictConfigModel`.

**Model form and mutability:** class inheriting from `_StrictConfigModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `zone_chapter` | `tuple[StrictStr, ...]` | `Field(min_length=1)` | `tuple[StrictStr, ...]` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `article` | `tuple[StrictStr, ...]` | `Field(min_length=1)` | `tuple[StrictStr, ...]` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `general_section` | `tuple[StrictStr, ...]` | `Field(min_length=1)` | `tuple[StrictStr, ...]` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `continuation` | `tuple[StrictStr, ...]` | `()` | `tuple[StrictStr, ...]` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `IgnoredPatternsConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `_StrictConfigModel`.

**Model form and mutability:** class inheriting from `_StrictConfigModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `page_headers` | `tuple[StrictStr, ...]` | `()` | `tuple[StrictStr, ...]` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `page_footers` | `tuple[StrictStr, ...]` | `()` | `tuple[StrictStr, ...]` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `TopicMatchPolicyConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `_StrictConfigModel`.

**Model form and mutability:** class inheriting from `_StrictConfigModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `boundary_mode` | `Literal['token']` | `required` | `Literal['token']` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `overlap_resolution` | `Literal['longest_match']` | `required` | `Literal['longest_match']` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `identifier` — `def identifier(self) -> str:`; decorators `property`. The complete method algorithm appears in the function/method section.

### `PlanningRegulationStructureConfig`

**Purpose:** Strict, document-locked grammar for one factual regulation structure.

**Inheritance:** `_StrictConfigModel`.

**Model form and mutability:** class inheriting from `_StrictConfigModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `schema_version` | `StrictInt` | `required` | `StrictInt` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `structure_profile` | `StrictStr` | `Field(min_length=1)` | `StrictStr` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `document_lock` | `DocumentLockConfig` | `required` | `DocumentLockConfig` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `document_layout` | `DocumentLayoutConfig` | `required` | `DocumentLayoutConfig` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `heading_patterns` | `HeadingPatternsConfig` | `required` | `HeadingPatternsConfig` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `ignored_patterns` | `IgnoredPatternsConfig` | `required` | `IgnoredPatternsConfig` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `zone_aliases` | `dict[StrictStr, StrictStr]` | `required` | `dict[StrictStr, StrictStr]` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `topics` | `dict[StrictStr, tuple[StrictStr, ...]]` | `required` | `dict[StrictStr, tuple[StrictStr, ...]]` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `topic_match_policy` | `TopicMatchPolicyConfig` | `required` | `TopicMatchPolicyConfig` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `topic_context_characters` | `StrictInt` | `Field(ge=0)` | `StrictInt` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `_validate_grammar` — `def _validate_grammar(self) -> PlanningRegulationStructureConfig:`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

### `PlanningRegulationStructureResult`

**Purpose:** Immutable lineage envelope for regulation sections and factual evidence.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `document_id` | `str` | `required` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `archive_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `pdf_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `index_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `structure_profile` | `str` | `required` | `str` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `structure_config_schema_version` | `int` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `structure_config_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `zones_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `zoning_intersection_hash_columns` | `tuple[str, ...]` | `required` | `tuple[str, ...]` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `zoning_intersections_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `source_records_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `section_hash_schema_version` | `int` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `sections_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `zone_map_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `topic_evidence_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `structure_result_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `sections` | `pd.DataFrame` | `required` | `pd.DataFrame` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `zone_mapping` | `pd.DataFrame` | `required` | `pd.DataFrame` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `topic_evidence` | `pd.DataFrame` | `required` | `pd.DataFrame` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `_LineRecord`

**Purpose:** Groups the `LineRecord` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `record_id` | `str` | `required` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `page_number` | `int` | `required` | `int` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `page_line_number` | `int` | `required` | `int` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `raw` | `str` | `required` | `str` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `_HeadingEvent`

**Purpose:** Groups the `HeadingEvent` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `record_position` | `int` | `required` | `int` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `section_type` | `Literal['GENERAL', 'ZONE_CHAPTER', 'ARTICLE']` | `required` | Categorical source, feature, or relation type constrained by the owning model or validator. |
| `heading_raw` | `str` | `required` | Uninterpreted source value retained without semantic coercion by normalization. |
| `heading_normalized` | `str` | `required` | `str` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `zone_chapter_label` | `str | None` | `required` | `str | None` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `article_number_raw` | `str | None` | `required` | Uninterpreted source value retained without semantic coercion by normalization. |
| `article_title_raw` | `str | None` | `required` | Uninterpreted source value retained without semantic coercion by normalization. |

**Validators and methods:**

- None.

### `_StructuralHeadingMatch`

**Purpose:** Groups the `StructuralHeadingMatch` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `section_type` | `Literal['GENERAL', 'ZONE_CHAPTER', 'ARTICLE']` | `required` | Categorical source, feature, or relation type constrained by the owning model or validator. |
| `pattern_index` | `int` | `required` | `int` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `named_captures` | `tuple[tuple[str, str | None], ...]` | `required` | `tuple[tuple[str, str | None], ...]` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `_SectionBoundary`

**Purpose:** Groups the `SectionBoundary` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `record_position` | `int` | `required` | `int` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `event` | `_HeadingEvent | None` | `required` | `_HeadingEvent | None` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `forced_table_of_contents` | `bool` | `required` | `bool` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `_SectionBuild`

**Purpose:** Groups the `SectionBuild` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `row` | `dict[str, object]` | `required` | `dict[str, object]` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `page_fragments` | `tuple[tuple[int, str], ...]` | `required` | `tuple[tuple[int, str], ...]` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `_UniqueKeyLoader`

**Purpose:** Groups the `UniqueKeyLoader` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `yaml.SafeLoader`.

**Model form and mutability:** class inheriting from `yaml.SafeLoader`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `_TopicMatch`

**Purpose:** Groups the `TopicMatch` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `term_index` | `int` | `required` | `int` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `search_term` | `str` | `required` | `str` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `normalized_term` | `str` | `required` | `str` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `normalized_start` | `int` | `required` | `int` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `normalized_end` | `int` | `required` | `int` state used by `src/landscout/stages/structure_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

## 6. Functions and methods

### `DocumentLayoutConfig._validate_pages`

**Signature**

```python
def _validate_pages(self) -> DocumentLayoutConfig:
```

**Purpose**

Validates and rejects malformed pages according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `DocumentLayoutConfig`. Observed return expression(s): `self`.

**Algorithm**

1. Computes `pages` from `self.table_of_contents_pages`.
2. Checks `any((page < 1 for page in pages)) or tuple(sorted(set(pages))) != pages`. When true: Raises `ValueError('table_of_contents_pages must contain unique ascending positive integers')`.
3. Returns `self`.

**Validation and invariants**

- Rejects or diverts the path when `any((page < 1 for page in pages)) or tuple(sorted(set(pages))) != pages` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `any`, `model_validator`, `set`, `sorted`, `tuple`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `TopicMatchPolicyConfig.identifier`

**Signature**

```python
def identifier(self) -> str:
```

**Purpose**

Implements identifier according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `f'{self.boundary_mode}_{self.overlap_resolution}'`.

**Algorithm**

1. Returns `f'{self.boundary_mode}_{self.overlap_resolution}'`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `PlanningRegulationStructureConfig._validate_grammar`

**Signature**

```python
def _validate_grammar(self) -> PlanningRegulationStructureConfig:
```

**Purpose**

Validates and rejects malformed grammar according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `PlanningRegulationStructureConfig`. Observed return expression(s): `self`.

**Algorithm**

1. Checks `self.schema_version != _SUPPORTED_CONFIG_SCHEMA_VERSION`. When true: Raises `ValueError(f'unsupported structure config schema: {self.schema_version}')`.
2. Calls `_exact_config_string(self.structure_profile, 'structure_profile')` for its validation or side effect.
3. Calls `_exact_config_string(self.document_lock.document_id, 'document_id')` for its validation or side effect.
4. Calls `_exact_config_string(self.document_lock.normalization_profile, 'normalization_profile')` for its validation or side effect.
5. Computes `pattern_groups` from `(self.heading_patterns.zone_chapter, self.heading_patterns.article, self.heading_patterns.general_section, self.heading_patterns.continuation, self.ignored_patterns.page_headers, self.ignored_patterns.page_footers)`.
6. Iterates `patterns` over `pattern_groups`. For each value: Checks `len(set(patterns)) != len(patterns)`. When true: Raises `ValueError('regular-expression patterns must be unique')`. Iterates `pattern` over `patterns`. For each value: Calls `_exact_config_string(pattern, 'regular-expression pattern')` for its validation or side effect. Runs guarded operation: Calls `re.compile(pattern)` for its validation or side effect. Handles `re.error`.
7. Defines `structural_pattern_owners` with annotation `dict[str, str]` from `{}`.
8. Iterates `(category, patterns)` over `(('ZONE_CHAPTER', self.heading_patterns.zone_chapter), ('GENERAL', self.heading_patterns.general_section), ('ARTICLE', self.heading_patterns.article))`. For each value: Iterates `pattern` over `patterns`. For each value: Computes `previous` from `structural_pattern_owners.get(pattern)`. Checks `previous is not None`. When true: Raises `ValueError(f'identical structural heading regex is reused across groups {previous} and {category}')`. Computes `structural_pattern_owners[pattern]` from `category`.
9. Computes `required_captures` from `((self.heading_patterns.zone_chapter, {'label'}, 'zone chapter'), (self.heading_patterns.article, {'zone', 'number', 'title'}, 'zone article'), (self.heading_patterns.general_section, {'number', 'title'}, 'general section'))`.
10. Iterates `(patterns, required, label)` over `required_captures`. For each value: Iterates `pattern` over `patterns`. For each value: Computes `missing` from `required.difference(re.compile(pattern).groupindex)`. Checks `missing`. When true: Raises `ValueError(f'{label} pattern lacks named captures: {sorted(missing)}')`.
11. Iterates `(alias, target)` over `self.zone_aliases.items()`. For each value: Calls `_exact_config_string(alias, 'zone alias')` for its validation or side effect. Calls `_exact_config_string(target, 'zone alias target')` for its validation or side effect.
12. Calls `_validate_alias_cycles(self.zone_aliases)` for its validation or side effect.
13. Checks `not self.topics`. When true: Raises `ValueError('topics must not be empty')`.
14. Iterates `topic` over `sorted(self.topics)`. For each value: Computes `terms` from `self.topics[topic]`. Calls `_exact_config_string(topic, 'topic')` for its validation or side effect. Checks `not terms`. When true: Raises `ValueError(f'topic {topic!r} must contain literal terms')`. Executes 2 additional source-ordered statement(s).
15. Returns `self`.

**Validation and invariants**

- Rejects or diverts the path when `self.schema_version != _SUPPORTED_CONFIG_SCHEMA_VERSION` is true.
- Rejects or diverts the path when `not self.topics` is true.
- Rejects or diverts the path when `len(set(patterns)) != len(patterns)` is true.
- Rejects or diverts the path when `not terms` is true.
- Rejects or diverts the path when `previous is not None` is true.
- Rejects or diverts the path when `missing` is true.
- Rejects or diverts the path when `not normalized_term or normalized_term in normalized` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `_exact_config_string`, `_normalize_search_text`, `_validate_alias_cycles`, `len`, `model_validator`, `normalized.add`, `re.compile`, `required.difference`, `self.zone_aliases.items`, `set`, `sorted`, `structural_pattern_owners.get`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_construct_unique_mapping`

**Signature**

```python
def _construct_unique_mapping(
    loader: yaml.SafeLoader,
    node: yaml.MappingNode,
    deep: bool = False,
) -> dict[object, object]:
```

**Purpose**

Implements construct unique mapping according to the exact implementation and guards in this file.

**Inputs**

- `loader` (`yaml.SafeLoader`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `node` (`yaml.MappingNode`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `deep` (`bool`; optional/default `False`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[object, object]`. Observed return expression(s): `result`.

**Algorithm**

1. Defines `result` with annotation `dict[object, object]` from `{}`.
2. Iterates `(key_node, value_node)` over `node.value`. For each value: Computes `key` from `loader.construct_object(key_node, deep=deep)`. Checks `key in result`. When true: Raises `PlanningRegulationStructureError(f'Duplicate YAML configuration key: {key!r}')`. Computes `result[key]` from `loader.construct_object(value_node, deep=deep)`.
3. Returns `result`.

**Validation and invariants**

- Rejects or diverts the path when `key in result` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationStructureError`, `loader.construct_object`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_exact_config_string`

**Signature**

```python
def _exact_config_string(value: str, label: str) -> str:
```

**Purpose**

Implements exact config string according to the exact implementation and guards in this file.

**Inputs**

- `value` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `value`.

**Algorithm**

1. Checks `not value or value != value.strip()`. When true: Raises `ValueError(f'{label} must be a non-empty exact string')`.
2. Returns `value`.

**Validation and invariants**

- Rejects or diverts the path when `not value or value != value.strip()` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `value.strip`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `PlanningRegulationStructureConfig._validate_grammar`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_alias_cycles`

**Signature**

```python
def _validate_alias_cycles(aliases: Mapping[str, str]) -> None:
```

**Purpose**

Validates and rejects malformed alias cycles according to the exact implementation and guards in this file.

**Inputs**

- `aliases` (`Mapping[str, str]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Iterates `start` over `aliases`. For each value: Defines `seen` with annotation `set[str]` from `set()`. Computes `current` from `start`. Repeats the guarded body while `current in aliases` remains true.

**Validation and invariants**

- Rejects or diverts the path when `current in seen` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `seen.add`, `set`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `PlanningRegulationStructureConfig._validate_grammar`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `load_planning_regulation_structure_config`

**Signature**

```python
def load_planning_regulation_structure_config(
    path: str | Path,
) -> PlanningRegulationStructureConfig:
```

**Purpose**

Load and strictly validate a document-specific structure grammar.

**Inputs**

- `path` (`str | Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `PlanningRegulationStructureConfig`. Observed return expression(s): `PlanningRegulationStructureConfig.model_validate(payload)`.

**Algorithm**

1. Runs guarded operation: Computes `config_path` from `Path(path)`. Computes `payload` from `yaml.load(config_path.read_text(encoding='utf-8'), Loader=_UniqueKeyLoader)`. Checks `not isinstance(payload, Mapping)`. When true: Raises `PlanningRegulationStructureError('Planning structure configuration must be a mapping')`. Returns `PlanningRegulationStructureConfig.model_validate(payload)`. Handles `PlanningRegulationStructureError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(payload, Mapping)` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `config_path.read_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `Path`, `PlanningRegulationStructureConfig.model_validate`, `PlanningRegulationStructureError`, `config_path.read_text`, `isinstance`, `yaml.load`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_resolved_config`
- `tests/unit/test_structure_planning_regulation.py` — `test_duplicate_yaml_alias_and_alias_cycle_are_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_invalid_regex_and_unknown_yaml_field_are_controlled`

**Tests**

- `tests/unit/test_structure_planning_regulation.py::test_duplicate_yaml_alias_and_alias_cycle_are_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_invalid_regex_and_unknown_yaml_field_are_controlled`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_strict_string`

**Signature**

```python
def _strict_string(value: object, label: str) -> str:
```

**Purpose**

Implements strict string according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `value`.

**Algorithm**

1. Checks `not isinstance(value, str) or not value or value != value.strip()`. When true: Raises `PlanningRegulationStructureError(f'{label} must be a non-empty exact string')`.
2. Returns `value`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(value, str) or not value or value != value.strip()` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationStructureError`, `isinstance`, `value.strip`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_build_zone_mapping`
- `src/landscout/stages/structure_planning_regulation.py` — `_canonical_chapter_label`
- `src/landscout/stages/structure_planning_regulation.py` — `_validate_result_self`
- `src/landscout/stages/structure_planning_regulation.py` — `_validate_sections`
- `src/landscout/stages/structure_planning_regulation.py` — `_validate_source_label_values`
- `src/landscout/stages/structure_planning_regulation.py` — `_validate_topic_evidence`
- `src/landscout/stages/structure_planning_regulation.py` — `_validate_zone_mapping`
- `src/landscout/stages/structure_planning_regulation.py` — `_validated_sha256`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_strict_nonnegative_integer`

**Signature**

```python
def _strict_nonnegative_integer(value: object, label: str) -> int:
```

**Purpose**

Implements strict nonnegative integer according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `int`. Observed return expression(s): `result`.

**Algorithm**

1. Checks `isinstance(value, bool) or not isinstance(value, Integral)`. When true: Raises `PlanningRegulationStructureError(f'{label} must be an integer')`.
2. Computes `result` from `int(value)`.
3. Checks `result < 0`. When true: Raises `PlanningRegulationStructureError(f'{label} must be non-negative')`.
4. Returns `result`.

**Validation and invariants**

- Rejects or diverts the path when `isinstance(value, bool) or not isinstance(value, Integral)` is true.
- Rejects or diverts the path when `result < 0` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationStructureError`, `int`, `isinstance`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_strict_positive_integer`
- `src/landscout/stages/structure_planning_regulation.py` — `_validate_sections`
- `src/landscout/stages/structure_planning_regulation.py` — `_validate_topic_evidence`
- `src/landscout/stages/structure_planning_regulation.py` — `_validate_zone_mapping`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_strict_positive_integer`

**Signature**

```python
def _strict_positive_integer(value: object, label: str) -> int:
```

**Purpose**

Implements strict positive integer according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `int`. Observed return expression(s): `result`.

**Algorithm**

1. Computes `result` from `_strict_nonnegative_integer(value, label)`.
2. Checks `result == 0`. When true: Raises `PlanningRegulationStructureError(f'{label} must be positive')`.
3. Returns `result`.

**Validation and invariants**

- Rejects or diverts the path when `result == 0` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationStructureError`, `_strict_nonnegative_integer`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_line_records`
- `src/landscout/stages/structure_planning_regulation.py` — `_page_tuple`
- `src/landscout/stages/structure_planning_regulation.py` — `_validate_document_lock`
- `src/landscout/stages/structure_planning_regulation.py` — `_validate_result_self`
- `src/landscout/stages/structure_planning_regulation.py` — `_validate_sections`
- `src/landscout/stages/structure_planning_regulation.py` — `_validate_topic_evidence`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validated_sha256`

**Signature**

```python
def _validated_sha256(value: object, label: str) -> str:
```

**Purpose**

Validates and returns canonical sha256 according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `checksum`.

**Algorithm**

1. Computes `checksum` from `_strict_string(value, label)`.
2. Checks `re.fullmatch('[0-9a-f]{64}', checksum) is None`. When true: Raises `PlanningRegulationStructureError(f'{label} must be exactly 64 lowercase hexadecimal characters')`.
3. Returns `checksum`.

**Validation and invariants**

- Rejects or diverts the path when `re.fullmatch('[0-9a-f]{64}', checksum) is None` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationStructureError`, `_strict_string`, `re.fullmatch`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_validate_result_self`
- `src/landscout/stages/structure_planning_regulation.py` — `_validate_sections`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_value`

**Signature**

```python
def _canonical_value(value: object) -> object:
```

**Purpose**

Implements canonical value according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. Observed return expression(s): `None`; `_canonical_value(value.item())`; `[_canonical_value(item) for item in value]`; `{str(key): _canonical_value(item) for key, item in value.items()}`; `value`.

**Algorithm**

1. Checks `value is None or value is pd.NA`. When true: Returns `None`.
2. Checks `isinstance(value, np.generic)`. When true: Returns `_canonical_value(value.item())`.
3. Checks `isinstance(value, (tuple, list, np.ndarray))`. When true: Returns `[_canonical_value(item) for item in value]`.
4. Checks `isinstance(value, Mapping)`. When true: Returns `{str(key): _canonical_value(item) for key, item in value.items()}`.
5. Checks `isinstance(value, float) and math.isnan(value)`. When true: Returns `None`.
6. Checks `isinstance(value, (str, int, float, bool))`. When true: Returns `value`.
7. Raises `PlanningRegulationStructureError(f'Value of type {type(value).__name__} cannot be canonically serialized')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationStructureError`, `_canonical_value`, `isinstance`, `math.isnan`, `str`, `type`, `value.item`, `value.items`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_canonical_frame_rows`
- `src/landscout/stages/structure_planning_regulation.py` — `_canonical_sha256`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_sha256`

**Signature**

```python
def _canonical_sha256(value: object) -> str:
```

**Purpose**

Implements canonical sha256 according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `sha256(serialized).hexdigest()`.

**Algorithm**

1. Runs guarded operation: Computes `serialized` from `json.dumps(_canonical_value(value), ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(',', ':')).encode('utf-8')`. Handles `PlanningRegulationStructureError`, `Exception`.
2. Returns `sha256(serialized).hexdigest()`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationStructureError`, `_canonical_value`, `json.dumps`, `json.dumps(_canonical_value(value), ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(',', ':')).encode`, `sha256`, `sha256(serialized).hexdigest`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_config_sha256`
- `src/landscout/stages/structure_planning_regulation.py` — `_frame_hash`
- `src/landscout/stages/structure_planning_regulation.py` — `_input_frame_sha256`
- `src/landscout/stages/structure_planning_regulation.py` — `_section_content_sha256`
- `src/landscout/stages/structure_planning_regulation.py` — `_source_records_sha256`
- `src/landscout/stages/structure_planning_regulation.py` — `_structure_result_content_sha256`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_config_sha256`

**Signature**

```python
def _config_sha256(config: PlanningRegulationStructureConfig) -> str:
```

**Purpose**

Implements config sha256 according to the exact implementation and guards in this file.

**Inputs**

- `config` (`PlanningRegulationStructureConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_sha256({'domain': 'landscout.planning_regulation.structure_config', 'config': payload})`.

**Algorithm**

1. Computes `payload` from `config.model_dump(mode='json')`.
2. Computes `payload['topics']` from `{topic: list(config.topics[topic]) for topic in sorted(config.topics)}`.
3. Returns `_canonical_sha256({'domain': 'landscout.planning_regulation.structure_config', 'config': payload})`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_sha256`, `config.model_dump`, `list`, `sorted`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_build_structure_result`
- `src/landscout/stages/structure_planning_regulation.py` — `_validate_result_self`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_document_lock`

**Signature**

```python
def _validate_document_lock(
    index: PlanningRegulationIndex,
    config: PlanningRegulationStructureConfig,
) -> None:
```

**Purpose**

Validates and rejects malformed document lock according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`PlanningRegulationStructureConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Calls `validate_planning_regulation_index(index)` for its validation or side effect.
2. Computes `lock` from `config.document_lock`.
3. Computes `comparisons` from `((index.document_id, lock.document_id, 'document ID'), (index.pdf_sha256, lock.pdf_sha256, 'PDF SHA256'), (index.pages_content_sha256, lock.pages_content_sha256, 'pages content SHA256'), (index.index_content_sha256, lock.index_content_sha256, 'index content SHA256'), (index.search_normalization_profile, lock.normaliza…`.
4. Iterates `(actual, expected, label)` over `comparisons`. For each value: Checks `actual != expected`. When true: Raises `PlanningRegulationStructureError(f'Planning structure {label} differs from its document lock')`.
5. Computes `indexed_pages` from `tuple((_strict_positive_integer(value, 'indexed page number') for value in index.pages['page_number'].tolist()))`.
6. Computes `indexed_page_set` from `set(indexed_pages)`.
7. Checks `config.document_layout.body_start_page not in indexed_page_set`. When true: Raises `PlanningRegulationStructureError('body_start_page must reference a real indexed page')`.
8. Computes `missing_toc_pages` from `sorted(set(config.document_layout.table_of_contents_pages).difference(indexed_page_set))`.
9. Checks `missing_toc_pages`. When true: Raises `PlanningRegulationStructureError(f'table_of_contents_pages reference nonexistent indexed pages: {missing_toc_pages}')`.

**Validation and invariants**

- Rejects or diverts the path when `config.document_layout.body_start_page not in indexed_page_set` is true.
- Rejects or diverts the path when `missing_toc_pages` is true.
- Rejects or diverts the path when `actual != expected` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationStructureError`, `_strict_positive_integer`, `index.pages['page_number'].tolist`, `set`, `set(config.document_layout.table_of_contents_pages).difference`, `sorted`, `tuple`, `validate_planning_regulation_index`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `structure_planning_regulation`
- `src/landscout/stages/structure_planning_regulation.py` — `validate_planning_regulation_structure_with_fragments`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_compiled`

**Signature**

```python
def _compiled(patterns: Sequence[str]) -> tuple[re.Pattern[str], ...]:
```

**Purpose**

Implements compiled according to the exact implementation and guards in this file.

**Inputs**

- `patterns` (`Sequence[str]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[re.Pattern[str], ...]`. Observed return expression(s): `tuple((re.compile(pattern) for pattern in patterns))`.

**Algorithm**

1. Returns `tuple((re.compile(pattern) for pattern in patterns))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `re.compile`, `tuple`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_heading_events`
- `src/landscout/stages/structure_planning_regulation.py` — `_line_records`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_matches_any`

**Signature**

```python
def _matches_any(value: str, patterns: Sequence[re.Pattern[str]]) -> bool:
```

**Purpose**

Implements matches any according to the exact implementation and guards in this file.

**Inputs**

- `value` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `patterns` (`Sequence[re.Pattern[str]]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `any((pattern.fullmatch(value) is not None for pattern in patterns))`.

**Algorithm**

1. Returns `any((pattern.fullmatch(value) is not None for pattern in patterns))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `any`, `pattern.fullmatch`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_heading_events`
- `src/landscout/stages/structure_planning_regulation.py` — `_retained_page_lines`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_retained_page_lines`

**Signature**

```python
def _retained_page_lines(
    raw_text: str,
    headers: Sequence[re.Pattern[str]],
    footers: Sequence[re.Pattern[str]],
) -> list[tuple[int, str]]:
```

**Purpose**

Implements retained page lines according to the exact implementation and guards in this file.

**Inputs**

- `raw_text` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `headers` (`Sequence[re.Pattern[str]]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `footers` (`Sequence[re.Pattern[str]]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `list[tuple[int, str]]`. Observed return expression(s): `lines[start:end]`.

**Algorithm**

1. Computes `lines` from `list(enumerate(raw_text.splitlines(), start=1))`.
2. Computes `start` from `0`.
3. Computes `first_nonempty` from `next((position for position, (_, line) in enumerate(lines) if line.strip()), None)`.
4. Checks `first_nonempty is not None and _matches_any(lines[first_nonempty][1].strip(), headers)`. When true: Computes `cursor` from `first_nonempty`. Repeats the guarded body while `cursor < len(lines)` remains true. Computes `start` from `cursor`.
5. Computes `end` from `len(lines)`.
6. Computes `last_nonempty` from `next((position for position in range(len(lines) - 1, start - 1, -1) if lines[position][1].strip()), None)`.
7. Checks `last_nonempty is not None and _matches_any(lines[last_nonempty][1].strip(), footers)`. When true: Computes `cursor` from `last_nonempty`. Repeats the guarded body while `cursor >= start` remains true. Computes `end` from `cursor + 1`.
8. Returns `lines[start:end]`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_matches_any`, `enumerate`, `len`, `line.strip`, `lines[cursor][1].strip`, `lines[first_nonempty][1].strip`, `lines[last_nonempty][1].strip`, `lines[position][1].strip`, `list`, `next`, `range`, `raw_text.splitlines`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_line_records`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_line_records`

**Signature**

```python
def _line_records(
    index: PlanningRegulationIndex,
    config: PlanningRegulationStructureConfig,
) -> list[_LineRecord]:
```

**Purpose**

Implements line records according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`PlanningRegulationStructureConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `list[_LineRecord]`. Observed return expression(s): `records`.

**Algorithm**

1. Computes `headers` from `_compiled(config.ignored_patterns.page_headers)`.
2. Computes `footers` from `_compiled(config.ignored_patterns.page_footers)`.
3. Defines `retained` with annotation `list[tuple[int, int, str]]` from `[]`.
4. Iterates `page` over `index.pages.to_dict('records')`. For each value: Computes `page_number` from `_strict_positive_integer(page['page_number'], 'page number')`. Computes `raw_text` from `page['raw_text']`. Checks `not isinstance(raw_text, str)`. When true: Raises `PlanningRegulationStructureError('Page raw text must be a string')`. Executes 1 additional source-ordered statement(s).
5. Computes `records` from `[_LineRecord(record_id=f'RECORD-{position:06d}', page_number=page_number, page_line_number=line_number, raw=raw_line) for position, (page_number, line_number, raw_line) in enumerate(retained, start=1)]`.
6. Checks `not records`. When true: Raises `PlanningRegulationStructureError('Regulation contains no structural text')`.
7. Returns `records`.

**Validation and invariants**

- Rejects or diverts the path when `not records` is true.
- Rejects or diverts the path when `not isinstance(raw_text, str)` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationStructureError`, `_LineRecord`, `_compiled`, `_retained_page_lines`, `_strict_positive_integer`, `enumerate`, `index.pages.to_dict`, `isinstance`, `retained.extend`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_build_sections`
- `tests/unit/test_structure_planning_regulation.py` — `_structure_with_document_layout`
- `tests/unit/test_structure_planning_regulation.py` — `test_blank_only_prefix_is_preserved_in_first_actual_section`
- `tests/unit/test_structure_planning_regulation.py` — `test_page_without_configured_header_or_footer_is_unchanged`
- `tests/unit/test_structure_planning_regulation.py` — `test_positional_header_footer_filter_preserves_matching_body_lines`
- `tests/unit/test_structure_planning_regulation.py` — `test_unique_zone_heading_and_nonheading_line_are_classified_deterministically`

**Tests**

- `tests/unit/test_structure_planning_regulation.py::test_blank_only_prefix_is_preserved_in_first_actual_section`
- `tests/unit/test_structure_planning_regulation.py::test_page_without_configured_header_or_footer_is_unchanged`
- `tests/unit/test_structure_planning_regulation.py::test_positional_header_footer_filter_preserves_matching_body_lines`
- `tests/unit/test_structure_planning_regulation.py::test_unique_zone_heading_and_nonheading_line_are_classified_deterministically`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_source_record_payload`

**Signature**

```python
def _source_record_payload(record: _LineRecord) -> dict[str, object]:
```

**Purpose**

Implements source record payload according to the exact implementation and guards in this file.

**Inputs**

- `record` (`_LineRecord`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `{'record_id': record.record_id, 'page_number': record.page_number, 'page_line_number': record.page_line_number, 'raw_text': record.raw}`.

**Algorithm**

1. Returns `{'record_id': record.record_id, 'page_number': record.page_number, 'page_line_number': record.page_line_number, 'raw_text': record.raw}`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_source_records_sha256`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_source_records_sha256`

**Signature**

```python
def _source_records_sha256(records: Sequence[_LineRecord]) -> str:
```

**Purpose**

Implements source records sha256 according to the exact implementation and guards in this file.

**Inputs**

- `records` (`Sequence[_LineRecord]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_sha256({'domain': 'landscout.planning_regulation.source_records', 'section_hash_schema_version': SECTION_HASH_SCHEMA_VERSION, 'records': [_source_record_payload(record) for record in records]})`.

**Algorithm**

1. Returns `_canonical_sha256({'domain': 'landscout.planning_regulation.source_records', 'section_hash_schema_version': SECTION_HASH_SCHEMA_VERSION, 'records': [_source_record_payload(record) for record in records]})`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_sha256`, `_source_record_payload`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_build_sections`
- `src/landscout/stages/structure_planning_regulation.py` — `_build_structure_result`
- `src/landscout/stages/structure_planning_regulation.py` — `_validate_sections`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_chapter_label`

**Signature**

```python
def _canonical_chapter_label(value: str) -> str:
```

**Purpose**

Implements canonical chapter label according to the exact implementation and guards in this file.

**Inputs**

- `value` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_strict_string(label, 'zone chapter label')`.

**Algorithm**

1. Computes `label` from `re.sub('\\s+', '', value)`.
2. Returns `_strict_string(label, 'zone chapter label')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_strict_string`, `re.sub`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_heading_events`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_classify_structural_heading`

**Signature**

```python
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
```

**Purpose**

Implements classify structural heading according to the exact implementation and guards in this file.

**Inputs**

- `record` (`_LineRecord`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `value` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `pattern_groups` (`Sequence[tuple[Literal['GENERAL', 'ZONE_CHAPTER', 'ARTICLE'], Sequence[re.Pattern[str]]]]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `_StructuralHeadingMatch | None`. Observed return expression(s): `matches[0] if matches else None`.

**Algorithm**

1. Defines `matches` with annotation `list[_StructuralHeadingMatch]` from `[]`.
2. Iterates `(section_type, patterns)` over `pattern_groups`. For each value: Iterates `(pattern_index, pattern)` over `enumerate(patterns)`. For each value: Computes `match` from `pattern.fullmatch(value)`. Checks `match is None`. When true: Executes `continue` control flow. Calls `matches.append(_StructuralHeadingMatch(section_type=section_type, pattern_index=pattern_index, named_captures=tuple(match.groupdict().items())))` for its validation or side effect.
3. Checks `len(matches) > 1`. When true: Computes `diagnostics` from `', '.join((f'{match.section_type}[{match.pattern_index}]' for match in matches))`. Raises `PlanningRegulationStructureError(f'Ambiguous structural heading at {record.record_id}, page {record.page_number}, line {record.page_line_number}: {diagnostics}')`.
4. Returns `matches[0] if matches else None`.

**Validation and invariants**

- Rejects or diverts the path when `len(matches) > 1` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `', '.join`, `PlanningRegulationStructureError`, `_StructuralHeadingMatch`, `enumerate`, `len`, `match.groupdict`, `match.groupdict().items`, `matches.append`, `pattern.fullmatch`, `tuple`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_heading_events`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_heading_events`

**Signature**

```python
def _heading_events(
    records: Sequence[_LineRecord],
    config: PlanningRegulationStructureConfig,
) -> list[_HeadingEvent]:
```

**Purpose**

Implements heading events according to the exact implementation and guards in this file.

**Inputs**

- `records` (`Sequence[_LineRecord]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`PlanningRegulationStructureConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `list[_HeadingEvent]`. Observed return expression(s): `events`.

**Algorithm**

1. Computes `zones` from `_compiled(config.heading_patterns.zone_chapter)`.
2. Computes `articles` from `_compiled(config.heading_patterns.article)`.
3. Computes `generals` from `_compiled(config.heading_patterns.general_section)`.
4. Computes `continuations` from `_compiled(config.heading_patterns.continuation)`.
5. Defines `structural_patterns` with annotation `tuple[tuple[Literal['GENERAL', 'ZONE_CHAPTER', 'ARTICLE'], Sequence[re.Pattern[str]]], ...]` from `(('ZONE_CHAPTER', zones), ('GENERAL', generals), ('ARTICLE', articles))`.
6. Computes `toc_pages` from `set(config.document_layout.table_of_contents_pages)`.
7. Defines `events` with annotation `list[_HeadingEvent]` from `[]`.
8. Computes `position` from `0`.
9. Repeats the guarded body while `position < len(records)` remains true.
10. Checks `not events`. When true: Raises `PlanningRegulationStructureError('No regulation body headings matched the configured grammar')`.
11. Returns `events`.

**Validation and invariants**

- Rejects or diverts the path when `not events` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `' '.join`, `' '.join([title.strip(), *continuation_titles]).strip`, `'\n'.join`, `PlanningRegulationStructureError`, `_HeadingEvent`, `_canonical_chapter_label`, `_classify_structural_heading`, `_compiled`, `_matches_any`, `_normalize_search_text`, `dict`, `events.append`, `groups.get`, `heading_lines.append`, `len`, `line.strip`, `record.raw.strip`, `records[cursor].raw.strip`, `set`, `title.strip`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_build_sections`
- `tests/unit/test_structure_planning_regulation.py` — `test_unique_zone_heading_and_nonheading_line_are_classified_deterministically`

**Tests**

- `tests/unit/test_structure_planning_regulation.py::test_unique_zone_heading_and_nonheading_line_are_classified_deterministically`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_page_fragments`

**Signature**

```python
def _page_fragments(records: Sequence[_LineRecord]) -> tuple[tuple[int, str], ...]:
```

**Purpose**

Implements page fragments according to the exact implementation and guards in this file.

**Inputs**

- `records` (`Sequence[_LineRecord]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[tuple[int, str], ...]`. Observed return expression(s): `tuple(fragments)`.

**Algorithm**

1. Defines `fragments` with annotation `list[tuple[int, str]]` from `[]`.
2. Defines `current_page` with annotation `int | None` from `None`.
3. Defines `lines` with annotation `list[str]` from `[]`.
4. Iterates `record` over `records`. For each value: Checks `current_page is not None and record.page_number != current_page`. When true: Calls `fragments.append((current_page, '\n'.join(lines)))` for its validation or side effect. Computes `lines` from `[]`. Computes `current_page` from `record.page_number`. Calls `lines.append(record.raw)` for its validation or side effect.
5. Checks `current_page is not None`. When true: Calls `fragments.append((current_page, '\n'.join(lines)))` for its validation or side effect.
6. Returns `tuple(fragments)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `'\n'.join`, `fragments.append`, `lines.append`, `tuple`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_build_sections`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_contiguous_page_blocks`

**Signature**

```python
def _contiguous_page_blocks(pages: Sequence[int]) -> tuple[tuple[int, ...], ...]:
```

**Purpose**

Implements contiguous page blocks according to the exact implementation and guards in this file.

**Inputs**

- `pages` (`Sequence[int]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[tuple[int, ...], ...]`. Observed return expression(s): `tuple((tuple(block) for block in blocks))`; `()`.

**Algorithm**

1. Checks `not pages`. When true: Returns `()`.
2. Defines `blocks` with annotation `list[list[int]]` from `[[pages[0]]]`.
3. Iterates `page` over `pages[1:]`. For each value: Checks `page == blocks[-1][-1] + 1`. When true: Calls `blocks[-1].append(page)` for its validation or side effect. Otherwise: Calls `blocks.append([page])` for its validation or side effect.
4. Returns `tuple((tuple(block) for block in blocks))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `blocks.append`, `blocks[-1].append`, `tuple`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_section_starts`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_section_starts`

**Signature**

```python
def _section_starts(
    records: Sequence[_LineRecord],
    events: Sequence[_HeadingEvent],
    config: PlanningRegulationStructureConfig,
) -> list[_SectionBoundary]:
```

**Purpose**

Implements section starts according to the exact implementation and guards in this file.

**Inputs**

- `records` (`Sequence[_LineRecord]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `events` (`Sequence[_HeadingEvent]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`PlanningRegulationStructureConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `list[_SectionBoundary]`. Observed return expression(s): `coalesced`.

**Algorithm**

1. Defines `starts_by_position` with annotation `dict[int, _SectionBoundary]` from `{event.record_position: _SectionBoundary(record_position=event.record_position, event=event, forced_table_of_contents=False) for event in events}`.
2. Defines `record_positions_by_page` with annotation `dict[int, list[int]]` from `{}`.
3. Iterates `(position, record)` over `enumerate(records)`. For each value: Calls `record_positions_by_page.setdefault(record.page_number, []).append(position)` for its validation or side effect.
4. Iterates `block` over `_contiguous_page_blocks(config.document_layout.table_of_contents_pages)`. For each value: Computes `positions` from `[position for page in block for position in record_positions_by_page.get(page, [])]`. Checks `not positions`. When true: Executes `continue` control flow. Computes `block_start` from `min(positions)`. Executes 3 additional source-ordered statement(s).
5. Computes `ordered` from `sorted(starts_by_position.values(), key=lambda boundary: boundary.record_position)`.
6. Computes `toc_pages` from `set(config.document_layout.table_of_contents_pages)`.
7. Iterates `(boundary_index, boundary)` over `enumerate(ordered)`. For each value: Checks `boundary.event is None`. When true: Executes `continue` control flow. Computes `minimum_position` from `ordered[boundary_index - 1].record_position if boundary_index > 0 else 0`. Computes `shifted_position` from `boundary.record_position`. Executes 2 additional source-ordered statement(s).
8. Defines `compacted` with annotation `dict[int, _SectionBoundary]` from `{}`.
9. Iterates `boundary` over `ordered`. For each value: Computes `existing` from `compacted.get(boundary.record_position)`. Checks `existing is None or boundary.forced_table_of_contents or (not existing.forced_table_of_contents and boundary.event is not None)`. When true: Computes `compacted[boundary.record_position]` from `boundary`.
10. Computes `ordered` from `sorted(compacted.values(), key=lambda boundary: boundary.record_position)`.
11. Checks `not ordered`. When true: Raises `PlanningRegulationStructureError('No regulation section boundary could be established')`.
12. Computes `first_boundary` from `ordered[0]`.
13. Checks `first_boundary.record_position > 0`. When true: Computes `prefix` from `records[:first_boundary.record_position]`. Checks `any((record.raw.strip() for record in prefix))`. When true: Calls `ordered.insert(0, _SectionBoundary(record_position=0, event=None, forced_table_of_contents=False))` for its validation or side effect. Otherwise: Computes `ordered[0]` from `replace(first_boundary, record_position=0)`.
14. Defines `coalesced` with annotation `list[_SectionBoundary]` from `[]`.
15. Iterates `(boundary_index, boundary)` over `enumerate(ordered)`. For each value: Computes `start` from `boundary.record_position`. Computes `end` from `ordered[boundary_index + 1].record_position if boundary_index + 1 < len(ordered) else len(records)`. Checks `not boundary.forced_table_of_contents and boundary.event is None and (not any((record.raw.strip() for record in records[start:end])))`. When true: Checks `boundary_index + 1 < len(ordered)`. When true: Computes `ordered[boundary_index + 1]` from `replace(ordered[boundary_index + 1], record_position=start)`. Executes `continue` control flow. Checks `coalesced`. When true: Executes `continue` control flow. Executes 1 additional source-ordered statement(s).
16. Returns `coalesced`.

**Validation and invariants**

- Rejects or diverts the path when `not ordered` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `PlanningRegulationStructureError`, `_SectionBoundary`, `_contiguous_page_blocks`, `any`, `coalesced.append`, `compacted.get`, `compacted.values`, `enumerate`, `len`, `max`, `min`, `ordered.insert`, `record.raw.strip`, `record_positions_by_page.get`, `record_positions_by_page.setdefault`, `record_positions_by_page.setdefault(record.page_number, []).append`, `records[shifted_position - 1].raw.strip`, `replace`, `set`, `sorted`, `starts_by_position.values`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_build_sections`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_section_content_sha256`

**Signature**

```python
def _section_content_sha256(row: Mapping[str, object]) -> str:
```

**Purpose**

Implements section content sha256 according to the exact implementation and guards in this file.

**Inputs**

- `row` (`Mapping[str, object]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_sha256({'domain': 'landscout.planning_regulation.section', 'section_hash_schema_version': SECTION_HASH_SCHEMA_VERSION, 'section': content})`.

**Algorithm**

1. Computes `content` from `{column: row[column] for column in SECTION_COLUMNS if column != 'section_content_sha256'}`.
2. Returns `_canonical_sha256({'domain': 'landscout.planning_regulation.section', 'section_hash_schema_version': SECTION_HASH_SCHEMA_VERSION, 'section': content})`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_sha256`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_build_sections`
- `src/landscout/stages/structure_planning_regulation.py` — `_validate_sections`
- `tests/unit/test_structure_planning_regulation.py` — `test_coordinated_section_row_mutation_is_caught_by_outer_envelope`

**Tests**

- `tests/unit/test_structure_planning_regulation.py::test_coordinated_section_row_mutation_is_caught_by_outer_envelope`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_build_sections`

**Signature**

```python
def _build_sections(
    index: PlanningRegulationIndex,
    config: PlanningRegulationStructureConfig,
) -> tuple[pd.DataFrame, tuple[_SectionBuild, ...], tuple[_LineRecord, ...]]:
```

**Purpose**

Builds sections according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`PlanningRegulationStructureConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[pd.DataFrame, tuple[_SectionBuild, ...], tuple[_LineRecord, ...]]`. Observed return expression(s): `(frame, tuple(builds), tuple(records))`.

**Algorithm**

1. Computes `records` from `_line_records(index, config)`.
2. Computes `events` from `_heading_events(records, config)`.
3. Computes `starts` from `_section_starts(records, events, config)`.
4. Defines `builds` with annotation `list[_SectionBuild]` from `[]`.
5. Defines `current_chapter_id` with annotation `str | None` from `None`.
6. Defines `current_chapter_label` with annotation `str | None` from `None`.
7. Iterates `(start_index, boundary)` over `enumerate(starts)`. For each value: Computes `start` from `boundary.record_position`. Computes `event` from `boundary.event`. Computes `end` from `starts[start_index + 1].record_position if start_index + 1 < len(starts) else len(records)`. Executes 10 additional source-ordered statement(s).
8. Computes `frame` from `pd.DataFrame([build.row for build in builds], columns=SECTION_COLUMNS)`.
9. Computes `frame['start_page']` from `frame['start_page'].astype('int64')`.
10. Computes `frame['end_page']` from `frame['end_page'].astype('int64')`.
11. Computes `frame['source_record_count']` from `frame['source_record_count'].astype('int64')`.
12. Computes `frame['character_count']` from `frame['character_count'].astype('int64')`.
13. Returns `(frame, tuple(builds), tuple(records))`.

**Validation and invariants**

- Rejects or diverts the path when `section_type == 'ARTICLE'` is true.
- Rejects or diverts the path when `current_chapter_id is None or current_chapter_label is None` is true.
- Rejects or diverts the path when `event.zone_chapter_label is None or event.zone_chapter_label.casefold() != current_chapter_label.casefold()` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `'\n'.join`, `PlanningRegulationStructureError`, `_SectionBuild`, `_heading_events`, `_line_records`, `_normalize_search_text`, `_page_fragments`, `_section_content_sha256`, `_section_starts`, `_source_records_sha256`, `builds.append`, `current_chapter_label.casefold`, `enumerate`, `event.zone_chapter_label.casefold`, `frame['character_count'].astype`, `frame['end_page'].astype`, `frame['source_record_count'].astype`, `frame['start_page'].astype`, `len`, `next`, `pd.DataFrame`, `record.raw.strip`, `tuple`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_build_structure_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_source_label_values`

**Signature**

```python
def _validate_source_label_values(series: pd.Series, label: str) -> None:
```

**Purpose**

Validates and rejects malformed source label values according to the exact implementation and guards in this file.

**Inputs**

- `series` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Iterates `value` over `series.tolist()`. For each value: Calls `_strict_string(value, label)` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_strict_string`, `series.tolist`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_validated_zoning_inputs`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validated_zoning_inputs`

**Signature**

```python
def _validated_zoning_inputs(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
    intersections: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
```

**Purpose**

Validates and returns canonical zoning inputs according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zones` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `intersections` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[pd.DataFrame, pd.DataFrame]`. Observed return expression(s): `(zone_copy, relation_copy)`.

**Algorithm**

1. Checks `not isinstance(zones, pd.DataFrame) or not isinstance(intersections, pd.DataFrame)`. When true: Raises `PlanningRegulationStructureError('Zones and zoning intersections must be DataFrames')`.
2. Computes `zone_required` from `{'planning_zone_id', 'source_zone_id', 'zone_label_raw', 'source_document_id', 'source_archive_sha256'}`.
3. Computes `relation_required` from `{'parcel_id', 'planning_zone_id', 'source_zone_id', 'zone_label_raw', 'relation_type', 'intersection_area_m2', 'source_document_id', 'source_archive_sha256'}`.
4. Computes `missing_zones` from `sorted(zone_required.difference(zones.columns))`.
5. Computes `missing_relations` from `sorted(relation_required.difference(intersections.columns))`.
6. Checks `missing_zones`. When true: Raises `PlanningRegulationStructureError(f'Zone catalog is missing required columns: {missing_zones}')`.
7. Checks `missing_relations`. When true: Raises `PlanningRegulationStructureError(f'Zoning intersections are missing required columns: {missing_relations}')`.
8. Computes `zone_copy` from `zones.copy(deep=True)`.
9. Computes `relation_copy` from `intersections.copy(deep=True)`.
10. Calls `_validate_source_label_values(zone_copy['planning_zone_id'], 'planning zone ID')` for its validation or side effect.
11. Calls `_validate_source_label_values(zone_copy['source_zone_id'], 'source zone ID')` for its validation or side effect.
12. Calls `_validate_source_label_values(zone_copy['zone_label_raw'], 'zone label')` for its validation or side effect.
13. Checks `zone_copy['planning_zone_id'].duplicated().any()`. When true: Raises `PlanningRegulationStructureError('Planning zone IDs must be unique')`.
14. Checks `zone_copy['source_zone_id'].duplicated().any()`. When true: Raises `PlanningRegulationStructureError('Source zone IDs must be unique')`.
15. Iterates `column` over `('source_document_id', 'source_archive_sha256')`. For each value: Calls `_validate_source_label_values(zone_copy[column], f'zone {column}')` for its validation or side effect.
16. Checks `not zone_copy['source_document_id'].eq(index.document_id).all()`. When true: Raises `PlanningRegulationStructureError('Zone document lineage differs from index')`.
17. Checks `not zone_copy['source_archive_sha256'].eq(index.archive_sha256).all()`. When true: Raises `PlanningRegulationStructureError('Zone archive lineage differs from index')`.
18. Iterates `column` over `('parcel_id', 'planning_zone_id', 'source_zone_id', 'zone_label_raw')`. For each value: Calls `_validate_source_label_values(relation_copy[column], f'intersection {column}')` for its validation or side effect.
19. Checks `relation_copy.duplicated(['parcel_id', 'planning_zone_id']).any()`. When true: Raises `PlanningRegulationStructureError('Parcel/zone intersection pairs must be unique')`.
20. Computes `known` from `set(zone_copy['planning_zone_id'].tolist())`.
21. Checks `not set(relation_copy['planning_zone_id'].tolist()).issubset(known)`. When true: Raises `PlanningRegulationStructureError('Zoning intersections reference an unknown planning zone')`.
22. Computes `catalog_by_id` from `zone_copy.set_index('planning_zone_id')`.
23. Computes `expected_labels` from `relation_copy['planning_zone_id'].map(catalog_by_id['zone_label_raw'])`.
24. Checks `not expected_labels.eq(relation_copy['zone_label_raw']).all()`. When true: Raises `PlanningRegulationStructureError('Intersection zone labels differ from the zone catalog')`.
25. Computes `expected_source_ids` from `relation_copy['planning_zone_id'].map(catalog_by_id['source_zone_id'])`.
26. Checks `not expected_source_ids.eq(relation_copy['source_zone_id']).all()`. When true: Raises `PlanningRegulationStructureError('Intersection source-zone IDs differ from the zone catalog')`.
27. Checks `not relation_copy['source_document_id'].eq(index.document_id).all()`. When true: Raises `PlanningRegulationStructureError('Intersection document lineage differs from index')`.
28. Checks `not relation_copy['source_archive_sha256'].eq(index.archive_sha256).all()`. When true: Raises `PlanningRegulationStructureError('Intersection archive lineage differs from index')`.
29. Computes `allowed_relations` from `{'AREA_OVERLAP', 'TOUCH_ONLY'}`.
30. Checks `not set(relation_copy['relation_type'].tolist()).issubset(allowed_relations)`. When true: Raises `PlanningRegulationStructureError('Zoning relation type is invalid')`.
31. Defines `metrics` with annotation `list[float]` from `[]`.
32. Iterates `value` over `relation_copy['intersection_area_m2'].tolist()`. For each value: Checks `isinstance(value, bool) or not isinstance(value, Real)`. When true: Raises `PlanningRegulationStructureError('Intersection areas must be numeric')`. Runs guarded operation: Computes `numeric` from `float(value)`. Handles `(TypeError, ValueError, OverflowError)`. Checks `not math.isfinite(numeric) or numeric < 0`. When true: Raises `PlanningRegulationStructureError('Intersection areas must be finite and non-negative')`. Executes 1 additional source-ordered statement(s).
33. Computes `relation_copy['intersection_area_m2']` from `pd.Series(metrics, index=relation_copy.index, dtype='float64')`.
34. Computes `positive` from `relation_copy['intersection_area_m2'].gt(0)`.
35. Checks `not relation_copy.loc[positive, 'relation_type'].eq('AREA_OVERLAP').all()`. When true: Raises `PlanningRegulationStructureError('Positive zoning relations must be AREA_OVERLAP')`.
36. Checks `not relation_copy.loc[~positive, 'relation_type'].eq('TOUCH_ONLY').all()`. When true: Raises `PlanningRegulationStructureError('Zero-area zoning relations must be TOUCH_ONLY')`.
37. Iterates `upper_column` over `('parcel_metric_area_m2', 'zone_area_m2')`. For each value: Checks `upper_column not in relation_copy.columns`. When true: Executes `continue` control flow. Iterates `(area, upper)` over `zip(relation_copy['intersection_area_m2'].tolist(), relation_copy[upper_column].tolist(), strict=True)`. For each value: Checks `isinstance(upper, bool) or not isinstance(upper, Real)`. When true: Raises `PlanningRegulationStructureError(f'{upper_column} must be numeric')`. Runs guarded operation: Computes `numeric_upper` from `float(upper)`. Handles `(TypeError, ValueError, OverflowError)`. Checks `not math.isfinite(numeric_upper) or numeric_upper < 0`. When true: Raises `PlanningRegulationStructureError(f'{upper_column} must be finite and non-negative')`. Executes 1 additional source-ordered statement(s).
38. Returns `(zone_copy, relation_copy)`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(zones, pd.DataFrame) or not isinstance(intersections, pd.DataFrame)` is true.
- Rejects or diverts the path when `missing_zones` is true.
- Rejects or diverts the path when `missing_relations` is true.
- Rejects or diverts the path when `zone_copy['planning_zone_id'].duplicated().any()` is true.
- Rejects or diverts the path when `zone_copy['source_zone_id'].duplicated().any()` is true.
- Rejects or diverts the path when `not zone_copy['source_document_id'].eq(index.document_id).all()` is true.
- Rejects or diverts the path when `not zone_copy['source_archive_sha256'].eq(index.archive_sha256).all()` is true.
- Rejects or diverts the path when `relation_copy.duplicated(['parcel_id', 'planning_zone_id']).any()` is true.
- Rejects or diverts the path when `not set(relation_copy['planning_zone_id'].tolist()).issubset(known)` is true.
- Rejects or diverts the path when `not expected_labels.eq(relation_copy['zone_label_raw']).all()` is true.
- Rejects or diverts the path when `not expected_source_ids.eq(relation_copy['source_zone_id']).all()` is true.
- Rejects or diverts the path when `not relation_copy['source_document_id'].eq(index.document_id).all()` is true.
- Rejects or diverts the path when `not relation_copy['source_archive_sha256'].eq(index.archive_sha256).all()` is true.
- Rejects or diverts the path when `not set(relation_copy['relation_type'].tolist()).issubset(allowed_relations)` is true.
- Rejects or diverts the path when `not relation_copy.loc[positive, 'relation_type'].eq('AREA_OVERLAP').all()` is true.
- Rejects or diverts the path when `not relation_copy.loc[~positive, 'relation_type'].eq('TOUCH_ONLY').all()` is true.
- Rejects or diverts the path when `isinstance(value, bool) or not isinstance(value, Real)` is true.
- Rejects or diverts the path when `not math.isfinite(numeric) or numeric < 0` is true.
- Rejects or diverts the path when `isinstance(upper, bool) or not isinstance(upper, Real)` is true.
- Rejects or diverts the path when `not math.isfinite(numeric_upper) or numeric_upper < 0` is true.
- Rejects or diverts the path when `area - numeric_upper > technical_overlay_tolerance(numeric_upper)` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `expected_labels.eq(relation_copy['zone_label_raw']).all`, `expected_source_ids.eq(relation_copy['source_zone_id']).all`, `intersections.copy`, `relation_copy.duplicated`, `relation_copy.duplicated(['parcel_id', 'planning_zone_id']).any`, `relation_copy.loc[positive, 'relation_type'].eq`, `relation_copy.loc[positive, 'relation_type'].eq('AREA_OVERLAP').all`, `relation_copy.loc[~positive, 'relation_type'].eq`, `relation_copy.loc[~positive, 'relation_type'].eq('TOUCH_ONLY').all`, `relation_copy['intersection_area_m2'].gt`, `relation_copy['intersection_area_m2'].tolist`, `relation_copy['planning_zone_id'].map`, `relation_copy['planning_zone_id'].tolist`, `relation_copy['relation_type'].tolist`, `relation_copy['source_archive_sha256'].eq`, `relation_copy['source_archive_sha256'].eq(index.archive_sha256).all`, `relation_copy['source_document_id'].eq`, `relation_copy['source_document_id'].eq(index.document_id).all`, `relation_copy[upper_column].tolist`, `set(relation_copy['planning_zone_id'].tolist()).issubset`, `set(relation_copy['relation_type'].tolist()).issubset`, `zone_copy.set_index`, `zone_copy['planning_zone_id'].duplicated`, `zone_copy['planning_zone_id'].duplicated().any`, `zone_copy['planning_zone_id'].tolist`, `zone_copy['source_archive_sha256'].eq`, `zone_copy['source_archive_sha256'].eq(index.archive_sha256).all`, `zone_copy['source_document_id'].eq`, `zone_copy['source_document_id'].eq(index.document_id).all`, `zone_copy['source_zone_id'].duplicated`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `PlanningRegulationStructureError`, `_validate_source_label_values`, `expected_labels.eq`, `expected_labels.eq(relation_copy['zone_label_raw']).all`, `expected_source_ids.eq`, `expected_source_ids.eq(relation_copy['source_zone_id']).all`, `float`, `intersections.copy`, `isinstance`, `math.isfinite`, `metrics.append`, `pd.Series`, `relation_copy.duplicated`, `relation_copy.duplicated(['parcel_id', 'planning_zone_id']).any`, `relation_copy.loc[positive, 'relation_type'].eq`, `relation_copy.loc[positive, 'relation_type'].eq('AREA_OVERLAP').all`, `relation_copy.loc[~positive, 'relation_type'].eq`, `relation_copy.loc[~positive, 'relation_type'].eq('TOUCH_ONLY').all`, `relation_copy['intersection_area_m2'].gt`, `relation_copy['intersection_area_m2'].tolist`, `relation_copy['planning_zone_id'].map`, `relation_copy['planning_zone_id'].tolist`, `relation_copy['relation_type'].tolist`, `relation_copy['source_archive_sha256'].eq`, `relation_copy['source_archive_sha256'].eq(index.archive_sha256).all`, `relation_copy['source_document_id'].eq`, `relation_copy['source_document_id'].eq(index.document_id).all`, `relation_copy[upper_column].tolist`, `relation_required.difference`, `set`, `set(relation_copy['planning_zone_id'].tolist()).issubset`, `set(relation_copy['relation_type'].tolist()).issubset`, `sorted`, `technical_overlay_tolerance`, `zip`, `zone_copy.set_index`, `zone_copy['planning_zone_id'].duplicated`, `zone_copy['planning_zone_id'].duplicated().any`, `zone_copy['planning_zone_id'].tolist`, `zone_copy['source_archive_sha256'].eq`, `zone_copy['source_archive_sha256'].eq(index.archive_sha256).all`, `zone_copy['source_document_id'].eq`, `zone_copy['source_document_id'].eq(index.document_id).all`, `zone_copy['source_zone_id'].duplicated`, `zone_copy['source_zone_id'].duplicated().any`, `zone_required.difference`, `zones.copy`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `structure_planning_regulation`
- `src/landscout/stages/structure_planning_regulation.py` — `validate_planning_regulation_structure_with_fragments`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_input_frame_sha256`

**Signature**

```python
def _input_frame_sha256(
    domain: str,
    frame: pd.DataFrame,
    columns: Sequence[str],
) -> str:
```

**Purpose**

Implements input frame sha256 according to the exact implementation and guards in this file.

**Inputs**

- `domain` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `columns` (`Sequence[str]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_sha256({'domain': domain, 'columns': list(columns), 'rows': frame.loc[:, columns].to_dict('records')})`.

**Algorithm**

1. Returns `_canonical_sha256({'domain': domain, 'columns': list(columns), 'rows': frame.loc[:, columns].to_dict('records')})`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_sha256`, `frame.loc[:, columns].to_dict`, `list`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_build_structure_result`
- `src/landscout/stages/structure_planning_regulation.py` — `_validate_result_self`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_intersection_hash_columns`

**Signature**

```python
def _intersection_hash_columns(frame: pd.DataFrame) -> tuple[str, ...]:
```

**Purpose**

Implements intersection hash columns according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[str, ...]`. Observed return expression(s): `_REQUIRED_INTERSECTION_INPUT_COLUMNS + tuple((column for column in _OPTIONAL_INTERSECTION_INPUT_COLUMNS if column in frame.columns))`.

**Algorithm**

1. Returns `_REQUIRED_INTERSECTION_INPUT_COLUMNS + tuple((column for column in _OPTIONAL_INTERSECTION_INPUT_COLUMNS if column in frame.columns))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `tuple`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_build_structure_result`
- `src/landscout/stages/structure_planning_regulation.py` — `_validate_result_self`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_resolved_alias`

**Signature**

```python
def _resolved_alias(label: str, aliases: Mapping[str, str]) -> str | None:
```

**Purpose**

Implements resolved alias according to the exact implementation and guards in this file.

**Inputs**

- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `aliases` (`Mapping[str, str]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str | None`. Observed return expression(s): `current`; `None`.

**Algorithm**

1. Checks `label not in aliases`. When true: Returns `None`.
2. Computes `current` from `label`.
3. Defines `visited` with annotation `set[str]` from `set()`.
4. Repeats the guarded body while `current in aliases` remains true.
5. Returns `current`.

**Validation and invariants**

- Rejects or diverts the path when `current in visited` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationStructureError`, `set`, `visited.add`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_build_zone_mapping`
- `src/landscout/stages/structure_planning_regulation.py` — `_validate_zone_mapping`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_dominant_counts`

**Signature**

```python
def _dominant_counts(intersections: pd.DataFrame) -> Counter[str]:
```

**Purpose**

Implements dominant counts according to the exact implementation and guards in this file.

**Inputs**

- `intersections` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Counter[str]`. Observed return expression(s): `Counter(selected['zone_label_raw'].tolist())`; `Counter()`.

**Algorithm**

1. Computes `positive` from `intersections.loc[intersections['intersection_area_m2'].gt(0), ['parcel_id', 'planning_zone_id', 'zone_label_raw', 'intersection_area_m2']].copy()`.
2. Checks `positive.empty`. When true: Returns `Counter()`.
3. Computes `positive` from `positive.sort_values(['parcel_id', 'intersection_area_m2', 'planning_zone_id'], ascending=[True, False, True], kind='mergesort')`.
4. Computes `selected` from `positive.drop_duplicates('parcel_id', keep='first')`.
5. Returns `Counter(selected['zone_label_raw'].tolist())`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `intersections.loc[intersections['intersection_area_m2'].gt(0), ['parcel_id', 'planning_zone_id', 'zone_label_raw', 'intersection_area_m2']].copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `Counter`, `intersections.loc[intersections['intersection_area_m2'].gt(0), ['parcel_id', 'planning_zone_id', 'zone_label_raw', 'intersection_area_m2']].copy`, `intersections['intersection_area_m2'].gt`, `positive.drop_duplicates`, `positive.sort_values`, `selected['zone_label_raw'].tolist`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_build_zone_mapping`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_build_zone_mapping`

**Signature**

```python
def _build_zone_mapping(
    index: PlanningRegulationIndex,
    config: PlanningRegulationStructureConfig,
    sections: pd.DataFrame,
    zones: pd.DataFrame,
    intersections: pd.DataFrame,
) -> pd.DataFrame:
```

**Purpose**

Builds zone mapping according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`PlanningRegulationStructureConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `sections` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zones` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `intersections` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `frame`.

**Algorithm**

1. Computes `chapters` from `sections.loc[sections['section_type'].eq('ZONE_CHAPTER'), ['section_id', 'zone_chapter_label']]`.
2. Defines `chapters_by_label` with annotation `dict[str, list[str]]` from `{}`.
3. Iterates `row` over `chapters.to_dict('records')`. For each value: Computes `label` from `_strict_string(row['zone_chapter_label'], 'zone chapter label')`. Calls `chapters_by_label.setdefault(label, []).append(row['section_id'])` for its validation or side effect.
4. Computes `zone_counts` from `Counter(zones['zone_label_raw'].tolist())`.
5. Computes `parcel_counts` from `intersections.groupby('zone_label_raw', sort=False)['parcel_id'].nunique().to_dict()`.
6. Computes `intersection_counts` from `Counter(intersections['zone_label_raw'].tolist())`.
7. Computes `dominant_counts` from `_dominant_counts(intersections)`.
8. Defines `rows` with annotation `list[dict[str, object]]` from `[]`.
9. Iterates `label` over `sorted(zone_counts)`. For each value: Computes `exact_sections` from `chapters_by_label.get(label, [])`. Defines `resolved` with annotation `str | None` from `None`. Defines `matched` with annotation `str | None` from `None`. Executes 2 additional source-ordered statement(s).
10. Computes `frame` from `pd.DataFrame(rows, columns=ZONE_MAPPING_COLUMNS)`.
11. Iterates `column` over `('zone_polygon_count', 'candidate_parcel_count', 'candidate_intersection_count', 'dominant_candidate_count')`. For each value: Computes `frame[column]` from `frame[column].astype('int64')`.
12. Computes `unresolved_dominant` from `frame.loc[frame['dominant_candidate_count'].gt(0) & ~frame['mapping_status'].isin({'EXACT', 'CONFIG_ALIAS'}), 'source_zone_label_raw'].tolist()`.
13. Checks `unresolved_dominant`. When true: Raises `PlanningRegulationStructureError(f'Dominant candidate zone labels lack an exact configured chapter mapping: {unresolved_dominant}')`.
14. Returns `frame`.

**Validation and invariants**

- Rejects or diverts the path when `unresolved_dominant` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `Counter`, `PlanningRegulationStructureError`, `_dominant_counts`, `_resolved_alias`, `_strict_string`, `chapters.to_dict`, `chapters_by_label.get`, `chapters_by_label.setdefault`, `chapters_by_label.setdefault(label, []).append`, `frame.loc[frame['dominant_candidate_count'].gt(0) & ~frame['mapping_status'].isin({'EXACT', 'CONFIG_ALIAS'}), 'source_zone_label_raw'].tolist`, `frame['dominant_candidate_count'].gt`, `frame['mapping_status'].isin`, `frame[column].astype`, `int`, `intersections.groupby`, `intersections.groupby('zone_label_raw', sort=False)['parcel_id'].nunique`, `intersections.groupby('zone_label_raw', sort=False)['parcel_id'].nunique().to_dict`, `intersections['zone_label_raw'].tolist`, `len`, `parcel_counts.get`, `pd.DataFrame`, `rows.append`, `sections['section_type'].eq`, `sorted`, `zones['zone_label_raw'].tolist`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_build_structure_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_is_token_character`

**Signature**

```python
def _is_token_character(value: str) -> bool:
```

**Purpose**

Returns whether `token character` satisfies the exact predicates and branches listed below.

**Inputs**

- `value` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `value.isalnum() or value == '_'`.

**Algorithm**

1. Returns `value.isalnum() or value == '_'`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `value.isalnum`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_literal_topic_matches`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_literal_topic_matches`

**Signature**

```python
def _literal_topic_matches(
    normalized_text: str,
    terms: Sequence[str],
) -> tuple[_TopicMatch, ...]:
```

**Purpose**

Implements literal topic matches according to the exact implementation and guards in this file.

**Inputs**

- `normalized_text` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `terms` (`Sequence[str]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[_TopicMatch, ...]`. Observed return expression(s): `tuple(sorted(selected, key=lambda item: (item.normalized_start, item.term_index)))`.

**Algorithm**

1. Defines `candidates` with annotation `list[_TopicMatch]` from `[]`.
2. Iterates `(term_index, search_term)` over `enumerate(terms)`. For each value: Computes `normalized_term` from `_normalize_search_text(search_term)`. Computes `cursor` from `0`. Repeats the guarded body while `True` remains true.
3. Defines `selected` with annotation `list[_TopicMatch]` from `[]`.
4. Iterates `candidate` over `sorted(candidates, key=lambda item: (-(item.normalized_end - item.normalized_start), item.term_index, item.normalized_start))`. For each value: Checks `any((candidate.normalized_start < existing.normalized_end and existing.normalized_start < candidate.normalized_end for existing in selected))`. When true: Executes `continue` control flow. Calls `selected.append(candidate)` for its validation or side effect.
5. Returns `tuple(sorted(selected, key=lambda item: (item.normalized_start, item.term_index)))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_TopicMatch`, `_is_token_character`, `_normalize_search_text`, `any`, `candidates.append`, `enumerate`, `len`, `normalized_text.find`, `selected.append`, `sorted`, `tuple`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_build_topic_evidence`
- `src/landscout/stages/structure_planning_regulation.py` — `_validate_topic_evidence`
- `tests/unit/test_structure_planning_regulation.py` — `test_equal_length_overlap_uses_configured_term_order_as_tie_break`
- `tests/unit/test_structure_planning_regulation.py` — `test_token_boundary_and_longest_match_policy`

**Tests**

- `tests/unit/test_structure_planning_regulation.py::test_equal_length_overlap_uses_configured_term_order_as_tie_break`
- `tests/unit/test_structure_planning_regulation.py::test_token_boundary_and_longest_match_policy`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_evidence_scope`

**Signature**

```python
def _evidence_scope(section_type: str) -> str:
```

**Purpose**

Implements evidence scope according to the exact implementation and guards in this file.

**Inputs**

- `section_type` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `'GENERAL_RULE'`; `'ZONE_SPECIFIC_RULE'`; `'OTHER_TEXT'`.

**Algorithm**

1. Checks `section_type == 'GENERAL'`. When true: Returns `'GENERAL_RULE'`.
2. Checks `section_type in {'ZONE_CHAPTER', 'ARTICLE'}`. When true: Returns `'ZONE_SPECIFIC_RULE'`.
3. Checks `section_type == 'OTHER'`. When true: Returns `'OTHER_TEXT'`.
4. Raises `PlanningRegulationStructureError('Topic evidence references an unsupported section type')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationStructureError`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_build_topic_evidence`
- `src/landscout/stages/structure_planning_regulation.py` — `_validate_topic_evidence`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_build_topic_evidence`

**Signature**

```python
def _build_topic_evidence(
    index: PlanningRegulationIndex,
    config: PlanningRegulationStructureConfig,
    builds: Sequence[_SectionBuild],
) -> pd.DataFrame:
```

**Purpose**

Builds topic evidence according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`PlanningRegulationStructureConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `builds` (`Sequence[_SectionBuild]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `frame`; `pd.DataFrame({column: pd.Series(dtype='int64' if column in {'page_number', 'occurrence_count', 'first_match_normalized_start', 'first_match_normalized_end', 'first_match_raw_start', 'first_match_raw_end'} else 'object') for column in TOPIC_EVIDENCE_COLUMNS})`.

**Algorithm**

1. Defines `rows` with annotation `list[dict[str, object]]` from `[]`.
2. Computes `context_characters` from `config.topic_context_characters`.
3. Computes `toc_pages` from `set(config.document_layout.table_of_contents_pages)`.
4. Iterates `topic` over `sorted(config.topics)`. For each value: Computes `terms` from `config.topics[topic]`. Iterates `build` over `builds`. For each value: Computes `section` from `build.row`. Iterates `(page_number, raw_fragment)` over `build.page_fragments`. For each value: Checks `page_number in toc_pages and (not config.document_layout.include_table_of_contents_in_topic_evidence)`. When true: Executes `continue` control flow. Computes `(normalized, spans)` from `_normalize_search_text_with_mapping(raw_fragment)`. Computes `matches` from `_literal_topic_matches(normalized, terms)`. Executes 3 additional source-ordered statement(s).
5. Checks `not rows`. When true: Returns `pd.DataFrame({column: pd.Series(dtype='int64' if column in {'page_number', 'occurrence_count', 'first_match_normalized_start', 'first_match_normalized_end', 'first_match_raw_start', 'first_match_raw_end'} else 'object') for column in TOPIC_EVIDENCE_COLUMNS})`.
6. Computes `frame` from `pd.DataFrame(rows, columns=TOPIC_EVIDENCE_COLUMNS)`.
7. Iterates `column` over `('page_number', 'occurrence_count', 'first_match_normalized_start', 'first_match_normalized_end', 'first_match_raw_start', 'first_match_raw_end')`. For each value: Computes `frame[column]` from `frame[column].astype('int64')`.
8. Returns `frame`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_evidence_scope`, `_literal_topic_matches`, `_normalize_search_text_with_mapping`, `_raw_context`, `by_term.get`, `by_term.setdefault`, `by_term.setdefault(match.term_index, []).append`, `frame[column].astype`, `len`, `max`, `min`, `pd.DataFrame`, `pd.Series`, `range`, `rows.append`, `set`, `sorted`, `str`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_build_structure_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_frame_hash`

**Signature**

```python
def _frame_hash(
    domain: str,
    result: PlanningRegulationStructureResult,
    frame: pd.DataFrame,
    columns: Sequence[str],
) -> str:
```

**Purpose**

Implements frame hash according to the exact implementation and guards in this file.

**Inputs**

- `domain` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `columns` (`Sequence[str]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_sha256({'domain': domain, 'section_hash_schema_version': result.section_hash_schema_version, 'document_id': result.document_id, 'archive_sha256': result.archive_sha256, 'pdf_sha256': result.pdf_sha256, 'index_content_sha256': result.index_content_sha256, 'structure_profile': result.structure_profile, 'structure_config_schema_version': result.structure_config_schema_version, 'structure_…`.

**Algorithm**

1. Returns `_canonical_sha256({'domain': domain, 'section_hash_schema_version': result.section_hash_schema_version, 'document_id': result.document_id, 'archive_sha256': result.archive_sha256, 'pdf_sha256': result.pdf_sha256, 'index_content_sha256': result.index_content_sha256, 'structure_profile': result.structure_profile, 'structure_config_schema_version': result.stru…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_sha256`, `frame.loc[:, columns].to_dict`, `list`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_result_with_hashes`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_structure_result_content_sha256`

**Signature**

```python
def _structure_result_content_sha256(
    result: PlanningRegulationStructureResult,
) -> str:
```

**Purpose**

Implements structure result content sha256 according to the exact implementation and guards in this file.

**Inputs**

- `result` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_sha256({'domain': 'landscout.planning_regulation.structure_result', 'document_id': result.document_id, 'archive_sha256': result.archive_sha256, 'pdf_sha256': result.pdf_sha256, 'index_content_sha256': result.index_content_sha256, 'structure_profile': result.structure_profile, 'structure_config_schema_version': result.structure_config_schema_version, 'structure_config_sha256': result.st…`.

**Algorithm**

1. Returns `_canonical_sha256({'domain': 'landscout.planning_regulation.structure_result', 'document_id': result.document_id, 'archive_sha256': result.archive_sha256, 'pdf_sha256': result.pdf_sha256, 'index_content_sha256': result.index_content_sha256, 'structure_profile': result.structure_profile, 'structure_config_schema_version': result.structure_config_schema_versi…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_sha256`, `list`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_result_with_hashes`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_result_with_hashes`

**Signature**

```python
def _result_with_hashes(
    result: PlanningRegulationStructureResult,
) -> PlanningRegulationStructureResult:
```

**Purpose**

Implements result with hashes according to the exact implementation and guards in this file.

**Inputs**

- `result` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `PlanningRegulationStructureResult`. Observed return expression(s): `replace(component_result, structure_result_content_sha256=_structure_result_content_sha256(component_result))`.

**Algorithm**

1. Computes `component_result` from `replace(result, sections_content_sha256=_frame_hash('landscout.planning_regulation.sections', result, result.sections, SECTION_COLUMNS), zone_map_content_sha256=_frame_hash('landscout.planning_regulation.zone_map', result, result.zone_mapping, ZONE_MAPPING_COLUMNS), topic_evidence_content_sha256=_frame_hash('landscout…`.
2. Returns `replace(component_result, structure_result_content_sha256=_structure_result_content_sha256(component_result))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_frame_hash`, `_structure_result_content_sha256`, `replace`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_build_structure_result`
- `src/landscout/stages/structure_planning_regulation.py` — `_validate_result_self`
- `tests/unit/test_interpret_bess_zoning.py` — `test_factual_zone_mapping_counts_are_recomputed`
- `tests/unit/test_interpret_bess_zoning.py` — `test_structure_config_and_hierarchy_changes_are_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_unmapped_dominant_zone_is_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_coordinated_topic_evidence_and_hash_mutation_is_rebuilt_and_rejected`

**Tests**

- `tests/unit/test_interpret_bess_zoning.py::test_factual_zone_mapping_counts_are_recomputed`
- `tests/unit/test_interpret_bess_zoning.py::test_structure_config_and_hierarchy_changes_are_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_unmapped_dominant_zone_is_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_coordinated_topic_evidence_and_hash_mutation_is_rebuilt_and_rejected`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_page_tuple`

**Signature**

```python
def _page_tuple(value: object) -> tuple[int, ...]:
```

**Purpose**

Implements page tuple according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[int, ...]`. Observed return expression(s): `tuple((_strict_positive_integer(item, 'section page number') for item in value))`.

**Algorithm**

1. Checks `not isinstance(value, (tuple, list, np.ndarray))`. When true: Raises `PlanningRegulationStructureError('Section page_numbers must be a sequence')`.
2. Returns `tuple((_strict_positive_integer(item, 'section page number') for item in value))`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(value, (tuple, list, np.ndarray))` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationStructureError`, `_strict_positive_integer`, `isinstance`, `tuple`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_validate_sections`
- `src/landscout/stages/structure_planning_regulation.py` — `_validate_topic_evidence`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_sections`

**Signature**

```python
def _validate_sections(
    index: PlanningRegulationIndex,
    result: PlanningRegulationStructureResult,
    records: Sequence[_LineRecord],
    config: PlanningRegulationStructureConfig,
) -> None:
```

**Purpose**

Validates and rejects malformed sections according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `records` (`Sequence[_LineRecord]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`PlanningRegulationStructureConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `frame` from `result.sections`.
2. Checks `not isinstance(frame, pd.DataFrame) or tuple(frame.columns) != SECTION_COLUMNS`. When true: Raises `PlanningRegulationStructureError('Section schema is not deterministic')`.
3. Checks `frame.empty`. When true: Raises `PlanningRegulationStructureError('Regulation sections must not be empty')`.
4. Checks `result.source_records_sha256 != _source_records_sha256(records)`. When true: Raises `PlanningRegulationStructureError('Retained source-record hash differs')`.
5. Computes `known_pages` from `set(index.pages['page_number'].tolist())`.
6. Computes `record_position` from `{record.record_id: position for position, record in enumerate(records)}`.
7. Defines `ids` with annotation `list[str]` from `[]`.
8. Computes `expected_record_start` from `0`.
9. Defines `parents` with annotation `dict[str, str]` from `{}`.
10. Defines `zone_by_id` with annotation `dict[str, str | None]` from `{}`.
11. Iterates `(sequence, row)` over `enumerate(frame.to_dict('records'), start=1)`. For each value: Computes `section_id` from `_strict_string(row['section_id'], 'section ID')`. Checks `section_id != f'SECTION-{sequence:04d}'`. When true: Raises `PlanningRegulationStructureError('Section IDs must be deterministic and sequential')`. Calls `ids.append(section_id)` for its validation or side effect. Executes 37 additional source-ordered statement(s).
12. Checks `expected_record_start != len(records)`. When true: Raises `PlanningRegulationStructureError('Retained source records are omitted from the section partition')`.
13. Checks `len(set(ids)) != len(ids)`. When true: Raises `PlanningRegulationStructureError('Section IDs must be unique')`.
14. Computes `type_by_id` from `dict(zip(ids, frame['section_type'].tolist(), strict=True))`.
15. Computes `order_by_id` from `{section_id: position for position, section_id in enumerate(ids)}`.
16. Iterates `(section_id, parent)` over `parents.items()`. For each value: Checks `parent not in type_by_id or type_by_id[parent] != 'ZONE_CHAPTER'`. When true: Raises `PlanningRegulationStructureError('Article parent section is invalid')`. Computes `section_type` from `type_by_id[section_id]`. Checks `section_type != 'ARTICLE'`. When true: Raises `PlanningRegulationStructureError('Only articles may have a parent section')`. Executes 2 additional source-ordered statement(s).

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(frame, pd.DataFrame) or tuple(frame.columns) != SECTION_COLUMNS` is true.
- Rejects or diverts the path when `frame.empty` is true.
- Rejects or diverts the path when `result.source_records_sha256 != _source_records_sha256(records)` is true.
- Rejects or diverts the path when `expected_record_start != len(records)` is true.
- Rejects or diverts the path when `len(set(ids)) != len(ids)` is true.
- Rejects or diverts the path when `section_id != f'SECTION-{sequence:04d}'` is true.
- Rejects or diverts the path when `section_type not in _SECTION_TYPES` is true.
- Rejects or diverts the path when `row['heading_normalized'] != _normalize_search_text(row['heading_raw'])` is true.
- Rejects or diverts the path when `row['normalized_text'] != _normalize_search_text(row['raw_text'])` is true.
- Rejects or diverts the path when `_strict_nonnegative_integer(row['character_count'], 'character count') != len(row['raw_text'])` is true.
- Rejects or diverts the path when `start_record_id not in record_position or end_record_id not in record_position` is true.
- Rejects or diverts the path when `start_record != expected_record_start or end_record < start_record` is true.
- Rejects or diverts the path when `not row['raw_text'].strip() and (not blank_toc_other)` is true.
- Rejects or diverts the path when `not row['heading_raw'].strip() and (not blank_toc_other)` is true.
- Rejects or diverts the path when `_strict_positive_integer(row['source_record_count'], 'source record count') != len(segment)` is true.
- Rejects or diverts the path when `_validated_sha256(row['source_records_sha256'], 'section source-record SHA256') != _source_records_sha256(segment)` is true.
- Rejects or diverts the path when `row['raw_text'] != '\n'.join((record.raw for record in segment))` is true.
- Rejects or diverts the path when `not pages or any((right <= left for left, right in pairwise(pages))) or (not set(pages).issubset(known_pages)) or (pages != expected_pages)` is true.
- Rejects or diverts the path when `start != pages[0] or end != pages[-1] or end < start` is true.
- Rejects or diverts the path when `_validated_sha256(row['section_content_sha256'], 'section content SHA256') != expected_hash` is true.
- Rejects or diverts the path when `section_type == 'ARTICLE'` is true.
- Rejects or diverts the path when `parent not in type_by_id or type_by_id[parent] != 'ZONE_CHAPTER'` is true.
- Rejects or diverts the path when `section_type != 'ARTICLE'` is true.
- Rejects or diverts the path when `order_by_id[parent] >= order_by_id[section_id]` is true.
- Rejects or diverts the path when `zone_by_id[parent] != zone_by_id[section_id]` is true.
- Rejects or diverts the path when `not isinstance(row[column], str)` is true.
- Rejects or diverts the path when `row[column] != actual` is true.
- Rejects or diverts the path when `zone_label is None` is true.
- Rejects or diverts the path when `section_id not in parents` is true.
- Rejects or diverts the path when `section_type == 'GENERAL'` is true.
- Rejects or diverts the path when `zone_label is not None or section_id in parents` is true.
- Rejects or diverts the path when `section_id in parents` is true.
- Rejects or diverts the path when `section_type == 'ZONE_CHAPTER'` is true.
- Rejects or diverts the path when `zone_label is not None` is true.
- Rejects or diverts the path when `value is not None and (not bool(pd.isna(value)))` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `'\n'.join`, `PlanningRegulationStructureError`, `_normalize_search_text`, `_page_tuple`, `_section_content_sha256`, `_source_records_sha256`, `_strict_nonnegative_integer`, `_strict_positive_integer`, `_strict_string`, `_validated_sha256`, `any`, `bool`, `dict`, `dict.fromkeys`, `enumerate`, `frame.to_dict`, `frame['section_type'].tolist`, `ids.append`, `index.pages['page_number'].tolist`, `isinstance`, `len`, `pairwise`, `parents.items`, `pd.isna`, `row['heading_raw'].strip`, `row['raw_text'].strip`, `set`, `set(pages).issubset`, `tuple`, `zip`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_validate_result_self`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_zone_mapping`

**Signature**

```python
def _validate_zone_mapping(
    result: PlanningRegulationStructureResult,
    config: PlanningRegulationStructureConfig,
) -> None:
```

**Purpose**

Validates and rejects malformed zone mapping according to the exact implementation and guards in this file.

**Inputs**

- `result` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`PlanningRegulationStructureConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `frame` from `result.zone_mapping`.
2. Checks `not isinstance(frame, pd.DataFrame) or tuple(frame.columns) != ZONE_MAPPING_COLUMNS`. When true: Raises `PlanningRegulationStructureError('Zone mapping schema is not deterministic')`.
3. Defines `labels` with annotation `list[str]` from `[]`.
4. Computes `sections` from `result.sections.set_index('section_id', drop=False)`.
5. Computes `exact_methods` from `{'EXACT': 'EXACT_HEADING', 'CONFIG_ALIAS': 'CONFIG_ALIAS', 'UNMAPPED': 'NONE', 'AMBIGUOUS': 'AMBIGUOUS'}`.
6. Iterates `row` over `frame.to_dict('records')`. For each value: Computes `label` from `_strict_string(row['source_zone_label_raw'], 'source zone label')`. Calls `labels.append(label)` for its validation or side effect. Computes `status` from `_strict_string(row['mapping_status'], 'mapping status')`. Executes 10 additional source-ordered statement(s).
7. Checks `labels != sorted(labels) or len(set(labels)) != len(labels)`. When true: Raises `PlanningRegulationStructureError('Zone mappings must be unique and sorted')`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(frame, pd.DataFrame) or tuple(frame.columns) != ZONE_MAPPING_COLUMNS` is true.
- Rejects or diverts the path when `labels != sorted(labels) or len(set(labels)) != len(labels)` is true.
- Rejects or diverts the path when `status not in _MAPPING_STATUSES or method not in _MAPPING_METHODS` is true.
- Rejects or diverts the path when `exact_methods[status] != method` is true.
- Rejects or diverts the path when `status in {'EXACT', 'CONFIG_ALIAS'}` is true.
- Rejects or diverts the path when `row['dominant_candidate_count'] > 0 and status not in {'EXACT', 'CONFIG_ALIAS'}` is true.
- Rejects or diverts the path when `not counts['dominant_candidate_count'] <= counts['candidate_parcel_count'] <= counts['candidate_intersection_count']` is true.
- Rejects or diverts the path when `column == 'zone_polygon_count' and count == 0` is true.
- Rejects or diverts the path when `matched_id not in sections.index` is true.
- Rejects or diverts the path when `matched_section['section_type'] != 'ZONE_CHAPTER'` is true.
- Rejects or diverts the path when `matched_section['zone_chapter_label'] != resolved` is true.
- Rejects or diverts the path when `status == 'EXACT' and resolved != label` is true.
- Rejects or diverts the path when `status == 'CONFIG_ALIAS' and resolved != _resolved_alias(label, config.zone_aliases)` is true.
- Rejects or diverts the path when `matched is not None and (not bool(pd.isna(matched)))` is true.
- Rejects or diverts the path when `row[column] != actual` is true.
- Rejects or diverts the path when `status == 'UNMAPPED' and row['resolved_zone_chapter_label'] is not None and (not bool(pd.isna(row['resolved_zone_chapter_label'])))` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationStructureError`, `_resolved_alias`, `_strict_nonnegative_integer`, `_strict_string`, `bool`, `frame.to_dict`, `isinstance`, `labels.append`, `len`, `pd.isna`, `result.sections.set_index`, `set`, `sorted`, `tuple`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_validate_result_self`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_topic_evidence`

**Signature**

```python
def _validate_topic_evidence(
    index: PlanningRegulationIndex,
    result: PlanningRegulationStructureResult,
    config: PlanningRegulationStructureConfig,
    builds: Sequence[_SectionBuild],
) -> None:
```

**Purpose**

Validates and rejects malformed topic evidence according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`PlanningRegulationStructureConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `builds` (`Sequence[_SectionBuild]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `frame` from `result.topic_evidence`.
2. Checks `not isinstance(frame, pd.DataFrame) or tuple(frame.columns) != TOPIC_EVIDENCE_COLUMNS`. When true: Raises `PlanningRegulationStructureError('Topic evidence schema is not deterministic')`.
3. Computes `sections` from `result.sections.set_index('section_id', drop=False)`.
4. Computes `fragments` from `{(str(build.row['section_id']), page_number): raw_fragment for build in builds for page_number, raw_fragment in build.page_fragments}`.
5. Computes `page_set` from `set(index.pages['page_number'].tolist())`.
6. Defines `keys` with annotation `set[tuple[str, str, str, int]]` from `set()`.
7. Iterates `row` over `frame.to_dict('records')`. For each value: Computes `topic` from `_strict_string(row['topic'], 'topic')`. Checks `topic not in config.topics`. When true: Raises `PlanningRegulationStructureError('Topic evidence topic is unconfigured')`. Computes `term` from `_strict_string(row['search_term'], 'search term')`. Executes 35 additional source-ordered statement(s).

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(frame, pd.DataFrame) or tuple(frame.columns) != TOPIC_EVIDENCE_COLUMNS` is true.
- Rejects or diverts the path when `topic not in config.topics` is true.
- Rejects or diverts the path when `term not in config.topics[topic]` is true.
- Rejects or diverts the path when `normalized != _normalize_search_text(term)` is true.
- Rejects or diverts the path when `section_id not in sections.index` is true.
- Rejects or diverts the path when `page not in page_set or page not in _page_tuple(sections.at[section_id, 'page_numbers'])` is true.
- Rejects or diverts the path when `(section_id, page) not in fragments` is true.
- Rejects or diverts the path when `count < 1` is true.
- Rejects or diverts the path when `not isinstance(row['raw_context'], str) or not isinstance(row['normalized_context'], str)` is true.
- Rejects or diverts the path when `scope not in _EVIDENCE_SCOPES` is true.
- Rejects or diverts the path when `scope != expected_scope` is true.
- Rejects or diverts the path when `row['match_policy'] != config.topic_match_policy.identifier` is true.
- Rejects or diverts the path when `not retained_matches` is true.
- Rejects or diverts the path when `count != len(retained_matches)` is true.
- Rejects or diverts the path when `row['raw_context'] != expected_raw_context or row['normalized_context'] != expected_normalized_context or row['raw_context'] not in raw_fragment` is true.
- Rejects or diverts the path when `key in keys` is true.
- Rejects or diverts the path when `actual != expected` is true.
- Rejects or diverts the path when `_strict_nonnegative_integer(row[column], column) != expected` is true.
- Rejects or diverts the path when `row[column] != actual` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationStructureError`, `_evidence_scope`, `_literal_topic_matches`, `_normalize_search_text`, `_normalize_search_text_with_mapping`, `_page_tuple`, `_raw_context`, `_strict_nonnegative_integer`, `_strict_positive_integer`, `_strict_string`, `bool`, `expected_positions.items`, `frame.to_dict`, `index.pages['page_number'].tolist`, `isinstance`, `keys.add`, `len`, `max`, `min`, `pd.isna`, `result.sections.set_index`, `set`, `str`, `tuple`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_validate_result_self`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_build_structure_result`

**Signature**

```python
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
```

**Purpose**

Builds structure result according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zones` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `intersections` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`PlanningRegulationStructureConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[PlanningRegulationStructureResult, tuple[_SectionBuild, ...], tuple[_LineRecord, ...]]`. Observed return expression(s): `(_result_with_hashes(result), builds, records)`.

**Algorithm**

1. Computes `(sections, builds, records)` from `_build_sections(index, config)`.
2. Computes `zone_mapping` from `_build_zone_mapping(index, config, sections, zones, intersections)`.
3. Computes `topic_evidence` from `_build_topic_evidence(index, config, builds)`.
4. Computes `intersection_hash_columns` from `_intersection_hash_columns(intersections)`.
5. Computes `result` from `PlanningRegulationStructureResult(document_id=index.document_id, archive_sha256=index.archive_sha256, pdf_sha256=index.pdf_sha256, index_content_sha256=index.index_content_sha256, structure_profile=config.structure_profile, structure_config_schema_version=config.schema_version, structure_config_sha256=_config_sha256(c…`.
6. Returns `(_result_with_hashes(result), builds, records)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationStructureResult`, `_build_sections`, `_build_topic_evidence`, `_build_zone_mapping`, `_config_sha256`, `_input_frame_sha256`, `_intersection_hash_columns`, `_result_with_hashes`, `_source_records_sha256`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `structure_planning_regulation`
- `src/landscout/stages/structure_planning_regulation.py` — `validate_planning_regulation_structure_with_fragments`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_result_self`

**Signature**

```python
def _validate_result_self(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
    intersections: pd.DataFrame,
    config: PlanningRegulationStructureConfig,
    result: PlanningRegulationStructureResult,
    builds: Sequence[_SectionBuild],
    records: Sequence[_LineRecord],
) -> None:
```

**Purpose**

Validates and rejects malformed result self according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zones` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `intersections` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`PlanningRegulationStructureConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `builds` (`Sequence[_SectionBuild]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `records` (`Sequence[_LineRecord]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Calls `validate_planning_regulation_index(index)` for its validation or side effect.
2. Checks `not isinstance(result, PlanningRegulationStructureResult)`. When true: Raises `PlanningRegulationStructureError('result must be a PlanningRegulationStructureResult')`.
3. Iterates `(value, label)` over `((result.document_id, 'document ID'), (result.archive_sha256, 'archive SHA256'), (result.pdf_sha256, 'PDF SHA256'), (result.index_content_sha256, 'index content SHA256'), (result.structure_profile, 'structure profile'))`. For each value: Calls `_strict_string(value, label)` for its validation or side effect.
4. Checks `result.document_id != index.document_id or result.archive_sha256 != index.archive_sha256 or result.pdf_sha256 != index.pdf_sha256 or (result.index_content_sha256 != index.index_content_sha256)`. When true: Raises `PlanningRegulationStructureError('Structure result lineage differs from index')`.
5. Calls `_validated_sha256(result.archive_sha256, 'archive SHA256')` for its validation or side effect.
6. Calls `_validated_sha256(result.pdf_sha256, 'PDF SHA256')` for its validation or side effect.
7. Calls `_validated_sha256(result.index_content_sha256, 'index content SHA256')` for its validation or side effect.
8. Computes `config_schema` from `_strict_positive_integer(result.structure_config_schema_version, 'structure config schema version')`.
9. Checks `config_schema != config.schema_version`. When true: Raises `PlanningRegulationStructureError('Structure config schema version differs')`.
10. Calls `_validated_sha256(result.structure_config_sha256, 'structure config SHA256')` for its validation or side effect.
11. Checks `result.structure_config_sha256 != _config_sha256(config)`. When true: Raises `PlanningRegulationStructureError('Structure config hash differs')`.
12. Computes `expected_zones_hash` from `_input_frame_sha256('landscout.planning_regulation.zones_input', zones, _ZONE_INPUT_COLUMNS)`.
13. Computes `expected_intersections_hash` from `_input_frame_sha256('landscout.planning_regulation.intersections_input', intersections, _intersection_hash_columns(intersections))`.
14. Checks `result.zones_content_sha256 != expected_zones_hash`. When true: Raises `PlanningRegulationStructureError('Zone input hash differs')`.
15. Computes `expected_intersection_columns` from `_intersection_hash_columns(intersections)`.
16. Checks `type(result.zoning_intersection_hash_columns) is not tuple or not all((isinstance(column, str) for column in result.zoning_intersection_hash_columns)) or result.zoning_intersection_hash_columns != expected_intersection_columns`. When true: Raises `PlanningRegulationStructureError('Intersection hash columns differ from the factual input schema')`.
17. Checks `result.zoning_intersections_content_sha256 != expected_intersections_hash`. When true: Raises `PlanningRegulationStructureError('Intersection input hash differs')`.
18. Calls `_validated_sha256(result.source_records_sha256, 'source records SHA256')` for its validation or side effect.
19. Computes `schema` from `_strict_positive_integer(result.section_hash_schema_version, 'section hash schema version')`.
20. Checks `schema != SECTION_HASH_SCHEMA_VERSION`. When true: Raises `PlanningRegulationStructureError('Unsupported section hash schema version')`.
21. Calls `_validate_sections(index, result, records, config)` for its validation or side effect.
22. Calls `_validate_zone_mapping(result, config)` for its validation or side effect.
23. Calls `_validate_topic_evidence(index, result, config, builds)` for its validation or side effect.
24. Computes `expected` from `_result_with_hashes(replace(result, sections_content_sha256='', zone_map_content_sha256='', topic_evidence_content_sha256='', structure_result_content_sha256=''))`.
25. Iterates `(actual, wanted, label)` over `((result.sections_content_sha256, expected.sections_content_sha256, 'sections'), (result.zone_map_content_sha256, expected.zone_map_content_sha256, 'zone map'), (result.topic_evidence_content_sha256, expected.topic_evidence_content_sha256, 'topic evidence'))`. For each value: Checks `_validated_sha256(actual, f'{label} content SHA256') != wanted`. When true: Raises `PlanningRegulationStructureError(f'{label} content hash differs')`.
26. Checks `_validated_sha256(result.structure_result_content_sha256, 'structure result content SHA256') != expected.structure_result_content_sha256`. When true: Raises `PlanningRegulationStructureError('Complete structure result hash differs')`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(result, PlanningRegulationStructureResult)` is true.
- Rejects or diverts the path when `result.document_id != index.document_id or result.archive_sha256 != index.archive_sha256 or result.pdf_sha256 != index.pdf_sha256 or (result.index_content_sha256 != index.index_content_sha256)` is true.
- Rejects or diverts the path when `config_schema != config.schema_version` is true.
- Rejects or diverts the path when `result.structure_config_sha256 != _config_sha256(config)` is true.
- Rejects or diverts the path when `result.zones_content_sha256 != expected_zones_hash` is true.
- Rejects or diverts the path when `type(result.zoning_intersection_hash_columns) is not tuple or not all((isinstance(column, str) for column in result.zoning_intersection_hash_columns)) or result.zoning_intersection_hash_columns != expected_intersection_columns` is true.
- Rejects or diverts the path when `result.zoning_intersections_content_sha256 != expected_intersections_hash` is true.
- Rejects or diverts the path when `schema != SECTION_HASH_SCHEMA_VERSION` is true.
- Rejects or diverts the path when `_validated_sha256(result.structure_result_content_sha256, 'structure result content SHA256') != expected.structure_result_content_sha256` is true.
- Rejects or diverts the path when `_validated_sha256(actual, f'{label} content SHA256') != wanted` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `PlanningRegulationStructureError`, `_config_sha256`, `_input_frame_sha256`, `_intersection_hash_columns`, `_result_with_hashes`, `_strict_positive_integer`, `_strict_string`, `_validate_sections`, `_validate_topic_evidence`, `_validate_zone_mapping`, `_validated_sha256`, `all`, `isinstance`, `replace`, `type`, `validate_planning_regulation_index`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `validate_planning_regulation_structure_with_fragments`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_resolved_config`

**Signature**

```python
def _resolved_config(
    config: PlanningRegulationStructureConfig | str | Path,
) -> PlanningRegulationStructureConfig:
```

**Purpose**

Implements resolved config according to the exact implementation and guards in this file.

**Inputs**

- `config` (`PlanningRegulationStructureConfig | str | Path`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `PlanningRegulationStructureConfig`. Observed return expression(s): `load_planning_regulation_structure_config(config)`; `PlanningRegulationStructureConfig.model_validate(config.model_dump(mode='python'))`.

**Algorithm**

1. Checks `isinstance(config, PlanningRegulationStructureConfig)`. When true: Runs guarded operation: Returns `PlanningRegulationStructureConfig.model_validate(config.model_dump(mode='python'))`. Handles `Exception`.
2. Returns `load_planning_regulation_structure_config(config)`.

**Validation and invariants**

- Rejects or diverts the path when `isinstance(config, PlanningRegulationStructureConfig)` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `load_planning_regulation_structure_config`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `PlanningRegulationStructureConfig.model_validate`, `PlanningRegulationStructureError`, `config.model_dump`, `isinstance`, `load_planning_regulation_structure_config`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `structure_planning_regulation`
- `src/landscout/stages/structure_planning_regulation.py` — `validate_planning_regulation_structure_with_fragments`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_frame_rows`

**Signature**

```python
def _canonical_frame_rows(frame: pd.DataFrame, columns: Sequence[str]) -> object:
```

**Purpose**

Implements canonical frame rows according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `columns` (`Sequence[str]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. Observed return expression(s): `_canonical_value(frame.loc[:, columns].to_dict('records'))`.

**Algorithm**

1. Returns `_canonical_value(frame.loc[:, columns].to_dict('records'))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_value`, `frame.loc[:, columns].to_dict`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `_compare_expected_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_compare_expected_result`

**Signature**

```python
def _compare_expected_result(
    result: PlanningRegulationStructureResult,
    expected: PlanningRegulationStructureResult,
) -> None:
```

**Purpose**

Compares expected result according to the exact implementation and guards in this file.

**Inputs**

- `result` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `expected` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `scalar_fields` from `('document_id', 'archive_sha256', 'pdf_sha256', 'index_content_sha256', 'structure_profile', 'structure_config_schema_version', 'structure_config_sha256', 'zones_content_sha256', 'zoning_intersection_hash_columns', 'zoning_intersections_content_sha256', 'source_records_sha256', 'section_hash_schema_version', 'sections…`.
2. Iterates `field` over `scalar_fields`. For each value: Checks `getattr(result, field) != getattr(expected, field)`. When true: Raises `PlanningRegulationStructureError(f'Structure result {field} differs from rebuilt source evidence')`.
3. Iterates `(name, columns)` over `(('sections', SECTION_COLUMNS), ('zone_mapping', ZONE_MAPPING_COLUMNS), ('topic_evidence', TOPIC_EVIDENCE_COLUMNS))`. For each value: Computes `actual_frame` from `getattr(result, name)`. Computes `expected_frame` from `getattr(expected, name)`. Checks `tuple(actual_frame.columns) != tuple(columns)`. When true: Raises `PlanningRegulationStructureError(f'{name} schema differs from rebuilt source evidence')`. Executes 1 additional source-ordered statement(s).

**Validation and invariants**

- Rejects or diverts the path when `getattr(result, field) != getattr(expected, field)` is true.
- Rejects or diverts the path when `tuple(actual_frame.columns) != tuple(columns)` is true.
- Rejects or diverts the path when `_canonical_frame_rows(actual_frame, columns) != _canonical_frame_rows(expected_frame, columns)` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationStructureError`, `_canonical_frame_rows`, `getattr`, `tuple`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `validate_planning_regulation_structure_with_fragments`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_section_page_fragments`

**Signature**

```python
def _section_page_fragments(
    result: PlanningRegulationStructureResult,
    builds: Sequence[_SectionBuild],
) -> pd.DataFrame:
```

**Purpose**

Implements section page fragments according to the exact implementation and guards in this file.

**Inputs**

- `result` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `builds` (`Sequence[_SectionBuild]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `frame`.

**Algorithm**

1. Computes `rows` from `[{'section_id': build.row['section_id'], 'page_number': page_number, 'raw_text': raw_text, 'section_page_fragment_sha256': sha256(raw_text.encode('utf-8')).hexdigest(), 'document_id': result.document_id, 'archive_sha256': result.archive_sha256, 'pdf_sha256': result.pdf_sha256, 'index_content_sha256': result.index_cont…`.
2. Computes `frame` from `pd.DataFrame(rows, columns=('section_id', 'page_number', 'raw_text', 'section_page_fragment_sha256', 'document_id', 'archive_sha256', 'pdf_sha256', 'index_content_sha256', 'structure_result_content_sha256', 'structure_profile'))`.
3. Computes `frame['page_number']` from `frame['page_number'].astype('int64')`.
4. Checks `frame.duplicated(['section_id', 'page_number']).any()`. When true: Raises `PlanningRegulationStructureError('Section/page fragment identity is not unique')`.
5. Returns `frame`.

**Validation and invariants**

- Rejects or diverts the path when `frame.duplicated(['section_id', 'page_number']).any()` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationStructureError`, `frame.duplicated`, `frame.duplicated(['section_id', 'page_number']).any`, `frame['page_number'].astype`, `pd.DataFrame`, `raw_text.encode`, `sha256`, `sha256(raw_text.encode('utf-8')).hexdigest`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `validate_planning_regulation_structure_with_fragments`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_planning_regulation_structure_with_fragments`

**Signature**

```python
def validate_planning_regulation_structure_with_fragments(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
    zoning_intersections: pd.DataFrame,
    config: PlanningRegulationStructureConfig | str | Path,
    result: PlanningRegulationStructureResult,
) -> pd.DataFrame:
```

**Purpose**

Validate the complete structure and return its retained page fragments.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zones` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zoning_intersections` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`PlanningRegulationStructureConfig | str | Path`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `_section_page_fragments(result, builds)`.

**Algorithm**

1. Runs guarded operation: Computes `resolved_config` from `_resolved_config(config)`. Calls `_validate_document_lock(index, resolved_config)` for its validation or side effect. Computes `(zones_copy, intersections_copy)` from `_validated_zoning_inputs(index, zones, zoning_intersections)`. Computes `(expected, builds, records)` from `_build_structure_result(index, zones_copy, intersections_copy, resolved_config)`. Executes 3 additional source-ordered statement(s). Handles `PlanningRegulationStructureError`, `Exception`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationStructureError`, `_build_structure_result`, `_compare_expected_result`, `_resolved_config`, `_section_page_fragments`, `_validate_document_lock`, `_validate_result_self`, `_validated_zoning_inputs`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_build_result`
- `src/landscout/stages/structure_planning_regulation.py` — `planning_regulation_section_page_fragments`
- `src/landscout/stages/structure_planning_regulation.py` — `validate_planning_regulation_structure`
- `tests/unit/test_structure_planning_regulation.py` — `test_source_complete_validator_can_return_validated_fragments`

**Tests**

- `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_can_return_validated_fragments`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_planning_regulation_structure`

**Signature**

```python
def validate_planning_regulation_structure(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
    zoning_intersections: pd.DataFrame,
    config: PlanningRegulationStructureConfig | str | Path,
    result: PlanningRegulationStructureResult,
) -> None:
```

**Purpose**

Rebuild and validate the complete structure from all factual inputs.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zones` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zoning_intersections` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`PlanningRegulationStructureConfig | str | Path`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Calls `validate_planning_regulation_structure_with_fragments(index, zones, zoning_intersections, config, result)` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `validate_planning_regulation_structure_with_fragments`.

**Known repository callers**

- `src/landscout/stages/structure_planning_regulation.py` — `structure_planning_regulation`
- `tests/unit/test_structure_planning_regulation.py` — `_structure_with_document_layout`
- `tests/unit/test_structure_planning_regulation.py` — `_validate`
- `tests/unit/test_structure_planning_regulation.py` — `test_blank_gap_after_toc_is_preserved_without_a_blank_other_section`
- `tests/unit/test_structure_planning_regulation.py` — `test_blank_only_prefix_is_preserved_in_first_actual_section`
- `tests/unit/test_structure_planning_regulation.py` — `test_document_layout_accepts_real_first_and_last_indexed_pages`
- `tests/unit/test_structure_planning_regulation.py` — `test_evidence_scope_is_derived_from_exact_section_type`
- `tests/unit/test_structure_planning_regulation.py` — `test_existing_empty_toc_page_is_valid_not_nonexistent`
- `tests/unit/test_structure_planning_regulation.py` — `test_intersection_hash_column_lineage_mutation_is_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_intersection_hash_columns_are_actual_and_deterministic`
- `tests/unit/test_structure_planning_regulation.py` — `test_intersection_upper_bound_uses_shared_relative_tolerance`
- `tests/unit/test_structure_planning_regulation.py` — `test_optional_intersection_metric_change_invalidates_existing_result`
- `tests/unit/test_structure_planning_regulation.py` — `test_source_complete_validator_rejects_changed_ambiguous_grammar`
- `tests/unit/test_structure_planning_regulation.py` — `test_source_complete_validator_rejects_post_build_source_change`
- `tests/unit/test_structure_planning_regulation.py` — `test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence`
- `tests/unit/test_structure_planning_regulation.py` — `test_wrong_intersection_source_zone_id_is_rejected`

**Tests**

- `tests/unit/test_structure_planning_regulation.py::test_blank_gap_after_toc_is_preserved_without_a_blank_other_section`
- `tests/unit/test_structure_planning_regulation.py::test_blank_only_prefix_is_preserved_in_first_actual_section`
- `tests/unit/test_structure_planning_regulation.py::test_document_layout_accepts_real_first_and_last_indexed_pages`
- `tests/unit/test_structure_planning_regulation.py::test_evidence_scope_is_derived_from_exact_section_type`
- `tests/unit/test_structure_planning_regulation.py::test_existing_empty_toc_page_is_valid_not_nonexistent`
- `tests/unit/test_structure_planning_regulation.py::test_intersection_hash_column_lineage_mutation_is_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_intersection_hash_columns_are_actual_and_deterministic`
- `tests/unit/test_structure_planning_regulation.py::test_intersection_upper_bound_uses_shared_relative_tolerance`
- `tests/unit/test_structure_planning_regulation.py::test_optional_intersection_metric_change_invalidates_existing_result`
- `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_rejects_changed_ambiguous_grammar`
- `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_rejects_post_build_source_change`
- `tests/unit/test_structure_planning_regulation.py::test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence`
- `tests/unit/test_structure_planning_regulation.py::test_wrong_intersection_source_zone_id_is_rejected`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `planning_regulation_section_page_fragments`

**Signature**

```python
def planning_regulation_section_page_fragments(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
    zoning_intersections: pd.DataFrame,
    config: PlanningRegulationStructureConfig | str | Path,
    result: PlanningRegulationStructureResult,
) -> pd.DataFrame:
```

**Purpose**

Return validated retained raw text for every section and source page.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zones` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zoning_intersections` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`PlanningRegulationStructureConfig | str | Path`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `validate_planning_regulation_structure_with_fragments(index, zones, zoning_intersections, config, result)`.

**Algorithm**

1. Runs guarded operation: Returns `validate_planning_regulation_structure_with_fragments(index, zones, zoning_intersections, config, result)`. Handles `PlanningRegulationStructureError`, `Exception`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationStructureError`, `validate_planning_regulation_structure_with_fragments`.

**Known repository callers**

- `tests/unit/test_interpret_bess_zoning.py` — `_policy`
- `tests/unit/test_interpret_bess_zoning.py` — `test_exact_section_page_occurrence_is_auditable`
- `tests/unit/test_interpret_bess_zoning.py` — `test_repeated_excerpt_occurrence_is_bound_to_policy`
- `tests/unit/test_interpret_bess_zoning.py` — `test_same_general_occurrence_may_be_scoped_to_different_chapters`

**Tests**

- `tests/unit/test_interpret_bess_zoning.py::test_exact_section_page_occurrence_is_auditable`
- `tests/unit/test_interpret_bess_zoning.py::test_repeated_excerpt_occurrence_is_bound_to_policy`
- `tests/unit/test_interpret_bess_zoning.py::test_same_general_occurrence_may_be_scoped_to_different_chapters`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `structure_planning_regulation`

**Signature**

```python
def structure_planning_regulation(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
    zoning_intersections: pd.DataFrame,
    config: PlanningRegulationStructureConfig | str | Path,
) -> PlanningRegulationStructureResult:
```

**Purpose**

Build source-locked sections, exact zone mappings, and literal topic evidence.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zones` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zoning_intersections` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`PlanningRegulationStructureConfig | str | Path`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `PlanningRegulationStructureResult`. Observed return expression(s): `result`.

**Algorithm**

1. Runs guarded operation: Computes `resolved_config` from `_resolved_config(config)`. Calls `_validate_document_lock(index, resolved_config)` for its validation or side effect. Computes `(zones_copy, intersections_copy)` from `_validated_zoning_inputs(index, zones, zoning_intersections)`. Computes `(result, _, _)` from `_build_structure_result(index, zones_copy, intersections_copy, resolved_config)`. Executes 2 additional source-ordered statement(s). Handles `PlanningRegulationStructureError`, `Exception`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `PlanningRegulationStructureError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationStructureError`, `_build_structure_result`, `_resolved_config`, `_validate_document_lock`, `_validated_zoning_inputs`, `validate_planning_regulation_structure`.

**Known repository callers**

- `tests/unit/test_interpret_bess_zoning.py` — `inputs`
- `tests/unit/test_structure_planning_regulation.py` — `_structure_with_document_layout`
- `tests/unit/test_structure_planning_regulation.py` — `test_alias_chain_resolves_to_final_configured_target`
- `tests/unit/test_structure_planning_regulation.py` — `test_ambiguous_continuation_candidate_fails_with_record_diagnostic`
- `tests/unit/test_structure_planning_regulation.py` — `test_blank_gap_after_toc_is_preserved_without_a_blank_other_section`
- `tests/unit/test_structure_planning_regulation.py` — `test_blank_only_prefix_is_preserved_in_first_actual_section`
- `tests/unit/test_structure_planning_regulation.py` — `test_document_layout_rejects_nonexistent_indexed_pages`
- `tests/unit/test_structure_planning_regulation.py` — `test_document_lock_mismatch_is_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_dominant_unmapped_zone_stops_processing`
- `tests/unit/test_structure_planning_regulation.py` — `test_equal_length_overlap_uses_configured_term_order_as_tie_break`
- `tests/unit/test_structure_planning_regulation.py` — `test_evidence_scope_is_derived_from_exact_section_type`
- `tests/unit/test_structure_planning_regulation.py` — `test_general_and_article_cross_category_match_is_ambiguous`
- `tests/unit/test_structure_planning_regulation.py` — `test_inputs_are_not_mutated`
- `tests/unit/test_structure_planning_regulation.py` — `test_intersection_area_cannot_exceed_available_geometry_area`
- `tests/unit/test_structure_planning_regulation.py` — `test_intersection_hash_column_lineage_mutation_is_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_intersection_hash_columns_are_actual_and_deterministic`
- `tests/unit/test_structure_planning_regulation.py` — `test_intersection_upper_bound_uses_shared_relative_tolerance`
- `tests/unit/test_structure_planning_regulation.py` — `test_normal_muret_compatible_grammar_remains_deterministic`
- `tests/unit/test_structure_planning_regulation.py` — `test_optional_intersection_metric_change_invalidates_existing_result`
- `tests/unit/test_structure_planning_regulation.py` — `test_reversed_topic_mapping_keys_do_not_change_output_or_hashes`
- `tests/unit/test_structure_planning_regulation.py` — `test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence`
- `tests/unit/test_structure_planning_regulation.py` — `test_two_article_patterns_matching_one_line_are_ambiguous`
- `tests/unit/test_structure_planning_regulation.py` — `test_two_zone_patterns_matching_one_line_are_ambiguous`
- `tests/unit/test_structure_planning_regulation.py` — `test_zone_and_general_cross_category_match_is_ambiguous`
- `tests/unit/test_structure_planning_regulation.py` — `valid_result`

**Tests**

- `tests/unit/test_structure_planning_regulation.py::test_alias_chain_resolves_to_final_configured_target`
- `tests/unit/test_structure_planning_regulation.py::test_ambiguous_continuation_candidate_fails_with_record_diagnostic`
- `tests/unit/test_structure_planning_regulation.py::test_blank_gap_after_toc_is_preserved_without_a_blank_other_section`
- `tests/unit/test_structure_planning_regulation.py::test_blank_only_prefix_is_preserved_in_first_actual_section`
- `tests/unit/test_structure_planning_regulation.py::test_document_layout_rejects_nonexistent_indexed_pages`
- `tests/unit/test_structure_planning_regulation.py::test_document_lock_mismatch_is_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_dominant_unmapped_zone_stops_processing`
- `tests/unit/test_structure_planning_regulation.py::test_equal_length_overlap_uses_configured_term_order_as_tie_break`
- `tests/unit/test_structure_planning_regulation.py::test_evidence_scope_is_derived_from_exact_section_type`
- `tests/unit/test_structure_planning_regulation.py::test_general_and_article_cross_category_match_is_ambiguous`
- `tests/unit/test_structure_planning_regulation.py::test_inputs_are_not_mutated`
- `tests/unit/test_structure_planning_regulation.py::test_intersection_area_cannot_exceed_available_geometry_area`
- `tests/unit/test_structure_planning_regulation.py::test_intersection_hash_column_lineage_mutation_is_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_intersection_hash_columns_are_actual_and_deterministic`
- `tests/unit/test_structure_planning_regulation.py::test_intersection_upper_bound_uses_shared_relative_tolerance`
- `tests/unit/test_structure_planning_regulation.py::test_normal_muret_compatible_grammar_remains_deterministic`
- `tests/unit/test_structure_planning_regulation.py::test_optional_intersection_metric_change_invalidates_existing_result`
- `tests/unit/test_structure_planning_regulation.py::test_reversed_topic_mapping_keys_do_not_change_output_or_hashes`
- `tests/unit/test_structure_planning_regulation.py::test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence`
- `tests/unit/test_structure_planning_regulation.py::test_two_article_patterns_matching_one_line_are_ambiguous`
- `tests/unit/test_structure_planning_regulation.py::test_two_zone_patterns_matching_one_line_are_ambiguous`
- `tests/unit/test_structure_planning_regulation.py::test_zone_and_general_cross_category_match_is_ambiguous`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `ARTICLE` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `GENERAL` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `ZONE_CHAPTER` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `article_number_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `article_title_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `ascending` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `candidate_intersection_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `candidate_parcel_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `character_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `document_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `dominant_candidate_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `drop` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `end_page` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `end_record_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `evidence_scope` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `first_match_normalized_end` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `first_match_normalized_start` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `first_match_raw_end` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `first_match_raw_start` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `heading_normalized` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `heading_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `index_content_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `intersection_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `kind` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `longest_match` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `mapping_method` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `mapping_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `match_policy` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `matched_section_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `normalized_context` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `normalized_search_term` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `normalized_text` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `occurrence_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `page_number` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `page_numbers` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_metric_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `parent_section_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `pdf_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `planning_zone_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `raw_context` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `raw_text` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `relation_type` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `resolved_zone_chapter_label` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `search_term` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `section_content_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `section_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `section_type` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `source_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `source_document_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_record_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `source_records_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `source_zone_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_zone_label_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `start_page` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `start_record_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `structure_profile` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `token` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `topic` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `topics` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `zone_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `zone_chapter_label` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `zone_label_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `zone_polygon_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |

## 8. Interfaces

Known static callers, internal calls, and tests are listed for every symbol. Package-level availability is controlled by this module's `__all__` and the relevant package `__init__.py`; private helpers are not a stable public API.

## 9. Error handling

Every explicit raise and guarded condition is listed with its function. Public boundaries translate malformed source/configuration/input conditions into the controlled exception classes shown by those functions and tests; raw implementation errors are not promised as API.

## 10. Side effects

Per-function side effects are derived from actual calls. Source adapters may perform guarded network, cache, archive, or filesystem operations; stages normally operate on copies unless their preservation validators state otherwise; tests use the boundaries stated per test.

## 11. Security / trust boundaries

Trust claims are limited to the explicit byte, schema, lineage, source-complete, path, URL, geometry, or policy checks implemented by this file and its callees. Textual lineage is not treated as physical proof unless the function revalidates the physical source.

## 12. GIS / CRS rules

GIS rules apply only where geometry/CRS calls or columns are listed above. Storage geometry is not silently repaired; metric work uses the explicit CRS transformations and calculation copies visible in the algorithm. Files without GIS calls impose no CRS contract.

## 13. Provenance rules

Provenance is carried only through exact source/configuration/hash fields shown by the models, constants, and frame columns. Consult `docs/code/SOURCE_TRUST_MODEL.md` for the cross-adapter chain.

## 14. Business meaning

This file contributes to LandScout's `planning` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.

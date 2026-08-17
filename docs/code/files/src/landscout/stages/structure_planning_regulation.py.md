# `src/landscout/stages/structure_planning_regulation.py`

## File identity

- Repository path: `src/landscout/stages/structure_planning_regulation.py`
- File type: Python source
- Layer: processing/policy stage
- Domain: planning
- Responsibility: Partitions the indexed written regulation into deterministic source-bound sections, zone mappings, and topic evidence.
- Source SHA256: `46707b5077b1e122158b4ca6be3363ee8ad7808ac62e08106854bee1e89da45e`

## 1. Purpose

Partitions the indexed written regulation into deterministic source-bound sections, zone mappings, and topic evidence.

## 2. Position in LandScout architecture

This file belongs to the **processing/policy stage** layer and the **planning** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import json`
- `import math`
- `import re`
- `from collections import Counter`
- `from collections.abc import Mapping, Sequence`
- `from dataclasses import dataclass, replace`
- `from hashlib import sha256`
- `from itertools import pairwise`
- `from numbers import Integral, Real`
- `from pathlib import Path`
- `from typing import Literal`

### Third-party packages

- `import numpy as np`
- `import pandas as pd`
- `import yaml`
- `from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictInt,
    StrictStr,
    model_validator,
)`

### Internal LandScout imports

- `from landscout.common.planning_text import (
    normalize_planning_search_text,
    normalize_planning_search_text_with_mapping,
    raw_context_from_spans,
)`
- `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    validate_planning_regulation_index,
)`
- `from landscout.stages.planning_overlay import technical_overlay_tolerance`

## 4. Contract taxonomy

### A. Python constants

#### `_normalize_search_text`

```python
_normalize_search_text = normalize_planning_search_text
```

Module-level callback/compatibility alias consumed by runtime calls and monkeypatch-based regression tests. Consumers include `src/landscout/stages/index_planning_regulation.py::_validate_pages` (direct call or construction), `src/landscout/stages/index_planning_regulation.py::_index_planning_regulation` (direct call or construction), `src/landscout/stages/index_planning_regulation.py::_validated_terms` (direct call or construction), `src/landscout/stages/structure_planning_regulation.py::PlanningRegulationStructureConfig._validate_grammar` (direct call or construction), `src/landscout/stages/structure_planning_regulation.py::_heading_events` (direct call or construction), `src/landscout/stages/structure_planning_regulation.py::_build_sections` (direct call or construction), `src/landscout/stages/structure_planning_regulation.py::_literal_topic_matches` (direct call or construction), `src/landscout/stages/structure_planning_regulation.py::_validate_sections` (direct call or construction), `src/landscout/stages/structure_planning_regulation.py::_validate_topic_evidence` (direct call or construction), `tests/unit/test_index_planning_regulation.py::test_french_literal_normalization` (direct call or construction), `tests/unit/test_interpret_bess_zoning.py::_index` (direct call or construction), `tests/unit/test_interpret_bess_zoning.py::<module>` (import/re-export), `tests/unit/test_structure_planning_regulation.py::_index` (direct call or construction), `tests/unit/test_structure_planning_regulation.py::test_coordinated_section_row_mutation_is_caught_by_outer_envelope` (direct call or construction), `tests/unit/test_structure_planning_regulation.py::<module>` (import/re-export).

#### `_normalize_search_text_with_mapping`

```python
_normalize_search_text_with_mapping = normalize_planning_search_text_with_mapping
```

Explicit mapping between source/input and target/output fields; keys and values are documented separately. Consumers include `src/landscout/stages/index_planning_regulation.py::_build_hits` (direct call or construction), `src/landscout/stages/structure_planning_regulation.py::_build_topic_evidence` (direct call or construction), `src/landscout/stages/structure_planning_regulation.py::_validate_topic_evidence` (direct call or construction).

#### `_raw_context`

```python
_raw_context = raw_context_from_spans
```

Module-level callback/compatibility alias consumed by runtime calls and monkeypatch-based regression tests. Consumers include `src/landscout/stages/index_planning_regulation.py::_build_hits` (direct call or construction), `src/landscout/stages/structure_planning_regulation.py::_build_topic_evidence` (direct call or construction), `src/landscout/stages/structure_planning_regulation.py::_validate_topic_evidence` (direct call or construction).

#### `SECTION_HASH_SCHEMA_VERSION`

```python
SECTION_HASH_SCHEMA_VERSION = 3
```

Supported schema/hash/manifest compatibility version used by validators and canonical hashing. Consumers include `src/landscout/stages/structure_planning_regulation.py::_build_structure_result` (value argument/reference), `tests/unit/test_structure_planning_regulation.py::<module>` (import/re-export).

#### `STRUCTURE_MANIFEST_SCHEMA_VERSION`

```python
STRUCTURE_MANIFEST_SCHEMA_VERSION = 4
```

Supported schema/hash/manifest compatibility version used by validators and canonical hashing. Consumers include `tests/unit/test_structure_planning_regulation.py::<module>` (import/re-export).

#### `_SUPPORTED_CONFIG_SCHEMA_VERSION`

```python
_SUPPORTED_CONFIG_SCHEMA_VERSION = 2
```

Supported schema/hash/manifest compatibility version used by validators and canonical hashing.

#### `_SECTION_TYPES`

```python
_SECTION_TYPES = frozenset({"GENERAL", "ZONE_CHAPTER", "ARTICLE", "OTHER"})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema.

#### `_MAPPING_STATUSES`

```python
_MAPPING_STATUSES = frozenset({"EXACT", "CONFIG_ALIAS", "UNMAPPED", "AMBIGUOUS"})
```

Explicit mapping between source/input and target/output fields; keys and values are documented separately.

#### `_MAPPING_METHODS`

```python
_MAPPING_METHODS = frozenset({"EXACT_HEADING", "CONFIG_ALIAS", "NONE", "AMBIGUOUS"})
```

Explicit mapping between source/input and target/output fields; keys and values are documented separately.

#### `_EVIDENCE_SCOPES`

```python
_EVIDENCE_SCOPES = frozenset(
    {"GENERAL_RULE", "ZONE_SPECIFIC_RULE", "OTHER_TEXT"}
)
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema.

#### `_ZONE_INPUT_COLUMNS`

```python
_ZONE_INPUT_COLUMNS = (
    "planning_zone_id",
    "source_zone_id",
    "zone_label_raw",
    "source_document_id",
    "source_archive_sha256",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/structure_planning_regulation.py::_build_structure_result` (value argument/reference), `src/landscout/stages/structure_planning_regulation.py::_validate_result_self` (value argument/reference).

#### `_REQUIRED_INTERSECTION_INPUT_COLUMNS`

```python
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
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section.

#### `_OPTIONAL_INTERSECTION_INPUT_COLUMNS`

```python
_OPTIONAL_INTERSECTION_INPUT_COLUMNS = (
    "parcel_metric_area_m2",
    "zone_area_m2",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section.

#### `SECTION_COLUMNS`

```python
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
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/structure_planning_regulation.py::_build_sections` (value argument/reference), `src/landscout/stages/structure_planning_regulation.py::_result_with_hashes` (value argument/reference).

#### `ZONE_MAPPING_COLUMNS`

```python
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
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/structure_planning_regulation.py::_build_zone_mapping` (value argument/reference), `src/landscout/stages/structure_planning_regulation.py::_result_with_hashes` (value argument/reference).

#### `TOPIC_EVIDENCE_COLUMNS`

```python
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
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/structure_planning_regulation.py::_build_topic_evidence` (value argument/reference), `src/landscout/stages/structure_planning_regulation.py::_result_with_hashes` (value argument/reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

- `__all__` — explicit public export allow-list.
```python
__all__ = [
    "PlanningRegulationStructureConfig",
    "PlanningRegulationStructureError",
    "PlanningRegulationStructureResult",
    "load_planning_regulation_structure_config",
    "planning_regulation_section_page_fragments",
    "structure_planning_regulation",
    "validate_planning_regulation_structure",
    "validate_planning_regulation_structure_with_fragments",
]
```


### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `PlanningRegulationStructureError`

**Purpose:** Raised when factual regulation structure integrity cannot be proven.

**Kind:** controlled exception.

**Inheritance:** `ValueError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    load_planning_regulation_structure_config,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`.
- import/re-export: `src/landscout/stages/interpret_bess_zoning.py::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    validate_planning_regulation_structure_with_fragments,
)`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_construct_unique_mapping` via `PlanningRegulationStructureError`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::load_planning_regulation_structure_config` via `PlanningRegulationStructureError`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_strict_string` via `PlanningRegulationStructureError`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_strict_nonnegative_integer` via `PlanningRegulationStructureError`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_strict_positive_integer` via `PlanningRegulationStructureError`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validated_sha256` via `PlanningRegulationStructureError`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_canonical_value` via `PlanningRegulationStructureError`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_canonical_sha256` via `PlanningRegulationStructureError`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_document_lock` via `PlanningRegulationStructureError`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_line_records` via `PlanningRegulationStructureError`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_classify_structural_heading` via `PlanningRegulationStructureError`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_heading_events` via `PlanningRegulationStructureError`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_section_starts` via `PlanningRegulationStructureError`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_build_sections` via `PlanningRegulationStructureError`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validated_zoning_inputs` via `PlanningRegulationStructureError`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_resolved_alias` via `PlanningRegulationStructureError`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_build_zone_mapping` via `PlanningRegulationStructureError`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_evidence_scope` via `PlanningRegulationStructureError`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_page_tuple` via `PlanningRegulationStructureError`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_sections` via `PlanningRegulationStructureError`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_zone_mapping` via `PlanningRegulationStructureError`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_topic_evidence` via `PlanningRegulationStructureError`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_result_self` via `PlanningRegulationStructureError`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_resolved_config` via `PlanningRegulationStructureError`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_compare_expected_result` via `PlanningRegulationStructureError`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_section_page_fragments` via `PlanningRegulationStructureError`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::validate_planning_regulation_structure_with_fragments` via `PlanningRegulationStructureError`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::planning_regulation_section_page_fragments` via `PlanningRegulationStructureError`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::structure_planning_regulation` via `PlanningRegulationStructureError`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_old_and_unknown_result_config_schema_versions_are_rejected` via `pytest.raises(PlanningRegulationStructureError, match='schema version')`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_old_and_unknown_section_hash_schema_versions_are_rejected` via `pytest.raises(PlanningRegulationStructureError, match='schema version')`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_document_layout_rejects_nonexistent_indexed_pages` via `pytest.raises(PlanningRegulationStructureError)`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_document_lock_mismatch_is_rejected` via `pytest.raises(PlanningRegulationStructureError, match='document lock')`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_invalid_regex_and_unknown_yaml_field_are_controlled` via `pytest.raises(PlanningRegulationStructureError)`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_duplicate_yaml_alias_and_alias_cycle_are_rejected` via `pytest.raises(PlanningRegulationStructureError)`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_duplicate_yaml_alias_and_alias_cycle_are_rejected` via `pytest.raises(PlanningRegulationStructureError, match='Duplicate YAML')`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_evidence_scope_is_derived_from_exact_section_type` via `pytest.raises(PlanningRegulationStructureError, match='scope')`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_coordinated_frame_mutation_is_rejected` via `pytest.raises(PlanningRegulationStructureError)`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_unknown_topic_page_reference_is_rejected` via `pytest.raises(PlanningRegulationStructureError, match='unknown page')`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_coordinated_section_row_mutation_is_caught_by_outer_envelope` via `pytest.raises(PlanningRegulationStructureError)`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_dominant_unmapped_zone_stops_processing` via `pytest.raises(PlanningRegulationStructureError, match='Dominant candidate')`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_two_zone_patterns_matching_one_line_are_ambiguous` via `pytest.raises(PlanningRegulationStructureError)`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_two_article_patterns_matching_one_line_are_ambiguous` via `pytest.raises(PlanningRegulationStructureError, match='ARTICLE\\[0\\].*ARTICLE\\[1\\]')`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_general_and_article_cross_category_match_is_ambiguous` via `pytest.raises(PlanningRegulationStructureError)`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_zone_and_general_cross_category_match_is_ambiguous` via `pytest.raises(PlanningRegulationStructureError)`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_ambiguous_continuation_candidate_fails_with_record_diagnostic` via `pytest.raises(PlanningRegulationStructureError)`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_rejects_changed_ambiguous_grammar` via `pytest.raises(PlanningRegulationStructureError, match='Ambiguous structural heading')`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_lossless_partition_mutation_is_rejected` via `pytest.raises(PlanningRegulationStructureError)`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_duplicate_or_reordered_record_partition_is_rejected` via `pytest.raises(PlanningRegulationStructureError, match='partition')`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_unsorted_section_pages_are_rejected` via `pytest.raises(PlanningRegulationStructureError, match='page references')`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_article_parent_semantics_are_enforced` via `pytest.raises(PlanningRegulationStructureError)`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_wrong_intersection_source_zone_id_is_rejected` via `pytest.raises(PlanningRegulationStructureError, match='source-zone')`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_intersection_area_cannot_exceed_available_geometry_area` via `pytest.raises(PlanningRegulationStructureError, match='exceeds')`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_intersection_upper_bound_uses_shared_relative_tolerance` via `pytest.raises(PlanningRegulationStructureError, match='exceeds')`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_optional_intersection_metric_change_invalidates_existing_result` via `pytest.raises(PlanningRegulationStructureError, match='input hash')`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_intersection_hash_column_lineage_mutation_is_rejected` via `pytest.raises(PlanningRegulationStructureError, match='hash columns')`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_zone_mapping_contract_mutations_are_rejected` via `pytest.raises(PlanningRegulationStructureError)`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_topic_evidence_semantic_mutations_are_rejected` via `pytest.raises(PlanningRegulationStructureError)`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_coordinated_topic_evidence_and_hash_mutation_is_rebuilt_and_rejected` via `pytest.raises(PlanningRegulationStructureError)`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_rejects_post_build_source_change` via `pytest.raises(PlanningRegulationStructureError)`.
- callback/function object: `tests/unit/test_structure_planning_regulation.py::test_source_and_result_hash_mutation_is_rejected` via `pytest.raises(PlanningRegulationStructureError)`.
- import/re-export: `tests/unit/test_structure_planning_regulation.py::<module>` via `from landscout.stages.structure_planning_regulation import (
    SECTION_HASH_SCHEMA_VERSION,
    STRUCTURE_MANIFEST_SCHEMA_VERSION,
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    _heading_events,
    _line_records,
    _literal_topic_matches,
    _result_with_hashes,
    _section_content_sha256,
    load_planning_regulation_structure_config,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`.

**Exact class source**

```python
class PlanningRegulationStructureError(ValueError):
    """Raised when factual regulation structure integrity cannot be proven."""
```

### `_StrictConfigModel`

**Purpose:** Validates the planning contract carried by its explicit validators and inherited fields.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

**Exact class source**

```python
class _StrictConfigModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
```

### `DocumentLockConfig`

**Purpose:** Validates the planning contract carried by `document_id`, `pdf_sha256`, `pages_content_sha256`, `index_content_sha256`, `normalization_profile`.

**Kind:** Pydantic model.

**Inheritance:** `_StrictConfigModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `document_id` | `document_id: StrictStr = Field(min_length=1)` | Exact identity for the entity named by the field; uniqueness, portability, and lineage meaning are only those explicitly validated by the owner. |
| `pdf_sha256` | `pdf_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `pages_content_sha256` | `pages_content_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `index_content_sha256` | `index_content_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `normalization_profile` | `normalization_profile: StrictStr = Field(min_length=1)` | Stores `DocumentLockConfig`'s `normalization profile` value under exact annotation `StrictStr`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

**Interface consumers**

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

**Exact class source**

```python
class DocumentLockConfig(_StrictConfigModel):
    document_id: StrictStr = Field(min_length=1)
    pdf_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    pages_content_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    index_content_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    normalization_profile: StrictStr = Field(min_length=1)
```

### `DocumentLayoutConfig`

**Purpose:** Validates the planning contract carried by `body_start_page`, `table_of_contents_pages`, `max_heading_continuation_lines`, `include_table_of_contents_in_topic_evidence`.

**Kind:** Pydantic model.

**Inheritance:** `_StrictConfigModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `body_start_page` | `body_start_page: StrictInt = Field(ge=1)` | Stores `DocumentLayoutConfig`'s `body start page` value under exact annotation `StrictInt`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `table_of_contents_pages` | `table_of_contents_pages: tuple[StrictInt, ...] = ()` | Structured `table of contents pages` collection owned by `DocumentLayoutConfig`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `max_heading_continuation_lines` | `max_heading_continuation_lines: StrictInt = Field(ge=0, le=10)` | Stores `DocumentLayoutConfig`'s `max heading continuation lines` value under exact annotation `StrictInt`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `include_table_of_contents_in_topic_evidence` | `include_table_of_contents_in_topic_evidence: StrictBool = False` | Boolean `include table of contents in topic evidence` flag on `DocumentLayoutConfig`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |

**Validators (exact source)**

`_validate_pages`:

```python
def _validate_pages(self) -> DocumentLayoutConfig:
        pages = self.table_of_contents_pages
        if any(page < 1 for page in pages) or tuple(sorted(set(pages))) != pages:
            raise ValueError(
                "table_of_contents_pages must contain unique ascending positive integers"
            )
        return self
```

**Interface consumers**

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

**Exact class source**

```python
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
```

### `HeadingPatternsConfig`

**Purpose:** Validates the planning contract carried by `zone_chapter`, `article`, `general_section`, `continuation`.

**Kind:** Pydantic model.

**Inheritance:** `_StrictConfigModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `zone_chapter` | `zone_chapter: tuple[StrictStr, ...] = Field(min_length=1)` | Structured `zone chapter` collection owned by `HeadingPatternsConfig`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `article` | `article: tuple[StrictStr, ...] = Field(min_length=1)` | Structured `article` collection owned by `HeadingPatternsConfig`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `general_section` | `general_section: tuple[StrictStr, ...] = Field(min_length=1)` | Structured `general section` collection owned by `HeadingPatternsConfig`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `continuation` | `continuation: tuple[StrictStr, ...] = ()` | Structured `continuation` collection owned by `HeadingPatternsConfig`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |

**Interface consumers**

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

**Exact class source**

```python
class HeadingPatternsConfig(_StrictConfigModel):
    zone_chapter: tuple[StrictStr, ...] = Field(min_length=1)
    article: tuple[StrictStr, ...] = Field(min_length=1)
    general_section: tuple[StrictStr, ...] = Field(min_length=1)
    continuation: tuple[StrictStr, ...] = ()
```

### `IgnoredPatternsConfig`

**Purpose:** Validates the planning contract carried by `page_headers`, `page_footers`.

**Kind:** Pydantic model.

**Inheritance:** `_StrictConfigModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `page_headers` | `page_headers: tuple[StrictStr, ...] = ()` | Structured `page headers` collection owned by `IgnoredPatternsConfig`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `page_footers` | `page_footers: tuple[StrictStr, ...] = ()` | Structured `page footers` collection owned by `IgnoredPatternsConfig`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |

**Interface consumers**

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

**Exact class source**

```python
class IgnoredPatternsConfig(_StrictConfigModel):
    page_headers: tuple[StrictStr, ...] = ()
    page_footers: tuple[StrictStr, ...] = ()
```

### `TopicMatchPolicyConfig`

**Purpose:** Validates the planning contract carried by `boundary_mode`, `overlap_resolution`.

**Kind:** Pydantic model.

**Inheritance:** `_StrictConfigModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `boundary_mode` | `boundary_mode: Literal["token"]` | Stores `TopicMatchPolicyConfig`'s `boundary mode` value under exact annotation `Literal['token']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `overlap_resolution` | `overlap_resolution: Literal["longest_match"]` | Stores `TopicMatchPolicyConfig`'s `overlap resolution` value under exact annotation `Literal['longest_match']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

**Interface consumers**

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

**Exact class source**

```python
class TopicMatchPolicyConfig(_StrictConfigModel):
    boundary_mode: Literal["token"]
    overlap_resolution: Literal["longest_match"]

    @property
    def identifier(self) -> str:
        return f"{self.boundary_mode}_{self.overlap_resolution}"
```

### `PlanningRegulationStructureConfig`

**Purpose:** Strict, document-locked grammar for one factual regulation structure.

**Kind:** Pydantic model.

**Inheritance:** `_StrictConfigModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `schema_version` | `schema_version: StrictInt` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `structure_profile` | `structure_profile: StrictStr = Field(min_length=1)` | Stores `PlanningRegulationStructureConfig`'s `structure profile` value under exact annotation `StrictStr`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `document_lock` | `document_lock: DocumentLockConfig` | Stores `PlanningRegulationStructureConfig`'s `document lock` value under exact annotation `DocumentLockConfig`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `document_layout` | `document_layout: DocumentLayoutConfig` | Stores `PlanningRegulationStructureConfig`'s `document layout` value under exact annotation `DocumentLayoutConfig`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `heading_patterns` | `heading_patterns: HeadingPatternsConfig` | Stores `PlanningRegulationStructureConfig`'s `heading patterns` value under exact annotation `HeadingPatternsConfig`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `ignored_patterns` | `ignored_patterns: IgnoredPatternsConfig` | Stores `PlanningRegulationStructureConfig`'s `ignored patterns` value under exact annotation `IgnoredPatternsConfig`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `zone_aliases` | `zone_aliases: dict[StrictStr, StrictStr]` | Structured `zone aliases` collection owned by `PlanningRegulationStructureConfig`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `topics` | `topics: dict[StrictStr, tuple[StrictStr, ...]]` | Structured `topics` collection owned by `PlanningRegulationStructureConfig`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `topic_match_policy` | `topic_match_policy: TopicMatchPolicyConfig` | Stores `PlanningRegulationStructureConfig`'s `topic match policy` value under exact annotation `TopicMatchPolicyConfig`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `topic_context_characters` | `topic_context_characters: StrictInt = Field(ge=0)` | `PlanningRegulationStructureConfig`'s `topic context characters` evidence/text field; it retains the exact configured or source meaning under annotation `StrictInt` and is not promoted to a legal conclusion. |

**Validators (exact source)**

`_validate_grammar`:

```python
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
```

**Interface consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    load_planning_regulation_structure_config,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`.
- import/re-export: `src/landscout/stages/interpret_bess_zoning.py::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    validate_planning_regulation_structure_with_fragments,
)`.
- callback/function object: `src/landscout/stages/structure_planning_regulation.py::_resolved_config` via `isinstance(config, PlanningRegulationStructureConfig)`.
- import/re-export: `tests/unit/test_interpret_bess_zoning.py::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
)`.
- import/re-export: `tests/unit/test_structure_planning_regulation.py::<module>` via `from landscout.stages.structure_planning_regulation import (
    SECTION_HASH_SCHEMA_VERSION,
    STRUCTURE_MANIFEST_SCHEMA_VERSION,
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    _heading_events,
    _line_records,
    _literal_topic_matches,
    _result_with_hashes,
    _section_content_sha256,
    load_planning_regulation_structure_config,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`.

**Exact class source**

```python
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
```

### `PlanningRegulationStructureResult`

**Purpose:** Immutable lineage envelope for regulation sections and factual evidence.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `document_id` | `document_id: str` | Exact identity for the entity named by the field; uniqueness, portability, and lineage meaning are only those explicitly validated by the owner. |
| `archive_sha256` | `archive_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `pdf_sha256` | `pdf_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `index_content_sha256` | `index_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `structure_profile` | `structure_profile: str` | Stores `PlanningRegulationStructureResult`'s `structure profile` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `structure_config_schema_version` | `structure_config_schema_version: int` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `structure_config_sha256` | `structure_config_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `zones_content_sha256` | `zones_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `zoning_intersection_hash_columns` | `zoning_intersection_hash_columns: tuple[str, ...]` | Structured `zoning intersection hash columns` collection owned by `PlanningRegulationStructureResult`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `zoning_intersections_content_sha256` | `zoning_intersections_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `source_records_sha256` | `source_records_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `section_hash_schema_version` | `section_hash_schema_version: int` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `sections_content_sha256` | `sections_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `zone_map_content_sha256` | `zone_map_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `topic_evidence_content_sha256` | `topic_evidence_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `structure_result_content_sha256` | `structure_result_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `sections` | `sections: pd.DataFrame` | Stores `PlanningRegulationStructureResult`'s `sections` value under exact annotation `pd.DataFrame`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `zone_mapping` | `zone_mapping: pd.DataFrame` | Stores `PlanningRegulationStructureResult`'s `zone mapping` value under exact annotation `pd.DataFrame`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `topic_evidence` | `topic_evidence: pd.DataFrame` | `PlanningRegulationStructureResult`'s `topic evidence` evidence/text field; it retains the exact configured or source meaning under annotation `pd.DataFrame` and is not promoted to a legal conclusion. |

**Interface consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    load_planning_regulation_structure_config,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`.
- import/re-export: `src/landscout/stages/interpret_bess_zoning.py::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    validate_planning_regulation_structure_with_fragments,
)`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_build_structure_result` via `PlanningRegulationStructureResult`.
- callback/function object: `src/landscout/stages/structure_planning_regulation.py::_validate_result_self` via `isinstance(result, PlanningRegulationStructureResult)`.

**Exact class source**

```python
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
```

### `_LineRecord`

**Purpose:** Immutable result/value envelope carrying `record_id`, `page_number`, `page_line_number`, `raw`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `record_id` | `record_id: str` | Exact identity for the entity named by the field; uniqueness, portability, and lineage meaning are only those explicitly validated by the owner. |
| `page_number` | `page_number: int` | Stores `_LineRecord`'s `page number` value under exact annotation `int`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `page_line_number` | `page_line_number: int` | Stores `_LineRecord`'s `page line number` value under exact annotation `int`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `raw` | `raw: str` | Stores `_LineRecord`'s `raw` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

**Interface consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_line_records` via `_LineRecord`.

**Exact class source**

```python
class _LineRecord:
    record_id: str
    page_number: int
    page_line_number: int
    raw: str
```

### `_HeadingEvent`

**Purpose:** Immutable result/value envelope carrying `record_position`, `section_type`, `heading_raw`, `heading_normalized`, `zone_chapter_label`, `article_number_raw`, `article_title_raw`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `record_position` | `record_position: int` | Stores `_HeadingEvent`'s `record position` value under exact annotation `int`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `section_type` | `section_type: Literal["GENERAL", "ZONE_CHAPTER", "ARTICLE"]` | Closed or validated `section type` classification on `_HeadingEvent`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `heading_raw` | `heading_raw: str` | Stores `_HeadingEvent`'s `heading raw` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `heading_normalized` | `heading_normalized: str` | Stores `_HeadingEvent`'s `heading normalized` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `zone_chapter_label` | `zone_chapter_label: str \| None` | `_HeadingEvent`'s `zone chapter label` evidence/text field; it retains the exact configured or source meaning under annotation `str | None` and is not promoted to a legal conclusion. |
| `article_number_raw` | `article_number_raw: str \| None` | Stores `_HeadingEvent`'s `article number raw` value under exact annotation `str | None`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `article_title_raw` | `article_title_raw: str \| None` | `_HeadingEvent`'s `article title raw` evidence/text field; it retains the exact configured or source meaning under annotation `str | None` and is not promoted to a legal conclusion. |

**Interface consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_heading_events` via `_HeadingEvent`.

**Exact class source**

```python
class _HeadingEvent:
    record_position: int
    section_type: Literal["GENERAL", "ZONE_CHAPTER", "ARTICLE"]
    heading_raw: str
    heading_normalized: str
    zone_chapter_label: str | None
    article_number_raw: str | None
    article_title_raw: str | None
```

### `_StructuralHeadingMatch`

**Purpose:** Immutable result/value envelope carrying `section_type`, `pattern_index`, `named_captures`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `section_type` | `section_type: Literal["GENERAL", "ZONE_CHAPTER", "ARTICLE"]` | Closed or validated `section type` classification on `_StructuralHeadingMatch`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `pattern_index` | `pattern_index: int` | Stores `_StructuralHeadingMatch`'s `pattern index` value under exact annotation `int`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `named_captures` | `named_captures: tuple[tuple[str, str \| None], ...]` | Structured `named captures` collection owned by `_StructuralHeadingMatch`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |

**Interface consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_classify_structural_heading` via `_StructuralHeadingMatch`.

**Exact class source**

```python
class _StructuralHeadingMatch:
    section_type: Literal["GENERAL", "ZONE_CHAPTER", "ARTICLE"]
    pattern_index: int
    named_captures: tuple[tuple[str, str | None], ...]
```

### `_SectionBoundary`

**Purpose:** Immutable result/value envelope carrying `record_position`, `event`, `forced_table_of_contents`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `record_position` | `record_position: int` | Stores `_SectionBoundary`'s `record position` value under exact annotation `int`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `event` | `event: _HeadingEvent \| None` | Stores `_SectionBoundary`'s `event` value under exact annotation `_HeadingEvent | None`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `forced_table_of_contents` | `forced_table_of_contents: bool` | Boolean `forced table of contents` flag on `_SectionBoundary`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |

**Interface consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_section_starts` via `_SectionBoundary`.

**Exact class source**

```python
class _SectionBoundary:
    record_position: int
    event: _HeadingEvent | None
    forced_table_of_contents: bool
```

### `_SectionBuild`

**Purpose:** Immutable result/value envelope carrying `row`, `page_fragments`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `row` | `row: dict[str, object]` | Structured `row` collection owned by `_SectionBuild`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `page_fragments` | `page_fragments: tuple[tuple[int, str], ...]` | Structured `page fragments` collection owned by `_SectionBuild`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |

**Interface consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_build_sections` via `_SectionBuild`.

**Exact class source**

```python
class _SectionBuild:
    row: dict[str, object]
    page_fragments: tuple[tuple[int, str], ...]
```

### `_UniqueKeyLoader`

**Purpose:** Private PyYAML SafeLoader subclass whose mapping constructor is replaced to reject duplicate YAML keys.

**Kind:** PyYAML loader subclass.

**Inheritance:** `yaml.SafeLoader`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- callback/function object: `src/landscout/stages/bess_planning_feature_policy.py::load_bess_planning_feature_policy_config` via `yaml.load(Path(path).read_text(encoding='utf-8'), Loader=_UniqueKeyLoader)`.
- callback/function object: `src/landscout/stages/interpret_bess_zoning.py::load_bess_zoning_policy_config` via `yaml.load(Path(path).read_text(encoding='utf-8'), Loader=_UniqueKeyLoader)`.
- callback/function object: `src/landscout/stages/resolve_planning_feature_codes.py::load_cnig_feature_code_profile` via `yaml.load(Path(path).read_text(encoding='utf-8'), Loader=_UniqueKeyLoader)`.
- callback/function object: `src/landscout/stages/road_vehicle_proxy_policy.py::load_ign_road_vehicle_proxy_policy` via `yaml.load(policy_bytes.decode('utf-8'), Loader=_UniqueKeyLoader)`.
- callback/function object: `src/landscout/stages/structure_planning_regulation.py::load_planning_regulation_structure_config` via `yaml.load(config_path.read_text(encoding='utf-8'), Loader=_UniqueKeyLoader)`.

**Exact class source**

```python
class _UniqueKeyLoader(yaml.SafeLoader):
    pass
```

### `_TopicMatch`

**Purpose:** Immutable result/value envelope carrying `term_index`, `search_term`, `normalized_term`, `normalized_start`, `normalized_end`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `term_index` | `term_index: int` | Stores `_TopicMatch`'s `term index` value under exact annotation `int`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `search_term` | `search_term: str` | Stores `_TopicMatch`'s `search term` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `normalized_term` | `normalized_term: str` | Stores `_TopicMatch`'s `normalized term` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `normalized_start` | `normalized_start: int` | Stores `_TopicMatch`'s `normalized start` value under exact annotation `int`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `normalized_end` | `normalized_end: int` | Stores `_TopicMatch`'s `normalized end` value under exact annotation `int`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

**Interface consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_literal_topic_matches` via `_TopicMatch`.

**Exact class source**

```python
class _TopicMatch:
    term_index: int
    search_term: str
    normalized_term: str
    normalized_start: int
    normalized_end: int
```


## 6. Functions and methods

### `DocumentLayoutConfig._validate_pages`

**Exact signature**

```python
def _validate_pages(self) -> DocumentLayoutConfig:
```

**Purpose**

Rejects malformed or inconsistent pages; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `DocumentLayoutConfig`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- Guard with a raise path: `any((page < 1 for page in pages)) or tuple(sorted(set(pages))) != pages`.
- Explicit raise expressions: `ValueError('table_of_contents_pages must contain unique ascending positive integers')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_index` via `_validate_pages`.

**Complete source-ordered implementation**

```python
def _validate_pages(self) -> DocumentLayoutConfig:
        pages = self.table_of_contents_pages
        if any(page < 1 for page in pages) or tuple(sorted(set(pages))) != pages:
            raise ValueError(
                "table_of_contents_pages must contain unique ascending positive integers"
            )
        return self
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `TopicMatchPolicyConfig.identifier`

**Exact signature**

```python
def identifier(self) -> str:
```

**Purpose**

Private `planning` helper for identifier; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
f'{self.boundary_mode}_{self.overlap_resolution}'
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- callback/function object: `src/landscout/stages/enrich_shape.py::enrich_parcel_shapes` via `isinstance(identifier, str)`.
- callback/function object: `src/landscout/stages/filter_parcels.py::_validate_exact_parcel_ids` via `isinstance(identifier, str)`.
- callback/function object: `src/landscout/stages/normalize_access_ign.py::_validate_identifiers` via `isinstance(identifier, str)`.
- callback/function object: `src/landscout/stages/normalize_grid_ign.py::_validate_input` via `isinstance(identifier, str)`.
- callback/function object: `src/landscout/stages/profile_shape.py::profile_shape_distribution` via `isinstance(identifier, str)`.
- callback/function object: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_coded_meaning_rows` via `isinstance(identifier, str)`.
- callback/function object: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_coded_meaning_rows` via `features.get(identifier)`.
- callback/function object: `src/landscout/stages/resolve_planning_feature_codes.py::_coded_relations` via `meanings.get(identifier)`.
- property/attribute access: `src/landscout/stages/structure_planning_regulation.py::_build_topic_evidence` via `config.topic_match_policy.identifier`.
- property/attribute access: `src/landscout/stages/structure_planning_regulation.py::_validate_topic_evidence` via `config.topic_match_policy.identifier`.

**Complete source-ordered implementation**

```python
def identifier(self) -> str:
        return f"{self.boundary_mode}_{self.overlap_resolution}"
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `PlanningRegulationStructureConfig._validate_grammar`

**Exact signature**

```python
def _validate_grammar(self) -> PlanningRegulationStructureConfig:
```

**Purpose**

Rejects malformed or inconsistent grammar; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `PlanningRegulationStructureConfig`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- Guard with a raise path: `self.schema_version != _SUPPORTED_CONFIG_SCHEMA_VERSION`.
- Guard with a raise path: `not self.topics`.
- Guard with a raise path: `len(set(patterns)) != len(patterns)`.
- Guard with a raise path: `not terms`.
- Guard with a raise path: `previous is not None`.
- Guard with a raise path: `missing`.
- Guard with a raise path: `not normalized_term or normalized_term in normalized`.
- Explicit raise expressions: `ValueError('regular-expression patterns must be unique')`, `ValueError('topics must not be empty')`, `ValueError(f'identical structural heading regex is reused across groups {previous} and {category}')`, `ValueError(f'invalid regular expression: {pattern}')`, `ValueError(f'topic {topic!r} contains duplicate normalized terms')`, `ValueError(f'topic {topic!r} must contain literal terms')`, `ValueError(f'unsupported structure config schema: {self.schema_version}')`, `ValueError(f'{label} pattern lacks named captures: {sorted(missing)}')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `structural_pattern_owners[pattern]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_construct_unique_mapping`

**Exact signature**

```python
def _construct_unique_mapping(
    loader: yaml.SafeLoader,
    node: yaml.MappingNode,
    deep: bool = False,
) -> dict[object, object]:
```

**Purpose**

Private `planning` helper for construct unique mapping; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[object, object]`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- Guard with a raise path: `key in result`.
- Explicit raise expressions: `PlanningRegulationStructureError(f'Duplicate YAML configuration key: {key!r}')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `result[key]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- callback/function object: `src/landscout/stages/bess_planning_feature_policy.py::<module>` via `_UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_unique_mapping)`.
- callback/function object: `src/landscout/stages/interpret_bess_zoning.py::<module>` via `_UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_unique_mapping)`.
- callback/function object: `src/landscout/stages/resolve_planning_feature_codes.py::<module>` via `_UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_unique_mapping)`.
- callback/function object: `src/landscout/stages/road_vehicle_proxy_policy.py::<module>` via `_UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_unique_mapping)`.
- callback/function object: `src/landscout/stages/structure_planning_regulation.py::<module>` via `_UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_unique_mapping)`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_exact_config_string`

**Exact signature**

```python
def _exact_config_string(value: str, label: str) -> str:
```

**Purpose**

Private `planning` helper for exact config string; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- Guard with a raise path: `not value or value != value.strip()`.
- Explicit raise expressions: `ValueError(f'{label} must be a non-empty exact string')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::PlanningRegulationStructureConfig._validate_grammar` via `_exact_config_string`.

**Complete source-ordered implementation**

```python
def _exact_config_string(value: str, label: str) -> str:
    if not value or value != value.strip():
        raise ValueError(f"{label} must be a non-empty exact string")
    return value
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_alias_cycles`

**Exact signature**

```python
def _validate_alias_cycles(aliases: Mapping[str, str]) -> None:
```

**Purpose**

Rejects malformed or inconsistent alias cycles; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `current in seen`.
- Explicit raise expressions: `ValueError(f'zone alias cycle detected at {current!r}')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::PlanningRegulationStructureConfig._validate_grammar` via `_validate_alias_cycles`.

**Complete source-ordered implementation**

```python
def _validate_alias_cycles(aliases: Mapping[str, str]) -> None:
    for start in aliases:
        seen: set[str] = set()
        current = start
        while current in aliases:
            if current in seen:
                raise ValueError(f"zone alias cycle detected at {current!r}")
            seen.add(current)
            current = aliases[current]
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `load_planning_regulation_structure_config`

**Exact signature**

```python
def load_planning_regulation_structure_config(
    path: str | Path,
) -> PlanningRegulationStructureConfig:
```

**Purpose**

Load and strictly validate a document-specific structure grammar.

**Return contract**

- Declared return annotation: `PlanningRegulationStructureConfig`.
- Every observed return expression is reproduced without truncation:
```python
PlanningRegulationStructureConfig.model_validate(payload)
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(payload, Mapping)`.
- Explicit raise expressions: `PlanningRegulationStructureError('Planning structure configuration is invalid')`, `PlanningRegulationStructureError('Planning structure configuration must be a mapping')`, `re-raise`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: `config_path.read_text`.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    load_planning_regulation_structure_config,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_resolved_config` via `load_planning_regulation_structure_config`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_invalid_regex_and_unknown_yaml_field_are_controlled` via `load_planning_regulation_structure_config`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_duplicate_yaml_alias_and_alias_cycle_are_rejected` via `load_planning_regulation_structure_config`.
- import/re-export: `tests/unit/test_structure_planning_regulation.py::<module>` via `from landscout.stages.structure_planning_regulation import (
    SECTION_HASH_SCHEMA_VERSION,
    STRUCTURE_MANIFEST_SCHEMA_VERSION,
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    _heading_events,
    _line_records,
    _literal_topic_matches,
    _result_with_hashes,
    _section_content_sha256,
    load_planning_regulation_structure_config,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_strict_string`

**Exact signature**

```python
def _strict_string(value: object, label: str) -> str:
```

**Purpose**

Private `planning` helper for strict string; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(value, str) or not value or value != value.strip()`.
- Explicit raise expressions: `PlanningRegulationStructureError(f'{label} must be a non-empty exact string')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_validate_exact_strings` via `_strict_string`.
- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_validate_optional_exact_strings` via `_strict_string`.
- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_standard_model` via `_strict_string`.
- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_planning_context` via `_strict_string`.
- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_normalize_layer` via `_strict_string`.
- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_validate_catalog_identity` via `_strict_string`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_validated_sha256` via `_strict_string`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_validated_relative_path` via `_strict_string`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_validated_pdf_basename` via `_strict_string`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_validate_document_lineage` via `_strict_string`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_written_file_matches` via `_strict_string`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_locate_regulation_pdf` via `_strict_string`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_index` via `_strict_string`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_validated_terms` via `_strict_string`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_search_result` via `_strict_string`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_validated_sha256` via `_strict_string`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_exact_id_series` via `_strict_string`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_validate_zones` via `_strict_string`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_validate_relations` via `_strict_string`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_zone_chapter_rows` via `_strict_string`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_validate_policy_evidence` via `_strict_string`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_validate_mapping` via `_strict_string`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_build_chapter_policy` via `_strict_string`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_build_source_zone_policy` via `_strict_string`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_build_parcel_output` via `_strict_string`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_planning_standard` via `_strict_string`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_coded_relations` via `_strict_string`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_inspected_layer_payload` via `_strict_string`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_planning_document_context_sha256` via `_strict_string`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_result_envelope` via `_strict_string`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validated_sha256` via `_strict_string`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_canonical_chapter_label` via `_strict_string`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_source_label_values` via `_strict_string`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_build_zone_mapping` via `_strict_string`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_sections` via `_strict_string`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_zone_mapping` via `_strict_string`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_topic_evidence` via `_strict_string`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_result_self` via `_strict_string`.

**Complete source-ordered implementation**

```python
def _strict_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise PlanningRegulationStructureError(
            f"{label} must be a non-empty exact string"
        )
    return value
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_strict_nonnegative_integer`

**Exact signature**

```python
def _strict_nonnegative_integer(value: object, label: str) -> int:
```

**Purpose**

Private `planning` helper for strict nonnegative integer; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `int`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- Guard with a raise path: `isinstance(value, bool) or not isinstance(value, Integral)`.
- Guard with a raise path: `result < 0`.
- Explicit raise expressions: `PlanningRegulationStructureError(f'{label} must be an integer')`, `PlanningRegulationStructureError(f'{label} must be non-negative')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_validate_coverage_summary` via `_strict_nonnegative_integer`.
- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_validate_layer_summary` via `_strict_nonnegative_integer`.
- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_integer_values` via `_strict_nonnegative_integer`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_strict_positive_integer` via `_strict_nonnegative_integer`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_validate_pages` via `_strict_nonnegative_integer`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::search_planning_regulation` via `_strict_nonnegative_integer`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_search_result` via `_strict_nonnegative_integer`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_strict_positive_integer` via `_strict_nonnegative_integer`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_validate_parcels` via `_strict_nonnegative_integer`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_compare_results` via `_strict_nonnegative_integer`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_strict_positive_integer` via `_strict_nonnegative_integer`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_sections` via `_strict_nonnegative_integer`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_zone_mapping` via `_strict_nonnegative_integer`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_topic_evidence` via `_strict_nonnegative_integer`.

**Complete source-ordered implementation**

```python
def _strict_nonnegative_integer(value: object, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, Integral):
        raise PlanningRegulationStructureError(f"{label} must be an integer")
    result = int(value)
    if result < 0:
        raise PlanningRegulationStructureError(f"{label} must be non-negative")
    return result
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_strict_positive_integer`

**Exact signature**

```python
def _strict_positive_integer(value: object, label: str) -> int:
```

**Purpose**

Private `planning` helper for strict positive integer; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `int`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- Guard with a raise path: `result == 0`.
- Explicit raise expressions: `PlanningRegulationStructureError(f'{label} must be positive')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_supported_schema_version` via `_strict_positive_integer`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_locate_regulation_pdf` via `_strict_positive_integer`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_validate_pages` via `_strict_positive_integer`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_index` via `_strict_positive_integer`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_search_result` via `_strict_positive_integer`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_validate_policy_evidence` via `_strict_positive_integer`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_compare_results` via `_strict_positive_integer`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_document_lock` via `_strict_positive_integer`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_line_records` via `_strict_positive_integer`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_page_tuple` via `_strict_positive_integer`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_sections` via `_strict_positive_integer`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_topic_evidence` via `_strict_positive_integer`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_result_self` via `_strict_positive_integer`.

**Complete source-ordered implementation**

```python
def _strict_positive_integer(value: object, label: str) -> int:
    result = _strict_nonnegative_integer(value, label)
    if result == 0:
        raise PlanningRegulationStructureError(f"{label} must be positive")
    return result
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validated_sha256`

**Exact signature**

```python
def _validated_sha256(value: object, label: str) -> str:
```

**Purpose**

Checks and returns canonical sha256; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
checksum
```

**Validation and exceptions**

- Guard with a raise path: `re.fullmatch('[0-9a-f]{64}', checksum) is None`.
- Explicit raise expressions: `PlanningRegulationStructureError(f'{label} must be exactly 64 lowercase hexadecimal characters')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_validate_document_lineage` via `_validated_sha256`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_locate_regulation_pdf` via `_validated_sha256`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_validate_pages` via `_validated_sha256`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_index` via `_validated_sha256`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_search_result` via `_validated_sha256`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_compare_results` via `_validated_sha256`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_sections` via `_validated_sha256`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_result_self` via `_validated_sha256`.

**Complete source-ordered implementation**

```python
def _validated_sha256(value: object, label: str) -> str:
    checksum = _strict_string(value, label)
    if re.fullmatch(r"[0-9a-f]{64}", checksum) is None:
        raise PlanningRegulationStructureError(
            f"{label} must be exactly 64 lowercase hexadecimal characters"
        )
    return checksum
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_value`

**Exact signature**

```python
def _canonical_value(value: object) -> object:
```

**Purpose**

Private `planning` helper for canonical value; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `object`.
- Every observed return expression is reproduced without truncation:
```python
None

_canonical_value(value.item())

[_canonical_value(item) for item in value]

{str(key): _canonical_value(item) for key, item in value.items()}

None

value
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `PlanningRegulationStructureError(f'Value of type {type(value).__name__} cannot be canonically serialized')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_canonical_value` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_frame_payload` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_canonical_value` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_frame_payload` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_canonical_value` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_frame_payload` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_canonical_value` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_canonical_sha256` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_frame_payload` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_compare_frames` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_compare_results` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_canonical_value` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_frame_payload` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_compare_frame` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_canonical_sha256` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_canonical_frame_rows` via `_canonical_value`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_sha256`

**Exact signature**

```python
def _canonical_sha256(value: object) -> str:
```

**Purpose**

Private `planning` helper for canonical sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
sha256(serialized).hexdigest()
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `PlanningRegulationStructureError('Canonical integrity serialization failed')`, `re-raise`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `sha256`, `sha256(serialized).hexdigest`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_frame_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_result_with_hashes` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_page_content_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_pages_content_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_index_content_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_source_selection_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_hits_content_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_frame_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_policy_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_factual_structure_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_zone_mapping_input_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_result_frame_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_complete_result_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_config_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_source_records_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_section_content_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_input_frame_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_frame_hash` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_structure_result_content_sha256` via `_canonical_sha256`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::_policy_payload` via `_canonical_sha256`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::_validated_config` via `_canonical_sha256`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_checked_in_policy_complete_snapshot_is_immutable` via `_canonical_sha256`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_profile_v1_snapshot_detects_policy_text_drift` via `_canonical_sha256`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_profile_v1_snapshot_detects_source_lock_drift` via `_canonical_sha256`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_duplicate_policy_pair_is_rejected` via `_canonical_sha256`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_invalid_or_legal_conclusion_status_is_rejected` via `_canonical_sha256`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_invalid_confidence_is_rejected` via `_canonical_sha256`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_noncanonical_whitespace_is_rejected` via `_canonical_sha256`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_policy_entries_require_deterministic_order` via `_canonical_sha256`.
- direct call or construction: `tests/unit/test_index_planning_regulation.py::test_canonical_hash_serialization_failure_is_controlled_and_chained` via `regulation_module._canonical_sha256`.
- property/attribute access: `tests/unit/test_index_planning_regulation.py::test_canonical_hash_serialization_failure_is_controlled_and_chained` via `regulation_module._canonical_sha256`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_config_sha256`

**Exact signature**

```python
def _config_sha256(config: PlanningRegulationStructureConfig) -> str:
```

**Purpose**

Private `planning` helper for config sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_sha256({'domain': 'landscout.planning_regulation.structure_config', 'config': payload})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_canonical_sha256`.
- Environment/process effects: none directly visible.
- In-memory mutation: `payload['topics']`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_build_structure_result` via `_config_sha256`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_result_self` via `_config_sha256`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_document_lock`

**Exact signature**

```python
def _validate_document_lock(
    index: PlanningRegulationIndex,
    config: PlanningRegulationStructureConfig,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent document lock; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `config.document_layout.body_start_page not in indexed_page_set`.
- Guard with a raise path: `missing_toc_pages`.
- Guard with a raise path: `actual != expected`.
- Explicit raise expressions: `PlanningRegulationStructureError('body_start_page must reference a real indexed page')`, `PlanningRegulationStructureError(f'Planning structure {label} differs from its document lock')`, `PlanningRegulationStructureError(f'table_of_contents_pages reference nonexistent indexed pages: {missing_toc_pages}')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::validate_planning_regulation_structure_with_fragments` via `_validate_document_lock`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::structure_planning_regulation` via `_validate_document_lock`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_compiled`

**Exact signature**

```python
def _compiled(patterns: Sequence[str]) -> tuple[re.Pattern[str], ...]:
```

**Purpose**

Private `planning` helper for compiled; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[re.Pattern[str], ...]`.
- Every observed return expression is reproduced without truncation:
```python
tuple((re.compile(pattern) for pattern in patterns))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_line_records` via `_compiled`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_heading_events` via `_compiled`.

**Complete source-ordered implementation**

```python
def _compiled(patterns: Sequence[str]) -> tuple[re.Pattern[str], ...]:
    return tuple(re.compile(pattern) for pattern in patterns)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_matches_any`

**Exact signature**

```python
def _matches_any(value: str, patterns: Sequence[re.Pattern[str]]) -> bool:
```

**Purpose**

Private `planning` helper for matches any; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
any((pattern.fullmatch(value) is not None for pattern in patterns))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_retained_page_lines` via `_matches_any`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_heading_events` via `_matches_any`.

**Complete source-ordered implementation**

```python
def _matches_any(value: str, patterns: Sequence[re.Pattern[str]]) -> bool:
    return any(pattern.fullmatch(value) is not None for pattern in patterns)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_retained_page_lines`

**Exact signature**

```python
def _retained_page_lines(
    raw_text: str,
    headers: Sequence[re.Pattern[str]],
    footers: Sequence[re.Pattern[str]],
) -> list[tuple[int, str]]:
```

**Purpose**

Private `planning` helper for retained page lines; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `list[tuple[int, str]]`.
- Every observed return expression is reproduced without truncation:
```python
lines[start:end]
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_line_records` via `_retained_page_lines`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_line_records`

**Exact signature**

```python
def _line_records(
    index: PlanningRegulationIndex,
    config: PlanningRegulationStructureConfig,
) -> list[_LineRecord]:
```

**Purpose**

Private `planning` helper for line records; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `list[_LineRecord]`.
- Every observed return expression is reproduced without truncation:
```python
records
```

**Validation and exceptions**

- Guard with a raise path: `not records`.
- Guard with a raise path: `not isinstance(raw_text, str)`.
- Explicit raise expressions: `PlanningRegulationStructureError('Page raw text must be a string')`, `PlanningRegulationStructureError('Regulation contains no structural text')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_build_sections` via `_line_records`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_positional_header_footer_filter_preserves_matching_body_lines` via `_line_records`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_page_without_configured_header_or_footer_is_unchanged` via `_line_records`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_blank_only_prefix_is_preserved_in_first_actual_section` via `_line_records`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::_structure_with_document_layout` via `_line_records`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_unique_zone_heading_and_nonheading_line_are_classified_deterministically` via `_line_records`.
- import/re-export: `tests/unit/test_structure_planning_regulation.py::<module>` via `from landscout.stages.structure_planning_regulation import (
    SECTION_HASH_SCHEMA_VERSION,
    STRUCTURE_MANIFEST_SCHEMA_VERSION,
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    _heading_events,
    _line_records,
    _literal_topic_matches,
    _result_with_hashes,
    _section_content_sha256,
    load_planning_regulation_structure_config,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_source_record_payload`

**Exact signature**

```python
def _source_record_payload(record: _LineRecord) -> dict[str, object]:
```

**Purpose**

Private `planning` helper for source record payload; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
{'record_id': record.record_id, 'page_number': record.page_number, 'page_line_number': record.page_line_number, 'raw_text': record.raw}
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_source_records_sha256` via `_source_record_payload`.

**Complete source-ordered implementation**

```python
def _source_record_payload(record: _LineRecord) -> dict[str, object]:
    return {
        "record_id": record.record_id,
        "page_number": record.page_number,
        "page_line_number": record.page_line_number,
        "raw_text": record.raw,
    }
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_source_records_sha256`

**Exact signature**

```python
def _source_records_sha256(records: Sequence[_LineRecord]) -> str:
```

**Purpose**

Private `planning` helper for source records sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_sha256({'domain': 'landscout.planning_regulation.source_records', 'section_hash_schema_version': SECTION_HASH_SCHEMA_VERSION, 'records': [_source_record_payload(record) for record in records]})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_canonical_sha256`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_build_sections` via `_source_records_sha256`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_sections` via `_source_records_sha256`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_build_structure_result` via `_source_records_sha256`.

**Complete source-ordered implementation**

```python
def _source_records_sha256(records: Sequence[_LineRecord]) -> str:
    return _canonical_sha256(
        {
            "domain": "landscout.planning_regulation.source_records",
            "section_hash_schema_version": SECTION_HASH_SCHEMA_VERSION,
            "records": [_source_record_payload(record) for record in records],
        }
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_chapter_label`

**Exact signature**

```python
def _canonical_chapter_label(value: str) -> str:
```

**Purpose**

Private `planning` helper for canonical chapter label; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_strict_string(label, 'zone chapter label')
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_heading_events` via `_canonical_chapter_label`.

**Complete source-ordered implementation**

```python
def _canonical_chapter_label(value: str) -> str:
    label = re.sub(r"\s+", "", value)
    return _strict_string(label, "zone chapter label")
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_classify_structural_heading`

**Exact signature**

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

Private `planning` helper for classify structural heading; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `_StructuralHeadingMatch | None`.
- Every observed return expression is reproduced without truncation:
```python
matches[0] if matches else None
```

**Validation and exceptions**

- Guard with a raise path: `len(matches) > 1`.
- Explicit raise expressions: `PlanningRegulationStructureError(f'Ambiguous structural heading at {record.record_id}, page {record.page_number}, line {record.page_line_number}: {diagnostics}')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_heading_events` via `_classify_structural_heading`.

**Complete source-ordered implementation**

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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_heading_events`

**Exact signature**

```python
def _heading_events(
    records: Sequence[_LineRecord],
    config: PlanningRegulationStructureConfig,
) -> list[_HeadingEvent]:
```

**Purpose**

Private `planning` helper for heading events; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `list[_HeadingEvent]`.
- Every observed return expression is reproduced without truncation:
```python
events
```

**Validation and exceptions**

- Guard with a raise path: `not events`.
- Explicit raise expressions: `PlanningRegulationStructureError('No regulation body headings matched the configured grammar')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_build_sections` via `_heading_events`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_unique_zone_heading_and_nonheading_line_are_classified_deterministically` via `_heading_events`.
- import/re-export: `tests/unit/test_structure_planning_regulation.py::<module>` via `from landscout.stages.structure_planning_regulation import (
    SECTION_HASH_SCHEMA_VERSION,
    STRUCTURE_MANIFEST_SCHEMA_VERSION,
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    _heading_events,
    _line_records,
    _literal_topic_matches,
    _result_with_hashes,
    _section_content_sha256,
    load_planning_regulation_structure_config,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_page_fragments`

**Exact signature**

```python
def _page_fragments(records: Sequence[_LineRecord]) -> tuple[tuple[int, str], ...]:
```

**Purpose**

Private `planning` helper for page fragments; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[tuple[int, str], ...]`.
- Every observed return expression is reproduced without truncation:
```python
tuple(fragments)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_build_sections` via `_page_fragments`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_contiguous_page_blocks`

**Exact signature**

```python
def _contiguous_page_blocks(pages: Sequence[int]) -> tuple[tuple[int, ...], ...]:
```

**Purpose**

Private `planning` helper for contiguous page blocks; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[tuple[int, ...], ...]`.
- Every observed return expression is reproduced without truncation:
```python
tuple((tuple(block) for block in blocks))

()
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_section_starts` via `_contiguous_page_blocks`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_section_starts`

**Exact signature**

```python
def _section_starts(
    records: Sequence[_LineRecord],
    events: Sequence[_HeadingEvent],
    config: PlanningRegulationStructureConfig,
) -> list[_SectionBoundary]:
```

**Purpose**

Private `planning` helper for section starts; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `list[_SectionBoundary]`.
- Every observed return expression is reproduced without truncation:
```python
coalesced
```

**Validation and exceptions**

- Guard with a raise path: `not ordered`.
- Explicit raise expressions: `PlanningRegulationStructureError('No regulation section boundary could be established')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `_SectionBoundary`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `compacted[boundary.record_position]`, `ordered[0]`, `ordered[boundary_index + 1]`, `ordered[boundary_index]`, `starts_by_position[block_end]`, `starts_by_position[block_start]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_build_sections` via `_section_starts`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_section_content_sha256`

**Exact signature**

```python
def _section_content_sha256(row: Mapping[str, object]) -> str:
```

**Purpose**

Private `planning` helper for section content sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_sha256({'domain': 'landscout.planning_regulation.section', 'section_hash_schema_version': SECTION_HASH_SCHEMA_VERSION, 'section': content})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_canonical_sha256`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_build_sections` via `_section_content_sha256`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_sections` via `_section_content_sha256`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_coordinated_section_row_mutation_is_caught_by_outer_envelope` via `_section_content_sha256`.
- import/re-export: `tests/unit/test_structure_planning_regulation.py::<module>` via `from landscout.stages.structure_planning_regulation import (
    SECTION_HASH_SCHEMA_VERSION,
    STRUCTURE_MANIFEST_SCHEMA_VERSION,
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    _heading_events,
    _line_records,
    _literal_topic_matches,
    _result_with_hashes,
    _section_content_sha256,
    load_planning_regulation_structure_config,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`.

**Complete source-ordered implementation**

```python
def _section_content_sha256(row: Mapping[str, object]) -> str:
    content = {column: row[column] for column in SECTION_COLUMNS if column != "section_content_sha256"}
    return _canonical_sha256(
        {
            "domain": "landscout.planning_regulation.section",
            "section_hash_schema_version": SECTION_HASH_SCHEMA_VERSION,
            "section": content,
        }
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_build_sections`

**Exact signature**

```python
def _build_sections(
    index: PlanningRegulationIndex,
    config: PlanningRegulationStructureConfig,
) -> tuple[pd.DataFrame, tuple[_SectionBuild, ...], tuple[_LineRecord, ...]]:
```

**Purpose**

Constructs sections; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[pd.DataFrame, tuple[_SectionBuild, ...], tuple[_LineRecord, ...]]`.
- Every observed return expression is reproduced without truncation:
```python
(frame, tuple(builds), tuple(records))
```

**Validation and exceptions**

- Guard with a raise path: `section_type == 'ARTICLE'`.
- Guard with a raise path: `current_chapter_id is None or current_chapter_label is None`.
- Guard with a raise path: `event.zone_chapter_label is None or event.zone_chapter_label.casefold() != current_chapter_label.casefold()`.
- Explicit raise expressions: `PlanningRegulationStructureError('Zone article has no preceding zone chapter')`, `PlanningRegulationStructureError('Zone article label differs from its active chapter')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_section_content_sha256`, `_source_records_sha256`.
- Environment/process effects: none directly visible.
- In-memory mutation: `frame['character_count']`, `frame['end_page']`, `frame['source_record_count']`, `frame['start_page']`, `row['section_content_sha256']`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_build_structure_result` via `_build_sections`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_source_label_values`

**Exact signature**

```python
def _validate_source_label_values(series: pd.Series, label: str) -> None:
```

**Purpose**

Rejects malformed or inconsistent source label values; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validated_zoning_inputs` via `_validate_source_label_values`.

**Complete source-ordered implementation**

```python
def _validate_source_label_values(series: pd.Series, label: str) -> None:
    for value in series.tolist():
        _strict_string(value, label)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validated_zoning_inputs`

**Exact signature**

```python
def _validated_zoning_inputs(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
    intersections: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
```

**Purpose**

Checks and returns canonical zoning inputs; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[pd.DataFrame, pd.DataFrame]`.
- Every observed return expression is reproduced without truncation:
```python
(zone_copy, relation_copy)
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(zones, pd.DataFrame) or not isinstance(intersections, pd.DataFrame)`.
- Guard with a raise path: `missing_zones`.
- Guard with a raise path: `missing_relations`.
- Guard with a raise path: `zone_copy['planning_zone_id'].duplicated().any()`.
- Guard with a raise path: `zone_copy['source_zone_id'].duplicated().any()`.
- Guard with a raise path: `not zone_copy['source_document_id'].eq(index.document_id).all()`.
- Guard with a raise path: `not zone_copy['source_archive_sha256'].eq(index.archive_sha256).all()`.
- Guard with a raise path: `relation_copy.duplicated(['parcel_id', 'planning_zone_id']).any()`.
- Guard with a raise path: `not set(relation_copy['planning_zone_id'].tolist()).issubset(known)`.
- Guard with a raise path: `not expected_labels.eq(relation_copy['zone_label_raw']).all()`.
- Guard with a raise path: `not expected_source_ids.eq(relation_copy['source_zone_id']).all()`.
- Guard with a raise path: `not relation_copy['source_document_id'].eq(index.document_id).all()`.
- Guard with a raise path: `not relation_copy['source_archive_sha256'].eq(index.archive_sha256).all()`.
- Guard with a raise path: `not set(relation_copy['relation_type'].tolist()).issubset(allowed_relations)`.
- Guard with a raise path: `not relation_copy.loc[positive, 'relation_type'].eq('AREA_OVERLAP').all()`.
- Guard with a raise path: `not relation_copy.loc[~positive, 'relation_type'].eq('TOUCH_ONLY').all()`.
- Guard with a raise path: `isinstance(value, bool) or not isinstance(value, Real)`.
- Guard with a raise path: `not math.isfinite(numeric) or numeric < 0`.
- Guard with a raise path: `isinstance(upper, bool) or not isinstance(upper, Real)`.
- Guard with a raise path: `not math.isfinite(numeric_upper) or numeric_upper < 0`.
- Guard with a raise path: `area - numeric_upper > technical_overlay_tolerance(numeric_upper)`.
- Explicit raise expressions: `PlanningRegulationStructureError('Intersection archive lineage differs from index')`, `PlanningRegulationStructureError('Intersection areas must be finite and non-negative')`, `PlanningRegulationStructureError('Intersection areas must be finite')`, `PlanningRegulationStructureError('Intersection areas must be numeric')`, `PlanningRegulationStructureError('Intersection document lineage differs from index')`, `PlanningRegulationStructureError('Intersection source-zone IDs differ from the zone catalog')`, `PlanningRegulationStructureError('Intersection zone labels differ from the zone catalog')`, `PlanningRegulationStructureError('Parcel/zone intersection pairs must be unique')`, `PlanningRegulationStructureError('Planning zone IDs must be unique')`, `PlanningRegulationStructureError('Positive zoning relations must be AREA_OVERLAP')`, `PlanningRegulationStructureError('Source zone IDs must be unique')`, `PlanningRegulationStructureError('Zero-area zoning relations must be TOUCH_ONLY')`, `PlanningRegulationStructureError('Zone archive lineage differs from index')`, `PlanningRegulationStructureError('Zone document lineage differs from index')`, `PlanningRegulationStructureError('Zones and zoning intersections must be DataFrames')`, `PlanningRegulationStructureError('Zoning intersections reference an unknown planning zone')`, `PlanningRegulationStructureError('Zoning relation type is invalid')`, `PlanningRegulationStructureError(f'Intersection area exceeds {upper_column}')`, `PlanningRegulationStructureError(f'Zone catalog is missing required columns: {missing_zones}')`, `PlanningRegulationStructureError(f'Zoning intersections are missing required columns: {missing_relations}')`, `PlanningRegulationStructureError(f'{upper_column} must be finite and non-negative')`, `PlanningRegulationStructureError(f'{upper_column} must be finite')`, `PlanningRegulationStructureError(f'{upper_column} must be numeric')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `intersections.copy`, `relation_copy.loc[positive, 'relation_type'].eq('AREA_OVERLAP').all`, `relation_copy['intersection_area_m2'].gt`, `relation_copy['intersection_area_m2'].tolist`.
- Hashing: `relation_copy['source_archive_sha256'].eq`, `relation_copy['source_archive_sha256'].eq(index.archive_sha256).all`, `zone_copy['source_archive_sha256'].eq`, `zone_copy['source_archive_sha256'].eq(index.archive_sha256).all`.
- Environment/process effects: none directly visible.
- In-memory mutation: `relation_copy['intersection_area_m2']`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::validate_planning_regulation_structure_with_fragments` via `_validated_zoning_inputs`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::structure_planning_regulation` via `_validated_zoning_inputs`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_input_frame_sha256`

**Exact signature**

```python
def _input_frame_sha256(
    domain: str,
    frame: pd.DataFrame,
    columns: Sequence[str],
) -> str:
```

**Purpose**

Private `planning` helper for input frame sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_sha256({'domain': domain, 'columns': list(columns), 'rows': frame.loc[:, columns].to_dict('records')})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_canonical_sha256`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_build_structure_result` via `_input_frame_sha256`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_result_self` via `_input_frame_sha256`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_intersection_hash_columns`

**Exact signature**

```python
def _intersection_hash_columns(frame: pd.DataFrame) -> tuple[str, ...]:
```

**Purpose**

Private `planning` helper for intersection hash columns; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[str, ...]`.
- Every observed return expression is reproduced without truncation:
```python
_REQUIRED_INTERSECTION_INPUT_COLUMNS + tuple((column for column in _OPTIONAL_INTERSECTION_INPUT_COLUMNS if column in frame.columns))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_build_structure_result` via `_intersection_hash_columns`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_result_self` via `_intersection_hash_columns`.

**Complete source-ordered implementation**

```python
def _intersection_hash_columns(frame: pd.DataFrame) -> tuple[str, ...]:
    return _REQUIRED_INTERSECTION_INPUT_COLUMNS + tuple(
        column
        for column in _OPTIONAL_INTERSECTION_INPUT_COLUMNS
        if column in frame.columns
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_resolved_alias`

**Exact signature**

```python
def _resolved_alias(label: str, aliases: Mapping[str, str]) -> str | None:
```

**Purpose**

Private `planning` helper for resolved alias; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str | None`.
- Every observed return expression is reproduced without truncation:
```python
current

None
```

**Validation and exceptions**

- Guard with a raise path: `current in visited`.
- Explicit raise expressions: `PlanningRegulationStructureError('Zone alias cycle is invalid')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_build_zone_mapping` via `_resolved_alias`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_zone_mapping` via `_resolved_alias`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_dominant_counts`

**Exact signature**

```python
def _dominant_counts(intersections: pd.DataFrame) -> Counter[str]:
```

**Purpose**

Private `planning` helper for dominant counts; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Counter[str]`.
- Every observed return expression is reproduced without truncation:
```python
Counter(selected['zone_label_raw'].tolist())

Counter()
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `intersections.loc[intersections['intersection_area_m2'].gt(0), ['parcel_id', 'planning_zone_id', 'zone_label_raw', 'intersection_area_m2']].copy`, `intersections['intersection_area_m2'].gt`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_build_zone_mapping` via `_dominant_counts`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_build_zone_mapping`

**Exact signature**

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

Constructs zone mapping; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
frame
```

**Validation and exceptions**

- Guard with a raise path: `unresolved_dominant`.
- Explicit raise expressions: `PlanningRegulationStructureError(f'Dominant candidate zone labels lack an exact configured chapter mapping: {unresolved_dominant}')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `intersections.groupby`, `intersections.groupby('zone_label_raw', sort=False)['parcel_id'].nunique`, `intersections.groupby('zone_label_raw', sort=False)['parcel_id'].nunique().to_dict`, `intersections['zone_label_raw'].tolist`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `frame[column]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_build_structure_result` via `_build_zone_mapping`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_is_token_character`

**Exact signature**

```python
def _is_token_character(value: str) -> bool:
```

**Purpose**

Tests whether token character; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
value.isalnum() or value == '_'
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_literal_topic_matches` via `_is_token_character`.

**Complete source-ordered implementation**

```python
def _is_token_character(value: str) -> bool:
    return value.isalnum() or value == "_"
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_literal_topic_matches`

**Exact signature**

```python
def _literal_topic_matches(
    normalized_text: str,
    terms: Sequence[str],
) -> tuple[_TopicMatch, ...]:
```

**Purpose**

Private `planning` helper for literal topic matches; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[_TopicMatch, ...]`.
- Every observed return expression is reproduced without truncation:
```python
tuple(sorted(selected, key=lambda item: (item.normalized_start, item.term_index)))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_build_topic_evidence` via `_literal_topic_matches`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_topic_evidence` via `_literal_topic_matches`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_equal_length_overlap_uses_configured_term_order_as_tie_break` via `_literal_topic_matches`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_token_boundary_and_longest_match_policy` via `_literal_topic_matches`.
- import/re-export: `tests/unit/test_structure_planning_regulation.py::<module>` via `from landscout.stages.structure_planning_regulation import (
    SECTION_HASH_SCHEMA_VERSION,
    STRUCTURE_MANIFEST_SCHEMA_VERSION,
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    _heading_events,
    _line_records,
    _literal_topic_matches,
    _result_with_hashes,
    _section_content_sha256,
    load_planning_regulation_structure_config,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_evidence_scope`

**Exact signature**

```python
def _evidence_scope(section_type: str) -> str:
```

**Purpose**

Private `planning` helper for evidence scope; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
'GENERAL_RULE'

'ZONE_SPECIFIC_RULE'

'OTHER_TEXT'
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `PlanningRegulationStructureError('Topic evidence references an unsupported section type')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_build_topic_evidence` via `_evidence_scope`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_topic_evidence` via `_evidence_scope`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_build_topic_evidence`

**Exact signature**

```python
def _build_topic_evidence(
    index: PlanningRegulationIndex,
    config: PlanningRegulationStructureConfig,
    builds: Sequence[_SectionBuild],
) -> pd.DataFrame:
```

**Purpose**

Constructs topic evidence; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
frame

pd.DataFrame({column: pd.Series(dtype='int64' if column in {'page_number', 'occurrence_count', 'first_match_normalized_start', 'first_match_normalized_end', 'first_match_raw_start', 'first_match_raw_end'} else 'object') for column in TOPIC_EVIDENCE_COLUMNS})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `frame[column]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_build_structure_result` via `_build_topic_evidence`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_frame_hash`

**Exact signature**

```python
def _frame_hash(
    domain: str,
    result: PlanningRegulationStructureResult,
    frame: pd.DataFrame,
    columns: Sequence[str],
) -> str:
```

**Purpose**

Private `planning` helper for frame hash; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_sha256({'domain': domain, 'section_hash_schema_version': result.section_hash_schema_version, 'document_id': result.document_id, 'archive_sha256': result.archive_sha256, 'pdf_sha256': result.pdf_sha256, 'index_content_sha256': result.index_content_sha256, 'structure_profile': result.structure_profile, 'structure_config_schema_version': result.structure_config_schema_version, 'structure_config_sha256': result.structure_config_sha256, 'zones_content_sha256': result.zones_content_sha256, 'zoning_intersection_hash_columns': list(result.zoning_intersection_hash_columns), 'zoning_intersections_content_sha256': result.zoning_intersections_content_sha256, 'source_records_sha256': result.source_records_sha256, 'rows': frame.loc[:, columns].to_dict('records')})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_canonical_sha256`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_result_with_hashes` via `_frame_hash`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_structure_result_content_sha256`

**Exact signature**

```python
def _structure_result_content_sha256(
    result: PlanningRegulationStructureResult,
) -> str:
```

**Purpose**

Private `planning` helper for structure result content sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_sha256({'domain': 'landscout.planning_regulation.structure_result', 'document_id': result.document_id, 'archive_sha256': result.archive_sha256, 'pdf_sha256': result.pdf_sha256, 'index_content_sha256': result.index_content_sha256, 'structure_profile': result.structure_profile, 'structure_config_schema_version': result.structure_config_schema_version, 'structure_config_sha256': result.structure_config_sha256, 'zones_content_sha256': result.zones_content_sha256, 'zoning_intersection_hash_columns': list(result.zoning_intersection_hash_columns), 'zoning_intersections_content_sha256': result.zoning_intersections_content_sha256, 'source_records_sha256': result.source_records_sha256, 'section_hash_schema_version': result.section_hash_schema_version, 'sections_content_sha256': result.sections_content_sha256, 'zone_map_content_sha256': result.zone_map_content_sha256, 'topic_evidence_content_sha256': result.topic_evidence_content_sha256})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_canonical_sha256`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_result_with_hashes` via `_structure_result_content_sha256`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_result_with_hashes`

**Exact signature**

```python
def _result_with_hashes(
    result: PlanningRegulationStructureResult,
) -> PlanningRegulationStructureResult:
```

**Purpose**

Private `planning` helper for result with hashes; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `PlanningRegulationStructureResult`.
- Every observed return expression is reproduced without truncation:
```python
replace(component_result, structure_result_content_sha256=_structure_result_content_sha256(component_result))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_frame_hash`, `_structure_result_content_sha256`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_build_result` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_result_envelope` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_build_result` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_result_envelope` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_build_result` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_validate_result_envelope` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_build_result` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_build_result` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_result_envelope` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_build_structure_result` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_result_self` via `_result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_build_from_relations` via `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_build_from_relations` via `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_rehash_coordinated_result` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_rehash_coordinated_result` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_local_corruption_fast_fails_before_heavy_validation` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_local_corruption_fast_fails_before_heavy_validation` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_coordinated_local_cross_table_corruption_is_rejected` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_coordinated_local_cross_table_corruption_is_rejected` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_output_dtype_and_non_2d_parcel_fail_locally` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_output_dtype_and_non_2d_parcel_fail_locally` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_selected_relation_role_requires_selected_status_and_priority` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_selected_relation_role_requires_selected_status_and_priority` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_only_application_result_schema_two_is_accepted` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_only_application_result_schema_two_is_accepted` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_authorized_status_artifact_fails_local_verified_byte_loading` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_authorized_status_artifact_fails_local_verified_byte_loading` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_no_relation_parcel_rejects_textual_null_identity` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_no_relation_parcel_rejects_textual_null_identity` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_decision_status_domain_rejects_forbidden_vocabulary` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_decision_status_domain_rejects_forbidden_vocabulary` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_persisted_feature_id_json_must_be_portable_and_canonical` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_persisted_feature_id_json_must_be_portable_and_canonical` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_changed_parcel_geometry_upstreams` via `application_module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_changed_parcel_geometry_upstreams` via `application_module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::_coordinated_policy_mutation` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::_coordinated_policy_mutation` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::_coordinated_feature_id_mutation` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::_coordinated_feature_id_mutation` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::_surface_touch_with_positive_area` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::_surface_touch_with_positive_area` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_schema_v1_dimension_blind_hash_representation_is_rejected_locally` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_schema_v1_dimension_blind_hash_representation_is_rejected_locally` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_complete_relation_facts_must_match_referenced_feature` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_complete_relation_facts_must_match_referenced_feature` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_feature_or_relation_policy_mutation_is_rejected` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_feature_or_relation_policy_mutation_is_rejected` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_application_relation_pair_is_rejected_locally` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_application_relation_pair_is_rejected_locally` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_parcel_id_is_exact` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_parcel_id_is_exact` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_application_relation_type_is_rejected_locally` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_application_relation_type_is_rejected_locally` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_official_and_application_statuses_cannot_contradict` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_official_and_application_statuses_cannot_contradict` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_application_source_lock_mutation_fast_fails` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_application_source_lock_mutation_fast_fails` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_pair_artifact_fails_local_loading` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_pair_artifact_fails_local_loading` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_wrong_2d_feature_geometry_fails_local_artifact_loading` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_wrong_2d_feature_geometry_fails_local_artifact_loading` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_geometry_role_is_intrinsic` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_geometry_role_is_intrinsic` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_metric_must_match_geometry` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_metric_must_match_geometry` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_catalog_identity_fields_are_intrinsic` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_catalog_identity_fields_are_intrinsic` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_requires_canonical_crs_and_global_identity` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_requires_canonical_crs_and_global_identity` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_identity_is_validated_locally` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_identity_is_validated_locally` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_participates_in_global_policy_mapping` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_participates_in_global_policy_mapping` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_locks_policy_result_schema_exactly` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_locks_policy_result_schema_exactly` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_locks_cnig_result_schema_exactly` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_locks_cnig_result_schema_exactly` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_identity_fast_fails_before_policy_source_validation` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_identity_fast_fails_before_policy_source_validation` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::_replace_application_frame` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::_replace_application_frame` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::_coordinated_referenced_lineage_mutation` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::_coordinated_referenced_lineage_mutation` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_row_lineage_must_match_application_envelope` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_row_lineage_must_match_application_envelope` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::_swap_referenced_feature_values` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::_swap_referenced_feature_values` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_factual_prefix_lineage_change` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_factual_prefix_lineage_change` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `coding_module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `coding_module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `policy_module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `policy_module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::_compatible_policy_mutation` via `module._result_with_hashes`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_page_tuple`

**Exact signature**

```python
def _page_tuple(value: object) -> tuple[int, ...]:
```

**Purpose**

Private `planning` helper for page tuple; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[int, ...]`.
- Every observed return expression is reproduced without truncation:
```python
tuple((_strict_positive_integer(item, 'section page number') for item in value))
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(value, (tuple, list, np.ndarray))`.
- Explicit raise expressions: `PlanningRegulationStructureError('Section page_numbers must be a sequence')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_sections` via `_page_tuple`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_topic_evidence` via `_page_tuple`.

**Complete source-ordered implementation**

```python
def _page_tuple(value: object) -> tuple[int, ...]:
    if not isinstance(value, (tuple, list, np.ndarray)):
        raise PlanningRegulationStructureError("Section page_numbers must be a sequence")
    return tuple(_strict_positive_integer(item, "section page number") for item in value)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_sections`

**Exact signature**

```python
def _validate_sections(
    index: PlanningRegulationIndex,
    result: PlanningRegulationStructureResult,
    records: Sequence[_LineRecord],
    config: PlanningRegulationStructureConfig,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent sections; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `not isinstance(frame, pd.DataFrame) or tuple(frame.columns) != SECTION_COLUMNS`.
- Guard with a raise path: `frame.empty`.
- Guard with a raise path: `result.source_records_sha256 != _source_records_sha256(records)`.
- Guard with a raise path: `expected_record_start != len(records)`.
- Guard with a raise path: `len(set(ids)) != len(ids)`.
- Guard with a raise path: `section_id != f'SECTION-{sequence:04d}'`.
- Guard with a raise path: `section_type not in _SECTION_TYPES`.
- Guard with a raise path: `row['heading_normalized'] != _normalize_search_text(row['heading_raw'])`.
- Guard with a raise path: `row['normalized_text'] != _normalize_search_text(row['raw_text'])`.
- Guard with a raise path: `_strict_nonnegative_integer(row['character_count'], 'character count') != len(row['raw_text'])`.
- Guard with a raise path: `start_record_id not in record_position or end_record_id not in record_position`.
- Guard with a raise path: `start_record != expected_record_start or end_record < start_record`.
- Guard with a raise path: `not row['raw_text'].strip() and (not blank_toc_other)`.
- Guard with a raise path: `not row['heading_raw'].strip() and (not blank_toc_other)`.
- Guard with a raise path: `_strict_positive_integer(row['source_record_count'], 'source record count') != len(segment)`.
- Guard with a raise path: `_validated_sha256(row['source_records_sha256'], 'section source-record SHA256') != _source_records_sha256(segment)`.
- Guard with a raise path: `row['raw_text'] != '\n'.join((record.raw for record in segment))`.
- Guard with a raise path: `not pages or any((right <= left for left, right in pairwise(pages))) or (not set(pages).issubset(known_pages)) or (pages != expected_pages)`.
- Guard with a raise path: `start != pages[0] or end != pages[-1] or end < start`.
- Guard with a raise path: `_validated_sha256(row['section_content_sha256'], 'section content SHA256') != expected_hash`.
- Guard with a raise path: `section_type == 'ARTICLE'`.
- Guard with a raise path: `parent not in type_by_id or type_by_id[parent] != 'ZONE_CHAPTER'`.
- Guard with a raise path: `section_type != 'ARTICLE'`.
- Guard with a raise path: `order_by_id[parent] >= order_by_id[section_id]`.
- Guard with a raise path: `zone_by_id[parent] != zone_by_id[section_id]`.
- Guard with a raise path: `not isinstance(row[column], str)`.
- Guard with a raise path: `row[column] != actual`.
- Guard with a raise path: `zone_label is None`.
- Guard with a raise path: `section_id not in parents`.
- Guard with a raise path: `section_type == 'GENERAL'`.
- Guard with a raise path: `zone_label is not None or section_id in parents`.
- Guard with a raise path: `section_id in parents`.
- Guard with a raise path: `section_type == 'ZONE_CHAPTER'`.
- Guard with a raise path: `zone_label is None`.
- Guard with a raise path: `zone_label is not None`.
- Guard with a raise path: `value is not None and (not bool(pd.isna(value)))`.
- Explicit raise expressions: `PlanningRegulationStructureError('Article parent is missing')`, `PlanningRegulationStructureError('Article parent must occur earlier in source order')`, `PlanningRegulationStructureError('Article parent section is invalid')`, `PlanningRegulationStructureError('Article zone label differs from its parent chapter')`, `PlanningRegulationStructureError('Article zone label is missing')`, `PlanningRegulationStructureError('Every nonblank section must retain a factual heading')`, `PlanningRegulationStructureError('General section cannot have a zone label or parent')`, `PlanningRegulationStructureError('OTHER section cannot have a zone label')`, `PlanningRegulationStructureError('Only an explicit TOC OTHER section may contain blank-only text')`, `PlanningRegulationStructureError('Only articles may have a parent section')`, `PlanningRegulationStructureError('Regulation sections must not be empty')`, `PlanningRegulationStructureError('Retained source records are omitted from the section partition')`, `PlanningRegulationStructureError('Retained source-record hash differs')`, `PlanningRegulationStructureError('Section IDs must be deterministic and sequential')`, `PlanningRegulationStructureError('Section IDs must be unique')`, `PlanningRegulationStructureError('Section character count differs')`, `PlanningRegulationStructureError('Section content hash differs')`, `PlanningRegulationStructureError('Section heading normalization differs')`, `PlanningRegulationStructureError('Section lineage differs')`, `PlanningRegulationStructureError('Section page range is invalid or unordered')`, `PlanningRegulationStructureError('Section page references are invalid')`, `PlanningRegulationStructureError('Section raw text differs from its retained source records')`, `PlanningRegulationStructureError('Section record boundary is unknown')`, `PlanningRegulationStructureError('Section schema is not deterministic')`, `PlanningRegulationStructureError('Section source-record count differs')`, `PlanningRegulationStructureError('Section source-record hash differs')`, `PlanningRegulationStructureError('Section text normalization differs')`, `PlanningRegulationStructureError('Section type is invalid')`, `PlanningRegulationStructureError('Sections do not preserve the exact source-record partition')`, `PlanningRegulationStructureError('Zone chapter label is missing')`, `PlanningRegulationStructureError('Zone chapter or OTHER section cannot have a parent')`, `PlanningRegulationStructureError(f'Section {column} must be a string')`, `PlanningRegulationStructureError(f'{section_type} {label} must be null')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_section_content_sha256`, `_source_records_sha256`, `_validated_sha256`.
- Environment/process effects: none directly visible.
- In-memory mutation: `parents[section_id]`, `zone_by_id[section_id]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_result_self` via `_validate_sections`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_zone_mapping`

**Exact signature**

```python
def _validate_zone_mapping(
    result: PlanningRegulationStructureResult,
    config: PlanningRegulationStructureConfig,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent zone mapping; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `not isinstance(frame, pd.DataFrame) or tuple(frame.columns) != ZONE_MAPPING_COLUMNS`.
- Guard with a raise path: `labels != sorted(labels) or len(set(labels)) != len(labels)`.
- Guard with a raise path: `status not in _MAPPING_STATUSES or method not in _MAPPING_METHODS`.
- Guard with a raise path: `exact_methods[status] != method`.
- Guard with a raise path: `status in {'EXACT', 'CONFIG_ALIAS'}`.
- Guard with a raise path: `row['dominant_candidate_count'] > 0 and status not in {'EXACT', 'CONFIG_ALIAS'}`.
- Guard with a raise path: `not counts['dominant_candidate_count'] <= counts['candidate_parcel_count'] <= counts['candidate_intersection_count']`.
- Guard with a raise path: `column == 'zone_polygon_count' and count == 0`.
- Guard with a raise path: `matched_id not in sections.index`.
- Guard with a raise path: `matched_section['section_type'] != 'ZONE_CHAPTER'`.
- Guard with a raise path: `matched_section['zone_chapter_label'] != resolved`.
- Guard with a raise path: `status == 'EXACT' and resolved != label`.
- Guard with a raise path: `status == 'CONFIG_ALIAS' and resolved != _resolved_alias(label, config.zone_aliases)`.
- Guard with a raise path: `matched is not None and (not bool(pd.isna(matched)))`.
- Guard with a raise path: `row[column] != actual`.
- Guard with a raise path: `status == 'UNMAPPED' and row['resolved_zone_chapter_label'] is not None and (not bool(pd.isna(row['resolved_zone_chapter_label'])))`.
- Explicit raise expressions: `PlanningRegulationStructureError('Configured zone mapping differs from its final alias target')`, `PlanningRegulationStructureError('Dominant candidate zone is unresolved')`, `PlanningRegulationStructureError('Exact zone mapping must preserve the source label')`, `PlanningRegulationStructureError('Resolved zone label differs from its matched chapter')`, `PlanningRegulationStructureError('Resolved zone mapping must reference a zone chapter')`, `PlanningRegulationStructureError('Unmapped zone must not claim a resolved chapter label')`, `PlanningRegulationStructureError('Unresolved zone mapping has a section ID')`, `PlanningRegulationStructureError('Zone candidate coverage counts are mathematically inconsistent')`, `PlanningRegulationStructureError('Zone mapping lineage differs')`, `PlanningRegulationStructureError('Zone mapping schema is not deterministic')`, `PlanningRegulationStructureError('Zone mapping section is unknown')`, `PlanningRegulationStructureError('Zone mapping status or method is invalid')`, `PlanningRegulationStructureError('Zone mapping status/method combination is invalid')`, `PlanningRegulationStructureError('Zone mappings must be unique and sorted')`, `PlanningRegulationStructureError('Zone polygon count must be positive')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `counts[column]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_result_self` via `_validate_zone_mapping`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_topic_evidence`

**Exact signature**

```python
def _validate_topic_evidence(
    index: PlanningRegulationIndex,
    result: PlanningRegulationStructureResult,
    config: PlanningRegulationStructureConfig,
    builds: Sequence[_SectionBuild],
) -> None:
```

**Purpose**

Rejects malformed or inconsistent topic evidence; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `not isinstance(frame, pd.DataFrame) or tuple(frame.columns) != TOPIC_EVIDENCE_COLUMNS`.
- Guard with a raise path: `topic not in config.topics`.
- Guard with a raise path: `term not in config.topics[topic]`.
- Guard with a raise path: `normalized != _normalize_search_text(term)`.
- Guard with a raise path: `section_id not in sections.index`.
- Guard with a raise path: `page not in page_set or page not in _page_tuple(sections.at[section_id, 'page_numbers'])`.
- Guard with a raise path: `(section_id, page) not in fragments`.
- Guard with a raise path: `count < 1`.
- Guard with a raise path: `not isinstance(row['raw_context'], str) or not isinstance(row['normalized_context'], str)`.
- Guard with a raise path: `scope not in _EVIDENCE_SCOPES`.
- Guard with a raise path: `scope != expected_scope`.
- Guard with a raise path: `row['match_policy'] != config.topic_match_policy.identifier`.
- Guard with a raise path: `not retained_matches`.
- Guard with a raise path: `count != len(retained_matches)`.
- Guard with a raise path: `row['raw_context'] != expected_raw_context or row['normalized_context'] != expected_normalized_context or row['raw_context'] not in raw_fragment`.
- Guard with a raise path: `key in keys`.
- Guard with a raise path: `actual != expected`.
- Guard with a raise path: `_strict_nonnegative_integer(row[column], column) != expected`.
- Guard with a raise path: `row[column] != actual`.
- Explicit raise expressions: `PlanningRegulationStructureError('Evidence scope is invalid')`, `PlanningRegulationStructureError('Topic context differs from retained source text')`, `PlanningRegulationStructureError('Topic contexts must be strings')`, `PlanningRegulationStructureError('Topic evidence has no retained source-text match')`, `PlanningRegulationStructureError('Topic evidence lineage differs')`, `PlanningRegulationStructureError('Topic evidence page is absent from its retained section text')`, `PlanningRegulationStructureError('Topic evidence references an unknown page')`, `PlanningRegulationStructureError('Topic evidence references an unknown section')`, `PlanningRegulationStructureError('Topic evidence row is duplicated')`, `PlanningRegulationStructureError('Topic evidence schema is not deterministic')`, `PlanningRegulationStructureError('Topic evidence scope differs from its section location')`, `PlanningRegulationStructureError('Topic evidence search term is unconfigured')`, `PlanningRegulationStructureError('Topic evidence topic is unconfigured')`, `PlanningRegulationStructureError('Topic match policy differs')`, `PlanningRegulationStructureError('Topic match provenance differs from source text')`, `PlanningRegulationStructureError('Topic occurrence count differs from retained source spans')`, `PlanningRegulationStructureError('Topic occurrence count is invalid')`, `PlanningRegulationStructureError('Topic search normalization differs')`, `PlanningRegulationStructureError(f'Topic evidence {column} differs from its section')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_result_self` via `_validate_topic_evidence`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_build_structure_result`

**Exact signature**

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

Constructs structure result; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[PlanningRegulationStructureResult, tuple[_SectionBuild, ...], tuple[_LineRecord, ...]]`.
- Every observed return expression is reproduced without truncation:
```python
(_result_with_hashes(result), builds, records)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `_intersection_hash_columns`.
- Hashing: `_config_sha256`, `_input_frame_sha256`, `_intersection_hash_columns`, `_result_with_hashes`, `_source_records_sha256`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::validate_planning_regulation_structure_with_fragments` via `_build_structure_result`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::structure_planning_regulation` via `_build_structure_result`.

**Complete source-ordered implementation**

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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_result_self`

**Exact signature**

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

Rejects malformed or inconsistent result self; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `not isinstance(result, PlanningRegulationStructureResult)`.
- Guard with a raise path: `result.document_id != index.document_id or result.archive_sha256 != index.archive_sha256 or result.pdf_sha256 != index.pdf_sha256 or (result.index_content_sha256 != index.index_content_sha256)`.
- Guard with a raise path: `config_schema != config.schema_version`.
- Guard with a raise path: `result.structure_config_sha256 != _config_sha256(config)`.
- Guard with a raise path: `result.zones_content_sha256 != expected_zones_hash`.
- Guard with a raise path: `type(result.zoning_intersection_hash_columns) is not tuple or not all((isinstance(column, str) for column in result.zoning_intersection_hash_columns)) or result.zoning_intersection_hash_columns != expected_intersection_columns`.
- Guard with a raise path: `result.zoning_intersections_content_sha256 != expected_intersections_hash`.
- Guard with a raise path: `schema != SECTION_HASH_SCHEMA_VERSION`.
- Guard with a raise path: `_validated_sha256(result.structure_result_content_sha256, 'structure result content SHA256') != expected.structure_result_content_sha256`.
- Guard with a raise path: `_validated_sha256(actual, f'{label} content SHA256') != wanted`.
- Explicit raise expressions: `PlanningRegulationStructureError('Complete structure result hash differs')`, `PlanningRegulationStructureError('Intersection hash columns differ from the factual input schema')`, `PlanningRegulationStructureError('Intersection input hash differs')`, `PlanningRegulationStructureError('Structure config hash differs')`, `PlanningRegulationStructureError('Structure config schema version differs')`, `PlanningRegulationStructureError('Structure result lineage differs from index')`, `PlanningRegulationStructureError('Unsupported section hash schema version')`, `PlanningRegulationStructureError('Zone input hash differs')`, `PlanningRegulationStructureError('result must be a PlanningRegulationStructureResult')`, `PlanningRegulationStructureError(f'{label} content hash differs')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `_intersection_hash_columns`.
- Hashing: `_config_sha256`, `_input_frame_sha256`, `_intersection_hash_columns`, `_result_with_hashes`, `_validated_sha256`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::validate_planning_regulation_structure_with_fragments` via `_validate_result_self`.

**Complete source-ordered implementation**

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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_resolved_config`

**Exact signature**

```python
def _resolved_config(
    config: PlanningRegulationStructureConfig | str | Path,
) -> PlanningRegulationStructureConfig:
```

**Purpose**

Private `planning` helper for resolved config; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `PlanningRegulationStructureConfig`.
- Every observed return expression is reproduced without truncation:
```python
load_planning_regulation_structure_config(config)

PlanningRegulationStructureConfig.model_validate(config.model_dump(mode='python'))
```

**Validation and exceptions**

- Guard with a raise path: `isinstance(config, PlanningRegulationStructureConfig)`.
- Explicit raise expressions: `PlanningRegulationStructureError('Planning structure configuration is invalid')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::validate_planning_regulation_structure_with_fragments` via `_resolved_config`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::structure_planning_regulation` via `_resolved_config`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_frame_rows`

**Exact signature**

```python
def _canonical_frame_rows(frame: pd.DataFrame, columns: Sequence[str]) -> object:
```

**Purpose**

Private `planning` helper for canonical frame rows; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `object`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_value(frame.loc[:, columns].to_dict('records'))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_compare_expected_result` via `_canonical_frame_rows`.

**Complete source-ordered implementation**

```python
def _canonical_frame_rows(frame: pd.DataFrame, columns: Sequence[str]) -> object:
    return _canonical_value(frame.loc[:, columns].to_dict("records"))
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_compare_expected_result`

**Exact signature**

```python
def _compare_expected_result(
    result: PlanningRegulationStructureResult,
    expected: PlanningRegulationStructureResult,
) -> None:
```

**Purpose**

Private `planning` helper for compare expected result; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `getattr(result, field) != getattr(expected, field)`.
- Guard with a raise path: `tuple(actual_frame.columns) != tuple(columns)`.
- Guard with a raise path: `_canonical_frame_rows(actual_frame, columns) != _canonical_frame_rows(expected_frame, columns)`.
- Explicit raise expressions: `PlanningRegulationStructureError(f'Structure result {field} differs from rebuilt source evidence')`, `PlanningRegulationStructureError(f'{name} differs from rebuilt source evidence')`, `PlanningRegulationStructureError(f'{name} schema differs from rebuilt source evidence')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::validate_planning_regulation_structure_with_fragments` via `_compare_expected_result`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_section_page_fragments`

**Exact signature**

```python
def _section_page_fragments(
    result: PlanningRegulationStructureResult,
    builds: Sequence[_SectionBuild],
) -> pd.DataFrame:
```

**Purpose**

Private `planning` helper for section page fragments; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
frame
```

**Validation and exceptions**

- Guard with a raise path: `frame.duplicated(['section_id', 'page_number']).any()`.
- Explicit raise expressions: `PlanningRegulationStructureError('Section/page fragment identity is not unique')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `sha256`, `sha256(raw_text.encode('utf-8')).hexdigest`.
- Environment/process effects: none directly visible.
- In-memory mutation: `frame['page_number']`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::validate_planning_regulation_structure_with_fragments` via `_section_page_fragments`.

**Complete source-ordered implementation**

```python
def _section_page_fragments(
    result: PlanningRegulationStructureResult,
    builds: Sequence[_SectionBuild],
) -> pd.DataFrame:
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_planning_regulation_structure_with_fragments`

**Exact signature**

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

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
_section_page_fragments(result, builds)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `PlanningRegulationStructureError('Planning regulation structure validation failed safely')`, `re-raise`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    load_planning_regulation_structure_config,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_build_result` via `validate_planning_regulation_structure_with_fragments`.
- import/re-export: `src/landscout/stages/interpret_bess_zoning.py::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    validate_planning_regulation_structure_with_fragments,
)`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::validate_planning_regulation_structure` via `validate_planning_regulation_structure_with_fragments`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::planning_regulation_section_page_fragments` via `validate_planning_regulation_structure_with_fragments`.
- property/attribute access: `tests/unit/test_interpret_bess_zoning.py::test_public_source_complete_validator_is_invoked` via `interpret_module.validate_planning_regulation_structure_with_fragments`.
- property/attribute access: `tests/unit/test_interpret_bess_zoning.py::test_one_build_result_performs_one_factual_structure_rebuild` via `interpret_module.validate_planning_regulation_structure_with_fragments`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_can_return_validated_fragments` via `validate_planning_regulation_structure_with_fragments`.
- import/re-export: `tests/unit/test_structure_planning_regulation.py::<module>` via `from landscout.stages.structure_planning_regulation import (
    SECTION_HASH_SCHEMA_VERSION,
    STRUCTURE_MANIFEST_SCHEMA_VERSION,
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    _heading_events,
    _line_records,
    _literal_topic_matches,
    _result_with_hashes,
    _section_content_sha256,
    load_planning_regulation_structure_config,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`.

**Complete source-ordered implementation**

```python
def validate_planning_regulation_structure_with_fragments(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
    zoning_intersections: pd.DataFrame,
    config: PlanningRegulationStructureConfig | str | Path,
    result: PlanningRegulationStructureResult,
) -> pd.DataFrame:
    """Validate the complete structure and return its retained page fragments."""

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
        return _section_page_fragments(result, builds)
    except PlanningRegulationStructureError:
        raise
    except Exception as error:
        raise PlanningRegulationStructureError(
            "Planning regulation structure validation failed safely"
        ) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_planning_regulation_structure`

**Exact signature**

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

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    load_planning_regulation_structure_config,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::structure_planning_regulation` via `validate_planning_regulation_structure`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::_validate` via `validate_planning_regulation_structure`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_document_layout_accepts_real_first_and_last_indexed_pages` via `validate_planning_regulation_structure`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_existing_empty_toc_page_is_valid_not_nonexistent` via `validate_planning_regulation_structure`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_evidence_scope_is_derived_from_exact_section_type` via `validate_planning_regulation_structure`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_blank_only_prefix_is_preserved_in_first_actual_section` via `validate_planning_regulation_structure`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence` via `validate_planning_regulation_structure`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_blank_gap_after_toc_is_preserved_without_a_blank_other_section` via `validate_planning_regulation_structure`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::_structure_with_document_layout` via `validate_planning_regulation_structure`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_rejects_changed_ambiguous_grammar` via `validate_planning_regulation_structure`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_wrong_intersection_source_zone_id_is_rejected` via `validate_planning_regulation_structure`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_intersection_upper_bound_uses_shared_relative_tolerance` via `validate_planning_regulation_structure`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_intersection_hash_columns_are_actual_and_deterministic` via `validate_planning_regulation_structure`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_optional_intersection_metric_change_invalidates_existing_result` via `validate_planning_regulation_structure`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_intersection_hash_column_lineage_mutation_is_rejected` via `validate_planning_regulation_structure`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_rejects_post_build_source_change` via `validate_planning_regulation_structure`.
- import/re-export: `tests/unit/test_structure_planning_regulation.py::<module>` via `from landscout.stages.structure_planning_regulation import (
    SECTION_HASH_SCHEMA_VERSION,
    STRUCTURE_MANIFEST_SCHEMA_VERSION,
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    _heading_events,
    _line_records,
    _literal_topic_matches,
    _result_with_hashes,
    _section_content_sha256,
    load_planning_regulation_structure_config,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`.

**Complete source-ordered implementation**

```python
def validate_planning_regulation_structure(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
    zoning_intersections: pd.DataFrame,
    config: PlanningRegulationStructureConfig | str | Path,
    result: PlanningRegulationStructureResult,
) -> None:
    """Rebuild and validate the complete structure from all factual inputs."""

    validate_planning_regulation_structure_with_fragments(
        index,
        zones,
        zoning_intersections,
        config,
        result,
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `planning_regulation_section_page_fragments`

**Exact signature**

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

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
validate_planning_regulation_structure_with_fragments(index, zones, zoning_intersections, config, result)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `PlanningRegulationStructureError('Planning regulation section/page fragments could not be rebuilt safely')`, `re-raise`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    load_planning_regulation_structure_config,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`.
- direct call or construction: `tests/unit/test_interpret_bess_zoning.py::_policy` via `planning_regulation_section_page_fragments`.
- direct call or construction: `tests/unit/test_interpret_bess_zoning.py::test_same_general_occurrence_may_be_scoped_to_different_chapters` via `planning_regulation_section_page_fragments`.
- direct call or construction: `tests/unit/test_interpret_bess_zoning.py::test_exact_section_page_occurrence_is_auditable` via `planning_regulation_section_page_fragments`.
- direct call or construction: `tests/unit/test_interpret_bess_zoning.py::test_repeated_excerpt_occurrence_is_bound_to_policy` via `planning_regulation_section_page_fragments`.
- import/re-export: `tests/unit/test_interpret_bess_zoning.py::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
)`.

**Complete source-ordered implementation**

```python
def planning_regulation_section_page_fragments(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
    zoning_intersections: pd.DataFrame,
    config: PlanningRegulationStructureConfig | str | Path,
    result: PlanningRegulationStructureResult,
) -> pd.DataFrame:
    """Return validated retained raw text for every section and source page."""

    try:
        return validate_planning_regulation_structure_with_fragments(
            index,
            zones,
            zoning_intersections,
            config,
            result,
        )
    except PlanningRegulationStructureError:
        raise
    except Exception as error:
        raise PlanningRegulationStructureError(
            "Planning regulation section/page fragments could not be rebuilt safely"
        ) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `structure_planning_regulation`

**Exact signature**

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

**Return contract**

- Declared return annotation: `PlanningRegulationStructureResult`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `PlanningRegulationStructureError('Planning regulation structure could not be built safely')`, `re-raise`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    load_planning_regulation_structure_config,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`.
- direct call or construction: `tests/unit/test_interpret_bess_zoning.py::inputs` via `structure_planning_regulation`.
- import/re-export: `tests/unit/test_interpret_bess_zoning.py::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
)`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::valid_result` via `structure_planning_regulation`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_document_layout_rejects_nonexistent_indexed_pages` via `structure_planning_regulation`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_document_lock_mismatch_is_rejected` via `structure_planning_regulation`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_evidence_scope_is_derived_from_exact_section_type` via `structure_planning_regulation`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_reversed_topic_mapping_keys_do_not_change_output_or_hashes` via `structure_planning_regulation`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_equal_length_overlap_uses_configured_term_order_as_tie_break` via `structure_planning_regulation`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_inputs_are_not_mutated` via `structure_planning_regulation`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_dominant_unmapped_zone_stops_processing` via `structure_planning_regulation`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_blank_only_prefix_is_preserved_in_first_actual_section` via `structure_planning_regulation`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence` via `structure_planning_regulation`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_blank_gap_after_toc_is_preserved_without_a_blank_other_section` via `structure_planning_regulation`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::_structure_with_document_layout` via `structure_planning_regulation`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_two_zone_patterns_matching_one_line_are_ambiguous` via `structure_planning_regulation`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_two_article_patterns_matching_one_line_are_ambiguous` via `structure_planning_regulation`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_general_and_article_cross_category_match_is_ambiguous` via `structure_planning_regulation`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_zone_and_general_cross_category_match_is_ambiguous` via `structure_planning_regulation`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_ambiguous_continuation_candidate_fails_with_record_diagnostic` via `structure_planning_regulation`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_normal_muret_compatible_grammar_remains_deterministic` via `structure_planning_regulation`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_intersection_area_cannot_exceed_available_geometry_area` via `structure_planning_regulation`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_intersection_upper_bound_uses_shared_relative_tolerance` via `structure_planning_regulation`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_intersection_hash_columns_are_actual_and_deterministic` via `structure_planning_regulation`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_optional_intersection_metric_change_invalidates_existing_result` via `structure_planning_regulation`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_intersection_hash_column_lineage_mutation_is_rejected` via `structure_planning_regulation`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_alias_chain_resolves_to_final_configured_target` via `structure_planning_regulation`.
- import/re-export: `tests/unit/test_structure_planning_regulation.py::<module>` via `from landscout.stages.structure_planning_regulation import (
    SECTION_HASH_SCHEMA_VERSION,
    STRUCTURE_MANIFEST_SCHEMA_VERSION,
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    _heading_events,
    _line_records,
    _literal_topic_matches,
    _result_with_hashes,
    _section_content_sha256,
    load_planning_regulation_structure_config,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.


## 7. Data contracts

### `_ZONE_INPUT_COLUMNS` — canonical or derived frame-column schema

```python
_ZONE_INPUT_COLUMNS = (
    "planning_zone_id",
    "source_zone_id",
    "zone_label_raw",
    "source_document_id",
    "source_archive_sha256",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `planning_zone_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 2 | `source_zone_id` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 3 | `zone_label_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 4 | `source_document_id` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 5 | `source_archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |

### `_REQUIRED_INTERSECTION_INPUT_COLUMNS` — required input frame fields (unordered when stored as a set)

```python
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
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `parcel_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 2 | `planning_zone_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 3 | `source_zone_id` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 4 | `zone_label_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 5 | `relation_type` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `intersection_area_m2` | float64 when builder initializes NaN/numeric metric; otherwise exact source numeric dtype shown by implementation | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 7 | `source_document_id` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 8 | `source_archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |

### `_OPTIONAL_INTERSECTION_INPUT_COLUMNS` — canonical or derived frame-column schema

```python
_OPTIONAL_INTERSECTION_INPUT_COLUMNS = (
    "parcel_metric_area_m2",
    "zone_area_m2",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `parcel_metric_area_m2` | float64 when builder initializes NaN/numeric metric; otherwise exact source numeric dtype shown by implementation | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 2 | `zone_area_m2` | float64 when builder initializes NaN/numeric metric; otherwise exact source numeric dtype shown by implementation | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |

### `SECTION_COLUMNS` — canonical or derived frame-column schema

```python
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
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `section_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 2 | `parent_section_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 3 | `section_type` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 4 | `heading_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 5 | `heading_normalized` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `zone_chapter_label` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 7 | `article_number_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 8 | `article_title_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 9 | `start_record_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 10 | `end_record_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 11 | `source_record_count` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 12 | `source_records_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 13 | `start_page` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 14 | `end_page` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 15 | `page_numbers` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 16 | `raw_text` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 17 | `normalized_text` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 18 | `character_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 19 | `section_content_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 20 | `document_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 21 | `archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 22 | `pdf_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 23 | `index_content_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 24 | `structure_profile` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |

### `ZONE_MAPPING_COLUMNS` — canonical or derived frame-column schema

```python
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
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `source_zone_label_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 2 | `resolved_zone_chapter_label` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `mapping_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 4 | `mapping_method` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 5 | `matched_section_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 6 | `zone_polygon_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 7 | `candidate_parcel_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 8 | `candidate_intersection_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 9 | `dominant_candidate_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 10 | `document_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 11 | `archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 12 | `pdf_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 13 | `index_content_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 14 | `structure_profile` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |

### `TOPIC_EVIDENCE_COLUMNS` — canonical or derived frame-column schema

```python
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
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `topic` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 2 | `search_term` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `normalized_search_term` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 4 | `match_policy` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 5 | `section_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 6 | `evidence_scope` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 7 | `zone_chapter_label` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `article_number_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 9 | `page_number` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 10 | `occurrence_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 11 | `first_match_normalized_start` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 12 | `first_match_normalized_end` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 13 | `first_match_raw_start` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 14 | `first_match_raw_end` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 15 | `raw_context` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 16 | `normalized_context` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 17 | `document_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 18 | `archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 19 | `pdf_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 20 | `index_content_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 21 | `structure_profile` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |


No enum/status/Literal value is classified as a column unless it is separately present in a canonical schema declaration. Mapping keys, JSON keys, dataclass fields, and configuration leaves remain distinct categories.

## 8. Interfaces

This module defines an exact `__all__` contract:

| Export | Kind | Origin | Included in `__all__` |
|---|---|---|---|
| `PlanningRegulationStructureConfig` | re-exported/defined Python symbol | `defined in `src/landscout/stages/structure_planning_regulation.py`` | yes |
| `PlanningRegulationStructureError` | re-exported/defined Python symbol | `defined in `src/landscout/stages/structure_planning_regulation.py`` | yes |
| `PlanningRegulationStructureResult` | re-exported/defined Python symbol | `defined in `src/landscout/stages/structure_planning_regulation.py`` | yes |
| `load_planning_regulation_structure_config` | re-exported/defined Python symbol | `defined in `src/landscout/stages/structure_planning_regulation.py`` | yes |
| `planning_regulation_section_page_fragments` | re-exported/defined Python symbol | `defined in `src/landscout/stages/structure_planning_regulation.py`` | yes |
| `structure_planning_regulation` | re-exported/defined Python symbol | `defined in `src/landscout/stages/structure_planning_regulation.py`` | yes |
| `validate_planning_regulation_structure` | re-exported/defined Python symbol | `defined in `src/landscout/stages/structure_planning_regulation.py`` | yes |
| `validate_planning_regulation_structure_with_fragments` | re-exported/defined Python symbol | `defined in `src/landscout/stages/structure_planning_regulation.py`` | yes |

## 9. Error handling

Controlled exceptions, local raise guards, delegated validators, and framework assertions are documented per exact function implementation. No broader error guarantee is inferred.

## 10. Side effects

Network I/O, filesystem reads/writes, in-memory mutation, input mutation, geometry/CRS calculations, hashing, and process/environment effects are listed separately for every function.

## 11. Security / trust boundaries

Textual URL/provider/hash fields are provenance claims, not physical proof. Physical proof exists only where the reproduced implementation revalidates transport, bytes, archive structure, source layers, geometry, or result hashes.


## 12. GIS / CRS rules

Only the explicit CRS/geometry validators and calculation copies in this module establish GIS behavior. No geometry repair, reprojection, or metric meaning is inferred from a field name alone.

## 13. Provenance rules

Configured identity, row lineage, byte identity, cache metadata, and source-complete revalidation are separate levels. This companion claims only the levels implemented above.

## 14. Business meaning

The module contributes to the planning flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.

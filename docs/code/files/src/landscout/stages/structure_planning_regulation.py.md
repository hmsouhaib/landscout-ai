# `src/landscout/stages/structure_planning_regulation.py`

## File identity

- Repository path: `src/landscout/stages/structure_planning_regulation.py`
- File type: Python source
- Layer: pipeline stage
- Domain: factual transformation, evidence, or policy boundary
- Responsibility: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.
- Source SHA256: `eb8acddb789a6ca8717bd70df9a40c32c8f1a689a3a0ae7b3b9ffc55d2ab3af4`

## 1. STEP 7F.1A.4 contract delta

- Fails closed when an applicable body page has extraction status ERROR while retaining valid blank-page handling.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

The file belongs to the **pipeline stage** layer and **factual transformation, evidence, or policy boundary** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

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

- `from landscout.common.immutable_mapping import freeze_mapping`
- `from landscout.common.planning_text import (
    normalize_planning_search_text,
    normalize_planning_search_text_with_mapping,
    raw_context_from_spans,
)`
- `from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml`
- `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    validate_planning_regulation_index,
)`
- `from landscout.stages.planning_overlay import technical_overlay_tolerance`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `_normalize_search_text`

- Category: module-level alias/value.
- Exact declaration:

```python
_normalize_search_text = normalize_planning_search_text
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_normalize_search_text_with_mapping`

- Category: module-level alias/value.
- Exact declaration:

```python
_normalize_search_text_with_mapping = normalize_planning_search_text_with_mapping
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_raw_context`

- Category: module-level alias/value.
- Exact declaration:

```python
_raw_context = raw_context_from_spans
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `__all__`

- Category: explicit package/module export list.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `PlanningRegulationStructureConfig`
  - `PlanningRegulationStructureError`
  - `PlanningRegulationStructureResult`
  - `load_planning_regulation_structure_config`
  - `planning_regulation_section_page_fragments`
  - `structure_planning_regulation`
  - `validate_planning_regulation_structure`
  - `validate_planning_regulation_structure_with_fragments`

### `SECTION_HASH_SCHEMA_VERSION`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
SECTION_HASH_SCHEMA_VERSION = 3
```

- Qualified consumers:
  - import: `tests.unit.test_structure_planning_regulation::<module>` via `from landscout.stages.structure_planning_regulation import (
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
)`
  - value/type reference: `tests.unit.test_structure_planning_regulation::test_structure_schema_versions_are_explicit` via `SECTION_HASH_SCHEMA_VERSION`

### `STRUCTURE_MANIFEST_SCHEMA_VERSION`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
STRUCTURE_MANIFEST_SCHEMA_VERSION = 4
```

- Qualified consumers:
  - import: `tests.unit.test_structure_planning_regulation::<module>` via `from landscout.stages.structure_planning_regulation import (
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
)`
  - value/type reference: `tests.unit.test_structure_planning_regulation::test_structure_schema_versions_are_explicit` via `STRUCTURE_MANIFEST_SCHEMA_VERSION`

### `_SUPPORTED_CONFIG_SCHEMA_VERSION`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
_SUPPORTED_CONFIG_SCHEMA_VERSION = 2
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_SECTION_TYPES`

- Category: module constant or closed domain.
- Exact declaration:

```python
_SECTION_TYPES = frozenset({"GENERAL", "ZONE_CHAPTER", "ARTICLE", "OTHER"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_MAPPING_STATUSES`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
_MAPPING_STATUSES = frozenset({"EXACT", "CONFIG_ALIAS", "UNMAPPED", "AMBIGUOUS"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_MAPPING_METHODS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
_MAPPING_METHODS = frozenset({"EXACT_HEADING", "CONFIG_ALIAS", "NONE", "AMBIGUOUS"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_EVIDENCE_SCOPES`

- Category: module constant or closed domain.
- Exact declaration:

```python
_EVIDENCE_SCOPES = frozenset({"GENERAL_RULE", "ZONE_SPECIFIC_RULE", "OTHER_TEXT"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_ZONE_INPUT_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
_ZONE_INPUT_COLUMNS = (
    "planning_zone_id",
    "source_zone_id",
    "zone_label_raw",
    "source_document_id",
    "source_archive_sha256",
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `planning_zone_id`
  - `source_zone_id`
  - `zone_label_raw`
  - `source_document_id`
  - `source_archive_sha256`

### `_REQUIRED_INTERSECTION_INPUT_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `parcel_id`
  - `planning_zone_id`
  - `source_zone_id`
  - `zone_label_raw`
  - `relation_type`
  - `intersection_area_m2`
  - `source_document_id`
  - `source_archive_sha256`

### `_OPTIONAL_INTERSECTION_INPUT_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
_OPTIONAL_INTERSECTION_INPUT_COLUMNS = (
    "parcel_metric_area_m2",
    "zone_area_m2",
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `parcel_metric_area_m2`
  - `zone_area_m2`

### `SECTION_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `section_id`
  - `parent_section_id`
  - `section_type`
  - `heading_raw`
  - `heading_normalized`
  - `zone_chapter_label`
  - `article_number_raw`
  - `article_title_raw`
  - `start_record_id`
  - `end_record_id`
  - `source_record_count`
  - `source_records_sha256`
  - `start_page`
  - `end_page`
  - `page_numbers`
  - `raw_text`
  - `normalized_text`
  - `character_count`
  - `section_content_sha256`
  - `document_id`
  - `archive_sha256`
  - `pdf_sha256`
  - `index_content_sha256`
  - `structure_profile`

### `ZONE_MAPPING_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `source_zone_label_raw`
  - `resolved_zone_chapter_label`
  - `mapping_status`
  - `mapping_method`
  - `matched_section_id`
  - `zone_polygon_count`
  - `candidate_parcel_count`
  - `candidate_intersection_count`
  - `dominant_candidate_count`
  - `document_id`
  - `archive_sha256`
  - `pdf_sha256`
  - `index_content_sha256`
  - `structure_profile`

### `TOPIC_EVIDENCE_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `topic`
  - `search_term`
  - `normalized_search_term`
  - `match_policy`
  - `section_id`
  - `evidence_scope`
  - `zone_chapter_label`
  - `article_number_raw`
  - `page_number`
  - `occurrence_count`
  - `first_match_normalized_start`
  - `first_match_normalized_end`
  - `first_match_raw_start`
  - `first_match_raw_end`
  - `raw_context`
  - `normalized_context`
  - `document_id`
  - `archive_sha256`
  - `pdf_sha256`
  - `index_content_sha256`
  - `structure_profile`


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `PlanningRegulationStructureError`

**Source purpose:** Raised when factual regulation structure integrity cannot be proven.

- Exact decorators: none.
- Exact bases: `ValueError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    load_planning_regulation_structure_config,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`
- import: `landscout.stages.interpret_bess_zoning::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    validate_planning_regulation_structure_with_fragments,
)`
- value/type reference: `landscout.stages.interpret_bess_zoning::validate_bess_zoning_precheck` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.interpret_bess_zoning::interpret_bess_zoning` via `PlanningRegulationStructureError`
- constructor call: `landscout.stages.structure_planning_regulation::load_planning_regulation_structure_config` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.structure_planning_regulation::load_planning_regulation_structure_config` via `PlanningRegulationStructureError`
- constructor call: `landscout.stages.structure_planning_regulation::_strict_string` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.structure_planning_regulation::_strict_string` via `PlanningRegulationStructureError`
- constructor call: `landscout.stages.structure_planning_regulation::_strict_nonnegative_integer` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.structure_planning_regulation::_strict_nonnegative_integer` via `PlanningRegulationStructureError`
- constructor call: `landscout.stages.structure_planning_regulation::_strict_positive_integer` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.structure_planning_regulation::_strict_positive_integer` via `PlanningRegulationStructureError`
- constructor call: `landscout.stages.structure_planning_regulation::_validated_sha256` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.structure_planning_regulation::_validated_sha256` via `PlanningRegulationStructureError`
- constructor call: `landscout.stages.structure_planning_regulation::_canonical_value` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.structure_planning_regulation::_canonical_value` via `PlanningRegulationStructureError`
- constructor call: `landscout.stages.structure_planning_regulation::_canonical_sha256` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.structure_planning_regulation::_canonical_sha256` via `PlanningRegulationStructureError`
- constructor call: `landscout.stages.structure_planning_regulation::_validate_document_lock` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_document_lock` via `PlanningRegulationStructureError`
- constructor call: `landscout.stages.structure_planning_regulation::_line_records` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.structure_planning_regulation::_line_records` via `PlanningRegulationStructureError`
- constructor call: `landscout.stages.structure_planning_regulation::_classify_structural_heading` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.structure_planning_regulation::_classify_structural_heading` via `PlanningRegulationStructureError`
- constructor call: `landscout.stages.structure_planning_regulation::_heading_events` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.structure_planning_regulation::_heading_events` via `PlanningRegulationStructureError`
- constructor call: `landscout.stages.structure_planning_regulation::_section_starts` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.structure_planning_regulation::_section_starts` via `PlanningRegulationStructureError`
- constructor call: `landscout.stages.structure_planning_regulation::_build_sections` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_sections` via `PlanningRegulationStructureError`
- constructor call: `landscout.stages.structure_planning_regulation::_validated_zoning_inputs` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.structure_planning_regulation::_validated_zoning_inputs` via `PlanningRegulationStructureError`
- constructor call: `landscout.stages.structure_planning_regulation::_resolved_alias` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.structure_planning_regulation::_resolved_alias` via `PlanningRegulationStructureError`
- constructor call: `landscout.stages.structure_planning_regulation::_build_zone_mapping` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_zone_mapping` via `PlanningRegulationStructureError`
- constructor call: `landscout.stages.structure_planning_regulation::_evidence_scope` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.structure_planning_regulation::_evidence_scope` via `PlanningRegulationStructureError`
- constructor call: `landscout.stages.structure_planning_regulation::_page_tuple` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.structure_planning_regulation::_page_tuple` via `PlanningRegulationStructureError`
- constructor call: `landscout.stages.structure_planning_regulation::_validate_sections` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_sections` via `PlanningRegulationStructureError`
- constructor call: `landscout.stages.structure_planning_regulation::_validate_zone_mapping` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_zone_mapping` via `PlanningRegulationStructureError`
- constructor call: `landscout.stages.structure_planning_regulation::_validate_topic_evidence` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_topic_evidence` via `PlanningRegulationStructureError`
- constructor call: `landscout.stages.structure_planning_regulation::_validate_result_self` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_result_self` via `PlanningRegulationStructureError`
- constructor call: `landscout.stages.structure_planning_regulation::_resolved_config` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.structure_planning_regulation::_resolved_config` via `PlanningRegulationStructureError`
- constructor call: `landscout.stages.structure_planning_regulation::_compare_expected_result` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.structure_planning_regulation::_compare_expected_result` via `PlanningRegulationStructureError`
- constructor call: `landscout.stages.structure_planning_regulation::_section_page_fragments` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.structure_planning_regulation::_section_page_fragments` via `PlanningRegulationStructureError`
- constructor call: `landscout.stages.structure_planning_regulation::validate_planning_regulation_structure_with_fragments` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.structure_planning_regulation::validate_planning_regulation_structure_with_fragments` via `PlanningRegulationStructureError`
- constructor call: `landscout.stages.structure_planning_regulation::planning_regulation_section_page_fragments` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.structure_planning_regulation::planning_regulation_section_page_fragments` via `PlanningRegulationStructureError`
- constructor call: `landscout.stages.structure_planning_regulation::structure_planning_regulation` via `PlanningRegulationStructureError`
- value/type reference: `landscout.stages.structure_planning_regulation::structure_planning_regulation` via `PlanningRegulationStructureError`
- import: `tests.unit.test_structure_planning_regulation::<module>` via `from landscout.stages.structure_planning_regulation import (
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
)`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_old_and_unknown_result_config_schema_versions_are_rejected` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_old_and_unknown_section_hash_schema_versions_are_rejected` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_document_layout_rejects_nonexistent_indexed_pages` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_document_lock_mismatch_is_rejected` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_invalid_regex_and_unknown_yaml_field_are_controlled` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_duplicate_yaml_alias_and_alias_cycle_are_rejected` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_evidence_scope_is_derived_from_exact_section_type` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_body_page_extraction_error_stops_structure` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_coordinated_frame_mutation_is_rejected` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_unknown_topic_page_reference_is_rejected` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_coordinated_section_row_mutation_is_caught_by_outer_envelope` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_dominant_unmapped_zone_stops_processing` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_two_zone_patterns_matching_one_line_are_ambiguous` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_two_article_patterns_matching_one_line_are_ambiguous` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_general_and_article_cross_category_match_is_ambiguous` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_zone_and_general_cross_category_match_is_ambiguous` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_ambiguous_continuation_candidate_fails_with_record_diagnostic` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_rejects_changed_ambiguous_grammar` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_lossless_partition_mutation_is_rejected` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_duplicate_or_reordered_record_partition_is_rejected` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_unsorted_section_pages_are_rejected` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_article_parent_semantics_are_enforced` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_wrong_intersection_source_zone_id_is_rejected` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_intersection_area_cannot_exceed_available_geometry_area` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_intersection_upper_bound_uses_shared_relative_tolerance` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_optional_intersection_metric_change_invalidates_existing_result` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_intersection_hash_column_lineage_mutation_is_rejected` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_zone_mapping_contract_mutations_are_rejected` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_topic_evidence_semantic_mutations_are_rejected` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_coordinated_topic_evidence_and_hash_mutation_is_rebuilt_and_rejected` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_rejects_post_build_source_change` via `PlanningRegulationStructureError`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_source_and_result_hash_mutation_is_rejected` via `PlanningRegulationStructureError`

**Exact class source**

```python
class PlanningRegulationStructureError(ValueError):
    """Raised when factual regulation structure integrity cannot be proven."""
```

### `_StrictConfigModel`

**Source purpose:** Defines `_StrictConfigModel`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _StrictConfigModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
```

### `DocumentLockConfig`

**Source purpose:** Defines `DocumentLockConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `document_id` | `StrictStr` | `Field(min_length=1)` | `document_id: StrictStr = Field(min_length=1)` |
| `pdf_sha256` | `StrictStr` | `Field(pattern=r"^[0-9a-f]{64}$")` | `pdf_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` |
| `pages_content_sha256` | `StrictStr` | `Field(pattern=r"^[0-9a-f]{64}$")` | `pages_content_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` |
| `index_content_sha256` | `StrictStr` | `Field(pattern=r"^[0-9a-f]{64}$")` | `index_content_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` |
| `normalization_profile` | `StrictStr` | `Field(min_length=1)` | `normalization_profile: StrictStr = Field(min_length=1)` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

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

**Source purpose:** Defines `DocumentLayoutConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `body_start_page` | `StrictInt` | `Field(ge=1)` | `body_start_page: StrictInt = Field(ge=1)` |
| `table_of_contents_pages` | `tuple[StrictInt, ...]` | `()` | `table_of_contents_pages: tuple[StrictInt, ...] = ()` |
| `max_heading_continuation_lines` | `StrictInt` | `Field(ge=0, le=10)` | `max_heading_continuation_lines: StrictInt = Field(ge=0, le=10)` |
| `include_table_of_contents_in_topic_evidence` | `StrictBool` | `False` | `include_table_of_contents_in_topic_evidence: StrictBool = False` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.stages.structure_planning_regulation::DocumentLayoutConfig._validate_pages` via `DocumentLayoutConfig`

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

**Source purpose:** Defines `HeadingPatternsConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `zone_chapter` | `tuple[StrictStr, ...]` | `Field(min_length=1)` | `zone_chapter: tuple[StrictStr, ...] = Field(min_length=1)` |
| `article` | `tuple[StrictStr, ...]` | `Field(min_length=1)` | `article: tuple[StrictStr, ...] = Field(min_length=1)` |
| `general_section` | `tuple[StrictStr, ...]` | `Field(min_length=1)` | `general_section: tuple[StrictStr, ...] = Field(min_length=1)` |
| `continuation` | `tuple[StrictStr, ...]` | `()` | `continuation: tuple[StrictStr, ...] = ()` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class HeadingPatternsConfig(_StrictConfigModel):
    zone_chapter: tuple[StrictStr, ...] = Field(min_length=1)
    article: tuple[StrictStr, ...] = Field(min_length=1)
    general_section: tuple[StrictStr, ...] = Field(min_length=1)
    continuation: tuple[StrictStr, ...] = ()
```

### `IgnoredPatternsConfig`

**Source purpose:** Defines `IgnoredPatternsConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `page_headers` | `tuple[StrictStr, ...]` | `()` | `page_headers: tuple[StrictStr, ...] = ()` |
| `page_footers` | `tuple[StrictStr, ...]` | `()` | `page_footers: tuple[StrictStr, ...] = ()` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class IgnoredPatternsConfig(_StrictConfigModel):
    page_headers: tuple[StrictStr, ...] = ()
    page_footers: tuple[StrictStr, ...] = ()
```

### `TopicMatchPolicyConfig`

**Source purpose:** Defines `TopicMatchPolicyConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `boundary_mode` | `Literal['token']` | `required` | `boundary_mode: Literal["token"]` |
| `overlap_resolution` | `Literal['longest_match']` | `required` | `overlap_resolution: Literal["longest_match"]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

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

**Source purpose:** Strict, document-locked grammar for one factual regulation structure.

- Exact decorators: none.
- Exact bases: `_StrictConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `schema_version` | `StrictInt` | `required` | `schema_version: StrictInt` |
| `structure_profile` | `StrictStr` | `Field(min_length=1)` | `structure_profile: StrictStr = Field(min_length=1)` |
| `document_lock` | `DocumentLockConfig` | `required` | `document_lock: DocumentLockConfig` |
| `document_layout` | `DocumentLayoutConfig` | `required` | `document_layout: DocumentLayoutConfig` |
| `heading_patterns` | `HeadingPatternsConfig` | `required` | `heading_patterns: HeadingPatternsConfig` |
| `ignored_patterns` | `IgnoredPatternsConfig` | `required` | `ignored_patterns: IgnoredPatternsConfig` |
| `zone_aliases` | `dict[StrictStr, StrictStr]` | `required` | `zone_aliases: dict[StrictStr, StrictStr]` |
| `topics` | `dict[StrictStr, tuple[StrictStr, ...]]` | `required` | `topics: dict[StrictStr, tuple[StrictStr, ...]]` |
| `topic_match_policy` | `TopicMatchPolicyConfig` | `required` | `topic_match_policy: TopicMatchPolicyConfig` |
| `topic_context_characters` | `StrictInt` | `Field(ge=0)` | `topic_context_characters: StrictInt = Field(ge=0)` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    load_planning_regulation_structure_config,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`
- import: `landscout.stages.interpret_bess_zoning::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    validate_planning_regulation_structure_with_fragments,
)`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_result` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::validate_bess_zoning_precheck` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::interpret_bess_zoning` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::PlanningRegulationStructureConfig._validate_grammar` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::load_planning_regulation_structure_config` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::_config_sha256` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_document_lock` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::_line_records` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::_heading_events` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::_section_starts` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_sections` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_zone_mapping` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_topic_evidence` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_sections` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_zone_mapping` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_topic_evidence` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_structure_result` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_result_self` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::_resolved_config` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::validate_planning_regulation_structure_with_fragments` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::validate_planning_regulation_structure` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::planning_regulation_section_page_fragments` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::structure_planning_regulation` via `PlanningRegulationStructureConfig`
- import: `tests.integration.test_gpu_planning_end_to_end::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureResult,
    structure_planning_regulation,
)`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_structure_config` via `PlanningRegulationStructureConfig`
- import: `tests.unit.test_interpret_bess_zoning::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
)`
- value/type reference: `tests.unit.test_interpret_bess_zoning::_structure_config` via `PlanningRegulationStructureConfig`
- import: `tests.unit.test_structure_planning_regulation::<module>` via `from landscout.stages.structure_planning_regulation import (
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
)`
- value/type reference: `tests.unit.test_structure_planning_regulation::_config` via `PlanningRegulationStructureConfig`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_old_and_unknown_config_schema_versions_are_rejected` via `PlanningRegulationStructureConfig`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_toc_topic_evidence_flag_rejects_boolean_coercion` via `PlanningRegulationStructureConfig`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_toc_topic_evidence_flag_accepts_exact_booleans` via `PlanningRegulationStructureConfig`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_evidence_scope_is_derived_from_exact_section_type` via `PlanningRegulationStructureConfig`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_reversed_topic_mapping_keys_do_not_change_output_or_hashes` via `PlanningRegulationStructureConfig`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_equal_length_overlap_uses_configured_term_order_as_tie_break` via `PlanningRegulationStructureConfig`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_blank_only_prefix_is_preserved_in_first_actual_section` via `PlanningRegulationStructureConfig`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence` via `PlanningRegulationStructureConfig`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_blank_gap_after_toc_is_preserved_without_a_blank_other_section` via `PlanningRegulationStructureConfig`
- value/type reference: `tests.unit.test_structure_planning_regulation::_structure_with_document_layout` via `PlanningRegulationStructureConfig`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_heading_patterns_require_mandatory_named_captures` via `PlanningRegulationStructureConfig`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_optional_pattern_lists_may_be_empty` via `PlanningRegulationStructureConfig`
- value/type reference: `tests.unit.test_structure_planning_regulation::_config_with_structural_patterns` via `PlanningRegulationStructureConfig`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_identical_structural_regex_across_groups_is_rejected_by_config` via `PlanningRegulationStructureConfig`

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
                    raise ValueError(
                        f"invalid regular expression: {pattern}"
                    ) from error
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
        object.__setattr__(self, "zone_aliases", freeze_mapping(self.zone_aliases))
        object.__setattr__(self, "topics", freeze_mapping(self.topics))
        return self
```

### `PlanningRegulationStructureResult`

**Source purpose:** Immutable lineage envelope for regulation sections and factual evidence.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `document_id` | `str` | `required` | `document_id: str` |
| `archive_sha256` | `str` | `required` | `archive_sha256: str` |
| `pdf_sha256` | `str` | `required` | `pdf_sha256: str` |
| `index_content_sha256` | `str` | `required` | `index_content_sha256: str` |
| `structure_profile` | `str` | `required` | `structure_profile: str` |
| `structure_config_schema_version` | `int` | `required` | `structure_config_schema_version: int` |
| `structure_config_sha256` | `str` | `required` | `structure_config_sha256: str` |
| `zones_content_sha256` | `str` | `required` | `zones_content_sha256: str` |
| `zoning_intersection_hash_columns` | `tuple[str, ...]` | `required` | `zoning_intersection_hash_columns: tuple[str, ...]` |
| `zoning_intersections_content_sha256` | `str` | `required` | `zoning_intersections_content_sha256: str` |
| `source_records_sha256` | `str` | `required` | `source_records_sha256: str` |
| `section_hash_schema_version` | `int` | `required` | `section_hash_schema_version: int` |
| `sections_content_sha256` | `str` | `required` | `sections_content_sha256: str` |
| `zone_map_content_sha256` | `str` | `required` | `zone_map_content_sha256: str` |
| `topic_evidence_content_sha256` | `str` | `required` | `topic_evidence_content_sha256: str` |
| `structure_result_content_sha256` | `str` | `required` | `structure_result_content_sha256: str` |
| `sections` | `pd.DataFrame` | `required` | `sections: pd.DataFrame` |
| `zone_mapping` | `pd.DataFrame` | `required` | `zone_mapping: pd.DataFrame` |
| `topic_evidence` | `pd.DataFrame` | `required` | `topic_evidence: pd.DataFrame` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    load_planning_regulation_structure_config,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`
- import: `landscout.stages.interpret_bess_zoning::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    validate_planning_regulation_structure_with_fragments,
)`
- value/type reference: `landscout.stages.interpret_bess_zoning::_factual_structure_sha256` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_policy_lock` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.interpret_bess_zoning::_zone_mapping_input_sha256` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.interpret_bess_zoning::_zone_chapter_rows` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.interpret_bess_zoning::_required_section_ids_by_chapter` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_policy_evidence` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_mapping` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.interpret_bess_zoning::_lineage` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_chapter_policy` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_route_assessments` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_evidence_route_links` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_source_zone_policy` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_parcel_zone_interpretations` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_result` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.interpret_bess_zoning::validate_bess_zoning_precheck` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.interpret_bess_zoning::interpret_bess_zoning` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.structure_planning_regulation::_frame_hash` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.structure_planning_regulation::_structure_result_content_sha256` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.structure_planning_regulation::_result_with_hashes` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_sections` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_zone_mapping` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_topic_evidence` via `PlanningRegulationStructureResult`
- constructor call: `landscout.stages.structure_planning_regulation::_build_structure_result` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_structure_result` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_result_self` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.structure_planning_regulation::_compare_expected_result` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.structure_planning_regulation::_section_page_fragments` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.structure_planning_regulation::validate_planning_regulation_structure_with_fragments` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.structure_planning_regulation::validate_planning_regulation_structure` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.structure_planning_regulation::planning_regulation_section_page_fragments` via `PlanningRegulationStructureResult`
- value/type reference: `landscout.stages.structure_planning_regulation::structure_planning_regulation` via `PlanningRegulationStructureResult`
- import: `tests.integration.test_gpu_planning_end_to_end::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureResult,
    structure_planning_regulation,
)`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_policy` via `PlanningRegulationStructureResult`

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

**Source purpose:** Defines `_LineRecord`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `record_id` | `str` | `required` | `record_id: str` |
| `page_number` | `int` | `required` | `page_number: int` |
| `page_line_number` | `int` | `required` | `page_line_number: int` |
| `raw` | `str` | `required` | `raw: str` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.stages.structure_planning_regulation::_line_records` via `_LineRecord`
- value/type reference: `landscout.stages.structure_planning_regulation::_line_records` via `_LineRecord`
- value/type reference: `landscout.stages.structure_planning_regulation::_source_record_payload` via `_LineRecord`
- value/type reference: `landscout.stages.structure_planning_regulation::_source_records_sha256` via `_LineRecord`
- value/type reference: `landscout.stages.structure_planning_regulation::_classify_structural_heading` via `_LineRecord`
- value/type reference: `landscout.stages.structure_planning_regulation::_heading_events` via `_LineRecord`
- value/type reference: `landscout.stages.structure_planning_regulation::_page_fragments` via `_LineRecord`
- value/type reference: `landscout.stages.structure_planning_regulation::_section_starts` via `_LineRecord`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_sections` via `_LineRecord`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_sections` via `_LineRecord`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_structure_result` via `_LineRecord`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_result_self` via `_LineRecord`

**Exact class source**

```python
class _LineRecord:
    record_id: str
    page_number: int
    page_line_number: int
    raw: str
```

### `_HeadingEvent`

**Source purpose:** Defines `_HeadingEvent`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `record_position` | `int` | `required` | `record_position: int` |
| `section_type` | `Literal['GENERAL', 'ZONE_CHAPTER', 'ARTICLE']` | `required` | `section_type: Literal["GENERAL", "ZONE_CHAPTER", "ARTICLE"]` |
| `heading_raw` | `str` | `required` | `heading_raw: str` |
| `heading_normalized` | `str` | `required` | `heading_normalized: str` |
| `zone_chapter_label` | `str \| None` | `required` | `zone_chapter_label: str \| None` |
| `article_number_raw` | `str \| None` | `required` | `article_number_raw: str \| None` |
| `article_title_raw` | `str \| None` | `required` | `article_title_raw: str \| None` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.stages.structure_planning_regulation::_heading_events` via `_HeadingEvent`
- value/type reference: `landscout.stages.structure_planning_regulation::_heading_events` via `_HeadingEvent`
- value/type reference: `landscout.stages.structure_planning_regulation::_section_starts` via `_HeadingEvent`

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

**Source purpose:** Defines `_StructuralHeadingMatch`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `section_type` | `Literal['GENERAL', 'ZONE_CHAPTER', 'ARTICLE']` | `required` | `section_type: Literal["GENERAL", "ZONE_CHAPTER", "ARTICLE"]` |
| `pattern_index` | `int` | `required` | `pattern_index: int` |
| `named_captures` | `tuple[tuple[str, str \| None], ...]` | `required` | `named_captures: tuple[tuple[str, str \| None], ...]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.stages.structure_planning_regulation::_classify_structural_heading` via `_StructuralHeadingMatch`
- value/type reference: `landscout.stages.structure_planning_regulation::_classify_structural_heading` via `_StructuralHeadingMatch`

**Exact class source**

```python
class _StructuralHeadingMatch:
    section_type: Literal["GENERAL", "ZONE_CHAPTER", "ARTICLE"]
    pattern_index: int
    named_captures: tuple[tuple[str, str | None], ...]
```

### `_SectionBoundary`

**Source purpose:** Defines `_SectionBoundary`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `record_position` | `int` | `required` | `record_position: int` |
| `event` | `_HeadingEvent \| None` | `required` | `event: _HeadingEvent \| None` |
| `forced_table_of_contents` | `bool` | `required` | `forced_table_of_contents: bool` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.stages.structure_planning_regulation::_section_starts` via `_SectionBoundary`
- value/type reference: `landscout.stages.structure_planning_regulation::_section_starts` via `_SectionBoundary`

**Exact class source**

```python
class _SectionBoundary:
    record_position: int
    event: _HeadingEvent | None
    forced_table_of_contents: bool
```

### `_SectionBuild`

**Source purpose:** Defines `_SectionBuild`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `row` | `dict[str, object]` | `required` | `row: dict[str, object]` |
| `page_fragments` | `tuple[tuple[int, str], ...]` | `required` | `page_fragments: tuple[tuple[int, str], ...]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.stages.structure_planning_regulation::_build_sections` via `_SectionBuild`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_sections` via `_SectionBuild`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_topic_evidence` via `_SectionBuild`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_topic_evidence` via `_SectionBuild`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_structure_result` via `_SectionBuild`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_result_self` via `_SectionBuild`
- value/type reference: `landscout.stages.structure_planning_regulation::_section_page_fragments` via `_SectionBuild`

**Exact class source**

```python
class _SectionBuild:
    row: dict[str, object]
    page_fragments: tuple[tuple[int, str], ...]
```

### `_TopicMatch`

**Source purpose:** Defines `_TopicMatch`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `term_index` | `int` | `required` | `term_index: int` |
| `search_term` | `str` | `required` | `search_term: str` |
| `normalized_term` | `str` | `required` | `normalized_term: str` |
| `normalized_start` | `int` | `required` | `normalized_start: int` |
| `normalized_end` | `int` | `required` | `normalized_end: int` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.stages.structure_planning_regulation::_literal_topic_matches` via `_TopicMatch`
- value/type reference: `landscout.stages.structure_planning_regulation::_literal_topic_matches` via `_TopicMatch`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_topic_evidence` via `_TopicMatch`

**Exact class source**

```python
class _TopicMatch:
    term_index: int
    search_term: str
    normalized_term: str
    normalized_start: int
    normalized_end: int
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `DocumentLayoutConfig._validate_pages`

**Purpose:** Implements `validate pages` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _validate_pages(self) -> DocumentLayoutConfig:
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `DocumentLayoutConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- Explicit raise paths:
  - `ValueError(<br>                "table_of_contents_pages must contain unique ascending positive integers"<br>            )` under lexical guard `any(page < 1 for page in pages) or tuple(sorted(set(pages))) != pages`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `model_validator` | `pydantic.model_validator` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `TopicMatchPolicyConfig.identifier`

**Purpose:** Implements `identifier` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def identifier(self) -> str:
```

- Exact decorators: `property`.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `f"{self.boundary_mode}_{self.overlap_resolution}"`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
- No calls.

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def identifier(self) -> str:
        return f"{self.boundary_mode}_{self.overlap_resolution}"
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `PlanningRegulationStructureConfig._validate_grammar`

**Purpose:** Implements `validate grammar` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _validate_grammar(self) -> PlanningRegulationStructureConfig:
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `PlanningRegulationStructureConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- Explicit raise paths:
  - `ValueError(<br>                f"unsupported structure config schema: {self.schema_version}"<br>            )` under lexical guard `self.schema_version != _SUPPORTED_CONFIG_SCHEMA_VERSION`.
  - `ValueError("regular-expression patterns must be unique")` under lexical guard `len(set(patterns)) != len(patterns)`.
  - `ValueError(<br>                        f"invalid regular expression: {pattern}"<br>                    )`.
  - `ValueError(<br>                        "identical structural heading regex is reused across "<br>                        f"groups {previous} and {category}"<br>                    )` under lexical guard `previous is not None`.
  - `ValueError(<br>                        f"{label} pattern lacks named captures: {sorted(missing)}"<br>                    )` under lexical guard `missing`.
  - `ValueError("topics must not be empty")` under lexical guard `not self.topics`.
  - `ValueError(f"topic {topic!r} must contain literal terms")` under lexical guard `not terms`.
  - `ValueError(<br>                        f"topic {topic!r} contains duplicate normalized terms"<br>                    )` under lexical guard `not normalized_term or normalized_term in normalized`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `_exact_config_string` | `landscout.stages.structure_planning_regulation._exact_config_string` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `re.compile` | `re.compile` |
| `structural_pattern_owners.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `required.difference` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `self.zone_aliases.items` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureConfig.zone_aliases.items` |
| `_validate_alias_cycles` | `landscout.stages.structure_planning_regulation._validate_alias_cycles` |
| `_normalize_search_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized.add` | `unresolved local/third-party receiver; no ownership inferred` |
| `object.__setattr__` | `unresolved local/third-party receiver; no ownership inferred` |
| `freeze_mapping` | `landscout.common.immutable_mapping.freeze_mapping` |
| `model_validator` | `pydantic.model_validator` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `structural_pattern_owners[pattern] = category`<br>`normalized.add(normalized_term)` |
| Direct parameter mutation | None directly present. |

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
                    raise ValueError(
                        f"invalid regular expression: {pattern}"
                    ) from error
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
        object.__setattr__(self, "zone_aliases", freeze_mapping(self.zone_aliases))
        object.__setattr__(self, "topics", freeze_mapping(self.topics))
        return self
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_exact_config_string`

**Purpose:** Implements `exact config string` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _exact_config_string(value: str, label: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `str` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `value`
- Explicit raise paths:
  - `ValueError(f"{label} must be a non-empty exact string")` under lexical guard `not value or value != value.strip()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::PlanningRegulationStructureConfig._validate_grammar` via `_exact_config_string`
- value/type reference: `landscout.stages.structure_planning_regulation::PlanningRegulationStructureConfig._validate_grammar` via `_exact_config_string`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _exact_config_string(value: str, label: str) -> str:
    if not value or value != value.strip():
        raise ValueError(f"{label} must be a non-empty exact string")
    return value
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_alias_cycles`

**Purpose:** Implements `validate alias cycles` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _validate_alias_cycles(aliases: Mapping[str, str]) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `aliases` | positional-or-keyword | `Mapping[str, str]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `ValueError(f"zone alias cycle detected at {current!r}")` under lexical guard `current in seen`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::PlanningRegulationStructureConfig._validate_grammar` via `_validate_alias_cycles`
- value/type reference: `landscout.stages.structure_planning_regulation::PlanningRegulationStructureConfig._validate_grammar` via `_validate_alias_cycles`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `seen.add` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `seen.add(current)` |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `load_planning_regulation_structure_config`

**Purpose:** Load and strictly validate a document-specific structure grammar.

**Exact signature**

```python
def load_planning_regulation_structure_config(
    path: str | Path,
) -> PlanningRegulationStructureConfig:
```

- Exact decorators: none.
- Declared return annotation: `PlanningRegulationStructureConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `str \| Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `PlanningRegulationStructureConfig.model_validate(payload)`
- Explicit raise paths:
  - `PlanningRegulationStructureError(<br>                "Planning structure configuration must be a mapping"<br>            )` under lexical guard `not isinstance(payload, Mapping)`.
  - `re-raise`.
  - `PlanningRegulationStructureError(str(error))`.
  - `PlanningRegulationStructureError(<br>            "Planning structure configuration is invalid"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    load_planning_regulation_structure_config,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`
- direct call: `landscout.stages.structure_planning_regulation::_resolved_config` via `load_planning_regulation_structure_config`
- value/type reference: `landscout.stages.structure_planning_regulation::_resolved_config` via `load_planning_regulation_structure_config`
- import: `tests.unit.test_structure_planning_regulation::<module>` via `from landscout.stages.structure_planning_regulation import (
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
)`
- direct call: `tests.unit.test_structure_planning_regulation::test_invalid_regex_and_unknown_yaml_field_are_controlled` via `load_planning_regulation_structure_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_invalid_regex_and_unknown_yaml_field_are_controlled` via `load_planning_regulation_structure_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_duplicate_yaml_alias_and_alias_cycle_are_rejected` via `load_planning_regulation_structure_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_duplicate_yaml_alias_and_alias_cycle_are_rejected` via `load_planning_regulation_structure_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Path` | `pathlib.Path` |
| `loads_strict_yaml` | `landscout.common.strict_yaml.loads_strict_yaml` |
| `config_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |
| `PlanningRegulationStructureConfig.model_validate` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureConfig.model_validate` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `config_path.read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def load_planning_regulation_structure_config(
    path: str | Path,
) -> PlanningRegulationStructureConfig:
    """Load and strictly validate a document-specific structure grammar."""

    try:
        config_path = Path(path)
        payload = loads_strict_yaml(config_path.read_bytes())
        if not isinstance(payload, Mapping):
            raise PlanningRegulationStructureError(
                "Planning structure configuration must be a mapping"
            )
        return PlanningRegulationStructureConfig.model_validate(payload)
    except PlanningRegulationStructureError:
        raise
    except StrictYamlError as error:
        raise PlanningRegulationStructureError(str(error)) from error
    except Exception as error:
        raise PlanningRegulationStructureError(
            "Planning structure configuration is invalid"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_strict_string`

**Purpose:** Implements `strict string` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _strict_string(value: object, label: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `value`
- Explicit raise paths:
  - `PlanningRegulationStructureError(<br>            f"{label} must be a non-empty exact string"<br>        )` under lexical guard `not isinstance(value, str) or not value or value != value.strip()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_validated_sha256` via `_strict_string`
- value/type reference: `landscout.stages.structure_planning_regulation::_validated_sha256` via `_strict_string`
- direct call: `landscout.stages.structure_planning_regulation::_canonical_chapter_label` via `_strict_string`
- value/type reference: `landscout.stages.structure_planning_regulation::_canonical_chapter_label` via `_strict_string`
- direct call: `landscout.stages.structure_planning_regulation::_validate_source_label_values` via `_strict_string`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_source_label_values` via `_strict_string`
- direct call: `landscout.stages.structure_planning_regulation::_build_zone_mapping` via `_strict_string`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_zone_mapping` via `_strict_string`
- direct call: `landscout.stages.structure_planning_regulation::_validate_sections` via `_strict_string`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_sections` via `_strict_string`
- direct call: `landscout.stages.structure_planning_regulation::_validate_zone_mapping` via `_strict_string`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_zone_mapping` via `_strict_string`
- direct call: `landscout.stages.structure_planning_regulation::_validate_topic_evidence` via `_strict_string`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_topic_evidence` via `_strict_string`
- direct call: `landscout.stages.structure_planning_regulation::_validate_result_self` via `_strict_string`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_result_self` via `_strict_string`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_strict_nonnegative_integer`

**Purpose:** Implements `strict nonnegative integer` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _strict_nonnegative_integer(value: object, label: str) -> int:
```

- Exact decorators: none.
- Declared return annotation: `int`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- Explicit raise paths:
  - `PlanningRegulationStructureError(f"{label} must be an integer")` under lexical guard `isinstance(value, bool) or not isinstance(value, Integral)`.
  - `PlanningRegulationStructureError(f"{label} must be non-negative")` under lexical guard `result < 0`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_strict_positive_integer` via `_strict_nonnegative_integer`
- value/type reference: `landscout.stages.structure_planning_regulation::_strict_positive_integer` via `_strict_nonnegative_integer`
- direct call: `landscout.stages.structure_planning_regulation::_validate_sections` via `_strict_nonnegative_integer`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_sections` via `_strict_nonnegative_integer`
- direct call: `landscout.stages.structure_planning_regulation::_validate_zone_mapping` via `_strict_nonnegative_integer`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_zone_mapping` via `_strict_nonnegative_integer`
- direct call: `landscout.stages.structure_planning_regulation::_validate_topic_evidence` via `_strict_nonnegative_integer`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_topic_evidence` via `_strict_nonnegative_integer`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_strict_positive_integer`

**Purpose:** Implements `strict positive integer` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _strict_positive_integer(value: object, label: str) -> int:
```

- Exact decorators: none.
- Declared return annotation: `int`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- Explicit raise paths:
  - `PlanningRegulationStructureError(f"{label} must be positive")` under lexical guard `result == 0`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_validate_document_lock` via `_strict_positive_integer`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_document_lock` via `_strict_positive_integer`
- direct call: `landscout.stages.structure_planning_regulation::_line_records` via `_strict_positive_integer`
- value/type reference: `landscout.stages.structure_planning_regulation::_line_records` via `_strict_positive_integer`
- direct call: `landscout.stages.structure_planning_regulation::_page_tuple` via `_strict_positive_integer`
- value/type reference: `landscout.stages.structure_planning_regulation::_page_tuple` via `_strict_positive_integer`
- direct call: `landscout.stages.structure_planning_regulation::_validate_sections` via `_strict_positive_integer`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_sections` via `_strict_positive_integer`
- direct call: `landscout.stages.structure_planning_regulation::_validate_topic_evidence` via `_strict_positive_integer`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_topic_evidence` via `_strict_positive_integer`
- direct call: `landscout.stages.structure_planning_regulation::_validate_result_self` via `_strict_positive_integer`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_result_self` via `_strict_positive_integer`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_strict_nonnegative_integer` | `landscout.stages.structure_planning_regulation._strict_nonnegative_integer` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _strict_positive_integer(value: object, label: str) -> int:
    result = _strict_nonnegative_integer(value, label)
    if result == 0:
        raise PlanningRegulationStructureError(f"{label} must be positive")
    return result
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validated_sha256`

**Purpose:** Implements `validated sha256` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _validated_sha256(value: object, label: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `checksum`
- Explicit raise paths:
  - `PlanningRegulationStructureError(<br>            f"{label} must be exactly 64 lowercase hexadecimal characters"<br>        )` under lexical guard `re.fullmatch(r"[0-9a-f]{64}", checksum) is None`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_validate_sections` via `_validated_sha256`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_sections` via `_validated_sha256`
- direct call: `landscout.stages.structure_planning_regulation::_validate_result_self` via `_validated_sha256`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_result_self` via `_validated_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_strict_string` | `landscout.stages.structure_planning_regulation._strict_string` |
| `re.fullmatch` | `re.fullmatch` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_canonical_value`

**Purpose:** Implements `canonical value` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _canonical_value(value: object) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `None`
  - `_canonical_value(value.item())`
  - `[_canonical_value(item) for item in value]`
  - `{str(key): _canonical_value(item) for key, item in value.items()}`
  - `value`
- Explicit raise paths:
  - `PlanningRegulationStructureError(<br>        f"Value of type {type(value).__name__} cannot be canonically serialized"<br>    )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_canonical_value` via `_canonical_value`
- value/type reference: `landscout.stages.structure_planning_regulation::_canonical_value` via `_canonical_value`
- direct call: `landscout.stages.structure_planning_regulation::_canonical_sha256` via `_canonical_value`
- value/type reference: `landscout.stages.structure_planning_regulation::_canonical_sha256` via `_canonical_value`
- direct call: `landscout.stages.structure_planning_regulation::_canonical_frame_rows` via `_canonical_value`
- value/type reference: `landscout.stages.structure_planning_regulation::_canonical_frame_rows` via `_canonical_value`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `_canonical_value` | `landscout.stages.structure_planning_regulation._canonical_value` |
| `value.item` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `math.isnan` | `math.isnan` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_canonical_sha256`

**Purpose:** Implements `canonical sha256` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _canonical_sha256(value: object) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `sha256(serialized).hexdigest()`
- Explicit raise paths:
  - `re-raise`.
  - `PlanningRegulationStructureError(<br>            "Canonical integrity serialization failed"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_config_sha256` via `_canonical_sha256`
- value/type reference: `landscout.stages.structure_planning_regulation::_config_sha256` via `_canonical_sha256`
- direct call: `landscout.stages.structure_planning_regulation::_source_records_sha256` via `_canonical_sha256`
- value/type reference: `landscout.stages.structure_planning_regulation::_source_records_sha256` via `_canonical_sha256`
- direct call: `landscout.stages.structure_planning_regulation::_section_content_sha256` via `_canonical_sha256`
- value/type reference: `landscout.stages.structure_planning_regulation::_section_content_sha256` via `_canonical_sha256`
- direct call: `landscout.stages.structure_planning_regulation::_input_frame_sha256` via `_canonical_sha256`
- value/type reference: `landscout.stages.structure_planning_regulation::_input_frame_sha256` via `_canonical_sha256`
- direct call: `landscout.stages.structure_planning_regulation::_frame_hash` via `_canonical_sha256`
- value/type reference: `landscout.stages.structure_planning_regulation::_frame_hash` via `_canonical_sha256`
- direct call: `landscout.stages.structure_planning_regulation::_structure_result_content_sha256` via `_canonical_sha256`
- value/type reference: `landscout.stages.structure_planning_regulation::_structure_result_content_sha256` via `_canonical_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `json.dumps(<br>            _canonical_value(value),<br>            ensure_ascii=False,<br>            allow_nan=False,<br>            sort_keys=True,<br>            separators=(",", ":"),<br>        ).encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `_canonical_value` | `landscout.stages.structure_planning_regulation._canonical_value` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |
| `sha256(serialized).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(serialized).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_config_sha256`

**Purpose:** Implements `config sha256` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _config_sha256(config: PlanningRegulationStructureConfig) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `PlanningRegulationStructureConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_sha256(<br>        {<br>            "domain": "landscout.planning_regulation.structure_config",<br>            "config": payload,<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_build_structure_result` via `_config_sha256`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_structure_result` via `_config_sha256`
- direct call: `landscout.stages.structure_planning_regulation::_validate_result_self` via `_config_sha256`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_result_self` via `_config_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `config.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `_canonical_sha256` | `landscout.stages.structure_planning_regulation._canonical_sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_canonical_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `payload["topics"] = {<br>        topic: list(config.topics[topic]) for topic in sorted(config.topics)<br>    }` |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_document_lock`

**Purpose:** Implements `validate document lock` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _validate_document_lock(
    index: PlanningRegulationIndex,
    config: PlanningRegulationStructureConfig,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `config` | positional-or-keyword | `PlanningRegulationStructureConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `PlanningRegulationStructureError(<br>                f"Planning structure {label} differs from its document lock"<br>            )` under lexical guard `actual != expected`.
  - `PlanningRegulationStructureError(<br>            "body_start_page must reference a real indexed page"<br>        )` under lexical guard `config.document_layout.body_start_page not in indexed_page_set`.
  - `PlanningRegulationStructureError(<br>            "table_of_contents_pages reference nonexistent indexed pages: "<br>            f"{missing_toc_pages}"<br>        )` under lexical guard `missing_toc_pages`.
  - `PlanningRegulationStructureError(<br>            f"Regulation body page extraction status is ERROR: {failed_body_pages}"<br>        )` under lexical guard `failed_body_pages`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::validate_planning_regulation_structure_with_fragments` via `_validate_document_lock`
- value/type reference: `landscout.stages.structure_planning_regulation::validate_planning_regulation_structure_with_fragments` via `_validate_document_lock`
- direct call: `landscout.stages.structure_planning_regulation::structure_planning_regulation` via `_validate_document_lock`
- value/type reference: `landscout.stages.structure_planning_regulation::structure_planning_regulation` via `_validate_document_lock`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `validate_planning_regulation_index` | `landscout.stages.index_planning_regulation.validate_planning_regulation_index` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_positive_integer` | `landscout.stages.structure_planning_regulation._strict_positive_integer` |
| `index.pages["page_number"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `set(config.document_layout.table_of_contents_pages).difference` | `unresolved local/third-party receiver; no ownership inferred` |
| `index.pages.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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
        set(config.document_layout.table_of_contents_pages).difference(indexed_page_set)
    )
    if missing_toc_pages:
        raise PlanningRegulationStructureError(
            "table_of_contents_pages reference nonexistent indexed pages: "
            f"{missing_toc_pages}"
        )
    table_of_contents_pages = set(config.document_layout.table_of_contents_pages)
    failed_body_pages = [
        _strict_positive_integer(row["page_number"], "indexed page number")
        for row in index.pages.to_dict("records")
        if _strict_positive_integer(row["page_number"], "indexed page number")
        >= config.document_layout.body_start_page
        and row["page_number"] not in table_of_contents_pages
        and row["extraction_status"] == "ERROR"
    ]
    if failed_body_pages:
        raise PlanningRegulationStructureError(
            f"Regulation body page extraction status is ERROR: {failed_body_pages}"
        )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_compiled`

**Purpose:** Implements `compiled` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _compiled(patterns: Sequence[str]) -> tuple[re.Pattern[str], ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[re.Pattern[str], ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `patterns` | positional-or-keyword | `Sequence[str]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `tuple(re.compile(pattern) for pattern in patterns)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_line_records` via `_compiled`
- value/type reference: `landscout.stages.structure_planning_regulation::_line_records` via `_compiled`
- direct call: `landscout.stages.structure_planning_regulation::_heading_events` via `_compiled`
- value/type reference: `landscout.stages.structure_planning_regulation::_heading_events` via `_compiled`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `re.compile` | `re.compile` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _compiled(patterns: Sequence[str]) -> tuple[re.Pattern[str], ...]:
    return tuple(re.compile(pattern) for pattern in patterns)
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_matches_any`

**Purpose:** Implements `matches any` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _matches_any(value: str, patterns: Sequence[re.Pattern[str]]) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `str` | `required` |
| `patterns` | positional-or-keyword | `Sequence[re.Pattern[str]]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `any(pattern.fullmatch(value) is not None for pattern in patterns)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_retained_page_lines` via `_matches_any`
- value/type reference: `landscout.stages.structure_planning_regulation::_retained_page_lines` via `_matches_any`
- direct call: `landscout.stages.structure_planning_regulation::_heading_events` via `_matches_any`
- value/type reference: `landscout.stages.structure_planning_regulation::_heading_events` via `_matches_any`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `pattern.fullmatch` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _matches_any(value: str, patterns: Sequence[re.Pattern[str]]) -> bool:
    return any(pattern.fullmatch(value) is not None for pattern in patterns)
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_retained_page_lines`

**Purpose:** Implements `retained page lines` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _retained_page_lines(
    raw_text: str,
    headers: Sequence[re.Pattern[str]],
    footers: Sequence[re.Pattern[str]],
) -> list[tuple[int, str]]:
```

- Exact decorators: none.
- Declared return annotation: `list[tuple[int, str]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `raw_text` | positional-or-keyword | `str` | `required` |
| `headers` | positional-or-keyword | `Sequence[re.Pattern[str]]` | `required` |
| `footers` | positional-or-keyword | `Sequence[re.Pattern[str]]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `lines[start:end]`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_line_records` via `_retained_page_lines`
- value/type reference: `landscout.stages.structure_planning_regulation::_line_records` via `_retained_page_lines`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |
| `raw_text.splitlines` | `unresolved local/third-party receiver; no ownership inferred` |
| `next` | `unresolved local/third-party receiver; no ownership inferred` |
| `line.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `_matches_any` | `landscout.stages.structure_planning_regulation._matches_any` |
| `lines[first_nonempty][1].strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `lines[cursor][1].strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `lines[position][1].strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `lines[last_nonempty][1].strip` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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
    if first_nonempty is not None and _matches_any(
        lines[first_nonempty][1].strip(), headers
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
    if last_nonempty is not None and _matches_any(
        lines[last_nonempty][1].strip(), footers
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_line_records`

**Purpose:** Implements `line records` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _line_records(
    index: PlanningRegulationIndex,
    config: PlanningRegulationStructureConfig,
) -> list[_LineRecord]:
```

- Exact decorators: none.
- Declared return annotation: `list[_LineRecord]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `config` | positional-or-keyword | `PlanningRegulationStructureConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `records`
- Explicit raise paths:
  - `PlanningRegulationStructureError("Page raw text must be a string")` under lexical guard `not isinstance(raw_text, str)`.
  - `PlanningRegulationStructureError("Regulation contains no structural text")` under lexical guard `not records`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_build_sections` via `_line_records`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_sections` via `_line_records`
- import: `tests.unit.test_structure_planning_regulation::<module>` via `from landscout.stages.structure_planning_regulation import (
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
)`
- direct call: `tests.unit.test_structure_planning_regulation::test_positional_header_footer_filter_preserves_matching_body_lines` via `_line_records`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_positional_header_footer_filter_preserves_matching_body_lines` via `_line_records`
- direct call: `tests.unit.test_structure_planning_regulation::test_page_without_configured_header_or_footer_is_unchanged` via `_line_records`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_page_without_configured_header_or_footer_is_unchanged` via `_line_records`
- direct call: `tests.unit.test_structure_planning_regulation::test_blank_only_prefix_is_preserved_in_first_actual_section` via `_line_records`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_blank_only_prefix_is_preserved_in_first_actual_section` via `_line_records`
- direct call: `tests.unit.test_structure_planning_regulation::_structure_with_document_layout` via `_line_records`
- value/type reference: `tests.unit.test_structure_planning_regulation::_structure_with_document_layout` via `_line_records`
- direct call: `tests.unit.test_structure_planning_regulation::test_unique_zone_heading_and_nonheading_line_are_classified_deterministically` via `_line_records`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_unique_zone_heading_and_nonheading_line_are_classified_deterministically` via `_line_records`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_compiled` | `landscout.stages.structure_planning_regulation._compiled` |
| `index.pages.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_positive_integer` | `landscout.stages.structure_planning_regulation._strict_positive_integer` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |
| `retained.extend` | `unresolved local/third-party receiver; no ownership inferred` |
| `_retained_page_lines` | `landscout.stages.structure_planning_regulation._retained_page_lines` |
| `_LineRecord` | `landscout.stages.structure_planning_regulation._LineRecord` |
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `retained.extend(<br>            (page_number, line_number, raw_line)<br>            for line_number, raw_line in _retained_page_lines(<br>                raw_text, headers, footers<br>            )<br>        )` |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_source_record_payload`

**Purpose:** Implements `source record payload` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _source_record_payload(record: _LineRecord) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `record` | positional-or-keyword | `_LineRecord` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>        "record_id": record.record_id,<br>        "page_number": record.page_number,<br>        "page_line_number": record.page_line_number,<br>        "raw_text": record.raw,<br>    }`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_source_records_sha256` via `_source_record_payload`
- value/type reference: `landscout.stages.structure_planning_regulation::_source_records_sha256` via `_source_record_payload`

Outbound call expressions and conservative ownership:
- No calls.

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_source_records_sha256`

**Purpose:** Implements `source records sha256` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _source_records_sha256(records: Sequence[_LineRecord]) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `records` | positional-or-keyword | `Sequence[_LineRecord]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_sha256(<br>        {<br>            "domain": "landscout.planning_regulation.source_records",<br>            "section_hash_schema_version": SECTION_HASH_SCHEMA_VERSION,<br>            "records": [_source_record_payload(record) for record in records],<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_build_sections` via `_source_records_sha256`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_sections` via `_source_records_sha256`
- direct call: `landscout.stages.structure_planning_regulation::_validate_sections` via `_source_records_sha256`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_sections` via `_source_records_sha256`
- direct call: `landscout.stages.structure_planning_regulation::_build_structure_result` via `_source_records_sha256`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_structure_result` via `_source_records_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_sha256` | `landscout.stages.structure_planning_regulation._canonical_sha256` |
| `_source_record_payload` | `landscout.stages.structure_planning_regulation._source_record_payload` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_canonical_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_canonical_chapter_label`

**Purpose:** Implements `canonical chapter label` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _canonical_chapter_label(value: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_strict_string(label, "zone chapter label")`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_heading_events` via `_canonical_chapter_label`
- value/type reference: `landscout.stages.structure_planning_regulation::_heading_events` via `_canonical_chapter_label`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `re.sub` | `re.sub` |
| `_strict_string` | `landscout.stages.structure_planning_regulation._strict_string` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _canonical_chapter_label(value: str) -> str:
    label = re.sub(r"\s+", "", value)
    return _strict_string(label, "zone chapter label")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_classify_structural_heading`

**Purpose:** Implements `classify structural heading` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

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

- Exact decorators: none.
- Declared return annotation: `_StructuralHeadingMatch | None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `record` | positional-or-keyword | `_LineRecord` | `required` |
| `value` | positional-or-keyword | `str` | `required` |
| `pattern_groups` | positional-or-keyword | `Sequence[tuple[Literal['GENERAL', 'ZONE_CHAPTER', 'ARTICLE'], Sequence[re.Pattern[str]]]]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `matches[0] if matches else None`
- Explicit raise paths:
  - `PlanningRegulationStructureError(<br>            "Ambiguous structural heading at "<br>            f"{record.record_id}, page {record.page_number}, "<br>            f"line {record.page_line_number}: {diagnostics}"<br>        )` under lexical guard `len(matches) > 1`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_heading_events` via `_classify_structural_heading`
- value/type reference: `landscout.stages.structure_planning_regulation::_heading_events` via `_classify_structural_heading`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |
| `pattern.fullmatch` | `unresolved local/third-party receiver; no ownership inferred` |
| `matches.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `_StructuralHeadingMatch` | `landscout.stages.structure_planning_regulation._StructuralHeadingMatch` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `match.groupdict().items` | `unresolved local/third-party receiver; no ownership inferred` |
| `match.groupdict` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `matches.append(<br>                _StructuralHeadingMatch(<br>                    section_type=section_type,<br>                    pattern_index=pattern_index,<br>                    named_captures=tuple(match.groupdict().items()),<br>                )<br>            )` |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_heading_events`

**Purpose:** Implements `heading events` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _heading_events(
    records: Sequence[_LineRecord],
    config: PlanningRegulationStructureConfig,
) -> list[_HeadingEvent]:
```

- Exact decorators: none.
- Declared return annotation: `list[_HeadingEvent]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `records` | positional-or-keyword | `Sequence[_LineRecord]` | `required` |
| `config` | positional-or-keyword | `PlanningRegulationStructureConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `events`
- Explicit raise paths:
  - `PlanningRegulationStructureError(<br>            "No regulation body headings matched the configured grammar"<br>        )` under lexical guard `not events`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_build_sections` via `_heading_events`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_sections` via `_heading_events`
- import: `tests.unit.test_structure_planning_regulation::<module>` via `from landscout.stages.structure_planning_regulation import (
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
)`
- direct call: `tests.unit.test_structure_planning_regulation::test_unique_zone_heading_and_nonheading_line_are_classified_deterministically` via `_heading_events`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_unique_zone_heading_and_nonheading_line_are_classified_deterministically` via `_heading_events`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_compiled` | `landscout.stages.structure_planning_regulation._compiled` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `record.raw.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `_classify_structural_heading` | `landscout.stages.structure_planning_regulation._classify_structural_heading` |
| `dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `groups.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `_canonical_chapter_label` | `landscout.stages.structure_planning_regulation._canonical_chapter_label` |
| `records[cursor].raw.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `_matches_any` | `landscout.stages.structure_planning_regulation._matches_any` |
| `heading_lines.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `"\n".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `line.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `" ".join([title.strip(), *continuation_titles]).strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `" ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `title.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `events.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `_HeadingEvent` | `landscout.stages.structure_planning_regulation._HeadingEvent` |
| `_normalize_search_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `heading_lines.append(records[cursor].raw)`<br>`events.append(<br>            _HeadingEvent(<br>                record_position=position,<br>                section_type=section_type,<br>                heading_raw=heading_raw,<br>                heading_normalized=_normalize_search_text(heading_raw),<br>                zone_chapter_label=chapter_label,<br>                article_number_raw=article_number,<br>                article_title_raw=title,<br>            )<br>        )` |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_page_fragments`

**Purpose:** Implements `page fragments` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _page_fragments(records: Sequence[_LineRecord]) -> tuple[tuple[int, str], ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[tuple[int, str], ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `records` | positional-or-keyword | `Sequence[_LineRecord]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `tuple(fragments)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_build_sections` via `_page_fragments`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_sections` via `_page_fragments`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `fragments.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `"\n".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `lines.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `fragments.append((current_page, "\n".join(lines)))`<br>`lines.append(record.raw)` |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_contiguous_page_blocks`

**Purpose:** Implements `contiguous page blocks` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _contiguous_page_blocks(pages: Sequence[int]) -> tuple[tuple[int, ...], ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[tuple[int, ...], ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `pages` | positional-or-keyword | `Sequence[int]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `()`
  - `tuple(tuple(block) for block in blocks)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_section_starts` via `_contiguous_page_blocks`
- value/type reference: `landscout.stages.structure_planning_regulation::_section_starts` via `_contiguous_page_blocks`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `blocks[-1].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `blocks.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `blocks[-1].append(page)`<br>`blocks.append([page])` |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_section_starts`

**Purpose:** Implements `section starts` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _section_starts(
    records: Sequence[_LineRecord],
    events: Sequence[_HeadingEvent],
    config: PlanningRegulationStructureConfig,
) -> list[_SectionBoundary]:
```

- Exact decorators: none.
- Declared return annotation: `list[_SectionBoundary]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `records` | positional-or-keyword | `Sequence[_LineRecord]` | `required` |
| `events` | positional-or-keyword | `Sequence[_HeadingEvent]` | `required` |
| `config` | positional-or-keyword | `PlanningRegulationStructureConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `coalesced`
- Explicit raise paths:
  - `PlanningRegulationStructureError(<br>            "No regulation section boundary could be established"<br>        )` under lexical guard `not ordered`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_build_sections` via `_section_starts`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_sections` via `_section_starts`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_SectionBoundary` | `landscout.stages.structure_planning_regulation._SectionBoundary` |
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |
| `record_positions_by_page.setdefault(record.page_number, []).append` | `unresolved local/third-party receiver; no ownership inferred` |
| `record_positions_by_page.setdefault` | `unresolved local/third-party receiver; no ownership inferred` |
| `_contiguous_page_blocks` | `landscout.stages.structure_planning_regulation._contiguous_page_blocks` |
| `record_positions_by_page.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `min` | `unresolved local/third-party receiver; no ownership inferred` |
| `max` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `starts_by_position.values` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `records[shifted_position - 1].raw.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `compacted.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `compacted.values` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `record.raw.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `ordered.insert` | `unresolved local/third-party receiver; no ownership inferred` |
| `coalesced.append` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `record_positions_by_page.setdefault(record.page_number, []).append(position)`<br>`record_positions_by_page.setdefault(record.page_number, [])`<br>`starts_by_position[block_start] = _SectionBoundary(<br>            record_position=block_start,<br>            event=None,<br>            forced_table_of_contents=True,<br>        )`<br>`starts_by_position[block_end] = _SectionBoundary(<br>                record_position=block_end,<br>                event=None,<br>                forced_table_of_contents=False,<br>            )`<br>`ordered[boundary_index] = replace(<br>            boundary,<br>            record_position=shifted_position,<br>        )`<br>`compacted[boundary.record_position] = boundary`<br>`ordered.insert(<br>                0,<br>                _SectionBoundary(<br>                    record_position=0,<br>                    event=None,<br>                    forced_table_of_contents=False,<br>                ),<br>            )`<br>`ordered[0] = replace(first_boundary, record_position=0)`<br>`ordered[boundary_index + 1] = replace(<br>                    ordered[boundary_index + 1],<br>                    record_position=start,<br>                )`<br>`coalesced.append(boundary)` |
| Direct parameter mutation | None directly present. |

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
            ordered[boundary_index - 1].record_position if boundary_index > 0 else 0
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
            or (not existing.forced_table_of_contents and boundary.event is not None)
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_section_content_sha256`

**Purpose:** Implements `section content sha256` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _section_content_sha256(row: Mapping[str, object]) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `row` | positional-or-keyword | `Mapping[str, object]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_sha256(<br>        {<br>            "domain": "landscout.planning_regulation.section",<br>            "section_hash_schema_version": SECTION_HASH_SCHEMA_VERSION,<br>            "section": content,<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_build_sections` via `_section_content_sha256`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_sections` via `_section_content_sha256`
- direct call: `landscout.stages.structure_planning_regulation::_validate_sections` via `_section_content_sha256`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_sections` via `_section_content_sha256`
- import: `tests.unit.test_structure_planning_regulation::<module>` via `from landscout.stages.structure_planning_regulation import (
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
)`
- direct call: `tests.unit.test_structure_planning_regulation::test_coordinated_section_row_mutation_is_caught_by_outer_envelope` via `_section_content_sha256`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_coordinated_section_row_mutation_is_caught_by_outer_envelope` via `_section_content_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_sha256` | `landscout.stages.structure_planning_regulation._canonical_sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_canonical_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _section_content_sha256(row: Mapping[str, object]) -> str:
    content = {
        column: row[column]
        for column in SECTION_COLUMNS
        if column != "section_content_sha256"
    }
    return _canonical_sha256(
        {
            "domain": "landscout.planning_regulation.section",
            "section_hash_schema_version": SECTION_HASH_SCHEMA_VERSION,
            "section": content,
        }
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_build_sections`

**Purpose:** Implements `build sections` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _build_sections(
    index: PlanningRegulationIndex,
    config: PlanningRegulationStructureConfig,
) -> tuple[pd.DataFrame, tuple[_SectionBuild, ...], tuple[_LineRecord, ...]]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[pd.DataFrame, tuple[_SectionBuild, ...], tuple[_LineRecord, ...]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `config` | positional-or-keyword | `PlanningRegulationStructureConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `frame, tuple(builds), tuple(records)`
- Explicit raise paths:
  - `PlanningRegulationStructureError(<br>                        "Zone article has no preceding zone chapter"<br>                    )` under lexical guard `event is None`.
  - `PlanningRegulationStructureError(<br>                        "Zone article label differs from its active chapter"<br>                    )` under lexical guard `event is None`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_build_structure_result` via `_build_sections`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_structure_result` via `_build_sections`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_line_records` | `landscout.stages.structure_planning_regulation._line_records` |
| `_heading_events` | `landscout.stages.structure_planning_regulation._heading_events` |
| `_section_starts` | `landscout.stages.structure_planning_regulation._section_starts` |
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `next` | `unresolved local/third-party receiver; no ownership inferred` |
| `record.raw.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `_normalize_search_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |
| `event.zone_chapter_label.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `current_chapter_label.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `_page_fragments` | `landscout.stages.structure_planning_regulation._page_fragments` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `"\n".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `_source_records_sha256` | `landscout.stages.structure_planning_regulation._source_records_sha256` |
| `_section_content_sha256` | `landscout.stages.structure_planning_regulation._section_content_sha256` |
| `builds.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `_SectionBuild` | `landscout.stages.structure_planning_regulation._SectionBuild` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `frame["start_page"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["end_page"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["source_record_count"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["character_count"].astype` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_source_records_sha256`<br>`_section_content_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `row["section_content_sha256"] = _section_content_sha256(row)`<br>`builds.append(_SectionBuild(row=row, page_fragments=fragments))`<br>`frame["start_page"] = frame["start_page"].astype("int64")`<br>`frame["end_page"] = frame["end_page"].astype("int64")`<br>`frame["source_record_count"] = frame["source_record_count"].astype("int64")`<br>`frame["character_count"] = frame["character_count"].astype("int64")` |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_source_label_values`

**Purpose:** Implements `validate source label values` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _validate_source_label_values(series: pd.Series, label: str) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `series` | positional-or-keyword | `pd.Series` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_validated_zoning_inputs` via `_validate_source_label_values`
- value/type reference: `landscout.stages.structure_planning_regulation::_validated_zoning_inputs` via `_validate_source_label_values`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `series.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_string` | `landscout.stages.structure_planning_regulation._strict_string` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_source_label_values(series: pd.Series, label: str) -> None:
    for value in series.tolist():
        _strict_string(value, label)
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validated_zoning_inputs`

**Purpose:** Implements `validated zoning inputs` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _validated_zoning_inputs(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
    intersections: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[pd.DataFrame, pd.DataFrame]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `zones` | positional-or-keyword | `pd.DataFrame` | `required` |
| `intersections` | positional-or-keyword | `pd.DataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `zone_copy, relation_copy`
- Explicit raise paths:
  - `PlanningRegulationStructureError(<br>            "Zones and zoning intersections must be DataFrames"<br>        )` under lexical guard `not isinstance(zones, pd.DataFrame) or not isinstance(<br>        intersections, pd.DataFrame<br>    )`.
  - `PlanningRegulationStructureError(<br>            f"Zone catalog is missing required columns: {missing_zones}"<br>        )` under lexical guard `missing_zones`.
  - `PlanningRegulationStructureError(<br>            f"Zoning intersections are missing required columns: {missing_relations}"<br>        )` under lexical guard `missing_relations`.
  - `PlanningRegulationStructureError("Planning zone IDs must be unique")` under lexical guard `zone_copy["planning_zone_id"].duplicated().any()`.
  - `PlanningRegulationStructureError("Source zone IDs must be unique")` under lexical guard `zone_copy["source_zone_id"].duplicated().any()`.
  - `PlanningRegulationStructureError(<br>            "Zone document lineage differs from index"<br>        )` under lexical guard `not zone_copy["source_document_id"].eq(index.document_id).all()`.
  - `PlanningRegulationStructureError(<br>            "Zone archive lineage differs from index"<br>        )` under lexical guard `not zone_copy["source_archive_sha256"].eq(index.archive_sha256).all()`.
  - `PlanningRegulationStructureError(<br>            "Parcel/zone intersection pairs must be unique"<br>        )` under lexical guard `relation_copy.duplicated(["parcel_id", "planning_zone_id"]).any()`.
  - `PlanningRegulationStructureError(<br>            "Zoning intersections reference an unknown planning zone"<br>        )` under lexical guard `not set(relation_copy["planning_zone_id"].tolist()).issubset(known)`.
  - `PlanningRegulationStructureError(<br>            "Intersection zone labels differ from the zone catalog"<br>        )` under lexical guard `not expected_labels.eq(relation_copy["zone_label_raw"]).all()`.
  - `PlanningRegulationStructureError(<br>            "Intersection source-zone IDs differ from the zone catalog"<br>        )` under lexical guard `not expected_source_ids.eq(relation_copy["source_zone_id"]).all()`.
  - `PlanningRegulationStructureError(<br>            "Intersection document lineage differs from index"<br>        )` under lexical guard `not relation_copy["source_document_id"].eq(index.document_id).all()`.
  - `PlanningRegulationStructureError(<br>            "Intersection archive lineage differs from index"<br>        )` under lexical guard `not relation_copy["source_archive_sha256"].eq(index.archive_sha256).all()`.
  - `PlanningRegulationStructureError("Zoning relation type is invalid")` under lexical guard `not set(relation_copy["relation_type"].tolist()).issubset(allowed_relations)`.
  - `PlanningRegulationStructureError("Intersection areas must be numeric")` under lexical guard `isinstance(value, bool) or not isinstance(value, Real)`.
  - `PlanningRegulationStructureError(<br>                "Intersection areas must be finite"<br>            )`.
  - `PlanningRegulationStructureError(<br>                "Intersection areas must be finite and non-negative"<br>            )` under lexical guard `not math.isfinite(numeric) or numeric < 0`.
  - `PlanningRegulationStructureError(<br>            "Positive zoning relations must be AREA_OVERLAP"<br>        )` under lexical guard `not relation_copy.loc[positive, "relation_type"].eq("AREA_OVERLAP").all()`.
  - `PlanningRegulationStructureError(<br>            "Zero-area zoning relations must be TOUCH_ONLY"<br>        )` under lexical guard `not relation_copy.loc[~positive, "relation_type"].eq("TOUCH_ONLY").all()`.
  - `PlanningRegulationStructureError(<br>                    f"{upper_column} must be numeric"<br>                )` under lexical guard `isinstance(upper, bool) or not isinstance(upper, Real)`.
  - `PlanningRegulationStructureError(<br>                    f"{upper_column} must be finite"<br>                )`.
  - `PlanningRegulationStructureError(<br>                    f"{upper_column} must be finite and non-negative"<br>                )` under lexical guard `not math.isfinite(numeric_upper) or numeric_upper < 0`.
  - `PlanningRegulationStructureError(<br>                    f"Intersection area exceeds {upper_column}"<br>                )` under lexical guard `area - numeric_upper > technical_overlay_tolerance(numeric_upper)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::validate_planning_regulation_structure_with_fragments` via `_validated_zoning_inputs`
- value/type reference: `landscout.stages.structure_planning_regulation::validate_planning_regulation_structure_with_fragments` via `_validated_zoning_inputs`
- direct call: `landscout.stages.structure_planning_regulation::structure_planning_regulation` via `_validated_zoning_inputs`
- value/type reference: `landscout.stages.structure_planning_regulation::structure_planning_regulation` via `_validated_zoning_inputs`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `zone_required.difference` | `unresolved local/third-party receiver; no ownership inferred` |
| `relation_required.difference` | `unresolved local/third-party receiver; no ownership inferred` |
| `zones.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `intersections.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_source_label_values` | `landscout.stages.structure_planning_regulation._validate_source_label_values` |
| `zone_copy["planning_zone_id"].duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `zone_copy["planning_zone_id"].duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `zone_copy["source_zone_id"].duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `zone_copy["source_zone_id"].duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `zone_copy["source_document_id"].eq(index.document_id).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `zone_copy["source_document_id"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `zone_copy["source_archive_sha256"].eq(index.archive_sha256).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `zone_copy["source_archive_sha256"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `relation_copy.duplicated(["parcel_id", "planning_zone_id"]).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `relation_copy.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `zone_copy["planning_zone_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `set(relation_copy["planning_zone_id"].tolist()).issubset` | `unresolved local/third-party receiver; no ownership inferred` |
| `relation_copy["planning_zone_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `zone_copy.set_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `relation_copy["planning_zone_id"].map` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected_labels.eq(relation_copy["zone_label_raw"]).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected_labels.eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected_source_ids.eq(relation_copy["source_zone_id"]).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected_source_ids.eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `relation_copy["source_document_id"].eq(index.document_id).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `relation_copy["source_document_id"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `relation_copy["source_archive_sha256"].eq(index.archive_sha256).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `relation_copy["source_archive_sha256"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `set(relation_copy["relation_type"].tolist()).issubset` | `unresolved local/third-party receiver; no ownership inferred` |
| `relation_copy["relation_type"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `relation_copy["intersection_area_m2"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `math.isfinite` | `math.isfinite` |
| `metrics.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.Series` | `pandas.Series` |
| `relation_copy["intersection_area_m2"].gt` | `unresolved local/third-party receiver; no ownership inferred` |
| `relation_copy.loc[positive, "relation_type"].eq("AREA_OVERLAP").all` | `unresolved local/third-party receiver; no ownership inferred` |
| `relation_copy.loc[positive, "relation_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `relation_copy.loc[~positive, "relation_type"].eq("TOUCH_ONLY").all` | `unresolved local/third-party receiver; no ownership inferred` |
| `relation_copy.loc[~positive, "relation_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `zip` | `unresolved local/third-party receiver; no ownership inferred` |
| `relation_copy[upper_column].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `technical_overlay_tolerance` | `landscout.stages.planning_overlay.technical_overlay_tolerance` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `zone_copy["source_archive_sha256"].eq(index.archive_sha256).all`<br>`zone_copy["source_archive_sha256"].eq`<br>`relation_copy["source_archive_sha256"].eq(index.archive_sha256).all`<br>`relation_copy["source_archive_sha256"].eq` |
| CRS/geometry/spatial calculation | `technical_overlay_tolerance` |
| External process/environment | None directly present. |
| In-memory mutation | `metrics.append(numeric)`<br>`relation_copy["intersection_area_m2"] = pd.Series(<br>        metrics, index=relation_copy.index, dtype="float64"<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validated_zoning_inputs(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
    intersections: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    if not isinstance(zones, pd.DataFrame) or not isinstance(
        intersections, pd.DataFrame
    ):
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
        raise PlanningRegulationStructureError(
            "Zone document lineage differs from index"
        )
    if not zone_copy["source_archive_sha256"].eq(index.archive_sha256).all():
        raise PlanningRegulationStructureError(
            "Zone archive lineage differs from index"
        )
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
            raise PlanningRegulationStructureError("Intersection areas must be numeric")
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
        raise PlanningRegulationStructureError(
            "Positive zoning relations must be AREA_OVERLAP"
        )
    if not relation_copy.loc[~positive, "relation_type"].eq("TOUCH_ONLY").all():
        raise PlanningRegulationStructureError(
            "Zero-area zoning relations must be TOUCH_ONLY"
        )
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_input_frame_sha256`

**Purpose:** Implements `input frame sha256` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _input_frame_sha256(
    domain: str,
    frame: pd.DataFrame,
    columns: Sequence[str],
) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `domain` | positional-or-keyword | `str` | `required` |
| `frame` | positional-or-keyword | `pd.DataFrame` | `required` |
| `columns` | positional-or-keyword | `Sequence[str]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_sha256(<br>        {<br>            "domain": domain,<br>            "columns": list(columns),<br>            "rows": frame.loc[:, columns].to_dict("records"),<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_build_structure_result` via `_input_frame_sha256`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_structure_result` via `_input_frame_sha256`
- direct call: `landscout.stages.structure_planning_regulation::_validate_result_self` via `_input_frame_sha256`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_result_self` via `_input_frame_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_sha256` | `landscout.stages.structure_planning_regulation._canonical_sha256` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.loc[:, columns].to_dict` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_canonical_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_intersection_hash_columns`

**Purpose:** Implements `intersection hash columns` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _intersection_hash_columns(frame: pd.DataFrame) -> tuple[str, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[str, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `pd.DataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_REQUIRED_INTERSECTION_INPUT_COLUMNS + tuple(<br>        column<br>        for column in _OPTIONAL_INTERSECTION_INPUT_COLUMNS<br>        if column in frame.columns<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_build_structure_result` via `_intersection_hash_columns`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_structure_result` via `_intersection_hash_columns`
- direct call: `landscout.stages.structure_planning_regulation::_validate_result_self` via `_intersection_hash_columns`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_result_self` via `_intersection_hash_columns`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_resolved_alias`

**Purpose:** Implements `resolved alias` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _resolved_alias(label: str, aliases: Mapping[str, str]) -> str | None:
```

- Exact decorators: none.
- Declared return annotation: `str | None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `label` | positional-or-keyword | `str` | `required` |
| `aliases` | positional-or-keyword | `Mapping[str, str]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `None`
  - `current`
- Explicit raise paths:
  - `PlanningRegulationStructureError("Zone alias cycle is invalid")` under lexical guard `current in visited`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_build_zone_mapping` via `_resolved_alias`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_zone_mapping` via `_resolved_alias`
- direct call: `landscout.stages.structure_planning_regulation::_validate_zone_mapping` via `_resolved_alias`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_zone_mapping` via `_resolved_alias`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |
| `visited.add` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `visited.add(current)` |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_dominant_counts`

**Purpose:** Implements `dominant counts` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _dominant_counts(intersections: pd.DataFrame) -> Counter[str]:
```

- Exact decorators: none.
- Declared return annotation: `Counter[str]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `intersections` | positional-or-keyword | `pd.DataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `Counter()`
  - `Counter(selected["zone_label_raw"].tolist())`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_build_zone_mapping` via `_dominant_counts`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_zone_mapping` via `_dominant_counts`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `intersections.loc[<br>        intersections["intersection_area_m2"].gt(0),<br>        ["parcel_id", "planning_zone_id", "zone_label_raw", "intersection_area_m2"],<br>    ].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `intersections["intersection_area_m2"].gt` | `unresolved local/third-party receiver; no ownership inferred` |
| `Counter` | `collections.Counter` |
| `positive.sort_values` | `unresolved local/third-party receiver; no ownership inferred` |
| `positive.drop_duplicates` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected["zone_label_raw"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_build_zone_mapping`

**Purpose:** Implements `build zone mapping` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

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

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `config` | positional-or-keyword | `PlanningRegulationStructureConfig` | `required` |
| `sections` | positional-or-keyword | `pd.DataFrame` | `required` |
| `zones` | positional-or-keyword | `pd.DataFrame` | `required` |
| `intersections` | positional-or-keyword | `pd.DataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `frame`
- Explicit raise paths:
  - `PlanningRegulationStructureError(<br>            "Dominant candidate zone labels lack an exact configured chapter mapping: "<br>            f"{unresolved_dominant}"<br>        )` under lexical guard `unresolved_dominant`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_build_structure_result` via `_build_zone_mapping`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_structure_result` via `_build_zone_mapping`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `sections["section_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `chapters.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_string` | `landscout.stages.structure_planning_regulation._strict_string` |
| `chapters_by_label.setdefault(label, []).append` | `unresolved local/third-party receiver; no ownership inferred` |
| `chapters_by_label.setdefault` | `unresolved local/third-party receiver; no ownership inferred` |
| `Counter` | `collections.Counter` |
| `zones["zone_label_raw"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `intersections.groupby("zone_label_raw", sort=False)["parcel_id"]<br>        .nunique()<br>        .to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `intersections.groupby("zone_label_raw", sort=False)["parcel_id"]<br>        .nunique` | `unresolved local/third-party receiver; no ownership inferred` |
| `intersections.groupby` | `unresolved local/third-party receiver; no ownership inferred` |
| `intersections["zone_label_raw"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `_dominant_counts` | `landscout.stages.structure_planning_regulation._dominant_counts` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `chapters_by_label.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `_resolved_alias` | `landscout.stages.structure_planning_regulation._resolved_alias` |
| `rows.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcel_counts.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `frame[column].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.loc[<br>        frame["dominant_candidate_count"].gt(0)<br>        & ~frame["mapping_status"].isin({"EXACT", "CONFIG_ALIAS"}),<br>        "source_zone_label_raw",<br>    ].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["dominant_candidate_count"].gt` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["mapping_status"].isin` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `chapters_by_label.setdefault(label, []).append(row["section_id"])`<br>`chapters_by_label.setdefault(label, [])`<br>`rows.append(<br>            {<br>                "source_zone_label_raw": label,<br>                "resolved_zone_chapter_label": resolved,<br>                "mapping_status": status,<br>                "mapping_method": method,<br>                "matched_section_id": matched,<br>                "zone_polygon_count": zone_counts[label],<br>                "candidate_parcel_count": int(parcel_counts.get(label, 0)),<br>                "candidate_intersection_count": intersection_counts[label],<br>                "dominant_candidate_count": dominant_counts[label],<br>                "document_id": index.document_id,<br>                "archive_sha256": index.archive_sha256,<br>                "pdf_sha256": index.pdf_sha256,<br>                "index_content_sha256": index.index_content_sha256,<br>                "structure_profile": config.structure_profile,<br>            }<br>        )`<br>`frame[column] = frame[column].astype("int64")` |
| Direct parameter mutation | None directly present. |

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
    parcel_counts = (
        intersections.groupby("zone_label_raw", sort=False)["parcel_id"]
        .nunique()
        .to_dict()
    )
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_is_token_character`

**Purpose:** Implements `is token character` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _is_token_character(value: str) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `value.isalnum() or value == "_"`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_literal_topic_matches` via `_is_token_character`
- value/type reference: `landscout.stages.structure_planning_regulation::_literal_topic_matches` via `_is_token_character`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `value.isalnum` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _is_token_character(value: str) -> bool:
    return value.isalnum() or value == "_"
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_literal_topic_matches`

**Purpose:** Implements `literal topic matches` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _literal_topic_matches(
    normalized_text: str,
    terms: Sequence[str],
) -> tuple[_TopicMatch, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[_TopicMatch, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `normalized_text` | positional-or-keyword | `str` | `required` |
| `terms` | positional-or-keyword | `Sequence[str]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `tuple(<br>        sorted(<br>            selected,<br>            key=lambda item: (item.normalized_start, item.term_index),<br>        )<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_build_topic_evidence` via `_literal_topic_matches`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_topic_evidence` via `_literal_topic_matches`
- direct call: `landscout.stages.structure_planning_regulation::_validate_topic_evidence` via `_literal_topic_matches`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_topic_evidence` via `_literal_topic_matches`
- import: `tests.unit.test_structure_planning_regulation::<module>` via `from landscout.stages.structure_planning_regulation import (
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
)`
- direct call: `tests.unit.test_structure_planning_regulation::test_equal_length_overlap_uses_configured_term_order_as_tie_break` via `_literal_topic_matches`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_equal_length_overlap_uses_configured_term_order_as_tie_break` via `_literal_topic_matches`
- direct call: `tests.unit.test_structure_planning_regulation::test_token_boundary_and_longest_match_policy` via `_literal_topic_matches`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_token_boundary_and_longest_match_policy` via `_literal_topic_matches`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |
| `_normalize_search_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized_text.find` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `_is_token_character` | `landscout.stages.structure_planning_regulation._is_token_character` |
| `candidates.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `_TopicMatch` | `landscout.stages.structure_planning_regulation._TopicMatch` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `candidates.append(<br>                    _TopicMatch(<br>                        term_index=term_index,<br>                        search_term=search_term,<br>                        normalized_term=normalized_term,<br>                        normalized_start=start,<br>                        normalized_end=end,<br>                    )<br>                )`<br>`selected.append(candidate)` |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_evidence_scope`

**Purpose:** Implements `evidence scope` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _evidence_scope(section_type: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `section_type` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `"GENERAL_RULE"`
  - `"ZONE_SPECIFIC_RULE"`
  - `"OTHER_TEXT"`
- Explicit raise paths:
  - `PlanningRegulationStructureError(<br>        "Topic evidence references an unsupported section type"<br>    )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_build_topic_evidence` via `_evidence_scope`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_topic_evidence` via `_evidence_scope`
- direct call: `landscout.stages.structure_planning_regulation::_validate_topic_evidence` via `_evidence_scope`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_topic_evidence` via `_evidence_scope`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_build_topic_evidence`

**Purpose:** Implements `build topic evidence` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _build_topic_evidence(
    index: PlanningRegulationIndex,
    config: PlanningRegulationStructureConfig,
    builds: Sequence[_SectionBuild],
) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `config` | positional-or-keyword | `PlanningRegulationStructureConfig` | `required` |
| `builds` | positional-or-keyword | `Sequence[_SectionBuild]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `pd.DataFrame(<br>            {<br>                column: pd.Series(<br>                    dtype=(<br>                        "int64"<br>                        if column<br>                        in {<br>                            "page_number",<br>                            "occurrence_count",<br>                            "first_match_normalized_start",<br>                            "first_match_normalized_end",<br>                            "first_match_raw_start",<br>                            "first_match_raw_end",<br>                        }<br>                        else "object"<br>                    )<br>                )<br>                for column in TOPIC_EVIDENCE_COLUMNS<br>            }<br>        )`
  - `frame`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_build_structure_result` via `_build_topic_evidence`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_structure_result` via `_build_topic_evidence`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `_normalize_search_text_with_mapping` | `unresolved local/third-party receiver; no ownership inferred` |
| `_literal_topic_matches` | `landscout.stages.structure_planning_regulation._literal_topic_matches` |
| `by_term.setdefault(match.term_index, []).append` | `unresolved local/third-party receiver; no ownership inferred` |
| `by_term.setdefault` | `unresolved local/third-party receiver; no ownership inferred` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `by_term.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `max` | `unresolved local/third-party receiver; no ownership inferred` |
| `min` | `unresolved local/third-party receiver; no ownership inferred` |
| `rows.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `_evidence_scope` | `landscout.stages.structure_planning_regulation._evidence_scope` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `_raw_context` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `pd.Series` | `pandas.Series` |
| `frame[column].astype` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `by_term.setdefault(match.term_index, []).append(match)`<br>`by_term.setdefault(match.term_index, [])`<br>`rows.append(<br>                        {<br>                            "topic": topic,<br>                            "search_term": first.search_term,<br>                            "normalized_search_term": first.normalized_term,<br>                            "match_policy": config.topic_match_policy.identifier,<br>                            "section_id": section["section_id"],<br>                            "evidence_scope": _evidence_scope(<br>                                str(section["section_type"])<br>                            ),<br>                            "zone_chapter_label": zone_label,<br>                            "article_number_raw": section["article_number_raw"],<br>                            "page_number": page_number,<br>                            "occurrence_count": len(retained),<br>                            "first_match_normalized_start": first.normalized_start,<br>                            "first_match_normalized_end": first.normalized_end,<br>                            "first_match_raw_start": raw_start,<br>                            "first_match_raw_end": raw_end,<br>                            "raw_context": _raw_context(<br>                                raw_fragment, spans, context_start, context_end<br>                            ),<br>                            "normalized_context": normalized[context_start:context_end],<br>                            "document_id": index.document_id,<br>                            "archive_sha256": index.archive_sha256,<br>                            "pdf_sha256": index.pdf_sha256,<br>                            "index_content_sha256": index.index_content_sha256,<br>                            "structure_profile": config.structure_profile,<br>                        }<br>                    )`<br>`frame[column] = frame[column].astype("int64")` |
| Direct parameter mutation | None directly present. |

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
                    context_start = max(0, first.normalized_start - context_characters)
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_frame_hash`

**Purpose:** Implements `frame hash` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _frame_hash(
    domain: str,
    result: PlanningRegulationStructureResult,
    frame: pd.DataFrame,
    columns: Sequence[str],
) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `domain` | positional-or-keyword | `str` | `required` |
| `result` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |
| `frame` | positional-or-keyword | `pd.DataFrame` | `required` |
| `columns` | positional-or-keyword | `Sequence[str]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_sha256(<br>        {<br>            "domain": domain,<br>            "section_hash_schema_version": result.section_hash_schema_version,<br>            "document_id": result.document_id,<br>            "archive_sha256": result.archive_sha256,<br>            "pdf_sha256": result.pdf_sha256,<br>            "index_content_sha256": result.index_content_sha256,<br>            "structure_profile": result.structure_profile,<br>            "structure_config_schema_version": result.structure_config_schema_version,<br>            "structure_config_sha256": result.structure_config_sha256,<br>            "zones_content_sha256": result.zones_content_sha256,<br>            "zoning_intersection_hash_columns": list(<br>                result.zoning_intersection_hash_columns<br>            ),<br>            "zoning_intersections_content_sha256": (<br>                result.zoning_intersections_content_sha256<br>            ),<br>            "source_records_sha256": result.source_records_sha256,<br>            "rows": frame.loc[:, columns].to_dict("records"),<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_result_with_hashes` via `_frame_hash`
- value/type reference: `landscout.stages.structure_planning_regulation::_result_with_hashes` via `_frame_hash`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_sha256` | `landscout.stages.structure_planning_regulation._canonical_sha256` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.loc[:, columns].to_dict` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_canonical_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_structure_result_content_sha256`

**Purpose:** Implements `structure result content sha256` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _structure_result_content_sha256(
    result: PlanningRegulationStructureResult,
) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_sha256(<br>        {<br>            "domain": "landscout.planning_regulation.structure_result",<br>            "document_id": result.document_id,<br>            "archive_sha256": result.archive_sha256,<br>            "pdf_sha256": result.pdf_sha256,<br>            "index_content_sha256": result.index_content_sha256,<br>            "structure_profile": result.structure_profile,<br>            "structure_config_schema_version": result.structure_config_schema_version,<br>            "structure_config_sha256": result.structure_config_sha256,<br>            "zones_content_sha256": result.zones_content_sha256,<br>            "zoning_intersection_hash_columns": list(<br>                result.zoning_intersection_hash_columns<br>            ),<br>            "zoning_intersections_content_sha256": (<br>                result.zoning_intersections_content_sha256<br>            ),<br>            "source_records_sha256": result.source_records_sha256,<br>            "section_hash_schema_version": result.section_hash_schema_version,<br>            "sections_content_sha256": result.sections_content_sha256,<br>            "zone_map_content_sha256": result.zone_map_content_sha256,<br>            "topic_evidence_content_sha256": result.topic_evidence_content_sha256,<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_result_with_hashes` via `_structure_result_content_sha256`
- value/type reference: `landscout.stages.structure_planning_regulation::_result_with_hashes` via `_structure_result_content_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_sha256` | `landscout.stages.structure_planning_regulation._canonical_sha256` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_canonical_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_result_with_hashes`

**Purpose:** Implements `result with hashes` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _result_with_hashes(
    result: PlanningRegulationStructureResult,
) -> PlanningRegulationStructureResult:
```

- Exact decorators: none.
- Declared return annotation: `PlanningRegulationStructureResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `replace(<br>        component_result,<br>        structure_result_content_sha256=_structure_result_content_sha256(<br>            component_result<br>        ),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_build_structure_result` via `_result_with_hashes`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_structure_result` via `_result_with_hashes`
- direct call: `landscout.stages.structure_planning_regulation::_validate_result_self` via `_result_with_hashes`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_result_self` via `_result_with_hashes`
- import: `tests.unit.test_interpret_bess_zoning::<module>` via `from landscout.stages.structure_planning_regulation import (
    _result_with_hashes as _structure_with_hashes,
)`
- direct call: `tests.unit.test_interpret_bess_zoning::test_unmapped_dominant_zone_is_rejected` via `_structure_with_hashes`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_unmapped_dominant_zone_is_rejected` via `_structure_with_hashes`
- direct call: `tests.unit.test_interpret_bess_zoning::test_structure_config_and_hierarchy_changes_are_rejected` via `_structure_with_hashes`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_structure_config_and_hierarchy_changes_are_rejected` via `_structure_with_hashes`
- direct call: `tests.unit.test_interpret_bess_zoning::test_factual_zone_mapping_counts_are_recomputed` via `_structure_with_hashes`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_factual_zone_mapping_counts_are_recomputed` via `_structure_with_hashes`
- import: `tests.unit.test_structure_planning_regulation::<module>` via `from landscout.stages.structure_planning_regulation import (
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
)`
- direct call: `tests.unit.test_structure_planning_regulation::test_coordinated_topic_evidence_and_hash_mutation_is_rebuilt_and_rejected` via `_result_with_hashes`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_coordinated_topic_evidence_and_hash_mutation_is_rebuilt_and_rejected` via `_result_with_hashes`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `replace` | `dataclasses.replace` |
| `_frame_hash` | `landscout.stages.structure_planning_regulation._frame_hash` |
| `_structure_result_content_sha256` | `landscout.stages.structure_planning_regulation._structure_result_content_sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_frame_hash`<br>`_structure_result_content_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_page_tuple`

**Purpose:** Implements `page tuple` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _page_tuple(value: object) -> tuple[int, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[int, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `tuple(<br>        _strict_positive_integer(item, "section page number") for item in value<br>    )`
- Explicit raise paths:
  - `PlanningRegulationStructureError(<br>            "Section page_numbers must be a sequence"<br>        )` under lexical guard `not isinstance(value, (tuple, list, np.ndarray))`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_validate_sections` via `_page_tuple`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_sections` via `_page_tuple`
- direct call: `landscout.stages.structure_planning_regulation::_validate_topic_evidence` via `_page_tuple`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_topic_evidence` via `_page_tuple`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_positive_integer` | `landscout.stages.structure_planning_regulation._strict_positive_integer` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _page_tuple(value: object) -> tuple[int, ...]:
    if not isinstance(value, (tuple, list, np.ndarray)):
        raise PlanningRegulationStructureError(
            "Section page_numbers must be a sequence"
        )
    return tuple(
        _strict_positive_integer(item, "section page number") for item in value
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_sections`

**Purpose:** Implements `validate sections` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _validate_sections(
    index: PlanningRegulationIndex,
    result: PlanningRegulationStructureResult,
    records: Sequence[_LineRecord],
    config: PlanningRegulationStructureConfig,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `result` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |
| `records` | positional-or-keyword | `Sequence[_LineRecord]` | `required` |
| `config` | positional-or-keyword | `PlanningRegulationStructureConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `PlanningRegulationStructureError("Section schema is not deterministic")` under lexical guard `not isinstance(frame, pd.DataFrame) or tuple(frame.columns) != SECTION_COLUMNS`.
  - `PlanningRegulationStructureError("Regulation sections must not be empty")` under lexical guard `frame.empty`.
  - `PlanningRegulationStructureError("Retained source-record hash differs")` under lexical guard `result.source_records_sha256 != _source_records_sha256(records)`.
  - `PlanningRegulationStructureError(<br>                "Section IDs must be deterministic and sequential"<br>            )` under lexical guard `section_id != f"SECTION-{sequence:04d}"`.
  - `PlanningRegulationStructureError("Section type is invalid")` under lexical guard `section_type not in _SECTION_TYPES`.
  - `PlanningRegulationStructureError(<br>                    f"Section {column} must be a string"<br>                )` under lexical guard `not isinstance(row[column], str)`.
  - `PlanningRegulationStructureError(<br>                "Section heading normalization differs"<br>            )` under lexical guard `row["heading_normalized"] != _normalize_search_text(row["heading_raw"])`.
  - `PlanningRegulationStructureError("Section text normalization differs")` under lexical guard `row["normalized_text"] != _normalize_search_text(row["raw_text"])`.
  - `PlanningRegulationStructureError("Section character count differs")` under lexical guard `_strict_nonnegative_integer(<br>            row["character_count"], "character count"<br>        ) != len(row["raw_text"])`.
  - `PlanningRegulationStructureError("Section record boundary is unknown")` under lexical guard `start_record_id not in record_position<br>            or end_record_id not in record_position`.
  - `PlanningRegulationStructureError(<br>                "Sections do not preserve the exact source-record partition"<br>            )` under lexical guard `start_record != expected_record_start or end_record < start_record`.
  - `PlanningRegulationStructureError(<br>                "Only an explicit TOC OTHER section may contain blank-only text"<br>            )` under lexical guard `not row["raw_text"].strip() and not blank_toc_other`.
  - `PlanningRegulationStructureError(<br>                "Every nonblank section must retain a factual heading"<br>            )` under lexical guard `not row["heading_raw"].strip() and not blank_toc_other`.
  - `PlanningRegulationStructureError(<br>                "Section source-record count differs"<br>            )` under lexical guard `_strict_positive_integer(<br>            row["source_record_count"], "source record count"<br>        ) != len(segment)`.
  - `PlanningRegulationStructureError("Section source-record hash differs")` under lexical guard `_validated_sha256(<br>            row["source_records_sha256"], "section source-record SHA256"<br>        ) != _source_records_sha256(segment)`.
  - `PlanningRegulationStructureError(<br>                "Section raw text differs from its retained source records"<br>            )` under lexical guard `row["raw_text"] != "\n".join(record.raw for record in segment)`.
  - `PlanningRegulationStructureError(<br>                "Section page references are invalid"<br>            )` under lexical guard `not pages<br>            or any(right <= left for left, right in pairwise(pages))<br>            or not set(pages).issubset(known_pages)<br>            or pages != expected_pages`.
  - `PlanningRegulationStructureError(<br>                "Section page range is invalid or unordered"<br>            )` under lexical guard `start != pages[0] or end != pages[-1] or end < start`.
  - `PlanningRegulationStructureError("Section lineage differs")` under lexical guard `row[column] != actual`.
  - `PlanningRegulationStructureError("Section content hash differs")` under lexical guard `_validated_sha256(row["section_content_sha256"], "section content SHA256")<br>            != expected_hash`.
  - `PlanningRegulationStructureError("Article zone label is missing")` under lexical guard `section_type == "ARTICLE"`.
  - `PlanningRegulationStructureError("Article parent is missing")` under lexical guard `section_type == "ARTICLE"`.
  - `PlanningRegulationStructureError(<br>                    "General section cannot have a zone label or parent"<br>                )` under lexical guard `section_type == "ARTICLE"`.
  - `PlanningRegulationStructureError(<br>                    "Zone chapter or OTHER section cannot have a parent"<br>                )` under lexical guard `section_type == "ARTICLE"`.
  - `PlanningRegulationStructureError(<br>                        "Zone chapter label is missing"<br>                    )` under lexical guard `section_type == "ARTICLE"`.
  - `PlanningRegulationStructureError(<br>                    "OTHER section cannot have a zone label"<br>                )` under lexical guard `section_type == "ARTICLE"`.
  - `PlanningRegulationStructureError(<br>                        f"{section_type} {label} must be null"<br>                    )` under lexical guard `section_type == "ARTICLE"`.
  - `PlanningRegulationStructureError(<br>            "Retained source records are omitted from the section partition"<br>        )` under lexical guard `expected_record_start != len(records)`.
  - `PlanningRegulationStructureError("Section IDs must be unique")` under lexical guard `len(set(ids)) != len(ids)`.
  - `PlanningRegulationStructureError("Article parent section is invalid")` under lexical guard `parent not in type_by_id or type_by_id[parent] != "ZONE_CHAPTER"`.
  - `PlanningRegulationStructureError(<br>                "Only articles may have a parent section"<br>            )` under lexical guard `section_type != "ARTICLE"`.
  - `PlanningRegulationStructureError(<br>                "Article parent must occur earlier in source order"<br>            )` under lexical guard `order_by_id[parent] >= order_by_id[section_id]`.
  - `PlanningRegulationStructureError(<br>                "Article zone label differs from its parent chapter"<br>            )` under lexical guard `zone_by_id[parent] != zone_by_id[section_id]`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_validate_result_self` via `_validate_sections`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_result_self` via `_validate_sections`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |
| `_source_records_sha256` | `landscout.stages.structure_planning_regulation._source_records_sha256` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `index.pages["page_number"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_string` | `landscout.stages.structure_planning_regulation._strict_string` |
| `ids.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `_normalize_search_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_nonnegative_integer` | `landscout.stages.structure_planning_regulation._strict_nonnegative_integer` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `row["raw_text"].strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `row["heading_raw"].strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_positive_integer` | `landscout.stages.structure_planning_regulation._strict_positive_integer` |
| `_validated_sha256` | `landscout.stages.structure_planning_regulation._validated_sha256` |
| `"\n".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `dict.fromkeys` | `unresolved local/third-party receiver; no ownership inferred` |
| `_page_tuple` | `landscout.stages.structure_planning_regulation._page_tuple` |
| `pairwise` | `itertools.pairwise` |
| `set(pages).issubset` | `unresolved local/third-party receiver; no ownership inferred` |
| `_section_content_sha256` | `landscout.stages.structure_planning_regulation._section_content_sha256` |
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.isna` | `pandas.isna` |
| `dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `zip` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["section_type"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `parents.items` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_source_records_sha256`<br>`_validated_sha256`<br>`_section_content_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `ids.append(section_id)`<br>`parents[section_id] = _strict_string(parent, "parent section ID")`<br>`zone_by_id[section_id] = zone_label` |
| Direct parameter mutation | None directly present. |

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
    record_position = {
        record.record_id: position for position, record in enumerate(records)
    }
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
        for column in (
            "heading_raw",
            "heading_normalized",
            "raw_text",
            "normalized_text",
        ):
            if not isinstance(row[column], str):
                raise PlanningRegulationStructureError(
                    f"Section {column} must be a string"
                )
        if row["heading_normalized"] != _normalize_search_text(row["heading_raw"]):
            raise PlanningRegulationStructureError(
                "Section heading normalization differs"
            )
        if row["normalized_text"] != _normalize_search_text(row["raw_text"]):
            raise PlanningRegulationStructureError("Section text normalization differs")
        if _strict_nonnegative_integer(
            row["character_count"], "character count"
        ) != len(row["raw_text"]):
            raise PlanningRegulationStructureError("Section character count differs")
        start_record_id = _strict_string(row["start_record_id"], "start record ID")
        end_record_id = _strict_string(row["end_record_id"], "end record ID")
        if (
            start_record_id not in record_position
            or end_record_id not in record_position
        ):
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
                record.page_number in config.document_layout.table_of_contents_pages
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
            raise PlanningRegulationStructureError(
                "Section source-record count differs"
            )
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
            raise PlanningRegulationStructureError(
                "Section page references are invalid"
            )
        start = _strict_positive_integer(row["start_page"], "section start page")
        end = _strict_positive_integer(row["end_page"], "section end page")
        if start != pages[0] or end != pages[-1] or end < start:
            raise PlanningRegulationStructureError(
                "Section page range is invalid or unordered"
            )
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
        if (
            _validated_sha256(row["section_content_sha256"], "section content SHA256")
            != expected_hash
        ):
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
            raise PlanningRegulationStructureError(
                "Only articles may have a parent section"
            )
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_zone_mapping`

**Purpose:** Implements `validate zone mapping` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _validate_zone_mapping(
    result: PlanningRegulationStructureResult,
    config: PlanningRegulationStructureConfig,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |
| `config` | positional-or-keyword | `PlanningRegulationStructureConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `PlanningRegulationStructureError(<br>            "Zone mapping schema is not deterministic"<br>        )` under lexical guard `not isinstance(frame, pd.DataFrame)<br>        or tuple(frame.columns) != ZONE_MAPPING_COLUMNS`.
  - `PlanningRegulationStructureError(<br>                "Zone mapping status or method is invalid"<br>            )` under lexical guard `status not in _MAPPING_STATUSES or method not in _MAPPING_METHODS`.
  - `PlanningRegulationStructureError(<br>                "Zone mapping status/method combination is invalid"<br>            )` under lexical guard `exact_methods[status] != method`.
  - `PlanningRegulationStructureError(<br>                    "Zone polygon count must be positive"<br>                )` under lexical guard `column == "zone_polygon_count" and count == 0`.
  - `PlanningRegulationStructureError(<br>                    "Zone mapping section is unknown"<br>                )` under lexical guard `status in {"EXACT", "CONFIG_ALIAS"}`.
  - `PlanningRegulationStructureError(<br>                    "Resolved zone mapping must reference a zone chapter"<br>                )` under lexical guard `status in {"EXACT", "CONFIG_ALIAS"}`.
  - `PlanningRegulationStructureError(<br>                    "Resolved zone label differs from its matched chapter"<br>                )` under lexical guard `status in {"EXACT", "CONFIG_ALIAS"}`.
  - `PlanningRegulationStructureError(<br>                    "Exact zone mapping must preserve the source label"<br>                )` under lexical guard `status in {"EXACT", "CONFIG_ALIAS"}`.
  - `PlanningRegulationStructureError(<br>                    "Configured zone mapping differs from its final alias target"<br>                )` under lexical guard `status in {"EXACT", "CONFIG_ALIAS"}`.
  - `PlanningRegulationStructureError(<br>                "Unresolved zone mapping has a section ID"<br>            )` under lexical guard `status in {"EXACT", "CONFIG_ALIAS"}`.
  - `PlanningRegulationStructureError(<br>                "Unmapped zone must not claim a resolved chapter label"<br>            )` under lexical guard `status in {"EXACT", "CONFIG_ALIAS"}`.
  - `PlanningRegulationStructureError(<br>                "Dominant candidate zone is unresolved"<br>            )` under lexical guard `row["dominant_candidate_count"] > 0 and status not in {<br>            "EXACT",<br>            "CONFIG_ALIAS",<br>        }`.
  - `PlanningRegulationStructureError(<br>                "Zone candidate coverage counts are mathematically inconsistent"<br>            )` under lexical guard `not (<br>            counts["dominant_candidate_count"]<br>            <= counts["candidate_parcel_count"]<br>            <= counts["candidate_intersection_count"]<br>        )`.
  - `PlanningRegulationStructureError("Zone mapping lineage differs")` under lexical guard `row[column] != actual`.
  - `PlanningRegulationStructureError(<br>            "Zone mappings must be unique and sorted"<br>        )` under lexical guard `labels != sorted(labels) or len(set(labels)) != len(labels)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_validate_result_self` via `_validate_zone_mapping`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_result_self` via `_validate_zone_mapping`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |
| `result.sections.set_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_string` | `landscout.stages.structure_planning_regulation._strict_string` |
| `labels.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_nonnegative_integer` | `landscout.stages.structure_planning_regulation._strict_nonnegative_integer` |
| `_resolved_alias` | `landscout.stages.structure_planning_regulation._resolved_alias` |
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.isna` | `pandas.isna` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `labels.append(label)`<br>`counts[column] = count` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_zone_mapping(
    result: PlanningRegulationStructureResult,
    config: PlanningRegulationStructureConfig,
) -> None:
    frame = result.zone_mapping
    if (
        not isinstance(frame, pd.DataFrame)
        or tuple(frame.columns) != ZONE_MAPPING_COLUMNS
    ):
        raise PlanningRegulationStructureError(
            "Zone mapping schema is not deterministic"
        )
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
            raise PlanningRegulationStructureError(
                "Zone mapping status or method is invalid"
            )
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
                raise PlanningRegulationStructureError(
                    "Zone polygon count must be positive"
                )
        matched = row["matched_section_id"]
        if status in {"EXACT", "CONFIG_ALIAS"}:
            matched_id = _strict_string(matched, "matched section ID")
            if matched_id not in sections.index:
                raise PlanningRegulationStructureError(
                    "Zone mapping section is unknown"
                )
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
            raise PlanningRegulationStructureError(
                "Unresolved zone mapping has a section ID"
            )
        elif (
            status == "UNMAPPED"
            and row["resolved_zone_chapter_label"] is not None
            and not bool(pd.isna(row["resolved_zone_chapter_label"]))
        ):
            raise PlanningRegulationStructureError(
                "Unmapped zone must not claim a resolved chapter label"
            )
        if row["dominant_candidate_count"] > 0 and status not in {
            "EXACT",
            "CONFIG_ALIAS",
        }:
            raise PlanningRegulationStructureError(
                "Dominant candidate zone is unresolved"
            )
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
        raise PlanningRegulationStructureError(
            "Zone mappings must be unique and sorted"
        )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_topic_evidence`

**Purpose:** Implements `validate topic evidence` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _validate_topic_evidence(
    index: PlanningRegulationIndex,
    result: PlanningRegulationStructureResult,
    config: PlanningRegulationStructureConfig,
    builds: Sequence[_SectionBuild],
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `result` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |
| `config` | positional-or-keyword | `PlanningRegulationStructureConfig` | `required` |
| `builds` | positional-or-keyword | `Sequence[_SectionBuild]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `PlanningRegulationStructureError(<br>            "Topic evidence schema is not deterministic"<br>        )` under lexical guard `not isinstance(frame, pd.DataFrame)<br>        or tuple(frame.columns) != TOPIC_EVIDENCE_COLUMNS`.
  - `PlanningRegulationStructureError(<br>                "Topic evidence topic is unconfigured"<br>            )` under lexical guard `topic not in config.topics`.
  - `PlanningRegulationStructureError(<br>                "Topic evidence search term is unconfigured"<br>            )` under lexical guard `term not in config.topics[topic]`.
  - `PlanningRegulationStructureError("Topic search normalization differs")` under lexical guard `normalized != _normalize_search_text(term)`.
  - `PlanningRegulationStructureError(<br>                "Topic evidence references an unknown section"<br>            )` under lexical guard `section_id not in sections.index`.
  - `PlanningRegulationStructureError(<br>                "Topic evidence references an unknown page"<br>            )` under lexical guard `page not in page_set or page not in _page_tuple(<br>            sections.at[section_id, "page_numbers"]<br>        )`.
  - `PlanningRegulationStructureError(<br>                "Topic evidence page is absent from its retained section text"<br>            )` under lexical guard `(section_id, page) not in fragments`.
  - `PlanningRegulationStructureError("Topic occurrence count is invalid")` under lexical guard `count < 1`.
  - `PlanningRegulationStructureError("Topic contexts must be strings")` under lexical guard `not isinstance(row["raw_context"], str) or not isinstance(<br>            row["normalized_context"], str<br>        )`.
  - `PlanningRegulationStructureError("Evidence scope is invalid")` under lexical guard `scope not in _EVIDENCE_SCOPES`.
  - `PlanningRegulationStructureError(<br>                "Topic evidence scope differs from its section location"<br>            )` under lexical guard `scope != expected_scope`.
  - `PlanningRegulationStructureError(<br>                    f"Topic evidence {column} differs from its section"<br>                )` under lexical guard `actual != expected`.
  - `PlanningRegulationStructureError("Topic match policy differs")` under lexical guard `row["match_policy"] != config.topic_match_policy.identifier`.
  - `PlanningRegulationStructureError(<br>                "Topic evidence has no retained source-text match"<br>            )` under lexical guard `not retained_matches`.
  - `PlanningRegulationStructureError(<br>                    "Topic match provenance differs from source text"<br>                )` under lexical guard `_strict_nonnegative_integer(row[column], column) != expected`.
  - `PlanningRegulationStructureError(<br>                "Topic occurrence count differs from retained source spans"<br>            )` under lexical guard `count != len(retained_matches)`.
  - `PlanningRegulationStructureError(<br>                "Topic context differs from retained source text"<br>            )` under lexical guard `row["raw_context"] != expected_raw_context<br>            or row["normalized_context"] != expected_normalized_context<br>            or row["raw_context"] not in raw_fragment`.
  - `PlanningRegulationStructureError("Topic evidence row is duplicated")` under lexical guard `key in keys`.
  - `PlanningRegulationStructureError("Topic evidence lineage differs")` under lexical guard `row[column] != actual`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_validate_result_self` via `_validate_topic_evidence`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_result_self` via `_validate_topic_evidence`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |
| `result.sections.set_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `index.pages["page_number"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_string` | `landscout.stages.structure_planning_regulation._strict_string` |
| `_normalize_search_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_positive_integer` | `landscout.stages.structure_planning_regulation._strict_positive_integer` |
| `_page_tuple` | `landscout.stages.structure_planning_regulation._page_tuple` |
| `_evidence_scope` | `landscout.stages.structure_planning_regulation._evidence_scope` |
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.isna` | `pandas.isna` |
| `_normalize_search_text_with_mapping` | `unresolved local/third-party receiver; no ownership inferred` |
| `_literal_topic_matches` | `landscout.stages.structure_planning_regulation._literal_topic_matches` |
| `expected_positions.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_nonnegative_integer` | `landscout.stages.structure_planning_regulation._strict_nonnegative_integer` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `max` | `unresolved local/third-party receiver; no ownership inferred` |
| `min` | `unresolved local/third-party receiver; no ownership inferred` |
| `_raw_context` | `unresolved local/third-party receiver; no ownership inferred` |
| `keys.add` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `keys.add(key)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_topic_evidence(
    index: PlanningRegulationIndex,
    result: PlanningRegulationStructureResult,
    config: PlanningRegulationStructureConfig,
    builds: Sequence[_SectionBuild],
) -> None:
    frame = result.topic_evidence
    if (
        not isinstance(frame, pd.DataFrame)
        or tuple(frame.columns) != TOPIC_EVIDENCE_COLUMNS
    ):
        raise PlanningRegulationStructureError(
            "Topic evidence schema is not deterministic"
        )
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
            raise PlanningRegulationStructureError(
                "Topic evidence topic is unconfigured"
            )
        term = _strict_string(row["search_term"], "search term")
        if term not in config.topics[topic]:
            raise PlanningRegulationStructureError(
                "Topic evidence search term is unconfigured"
            )
        normalized = _strict_string(
            row["normalized_search_term"], "normalized search term"
        )
        if normalized != _normalize_search_text(term):
            raise PlanningRegulationStructureError("Topic search normalization differs")
        section_id = _strict_string(row["section_id"], "topic section ID")
        if section_id not in sections.index:
            raise PlanningRegulationStructureError(
                "Topic evidence references an unknown section"
            )
        page = _strict_positive_integer(row["page_number"], "topic page number")
        if page not in page_set or page not in _page_tuple(
            sections.at[section_id, "page_numbers"]
        ):
            raise PlanningRegulationStructureError(
                "Topic evidence references an unknown page"
            )
        if (section_id, page) not in fragments:
            raise PlanningRegulationStructureError(
                "Topic evidence page is absent from its retained section text"
            )
        count = _strict_positive_integer(
            row["occurrence_count"], "topic occurrence count"
        )
        if count < 1:
            raise PlanningRegulationStructureError("Topic occurrence count is invalid")
        if not isinstance(row["raw_context"], str) or not isinstance(
            row["normalized_context"], str
        ):
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
        context_start = max(0, first.normalized_start - config.topic_context_characters)
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_build_structure_result`

**Purpose:** Implements `build structure result` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

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

- Exact decorators: none.
- Declared return annotation: `tuple[PlanningRegulationStructureResult, tuple[_SectionBuild, ...], tuple[_LineRecord, ...]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `zones` | positional-or-keyword | `pd.DataFrame` | `required` |
| `intersections` | positional-or-keyword | `pd.DataFrame` | `required` |
| `config` | positional-or-keyword | `PlanningRegulationStructureConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_result_with_hashes(result), builds, records`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::validate_planning_regulation_structure_with_fragments` via `_build_structure_result`
- value/type reference: `landscout.stages.structure_planning_regulation::validate_planning_regulation_structure_with_fragments` via `_build_structure_result`
- direct call: `landscout.stages.structure_planning_regulation::structure_planning_regulation` via `_build_structure_result`
- value/type reference: `landscout.stages.structure_planning_regulation::structure_planning_regulation` via `_build_structure_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_build_sections` | `landscout.stages.structure_planning_regulation._build_sections` |
| `_build_zone_mapping` | `landscout.stages.structure_planning_regulation._build_zone_mapping` |
| `_build_topic_evidence` | `landscout.stages.structure_planning_regulation._build_topic_evidence` |
| `_intersection_hash_columns` | `landscout.stages.structure_planning_regulation._intersection_hash_columns` |
| `PlanningRegulationStructureResult` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureResult` |
| `_config_sha256` | `landscout.stages.structure_planning_regulation._config_sha256` |
| `_input_frame_sha256` | `landscout.stages.structure_planning_regulation._input_frame_sha256` |
| `_source_records_sha256` | `landscout.stages.structure_planning_regulation._source_records_sha256` |
| `_result_with_hashes` | `landscout.stages.structure_planning_regulation._result_with_hashes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_intersection_hash_columns`<br>`_config_sha256`<br>`_input_frame_sha256`<br>`_source_records_sha256`<br>`_result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_result_self`

**Purpose:** Implements `validate result self` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

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

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `zones` | positional-or-keyword | `pd.DataFrame` | `required` |
| `intersections` | positional-or-keyword | `pd.DataFrame` | `required` |
| `config` | positional-or-keyword | `PlanningRegulationStructureConfig` | `required` |
| `result` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |
| `builds` | positional-or-keyword | `Sequence[_SectionBuild]` | `required` |
| `records` | positional-or-keyword | `Sequence[_LineRecord]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `PlanningRegulationStructureError(<br>            "result must be a PlanningRegulationStructureResult"<br>        )` under lexical guard `not isinstance(result, PlanningRegulationStructureResult)`.
  - `PlanningRegulationStructureError(<br>            "Structure result lineage differs from index"<br>        )` under lexical guard `result.document_id != index.document_id<br>        or result.archive_sha256 != index.archive_sha256<br>        or result.pdf_sha256 != index.pdf_sha256<br>        or result.index_content_sha256 != index.index_content_sha256`.
  - `PlanningRegulationStructureError(<br>            "Structure config schema version differs"<br>        )` under lexical guard `config_schema != config.schema_version`.
  - `PlanningRegulationStructureError("Structure config hash differs")` under lexical guard `result.structure_config_sha256 != _config_sha256(config)`.
  - `PlanningRegulationStructureError("Zone input hash differs")` under lexical guard `result.zones_content_sha256 != expected_zones_hash`.
  - `PlanningRegulationStructureError(<br>            "Intersection hash columns differ from the factual input schema"<br>        )` under lexical guard `type(result.zoning_intersection_hash_columns) is not tuple<br>        or not all(<br>            isinstance(column, str)<br>            for column in result.zoning_intersection_hash_columns<br>        )<br>        or result.zoning_intersection_hash_columns != expected_intersection_columns`.
  - `PlanningRegulationStructureError("Intersection input hash differs")` under lexical guard `result.zoning_intersections_content_sha256 != expected_intersections_hash`.
  - `PlanningRegulationStructureError(<br>            "Unsupported section hash schema version"<br>        )` under lexical guard `schema != SECTION_HASH_SCHEMA_VERSION`.
  - `PlanningRegulationStructureError(f"{label} content hash differs")` under lexical guard `_validated_sha256(actual, f"{label} content SHA256") != wanted`.
  - `PlanningRegulationStructureError("Complete structure result hash differs")` under lexical guard `_validated_sha256(<br>            result.structure_result_content_sha256,<br>            "structure result content SHA256",<br>        )<br>        != expected.structure_result_content_sha256`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::validate_planning_regulation_structure_with_fragments` via `_validate_result_self`
- value/type reference: `landscout.stages.structure_planning_regulation::validate_planning_regulation_structure_with_fragments` via `_validate_result_self`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `validate_planning_regulation_index` | `landscout.stages.index_planning_regulation.validate_planning_regulation_index` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |
| `_strict_string` | `landscout.stages.structure_planning_regulation._strict_string` |
| `_validated_sha256` | `landscout.stages.structure_planning_regulation._validated_sha256` |
| `_strict_positive_integer` | `landscout.stages.structure_planning_regulation._strict_positive_integer` |
| `_config_sha256` | `landscout.stages.structure_planning_regulation._config_sha256` |
| `_input_frame_sha256` | `landscout.stages.structure_planning_regulation._input_frame_sha256` |
| `_intersection_hash_columns` | `landscout.stages.structure_planning_regulation._intersection_hash_columns` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `all` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_sections` | `landscout.stages.structure_planning_regulation._validate_sections` |
| `_validate_zone_mapping` | `landscout.stages.structure_planning_regulation._validate_zone_mapping` |
| `_validate_topic_evidence` | `landscout.stages.structure_planning_regulation._validate_topic_evidence` |
| `_result_with_hashes` | `landscout.stages.structure_planning_regulation._result_with_hashes` |
| `replace` | `dataclasses.replace` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_validated_sha256`<br>`_config_sha256`<br>`_input_frame_sha256`<br>`_intersection_hash_columns`<br>`_result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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
        raise PlanningRegulationStructureError(
            "Structure result lineage differs from index"
        )
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
        raise PlanningRegulationStructureError(
            "Unsupported section hash schema version"
        )
    _validate_sections(index, result, records, config)
    _validate_zone_mapping(result, config)
    _validate_topic_evidence(index, result, config, builds)
    expected = _result_with_hashes(
        replace(
            result,
            sections_content_sha256="",
            zone_map_content_sha256="",
            topic_evidence_content_sha256="",
            structure_result_content_sha256="",
        )
    )
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
    if (
        _validated_sha256(
            result.structure_result_content_sha256,
            "structure result content SHA256",
        )
        != expected.structure_result_content_sha256
    ):
        raise PlanningRegulationStructureError("Complete structure result hash differs")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_resolved_config`

**Purpose:** Implements `resolved config` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _resolved_config(
    config: PlanningRegulationStructureConfig | str | Path,
) -> PlanningRegulationStructureConfig:
```

- Exact decorators: none.
- Declared return annotation: `PlanningRegulationStructureConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `PlanningRegulationStructureConfig \| str \| Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `PlanningRegulationStructureConfig.model_validate(<br>                config.model_dump(mode="python")<br>            )`
  - `load_planning_regulation_structure_config(config)`
- Explicit raise paths:
  - `PlanningRegulationStructureError(<br>                "Planning structure configuration is invalid"<br>            )` under lexical guard `isinstance(config, PlanningRegulationStructureConfig)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::validate_planning_regulation_structure_with_fragments` via `_resolved_config`
- value/type reference: `landscout.stages.structure_planning_regulation::validate_planning_regulation_structure_with_fragments` via `_resolved_config`
- direct call: `landscout.stages.structure_planning_regulation::structure_planning_regulation` via `_resolved_config`
- value/type reference: `landscout.stages.structure_planning_regulation::structure_planning_regulation` via `_resolved_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationStructureConfig.model_validate` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureConfig.model_validate` |
| `config.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |
| `load_planning_regulation_structure_config` | `landscout.stages.structure_planning_regulation.load_planning_regulation_structure_config` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_canonical_frame_rows`

**Purpose:** Implements `canonical frame rows` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _canonical_frame_rows(frame: pd.DataFrame, columns: Sequence[str]) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `pd.DataFrame` | `required` |
| `columns` | positional-or-keyword | `Sequence[str]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_value(frame.loc[:, columns].to_dict("records"))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::_compare_expected_result` via `_canonical_frame_rows`
- value/type reference: `landscout.stages.structure_planning_regulation::_compare_expected_result` via `_canonical_frame_rows`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_value` | `landscout.stages.structure_planning_regulation._canonical_value` |
| `frame.loc[:, columns].to_dict` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _canonical_frame_rows(frame: pd.DataFrame, columns: Sequence[str]) -> object:
    return _canonical_value(frame.loc[:, columns].to_dict("records"))
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_compare_expected_result`

**Purpose:** Implements `compare expected result` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _compare_expected_result(
    result: PlanningRegulationStructureResult,
    expected: PlanningRegulationStructureResult,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |
| `expected` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `PlanningRegulationStructureError(<br>                f"Structure result {field} differs from rebuilt source evidence"<br>            )` under lexical guard `getattr(result, field) != getattr(expected, field)`.
  - `PlanningRegulationStructureError(<br>                f"{name} schema differs from rebuilt source evidence"<br>            )` under lexical guard `tuple(actual_frame.columns) != tuple(columns)`.
  - `PlanningRegulationStructureError(<br>                f"{name} differs from rebuilt source evidence"<br>            )` under lexical guard `_canonical_frame_rows(actual_frame, columns) != _canonical_frame_rows(<br>            expected_frame, columns<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::validate_planning_regulation_structure_with_fragments` via `_compare_expected_result`
- value/type reference: `landscout.stages.structure_planning_regulation::validate_planning_regulation_structure_with_fragments` via `_compare_expected_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `_canonical_frame_rows` | `landscout.stages.structure_planning_regulation._canonical_frame_rows` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_section_page_fragments`

**Purpose:** Implements `section page fragments` within the file role: Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors.

**Exact signature**

```python
def _section_page_fragments(
    result: PlanningRegulationStructureResult,
    builds: Sequence[_SectionBuild],
) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |
| `builds` | positional-or-keyword | `Sequence[_SectionBuild]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `frame`
- Explicit raise paths:
  - `PlanningRegulationStructureError(<br>            "Section/page fragment identity is not unique"<br>        )` under lexical guard `frame.duplicated(["section_id", "page_number"]).any()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.structure_planning_regulation::validate_planning_regulation_structure_with_fragments` via `_section_page_fragments`
- value/type reference: `landscout.stages.structure_planning_regulation::validate_planning_regulation_structure_with_fragments` via `_section_page_fragments`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `sha256(<br>                raw_text.encode("utf-8")<br>            ).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `raw_text.encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `frame["page_number"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.duplicated(["section_id", "page_number"]).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(<br>                raw_text.encode("utf-8")<br>            ).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `frame["page_number"] = frame["page_number"].astype("int64")` |
| Direct parameter mutation | None directly present. |

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
            "structure_result_content_sha256": (result.structure_result_content_sha256),
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `validate_planning_regulation_structure_with_fragments`

**Purpose:** Validate the complete structure and return its retained page fragments.

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

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `zones` | positional-or-keyword | `pd.DataFrame` | `required` |
| `zoning_intersections` | positional-or-keyword | `pd.DataFrame` | `required` |
| `config` | positional-or-keyword | `PlanningRegulationStructureConfig \| str \| Path` | `required` |
| `result` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_section_page_fragments(result, builds)`
- Explicit raise paths:
  - `re-raise`.
  - `PlanningRegulationStructureError(<br>            "Planning regulation structure validation failed safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    load_planning_regulation_structure_config,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`
- import: `landscout.stages.interpret_bess_zoning::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    validate_planning_regulation_structure_with_fragments,
)`
- direct call: `landscout.stages.interpret_bess_zoning::_build_result` via `validate_planning_regulation_structure_with_fragments`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_result` via `validate_planning_regulation_structure_with_fragments`
- direct call: `landscout.stages.structure_planning_regulation::validate_planning_regulation_structure` via `validate_planning_regulation_structure_with_fragments`
- value/type reference: `landscout.stages.structure_planning_regulation::validate_planning_regulation_structure` via `validate_planning_regulation_structure_with_fragments`
- direct call: `landscout.stages.structure_planning_regulation::planning_regulation_section_page_fragments` via `validate_planning_regulation_structure_with_fragments`
- value/type reference: `landscout.stages.structure_planning_regulation::planning_regulation_section_page_fragments` via `validate_planning_regulation_structure_with_fragments`
- import: `tests.unit.test_structure_planning_regulation::<module>` via `from landscout.stages.structure_planning_regulation import (
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
)`
- direct call: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_can_return_validated_fragments` via `validate_planning_regulation_structure_with_fragments`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_can_return_validated_fragments` via `validate_planning_regulation_structure_with_fragments`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_resolved_config` | `landscout.stages.structure_planning_regulation._resolved_config` |
| `_validate_document_lock` | `landscout.stages.structure_planning_regulation._validate_document_lock` |
| `_validated_zoning_inputs` | `landscout.stages.structure_planning_regulation._validated_zoning_inputs` |
| `_build_structure_result` | `landscout.stages.structure_planning_regulation._build_structure_result` |
| `_validate_result_self` | `landscout.stages.structure_planning_regulation._validate_result_self` |
| `_compare_expected_result` | `landscout.stages.structure_planning_regulation._compare_expected_result` |
| `_section_page_fragments` | `landscout.stages.structure_planning_regulation._section_page_fragments` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `validate_planning_regulation_structure`

**Purpose:** Rebuild and validate the complete structure from all factual inputs.

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

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `zones` | positional-or-keyword | `pd.DataFrame` | `required` |
| `zoning_intersections` | positional-or-keyword | `pd.DataFrame` | `required` |
| `config` | positional-or-keyword | `PlanningRegulationStructureConfig \| str \| Path` | `required` |
| `result` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    load_planning_regulation_structure_config,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`
- direct call: `landscout.stages.structure_planning_regulation::structure_planning_regulation` via `validate_planning_regulation_structure`
- value/type reference: `landscout.stages.structure_planning_regulation::structure_planning_regulation` via `validate_planning_regulation_structure`
- import: `tests.unit.test_structure_planning_regulation::<module>` via `from landscout.stages.structure_planning_regulation import (
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
)`
- direct call: `tests.unit.test_structure_planning_regulation::_validate` via `validate_planning_regulation_structure`
- value/type reference: `tests.unit.test_structure_planning_regulation::_validate` via `validate_planning_regulation_structure`
- direct call: `tests.unit.test_structure_planning_regulation::test_document_layout_accepts_real_first_and_last_indexed_pages` via `validate_planning_regulation_structure`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_document_layout_accepts_real_first_and_last_indexed_pages` via `validate_planning_regulation_structure`
- direct call: `tests.unit.test_structure_planning_regulation::test_existing_empty_toc_page_is_valid_not_nonexistent` via `validate_planning_regulation_structure`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_existing_empty_toc_page_is_valid_not_nonexistent` via `validate_planning_regulation_structure`
- direct call: `tests.unit.test_structure_planning_regulation::test_evidence_scope_is_derived_from_exact_section_type` via `validate_planning_regulation_structure`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_evidence_scope_is_derived_from_exact_section_type` via `validate_planning_regulation_structure`
- direct call: `tests.unit.test_structure_planning_regulation::test_blank_only_prefix_is_preserved_in_first_actual_section` via `validate_planning_regulation_structure`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_blank_only_prefix_is_preserved_in_first_actual_section` via `validate_planning_regulation_structure`
- direct call: `tests.unit.test_structure_planning_regulation::test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence` via `validate_planning_regulation_structure`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence` via `validate_planning_regulation_structure`
- direct call: `tests.unit.test_structure_planning_regulation::test_blank_gap_after_toc_is_preserved_without_a_blank_other_section` via `validate_planning_regulation_structure`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_blank_gap_after_toc_is_preserved_without_a_blank_other_section` via `validate_planning_regulation_structure`
- direct call: `tests.unit.test_structure_planning_regulation::_structure_with_document_layout` via `validate_planning_regulation_structure`
- value/type reference: `tests.unit.test_structure_planning_regulation::_structure_with_document_layout` via `validate_planning_regulation_structure`
- direct call: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_rejects_changed_ambiguous_grammar` via `validate_planning_regulation_structure`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_rejects_changed_ambiguous_grammar` via `validate_planning_regulation_structure`
- direct call: `tests.unit.test_structure_planning_regulation::test_wrong_intersection_source_zone_id_is_rejected` via `validate_planning_regulation_structure`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_wrong_intersection_source_zone_id_is_rejected` via `validate_planning_regulation_structure`
- direct call: `tests.unit.test_structure_planning_regulation::test_intersection_upper_bound_uses_shared_relative_tolerance` via `validate_planning_regulation_structure`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_intersection_upper_bound_uses_shared_relative_tolerance` via `validate_planning_regulation_structure`
- direct call: `tests.unit.test_structure_planning_regulation::test_intersection_hash_columns_are_actual_and_deterministic` via `validate_planning_regulation_structure`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_intersection_hash_columns_are_actual_and_deterministic` via `validate_planning_regulation_structure`
- direct call: `tests.unit.test_structure_planning_regulation::test_optional_intersection_metric_change_invalidates_existing_result` via `validate_planning_regulation_structure`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_optional_intersection_metric_change_invalidates_existing_result` via `validate_planning_regulation_structure`
- direct call: `tests.unit.test_structure_planning_regulation::test_intersection_hash_column_lineage_mutation_is_rejected` via `validate_planning_regulation_structure`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_intersection_hash_column_lineage_mutation_is_rejected` via `validate_planning_regulation_structure`
- direct call: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_rejects_post_build_source_change` via `validate_planning_regulation_structure`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_rejects_post_build_source_change` via `validate_planning_regulation_structure`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `validate_planning_regulation_structure_with_fragments` | `landscout.stages.structure_planning_regulation.validate_planning_regulation_structure_with_fragments` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `planning_regulation_section_page_fragments`

**Purpose:** Return validated retained raw text for every section and source page.

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

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `zones` | positional-or-keyword | `pd.DataFrame` | `required` |
| `zoning_intersections` | positional-or-keyword | `pd.DataFrame` | `required` |
| `config` | positional-or-keyword | `PlanningRegulationStructureConfig \| str \| Path` | `required` |
| `result` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `validate_planning_regulation_structure_with_fragments(<br>            index,<br>            zones,<br>            zoning_intersections,<br>            config,<br>            result,<br>        )`
- Explicit raise paths:
  - `re-raise`.
  - `PlanningRegulationStructureError(<br>            "Planning regulation section/page fragments could not be rebuilt safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    load_planning_regulation_structure_config,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`
- import: `tests.unit.test_interpret_bess_zoning::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
)`
- direct call: `tests.unit.test_interpret_bess_zoning::_policy` via `planning_regulation_section_page_fragments`
- value/type reference: `tests.unit.test_interpret_bess_zoning::_policy` via `planning_regulation_section_page_fragments`
- direct call: `tests.unit.test_interpret_bess_zoning::test_same_general_occurrence_may_be_scoped_to_different_chapters` via `planning_regulation_section_page_fragments`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_same_general_occurrence_may_be_scoped_to_different_chapters` via `planning_regulation_section_page_fragments`
- direct call: `tests.unit.test_interpret_bess_zoning::test_exact_section_page_occurrence_is_auditable` via `planning_regulation_section_page_fragments`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_exact_section_page_occurrence_is_auditable` via `planning_regulation_section_page_fragments`
- direct call: `tests.unit.test_interpret_bess_zoning::test_repeated_excerpt_occurrence_is_bound_to_policy` via `planning_regulation_section_page_fragments`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_repeated_excerpt_occurrence_is_bound_to_policy` via `planning_regulation_section_page_fragments`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `validate_planning_regulation_structure_with_fragments` | `landscout.stages.structure_planning_regulation.validate_planning_regulation_structure_with_fragments` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `structure_planning_regulation`

**Purpose:** Build source-locked sections, exact zone mappings, and literal topic evidence.

**Exact signature**

```python
def structure_planning_regulation(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
    zoning_intersections: pd.DataFrame,
    config: PlanningRegulationStructureConfig | str | Path,
) -> PlanningRegulationStructureResult:
```

- Exact decorators: none.
- Declared return annotation: `PlanningRegulationStructureResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `zones` | positional-or-keyword | `pd.DataFrame` | `required` |
| `zoning_intersections` | positional-or-keyword | `pd.DataFrame` | `required` |
| `config` | positional-or-keyword | `PlanningRegulationStructureConfig \| str \| Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- Explicit raise paths:
  - `re-raise`.
  - `PlanningRegulationStructureError(<br>            "Planning regulation structure could not be built safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    load_planning_regulation_structure_config,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`
- import: `tests.integration.test_gpu_planning_end_to_end::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureResult,
    structure_planning_regulation,
)`
- direct call: `tests.integration.test_gpu_planning_end_to_end::_build_physical_chain` via `structure_planning_regulation`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_build_physical_chain` via `structure_planning_regulation`
- import: `tests.unit.test_interpret_bess_zoning::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
)`
- direct call: `tests.unit.test_interpret_bess_zoning::inputs` via `structure_planning_regulation`
- value/type reference: `tests.unit.test_interpret_bess_zoning::inputs` via `structure_planning_regulation`
- import: `tests.unit.test_structure_planning_regulation::<module>` via `from landscout.stages.structure_planning_regulation import (
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
)`
- direct call: `tests.unit.test_structure_planning_regulation::valid_result` via `structure_planning_regulation`
- value/type reference: `tests.unit.test_structure_planning_regulation::valid_result` via `structure_planning_regulation`
- direct call: `tests.unit.test_structure_planning_regulation::test_document_layout_rejects_nonexistent_indexed_pages` via `structure_planning_regulation`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_document_layout_rejects_nonexistent_indexed_pages` via `structure_planning_regulation`
- direct call: `tests.unit.test_structure_planning_regulation::test_document_lock_mismatch_is_rejected` via `structure_planning_regulation`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_document_lock_mismatch_is_rejected` via `structure_planning_regulation`
- direct call: `tests.unit.test_structure_planning_regulation::test_evidence_scope_is_derived_from_exact_section_type` via `structure_planning_regulation`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_evidence_scope_is_derived_from_exact_section_type` via `structure_planning_regulation`
- direct call: `tests.unit.test_structure_planning_regulation::test_reversed_topic_mapping_keys_do_not_change_output_or_hashes` via `structure_planning_regulation`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_reversed_topic_mapping_keys_do_not_change_output_or_hashes` via `structure_planning_regulation`
- direct call: `tests.unit.test_structure_planning_regulation::test_equal_length_overlap_uses_configured_term_order_as_tie_break` via `structure_planning_regulation`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_equal_length_overlap_uses_configured_term_order_as_tie_break` via `structure_planning_regulation`
- direct call: `tests.unit.test_structure_planning_regulation::test_inputs_are_not_mutated` via `structure_planning_regulation`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_inputs_are_not_mutated` via `structure_planning_regulation`
- direct call: `tests.unit.test_structure_planning_regulation::test_body_page_extraction_error_stops_structure` via `structure_planning_regulation`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_body_page_extraction_error_stops_structure` via `structure_planning_regulation`
- direct call: `tests.unit.test_structure_planning_regulation::test_blank_successfully_extracted_body_page_remains_valid` via `structure_planning_regulation`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_blank_successfully_extracted_body_page_remains_valid` via `structure_planning_regulation`
- direct call: `tests.unit.test_structure_planning_regulation::test_dominant_unmapped_zone_stops_processing` via `structure_planning_regulation`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_dominant_unmapped_zone_stops_processing` via `structure_planning_regulation`
- direct call: `tests.unit.test_structure_planning_regulation::test_blank_only_prefix_is_preserved_in_first_actual_section` via `structure_planning_regulation`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_blank_only_prefix_is_preserved_in_first_actual_section` via `structure_planning_regulation`
- direct call: `tests.unit.test_structure_planning_regulation::test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence` via `structure_planning_regulation`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence` via `structure_planning_regulation`
- direct call: `tests.unit.test_structure_planning_regulation::test_blank_gap_after_toc_is_preserved_without_a_blank_other_section` via `structure_planning_regulation`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_blank_gap_after_toc_is_preserved_without_a_blank_other_section` via `structure_planning_regulation`
- direct call: `tests.unit.test_structure_planning_regulation::_structure_with_document_layout` via `structure_planning_regulation`
- value/type reference: `tests.unit.test_structure_planning_regulation::_structure_with_document_layout` via `structure_planning_regulation`
- direct call: `tests.unit.test_structure_planning_regulation::test_two_zone_patterns_matching_one_line_are_ambiguous` via `structure_planning_regulation`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_two_zone_patterns_matching_one_line_are_ambiguous` via `structure_planning_regulation`
- direct call: `tests.unit.test_structure_planning_regulation::test_two_article_patterns_matching_one_line_are_ambiguous` via `structure_planning_regulation`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_two_article_patterns_matching_one_line_are_ambiguous` via `structure_planning_regulation`
- direct call: `tests.unit.test_structure_planning_regulation::test_general_and_article_cross_category_match_is_ambiguous` via `structure_planning_regulation`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_general_and_article_cross_category_match_is_ambiguous` via `structure_planning_regulation`
- direct call: `tests.unit.test_structure_planning_regulation::test_zone_and_general_cross_category_match_is_ambiguous` via `structure_planning_regulation`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_zone_and_general_cross_category_match_is_ambiguous` via `structure_planning_regulation`
- direct call: `tests.unit.test_structure_planning_regulation::test_ambiguous_continuation_candidate_fails_with_record_diagnostic` via `structure_planning_regulation`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_ambiguous_continuation_candidate_fails_with_record_diagnostic` via `structure_planning_regulation`
- direct call: `tests.unit.test_structure_planning_regulation::test_normal_muret_compatible_grammar_remains_deterministic` via `structure_planning_regulation`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_normal_muret_compatible_grammar_remains_deterministic` via `structure_planning_regulation`
- direct call: `tests.unit.test_structure_planning_regulation::test_intersection_area_cannot_exceed_available_geometry_area` via `structure_planning_regulation`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_intersection_area_cannot_exceed_available_geometry_area` via `structure_planning_regulation`
- direct call: `tests.unit.test_structure_planning_regulation::test_intersection_upper_bound_uses_shared_relative_tolerance` via `structure_planning_regulation`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_intersection_upper_bound_uses_shared_relative_tolerance` via `structure_planning_regulation`
- direct call: `tests.unit.test_structure_planning_regulation::test_intersection_hash_columns_are_actual_and_deterministic` via `structure_planning_regulation`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_intersection_hash_columns_are_actual_and_deterministic` via `structure_planning_regulation`
- direct call: `tests.unit.test_structure_planning_regulation::test_optional_intersection_metric_change_invalidates_existing_result` via `structure_planning_regulation`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_optional_intersection_metric_change_invalidates_existing_result` via `structure_planning_regulation`
- direct call: `tests.unit.test_structure_planning_regulation::test_intersection_hash_column_lineage_mutation_is_rejected` via `structure_planning_regulation`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_intersection_hash_column_lineage_mutation_is_rejected` via `structure_planning_regulation`
- direct call: `tests.unit.test_structure_planning_regulation::test_alias_chain_resolves_to_final_configured_target` via `structure_planning_regulation`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_alias_chain_resolves_to_final_configured_target` via `structure_planning_regulation`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_resolved_config` | `landscout.stages.structure_planning_regulation._resolved_config` |
| `_validate_document_lock` | `landscout.stages.structure_planning_regulation._validate_document_lock` |
| `_validated_zoning_inputs` | `landscout.stages.structure_planning_regulation._validated_zoning_inputs` |
| `_build_structure_result` | `landscout.stages.structure_planning_regulation._build_structure_result` |
| `validate_planning_regulation_structure` | `landscout.stages.structure_planning_regulation.validate_planning_regulation_structure` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.


## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: `_normalize_search_text_with_mapping`, `SECTION_HASH_SCHEMA_VERSION`, `STRUCTURE_MANIFEST_SCHEMA_VERSION`, `_SUPPORTED_CONFIG_SCHEMA_VERSION`, `_MAPPING_STATUSES`, `_MAPPING_METHODS`, `_ZONE_INPUT_COLUMNS`, `_REQUIRED_INTERSECTION_INPUT_COLUMNS`, `_OPTIONAL_INTERSECTION_INPUT_COLUMNS`, `SECTION_COLUMNS`, `ZONE_MAPPING_COLUMNS`, `TOPIC_EVIDENCE_COLUMNS`.
- Exact value/null/index/CRS/geometry/hash behavior is claimed only where the reproduced validators and operations enforce it.

## 8. Public exports and package ownership

Exact `__all__` members and local origins:

| Export | Local origin binding |
|---|---|
| `PlanningRegulationStructureConfig` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureConfig` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |
| `PlanningRegulationStructureResult` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureResult` |
| `load_planning_regulation_structure_config` | `landscout.stages.structure_planning_regulation.load_planning_regulation_structure_config` |
| `planning_regulation_section_page_fragments` | `landscout.stages.structure_planning_regulation.planning_regulation_section_page_fragments` |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `validate_planning_regulation_structure` | `landscout.stages.structure_planning_regulation.validate_planning_regulation_structure` |
| `validate_planning_regulation_structure_with_fragments` | `landscout.stages.structure_planning_regulation.validate_planning_regulation_structure_with_fragments` |

## 9. Trust, provenance, side effects, and business boundary

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
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
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictInt,
    StrictStr,
    model_validator,
)

from landscout.common.immutable_mapping import freeze_mapping
from landscout.common.planning_text import (
    normalize_planning_search_text,
    normalize_planning_search_text_with_mapping,
    raw_context_from_spans,
)
from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml
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
    "validate_planning_regulation_structure_with_fragments",
]

SECTION_HASH_SCHEMA_VERSION = 3
STRUCTURE_MANIFEST_SCHEMA_VERSION = 4
_SUPPORTED_CONFIG_SCHEMA_VERSION = 2

_SECTION_TYPES = frozenset({"GENERAL", "ZONE_CHAPTER", "ARTICLE", "OTHER"})
_MAPPING_STATUSES = frozenset({"EXACT", "CONFIG_ALIAS", "UNMAPPED", "AMBIGUOUS"})
_MAPPING_METHODS = frozenset({"EXACT_HEADING", "CONFIG_ALIAS", "NONE", "AMBIGUOUS"})
_EVIDENCE_SCOPES = frozenset({"GENERAL_RULE", "ZONE_SPECIFIC_RULE", "OTHER_TEXT"})

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
                    raise ValueError(
                        f"invalid regular expression: {pattern}"
                    ) from error
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
        object.__setattr__(self, "zone_aliases", freeze_mapping(self.zone_aliases))
        object.__setattr__(self, "topics", freeze_mapping(self.topics))
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
        payload = loads_strict_yaml(config_path.read_bytes())
        if not isinstance(payload, Mapping):
            raise PlanningRegulationStructureError(
                "Planning structure configuration must be a mapping"
            )
        return PlanningRegulationStructureConfig.model_validate(payload)
    except PlanningRegulationStructureError:
        raise
    except StrictYamlError as error:
        raise PlanningRegulationStructureError(str(error)) from error
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
        set(config.document_layout.table_of_contents_pages).difference(indexed_page_set)
    )
    if missing_toc_pages:
        raise PlanningRegulationStructureError(
            "table_of_contents_pages reference nonexistent indexed pages: "
            f"{missing_toc_pages}"
        )
    table_of_contents_pages = set(config.document_layout.table_of_contents_pages)
    failed_body_pages = [
        _strict_positive_integer(row["page_number"], "indexed page number")
        for row in index.pages.to_dict("records")
        if _strict_positive_integer(row["page_number"], "indexed page number")
        >= config.document_layout.body_start_page
        and row["page_number"] not in table_of_contents_pages
        and row["extraction_status"] == "ERROR"
    ]
    if failed_body_pages:
        raise PlanningRegulationStructureError(
            f"Regulation body page extraction status is ERROR: {failed_body_pages}"
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
    if first_nonempty is not None and _matches_any(
        lines[first_nonempty][1].strip(), headers
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
    if last_nonempty is not None and _matches_any(
        lines[last_nonempty][1].strip(), footers
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
            ordered[boundary_index - 1].record_position if boundary_index > 0 else 0
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
            or (not existing.forced_table_of_contents and boundary.event is not None)
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
    content = {
        column: row[column]
        for column in SECTION_COLUMNS
        if column != "section_content_sha256"
    }
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
    if not isinstance(zones, pd.DataFrame) or not isinstance(
        intersections, pd.DataFrame
    ):
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
        raise PlanningRegulationStructureError(
            "Zone document lineage differs from index"
        )
    if not zone_copy["source_archive_sha256"].eq(index.archive_sha256).all():
        raise PlanningRegulationStructureError(
            "Zone archive lineage differs from index"
        )
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
            raise PlanningRegulationStructureError("Intersection areas must be numeric")
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
        raise PlanningRegulationStructureError(
            "Positive zoning relations must be AREA_OVERLAP"
        )
    if not relation_copy.loc[~positive, "relation_type"].eq("TOUCH_ONLY").all():
        raise PlanningRegulationStructureError(
            "Zero-area zoning relations must be TOUCH_ONLY"
        )
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
    parcel_counts = (
        intersections.groupby("zone_label_raw", sort=False)["parcel_id"]
        .nunique()
        .to_dict()
    )
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
                    context_start = max(0, first.normalized_start - context_characters)
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
        raise PlanningRegulationStructureError(
            "Section page_numbers must be a sequence"
        )
    return tuple(
        _strict_positive_integer(item, "section page number") for item in value
    )


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
    record_position = {
        record.record_id: position for position, record in enumerate(records)
    }
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
        for column in (
            "heading_raw",
            "heading_normalized",
            "raw_text",
            "normalized_text",
        ):
            if not isinstance(row[column], str):
                raise PlanningRegulationStructureError(
                    f"Section {column} must be a string"
                )
        if row["heading_normalized"] != _normalize_search_text(row["heading_raw"]):
            raise PlanningRegulationStructureError(
                "Section heading normalization differs"
            )
        if row["normalized_text"] != _normalize_search_text(row["raw_text"]):
            raise PlanningRegulationStructureError("Section text normalization differs")
        if _strict_nonnegative_integer(
            row["character_count"], "character count"
        ) != len(row["raw_text"]):
            raise PlanningRegulationStructureError("Section character count differs")
        start_record_id = _strict_string(row["start_record_id"], "start record ID")
        end_record_id = _strict_string(row["end_record_id"], "end record ID")
        if (
            start_record_id not in record_position
            or end_record_id not in record_position
        ):
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
                record.page_number in config.document_layout.table_of_contents_pages
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
            raise PlanningRegulationStructureError(
                "Section source-record count differs"
            )
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
            raise PlanningRegulationStructureError(
                "Section page references are invalid"
            )
        start = _strict_positive_integer(row["start_page"], "section start page")
        end = _strict_positive_integer(row["end_page"], "section end page")
        if start != pages[0] or end != pages[-1] or end < start:
            raise PlanningRegulationStructureError(
                "Section page range is invalid or unordered"
            )
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
        if (
            _validated_sha256(row["section_content_sha256"], "section content SHA256")
            != expected_hash
        ):
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
            raise PlanningRegulationStructureError(
                "Only articles may have a parent section"
            )
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
    if (
        not isinstance(frame, pd.DataFrame)
        or tuple(frame.columns) != ZONE_MAPPING_COLUMNS
    ):
        raise PlanningRegulationStructureError(
            "Zone mapping schema is not deterministic"
        )
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
            raise PlanningRegulationStructureError(
                "Zone mapping status or method is invalid"
            )
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
                raise PlanningRegulationStructureError(
                    "Zone polygon count must be positive"
                )
        matched = row["matched_section_id"]
        if status in {"EXACT", "CONFIG_ALIAS"}:
            matched_id = _strict_string(matched, "matched section ID")
            if matched_id not in sections.index:
                raise PlanningRegulationStructureError(
                    "Zone mapping section is unknown"
                )
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
            raise PlanningRegulationStructureError(
                "Unresolved zone mapping has a section ID"
            )
        elif (
            status == "UNMAPPED"
            and row["resolved_zone_chapter_label"] is not None
            and not bool(pd.isna(row["resolved_zone_chapter_label"]))
        ):
            raise PlanningRegulationStructureError(
                "Unmapped zone must not claim a resolved chapter label"
            )
        if row["dominant_candidate_count"] > 0 and status not in {
            "EXACT",
            "CONFIG_ALIAS",
        }:
            raise PlanningRegulationStructureError(
                "Dominant candidate zone is unresolved"
            )
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
        raise PlanningRegulationStructureError(
            "Zone mappings must be unique and sorted"
        )


def _validate_topic_evidence(
    index: PlanningRegulationIndex,
    result: PlanningRegulationStructureResult,
    config: PlanningRegulationStructureConfig,
    builds: Sequence[_SectionBuild],
) -> None:
    frame = result.topic_evidence
    if (
        not isinstance(frame, pd.DataFrame)
        or tuple(frame.columns) != TOPIC_EVIDENCE_COLUMNS
    ):
        raise PlanningRegulationStructureError(
            "Topic evidence schema is not deterministic"
        )
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
            raise PlanningRegulationStructureError(
                "Topic evidence topic is unconfigured"
            )
        term = _strict_string(row["search_term"], "search term")
        if term not in config.topics[topic]:
            raise PlanningRegulationStructureError(
                "Topic evidence search term is unconfigured"
            )
        normalized = _strict_string(
            row["normalized_search_term"], "normalized search term"
        )
        if normalized != _normalize_search_text(term):
            raise PlanningRegulationStructureError("Topic search normalization differs")
        section_id = _strict_string(row["section_id"], "topic section ID")
        if section_id not in sections.index:
            raise PlanningRegulationStructureError(
                "Topic evidence references an unknown section"
            )
        page = _strict_positive_integer(row["page_number"], "topic page number")
        if page not in page_set or page not in _page_tuple(
            sections.at[section_id, "page_numbers"]
        ):
            raise PlanningRegulationStructureError(
                "Topic evidence references an unknown page"
            )
        if (section_id, page) not in fragments:
            raise PlanningRegulationStructureError(
                "Topic evidence page is absent from its retained section text"
            )
        count = _strict_positive_integer(
            row["occurrence_count"], "topic occurrence count"
        )
        if count < 1:
            raise PlanningRegulationStructureError("Topic occurrence count is invalid")
        if not isinstance(row["raw_context"], str) or not isinstance(
            row["normalized_context"], str
        ):
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
        context_start = max(0, first.normalized_start - config.topic_context_characters)
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
        raise PlanningRegulationStructureError(
            "Structure result lineage differs from index"
        )
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
        raise PlanningRegulationStructureError(
            "Unsupported section hash schema version"
        )
    _validate_sections(index, result, records, config)
    _validate_zone_mapping(result, config)
    _validate_topic_evidence(index, result, config, builds)
    expected = _result_with_hashes(
        replace(
            result,
            sections_content_sha256="",
            zone_map_content_sha256="",
            topic_evidence_content_sha256="",
            structure_result_content_sha256="",
        )
    )
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
    if (
        _validated_sha256(
            result.structure_result_content_sha256,
            "structure result content SHA256",
        )
        != expected.structure_result_content_sha256
    ):
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
            "structure_result_content_sha256": (result.structure_result_content_sha256),
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

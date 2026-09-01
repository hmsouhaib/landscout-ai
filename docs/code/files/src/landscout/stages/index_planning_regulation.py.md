# `src/landscout/stages/index_planning_regulation.py`

## File identity

- Repository path: `src/landscout/stages/index_planning_regulation.py`
- File type: Python source
- Layer: pipeline stage
- Domain: factual transformation, evidence, or policy boundary
- Responsibility: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.
- Source SHA256: `30246abb4ca296ccfbb4f6d80328883e49f6563191d3ece0ee5aad4184f84a36`

## 1. STEP 7F.1A.4 contract delta

- Ruff formatting only in STEP 7F.1A.4; executable contract, values, schemas, and test intent are unchanged. The companion is refreshed because its raw bytes and SHA changed.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

The file belongs to the **pipeline stage** layer and **factual transformation, evidence, or policy boundary** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import json`
- `from collections.abc import Sequence`
- `from dataclasses import dataclass, replace`
- `from hashlib import sha256`
- `from importlib.metadata import version`
- `from numbers import Integral`
- `from pathlib import Path, PurePosixPath`
- `from re import escape, finditer, fullmatch, sub`
- `from typing import Literal`

### Third-party packages

- `import geopandas as gpd`
- `import pandas as pd`
- `from pypdf import PdfReader`

### Internal LandScout imports

- `from landscout.common import planning_text`
- `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuWrittenFile,
    revalidate_gpu_spatial_layer_source,
)`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `__all__`

- Category: explicit package/module export list.
- Exact declaration:

```python
__all__ = [
    "PlanningRegulationIndex",
    "PlanningRegulationIndexError",
    "PlanningRegulationSearchResult",
    "index_planning_regulation",
    "search_planning_regulation",
    "validate_planning_regulation_index",
    "validate_planning_regulation_search_result",
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `PlanningRegulationIndex`
  - `PlanningRegulationIndexError`
  - `PlanningRegulationSearchResult`
  - `index_planning_regulation`
  - `search_planning_regulation`
  - `validate_planning_regulation_index`
  - `validate_planning_regulation_search_result`

### `SEARCH_NORMALIZATION_PROFILE`

- Category: module constant or closed domain.
- Exact declaration:

```python
SEARCH_NORMALIZATION_PROFILE = planning_text.SEARCH_NORMALIZATION_PROFILE
```

- Qualified consumers:
  - import: `tests.unit.test_index_planning_regulation::<module>` via `from landscout.stages.index_planning_regulation import (
    PAGE_COLUMNS,
    SEARCH_HIT_COLUMNS,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndexError,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`
  - value/type reference: `tests.unit.test_index_planning_regulation::test_search_result_envelope_is_valid_and_deterministic` via `SEARCH_NORMALIZATION_PROFILE`
  - import: `tests.unit.test_interpret_bess_zoning::<module>` via `from landscout.stages.index_planning_regulation import (
    INDEX_HASH_SCHEMA_VERSION,
    PAGE_HASH_SCHEMA_VERSION,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndex,
    _index_content_sha256,
    _normalize_search_text,
    _page_content_sha256,
    _pages_content_sha256,
)`
  - value/type reference: `tests.unit.test_interpret_bess_zoning::_index` via `SEARCH_NORMALIZATION_PROFILE`
  - import: `tests.unit.test_structure_planning_regulation::<module>` via `from landscout.stages.index_planning_regulation import (
    INDEX_HASH_SCHEMA_VERSION,
    PAGE_HASH_SCHEMA_VERSION,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndex,
    _index_content_sha256,
    _normalize_search_text,
    _page_content_sha256,
    _pages_content_sha256,
)`
  - value/type reference: `tests.unit.test_structure_planning_regulation::_index` via `SEARCH_NORMALIZATION_PROFILE`

### `_normalize_search_text`

- Category: module-level alias/value.
- Exact declaration:

```python
_normalize_search_text = planning_text.normalize_planning_search_text
```

- Qualified consumers:
  - import: `tests.unit.test_interpret_bess_zoning::<module>` via `from landscout.stages.index_planning_regulation import (
    INDEX_HASH_SCHEMA_VERSION,
    PAGE_HASH_SCHEMA_VERSION,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndex,
    _index_content_sha256,
    _normalize_search_text,
    _page_content_sha256,
    _pages_content_sha256,
)`
  - direct call: `tests.unit.test_interpret_bess_zoning::_index` via `_normalize_search_text`
  - value/type reference: `tests.unit.test_interpret_bess_zoning::_index` via `_normalize_search_text`
  - import: `tests.unit.test_structure_planning_regulation::<module>` via `from landscout.stages.index_planning_regulation import (
    INDEX_HASH_SCHEMA_VERSION,
    PAGE_HASH_SCHEMA_VERSION,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndex,
    _index_content_sha256,
    _normalize_search_text,
    _page_content_sha256,
    _pages_content_sha256,
)`
  - direct call: `tests.unit.test_structure_planning_regulation::_index` via `_normalize_search_text`
  - value/type reference: `tests.unit.test_structure_planning_regulation::_index` via `_normalize_search_text`
  - direct call: `tests.unit.test_structure_planning_regulation::test_coordinated_section_row_mutation_is_caught_by_outer_envelope` via `_normalize_search_text`
  - value/type reference: `tests.unit.test_structure_planning_regulation::test_coordinated_section_row_mutation_is_caught_by_outer_envelope` via `_normalize_search_text`

### `_normalize_search_text_with_mapping`

- Category: module-level alias/value.
- Exact declaration:

```python
_normalize_search_text_with_mapping = (
    planning_text.normalize_planning_search_text_with_mapping
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_raw_context`

- Category: module-level alias/value.
- Exact declaration:

```python
_raw_context = planning_text.raw_context_from_spans
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `PAGE_HASH_SCHEMA_VERSION`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
PAGE_HASH_SCHEMA_VERSION = 1
```

- Qualified consumers:
  - import: `tests.unit.test_interpret_bess_zoning::<module>` via `from landscout.stages.index_planning_regulation import (
    INDEX_HASH_SCHEMA_VERSION,
    PAGE_HASH_SCHEMA_VERSION,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndex,
    _index_content_sha256,
    _normalize_search_text,
    _page_content_sha256,
    _pages_content_sha256,
)`
  - value/type reference: `tests.unit.test_interpret_bess_zoning::_index` via `PAGE_HASH_SCHEMA_VERSION`
  - import: `tests.unit.test_structure_planning_regulation::<module>` via `from landscout.stages.index_planning_regulation import (
    INDEX_HASH_SCHEMA_VERSION,
    PAGE_HASH_SCHEMA_VERSION,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndex,
    _index_content_sha256,
    _normalize_search_text,
    _page_content_sha256,
    _pages_content_sha256,
)`
  - value/type reference: `tests.unit.test_structure_planning_regulation::_index` via `PAGE_HASH_SCHEMA_VERSION`

### `INDEX_HASH_SCHEMA_VERSION`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
INDEX_HASH_SCHEMA_VERSION = 1
```

- Qualified consumers:
  - import: `tests.unit.test_interpret_bess_zoning::<module>` via `from landscout.stages.index_planning_regulation import (
    INDEX_HASH_SCHEMA_VERSION,
    PAGE_HASH_SCHEMA_VERSION,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndex,
    _index_content_sha256,
    _normalize_search_text,
    _page_content_sha256,
    _pages_content_sha256,
)`
  - value/type reference: `tests.unit.test_interpret_bess_zoning::_index` via `INDEX_HASH_SCHEMA_VERSION`
  - import: `tests.unit.test_structure_planning_regulation::<module>` via `from landscout.stages.index_planning_regulation import (
    INDEX_HASH_SCHEMA_VERSION,
    PAGE_HASH_SCHEMA_VERSION,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndex,
    _index_content_sha256,
    _normalize_search_text,
    _page_content_sha256,
    _pages_content_sha256,
)`
  - value/type reference: `tests.unit.test_structure_planning_regulation::_index` via `INDEX_HASH_SCHEMA_VERSION`

### `SEARCH_HASH_SCHEMA_VERSION`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
SEARCH_HASH_SCHEMA_VERSION = 1
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `PAGE_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
PAGE_COLUMNS = (
    "page_number",
    "extraction_status",
    "raw_text",
    "normalized_search_text",
    "character_count",
    "extraction_error",
    "page_content_sha256",
)
```

- Qualified consumers:
  - import: `tests.unit.test_index_planning_regulation::<module>` via `from landscout.stages.index_planning_regulation import (
    PAGE_COLUMNS,
    SEARCH_HIT_COLUMNS,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndexError,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`
  - value/type reference: `tests.unit.test_index_planning_regulation::test_page_states_numbering_and_hashes` via `PAGE_COLUMNS`
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `page_number`
  - `extraction_status`
  - `raw_text`
  - `normalized_search_text`
  - `character_count`
  - `extraction_error`
  - `page_content_sha256`

### `SEARCH_HIT_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
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
```

- Qualified consumers:
  - import: `tests.unit.test_index_planning_regulation::<module>` via `from landscout.stages.index_planning_regulation import (
    PAGE_COLUMNS,
    SEARCH_HIT_COLUMNS,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndexError,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`
  - value/type reference: `tests.unit.test_index_planning_regulation::test_search_result_envelope_is_valid_and_deterministic` via `SEARCH_HIT_COLUMNS`
  - value/type reference: `tests.unit.test_index_planning_regulation::test_empty_search_result_has_stable_schema_and_lineage` via `SEARCH_HIT_COLUMNS`
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `document_id`
  - `archive_sha256`
  - `pdf_sha256`
  - `search_normalization_profile`
  - `search_term`
  - `normalized_search_term`
  - `page_number`
  - `occurrence_count`
  - `raw_context`
  - `normalized_context`

### `ExtractionStatus`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
ExtractionStatus = Literal["TEXT", "EMPTY", "ERROR"]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_validate_index`

- Category: module-level alias/value.
- Exact declaration:

```python
_validate_index = validate_planning_regulation_index
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `PlanningRegulationIndexError`

**Source purpose:** Raised when regulation indexing or search integrity cannot be proven.

- Exact decorators: none.
- Exact bases: `ValueError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    PlanningRegulationIndexError,
    PlanningRegulationSearchResult,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`
- constructor call: `landscout.stages.index_planning_regulation::_strict_string` via `PlanningRegulationIndexError`
- value/type reference: `landscout.stages.index_planning_regulation::_strict_string` via `PlanningRegulationIndexError`
- constructor call: `landscout.stages.index_planning_regulation::_strict_nonnegative_integer` via `PlanningRegulationIndexError`
- value/type reference: `landscout.stages.index_planning_regulation::_strict_nonnegative_integer` via `PlanningRegulationIndexError`
- constructor call: `landscout.stages.index_planning_regulation::_strict_positive_integer` via `PlanningRegulationIndexError`
- value/type reference: `landscout.stages.index_planning_regulation::_strict_positive_integer` via `PlanningRegulationIndexError`
- constructor call: `landscout.stages.index_planning_regulation::_supported_schema_version` via `PlanningRegulationIndexError`
- value/type reference: `landscout.stages.index_planning_regulation::_supported_schema_version` via `PlanningRegulationIndexError`
- constructor call: `landscout.stages.index_planning_regulation::_validated_sha256` via `PlanningRegulationIndexError`
- value/type reference: `landscout.stages.index_planning_regulation::_validated_sha256` via `PlanningRegulationIndexError`
- constructor call: `landscout.stages.index_planning_regulation::_canonical_sha256` via `PlanningRegulationIndexError`
- value/type reference: `landscout.stages.index_planning_regulation::_canonical_sha256` via `PlanningRegulationIndexError`
- constructor call: `landscout.stages.index_planning_regulation::_is_link_or_junction` via `PlanningRegulationIndexError`
- value/type reference: `landscout.stages.index_planning_regulation::_is_link_or_junction` via `PlanningRegulationIndexError`
- constructor call: `landscout.stages.index_planning_regulation::_validated_relative_path` via `PlanningRegulationIndexError`
- value/type reference: `landscout.stages.index_planning_regulation::_validated_relative_path` via `PlanningRegulationIndexError`
- constructor call: `landscout.stages.index_planning_regulation::_validated_pdf_basename` via `PlanningRegulationIndexError`
- value/type reference: `landscout.stages.index_planning_regulation::_validated_pdf_basename` via `PlanningRegulationIndexError`
- constructor call: `landscout.stages.index_planning_regulation::_file_sha256` via `PlanningRegulationIndexError`
- value/type reference: `landscout.stages.index_planning_regulation::_file_sha256` via `PlanningRegulationIndexError`
- constructor call: `landscout.stages.index_planning_regulation::_revalidate_zoning_source` via `PlanningRegulationIndexError`
- value/type reference: `landscout.stages.index_planning_regulation::_revalidate_zoning_source` via `PlanningRegulationIndexError`
- constructor call: `landscout.stages.index_planning_regulation::_validate_document_lineage` via `PlanningRegulationIndexError`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_document_lineage` via `PlanningRegulationIndexError`
- constructor call: `landscout.stages.index_planning_regulation::_zoning_regulation_filenames` via `PlanningRegulationIndexError`
- value/type reference: `landscout.stages.index_planning_regulation::_zoning_regulation_filenames` via `PlanningRegulationIndexError`
- constructor call: `landscout.stages.index_planning_regulation::_written_file_matches` via `PlanningRegulationIndexError`
- value/type reference: `landscout.stages.index_planning_regulation::_written_file_matches` via `PlanningRegulationIndexError`
- constructor call: `landscout.stages.index_planning_regulation::_resolve_regulation_filename` via `PlanningRegulationIndexError`
- value/type reference: `landscout.stages.index_planning_regulation::_resolve_regulation_filename` via `PlanningRegulationIndexError`
- constructor call: `landscout.stages.index_planning_regulation::_locate_regulation_pdf` via `PlanningRegulationIndexError`
- value/type reference: `landscout.stages.index_planning_regulation::_locate_regulation_pdf` via `PlanningRegulationIndexError`
- constructor call: `landscout.stages.index_planning_regulation::_validate_pages` via `PlanningRegulationIndexError`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_pages` via `PlanningRegulationIndexError`
- constructor call: `landscout.stages.index_planning_regulation::_pypdf_version` via `PlanningRegulationIndexError`
- value/type reference: `landscout.stages.index_planning_regulation::_pypdf_version` via `PlanningRegulationIndexError`
- constructor call: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `PlanningRegulationIndexError`
- value/type reference: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `PlanningRegulationIndexError`
- constructor call: `landscout.stages.index_planning_regulation::index_planning_regulation` via `PlanningRegulationIndexError`
- value/type reference: `landscout.stages.index_planning_regulation::index_planning_regulation` via `PlanningRegulationIndexError`
- constructor call: `landscout.stages.index_planning_regulation::_validate_planning_regulation_index` via `PlanningRegulationIndexError`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_planning_regulation_index` via `PlanningRegulationIndexError`
- constructor call: `landscout.stages.index_planning_regulation::validate_planning_regulation_index` via `PlanningRegulationIndexError`
- value/type reference: `landscout.stages.index_planning_regulation::validate_planning_regulation_index` via `PlanningRegulationIndexError`
- constructor call: `landscout.stages.index_planning_regulation::_validated_terms` via `PlanningRegulationIndexError`
- value/type reference: `landscout.stages.index_planning_regulation::_validated_terms` via `PlanningRegulationIndexError`
- constructor call: `landscout.stages.index_planning_regulation::_validate_planning_regulation_search_result` via `PlanningRegulationIndexError`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_planning_regulation_search_result` via `PlanningRegulationIndexError`
- constructor call: `landscout.stages.index_planning_regulation::validate_planning_regulation_search_result` via `PlanningRegulationIndexError`
- value/type reference: `landscout.stages.index_planning_regulation::validate_planning_regulation_search_result` via `PlanningRegulationIndexError`
- import: `tests.unit.test_index_planning_regulation::<module>` via `from landscout.stages.index_planning_regulation import (
    PAGE_COLUMNS,
    SEARCH_HIT_COLUMNS,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndexError,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`
- value/type reference: `tests.unit.test_index_planning_regulation::test_mutated_loaded_nomfic_is_rejected_before_selection` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_mutated_loaded_zoning_geometry_or_order_is_rejected` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_zoning_source_bytes_changed_after_ingestion_are_rejected` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_zoning_source_inventory_integrity_mismatch_is_rejected` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_missing_nomfic_field_is_rejected` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_null_nomfic_is_rejected` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_multiple_nomfic_values_are_ambiguous` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_unsafe_explicit_filename_is_rejected` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_explicit_filename_not_referenced_by_zoning_fails` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_filename_absent_from_written_files_fails` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_filename_absent_from_inventory_fails` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_duplicate_inventory_basename_fails` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_path_outside_root_is_rejected` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_pdf_inventory_integrity_mismatch_fails` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_zero_page_pdf_is_rejected` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_pdf_reader_failure_is_controlled_and_chained` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_version_discovery_failure_is_controlled_and_chained` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_coordinated_page_mutation_fails_envelope_hash` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_index_integrity_mutations_fail` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_complete_index_envelope_mutation_is_rejected` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_unsupported_or_malformed_index_hash_schema_is_rejected` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_malformed_page_hash_schema_is_rejected_as_controlled_error` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_search_index_identity_schema_and_terms_are_sealed` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_search_requested_terms_must_be_an_immutable_exact_tuple` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_search_result_integrity_mutations_fail` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_search_hit_lineage_mutation_fails` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_invalid_search_term_is_rejected` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_duplicate_normalized_search_terms_are_rejected` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_malformed_page_value_raises_controlled_index_error` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_malformed_hit_value_raises_controlled_index_error` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_canonical_hash_serialization_failure_is_controlled_and_chained` via `PlanningRegulationIndexError`
- value/type reference: `tests.unit.test_index_planning_regulation::test_malformed_source_metadata_raises_controlled_index_error` via `PlanningRegulationIndexError`

**Exact class source**

```python
class PlanningRegulationIndexError(ValueError):
    """Raised when regulation indexing or search integrity cannot be proven."""
```

### `PlanningRegulationIndex`

**Source purpose:** Immutable lineage envelope around a deterministic page text table.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `document_id` | `str` | `required` | `document_id: str` |
| `archive_sha256` | `str` | `required` | `archive_sha256: str` |
| `regulation_filename` | `str` | `required` | `regulation_filename: str` |
| `source_selection_method` | `str` | `required` | `source_selection_method: str` |
| `source_selection_sha256` | `str` | `required` | `source_selection_sha256: str` |
| `pdf_relative_path` | `str` | `required` | `pdf_relative_path: str` |
| `pdf_size_bytes` | `int` | `required` | `pdf_size_bytes: int` |
| `pdf_sha256` | `str` | `required` | `pdf_sha256: str` |
| `extraction_library` | `str` | `required` | `extraction_library: str` |
| `extraction_library_version` | `str` | `required` | `extraction_library_version: str` |
| `search_normalization_profile` | `str` | `required` | `search_normalization_profile: str` |
| `page_hash_schema_version` | `int` | `required` | `page_hash_schema_version: int` |
| `index_hash_schema_version` | `int` | `required` | `index_hash_schema_version: int` |
| `total_page_count` | `int` | `required` | `total_page_count: int` |
| `pages_content_sha256` | `str` | `required` | `pages_content_sha256: str` |
| `index_content_sha256` | `str` | `required` | `index_content_sha256: str` |
| `pages` | `pd.DataFrame` | `required` | `pages: pd.DataFrame` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    PlanningRegulationIndexError,
    PlanningRegulationSearchResult,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`
- value/type reference: `landscout.stages.index_planning_regulation::_index_hash_payload` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.index_planning_regulation::_index_content_sha256` via `PlanningRegulationIndex`
- constructor call: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.index_planning_regulation::index_planning_regulation` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_planning_regulation_index` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.index_planning_regulation::validate_planning_regulation_index` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.index_planning_regulation::_build_hits` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.index_planning_regulation::_hits_content_sha256` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.index_planning_regulation::search_planning_regulation` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_planning_regulation_search_result` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.index_planning_regulation::validate_planning_regulation_search_result` via `PlanningRegulationIndex`
- import: `landscout.stages.interpret_bess_zoning::<module>` via `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    validate_planning_regulation_index,
)`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_policy_lock` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_parcels` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_zones` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_relations` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_policy_evidence` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.interpret_bess_zoning::_lineage` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_chapter_policy` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_route_assessments` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_evidence_route_links` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_source_zone_policy` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_parcel_zone_interpretations` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_result` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.interpret_bess_zoning::validate_bess_zoning_precheck` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.interpret_bess_zoning::interpret_bess_zoning` via `PlanningRegulationIndex`
- import: `landscout.stages.structure_planning_regulation::<module>` via `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    validate_planning_regulation_index,
)`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_document_lock` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.structure_planning_regulation::_line_records` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_sections` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.structure_planning_regulation::_validated_zoning_inputs` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_zone_mapping` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_topic_evidence` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_sections` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_topic_evidence` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_structure_result` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_result_self` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.structure_planning_regulation::validate_planning_regulation_structure_with_fragments` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.structure_planning_regulation::validate_planning_regulation_structure` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.structure_planning_regulation::planning_regulation_section_page_fragments` via `PlanningRegulationIndex`
- value/type reference: `landscout.stages.structure_planning_regulation::structure_planning_regulation` via `PlanningRegulationIndex`
- import: `tests.integration.test_gpu_planning_end_to_end::<module>` via `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    index_planning_regulation,
)`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_structure_config` via `PlanningRegulationIndex`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_policy` via `PlanningRegulationIndex`
- import: `tests.unit.test_interpret_bess_zoning::<module>` via `from landscout.stages.index_planning_regulation import (
    INDEX_HASH_SCHEMA_VERSION,
    PAGE_HASH_SCHEMA_VERSION,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndex,
    _index_content_sha256,
    _normalize_search_text,
    _page_content_sha256,
    _pages_content_sha256,
)`
- constructor call: `tests.unit.test_interpret_bess_zoning::_index` via `PlanningRegulationIndex`
- value/type reference: `tests.unit.test_interpret_bess_zoning::_index` via `PlanningRegulationIndex`
- value/type reference: `tests.unit.test_interpret_bess_zoning::_zones` via `PlanningRegulationIndex`
- value/type reference: `tests.unit.test_interpret_bess_zoning::_relations` via `PlanningRegulationIndex`
- value/type reference: `tests.unit.test_interpret_bess_zoning::_structure_config` via `PlanningRegulationIndex`
- value/type reference: `tests.unit.test_interpret_bess_zoning::_parcels` via `PlanningRegulationIndex`
- import: `tests.unit.test_structure_planning_regulation::<module>` via `from landscout.stages.index_planning_regulation import (
    INDEX_HASH_SCHEMA_VERSION,
    PAGE_HASH_SCHEMA_VERSION,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndex,
    _index_content_sha256,
    _normalize_search_text,
    _page_content_sha256,
    _pages_content_sha256,
)`
- constructor call: `tests.unit.test_structure_planning_regulation::_index` via `PlanningRegulationIndex`
- value/type reference: `tests.unit.test_structure_planning_regulation::_index` via `PlanningRegulationIndex`
- value/type reference: `tests.unit.test_structure_planning_regulation::_config` via `PlanningRegulationIndex`
- value/type reference: `tests.unit.test_structure_planning_regulation::_zones` via `PlanningRegulationIndex`
- value/type reference: `tests.unit.test_structure_planning_regulation::_intersections` via `PlanningRegulationIndex`
- value/type reference: `tests.unit.test_structure_planning_regulation::_validate` via `PlanningRegulationIndex`
- value/type reference: `tests.unit.test_structure_planning_regulation::_config_with_structural_patterns` via `PlanningRegulationIndex`

**Exact class source**

```python
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
```

### `PlanningRegulationSearchResult`

**Source purpose:** Immutable lineage envelope around deterministic factual search hits.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `document_id` | `str` | `required` | `document_id: str` |
| `archive_sha256` | `str` | `required` | `archive_sha256: str` |
| `pdf_sha256` | `str` | `required` | `pdf_sha256: str` |
| `search_normalization_profile` | `str` | `required` | `search_normalization_profile: str` |
| `search_hash_schema_version` | `int` | `required` | `search_hash_schema_version: int` |
| `index_content_sha256` | `str` | `required` | `index_content_sha256: str` |
| `requested_terms` | `tuple[str, ...]` | `required` | `requested_terms: tuple[str, ...]` |
| `context_characters` | `int` | `required` | `context_characters: int` |
| `hit_count` | `int` | `required` | `hit_count: int` |
| `hits_content_sha256` | `str` | `required` | `hits_content_sha256: str` |
| `hits` | `pd.DataFrame` | `required` | `hits: pd.DataFrame` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    PlanningRegulationIndexError,
    PlanningRegulationSearchResult,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`
- constructor call: `landscout.stages.index_planning_regulation::search_planning_regulation` via `PlanningRegulationSearchResult`
- value/type reference: `landscout.stages.index_planning_regulation::search_planning_regulation` via `PlanningRegulationSearchResult`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_planning_regulation_search_result` via `PlanningRegulationSearchResult`
- value/type reference: `landscout.stages.index_planning_regulation::validate_planning_regulation_search_result` via `PlanningRegulationSearchResult`

**Exact class source**

```python
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
```

### `_ZoningSourceFileIntegrity`

**Source purpose:** Defines `_ZoningSourceFileIntegrity`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `relative_path` | `str` | `required` | `relative_path: str` |
| `size_bytes` | `int` | `required` | `size_bytes: int` |
| `sha256` | `str` | `required` | `sha256: str` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.stages.index_planning_regulation::_revalidate_zoning_source` via `_ZoningSourceFileIntegrity`
- value/type reference: `landscout.stages.index_planning_regulation::_revalidate_zoning_source` via `_ZoningSourceFileIntegrity`

**Exact class source**

```python
class _ZoningSourceFileIntegrity:
    relative_path: str
    size_bytes: int
    sha256: str
```

### `_ZoningSourceEvidence`

**Source purpose:** Defines `_ZoningSourceEvidence`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `source_layer` | `str` | `required` | `source_layer: str` |
| `driver` | `str` | `required` | `driver: str` |
| `files` | `tuple[_ZoningSourceFileIntegrity, ...]` | `required` | `files: tuple[_ZoningSourceFileIntegrity, ...]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.stages.index_planning_regulation::_revalidate_zoning_source` via `_ZoningSourceEvidence`
- value/type reference: `landscout.stages.index_planning_regulation::_revalidate_zoning_source` via `_ZoningSourceEvidence`
- value/type reference: `landscout.stages.index_planning_regulation::_resolve_regulation_filename` via `_ZoningSourceEvidence`
- value/type reference: `landscout.stages.index_planning_regulation::_source_selection_sha256` via `_ZoningSourceEvidence`

**Exact class source**

```python
class _ZoningSourceEvidence:
    source_layer: str
    driver: str
    files: tuple[_ZoningSourceFileIntegrity, ...]
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_strict_string`

**Purpose:** Implements `strict string` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

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
  - `PlanningRegulationIndexError(f"{label} must be a non-empty exact string")` under lexical guard `not isinstance(value, str) or not value or value != value.strip()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::_validated_sha256` via `_strict_string`
- value/type reference: `landscout.stages.index_planning_regulation::_validated_sha256` via `_strict_string`
- direct call: `landscout.stages.index_planning_regulation::_validated_relative_path` via `_strict_string`
- value/type reference: `landscout.stages.index_planning_regulation::_validated_relative_path` via `_strict_string`
- direct call: `landscout.stages.index_planning_regulation::_validated_pdf_basename` via `_strict_string`
- value/type reference: `landscout.stages.index_planning_regulation::_validated_pdf_basename` via `_strict_string`
- direct call: `landscout.stages.index_planning_regulation::_validate_document_lineage` via `_strict_string`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_document_lineage` via `_strict_string`
- direct call: `landscout.stages.index_planning_regulation::_written_file_matches` via `_strict_string`
- value/type reference: `landscout.stages.index_planning_regulation::_written_file_matches` via `_strict_string`
- direct call: `landscout.stages.index_planning_regulation::_locate_regulation_pdf` via `_strict_string`
- value/type reference: `landscout.stages.index_planning_regulation::_locate_regulation_pdf` via `_strict_string`
- direct call: `landscout.stages.index_planning_regulation::_validate_planning_regulation_index` via `_strict_string`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_planning_regulation_index` via `_strict_string`
- direct call: `landscout.stages.index_planning_regulation::_validated_terms` via `_strict_string`
- value/type reference: `landscout.stages.index_planning_regulation::_validated_terms` via `_strict_string`
- direct call: `landscout.stages.index_planning_regulation::_validate_planning_regulation_search_result` via `_strict_string`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_planning_regulation_search_result` via `_strict_string`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationIndexError` | `landscout.stages.index_planning_regulation.PlanningRegulationIndexError` |

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
        raise PlanningRegulationIndexError(f"{label} must be a non-empty exact string")
    return value
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_strict_nonnegative_integer`

**Purpose:** Implements `strict nonnegative integer` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

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
  - `int(value)`
- Explicit raise paths:
  - `PlanningRegulationIndexError(f"{label} must be an integer")` under lexical guard `isinstance(value, bool) or not isinstance(value, Integral)`.
  - `PlanningRegulationIndexError(f"{label} must be non-negative")` under lexical guard `value < 0`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::_strict_positive_integer` via `_strict_nonnegative_integer`
- value/type reference: `landscout.stages.index_planning_regulation::_strict_positive_integer` via `_strict_nonnegative_integer`
- direct call: `landscout.stages.index_planning_regulation::_validate_pages` via `_strict_nonnegative_integer`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_pages` via `_strict_nonnegative_integer`
- direct call: `landscout.stages.index_planning_regulation::search_planning_regulation` via `_strict_nonnegative_integer`
- value/type reference: `landscout.stages.index_planning_regulation::search_planning_regulation` via `_strict_nonnegative_integer`
- direct call: `landscout.stages.index_planning_regulation::_validate_planning_regulation_search_result` via `_strict_nonnegative_integer`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_planning_regulation_search_result` via `_strict_nonnegative_integer`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationIndexError` | `landscout.stages.index_planning_regulation.PlanningRegulationIndexError` |
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
        raise PlanningRegulationIndexError(f"{label} must be an integer")
    if value < 0:
        raise PlanningRegulationIndexError(f"{label} must be non-negative")
    return int(value)
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_strict_positive_integer`

**Purpose:** Implements `strict positive integer` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

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
  - `PlanningRegulationIndexError(f"{label} must be positive")` under lexical guard `result == 0`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::_supported_schema_version` via `_strict_positive_integer`
- value/type reference: `landscout.stages.index_planning_regulation::_supported_schema_version` via `_strict_positive_integer`
- direct call: `landscout.stages.index_planning_regulation::_locate_regulation_pdf` via `_strict_positive_integer`
- value/type reference: `landscout.stages.index_planning_regulation::_locate_regulation_pdf` via `_strict_positive_integer`
- direct call: `landscout.stages.index_planning_regulation::_validate_pages` via `_strict_positive_integer`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_pages` via `_strict_positive_integer`
- direct call: `landscout.stages.index_planning_regulation::_validate_planning_regulation_index` via `_strict_positive_integer`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_planning_regulation_index` via `_strict_positive_integer`
- direct call: `landscout.stages.index_planning_regulation::_validate_planning_regulation_search_result` via `_strict_positive_integer`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_planning_regulation_search_result` via `_strict_positive_integer`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_strict_nonnegative_integer` | `landscout.stages.index_planning_regulation._strict_nonnegative_integer` |
| `PlanningRegulationIndexError` | `landscout.stages.index_planning_regulation.PlanningRegulationIndexError` |

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
        raise PlanningRegulationIndexError(f"{label} must be positive")
    return result
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_supported_schema_version`

**Purpose:** Implements `supported schema version` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

**Exact signature**

```python
def _supported_schema_version(value: object, supported: int, label: str) -> int:
```

- Exact decorators: none.
- Declared return annotation: `int`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `supported` | positional-or-keyword | `int` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- Explicit raise paths:
  - `PlanningRegulationIndexError(<br>            f"Unsupported {label}: {result}; expected {supported}"<br>        )` under lexical guard `result != supported`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::_validate_planning_regulation_index` via `_supported_schema_version`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_planning_regulation_index` via `_supported_schema_version`
- direct call: `landscout.stages.index_planning_regulation::_validate_planning_regulation_search_result` via `_supported_schema_version`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_planning_regulation_search_result` via `_supported_schema_version`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_strict_positive_integer` | `landscout.stages.index_planning_regulation._strict_positive_integer` |
| `PlanningRegulationIndexError` | `landscout.stages.index_planning_regulation.PlanningRegulationIndexError` |

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
def _supported_schema_version(value: object, supported: int, label: str) -> int:
    result = _strict_positive_integer(value, label)
    if result != supported:
        raise PlanningRegulationIndexError(
            f"Unsupported {label}: {result}; expected {supported}"
        )
    return result
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validated_sha256`

**Purpose:** Implements `validated sha256` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

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
  - `PlanningRegulationIndexError(<br>            f"{label} must contain exactly 64 lowercase hexadecimal characters"<br>        )` under lexical guard `fullmatch(r"[0-9a-f]{64}", checksum) is None`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::_validate_document_lineage` via `_validated_sha256`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_document_lineage` via `_validated_sha256`
- direct call: `landscout.stages.index_planning_regulation::_locate_regulation_pdf` via `_validated_sha256`
- value/type reference: `landscout.stages.index_planning_regulation::_locate_regulation_pdf` via `_validated_sha256`
- direct call: `landscout.stages.index_planning_regulation::_validate_pages` via `_validated_sha256`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_pages` via `_validated_sha256`
- direct call: `landscout.stages.index_planning_regulation::_validate_planning_regulation_index` via `_validated_sha256`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_planning_regulation_index` via `_validated_sha256`
- direct call: `landscout.stages.index_planning_regulation::_validate_planning_regulation_search_result` via `_validated_sha256`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_planning_regulation_search_result` via `_validated_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_strict_string` | `landscout.stages.index_planning_regulation._strict_string` |
| `fullmatch` | `re.fullmatch` |
| `PlanningRegulationIndexError` | `landscout.stages.index_planning_regulation.PlanningRegulationIndexError` |

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
    if fullmatch(r"[0-9a-f]{64}", checksum) is None:
        raise PlanningRegulationIndexError(
            f"{label} must contain exactly 64 lowercase hexadecimal characters"
        )
    return checksum
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_canonical_sha256`

**Purpose:** Implements `canonical sha256` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

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
  - `sha256(payload).hexdigest()`
- Explicit raise paths:
  - `PlanningRegulationIndexError(<br>            "Canonical integrity payload cannot be serialized"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::_page_content_sha256` via `_canonical_sha256`
- value/type reference: `landscout.stages.index_planning_regulation::_page_content_sha256` via `_canonical_sha256`
- direct call: `landscout.stages.index_planning_regulation::_pages_content_sha256` via `_canonical_sha256`
- value/type reference: `landscout.stages.index_planning_regulation::_pages_content_sha256` via `_canonical_sha256`
- direct call: `landscout.stages.index_planning_regulation::_index_content_sha256` via `_canonical_sha256`
- value/type reference: `landscout.stages.index_planning_regulation::_index_content_sha256` via `_canonical_sha256`
- direct call: `landscout.stages.index_planning_regulation::_source_selection_sha256` via `_canonical_sha256`
- value/type reference: `landscout.stages.index_planning_regulation::_source_selection_sha256` via `_canonical_sha256`
- direct call: `landscout.stages.index_planning_regulation::_hits_content_sha256` via `_canonical_sha256`
- value/type reference: `landscout.stages.index_planning_regulation::_hits_content_sha256` via `_canonical_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `json.dumps(<br>            value,<br>            ensure_ascii=False,<br>            allow_nan=False,<br>            sort_keys=True,<br>            separators=(",", ":"),<br>        ).encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `PlanningRegulationIndexError` | `landscout.stages.index_planning_regulation.PlanningRegulationIndexError` |
| `sha256(payload).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(payload).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_is_link_or_junction`

**Purpose:** Implements `is link or junction` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

**Exact signature**

```python
def _is_link_or_junction(path: Path) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `path.is_symlink() or path.is_junction()`
- Explicit raise paths:
  - `PlanningRegulationIndexError(<br>            f"Cannot inspect GPU extraction path safely: {path}"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::_locate_regulation_pdf` via `_is_link_or_junction`
- value/type reference: `landscout.stages.index_planning_regulation::_locate_regulation_pdf` via `_is_link_or_junction`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.is_symlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_junction` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationIndexError` | `landscout.stages.index_planning_regulation.PlanningRegulationIndexError` |

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
def _is_link_or_junction(path: Path) -> bool:
    try:
        return path.is_symlink() or path.is_junction()
    except OSError as error:
        raise PlanningRegulationIndexError(
            f"Cannot inspect GPU extraction path safely: {path}"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validated_relative_path`

**Purpose:** Implements `validated relative path` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

**Exact signature**

```python
def _validated_relative_path(value: object) -> PurePosixPath:
```

- Exact decorators: none.
- Declared return annotation: `PurePosixPath`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `relative`
- Explicit raise paths:
  - `PlanningRegulationIndexError("GPU inventory path is unsafe")` under lexical guard `"\\" in raw or "\x00" in raw`.
  - `PlanningRegulationIndexError("GPU inventory path is unsafe")` under lexical guard `any(part in {"", ".", ".."} for part in parts)`.
  - `PlanningRegulationIndexError("GPU inventory path is unsafe")` under lexical guard `relative.is_absolute() or relative.as_posix() != raw`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::_locate_regulation_pdf` via `_validated_relative_path`
- value/type reference: `landscout.stages.index_planning_regulation::_locate_regulation_pdf` via `_validated_relative_path`
- direct call: `landscout.stages.index_planning_regulation::_validate_planning_regulation_index` via `_validated_relative_path`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_planning_regulation_index` via `_validated_relative_path`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_strict_string` | `landscout.stages.index_planning_regulation._strict_string` |
| `PlanningRegulationIndexError` | `landscout.stages.index_planning_regulation.PlanningRegulationIndexError` |
| `raw.split` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `PurePosixPath` | `pathlib.PurePosixPath` |
| `relative.is_absolute` | `unresolved local/third-party receiver; no ownership inferred` |
| `relative.as_posix` | `unresolved local/third-party receiver; no ownership inferred` |

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
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validated_pdf_basename`

**Purpose:** Implements `validated pdf basename` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

**Exact signature**

```python
def _validated_pdf_basename(value: object) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `name`
- Explicit raise paths:
  - `PlanningRegulationIndexError(<br>            "regulation PDF filename must be one safe PDF basename"<br>        )` under lexical guard `name in {".", ".."}<br>        or "/" in name<br>        or "\\" in name<br>        or Path(name).name != name<br>        or not name.casefold().endswith(".pdf")<br>        or any(ord(character) < 32 or ord(character) == 127 for character in name)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::_zoning_regulation_filenames` via `_validated_pdf_basename`
- value/type reference: `landscout.stages.index_planning_regulation::_zoning_regulation_filenames` via `_validated_pdf_basename`
- direct call: `landscout.stages.index_planning_regulation::_resolve_regulation_filename` via `_validated_pdf_basename`
- value/type reference: `landscout.stages.index_planning_regulation::_resolve_regulation_filename` via `_validated_pdf_basename`
- direct call: `landscout.stages.index_planning_regulation::_validate_planning_regulation_index` via `_validated_pdf_basename`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_planning_regulation_index` via `_validated_pdf_basename`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_strict_string` | `landscout.stages.index_planning_regulation._strict_string` |
| `Path` | `pathlib.Path` |
| `name.casefold().endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `name.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `ord` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationIndexError` | `landscout.stages.index_planning_regulation.PlanningRegulationIndexError` |

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
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_file_sha256`

**Purpose:** Implements `file sha256` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

**Exact signature**

```python
def _file_sha256(path: Path) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `digest.hexdigest()`
- Explicit raise paths:
  - `PlanningRegulationIndexError(<br>            "Regulation PDF checksum cannot be calculated"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::_locate_regulation_pdf` via `_file_sha256`
- value/type reference: `landscout.stages.index_planning_regulation::_locate_regulation_pdf` via `_file_sha256`
- direct call: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `_file_sha256`
- value/type reference: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `_file_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `sha256` | `hashlib.sha256` |
| `path.open` | `unresolved local/third-party receiver; no ownership inferred` |
| `stream.read` | `unresolved local/third-party receiver; no ownership inferred` |
| `digest.update` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationIndexError` | `landscout.stages.index_planning_regulation.PlanningRegulationIndexError` |
| `digest.hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.open` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `digest.update(chunk)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_revalidate_zoning_source`

**Purpose:** Re-read immutable zoning bytes before trusting source PDF references.

**Exact signature**

```python
def _revalidate_zoning_source(
    planning_document: GpuPlanningDocument,
) -> tuple[gpd.GeoDataFrame, _ZoningSourceEvidence]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[gpd.GeoDataFrame, _ZoningSourceEvidence]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `source.data, _ZoningSourceEvidence(<br>            source_layer=source.source_layer,<br>            driver=source.driver,<br>            files=tuple(<br>                _ZoningSourceFileIntegrity(<br>                    relative_path=item.relative_path,<br>                    size_bytes=item.size_bytes,<br>                    sha256=item.sha256,<br>                )<br>                for item in source.files<br>            ),<br>        )`
- Explicit raise paths:
  - `PlanningRegulationIndexError("GPU zoning is missing NOMFIC")` under lexical guard `"NOMFIC" not in source.data.columns`.
  - `re-raise`.
  - `PlanningRegulationIndexError(<br>            f"GPU zoning source integrity cannot be revalidated: {error}"<br>        )`.
  - `PlanningRegulationIndexError(<br>            "GPU zoning source cannot be revalidated"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::_resolve_regulation_filename` via `_revalidate_zoning_source`
- value/type reference: `landscout.stages.index_planning_regulation::_resolve_regulation_filename` via `_revalidate_zoning_source`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `revalidate_gpu_spatial_layer_source` | `landscout.sources.gpu_fr.revalidate_gpu_spatial_layer_source` |
| `PlanningRegulationIndexError` | `landscout.stages.index_planning_regulation.PlanningRegulationIndexError` |
| `_ZoningSourceEvidence` | `landscout.stages.index_planning_regulation._ZoningSourceEvidence` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `_ZoningSourceFileIntegrity` | `landscout.stages.index_planning_regulation._ZoningSourceFileIntegrity` |

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
def _revalidate_zoning_source(
    planning_document: GpuPlanningDocument,
) -> tuple[gpd.GeoDataFrame, _ZoningSourceEvidence]:
    """Re-read immutable zoning bytes before trusting source PDF references."""

    try:
        source = revalidate_gpu_spatial_layer_source(
            planning_document, planning_document.zoning
        )
        if "NOMFIC" not in source.data.columns:
            raise PlanningRegulationIndexError("GPU zoning is missing NOMFIC")
        return source.data, _ZoningSourceEvidence(
            source_layer=source.source_layer,
            driver=source.driver,
            files=tuple(
                _ZoningSourceFileIntegrity(
                    relative_path=item.relative_path,
                    size_bytes=item.size_bytes,
                    sha256=item.sha256,
                )
                for item in source.files
            ),
        )
    except PlanningRegulationIndexError:
        raise
    except GpuSpatialInspectionError as error:
        raise PlanningRegulationIndexError(
            f"GPU zoning source integrity cannot be revalidated: {error}"
        ) from error
    except Exception as error:
        raise PlanningRegulationIndexError(
            "GPU zoning source cannot be revalidated"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_document_lineage`

**Purpose:** Implements `validate document lineage` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

**Exact signature**

```python
def _validate_document_lineage(
    planning_document: GpuPlanningDocument,
) -> tuple[str, str]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[str, str]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `document_id, archive_sha`
- Explicit raise paths:
  - `PlanningRegulationIndexError(<br>            "planning_document must be a GpuPlanningDocument"<br>        )` under lexical guard `not isinstance(planning_document, GpuPlanningDocument)`.
  - `PlanningRegulationIndexError("GPU extraction lineage is invalid")` under lexical guard `not isinstance(extraction, GpuExtraction)`.
  - `PlanningRegulationIndexError("GPU archive lineage is invalid")` under lexical guard `not isinstance(archive, GpuArchiveDownload) or not isinstance(<br>        archive.document, GpuDocumentMetadata<br>    )`.
  - `PlanningRegulationIndexError("GPU archive format must be zip")` under lexical guard `not isinstance(archive.archive_format, str) or (<br>        archive.archive_format.casefold() != "zip"<br>    )`.
  - `PlanningRegulationIndexError(<br>            "GPU planning document is not the current effective DU"<br>        )` under lexical guard `metadata.document_family != "DU"<br>        or metadata.status != "document.production"<br>        or metadata.legal_status != "APPROVED"<br>        or metadata.effective_status != "EN_VIGUEUR"`.
  - `PlanningRegulationIndexError("GPU spatial-layer lineage is invalid")` under lexical guard `type(planning_document.related_layers) is not tuple<br>        or type(planning_document.all_spatial_layers) is not tuple`.
  - `PlanningRegulationIndexError("GPU zoning logical layer is invalid")` under lexical guard `planning_document.zoning.logical_name != "zoning"`.
  - `PlanningRegulationIndexError(<br>            "GPU zoning reference is absent from discovered spatial layers"<br>        )` under lexical guard `planning_document.zoning.reference not in planning_document.all_spatial_layers`.
  - `PlanningRegulationIndexError(<br>                "GPU spatial-layer lineage is inconsistent with the archive"<br>            )` under lexical guard `layer.summary.source_document_id != document_id<br>            or layer.summary.source_archive_sha256 != archive_sha<br>            or layer.summary.source_layer != layer.reference.source_layer<br>            or layer.summary.feature_count != len(layer.data)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `_validate_document_lineage`
- value/type reference: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `_validate_document_lineage`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationIndexError` | `landscout.stages.index_planning_regulation.PlanningRegulationIndexError` |
| `_strict_string` | `landscout.stages.index_planning_regulation._strict_string` |
| `_validated_sha256` | `landscout.stages.index_planning_regulation._validated_sha256` |
| `archive.archive_format.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_validated_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_document_lineage(
    planning_document: GpuPlanningDocument,
) -> tuple[str, str]:
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
    if (
        type(planning_document.related_layers) is not tuple
        or type(planning_document.all_spatial_layers) is not tuple
    ):
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
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_zoning_regulation_filenames`

**Purpose:** Implements `zoning regulation filenames` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

**Exact signature**

```python
def _zoning_regulation_filenames(zoning: gpd.GeoDataFrame) -> tuple[str, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[str, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `zoning` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `tuple(sorted(values, key=str.casefold))`
- Explicit raise paths:
  - `PlanningRegulationIndexError("GPU zoning is missing NOMFIC")` under lexical guard `"NOMFIC" not in zoning.columns`.
  - `re-raise`.
  - `PlanningRegulationIndexError(<br>            "GPU zoning NOMFIC values cannot be validated"<br>        )`.
  - `PlanningRegulationIndexError(<br>            "GPU zoning NOMFIC contains no regulation filename"<br>        )` under lexical guard `not values`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::_resolve_regulation_filename` via `_zoning_regulation_filenames`
- value/type reference: `landscout.stages.index_planning_regulation::_resolve_regulation_filename` via `_zoning_regulation_filenames`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `PlanningRegulationIndexError` | `landscout.stages.index_planning_regulation.PlanningRegulationIndexError` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `zoning["NOMFIC"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.isna` | `pandas.isna` |
| `values.add` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_pdf_basename` | `landscout.stages.index_planning_regulation._validated_pdf_basename` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `values.add(_validated_pdf_basename(value))` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _zoning_regulation_filenames(zoning: gpd.GeoDataFrame) -> tuple[str, ...]:
    if "NOMFIC" not in zoning.columns:
        raise PlanningRegulationIndexError("GPU zoning is missing NOMFIC")
    values: set[str] = set()
    try:
        source_values = zoning["NOMFIC"].tolist()
        for value in source_values:
            if (
                value is None
                or value is pd.NA
                or (isinstance(value, float) and pd.isna(value))
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
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_written_file_matches`

**Purpose:** Implements `written file matches` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

**Exact signature**

```python
def _written_file_matches(
    planning_document: GpuPlanningDocument, filename: str
) -> tuple[GpuWrittenFile, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[GpuWrittenFile, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |
| `filename` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `tuple(matches)`
- Explicit raise paths:
  - `PlanningRegulationIndexError(<br>            "GPU written-files metadata must be an immutable tuple"<br>        )` under lexical guard `type(written_files) is not tuple`.
  - `PlanningRegulationIndexError("GPU written-files metadata is invalid")` under lexical guard `not isinstance(item, GpuWrittenFile)`.
  - `PlanningRegulationIndexError(<br>            f"Regulation PDF is absent from official written_files: {filename}"<br>        )` under lexical guard `not matches`.
  - `PlanningRegulationIndexError(<br>            f"Regulation PDF is duplicated in official written_files: {filename}"<br>        )` under lexical guard `len(matches) != 1`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::_resolve_regulation_filename` via `_written_file_matches`
- value/type reference: `landscout.stages.index_planning_regulation::_resolve_regulation_filename` via `_written_file_matches`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationIndexError` | `landscout.stages.index_planning_regulation.PlanningRegulationIndexError` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_string` | `landscout.stages.index_planning_regulation._strict_string` |
| `matches.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | `matches.append(item)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_resolve_regulation_filename`

**Purpose:** Implements `resolve regulation filename` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

**Exact signature**

```python
def _resolve_regulation_filename(
    planning_document: GpuPlanningDocument,
    regulation_filename: str | None,
) -> tuple[str, str, _ZoningSourceEvidence, GpuWrittenFile]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[str, str, _ZoningSourceEvidence, GpuWrittenFile]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |
| `regulation_filename` | positional-or-keyword | `str \| None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `selected, method, zoning_evidence, written_file`
- Explicit raise paths:
  - `PlanningRegulationIndexError(<br>                "GPU zoning NOMFIC regulation selection is ambiguous"<br>            )` under lexical guard `regulation_filename is None`.
  - `PlanningRegulationIndexError(<br>                "Explicit regulation filename is not referenced by zoning NOMFIC"<br>            )` under lexical guard `regulation_filename is None`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `_resolve_regulation_filename`
- value/type reference: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `_resolve_regulation_filename`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_revalidate_zoning_source` | `landscout.stages.index_planning_regulation._revalidate_zoning_source` |
| `_zoning_regulation_filenames` | `landscout.stages.index_planning_regulation._zoning_regulation_filenames` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationIndexError` | `landscout.stages.index_planning_regulation.PlanningRegulationIndexError` |
| `_validated_pdf_basename` | `landscout.stages.index_planning_regulation._validated_pdf_basename` |
| `_written_file_matches` | `landscout.stages.index_planning_regulation._written_file_matches` |

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
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_locate_regulation_pdf`

**Purpose:** Implements `locate regulation pdf` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

**Exact signature**

```python
def _locate_regulation_pdf(
    planning_document: GpuPlanningDocument,
    pdf_basename: str,
) -> tuple[Path, GpuExtractedFile]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[Path, GpuExtractedFile]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |
| `pdf_basename` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `path, item`
- Explicit raise paths:
  - `PlanningRegulationIndexError(<br>            "GPU extraction root must be a regular directory"<br>        )` under lexical guard `not isinstance(root, Path) or _is_link_or_junction(root) or not root.is_dir()`.
  - `PlanningRegulationIndexError("GPU extraction inventory is invalid")` under lexical guard `not isinstance(item, GpuExtractedFile)`.
  - `PlanningRegulationIndexError(<br>                "GPU extraction inventory contains duplicate paths"<br>            )` under lexical guard `item.relative_path in inventory_paths`.
  - `PlanningRegulationIndexError(<br>            f"Regulation PDF is missing from GPU inventory: {pdf_basename}"<br>        )` under lexical guard `not matches`.
  - `PlanningRegulationIndexError(<br>            f"Regulation PDF is ambiguous in GPU inventory: {pdf_basename}"<br>        )` under lexical guard `len(matches) != 1`.
  - `PlanningRegulationIndexError(<br>            "Regulation PDF inventory classification is inconsistent"<br>        )` under lexical guard `file_type.casefold() != "pdf" or item.category != "WRITTEN_REGULATION"`.
  - `PlanningRegulationIndexError(<br>            "GPU extraction root cannot be resolved safely"<br>        )`.
  - `PlanningRegulationIndexError(<br>            "Regulation PDF path escapes the GPU extraction root"<br>        )`.
  - `PlanningRegulationIndexError(<br>                "Regulation PDF path contains a symbolic link or junction"<br>            )` under lexical guard `_is_link_or_junction(current)`.
  - `PlanningRegulationIndexError(<br>            "Regulation PDF must be an extracted regular file"<br>        )` under lexical guard `not path.is_file()`.
  - `PlanningRegulationIndexError(<br>            "Regulation PDF size cannot be read"<br>        )`.
  - `PlanningRegulationIndexError(<br>            "Regulation PDF size differs from extraction inventory"<br>        )` under lexical guard `actual_size != expected_size`.
  - `PlanningRegulationIndexError(<br>            "Regulation PDF SHA256 differs from extraction inventory"<br>        )` under lexical guard `_file_sha256(path) != expected_sha`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `_locate_regulation_pdf`
- value/type reference: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `_locate_regulation_pdf`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `_is_link_or_junction` | `landscout.stages.index_planning_regulation._is_link_or_junction` |
| `root.is_dir` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationIndexError` | `landscout.stages.index_planning_regulation.PlanningRegulationIndexError` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_relative_path` | `landscout.stages.index_planning_regulation._validated_relative_path` |
| `inventory_paths.add` | `unresolved local/third-party receiver; no ownership inferred` |
| `matches.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_string` | `landscout.stages.index_planning_regulation._strict_string` |
| `file_type.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `root.resolve` | `unresolved local/third-party receiver; no ownership inferred` |
| `root.joinpath` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.resolve` | `unresolved local/third-party receiver; no ownership inferred` |
| `resolved.relative_to` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_positive_integer` | `landscout.stages.index_planning_regulation._strict_positive_integer` |
| `path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_sha256` | `landscout.stages.index_planning_regulation._validated_sha256` |
| `_file_sha256` | `landscout.stages.index_planning_regulation._file_sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `root.is_dir`<br>`path.is_file`<br>`path.stat` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_validated_sha256`<br>`_file_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `inventory_paths.add(item.relative_path)`<br>`matches.append((relative, item))` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_page_error`

**Purpose:** Implements `page error` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

**Exact signature**

```python
def _page_error(error: Exception) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `error` | positional-or-keyword | `Exception` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `f"{type(error).__name__}: {message}" if message else type(error).__name__`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `_page_error`
- value/type reference: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `_page_error`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `sub(r"\s+", " ", str(error)).strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `sub` | `re.sub` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
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
def _page_error(error: Exception) -> str:
    message = sub(r"\s+", " ", str(error)).strip()
    return f"{type(error).__name__}: {message}" if message else type(error).__name__
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_canonical_page_record`

**Purpose:** Implements `canonical page record` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

**Exact signature**

```python
def _canonical_page_record(row: dict[str, object]) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `row` | positional-or-keyword | `dict[str, object]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `record`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::_page_hash_payload` via `_canonical_page_record`
- value/type reference: `landscout.stages.index_planning_regulation::_page_hash_payload` via `_canonical_page_record`
- direct call: `landscout.stages.index_planning_regulation::_pages_content_sha256` via `_canonical_page_record`
- value/type reference: `landscout.stages.index_planning_regulation::_pages_content_sha256` via `_canonical_page_record`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.isna` | `pandas.isna` |

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
| In-memory mutation | `record["extraction_error"] = None` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _canonical_page_record(row: dict[str, object]) -> dict[str, object]:
    record = {key: row[key] for key in PAGE_COLUMNS if key != "page_content_sha256"}
    if bool(pd.isna(record["extraction_error"])):
        record["extraction_error"] = None
    return record
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_page_hash_payload`

**Purpose:** Implements `page hash payload` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

**Exact signature**

```python
def _page_hash_payload(
    row: dict[str, object],
    page_hash_schema_version: int = PAGE_HASH_SCHEMA_VERSION,
    search_normalization_profile: str = SEARCH_NORMALIZATION_PROFILE,
) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `row` | positional-or-keyword | `dict[str, object]` | `required` |
| `page_hash_schema_version` | positional-or-keyword | `int` | `PAGE_HASH_SCHEMA_VERSION` |
| `search_normalization_profile` | positional-or-keyword | `str` | `SEARCH_NORMALIZATION_PROFILE` |

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>        "schema_version": page_hash_schema_version,<br>        "search_normalization_profile": search_normalization_profile,<br>        "page": _canonical_page_record(row),<br>    }`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::_page_content_sha256` via `_page_hash_payload`
- value/type reference: `landscout.stages.index_planning_regulation::_page_content_sha256` via `_page_hash_payload`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_page_record` | `landscout.stages.index_planning_regulation._canonical_page_record` |

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
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_page_content_sha256`

**Purpose:** Implements `page content sha256` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

**Exact signature**

```python
def _page_content_sha256(
    row: dict[str, object],
    page_hash_schema_version: int = PAGE_HASH_SCHEMA_VERSION,
    search_normalization_profile: str = SEARCH_NORMALIZATION_PROFILE,
) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `row` | positional-or-keyword | `dict[str, object]` | `required` |
| `page_hash_schema_version` | positional-or-keyword | `int` | `PAGE_HASH_SCHEMA_VERSION` |
| `search_normalization_profile` | positional-or-keyword | `str` | `SEARCH_NORMALIZATION_PROFILE` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_sha256(<br>        _page_hash_payload(<br>            row,<br>            page_hash_schema_version,<br>            search_normalization_profile,<br>        )<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::_validate_pages` via `_page_content_sha256`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_pages` via `_page_content_sha256`
- direct call: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `_page_content_sha256`
- value/type reference: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `_page_content_sha256`
- import: `tests.unit.test_interpret_bess_zoning::<module>` via `from landscout.stages.index_planning_regulation import (
    INDEX_HASH_SCHEMA_VERSION,
    PAGE_HASH_SCHEMA_VERSION,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndex,
    _index_content_sha256,
    _normalize_search_text,
    _page_content_sha256,
    _pages_content_sha256,
)`
- direct call: `tests.unit.test_interpret_bess_zoning::_index` via `_page_content_sha256`
- value/type reference: `tests.unit.test_interpret_bess_zoning::_index` via `_page_content_sha256`
- import: `tests.unit.test_structure_planning_regulation::<module>` via `from landscout.stages.index_planning_regulation import (
    INDEX_HASH_SCHEMA_VERSION,
    PAGE_HASH_SCHEMA_VERSION,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndex,
    _index_content_sha256,
    _normalize_search_text,
    _page_content_sha256,
    _pages_content_sha256,
)`
- direct call: `tests.unit.test_structure_planning_regulation::_index` via `_page_content_sha256`
- value/type reference: `tests.unit.test_structure_planning_regulation::_index` via `_page_content_sha256`
- direct call: `tests.unit.test_structure_planning_regulation::test_body_page_extraction_error_stops_structure` via `_page_content_sha256`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_body_page_extraction_error_stops_structure` via `_page_content_sha256`
- direct call: `tests.unit.test_structure_planning_regulation::test_blank_successfully_extracted_body_page_remains_valid` via `_page_content_sha256`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_blank_successfully_extracted_body_page_remains_valid` via `_page_content_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_sha256` | `landscout.stages.index_planning_regulation._canonical_sha256` |
| `_page_hash_payload` | `landscout.stages.index_planning_regulation._page_hash_payload` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_canonical_sha256`<br>`_page_hash_payload` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_pages_content_sha256`

**Purpose:** Implements `pages content sha256` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

**Exact signature**

```python
def _pages_content_sha256(
    frame: pd.DataFrame,
    page_hash_schema_version: int = PAGE_HASH_SCHEMA_VERSION,
    search_normalization_profile: str = SEARCH_NORMALIZATION_PROFILE,
) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `pd.DataFrame` | `required` |
| `page_hash_schema_version` | positional-or-keyword | `int` | `PAGE_HASH_SCHEMA_VERSION` |
| `search_normalization_profile` | positional-or-keyword | `str` | `SEARCH_NORMALIZATION_PROFILE` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_sha256(<br>        {<br>            "schema_version": page_hash_schema_version,<br>            "search_normalization_profile": search_normalization_profile,<br>            "pages": pages,<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `_pages_content_sha256`
- value/type reference: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `_pages_content_sha256`
- direct call: `landscout.stages.index_planning_regulation::_validate_planning_regulation_index` via `_pages_content_sha256`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_planning_regulation_index` via `_pages_content_sha256`
- import: `tests.unit.test_interpret_bess_zoning::<module>` via `from landscout.stages.index_planning_regulation import (
    INDEX_HASH_SCHEMA_VERSION,
    PAGE_HASH_SCHEMA_VERSION,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndex,
    _index_content_sha256,
    _normalize_search_text,
    _page_content_sha256,
    _pages_content_sha256,
)`
- direct call: `tests.unit.test_interpret_bess_zoning::_index` via `_pages_content_sha256`
- value/type reference: `tests.unit.test_interpret_bess_zoning::_index` via `_pages_content_sha256`
- import: `tests.unit.test_structure_planning_regulation::<module>` via `from landscout.stages.index_planning_regulation import (
    INDEX_HASH_SCHEMA_VERSION,
    PAGE_HASH_SCHEMA_VERSION,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndex,
    _index_content_sha256,
    _normalize_search_text,
    _page_content_sha256,
    _pages_content_sha256,
)`
- direct call: `tests.unit.test_structure_planning_regulation::_index` via `_pages_content_sha256`
- value/type reference: `tests.unit.test_structure_planning_regulation::_index` via `_pages_content_sha256`
- direct call: `tests.unit.test_structure_planning_regulation::test_body_page_extraction_error_stops_structure` via `_pages_content_sha256`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_body_page_extraction_error_stops_structure` via `_pages_content_sha256`
- direct call: `tests.unit.test_structure_planning_regulation::test_blank_successfully_extracted_body_page_remains_valid` via `_pages_content_sha256`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_blank_successfully_extracted_body_page_remains_valid` via `_pages_content_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `frame.loc[:, PAGE_COLUMNS].to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `_canonical_page_record` | `landscout.stages.index_planning_regulation._canonical_page_record` |
| `pages.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `_canonical_sha256` | `landscout.stages.index_planning_regulation._canonical_sha256` |

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
| In-memory mutation | `canonical["page_content_sha256"] = row["page_content_sha256"]`<br>`pages.append(canonical)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_pages_frame`

**Purpose:** Implements `pages frame` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

**Exact signature**

```python
def _pages_frame(rows: list[dict[str, object]]) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `rows` | positional-or-keyword | `list[dict[str, object]]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `frame`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `_pages_frame`
- value/type reference: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `_pages_frame`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pd.DataFrame` | `pandas.DataFrame` |
| `frame["page_number"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["character_count"].astype` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `frame["page_number"] = frame["page_number"].astype("int64")`<br>`frame["character_count"] = frame["character_count"].astype("int64")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _pages_frame(rows: list[dict[str, object]]) -> pd.DataFrame:
    frame = pd.DataFrame(rows, columns=PAGE_COLUMNS)
    frame["page_number"] = frame["page_number"].astype("int64")
    frame["character_count"] = frame["character_count"].astype("int64")
    return frame
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_index_hash_payload`

**Purpose:** Implements `index hash payload` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

**Exact signature**

```python
def _index_hash_payload(index: PlanningRegulationIndex) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>        "domain": "landscout.planning_regulation.index",<br>        "index_hash_schema_version": index.index_hash_schema_version,<br>        "document_id": index.document_id,<br>        "archive_sha256": index.archive_sha256,<br>        "regulation_filename": index.regulation_filename,<br>        "source_selection_method": index.source_selection_method,<br>        "source_selection_sha256": index.source_selection_sha256,<br>        "pdf_relative_path": index.pdf_relative_path,<br>        "pdf_size_bytes": index.pdf_size_bytes,<br>        "pdf_sha256": index.pdf_sha256,<br>        "extraction_library": index.extraction_library,<br>        "extraction_library_version": index.extraction_library_version,<br>        "search_normalization_profile": index.search_normalization_profile,<br>        "page_hash_schema_version": index.page_hash_schema_version,<br>        "total_page_count": index.total_page_count,<br>        "pages_content_sha256": index.pages_content_sha256,<br>    }`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::_index_content_sha256` via `_index_hash_payload`
- value/type reference: `landscout.stages.index_planning_regulation::_index_content_sha256` via `_index_hash_payload`

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
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_index_content_sha256`

**Purpose:** Implements `index content sha256` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

**Exact signature**

```python
def _index_content_sha256(index: PlanningRegulationIndex) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_sha256(_index_hash_payload(index))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `_index_content_sha256`
- value/type reference: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `_index_content_sha256`
- direct call: `landscout.stages.index_planning_regulation::_validate_planning_regulation_index` via `_index_content_sha256`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_planning_regulation_index` via `_index_content_sha256`
- import: `tests.unit.test_interpret_bess_zoning::<module>` via `from landscout.stages.index_planning_regulation import (
    INDEX_HASH_SCHEMA_VERSION,
    PAGE_HASH_SCHEMA_VERSION,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndex,
    _index_content_sha256,
    _normalize_search_text,
    _page_content_sha256,
    _pages_content_sha256,
)`
- direct call: `tests.unit.test_interpret_bess_zoning::_index` via `_index_content_sha256`
- value/type reference: `tests.unit.test_interpret_bess_zoning::_index` via `_index_content_sha256`
- import: `tests.unit.test_structure_planning_regulation::<module>` via `from landscout.stages.index_planning_regulation import (
    INDEX_HASH_SCHEMA_VERSION,
    PAGE_HASH_SCHEMA_VERSION,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndex,
    _index_content_sha256,
    _normalize_search_text,
    _page_content_sha256,
    _pages_content_sha256,
)`
- direct call: `tests.unit.test_structure_planning_regulation::_index` via `_index_content_sha256`
- value/type reference: `tests.unit.test_structure_planning_regulation::_index` via `_index_content_sha256`
- direct call: `tests.unit.test_structure_planning_regulation::test_body_page_extraction_error_stops_structure` via `_index_content_sha256`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_body_page_extraction_error_stops_structure` via `_index_content_sha256`
- direct call: `tests.unit.test_structure_planning_regulation::test_blank_successfully_extracted_body_page_remains_valid` via `_index_content_sha256`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_blank_successfully_extracted_body_page_remains_valid` via `_index_content_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_sha256` | `landscout.stages.index_planning_regulation._canonical_sha256` |
| `_index_hash_payload` | `landscout.stages.index_planning_regulation._index_hash_payload` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_canonical_sha256`<br>`_index_hash_payload` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _index_content_sha256(index: PlanningRegulationIndex) -> str:
    return _canonical_sha256(_index_hash_payload(index))
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_source_selection_sha256`

**Purpose:** Implements `source selection sha256` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

**Exact signature**

```python
def _source_selection_sha256(
    filename: str,
    method: str,
    zoning_evidence: _ZoningSourceEvidence,
    written_file: GpuWrittenFile,
    pdf_inventory: GpuExtractedFile,
) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `filename` | positional-or-keyword | `str` | `required` |
| `method` | positional-or-keyword | `str` | `required` |
| `zoning_evidence` | positional-or-keyword | `_ZoningSourceEvidence` | `required` |
| `written_file` | positional-or-keyword | `GpuWrittenFile` | `required` |
| `pdf_inventory` | positional-or-keyword | `GpuExtractedFile` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_sha256(<br>        {<br>            "domain": "landscout.planning_regulation.source_selection",<br>            "regulation_filename": filename,<br>            "source_selection_method": method,<br>            "zoning": {<br>                "source_layer": zoning_evidence.source_layer,<br>                "driver": zoning_evidence.driver,<br>                "source_files": [<br>                    {<br>                        "relative_path": item.relative_path,<br>                        "size_bytes": item.size_bytes,<br>                        "sha256": item.sha256,<br>                    }<br>                    for item in zoning_evidence.files<br>                ],<br>            },<br>            "written_file": {<br>                "filename": written_file.filename,<br>                "title": written_file.title,<br>                "document_path": written_file.document_path,<br>                "source_url": written_file.source_url,<br>            },<br>            "pdf_inventory": {<br>                "relative_path": pdf_inventory.relative_path,<br>                "size_bytes": pdf_inventory.size_bytes,<br>                "sha256": pdf_inventory.sha256,<br>                "file_type": pdf_inventory.file_type,<br>                "category": pdf_inventory.category,<br>            },<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `_source_selection_sha256`
- value/type reference: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `_source_selection_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_sha256` | `landscout.stages.index_planning_regulation._canonical_sha256` |

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
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_pages`

**Purpose:** Implements `validate pages` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

**Exact signature**

```python
def _validate_pages(
    frame: pd.DataFrame,
    total_page_count: int,
    page_hash_schema_version: int,
    search_normalization_profile: str,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `pd.DataFrame` | `required` |
| `total_page_count` | positional-or-keyword | `int` | `required` |
| `page_hash_schema_version` | positional-or-keyword | `int` | `required` |
| `search_normalization_profile` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `PlanningRegulationIndexError("Regulation pages must be a DataFrame")` under lexical guard `not isinstance(frame, pd.DataFrame)`.
  - `PlanningRegulationIndexError(<br>            "Regulation page schema is not deterministic"<br>        )` under lexical guard `tuple(frame.columns) != PAGE_COLUMNS`.
  - `PlanningRegulationIndexError("Regulation page count is inconsistent")` under lexical guard `len(frame) != total_page_count`.
  - `PlanningRegulationIndexError(<br>            "Regulation page numbers must be unique and ordered from 1"<br>        )` under lexical guard `frame["page_number"].tolist() != list(range(1, total_page_count + 1))`.
  - `PlanningRegulationIndexError("Regulation extraction status is invalid")` under lexical guard `not frame["extraction_status"].isin({"TEXT", "EMPTY", "ERROR"}).all()`.
  - `PlanningRegulationIndexError("Regulation page text must be a string")` under lexical guard `not isinstance(raw_text, str) or not isinstance(normalized, str)`.
  - `PlanningRegulationIndexError(<br>                "Regulation page character count is inconsistent"<br>            )` under lexical guard `character_count != len(raw_text)`.
  - `PlanningRegulationIndexError(<br>                "Regulation normalized search text is inconsistent"<br>            )` under lexical guard `normalized != _normalize_search_text(raw_text)`.
  - `PlanningRegulationIndexError("TEXT page state is inconsistent")` under lexical guard `status == "TEXT" and (not normalized or not error_is_null)`.
  - `PlanningRegulationIndexError("EMPTY page state is inconsistent")` under lexical guard `status == "EMPTY" and (normalized or not error_is_null)`.
  - `PlanningRegulationIndexError("ERROR page state is inconsistent")` under lexical guard `status == "ERROR" and (<br>            raw_text<br>            or normalized<br>            or not isinstance(extraction_error, str)<br>            or not extraction_error<br>        )`.
  - `PlanningRegulationIndexError("Regulation page content hash differs")` under lexical guard `checksum != _page_content_sha256(<br>            row,<br>            page_hash_schema_version,<br>            search_normalization_profile,<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::_validate_planning_regulation_index` via `_validate_pages`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_planning_regulation_index` via `_validate_pages`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationIndexError` | `landscout.stages.index_planning_regulation.PlanningRegulationIndexError` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["page_number"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["extraction_status"].isin({"TEXT", "EMPTY", "ERROR"}).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["extraction_status"].isin` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_positive_integer` | `landscout.stages.index_planning_regulation._strict_positive_integer` |
| `_strict_nonnegative_integer` | `landscout.stages.index_planning_regulation._strict_nonnegative_integer` |
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.isna` | `pandas.isna` |
| `_normalize_search_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_sha256` | `landscout.stages.index_planning_regulation._validated_sha256` |
| `_page_content_sha256` | `landscout.stages.index_planning_regulation._page_content_sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_validated_sha256`<br>`_page_content_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_pages(
    frame: pd.DataFrame,
    total_page_count: int,
    page_hash_schema_version: int,
    search_normalization_profile: str,
) -> None:
    if not isinstance(frame, pd.DataFrame):
        raise PlanningRegulationIndexError("Regulation pages must be a DataFrame")
    if tuple(frame.columns) != PAGE_COLUMNS:
        raise PlanningRegulationIndexError(
            "Regulation page schema is not deterministic"
        )
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
        checksum = _validated_sha256(row["page_content_sha256"], "page content SHA256")
        if checksum != _page_content_sha256(
            row,
            page_hash_schema_version,
            search_normalization_profile,
        ):
            raise PlanningRegulationIndexError("Regulation page content hash differs")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_pypdf_version`

**Purpose:** Implements `pypdf version` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

**Exact signature**

```python
def _pypdf_version() -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `version("pypdf")`
- Explicit raise paths:
  - `PlanningRegulationIndexError(<br>            "pypdf package version cannot be determined"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `_pypdf_version`
- value/type reference: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `_pypdf_version`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `version` | `importlib.metadata.version` |
| `PlanningRegulationIndexError` | `landscout.stages.index_planning_regulation.PlanningRegulationIndexError` |

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
def _pypdf_version() -> str:
    try:
        return version("pypdf")
    except Exception as error:
        raise PlanningRegulationIndexError(
            "pypdf package version cannot be determined"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_index_planning_regulation`

**Purpose:** Index the source-validated primary written regulation page by page.

**Exact signature**

```python
def _index_planning_regulation(
    planning_document: GpuPlanningDocument,
    regulation_filename: str | None = None,
) -> PlanningRegulationIndex:
```

- Exact decorators: none.
- Declared return annotation: `PlanningRegulationIndex`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |
| `regulation_filename` | positional-or-keyword | `str \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- Explicit raise paths:
  - `PlanningRegulationIndexError(<br>                    "Encrypted regulation PDFs are not supported"<br>                )` under lexical guard `reader.is_encrypted`.
  - `PlanningRegulationIndexError(<br>                    "Regulation PDF must contain at least one page"<br>                )` under lexical guard `total_page_count == 0`.
  - `TypeError("PDF page extractor returned non-text data")` under lexical guard `not isinstance(raw_text, str)`.
  - `re-raise`.
  - `PlanningRegulationIndexError(<br>            "Regulation PDF cannot be opened or parsed"<br>        )`.
  - `PlanningRegulationIndexError(<br>            "Regulation PDF size cannot be revalidated"<br>        )`.
  - `PlanningRegulationIndexError(<br>            "Regulation PDF changed during text extraction"<br>        )` under lexical guard `final_size != inventory.size_bytes or final_sha != inventory.sha256`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::index_planning_regulation` via `_index_planning_regulation`
- value/type reference: `landscout.stages.index_planning_regulation::index_planning_regulation` via `_index_planning_regulation`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_document_lineage` | `landscout.stages.index_planning_regulation._validate_document_lineage` |
| `_resolve_regulation_filename` | `landscout.stages.index_planning_regulation._resolve_regulation_filename` |
| `_locate_regulation_pdf` | `landscout.stages.index_planning_regulation._locate_regulation_pdf` |
| `_source_selection_sha256` | `landscout.stages.index_planning_regulation._source_selection_sha256` |
| `path.open` | `unresolved local/third-party receiver; no ownership inferred` |
| `PdfReader` | `pypdf.PdfReader` |
| `PlanningRegulationIndexError` | `landscout.stages.index_planning_regulation.PlanningRegulationIndexError` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `reader.pages[page_index].extract_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |
| `_normalize_search_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `_page_error` | `landscout.stages.index_planning_regulation._page_error` |
| `_page_content_sha256` | `landscout.stages.index_planning_regulation._page_content_sha256` |
| `rows.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `_file_sha256` | `landscout.stages.index_planning_regulation._file_sha256` |
| `_pages_frame` | `landscout.stages.index_planning_regulation._pages_frame` |
| `PlanningRegulationIndex` | `landscout.stages.index_planning_regulation.PlanningRegulationIndex` |
| `_pypdf_version` | `landscout.stages.index_planning_regulation._pypdf_version` |
| `_pages_content_sha256` | `landscout.stages.index_planning_regulation._pages_content_sha256` |
| `replace` | `dataclasses.replace` |
| `_index_content_sha256` | `landscout.stages.index_planning_regulation._index_content_sha256` |
| `validate_planning_regulation_index` | `landscout.stages.index_planning_regulation.validate_planning_regulation_index` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.open`<br>`path.stat` |
| Filesystem/archive write or publication | `reader.pages[page_index].extract_text` |
| Hashing/byte identity | `_source_selection_sha256`<br>`_page_content_sha256`<br>`_file_sha256`<br>`_pages_content_sha256`<br>`_index_content_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `row["page_content_sha256"] = _page_content_sha256(row)`<br>`rows.append(row)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `index_planning_regulation`

**Purpose:** Index one source-validated written regulation with controlled failures.

**Exact signature**

```python
def index_planning_regulation(
    planning_document: GpuPlanningDocument,
    regulation_filename: str | None = None,
) -> PlanningRegulationIndex:
```

- Exact decorators: none.
- Declared return annotation: `PlanningRegulationIndex`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |
| `regulation_filename` | positional-or-keyword | `str \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `_index_planning_regulation(planning_document, regulation_filename)`
- Explicit raise paths:
  - `re-raise`.
  - `PlanningRegulationIndexError(<br>            "Planning regulation indexing failed safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    PlanningRegulationIndexError,
    PlanningRegulationSearchResult,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`
- import: `tests.integration.test_gpu_planning_end_to_end::<module>` via `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    index_planning_regulation,
)`
- direct call: `tests.integration.test_gpu_planning_end_to_end::_build_physical_chain` via `index_planning_regulation`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_build_physical_chain` via `index_planning_regulation`
- import: `tests.unit.test_index_planning_regulation::<module>` via `from landscout.stages.index_planning_regulation import (
    PAGE_COLUMNS,
    SEARCH_HIT_COLUMNS,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndexError,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`
- direct call: `tests.unit.test_index_planning_regulation::_one_page_index` via `index_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::_one_page_index` via `index_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_source_nomfic_resolves_generic_filename` via `index_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_source_nomfic_resolves_generic_filename` via `index_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_explicit_source_validated_selection_succeeds` via `index_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_explicit_source_validated_selection_succeeds` via `index_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_unchanged_zoning_source_is_revalidated_before_selection` via `index_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_unchanged_zoning_source_is_revalidated_before_selection` via `index_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_mutated_loaded_nomfic_is_rejected_before_selection` via `index_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_mutated_loaded_nomfic_is_rejected_before_selection` via `index_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_mutated_loaded_zoning_geometry_or_order_is_rejected` via `index_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_mutated_loaded_zoning_geometry_or_order_is_rejected` via `index_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_zoning_source_bytes_changed_after_ingestion_are_rejected` via `index_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_zoning_source_bytes_changed_after_ingestion_are_rejected` via `index_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_zoning_source_inventory_integrity_mismatch_is_rejected` via `index_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_zoning_source_inventory_integrity_mismatch_is_rejected` via `index_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_missing_nomfic_field_is_rejected` via `index_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_missing_nomfic_field_is_rejected` via `index_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_null_nomfic_is_rejected` via `index_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_null_nomfic_is_rejected` via `index_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_multiple_nomfic_values_are_ambiguous` via `index_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_multiple_nomfic_values_are_ambiguous` via `index_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_unsafe_explicit_filename_is_rejected` via `index_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_unsafe_explicit_filename_is_rejected` via `index_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_explicit_filename_not_referenced_by_zoning_fails` via `index_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_explicit_filename_not_referenced_by_zoning_fails` via `index_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_filename_absent_from_written_files_fails` via `index_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_filename_absent_from_written_files_fails` via `index_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_unrelated_non_pdf_written_file_does_not_block_selection` via `index_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_unrelated_non_pdf_written_file_does_not_block_selection` via `index_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_filename_absent_from_inventory_fails` via `index_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_filename_absent_from_inventory_fails` via `index_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_duplicate_inventory_basename_fails` via `index_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_duplicate_inventory_basename_fails` via `index_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_path_outside_root_is_rejected` via `index_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_path_outside_root_is_rejected` via `index_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_pdf_inventory_integrity_mismatch_fails` via `index_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_pdf_inventory_integrity_mismatch_fails` via `index_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_page_states_numbering_and_hashes` via `index_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_page_states_numbering_and_hashes` via `index_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_zero_page_pdf_is_rejected` via `index_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_zero_page_pdf_is_rejected` via `index_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_pdf_reader_failure_is_controlled_and_chained` via `index_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_pdf_reader_failure_is_controlled_and_chained` via `index_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_version_discovery_failure_is_controlled_and_chained` via `index_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_version_discovery_failure_is_controlled_and_chained` via `index_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_index_integrity_mutations_fail` via `index_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_index_integrity_mutations_fail` via `index_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_malformed_source_metadata_raises_controlled_index_error` via `index_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_malformed_source_metadata_raises_controlled_index_error` via `index_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_extraction_and_search_do_not_mutate_inputs` via `index_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_extraction_and_search_do_not_mutate_inputs` via `index_planning_regulation`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index_planning_regulation` | `landscout.stages.index_planning_regulation._index_planning_regulation` |
| `PlanningRegulationIndexError` | `landscout.stages.index_planning_regulation.PlanningRegulationIndexError` |

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
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_planning_regulation_index`

**Purpose:** Implements `validate planning regulation index` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

**Exact signature**

```python
def _validate_planning_regulation_index(index: PlanningRegulationIndex) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `PlanningRegulationIndexError("index must be a PlanningRegulationIndex")` under lexical guard `not isinstance(index, PlanningRegulationIndex)`.
  - `PlanningRegulationIndexError(<br>            "Regulation source-selection method is unsupported"<br>        )` under lexical guard `index.source_selection_method not in {<br>        "ZONING_NOMFIC",<br>        "EXPLICIT_ZONING_NOMFIC",<br>    }`.
  - `PlanningRegulationIndexError(<br>            "Regulation filename differs from PDF relative path"<br>        )` under lexical guard `relative_pdf.name != filename`.
  - `PlanningRegulationIndexError("Regulation extraction library differs")` under lexical guard `index.extraction_library != "pypdf"`.
  - `PlanningRegulationIndexError(<br>            "Regulation search normalization profile is unsupported"<br>        )` under lexical guard `index.search_normalization_profile != SEARCH_NORMALIZATION_PROFILE`.
  - `PlanningRegulationIndexError("Regulation pages envelope hash differs")` under lexical guard `checksum != _pages_content_sha256(<br>        index.pages,<br>        page_schema,<br>        index.search_normalization_profile,<br>    )`.
  - `PlanningRegulationIndexError("Regulation index envelope hash differs")` under lexical guard `index_checksum != _index_content_sha256(index)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::validate_planning_regulation_index` via `_validate_planning_regulation_index`
- value/type reference: `landscout.stages.index_planning_regulation::validate_planning_regulation_index` via `_validate_planning_regulation_index`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationIndexError` | `landscout.stages.index_planning_regulation.PlanningRegulationIndexError` |
| `_strict_string` | `landscout.stages.index_planning_regulation._strict_string` |
| `_validated_sha256` | `landscout.stages.index_planning_regulation._validated_sha256` |
| `_validated_pdf_basename` | `landscout.stages.index_planning_regulation._validated_pdf_basename` |
| `_validated_relative_path` | `landscout.stages.index_planning_regulation._validated_relative_path` |
| `_strict_positive_integer` | `landscout.stages.index_planning_regulation._strict_positive_integer` |
| `_supported_schema_version` | `landscout.stages.index_planning_regulation._supported_schema_version` |
| `_validate_pages` | `landscout.stages.index_planning_regulation._validate_pages` |
| `_pages_content_sha256` | `landscout.stages.index_planning_regulation._pages_content_sha256` |
| `_index_content_sha256` | `landscout.stages.index_planning_regulation._index_content_sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_validated_sha256`<br>`_pages_content_sha256`<br>`_index_content_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_planning_regulation_index(index: PlanningRegulationIndex) -> None:
    if not isinstance(index, PlanningRegulationIndex):
        raise PlanningRegulationIndexError("index must be a PlanningRegulationIndex")
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
    checksum = _validated_sha256(index.pages_content_sha256, "pages content SHA256")
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
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `validate_planning_regulation_index`

**Purpose:** Validate all page, metadata, and complete index integrity contracts.

**Exact signature**

```python
def validate_planning_regulation_index(index: PlanningRegulationIndex) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `re-raise`.
  - `PlanningRegulationIndexError(<br>            "Regulation index validation failed safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    PlanningRegulationIndexError,
    PlanningRegulationSearchResult,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`
- direct call: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `validate_planning_regulation_index`
- value/type reference: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `validate_planning_regulation_index`
- direct call: `landscout.stages.index_planning_regulation::search_planning_regulation` via `validate_planning_regulation_index`
- value/type reference: `landscout.stages.index_planning_regulation::search_planning_regulation` via `validate_planning_regulation_index`
- direct call: `landscout.stages.index_planning_regulation::_validate_planning_regulation_search_result` via `validate_planning_regulation_index`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_planning_regulation_search_result` via `validate_planning_regulation_index`
- import: `landscout.stages.interpret_bess_zoning::<module>` via `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    validate_planning_regulation_index,
)`
- direct call: `landscout.stages.interpret_bess_zoning::_build_result` via `validate_planning_regulation_index`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_result` via `validate_planning_regulation_index`
- import: `landscout.stages.structure_planning_regulation::<module>` via `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    validate_planning_regulation_index,
)`
- direct call: `landscout.stages.structure_planning_regulation::_validate_document_lock` via `validate_planning_regulation_index`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_document_lock` via `validate_planning_regulation_index`
- direct call: `landscout.stages.structure_planning_regulation::_validate_result_self` via `validate_planning_regulation_index`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_result_self` via `validate_planning_regulation_index`
- import: `tests.unit.test_index_planning_regulation::<module>` via `from landscout.stages.index_planning_regulation import (
    PAGE_COLUMNS,
    SEARCH_HIT_COLUMNS,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndexError,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`
- direct call: `tests.unit.test_index_planning_regulation::test_page_states_numbering_and_hashes` via `validate_planning_regulation_index`
- value/type reference: `tests.unit.test_index_planning_regulation::test_page_states_numbering_and_hashes` via `validate_planning_regulation_index`
- direct call: `tests.unit.test_index_planning_regulation::test_coordinated_page_mutation_fails_envelope_hash` via `validate_planning_regulation_index`
- value/type reference: `tests.unit.test_index_planning_regulation::test_coordinated_page_mutation_fails_envelope_hash` via `validate_planning_regulation_index`
- direct call: `tests.unit.test_index_planning_regulation::test_index_integrity_mutations_fail` via `validate_planning_regulation_index`
- value/type reference: `tests.unit.test_index_planning_regulation::test_index_integrity_mutations_fail` via `validate_planning_regulation_index`
- direct call: `tests.unit.test_index_planning_regulation::test_complete_index_envelope_mutation_is_rejected` via `validate_planning_regulation_index`
- value/type reference: `tests.unit.test_index_planning_regulation::test_complete_index_envelope_mutation_is_rejected` via `validate_planning_regulation_index`
- direct call: `tests.unit.test_index_planning_regulation::test_unsupported_or_malformed_index_hash_schema_is_rejected` via `validate_planning_regulation_index`
- value/type reference: `tests.unit.test_index_planning_regulation::test_unsupported_or_malformed_index_hash_schema_is_rejected` via `validate_planning_regulation_index`
- direct call: `tests.unit.test_index_planning_regulation::test_malformed_page_hash_schema_is_rejected_as_controlled_error` via `validate_planning_regulation_index`
- value/type reference: `tests.unit.test_index_planning_regulation::test_malformed_page_hash_schema_is_rejected_as_controlled_error` via `validate_planning_regulation_index`
- direct call: `tests.unit.test_index_planning_regulation::test_malformed_page_value_raises_controlled_index_error` via `validate_planning_regulation_index`
- value/type reference: `tests.unit.test_index_planning_regulation::test_malformed_page_value_raises_controlled_index_error` via `validate_planning_regulation_index`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_planning_regulation_index` | `landscout.stages.index_planning_regulation._validate_planning_regulation_index` |
| `PlanningRegulationIndexError` | `landscout.stages.index_planning_regulation.PlanningRegulationIndexError` |

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
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validated_terms`

**Purpose:** Implements `validated terms` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

**Exact signature**

```python
def _validated_terms(terms: Sequence[str]) -> tuple[tuple[str, str], ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[tuple[str, str], ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `terms` | positional-or-keyword | `Sequence[str]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `tuple(result)`
- Explicit raise paths:
  - `PlanningRegulationIndexError("Search terms must be a sequence of terms")` under lexical guard `isinstance(terms, (str, bytes)) or not isinstance(terms, Sequence)`.
  - `PlanningRegulationIndexError(<br>                "Search terms must be unique after normalization"<br>            )` under lexical guard `not normalized_term or normalized_term in normalized_seen`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::search_planning_regulation` via `_validated_terms`
- value/type reference: `landscout.stages.index_planning_regulation::search_planning_regulation` via `_validated_terms`
- direct call: `landscout.stages.index_planning_regulation::_validate_planning_regulation_search_result` via `_validated_terms`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_planning_regulation_search_result` via `_validated_terms`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationIndexError` | `landscout.stages.index_planning_regulation.PlanningRegulationIndexError` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_string` | `landscout.stages.index_planning_regulation._strict_string` |
| `_normalize_search_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized_seen.add` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.append` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | `normalized_seen.add(normalized_term)`<br>`result.append((raw_term, normalized_term))` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_empty_hits`

**Purpose:** Implements `empty hits` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

**Exact signature**

```python
def _empty_hits() -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `pd.DataFrame(<br>        {<br>            column: pd.Series(<br>                dtype=(<br>                    "int64"<br>                    if column in {"page_number", "occurrence_count"}<br>                    else "object"<br>                )<br>            )<br>            for column in SEARCH_HIT_COLUMNS<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::_build_hits` via `_empty_hits`
- value/type reference: `landscout.stages.index_planning_regulation::_build_hits` via `_empty_hits`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pd.DataFrame` | `pandas.DataFrame` |
| `pd.Series` | `pandas.Series` |

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
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_build_hits`

**Purpose:** Implements `build hits` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

**Exact signature**

```python
def _build_hits(
    index: PlanningRegulationIndex,
    terms: tuple[tuple[str, str], ...],
    context_characters: int,
) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `terms` | positional-or-keyword | `tuple[tuple[str, str], ...]` | `required` |
| `context_characters` | positional-or-keyword | `int` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_empty_hits()`
  - `frame`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::search_planning_regulation` via `_build_hits`
- value/type reference: `landscout.stages.index_planning_regulation::search_planning_regulation` via `_build_hits`
- direct call: `landscout.stages.index_planning_regulation::_validate_planning_regulation_search_result` via `_build_hits`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_planning_regulation_search_result` via `_build_hits`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `escape` | `re.escape` |
| `index.pages.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `_normalize_search_text_with_mapping` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `finditer` | `re.finditer` |
| `max` | `unresolved local/third-party receiver; no ownership inferred` |
| `first.start` | `unresolved local/third-party receiver; no ownership inferred` |
| `min` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `first.end` | `unresolved local/third-party receiver; no ownership inferred` |
| `hits.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `_raw_context` | `unresolved local/third-party receiver; no ownership inferred` |
| `_empty_hits` | `landscout.stages.index_planning_regulation._empty_hits` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `frame["page_number"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["occurrence_count"].astype` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `hits.append(<br>                {<br>                    "document_id": index.document_id,<br>                    "archive_sha256": index.archive_sha256,<br>                    "pdf_sha256": index.pdf_sha256,<br>                    "search_normalization_profile": SEARCH_NORMALIZATION_PROFILE,<br>                    "search_term": raw_term,<br>                    "normalized_search_term": normalized_term,<br>                    "page_number": page["page_number"],<br>                    "occurrence_count": len(matches),<br>                    "raw_context": _raw_context(<br>                        raw_text, raw_spans, context_start, context_end<br>                    ),<br>                    "normalized_context": normalized_text[context_start:context_end],<br>                }<br>            )`<br>`frame["page_number"] = frame["page_number"].astype("int64")`<br>`frame["occurrence_count"] = frame["occurrence_count"].astype("int64")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
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
            normalized_text, raw_spans = _normalize_search_text_with_mapping(raw_text)
            matches = list(finditer(pattern, normalized_text))
            if not matches:
                continue
            first = matches[0]
            context_start = max(0, first.start() - context_characters)
            context_end = min(len(normalized_text), first.end() + context_characters)
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
                    "normalized_context": normalized_text[context_start:context_end],
                }
            )
    if not hits:
        return _empty_hits()
    frame = pd.DataFrame(hits, columns=SEARCH_HIT_COLUMNS)
    frame["page_number"] = frame["page_number"].astype("int64")
    frame["occurrence_count"] = frame["occurrence_count"].astype("int64")
    return frame
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_hits_content_sha256`

**Purpose:** Implements `hits content sha256` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

**Exact signature**

```python
def _hits_content_sha256(
    index: PlanningRegulationIndex,
    requested_terms: tuple[str, ...],
    context_characters: int,
    hits: pd.DataFrame,
    search_hash_schema_version: int = SEARCH_HASH_SCHEMA_VERSION,
) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `requested_terms` | positional-or-keyword | `tuple[str, ...]` | `required` |
| `context_characters` | positional-or-keyword | `int` | `required` |
| `hits` | positional-or-keyword | `pd.DataFrame` | `required` |
| `search_hash_schema_version` | positional-or-keyword | `int` | `SEARCH_HASH_SCHEMA_VERSION` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_sha256(<br>        {<br>            "domain": "landscout.planning_regulation.search",<br>            "search_hash_schema_version": search_hash_schema_version,<br>            "index_content_sha256": index.index_content_sha256,<br>            "document_id": index.document_id,<br>            "archive_sha256": index.archive_sha256,<br>            "pdf_sha256": index.pdf_sha256,<br>            "search_normalization_profile": index.search_normalization_profile,<br>            "requested_terms": list(requested_terms),<br>            "context_characters": context_characters,<br>            "hit_count": len(hits),<br>            "hits": hits.loc[:, SEARCH_HIT_COLUMNS].to_dict("records"),<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::search_planning_regulation` via `_hits_content_sha256`
- value/type reference: `landscout.stages.index_planning_regulation::search_planning_regulation` via `_hits_content_sha256`
- direct call: `landscout.stages.index_planning_regulation::_validate_planning_regulation_search_result` via `_hits_content_sha256`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_planning_regulation_search_result` via `_hits_content_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_sha256` | `landscout.stages.index_planning_regulation._canonical_sha256` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `hits.loc[:, SEARCH_HIT_COLUMNS].to_dict` | `unresolved local/third-party receiver; no ownership inferred` |

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
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `search_planning_regulation`

**Purpose:** Return sealed literal search hits with raw and normalized contexts.

**Exact signature**

```python
def search_planning_regulation(
    index: PlanningRegulationIndex,
    terms: Sequence[str],
    *,
    context_characters: int = 80,
) -> PlanningRegulationSearchResult:
```

- Exact decorators: none.
- Declared return annotation: `PlanningRegulationSearchResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `terms` | positional-or-keyword | `Sequence[str]` | `required` |
| `context_characters` | keyword-only | `int` | `80` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    PlanningRegulationIndexError,
    PlanningRegulationSearchResult,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`
- import: `tests.unit.test_index_planning_regulation::<module>` via `from landscout.stages.index_planning_regulation import (
    PAGE_COLUMNS,
    SEARCH_HIT_COLUMNS,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndexError,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`
- direct call: `tests.unit.test_index_planning_regulation::test_raw_context_preserves_source_typography` via `search_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_raw_context_preserves_source_typography` via `search_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_zero_context_preserves_complete_raw_unicode_span` via `search_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_zero_context_preserves_complete_raw_unicode_span` via `search_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_literal_search_does_not_add_semantic_synonyms` via `search_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_literal_search_does_not_add_semantic_synonyms` via `search_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::_valid_search_result` via `search_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::_valid_search_result` via `search_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_search_result_envelope_is_valid_and_deterministic` via `search_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_search_result_envelope_is_valid_and_deterministic` via `search_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_invalid_search_term_is_rejected` via `search_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_invalid_search_term_is_rejected` via `search_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_duplicate_normalized_search_terms_are_rejected` via `search_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_duplicate_normalized_search_terms_are_rejected` via `search_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_empty_search_result_has_stable_schema_and_lineage` via `search_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_empty_search_result_has_stable_schema_and_lineage` via `search_planning_regulation`
- direct call: `tests.unit.test_index_planning_regulation::test_extraction_and_search_do_not_mutate_inputs` via `search_planning_regulation`
- value/type reference: `tests.unit.test_index_planning_regulation::test_extraction_and_search_do_not_mutate_inputs` via `search_planning_regulation`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `validate_planning_regulation_index` | `landscout.stages.index_planning_regulation.validate_planning_regulation_index` |
| `_validated_terms` | `landscout.stages.index_planning_regulation._validated_terms` |
| `_strict_nonnegative_integer` | `landscout.stages.index_planning_regulation._strict_nonnegative_integer` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `_build_hits` | `landscout.stages.index_planning_regulation._build_hits` |
| `PlanningRegulationSearchResult` | `landscout.stages.index_planning_regulation.PlanningRegulationSearchResult` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `_hits_content_sha256` | `landscout.stages.index_planning_regulation._hits_content_sha256` |
| `validate_planning_regulation_search_result` | `landscout.stages.index_planning_regulation.validate_planning_regulation_search_result` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_hits_content_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_planning_regulation_search_result`

**Purpose:** Implements `validate planning regulation search result` within the file role: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

**Exact signature**

```python
def _validate_planning_regulation_search_result(
    index: PlanningRegulationIndex,
    result: PlanningRegulationSearchResult,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `result` | positional-or-keyword | `PlanningRegulationSearchResult` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `PlanningRegulationIndexError(<br>            "result must be a PlanningRegulationSearchResult"<br>        )` under lexical guard `not isinstance(result, PlanningRegulationSearchResult)`.
  - `PlanningRegulationIndexError("Search-result lineage differs from index")` under lexical guard `result.document_id != index.document_id<br>        or result.archive_sha256 != index.archive_sha256<br>        or result.pdf_sha256 != index.pdf_sha256<br>        or result.search_normalization_profile != index.search_normalization_profile<br>        or result.index_content_sha256 != index.index_content_sha256`.
  - `PlanningRegulationIndexError(<br>            "Search-result requested_terms must be tuple[str, ...]"<br>        )` under lexical guard `type(result.requested_terms) is not tuple`.
  - `PlanningRegulationIndexError("Search-hit schema is not deterministic")` under lexical guard `not isinstance(result.hits, pd.DataFrame) or tuple(result.hits.columns) != (<br>        SEARCH_HIT_COLUMNS<br>    )`.
  - `PlanningRegulationIndexError("Search-result hit count differs")` under lexical guard `hit_count != len(result.hits)`.
  - `PlanningRegulationIndexError("Search-hit lineage differs from index")` under lexical guard `row["document_id"] != index.document_id<br>            or row["archive_sha256"] != index.archive_sha256<br>            or row["pdf_sha256"] != index.pdf_sha256<br>            or row["search_normalization_profile"] != index.search_normalization_profile`.
  - `PlanningRegulationIndexError("Search hit has an unrequested term")` under lexical guard `normalized_term not in allowed_terms`.
  - `PlanningRegulationIndexError("Search hit references an unknown page")` under lexical guard `page_number not in allowed_pages`.
  - `PlanningRegulationIndexError(<br>                "Search hit page/term pair is duplicated"<br>            )` under lexical guard `pair in seen`.
  - `PlanningRegulationIndexError("Search contexts must be strings")` under lexical guard `not isinstance(row["raw_context"], str) or not isinstance(<br>            row["normalized_context"], str<br>        )`.
  - `PlanningRegulationIndexError("Search-result content hash differs")` under lexical guard `checksum != _hits_content_sha256(<br>        index,<br>        requested,<br>        context,<br>        result.hits,<br>        search_schema,<br>    )`.
  - `PlanningRegulationIndexError(<br>            "Search-result rows differ from deterministic source search"<br>        )` under lexical guard `not result.hits.reset_index(drop=True).equals(expected)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.index_planning_regulation::validate_planning_regulation_search_result` via `_validate_planning_regulation_search_result`
- value/type reference: `landscout.stages.index_planning_regulation::validate_planning_regulation_search_result` via `_validate_planning_regulation_search_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `validate_planning_regulation_index` | `landscout.stages.index_planning_regulation.validate_planning_regulation_index` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationIndexError` | `landscout.stages.index_planning_regulation.PlanningRegulationIndexError` |
| `_supported_schema_version` | `landscout.stages.index_planning_regulation._supported_schema_version` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_terms` | `landscout.stages.index_planning_regulation._validated_terms` |
| `_strict_nonnegative_integer` | `landscout.stages.index_planning_regulation._strict_nonnegative_integer` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `index.pages["page_number"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.hits.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_string` | `landscout.stages.index_planning_regulation._strict_string` |
| `_strict_positive_integer` | `landscout.stages.index_planning_regulation._strict_positive_integer` |
| `seen.add` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_sha256` | `landscout.stages.index_planning_regulation._validated_sha256` |
| `_hits_content_sha256` | `landscout.stages.index_planning_regulation._hits_content_sha256` |
| `_build_hits` | `landscout.stages.index_planning_regulation._build_hits` |
| `result.hits.reset_index(drop=True).equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.hits.reset_index` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_validated_sha256`<br>`_hits_content_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `seen.add(pair)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
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
        or result.search_normalization_profile != index.search_normalization_profile
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
            or row["search_normalization_profile"] != index.search_normalization_profile
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
            raise PlanningRegulationIndexError(
                "Search hit page/term pair is duplicated"
            )
        seen.add(pair)
        _strict_positive_integer(row["occurrence_count"], "occurrence count")
        if not isinstance(row["raw_context"], str) or not isinstance(
            row["normalized_context"], str
        ):
            raise PlanningRegulationIndexError("Search contexts must be strings")
    requested = tuple(raw for raw, _ in validated_terms)
    checksum = _validated_sha256(result.hits_content_sha256, "hits content SHA256")
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
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `validate_planning_regulation_search_result`

**Purpose:** Validate search lineage, schema, rows, hash, and source-derived contexts.

**Exact signature**

```python
def validate_planning_regulation_search_result(
    index: PlanningRegulationIndex,
    result: PlanningRegulationSearchResult,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `result` | positional-or-keyword | `PlanningRegulationSearchResult` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `re-raise`.
  - `PlanningRegulationIndexError(<br>            "Regulation search-result validation failed safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    PlanningRegulationIndexError,
    PlanningRegulationSearchResult,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`
- direct call: `landscout.stages.index_planning_regulation::search_planning_regulation` via `validate_planning_regulation_search_result`
- value/type reference: `landscout.stages.index_planning_regulation::search_planning_regulation` via `validate_planning_regulation_search_result`
- import: `tests.unit.test_index_planning_regulation::<module>` via `from landscout.stages.index_planning_regulation import (
    PAGE_COLUMNS,
    SEARCH_HIT_COLUMNS,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndexError,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`
- direct call: `tests.unit.test_index_planning_regulation::test_search_result_envelope_is_valid_and_deterministic` via `validate_planning_regulation_search_result`
- value/type reference: `tests.unit.test_index_planning_regulation::test_search_result_envelope_is_valid_and_deterministic` via `validate_planning_regulation_search_result`
- direct call: `tests.unit.test_index_planning_regulation::test_search_index_identity_schema_and_terms_are_sealed` via `validate_planning_regulation_search_result`
- value/type reference: `tests.unit.test_index_planning_regulation::test_search_index_identity_schema_and_terms_are_sealed` via `validate_planning_regulation_search_result`
- direct call: `tests.unit.test_index_planning_regulation::test_search_requested_terms_must_be_an_immutable_exact_tuple` via `validate_planning_regulation_search_result`
- value/type reference: `tests.unit.test_index_planning_regulation::test_search_requested_terms_must_be_an_immutable_exact_tuple` via `validate_planning_regulation_search_result`
- direct call: `tests.unit.test_index_planning_regulation::test_search_result_integrity_mutations_fail` via `validate_planning_regulation_search_result`
- value/type reference: `tests.unit.test_index_planning_regulation::test_search_result_integrity_mutations_fail` via `validate_planning_regulation_search_result`
- direct call: `tests.unit.test_index_planning_regulation::test_search_hit_lineage_mutation_fails` via `validate_planning_regulation_search_result`
- value/type reference: `tests.unit.test_index_planning_regulation::test_search_hit_lineage_mutation_fails` via `validate_planning_regulation_search_result`
- direct call: `tests.unit.test_index_planning_regulation::test_empty_search_result_has_stable_schema_and_lineage` via `validate_planning_regulation_search_result`
- value/type reference: `tests.unit.test_index_planning_regulation::test_empty_search_result_has_stable_schema_and_lineage` via `validate_planning_regulation_search_result`
- direct call: `tests.unit.test_index_planning_regulation::test_malformed_hit_value_raises_controlled_index_error` via `validate_planning_regulation_search_result`
- value/type reference: `tests.unit.test_index_planning_regulation::test_malformed_hit_value_raises_controlled_index_error` via `validate_planning_regulation_search_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_planning_regulation_search_result` | `landscout.stages.index_planning_regulation._validate_planning_regulation_search_result` |
| `PlanningRegulationIndexError` | `landscout.stages.index_planning_regulation.PlanningRegulationIndexError` |

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
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.


## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: `_normalize_search_text_with_mapping`, `PAGE_HASH_SCHEMA_VERSION`, `INDEX_HASH_SCHEMA_VERSION`, `SEARCH_HASH_SCHEMA_VERSION`, `PAGE_COLUMNS`, `SEARCH_HIT_COLUMNS`.
- Exact value/null/index/CRS/geometry/hash behavior is claimed only where the reproduced validators and operations enforce it.

## 8. Public exports and package ownership

Exact `__all__` members and local origins:

| Export | Local origin binding |
|---|---|
| `PlanningRegulationIndex` | `landscout.stages.index_planning_regulation.PlanningRegulationIndex` |
| `PlanningRegulationIndexError` | `landscout.stages.index_planning_regulation.PlanningRegulationIndexError` |
| `PlanningRegulationSearchResult` | `landscout.stages.index_planning_regulation.PlanningRegulationSearchResult` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |
| `search_planning_regulation` | `landscout.stages.index_planning_regulation.search_planning_regulation` |
| `validate_planning_regulation_index` | `landscout.stages.index_planning_regulation.validate_planning_regulation_index` |
| `validate_planning_regulation_search_result` | `landscout.stages.index_planning_regulation.validate_planning_regulation_search_result` |

## 9. Trust, provenance, side effects, and business boundary

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
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

from landscout.common import planning_text
from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuWrittenFile,
    revalidate_gpu_spatial_layer_source,
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
        raise PlanningRegulationIndexError(f"{label} must be a non-empty exact string")
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


def _revalidate_zoning_source(
    planning_document: GpuPlanningDocument,
) -> tuple[gpd.GeoDataFrame, _ZoningSourceEvidence]:
    """Re-read immutable zoning bytes before trusting source PDF references."""

    try:
        source = revalidate_gpu_spatial_layer_source(
            planning_document, planning_document.zoning
        )
        if "NOMFIC" not in source.data.columns:
            raise PlanningRegulationIndexError("GPU zoning is missing NOMFIC")
        return source.data, _ZoningSourceEvidence(
            source_layer=source.source_layer,
            driver=source.driver,
            files=tuple(
                _ZoningSourceFileIntegrity(
                    relative_path=item.relative_path,
                    size_bytes=item.size_bytes,
                    sha256=item.sha256,
                )
                for item in source.files
            ),
        )
    except PlanningRegulationIndexError:
        raise
    except GpuSpatialInspectionError as error:
        raise PlanningRegulationIndexError(
            f"GPU zoning source integrity cannot be revalidated: {error}"
        ) from error
    except Exception as error:
        raise PlanningRegulationIndexError(
            "GPU zoning source cannot be revalidated"
        ) from error


def _validate_document_lineage(
    planning_document: GpuPlanningDocument,
) -> tuple[str, str]:
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
    if (
        type(planning_document.related_layers) is not tuple
        or type(planning_document.all_spatial_layers) is not tuple
    ):
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
            if (
                value is None
                or value is pd.NA
                or (isinstance(value, float) and pd.isna(value))
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
    record = {key: row[key] for key in PAGE_COLUMNS if key != "page_content_sha256"}
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
        raise PlanningRegulationIndexError(
            "Regulation page schema is not deterministic"
        )
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
        checksum = _validated_sha256(row["page_content_sha256"], "page content SHA256")
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
        raise PlanningRegulationIndexError("index must be a PlanningRegulationIndex")
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
    checksum = _validated_sha256(index.pages_content_sha256, "pages content SHA256")
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
            normalized_text, raw_spans = _normalize_search_text_with_mapping(raw_text)
            matches = list(finditer(pattern, normalized_text))
            if not matches:
                continue
            first = matches[0]
            context_start = max(0, first.start() - context_characters)
            context_end = min(len(normalized_text), first.end() + context_characters)
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
                    "normalized_context": normalized_text[context_start:context_end],
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
        or result.search_normalization_profile != index.search_normalization_profile
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
            or row["search_normalization_profile"] != index.search_normalization_profile
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
            raise PlanningRegulationIndexError(
                "Search hit page/term pair is duplicated"
            )
        seen.add(pair)
        _strict_positive_integer(row["occurrence_count"], "occurrence count")
        if not isinstance(row["raw_context"], str) or not isinstance(
            row["normalized_context"], str
        ):
            raise PlanningRegulationIndexError("Search contexts must be strings")
    requested = tuple(raw for raw, _ in validated_terms)
    checksum = _validated_sha256(result.hits_content_sha256, "hits content SHA256")
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
```

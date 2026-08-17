# `src/landscout/stages/index_planning_regulation.py`

## File identity

- Repository path: `src/landscout/stages/index_planning_regulation.py`
- File type: Python source
- Layer: processing stage
- Domain: planning
- Responsibility: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.
- Source SHA256: `b9434ebeb1b3e05a0604bb56facde5f17183beb04cc2b6da667a438d11aa50d1`

## 1. Purpose

Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

## 2. Position in LandScout architecture

This file belongs to the **processing stage** layer and the **planning** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

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

### A. Python constants

#### `SEARCH_NORMALIZATION_PROFILE`

```python
SEARCH_NORMALIZATION_PROFILE = planning_text.SEARCH_NORMALIZATION_PROFILE
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_index_planning_regulation.py::<module>` (import), `tests/unit/test_interpret_bess_zoning.py::<module>` (import), `tests/unit/test_structure_planning_regulation.py::<module>` (import), `src/landscout/stages/index_planning_regulation.py::_index_planning_regulation` (value reference), `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_index` (value reference), `src/landscout/stages/index_planning_regulation.py::_build_hits` (value reference), `tests/unit/test_index_planning_regulation.py::test_search_result_envelope_is_valid_and_deterministic` (value reference), `tests/unit/test_interpret_bess_zoning.py::_index` (value reference), `tests/unit/test_structure_planning_regulation.py::_index` (value reference).

#### `_normalize_search_text`

```python
_normalize_search_text = planning_text.normalize_planning_search_text
```

Private module-level technical value; only the qualified references below are attributed to this declaration. Consumers include `tests/unit/test_interpret_bess_zoning.py::<module>` (import), `tests/unit/test_structure_planning_regulation.py::<module>` (import).

#### `_normalize_search_text_with_mapping`

```python
_normalize_search_text_with_mapping = (
    planning_text.normalize_planning_search_text_with_mapping
)
```

Explicit mapping between source/input and target/output fields; keys and values are documented separately.

#### `_raw_context`

```python
_raw_context = planning_text.raw_context_from_spans
```

Private module-level technical value; only the qualified references below are attributed to this declaration.

#### `PAGE_HASH_SCHEMA_VERSION`

```python
PAGE_HASH_SCHEMA_VERSION = 1
```

Supported schema/hash/manifest compatibility version used by validators and canonical hashing. Consumers include `tests/unit/test_interpret_bess_zoning.py::<module>` (import), `tests/unit/test_structure_planning_regulation.py::<module>` (import), `src/landscout/stages/index_planning_regulation.py::_index_planning_regulation` (value reference), `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_index` (value reference), `tests/unit/test_interpret_bess_zoning.py::_index` (value reference), `tests/unit/test_structure_planning_regulation.py::_index` (value reference).

#### `INDEX_HASH_SCHEMA_VERSION`

```python
INDEX_HASH_SCHEMA_VERSION = 1
```

Supported schema/hash/manifest compatibility version used by validators and canonical hashing. Consumers include `tests/unit/test_interpret_bess_zoning.py::<module>` (import), `tests/unit/test_structure_planning_regulation.py::<module>` (import), `src/landscout/stages/index_planning_regulation.py::_index_planning_regulation` (value reference), `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_index` (value reference), `tests/unit/test_interpret_bess_zoning.py::_index` (value reference), `tests/unit/test_structure_planning_regulation.py::_index` (value reference).

#### `SEARCH_HASH_SCHEMA_VERSION`

```python
SEARCH_HASH_SCHEMA_VERSION = 1
```

Supported schema/hash/manifest compatibility version used by validators and canonical hashing. Consumers include `src/landscout/stages/index_planning_regulation.py::search_planning_regulation` (value reference), `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_search_result` (value reference).

#### `PAGE_COLUMNS`

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

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `tests/unit/test_index_planning_regulation.py::<module>` (import), `src/landscout/stages/index_planning_regulation.py::_canonical_page_record` (value reference), `src/landscout/stages/index_planning_regulation.py::_pages_content_sha256` (value reference), `src/landscout/stages/index_planning_regulation.py::_pages_frame` (value reference), `src/landscout/stages/index_planning_regulation.py::_validate_pages` (value reference), `tests/unit/test_index_planning_regulation.py::test_page_states_numbering_and_hashes` (value reference).

#### `SEARCH_HIT_COLUMNS`

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

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `tests/unit/test_index_planning_regulation.py::<module>` (import), `src/landscout/stages/index_planning_regulation.py::_empty_hits` (value reference), `src/landscout/stages/index_planning_regulation.py::_build_hits` (value reference), `src/landscout/stages/index_planning_regulation.py::_hits_content_sha256` (value reference), `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_search_result` (value reference), `tests/unit/test_index_planning_regulation.py::test_search_result_envelope_is_valid_and_deterministic` (value reference), `tests/unit/test_index_planning_regulation.py::test_empty_search_result_has_stable_schema_and_lineage` (value reference).

#### `_validate_index`

```python
_validate_index = validate_planning_regulation_index
```

Private module-level technical value; only the qualified references below are attributed to this declaration.


### B. Type aliases and closed domains

#### `ExtractionStatus`

```python
ExtractionStatus = Literal["TEXT", "EMPTY", "ERROR"]
```

Closed Literal value domain shown exactly above; members are values, not frame columns. Enforced/consumed by `src/landscout/stages/index_planning_regulation.py::_index_planning_regulation` (type annotation).


### C. Meaningful dunder contracts

- `__all__` — explicit public export allow-list.
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


### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `PlanningRegulationIndexError`

**Purpose:** Raised when regulation indexing or search integrity cannot be proven.

**Kind:** controlled exception.

**Inheritance:** `ValueError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    PlanningRegulationIndexError,
    PlanningRegulationSearchResult,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`.
- import: `tests/unit/test_index_planning_regulation.py::<module>` via `from landscout.stages.index_planning_regulation import (
    PAGE_COLUMNS,
    SEARCH_HIT_COLUMNS,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndexError,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::_strict_string` via `PlanningRegulationIndexError`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::_strict_nonnegative_integer` via `PlanningRegulationIndexError`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::_strict_positive_integer` via `PlanningRegulationIndexError`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::_supported_schema_version` via `PlanningRegulationIndexError`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::_validated_sha256` via `PlanningRegulationIndexError`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::_canonical_sha256` via `PlanningRegulationIndexError`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::_is_link_or_junction` via `PlanningRegulationIndexError`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::_validated_relative_path` via `PlanningRegulationIndexError`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::_validated_pdf_basename` via `PlanningRegulationIndexError`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::_file_sha256` via `PlanningRegulationIndexError`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::_revalidate_zoning_source` via `PlanningRegulationIndexError`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::_validate_document_lineage` via `PlanningRegulationIndexError`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::_zoning_regulation_filenames` via `PlanningRegulationIndexError`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::_written_file_matches` via `PlanningRegulationIndexError`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::_resolve_regulation_filename` via `PlanningRegulationIndexError`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::_locate_regulation_pdf` via `PlanningRegulationIndexError`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::_validate_pages` via `PlanningRegulationIndexError`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::_pypdf_version` via `PlanningRegulationIndexError`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::_index_planning_regulation` via `PlanningRegulationIndexError`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::index_planning_regulation` via `PlanningRegulationIndexError`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_index` via `PlanningRegulationIndexError`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::validate_planning_regulation_index` via `PlanningRegulationIndexError`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::_validated_terms` via `PlanningRegulationIndexError`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_search_result` via `PlanningRegulationIndexError`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::validate_planning_regulation_search_result` via `PlanningRegulationIndexError`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_mutated_loaded_nomfic_is_rejected_before_selection` via `pytest.raises(PlanningRegulationIndexError, match='zoning|source')`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_mutated_loaded_zoning_geometry_or_order_is_rejected` via `pytest.raises(PlanningRegulationIndexError, match='zoning|source')`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_zoning_source_bytes_changed_after_ingestion_are_rejected` via `pytest.raises(PlanningRegulationIndexError, match='size|SHA256|integrity')`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_zoning_source_inventory_integrity_mismatch_is_rejected` via `pytest.raises(PlanningRegulationIndexError, match='size|SHA256|integrity')`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_missing_nomfic_field_is_rejected` via `pytest.raises(PlanningRegulationIndexError, match='missing NOMFIC')`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_null_nomfic_is_rejected` via `pytest.raises(PlanningRegulationIndexError, match='no regulation filename')`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_multiple_nomfic_values_are_ambiguous` via `pytest.raises(PlanningRegulationIndexError, match='ambiguous')`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_unsafe_explicit_filename_is_rejected` via `pytest.raises(PlanningRegulationIndexError, match='filename')`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_explicit_filename_not_referenced_by_zoning_fails` via `pytest.raises(PlanningRegulationIndexError, match='not referenced')`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_filename_absent_from_written_files_fails` via `pytest.raises(PlanningRegulationIndexError, match='written_files')`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_filename_absent_from_inventory_fails` via `pytest.raises(PlanningRegulationIndexError, match='missing from GPU inventory|verified manifest')`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_duplicate_inventory_basename_fails` via `pytest.raises(PlanningRegulationIndexError, match='ambiguous')`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_path_outside_root_is_rejected` via `pytest.raises(PlanningRegulationIndexError, match='unsafe|verified manifest')`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_pdf_inventory_integrity_mismatch_fails` via `pytest.raises(PlanningRegulationIndexError, match='differs')`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_zero_page_pdf_is_rejected` via `pytest.raises(PlanningRegulationIndexError, match='at least one page')`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_pdf_reader_failure_is_controlled_and_chained` via `pytest.raises(PlanningRegulationIndexError, match='opened or parsed')`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_version_discovery_failure_is_controlled_and_chained` via `pytest.raises(PlanningRegulationIndexError, match='version')`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_coordinated_page_mutation_fails_envelope_hash` via `pytest.raises(PlanningRegulationIndexError, match='envelope')`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_index_integrity_mutations_fail` via `pytest.raises(PlanningRegulationIndexError)`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_complete_index_envelope_mutation_is_rejected` via `pytest.raises(PlanningRegulationIndexError)`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_unsupported_or_malformed_index_hash_schema_is_rejected` via `pytest.raises(PlanningRegulationIndexError)`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_malformed_page_hash_schema_is_rejected_as_controlled_error` via `pytest.raises(PlanningRegulationIndexError)`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_search_index_identity_schema_and_terms_are_sealed` via `pytest.raises(PlanningRegulationIndexError)`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_search_requested_terms_must_be_an_immutable_exact_tuple` via `pytest.raises(PlanningRegulationIndexError, match='tuple')`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_search_result_integrity_mutations_fail` via `pytest.raises(PlanningRegulationIndexError)`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_search_hit_lineage_mutation_fails` via `pytest.raises(PlanningRegulationIndexError, match='lineage')`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_invalid_search_term_is_rejected` via `pytest.raises(PlanningRegulationIndexError, match='search term')`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_duplicate_normalized_search_terms_are_rejected` via `pytest.raises(PlanningRegulationIndexError, match='unique')`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_malformed_page_value_raises_controlled_index_error` via `pytest.raises(PlanningRegulationIndexError)`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_malformed_hit_value_raises_controlled_index_error` via `pytest.raises(PlanningRegulationIndexError)`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_canonical_hash_serialization_failure_is_controlled_and_chained` via `pytest.raises(PlanningRegulationIndexError, match='serialized')`.
- expected exception type: `tests/unit/test_index_planning_regulation.py::test_malformed_source_metadata_raises_controlled_index_error` via `pytest.raises(PlanningRegulationIndexError)`.

**Exact class source**

```python
class PlanningRegulationIndexError(ValueError):
    """Raised when regulation indexing or search integrity cannot be proven."""
```

### `PlanningRegulationIndex`

**Purpose:** Immutable lineage envelope around a deterministic page text table.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `document_id` | `document_id: str` | Exact identity for the entity named by the field; uniqueness, portability, and lineage meaning are only those explicitly validated by the owner. |
| `archive_sha256` | `archive_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `regulation_filename` | `regulation_filename: str` | Portable basename for the named physical file; it must agree with the owning path/manifest contract where validated. |
| `source_selection_method` | `source_selection_method: str` | Source fact or textual lineage named by the suffix; it becomes physical proof only where a validator rechecks bytes/source content. |
| `source_selection_sha256` | `source_selection_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `pdf_relative_path` | `pdf_relative_path: str` | Filesystem location for the artifact named by the field; containment, portability, link, existence, and recovery checks belong to the owning source/artifact validator. |
| `pdf_size_bytes` | `pdf_size_bytes: int` | Measured physical written-regulation PDF size in bytes. |
| `pdf_sha256` | `pdf_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `extraction_library` | `extraction_library: str` | `PlanningRegulationIndex.extraction_library` carries the extraction library used by the reproduced constructors and validators; its declared type is `str` and no legal meaning is inferred beyond that owner. |
| `extraction_library_version` | `extraction_library_version: str` | `PlanningRegulationIndex.extraction_library_version` carries the extraction library version used by the reproduced constructors and validators; its declared type is `str` and no legal meaning is inferred beyond that owner. |
| `search_normalization_profile` | `search_normalization_profile: str` | Named deterministic text-normalization profile used to index and search regulation pages. |
| `page_hash_schema_version` | `page_hash_schema_version: int` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `index_hash_schema_version` | `index_hash_schema_version: int` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `total_page_count` | `total_page_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `pages_content_sha256` | `pages_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `index_content_sha256` | `index_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `pages` | `pages: pd.DataFrame` | Deterministically ordered regulation PDF page records. |

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    PlanningRegulationIndexError,
    PlanningRegulationSearchResult,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`.
- import: `src/landscout/stages/interpret_bess_zoning.py::<module>` via `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    validate_planning_regulation_index,
)`.
- import: `src/landscout/stages/structure_planning_regulation.py::<module>` via `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    validate_planning_regulation_index,
)`.
- import: `tests/unit/test_interpret_bess_zoning.py::<module>` via `from landscout.stages.index_planning_regulation import (
    INDEX_HASH_SCHEMA_VERSION,
    PAGE_HASH_SCHEMA_VERSION,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndex,
    _index_content_sha256,
    _normalize_search_text,
    _page_content_sha256,
    _pages_content_sha256,
)`.
- import: `tests/unit/test_structure_planning_regulation.py::<module>` via `from landscout.stages.index_planning_regulation import (
    INDEX_HASH_SCHEMA_VERSION,
    PAGE_HASH_SCHEMA_VERSION,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndex,
    _index_content_sha256,
    _normalize_search_text,
    _page_content_sha256,
    _pages_content_sha256,
)`.
- type annotation: `src/landscout/stages/index_planning_regulation.py::_index_hash_payload` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/index_planning_regulation.py::_index_content_sha256` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/index_planning_regulation.py::_index_planning_regulation` via `PlanningRegulationIndex`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::_index_planning_regulation` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/index_planning_regulation.py::index_planning_regulation` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_index` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/index_planning_regulation.py::validate_planning_regulation_index` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/index_planning_regulation.py::_build_hits` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/index_planning_regulation.py::_hits_content_sha256` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/index_planning_regulation.py::search_planning_regulation` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_search_result` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/index_planning_regulation.py::validate_planning_regulation_search_result` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_validate_policy_lock` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_validate_parcels` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_validate_zones` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_validate_relations` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_validate_policy_evidence` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_lineage` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_build_chapter_policy` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_build_route_assessments` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_build_evidence_route_links` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_build_source_zone_policy` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_build_parcel_zone_interpretations` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_build_result` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::validate_bess_zoning_precheck` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::interpret_bess_zoning` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/structure_planning_regulation.py::_validate_document_lock` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/structure_planning_regulation.py::_line_records` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/structure_planning_regulation.py::_build_sections` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/structure_planning_regulation.py::_validated_zoning_inputs` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/structure_planning_regulation.py::_build_zone_mapping` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/structure_planning_regulation.py::_build_topic_evidence` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/structure_planning_regulation.py::_validate_sections` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/structure_planning_regulation.py::_validate_topic_evidence` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/structure_planning_regulation.py::_build_structure_result` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/structure_planning_regulation.py::_validate_result_self` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/structure_planning_regulation.py::validate_planning_regulation_structure_with_fragments` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/structure_planning_regulation.py::validate_planning_regulation_structure` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/structure_planning_regulation.py::planning_regulation_section_page_fragments` via `PlanningRegulationIndex`.
- type annotation: `src/landscout/stages/structure_planning_regulation.py::structure_planning_regulation` via `PlanningRegulationIndex`.
- type annotation: `tests/unit/test_interpret_bess_zoning.py::_index` via `PlanningRegulationIndex`.
- constructor call: `tests/unit/test_interpret_bess_zoning.py::_index` via `PlanningRegulationIndex`.
- type annotation: `tests/unit/test_interpret_bess_zoning.py::_zones` via `PlanningRegulationIndex`.
- type annotation: `tests/unit/test_interpret_bess_zoning.py::_relations` via `PlanningRegulationIndex`.
- type annotation: `tests/unit/test_interpret_bess_zoning.py::_structure_config` via `PlanningRegulationIndex`.
- type annotation: `tests/unit/test_interpret_bess_zoning.py::_parcels` via `PlanningRegulationIndex`.
- type annotation: `tests/unit/test_structure_planning_regulation.py::_index` via `PlanningRegulationIndex`.
- constructor call: `tests/unit/test_structure_planning_regulation.py::_index` via `PlanningRegulationIndex`.
- type annotation: `tests/unit/test_structure_planning_regulation.py::_config` via `PlanningRegulationIndex`.
- type annotation: `tests/unit/test_structure_planning_regulation.py::_zones` via `PlanningRegulationIndex`.
- type annotation: `tests/unit/test_structure_planning_regulation.py::_intersections` via `PlanningRegulationIndex`.
- type annotation: `tests/unit/test_structure_planning_regulation.py::_validate` via `PlanningRegulationIndex`.
- type annotation: `tests/unit/test_structure_planning_regulation.py::_config_with_structural_patterns` via `PlanningRegulationIndex`.

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

**Purpose:** Immutable lineage envelope around deterministic factual search hits.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `document_id` | `document_id: str` | Exact identity for the entity named by the field; uniqueness, portability, and lineage meaning are only those explicitly validated by the owner. |
| `archive_sha256` | `archive_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `pdf_sha256` | `pdf_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `search_normalization_profile` | `search_normalization_profile: str` | Named deterministic text-normalization profile used to index and search regulation pages. |
| `search_hash_schema_version` | `search_hash_schema_version: int` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `index_content_sha256` | `index_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `requested_terms` | `requested_terms: tuple[str, ...]` | Structured `requested terms` collection owned by `PlanningRegulationSearchResult`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `context_characters` | `context_characters: int` | `PlanningRegulationSearchResult.context_characters` carries the context characters used by the reproduced constructors and validators; its declared type is `int` and no legal meaning is inferred beyond that owner. |
| `hit_count` | `hit_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `hits_content_sha256` | `hits_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `hits` | `hits: pd.DataFrame` | Deterministically ordered exact regulation search matches. |

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    PlanningRegulationIndexError,
    PlanningRegulationSearchResult,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`.
- type annotation: `src/landscout/stages/index_planning_regulation.py::search_planning_regulation` via `PlanningRegulationSearchResult`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::search_planning_regulation` via `PlanningRegulationSearchResult`.
- type annotation: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_search_result` via `PlanningRegulationSearchResult`.
- type annotation: `src/landscout/stages/index_planning_regulation.py::validate_planning_regulation_search_result` via `PlanningRegulationSearchResult`.

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

**Purpose:** Immutable result/value envelope carrying `relative_path`, `size_bytes`, `sha256`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `relative_path` | `relative_path: str` | Filesystem location for the artifact named by the field; containment, portability, link, existence, and recovery checks belong to the owning source/artifact validator. |
| `size_bytes` | `size_bytes: int` | Measured physical file size in bytes for this artifact or extracted source member. |
| `sha256` | `sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |

**Interface consumers**

- type annotation: `src/landscout/stages/index_planning_regulation.py::_ZoningSourceEvidence` via `_ZoningSourceFileIntegrity`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::_revalidate_zoning_source` via `_ZoningSourceFileIntegrity`.

**Exact class source**

```python
class _ZoningSourceFileIntegrity:
    relative_path: str
    size_bytes: int
    sha256: str
```

### `_ZoningSourceEvidence`

**Purpose:** Immutable result/value envelope carrying `source_layer`, `driver`, `files`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `source_layer` | `source_layer: str` | Exact source-lineage scalar named by the field; it is compared with configuration/result/row lineage but is not physical proof without source-byte revalidation. |
| `driver` | `driver: str` | Physical GIS driver reported for the inspected source file/layer. |
| `files` | `files: tuple[_ZoningSourceFileIntegrity, ...]` | Ordered collection of the named source/configuration records; member type, uniqueness, order, and identity are validated by the owning model/source boundary. |

**Interface consumers**

- type annotation: `src/landscout/stages/index_planning_regulation.py::_revalidate_zoning_source` via `_ZoningSourceEvidence`.
- constructor call: `src/landscout/stages/index_planning_regulation.py::_revalidate_zoning_source` via `_ZoningSourceEvidence`.
- type annotation: `src/landscout/stages/index_planning_regulation.py::_resolve_regulation_filename` via `_ZoningSourceEvidence`.
- type annotation: `src/landscout/stages/index_planning_regulation.py::_source_selection_sha256` via `_ZoningSourceEvidence`.

**Exact class source**

```python
class _ZoningSourceEvidence:
    source_layer: str
    driver: str
    files: tuple[_ZoningSourceFileIntegrity, ...]
```


## 6. Functions and methods

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
- Explicit raise expressions: `PlanningRegulationIndexError(f'{label} must be a non-empty exact string')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::_validated_sha256` via `_strict_string`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_validated_relative_path` via `_strict_string`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_validated_pdf_basename` via `_strict_string`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_validate_document_lineage` via `_strict_string`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_written_file_matches` via `_strict_string`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_locate_regulation_pdf` via `_strict_string`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_index` via `_strict_string`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_validated_terms` via `_strict_string`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_search_result` via `_strict_string`.

**Complete source-ordered implementation**

```python
def _strict_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise PlanningRegulationIndexError(
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
int(value)
```

**Validation and exceptions**

- Guard with a raise path: `isinstance(value, bool) or not isinstance(value, Integral)`.
- Guard with a raise path: `value < 0`.
- Explicit raise expressions: `PlanningRegulationIndexError(f'{label} must be an integer')`, `PlanningRegulationIndexError(f'{label} must be non-negative')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::_strict_positive_integer` via `_strict_nonnegative_integer`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_validate_pages` via `_strict_nonnegative_integer`.
- direct call: `src/landscout/stages/index_planning_regulation.py::search_planning_regulation` via `_strict_nonnegative_integer`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_search_result` via `_strict_nonnegative_integer`.

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
- Explicit raise expressions: `PlanningRegulationIndexError(f'{label} must be positive')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::_supported_schema_version` via `_strict_positive_integer`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_locate_regulation_pdf` via `_strict_positive_integer`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_validate_pages` via `_strict_positive_integer`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_index` via `_strict_positive_integer`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_search_result` via `_strict_positive_integer`.

**Complete source-ordered implementation**

```python
def _strict_positive_integer(value: object, label: str) -> int:
    result = _strict_nonnegative_integer(value, label)
    if result == 0:
        raise PlanningRegulationIndexError(f"{label} must be positive")
    return result
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_supported_schema_version`

**Exact signature**

```python
def _supported_schema_version(value: object, supported: int, label: str) -> int:
```

**Purpose**

Private `planning` helper for supported schema version; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `int`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- Guard with a raise path: `result != supported`.
- Explicit raise expressions: `PlanningRegulationIndexError(f'Unsupported {label}: {result}; expected {supported}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_index` via `_supported_schema_version`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_search_result` via `_supported_schema_version`.

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

- Guard with a raise path: `fullmatch('[0-9a-f]{64}', checksum) is None`.
- Explicit raise expressions: `PlanningRegulationIndexError(f'{label} must contain exactly 64 lowercase hexadecimal characters')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::_validate_document_lineage` via `_validated_sha256`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_locate_regulation_pdf` via `_validated_sha256`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_validate_pages` via `_validated_sha256`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_index` via `_validated_sha256`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_search_result` via `_validated_sha256`.

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
sha256(payload).hexdigest()
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `PlanningRegulationIndexError('Canonical integrity payload cannot be serialized')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `sha256`, `sha256(payload).hexdigest`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::_page_content_sha256` via `_canonical_sha256`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_pages_content_sha256` via `_canonical_sha256`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_index_content_sha256` via `_canonical_sha256`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_source_selection_sha256` via `_canonical_sha256`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_hits_content_sha256` via `_canonical_sha256`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_is_link_or_junction`

**Exact signature**

```python
def _is_link_or_junction(path: Path) -> bool:
```

**Purpose**

Tests whether link or junction; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
path.is_symlink() or path.is_junction()
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `PlanningRegulationIndexError(f'Cannot inspect GPU extraction path safely: {path}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::_locate_regulation_pdf` via `_is_link_or_junction`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validated_relative_path`

**Exact signature**

```python
def _validated_relative_path(value: object) -> PurePosixPath:
```

**Purpose**

Checks and returns canonical relative path; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `PurePosixPath`.
- Every observed return expression is reproduced without truncation:
```python
relative
```

**Validation and exceptions**

- Guard with a raise path: `'\\' in raw or '\x00' in raw`.
- Guard with a raise path: `any((part in {'', '.', '..'} for part in parts))`.
- Guard with a raise path: `relative.is_absolute() or relative.as_posix() != raw`.
- Explicit raise expressions: `PlanningRegulationIndexError('GPU inventory path is unsafe')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::_locate_regulation_pdf` via `_validated_relative_path`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_index` via `_validated_relative_path`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validated_pdf_basename`

**Exact signature**

```python
def _validated_pdf_basename(value: object) -> str:
```

**Purpose**

Checks and returns canonical pdf basename; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
name
```

**Validation and exceptions**

- Guard with a raise path: `name in {'.', '..'} or '/' in name or '\\' in name or (Path(name).name != name) or (not name.casefold().endswith('.pdf')) or any((ord(character) < 32 or ord(character) == 127 for character in name))`.
- Explicit raise expressions: `PlanningRegulationIndexError('regulation PDF filename must be one safe PDF basename')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::_zoning_regulation_filenames` via `_validated_pdf_basename`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_resolve_regulation_filename` via `_validated_pdf_basename`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_index` via `_validated_pdf_basename`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_file_sha256`

**Exact signature**

```python
def _file_sha256(path: Path) -> str:
```

**Purpose**

Private `planning` helper for file sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
digest.hexdigest()
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `PlanningRegulationIndexError('Regulation PDF checksum cannot be calculated')`.

**Side effects**

- Network I/O: none.
- Filesystem read: `path.open`, `stream.read`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `digest.hexdigest`, `sha256`.
- Environment/process effects: none.
- In-memory mutation: `digest`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::_locate_regulation_pdf` via `_file_sha256`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_index_planning_regulation` via `_file_sha256`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_revalidate_zoning_source`

**Exact signature**

```python
def _revalidate_zoning_source(
    planning_document: GpuPlanningDocument,
) -> tuple[gpd.GeoDataFrame, _ZoningSourceEvidence]:
```

**Purpose**

Re-read immutable zoning bytes before trusting source PDF references.

**Return contract**

- Declared return annotation: `tuple[gpd.GeoDataFrame, _ZoningSourceEvidence]`.
- Every observed return expression is reproduced without truncation:
```python
(source.data, _ZoningSourceEvidence(source_layer=source.source_layer, driver=source.driver, files=tuple((_ZoningSourceFileIntegrity(relative_path=item.relative_path, size_bytes=item.size_bytes, sha256=item.sha256) for item in source.files))))
```

**Validation and exceptions**

- Guard with a raise path: `'NOMFIC' not in source.data.columns`.
- Explicit raise expressions: `PlanningRegulationIndexError('GPU zoning is missing NOMFIC')`, `PlanningRegulationIndexError('GPU zoning source cannot be revalidated')`, `PlanningRegulationIndexError(f'GPU zoning source integrity cannot be revalidated: {error}')`, `re-raise`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::_resolve_regulation_filename` via `_revalidate_zoning_source`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_document_lineage`

**Exact signature**

```python
def _validate_document_lineage(planning_document: GpuPlanningDocument) -> tuple[str, str]:
```

**Purpose**

Rejects malformed or inconsistent document lineage; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[str, str]`.
- Every observed return expression is reproduced without truncation:
```python
(document_id, archive_sha)
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(planning_document, GpuPlanningDocument)`.
- Guard with a raise path: `not isinstance(extraction, GpuExtraction)`.
- Guard with a raise path: `not isinstance(archive, GpuArchiveDownload) or not isinstance(archive.document, GpuDocumentMetadata)`.
- Guard with a raise path: `not isinstance(archive.archive_format, str) or archive.archive_format.casefold() != 'zip'`.
- Guard with a raise path: `metadata.document_family != 'DU' or metadata.status != 'document.production' or metadata.legal_status != 'APPROVED' or (metadata.effective_status != 'EN_VIGUEUR')`.
- Guard with a raise path: `type(planning_document.related_layers) is not tuple or type(planning_document.all_spatial_layers) is not tuple`.
- Guard with a raise path: `planning_document.zoning.logical_name != 'zoning'`.
- Guard with a raise path: `planning_document.zoning.reference not in planning_document.all_spatial_layers`.
- Guard with a raise path: `layer.summary.source_document_id != document_id or layer.summary.source_archive_sha256 != archive_sha or layer.summary.source_layer != layer.reference.source_layer or (layer.summary.feature_count != len(layer.data))`.
- Explicit raise expressions: `PlanningRegulationIndexError('GPU archive format must be zip')`, `PlanningRegulationIndexError('GPU archive lineage is invalid')`, `PlanningRegulationIndexError('GPU extraction lineage is invalid')`, `PlanningRegulationIndexError('GPU planning document is not the current effective DU')`, `PlanningRegulationIndexError('GPU spatial-layer lineage is inconsistent with the archive')`, `PlanningRegulationIndexError('GPU spatial-layer lineage is invalid')`, `PlanningRegulationIndexError('GPU zoning logical layer is invalid')`, `PlanningRegulationIndexError('GPU zoning reference is absent from discovered spatial layers')`, `PlanningRegulationIndexError('planning_document must be a GpuPlanningDocument')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_validated_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::_index_planning_regulation` via `_validate_document_lineage`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_zoning_regulation_filenames`

**Exact signature**

```python
def _zoning_regulation_filenames(zoning: gpd.GeoDataFrame) -> tuple[str, ...]:
```

**Purpose**

Private `planning` helper for zoning regulation filenames; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[str, ...]`.
- Every observed return expression is reproduced without truncation:
```python
tuple(sorted(values, key=str.casefold))
```

**Validation and exceptions**

- Guard with a raise path: `'NOMFIC' not in zoning.columns`.
- Guard with a raise path: `not values`.
- Explicit raise expressions: `PlanningRegulationIndexError('GPU zoning NOMFIC contains no regulation filename')`, `PlanningRegulationIndexError('GPU zoning NOMFIC values cannot be validated')`, `PlanningRegulationIndexError('GPU zoning is missing NOMFIC')`, `re-raise`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `values`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::_resolve_regulation_filename` via `_zoning_regulation_filenames`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_written_file_matches`

**Exact signature**

```python
def _written_file_matches(
    planning_document: GpuPlanningDocument, filename: str
) -> tuple[GpuWrittenFile, ...]:
```

**Purpose**

Private `planning` helper for written file matches; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[GpuWrittenFile, ...]`.
- Every observed return expression is reproduced without truncation:
```python
tuple(matches)
```

**Validation and exceptions**

- Guard with a raise path: `type(written_files) is not tuple`.
- Guard with a raise path: `not matches`.
- Guard with a raise path: `len(matches) != 1`.
- Guard with a raise path: `not isinstance(item, GpuWrittenFile)`.
- Explicit raise expressions: `PlanningRegulationIndexError('GPU written-files metadata is invalid')`, `PlanningRegulationIndexError('GPU written-files metadata must be an immutable tuple')`, `PlanningRegulationIndexError(f'Regulation PDF is absent from official written_files: {filename}')`, `PlanningRegulationIndexError(f'Regulation PDF is duplicated in official written_files: {filename}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `matches`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::_resolve_regulation_filename` via `_written_file_matches`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_resolve_regulation_filename`

**Exact signature**

```python
def _resolve_regulation_filename(
    planning_document: GpuPlanningDocument,
    regulation_filename: str | None,
) -> tuple[str, str, _ZoningSourceEvidence, GpuWrittenFile]:
```

**Purpose**

Resolves regulation filename; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[str, str, _ZoningSourceEvidence, GpuWrittenFile]`.
- Every observed return expression is reproduced without truncation:
```python
(selected, method, zoning_evidence, written_file)
```

**Validation and exceptions**

- Guard with a raise path: `regulation_filename is None`.
- Guard with a raise path: `len(referenced) != 1`.
- Guard with a raise path: `selected not in referenced`.
- Explicit raise expressions: `PlanningRegulationIndexError('Explicit regulation filename is not referenced by zoning NOMFIC')`, `PlanningRegulationIndexError('GPU zoning NOMFIC regulation selection is ambiguous')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::_index_planning_regulation` via `_resolve_regulation_filename`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_locate_regulation_pdf`

**Exact signature**

```python
def _locate_regulation_pdf(
    planning_document: GpuPlanningDocument,
    pdf_basename: str,
) -> tuple[Path, GpuExtractedFile]:
```

**Purpose**

Private `planning` helper for locate regulation pdf; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[Path, GpuExtractedFile]`.
- Every observed return expression is reproduced without truncation:
```python
(path, item)
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(root, Path) or _is_link_or_junction(root) or (not root.is_dir())`.
- Guard with a raise path: `not matches`.
- Guard with a raise path: `len(matches) != 1`.
- Guard with a raise path: `file_type.casefold() != 'pdf' or item.category != 'WRITTEN_REGULATION'`.
- Guard with a raise path: `not path.is_file()`.
- Guard with a raise path: `actual_size != expected_size`.
- Guard with a raise path: `_file_sha256(path) != expected_sha`.
- Guard with a raise path: `not isinstance(item, GpuExtractedFile)`.
- Guard with a raise path: `item.relative_path in inventory_paths`.
- Guard with a raise path: `_is_link_or_junction(current)`.
- Explicit raise expressions: `PlanningRegulationIndexError('GPU extraction inventory contains duplicate paths')`, `PlanningRegulationIndexError('GPU extraction inventory is invalid')`, `PlanningRegulationIndexError('GPU extraction root cannot be resolved safely')`, `PlanningRegulationIndexError('GPU extraction root must be a regular directory')`, `PlanningRegulationIndexError('Regulation PDF SHA256 differs from extraction inventory')`, `PlanningRegulationIndexError('Regulation PDF inventory classification is inconsistent')`, `PlanningRegulationIndexError('Regulation PDF must be an extracted regular file')`, `PlanningRegulationIndexError('Regulation PDF path contains a symbolic link or junction')`, `PlanningRegulationIndexError('Regulation PDF path escapes the GPU extraction root')`, `PlanningRegulationIndexError('Regulation PDF size cannot be read')`, `PlanningRegulationIndexError('Regulation PDF size differs from extraction inventory')`, `PlanningRegulationIndexError(f'Regulation PDF is ambiguous in GPU inventory: {pdf_basename}')`, `PlanningRegulationIndexError(f'Regulation PDF is missing from GPU inventory: {pdf_basename}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: `path.is_file`, `path.stat`, `root.is_dir`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_file_sha256`, `_validated_sha256`.
- Environment/process effects: none.
- In-memory mutation: `inventory_paths`, `matches`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::_index_planning_regulation` via `_locate_regulation_pdf`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_page_error`

**Exact signature**

```python
def _page_error(error: Exception) -> str:
```

**Purpose**

Private `planning` helper for page error; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
f'{type(error).__name__}: {message}' if message else type(error).__name__
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::_index_planning_regulation` via `_page_error`.

**Complete source-ordered implementation**

```python
def _page_error(error: Exception) -> str:
    message = sub(r"\s+", " ", str(error)).strip()
    return f"{type(error).__name__}: {message}" if message else type(error).__name__
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_page_record`

**Exact signature**

```python
def _canonical_page_record(row: dict[str, object]) -> dict[str, object]:
```

**Purpose**

Private `planning` helper for canonical page record; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
record
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `record['extraction_error']`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::_page_hash_payload` via `_canonical_page_record`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_pages_content_sha256` via `_canonical_page_record`.

**Complete source-ordered implementation**

```python
def _canonical_page_record(row: dict[str, object]) -> dict[str, object]:
    record = {
        key: row[key]
        for key in PAGE_COLUMNS
        if key != "page_content_sha256"
    }
    if bool(pd.isna(record["extraction_error"])):
        record["extraction_error"] = None
    return record
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_page_hash_payload`

**Exact signature**

```python
def _page_hash_payload(
    row: dict[str, object],
    page_hash_schema_version: int = PAGE_HASH_SCHEMA_VERSION,
    search_normalization_profile: str = SEARCH_NORMALIZATION_PROFILE,
) -> dict[str, object]:
```

**Purpose**

Private `planning` helper for page hash payload; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
{'schema_version': page_hash_schema_version, 'search_normalization_profile': search_normalization_profile, 'page': _canonical_page_record(row)}
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::_page_content_sha256` via `_page_hash_payload`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_page_content_sha256`

**Exact signature**

```python
def _page_content_sha256(
    row: dict[str, object],
    page_hash_schema_version: int = PAGE_HASH_SCHEMA_VERSION,
    search_normalization_profile: str = SEARCH_NORMALIZATION_PROFILE,
) -> str:
```

**Purpose**

Private `planning` helper for page content sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_sha256(_page_hash_payload(row, page_hash_schema_version, search_normalization_profile))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_canonical_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- import: `tests/unit/test_interpret_bess_zoning.py::<module>` via `from landscout.stages.index_planning_regulation import (
    INDEX_HASH_SCHEMA_VERSION,
    PAGE_HASH_SCHEMA_VERSION,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndex,
    _index_content_sha256,
    _normalize_search_text,
    _page_content_sha256,
    _pages_content_sha256,
)`.
- import: `tests/unit/test_structure_planning_regulation.py::<module>` via `from landscout.stages.index_planning_regulation import (
    INDEX_HASH_SCHEMA_VERSION,
    PAGE_HASH_SCHEMA_VERSION,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndex,
    _index_content_sha256,
    _normalize_search_text,
    _page_content_sha256,
    _pages_content_sha256,
)`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_validate_pages` via `_page_content_sha256`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_index_planning_regulation` via `_page_content_sha256`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::_index` via `_page_content_sha256`.
- direct call: `tests/unit/test_structure_planning_regulation.py::_index` via `_page_content_sha256`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_pages_content_sha256`

**Exact signature**

```python
def _pages_content_sha256(
    frame: pd.DataFrame,
    page_hash_schema_version: int = PAGE_HASH_SCHEMA_VERSION,
    search_normalization_profile: str = SEARCH_NORMALIZATION_PROFILE,
) -> str:
```

**Purpose**

Private `planning` helper for pages content sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_sha256({'schema_version': page_hash_schema_version, 'search_normalization_profile': search_normalization_profile, 'pages': pages})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_canonical_sha256`.
- Environment/process effects: none.
- In-memory mutation: `canonical['page_content_sha256']`, `pages`.
- Input mutation: none.

**Repository interfaces and consumers**

- import: `tests/unit/test_interpret_bess_zoning.py::<module>` via `from landscout.stages.index_planning_regulation import (
    INDEX_HASH_SCHEMA_VERSION,
    PAGE_HASH_SCHEMA_VERSION,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndex,
    _index_content_sha256,
    _normalize_search_text,
    _page_content_sha256,
    _pages_content_sha256,
)`.
- import: `tests/unit/test_structure_planning_regulation.py::<module>` via `from landscout.stages.index_planning_regulation import (
    INDEX_HASH_SCHEMA_VERSION,
    PAGE_HASH_SCHEMA_VERSION,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndex,
    _index_content_sha256,
    _normalize_search_text,
    _page_content_sha256,
    _pages_content_sha256,
)`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_index_planning_regulation` via `_pages_content_sha256`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_index` via `_pages_content_sha256`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::_index` via `_pages_content_sha256`.
- direct call: `tests/unit/test_structure_planning_regulation.py::_index` via `_pages_content_sha256`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_pages_frame`

**Exact signature**

```python
def _pages_frame(rows: list[dict[str, object]]) -> pd.DataFrame:
```

**Purpose**

Private `planning` helper for pages frame; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
frame
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `frame['character_count']`, `frame['page_number']`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::_index_planning_regulation` via `_pages_frame`.

**Complete source-ordered implementation**

```python
def _pages_frame(rows: list[dict[str, object]]) -> pd.DataFrame:
    frame = pd.DataFrame(rows, columns=PAGE_COLUMNS)
    frame["page_number"] = frame["page_number"].astype("int64")
    frame["character_count"] = frame["character_count"].astype("int64")
    return frame
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_index_hash_payload`

**Exact signature**

```python
def _index_hash_payload(index: PlanningRegulationIndex) -> dict[str, object]:
```

**Purpose**

Private `planning` helper for index hash payload; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
{'domain': 'landscout.planning_regulation.index', 'index_hash_schema_version': index.index_hash_schema_version, 'document_id': index.document_id, 'archive_sha256': index.archive_sha256, 'regulation_filename': index.regulation_filename, 'source_selection_method': index.source_selection_method, 'source_selection_sha256': index.source_selection_sha256, 'pdf_relative_path': index.pdf_relative_path, 'pdf_size_bytes': index.pdf_size_bytes, 'pdf_sha256': index.pdf_sha256, 'extraction_library': index.extraction_library, 'extraction_library_version': index.extraction_library_version, 'search_normalization_profile': index.search_normalization_profile, 'page_hash_schema_version': index.page_hash_schema_version, 'total_page_count': index.total_page_count, 'pages_content_sha256': index.pages_content_sha256}
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::_index_content_sha256` via `_index_hash_payload`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_index_content_sha256`

**Exact signature**

```python
def _index_content_sha256(index: PlanningRegulationIndex) -> str:
```

**Purpose**

Private `planning` helper for index content sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_sha256(_index_hash_payload(index))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_canonical_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- import: `tests/unit/test_interpret_bess_zoning.py::<module>` via `from landscout.stages.index_planning_regulation import (
    INDEX_HASH_SCHEMA_VERSION,
    PAGE_HASH_SCHEMA_VERSION,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndex,
    _index_content_sha256,
    _normalize_search_text,
    _page_content_sha256,
    _pages_content_sha256,
)`.
- import: `tests/unit/test_structure_planning_regulation.py::<module>` via `from landscout.stages.index_planning_regulation import (
    INDEX_HASH_SCHEMA_VERSION,
    PAGE_HASH_SCHEMA_VERSION,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndex,
    _index_content_sha256,
    _normalize_search_text,
    _page_content_sha256,
    _pages_content_sha256,
)`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_index_planning_regulation` via `_index_content_sha256`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_index` via `_index_content_sha256`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::_index` via `_index_content_sha256`.
- direct call: `tests/unit/test_structure_planning_regulation.py::_index` via `_index_content_sha256`.

**Complete source-ordered implementation**

```python
def _index_content_sha256(index: PlanningRegulationIndex) -> str:
    return _canonical_sha256(_index_hash_payload(index))
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_source_selection_sha256`

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

**Purpose**

Private `planning` helper for source selection sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_sha256({'domain': 'landscout.planning_regulation.source_selection', 'regulation_filename': filename, 'source_selection_method': method, 'zoning': {'source_layer': zoning_evidence.source_layer, 'driver': zoning_evidence.driver, 'source_files': [{'relative_path': item.relative_path, 'size_bytes': item.size_bytes, 'sha256': item.sha256} for item in zoning_evidence.files]}, 'written_file': {'filename': written_file.filename, 'title': written_file.title, 'document_path': written_file.document_path, 'source_url': written_file.source_url}, 'pdf_inventory': {'relative_path': pdf_inventory.relative_path, 'size_bytes': pdf_inventory.size_bytes, 'sha256': pdf_inventory.sha256, 'file_type': pdf_inventory.file_type, 'category': pdf_inventory.category}})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_canonical_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::_index_planning_regulation` via `_source_selection_sha256`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_pages`

**Exact signature**

```python
def _validate_pages(
    frame: pd.DataFrame,
    total_page_count: int,
    page_hash_schema_version: int,
    search_normalization_profile: str,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent pages; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `not isinstance(frame, pd.DataFrame)`.
- Guard with a raise path: `tuple(frame.columns) != PAGE_COLUMNS`.
- Guard with a raise path: `len(frame) != total_page_count`.
- Guard with a raise path: `frame['page_number'].tolist() != list(range(1, total_page_count + 1))`.
- Guard with a raise path: `not frame['extraction_status'].isin({'TEXT', 'EMPTY', 'ERROR'}).all()`.
- Guard with a raise path: `not isinstance(raw_text, str) or not isinstance(normalized, str)`.
- Guard with a raise path: `character_count != len(raw_text)`.
- Guard with a raise path: `normalized != _normalize_search_text(raw_text)`.
- Guard with a raise path: `status == 'TEXT' and (not normalized or not error_is_null)`.
- Guard with a raise path: `status == 'EMPTY' and (normalized or not error_is_null)`.
- Guard with a raise path: `status == 'ERROR' and (raw_text or normalized or (not isinstance(extraction_error, str)) or (not extraction_error))`.
- Guard with a raise path: `checksum != _page_content_sha256(row, page_hash_schema_version, search_normalization_profile)`.
- Explicit raise expressions: `PlanningRegulationIndexError('EMPTY page state is inconsistent')`, `PlanningRegulationIndexError('ERROR page state is inconsistent')`, `PlanningRegulationIndexError('Regulation extraction status is invalid')`, `PlanningRegulationIndexError('Regulation normalized search text is inconsistent')`, `PlanningRegulationIndexError('Regulation page character count is inconsistent')`, `PlanningRegulationIndexError('Regulation page content hash differs')`, `PlanningRegulationIndexError('Regulation page count is inconsistent')`, `PlanningRegulationIndexError('Regulation page numbers must be unique and ordered from 1')`, `PlanningRegulationIndexError('Regulation page schema is not deterministic')`, `PlanningRegulationIndexError('Regulation page text must be a string')`, `PlanningRegulationIndexError('Regulation pages must be a DataFrame')`, `PlanningRegulationIndexError('TEXT page state is inconsistent')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_page_content_sha256`, `_validated_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_index` via `_validate_pages`.

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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_pypdf_version`

**Exact signature**

```python
def _pypdf_version() -> str:
```

**Purpose**

Private `planning` helper for pypdf version; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
version('pypdf')
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `PlanningRegulationIndexError('pypdf package version cannot be determined')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::_index_planning_regulation` via `_pypdf_version`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_index_planning_regulation`

**Exact signature**

```python
def _index_planning_regulation(
    planning_document: GpuPlanningDocument,
    regulation_filename: str | None = None,
) -> PlanningRegulationIndex:
```

**Purpose**

Index the source-validated primary written regulation page by page.

**Return contract**

- Declared return annotation: `PlanningRegulationIndex`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- Guard with a raise path: `final_size != inventory.size_bytes or final_sha != inventory.sha256`.
- Guard with a raise path: `reader.is_encrypted`.
- Guard with a raise path: `total_page_count == 0`.
- Guard with a raise path: `not isinstance(raw_text, str)`.
- Explicit raise expressions: `PlanningRegulationIndexError('Encrypted regulation PDFs are not supported')`, `PlanningRegulationIndexError('Regulation PDF cannot be opened or parsed')`, `PlanningRegulationIndexError('Regulation PDF changed during text extraction')`, `PlanningRegulationIndexError('Regulation PDF must contain at least one page')`, `PlanningRegulationIndexError('Regulation PDF size cannot be revalidated')`, `TypeError('PDF page extractor returned non-text data')`, `re-raise`.

**Side effects**

- Network I/O: none.
- Filesystem read: `path.open`, `path.stat`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_file_sha256`, `_index_content_sha256`, `_page_content_sha256`, `_pages_content_sha256`, `_source_selection_sha256`.
- Environment/process effects: none.
- In-memory mutation: `row['page_content_sha256']`, `rows`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::index_planning_regulation` via `_index_planning_regulation`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `index_planning_regulation`

**Exact signature**

```python
def index_planning_regulation(
    planning_document: GpuPlanningDocument,
    regulation_filename: str | None = None,
) -> PlanningRegulationIndex:
```

**Purpose**

Index one source-validated written regulation with controlled failures.

**Return contract**

- Declared return annotation: `PlanningRegulationIndex`.
- Every observed return expression is reproduced without truncation:
```python
_index_planning_regulation(planning_document, regulation_filename)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `PlanningRegulationIndexError('Planning regulation indexing failed safely')`, `re-raise`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    PlanningRegulationIndexError,
    PlanningRegulationSearchResult,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`.
- import: `tests/unit/test_index_planning_regulation.py::<module>` via `from landscout.stages.index_planning_regulation import (
    PAGE_COLUMNS,
    SEARCH_HIT_COLUMNS,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndexError,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`.
- direct call: `tests/unit/test_index_planning_regulation.py::_one_page_index` via `index_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_source_nomfic_resolves_generic_filename` via `index_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_explicit_source_validated_selection_succeeds` via `index_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_unchanged_zoning_source_is_revalidated_before_selection` via `index_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_mutated_loaded_nomfic_is_rejected_before_selection` via `index_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_mutated_loaded_zoning_geometry_or_order_is_rejected` via `index_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_zoning_source_bytes_changed_after_ingestion_are_rejected` via `index_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_zoning_source_inventory_integrity_mismatch_is_rejected` via `index_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_missing_nomfic_field_is_rejected` via `index_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_null_nomfic_is_rejected` via `index_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_multiple_nomfic_values_are_ambiguous` via `index_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_unsafe_explicit_filename_is_rejected` via `index_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_explicit_filename_not_referenced_by_zoning_fails` via `index_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_filename_absent_from_written_files_fails` via `index_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_unrelated_non_pdf_written_file_does_not_block_selection` via `index_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_filename_absent_from_inventory_fails` via `index_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_duplicate_inventory_basename_fails` via `index_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_path_outside_root_is_rejected` via `index_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_pdf_inventory_integrity_mismatch_fails` via `index_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_page_states_numbering_and_hashes` via `index_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_zero_page_pdf_is_rejected` via `index_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_pdf_reader_failure_is_controlled_and_chained` via `index_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_version_discovery_failure_is_controlled_and_chained` via `index_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_index_integrity_mutations_fail` via `index_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_malformed_source_metadata_raises_controlled_index_error` via `index_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_extraction_and_search_do_not_mutate_inputs` via `index_planning_regulation`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_planning_regulation_index`

**Exact signature**

```python
def _validate_planning_regulation_index(index: PlanningRegulationIndex) -> None:
```

**Purpose**

Rejects malformed or inconsistent planning regulation index; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `not isinstance(index, PlanningRegulationIndex)`.
- Guard with a raise path: `index.source_selection_method not in {'ZONING_NOMFIC', 'EXPLICIT_ZONING_NOMFIC'}`.
- Guard with a raise path: `relative_pdf.name != filename`.
- Guard with a raise path: `index.extraction_library != 'pypdf'`.
- Guard with a raise path: `index.search_normalization_profile != SEARCH_NORMALIZATION_PROFILE`.
- Guard with a raise path: `checksum != _pages_content_sha256(index.pages, page_schema, index.search_normalization_profile)`.
- Guard with a raise path: `index_checksum != _index_content_sha256(index)`.
- Explicit raise expressions: `PlanningRegulationIndexError('Regulation extraction library differs')`, `PlanningRegulationIndexError('Regulation filename differs from PDF relative path')`, `PlanningRegulationIndexError('Regulation index envelope hash differs')`, `PlanningRegulationIndexError('Regulation pages envelope hash differs')`, `PlanningRegulationIndexError('Regulation search normalization profile is unsupported')`, `PlanningRegulationIndexError('Regulation source-selection method is unsupported')`, `PlanningRegulationIndexError('index must be a PlanningRegulationIndex')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_index_content_sha256`, `_pages_content_sha256`, `_validated_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::validate_planning_regulation_index` via `_validate_planning_regulation_index`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_planning_regulation_index`

**Exact signature**

```python
def validate_planning_regulation_index(index: PlanningRegulationIndex) -> None:
```

**Purpose**

Validate all page, metadata, and complete index integrity contracts.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `PlanningRegulationIndexError('Regulation index validation failed safely')`, `re-raise`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    PlanningRegulationIndexError,
    PlanningRegulationSearchResult,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`.
- import: `src/landscout/stages/interpret_bess_zoning.py::<module>` via `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    validate_planning_regulation_index,
)`.
- import: `src/landscout/stages/structure_planning_regulation.py::<module>` via `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    validate_planning_regulation_index,
)`.
- import: `tests/unit/test_index_planning_regulation.py::<module>` via `from landscout.stages.index_planning_regulation import (
    PAGE_COLUMNS,
    SEARCH_HIT_COLUMNS,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndexError,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_index_planning_regulation` via `validate_planning_regulation_index`.
- direct call: `src/landscout/stages/index_planning_regulation.py::search_planning_regulation` via `validate_planning_regulation_index`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_search_result` via `validate_planning_regulation_index`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_result` via `validate_planning_regulation_index`.
- direct call: `src/landscout/stages/structure_planning_regulation.py::_validate_document_lock` via `validate_planning_regulation_index`.
- direct call: `src/landscout/stages/structure_planning_regulation.py::_validate_result_self` via `validate_planning_regulation_index`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_page_states_numbering_and_hashes` via `validate_planning_regulation_index`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_coordinated_page_mutation_fails_envelope_hash` via `validate_planning_regulation_index`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_index_integrity_mutations_fail` via `validate_planning_regulation_index`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_complete_index_envelope_mutation_is_rejected` via `validate_planning_regulation_index`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_unsupported_or_malformed_index_hash_schema_is_rejected` via `validate_planning_regulation_index`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_malformed_page_hash_schema_is_rejected_as_controlled_error` via `validate_planning_regulation_index`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_malformed_page_value_raises_controlled_index_error` via `validate_planning_regulation_index`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validated_terms`

**Exact signature**

```python
def _validated_terms(terms: Sequence[str]) -> tuple[tuple[str, str], ...]:
```

**Purpose**

Checks and returns canonical terms; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[tuple[str, str], ...]`.
- Every observed return expression is reproduced without truncation:
```python
tuple(result)
```

**Validation and exceptions**

- Guard with a raise path: `isinstance(terms, (str, bytes)) or not isinstance(terms, Sequence)`.
- Guard with a raise path: `not normalized_term or normalized_term in normalized_seen`.
- Explicit raise expressions: `PlanningRegulationIndexError('Search terms must be a sequence of terms')`, `PlanningRegulationIndexError('Search terms must be unique after normalization')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `normalized_seen`, `result`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::search_planning_regulation` via `_validated_terms`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_search_result` via `_validated_terms`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_empty_hits`

**Exact signature**

```python
def _empty_hits() -> pd.DataFrame:
```

**Purpose**

Private `planning` helper for empty hits; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
pd.DataFrame({column: pd.Series(dtype='int64' if column in {'page_number', 'occurrence_count'} else 'object') for column in SEARCH_HIT_COLUMNS})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::_build_hits` via `_empty_hits`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_build_hits`

**Exact signature**

```python
def _build_hits(
    index: PlanningRegulationIndex,
    terms: tuple[tuple[str, str], ...],
    context_characters: int,
) -> pd.DataFrame:
```

**Purpose**

Constructs hits; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
frame

_empty_hits()
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `frame['occurrence_count']`, `frame['page_number']`, `hits`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::search_planning_regulation` via `_build_hits`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_search_result` via `_build_hits`.

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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_hits_content_sha256`

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

**Purpose**

Private `planning` helper for hits content sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_sha256({'domain': 'landscout.planning_regulation.search', 'search_hash_schema_version': search_hash_schema_version, 'index_content_sha256': index.index_content_sha256, 'document_id': index.document_id, 'archive_sha256': index.archive_sha256, 'pdf_sha256': index.pdf_sha256, 'search_normalization_profile': index.search_normalization_profile, 'requested_terms': list(requested_terms), 'context_characters': context_characters, 'hit_count': len(hits), 'hits': hits.loc[:, SEARCH_HIT_COLUMNS].to_dict('records')})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_canonical_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::search_planning_regulation` via `_hits_content_sha256`.
- direct call: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_search_result` via `_hits_content_sha256`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `search_planning_regulation`

**Exact signature**

```python
def search_planning_regulation(
    index: PlanningRegulationIndex,
    terms: Sequence[str],
    *,
    context_characters: int = 80,
) -> PlanningRegulationSearchResult:
```

**Purpose**

Return sealed literal search hits with raw and normalized contexts.

**Return contract**

- Declared return annotation: `PlanningRegulationSearchResult`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_hits_content_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    PlanningRegulationIndexError,
    PlanningRegulationSearchResult,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`.
- import: `tests/unit/test_index_planning_regulation.py::<module>` via `from landscout.stages.index_planning_regulation import (
    PAGE_COLUMNS,
    SEARCH_HIT_COLUMNS,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndexError,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_raw_context_preserves_source_typography` via `search_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_zero_context_preserves_complete_raw_unicode_span` via `search_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_literal_search_does_not_add_semantic_synonyms` via `search_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::_valid_search_result` via `search_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_search_result_envelope_is_valid_and_deterministic` via `search_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_invalid_search_term_is_rejected` via `search_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_duplicate_normalized_search_terms_are_rejected` via `search_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_empty_search_result_has_stable_schema_and_lineage` via `search_planning_regulation`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_extraction_and_search_do_not_mutate_inputs` via `search_planning_regulation`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_planning_regulation_search_result`

**Exact signature**

```python
def _validate_planning_regulation_search_result(
    index: PlanningRegulationIndex,
    result: PlanningRegulationSearchResult,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent planning regulation search result; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `not isinstance(result, PlanningRegulationSearchResult)`.
- Guard with a raise path: `result.document_id != index.document_id or result.archive_sha256 != index.archive_sha256 or result.pdf_sha256 != index.pdf_sha256 or (result.search_normalization_profile != index.search_normalization_profile) or (result.index_content_sha256 != index.index_content_sha256)`.
- Guard with a raise path: `type(result.requested_terms) is not tuple`.
- Guard with a raise path: `not isinstance(result.hits, pd.DataFrame) or tuple(result.hits.columns) != SEARCH_HIT_COLUMNS`.
- Guard with a raise path: `hit_count != len(result.hits)`.
- Guard with a raise path: `checksum != _hits_content_sha256(index, requested, context, result.hits, search_schema)`.
- Guard with a raise path: `not result.hits.reset_index(drop=True).equals(expected)`.
- Guard with a raise path: `row['document_id'] != index.document_id or row['archive_sha256'] != index.archive_sha256 or row['pdf_sha256'] != index.pdf_sha256 or (row['search_normalization_profile'] != index.search_normalization_profile)`.
- Guard with a raise path: `normalized_term not in allowed_terms`.
- Guard with a raise path: `page_number not in allowed_pages`.
- Guard with a raise path: `pair in seen`.
- Guard with a raise path: `not isinstance(row['raw_context'], str) or not isinstance(row['normalized_context'], str)`.
- Explicit raise expressions: `PlanningRegulationIndexError('Search contexts must be strings')`, `PlanningRegulationIndexError('Search hit has an unrequested term')`, `PlanningRegulationIndexError('Search hit page/term pair is duplicated')`, `PlanningRegulationIndexError('Search hit references an unknown page')`, `PlanningRegulationIndexError('Search-hit lineage differs from index')`, `PlanningRegulationIndexError('Search-hit schema is not deterministic')`, `PlanningRegulationIndexError('Search-result content hash differs')`, `PlanningRegulationIndexError('Search-result hit count differs')`, `PlanningRegulationIndexError('Search-result lineage differs from index')`, `PlanningRegulationIndexError('Search-result requested_terms must be tuple[str, ...]')`, `PlanningRegulationIndexError('Search-result rows differ from deterministic source search')`, `PlanningRegulationIndexError('result must be a PlanningRegulationSearchResult')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_hits_content_sha256`, `_validated_sha256`.
- Environment/process effects: none.
- In-memory mutation: `seen`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/index_planning_regulation.py::validate_planning_regulation_search_result` via `_validate_planning_regulation_search_result`.

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
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_planning_regulation_search_result`

**Exact signature**

```python
def validate_planning_regulation_search_result(
    index: PlanningRegulationIndex,
    result: PlanningRegulationSearchResult,
) -> None:
```

**Purpose**

Validate search lineage, schema, rows, hash, and source-derived contexts.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `PlanningRegulationIndexError('Regulation search-result validation failed safely')`, `re-raise`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    PlanningRegulationIndexError,
    PlanningRegulationSearchResult,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`.
- import: `tests/unit/test_index_planning_regulation.py::<module>` via `from landscout.stages.index_planning_regulation import (
    PAGE_COLUMNS,
    SEARCH_HIT_COLUMNS,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndexError,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`.
- direct call: `src/landscout/stages/index_planning_regulation.py::search_planning_regulation` via `validate_planning_regulation_search_result`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_search_result_envelope_is_valid_and_deterministic` via `validate_planning_regulation_search_result`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_search_index_identity_schema_and_terms_are_sealed` via `validate_planning_regulation_search_result`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_search_requested_terms_must_be_an_immutable_exact_tuple` via `validate_planning_regulation_search_result`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_search_result_integrity_mutations_fail` via `validate_planning_regulation_search_result`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_search_hit_lineage_mutation_fails` via `validate_planning_regulation_search_result`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_empty_search_result_has_stable_schema_and_lineage` via `validate_planning_regulation_search_result`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_malformed_hit_value_raises_controlled_index_error` via `validate_planning_regulation_search_result`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.


## 7. Data contracts

### `PAGE_COLUMNS` — canonical or derived frame-column schema

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

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `page_number` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 2 | `extraction_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | derived factual classification | Stores one value from its separately documented closed domain; domain values are not columns. |
| 3 | `raw_text` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 4 | `normalized_search_text` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 5 | `character_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 6 | `extraction_error` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 7 | `page_content_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |

### `SEARCH_HIT_COLUMNS` — canonical or derived frame-column schema

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

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `document_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 2 | `archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 3 | `pdf_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 4 | `search_normalization_profile` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 5 | `search_term` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `normalized_search_term` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 7 | `page_number` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `occurrence_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 9 | `raw_context` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 10 | `normalized_context` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |


No enum/status/Literal value is classified as a column unless it is separately present in a canonical schema declaration. Mapping keys, JSON keys, dataclass fields, and configuration leaves remain distinct categories.

## 8. Interfaces

This module defines an exact `__all__` contract:

| Export | Kind | Origin | Included in `__all__` |
|---|---|---|---|
| `PlanningRegulationIndex` | public symbol defined in this module | `defined in `src/landscout/stages/index_planning_regulation.py`` | yes |
| `PlanningRegulationIndexError` | public symbol defined in this module | `defined in `src/landscout/stages/index_planning_regulation.py`` | yes |
| `PlanningRegulationSearchResult` | public symbol defined in this module | `defined in `src/landscout/stages/index_planning_regulation.py`` | yes |
| `index_planning_regulation` | public symbol defined in this module | `defined in `src/landscout/stages/index_planning_regulation.py`` | yes |
| `search_planning_regulation` | public symbol defined in this module | `defined in `src/landscout/stages/index_planning_regulation.py`` | yes |
| `validate_planning_regulation_index` | public symbol defined in this module | `defined in `src/landscout/stages/index_planning_regulation.py`` | yes |
| `validate_planning_regulation_search_result` | public symbol defined in this module | `defined in `src/landscout/stages/index_planning_regulation.py`` | yes |

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

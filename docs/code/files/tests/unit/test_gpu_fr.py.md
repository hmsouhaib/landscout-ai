# `tests/unit/test_gpu_fr.py`

## File identity

- Repository path: `tests/unit/test_gpu_fr.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.
- Source SHA256: `a3511fec0dbfae47ed761e7deedaf958a8960fd60e8488d6db478eb0965aeb49`

## 1. Purpose

Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import io`
- `import json`
- `import warnings`
- `import zipfile`
- `from dataclasses import replace`
- `from datetime import UTC, datetime, timedelta`
- `from pathlib import Path`
- `from typing import Self`
- `from urllib.error import URLError`

### Third-party packages

- `import geopandas as gpd`
- `import pytest`
- `from pydantic import HttpUrl, ValidationError`
- `from shapely.geometry import Polygon`

### Internal LandScout imports

- `import landscout.sources.gpu_fr as gpu`
- `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuDiscoveryError,
    GpuDownloadError,
    GpuExtraction,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    validate_gpu_archive,
)`

## 4. Contract taxonomy

### A. Python constants

#### `_UNSAFE_ARCHIVE_NAMES`

```python
_UNSAFE_ARCHIVE_NAMES = (
    "../escape",
    r"..\escape",
    "/absolute",
    r"C:\absolute",
    ".",
    "..",
    " leading",
    "trailing ",
    "nul\x00name",
    "CON",
    "nul.txt",
    "bad:name",
    "bad?.zip",
    "trailing.",
    "archive.zip.zip",
    "a" * 252,
)
```

Module-level technical/source/policy constant consumed by the exact references below.


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `_Response`

**Purpose:** Encapsulates the test behavior implemented by its exact methods and attributes below.

**Kind:** class.

**Inheritance:** `io.BytesIO`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- type annotation: `tests/unit/test_gpu_fr.py::_patch_json_responses.opener` via `_Response`.
- constructor call: `tests/unit/test_gpu_fr.py::_patch_json_responses.opener` via `_Response`.
- constructor call: `tests/unit/test_gpu_fr.py::_download` via `_Response`.
- constructor call: `tests/unit/test_gpu_fr.py::test_archive_name_with_one_zip_suffix_is_not_duplicated` via `_Response`.
- type annotation: `tests/unit/test_gpu_fr.py::test_stale_recovery_backup_rejects_cache_before_network.fail_network` via `_Response`.
- constructor call: `tests/unit/test_gpu_fr.py::test_expired_cache_is_refreshed` via `_Response`.
- type annotation: `tests/unit/test_gpu_fr.py::test_failed_refresh_preserves_previous_cache.fail` via `_Response`.
- constructor call: `tests/unit/test_gpu_fr.py::test_metadata_publication_failure_rolls_back_both_cache_files` via `_Response`.
- constructor call: `tests/unit/test_gpu_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_Response`.
- type annotation: `tests/unit/test_gpu_fr.py::test_preexisting_temporary_archive_symlink_cannot_modify_target.record_network` via `_Response`.
- constructor call: `tests/unit/test_gpu_fr.py::test_preexisting_temporary_archive_symlink_cannot_modify_target.record_network` via `_Response`.
- constructor call: `tests/unit/test_gpu_fr.py::test_corrupt_download_is_rejected` via `_Response`.
- constructor call: `tests/unit/test_gpu_fr.py::test_tampered_sidecar_invalidates_cache` via `_Response`.
- constructor call: `tests/unit/test_gpu_fr.py::test_cached_document_lineage_change_forces_refresh` via `_Response`.

**Exact class source**

```python
class _Response(io.BytesIO):
    def __enter__(self) -> Self:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()
```


## 6. Functions and methods

### `_Response.__enter__`

**Exact signature**

```python
def __enter__(self) -> Self:
```

**Purpose**

Private `test` helper for enter; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Self`.
- Every observed return expression is reproduced without truncation:
```python
self
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

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def __enter__(self) -> Self:
        return self
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_Response.__exit__`

**Exact signature**

```python
def __exit__(self, *args: object) -> None:
```

**Purpose**

Private `test` helper for exit; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

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

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def __exit__(self, *args: object) -> None:
        self.close()
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_config`

**Exact signature**

```python
def _config() -> GpuSourceConfig:
```

**Purpose**

Private `test` helper for config; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `GpuSourceConfig`.
- Every observed return expression is reproduced without truncation:
```python
load_gpu_source_config(Path('configs/sources/gpu_fr.yaml'))
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

- direct call: `tests/unit/test_gpu_fr.py::_document` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::_download` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_valid_config_and_urls` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_invalid_config_values_are_rejected` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_mutated_loaded_api_origin_is_rejected_before_discovery_network` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_unknown_config_field_is_rejected` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_written_material_url_must_be_exact_official_https_api_url` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_written_material_fallback_rejects_unsafe_archive_url_provenance` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_no_current_document_is_rejected` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_ambiguous_current_documents_are_rejected` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_missing_document_identity_is_rejected` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_document_details_must_match_selected_listing` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_document_details_commune_must_match_selected_listing` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_discovery_rejects_unsafe_archive_name` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_download_rejects_document_inconsistent_with_config` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_download_rejects_forged_written_file_provenance_before_network` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_download_rejects_forged_unsafe_archive_name_before_io` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_archive_name_with_one_zip_suffix_is_not_duplicated` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_fresh_cache_is_reused` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_stale_recovery_backup_rejects_cache_before_network` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_expired_cache_is_refreshed` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_failed_refresh_preserves_previous_cache` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_metadata_publication_failure_rolls_back_both_cache_files` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_preexisting_temporary_archive_symlink_cannot_modify_target` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_corrupt_download_is_rejected` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_tampered_sidecar_invalidates_cache` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_spatial_inventory_and_inspection_preserve_source_quality` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_missing_zoning_layer_fails_clearly` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_ambiguous_zoning_layer_fails_clearly` via `_config`.
- direct call: `tests/unit/test_gpu_fr.py::test_cached_document_lineage_change_forces_refresh` via `_config`.

**Complete source-ordered implementation**

```python
def _config() -> GpuSourceConfig:
    return load_gpu_source_config(Path("configs/sources/gpu_fr.yaml"))
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_listing_item`

**Exact signature**

```python
def _listing_item(**overrides: object) -> dict[str, object]:
```

**Purpose**

Private `test` helper for listing item; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
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
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `result`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_gpu_fr.py::_details` via `_listing_item`.
- direct call: `tests/unit/test_gpu_fr.py::_document` via `_listing_item`.
- direct call: `tests/unit/test_gpu_fr.py::test_written_material_url_must_be_exact_official_https_api_url` via `_listing_item`.
- direct call: `tests/unit/test_gpu_fr.py::test_written_material_fallback_rejects_unsafe_archive_url_provenance` via `_listing_item`.
- direct call: `tests/unit/test_gpu_fr.py::test_no_current_document_is_rejected` via `_listing_item`.
- direct call: `tests/unit/test_gpu_fr.py::test_ambiguous_current_documents_are_rejected` via `_listing_item`.
- direct call: `tests/unit/test_gpu_fr.py::test_missing_document_identity_is_rejected` via `_listing_item`.
- direct call: `tests/unit/test_gpu_fr.py::test_document_details_must_match_selected_listing` via `_listing_item`.
- direct call: `tests/unit/test_gpu_fr.py::test_document_details_commune_must_match_selected_listing` via `_listing_item`.
- direct call: `tests/unit/test_gpu_fr.py::test_discovery_rejects_unsafe_archive_name` via `_listing_item`.

**Complete source-ordered implementation**

```python
def _listing_item(**overrides: object) -> dict[str, object]:
    result: dict[str, object] = {
        "id": "doc-1",
        "status": "document.production",
        "legalStatus": "APPROVED",
        "effectiveStatus": "EN_VIGUEUR",
        "originalName": "31395_PLU_20240215",
        "type": "PLU",
        "name": "DU_31395",
        "grid": {"name": "31395", "title": "MURET"},
    }
    result.update(overrides)
    return result
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_details`

**Exact signature**

```python
def _details(**overrides: object) -> dict[str, object]:
```

**Purpose**

Private `test` helper for details; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
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
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `result`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_gpu_fr.py::_document` via `_details`.
- direct call: `tests/unit/test_gpu_fr.py::test_written_material_url_must_be_exact_official_https_api_url` via `_details`.
- direct call: `tests/unit/test_gpu_fr.py::test_written_material_fallback_rejects_unsafe_archive_url_provenance` via `_details`.
- direct call: `tests/unit/test_gpu_fr.py::test_document_details_must_match_selected_listing` via `_details`.
- direct call: `tests/unit/test_gpu_fr.py::test_document_details_commune_must_match_selected_listing` via `_details`.
- direct call: `tests/unit/test_gpu_fr.py::test_discovery_rejects_unsafe_archive_name` via `_details`.

**Complete source-ordered implementation**

```python
def _details(**overrides: object) -> dict[str, object]:
    result = _listing_item(
        title="Plan Local d'Urbanisme de Muret",
        producer="Mairie de Muret",
        projectionCode="EPSG:2154",
        publicationDate="26/03/2024 08:52:34",
        updateDate="26/03/2024 08:52:34",
        metadata="fr-000031395-plu20240215",
        archiveUrl="https://www.geoportail-urbanisme.gouv.fr/api/document/doc-1/download/31395_PLU_20240215.zip",
        writingMaterials={
            "reglement.pdf": "https://www.geoportail-urbanisme.gouv.fr/api/document/doc-1/files/reglement.pdf"
        },
    )
    result.update(overrides)
    return result
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_files`

**Exact signature**

```python
def _files() -> list[dict[str, object]]:
```

**Purpose**

Private `test` helper for files; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `list[dict[str, object]]`.
- Every observed return expression is reproduced without truncation:
```python
[{'name': 'reglement.pdf', 'title': 'Règlement écrit', 'path': 'Règlements'}]
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

- direct call: `tests/unit/test_gpu_fr.py::_document` via `_files`.
- direct call: `tests/unit/test_gpu_fr.py::test_written_material_url_must_be_exact_official_https_api_url` via `_files`.
- direct call: `tests/unit/test_gpu_fr.py::test_written_material_fallback_rejects_unsafe_archive_url_provenance` via `_files`.
- direct call: `tests/unit/test_gpu_fr.py::test_document_details_must_match_selected_listing` via `_files`.
- direct call: `tests/unit/test_gpu_fr.py::test_document_details_commune_must_match_selected_listing` via `_files`.
- direct call: `tests/unit/test_gpu_fr.py::test_discovery_rejects_unsafe_archive_name` via `_files`.

**Complete source-ordered implementation**

```python
def _files() -> list[dict[str, object]]:
    return [{"name": "reglement.pdf", "title": "Règlement écrit", "path": "Règlements"}]
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_patch_json_responses`

**Exact signature**

```python
def _patch_json_responses(monkeypatch: pytest.MonkeyPatch, values: list[object]) -> None:
```

**Purpose**

Private `test` helper for patch json responses; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- Every observed return expression is reproduced without truncation:
```python
_Response(json.dumps(next(responses)).encode())
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

- direct call: `tests/unit/test_gpu_fr.py::_document` via `_patch_json_responses`.
- direct call: `tests/unit/test_gpu_fr.py::test_written_material_url_must_be_exact_official_https_api_url` via `_patch_json_responses`.
- direct call: `tests/unit/test_gpu_fr.py::test_written_material_fallback_rejects_unsafe_archive_url_provenance` via `_patch_json_responses`.
- direct call: `tests/unit/test_gpu_fr.py::test_no_current_document_is_rejected` via `_patch_json_responses`.
- direct call: `tests/unit/test_gpu_fr.py::test_ambiguous_current_documents_are_rejected` via `_patch_json_responses`.
- direct call: `tests/unit/test_gpu_fr.py::test_missing_document_identity_is_rejected` via `_patch_json_responses`.
- direct call: `tests/unit/test_gpu_fr.py::test_document_details_must_match_selected_listing` via `_patch_json_responses`.
- direct call: `tests/unit/test_gpu_fr.py::test_document_details_commune_must_match_selected_listing` via `_patch_json_responses`.
- direct call: `tests/unit/test_gpu_fr.py::test_discovery_rejects_unsafe_archive_name` via `_patch_json_responses`.

**Complete source-ordered implementation**

```python
def _patch_json_responses(monkeypatch: pytest.MonkeyPatch, values: list[object]) -> None:
    responses = iter(values)

    def opener(*args: object, **kwargs: object) -> _Response:
        return _Response(json.dumps(next(responses)).encode())

    monkeypatch.setattr(gpu, "open_safe_https", opener)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_patch_json_responses.opener`

**Exact signature**

```python
def opener(*args: object, **kwargs: object) -> _Response:
```

**Purpose**

Private `test` helper for opener; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `_Response`.
- Every observed return expression is reproduced without truncation:
```python
_Response(json.dumps(next(responses)).encode())
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

- function object argument: `tests/unit/test_gpu_fr.py::_patch_json_responses` via `monkeypatch.setattr(gpu, 'open_safe_https', opener)`.

**Complete source-ordered implementation**

```python
def opener(*args: object, **kwargs: object) -> _Response:
        return _Response(json.dumps(next(responses)).encode())
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_document`

**Exact signature**

```python
def _document(monkeypatch: pytest.MonkeyPatch):
```

**Purpose**

Private `test` helper for document; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `unannotated`.
- Every observed return expression is reproduced without truncation:
```python
discover_current_gpu_document(_config())
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

- direct call: `tests/unit/test_gpu_fr.py::_download` via `_document`.
- direct call: `tests/unit/test_gpu_fr.py::test_document_discovery_success` via `_document`.
- direct call: `tests/unit/test_gpu_fr.py::test_download_rejects_document_inconsistent_with_config` via `_document`.
- direct call: `tests/unit/test_gpu_fr.py::test_download_rejects_forged_written_file_provenance_before_network` via `_document`.
- direct call: `tests/unit/test_gpu_fr.py::test_download_rejects_forged_unsafe_archive_name_before_io` via `_document`.
- direct call: `tests/unit/test_gpu_fr.py::test_archive_name_with_one_zip_suffix_is_not_duplicated` via `_document`.
- direct call: `tests/unit/test_gpu_fr.py::test_preexisting_temporary_archive_symlink_cannot_modify_target` via `_document`.
- direct call: `tests/unit/test_gpu_fr.py::test_corrupt_download_is_rejected` via `_document`.

**Complete source-ordered implementation**

```python
def _document(monkeypatch: pytest.MonkeyPatch):
    _patch_json_responses(monkeypatch, [[_listing_item()], _details(), _files()])
    return discover_current_gpu_document(_config())
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_zip_bytes`

**Exact signature**

```python
def _zip_bytes(files: dict[str, bytes] | None = None) -> bytes:
```

**Purpose**

Private `test` helper for zip bytes; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bytes`.
- Every observed return expression is reproduced without truncation:
```python
stream.getvalue()
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

- direct call: `tests/unit/test_gpu_fr.py::_download` via `_zip_bytes`.
- direct call: `tests/unit/test_gpu_fr.py::test_archive_name_with_one_zip_suffix_is_not_duplicated` via `_zip_bytes`.
- direct call: `tests/unit/test_gpu_fr.py::test_expired_cache_is_refreshed` via `_zip_bytes`.
- direct call: `tests/unit/test_gpu_fr.py::test_metadata_publication_failure_rolls_back_both_cache_files` via `_zip_bytes`.
- direct call: `tests/unit/test_gpu_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_zip_bytes`.
- direct call: `tests/unit/test_gpu_fr.py::test_preexisting_temporary_archive_symlink_cannot_modify_target.record_network` via `_zip_bytes`.
- direct call: `tests/unit/test_gpu_fr.py::test_tampered_sidecar_invalidates_cache` via `_zip_bytes`.
- direct call: `tests/unit/test_gpu_fr.py::test_archive_path_traversal_is_rejected` via `_zip_bytes`.
- direct call: `tests/unit/test_gpu_fr.py::test_zip_cannot_claim_extraction_manifest_path` via `_zip_bytes`.
- direct call: `tests/unit/test_gpu_fr.py::test_extraction_inventory_and_cache` via `_zip_bytes`.
- direct call: `tests/unit/test_gpu_fr.py::test_stale_download_object_rejects_replaced_valid_archive` via `_zip_bytes`.
- direct call: `tests/unit/test_gpu_fr.py::test_tampered_extraction_is_rebuilt_from_verified_archive` via `_zip_bytes`.
- direct call: `tests/unit/test_gpu_fr.py::test_cached_document_lineage_change_forces_refresh` via `_zip_bytes`.

**Complete source-ordered implementation**

```python
def _zip_bytes(files: dict[str, bytes] | None = None) -> bytes:
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, content in (files or {"document/readme.txt": b"GPU"}).items():
            archive.writestr(name, content)
    return stream.getvalue()
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_zip_member_bytes`

**Exact signature**

```python
def _zip_member_bytes(members: list[tuple[str, bytes]]) -> bytes:
```

**Purpose**

Private `test` helper for zip member bytes; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bytes`.
- Every observed return expression is reproduced without truncation:
```python
stream.getvalue()
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

- direct call: `tests/unit/test_gpu_fr.py::test_duplicate_zip_extraction_targets_are_rejected` via `_zip_member_bytes`.
- direct call: `tests/unit/test_gpu_fr.py::test_zip_file_directory_target_collision_is_rejected` via `_zip_member_bytes`.

**Complete source-ordered implementation**

```python
def _zip_member_bytes(members: list[tuple[str, bytes]]) -> bytes:
    stream = io.BytesIO()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for name, content in members:
                archive.writestr(name, content)
    return stream.getvalue()
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_download`

**Exact signature**

```python
def _download(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    archive_bytes: bytes | None = None,
) -> GpuArchiveDownload:
```

**Purpose**

Acquires, verifies, and records download; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `GpuArchiveDownload`.
- Every observed return expression is reproduced without truncation:
```python
download_gpu_document(document, _config(), tmp_path)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: `download_gpu_document`.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_gpu_fr.py::test_successful_download_persists_sha_and_sidecar` via `_download`.
- direct call: `tests/unit/test_gpu_fr.py::test_fresh_cache_is_reused` via `_download`.
- direct call: `tests/unit/test_gpu_fr.py::test_stale_recovery_backup_rejects_cache_before_network` via `_download`.
- direct call: `tests/unit/test_gpu_fr.py::test_expired_cache_is_refreshed` via `_download`.
- direct call: `tests/unit/test_gpu_fr.py::test_failed_refresh_preserves_previous_cache` via `_download`.
- direct call: `tests/unit/test_gpu_fr.py::test_metadata_publication_failure_rolls_back_both_cache_files` via `_download`.
- direct call: `tests/unit/test_gpu_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_download`.
- direct call: `tests/unit/test_gpu_fr.py::test_tampered_sidecar_invalidates_cache` via `_download`.
- direct call: `tests/unit/test_gpu_fr.py::test_extraction_inventory_and_cache` via `_download`.
- direct call: `tests/unit/test_gpu_fr.py::test_stale_download_object_rejects_replaced_valid_archive` via `_download`.
- direct call: `tests/unit/test_gpu_fr.py::test_extraction_rejects_archive_object_inconsistent_with_path` via `_download`.
- direct call: `tests/unit/test_gpu_fr.py::test_tampered_extraction_is_rebuilt_from_verified_archive` via `_download`.
- direct call: `tests/unit/test_gpu_fr.py::test_cached_document_lineage_change_forces_refresh` via `_download`.

**Complete source-ordered implementation**

```python
def _download(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    archive_bytes: bytes | None = None,
) -> GpuArchiveDownload:
    document = _document(monkeypatch)
    monkeypatch.setattr(gpu, "open_safe_https", lambda *args, **kwargs: _Response(archive_bytes or _zip_bytes()))
    return download_gpu_document(document, _config(), tmp_path)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_planning_archive`

**Exact signature**

```python
def _planning_archive(tmp_path: Path) -> Path:
```

**Purpose**

Private `test` helper for planning archive; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Path`.
- Every observed return expression is reproduced without truncation:
```python
archive_path
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: `package.rglob`, `path.is_file`.
- Filesystem write: `(package / '31395_reglement.pdf').write_bytes`, `(package / 'metadata.xml').write_text`, `package.mkdir`, `prescription.to_file`, `zoning.to_file`.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_gpu_fr.py::test_spatial_inventory_and_inspection_preserve_source_quality` via `_planning_archive`.
- direct call: `tests/unit/test_gpu_fr.py::test_missing_zoning_layer_fails_clearly` via `_planning_archive`.
- direct call: `tests/unit/test_gpu_fr.py::test_ambiguous_zoning_layer_fails_clearly` via `_planning_archive`.

**Complete source-ordered implementation**

```python
def _planning_archive(tmp_path: Path) -> Path:
    package = tmp_path / "package"
    package.mkdir()
    gpkg = package / "planning.gpkg"
    valid = Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])
    invalid = Polygon([(0, 0), (10, 10), (10, 0), (0, 10), (0, 0)])
    zoning = gpd.GeoDataFrame(
        {"LIBELLE": ["U", "N", None], "TYPEZONE": ["U", "N", "AU"]},
        geometry=[valid, invalid, None],
        crs="EPSG:2154",
    )
    prescription = gpd.GeoDataFrame(
        {"TYPEPSC": [5]}, geometry=[valid], crs="EPSG:2154"
    )
    zoning.to_file(gpkg, layer="zone_urba", driver="GPKG", engine="pyogrio")
    prescription.to_file(
        gpkg, layer="prescription_surf", driver="GPKG", engine="pyogrio", mode="a"
    )
    (package / "31395_reglement.pdf").write_bytes(b"%PDF synthetic")
    (package / "metadata.xml").write_text(
        "<metadata><standard>CNIG PLU v2017</standard></metadata>", encoding="utf-8"
    )
    archive_path = tmp_path / "planning.zip"
    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in package.rglob("*"):
            if path.is_file():
                archive.write(path, path.relative_to(package).as_posix())
    return archive_path
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_config_and_urls`

**Purpose**

Exercises `valid config and urls`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
config = _config()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert build_gpu_partition(config) == "DU_31395"
assert "partition=DU_31395" in build_gpu_document_list_url(config)
assert build_gpu_partition_download_url(config).endswith(
        "/document/download-by-partition/DU_31395"
    )
```

**Regression protected**

Locks `valid config and urls` through the exact asserted conditions: `build_gpu_partition(config) == 'DU_31395'`; `'partition=DU_31395' in build_gpu_document_list_url(config)`; `build_gpu_partition_download_url(config).endswith('/document/download-by-partition/DU_31395')`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_valid_config_and_urls() -> None:
    config = _config()
    assert build_gpu_partition(config) == "DU_31395"
    assert "partition=DU_31395" in build_gpu_document_list_url(config)
    assert build_gpu_partition_download_url(config).endswith(
        "/document/download-by-partition/DU_31395"
    )
```

### `test_invalid_config_values_are_rejected`

**Purpose**

Exercises `invalid config values are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `path`, `value`.

**Setup**

```python
payload = _config().model_dump(mode="json")
payload[path[0]][path[1]] = value
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError):
        GpuSourceConfig.model_validate(payload)
```

**Regression protected**

Locks `invalid config values are rejected`: the reproduced adversarial input must raise `ValidationError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_invalid_config_values_are_rejected(path: tuple[str, str], value: object) -> None:
    payload = _config().model_dump(mode="json")
    payload[path[0]][path[1]] = value
    with pytest.raises(ValidationError):
        GpuSourceConfig.model_validate(payload)
```

### `test_mutated_loaded_api_origin_is_rejected_before_discovery_network`

**Purpose**

Exercises `mutated loaded api origin is rejected before discovery network`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
config = _config()
config.api.base_url = HttpUrl("https://unrelated.example/api")
network_calls = 0
def fail_network(*args: object, **kwargs: object) -> object:
        nonlocal network_calls
        network_calls += 1
        raise AssertionError("network used after GPU origin mutation")
monkeypatch.setattr(gpu, "open_safe_https", fail_network)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GpuDiscoveryError, match="config|official|origin"):
        discover_current_gpu_document(config)
assert network_calls == 0
```

**Regression protected**

Locks `mutated loaded api origin is rejected before discovery network`: the reproduced adversarial input must raise `GpuDiscoveryError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_mutated_loaded_api_origin_is_rejected_before_discovery_network(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config = _config()
    config.api.base_url = HttpUrl("https://unrelated.example/api")
    network_calls = 0

    def fail_network(*args: object, **kwargs: object) -> object:
        nonlocal network_calls
        network_calls += 1
        raise AssertionError("network used after GPU origin mutation")

    monkeypatch.setattr(gpu, "open_safe_https", fail_network)

    with pytest.raises(GpuDiscoveryError, match="config|official|origin"):
        discover_current_gpu_document(config)

    assert network_calls == 0
```

### `test_mutated_loaded_api_origin_is_rejected_before_discovery_network.fail_network`

**Exact signature**

```python
def fail_network(*args: object, **kwargs: object) -> object:
```

**Purpose**

Private `test` helper for fail network; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `object`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `AssertionError('network used after GPU origin mutation')`.

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

- function object argument: `tests/unit/test_gpu_fr.py::test_mutated_loaded_api_origin_is_rejected_before_discovery_network` via `monkeypatch.setattr(gpu, 'open_safe_https', fail_network)`.

**Complete source-ordered implementation**

```python
def fail_network(*args: object, **kwargs: object) -> object:
        nonlocal network_calls
        network_calls += 1
        raise AssertionError("network used after GPU origin mutation")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unknown_config_field_is_rejected`

**Purpose**

Exercises `unknown config field is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
payload = _config().model_dump(mode="json")
payload["unexpected"] = True
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError):
        GpuSourceConfig.model_validate(payload)
```

**Regression protected**

Locks `unknown config field is rejected`: the reproduced adversarial input must raise `ValidationError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_unknown_config_field_is_rejected() -> None:
    payload = _config().model_dump(mode="json")
    payload["unexpected"] = True
    with pytest.raises(ValidationError):
        GpuSourceConfig.model_validate(payload)
```

### `test_document_discovery_success`

**Purpose**

Exercises `document discovery success`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document = _document(monkeypatch)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert document.document_id == "doc-1"
assert document.document_type == "PLU"
assert document.effective_status == "EN_VIGUEUR"
assert document.archive_name == "31395_PLU_20240215"
assert document.version is None
assert document.written_files[0].title == "Règlement écrit"
assert document.written_files[0].source_url == (
        "https://www.geoportail-urbanisme.gouv.fr/api/document/"
        "doc-1/files/reglement.pdf"
    )
```

**Regression protected**

Locks `document discovery success` through the exact asserted conditions: `document.document_id == 'doc-1'`; `document.document_type == 'PLU'`; `document.effective_status == 'EN_VIGUEUR'`; `document.archive_name == '31395_PLU_20240215'`; plus 3 additional reproduced assertion(s).

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_document_discovery_success(monkeypatch: pytest.MonkeyPatch) -> None:
    document = _document(monkeypatch)
    assert document.document_id == "doc-1"
    assert document.document_type == "PLU"
    assert document.effective_status == "EN_VIGUEUR"
    assert document.archive_name == "31395_PLU_20240215"
    assert document.version is None
    assert document.written_files[0].title == "Règlement écrit"
    assert document.written_files[0].source_url == (
        "https://www.geoportail-urbanisme.gouv.fr/api/document/"
        "doc-1/files/reglement.pdf"
    )
```

### `test_written_material_url_must_be_exact_official_https_api_url`

**Purpose**

Exercises `written material url must be exact official https api url`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `source_url`.

**Setup**

```python
_patch_json_responses(
        monkeypatch,
        [
            [_listing_item()],
            _details(writingMaterials={"reglement.pdf": source_url}),
            _files(),
        ],
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GpuDiscoveryError, match="written material URL"):
        discover_current_gpu_document(_config())
```

**Regression protected**

Locks `written material url must be exact official https api url`: the reproduced adversarial input must raise `GpuDiscoveryError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_written_material_url_must_be_exact_official_https_api_url(
    monkeypatch: pytest.MonkeyPatch,
    source_url: str,
) -> None:
    _patch_json_responses(
        monkeypatch,
        [
            [_listing_item()],
            _details(writingMaterials={"reglement.pdf": source_url}),
            _files(),
        ],
    )

    with pytest.raises(GpuDiscoveryError, match="written material URL"):
        discover_current_gpu_document(_config())
```

### `test_written_material_fallback_rejects_unsafe_archive_url_provenance`

**Purpose**

Exercises `written material fallback rejects unsafe archive url provenance`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `archive_url`.

**Setup**

```python
_patch_json_responses(
        monkeypatch,
        [
            [_listing_item()],
            _details(archiveUrl=archive_url, writingMaterials={}),
            _files(),
        ],
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GpuDiscoveryError, match="archive URL"):
        discover_current_gpu_document(_config())
```

**Regression protected**

Locks `written material fallback rejects unsafe archive url provenance`: the reproduced adversarial input must raise `GpuDiscoveryError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_written_material_fallback_rejects_unsafe_archive_url_provenance(
    monkeypatch: pytest.MonkeyPatch,
    archive_url: str,
) -> None:
    _patch_json_responses(
        monkeypatch,
        [
            [_listing_item()],
            _details(archiveUrl=archive_url, writingMaterials={}),
            _files(),
        ],
    )

    with pytest.raises(GpuDiscoveryError, match="archive URL"):
        discover_current_gpu_document(_config())
```

### `test_no_current_document_is_rejected`

**Purpose**

Exercises `no current document is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_patch_json_responses(monkeypatch, [[_listing_item(status="document.deleted")]])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GpuDiscoveryError, match="No current"):
        discover_current_gpu_document(_config())
```

**Regression protected**

Locks `no current document is rejected`: the reproduced adversarial input must raise `GpuDiscoveryError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_no_current_document_is_rejected(monkeypatch: pytest.MonkeyPatch) -> None:
    _patch_json_responses(monkeypatch, [[_listing_item(status="document.deleted")]])
    with pytest.raises(GpuDiscoveryError, match="No current"):
        discover_current_gpu_document(_config())
```

### `test_ambiguous_current_documents_are_rejected`

**Purpose**

Exercises `ambiguous current documents are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_patch_json_responses(monkeypatch, [[_listing_item(), _listing_item(id="doc-2")]])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GpuDiscoveryError, match="Ambiguous"):
        discover_current_gpu_document(_config())
```

**Regression protected**

Locks `ambiguous current documents are rejected`: the reproduced adversarial input must raise `GpuDiscoveryError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_ambiguous_current_documents_are_rejected(monkeypatch: pytest.MonkeyPatch) -> None:
    _patch_json_responses(monkeypatch, [[_listing_item(), _listing_item(id="doc-2")]])
    with pytest.raises(GpuDiscoveryError, match="Ambiguous"):
        discover_current_gpu_document(_config())
```

### `test_missing_document_identity_is_rejected`

**Purpose**

Exercises `missing document identity is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `field`.

**Setup**

```python
item = _listing_item()
item.pop(field)
_patch_json_responses(monkeypatch, [[item]])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GpuDiscoveryError, match="missing"):
        discover_current_gpu_document(_config())
```

**Regression protected**

Locks `missing document identity is rejected`: the reproduced adversarial input must raise `GpuDiscoveryError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_missing_document_identity_is_rejected(
    monkeypatch: pytest.MonkeyPatch, field: str
) -> None:
    item = _listing_item()
    item.pop(field)
    _patch_json_responses(monkeypatch, [[item]])
    with pytest.raises(GpuDiscoveryError, match="missing"):
        discover_current_gpu_document(_config())
```

### `test_document_details_must_match_selected_listing`

**Purpose**

Exercises `document details must match selected listing`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `different_value`, `field`.

**Setup**

```python
_patch_json_responses(
        monkeypatch,
        [[_listing_item()], _details(**{field: different_value}), _files()],
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GpuDiscoveryError, match="match|changed|current"):
        discover_current_gpu_document(_config())
```

**Regression protected**

Locks `document details must match selected listing`: the reproduced adversarial input must raise `GpuDiscoveryError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_document_details_must_match_selected_listing(
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    different_value: str,
) -> None:
    _patch_json_responses(
        monkeypatch,
        [[_listing_item()], _details(**{field: different_value}), _files()],
    )

    with pytest.raises(GpuDiscoveryError, match="match|changed|current"):
        discover_current_gpu_document(_config())
```

### `test_document_details_commune_must_match_selected_listing`

**Purpose**

Exercises `document details commune must match selected listing`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_patch_json_responses(
        monkeypatch,
        [
            [_listing_item()],
            _details(grid={"name": "99999", "title": "OTHER"}),
            _files(),
        ],
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GpuDiscoveryError, match="match"):
        discover_current_gpu_document(_config())
```

**Regression protected**

Locks `document details commune must match selected listing`: the reproduced adversarial input must raise `GpuDiscoveryError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_document_details_commune_must_match_selected_listing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _patch_json_responses(
        monkeypatch,
        [
            [_listing_item()],
            _details(grid={"name": "99999", "title": "OTHER"}),
            _files(),
        ],
    )

    with pytest.raises(GpuDiscoveryError, match="match"):
        discover_current_gpu_document(_config())
```

### `test_discovery_rejects_unsafe_archive_name`

**Purpose**

Exercises `discovery rejects unsafe archive name`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `archive_name`.

**Setup**

```python
_patch_json_responses(
        monkeypatch,
        [
            [_listing_item(originalName=archive_name)],
            _details(originalName=archive_name),
            _files(),
        ],
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GpuDiscoveryError, match="archive name|safe"):
        discover_current_gpu_document(_config())
```

**Regression protected**

Locks `discovery rejects unsafe archive name`: the reproduced adversarial input must raise `GpuDiscoveryError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_discovery_rejects_unsafe_archive_name(
    monkeypatch: pytest.MonkeyPatch,
    archive_name: str,
) -> None:
    _patch_json_responses(
        monkeypatch,
        [
            [_listing_item(originalName=archive_name)],
            _details(originalName=archive_name),
            _files(),
        ],
    )

    with pytest.raises(GpuDiscoveryError, match="archive name|safe"):
        discover_current_gpu_document(_config())
```

### `test_successful_download_persists_sha_and_sidecar`

**Purpose**

Exercises `successful download persists sha and sidecar`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _download(tmp_path, monkeypatch)
sidecar = json.loads((tmp_path / f"{result.filename}.metadata.json").read_text())
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert result.path.is_file()
assert result.file_size > 0
assert len(result.sha256) == 64
assert sidecar["sha256"] == result.sha256
assert sidecar["document"]["document_id"] == "doc-1"
assert not list(tmp_path.glob("*.part"))
```

**Regression protected**

Locks `successful download persists sha and sidecar` through the exact asserted conditions: `result.path.is_file()`; `result.file_size > 0`; `len(result.sha256) == 64`; `sidecar['sha256'] == result.sha256`; plus 2 additional reproduced assertion(s).

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_successful_download_persists_sha_and_sidecar(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    result = _download(tmp_path, monkeypatch)
    sidecar = json.loads((tmp_path / f"{result.filename}.metadata.json").read_text())
    assert result.path.is_file()
    assert result.file_size > 0
    assert len(result.sha256) == 64
    assert sidecar["sha256"] == result.sha256
    assert sidecar["document"]["document_id"] == "doc-1"
    assert not list(tmp_path.glob("*.part"))
```

### `test_download_rejects_document_inconsistent_with_config`

**Purpose**

Exercises `download rejects document inconsistent with config`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `different_value`, `field`.

**Setup**

```python
document = replace(_document(monkeypatch), **{field: different_value})
monkeypatch.setattr(
        gpu,
        "open_safe_https",
        lambda *args, **kwargs: pytest.fail("invalid document reached network"),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GpuDownloadError, match="document|identity|config"):
        download_gpu_document(document, _config(), tmp_path)
assert not any(tmp_path.iterdir())
```

**Regression protected**

Locks `download rejects document inconsistent with config`: the reproduced adversarial input must raise `GpuDownloadError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_download_rejects_document_inconsistent_with_config(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    different_value: str,
) -> None:
    document = replace(_document(monkeypatch), **{field: different_value})
    monkeypatch.setattr(
        gpu,
        "open_safe_https",
        lambda *args, **kwargs: pytest.fail("invalid document reached network"),
    )

    with pytest.raises(GpuDownloadError, match="document|identity|config"):
        download_gpu_document(document, _config(), tmp_path)

    assert not any(tmp_path.iterdir())
```

### `test_download_rejects_forged_written_file_provenance_before_network`

**Purpose**

Exercises `download rejects forged written file provenance before network`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `mutation`.

**Setup**

```python
original = _document(monkeypatch)
if mutation == "forged-source-url":
        written_files = (
            replace(
                original.written_files[0],
                source_url="http://unrelated.example/reglement.pdf",
            ),
        )
    else:
        written_files = (object(),)
document = replace(original, written_files=written_files)
network_calls = 0
def fail_network(*args: object, **kwargs: object) -> object:
        nonlocal network_calls
        network_calls += 1
        raise AssertionError("forged written-file provenance reached network")
monkeypatch.setattr(gpu, "open_safe_https", fail_network)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GpuDownloadError, match="written|document|source|URL"):
        download_gpu_document(document, _config(), tmp_path)
assert network_calls == 0
```

**Regression protected**

Locks `download rejects forged written file provenance before network`: the reproduced adversarial input must raise `GpuDownloadError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_download_rejects_forged_written_file_provenance_before_network(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation: str,
) -> None:
    original = _document(monkeypatch)
    if mutation == "forged-source-url":
        written_files = (
            replace(
                original.written_files[0],
                source_url="http://unrelated.example/reglement.pdf",
            ),
        )
    else:
        written_files = (object(),)
    document = replace(original, written_files=written_files)  # type: ignore[arg-type]
    network_calls = 0

    def fail_network(*args: object, **kwargs: object) -> object:
        nonlocal network_calls
        network_calls += 1
        raise AssertionError("forged written-file provenance reached network")

    monkeypatch.setattr(gpu, "open_safe_https", fail_network)

    with pytest.raises(GpuDownloadError, match="written|document|source|URL"):
        download_gpu_document(document, _config(), tmp_path)

    assert network_calls == 0
```

### `test_download_rejects_forged_written_file_provenance_before_network.fail_network`

**Exact signature**

```python
def fail_network(*args: object, **kwargs: object) -> object:
```

**Purpose**

Private `test` helper for fail network; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `object`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `AssertionError('forged written-file provenance reached network')`.

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

- function object argument: `tests/unit/test_gpu_fr.py::test_download_rejects_forged_written_file_provenance_before_network` via `monkeypatch.setattr(gpu, 'open_safe_https', fail_network)`.

**Complete source-ordered implementation**

```python
def fail_network(*args: object, **kwargs: object) -> object:
        nonlocal network_calls
        network_calls += 1
        raise AssertionError("forged written-file provenance reached network")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_download_rejects_forged_unsafe_archive_name_before_io`

**Purpose**

Exercises `download rejects forged unsafe archive name before io`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `archive_name`.

**Setup**

```python
document = replace(_document(monkeypatch), archive_name=archive_name)
monkeypatch.setattr(
        gpu,
        "open_safe_https",
        lambda *args, **kwargs: pytest.fail("unsafe archive name reached network"),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GpuDownloadError, match="archive name|archive filename|safe"):
        download_gpu_document(document, _config(), tmp_path / "cache")
assert not (tmp_path / "escape.zip").exists()
```

**Regression protected**

Locks `download rejects forged unsafe archive name before io`: the reproduced adversarial input must raise `GpuDownloadError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_download_rejects_forged_unsafe_archive_name_before_io(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    archive_name: str,
) -> None:
    document = replace(_document(monkeypatch), archive_name=archive_name)
    monkeypatch.setattr(
        gpu,
        "open_safe_https",
        lambda *args, **kwargs: pytest.fail("unsafe archive name reached network"),
    )

    with pytest.raises(GpuDownloadError, match="archive name|archive filename|safe"):
        download_gpu_document(document, _config(), tmp_path / "cache")

    assert not (tmp_path / "escape.zip").exists()
```

### `test_archive_name_with_one_zip_suffix_is_not_duplicated`

**Purpose**

Exercises `archive name with one zip suffix is not duplicated`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document = replace(_document(monkeypatch), archive_name="safe-name.zip")
monkeypatch.setattr(
        gpu,
        "open_safe_https",
        lambda *args, **kwargs: _Response(_zip_bytes()),
    )
```

**Action**

```python
result = download_gpu_document(document, _config(), tmp_path)
```

**Expected result**

```python
assert result.filename == "safe-name.zip"
assert result.path == tmp_path / "safe-name.zip"
```

**Regression protected**

Locks `archive name with one zip suffix is not duplicated` through the exact asserted conditions: `result.filename == 'safe-name.zip'`; `result.path == tmp_path / 'safe-name.zip'`.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_archive_name_with_one_zip_suffix_is_not_duplicated(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    document = replace(_document(monkeypatch), archive_name="safe-name.zip")
    monkeypatch.setattr(
        gpu,
        "open_safe_https",
        lambda *args, **kwargs: _Response(_zip_bytes()),
    )

    result = download_gpu_document(document, _config(), tmp_path)

    assert result.filename == "safe-name.zip"
    assert result.path == tmp_path / "safe-name.zip"
```

### `test_fresh_cache_is_reused`

**Purpose**

Exercises `fresh cache is reused`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
first = _download(tmp_path, monkeypatch)
monkeypatch.setattr(gpu, "open_safe_https", lambda *args, **kwargs: pytest.fail("network used"))
```

**Action**

```python
second = download_gpu_document(first.document, _config(), tmp_path)
```

**Expected result**

```python
assert second.cache_hit
assert second.sha256 == first.sha256
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_fresh_cache_is_reused(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    first = _download(tmp_path, monkeypatch)
    monkeypatch.setattr(gpu, "open_safe_https", lambda *args, **kwargs: pytest.fail("network used"))
    second = download_gpu_document(first.document, _config(), tmp_path)
    assert second.cache_hit
    assert second.sha256 == first.sha256
```

### `test_stale_recovery_backup_rejects_cache_before_network`

**Purpose**

Exercises `stale recovery backup rejects cache before network`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
first = _download(tmp_path, monkeypatch)
recovery_path = first.path.with_suffix(f"{first.path.suffix}.bak")
recovery_bytes = b"manual GPU recovery material"
recovery_path.write_bytes(recovery_bytes)
def fail_network(*args: object, **kwargs: object) -> _Response:
        pytest.fail("stale recovery must fail before network")
monkeypatch.setattr(gpu, "open_safe_https", fail_network)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GpuDownloadError, match="backup|recovery|manual"):
        download_gpu_document(first.document, _config(), tmp_path)
assert recovery_path.read_bytes() == recovery_bytes
```

**Regression protected**

Locks `stale recovery backup rejects cache before network`: the reproduced adversarial input must raise `GpuDownloadError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_stale_recovery_backup_rejects_cache_before_network(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    first = _download(tmp_path, monkeypatch)
    recovery_path = first.path.with_suffix(f"{first.path.suffix}.bak")
    recovery_bytes = b"manual GPU recovery material"
    recovery_path.write_bytes(recovery_bytes)

    def fail_network(*args: object, **kwargs: object) -> _Response:
        pytest.fail("stale recovery must fail before network")

    monkeypatch.setattr(gpu, "open_safe_https", fail_network)
    with pytest.raises(GpuDownloadError, match="backup|recovery|manual"):
        download_gpu_document(first.document, _config(), tmp_path)

    assert recovery_path.read_bytes() == recovery_bytes
```

### `test_stale_recovery_backup_rejects_cache_before_network.fail_network`

**Exact signature**

```python
def fail_network(*args: object, **kwargs: object) -> _Response:
```

**Purpose**

Private `test` helper for fail network; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `_Response`.
- No explicit return; normal completion returns `None`.

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

- function object argument: `tests/unit/test_gpu_fr.py::test_stale_recovery_backup_rejects_cache_before_network` via `monkeypatch.setattr(gpu, 'open_safe_https', fail_network)`.

**Complete source-ordered implementation**

```python
def fail_network(*args: object, **kwargs: object) -> _Response:
        pytest.fail("stale recovery must fail before network")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_expired_cache_is_refreshed`

**Purpose**

Exercises `expired cache is refreshed`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
first = _download(tmp_path, monkeypatch)
sidecar_path = tmp_path / f"{first.filename}.metadata.json"
sidecar = json.loads(sidecar_path.read_text())
sidecar["download_timestamp"] = (datetime.now(UTC) - timedelta(days=8)).isoformat()
sidecar_path.write_text(json.dumps(sidecar), encoding="utf-8")
fresh_bytes = _zip_bytes({"fresh.txt": b"fresh"})
monkeypatch.setattr(gpu, "open_safe_https", lambda *args, **kwargs: _Response(fresh_bytes))
```

**Action**

```python
refreshed = download_gpu_document(first.document, _config(), tmp_path)
```

**Expected result**

```python
assert not refreshed.cache_hit
assert refreshed.sha256 != first.sha256
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_expired_cache_is_refreshed(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    first = _download(tmp_path, monkeypatch)
    sidecar_path = tmp_path / f"{first.filename}.metadata.json"
    sidecar = json.loads(sidecar_path.read_text())
    sidecar["download_timestamp"] = (datetime.now(UTC) - timedelta(days=8)).isoformat()
    sidecar_path.write_text(json.dumps(sidecar), encoding="utf-8")
    fresh_bytes = _zip_bytes({"fresh.txt": b"fresh"})
    monkeypatch.setattr(gpu, "open_safe_https", lambda *args, **kwargs: _Response(fresh_bytes))
    refreshed = download_gpu_document(first.document, _config(), tmp_path)
    assert not refreshed.cache_hit
    assert refreshed.sha256 != first.sha256
```

### `test_failed_refresh_preserves_previous_cache`

**Purpose**

Exercises `failed refresh preserves previous cache`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
first = _download(tmp_path, monkeypatch)
sidecar_path = tmp_path / f"{first.filename}.metadata.json"
sidecar = json.loads(sidecar_path.read_text())
sidecar["download_timestamp"] = (datetime.now(UTC) - timedelta(days=8)).isoformat()
sidecar_path.write_text(json.dumps(sidecar), encoding="utf-8")
old_archive = first.path.read_bytes()
old_sidecar = sidecar_path.read_bytes()
def fail(*args: object, **kwargs: object) -> _Response:
        raise URLError("offline")
monkeypatch.setattr(gpu, "open_safe_https", fail)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GpuDownloadError):
        download_gpu_document(first.document, _config(), tmp_path)
assert first.path.read_bytes() == old_archive
assert sidecar_path.read_bytes() == old_sidecar
assert not list(tmp_path.glob("*.part"))
```

**Regression protected**

Locks `failed refresh preserves previous cache`: the reproduced adversarial input must raise `GpuDownloadError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_failed_refresh_preserves_previous_cache(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    first = _download(tmp_path, monkeypatch)
    sidecar_path = tmp_path / f"{first.filename}.metadata.json"
    sidecar = json.loads(sidecar_path.read_text())
    sidecar["download_timestamp"] = (datetime.now(UTC) - timedelta(days=8)).isoformat()
    sidecar_path.write_text(json.dumps(sidecar), encoding="utf-8")
    old_archive = first.path.read_bytes()
    old_sidecar = sidecar_path.read_bytes()

    def fail(*args: object, **kwargs: object) -> _Response:
        raise URLError("offline")

    monkeypatch.setattr(gpu, "open_safe_https", fail)
    with pytest.raises(GpuDownloadError):
        download_gpu_document(first.document, _config(), tmp_path)
    assert first.path.read_bytes() == old_archive
    assert sidecar_path.read_bytes() == old_sidecar
    assert not list(tmp_path.glob("*.part"))
```

### `test_failed_refresh_preserves_previous_cache.fail`

**Exact signature**

```python
def fail(*args: object, **kwargs: object) -> _Response:
```

**Purpose**

Private `test` helper for fail; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `_Response`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `URLError('offline')`.

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

- function object argument: `tests/unit/test_gpu_fr.py::test_failed_refresh_preserves_previous_cache` via `monkeypatch.setattr(gpu, 'open_safe_https', fail)`.

**Complete source-ordered implementation**

```python
def fail(*args: object, **kwargs: object) -> _Response:
        raise URLError("offline")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_metadata_publication_failure_rolls_back_both_cache_files`

**Purpose**

Exercises `metadata publication failure rolls back both cache files`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
first = _download(tmp_path, monkeypatch)
sidecar_path = tmp_path / f"{first.filename}.metadata.json"
sidecar = json.loads(sidecar_path.read_text())
sidecar["download_timestamp"] = (datetime.now(UTC) - timedelta(days=8)).isoformat()
sidecar_path.write_text(json.dumps(sidecar), encoding="utf-8")
old_archive = first.path.read_bytes()
old_sidecar = sidecar_path.read_bytes()
monkeypatch.setattr(
        gpu, "open_safe_https", lambda *args, **kwargs: _Response(_zip_bytes({"fresh": b"x"}))
    )
original_replace = gpu._replace_file
failed = False
def fail_new_metadata_once(source: Path, target: Path) -> None:
        nonlocal failed
        if source.suffix == ".part" and target == sidecar_path and not failed:
            failed = True
            raise OSError("simulated metadata lock")
        original_replace(source, target)
monkeypatch.setattr(gpu, "_replace_file", fail_new_metadata_once)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GpuDownloadError):
        download_gpu_document(first.document, _config(), tmp_path)
assert first.path.read_bytes() == old_archive
assert sidecar_path.read_bytes() == old_sidecar
assert not list(tmp_path.glob("*.part"))
assert not list(tmp_path.glob("*.bak"))
```

**Regression protected**

Locks `metadata publication failure rolls back both cache files`: the reproduced adversarial input must raise `GpuDownloadError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_metadata_publication_failure_rolls_back_both_cache_files(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    first = _download(tmp_path, monkeypatch)
    sidecar_path = tmp_path / f"{first.filename}.metadata.json"
    sidecar = json.loads(sidecar_path.read_text())
    sidecar["download_timestamp"] = (datetime.now(UTC) - timedelta(days=8)).isoformat()
    sidecar_path.write_text(json.dumps(sidecar), encoding="utf-8")
    old_archive = first.path.read_bytes()
    old_sidecar = sidecar_path.read_bytes()
    monkeypatch.setattr(
        gpu, "open_safe_https", lambda *args, **kwargs: _Response(_zip_bytes({"fresh": b"x"}))
    )
    original_replace = gpu._replace_file
    failed = False

    def fail_new_metadata_once(source: Path, target: Path) -> None:
        nonlocal failed
        if source.suffix == ".part" and target == sidecar_path and not failed:
            failed = True
            raise OSError("simulated metadata lock")
        original_replace(source, target)

    monkeypatch.setattr(gpu, "_replace_file", fail_new_metadata_once)
    with pytest.raises(GpuDownloadError):
        download_gpu_document(first.document, _config(), tmp_path)
    assert first.path.read_bytes() == old_archive
    assert sidecar_path.read_bytes() == old_sidecar
    assert not list(tmp_path.glob("*.part"))
    assert not list(tmp_path.glob("*.bak"))
```

### `test_metadata_publication_failure_rolls_back_both_cache_files.fail_new_metadata_once`

**Exact signature**

```python
def fail_new_metadata_once(source: Path, target: Path) -> None:
```

**Purpose**

Private `test` helper for fail new metadata once; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `source.suffix == '.part' and target == sidecar_path and (not failed)`.
- Explicit raise expressions: `OSError('simulated metadata lock')`.

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

- function object argument: `tests/unit/test_gpu_fr.py::test_metadata_publication_failure_rolls_back_both_cache_files` via `monkeypatch.setattr(gpu, '_replace_file', fail_new_metadata_once)`.

**Complete source-ordered implementation**

```python
def fail_new_metadata_once(source: Path, target: Path) -> None:
        nonlocal failed
        if source.suffix == ".part" and target == sidecar_path and not failed:
            failed = True
            raise OSError("simulated metadata lock")
        original_replace(source, target)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_publication_and_rollback_failure_preserves_exact_recovery_backups`

**Purpose**

Exercises `publication and rollback failure preserves exact recovery backups`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
archive_path = tmp_path / "cached.zip"
metadata_path = tmp_path / "cached.zip.metadata.json"
temporary_archive = tmp_path / "cached.zip.part"
temporary_metadata = tmp_path / "cached.zip.metadata.json.part"
old_archive = b"exact old archive"
old_metadata = b"exact old metadata"
archive_path.write_bytes(old_archive)
metadata_path.write_bytes(old_metadata)
temporary_archive.write_bytes(b"replacement archive")
temporary_metadata.write_bytes(b"replacement metadata")
archive_backup = archive_path.with_suffix(f"{archive_path.suffix}.bak")
metadata_backup = metadata_path.with_suffix(f"{metadata_path.suffix}.bak")
original_replace = gpu._replace_file
def fail_publication_and_rollback(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        if source == archive_backup and target == archive_path:
            raise OSError("simulated archive rollback failure")
        original_replace(source, target)
monkeypatch.setattr(
        gpu,
        "_replace_file",
        fail_publication_and_rollback,
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GpuDownloadError, match="rollback"):
        gpu._publish_cache_pair(
            temporary_archive,
            temporary_metadata,
            archive_path,
            metadata_path,
        )
assert archive_backup.read_bytes() == old_archive
assert metadata_backup.read_bytes() == old_metadata
```

**Regression protected**

Prevents cache publication/rollback failures from destroying the last recoverable bytes; the exact old archive/metadata or extraction tree asserted below must survive in recovery material.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_publication_and_rollback_failure_preserves_exact_recovery_backups(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    archive_path = tmp_path / "cached.zip"
    metadata_path = tmp_path / "cached.zip.metadata.json"
    temporary_archive = tmp_path / "cached.zip.part"
    temporary_metadata = tmp_path / "cached.zip.metadata.json.part"
    old_archive = b"exact old archive"
    old_metadata = b"exact old metadata"
    archive_path.write_bytes(old_archive)
    metadata_path.write_bytes(old_metadata)
    temporary_archive.write_bytes(b"replacement archive")
    temporary_metadata.write_bytes(b"replacement metadata")
    archive_backup = archive_path.with_suffix(f"{archive_path.suffix}.bak")
    metadata_backup = metadata_path.with_suffix(f"{metadata_path.suffix}.bak")
    original_replace = gpu._replace_file

    def fail_publication_and_rollback(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        if source == archive_backup and target == archive_path:
            raise OSError("simulated archive rollback failure")
        original_replace(source, target)

    monkeypatch.setattr(
        gpu,
        "_replace_file",
        fail_publication_and_rollback,
    )
    with pytest.raises(GpuDownloadError, match="rollback"):
        gpu._publish_cache_pair(
            temporary_archive,
            temporary_metadata,
            archive_path,
            metadata_path,
        )

    assert archive_backup.read_bytes() == old_archive
    assert metadata_backup.read_bytes() == old_metadata
```

### `test_publication_and_rollback_failure_preserves_exact_recovery_backups.fail_publication_and_rollback`

**Exact signature**

```python
def fail_publication_and_rollback(source: Path, target: Path) -> None:
```

**Purpose**

Private `test` helper for fail publication and rollback; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `source == temporary_metadata and target == metadata_path`.
- Guard with a raise path: `source == archive_backup and target == archive_path`.
- Explicit raise expressions: `OSError('simulated archive rollback failure')`, `OSError('simulated metadata publication failure')`.

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

- function object argument: `tests/unit/test_gpu_fr.py::test_publication_and_rollback_failure_preserves_exact_recovery_backups` via `monkeypatch.setattr(gpu, '_replace_file', fail_publication_and_rollback)`.

**Complete source-ordered implementation**

```python
def fail_publication_and_rollback(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        if source == archive_backup and target == archive_path:
            raise OSError("simulated archive rollback failure")
        original_replace(source, target)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_cleanup_failure_does_not_mask_double_failure_recovery_error`

**Purpose**

Exercises `cleanup failure does not mask double failure recovery error`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
first = _download(tmp_path, monkeypatch)
metadata_path = tmp_path / f"{first.filename}.metadata.json"
metadata = json.loads(metadata_path.read_text())
metadata["download_timestamp"] = (
        datetime.now(UTC) - timedelta(days=8)
    ).isoformat()
metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
old_archive = first.path.read_bytes()
old_metadata = metadata_path.read_bytes()
temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
archive_backup = first.path.with_suffix(f"{first.path.suffix}.bak")
metadata_backup = metadata_path.with_suffix(f"{metadata_path.suffix}.bak")
original_replace = gpu._replace_file
original_unlink = Path.unlink
rollback_failed = False
def fail_publication_and_rollback(source: Path, target: Path) -> None:
        nonlocal rollback_failed
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        if source == archive_backup and target == first.path:
            rollback_failed = True
            raise OSError("simulated archive rollback failure")
        original_replace(source, target)
def fail_temporary_cleanup(path: Path, *, missing_ok: bool = False) -> None:
        if rollback_failed and path == temporary_metadata:
            raise PermissionError("simulated temporary cleanup failure")
        original_unlink(path, missing_ok=missing_ok)
monkeypatch.setattr(
        gpu,
        "open_safe_https",
        lambda *args, **kwargs: _Response(_zip_bytes({"fresh": b"x"})),
    )
monkeypatch.setattr(gpu, "_replace_file", fail_publication_and_rollback)
monkeypatch.setattr(Path, "unlink", fail_temporary_cleanup)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GpuDownloadError, match="rollback"):
        download_gpu_document(first.document, _config(), tmp_path)
assert archive_backup.read_bytes() == old_archive
assert metadata_backup.read_bytes() == old_metadata
```

**Regression protected**

Prevents failed cache publication and failed rollback from deleting the last recoverable backup bytes.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_cleanup_failure_does_not_mask_double_failure_recovery_error(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    first = _download(tmp_path, monkeypatch)
    metadata_path = tmp_path / f"{first.filename}.metadata.json"
    metadata = json.loads(metadata_path.read_text())
    metadata["download_timestamp"] = (
        datetime.now(UTC) - timedelta(days=8)
    ).isoformat()
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
    old_archive = first.path.read_bytes()
    old_metadata = metadata_path.read_bytes()
    temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
    archive_backup = first.path.with_suffix(f"{first.path.suffix}.bak")
    metadata_backup = metadata_path.with_suffix(f"{metadata_path.suffix}.bak")
    original_replace = gpu._replace_file
    original_unlink = Path.unlink
    rollback_failed = False

    def fail_publication_and_rollback(source: Path, target: Path) -> None:
        nonlocal rollback_failed
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        if source == archive_backup and target == first.path:
            rollback_failed = True
            raise OSError("simulated archive rollback failure")
        original_replace(source, target)

    def fail_temporary_cleanup(path: Path, *, missing_ok: bool = False) -> None:
        if rollback_failed and path == temporary_metadata:
            raise PermissionError("simulated temporary cleanup failure")
        original_unlink(path, missing_ok=missing_ok)

    monkeypatch.setattr(
        gpu,
        "open_safe_https",
        lambda *args, **kwargs: _Response(_zip_bytes({"fresh": b"x"})),
    )
    monkeypatch.setattr(gpu, "_replace_file", fail_publication_and_rollback)
    monkeypatch.setattr(Path, "unlink", fail_temporary_cleanup)
    with pytest.raises(GpuDownloadError, match="rollback"):
        download_gpu_document(first.document, _config(), tmp_path)

    assert archive_backup.read_bytes() == old_archive
    assert metadata_backup.read_bytes() == old_metadata
```

### `test_cleanup_failure_does_not_mask_double_failure_recovery_error.fail_publication_and_rollback`

**Exact signature**

```python
def fail_publication_and_rollback(source: Path, target: Path) -> None:
```

**Purpose**

Private `test` helper for fail publication and rollback; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `source == temporary_metadata and target == metadata_path`.
- Guard with a raise path: `source == archive_backup and target == first.path`.
- Explicit raise expressions: `OSError('simulated archive rollback failure')`, `OSError('simulated metadata publication failure')`.

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

- function object argument: `tests/unit/test_gpu_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `monkeypatch.setattr(gpu, '_replace_file', fail_publication_and_rollback)`.

**Complete source-ordered implementation**

```python
def fail_publication_and_rollback(source: Path, target: Path) -> None:
        nonlocal rollback_failed
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        if source == archive_backup and target == first.path:
            rollback_failed = True
            raise OSError("simulated archive rollback failure")
        original_replace(source, target)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_cleanup_failure_does_not_mask_double_failure_recovery_error.fail_temporary_cleanup`

**Exact signature**

```python
def fail_temporary_cleanup(path: Path, *, missing_ok: bool = False) -> None:
```

**Purpose**

Private `test` helper for fail temporary cleanup; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `rollback_failed and path == temporary_metadata`.
- Explicit raise expressions: `PermissionError('simulated temporary cleanup failure')`.

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

- function object argument: `tests/unit/test_gpu_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `monkeypatch.setattr(Path, 'unlink', fail_temporary_cleanup)`.

**Complete source-ordered implementation**

```python
def fail_temporary_cleanup(path: Path, *, missing_ok: bool = False) -> None:
        if rollback_failed and path == temporary_metadata:
            raise PermissionError("simulated temporary cleanup failure")
        original_unlink(path, missing_ok=missing_ok)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_stale_cache_recovery_backup_fails_closed_without_destroying_it`

**Purpose**

Exercises `stale cache recovery backup fails closed without destroying it`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
archive_path = tmp_path / "cached.zip"
metadata_path = tmp_path / "cached.zip.metadata.json"
temporary_archive = tmp_path / "cached.zip.part"
temporary_metadata = tmp_path / "cached.zip.metadata.json.part"
archive_backup = tmp_path / "cached.zip.bak"
archive_path.write_bytes(b"old archive")
metadata_path.write_bytes(b"old metadata")
temporary_archive.write_bytes(b"new archive")
temporary_metadata.write_bytes(b"new metadata")
archive_backup.write_bytes(b"manual recovery archive")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GpuDownloadError, match="backup|recovery|manual"):
        gpu._publish_cache_pair(
            temporary_archive,
            temporary_metadata,
            archive_path,
            metadata_path,
        )
assert archive_path.read_bytes() == b"old archive"
assert metadata_path.read_bytes() == b"old metadata"
assert archive_backup.read_bytes() == b"manual recovery archive"
```

**Regression protected**

Locks `stale cache recovery backup fails closed without destroying it`: the reproduced adversarial input must raise `GpuDownloadError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_stale_cache_recovery_backup_fails_closed_without_destroying_it(
    tmp_path: Path,
) -> None:
    archive_path = tmp_path / "cached.zip"
    metadata_path = tmp_path / "cached.zip.metadata.json"
    temporary_archive = tmp_path / "cached.zip.part"
    temporary_metadata = tmp_path / "cached.zip.metadata.json.part"
    archive_backup = tmp_path / "cached.zip.bak"
    archive_path.write_bytes(b"old archive")
    metadata_path.write_bytes(b"old metadata")
    temporary_archive.write_bytes(b"new archive")
    temporary_metadata.write_bytes(b"new metadata")
    archive_backup.write_bytes(b"manual recovery archive")

    with pytest.raises(GpuDownloadError, match="backup|recovery|manual"):
        gpu._publish_cache_pair(
            temporary_archive,
            temporary_metadata,
            archive_path,
            metadata_path,
        )

    assert archive_path.read_bytes() == b"old archive"
    assert metadata_path.read_bytes() == b"old metadata"
    assert archive_backup.read_bytes() == b"manual recovery archive"
```

### `test_preexisting_temporary_archive_symlink_cannot_modify_target`

**Purpose**

Exercises `preexisting temporary archive symlink cannot modify target`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document = _document(monkeypatch)
filename = gpu._safe_gpu_archive_filename(document.archive_name)
temporary_archive = tmp_path / f"{filename}.part"
sentinel = tmp_path / "do-not-overwrite.txt"
sentinel_bytes = b"irreplaceable sentinel bytes"
sentinel.write_bytes(sentinel_bytes)
original_is_symlink = Path.is_symlink
original_open = Path.open
def simulated_is_symlink(path: Path) -> bool:
        return path == temporary_archive or original_is_symlink(path)
def simulated_symlink_open(
        path: Path, *args: object, **kwargs: object
    ) -> object:
        if path == temporary_archive:
            return original_open(sentinel, *args, **kwargs)
        return original_open(path, *args, **kwargs)
opener_calls = 0
def record_network(*args: object, **kwargs: object) -> _Response:
        nonlocal opener_calls
        opener_calls += 1
        return _Response(_zip_bytes())
monkeypatch.setattr(Path, "is_symlink", simulated_is_symlink)
monkeypatch.setattr(Path, "open", simulated_symlink_open)
monkeypatch.setattr(gpu, "open_safe_https", record_network)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GpuDownloadError):
        download_gpu_document(document, _config(), tmp_path)
assert opener_calls == 0
assert sentinel.read_bytes() == sentinel_bytes
```

**Regression protected**

Locks `preexisting temporary archive symlink cannot modify target`: the reproduced adversarial input must raise `GpuDownloadError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_preexisting_temporary_archive_symlink_cannot_modify_target(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    document = _document(monkeypatch)
    filename = gpu._safe_gpu_archive_filename(document.archive_name)
    temporary_archive = tmp_path / f"{filename}.part"
    sentinel = tmp_path / "do-not-overwrite.txt"
    sentinel_bytes = b"irreplaceable sentinel bytes"
    sentinel.write_bytes(sentinel_bytes)
    original_is_symlink = Path.is_symlink
    original_open = Path.open

    def simulated_is_symlink(path: Path) -> bool:
        return path == temporary_archive or original_is_symlink(path)

    def simulated_symlink_open(
        path: Path, *args: object, **kwargs: object
    ) -> object:
        if path == temporary_archive:
            return original_open(sentinel, *args, **kwargs)
        return original_open(path, *args, **kwargs)

    opener_calls = 0

    def record_network(*args: object, **kwargs: object) -> _Response:
        nonlocal opener_calls
        opener_calls += 1
        return _Response(_zip_bytes())

    monkeypatch.setattr(Path, "is_symlink", simulated_is_symlink)
    monkeypatch.setattr(Path, "open", simulated_symlink_open)
    monkeypatch.setattr(gpu, "open_safe_https", record_network)

    with pytest.raises(GpuDownloadError):
        download_gpu_document(document, _config(), tmp_path)

    assert opener_calls == 0
    assert sentinel.read_bytes() == sentinel_bytes
```

### `test_preexisting_temporary_archive_symlink_cannot_modify_target.simulated_is_symlink`

**Exact signature**

```python
def simulated_is_symlink(path: Path) -> bool:
```

**Purpose**

Private `test` helper for simulated is symlink; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
path == temporary_archive or original_is_symlink(path)
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

- function object argument: `tests/unit/test_gpu_fr.py::test_preexisting_temporary_archive_symlink_cannot_modify_target` via `monkeypatch.setattr(Path, 'is_symlink', simulated_is_symlink)`.

**Complete source-ordered implementation**

```python
def simulated_is_symlink(path: Path) -> bool:
        return path == temporary_archive or original_is_symlink(path)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_preexisting_temporary_archive_symlink_cannot_modify_target.simulated_symlink_open`

**Exact signature**

```python
def simulated_symlink_open(
        path: Path, *args: object, **kwargs: object
    ) -> object:
```

**Purpose**

Private `test` helper for simulated symlink open; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `object`.
- Every observed return expression is reproduced without truncation:
```python
original_open(path, *args, **kwargs)

original_open(sentinel, *args, **kwargs)
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

- function object argument: `tests/unit/test_gpu_fr.py::test_preexisting_temporary_archive_symlink_cannot_modify_target` via `monkeypatch.setattr(Path, 'open', simulated_symlink_open)`.

**Complete source-ordered implementation**

```python
def simulated_symlink_open(
        path: Path, *args: object, **kwargs: object
    ) -> object:
        if path == temporary_archive:
            return original_open(sentinel, *args, **kwargs)
        return original_open(path, *args, **kwargs)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_preexisting_temporary_archive_symlink_cannot_modify_target.record_network`

**Exact signature**

```python
def record_network(*args: object, **kwargs: object) -> _Response:
```

**Purpose**

Private `test` helper for record network; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `_Response`.
- Every observed return expression is reproduced without truncation:
```python
_Response(_zip_bytes())
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

- function object argument: `tests/unit/test_gpu_fr.py::test_preexisting_temporary_archive_symlink_cannot_modify_target` via `monkeypatch.setattr(gpu, 'open_safe_https', record_network)`.

**Complete source-ordered implementation**

```python
def record_network(*args: object, **kwargs: object) -> _Response:
        nonlocal opener_calls
        opener_calls += 1
        return _Response(_zip_bytes())
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_corrupt_download_is_rejected`

**Purpose**

Exercises `corrupt download is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document = _document(monkeypatch)
monkeypatch.setattr(gpu, "open_safe_https", lambda *args, **kwargs: _Response(b"not zip"))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GpuDownloadError):
        download_gpu_document(document, _config(), tmp_path)
assert not list(tmp_path.glob("*.part"))
```

**Regression protected**

Locks `corrupt download is rejected`: the reproduced adversarial input must raise `GpuDownloadError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_corrupt_download_is_rejected(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    document = _document(monkeypatch)
    monkeypatch.setattr(gpu, "open_safe_https", lambda *args, **kwargs: _Response(b"not zip"))
    with pytest.raises(GpuDownloadError):
        download_gpu_document(document, _config(), tmp_path)
    assert not list(tmp_path.glob("*.part"))
```

### `test_tampered_sidecar_invalidates_cache`

**Purpose**

Exercises `tampered sidecar invalidates cache`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
first = _download(tmp_path, monkeypatch)
sidecar_path = tmp_path / f"{first.filename}.metadata.json"
sidecar = json.loads(sidecar_path.read_text())
sidecar["sha256"] = "0" * 64
sidecar_path.write_text(json.dumps(sidecar), encoding="utf-8")
monkeypatch.setattr(gpu, "open_safe_https", lambda *args, **kwargs: _Response(_zip_bytes()))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert not download_gpu_document(first.document, _config(), tmp_path).cache_hit
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_tampered_sidecar_invalidates_cache(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    first = _download(tmp_path, monkeypatch)
    sidecar_path = tmp_path / f"{first.filename}.metadata.json"
    sidecar = json.loads(sidecar_path.read_text())
    sidecar["sha256"] = "0" * 64
    sidecar_path.write_text(json.dumps(sidecar), encoding="utf-8")
    monkeypatch.setattr(gpu, "open_safe_https", lambda *args, **kwargs: _Response(_zip_bytes()))
    assert not download_gpu_document(first.document, _config(), tmp_path).cache_hit
```

### `test_archive_path_traversal_is_rejected`

**Purpose**

Exercises `archive path traversal is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
path = tmp_path / "unsafe.zip"
path.write_bytes(_zip_bytes({"../escape.txt": b"bad"}))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GpuArchiveError, match="Unsafe"):
        validate_gpu_archive(path)
```

**Regression protected**

Locks `archive path traversal is rejected`: the reproduced adversarial input must raise `GpuArchiveError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_archive_path_traversal_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "unsafe.zip"
    path.write_bytes(_zip_bytes({"../escape.txt": b"bad"}))
    with pytest.raises(GpuArchiveError, match="Unsafe"):
        validate_gpu_archive(path)
```

### `test_archive_symlink_is_rejected`

**Purpose**

Exercises `archive symlink is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
path = tmp_path / "unsafe.zip"
with zipfile.ZipFile(path, "w") as archive:
        entry = zipfile.ZipInfo("link")
        entry.create_system = 3
        entry.external_attr = (0o120777 << 16) | 0xA000
        archive.writestr(entry, "target")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GpuArchiveError, match="Symbolic"):
        validate_gpu_archive(path)
```

**Regression protected**

Locks `archive symlink is rejected`: the reproduced adversarial input must raise `GpuArchiveError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_archive_symlink_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "unsafe.zip"
    with zipfile.ZipFile(path, "w") as archive:
        entry = zipfile.ZipInfo("link")
        entry.create_system = 3
        entry.external_attr = (0o120777 << 16) | 0xA000
        archive.writestr(entry, "target")
    with pytest.raises(GpuArchiveError, match="Symbolic"):
        validate_gpu_archive(path)
```

### `test_duplicate_zip_extraction_targets_are_rejected`

**Purpose**

Exercises `duplicate zip extraction targets are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `members`.

**Setup**

```python
path = tmp_path / "collision.zip"
path.write_bytes(_zip_member_bytes(members))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GpuArchiveError, match="(?i)duplicate|collid"):
        validate_gpu_archive(path)
```

**Regression protected**

Locks `duplicate zip extraction targets are rejected`: the reproduced adversarial input must raise `GpuArchiveError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_duplicate_zip_extraction_targets_are_rejected(
    tmp_path: Path,
    members: list[tuple[str, bytes]],
) -> None:
    path = tmp_path / "collision.zip"
    path.write_bytes(_zip_member_bytes(members))

    with pytest.raises(GpuArchiveError, match="(?i)duplicate|collid"):
        validate_gpu_archive(path)
```

### `test_zip_file_directory_target_collision_is_rejected`

**Purpose**

Exercises `zip file directory target collision is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
path = tmp_path / "collision.zip"
path.write_bytes(
        _zip_member_bytes(
            [("blocked", b"file"), ("blocked/child.txt", b"child")]
        )
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GpuArchiveError, match="collision|target"):
        validate_gpu_archive(path)
```

**Regression protected**

Locks `zip file directory target collision is rejected`: the reproduced adversarial input must raise `GpuArchiveError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_zip_file_directory_target_collision_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "collision.zip"
    path.write_bytes(
        _zip_member_bytes(
            [("blocked", b"file"), ("blocked/child.txt", b"child")]
        )
    )

    with pytest.raises(GpuArchiveError, match="collision|target"):
        validate_gpu_archive(path)
```

### `test_zip_cannot_claim_extraction_manifest_path`

**Purpose**

Exercises `zip cannot claim extraction manifest path`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
path = tmp_path / "collision.zip"
path.write_bytes(
        _zip_bytes({f"{gpu.EXTRACTION_MANIFEST_NAME}/child": b"forbidden"})
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GpuArchiveError, match="manifest"):
        validate_gpu_archive(path)
```

**Regression protected**

Locks `zip cannot claim extraction manifest path`: the reproduced adversarial input must raise `GpuArchiveError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_zip_cannot_claim_extraction_manifest_path(tmp_path: Path) -> None:
    path = tmp_path / "collision.zip"
    path.write_bytes(
        _zip_bytes({f"{gpu.EXTRACTION_MANIFEST_NAME}/child": b"forbidden"})
    )

    with pytest.raises(GpuArchiveError, match="manifest"):
        validate_gpu_archive(path)
```

### `test_extraction_inventory_and_cache`

**Purpose**

Exercises `extraction inventory and cache`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
first = _download(
        tmp_path / "cache",
        monkeypatch,
        _zip_bytes({"data/a.txt": b"x", "docs/reglement.pdf": b"pdf"}),
    )
manifest = json.loads(
        (
            extracted.extraction_root / gpu.EXTRACTION_MANIFEST_NAME
        ).read_text(encoding="utf-8")
    )
```

**Action**

```python
extracted = extract_gpu_document(first, tmp_path / "cache")
```

**Expected result**

```python
assert [item.relative_path for item in extracted.files] == [
        "data/a.txt",
        "docs/reglement.pdf",
    ]
assert {item.category for item in extracted.files} == {
        "METADATA",
        "WRITTEN_REGULATION",
    }
assert extract_gpu_document(first, tmp_path / "cache").cache_hit
assert manifest["schema_version"] == 2
assert manifest["archive_sha256"] == first.sha256
assert manifest["files"] == [
        {
            "relative_path": item.relative_path,
            "size_bytes": item.size_bytes,
            "sha256": item.sha256,
        }
        for item in extracted.files
    ]
assert not list((tmp_path / "cache" / "x").glob("*.part"))
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_extraction_inventory_and_cache(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    first = _download(
        tmp_path / "cache",
        monkeypatch,
        _zip_bytes({"data/a.txt": b"x", "docs/reglement.pdf": b"pdf"}),
    )
    extracted = extract_gpu_document(first, tmp_path / "cache")
    assert [item.relative_path for item in extracted.files] == [
        "data/a.txt",
        "docs/reglement.pdf",
    ]
    assert {item.category for item in extracted.files} == {
        "METADATA",
        "WRITTEN_REGULATION",
    }
    assert extract_gpu_document(first, tmp_path / "cache").cache_hit
    manifest = json.loads(
        (
            extracted.extraction_root / gpu.EXTRACTION_MANIFEST_NAME
        ).read_text(encoding="utf-8")
    )
    assert manifest["schema_version"] == 2
    assert manifest["archive_sha256"] == first.sha256
    assert manifest["files"] == [
        {
            "relative_path": item.relative_path,
            "size_bytes": item.size_bytes,
            "sha256": item.sha256,
        }
        for item in extracted.files
    ]
    assert not list((tmp_path / "cache" / "x").glob("*.part"))
```

### `test_stale_download_object_rejects_replaced_valid_archive`

**Purpose**

Exercises `stale download object rejects replaced valid archive`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
download = _download(
        tmp_path / "cache",
        monkeypatch,
        _zip_bytes({"data/value.txt": b"A"}),
    )
replacement = _zip_bytes({"data/value.txt": b"B"})
download.path.write_bytes(replacement)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert len(replacement) == download.file_size
with pytest.raises(GpuArchiveError, match="checksum|SHA|stale|metadata"):
        extract_gpu_document(download, tmp_path / "cache")
assert not (tmp_path / "cache" / "x" / download.sha256[:16]).exists()
```

**Regression protected**

Locks `stale download object rejects replaced valid archive`: the reproduced adversarial input must raise `GpuArchiveError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_stale_download_object_rejects_replaced_valid_archive(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    download = _download(
        tmp_path / "cache",
        monkeypatch,
        _zip_bytes({"data/value.txt": b"A"}),
    )
    replacement = _zip_bytes({"data/value.txt": b"B"})
    assert len(replacement) == download.file_size
    download.path.write_bytes(replacement)

    with pytest.raises(GpuArchiveError, match="checksum|SHA|stale|metadata"):
        extract_gpu_document(download, tmp_path / "cache")

    assert not (tmp_path / "cache" / "x" / download.sha256[:16]).exists()
```

### `test_extraction_rejects_archive_object_inconsistent_with_path`

**Purpose**

Exercises `extraction rejects archive object inconsistent with path`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `field`, `value`.

**Setup**

```python
download = _download(tmp_path / "cache", monkeypatch)
stale = replace(download, **{field: value})
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GpuArchiveError, match="archive|metadata|checksum|size"):
        extract_gpu_document(stale, tmp_path / "cache")
```

**Regression protected**

Locks `extraction rejects archive object inconsistent with path`: the reproduced adversarial input must raise `GpuArchiveError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_extraction_rejects_archive_object_inconsistent_with_path(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    value: object,
) -> None:
    download = _download(tmp_path / "cache", monkeypatch)
    stale = replace(download, **{field: value})

    with pytest.raises(GpuArchiveError, match="archive|metadata|checksum|size"):
        extract_gpu_document(stale, tmp_path / "cache")
```

### `test_tampered_extraction_is_rebuilt_from_verified_archive`

**Purpose**

Exercises `tampered extraction is rebuilt from verified archive`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `mutation`.

**Setup**

```python
download = _download(
        tmp_path / "cache",
        monkeypatch,
        _zip_bytes(
            {
                "data/value.txt": b"source",
                "docs/reglement.pdf": b"pdf",
            }
        ),
    )
original = first.extraction_root / "data" / "value.txt"
if mutation == "content":
        original.write_bytes(b"forged")
    elif mutation == "deleted":
        original.unlink()
    elif mutation == "added":
        (first.extraction_root / "unexpected.txt").write_bytes(b"unexpected")
    else:
        original.rename(original.with_name("renamed.txt"))
```

**Action**

```python
first = extract_gpu_document(download, tmp_path / "cache")
refreshed = extract_gpu_document(download, tmp_path / "cache")
```

**Expected result**

```python
assert not refreshed.cache_hit
assert (refreshed.extraction_root / "data" / "value.txt").read_bytes() == b"source"
assert not (refreshed.extraction_root / "data" / "renamed.txt").exists()
assert not (refreshed.extraction_root / "unexpected.txt").exists()
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_tampered_extraction_is_rebuilt_from_verified_archive(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation: str,
) -> None:
    download = _download(
        tmp_path / "cache",
        monkeypatch,
        _zip_bytes(
            {
                "data/value.txt": b"source",
                "docs/reglement.pdf": b"pdf",
            }
        ),
    )
    first = extract_gpu_document(download, tmp_path / "cache")
    original = first.extraction_root / "data" / "value.txt"
    if mutation == "content":
        original.write_bytes(b"forged")
    elif mutation == "deleted":
        original.unlink()
    elif mutation == "added":
        (first.extraction_root / "unexpected.txt").write_bytes(b"unexpected")
    else:
        original.rename(original.with_name("renamed.txt"))

    refreshed = extract_gpu_document(download, tmp_path / "cache")

    assert not refreshed.cache_hit
    assert (refreshed.extraction_root / "data" / "value.txt").read_bytes() == b"source"
    assert not (refreshed.extraction_root / "data" / "renamed.txt").exists()
    assert not (refreshed.extraction_root / "unexpected.txt").exists()
```

### `_extraction_from_archive`

**Exact signature**

```python
def _extraction_from_archive(path: Path, tmp_path: Path) -> GpuExtraction:
```

**Purpose**

Private `test` helper for extraction from archive; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `GpuExtraction`.
- Every observed return expression is reproduced without truncation:
```python
extract_gpu_document(download, tmp_path / 'cache')
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: `path.stat`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `gpu._sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_gpu_fr.py::test_spatial_inventory_and_inspection_preserve_source_quality` via `_extraction_from_archive`.
- direct call: `tests/unit/test_gpu_fr.py::test_missing_zoning_layer_fails_clearly` via `_extraction_from_archive`.
- direct call: `tests/unit/test_gpu_fr.py::test_ambiguous_zoning_layer_fails_clearly` via `_extraction_from_archive`.

**Complete source-ordered implementation**

```python
def _extraction_from_archive(path: Path, tmp_path: Path) -> GpuExtraction:
    document = gpu.GpuDocumentMetadata(
        provider="GPU",
        portal="GPU",
        commune_code="31395",
        partition="DU_31395",
        document_id="doc-1",
        document_family="DU",
        document_type="PLU",
        document_title=None,
        status="document.production",
        legal_status="APPROVED",
        effective_status="EN_VIGUEUR",
        version=None,
        archive_name=path.stem,
        publication_timestamp=None,
        update_timestamp=None,
        revision_date=None,
        producer=None,
        standard_model=None,
        projection="EPSG:2154",
        metadata_identifier=None,
        source_url="https://example.test/archive.zip",
        written_files=(),
    )
    download = GpuArchiveDownload(
        document=document,
        download_timestamp=datetime.now(UTC).isoformat(),
        filename=path.name,
        archive_format="zip",
        file_size=path.stat().st_size,
        sha256=gpu._sha256(path),
        path=path,
        cache_hit=False,
    )
    return extract_gpu_document(download, tmp_path / "cache")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_spatial_inventory_and_inspection_preserve_source_quality`

**Purpose**

Exercises `spatial inventory and inspection preserve source quality`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
extraction = _extraction_from_archive(_planning_archive(tmp_path), tmp_path)
```

**Action**

```python
references = discover_gpu_spatial_layers(extraction)
result = inspect_gpu_planning_document(extraction, _config())
```

**Expected result**

```python
assert [item.source_layer for item in references] == [
        "prescription_surf",
        "zone_urba",
    ]
assert result.zoning.reference.source_layer == "zone_urba"
assert result.zoning.summary.crs == "EPSG:2154"
assert result.zoning.summary.feature_count == 3
assert result.zoning.summary.null_geometry_count == 1
assert result.zoning.summary.invalid_geometry_count == 1
assert not result.zoning.data.geometry.iloc[1].is_valid
assert result.related_layers[0].logical_name == "prescription_surface"
assert extraction.standard_models == ("CNIG PLU v2017",)
assert [item.relative_path for item in extraction.files] == sorted(
        item.relative_path for item in extraction.files
    )
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_spatial_inventory_and_inspection_preserve_source_quality(tmp_path: Path) -> None:
    extraction = _extraction_from_archive(_planning_archive(tmp_path), tmp_path)
    references = discover_gpu_spatial_layers(extraction)
    assert [item.source_layer for item in references] == [
        "prescription_surf",
        "zone_urba",
    ]
    result = inspect_gpu_planning_document(extraction, _config())
    assert result.zoning.reference.source_layer == "zone_urba"
    assert result.zoning.summary.crs == "EPSG:2154"
    assert result.zoning.summary.feature_count == 3
    assert result.zoning.summary.null_geometry_count == 1
    assert result.zoning.summary.invalid_geometry_count == 1
    assert not result.zoning.data.geometry.iloc[1].is_valid
    assert result.related_layers[0].logical_name == "prescription_surface"
    assert extraction.standard_models == ("CNIG PLU v2017",)
    assert [item.relative_path for item in extraction.files] == sorted(
        item.relative_path for item in extraction.files
    )
```

### `test_missing_zoning_layer_fails_clearly`

**Purpose**

Exercises `missing zoning layer fails clearly`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _planning_archive(tmp_path)
extraction = _extraction_from_archive(source, tmp_path)
payload = _config().model_dump(mode="json")
payload["spatial_layers"]["zoning"]["match_tokens"] = ["missing"]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GpuSpatialInspectionError, match="zoning"):
        inspect_gpu_planning_document(
            extraction, GpuSourceConfig.model_validate(payload)
        )
```

**Regression protected**

Locks `missing zoning layer fails clearly`: the reproduced adversarial input must raise `GpuSpatialInspectionError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_missing_zoning_layer_fails_clearly(tmp_path: Path) -> None:
    source = _planning_archive(tmp_path)
    extraction = _extraction_from_archive(source, tmp_path)
    payload = _config().model_dump(mode="json")
    payload["spatial_layers"]["zoning"]["match_tokens"] = ["missing"]
    with pytest.raises(GpuSpatialInspectionError, match="zoning"):
        inspect_gpu_planning_document(
            extraction, GpuSourceConfig.model_validate(payload)
        )
```

### `test_ambiguous_zoning_layer_fails_clearly`

**Purpose**

Exercises `ambiguous zoning layer fails clearly`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
extraction = _extraction_from_archive(_planning_archive(tmp_path), tmp_path)
payload = _config().model_dump(mode="json")
payload["spatial_layers"]["zoning"]["match_tokens"] = [
        "zone_urba",
        "prescription_surf",
    ]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GpuSpatialInspectionError, match="found 2"):
        inspect_gpu_planning_document(
            extraction, GpuSourceConfig.model_validate(payload)
        )
```

**Regression protected**

Locks `ambiguous zoning layer fails clearly`: the reproduced adversarial input must raise `GpuSpatialInspectionError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_ambiguous_zoning_layer_fails_clearly(tmp_path: Path) -> None:
    extraction = _extraction_from_archive(_planning_archive(tmp_path), tmp_path)
    payload = _config().model_dump(mode="json")
    payload["spatial_layers"]["zoning"]["match_tokens"] = [
        "zone_urba",
        "prescription_surf",
    ]
    with pytest.raises(GpuSpatialInspectionError, match="found 2"):
        inspect_gpu_planning_document(
            extraction, GpuSourceConfig.model_validate(payload)
        )
```

### `test_cached_document_lineage_change_forces_refresh`

**Purpose**

Exercises `cached document lineage change forces refresh`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
first = _download(tmp_path, monkeypatch)
changed = replace(
        first.document,
        document_id="doc-2",
        written_files=tuple(
            replace(
                item,
                source_url=(
                    item.source_url.replace("/doc-1/", "/doc-2/")
                    if item.source_url is not None
                    else None
                ),
            )
            for item in first.document.written_files
        ),
    )
monkeypatch.setattr(gpu, "open_safe_https", lambda *args, **kwargs: _Response(_zip_bytes()))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert not download_gpu_document(changed, _config(), tmp_path).cache_hit
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_cached_document_lineage_change_forces_refresh(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    first = _download(tmp_path, monkeypatch)
    changed = replace(
        first.document,
        document_id="doc-2",
        written_files=tuple(
            replace(
                item,
                source_url=(
                    item.source_url.replace("/doc-1/", "/doc-2/")
                    if item.source_url is not None
                    else None
                ),
            )
            for item in first.document.written_files
        ),
    )
    monkeypatch.setattr(gpu, "open_safe_https", lambda *args, **kwargs: _Response(_zip_bytes()))
    assert not download_gpu_document(changed, _config(), tmp_path).cache_hit
```


## 7. Data contracts

No module-level canonical frame schema, mapping, or dtype declaration is present. Any frame interaction is recoverable from the complete function implementations below; no string literal is promoted to a column merely because it appears in code.

No enum/status/Literal value is classified as a column unless it is separately present in a canonical schema declaration. Mapping keys, JSON keys, dataclass fields, and configuration leaves remain distinct categories.

## 8. Interfaces

This module does not define `__all__`; no package-export guarantee is inferred from its absence. Symbols can still be imported directly or re-exported by a separate package initializer, as shown by the reference lists.

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

The module contributes to the test flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.

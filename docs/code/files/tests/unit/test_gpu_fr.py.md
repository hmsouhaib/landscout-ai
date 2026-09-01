# `tests/unit/test_gpu_fr.py`

## File identity

- Repository path: `tests/unit/test_gpu_fr.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.
- Source SHA256: `e03d758f96f52b143f2908557cea2b10c087316d73a093ddf0174f86abe46622`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for gpu fr; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import io`
- `import json`
- `import os`
- `import shutil`
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

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `_UNSAFE_ARCHIVE_NAMES`

- Category: module constant or closed domain.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `_Response`

**Source purpose:** Defines `_Response`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `io.BytesIO`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- constructor call: `tests.unit.test_gpu_fr::_patch_json_responses.opener` via `_Response`
- value/type reference: `tests.unit.test_gpu_fr::_patch_json_responses.opener` via `_Response`
- value/type reference: `tests.unit.test_gpu_fr::test_stale_recovery_backup_rejects_cache_before_network.fail_network` via `_Response`
- value/type reference: `tests.unit.test_gpu_fr::test_failed_refresh_preserves_previous_cache.fail` via `_Response`
- constructor call: `tests.unit.test_gpu_fr::test_preexisting_temporary_archive_symlink_cannot_modify_target.record_network` via `_Response`
- value/type reference: `tests.unit.test_gpu_fr::test_preexisting_temporary_archive_symlink_cannot_modify_target.record_network` via `_Response`

**Exact class source**

```python
class _Response(io.BytesIO):
    def __enter__(self) -> Self:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_Response.__enter__`

**Purpose:** Implements `enter` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def __enter__(self) -> Self:
```

- Exact decorators: none.
- Declared return annotation: `Self`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
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
def __enter__(self) -> Self:
        return self
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_Response.__exit__`

**Purpose:** Implements `exit` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def __exit__(self, *args: object) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
| `*args` | variadic positional | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `self.close` | `tests.unit.test_gpu_fr._Response.close` |

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
def __exit__(self, *args: object) -> None:
        self.close()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_config`

**Purpose:** Implements `config` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def _config() -> GpuSourceConfig:
```

- Exact decorators: none.
- Declared return annotation: `GpuSourceConfig`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `load_gpu_source_config(Path("configs/sources/gpu_fr.yaml"))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_gpu_fr::_document` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::_document` via `_config`
- direct call: `tests.unit.test_gpu_fr::_download` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::_download` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_valid_config_and_urls` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_valid_config_and_urls` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_invalid_config_values_are_rejected` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_invalid_config_values_are_rejected` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_mutated_loaded_api_origin_is_rejected_before_discovery_network` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_mutated_loaded_api_origin_is_rejected_before_discovery_network` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_gpu_source_identity_is_exact` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_gpu_source_identity_is_exact` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_gpu_cache_age_rejects_coercion_and_nonfinite` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_gpu_cache_age_rejects_coercion_and_nonfinite` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_gpu_source_config_identity_is_deterministic_and_content_bound` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_gpu_source_config_identity_is_deterministic_and_content_bound` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_unknown_config_field_is_rejected` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_unknown_config_field_is_rejected` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_gpu_api_json_is_strict_before_document_selection` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_gpu_api_json_is_strict_before_document_selection` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_written_material_url_must_be_exact_official_https_api_url` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_written_material_url_must_be_exact_official_https_api_url` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_written_material_fallback_rejects_unsafe_archive_url_provenance` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_written_material_fallback_rejects_unsafe_archive_url_provenance` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_no_current_document_is_rejected` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_no_current_document_is_rejected` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_ambiguous_current_documents_are_rejected` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_ambiguous_current_documents_are_rejected` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_missing_document_identity_is_rejected` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_missing_document_identity_is_rejected` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_document_details_must_match_selected_listing` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_document_details_must_match_selected_listing` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_document_details_commune_must_match_selected_listing` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_document_details_commune_must_match_selected_listing` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_discovery_rejects_unsafe_archive_name` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_discovery_rejects_unsafe_archive_name` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_download_rejects_document_inconsistent_with_config` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_download_rejects_document_inconsistent_with_config` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_download_rejects_forged_written_file_provenance_before_network` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_download_rejects_forged_written_file_provenance_before_network` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_download_rejects_forged_unsafe_archive_name_before_io` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_download_rejects_forged_unsafe_archive_name_before_io` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_archive_name_with_one_zip_suffix_is_not_duplicated` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_archive_name_with_one_zip_suffix_is_not_duplicated` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_fresh_cache_is_reused` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_fresh_cache_is_reused` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_stale_recovery_backup_rejects_cache_before_network` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_stale_recovery_backup_rejects_cache_before_network` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_expired_cache_is_refreshed` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_expired_cache_is_refreshed` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_failed_refresh_preserves_previous_cache` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_failed_refresh_preserves_previous_cache` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_metadata_publication_failure_rolls_back_both_cache_files` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_metadata_publication_failure_rolls_back_both_cache_files` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_preexisting_temporary_archive_symlink_cannot_modify_target` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_preexisting_temporary_archive_symlink_cannot_modify_target` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_corrupt_download_is_rejected` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_corrupt_download_is_rejected` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_tampered_sidecar_invalidates_cache` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_tampered_sidecar_invalidates_cache` via `_config`
- direct call: `tests.unit.test_gpu_fr::_extraction_from_archive` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::_extraction_from_archive` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_spatial_inventory_and_inspection_preserve_source_quality` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_spatial_inventory_and_inspection_preserve_source_quality` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_missing_zoning_layer_fails_clearly` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_missing_zoning_layer_fails_clearly` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_ambiguous_zoning_layer_fails_clearly` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_ambiguous_zoning_layer_fails_clearly` via `_config`
- direct call: `tests.unit.test_gpu_fr::_config_with_shared_role_token` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::_config_with_shared_role_token` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_inspection_rejects_mutated_config_before_layer_discovery` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_inspection_rejects_mutated_config_before_layer_discovery` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_inspection_rejects_archive_byte_mutation_before_layer_discovery` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_inspection_rejects_archive_byte_mutation_before_layer_discovery` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_inspection_rejects_document_lineage_not_matching_config` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_inspection_rejects_document_lineage_not_matching_config` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_planning_document_records_and_revalidates_exact_config_identity` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_planning_document_records_and_revalidates_exact_config_identity` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_source_complete_revalidation_rejects_coordinated_spatial_omission` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_source_complete_revalidation_rejects_coordinated_spatial_omission` via `_config`
- direct call: `tests.unit.test_gpu_fr::test_cached_document_lineage_change_forces_refresh` via `_config`
- value/type reference: `tests.unit.test_gpu_fr::test_cached_document_lineage_change_forces_refresh` via `_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_gpu_source_config` | `landscout.sources.gpu_fr.load_gpu_source_config` |
| `Path` | `pathlib.Path` |

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
def _config() -> GpuSourceConfig:
    return load_gpu_source_config(Path("configs/sources/gpu_fr.yaml"))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_listing_item`

**Purpose:** Implements `listing item` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def _listing_item(**overrides: object) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `**overrides` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_gpu_fr::_details` via `_listing_item`
- value/type reference: `tests.unit.test_gpu_fr::_details` via `_listing_item`
- direct call: `tests.unit.test_gpu_fr::_document` via `_listing_item`
- value/type reference: `tests.unit.test_gpu_fr::_document` via `_listing_item`
- direct call: `tests.unit.test_gpu_fr::test_written_material_url_must_be_exact_official_https_api_url` via `_listing_item`
- value/type reference: `tests.unit.test_gpu_fr::test_written_material_url_must_be_exact_official_https_api_url` via `_listing_item`
- direct call: `tests.unit.test_gpu_fr::test_written_material_fallback_rejects_unsafe_archive_url_provenance` via `_listing_item`
- value/type reference: `tests.unit.test_gpu_fr::test_written_material_fallback_rejects_unsafe_archive_url_provenance` via `_listing_item`
- direct call: `tests.unit.test_gpu_fr::test_no_current_document_is_rejected` via `_listing_item`
- value/type reference: `tests.unit.test_gpu_fr::test_no_current_document_is_rejected` via `_listing_item`
- direct call: `tests.unit.test_gpu_fr::test_ambiguous_current_documents_are_rejected` via `_listing_item`
- value/type reference: `tests.unit.test_gpu_fr::test_ambiguous_current_documents_are_rejected` via `_listing_item`
- direct call: `tests.unit.test_gpu_fr::test_missing_document_identity_is_rejected` via `_listing_item`
- value/type reference: `tests.unit.test_gpu_fr::test_missing_document_identity_is_rejected` via `_listing_item`
- direct call: `tests.unit.test_gpu_fr::test_document_details_must_match_selected_listing` via `_listing_item`
- value/type reference: `tests.unit.test_gpu_fr::test_document_details_must_match_selected_listing` via `_listing_item`
- direct call: `tests.unit.test_gpu_fr::test_document_details_commune_must_match_selected_listing` via `_listing_item`
- value/type reference: `tests.unit.test_gpu_fr::test_document_details_commune_must_match_selected_listing` via `_listing_item`
- direct call: `tests.unit.test_gpu_fr::test_discovery_rejects_unsafe_archive_name` via `_listing_item`
- value/type reference: `tests.unit.test_gpu_fr::test_discovery_rejects_unsafe_archive_name` via `_listing_item`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `result.update` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `result.update(overrides)` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_details`

**Purpose:** Implements `details` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def _details(**overrides: object) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `**overrides` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_gpu_fr::_document` via `_details`
- value/type reference: `tests.unit.test_gpu_fr::_document` via `_details`
- direct call: `tests.unit.test_gpu_fr::test_written_material_url_must_be_exact_official_https_api_url` via `_details`
- value/type reference: `tests.unit.test_gpu_fr::test_written_material_url_must_be_exact_official_https_api_url` via `_details`
- direct call: `tests.unit.test_gpu_fr::test_written_material_fallback_rejects_unsafe_archive_url_provenance` via `_details`
- value/type reference: `tests.unit.test_gpu_fr::test_written_material_fallback_rejects_unsafe_archive_url_provenance` via `_details`
- direct call: `tests.unit.test_gpu_fr::test_document_details_must_match_selected_listing` via `_details`
- value/type reference: `tests.unit.test_gpu_fr::test_document_details_must_match_selected_listing` via `_details`
- direct call: `tests.unit.test_gpu_fr::test_document_details_commune_must_match_selected_listing` via `_details`
- value/type reference: `tests.unit.test_gpu_fr::test_document_details_commune_must_match_selected_listing` via `_details`
- direct call: `tests.unit.test_gpu_fr::test_discovery_rejects_unsafe_archive_name` via `_details`
- value/type reference: `tests.unit.test_gpu_fr::test_discovery_rejects_unsafe_archive_name` via `_details`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_listing_item` | `tests.unit.test_gpu_fr._listing_item` |
| `result.update` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `result.update(overrides)` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_files`

**Purpose:** Implements `files` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def _files() -> list[dict[str, object]]:
```

- Exact decorators: none.
- Declared return annotation: `list[dict[str, object]]`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `[{"name": "reglement.pdf", "title": "Règlement écrit", "path": "Règlements"}]`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_gpu_fr::_document` via `_files`
- value/type reference: `tests.unit.test_gpu_fr::_document` via `_files`
- direct call: `tests.unit.test_gpu_fr::test_written_material_url_must_be_exact_official_https_api_url` via `_files`
- value/type reference: `tests.unit.test_gpu_fr::test_written_material_url_must_be_exact_official_https_api_url` via `_files`
- direct call: `tests.unit.test_gpu_fr::test_written_material_fallback_rejects_unsafe_archive_url_provenance` via `_files`
- value/type reference: `tests.unit.test_gpu_fr::test_written_material_fallback_rejects_unsafe_archive_url_provenance` via `_files`
- direct call: `tests.unit.test_gpu_fr::test_document_details_must_match_selected_listing` via `_files`
- value/type reference: `tests.unit.test_gpu_fr::test_document_details_must_match_selected_listing` via `_files`
- direct call: `tests.unit.test_gpu_fr::test_document_details_commune_must_match_selected_listing` via `_files`
- value/type reference: `tests.unit.test_gpu_fr::test_document_details_commune_must_match_selected_listing` via `_files`
- direct call: `tests.unit.test_gpu_fr::test_discovery_rejects_unsafe_archive_name` via `_files`
- value/type reference: `tests.unit.test_gpu_fr::test_discovery_rejects_unsafe_archive_name` via `_files`

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
def _files() -> list[dict[str, object]]:
    return [{"name": "reglement.pdf", "title": "Règlement écrit", "path": "Règlements"}]
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_patch_json_responses`

**Purpose:** Implements `patch json responses` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def _patch_json_responses(
    monkeypatch: pytest.MonkeyPatch, values: list[object]
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `values` | positional-or-keyword | `list[object]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_gpu_fr::_document` via `_patch_json_responses`
- value/type reference: `tests.unit.test_gpu_fr::_document` via `_patch_json_responses`
- direct call: `tests.unit.test_gpu_fr::test_written_material_url_must_be_exact_official_https_api_url` via `_patch_json_responses`
- value/type reference: `tests.unit.test_gpu_fr::test_written_material_url_must_be_exact_official_https_api_url` via `_patch_json_responses`
- direct call: `tests.unit.test_gpu_fr::test_written_material_fallback_rejects_unsafe_archive_url_provenance` via `_patch_json_responses`
- value/type reference: `tests.unit.test_gpu_fr::test_written_material_fallback_rejects_unsafe_archive_url_provenance` via `_patch_json_responses`
- direct call: `tests.unit.test_gpu_fr::test_no_current_document_is_rejected` via `_patch_json_responses`
- value/type reference: `tests.unit.test_gpu_fr::test_no_current_document_is_rejected` via `_patch_json_responses`
- direct call: `tests.unit.test_gpu_fr::test_ambiguous_current_documents_are_rejected` via `_patch_json_responses`
- value/type reference: `tests.unit.test_gpu_fr::test_ambiguous_current_documents_are_rejected` via `_patch_json_responses`
- direct call: `tests.unit.test_gpu_fr::test_missing_document_identity_is_rejected` via `_patch_json_responses`
- value/type reference: `tests.unit.test_gpu_fr::test_missing_document_identity_is_rejected` via `_patch_json_responses`
- direct call: `tests.unit.test_gpu_fr::test_document_details_must_match_selected_listing` via `_patch_json_responses`
- value/type reference: `tests.unit.test_gpu_fr::test_document_details_must_match_selected_listing` via `_patch_json_responses`
- direct call: `tests.unit.test_gpu_fr::test_document_details_commune_must_match_selected_listing` via `_patch_json_responses`
- value/type reference: `tests.unit.test_gpu_fr::test_document_details_commune_must_match_selected_listing` via `_patch_json_responses`
- direct call: `tests.unit.test_gpu_fr::test_discovery_rejects_unsafe_archive_name` via `_patch_json_responses`
- value/type reference: `tests.unit.test_gpu_fr::test_discovery_rejects_unsafe_archive_name` via `_patch_json_responses`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `iter` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _patch_json_responses(
    monkeypatch: pytest.MonkeyPatch, values: list[object]
) -> None:
    responses = iter(values)

    def opener(*args: object, **kwargs: object) -> _Response:
        return _Response(json.dumps(next(responses)).encode())

    monkeypatch.setattr(gpu, "open_safe_https", opener)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_patch_json_responses.opener`

**Purpose:** Implements `opener` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def opener(*args: object, **kwargs: object) -> _Response:
```

- Exact decorators: none.
- Declared return annotation: `_Response`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `_Response(json.dumps(next(responses)).encode())`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_Response` | `tests.unit.test_gpu_fr._Response` |
| `json.dumps(next(responses)).encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `next` | `unresolved local/third-party receiver; no ownership inferred` |

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
def opener(*args: object, **kwargs: object) -> _Response:
        return _Response(json.dumps(next(responses)).encode())
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_document`

**Purpose:** Implements `document` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def _document(monkeypatch: pytest.MonkeyPatch):
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `discover_current_gpu_document(_config())`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_gpu_fr::_download` via `_document`
- value/type reference: `tests.unit.test_gpu_fr::_download` via `_document`
- direct call: `tests.unit.test_gpu_fr::test_document_discovery_success` via `_document`
- value/type reference: `tests.unit.test_gpu_fr::test_document_discovery_success` via `_document`
- direct call: `tests.unit.test_gpu_fr::test_download_rejects_document_inconsistent_with_config` via `_document`
- value/type reference: `tests.unit.test_gpu_fr::test_download_rejects_document_inconsistent_with_config` via `_document`
- direct call: `tests.unit.test_gpu_fr::test_download_rejects_forged_written_file_provenance_before_network` via `_document`
- value/type reference: `tests.unit.test_gpu_fr::test_download_rejects_forged_written_file_provenance_before_network` via `_document`
- direct call: `tests.unit.test_gpu_fr::test_download_rejects_forged_unsafe_archive_name_before_io` via `_document`
- value/type reference: `tests.unit.test_gpu_fr::test_download_rejects_forged_unsafe_archive_name_before_io` via `_document`
- direct call: `tests.unit.test_gpu_fr::test_archive_name_with_one_zip_suffix_is_not_duplicated` via `_document`
- value/type reference: `tests.unit.test_gpu_fr::test_archive_name_with_one_zip_suffix_is_not_duplicated` via `_document`
- direct call: `tests.unit.test_gpu_fr::test_preexisting_temporary_archive_symlink_cannot_modify_target` via `_document`
- value/type reference: `tests.unit.test_gpu_fr::test_preexisting_temporary_archive_symlink_cannot_modify_target` via `_document`
- direct call: `tests.unit.test_gpu_fr::test_corrupt_download_is_rejected` via `_document`
- value/type reference: `tests.unit.test_gpu_fr::test_corrupt_download_is_rejected` via `_document`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_patch_json_responses` | `tests.unit.test_gpu_fr._patch_json_responses` |
| `_listing_item` | `tests.unit.test_gpu_fr._listing_item` |
| `_details` | `tests.unit.test_gpu_fr._details` |
| `_files` | `tests.unit.test_gpu_fr._files` |
| `discover_current_gpu_document` | `landscout.sources.gpu_fr.discover_current_gpu_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |

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
def _document(monkeypatch: pytest.MonkeyPatch):
    _patch_json_responses(monkeypatch, [[_listing_item()], _details(), _files()])
    return discover_current_gpu_document(_config())
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_zip_bytes`

**Purpose:** Implements `zip bytes` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def _zip_bytes(files: dict[str, bytes] | None = None) -> bytes:
```

- Exact decorators: none.
- Declared return annotation: `bytes`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `files` | positional-or-keyword | `dict[str, bytes] \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `stream.getvalue()`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_gpu_fr::test_expired_cache_is_refreshed` via `_zip_bytes`
- value/type reference: `tests.unit.test_gpu_fr::test_expired_cache_is_refreshed` via `_zip_bytes`
- direct call: `tests.unit.test_gpu_fr::test_preexisting_temporary_archive_symlink_cannot_modify_target.record_network` via `_zip_bytes`
- value/type reference: `tests.unit.test_gpu_fr::test_preexisting_temporary_archive_symlink_cannot_modify_target.record_network` via `_zip_bytes`
- direct call: `tests.unit.test_gpu_fr::test_archive_path_traversal_is_rejected` via `_zip_bytes`
- value/type reference: `tests.unit.test_gpu_fr::test_archive_path_traversal_is_rejected` via `_zip_bytes`
- direct call: `tests.unit.test_gpu_fr::test_zip_cannot_claim_extraction_manifest_path` via `_zip_bytes`
- value/type reference: `tests.unit.test_gpu_fr::test_zip_cannot_claim_extraction_manifest_path` via `_zip_bytes`
- direct call: `tests.unit.test_gpu_fr::test_extraction_inventory_and_cache` via `_zip_bytes`
- value/type reference: `tests.unit.test_gpu_fr::test_extraction_inventory_and_cache` via `_zip_bytes`
- direct call: `tests.unit.test_gpu_fr::test_stale_download_object_rejects_replaced_valid_archive` via `_zip_bytes`
- value/type reference: `tests.unit.test_gpu_fr::test_stale_download_object_rejects_replaced_valid_archive` via `_zip_bytes`
- direct call: `tests.unit.test_gpu_fr::test_tampered_extraction_is_rebuilt_from_verified_archive` via `_zip_bytes`
- value/type reference: `tests.unit.test_gpu_fr::test_tampered_extraction_is_rebuilt_from_verified_archive` via `_zip_bytes`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `io.BytesIO` | `io.BytesIO` |
| `zipfile.ZipFile` | `zipfile.ZipFile` |
| `(files or {"document/readme.txt": b"GPU"}).items` | `unresolved local/third-party receiver; no ownership inferred` |
| `archive.writestr` | `unresolved local/third-party receiver; no ownership inferred` |
| `stream.getvalue` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `zipfile.ZipFile` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_zip_member_bytes`

**Purpose:** Implements `zip member bytes` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def _zip_member_bytes(members: list[tuple[str, bytes]]) -> bytes:
```

- Exact decorators: none.
- Declared return annotation: `bytes`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `members` | positional-or-keyword | `list[tuple[str, bytes]]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `stream.getvalue()`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_gpu_fr::test_duplicate_zip_extraction_targets_are_rejected` via `_zip_member_bytes`
- value/type reference: `tests.unit.test_gpu_fr::test_duplicate_zip_extraction_targets_are_rejected` via `_zip_member_bytes`
- direct call: `tests.unit.test_gpu_fr::test_zip_file_directory_target_collision_is_rejected` via `_zip_member_bytes`
- value/type reference: `tests.unit.test_gpu_fr::test_zip_file_directory_target_collision_is_rejected` via `_zip_member_bytes`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `io.BytesIO` | `io.BytesIO` |
| `warnings.catch_warnings` | `warnings.catch_warnings` |
| `warnings.simplefilter` | `warnings.simplefilter` |
| `zipfile.ZipFile` | `zipfile.ZipFile` |
| `archive.writestr` | `unresolved local/third-party receiver; no ownership inferred` |
| `stream.getvalue` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `zipfile.ZipFile` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_download`

**Purpose:** Implements `download` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def _download(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    archive_bytes: bytes | None = None,
) -> GpuArchiveDownload:
```

- Exact decorators: none.
- Declared return annotation: `GpuArchiveDownload`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `archive_bytes` | positional-or-keyword | `bytes \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `download_gpu_document(document, _config(), tmp_path)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_gpu_fr::test_successful_download_persists_sha_and_sidecar` via `_download`
- value/type reference: `tests.unit.test_gpu_fr::test_successful_download_persists_sha_and_sidecar` via `_download`
- direct call: `tests.unit.test_gpu_fr::test_fresh_cache_is_reused` via `_download`
- value/type reference: `tests.unit.test_gpu_fr::test_fresh_cache_is_reused` via `_download`
- direct call: `tests.unit.test_gpu_fr::test_boolean_cache_integrity_counts_are_not_accepted_as_integers` via `_download`
- value/type reference: `tests.unit.test_gpu_fr::test_boolean_cache_integrity_counts_are_not_accepted_as_integers` via `_download`
- direct call: `tests.unit.test_gpu_fr::test_stale_recovery_backup_rejects_cache_before_network` via `_download`
- value/type reference: `tests.unit.test_gpu_fr::test_stale_recovery_backup_rejects_cache_before_network` via `_download`
- direct call: `tests.unit.test_gpu_fr::test_expired_cache_is_refreshed` via `_download`
- value/type reference: `tests.unit.test_gpu_fr::test_expired_cache_is_refreshed` via `_download`
- direct call: `tests.unit.test_gpu_fr::test_failed_refresh_preserves_previous_cache` via `_download`
- value/type reference: `tests.unit.test_gpu_fr::test_failed_refresh_preserves_previous_cache` via `_download`
- direct call: `tests.unit.test_gpu_fr::test_metadata_publication_failure_rolls_back_both_cache_files` via `_download`
- value/type reference: `tests.unit.test_gpu_fr::test_metadata_publication_failure_rolls_back_both_cache_files` via `_download`
- direct call: `tests.unit.test_gpu_fr::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_download`
- value/type reference: `tests.unit.test_gpu_fr::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_download`
- direct call: `tests.unit.test_gpu_fr::test_tampered_sidecar_invalidates_cache` via `_download`
- value/type reference: `tests.unit.test_gpu_fr::test_tampered_sidecar_invalidates_cache` via `_download`
- direct call: `tests.unit.test_gpu_fr::test_extraction_inventory_and_cache` via `_download`
- value/type reference: `tests.unit.test_gpu_fr::test_extraction_inventory_and_cache` via `_download`
- direct call: `tests.unit.test_gpu_fr::test_extraction_manifest_is_created_exclusively` via `_download`
- value/type reference: `tests.unit.test_gpu_fr::test_extraction_manifest_is_created_exclusively` via `_download`
- direct call: `tests.unit.test_gpu_fr::test_stale_extraction_backup_fails_closed_and_is_preserved` via `_download`
- value/type reference: `tests.unit.test_gpu_fr::test_stale_extraction_backup_fails_closed_and_is_preserved` via `_download`
- direct call: `tests.unit.test_gpu_fr::test_extraction_publication_and_rollback_failure_preserves_backup` via `_download`
- value/type reference: `tests.unit.test_gpu_fr::test_extraction_publication_and_rollback_failure_preserves_backup` via `_download`
- direct call: `tests.unit.test_gpu_fr::test_extraction_publication_failure_restores_existing_root` via `_download`
- value/type reference: `tests.unit.test_gpu_fr::test_extraction_publication_failure_restores_existing_root` via `_download`
- direct call: `tests.unit.test_gpu_fr::test_extraction_backup_move_failure_preserves_existing_root` via `_download`
- value/type reference: `tests.unit.test_gpu_fr::test_extraction_backup_move_failure_preserves_existing_root` via `_download`
- direct call: `tests.unit.test_gpu_fr::test_extraction_temporary_link_is_rejected_without_unlinking_target` via `_download`
- value/type reference: `tests.unit.test_gpu_fr::test_extraction_temporary_link_is_rejected_without_unlinking_target` via `_download`
- direct call: `tests.unit.test_gpu_fr::test_stale_extraction_temporary_directory_fails_closed_and_is_preserved` via `_download`
- value/type reference: `tests.unit.test_gpu_fr::test_stale_extraction_temporary_directory_fails_closed_and_is_preserved` via `_download`
- direct call: `tests.unit.test_gpu_fr::test_duplicate_extraction_manifest_key_forces_verified_rebuild` via `_download`
- value/type reference: `tests.unit.test_gpu_fr::test_duplicate_extraction_manifest_key_forces_verified_rebuild` via `_download`
- direct call: `tests.unit.test_gpu_fr::test_stale_download_object_rejects_replaced_valid_archive` via `_download`
- value/type reference: `tests.unit.test_gpu_fr::test_stale_download_object_rejects_replaced_valid_archive` via `_download`
- direct call: `tests.unit.test_gpu_fr::test_extraction_rejects_archive_object_inconsistent_with_path` via `_download`
- value/type reference: `tests.unit.test_gpu_fr::test_extraction_rejects_archive_object_inconsistent_with_path` via `_download`
- direct call: `tests.unit.test_gpu_fr::test_tampered_extraction_is_rebuilt_from_verified_archive` via `_download`
- value/type reference: `tests.unit.test_gpu_fr::test_tampered_extraction_is_rebuilt_from_verified_archive` via `_download`
- direct call: `tests.unit.test_gpu_fr::test_cached_document_lineage_change_forces_refresh` via `_download`
- value/type reference: `tests.unit.test_gpu_fr::test_cached_document_lineage_change_forces_refresh` via `_download`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_document` | `tests.unit.test_gpu_fr._document` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `download_gpu_document` | `landscout.sources.gpu_fr.download_gpu_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |

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
def _download(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    archive_bytes: bytes | None = None,
) -> GpuArchiveDownload:
    document = _document(monkeypatch)
    monkeypatch.setattr(
        gpu,
        "open_safe_https",
        lambda *args, **kwargs: _Response(archive_bytes or _zip_bytes()),
    )
    return download_gpu_document(document, _config(), tmp_path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_planning_archive`

**Purpose:** Implements `planning archive` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def _planning_archive(tmp_path: Path) -> Path:
```

- Exact decorators: none.
- Declared return annotation: `Path`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `archive_path`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_gpu_fr::test_spatial_inventory_and_inspection_preserve_source_quality` via `_planning_archive`
- value/type reference: `tests.unit.test_gpu_fr::test_spatial_inventory_and_inspection_preserve_source_quality` via `_planning_archive`
- direct call: `tests.unit.test_gpu_fr::test_missing_zoning_layer_fails_clearly` via `_planning_archive`
- value/type reference: `tests.unit.test_gpu_fr::test_missing_zoning_layer_fails_clearly` via `_planning_archive`
- direct call: `tests.unit.test_gpu_fr::test_ambiguous_zoning_layer_fails_clearly` via `_planning_archive`
- value/type reference: `tests.unit.test_gpu_fr::test_ambiguous_zoning_layer_fails_clearly` via `_planning_archive`
- direct call: `tests.unit.test_gpu_fr::test_inspection_rejects_one_physical_layer_for_two_logical_roles` via `_planning_archive`
- value/type reference: `tests.unit.test_gpu_fr::test_inspection_rejects_one_physical_layer_for_two_logical_roles` via `_planning_archive`
- direct call: `tests.unit.test_gpu_fr::test_inspection_rejects_mutated_config_before_layer_discovery` via `_planning_archive`
- value/type reference: `tests.unit.test_gpu_fr::test_inspection_rejects_mutated_config_before_layer_discovery` via `_planning_archive`
- direct call: `tests.unit.test_gpu_fr::test_inspection_rejects_archive_byte_mutation_before_layer_discovery` via `_planning_archive`
- value/type reference: `tests.unit.test_gpu_fr::test_inspection_rejects_archive_byte_mutation_before_layer_discovery` via `_planning_archive`
- direct call: `tests.unit.test_gpu_fr::test_inspection_rejects_document_lineage_not_matching_config` via `_planning_archive`
- value/type reference: `tests.unit.test_gpu_fr::test_inspection_rejects_document_lineage_not_matching_config` via `_planning_archive`
- direct call: `tests.unit.test_gpu_fr::test_planning_document_records_and_revalidates_exact_config_identity` via `_planning_archive`
- value/type reference: `tests.unit.test_gpu_fr::test_planning_document_records_and_revalidates_exact_config_identity` via `_planning_archive`
- direct call: `tests.unit.test_gpu_fr::test_source_complete_revalidation_rejects_coordinated_spatial_omission` via `_planning_archive`
- value/type reference: `tests.unit.test_gpu_fr::test_source_complete_revalidation_rejects_coordinated_spatial_omission` via `_planning_archive`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `package.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `Polygon` | `shapely.geometry.Polygon` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `zoning.to_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `prescription.to_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `(package / "31395_reglement.pdf").write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `(package / "metadata.xml").write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `zipfile.ZipFile` | `zipfile.ZipFile` |
| `package.rglob` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `archive.write` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.relative_to(package).as_posix` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.relative_to` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `zipfile.ZipFile`<br>`path.is_file` |
| Filesystem/archive write or publication | `package.mkdir`<br>`(package / "31395_reglement.pdf").write_bytes`<br>`(package / "metadata.xml").write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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
    prescription = gpd.GeoDataFrame({"TYPEPSC": [5]}, geometry=[valid], crs="EPSG:2154")
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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_config_and_urls`

**Purpose:** Regression invariant: valid config and urls. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_config_and_urls() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert build_gpu_partition(config) == "DU_31395"`
  - `assert "partition=DU_31395" in build_gpu_document_list_url(config)`
  - `assert build_gpu_partition_download_url(config).endswith(<br>        "/document/download-by-partition/DU_31395"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_config` | `tests.unit.test_gpu_fr._config` |
| `build_gpu_partition` | `landscout.sources.gpu_fr.build_gpu_partition` |
| `build_gpu_document_list_url` | `landscout.sources.gpu_fr.build_gpu_document_list_url` |
| `build_gpu_partition_download_url(config).endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `build_gpu_partition_download_url` | `landscout.sources.gpu_fr.build_gpu_partition_download_url` |

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
def test_valid_config_and_urls() -> None:
    config = _config()
    assert build_gpu_partition(config) == "DU_31395"
    assert "partition=DU_31395" in build_gpu_document_list_url(config)
    assert build_gpu_partition_download_url(config).endswith(
        "/document/download-by-partition/DU_31395"
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_gpu_yaml_key_is_rejected`

**Purpose:** Regression invariant: duplicate gpu yaml key is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_gpu_yaml_key_is_rejected(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(gpu.GpuConfigError)`
- Exact assertions:
  - `assert "duplicate" in str(captured.value.__cause__).casefold()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `config_path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path("configs/sources/gpu_fr.yaml").read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path` | `pathlib.Path` |
| `pytest.raises` | `pytest.raises` |
| `load_gpu_source_config` | `landscout.sources.gpu_fr.load_gpu_source_config` |
| `str(captured.value.__cause__).casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `Path("configs/sources/gpu_fr.yaml").read_bytes` |
| Filesystem/archive write or publication | `config_path.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_duplicate_gpu_yaml_key_is_rejected(tmp_path: Path) -> None:
    config_path = tmp_path / "gpu.yaml"
    config_path.write_bytes(
        Path("configs/sources/gpu_fr.yaml").read_bytes() + b"\nprovider: UNTRUSTED\n"
    )

    with pytest.raises(gpu.GpuConfigError) as captured:
        load_gpu_source_config(config_path)

    assert "duplicate" in str(captured.value.__cause__).casefold()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_config_values_are_rejected`

**Purpose:** Regression invariant: invalid config values are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_config_values_are_rejected(
    path: tuple[str, str], value: object
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("path", "value"),
    [
        (("pilot", "commune_code"), "3139"),
        (("api", "base_url"), "file:///api"),
        (("api", "base_url"), "http://www.geoportail-urbanisme.gouv.fr/api"),
        (("api", "base_url"), "https://example.com/api"),
        (("api", "base_url"), "https://www.geoportail-urbanisme.gouv.fr:8443/api"),
        (("api", "base_url"), "https://www.geoportail-urbanisme.gouv.fr/api?x=1"),
        (("download", "strategy"), "parcel"),
        (("download", "partition_template"), ""),
        (("cache", "max_age_hours"), -1),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `tuple[str, str]` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_config().model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `_config` | `tests.unit.test_gpu_fr._config` |
| `pytest.raises` | `pytest.raises` |
| `GpuSourceConfig.model_validate` | `landscout.sources.gpu_fr.GpuSourceConfig.model_validate` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
| In-memory mutation | `payload[path[0]][path[1]] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_invalid_config_values_are_rejected(
    path: tuple[str, str], value: object
) -> None:
    payload = _config().model_dump(mode="json")
    payload[path[0]][path[1]] = value
    with pytest.raises(ValidationError):
        GpuSourceConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_mutated_loaded_api_origin_is_rejected_before_discovery_network`

**Purpose:** Regression invariant: mutated loaded api origin is rejected before discovery network. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_mutated_loaded_api_origin_is_rejected_before_discovery_network(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError, match="frozen")`
  - `pytest.raises(GpuDiscoveryError, match="config\|official\|origin")`
- Exact assertions:
  - `assert network_calls == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_config` | `tests.unit.test_gpu_fr._config` |
| `pytest.raises` | `pytest.raises` |
| `HttpUrl` | `pydantic.HttpUrl` |
| `config.api.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `config.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `discover_current_gpu_document` | `landscout.sources.gpu_fr.discover_current_gpu_document` |

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
| In-memory mutation | `config.api.base_url = HttpUrl("https://unrelated.example/api")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_mutated_loaded_api_origin_is_rejected_before_discovery_network(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config = _config()
    with pytest.raises(ValidationError, match="frozen"):
        config.api.base_url = HttpUrl("https://unrelated.example/api")
    forged_api = config.api.model_copy(
        update={"base_url": HttpUrl("https://unrelated.example/api")}
    )
    forged = config.model_copy(update={"api": forged_api})
    network_calls = 0

    def fail_network(*args: object, **kwargs: object) -> object:
        nonlocal network_calls
        network_calls += 1
        raise AssertionError("network used after GPU origin mutation")

    monkeypatch.setattr(gpu, "open_safe_https", fail_network)

    with pytest.raises(GpuDiscoveryError, match="config|official|origin"):
        discover_current_gpu_document(forged)

    assert network_calls == 0
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_mutated_loaded_api_origin_is_rejected_before_discovery_network.fail_network`

**Purpose:** Implements `fail network` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def fail_network(*args: object, **kwargs: object) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `AssertionError("network used after GPU origin mutation")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |

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
def fail_network(*args: object, **kwargs: object) -> object:
        nonlocal network_calls
        network_calls += 1
        raise AssertionError("network used after GPU origin mutation")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_gpu_source_identity_is_exact`

**Purpose:** Regression invariant: gpu source identity is exact. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_gpu_source_identity_is_exact(field: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("field", ["provider", "portal"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `field` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_config().model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `_config` | `tests.unit.test_gpu_fr._config` |
| `pytest.raises` | `pytest.raises` |
| `GpuSourceConfig.model_validate` | `landscout.sources.gpu_fr.GpuSourceConfig.model_validate` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
| In-memory mutation | `payload[field] = "UNTRUSTED"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_gpu_source_identity_is_exact(field: str) -> None:
    payload = _config().model_dump(mode="python")
    payload[field] = "UNTRUSTED"

    with pytest.raises(ValidationError):
        GpuSourceConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_gpu_cache_age_rejects_coercion_and_nonfinite`

**Purpose:** Regression invariant: gpu cache age rejects coercion and nonfinite. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_gpu_cache_age_rejects_coercion_and_nonfinite(value: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize("value", [True, "168", float("nan"), float("inf")])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_config().model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `_config` | `tests.unit.test_gpu_fr._config` |
| `pytest.raises` | `pytest.raises` |
| `GpuSourceConfig.model_validate` | `landscout.sources.gpu_fr.GpuSourceConfig.model_validate` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `payload["cache"]["max_age_hours"] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_gpu_cache_age_rejects_coercion_and_nonfinite(value: object) -> None:
    payload = _config().model_dump(mode="python")
    payload["cache"]["max_age_hours"] = value

    with pytest.raises(ValidationError):
        GpuSourceConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_gpu_source_config_identity_is_deterministic_and_content_bound`

**Purpose:** Regression invariant: gpu source config identity is deterministic and content bound. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_gpu_source_config_identity_is_deterministic_and_content_bound() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert gpu._source_config_sha256(reconstructed) == gpu._source_config_sha256(config)`
  - `assert gpu._source_config_sha256(changed) != gpu._source_config_sha256(config)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_config` | `tests.unit.test_gpu_fr._config` |
| `GpuSourceConfig.model_validate` | `landscout.sources.gpu_fr.GpuSourceConfig.model_validate` |
| `dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `reversed` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `config.model_dump(mode="python").items` | `unresolved local/third-party receiver; no ownership inferred` |
| `config.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpu._source_config_sha256` | `landscout.sources.gpu_fr._source_config_sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `gpu._source_config_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `changed_payload["cache"]["max_age_hours"] = 169` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_gpu_source_config_identity_is_deterministic_and_content_bound() -> None:
    config = _config()
    reconstructed = GpuSourceConfig.model_validate(
        dict(reversed(tuple(config.model_dump(mode="python").items())))
    )
    changed_payload = config.model_dump(mode="python")
    changed_payload["cache"]["max_age_hours"] = 169
    changed = GpuSourceConfig.model_validate(changed_payload)

    assert gpu._source_config_sha256(reconstructed) == gpu._source_config_sha256(config)
    assert gpu._source_config_sha256(changed) != gpu._source_config_sha256(config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unknown_config_field_is_rejected`

**Purpose:** Regression invariant: unknown config field is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unknown_config_field_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_config().model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `_config` | `tests.unit.test_gpu_fr._config` |
| `pytest.raises` | `pytest.raises` |
| `GpuSourceConfig.model_validate` | `landscout.sources.gpu_fr.GpuSourceConfig.model_validate` |

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
| In-memory mutation | `payload["unexpected"] = True` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_unknown_config_field_is_rejected() -> None:
    payload = _config().model_dump(mode="json")
    payload["unexpected"] = True
    with pytest.raises(ValidationError):
        GpuSourceConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_document_discovery_success`

**Purpose:** Regression invariant: document discovery success. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_document_discovery_success(monkeypatch: pytest.MonkeyPatch) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert document.document_id == "doc-1"`
  - `assert document.document_type == "PLU"`
  - `assert document.effective_status == "EN_VIGUEUR"`
  - `assert document.archive_name == "31395_PLU_20240215"`
  - `assert document.version is None`
  - `assert document.written_files[0].title == "Règlement écrit"`
  - `assert document.written_files[0].source_url == (<br>        "https://www.geoportail-urbanisme.gouv.fr/api/document/"<br>        "doc-1/files/reglement.pdf"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_document` | `tests.unit.test_gpu_fr._document` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_gpu_api_json_is_strict_before_document_selection`

**Purpose:** Regression invariant: gpu api json is strict before document selection. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_gpu_api_json_is_strict_before_document_selection(
    monkeypatch: pytest.MonkeyPatch,
    payload: bytes,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "payload",
    [
        b'[{"id":"doc-1","id":"doc-2"}]',
        b"[NaN]",
        b"[Infinity]",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `payload` | positional-or-keyword | `bytes` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuDiscoveryError, match="JSON\|duplicate\|finite\|metadata")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `discover_current_gpu_document` | `landscout.sources.gpu_fr.discover_current_gpu_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
def test_gpu_api_json_is_strict_before_document_selection(
    monkeypatch: pytest.MonkeyPatch,
    payload: bytes,
) -> None:
    monkeypatch.setattr(
        gpu,
        "open_safe_https",
        lambda *args, **kwargs: _Response(payload),
    )

    with pytest.raises(GpuDiscoveryError, match="JSON|duplicate|finite|metadata"):
        discover_current_gpu_document(_config())
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_written_material_url_must_be_exact_official_https_api_url`

**Purpose:** Regression invariant: written material url must be exact official https api url. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_written_material_url_must_be_exact_official_https_api_url(
    monkeypatch: pytest.MonkeyPatch,
    source_url: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "source_url",
    [
        (
            "http://www.geoportail-urbanisme.gouv.fr/api/document/"
            "doc-1/files/reglement.pdf"
        ),
        "https://unrelated.example/api/document/doc-1/files/reglement.pdf",
    ],
    ids=["http", "unrelated-https-origin"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `source_url` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuDiscoveryError, match="written material URL")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_patch_json_responses` | `tests.unit.test_gpu_fr._patch_json_responses` |
| `_listing_item` | `tests.unit.test_gpu_fr._listing_item` |
| `_details` | `tests.unit.test_gpu_fr._details` |
| `_files` | `tests.unit.test_gpu_fr._files` |
| `pytest.raises` | `pytest.raises` |
| `discover_current_gpu_document` | `landscout.sources.gpu_fr.discover_current_gpu_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_written_material_fallback_rejects_unsafe_archive_url_provenance`

**Purpose:** Regression invariant: written material fallback rejects unsafe archive url provenance. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_written_material_fallback_rejects_unsafe_archive_url_provenance(
    monkeypatch: pytest.MonkeyPatch,
    archive_url: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "archive_url",
    [
        (
            "http://www.geoportail-urbanisme.gouv.fr/api/document/"
            "doc-1/download/31395_PLU_20240215.zip"
        ),
        (
            "https://unrelated.example/api/document/doc-1/download/"
            "31395_PLU_20240215.zip"
        ),
    ],
    ids=["http", "unrelated-https-origin"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `archive_url` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuDiscoveryError, match="archive URL")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_patch_json_responses` | `tests.unit.test_gpu_fr._patch_json_responses` |
| `_listing_item` | `tests.unit.test_gpu_fr._listing_item` |
| `_details` | `tests.unit.test_gpu_fr._details` |
| `_files` | `tests.unit.test_gpu_fr._files` |
| `pytest.raises` | `pytest.raises` |
| `discover_current_gpu_document` | `landscout.sources.gpu_fr.discover_current_gpu_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_no_current_document_is_rejected`

**Purpose:** Regression invariant: no current document is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_no_current_document_is_rejected(monkeypatch: pytest.MonkeyPatch) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuDiscoveryError, match="No current")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_patch_json_responses` | `tests.unit.test_gpu_fr._patch_json_responses` |
| `_listing_item` | `tests.unit.test_gpu_fr._listing_item` |
| `pytest.raises` | `pytest.raises` |
| `discover_current_gpu_document` | `landscout.sources.gpu_fr.discover_current_gpu_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |

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
def test_no_current_document_is_rejected(monkeypatch: pytest.MonkeyPatch) -> None:
    _patch_json_responses(monkeypatch, [[_listing_item(status="document.deleted")]])
    with pytest.raises(GpuDiscoveryError, match="No current"):
        discover_current_gpu_document(_config())
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_ambiguous_current_documents_are_rejected`

**Purpose:** Regression invariant: ambiguous current documents are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_ambiguous_current_documents_are_rejected(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuDiscoveryError, match="Ambiguous")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_patch_json_responses` | `tests.unit.test_gpu_fr._patch_json_responses` |
| `_listing_item` | `tests.unit.test_gpu_fr._listing_item` |
| `pytest.raises` | `pytest.raises` |
| `discover_current_gpu_document` | `landscout.sources.gpu_fr.discover_current_gpu_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |

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
def test_ambiguous_current_documents_are_rejected(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _patch_json_responses(monkeypatch, [[_listing_item(), _listing_item(id="doc-2")]])
    with pytest.raises(GpuDiscoveryError, match="Ambiguous"):
        discover_current_gpu_document(_config())
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_document_identity_is_rejected`

**Purpose:** Regression invariant: missing document identity is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_missing_document_identity_is_rejected(
    monkeypatch: pytest.MonkeyPatch, field: str
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("field", ["id", "originalName", "type"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `field` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuDiscoveryError, match="missing")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_listing_item` | `tests.unit.test_gpu_fr._listing_item` |
| `item.pop` | `unresolved local/third-party receiver; no ownership inferred` |
| `_patch_json_responses` | `tests.unit.test_gpu_fr._patch_json_responses` |
| `pytest.raises` | `pytest.raises` |
| `discover_current_gpu_document` | `landscout.sources.gpu_fr.discover_current_gpu_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
| In-memory mutation | `item.pop(field)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_document_details_must_match_selected_listing`

**Purpose:** Regression invariant: document details must match selected listing. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_document_details_must_match_selected_listing(
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    different_value: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "different_value"),
    [
        ("id", "doc-2"),
        ("originalName", "31395_PLU_OTHER"),
        ("name", "DU_99999"),
        ("type", "CC"),
        ("status", "document.deleted"),
        ("legalStatus", "CANCELLED"),
        ("effectiveStatus", "ANNULE"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `field` | positional-or-keyword | `str` | `required` |
| `different_value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuDiscoveryError, match="match\|changed\|current")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_patch_json_responses` | `tests.unit.test_gpu_fr._patch_json_responses` |
| `_listing_item` | `tests.unit.test_gpu_fr._listing_item` |
| `_details` | `tests.unit.test_gpu_fr._details` |
| `_files` | `tests.unit.test_gpu_fr._files` |
| `pytest.raises` | `pytest.raises` |
| `discover_current_gpu_document` | `landscout.sources.gpu_fr.discover_current_gpu_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_document_details_commune_must_match_selected_listing`

**Purpose:** Regression invariant: document details commune must match selected listing. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_document_details_commune_must_match_selected_listing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuDiscoveryError, match="match")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_patch_json_responses` | `tests.unit.test_gpu_fr._patch_json_responses` |
| `_listing_item` | `tests.unit.test_gpu_fr._listing_item` |
| `_details` | `tests.unit.test_gpu_fr._details` |
| `_files` | `tests.unit.test_gpu_fr._files` |
| `pytest.raises` | `pytest.raises` |
| `discover_current_gpu_document` | `landscout.sources.gpu_fr.discover_current_gpu_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_discovery_rejects_unsafe_archive_name`

**Purpose:** Regression invariant: discovery rejects unsafe archive name. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_discovery_rejects_unsafe_archive_name(
    monkeypatch: pytest.MonkeyPatch,
    archive_name: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "archive_name",
    _UNSAFE_ARCHIVE_NAMES,
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `archive_name` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuDiscoveryError, match="archive name\|safe")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_patch_json_responses` | `tests.unit.test_gpu_fr._patch_json_responses` |
| `_listing_item` | `tests.unit.test_gpu_fr._listing_item` |
| `_details` | `tests.unit.test_gpu_fr._details` |
| `_files` | `tests.unit.test_gpu_fr._files` |
| `pytest.raises` | `pytest.raises` |
| `discover_current_gpu_document` | `landscout.sources.gpu_fr.discover_current_gpu_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_successful_download_persists_sha_and_sidecar`

**Purpose:** Regression invariant: successful download persists sha and sidecar. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_successful_download_persists_sha_and_sidecar(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.path.is_file()`
  - `assert result.file_size > 0`
  - `assert len(result.sha256) == 64`
  - `assert sidecar["sha256"] == result.sha256`
  - `assert sidecar["document"]["document_id"] == "doc-1"`
  - `assert not list(tmp_path.glob("*.part"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_gpu_fr._download` |
| `json.loads` | `json.loads` |
| `(tmp_path / f"{result.filename}.metadata.json").read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `tmp_path.glob` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `(tmp_path / f"{result.filename}.metadata.json").read_text`<br>`result.path.is_file`<br>`tmp_path.glob` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_download_rejects_document_inconsistent_with_config`

**Purpose:** Regression invariant: download rejects document inconsistent with config. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_download_rejects_document_inconsistent_with_config(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    different_value: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "different_value"),
    [
        ("provider", "OTHER PROVIDER"),
        ("portal", "OTHER PORTAL"),
        ("commune_code", "99999"),
        ("partition", "DU_99999"),
        ("status", "document.deleted"),
        ("legal_status", "CANCELLED"),
        ("effective_status", "ANNULE"),
        ("source_url", "https://example.test/not-the-gpu.zip"),
        (
            "source_url",
            (
                "https://www.geoportail-urbanisme.gouv.fr/api/document/"
                "download-by-partition/DU_99999"
            ),
        ),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `field` | positional-or-keyword | `str` | `required` |
| `different_value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuDownloadError, match="document\|identity\|config")`
- Exact assertions:
  - `assert not any(tmp_path.iterdir())`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `replace` | `dataclasses.replace` |
| `_document` | `tests.unit.test_gpu_fr._document` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `download_gpu_document` | `landscout.sources.gpu_fr.download_gpu_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `tmp_path.iterdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `tmp_path.iterdir` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_download_rejects_forged_written_file_provenance_before_network`

**Purpose:** Regression invariant: download rejects forged written file provenance before network. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_download_rejects_forged_written_file_provenance_before_network(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("mutation", ["forged-source-url", "wrong-item-type"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `mutation` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuDownloadError, match="written\|document\|source\|URL")`
- Exact assertions:
  - `assert network_calls == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_document` | `tests.unit.test_gpu_fr._document` |
| `replace` | `dataclasses.replace` |
| `object` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `download_gpu_document` | `landscout.sources.gpu_fr.download_gpu_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_download_rejects_forged_written_file_provenance_before_network.fail_network`

**Purpose:** Implements `fail network` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def fail_network(*args: object, **kwargs: object) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `AssertionError("forged written-file provenance reached network")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |

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
def fail_network(*args: object, **kwargs: object) -> object:
        nonlocal network_calls
        network_calls += 1
        raise AssertionError("forged written-file provenance reached network")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_download_rejects_forged_unsafe_archive_name_before_io`

**Purpose:** Regression invariant: download rejects forged unsafe archive name before io. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_download_rejects_forged_unsafe_archive_name_before_io(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    archive_name: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "archive_name",
    _UNSAFE_ARCHIVE_NAMES,
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `archive_name` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuDownloadError, match="archive name\|archive filename\|safe")`
- Exact assertions:
  - `assert not (tmp_path / "escape.zip").exists()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `replace` | `dataclasses.replace` |
| `_document` | `tests.unit.test_gpu_fr._document` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `download_gpu_document` | `landscout.sources.gpu_fr.download_gpu_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |
| `(tmp_path / "escape.zip").exists` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `(tmp_path / "escape.zip").exists` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_archive_name_with_one_zip_suffix_is_not_duplicated`

**Purpose:** Regression invariant: archive name with one zip suffix is not duplicated. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_archive_name_with_one_zip_suffix_is_not_duplicated(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.filename == "safe-name.zip"`
  - `assert result.path == tmp_path / "safe-name.zip"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `replace` | `dataclasses.replace` |
| `_document` | `tests.unit.test_gpu_fr._document` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `download_gpu_document` | `landscout.sources.gpu_fr.download_gpu_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_fresh_cache_is_reused`

**Purpose:** Regression invariant: fresh cache is reused. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_fresh_cache_is_reused(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert second.cache_hit`
  - `assert second.sha256 == first.sha256`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_gpu_fr._download` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `download_gpu_document` | `landscout.sources.gpu_fr.download_gpu_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |

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
def test_fresh_cache_is_reused(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    first = _download(tmp_path, monkeypatch)
    monkeypatch.setattr(
        gpu, "open_safe_https", lambda *args, **kwargs: pytest.fail("network used")
    )
    second = download_gpu_document(first.document, _config(), tmp_path)
    assert second.cache_hit
    assert second.sha256 == first.sha256
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_boolean_cache_integrity_counts_are_not_accepted_as_integers`

**Purpose:** Regression invariant: boolean cache integrity counts are not accepted as integers. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_boolean_cache_integrity_counts_are_not_accepted_as_integers(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("field", ["file_size", "member_count"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `field` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert (<br>        gpu._load_cached_archive(<br>            first.path,<br>            metadata_path,<br>            first.document,<br>            max_age_hours=168,<br>        )<br>        is None<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_gpu_fr._download` |
| `json.loads` | `json.loads` |
| `metadata_path.read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpu._load_cached_archive` | `landscout.sources.gpu_fr._load_cached_archive` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `metadata_path.read_text` |
| Filesystem/archive write or publication | `metadata_path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `payload["file_size"] = 1`<br>`payload["member_count"] = 1`<br>`payload[field] = True` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_boolean_cache_integrity_counts_are_not_accepted_as_integers(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
) -> None:
    first = _download(tmp_path, monkeypatch)
    metadata_path = tmp_path / f"{first.filename}.metadata.json"
    payload = json.loads(metadata_path.read_text(encoding="utf-8"))
    payload["file_size"] = 1
    payload["member_count"] = 1
    payload[field] = True
    metadata_path.write_text(json.dumps(payload), encoding="utf-8")
    original_stat = Path.stat

    def one_byte_archive_stat(
        path: Path, *args: object, **kwargs: object
    ) -> os.stat_result:
        result = original_stat(path, *args, **kwargs)
        if path != first.path:
            return result
        values = list(result)
        values[6] = 1
        return os.stat_result(values)

    monkeypatch.setattr(Path, "stat", one_byte_archive_stat)
    monkeypatch.setattr(gpu, "validate_gpu_archive", lambda path: ("member",))
    monkeypatch.setattr(gpu, "_sha256", lambda path: first.sha256)

    assert (
        gpu._load_cached_archive(
            first.path,
            metadata_path,
            first.document,
            max_age_hours=168,
        )
        is None
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_boolean_cache_integrity_counts_are_not_accepted_as_integers.one_byte_archive_stat`

**Purpose:** Implements `one byte archive stat` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def one_byte_archive_stat(
        path: Path, *args: object, **kwargs: object
    ) -> os.stat_result:
```

- Exact decorators: none.
- Declared return annotation: `os.stat_result`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
  - `os.stat_result(values)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `original_stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `os.stat_result` | `os.stat_result` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `os.stat_result` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `values[6] = 1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def one_byte_archive_stat(
        path: Path, *args: object, **kwargs: object
    ) -> os.stat_result:
        result = original_stat(path, *args, **kwargs)
        if path != first.path:
            return result
        values = list(result)
        values[6] = 1
        return os.stat_result(values)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_stale_recovery_backup_rejects_cache_before_network`

**Purpose:** Regression invariant: stale recovery backup rejects cache before network. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_stale_recovery_backup_rejects_cache_before_network(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuDownloadError, match="backup\|recovery\|manual")`
- Exact assertions:
  - `assert recovery_path.read_bytes() == recovery_bytes`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_gpu_fr._download` |
| `first.path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `recovery_path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `download_gpu_document` | `landscout.sources.gpu_fr.download_gpu_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |
| `recovery_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `recovery_path.read_bytes` |
| Filesystem/archive write or publication | `recovery_path.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_stale_recovery_backup_rejects_cache_before_network.fail_network`

**Purpose:** Implements `fail network` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def fail_network(*args: object, **kwargs: object) -> _Response:
```

- Exact decorators: none.
- Declared return annotation: `_Response`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.fail` | `pytest.fail` |

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
def fail_network(*args: object, **kwargs: object) -> _Response:
        pytest.fail("stale recovery must fail before network")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_expired_cache_is_refreshed`

**Purpose:** Regression invariant: expired cache is refreshed. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_expired_cache_is_refreshed(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert not refreshed.cache_hit`
  - `assert refreshed.sha256 != first.sha256`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_gpu_fr._download` |
| `json.loads` | `json.loads` |
| `sidecar_path.read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `(datetime.now(UTC) - timedelta(days=8)).isoformat` | `unresolved local/third-party receiver; no ownership inferred` |
| `datetime.now` | `datetime.datetime.now` |
| `timedelta` | `datetime.timedelta` |
| `sidecar_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `_zip_bytes` | `tests.unit.test_gpu_fr._zip_bytes` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `download_gpu_document` | `landscout.sources.gpu_fr.download_gpu_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `sidecar_path.read_text` |
| Filesystem/archive write or publication | `sidecar_path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `sidecar["download_timestamp"] = (datetime.now(UTC) - timedelta(days=8)).isoformat()` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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
    monkeypatch.setattr(
        gpu, "open_safe_https", lambda *args, **kwargs: _Response(fresh_bytes)
    )
    refreshed = download_gpu_document(first.document, _config(), tmp_path)
    assert not refreshed.cache_hit
    assert refreshed.sha256 != first.sha256
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_failed_refresh_preserves_previous_cache`

**Purpose:** Regression invariant: failed refresh preserves previous cache. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_failed_refresh_preserves_previous_cache(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuDownloadError)`
- Exact assertions:
  - `assert first.path.read_bytes() == old_archive`
  - `assert sidecar_path.read_bytes() == old_sidecar`
  - `assert not list(tmp_path.glob("*.part"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_gpu_fr._download` |
| `json.loads` | `json.loads` |
| `sidecar_path.read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `(datetime.now(UTC) - timedelta(days=8)).isoformat` | `unresolved local/third-party receiver; no ownership inferred` |
| `datetime.now` | `datetime.datetime.now` |
| `timedelta` | `datetime.timedelta` |
| `sidecar_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `first.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `sidecar_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `download_gpu_document` | `landscout.sources.gpu_fr.download_gpu_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `tmp_path.glob` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `sidecar_path.read_text`<br>`first.path.read_bytes`<br>`sidecar_path.read_bytes`<br>`tmp_path.glob` |
| Filesystem/archive write or publication | `sidecar_path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `sidecar["download_timestamp"] = (datetime.now(UTC) - timedelta(days=8)).isoformat()` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_failed_refresh_preserves_previous_cache.fail`

**Purpose:** Implements `fail` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def fail(*args: object, **kwargs: object) -> _Response:
```

- Exact decorators: none.
- Declared return annotation: `_Response`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `URLError("offline")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `URLError` | `urllib.error.URLError` |

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
def fail(*args: object, **kwargs: object) -> _Response:
        raise URLError("offline")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_metadata_publication_failure_rolls_back_both_cache_files`

**Purpose:** Regression invariant: metadata publication failure rolls back both cache files. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_metadata_publication_failure_rolls_back_both_cache_files(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuDownloadError)`
- Exact assertions:
  - `assert first.path.read_bytes() == old_archive`
  - `assert sidecar_path.read_bytes() == old_sidecar`
  - `assert not list(tmp_path.glob("*.part"))`
  - `assert not list(tmp_path.glob("*.bak"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_gpu_fr._download` |
| `json.loads` | `json.loads` |
| `sidecar_path.read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `(datetime.now(UTC) - timedelta(days=8)).isoformat` | `unresolved local/third-party receiver; no ownership inferred` |
| `datetime.now` | `datetime.datetime.now` |
| `timedelta` | `datetime.timedelta` |
| `sidecar_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `first.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `sidecar_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `download_gpu_document` | `landscout.sources.gpu_fr.download_gpu_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `tmp_path.glob` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `sidecar_path.read_text`<br>`first.path.read_bytes`<br>`sidecar_path.read_bytes`<br>`tmp_path.glob` |
| Filesystem/archive write or publication | `sidecar_path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `sidecar["download_timestamp"] = (datetime.now(UTC) - timedelta(days=8)).isoformat()` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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
        gpu,
        "open_safe_https",
        lambda *args, **kwargs: _Response(_zip_bytes({"fresh": b"x"})),
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_metadata_publication_failure_rolls_back_both_cache_files.fail_new_metadata_once`

**Purpose:** Implements `fail new metadata once` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def fail_new_metadata_once(source: Path, target: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `Path` | `required` |
| `target` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `OSError("simulated metadata lock")` under lexical guard `source.suffix == ".part" and target == sidecar_path and not failed`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `OSError` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_replace` | `unresolved local/third-party receiver; no ownership inferred` |

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
def fail_new_metadata_once(source: Path, target: Path) -> None:
        nonlocal failed
        if source.suffix == ".part" and target == sidecar_path and not failed:
            failed = True
            raise OSError("simulated metadata lock")
        original_replace(source, target)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_publication_and_rollback_failure_preserves_exact_recovery_backups`

**Purpose:** Regression invariant: publication and rollback failure preserves exact recovery backups. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_publication_and_rollback_failure_preserves_exact_recovery_backups(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuDownloadError, match="rollback")`
- Exact assertions:
  - `assert archive_backup.read_bytes() == old_archive`
  - `assert metadata_backup.read_bytes() == old_metadata`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `archive_path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `temporary_archive.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `temporary_metadata.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `archive_path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `gpu._publish_cache_pair` | `landscout.sources.gpu_fr._publish_cache_pair` |
| `archive_backup.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_backup.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `archive_backup.read_bytes`<br>`metadata_backup.read_bytes` |
| Filesystem/archive write or publication | `archive_path.write_bytes`<br>`metadata_path.write_bytes`<br>`temporary_archive.write_bytes`<br>`temporary_metadata.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_publication_and_rollback_failure_preserves_exact_recovery_backups.fail_publication_and_rollback`

**Purpose:** Implements `fail publication and rollback` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def fail_publication_and_rollback(source: Path, target: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `Path` | `required` |
| `target` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `OSError("simulated metadata publication failure")` under lexical guard `source == temporary_metadata and target == metadata_path`.
  - `OSError("simulated archive rollback failure")` under lexical guard `source == archive_backup and target == archive_path`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `OSError` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_replace` | `unresolved local/third-party receiver; no ownership inferred` |

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
def fail_publication_and_rollback(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        if source == archive_backup and target == archive_path:
            raise OSError("simulated archive rollback failure")
        original_replace(source, target)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_cleanup_failure_does_not_mask_double_failure_recovery_error`

**Purpose:** Regression invariant: cleanup failure does not mask double failure recovery error. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_cleanup_failure_does_not_mask_double_failure_recovery_error(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuDownloadError, match="rollback")`
- Exact assertions:
  - `assert archive_backup.read_bytes() == old_archive`
  - `assert metadata_backup.read_bytes() == old_metadata`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_gpu_fr._download` |
| `json.loads` | `json.loads` |
| `metadata_path.read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `(datetime.now(UTC) - timedelta(days=8)).isoformat` | `unresolved local/third-party receiver; no ownership inferred` |
| `datetime.now` | `datetime.datetime.now` |
| `timedelta` | `datetime.timedelta` |
| `metadata_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `first.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `first.path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `download_gpu_document` | `landscout.sources.gpu_fr.download_gpu_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |
| `archive_backup.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_backup.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `metadata_path.read_text`<br>`first.path.read_bytes`<br>`metadata_path.read_bytes`<br>`archive_backup.read_bytes`<br>`metadata_backup.read_bytes` |
| Filesystem/archive write or publication | `metadata_path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `metadata["download_timestamp"] = (datetime.now(UTC) - timedelta(days=8)).isoformat()` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_cleanup_failure_does_not_mask_double_failure_recovery_error(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    first = _download(tmp_path, monkeypatch)
    metadata_path = tmp_path / f"{first.filename}.metadata.json"
    metadata = json.loads(metadata_path.read_text())
    metadata["download_timestamp"] = (datetime.now(UTC) - timedelta(days=8)).isoformat()
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_cleanup_failure_does_not_mask_double_failure_recovery_error.fail_publication_and_rollback`

**Purpose:** Implements `fail publication and rollback` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def fail_publication_and_rollback(source: Path, target: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `Path` | `required` |
| `target` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `OSError("simulated metadata publication failure")` under lexical guard `source == temporary_metadata and target == metadata_path`.
  - `OSError("simulated archive rollback failure")` under lexical guard `source == archive_backup and target == first.path`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `OSError` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_replace` | `unresolved local/third-party receiver; no ownership inferred` |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_cleanup_failure_does_not_mask_double_failure_recovery_error.fail_temporary_cleanup`

**Purpose:** Implements `fail temporary cleanup` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def fail_temporary_cleanup(path: Path, *, missing_ok: bool = False) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |
| `missing_ok` | keyword-only | `bool` | `False` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `PermissionError("simulated temporary cleanup failure")` under lexical guard `rollback_failed and path == temporary_metadata`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `PermissionError` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_unlink` | `unresolved local/third-party receiver; no ownership inferred` |

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
def fail_temporary_cleanup(path: Path, *, missing_ok: bool = False) -> None:
        if rollback_failed and path == temporary_metadata:
            raise PermissionError("simulated temporary cleanup failure")
        original_unlink(path, missing_ok=missing_ok)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_stale_cache_recovery_backup_fails_closed_without_destroying_it`

**Purpose:** Regression invariant: stale cache recovery backup fails closed without destroying it. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_stale_cache_recovery_backup_fails_closed_without_destroying_it(
    tmp_path: Path,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuDownloadError, match="backup\|recovery\|manual")`
- Exact assertions:
  - `assert archive_path.read_bytes() == b"old archive"`
  - `assert metadata_path.read_bytes() == b"old metadata"`
  - `assert archive_backup.read_bytes() == b"manual recovery archive"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `archive_path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `temporary_archive.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `temporary_metadata.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `archive_backup.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `gpu._publish_cache_pair` | `landscout.sources.gpu_fr._publish_cache_pair` |
| `archive_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `archive_backup.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `archive_path.read_bytes`<br>`metadata_path.read_bytes`<br>`archive_backup.read_bytes` |
| Filesystem/archive write or publication | `archive_path.write_bytes`<br>`metadata_path.write_bytes`<br>`temporary_archive.write_bytes`<br>`temporary_metadata.write_bytes`<br>`archive_backup.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_preexisting_temporary_archive_symlink_cannot_modify_target`

**Purpose:** Regression invariant: preexisting temporary archive symlink cannot modify target. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_preexisting_temporary_archive_symlink_cannot_modify_target(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuDownloadError)`
- Exact assertions:
  - `assert opener_calls == 0`
  - `assert sentinel.read_bytes() == sentinel_bytes`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_document` | `tests.unit.test_gpu_fr._document` |
| `gpu._safe_gpu_archive_filename` | `landscout.sources.gpu_fr._safe_gpu_archive_filename` |
| `sentinel.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `download_gpu_document` | `landscout.sources.gpu_fr.download_gpu_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |
| `sentinel.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `sentinel.read_bytes` |
| Filesystem/archive write or publication | `sentinel.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

    def simulated_symlink_open(path: Path, *args: object, **kwargs: object) -> object:
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_preexisting_temporary_archive_symlink_cannot_modify_target.simulated_is_symlink`

**Purpose:** Implements `simulated is symlink` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def simulated_is_symlink(path: Path) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `path == temporary_archive or original_is_symlink(path)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `original_is_symlink` | `unresolved local/third-party receiver; no ownership inferred` |

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
def simulated_is_symlink(path: Path) -> bool:
        return path == temporary_archive or original_is_symlink(path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_preexisting_temporary_archive_symlink_cannot_modify_target.simulated_symlink_open`

**Purpose:** Implements `simulated symlink open` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def simulated_symlink_open(path: Path, *args: object, **kwargs: object) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `original_open(sentinel, *args, **kwargs)`
  - `original_open(path, *args, **kwargs)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `original_open` | `unresolved local/third-party receiver; no ownership inferred` |

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
def simulated_symlink_open(path: Path, *args: object, **kwargs: object) -> object:
        if path == temporary_archive:
            return original_open(sentinel, *args, **kwargs)
        return original_open(path, *args, **kwargs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_preexisting_temporary_archive_symlink_cannot_modify_target.record_network`

**Purpose:** Implements `record network` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def record_network(*args: object, **kwargs: object) -> _Response:
```

- Exact decorators: none.
- Declared return annotation: `_Response`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `_Response(_zip_bytes())`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_Response` | `tests.unit.test_gpu_fr._Response` |
| `_zip_bytes` | `tests.unit.test_gpu_fr._zip_bytes` |

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
def record_network(*args: object, **kwargs: object) -> _Response:
        nonlocal opener_calls
        opener_calls += 1
        return _Response(_zip_bytes())
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_corrupt_download_is_rejected`

**Purpose:** Regression invariant: corrupt download is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_corrupt_download_is_rejected(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuDownloadError)`
- Exact assertions:
  - `assert not list(tmp_path.glob("*.part"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_document` | `tests.unit.test_gpu_fr._document` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `download_gpu_document` | `landscout.sources.gpu_fr.download_gpu_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `tmp_path.glob` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `tmp_path.glob` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_corrupt_download_is_rejected(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    document = _document(monkeypatch)
    monkeypatch.setattr(
        gpu, "open_safe_https", lambda *args, **kwargs: _Response(b"not zip")
    )
    with pytest.raises(GpuDownloadError):
        download_gpu_document(document, _config(), tmp_path)
    assert not list(tmp_path.glob("*.part"))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_tampered_sidecar_invalidates_cache`

**Purpose:** Regression invariant: tampered sidecar invalidates cache. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_tampered_sidecar_invalidates_cache(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert not download_gpu_document(first.document, _config(), tmp_path).cache_hit`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_gpu_fr._download` |
| `json.loads` | `json.loads` |
| `sidecar_path.read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `sidecar_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `download_gpu_document` | `landscout.sources.gpu_fr.download_gpu_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `sidecar_path.read_text` |
| Filesystem/archive write or publication | `sidecar_path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `sidecar["sha256"] = "0" * 64` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_tampered_sidecar_invalidates_cache(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    first = _download(tmp_path, monkeypatch)
    sidecar_path = tmp_path / f"{first.filename}.metadata.json"
    sidecar = json.loads(sidecar_path.read_text())
    sidecar["sha256"] = "0" * 64
    sidecar_path.write_text(json.dumps(sidecar), encoding="utf-8")
    monkeypatch.setattr(
        gpu, "open_safe_https", lambda *args, **kwargs: _Response(_zip_bytes())
    )
    assert not download_gpu_document(first.document, _config(), tmp_path).cache_hit
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_archive_path_traversal_is_rejected`

**Purpose:** Regression invariant: archive path traversal is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_archive_path_traversal_is_rejected(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuArchiveError, match="Unsafe")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_zip_bytes` | `tests.unit.test_gpu_fr._zip_bytes` |
| `pytest.raises` | `pytest.raises` |
| `validate_gpu_archive` | `landscout.sources.gpu_fr.validate_gpu_archive` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `path.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_archive_path_traversal_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "unsafe.zip"
    path.write_bytes(_zip_bytes({"../escape.txt": b"bad"}))
    with pytest.raises(GpuArchiveError, match="Unsafe"):
        validate_gpu_archive(path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_archive_symlink_is_rejected`

**Purpose:** Regression invariant: archive symlink is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_archive_symlink_is_rejected(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuArchiveError, match="Symbolic")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `zipfile.ZipFile` | `zipfile.ZipFile` |
| `zipfile.ZipInfo` | `zipfile.ZipInfo` |
| `archive.writestr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `validate_gpu_archive` | `landscout.sources.gpu_fr.validate_gpu_archive` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `zipfile.ZipFile`<br>`zipfile.ZipInfo` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `entry.create_system = 3`<br>`entry.external_attr = (0o120777 << 16) \| 0xA000` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_zip_extraction_targets_are_rejected`

**Purpose:** Regression invariant: duplicate zip extraction targets are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_zip_extraction_targets_are_rejected(
    tmp_path: Path,
    members: list[tuple[str, bytes]],
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "members",
    [
        [("duplicate.txt", b"first"), ("duplicate.txt", b"second")],
        [("folder/file.txt", b"first"), (r"folder\file.txt", b"second")],
        [("folder/file.txt", b"first"), ("folder/./file.txt", b"second")],
        [("Folder/File.txt", b"first"), ("folder/file.txt", b"second")],
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `members` | positional-or-keyword | `list[tuple[str, bytes]]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuArchiveError, match="(?i)duplicate\|collid")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_zip_member_bytes` | `tests.unit.test_gpu_fr._zip_member_bytes` |
| `pytest.raises` | `pytest.raises` |
| `validate_gpu_archive` | `landscout.sources.gpu_fr.validate_gpu_archive` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `path.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_zip_file_directory_target_collision_is_rejected`

**Purpose:** Regression invariant: zip file directory target collision is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_zip_file_directory_target_collision_is_rejected(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuArchiveError, match="collision\|target")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_zip_member_bytes` | `tests.unit.test_gpu_fr._zip_member_bytes` |
| `pytest.raises` | `pytest.raises` |
| `validate_gpu_archive` | `landscout.sources.gpu_fr.validate_gpu_archive` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `path.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_zip_file_directory_target_collision_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "collision.zip"
    path.write_bytes(
        _zip_member_bytes([("blocked", b"file"), ("blocked/child.txt", b"child")])
    )

    with pytest.raises(GpuArchiveError, match="collision|target"):
        validate_gpu_archive(path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_zip_cannot_claim_extraction_manifest_path`

**Purpose:** Regression invariant: zip cannot claim extraction manifest path. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_zip_cannot_claim_extraction_manifest_path(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuArchiveError, match="manifest")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_zip_bytes` | `tests.unit.test_gpu_fr._zip_bytes` |
| `pytest.raises` | `pytest.raises` |
| `validate_gpu_archive` | `landscout.sources.gpu_fr.validate_gpu_archive` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `path.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_zip_cannot_claim_extraction_manifest_path(tmp_path: Path) -> None:
    path = tmp_path / "collision.zip"
    path.write_bytes(
        _zip_bytes({f"{gpu.EXTRACTION_MANIFEST_NAME}/child": b"forbidden"})
    )

    with pytest.raises(GpuArchiveError, match="manifest"):
        validate_gpu_archive(path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_inventory_and_cache`

**Purpose:** Regression invariant: extraction inventory and cache. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_extraction_inventory_and_cache(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert [item.relative_path for item in extracted.files] == [<br>        "data/a.txt",<br>        "docs/reglement.pdf",<br>    ]`
  - `assert {item.category for item in extracted.files} == {<br>        "METADATA",<br>        "WRITTEN_REGULATION",<br>    }`
  - `assert extract_gpu_document(first, tmp_path / "cache").cache_hit`
  - `assert manifest["schema_version"] == 2`
  - `assert manifest["archive_sha256"] == first.sha256`
  - `assert manifest["files"] == [<br>        {<br>            "relative_path": item.relative_path,<br>            "size_bytes": item.size_bytes,<br>            "sha256": item.sha256,<br>        }<br>        for item in extracted.files<br>    ]`
  - `assert not list((tmp_path / "cache" / "x").glob("*.part"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_gpu_fr._download` |
| `_zip_bytes` | `tests.unit.test_gpu_fr._zip_bytes` |
| `extract_gpu_document` | `landscout.sources.gpu_fr.extract_gpu_document` |
| `json.loads` | `json.loads` |
| `(extracted.extraction_root / gpu.EXTRACTION_MANIFEST_NAME).read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `(tmp_path / "cache" / "x").glob` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `(extracted.extraction_root / gpu.EXTRACTION_MANIFEST_NAME).read_text`<br>`(tmp_path / "cache" / "x").glob` |
| Filesystem/archive write or publication | `(extracted.extraction_root / gpu.EXTRACTION_MANIFEST_NAME).read_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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
        (extracted.extraction_root / gpu.EXTRACTION_MANIFEST_NAME).read_text(
            encoding="utf-8"
        )
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_manifest_is_created_exclusively`

**Purpose:** Regression invariant: extraction manifest is created exclusively. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_extraction_manifest_is_created_exclusively(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert manifest_modes == ["x", "rb"]`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_gpu_fr._download` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `extract_gpu_document` | `landscout.sources.gpu_fr.extract_gpu_document` |

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
def test_extraction_manifest_is_created_exclusively(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    download = _download(tmp_path / "cache", monkeypatch)
    original_open = Path.open
    manifest_modes: list[str] = []

    def observed_open(
        path: Path,
        mode: str = "r",
        *args: object,
        **kwargs: object,
    ) -> object:
        if path.name == gpu.EXTRACTION_MANIFEST_NAME:
            manifest_modes.append(mode)
        return original_open(path, mode, *args, **kwargs)

    monkeypatch.setattr(Path, "open", observed_open)

    extract_gpu_document(download, tmp_path / "cache")

    assert manifest_modes == ["x", "rb"]
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_manifest_is_created_exclusively.observed_open`

**Purpose:** Implements `observed open` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def observed_open(
        path: Path,
        mode: str = "r",
        *args: object,
        **kwargs: object,
    ) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |
| `mode` | positional-or-keyword | `str` | `'r'` |
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `original_open(path, mode, *args, **kwargs)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `manifest_modes.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_open` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `manifest_modes.append(mode)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def observed_open(
        path: Path,
        mode: str = "r",
        *args: object,
        **kwargs: object,
    ) -> object:
        if path.name == gpu.EXTRACTION_MANIFEST_NAME:
            manifest_modes.append(mode)
        return original_open(path, mode, *args, **kwargs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_stale_extraction_backup_fails_closed_and_is_preserved`

**Purpose:** Regression invariant: stale extraction backup fails closed and is preserved. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_stale_extraction_backup_fails_closed_and_is_preserved(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuArchiveError, match="backup\|recovery\|manual")`
- Exact assertions:
  - `assert sentinel.read_bytes() == b"preserve"`
  - `assert extracted.extraction_root.is_dir()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_gpu_fr._download` |
| `extract_gpu_document` | `landscout.sources.gpu_fr.extract_gpu_document` |
| `extracted.extraction_root.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `backup.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `sentinel.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `sentinel.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `extracted.extraction_root.is_dir` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `sentinel.read_bytes`<br>`extracted.extraction_root.is_dir` |
| Filesystem/archive write or publication | `extracted.extraction_root.with_name`<br>`backup.mkdir`<br>`sentinel.write_bytes`<br>`extracted.extraction_root.is_dir` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_stale_extraction_backup_fails_closed_and_is_preserved(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    download = _download(tmp_path / "cache", monkeypatch)
    extracted = extract_gpu_document(download, tmp_path / "cache")
    backup = extracted.extraction_root.with_name(
        f"{extracted.extraction_root.name}.bak"
    )
    backup.mkdir()
    sentinel = backup / "manual-recovery.txt"
    sentinel.write_bytes(b"preserve")

    with pytest.raises(GpuArchiveError, match="backup|recovery|manual"):
        extract_gpu_document(download, tmp_path / "cache")

    assert sentinel.read_bytes() == b"preserve"
    assert extracted.extraction_root.is_dir()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_publication_and_rollback_failure_preserves_backup`

**Purpose:** Regression invariant: extraction publication and rollback failure preserves backup. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_extraction_publication_and_rollback_failure_preserves_backup(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuArchiveError, match="rollback")`
  - `pytest.raises(GpuArchiveError, match="backup\|recovery\|manual")`
- Exact assertions:
  - `assert (backup / sentinel.name).read_bytes() == b"preserve"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_gpu_fr._download` |
| `extract_gpu_document` | `landscout.sources.gpu_fr.extract_gpu_document` |
| `sentinel.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `extracted.extraction_root.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `(backup / sentinel.name).read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `(backup / sentinel.name).read_bytes` |
| Filesystem/archive write or publication | `sentinel.write_bytes`<br>`extracted.extraction_root.with_name` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_extraction_publication_and_rollback_failure_preserves_backup(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    download = _download(tmp_path / "cache", monkeypatch)
    extracted = extract_gpu_document(download, tmp_path / "cache")
    sentinel = extracted.extraction_root / "manual-recovery.txt"
    sentinel.write_bytes(b"preserve")
    backup = extracted.extraction_root.with_name(
        f"{extracted.extraction_root.name}.bak"
    )
    temporary = extracted.extraction_root.with_name(
        f"{extracted.extraction_root.name}.part"
    )
    original_move = shutil.move

    def fail_publication_and_rollback(source: str, target: str) -> object:
        source_path = Path(source)
        target_path = Path(target)
        if source_path == temporary and target_path == extracted.extraction_root:
            raise OSError("simulated extraction publication failure")
        if source_path == backup and target_path == extracted.extraction_root:
            raise OSError("simulated extraction rollback failure")
        return original_move(source, target)

    monkeypatch.setattr(shutil, "move", fail_publication_and_rollback)

    with pytest.raises(GpuArchiveError, match="rollback"):
        extract_gpu_document(download, tmp_path / "cache")

    assert (backup / sentinel.name).read_bytes() == b"preserve"
    with pytest.raises(GpuArchiveError, match="backup|recovery|manual"):
        extract_gpu_document(download, tmp_path / "cache")
    assert (backup / sentinel.name).read_bytes() == b"preserve"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_publication_and_rollback_failure_preserves_backup.fail_publication_and_rollback`

**Purpose:** Implements `fail publication and rollback` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def fail_publication_and_rollback(source: str, target: str) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `str` | `required` |
| `target` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `original_move(source, target)`
- Explicit raise paths:
  - `OSError("simulated extraction publication failure")` under lexical guard `source_path == temporary and target_path == extracted.extraction_root`.
  - `OSError("simulated extraction rollback failure")` under lexical guard `source_path == backup and target_path == extracted.extraction_root`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Path` | `pathlib.Path` |
| `OSError` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_move` | `unresolved local/third-party receiver; no ownership inferred` |

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
def fail_publication_and_rollback(source: str, target: str) -> object:
        source_path = Path(source)
        target_path = Path(target)
        if source_path == temporary and target_path == extracted.extraction_root:
            raise OSError("simulated extraction publication failure")
        if source_path == backup and target_path == extracted.extraction_root:
            raise OSError("simulated extraction rollback failure")
        return original_move(source, target)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_publication_failure_restores_existing_root`

**Purpose:** Regression invariant: extraction publication failure restores existing root. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_extraction_publication_failure_restores_existing_root(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuArchiveError, match="publication")`
- Exact assertions:
  - `assert sentinel.read_bytes() == b"restore-me"`
  - `assert not backup.exists()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_gpu_fr._download` |
| `extract_gpu_document` | `landscout.sources.gpu_fr.extract_gpu_document` |
| `sentinel.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `extracted.extraction_root.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `sentinel.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `backup.exists` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `sentinel.read_bytes`<br>`backup.exists` |
| Filesystem/archive write or publication | `sentinel.write_bytes`<br>`extracted.extraction_root.with_name` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_extraction_publication_failure_restores_existing_root(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    download = _download(tmp_path / "cache", monkeypatch)
    extracted = extract_gpu_document(download, tmp_path / "cache")
    sentinel = extracted.extraction_root / "rollback-source.txt"
    sentinel.write_bytes(b"restore-me")
    temporary = extracted.extraction_root.with_name(
        f"{extracted.extraction_root.name}.part"
    )
    backup = extracted.extraction_root.with_name(
        f"{extracted.extraction_root.name}.bak"
    )
    original_move = shutil.move

    def fail_publication(source: str, target: str) -> object:
        if Path(source) == temporary and Path(target) == extracted.extraction_root:
            raise OSError("simulated extraction publication failure")
        return original_move(source, target)

    monkeypatch.setattr(shutil, "move", fail_publication)

    with pytest.raises(GpuArchiveError, match="publication"):
        extract_gpu_document(download, tmp_path / "cache")

    assert sentinel.read_bytes() == b"restore-me"
    assert not backup.exists()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_publication_failure_restores_existing_root.fail_publication`

**Purpose:** Implements `fail publication` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def fail_publication(source: str, target: str) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `str` | `required` |
| `target` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `original_move(source, target)`
- Explicit raise paths:
  - `OSError("simulated extraction publication failure")` under lexical guard `Path(source) == temporary and Path(target) == extracted.extraction_root`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Path` | `pathlib.Path` |
| `OSError` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_move` | `unresolved local/third-party receiver; no ownership inferred` |

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
def fail_publication(source: str, target: str) -> object:
        if Path(source) == temporary and Path(target) == extracted.extraction_root:
            raise OSError("simulated extraction publication failure")
        return original_move(source, target)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_backup_move_failure_preserves_existing_root`

**Purpose:** Regression invariant: extraction backup move failure preserves existing root. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_extraction_backup_move_failure_preserves_existing_root(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuArchiveError, match="backup.*failed")`
- Exact assertions:
  - `assert sentinel.read_bytes() == b"preserve-existing-root"`
  - `assert not backup.exists()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_gpu_fr._download` |
| `extract_gpu_document` | `landscout.sources.gpu_fr.extract_gpu_document` |
| `sentinel.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `extracted.extraction_root.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `sentinel.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `backup.exists` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `sentinel.read_bytes`<br>`backup.exists` |
| Filesystem/archive write or publication | `sentinel.write_bytes`<br>`extracted.extraction_root.with_name` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_extraction_backup_move_failure_preserves_existing_root(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    download = _download(tmp_path / "cache", monkeypatch)
    extracted = extract_gpu_document(download, tmp_path / "cache")
    sentinel = extracted.extraction_root / "manual-recovery.txt"
    sentinel.write_bytes(b"preserve-existing-root")
    backup = extracted.extraction_root.with_name(
        f"{extracted.extraction_root.name}.bak"
    )
    original_move = shutil.move

    def fail_initial_backup(source: str, target: str) -> object:
        if Path(source) == extracted.extraction_root and Path(target) == backup:
            raise OSError("simulated initial backup failure")
        return original_move(source, target)

    monkeypatch.setattr(shutil, "move", fail_initial_backup)

    with pytest.raises(GpuArchiveError, match="backup.*failed"):
        extract_gpu_document(download, tmp_path / "cache")

    assert sentinel.read_bytes() == b"preserve-existing-root"
    assert not backup.exists()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_backup_move_failure_preserves_existing_root.fail_initial_backup`

**Purpose:** Implements `fail initial backup` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def fail_initial_backup(source: str, target: str) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `str` | `required` |
| `target` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `original_move(source, target)`
- Explicit raise paths:
  - `OSError("simulated initial backup failure")` under lexical guard `Path(source) == extracted.extraction_root and Path(target) == backup`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Path` | `pathlib.Path` |
| `OSError` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_move` | `unresolved local/third-party receiver; no ownership inferred` |

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
def fail_initial_backup(source: str, target: str) -> object:
        if Path(source) == extracted.extraction_root and Path(target) == backup:
            raise OSError("simulated initial backup failure")
        return original_move(source, target)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_inventory_rejects_special_entry`

**Purpose:** Regression invariant: extraction inventory rejects special entry. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_extraction_inventory_rejects_special_entry(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuArchiveError, match="special filesystem entry")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `root.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `special.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `gpu._inventory` | `landscout.sources.gpu_fr._inventory` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `root.mkdir`<br>`special.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_extraction_inventory_rejects_special_entry(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    root = tmp_path / "extraction"
    root.mkdir()
    special = root / "special-entry"
    special.write_bytes(b"source")
    original_is_file = Path.is_file
    original_is_dir = Path.is_dir

    def simulated_is_file(path: Path) -> bool:
        return False if path == special else original_is_file(path)

    def simulated_is_dir(path: Path) -> bool:
        return False if path == special else original_is_dir(path)

    monkeypatch.setattr(Path, "is_file", simulated_is_file)
    monkeypatch.setattr(Path, "is_dir", simulated_is_dir)

    with pytest.raises(GpuArchiveError, match="special filesystem entry"):
        gpu._inventory(root)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_inventory_rejects_special_entry.simulated_is_file`

**Purpose:** Implements `simulated is file` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def simulated_is_file(path: Path) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `False if path == special else original_is_file(path)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `original_is_file` | `unresolved local/third-party receiver; no ownership inferred` |

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
def simulated_is_file(path: Path) -> bool:
        return False if path == special else original_is_file(path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_inventory_rejects_special_entry.simulated_is_dir`

**Purpose:** Implements `simulated is dir` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def simulated_is_dir(path: Path) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `False if path == special else original_is_dir(path)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `original_is_dir` | `unresolved local/third-party receiver; no ownership inferred` |

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
def simulated_is_dir(path: Path) -> bool:
        return False if path == special else original_is_dir(path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_cleanup_preserves_primary_controlled_error`

**Purpose:** Regression invariant: extraction cleanup preserves primary controlled error. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_extraction_cleanup_preserves_primary_controlled_error(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuArchiveError, match="could not be cleaned")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuArchiveError` | `landscout.sources.gpu_fr.GpuArchiveError` |
| `gpu._cleanup_temporary_extraction_directory` | `landscout.sources.gpu_fr._cleanup_temporary_extraction_directory` |
| `pytest.raises` | `pytest.raises` |

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
def test_extraction_cleanup_preserves_primary_controlled_error(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    temporary = tmp_path / "extraction.part"

    def fail_cleanup(path: Path) -> None:
        assert path == temporary
        raise PermissionError("simulated cleanup failure")

    monkeypatch.setattr(gpu, "_remove_extraction_path", fail_cleanup)
    primary = GpuArchiveError("primary extraction failure")

    gpu._cleanup_temporary_extraction_directory(temporary, primary)

    with pytest.raises(GpuArchiveError, match="could not be cleaned"):
        gpu._cleanup_temporary_extraction_directory(temporary, None)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_cleanup_preserves_primary_controlled_error.fail_cleanup`

**Purpose:** Implements `fail cleanup` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def fail_cleanup(path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `PermissionError("simulated cleanup failure")`.
- Exact assertions:
  - `assert path == temporary`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `PermissionError` | `unresolved local/third-party receiver; no ownership inferred` |

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
def fail_cleanup(path: Path) -> None:
        assert path == temporary
        raise PermissionError("simulated cleanup failure")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_temporary_link_is_rejected_without_unlinking_target`

**Purpose:** Regression invariant: extraction temporary link is rejected without unlinking target. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_extraction_temporary_link_is_rejected_without_unlinking_target(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    link_kind: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("link_kind", ["symlink", "junction"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `link_kind` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuArchiveError, match="temporary\|link\|junction")`
- Exact assertions:
  - `assert unlink_calls == 0`
  - `assert rmdir_calls == 0`
  - `assert rmtree_calls == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_gpu_fr._download` |
| `root.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `extract_gpu_document` | `landscout.sources.gpu_fr.extract_gpu_document` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
def test_extraction_temporary_link_is_rejected_without_unlinking_target(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    link_kind: str,
) -> None:
    download = _download(tmp_path / "cache", monkeypatch)
    root = tmp_path / "cache" / "x" / download.sha256[:16]
    temporary = root.with_name(f"{root.name}.part")
    original_is_symlink = Path.is_symlink
    original_is_junction = Path.is_junction
    original_unlink = Path.unlink
    original_rmdir = Path.rmdir
    original_rmtree = shutil.rmtree
    unlink_calls = 0
    rmdir_calls = 0
    rmtree_calls = 0

    def simulated_is_symlink(path: Path) -> bool:
        return (link_kind == "symlink" and path == temporary) or original_is_symlink(
            path
        )

    def simulated_is_junction(path: Path) -> bool:
        return (link_kind == "junction" and path == temporary) or original_is_junction(
            path
        )

    def protected_unlink(path: Path, *args: object, **kwargs: object) -> None:
        nonlocal unlink_calls
        if path == temporary:
            unlink_calls += 1
            raise AssertionError("temporary link was unlinked")
        original_unlink(path, *args, **kwargs)

    def protected_rmdir(path: Path, *args: object, **kwargs: object) -> None:
        nonlocal rmdir_calls
        if path == temporary:
            rmdir_calls += 1
            raise AssertionError("temporary junction was removed")
        original_rmdir(path, *args, **kwargs)

    def protected_rmtree(path: object, *args: object, **kwargs: object) -> None:
        nonlocal rmtree_calls
        if Path(path) == temporary:
            rmtree_calls += 1
            raise AssertionError("temporary link tree was removed")
        original_rmtree(path, *args, **kwargs)

    monkeypatch.setattr(Path, "is_symlink", simulated_is_symlink)
    monkeypatch.setattr(Path, "is_junction", simulated_is_junction)
    monkeypatch.setattr(Path, "unlink", protected_unlink)
    monkeypatch.setattr(Path, "rmdir", protected_rmdir)
    monkeypatch.setattr(shutil, "rmtree", protected_rmtree)

    with pytest.raises(GpuArchiveError, match="temporary|link|junction"):
        extract_gpu_document(download, tmp_path / "cache")

    assert unlink_calls == 0
    assert rmdir_calls == 0
    assert rmtree_calls == 0
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_temporary_link_is_rejected_without_unlinking_target.simulated_is_symlink`

**Purpose:** Implements `simulated is symlink` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def simulated_is_symlink(path: Path) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `(link_kind == "symlink" and path == temporary) or original_is_symlink(<br>            path<br>        )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `original_is_symlink` | `unresolved local/third-party receiver; no ownership inferred` |

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
def simulated_is_symlink(path: Path) -> bool:
        return (link_kind == "symlink" and path == temporary) or original_is_symlink(
            path
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_temporary_link_is_rejected_without_unlinking_target.simulated_is_junction`

**Purpose:** Implements `simulated is junction` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def simulated_is_junction(path: Path) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `(link_kind == "junction" and path == temporary) or original_is_junction(<br>            path<br>        )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `original_is_junction` | `unresolved local/third-party receiver; no ownership inferred` |

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
def simulated_is_junction(path: Path) -> bool:
        return (link_kind == "junction" and path == temporary) or original_is_junction(
            path
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_temporary_link_is_rejected_without_unlinking_target.protected_unlink`

**Purpose:** Implements `protected unlink` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def protected_unlink(path: Path, *args: object, **kwargs: object) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `AssertionError("temporary link was unlinked")` under lexical guard `path == temporary`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_unlink` | `unresolved local/third-party receiver; no ownership inferred` |

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
def protected_unlink(path: Path, *args: object, **kwargs: object) -> None:
        nonlocal unlink_calls
        if path == temporary:
            unlink_calls += 1
            raise AssertionError("temporary link was unlinked")
        original_unlink(path, *args, **kwargs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_temporary_link_is_rejected_without_unlinking_target.protected_rmdir`

**Purpose:** Implements `protected rmdir` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def protected_rmdir(path: Path, *args: object, **kwargs: object) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `AssertionError("temporary junction was removed")` under lexical guard `path == temporary`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_rmdir` | `unresolved local/third-party receiver; no ownership inferred` |

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
def protected_rmdir(path: Path, *args: object, **kwargs: object) -> None:
        nonlocal rmdir_calls
        if path == temporary:
            rmdir_calls += 1
            raise AssertionError("temporary junction was removed")
        original_rmdir(path, *args, **kwargs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_temporary_link_is_rejected_without_unlinking_target.protected_rmtree`

**Purpose:** Implements `protected rmtree` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def protected_rmtree(path: object, *args: object, **kwargs: object) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `object` | `required` |
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `AssertionError("temporary link tree was removed")` under lexical guard `Path(path) == temporary`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Path` | `pathlib.Path` |
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_rmtree` | `unresolved local/third-party receiver; no ownership inferred` |

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
def protected_rmtree(path: object, *args: object, **kwargs: object) -> None:
        nonlocal rmtree_calls
        if Path(path) == temporary:
            rmtree_calls += 1
            raise AssertionError("temporary link tree was removed")
        original_rmtree(path, *args, **kwargs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_stale_extraction_temporary_directory_fails_closed_and_is_preserved`

**Purpose:** Regression invariant: stale extraction temporary directory fails closed and is preserved. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_stale_extraction_temporary_directory_fails_closed_and_is_preserved(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuArchiveError, match="temporary\|manual\|recovery")`
- Exact assertions:
  - `assert sentinel.read_bytes() == b"preserve-stale-temporary"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_gpu_fr._download` |
| `root.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `temporary.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `sentinel.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `extract_gpu_document` | `landscout.sources.gpu_fr.extract_gpu_document` |
| `sentinel.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `sentinel.read_bytes` |
| Filesystem/archive write or publication | `temporary.mkdir`<br>`sentinel.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_stale_extraction_temporary_directory_fails_closed_and_is_preserved(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    download = _download(tmp_path / "cache", monkeypatch)
    root = tmp_path / "cache" / "x" / download.sha256[:16]
    temporary = root.with_name(f"{root.name}.part")
    temporary.mkdir(parents=True)
    sentinel = temporary / "manual-recovery.txt"
    sentinel.write_bytes(b"preserve-stale-temporary")

    with pytest.raises(GpuArchiveError, match="temporary|manual|recovery"):
        extract_gpu_document(download, tmp_path / "cache")

    assert sentinel.read_bytes() == b"preserve-stale-temporary"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_extraction_manifest_key_forces_verified_rebuild`

**Purpose:** Regression invariant: duplicate extraction manifest key forces verified rebuild. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_extraction_manifest_key_forces_verified_rebuild(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert not rebuilt.cache_hit`
  - `assert not rebuilt.extraction_root.with_name(<br>        f"{rebuilt.extraction_root.name}.bak"<br>    ).exists()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_gpu_fr._download` |
| `extract_gpu_document` | `landscout.sources.gpu_fr.extract_gpu_document` |
| `json.loads` | `json.loads` |
| `manifest.read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `manifest.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `rebuilt.extraction_root.with_name(<br>        f"{rebuilt.extraction_root.name}.bak"<br>    ).exists` | `unresolved local/third-party receiver; no ownership inferred` |
| `rebuilt.extraction_root.with_name` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `manifest.read_text`<br>`rebuilt.extraction_root.with_name(<br>        f"{rebuilt.extraction_root.name}.bak"<br>    ).exists` |
| Filesystem/archive write or publication | `manifest.write_text`<br>`rebuilt.extraction_root.with_name(<br>        f"{rebuilt.extraction_root.name}.bak"<br>    ).exists`<br>`rebuilt.extraction_root.with_name` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_duplicate_extraction_manifest_key_forces_verified_rebuild(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    download = _download(tmp_path / "cache", monkeypatch)
    first = extract_gpu_document(download, tmp_path / "cache")
    manifest = first.extraction_root / gpu.EXTRACTION_MANIFEST_NAME
    payload = json.loads(manifest.read_text(encoding="utf-8"))
    manifest.write_text(
        "{"
        f'"schema_version":{payload["schema_version"]},'
        f'"archive_sha256":"{payload["archive_sha256"]}",'
        f'"archive_sha256":"{payload["archive_sha256"]}",'
        f'"files":{json.dumps(payload["files"])}'
        "}",
        encoding="utf-8",
    )

    rebuilt = extract_gpu_document(download, tmp_path / "cache")

    assert not rebuilt.cache_hit
    assert not rebuilt.extraction_root.with_name(
        f"{rebuilt.extraction_root.name}.bak"
    ).exists()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_stale_download_object_rejects_replaced_valid_archive`

**Purpose:** Regression invariant: stale download object rejects replaced valid archive. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_stale_download_object_rejects_replaced_valid_archive(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuArchiveError, match="checksum\|SHA\|stale\|metadata")`
- Exact assertions:
  - `assert len(replacement) == download.file_size`
  - `assert not (tmp_path / "cache" / "x" / download.sha256[:16]).exists()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_gpu_fr._download` |
| `_zip_bytes` | `tests.unit.test_gpu_fr._zip_bytes` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `download.path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `extract_gpu_document` | `landscout.sources.gpu_fr.extract_gpu_document` |
| `(tmp_path / "cache" / "x" / download.sha256[:16]).exists` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `(tmp_path / "cache" / "x" / download.sha256[:16]).exists` |
| Filesystem/archive write or publication | `download.path.write_bytes` |
| Hashing/byte identity | `(tmp_path / "cache" / "x" / download.sha256[:16]).exists` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_rejects_archive_object_inconsistent_with_path`

**Purpose:** Regression invariant: extraction rejects archive object inconsistent with path. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_extraction_rejects_archive_object_inconsistent_with_path(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "value"),
    [
        ("sha256", "0" * 64),
        ("file_size", 1),
        ("filename", "other.zip"),
        ("archive_format", "7z"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `field` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuArchiveError, match="archive\|metadata\|checksum\|size")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_gpu_fr._download` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `extract_gpu_document` | `landscout.sources.gpu_fr.extract_gpu_document` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_tampered_extraction_is_rebuilt_from_verified_archive`

**Purpose:** Regression invariant: tampered extraction is rebuilt from verified archive. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_tampered_extraction_is_rebuilt_from_verified_archive(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("mutation", ["content", "deleted", "added", "path"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `mutation` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert not refreshed.cache_hit`
  - `assert (refreshed.extraction_root / "data" / "value.txt").read_bytes() == b"source"`
  - `assert not (refreshed.extraction_root / "data" / "renamed.txt").exists()`
  - `assert not (refreshed.extraction_root / "unexpected.txt").exists()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_gpu_fr._download` |
| `_zip_bytes` | `tests.unit.test_gpu_fr._zip_bytes` |
| `extract_gpu_document` | `landscout.sources.gpu_fr.extract_gpu_document` |
| `original.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `original.unlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `(first.extraction_root / "unexpected.txt").write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `original.rename` | `unresolved local/third-party receiver; no ownership inferred` |
| `original.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `(refreshed.extraction_root / "data" / "value.txt").read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `(refreshed.extraction_root / "data" / "renamed.txt").exists` | `unresolved local/third-party receiver; no ownership inferred` |
| `(refreshed.extraction_root / "unexpected.txt").exists` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `(refreshed.extraction_root / "data" / "value.txt").read_bytes`<br>`(refreshed.extraction_root / "data" / "renamed.txt").exists`<br>`(refreshed.extraction_root / "unexpected.txt").exists` |
| Filesystem/archive write or publication | `original.write_bytes`<br>`original.unlink`<br>`(first.extraction_root / "unexpected.txt").write_bytes`<br>`(refreshed.extraction_root / "data" / "value.txt").read_bytes`<br>`(refreshed.extraction_root / "data" / "renamed.txt").exists`<br>`(refreshed.extraction_root / "unexpected.txt").exists` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `original.rename(original.with_name("renamed.txt"))` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_extraction_from_archive`

**Purpose:** Implements `extraction from archive` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def _extraction_from_archive(path: Path, tmp_path: Path) -> GpuExtraction:
```

- Exact decorators: none.
- Declared return annotation: `GpuExtraction`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `extract_gpu_document(download, tmp_path / "cache")`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_gpu_fr::test_spatial_inventory_and_inspection_preserve_source_quality` via `_extraction_from_archive`
- value/type reference: `tests.unit.test_gpu_fr::test_spatial_inventory_and_inspection_preserve_source_quality` via `_extraction_from_archive`
- direct call: `tests.unit.test_gpu_fr::test_missing_zoning_layer_fails_clearly` via `_extraction_from_archive`
- value/type reference: `tests.unit.test_gpu_fr::test_missing_zoning_layer_fails_clearly` via `_extraction_from_archive`
- direct call: `tests.unit.test_gpu_fr::test_ambiguous_zoning_layer_fails_clearly` via `_extraction_from_archive`
- value/type reference: `tests.unit.test_gpu_fr::test_ambiguous_zoning_layer_fails_clearly` via `_extraction_from_archive`
- direct call: `tests.unit.test_gpu_fr::test_inspection_rejects_one_physical_layer_for_two_logical_roles` via `_extraction_from_archive`
- value/type reference: `tests.unit.test_gpu_fr::test_inspection_rejects_one_physical_layer_for_two_logical_roles` via `_extraction_from_archive`
- direct call: `tests.unit.test_gpu_fr::test_inspection_rejects_mutated_config_before_layer_discovery` via `_extraction_from_archive`
- value/type reference: `tests.unit.test_gpu_fr::test_inspection_rejects_mutated_config_before_layer_discovery` via `_extraction_from_archive`
- direct call: `tests.unit.test_gpu_fr::test_inspection_rejects_archive_byte_mutation_before_layer_discovery` via `_extraction_from_archive`
- value/type reference: `tests.unit.test_gpu_fr::test_inspection_rejects_archive_byte_mutation_before_layer_discovery` via `_extraction_from_archive`
- direct call: `tests.unit.test_gpu_fr::test_inspection_rejects_document_lineage_not_matching_config` via `_extraction_from_archive`
- value/type reference: `tests.unit.test_gpu_fr::test_inspection_rejects_document_lineage_not_matching_config` via `_extraction_from_archive`
- direct call: `tests.unit.test_gpu_fr::test_planning_document_records_and_revalidates_exact_config_identity` via `_extraction_from_archive`
- value/type reference: `tests.unit.test_gpu_fr::test_planning_document_records_and_revalidates_exact_config_identity` via `_extraction_from_archive`
- direct call: `tests.unit.test_gpu_fr::test_source_complete_revalidation_rejects_coordinated_spatial_omission` via `_extraction_from_archive`
- value/type reference: `tests.unit.test_gpu_fr::test_source_complete_revalidation_rejects_coordinated_spatial_omission` via `_extraction_from_archive`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_config` | `tests.unit.test_gpu_fr._config` |
| `gpu.GpuDocumentMetadata` | `landscout.sources.gpu_fr.GpuDocumentMetadata` |
| `build_gpu_partition_download_url` | `landscout.sources.gpu_fr.build_gpu_partition_download_url` |
| `GpuArchiveDownload` | `landscout.sources.gpu_fr.GpuArchiveDownload` |
| `datetime.now(UTC).isoformat` | `unresolved local/third-party receiver; no ownership inferred` |
| `datetime.now` | `datetime.datetime.now` |
| `path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpu._sha256` | `landscout.sources.gpu_fr._sha256` |
| `extract_gpu_document` | `landscout.sources.gpu_fr.extract_gpu_document` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.stat` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `gpu._sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _extraction_from_archive(path: Path, tmp_path: Path) -> GpuExtraction:
    config = _config()
    document = gpu.GpuDocumentMetadata(
        provider=config.provider,
        portal=config.portal,
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
        source_url=build_gpu_partition_download_url(config),
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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_spatial_inventory_and_inspection_preserve_source_quality`

**Purpose:** Regression invariant: spatial inventory and inspection preserve source quality. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_spatial_inventory_and_inspection_preserve_source_quality(
    tmp_path: Path,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert [item.source_layer for item in references] == [<br>        "prescription_surf",<br>        "zone_urba",<br>    ]`
  - `assert result.zoning.reference.source_layer == "zone_urba"`
  - `assert result.zoning.summary.crs == "EPSG:2154"`
  - `assert result.zoning.summary.feature_count == 3`
  - `assert result.zoning.summary.null_geometry_count == 1`
  - `assert result.zoning.summary.invalid_geometry_count == 1`
  - `assert not result.zoning.data.geometry.iloc[1].is_valid`
  - `assert result.related_layers[0].logical_name == "prescription_surface"`
  - `assert extraction.standard_models == ("CNIG PLU v2017",)`
  - `assert [item.relative_path for item in extraction.files] == sorted(<br>        item.relative_path for item in extraction.files<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_extraction_from_archive` | `tests.unit.test_gpu_fr._extraction_from_archive` |
| `_planning_archive` | `tests.unit.test_gpu_fr._planning_archive` |
| `discover_gpu_spatial_layers` | `landscout.sources.gpu_fr.discover_gpu_spatial_layers` |
| `inspect_gpu_planning_document` | `landscout.sources.gpu_fr.inspect_gpu_planning_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |
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
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_spatial_inventory_and_inspection_preserve_source_quality(
    tmp_path: Path,
) -> None:
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_zoning_layer_fails_clearly`

**Purpose:** Regression invariant: missing zoning layer fails clearly. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_missing_zoning_layer_fails_clearly(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuSpatialInspectionError, match="zoning")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_planning_archive` | `tests.unit.test_gpu_fr._planning_archive` |
| `_extraction_from_archive` | `tests.unit.test_gpu_fr._extraction_from_archive` |
| `_config().model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `_config` | `tests.unit.test_gpu_fr._config` |
| `pytest.raises` | `pytest.raises` |
| `inspect_gpu_planning_document` | `landscout.sources.gpu_fr.inspect_gpu_planning_document` |
| `GpuSourceConfig.model_validate` | `landscout.sources.gpu_fr.GpuSourceConfig.model_validate` |

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
| In-memory mutation | `payload["spatial_layers"]["zoning"]["match_tokens"] = ["missing"]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_ambiguous_zoning_layer_fails_clearly`

**Purpose:** Regression invariant: ambiguous zoning layer fails clearly. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_ambiguous_zoning_layer_fails_clearly(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuSpatialInspectionError, match="found 2")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_extraction_from_archive` | `tests.unit.test_gpu_fr._extraction_from_archive` |
| `_planning_archive` | `tests.unit.test_gpu_fr._planning_archive` |
| `_config().model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `_config` | `tests.unit.test_gpu_fr._config` |
| `pytest.raises` | `pytest.raises` |
| `inspect_gpu_planning_document` | `landscout.sources.gpu_fr.inspect_gpu_planning_document` |
| `GpuSourceConfig.model_validate` | `landscout.sources.gpu_fr.GpuSourceConfig.model_validate` |

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
| In-memory mutation | `payload["spatial_layers"]["zoning"]["match_tokens"] = [<br>        "zone_urba",<br>        "prescription_surf",<br>    ]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_config_with_shared_role_token`

**Purpose:** Implements `config with shared role token` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def _config_with_shared_role_token(
    first_role: str,
    second_role: str,
    token: str,
) -> GpuSourceConfig:
```

- Exact decorators: none.
- Declared return annotation: `GpuSourceConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `first_role` | positional-or-keyword | `str` | `required` |
| `second_role` | positional-or-keyword | `str` | `required` |
| `token` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `GpuSourceConfig.model_validate(payload)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_gpu_fr::test_inspection_rejects_one_physical_layer_for_two_logical_roles` via `_config_with_shared_role_token`
- value/type reference: `tests.unit.test_gpu_fr::test_inspection_rejects_one_physical_layer_for_two_logical_roles` via `_config_with_shared_role_token`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_config().model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `_config` | `tests.unit.test_gpu_fr._config` |
| `GpuSourceConfig.model_validate` | `landscout.sources.gpu_fr.GpuSourceConfig.model_validate` |

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
| In-memory mutation | `payload["spatial_layers"][first_role]["match_tokens"] = [token]`<br>`payload["spatial_layers"][second_role]["match_tokens"] = [token]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _config_with_shared_role_token(
    first_role: str,
    second_role: str,
    token: str,
) -> GpuSourceConfig:
    payload = _config().model_dump(mode="python")
    payload["spatial_layers"][first_role]["match_tokens"] = [token]
    payload["spatial_layers"][second_role]["match_tokens"] = [token]
    return GpuSourceConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_inspection_rejects_one_physical_layer_for_two_logical_roles`

**Purpose:** Regression invariant: inspection rejects one physical layer for two logical roles. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_inspection_rejects_one_physical_layer_for_two_logical_roles(
    tmp_path: Path,
    first_role: str,
    second_role: str,
    token: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("first_role", "second_role", "token"),
    [
        ("zoning", "prescription_surface", "zone_urba"),
        ("prescription_surface", "prescription_line", "prescription_surf"),
        ("prescription_surface", "information_surface", "prescription_surf"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `first_role` | positional-or-keyword | `str` | `required` |
| `second_role` | positional-or-keyword | `str` | `required` |
| `token` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuSpatialInspectionError, match="role\|logical\|same layer")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_extraction_from_archive` | `tests.unit.test_gpu_fr._extraction_from_archive` |
| `_planning_archive` | `tests.unit.test_gpu_fr._planning_archive` |
| `_config_with_shared_role_token` | `tests.unit.test_gpu_fr._config_with_shared_role_token` |
| `pytest.raises` | `pytest.raises` |
| `inspect_gpu_planning_document` | `landscout.sources.gpu_fr.inspect_gpu_planning_document` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
def test_inspection_rejects_one_physical_layer_for_two_logical_roles(
    tmp_path: Path,
    first_role: str,
    second_role: str,
    token: str,
) -> None:
    extraction = _extraction_from_archive(_planning_archive(tmp_path), tmp_path)
    config = _config_with_shared_role_token(first_role, second_role, token)

    with pytest.raises(GpuSpatialInspectionError, match="role|logical|same layer"):
        inspect_gpu_planning_document(extraction, config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_inspection_rejects_mutated_config_before_layer_discovery`

**Purpose:** Regression invariant: inspection rejects mutated config before layer discovery. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_inspection_rejects_mutated_config_before_layer_discovery(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuSpatialInspectionError, match="config\|provider")`
- Exact assertions:
  - `assert discovery_calls == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_extraction_from_archive` | `tests.unit.test_gpu_fr._extraction_from_archive` |
| `_planning_archive` | `tests.unit.test_gpu_fr._planning_archive` |
| `_config().model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_config` | `tests.unit.test_gpu_fr._config` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `inspect_gpu_planning_document` | `landscout.sources.gpu_fr.inspect_gpu_planning_document` |

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
def test_inspection_rejects_mutated_config_before_layer_discovery(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    extraction = _extraction_from_archive(_planning_archive(tmp_path), tmp_path)
    forged = _config().model_copy(update={"provider": "UNTRUSTED"})
    discovery_calls = 0

    def counted(*args: object, **kwargs: object) -> object:
        nonlocal discovery_calls
        discovery_calls += 1
        raise AssertionError("layer discovery ran for an invalid config")

    monkeypatch.setattr(gpu, "discover_gpu_spatial_layers", counted)

    with pytest.raises(GpuSpatialInspectionError, match="config|provider"):
        inspect_gpu_planning_document(extraction, forged)

    assert discovery_calls == 0
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_inspection_rejects_mutated_config_before_layer_discovery.counted`

**Purpose:** Implements `counted` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def counted(*args: object, **kwargs: object) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `AssertionError("layer discovery ran for an invalid config")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |

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
def counted(*args: object, **kwargs: object) -> object:
        nonlocal discovery_calls
        discovery_calls += 1
        raise AssertionError("layer discovery ran for an invalid config")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_inspection_rejects_archive_byte_mutation_before_layer_discovery`

**Purpose:** Regression invariant: inspection rejects archive byte mutation before layer discovery. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_inspection_rejects_archive_byte_mutation_before_layer_discovery(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuSpatialInspectionError, match="archive\|source\|config")`
- Exact assertions:
  - `assert discovery_calls == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_planning_archive` | `tests.unit.test_gpu_fr._planning_archive` |
| `_extraction_from_archive` | `tests.unit.test_gpu_fr._extraction_from_archive` |
| `archive.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `archive.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `inspect_gpu_planning_document` | `landscout.sources.gpu_fr.inspect_gpu_planning_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `archive.read_bytes` |
| Filesystem/archive write or publication | `archive.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_inspection_rejects_archive_byte_mutation_before_layer_discovery(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    archive = _planning_archive(tmp_path)
    extraction = _extraction_from_archive(archive, tmp_path)
    archive.write_bytes(archive.read_bytes() + b"post-extraction-mutation")
    discovery_calls = 0

    def counted(*args: object, **kwargs: object) -> object:
        nonlocal discovery_calls
        discovery_calls += 1
        raise AssertionError("layer discovery ran after archive mutation")

    monkeypatch.setattr(gpu, "discover_gpu_spatial_layers", counted)

    with pytest.raises(GpuSpatialInspectionError, match="archive|source|config"):
        inspect_gpu_planning_document(extraction, _config())

    assert discovery_calls == 0
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_inspection_rejects_archive_byte_mutation_before_layer_discovery.counted`

**Purpose:** Implements `counted` within the file role: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

**Exact signature**

```python
def counted(*args: object, **kwargs: object) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `AssertionError("layer discovery ran after archive mutation")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |

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
def counted(*args: object, **kwargs: object) -> object:
        nonlocal discovery_calls
        discovery_calls += 1
        raise AssertionError("layer discovery ran after archive mutation")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_inspection_rejects_document_lineage_not_matching_config`

**Purpose:** Regression invariant: inspection rejects document lineage not matching config. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_inspection_rejects_document_lineage_not_matching_config(
    tmp_path: Path,
    field: str,
    value: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "value"),
    [
        ("commune_code", "99999"),
        ("partition", "DU_99999"),
        ("document_type", ""),
        (
            "source_url",
            "https://www.geoportail-urbanisme.gouv.fr/api/document/download-by-partition/DU_99999",
        ),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `field` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        GpuSpatialInspectionError,<br>        match="config\|commune\|partition\|URL\|type\|planning",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_extraction_from_archive` | `tests.unit.test_gpu_fr._extraction_from_archive` |
| `_planning_archive` | `tests.unit.test_gpu_fr._planning_archive` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `inspect_gpu_planning_document` | `landscout.sources.gpu_fr.inspect_gpu_planning_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
def test_inspection_rejects_document_lineage_not_matching_config(
    tmp_path: Path,
    field: str,
    value: str,
) -> None:
    extraction = _extraction_from_archive(_planning_archive(tmp_path), tmp_path)
    document = replace(extraction.archive.document, **{field: value})
    forged = replace(
        extraction,
        archive=replace(extraction.archive, document=document),
    )

    with pytest.raises(
        GpuSpatialInspectionError,
        match="config|commune|partition|URL|type|planning",
    ):
        inspect_gpu_planning_document(forged, _config())
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_planning_document_records_and_revalidates_exact_config_identity`

**Purpose:** Regression invariant: planning document records and revalidates exact config identity. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_planning_document_records_and_revalidates_exact_config_identity(
    tmp_path: Path,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuSpatialInspectionError, match="config\|SHA")`
  - `pytest.raises(GpuSpatialInspectionError, match="inventory\|tuple")`
- Exact assertions:
  - `assert result.source_config == _config()`
  - `assert result.source_config_sha256 == gpu._source_config_sha256(_config())`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_extraction_from_archive` | `tests.unit.test_gpu_fr._extraction_from_archive` |
| `_planning_archive` | `tests.unit.test_gpu_fr._planning_archive` |
| `inspect_gpu_planning_document` | `landscout.sources.gpu_fr.inspect_gpu_planning_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |
| `gpu._source_config_sha256` | `landscout.sources.gpu_fr._source_config_sha256` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `gpu.revalidate_gpu_spatial_layer_source` | `landscout.sources.gpu_fr.revalidate_gpu_spatial_layer_source` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `gpu._source_config_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_planning_document_records_and_revalidates_exact_config_identity(
    tmp_path: Path,
) -> None:
    extraction = _extraction_from_archive(_planning_archive(tmp_path), tmp_path)
    result = inspect_gpu_planning_document(extraction, _config())

    assert result.source_config == _config()
    assert result.source_config_sha256 == gpu._source_config_sha256(_config())
    forged = replace(result, source_config_sha256="0" * 64)
    with pytest.raises(GpuSpatialInspectionError, match="config|SHA"):
        gpu.revalidate_gpu_spatial_layer_source(forged, forged.zoning)
    malformed_inventory = replace(
        result,
        all_spatial_layers=list(result.all_spatial_layers),  # type: ignore[arg-type]
    )
    with pytest.raises(GpuSpatialInspectionError, match="inventory|tuple"):
        gpu.revalidate_gpu_spatial_layer_source(
            malformed_inventory,
            malformed_inventory.zoning,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_revalidation_rejects_coordinated_spatial_omission`

**Purpose:** Regression invariant: source complete revalidation rejects coordinated spatial omission. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_revalidation_rejects_coordinated_spatial_omission(
    tmp_path: Path,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GpuSpatialInspectionError, match="spatial inventory\|physical")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_extraction_from_archive` | `tests.unit.test_gpu_fr._extraction_from_archive` |
| `_planning_archive` | `tests.unit.test_gpu_fr._planning_archive` |
| `inspect_gpu_planning_document` | `landscout.sources.gpu_fr.inspect_gpu_planning_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `gpu.revalidate_gpu_spatial_layer_source` | `landscout.sources.gpu_fr.revalidate_gpu_spatial_layer_source` |

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
def test_source_complete_revalidation_rejects_coordinated_spatial_omission(
    tmp_path: Path,
) -> None:
    extraction = _extraction_from_archive(_planning_archive(tmp_path), tmp_path)
    result = inspect_gpu_planning_document(extraction, _config())
    forged = replace(
        result,
        all_spatial_layers=(result.zoning.reference,),
        related_layers=(),
    )

    with pytest.raises(GpuSpatialInspectionError, match="spatial inventory|physical"):
        gpu.revalidate_gpu_spatial_layer_source(forged, forged.zoning)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_cached_document_lineage_change_forces_refresh`

**Purpose:** Regression invariant: cached document lineage change forces refresh. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_cached_document_lineage_change_forces_refresh(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert not download_gpu_document(changed, _config(), tmp_path).cache_hit`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_gpu_fr._download` |
| `replace` | `dataclasses.replace` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `item.source_url.replace` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `download_gpu_document` | `landscout.sources.gpu_fr.download_gpu_document` |
| `_config` | `tests.unit.test_gpu_fr._config` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `item.source_url.replace` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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
    monkeypatch.setattr(
        gpu, "open_safe_https", lambda *args, **kwargs: _Response(_zip_bytes())
    )
    assert not download_gpu_document(changed, _config(), tmp_path).cache_hit
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **64**.
- Pytest fixtures (decorator-proven): **0**.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_valid_config_and_urls` | none | none | 3 | Proves valid config and urls using the exact source reproduced in section 7. |
| `test_duplicate_gpu_yaml_key_is_rejected` | none | pytest.raises(gpu.GpuConfigError) | 1 | Proves duplicate gpu yaml key is rejected using the exact source reproduced in section 7. |
| `test_invalid_config_values_are_rejected` | pytest.mark.parametrize(<br>    ("path", "value"),<br>    [<br>        (("pilot", "commune_code"), "3139"),<br>        (("api", "base_url"), "file:///api"),<br>        (("api", "base_url"), "http://www.geoportail-urbanisme.gouv.fr/api"),<br>        (("api", "base_url"), "https://example.com/api"),<br>        (("api", "base_url"), "https://www.geoportail-urbanisme.gouv.fr:8443/api"),<br>        (("api", "base_url"), "https://www.geoportail-urbanisme.gouv.fr/api?x=1"),<br>        (("download", "strategy"), "parcel"),<br>        (("download", "partition_template"), ""),<br>        (("cache", "max_age_hours"), -1),<br>    ],<br>) | pytest.raises(ValidationError) | 0 | Proves invalid config values are rejected using the exact source reproduced in section 7. |
| `test_mutated_loaded_api_origin_is_rejected_before_discovery_network` | none | pytest.raises(ValidationError, match="frozen"); pytest.raises(GpuDiscoveryError, match="config\|official\|origin") | 1 | Proves mutated loaded api origin is rejected before discovery network using the exact source reproduced in section 7. |
| `test_gpu_source_identity_is_exact` | pytest.mark.parametrize("field", ["provider", "portal"]) | pytest.raises(ValidationError) | 0 | Proves gpu source identity is exact using the exact source reproduced in section 7. |
| `test_gpu_cache_age_rejects_coercion_and_nonfinite` | pytest.mark.parametrize("value", [True, "168", float("nan"), float("inf")]) | pytest.raises(ValidationError) | 0 | Proves gpu cache age rejects coercion and nonfinite using the exact source reproduced in section 7. |
| `test_gpu_source_config_identity_is_deterministic_and_content_bound` | none | none | 2 | Proves gpu source config identity is deterministic and content bound using the exact source reproduced in section 7. |
| `test_unknown_config_field_is_rejected` | none | pytest.raises(ValidationError) | 0 | Proves unknown config field is rejected using the exact source reproduced in section 7. |
| `test_document_discovery_success` | none | none | 7 | Proves document discovery success using the exact source reproduced in section 7. |
| `test_gpu_api_json_is_strict_before_document_selection` | pytest.mark.parametrize(<br>    "payload",<br>    [<br>        b'[{"id":"doc-1","id":"doc-2"}]',<br>        b"[NaN]",<br>        b"[Infinity]",<br>    ],<br>) | pytest.raises(GpuDiscoveryError, match="JSON\|duplicate\|finite\|metadata") | 0 | Proves gpu api json is strict before document selection using the exact source reproduced in section 7. |
| `test_written_material_url_must_be_exact_official_https_api_url` | pytest.mark.parametrize(<br>    "source_url",<br>    [<br>        (<br>            "http://www.geoportail-urbanisme.gouv.fr/api/document/"<br>            "doc-1/files/reglement.pdf"<br>        ),<br>        "https://unrelated.example/api/document/doc-1/files/reglement.pdf",<br>    ],<br>    ids=["http", "unrelated-https-origin"],<br>) | pytest.raises(GpuDiscoveryError, match="written material URL") | 0 | Proves written material url must be exact official https api url using the exact source reproduced in section 7. |
| `test_written_material_fallback_rejects_unsafe_archive_url_provenance` | pytest.mark.parametrize(<br>    "archive_url",<br>    [<br>        (<br>            "http://www.geoportail-urbanisme.gouv.fr/api/document/"<br>            "doc-1/download/31395_PLU_20240215.zip"<br>        ),<br>        (<br>            "https://unrelated.example/api/document/doc-1/download/"<br>            "31395_PLU_20240215.zip"<br>        ),<br>    ],<br>    ids=["http", "unrelated-https-origin"],<br>) | pytest.raises(GpuDiscoveryError, match="archive URL") | 0 | Proves written material fallback rejects unsafe archive url provenance using the exact source reproduced in section 7. |
| `test_no_current_document_is_rejected` | none | pytest.raises(GpuDiscoveryError, match="No current") | 0 | Proves no current document is rejected using the exact source reproduced in section 7. |
| `test_ambiguous_current_documents_are_rejected` | none | pytest.raises(GpuDiscoveryError, match="Ambiguous") | 0 | Proves ambiguous current documents are rejected using the exact source reproduced in section 7. |
| `test_missing_document_identity_is_rejected` | pytest.mark.parametrize("field", ["id", "originalName", "type"]) | pytest.raises(GpuDiscoveryError, match="missing") | 0 | Proves missing document identity is rejected using the exact source reproduced in section 7. |
| `test_document_details_must_match_selected_listing` | pytest.mark.parametrize(<br>    ("field", "different_value"),<br>    [<br>        ("id", "doc-2"),<br>        ("originalName", "31395_PLU_OTHER"),<br>        ("name", "DU_99999"),<br>        ("type", "CC"),<br>        ("status", "document.deleted"),<br>        ("legalStatus", "CANCELLED"),<br>        ("effectiveStatus", "ANNULE"),<br>    ],<br>) | pytest.raises(GpuDiscoveryError, match="match\|changed\|current") | 0 | Proves document details must match selected listing using the exact source reproduced in section 7. |
| `test_document_details_commune_must_match_selected_listing` | none | pytest.raises(GpuDiscoveryError, match="match") | 0 | Proves document details commune must match selected listing using the exact source reproduced in section 7. |
| `test_discovery_rejects_unsafe_archive_name` | pytest.mark.parametrize(<br>    "archive_name",<br>    _UNSAFE_ARCHIVE_NAMES,<br>) | pytest.raises(GpuDiscoveryError, match="archive name\|safe") | 0 | Proves discovery rejects unsafe archive name using the exact source reproduced in section 7. |
| `test_successful_download_persists_sha_and_sidecar` | none | none | 6 | Proves successful download persists sha and sidecar using the exact source reproduced in section 7. |
| `test_download_rejects_document_inconsistent_with_config` | pytest.mark.parametrize(<br>    ("field", "different_value"),<br>    [<br>        ("provider", "OTHER PROVIDER"),<br>        ("portal", "OTHER PORTAL"),<br>        ("commune_code", "99999"),<br>        ("partition", "DU_99999"),<br>        ("status", "document.deleted"),<br>        ("legal_status", "CANCELLED"),<br>        ("effective_status", "ANNULE"),<br>        ("source_url", "https://example.test/not-the-gpu.zip"),<br>        (<br>            "source_url",<br>            (<br>                "https://www.geoportail-urbanisme.gouv.fr/api/document/"<br>                "download-by-partition/DU_99999"<br>            ),<br>        ),<br>    ],<br>) | pytest.raises(GpuDownloadError, match="document\|identity\|config") | 1 | Proves download rejects document inconsistent with config using the exact source reproduced in section 7. |
| `test_download_rejects_forged_written_file_provenance_before_network` | pytest.mark.parametrize("mutation", ["forged-source-url", "wrong-item-type"]) | pytest.raises(GpuDownloadError, match="written\|document\|source\|URL") | 1 | Proves download rejects forged written file provenance before network using the exact source reproduced in section 7. |
| `test_download_rejects_forged_unsafe_archive_name_before_io` | pytest.mark.parametrize(<br>    "archive_name",<br>    _UNSAFE_ARCHIVE_NAMES,<br>) | pytest.raises(GpuDownloadError, match="archive name\|archive filename\|safe") | 1 | Proves download rejects forged unsafe archive name before io using the exact source reproduced in section 7. |
| `test_archive_name_with_one_zip_suffix_is_not_duplicated` | none | none | 2 | Proves archive name with one zip suffix is not duplicated using the exact source reproduced in section 7. |
| `test_fresh_cache_is_reused` | none | none | 2 | Proves fresh cache is reused using the exact source reproduced in section 7. |
| `test_boolean_cache_integrity_counts_are_not_accepted_as_integers` | pytest.mark.parametrize("field", ["file_size", "member_count"]) | none | 1 | Proves boolean cache integrity counts are not accepted as integers using the exact source reproduced in section 7. |
| `test_stale_recovery_backup_rejects_cache_before_network` | none | pytest.raises(GpuDownloadError, match="backup\|recovery\|manual") | 1 | Proves stale recovery backup rejects cache before network using the exact source reproduced in section 7. |
| `test_expired_cache_is_refreshed` | none | none | 2 | Proves expired cache is refreshed using the exact source reproduced in section 7. |
| `test_failed_refresh_preserves_previous_cache` | none | pytest.raises(GpuDownloadError) | 3 | Proves failed refresh preserves previous cache using the exact source reproduced in section 7. |
| `test_metadata_publication_failure_rolls_back_both_cache_files` | none | pytest.raises(GpuDownloadError) | 4 | Proves metadata publication failure rolls back both cache files using the exact source reproduced in section 7. |
| `test_publication_and_rollback_failure_preserves_exact_recovery_backups` | none | pytest.raises(GpuDownloadError, match="rollback") | 2 | Proves publication and rollback failure preserves exact recovery backups using the exact source reproduced in section 7. |
| `test_cleanup_failure_does_not_mask_double_failure_recovery_error` | none | pytest.raises(GpuDownloadError, match="rollback") | 2 | Proves cleanup failure does not mask double failure recovery error using the exact source reproduced in section 7. |
| `test_stale_cache_recovery_backup_fails_closed_without_destroying_it` | none | pytest.raises(GpuDownloadError, match="backup\|recovery\|manual") | 3 | Proves stale cache recovery backup fails closed without destroying it using the exact source reproduced in section 7. |
| `test_preexisting_temporary_archive_symlink_cannot_modify_target` | none | pytest.raises(GpuDownloadError) | 2 | Proves preexisting temporary archive symlink cannot modify target using the exact source reproduced in section 7. |
| `test_corrupt_download_is_rejected` | none | pytest.raises(GpuDownloadError) | 1 | Proves corrupt download is rejected using the exact source reproduced in section 7. |
| `test_tampered_sidecar_invalidates_cache` | none | none | 1 | Proves tampered sidecar invalidates cache using the exact source reproduced in section 7. |
| `test_archive_path_traversal_is_rejected` | none | pytest.raises(GpuArchiveError, match="Unsafe") | 0 | Proves archive path traversal is rejected using the exact source reproduced in section 7. |
| `test_archive_symlink_is_rejected` | none | pytest.raises(GpuArchiveError, match="Symbolic") | 0 | Proves archive symlink is rejected using the exact source reproduced in section 7. |
| `test_duplicate_zip_extraction_targets_are_rejected` | pytest.mark.parametrize(<br>    "members",<br>    [<br>        [("duplicate.txt", b"first"), ("duplicate.txt", b"second")],<br>        [("folder/file.txt", b"first"), (r"folder\file.txt", b"second")],<br>        [("folder/file.txt", b"first"), ("folder/./file.txt", b"second")],<br>        [("Folder/File.txt", b"first"), ("folder/file.txt", b"second")],<br>    ],<br>) | pytest.raises(GpuArchiveError, match="(?i)duplicate\|collid") | 0 | Proves duplicate zip extraction targets are rejected using the exact source reproduced in section 7. |
| `test_zip_file_directory_target_collision_is_rejected` | none | pytest.raises(GpuArchiveError, match="collision\|target") | 0 | Proves zip file directory target collision is rejected using the exact source reproduced in section 7. |
| `test_zip_cannot_claim_extraction_manifest_path` | none | pytest.raises(GpuArchiveError, match="manifest") | 0 | Proves zip cannot claim extraction manifest path using the exact source reproduced in section 7. |
| `test_extraction_inventory_and_cache` | none | none | 7 | Proves extraction inventory and cache using the exact source reproduced in section 7. |
| `test_extraction_manifest_is_created_exclusively` | none | none | 1 | Proves extraction manifest is created exclusively using the exact source reproduced in section 7. |
| `test_stale_extraction_backup_fails_closed_and_is_preserved` | none | pytest.raises(GpuArchiveError, match="backup\|recovery\|manual") | 2 | Proves stale extraction backup fails closed and is preserved using the exact source reproduced in section 7. |
| `test_extraction_publication_and_rollback_failure_preserves_backup` | none | pytest.raises(GpuArchiveError, match="rollback"); pytest.raises(GpuArchiveError, match="backup\|recovery\|manual") | 2 | Proves extraction publication and rollback failure preserves backup using the exact source reproduced in section 7. |
| `test_extraction_publication_failure_restores_existing_root` | none | pytest.raises(GpuArchiveError, match="publication") | 2 | Proves extraction publication failure restores existing root using the exact source reproduced in section 7. |
| `test_extraction_backup_move_failure_preserves_existing_root` | none | pytest.raises(GpuArchiveError, match="backup.*failed") | 2 | Proves extraction backup move failure preserves existing root using the exact source reproduced in section 7. |
| `test_extraction_inventory_rejects_special_entry` | none | pytest.raises(GpuArchiveError, match="special filesystem entry") | 0 | Proves extraction inventory rejects special entry using the exact source reproduced in section 7. |
| `test_extraction_cleanup_preserves_primary_controlled_error` | none | pytest.raises(GpuArchiveError, match="could not be cleaned") | 0 | Proves extraction cleanup preserves primary controlled error using the exact source reproduced in section 7. |
| `test_extraction_temporary_link_is_rejected_without_unlinking_target` | pytest.mark.parametrize("link_kind", ["symlink", "junction"]) | pytest.raises(GpuArchiveError, match="temporary\|link\|junction") | 3 | Proves extraction temporary link is rejected without unlinking target using the exact source reproduced in section 7. |
| `test_stale_extraction_temporary_directory_fails_closed_and_is_preserved` | none | pytest.raises(GpuArchiveError, match="temporary\|manual\|recovery") | 1 | Proves stale extraction temporary directory fails closed and is preserved using the exact source reproduced in section 7. |
| `test_duplicate_extraction_manifest_key_forces_verified_rebuild` | none | none | 2 | Proves duplicate extraction manifest key forces verified rebuild using the exact source reproduced in section 7. |
| `test_stale_download_object_rejects_replaced_valid_archive` | none | pytest.raises(GpuArchiveError, match="checksum\|SHA\|stale\|metadata") | 2 | Proves stale download object rejects replaced valid archive using the exact source reproduced in section 7. |
| `test_extraction_rejects_archive_object_inconsistent_with_path` | pytest.mark.parametrize(<br>    ("field", "value"),<br>    [<br>        ("sha256", "0" * 64),<br>        ("file_size", 1),<br>        ("filename", "other.zip"),<br>        ("archive_format", "7z"),<br>    ],<br>) | pytest.raises(GpuArchiveError, match="archive\|metadata\|checksum\|size") | 0 | Proves extraction rejects archive object inconsistent with path using the exact source reproduced in section 7. |
| `test_tampered_extraction_is_rebuilt_from_verified_archive` | pytest.mark.parametrize("mutation", ["content", "deleted", "added", "path"]) | none | 4 | Proves tampered extraction is rebuilt from verified archive using the exact source reproduced in section 7. |
| `test_spatial_inventory_and_inspection_preserve_source_quality` | none | none | 10 | Proves spatial inventory and inspection preserve source quality using the exact source reproduced in section 7. |
| `test_missing_zoning_layer_fails_clearly` | none | pytest.raises(GpuSpatialInspectionError, match="zoning") | 0 | Proves missing zoning layer fails clearly using the exact source reproduced in section 7. |
| `test_ambiguous_zoning_layer_fails_clearly` | none | pytest.raises(GpuSpatialInspectionError, match="found 2") | 0 | Proves ambiguous zoning layer fails clearly using the exact source reproduced in section 7. |
| `test_inspection_rejects_one_physical_layer_for_two_logical_roles` | pytest.mark.parametrize(<br>    ("first_role", "second_role", "token"),<br>    [<br>        ("zoning", "prescription_surface", "zone_urba"),<br>        ("prescription_surface", "prescription_line", "prescription_surf"),<br>        ("prescription_surface", "information_surface", "prescription_surf"),<br>    ],<br>) | pytest.raises(GpuSpatialInspectionError, match="role\|logical\|same layer") | 0 | Proves inspection rejects one physical layer for two logical roles using the exact source reproduced in section 7. |
| `test_inspection_rejects_mutated_config_before_layer_discovery` | none | pytest.raises(GpuSpatialInspectionError, match="config\|provider") | 1 | Proves inspection rejects mutated config before layer discovery using the exact source reproduced in section 7. |
| `test_inspection_rejects_archive_byte_mutation_before_layer_discovery` | none | pytest.raises(GpuSpatialInspectionError, match="archive\|source\|config") | 1 | Proves inspection rejects archive byte mutation before layer discovery using the exact source reproduced in section 7. |
| `test_inspection_rejects_document_lineage_not_matching_config` | pytest.mark.parametrize(<br>    ("field", "value"),<br>    [<br>        ("commune_code", "99999"),<br>        ("partition", "DU_99999"),<br>        ("document_type", ""),<br>        (<br>            "source_url",<br>            "https://www.geoportail-urbanisme.gouv.fr/api/document/download-by-partition/DU_99999",<br>        ),<br>    ],<br>) | pytest.raises(<br>        GpuSpatialInspectionError,<br>        match="config\|commune\|partition\|URL\|type\|planning",<br>    ) | 0 | Proves inspection rejects document lineage not matching config using the exact source reproduced in section 7. |
| `test_planning_document_records_and_revalidates_exact_config_identity` | none | pytest.raises(GpuSpatialInspectionError, match="config\|SHA"); pytest.raises(GpuSpatialInspectionError, match="inventory\|tuple") | 2 | Proves planning document records and revalidates exact config identity using the exact source reproduced in section 7. |
| `test_source_complete_revalidation_rejects_coordinated_spatial_omission` | none | pytest.raises(GpuSpatialInspectionError, match="spatial inventory\|physical") | 0 | Proves source complete revalidation rejects coordinated spatial omission using the exact source reproduced in section 7. |
| `test_cached_document_lineage_change_forces_refresh` | none | none | 1 | Proves cached document lineage change forces refresh using the exact source reproduced in section 7. |

## 8. Public exports and package ownership

This module declares no `__all__`; no package-level public guarantee is inferred from direct importability alone.

## 9. Trust, provenance, side effects, and business boundary

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
from __future__ import annotations

import io
import json
import os
import shutil
import warnings
import zipfile
from dataclasses import replace
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Self
from urllib.error import URLError

import geopandas as gpd  # type: ignore[import-untyped]
import pytest
from pydantic import HttpUrl, ValidationError
from shapely.geometry import Polygon

import landscout.sources.gpu_fr as gpu
from landscout.sources.gpu_fr import (
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
)

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


class _Response(io.BytesIO):
    def __enter__(self) -> Self:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()


def _config() -> GpuSourceConfig:
    return load_gpu_source_config(Path("configs/sources/gpu_fr.yaml"))


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


def _files() -> list[dict[str, object]]:
    return [{"name": "reglement.pdf", "title": "Règlement écrit", "path": "Règlements"}]


def _patch_json_responses(
    monkeypatch: pytest.MonkeyPatch, values: list[object]
) -> None:
    responses = iter(values)

    def opener(*args: object, **kwargs: object) -> _Response:
        return _Response(json.dumps(next(responses)).encode())

    monkeypatch.setattr(gpu, "open_safe_https", opener)


def _document(monkeypatch: pytest.MonkeyPatch):
    _patch_json_responses(monkeypatch, [[_listing_item()], _details(), _files()])
    return discover_current_gpu_document(_config())


def _zip_bytes(files: dict[str, bytes] | None = None) -> bytes:
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, content in (files or {"document/readme.txt": b"GPU"}).items():
            archive.writestr(name, content)
    return stream.getvalue()


def _zip_member_bytes(members: list[tuple[str, bytes]]) -> bytes:
    stream = io.BytesIO()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for name, content in members:
                archive.writestr(name, content)
    return stream.getvalue()


def _download(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    archive_bytes: bytes | None = None,
) -> GpuArchiveDownload:
    document = _document(monkeypatch)
    monkeypatch.setattr(
        gpu,
        "open_safe_https",
        lambda *args, **kwargs: _Response(archive_bytes or _zip_bytes()),
    )
    return download_gpu_document(document, _config(), tmp_path)


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
    prescription = gpd.GeoDataFrame({"TYPEPSC": [5]}, geometry=[valid], crs="EPSG:2154")
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


def test_valid_config_and_urls() -> None:
    config = _config()
    assert build_gpu_partition(config) == "DU_31395"
    assert "partition=DU_31395" in build_gpu_document_list_url(config)
    assert build_gpu_partition_download_url(config).endswith(
        "/document/download-by-partition/DU_31395"
    )


def test_duplicate_gpu_yaml_key_is_rejected(tmp_path: Path) -> None:
    config_path = tmp_path / "gpu.yaml"
    config_path.write_bytes(
        Path("configs/sources/gpu_fr.yaml").read_bytes() + b"\nprovider: UNTRUSTED\n"
    )

    with pytest.raises(gpu.GpuConfigError) as captured:
        load_gpu_source_config(config_path)

    assert "duplicate" in str(captured.value.__cause__).casefold()


@pytest.mark.parametrize(
    ("path", "value"),
    [
        (("pilot", "commune_code"), "3139"),
        (("api", "base_url"), "file:///api"),
        (("api", "base_url"), "http://www.geoportail-urbanisme.gouv.fr/api"),
        (("api", "base_url"), "https://example.com/api"),
        (("api", "base_url"), "https://www.geoportail-urbanisme.gouv.fr:8443/api"),
        (("api", "base_url"), "https://www.geoportail-urbanisme.gouv.fr/api?x=1"),
        (("download", "strategy"), "parcel"),
        (("download", "partition_template"), ""),
        (("cache", "max_age_hours"), -1),
    ],
)
def test_invalid_config_values_are_rejected(
    path: tuple[str, str], value: object
) -> None:
    payload = _config().model_dump(mode="json")
    payload[path[0]][path[1]] = value
    with pytest.raises(ValidationError):
        GpuSourceConfig.model_validate(payload)


def test_mutated_loaded_api_origin_is_rejected_before_discovery_network(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config = _config()
    with pytest.raises(ValidationError, match="frozen"):
        config.api.base_url = HttpUrl("https://unrelated.example/api")
    forged_api = config.api.model_copy(
        update={"base_url": HttpUrl("https://unrelated.example/api")}
    )
    forged = config.model_copy(update={"api": forged_api})
    network_calls = 0

    def fail_network(*args: object, **kwargs: object) -> object:
        nonlocal network_calls
        network_calls += 1
        raise AssertionError("network used after GPU origin mutation")

    monkeypatch.setattr(gpu, "open_safe_https", fail_network)

    with pytest.raises(GpuDiscoveryError, match="config|official|origin"):
        discover_current_gpu_document(forged)

    assert network_calls == 0


@pytest.mark.parametrize("field", ["provider", "portal"])
def test_gpu_source_identity_is_exact(field: str) -> None:
    payload = _config().model_dump(mode="python")
    payload[field] = "UNTRUSTED"

    with pytest.raises(ValidationError):
        GpuSourceConfig.model_validate(payload)


@pytest.mark.parametrize("value", [True, "168", float("nan"), float("inf")])
def test_gpu_cache_age_rejects_coercion_and_nonfinite(value: object) -> None:
    payload = _config().model_dump(mode="python")
    payload["cache"]["max_age_hours"] = value

    with pytest.raises(ValidationError):
        GpuSourceConfig.model_validate(payload)


def test_gpu_source_config_identity_is_deterministic_and_content_bound() -> None:
    config = _config()
    reconstructed = GpuSourceConfig.model_validate(
        dict(reversed(tuple(config.model_dump(mode="python").items())))
    )
    changed_payload = config.model_dump(mode="python")
    changed_payload["cache"]["max_age_hours"] = 169
    changed = GpuSourceConfig.model_validate(changed_payload)

    assert gpu._source_config_sha256(reconstructed) == gpu._source_config_sha256(config)
    assert gpu._source_config_sha256(changed) != gpu._source_config_sha256(config)


def test_unknown_config_field_is_rejected() -> None:
    payload = _config().model_dump(mode="json")
    payload["unexpected"] = True
    with pytest.raises(ValidationError):
        GpuSourceConfig.model_validate(payload)


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


@pytest.mark.parametrize(
    "payload",
    [
        b'[{"id":"doc-1","id":"doc-2"}]',
        b"[NaN]",
        b"[Infinity]",
    ],
)
def test_gpu_api_json_is_strict_before_document_selection(
    monkeypatch: pytest.MonkeyPatch,
    payload: bytes,
) -> None:
    monkeypatch.setattr(
        gpu,
        "open_safe_https",
        lambda *args, **kwargs: _Response(payload),
    )

    with pytest.raises(GpuDiscoveryError, match="JSON|duplicate|finite|metadata"):
        discover_current_gpu_document(_config())


@pytest.mark.parametrize(
    "source_url",
    [
        (
            "http://www.geoportail-urbanisme.gouv.fr/api/document/"
            "doc-1/files/reglement.pdf"
        ),
        "https://unrelated.example/api/document/doc-1/files/reglement.pdf",
    ],
    ids=["http", "unrelated-https-origin"],
)
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


@pytest.mark.parametrize(
    "archive_url",
    [
        (
            "http://www.geoportail-urbanisme.gouv.fr/api/document/"
            "doc-1/download/31395_PLU_20240215.zip"
        ),
        (
            "https://unrelated.example/api/document/doc-1/download/"
            "31395_PLU_20240215.zip"
        ),
    ],
    ids=["http", "unrelated-https-origin"],
)
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


def test_no_current_document_is_rejected(monkeypatch: pytest.MonkeyPatch) -> None:
    _patch_json_responses(monkeypatch, [[_listing_item(status="document.deleted")]])
    with pytest.raises(GpuDiscoveryError, match="No current"):
        discover_current_gpu_document(_config())


def test_ambiguous_current_documents_are_rejected(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _patch_json_responses(monkeypatch, [[_listing_item(), _listing_item(id="doc-2")]])
    with pytest.raises(GpuDiscoveryError, match="Ambiguous"):
        discover_current_gpu_document(_config())


@pytest.mark.parametrize("field", ["id", "originalName", "type"])
def test_missing_document_identity_is_rejected(
    monkeypatch: pytest.MonkeyPatch, field: str
) -> None:
    item = _listing_item()
    item.pop(field)
    _patch_json_responses(monkeypatch, [[item]])
    with pytest.raises(GpuDiscoveryError, match="missing"):
        discover_current_gpu_document(_config())


@pytest.mark.parametrize(
    ("field", "different_value"),
    [
        ("id", "doc-2"),
        ("originalName", "31395_PLU_OTHER"),
        ("name", "DU_99999"),
        ("type", "CC"),
        ("status", "document.deleted"),
        ("legalStatus", "CANCELLED"),
        ("effectiveStatus", "ANNULE"),
    ],
)
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


@pytest.mark.parametrize(
    "archive_name",
    _UNSAFE_ARCHIVE_NAMES,
)
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


@pytest.mark.parametrize(
    ("field", "different_value"),
    [
        ("provider", "OTHER PROVIDER"),
        ("portal", "OTHER PORTAL"),
        ("commune_code", "99999"),
        ("partition", "DU_99999"),
        ("status", "document.deleted"),
        ("legal_status", "CANCELLED"),
        ("effective_status", "ANNULE"),
        ("source_url", "https://example.test/not-the-gpu.zip"),
        (
            "source_url",
            (
                "https://www.geoportail-urbanisme.gouv.fr/api/document/"
                "download-by-partition/DU_99999"
            ),
        ),
    ],
)
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


@pytest.mark.parametrize("mutation", ["forged-source-url", "wrong-item-type"])
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


@pytest.mark.parametrize(
    "archive_name",
    _UNSAFE_ARCHIVE_NAMES,
)
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


def test_fresh_cache_is_reused(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    first = _download(tmp_path, monkeypatch)
    monkeypatch.setattr(
        gpu, "open_safe_https", lambda *args, **kwargs: pytest.fail("network used")
    )
    second = download_gpu_document(first.document, _config(), tmp_path)
    assert second.cache_hit
    assert second.sha256 == first.sha256


@pytest.mark.parametrize("field", ["file_size", "member_count"])
def test_boolean_cache_integrity_counts_are_not_accepted_as_integers(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
) -> None:
    first = _download(tmp_path, monkeypatch)
    metadata_path = tmp_path / f"{first.filename}.metadata.json"
    payload = json.loads(metadata_path.read_text(encoding="utf-8"))
    payload["file_size"] = 1
    payload["member_count"] = 1
    payload[field] = True
    metadata_path.write_text(json.dumps(payload), encoding="utf-8")
    original_stat = Path.stat

    def one_byte_archive_stat(
        path: Path, *args: object, **kwargs: object
    ) -> os.stat_result:
        result = original_stat(path, *args, **kwargs)
        if path != first.path:
            return result
        values = list(result)
        values[6] = 1
        return os.stat_result(values)

    monkeypatch.setattr(Path, "stat", one_byte_archive_stat)
    monkeypatch.setattr(gpu, "validate_gpu_archive", lambda path: ("member",))
    monkeypatch.setattr(gpu, "_sha256", lambda path: first.sha256)

    assert (
        gpu._load_cached_archive(
            first.path,
            metadata_path,
            first.document,
            max_age_hours=168,
        )
        is None
    )


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


def test_expired_cache_is_refreshed(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    first = _download(tmp_path, monkeypatch)
    sidecar_path = tmp_path / f"{first.filename}.metadata.json"
    sidecar = json.loads(sidecar_path.read_text())
    sidecar["download_timestamp"] = (datetime.now(UTC) - timedelta(days=8)).isoformat()
    sidecar_path.write_text(json.dumps(sidecar), encoding="utf-8")
    fresh_bytes = _zip_bytes({"fresh.txt": b"fresh"})
    monkeypatch.setattr(
        gpu, "open_safe_https", lambda *args, **kwargs: _Response(fresh_bytes)
    )
    refreshed = download_gpu_document(first.document, _config(), tmp_path)
    assert not refreshed.cache_hit
    assert refreshed.sha256 != first.sha256


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
        gpu,
        "open_safe_https",
        lambda *args, **kwargs: _Response(_zip_bytes({"fresh": b"x"})),
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


def test_cleanup_failure_does_not_mask_double_failure_recovery_error(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    first = _download(tmp_path, monkeypatch)
    metadata_path = tmp_path / f"{first.filename}.metadata.json"
    metadata = json.loads(metadata_path.read_text())
    metadata["download_timestamp"] = (datetime.now(UTC) - timedelta(days=8)).isoformat()
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

    def simulated_symlink_open(path: Path, *args: object, **kwargs: object) -> object:
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


def test_corrupt_download_is_rejected(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    document = _document(monkeypatch)
    monkeypatch.setattr(
        gpu, "open_safe_https", lambda *args, **kwargs: _Response(b"not zip")
    )
    with pytest.raises(GpuDownloadError):
        download_gpu_document(document, _config(), tmp_path)
    assert not list(tmp_path.glob("*.part"))


def test_tampered_sidecar_invalidates_cache(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    first = _download(tmp_path, monkeypatch)
    sidecar_path = tmp_path / f"{first.filename}.metadata.json"
    sidecar = json.loads(sidecar_path.read_text())
    sidecar["sha256"] = "0" * 64
    sidecar_path.write_text(json.dumps(sidecar), encoding="utf-8")
    monkeypatch.setattr(
        gpu, "open_safe_https", lambda *args, **kwargs: _Response(_zip_bytes())
    )
    assert not download_gpu_document(first.document, _config(), tmp_path).cache_hit


def test_archive_path_traversal_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "unsafe.zip"
    path.write_bytes(_zip_bytes({"../escape.txt": b"bad"}))
    with pytest.raises(GpuArchiveError, match="Unsafe"):
        validate_gpu_archive(path)


def test_archive_symlink_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "unsafe.zip"
    with zipfile.ZipFile(path, "w") as archive:
        entry = zipfile.ZipInfo("link")
        entry.create_system = 3
        entry.external_attr = (0o120777 << 16) | 0xA000
        archive.writestr(entry, "target")
    with pytest.raises(GpuArchiveError, match="Symbolic"):
        validate_gpu_archive(path)


@pytest.mark.parametrize(
    "members",
    [
        [("duplicate.txt", b"first"), ("duplicate.txt", b"second")],
        [("folder/file.txt", b"first"), (r"folder\file.txt", b"second")],
        [("folder/file.txt", b"first"), ("folder/./file.txt", b"second")],
        [("Folder/File.txt", b"first"), ("folder/file.txt", b"second")],
    ],
)
def test_duplicate_zip_extraction_targets_are_rejected(
    tmp_path: Path,
    members: list[tuple[str, bytes]],
) -> None:
    path = tmp_path / "collision.zip"
    path.write_bytes(_zip_member_bytes(members))

    with pytest.raises(GpuArchiveError, match="(?i)duplicate|collid"):
        validate_gpu_archive(path)


def test_zip_file_directory_target_collision_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "collision.zip"
    path.write_bytes(
        _zip_member_bytes([("blocked", b"file"), ("blocked/child.txt", b"child")])
    )

    with pytest.raises(GpuArchiveError, match="collision|target"):
        validate_gpu_archive(path)


def test_zip_cannot_claim_extraction_manifest_path(tmp_path: Path) -> None:
    path = tmp_path / "collision.zip"
    path.write_bytes(
        _zip_bytes({f"{gpu.EXTRACTION_MANIFEST_NAME}/child": b"forbidden"})
    )

    with pytest.raises(GpuArchiveError, match="manifest"):
        validate_gpu_archive(path)


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
        (extracted.extraction_root / gpu.EXTRACTION_MANIFEST_NAME).read_text(
            encoding="utf-8"
        )
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


def test_extraction_manifest_is_created_exclusively(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    download = _download(tmp_path / "cache", monkeypatch)
    original_open = Path.open
    manifest_modes: list[str] = []

    def observed_open(
        path: Path,
        mode: str = "r",
        *args: object,
        **kwargs: object,
    ) -> object:
        if path.name == gpu.EXTRACTION_MANIFEST_NAME:
            manifest_modes.append(mode)
        return original_open(path, mode, *args, **kwargs)

    monkeypatch.setattr(Path, "open", observed_open)

    extract_gpu_document(download, tmp_path / "cache")

    assert manifest_modes == ["x", "rb"]


def test_stale_extraction_backup_fails_closed_and_is_preserved(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    download = _download(tmp_path / "cache", monkeypatch)
    extracted = extract_gpu_document(download, tmp_path / "cache")
    backup = extracted.extraction_root.with_name(
        f"{extracted.extraction_root.name}.bak"
    )
    backup.mkdir()
    sentinel = backup / "manual-recovery.txt"
    sentinel.write_bytes(b"preserve")

    with pytest.raises(GpuArchiveError, match="backup|recovery|manual"):
        extract_gpu_document(download, tmp_path / "cache")

    assert sentinel.read_bytes() == b"preserve"
    assert extracted.extraction_root.is_dir()


def test_extraction_publication_and_rollback_failure_preserves_backup(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    download = _download(tmp_path / "cache", monkeypatch)
    extracted = extract_gpu_document(download, tmp_path / "cache")
    sentinel = extracted.extraction_root / "manual-recovery.txt"
    sentinel.write_bytes(b"preserve")
    backup = extracted.extraction_root.with_name(
        f"{extracted.extraction_root.name}.bak"
    )
    temporary = extracted.extraction_root.with_name(
        f"{extracted.extraction_root.name}.part"
    )
    original_move = shutil.move

    def fail_publication_and_rollback(source: str, target: str) -> object:
        source_path = Path(source)
        target_path = Path(target)
        if source_path == temporary and target_path == extracted.extraction_root:
            raise OSError("simulated extraction publication failure")
        if source_path == backup and target_path == extracted.extraction_root:
            raise OSError("simulated extraction rollback failure")
        return original_move(source, target)

    monkeypatch.setattr(shutil, "move", fail_publication_and_rollback)

    with pytest.raises(GpuArchiveError, match="rollback"):
        extract_gpu_document(download, tmp_path / "cache")

    assert (backup / sentinel.name).read_bytes() == b"preserve"
    with pytest.raises(GpuArchiveError, match="backup|recovery|manual"):
        extract_gpu_document(download, tmp_path / "cache")
    assert (backup / sentinel.name).read_bytes() == b"preserve"


def test_extraction_publication_failure_restores_existing_root(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    download = _download(tmp_path / "cache", monkeypatch)
    extracted = extract_gpu_document(download, tmp_path / "cache")
    sentinel = extracted.extraction_root / "rollback-source.txt"
    sentinel.write_bytes(b"restore-me")
    temporary = extracted.extraction_root.with_name(
        f"{extracted.extraction_root.name}.part"
    )
    backup = extracted.extraction_root.with_name(
        f"{extracted.extraction_root.name}.bak"
    )
    original_move = shutil.move

    def fail_publication(source: str, target: str) -> object:
        if Path(source) == temporary and Path(target) == extracted.extraction_root:
            raise OSError("simulated extraction publication failure")
        return original_move(source, target)

    monkeypatch.setattr(shutil, "move", fail_publication)

    with pytest.raises(GpuArchiveError, match="publication"):
        extract_gpu_document(download, tmp_path / "cache")

    assert sentinel.read_bytes() == b"restore-me"
    assert not backup.exists()


def test_extraction_backup_move_failure_preserves_existing_root(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    download = _download(tmp_path / "cache", monkeypatch)
    extracted = extract_gpu_document(download, tmp_path / "cache")
    sentinel = extracted.extraction_root / "manual-recovery.txt"
    sentinel.write_bytes(b"preserve-existing-root")
    backup = extracted.extraction_root.with_name(
        f"{extracted.extraction_root.name}.bak"
    )
    original_move = shutil.move

    def fail_initial_backup(source: str, target: str) -> object:
        if Path(source) == extracted.extraction_root and Path(target) == backup:
            raise OSError("simulated initial backup failure")
        return original_move(source, target)

    monkeypatch.setattr(shutil, "move", fail_initial_backup)

    with pytest.raises(GpuArchiveError, match="backup.*failed"):
        extract_gpu_document(download, tmp_path / "cache")

    assert sentinel.read_bytes() == b"preserve-existing-root"
    assert not backup.exists()


def test_extraction_inventory_rejects_special_entry(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    root = tmp_path / "extraction"
    root.mkdir()
    special = root / "special-entry"
    special.write_bytes(b"source")
    original_is_file = Path.is_file
    original_is_dir = Path.is_dir

    def simulated_is_file(path: Path) -> bool:
        return False if path == special else original_is_file(path)

    def simulated_is_dir(path: Path) -> bool:
        return False if path == special else original_is_dir(path)

    monkeypatch.setattr(Path, "is_file", simulated_is_file)
    monkeypatch.setattr(Path, "is_dir", simulated_is_dir)

    with pytest.raises(GpuArchiveError, match="special filesystem entry"):
        gpu._inventory(root)


def test_extraction_cleanup_preserves_primary_controlled_error(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    temporary = tmp_path / "extraction.part"

    def fail_cleanup(path: Path) -> None:
        assert path == temporary
        raise PermissionError("simulated cleanup failure")

    monkeypatch.setattr(gpu, "_remove_extraction_path", fail_cleanup)
    primary = GpuArchiveError("primary extraction failure")

    gpu._cleanup_temporary_extraction_directory(temporary, primary)

    with pytest.raises(GpuArchiveError, match="could not be cleaned"):
        gpu._cleanup_temporary_extraction_directory(temporary, None)


@pytest.mark.parametrize("link_kind", ["symlink", "junction"])
def test_extraction_temporary_link_is_rejected_without_unlinking_target(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    link_kind: str,
) -> None:
    download = _download(tmp_path / "cache", monkeypatch)
    root = tmp_path / "cache" / "x" / download.sha256[:16]
    temporary = root.with_name(f"{root.name}.part")
    original_is_symlink = Path.is_symlink
    original_is_junction = Path.is_junction
    original_unlink = Path.unlink
    original_rmdir = Path.rmdir
    original_rmtree = shutil.rmtree
    unlink_calls = 0
    rmdir_calls = 0
    rmtree_calls = 0

    def simulated_is_symlink(path: Path) -> bool:
        return (link_kind == "symlink" and path == temporary) or original_is_symlink(
            path
        )

    def simulated_is_junction(path: Path) -> bool:
        return (link_kind == "junction" and path == temporary) or original_is_junction(
            path
        )

    def protected_unlink(path: Path, *args: object, **kwargs: object) -> None:
        nonlocal unlink_calls
        if path == temporary:
            unlink_calls += 1
            raise AssertionError("temporary link was unlinked")
        original_unlink(path, *args, **kwargs)

    def protected_rmdir(path: Path, *args: object, **kwargs: object) -> None:
        nonlocal rmdir_calls
        if path == temporary:
            rmdir_calls += 1
            raise AssertionError("temporary junction was removed")
        original_rmdir(path, *args, **kwargs)

    def protected_rmtree(path: object, *args: object, **kwargs: object) -> None:
        nonlocal rmtree_calls
        if Path(path) == temporary:
            rmtree_calls += 1
            raise AssertionError("temporary link tree was removed")
        original_rmtree(path, *args, **kwargs)

    monkeypatch.setattr(Path, "is_symlink", simulated_is_symlink)
    monkeypatch.setattr(Path, "is_junction", simulated_is_junction)
    monkeypatch.setattr(Path, "unlink", protected_unlink)
    monkeypatch.setattr(Path, "rmdir", protected_rmdir)
    monkeypatch.setattr(shutil, "rmtree", protected_rmtree)

    with pytest.raises(GpuArchiveError, match="temporary|link|junction"):
        extract_gpu_document(download, tmp_path / "cache")

    assert unlink_calls == 0
    assert rmdir_calls == 0
    assert rmtree_calls == 0


def test_stale_extraction_temporary_directory_fails_closed_and_is_preserved(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    download = _download(tmp_path / "cache", monkeypatch)
    root = tmp_path / "cache" / "x" / download.sha256[:16]
    temporary = root.with_name(f"{root.name}.part")
    temporary.mkdir(parents=True)
    sentinel = temporary / "manual-recovery.txt"
    sentinel.write_bytes(b"preserve-stale-temporary")

    with pytest.raises(GpuArchiveError, match="temporary|manual|recovery"):
        extract_gpu_document(download, tmp_path / "cache")

    assert sentinel.read_bytes() == b"preserve-stale-temporary"


def test_duplicate_extraction_manifest_key_forces_verified_rebuild(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    download = _download(tmp_path / "cache", monkeypatch)
    first = extract_gpu_document(download, tmp_path / "cache")
    manifest = first.extraction_root / gpu.EXTRACTION_MANIFEST_NAME
    payload = json.loads(manifest.read_text(encoding="utf-8"))
    manifest.write_text(
        "{"
        f'"schema_version":{payload["schema_version"]},'
        f'"archive_sha256":"{payload["archive_sha256"]}",'
        f'"archive_sha256":"{payload["archive_sha256"]}",'
        f'"files":{json.dumps(payload["files"])}'
        "}",
        encoding="utf-8",
    )

    rebuilt = extract_gpu_document(download, tmp_path / "cache")

    assert not rebuilt.cache_hit
    assert not rebuilt.extraction_root.with_name(
        f"{rebuilt.extraction_root.name}.bak"
    ).exists()


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


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("sha256", "0" * 64),
        ("file_size", 1),
        ("filename", "other.zip"),
        ("archive_format", "7z"),
    ],
)
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


@pytest.mark.parametrize("mutation", ["content", "deleted", "added", "path"])
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


def _extraction_from_archive(path: Path, tmp_path: Path) -> GpuExtraction:
    config = _config()
    document = gpu.GpuDocumentMetadata(
        provider=config.provider,
        portal=config.portal,
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
        source_url=build_gpu_partition_download_url(config),
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


def test_spatial_inventory_and_inspection_preserve_source_quality(
    tmp_path: Path,
) -> None:
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


def test_missing_zoning_layer_fails_clearly(tmp_path: Path) -> None:
    source = _planning_archive(tmp_path)
    extraction = _extraction_from_archive(source, tmp_path)
    payload = _config().model_dump(mode="json")
    payload["spatial_layers"]["zoning"]["match_tokens"] = ["missing"]
    with pytest.raises(GpuSpatialInspectionError, match="zoning"):
        inspect_gpu_planning_document(
            extraction, GpuSourceConfig.model_validate(payload)
        )


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


def _config_with_shared_role_token(
    first_role: str,
    second_role: str,
    token: str,
) -> GpuSourceConfig:
    payload = _config().model_dump(mode="python")
    payload["spatial_layers"][first_role]["match_tokens"] = [token]
    payload["spatial_layers"][second_role]["match_tokens"] = [token]
    return GpuSourceConfig.model_validate(payload)


@pytest.mark.parametrize(
    ("first_role", "second_role", "token"),
    [
        ("zoning", "prescription_surface", "zone_urba"),
        ("prescription_surface", "prescription_line", "prescription_surf"),
        ("prescription_surface", "information_surface", "prescription_surf"),
    ],
)
def test_inspection_rejects_one_physical_layer_for_two_logical_roles(
    tmp_path: Path,
    first_role: str,
    second_role: str,
    token: str,
) -> None:
    extraction = _extraction_from_archive(_planning_archive(tmp_path), tmp_path)
    config = _config_with_shared_role_token(first_role, second_role, token)

    with pytest.raises(GpuSpatialInspectionError, match="role|logical|same layer"):
        inspect_gpu_planning_document(extraction, config)


def test_inspection_rejects_mutated_config_before_layer_discovery(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    extraction = _extraction_from_archive(_planning_archive(tmp_path), tmp_path)
    forged = _config().model_copy(update={"provider": "UNTRUSTED"})
    discovery_calls = 0

    def counted(*args: object, **kwargs: object) -> object:
        nonlocal discovery_calls
        discovery_calls += 1
        raise AssertionError("layer discovery ran for an invalid config")

    monkeypatch.setattr(gpu, "discover_gpu_spatial_layers", counted)

    with pytest.raises(GpuSpatialInspectionError, match="config|provider"):
        inspect_gpu_planning_document(extraction, forged)

    assert discovery_calls == 0


def test_inspection_rejects_archive_byte_mutation_before_layer_discovery(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    archive = _planning_archive(tmp_path)
    extraction = _extraction_from_archive(archive, tmp_path)
    archive.write_bytes(archive.read_bytes() + b"post-extraction-mutation")
    discovery_calls = 0

    def counted(*args: object, **kwargs: object) -> object:
        nonlocal discovery_calls
        discovery_calls += 1
        raise AssertionError("layer discovery ran after archive mutation")

    monkeypatch.setattr(gpu, "discover_gpu_spatial_layers", counted)

    with pytest.raises(GpuSpatialInspectionError, match="archive|source|config"):
        inspect_gpu_planning_document(extraction, _config())

    assert discovery_calls == 0


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("commune_code", "99999"),
        ("partition", "DU_99999"),
        ("document_type", ""),
        (
            "source_url",
            "https://www.geoportail-urbanisme.gouv.fr/api/document/download-by-partition/DU_99999",
        ),
    ],
)
def test_inspection_rejects_document_lineage_not_matching_config(
    tmp_path: Path,
    field: str,
    value: str,
) -> None:
    extraction = _extraction_from_archive(_planning_archive(tmp_path), tmp_path)
    document = replace(extraction.archive.document, **{field: value})
    forged = replace(
        extraction,
        archive=replace(extraction.archive, document=document),
    )

    with pytest.raises(
        GpuSpatialInspectionError,
        match="config|commune|partition|URL|type|planning",
    ):
        inspect_gpu_planning_document(forged, _config())


def test_planning_document_records_and_revalidates_exact_config_identity(
    tmp_path: Path,
) -> None:
    extraction = _extraction_from_archive(_planning_archive(tmp_path), tmp_path)
    result = inspect_gpu_planning_document(extraction, _config())

    assert result.source_config == _config()
    assert result.source_config_sha256 == gpu._source_config_sha256(_config())
    forged = replace(result, source_config_sha256="0" * 64)
    with pytest.raises(GpuSpatialInspectionError, match="config|SHA"):
        gpu.revalidate_gpu_spatial_layer_source(forged, forged.zoning)
    malformed_inventory = replace(
        result,
        all_spatial_layers=list(result.all_spatial_layers),  # type: ignore[arg-type]
    )
    with pytest.raises(GpuSpatialInspectionError, match="inventory|tuple"):
        gpu.revalidate_gpu_spatial_layer_source(
            malformed_inventory,
            malformed_inventory.zoning,
        )


def test_source_complete_revalidation_rejects_coordinated_spatial_omission(
    tmp_path: Path,
) -> None:
    extraction = _extraction_from_archive(_planning_archive(tmp_path), tmp_path)
    result = inspect_gpu_planning_document(extraction, _config())
    forged = replace(
        result,
        all_spatial_layers=(result.zoning.reference,),
        related_layers=(),
    )

    with pytest.raises(GpuSpatialInspectionError, match="spatial inventory|physical"):
        gpu.revalidate_gpu_spatial_layer_source(forged, forged.zoning)


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
    monkeypatch.setattr(
        gpu, "open_safe_https", lambda *args, **kwargs: _Response(_zip_bytes())
    )
    assert not download_gpu_document(changed, _config(), tmp_path).cache_hit
```

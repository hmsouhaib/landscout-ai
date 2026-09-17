# `tests/unit/test_gpu_fr.py`

## File identity

- Repository path: `tests/unit/test_gpu_fr.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Tests GPU config, discovery, cache/extraction recovery and source-bound spatial inspection using mocked transport and synthetic local files; coverage is limited to the explicit assertions in this file.
- Source SHA256: `e03d758f96f52b143f2908557cea2b10c087316d73a093ddf0174f86abe46622`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for gpu fr; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Tests GPU config, discovery, cache/extraction recovery and source-bound spatial inspection using mocked transport and synthetic local files; coverage is limited to the explicit assertions in this file.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to its actual fixtures, attacks and assertions. The per-callable prose below is the behavioral explanation; exact code blocks and call-expression tables are verification aids, not substitutes for that explanation. `GpuSourceConfig.model_validate` is the model-facing Pydantic API inherited from `BaseModel`, not a method implemented in this test or overridden in `gpu_fr`.

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
  - Used by the parametrization decorators on `test_discovery_rejects_unsafe_archive_name` and `test_download_rejects_forged_unsafe_archive_name_before_io`; the sixteen literal values are reused at both public boundaries.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `_Response`

**Source purpose:** In-memory response fixture implementing the context-manager protocol expected by the GPU transport consumer. It inherits `io.BytesIO` storage and read behavior; its own exit method closes that buffer. It owns no socket, HTTP headers or new fields.

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

**Purpose, ordered behavior and effects:** Return the same in-memory byte stream for a `with` statement; no HTTP connection or filesystem stream is opened.

**Exact signature**

```python
def __enter__(self) -> Self:
```

- Exact decorators: none.
- Declared return annotation: `Self`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | not annotated | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
- No calls.

**Complete source-ordered implementation**

```python
def __enter__(self) -> Self:
        return self
```

### `_Response.__exit__`

**Purpose, ordered behavior and effects:** Close the inherited `io.BytesIO` buffer on context exit, ignoring the exception arguments and returning `None`, so any active exception is not suppressed. This changes only the in-memory stream state.

**Exact signature**

```python
def __exit__(self, *args: object) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | not annotated | `required` |
| `*args` | variadic positional | `object` | `variadic` |

**Return and exception contract**


**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `self.close` | `io.BytesIO.close` (inherited by `_Response`; no local override) |

**Complete source-ordered implementation**

```python
def __exit__(self, *args: object) -> None:
        self.close()
```

### `_config`

**Purpose, ordered behavior and effects:** Load the checked-in `configs/sources/gpu_fr.yaml` through the real strict loader and return its validated immutable `GpuSourceConfig`. This helper reads local YAML; it does not contact the GPU API.

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

**Complete source-ordered implementation**

```python
def _config() -> GpuSourceConfig:
    return load_gpu_source_config(Path("configs/sources/gpu_fr.yaml"))
```

### `_listing_item`

**Purpose, ordered behavior and effects:** Create a new mutable listing-response dictionary for current, approved, in-force `doc-1`, type `PLU`, archive `31395_PLU_20240215`, partition `DU_31395` and Muret grid. Apply keyword overrides to that new dictionary and return it; it is a synthetic API payload, not validated source evidence.

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

### `_details`

**Purpose, ordered behavior and effects:** Start with a fresh listing payload, add synthetic Muret title/producer, EPSG:2154, publication/update strings, metadata ID, official archive URL and written-material URL mapping, then apply the supplied overrides. Only the new dictionary is mutated; no metadata or document is fetched.

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

### `_files`

**Purpose, ordered behavior and effects:** Return a new one-item mutable files-list payload naming `reglement.pdf`, its accented written-regulation title and `Règlements` path. This describes a synthetic API response; it does not create or read a PDF.

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

**Complete source-ordered implementation**

```python
def _files() -> list[dict[str, object]]:
    return [{"name": "reglement.pdf", "title": "Règlement écrit", "path": "Règlements"}]
```

### `_patch_json_responses`

**Purpose, ordered behavior and effects:** Retain an iterator over the supplied response sequence and monkeypatch `gpu.open_safe_https` with the nested opener for this test. The patch replaces the shared transport entry point, bypassing real DNS, socket validation and HTTP while leaving the GPU JSON decoder and document-selection logic active.

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
| `monkeypatch.setattr` | `pytest.MonkeyPatch.setattr` (test-scoped replacement; target described above) |

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

### `_patch_json_responses.opener`

**Purpose, ordered behavior and effects:** When the patched `gpu.open_safe_https` is called, consume the next supplied object, JSON-serialize and encode it, and return an in-memory `_Response`. Request arguments are ignored; exhaustion raises `StopIteration`, and no request URL or live network behavior is verified by this callback.

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

**Complete source-ordered implementation**

```python
def opener(*args: object, **kwargs: object) -> _Response:
        return _Response(json.dumps(next(responses)).encode())
```

### `_document`

**Purpose, ordered behavior and effects:** Install the ordered synthetic listing, detail and file responses, then call the real `discover_current_gpu_document(_config())` and return its metadata record. The function has no return annotation; its actual return is `GpuDocumentMetadata`, not `None`. Discovery/parsing is exercised, but transport and remote provenance are mocked.

**Exact signature**

```python
def _document(monkeypatch: pytest.MonkeyPatch):
```

- Exact decorators: none.
- Declared return annotation: absent (the actual return is `GpuDocumentMetadata`).

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `discover_current_gpu_document(_config())`

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

**Complete source-ordered implementation**

```python
def _document(monkeypatch: pytest.MonkeyPatch):
    _patch_json_responses(monkeypatch, [[_listing_item()], _details(), _files()])
    return discover_current_gpu_document(_config())
```

### `_zip_bytes`

**Purpose, ordered behavior and effects:** Write each entry of `files` into a DEFLATED ZIP held in `io.BytesIO`, close the ZIP and return immutable bytes. `None` and an empty dictionary both select the default `document/readme.txt` payload because the implementation uses `files or default`; no file is written to disk.

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

**Complete source-ordered implementation**

```python
def _zip_bytes(files: dict[str, bytes] | None = None) -> bytes:
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, content in (files or {"document/readme.txt": b"GPU"}).items():
            archive.writestr(name, content)
    return stream.getvalue()
```

### `_zip_member_bytes`

**Purpose, ordered behavior and effects:** Create an in-memory DEFLATED ZIP from the ordered member list, allowing duplicate names for hostile fixtures. Suppress only `UserWarning` during fixture construction, not warnings from the validator under test; return the completed bytes without filesystem or network I/O.

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

### `_download`

**Purpose, ordered behavior and effects:** Discover the synthetic document through `_document`, replace the transport with an in-memory ZIP response and invoke the real downloader in `tmp_path`. A falsey `archive_bytes` selects the default ZIP. The public downloader performs real temporary-file, ZIP, hash, sidecar and publication work on synthetic local bytes; HTTP and DNS are bypassed.

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

### `_planning_archive`

**Purpose, ordered behavior and effects:** Create a local synthetic package containing a real EPSG:2154 GeoPackage: three zoning polygons (valid square, invalid bow-tie, NULL) with raw label/code attributes and one prescription polygon. Write marker PDF bytes and a CNIG-standard XML file, then traverse and ZIP those regular files into `planning.zip`. GeoPandas/native GIS writing and local archive I/O are real; the PDF marker is not evidence of readable written regulations.

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

### `test_valid_config_and_urls`

**Purpose, ordered behavior and effects:** Load real checked-in YAML and assert the Muret partition is `DU_31395`, its listing query contains that partition, and its download URL ends with the exact partition endpoint. URL construction is exercised without network requests; substring/suffix assertions are not a full transport-safety test.

**Exact signature**

```python
def test_valid_config_and_urls() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

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

### `test_duplicate_gpu_yaml_key_is_rejected`

**Purpose, ordered behavior and effects:** Copy the checked-in YAML to a temporary file with a second `provider` key, invoke the real loader, and require `GpuConfigError` whose cause mentions a duplicate. The temporary write is the attack; parser rejection, not a later provider comparison, is asserted.

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

### `test_invalid_config_values_are_rejected`

**Purpose, ordered behavior and effects:** For nine declared path/value cases, dump a valid config to a mutable payload, replace one nested value and require Pydantic `ValidationError` during reconstruction. Cases cover a short commune code, file/HTTP/foreign/port/query API origins, wrong download strategy, empty partition template and negative cache age; no network or GIS work occurs.

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

### `test_mutated_loaded_api_origin_is_rejected_before_discovery_network`

**Purpose, ordered behavior and effects:** First require direct assignment to the frozen API config to fail immediately. Then deliberately bypass validation with nested `model_copy(update=...)` objects carrying a foreign API origin, install a counting transport failure and call public discovery. Require a controlled discovery error and zero transport calls, demonstrating boundary reconstruction independently of frozen assignment.

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

### `test_mutated_loaded_api_origin_is_rejected_before_discovery_network.fail_network`

**Purpose, ordered behavior and effects:** Installed as `gpu.open_safe_https`, increment the enclosing network counter and unconditionally raise `AssertionError` if invalid-origin discovery reaches transport. No HTTP is issued and there is no normal return.

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

- Explicit raise paths:
  - `AssertionError("network used after GPU origin mutation")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |

**Complete source-ordered implementation**

```python
def fail_network(*args: object, **kwargs: object) -> object:
        nonlocal network_calls
        network_calls += 1
        raise AssertionError("network used after GPU origin mutation")
```

### `test_gpu_source_identity_is_exact`

**Purpose, ordered behavior and effects:** For `provider` and `portal` separately, replace the field in a mutable dump with `UNTRUSTED` and require `GpuSourceConfig.model_validate` to raise `ValidationError`. This verifies exact configured source identity, not a live producer response.

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

**Complete source-ordered implementation**

```python
def test_gpu_source_identity_is_exact(field: str) -> None:
    payload = _config().model_dump(mode="python")
    payload[field] = "UNTRUSTED"

    with pytest.raises(ValidationError):
        GpuSourceConfig.model_validate(payload)
```

### `test_gpu_cache_age_rejects_coercion_and_nonfinite`

**Purpose, ordered behavior and effects:** Replace `cache.max_age_hours` with each of `True`, text `168`, NaN and infinity, and require immediate Pydantic validation failure. Four declared cases isolate coercion/non-finite rejection after reading the valid local config.

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

**Complete source-ordered implementation**

```python
def test_gpu_cache_age_rejects_coercion_and_nonfinite(value: object) -> None:
    payload = _config().model_dump(mode="python")
    payload["cache"]["max_age_hours"] = value

    with pytest.raises(ValidationError):
        GpuSourceConfig.model_validate(payload)
```

### `test_gpu_source_config_identity_is_deterministic_and_content_bound`

**Purpose, ordered behavior and effects:** Reconstruct a config from the same outer mapping in reverse insertion order and compare its computed config SHA with the original. Then change cache age from 168 to 169 in a fresh dump and require a different SHA. This tests semantic config hashing, not YAML-byte identity or all possible field mutations.

**Exact signature**

```python
def test_gpu_source_config_identity_is_deterministic_and_content_bound() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

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

### `test_unknown_config_field_is_rejected`

**Purpose, ordered behavior and effects:** Add root key `unexpected` to a mutable config dump and require `ValidationError` on reconstruction. The checked-in YAML and original immutable model remain unchanged.

**Exact signature**

```python
def test_unknown_config_field_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

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

**Complete source-ordered implementation**

```python
def test_unknown_config_field_is_rejected() -> None:
    payload = _config().model_dump(mode="json")
    payload["unexpected"] = True
    with pytest.raises(ValidationError):
        GpuSourceConfig.model_validate(payload)
```

### `test_document_discovery_success`

**Purpose, ordered behavior and effects:** Run real discovery over the ordered in-memory API fixtures and check document ID, type, effective status, archive name, absent version, written-file title and canonical official file URL. These are fixture-backed parsing/selection assertions, not a new real-source discovery.

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

### `test_gpu_api_json_is_strict_before_document_selection`

**Purpose, ordered behavior and effects:** Patch the transport to return raw bytes containing a duplicate ID key, NaN or Infinity, and require a controlled JSON/metadata discovery error in each of three cases. Raw bytes deliberately bypass `json.dumps` so the strict decoder, rather than fixture serialization, sees the malformed JSON.

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

### `test_written_material_url_must_be_exact_official_https_api_url`

**Purpose, ordered behavior and effects:** Supply an HTTP or unrelated-HTTPS written-material URL in otherwise consistent listing/detail/file responses. Require discovery to reject the written-material URL; the API responses are in-memory, so this establishes lexical provenance enforcement rather than DNS/socket safety.

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

### `test_written_material_fallback_rejects_unsafe_archive_url_provenance`

**Purpose, ordered behavior and effects:** Remove `writingMaterials`, supply an unsafe HTTP or foreign-HTTPS archive URL and retain the files-list fallback fixture. Require an archive-URL discovery error in both cases; fallback must not conceal the unsafe archive provenance.

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

### `test_no_current_document_is_rejected`

**Purpose, ordered behavior and effects:** Provide only a listing item with deleted status and require discovery to raise a `No current` error. The one-response iterator ensures selection ends without fetching details for a non-current document.

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

**Complete source-ordered implementation**

```python
def test_no_current_document_is_rejected(monkeypatch: pytest.MonkeyPatch) -> None:
    _patch_json_responses(monkeypatch, [[_listing_item(status="document.deleted")]])
    with pytest.raises(GpuDiscoveryError, match="No current"):
        discover_current_gpu_document(_config())
```

### `test_ambiguous_current_documents_are_rejected`

**Purpose, ordered behavior and effects:** Provide two distinct otherwise-current document IDs in the listing and require an ambiguous-selection error. No arbitrary first-document selection is accepted and no detail response is supplied.

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

**Complete source-ordered implementation**

```python
def test_ambiguous_current_documents_are_rejected(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _patch_json_responses(monkeypatch, [[_listing_item(), _listing_item(id="doc-2")]])
    with pytest.raises(GpuDiscoveryError, match="Ambiguous"):
        discover_current_gpu_document(_config())
```

### `test_missing_document_identity_is_rejected`

**Purpose, ordered behavior and effects:** Remove `id`, `originalName` or `type` from an otherwise valid listing dictionary, one field per case. Feed that listing through real discovery and require a missing-identity error before detail retrieval.

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

### `test_document_details_must_match_selected_listing`

**Purpose, ordered behavior and effects:** Keep the selected listing fixed and change one of seven detail fields: ID, archive name, partition name, type, status, legal status or effective status. Require a mismatch/changed/current discovery error; details cannot silently replace the selected identity or eligibility state.

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

### `test_document_details_commune_must_match_selected_listing`

**Purpose, ordered behavior and effects:** Keep the valid Muret listing but replace the detail grid with commune `99999`. Require discovery to reject the mismatch rather than trusting a consistent-looking document ID alone.

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

### `test_discovery_rejects_unsafe_archive_name`

**Purpose, ordered behavior and effects:** Apply each of the sixteen `_UNSAFE_ARCHIVE_NAMES` to both listing and detail archive names while supplying normal file metadata. Require an archive-name/safety discovery error for traversal, absolute/drive paths, dot names, whitespace/control characters, Windows device/forbidden names, repeated ZIP suffix and overlength input.

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

### `test_successful_download_persists_sha_and_sidecar`

**Purpose, ordered behavior and effects:** Download a synthetic ZIP through the mocked transport using real cache publication, then read the sidecar and check physical archive existence, positive size, 64-character SHA, sidecar/result SHA agreement, document ID and absence of top-level `.part` files. These assertions do not independently recompute the digest.

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

### `test_download_rejects_document_inconsistent_with_config`

**Purpose, ordered behavior and effects:** Forge one of nine metadata fields/values with `dataclasses.replace`, including source identity, commune/partition/state and unrelated or wrong-partition URLs. Replace transport with `pytest.fail`, call the public downloader and require `GpuDownloadError` plus an entirely empty temporary destination directory.

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

### `test_download_rejects_forged_written_file_provenance_before_network`

**Purpose, ordered behavior and effects:** Replace written files with either a record carrying an HTTP source URL or an object of the wrong runtime type. Install a counting failing transport; require a controlled download error and zero calls in both cases, demonstrating provenance/type checks before network use.

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

### `test_download_rejects_forged_written_file_provenance_before_network.fail_network`

**Purpose, ordered behavior and effects:** Installed at `gpu.open_safe_https`, increment the closed-over counter and unconditionally raise `AssertionError` if forged written-file provenance reaches transport. It performs no actual network work and cannot return normally.

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

- Explicit raise paths:
  - `AssertionError("forged written-file provenance reached network")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |

**Complete source-ordered implementation**

```python
def fail_network(*args: object, **kwargs: object) -> object:
        nonlocal network_calls
        network_calls += 1
        raise AssertionError("forged written-file provenance reached network")
```

### `test_download_rejects_forged_unsafe_archive_name_before_io`

**Purpose, ordered behavior and effects:** Forge each of the same sixteen unsafe archive names on an otherwise discovered document, replace transport with a failure sentinel, and require a controlled download error. The explicit filesystem assertion is that `tmp_path/escape.zip` does not exist; it is not an assertion that every possible path was untouched.

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

### `test_archive_name_with_one_zip_suffix_is_not_duplicated`

**Purpose, ordered behavior and effects:** Forge the safe already-suffixed archive name `safe-name.zip`, serve valid ZIP bytes through the mock and run real download/cache publication. Require both the result filename and path to contain exactly one `.zip` suffix.

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

### `test_fresh_cache_is_reused`

**Purpose, ordered behavior and effects:** Populate a real local cache with synthetic ZIP bytes, then replace transport with `pytest.fail` and download the same document again. Require `cache_hit=True` and unchanged SHA; the second call performs local verification without reaching the patched HTTP entry point.

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

### `test_boolean_cache_integrity_counts_are_not_accepted_as_integers`

**Purpose, ordered behavior and effects:** For sidecar `file_size` and `member_count`, set both numeric expectations to one and replace only the selected field with `True`. Mock archive size, ZIP member list and SHA to matching values, then require the private cache loader to return `None`. These two cases isolate bool-versus-int validation; the mocked physical checks do not certify a real one-byte ZIP.

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

### `test_boolean_cache_integrity_counts_are_not_accepted_as_integers.one_byte_archive_stat`

**Purpose, ordered behavior and effects:** Installed as `Path.stat`, call the saved real stat first; for the cached archive only, copy its tuple fields, set size slot 6 to one and return a new `os.stat_result`. Other paths retain their real result. The filesystem read comes from `original_stat`, not construction of `os.stat_result`.

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

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `original_stat` | pathlib.Path.stat (saved before monkeypatch) |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `os.stat_result` | `os.stat_result` |

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

### `test_stale_recovery_backup_rejects_cache_before_network`

**Purpose, ordered behavior and effects:** Populate the cache, write a manual-recovery archive backup, install a failing transport and invoke the downloader again. Require a backup/recovery/manual error and exact preservation of the backup bytes; the otherwise usable cache may not consume unresolved recovery material.

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

### `test_stale_recovery_backup_rejects_cache_before_network.fail_network`

**Purpose, ordered behavior and effects:** Installed as the transport replacement, unconditionally call `pytest.fail` if download attempts network access while a recovery backup exists. The `_Response` annotation does not imply a normal return.

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


**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.fail` | `pytest.fail` |

**Complete source-ordered implementation**

```python
def fail_network(*args: object, **kwargs: object) -> _Response:
        pytest.fail("stale recovery must fail before network")
```

### `test_expired_cache_is_refreshed`

**Purpose, ordered behavior and effects:** Rewrite the cached sidecar timestamp to eight days before the test clock, supply different valid ZIP bytes through the transport mock and run download again. Require a non-cache-hit result with changed SHA, exercising real replacement of expired local bytes.

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

### `test_failed_refresh_preserves_previous_cache`

**Purpose, ordered behavior and effects:** Expire a real synthetic cache, retain exact old archive/sidecar bytes and replace transport with an injected offline `URLError`. Require `GpuDownloadError`, byte-for-byte preservation of both old cache files and no top-level `.part` remnants.

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

### `test_failed_refresh_preserves_previous_cache.fail`

**Purpose, ordered behavior and effects:** Installed as `gpu.open_safe_https`, always raise `URLError('offline')` to trigger the downloader's controlled transport-failure path without a real request. It never returns a response.

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

- Explicit raise paths:
  - `URLError("offline")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `URLError` | `urllib.error.URLError` |

**Complete source-ordered implementation**

```python
def fail(*args: object, **kwargs: object) -> _Response:
        raise URLError("offline")
```

### `test_metadata_publication_failure_rolls_back_both_cache_files`

**Purpose, ordered behavior and effects:** Expire a populated cache, retain exact old bytes, supply refresh ZIP bytes and patch `_replace_file` to fail once when publishing the new sidecar. Require `GpuDownloadError`, restoration of both original files and absence of `.part` and `.bak` remnants after successful rollback.

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

### `test_metadata_publication_failure_rolls_back_both_cache_files.fail_new_metadata_once`

**Purpose, ordered behavior and effects:** Installed as `gpu._replace_file`, raise `OSError` once for a `.part` source targeting the metadata sidecar and set the closed-over failure flag. Delegate every other call to the saved real replacement helper, so rollback and its filesystem writes remain real.

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

- Explicit raise paths:
  - `OSError("simulated metadata lock")` under lexical guard `source.suffix == ".part" and target == sidecar_path and not failed`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `OSError` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_replace` | landscout.sources.gpu_fr._replace_file (saved before monkeypatch) |

**Complete source-ordered implementation**

```python
def fail_new_metadata_once(source: Path, target: Path) -> None:
        nonlocal failed
        if source.suffix == ".part" and target == sidecar_path and not failed:
            failed = True
            raise OSError("simulated metadata lock")
        original_replace(source, target)
```

### `test_publication_and_rollback_failure_preserves_exact_recovery_backups`

**Purpose, ordered behavior and effects:** Create simple old/new byte files and call the private cache-pair publisher directly while injecting failures for new-sidecar publication and old-archive restoration. Require a rollback error and exact old archive and metadata bytes in both backups. These are publication-state fixtures, not validated ZIP archives.

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

### `test_publication_and_rollback_failure_preserves_exact_recovery_backups.fail_publication_and_rollback`

**Purpose, ordered behavior and effects:** Installed as `_replace_file`, raise `OSError` for the selected new-metadata move and archive-backup rollback; delegate all other replacements to the original helper. This makes two particular filesystem transitions fail without globally disabling publication.

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
| `original_replace` | landscout.sources.gpu_fr._replace_file (saved before monkeypatch) |

**Complete source-ordered implementation**

```python
def fail_publication_and_rollback(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        if source == archive_backup and target == archive_path:
            raise OSError("simulated archive rollback failure")
        original_replace(source, target)
```

### `test_cleanup_failure_does_not_mask_double_failure_recovery_error`

**Purpose, ordered behavior and effects:** Expire a real synthetic cache and inject sidecar-publication failure, archive-rollback failure, then temporary-sidecar unlink failure. Require the public downloader's error still to mention rollback and both recovery backups to preserve the exact old bytes; cleanup failure must not replace the primary recovery diagnosis.

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

### `test_cleanup_failure_does_not_mask_double_failure_recovery_error.fail_publication_and_rollback`

**Purpose, ordered behavior and effects:** Replace `_replace_file` only for the chosen new-sidecar publication and archive-backup restoration. On the latter set `rollback_failed` before raising, enabling the separate unlink fault; other calls perform real saved replacements.

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
| `original_replace` | landscout.sources.gpu_fr._replace_file (saved before monkeypatch) |

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

### `test_cleanup_failure_does_not_mask_double_failure_recovery_error.fail_temporary_cleanup`

**Purpose, ordered behavior and effects:** Installed as `Path.unlink`, raise `PermissionError` only after the rollback-failure flag is set and only for the temporary sidecar. Otherwise invoke the saved real unlink with the supplied `missing_ok`; this callback may remove other temporary files.

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

- Explicit raise paths:
  - `PermissionError("simulated temporary cleanup failure")` under lexical guard `rollback_failed and path == temporary_metadata`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `PermissionError` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_unlink` | pathlib.Path.unlink (saved before monkeypatch) |

**Complete source-ordered implementation**

```python
def fail_temporary_cleanup(path: Path, *, missing_ok: bool = False) -> None:
        if rollback_failed and path == temporary_metadata:
            raise PermissionError("simulated temporary cleanup failure")
        original_unlink(path, missing_ok=missing_ok)
```

### `test_stale_cache_recovery_backup_fails_closed_without_destroying_it`

**Purpose, ordered behavior and effects:** Create old cache files, candidate replacement files and a pre-existing manual archive backup, then call the private publisher. Require a recovery/manual error and exact preservation of both old targets and the manual backup. The fixtures isolate publication safeguards, without ZIP or source-discovery validation.

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

### `test_preexisting_temporary_archive_symlink_cannot_modify_target`

**Purpose, ordered behavior and effects:** Simulate the expected temporary archive path being a symlink by monkeypatching `Path.is_symlink`, and redirect any attempted opening of it to a protected sentinel file. Invoke the real downloader with a counted response mock; require a download error, zero transport calls and unchanged sentinel bytes. No OS symlink is created.

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

### `test_preexisting_temporary_archive_symlink_cannot_modify_target.simulated_is_symlink`

**Purpose, ordered behavior and effects:** Installed as `Path.is_symlink`, return true for the attack temporary path and otherwise call the saved real metadata check. This simulates a link classification; it does not create or alter a link.

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

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `original_is_symlink` | pathlib.Path.is_symlink (saved before monkeypatch) |

**Complete source-ordered implementation**

```python
def simulated_is_symlink(path: Path) -> bool:
        return path == temporary_archive or original_is_symlink(path)
```

### `test_preexisting_temporary_archive_symlink_cannot_modify_target.simulated_symlink_open`

**Purpose, ordered behavior and effects:** Installed as `Path.open`, redirect only the attack temporary path to the sentinel and delegate every other open unchanged, preserving all mode arguments. If reached with a write mode this would affect the sentinel; the enclosing regression requires rejection before that unsafe opening.

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

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `original_open` | pathlib.Path.open (saved before monkeypatch) |

**Complete source-ordered implementation**

```python
def simulated_symlink_open(path: Path, *args: object, **kwargs: object) -> object:
        if path == temporary_archive:
            return original_open(sentinel, *args, **kwargs)
        return original_open(path, *args, **kwargs)
```

### `test_preexisting_temporary_archive_symlink_cannot_modify_target.record_network`

**Purpose, ordered behavior and effects:** Installed as the mocked transport, increment the enclosing opener count and return a fresh in-memory valid ZIP response. It performs no HTTP; a correct early link rejection leaves its count at zero.

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

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_Response` | `tests.unit.test_gpu_fr._Response` |
| `_zip_bytes` | `tests.unit.test_gpu_fr._zip_bytes` |

**Complete source-ordered implementation**

```python
def record_network(*args: object, **kwargs: object) -> _Response:
        nonlocal opener_calls
        opener_calls += 1
        return _Response(_zip_bytes())
```

### `test_corrupt_download_is_rejected`

**Purpose, ordered behavior and effects:** Serve non-ZIP bytes after synthetic document discovery and call the real downloader. Require `GpuDownloadError` and no top-level `.part` files, exercising validation and cleanup of a physically written corrupt temporary archive.

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

### `test_tampered_sidecar_invalidates_cache`

**Purpose, ordered behavior and effects:** Populate a synthetic cache, replace its recorded SHA with sixty-four zeroes, supply valid ZIP bytes through the mock and download again. Require a fresh result rather than a cache hit, proving a sidecar checksum claim alone cannot authorize reuse.

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

### `test_archive_path_traversal_is_rejected`

**Purpose, ordered behavior and effects:** Write a real temporary ZIP containing `../escape.txt`, then require `validate_gpu_archive` to raise an unsafe-path archive error. The test validates ZIP metadata/member safety without extracting the attack entry.

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

**Complete source-ordered implementation**

```python
def test_archive_path_traversal_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "unsafe.zip"
    path.write_bytes(_zip_bytes({"../escape.txt": b"bad"}))
    with pytest.raises(GpuArchiveError, match="Unsafe"):
        validate_gpu_archive(path)
```

### `test_archive_symlink_is_rejected`

**Purpose, ordered behavior and effects:** Write a ZIP member with Unix symlink mode bits and a target string payload, then require the real archive validator to reject symbolic links. The ZIP file and `ZipInfo` attributes are real fixture bytes; no filesystem symlink is created.

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

### `test_duplicate_zip_extraction_targets_are_rejected`

**Purpose, ordered behavior and effects:** Write four hostile ZIP fixtures covering duplicate raw names, slash/backslash aliases, dot-component aliases and case-folded aliases. Require duplicate/collision archive errors; `_zip_member_bytes` suppresses only the expected fixture-construction warning.

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

### `test_zip_file_directory_target_collision_is_rejected`

**Purpose, ordered behavior and effects:** Write a ZIP containing file `blocked` and child `blocked/child.txt`, then require a collision/target archive error. A file cannot simultaneously act as a parent extraction directory.

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

### `test_zip_cannot_claim_extraction_manifest_path`

**Purpose, ordered behavior and effects:** Write a ZIP with an entry underneath the reserved extraction-manifest name and require an archive error mentioning the manifest. This rejects collision with the local integrity marker before extraction.

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

### `test_extraction_inventory_and_cache`

**Purpose, ordered behavior and effects:** Download and extract a synthetic two-member archive, then verify sorted relative paths, metadata/written-regulation categories and a cache hit on repeat extraction. Read the schema-2 manifest and compare its archive SHA and exact path/size/SHA records with the returned inventory; assert no `.part` entries in the checked extraction-cache location.

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

### `test_extraction_manifest_is_created_exclusively`

**Purpose, ordered behavior and effects:** Wrap `Path.open` while performing a real synthetic extraction, recording only accesses to the manifest filename. Require the exact mode sequence `['x', 'rb']`: exclusive creation followed by byte verification, not an overwrite mode.

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

### `test_extraction_manifest_is_created_exclusively.observed_open`

**Purpose, ordered behavior and effects:** Installed as `Path.open`, append the mode only when the filename is the extraction manifest, then delegate every open to the saved real method. The callback records in-memory observations while preserving actual local reads, writes and their errors.

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

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `manifest_modes.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_open` | pathlib.Path.open (saved before monkeypatch) |

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

### `test_stale_extraction_backup_fails_closed_and_is_preserved`

**Purpose, ordered behavior and effects:** Extract a valid synthetic archive, create a sibling `.bak` directory containing a sentinel, and attempt extraction again. Require a recovery/manual error, unchanged sentinel bytes and an intact current extraction directory; even an otherwise reusable cache must preserve unresolved backup material.

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

### `test_extraction_publication_and_rollback_failure_preserves_backup`

**Purpose, ordered behavior and effects:** Add an unexpected sentinel to a real extracted tree so reuse fails, then inject both replacement-tree publication and backup-restoration failures. Require a rollback error and preserved sentinel in the backup; a second call must reject that remaining backup as manual recovery and preserve it again.

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

### `test_extraction_publication_and_rollback_failure_preserves_backup.fail_publication_and_rollback`

**Purpose, ordered behavior and effects:** Installed as `shutil.move`, compare converted source/target paths and fail only temporary-tree publication or backup restoration to the current root. Delegate other moves to the saved real function, allowing the initial backup transition to occur.

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
| `original_move` | shutil.move (saved before monkeypatch) |

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

### `test_extraction_publication_failure_restores_existing_root`

**Purpose, ordered behavior and effects:** Invalidate a synthetic extraction by adding a sentinel and inject failure only when the replacement temporary tree moves to the root. Require a publication error, sentinel restored at its original location and no remaining backup, proving successful rollback of the old directory.

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

### `test_extraction_publication_failure_restores_existing_root.fail_publication`

**Purpose, ordered behavior and effects:** Installed as `shutil.move`, reject the exact temporary-to-root transition and delegate all other moves, including backup restoration, to the saved real function. This isolates publication failure from rollback failure.

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
| `original_move` | shutil.move (saved before monkeypatch) |

**Complete source-ordered implementation**

```python
def fail_publication(source: str, target: str) -> object:
        if Path(source) == temporary and Path(target) == extracted.extraction_root:
            raise OSError("simulated extraction publication failure")
        return original_move(source, target)
```

### `test_extraction_backup_move_failure_preserves_existing_root`

**Purpose, ordered behavior and effects:** Add a sentinel to an extracted tree and inject failure on the initial current-root-to-backup move. Require a controlled backup-failed error, unchanged sentinel and no created backup; the old root must not be removed because a backup attempt failed.

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

### `test_extraction_backup_move_failure_preserves_existing_root.fail_initial_backup`

**Purpose, ordered behavior and effects:** Installed as `shutil.move`, raise only for the exact initial root-to-backup transition and delegate other moves. The failure is injected before moving the original tree.

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
| `original_move` | shutil.move (saved before monkeypatch) |

**Complete source-ordered implementation**

```python
def fail_initial_backup(source: str, target: str) -> object:
        if Path(source) == extracted.extraction_root and Path(target) == backup:
            raise OSError("simulated initial backup failure")
        return original_move(source, target)
```

### `test_extraction_inventory_rejects_special_entry`

**Purpose, ordered behavior and effects:** Create a regular local file, then monkeypatch its `is_file` and `is_dir` answers to false while leaving other paths genuine. Require the private inventory routine to reject a special filesystem entry; this is a simulated classification, not a created device or socket.

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

### `test_extraction_inventory_rejects_special_entry.simulated_is_file`

**Purpose, ordered behavior and effects:** Installed as `Path.is_file`, return false for the designated synthetic special entry and otherwise execute the saved real metadata query. No filesystem type is actually changed.

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

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `original_is_file` | pathlib.Path.is_file (saved before monkeypatch) |

**Complete source-ordered implementation**

```python
def simulated_is_file(path: Path) -> bool:
        return False if path == special else original_is_file(path)
```

### `test_extraction_inventory_rejects_special_entry.simulated_is_dir`

**Purpose, ordered behavior and effects:** Installed as `Path.is_dir`, return false for the same designated entry and otherwise execute the saved real directory check. Together with the file-check patch it drives the special-entry rejection path.

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

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `original_is_dir` | pathlib.Path.is_dir (saved before monkeypatch) |

**Complete source-ordered implementation**

```python
def simulated_is_dir(path: Path) -> bool:
        return False if path == special else original_is_dir(path)
```

### `test_extraction_cleanup_preserves_primary_controlled_error`

**Purpose, ordered behavior and effects:** Patch directory removal to raise `PermissionError`, then call the private cleanup helper with a primary `GpuArchiveError` and require normal completion so the original error can remain authoritative. Calling it again without a primary error must instead raise a controlled could-not-clean archive error. No tree is actually deleted.

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

### `test_extraction_cleanup_preserves_primary_controlled_error.fail_cleanup`

**Purpose, ordered behavior and effects:** Installed as `gpu._remove_extraction_path`, assert the requested path is exactly the intended temporary directory and then raise `PermissionError`. It performs no removal and has no normal return.

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

**Complete source-ordered implementation**

```python
def fail_cleanup(path: Path) -> None:
        assert path == temporary
        raise PermissionError("simulated cleanup failure")
```

### `test_extraction_temporary_link_is_rejected_without_unlinking_target`

**Purpose, ordered behavior and effects:** For simulated symlink and junction classifications at the expected extraction temporary path, wrap unlink/rmdir/rmtree with protected counters and call real extraction. Require a controlled temporary-link error and zero protected deletion calls. No OS link is created; the test proves pre-cleanup rejection at these simulated metadata boundaries.

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

### `test_extraction_temporary_link_is_rejected_without_unlinking_target.simulated_is_symlink`

**Purpose, ordered behavior and effects:** Installed as `Path.is_symlink`, return true only for the selected symlink case at the expected temporary path; all other checks delegate to the real saved method. The junction case is not forced true by this callback.

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

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `original_is_symlink` | pathlib.Path.is_symlink (saved before monkeypatch) |

**Complete source-ordered implementation**

```python
def simulated_is_symlink(path: Path) -> bool:
        return (link_kind == "symlink" and path == temporary) or original_is_symlink(
            path
        )
```

### `test_extraction_temporary_link_is_rejected_without_unlinking_target.simulated_is_junction`

**Purpose, ordered behavior and effects:** Installed as `Path.is_junction`, return true only for the selected junction case at the temporary path, otherwise delegate to the saved real method. This is metadata simulation, not junction creation.

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

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `original_is_junction` | pathlib.Path.is_junction (saved before monkeypatch) |

**Complete source-ordered implementation**

```python
def simulated_is_junction(path: Path) -> bool:
        return (link_kind == "junction" and path == temporary) or original_is_junction(
            path
        )
```

### `test_extraction_temporary_link_is_rejected_without_unlinking_target.protected_unlink`

**Purpose, ordered behavior and effects:** Installed as `Path.unlink`, increment the enclosing protected counter and raise `AssertionError` if the temporary link is targeted. For all other paths delegate to the real saved unlink, retaining ordinary cleanup behavior.

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

- Explicit raise paths:
  - `AssertionError("temporary link was unlinked")` under lexical guard `path == temporary`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_unlink` | pathlib.Path.unlink (saved before monkeypatch) |

**Complete source-ordered implementation**

```python
def protected_unlink(path: Path, *args: object, **kwargs: object) -> None:
        nonlocal unlink_calls
        if path == temporary:
            unlink_calls += 1
            raise AssertionError("temporary link was unlinked")
        original_unlink(path, *args, **kwargs)
```

### `test_extraction_temporary_link_is_rejected_without_unlinking_target.protected_rmdir`

**Purpose, ordered behavior and effects:** Installed as `Path.rmdir`, increment the enclosing counter and raise if the designated temporary path is targeted. Other directory removals execute through the saved real method.

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

- Explicit raise paths:
  - `AssertionError("temporary junction was removed")` under lexical guard `path == temporary`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_rmdir` | pathlib.Path.rmdir (saved before monkeypatch) |

**Complete source-ordered implementation**

```python
def protected_rmdir(path: Path, *args: object, **kwargs: object) -> None:
        nonlocal rmdir_calls
        if path == temporary:
            rmdir_calls += 1
            raise AssertionError("temporary junction was removed")
        original_rmdir(path, *args, **kwargs)
```

### `test_extraction_temporary_link_is_rejected_without_unlinking_target.protected_rmtree`

**Purpose, ordered behavior and effects:** Installed as `shutil.rmtree`, convert the supplied path for comparison, count and reject an attempt to remove the protected temporary path recursively, and delegate other calls. The enclosing test requires this protected branch never to be reached.

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
| `original_rmtree` | shutil.rmtree (saved before monkeypatch) |

**Complete source-ordered implementation**

```python
def protected_rmtree(path: object, *args: object, **kwargs: object) -> None:
        nonlocal rmtree_calls
        if Path(path) == temporary:
            rmtree_calls += 1
            raise AssertionError("temporary link tree was removed")
        original_rmtree(path, *args, **kwargs)
```

### `test_stale_extraction_temporary_directory_fails_closed_and_is_preserved`

**Purpose, ordered behavior and effects:** Create an actual pre-existing temporary extraction directory containing a sentinel before calling extraction. Require a temporary/manual/recovery error and exact preservation of the sentinel, distinguishing stale real directories from the separately simulated links.

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

### `test_duplicate_extraction_manifest_key_forces_verified_rebuild`

**Purpose, ordered behavior and effects:** Extract valid synthetic bytes, rewrite the manifest with the archive-SHA key duplicated even though its repeated value agrees, and call extraction again. Require a rebuild rather than a cache hit and no leftover backup; duplicate-key JSON is not valid integrity evidence.

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

### `test_stale_download_object_rejects_replaced_valid_archive`

**Purpose, ordered behavior and effects:** Populate a downloaded ZIP, replace its physical bytes with a different valid ZIP of exactly the same byte length, and attempt extraction using the stale download record. Require a checksum/stale-metadata archive error and absence of the old-hash extraction root; size equality cannot replace byte identity.

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

### `test_extraction_rejects_archive_object_inconsistent_with_path`

**Purpose, ordered behavior and effects:** Forge the recorded SHA, size, filename or archive format while leaving a real synthetic ZIP path in place. For each of four cases require the public extractor to reject inconsistent archive metadata rather than trusting the frozen record's constructor.

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

### `test_tampered_extraction_is_rebuilt_from_verified_archive`

**Purpose, ordered behavior and effects:** After a real extraction, modify member content, delete it, add an unexpected file or rename it, one mutation per case. Re-extract from the unchanged verified synthetic archive and require `cache_hit=False`, original source bytes restored, and both renamed/unexpected paths absent. The attacks and repair of this disposable cache are physical local I/O, not geometry repair.

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

### `_extraction_from_archive`

**Purpose, ordered behavior and effects:** Construct synthetic current Muret document metadata and a `GpuArchiveDownload` using the actual supplied local ZIP path, current UTC timestamp, physical byte size and computed SHA. Call the real extractor under `tmp_path/cache` and return its extraction. Discovery/download network steps are bypassed, while ZIP validation, extraction, inventory and manifest generation are real.

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

### `test_spatial_inventory_and_inspection_preserve_source_quality`

**Purpose, ordered behavior and effects:** Create and extract the real synthetic GeoPackage package, discover its two physical layers and inspect with the real config. Check layer ordering/roles, EPSG:2154, three zoning rows, one NULL and one invalid geometry, persistence of the invalid bow-tie, CNIG XML identity and sorted file inventory. No source geometry is repaired.

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

### `test_missing_zoning_layer_fails_clearly`

**Purpose, ordered behavior and effects:** Construct a real synthetic package and a validated config whose zoning match token is `missing`. Require physical inspection to fail with a zoning error instead of producing an empty or invented zoning role.

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

### `test_ambiguous_zoning_layer_fails_clearly`

**Purpose, ordered behavior and effects:** Give zoning both `zone_urba` and `prescription_surf` tokens against the real two-layer synthetic package. Require inspection to report two matches rather than selecting one arbitrarily.

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

### `_config_with_shared_role_token`

**Purpose, ordered behavior and effects:** Dump a freshly loaded config to an independent mutable payload, assign the same token list to the two named logical roles, then validate a new immutable config. The existing loaded config is not mutated; role ambiguity is intentionally left for physical inspection rather than simulated by a fake layer reader.

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

### `test_inspection_rejects_one_physical_layer_for_two_logical_roles`

**Purpose, ordered behavior and effects:** For three declared role pairs, assign one shared token so the same physical zoning or prescription layer would satisfy both logical roles. Inspect the real synthetic package and require a role/same-layer error, including cross-family and cross-prescription/information collisions.

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

### `test_inspection_rejects_mutated_config_before_layer_discovery`

**Purpose, ordered behavior and effects:** Create a real synthetic extraction, bypass config validation with `model_copy` carrying an untrusted provider, and replace layer discovery with a counted assertion failure. Require controlled config/provider rejection with zero discovery calls; the forged object is reconstructed before spatial discovery.

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

### `test_inspection_rejects_mutated_config_before_layer_discovery.counted`

**Purpose, ordered behavior and effects:** Installed as `gpu.discover_gpu_spatial_layers`, increment the enclosing counter and always raise `AssertionError` if invalid-config inspection reaches layer discovery. It performs no GIS read and never returns normally.

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

- Explicit raise paths:
  - `AssertionError("layer discovery ran for an invalid config")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |

**Complete source-ordered implementation**

```python
def counted(*args: object, **kwargs: object) -> object:
        nonlocal discovery_calls
        discovery_calls += 1
        raise AssertionError("layer discovery ran for an invalid config")
```

### `test_inspection_rejects_archive_byte_mutation_before_layer_discovery`

**Purpose, ordered behavior and effects:** Create and extract a valid synthetic package, append changed bytes to the source ZIP and replace spatial discovery with a counted failure callback. Require controlled archive/source/config rejection and zero discovery calls, proving archive revalidation precedes layer discovery.

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

### `test_inspection_rejects_archive_byte_mutation_before_layer_discovery.counted`

**Purpose, ordered behavior and effects:** Installed as `gpu.discover_gpu_spatial_layers`, increment the counter and unconditionally raise if inspection of the stale archive reaches spatial discovery. It performs no actual layer listing or feature read.

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

- Explicit raise paths:
  - `AssertionError("layer discovery ran after archive mutation")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |

**Complete source-ordered implementation**

```python
def counted(*args: object, **kwargs: object) -> object:
        nonlocal discovery_calls
        discovery_calls += 1
        raise AssertionError("layer discovery ran after archive mutation")
```

### `test_inspection_rejects_document_lineage_not_matching_config`

**Purpose, ordered behavior and effects:** Forge the extraction's nested document commune, partition, empty document type or wrong-partition official URL while retaining the real extracted package. Require inspection to reject each of four source/config lineage inconsistencies before accepting a planning document.

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

### `test_planning_document_records_and_revalidates_exact_config_identity`

**Purpose, ordered behavior and effects:** Inspect a real synthetic package and verify the returned record retains the validated config and matching full config hash. Forge either the config SHA or the immutable all-layer inventory as a list, then call the public single-layer revalidator and require controlled rejection for each attack.

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

### `test_source_complete_revalidation_rejects_coordinated_spatial_omission`

**Purpose, ordered behavior and effects:** Inspect the real two-layer package, then forge both the related-layer tuple and all-spatial-layer inventory to omit the prescription layer while keeping zoning. Public zoning revalidation must reject the mismatch against physical inventory; coordinated caller omissions are not authoritative.

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

### `test_cached_document_lineage_change_forces_refresh`

**Purpose, ordered behavior and effects:** Populate a cache for `doc-1`, construct metadata for `doc-2` and consistently rewrite its written-file URLs, then serve a valid synthetic ZIP through the transport mock. Require a non-cache-hit result, showing that internally consistent changed document lineage cannot reuse the previous sidecar.

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


## 7. Test-specific regression contract

- Top-level test definitions: **64**; their explicit decorators declare **143 cases**. This is static parameter arithmetic, not a claim that Pytest collection or execution occurred during this prose audit.
- Additional callable definitions: **41** (fixture helpers, response methods and nested callbacks). The response class has no locally declared fields.
- Pytest fixtures (decorator-proven): **0**.

### Per-test regression index

The ordered setup, attacked boundary, assertion meaning and mock limitations are explained for every test in section 6. The table below is an index of declared cases and direct assertion statements, not an execution report; expected-exception contexts and callback assertions also contribute to a test's checks.

| Test | Parametrization | Expected exception contexts | Assertion count | Declared cases |
|---|---|---|---:|---:|
| `test_valid_config_and_urls` | none | none | 3 | 1 |
| `test_duplicate_gpu_yaml_key_is_rejected` | none | pytest.raises(gpu.GpuConfigError) | 1 | 1 |
| `test_invalid_config_values_are_rejected` | pytest.mark.parametrize(<br>    ("path", "value"),<br>    [<br>        (("pilot", "commune_code"), "3139"),<br>        (("api", "base_url"), "file:///api"),<br>        (("api", "base_url"), "http://www.geoportail-urbanisme.gouv.fr/api"),<br>        (("api", "base_url"), "https://example.com/api"),<br>        (("api", "base_url"), "https://www.geoportail-urbanisme.gouv.fr:8443/api"),<br>        (("api", "base_url"), "https://www.geoportail-urbanisme.gouv.fr/api?x=1"),<br>        (("download", "strategy"), "parcel"),<br>        (("download", "partition_template"), ""),<br>        (("cache", "max_age_hours"), -1),<br>    ],<br>) | pytest.raises(ValidationError) | 0 | 9 |
| `test_mutated_loaded_api_origin_is_rejected_before_discovery_network` | none | pytest.raises(ValidationError, match="frozen"); pytest.raises(GpuDiscoveryError, match="config\|official\|origin") | 1 | 1 |
| `test_gpu_source_identity_is_exact` | pytest.mark.parametrize("field", ["provider", "portal"]) | pytest.raises(ValidationError) | 0 | 2 |
| `test_gpu_cache_age_rejects_coercion_and_nonfinite` | pytest.mark.parametrize("value", [True, "168", float("nan"), float("inf")]) | pytest.raises(ValidationError) | 0 | 4 |
| `test_gpu_source_config_identity_is_deterministic_and_content_bound` | none | none | 2 | 1 |
| `test_unknown_config_field_is_rejected` | none | pytest.raises(ValidationError) | 0 | 1 |
| `test_document_discovery_success` | none | none | 7 | 1 |
| `test_gpu_api_json_is_strict_before_document_selection` | pytest.mark.parametrize(<br>    "payload",<br>    [<br>        b'[{"id":"doc-1","id":"doc-2"}]',<br>        b"[NaN]",<br>        b"[Infinity]",<br>    ],<br>) | pytest.raises(GpuDiscoveryError, match="JSON\|duplicate\|finite\|metadata") | 0 | 3 |
| `test_written_material_url_must_be_exact_official_https_api_url` | pytest.mark.parametrize(<br>    "source_url",<br>    [<br>        (<br>            "http://www.geoportail-urbanisme.gouv.fr/api/document/"<br>            "doc-1/files/reglement.pdf"<br>        ),<br>        "https://unrelated.example/api/document/doc-1/files/reglement.pdf",<br>    ],<br>    ids=["http", "unrelated-https-origin"],<br>) | pytest.raises(GpuDiscoveryError, match="written material URL") | 0 | 2 |
| `test_written_material_fallback_rejects_unsafe_archive_url_provenance` | pytest.mark.parametrize(<br>    "archive_url",<br>    [<br>        (<br>            "http://www.geoportail-urbanisme.gouv.fr/api/document/"<br>            "doc-1/download/31395_PLU_20240215.zip"<br>        ),<br>        (<br>            "https://unrelated.example/api/document/doc-1/download/"<br>            "31395_PLU_20240215.zip"<br>        ),<br>    ],<br>    ids=["http", "unrelated-https-origin"],<br>) | pytest.raises(GpuDiscoveryError, match="archive URL") | 0 | 2 |
| `test_no_current_document_is_rejected` | none | pytest.raises(GpuDiscoveryError, match="No current") | 0 | 1 |
| `test_ambiguous_current_documents_are_rejected` | none | pytest.raises(GpuDiscoveryError, match="Ambiguous") | 0 | 1 |
| `test_missing_document_identity_is_rejected` | pytest.mark.parametrize("field", ["id", "originalName", "type"]) | pytest.raises(GpuDiscoveryError, match="missing") | 0 | 3 |
| `test_document_details_must_match_selected_listing` | pytest.mark.parametrize(<br>    ("field", "different_value"),<br>    [<br>        ("id", "doc-2"),<br>        ("originalName", "31395_PLU_OTHER"),<br>        ("name", "DU_99999"),<br>        ("type", "CC"),<br>        ("status", "document.deleted"),<br>        ("legalStatus", "CANCELLED"),<br>        ("effectiveStatus", "ANNULE"),<br>    ],<br>) | pytest.raises(GpuDiscoveryError, match="match\|changed\|current") | 0 | 7 |
| `test_document_details_commune_must_match_selected_listing` | none | pytest.raises(GpuDiscoveryError, match="match") | 0 | 1 |
| `test_discovery_rejects_unsafe_archive_name` | pytest.mark.parametrize(<br>    "archive_name",<br>    _UNSAFE_ARCHIVE_NAMES,<br>) | pytest.raises(GpuDiscoveryError, match="archive name\|safe") | 0 | 16 |
| `test_successful_download_persists_sha_and_sidecar` | none | none | 6 | 1 |
| `test_download_rejects_document_inconsistent_with_config` | pytest.mark.parametrize(<br>    ("field", "different_value"),<br>    [<br>        ("provider", "OTHER PROVIDER"),<br>        ("portal", "OTHER PORTAL"),<br>        ("commune_code", "99999"),<br>        ("partition", "DU_99999"),<br>        ("status", "document.deleted"),<br>        ("legal_status", "CANCELLED"),<br>        ("effective_status", "ANNULE"),<br>        ("source_url", "https://example.test/not-the-gpu.zip"),<br>        (<br>            "source_url",<br>            (<br>                "https://www.geoportail-urbanisme.gouv.fr/api/document/"<br>                "download-by-partition/DU_99999"<br>            ),<br>        ),<br>    ],<br>) | pytest.raises(GpuDownloadError, match="document\|identity\|config") | 1 | 9 |
| `test_download_rejects_forged_written_file_provenance_before_network` | pytest.mark.parametrize("mutation", ["forged-source-url", "wrong-item-type"]) | pytest.raises(GpuDownloadError, match="written\|document\|source\|URL") | 1 | 2 |
| `test_download_rejects_forged_unsafe_archive_name_before_io` | pytest.mark.parametrize(<br>    "archive_name",<br>    _UNSAFE_ARCHIVE_NAMES,<br>) | pytest.raises(GpuDownloadError, match="archive name\|archive filename\|safe") | 1 | 16 |
| `test_archive_name_with_one_zip_suffix_is_not_duplicated` | none | none | 2 | 1 |
| `test_fresh_cache_is_reused` | none | none | 2 | 1 |
| `test_boolean_cache_integrity_counts_are_not_accepted_as_integers` | pytest.mark.parametrize("field", ["file_size", "member_count"]) | none | 1 | 2 |
| `test_stale_recovery_backup_rejects_cache_before_network` | none | pytest.raises(GpuDownloadError, match="backup\|recovery\|manual") | 1 | 1 |
| `test_expired_cache_is_refreshed` | none | none | 2 | 1 |
| `test_failed_refresh_preserves_previous_cache` | none | pytest.raises(GpuDownloadError) | 3 | 1 |
| `test_metadata_publication_failure_rolls_back_both_cache_files` | none | pytest.raises(GpuDownloadError) | 4 | 1 |
| `test_publication_and_rollback_failure_preserves_exact_recovery_backups` | none | pytest.raises(GpuDownloadError, match="rollback") | 2 | 1 |
| `test_cleanup_failure_does_not_mask_double_failure_recovery_error` | none | pytest.raises(GpuDownloadError, match="rollback") | 2 | 1 |
| `test_stale_cache_recovery_backup_fails_closed_without_destroying_it` | none | pytest.raises(GpuDownloadError, match="backup\|recovery\|manual") | 3 | 1 |
| `test_preexisting_temporary_archive_symlink_cannot_modify_target` | none | pytest.raises(GpuDownloadError) | 2 | 1 |
| `test_corrupt_download_is_rejected` | none | pytest.raises(GpuDownloadError) | 1 | 1 |
| `test_tampered_sidecar_invalidates_cache` | none | none | 1 | 1 |
| `test_archive_path_traversal_is_rejected` | none | pytest.raises(GpuArchiveError, match="Unsafe") | 0 | 1 |
| `test_archive_symlink_is_rejected` | none | pytest.raises(GpuArchiveError, match="Symbolic") | 0 | 1 |
| `test_duplicate_zip_extraction_targets_are_rejected` | pytest.mark.parametrize(<br>    "members",<br>    [<br>        [("duplicate.txt", b"first"), ("duplicate.txt", b"second")],<br>        [("folder/file.txt", b"first"), (r"folder\file.txt", b"second")],<br>        [("folder/file.txt", b"first"), ("folder/./file.txt", b"second")],<br>        [("Folder/File.txt", b"first"), ("folder/file.txt", b"second")],<br>    ],<br>) | pytest.raises(GpuArchiveError, match="(?i)duplicate\|collid") | 0 | 4 |
| `test_zip_file_directory_target_collision_is_rejected` | none | pytest.raises(GpuArchiveError, match="collision\|target") | 0 | 1 |
| `test_zip_cannot_claim_extraction_manifest_path` | none | pytest.raises(GpuArchiveError, match="manifest") | 0 | 1 |
| `test_extraction_inventory_and_cache` | none | none | 7 | 1 |
| `test_extraction_manifest_is_created_exclusively` | none | none | 1 | 1 |
| `test_stale_extraction_backup_fails_closed_and_is_preserved` | none | pytest.raises(GpuArchiveError, match="backup\|recovery\|manual") | 2 | 1 |
| `test_extraction_publication_and_rollback_failure_preserves_backup` | none | pytest.raises(GpuArchiveError, match="rollback"); pytest.raises(GpuArchiveError, match="backup\|recovery\|manual") | 2 | 1 |
| `test_extraction_publication_failure_restores_existing_root` | none | pytest.raises(GpuArchiveError, match="publication") | 2 | 1 |
| `test_extraction_backup_move_failure_preserves_existing_root` | none | pytest.raises(GpuArchiveError, match="backup.*failed") | 2 | 1 |
| `test_extraction_inventory_rejects_special_entry` | none | pytest.raises(GpuArchiveError, match="special filesystem entry") | 0 | 1 |
| `test_extraction_cleanup_preserves_primary_controlled_error` | none | pytest.raises(GpuArchiveError, match="could not be cleaned") | 0 | 1 |
| `test_extraction_temporary_link_is_rejected_without_unlinking_target` | pytest.mark.parametrize("link_kind", ["symlink", "junction"]) | pytest.raises(GpuArchiveError, match="temporary\|link\|junction") | 3 | 2 |
| `test_stale_extraction_temporary_directory_fails_closed_and_is_preserved` | none | pytest.raises(GpuArchiveError, match="temporary\|manual\|recovery") | 1 | 1 |
| `test_duplicate_extraction_manifest_key_forces_verified_rebuild` | none | none | 2 | 1 |
| `test_stale_download_object_rejects_replaced_valid_archive` | none | pytest.raises(GpuArchiveError, match="checksum\|SHA\|stale\|metadata") | 2 | 1 |
| `test_extraction_rejects_archive_object_inconsistent_with_path` | pytest.mark.parametrize(<br>    ("field", "value"),<br>    [<br>        ("sha256", "0" * 64),<br>        ("file_size", 1),<br>        ("filename", "other.zip"),<br>        ("archive_format", "7z"),<br>    ],<br>) | pytest.raises(GpuArchiveError, match="archive\|metadata\|checksum\|size") | 0 | 4 |
| `test_tampered_extraction_is_rebuilt_from_verified_archive` | pytest.mark.parametrize("mutation", ["content", "deleted", "added", "path"]) | none | 4 | 4 |
| `test_spatial_inventory_and_inspection_preserve_source_quality` | none | none | 10 | 1 |
| `test_missing_zoning_layer_fails_clearly` | none | pytest.raises(GpuSpatialInspectionError, match="zoning") | 0 | 1 |
| `test_ambiguous_zoning_layer_fails_clearly` | none | pytest.raises(GpuSpatialInspectionError, match="found 2") | 0 | 1 |
| `test_inspection_rejects_one_physical_layer_for_two_logical_roles` | pytest.mark.parametrize(<br>    ("first_role", "second_role", "token"),<br>    [<br>        ("zoning", "prescription_surface", "zone_urba"),<br>        ("prescription_surface", "prescription_line", "prescription_surf"),<br>        ("prescription_surface", "information_surface", "prescription_surf"),<br>    ],<br>) | pytest.raises(GpuSpatialInspectionError, match="role\|logical\|same layer") | 0 | 3 |
| `test_inspection_rejects_mutated_config_before_layer_discovery` | none | pytest.raises(GpuSpatialInspectionError, match="config\|provider") | 1 | 1 |
| `test_inspection_rejects_archive_byte_mutation_before_layer_discovery` | none | pytest.raises(GpuSpatialInspectionError, match="archive\|source\|config") | 1 | 1 |
| `test_inspection_rejects_document_lineage_not_matching_config` | pytest.mark.parametrize(<br>    ("field", "value"),<br>    [<br>        ("commune_code", "99999"),<br>        ("partition", "DU_99999"),<br>        ("document_type", ""),<br>        (<br>            "source_url",<br>            "https://www.geoportail-urbanisme.gouv.fr/api/document/download-by-partition/DU_99999",<br>        ),<br>    ],<br>) | pytest.raises(<br>        GpuSpatialInspectionError,<br>        match="config\|commune\|partition\|URL\|type\|planning",<br>    ) | 0 | 4 |
| `test_planning_document_records_and_revalidates_exact_config_identity` | none | pytest.raises(GpuSpatialInspectionError, match="config\|SHA"); pytest.raises(GpuSpatialInspectionError, match="inventory\|tuple") | 2 | 1 |
| `test_source_complete_revalidation_rejects_coordinated_spatial_omission` | none | pytest.raises(GpuSpatialInspectionError, match="spatial inventory\|physical") | 0 | 1 |
| `test_cached_document_lineage_change_forces_refresh` | none | none | 1 | 1 |

## 8. Public exports and package ownership

This module declares no `__all__`; no package-level public guarantee is inferred from direct importability alone.

## 9. Trust, provenance, side effects, and business boundary

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Each callable's manually reviewed purpose/ordered-behavior paragraph distinguishes fixture setup, the attacked boundary, actual local I/O and injected callbacks. Every `gpu.open_safe_https` replacement bypasses shared DNS/socket behavior; separate shared-transport tests own that contract. Real synthetic GeoPackage and ZIP readers remain active except where a named regression deliberately isolates a scalar/cache gate.
- Pytest restores monkeypatches after the test. Temporary files and model-dump dictionaries are disposable fixtures, not modifications to the checked-in config or the real GPU cache. No test result is inferred from reading this companion.

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

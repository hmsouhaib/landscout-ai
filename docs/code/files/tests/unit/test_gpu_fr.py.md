# `tests/unit/test_gpu_fr.py`

## File identity

- Repository path: `tests/unit/test_gpu_fr.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `a3511fec0dbfae47ed761e7deedaf958a8960fd60e8488d6db478eb0965aeb49`

## 1. Purpose

Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import io` — required by the implementation paths and symbols documented below.
- `import json` — required by the implementation paths and symbols documented below.
- `import warnings` — required by the implementation paths and symbols documented below.
- `import zipfile` — required by the implementation paths and symbols documented below.
- `from dataclasses import replace` — required by the implementation paths and symbols documented below.
- `from datetime import UTC, datetime, timedelta` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.
- `from typing import Self` — required by the implementation paths and symbols documented below.
- `from urllib.error import URLError` — required by the implementation paths and symbols documented below.

### Third-party

- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import pytest` — required by the implementation paths and symbols documented below.
- `from pydantic import HttpUrl, ValidationError` — required by the implementation paths and symbols documented below.
- `from shapely.geometry import Polygon` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `import landscout.sources.gpu_fr as gpu` — required by the implementation paths and symbols documented below.
- `from landscout.sources.gpu_fr import ( GpuArchiveDownload, GpuArchiveError, GpuDiscoveryError, GpuDownloadError, GpuExtraction, GpuSourceConfig, GpuSpatialInspectionError, build_gpu_document_list_url, build_gpu_partition, build_gpu_partition_download_url, discover_current_gpu_document, discover_gpu…` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `_UNSAFE_ARCHIVE_NAMES` | `( "../escape", r"..\escape", "/absolute", r"C:\absolute", ".", "..", " leading", "trailing ", "nul\x00name", "CON", "nul.txt", "bad:name", "bad?.zip", "trailing.", "archive.zip.zip", "a" * 252, )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `_Response`

**Purpose:** Groups the `Response` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `io.BytesIO`.

**Model form and mutability:** class inheriting from `io.BytesIO`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- `__enter__` — `def __enter__(self) -> Self:`; decorators `none`. The complete method algorithm appears in the function/method section.
- `__exit__` — `def __exit__(self, *args: object) -> None:`; decorators `none`. The complete method algorithm appears in the function/method section.

## 6. Functions and methods

### `_Response.__enter__`

**Signature**

```python
def __enter__(self) -> Self:
```

**Purpose**

Implements enter according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Self`. Observed return expression(s): `self`.

**Algorithm**

1. Returns `self`.

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

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_Response.__exit__`

**Signature**

```python
def __exit__(self, *args: object) -> None:
```

**Purpose**

Implements exit according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Calls `self.close()` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `self.close`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_config`

**Signature**

```python
def _config() -> GpuSourceConfig:
```

**Purpose**

Implements config according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `GpuSourceConfig`. Observed return expression(s): `load_gpu_source_config(Path('configs/sources/gpu_fr.yaml'))`.

**Algorithm**

1. Returns `load_gpu_source_config(Path('configs/sources/gpu_fr.yaml'))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `load_gpu_source_config`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `Path`, `load_gpu_source_config`.

**Known repository callers**

- `tests/unit/test_gpu_fr.py` — `_document`
- `tests/unit/test_gpu_fr.py` — `_download`
- `tests/unit/test_gpu_fr.py` — `test_ambiguous_current_documents_are_rejected`
- `tests/unit/test_gpu_fr.py` — `test_ambiguous_zoning_layer_fails_clearly`
- `tests/unit/test_gpu_fr.py` — `test_archive_name_with_one_zip_suffix_is_not_duplicated`
- `tests/unit/test_gpu_fr.py` — `test_cached_document_lineage_change_forces_refresh`
- `tests/unit/test_gpu_fr.py` — `test_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_gpu_fr.py` — `test_corrupt_download_is_rejected`
- `tests/unit/test_gpu_fr.py` — `test_discovery_rejects_unsafe_archive_name`
- `tests/unit/test_gpu_fr.py` — `test_document_details_commune_must_match_selected_listing`
- `tests/unit/test_gpu_fr.py` — `test_document_details_must_match_selected_listing`
- `tests/unit/test_gpu_fr.py` — `test_download_rejects_document_inconsistent_with_config`
- `tests/unit/test_gpu_fr.py` — `test_download_rejects_forged_unsafe_archive_name_before_io`
- `tests/unit/test_gpu_fr.py` — `test_download_rejects_forged_written_file_provenance_before_network`
- `tests/unit/test_gpu_fr.py` — `test_expired_cache_is_refreshed`
- `tests/unit/test_gpu_fr.py` — `test_failed_refresh_preserves_previous_cache`
- `tests/unit/test_gpu_fr.py` — `test_fresh_cache_is_reused`
- `tests/unit/test_gpu_fr.py` — `test_invalid_config_values_are_rejected`
- `tests/unit/test_gpu_fr.py` — `test_metadata_publication_failure_rolls_back_both_cache_files`
- `tests/unit/test_gpu_fr.py` — `test_missing_document_identity_is_rejected`
- `tests/unit/test_gpu_fr.py` — `test_missing_zoning_layer_fails_clearly`
- `tests/unit/test_gpu_fr.py` — `test_mutated_loaded_api_origin_is_rejected_before_discovery_network`
- `tests/unit/test_gpu_fr.py` — `test_no_current_document_is_rejected`
- `tests/unit/test_gpu_fr.py` — `test_preexisting_temporary_archive_symlink_cannot_modify_target`
- `tests/unit/test_gpu_fr.py` — `test_spatial_inventory_and_inspection_preserve_source_quality`
- `tests/unit/test_gpu_fr.py` — `test_stale_recovery_backup_rejects_cache_before_network`
- `tests/unit/test_gpu_fr.py` — `test_tampered_sidecar_invalidates_cache`
- `tests/unit/test_gpu_fr.py` — `test_unknown_config_field_is_rejected`
- `tests/unit/test_gpu_fr.py` — `test_valid_config_and_urls`
- `tests/unit/test_gpu_fr.py` — `test_written_material_fallback_rejects_unsafe_archive_url_provenance`
- `tests/unit/test_gpu_fr.py` — `test_written_material_url_must_be_exact_official_https_api_url`

**Tests**

- `tests/unit/test_gpu_fr.py::test_ambiguous_current_documents_are_rejected`
- `tests/unit/test_gpu_fr.py::test_ambiguous_zoning_layer_fails_clearly`
- `tests/unit/test_gpu_fr.py::test_archive_name_with_one_zip_suffix_is_not_duplicated`
- `tests/unit/test_gpu_fr.py::test_cached_document_lineage_change_forces_refresh`
- `tests/unit/test_gpu_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_gpu_fr.py::test_corrupt_download_is_rejected`
- `tests/unit/test_gpu_fr.py::test_discovery_rejects_unsafe_archive_name`
- `tests/unit/test_gpu_fr.py::test_document_details_commune_must_match_selected_listing`
- `tests/unit/test_gpu_fr.py::test_document_details_must_match_selected_listing`
- `tests/unit/test_gpu_fr.py::test_download_rejects_document_inconsistent_with_config`
- `tests/unit/test_gpu_fr.py::test_download_rejects_forged_unsafe_archive_name_before_io`
- `tests/unit/test_gpu_fr.py::test_download_rejects_forged_written_file_provenance_before_network`
- `tests/unit/test_gpu_fr.py::test_expired_cache_is_refreshed`
- `tests/unit/test_gpu_fr.py::test_failed_refresh_preserves_previous_cache`
- `tests/unit/test_gpu_fr.py::test_fresh_cache_is_reused`
- `tests/unit/test_gpu_fr.py::test_invalid_config_values_are_rejected`
- `tests/unit/test_gpu_fr.py::test_metadata_publication_failure_rolls_back_both_cache_files`
- `tests/unit/test_gpu_fr.py::test_missing_document_identity_is_rejected`
- `tests/unit/test_gpu_fr.py::test_missing_zoning_layer_fails_clearly`
- `tests/unit/test_gpu_fr.py::test_mutated_loaded_api_origin_is_rejected_before_discovery_network`
- `tests/unit/test_gpu_fr.py::test_no_current_document_is_rejected`
- `tests/unit/test_gpu_fr.py::test_preexisting_temporary_archive_symlink_cannot_modify_target`
- `tests/unit/test_gpu_fr.py::test_spatial_inventory_and_inspection_preserve_source_quality`
- `tests/unit/test_gpu_fr.py::test_stale_recovery_backup_rejects_cache_before_network`
- `tests/unit/test_gpu_fr.py::test_tampered_sidecar_invalidates_cache`
- `tests/unit/test_gpu_fr.py::test_unknown_config_field_is_rejected`
- `tests/unit/test_gpu_fr.py::test_valid_config_and_urls`
- `tests/unit/test_gpu_fr.py::test_written_material_fallback_rejects_unsafe_archive_url_provenance`
- `tests/unit/test_gpu_fr.py::test_written_material_url_must_be_exact_official_https_api_url`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_listing_item`

**Signature**

```python
def _listing_item(**overrides: object) -> dict[str, object]:
```

**Purpose**

Implements listing item according to the exact implementation and guards in this file.

**Inputs**

- `**overrides` (`object`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `result`.

**Algorithm**

1. Defines `result` with annotation `dict[str, object]` from `{'id': 'doc-1', 'status': 'document.production', 'legalStatus': 'APPROVED', 'effectiveStatus': 'EN_VIGUEUR', 'originalName': '31395_PLU_20240215', 'type': 'PLU', 'name': 'DU_31395', 'grid': {'name': '31395', 'title': 'MURET'}}`.
2. Calls `result.update(overrides)` for its validation or side effect.
3. Returns `result`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `result.update`.

**Known repository callers**

- `tests/unit/test_gpu_fr.py` — `_details`
- `tests/unit/test_gpu_fr.py` — `_document`
- `tests/unit/test_gpu_fr.py` — `test_ambiguous_current_documents_are_rejected`
- `tests/unit/test_gpu_fr.py` — `test_discovery_rejects_unsafe_archive_name`
- `tests/unit/test_gpu_fr.py` — `test_document_details_commune_must_match_selected_listing`
- `tests/unit/test_gpu_fr.py` — `test_document_details_must_match_selected_listing`
- `tests/unit/test_gpu_fr.py` — `test_missing_document_identity_is_rejected`
- `tests/unit/test_gpu_fr.py` — `test_no_current_document_is_rejected`
- `tests/unit/test_gpu_fr.py` — `test_written_material_fallback_rejects_unsafe_archive_url_provenance`
- `tests/unit/test_gpu_fr.py` — `test_written_material_url_must_be_exact_official_https_api_url`

**Tests**

- `tests/unit/test_gpu_fr.py::test_ambiguous_current_documents_are_rejected`
- `tests/unit/test_gpu_fr.py::test_discovery_rejects_unsafe_archive_name`
- `tests/unit/test_gpu_fr.py::test_document_details_commune_must_match_selected_listing`
- `tests/unit/test_gpu_fr.py::test_document_details_must_match_selected_listing`
- `tests/unit/test_gpu_fr.py::test_missing_document_identity_is_rejected`
- `tests/unit/test_gpu_fr.py::test_no_current_document_is_rejected`
- `tests/unit/test_gpu_fr.py::test_written_material_fallback_rejects_unsafe_archive_url_provenance`
- `tests/unit/test_gpu_fr.py::test_written_material_url_must_be_exact_official_https_api_url`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_details`

**Signature**

```python
def _details(**overrides: object) -> dict[str, object]:
```

**Purpose**

Implements details according to the exact implementation and guards in this file.

**Inputs**

- `**overrides` (`object`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `result`.

**Algorithm**

1. Computes `result` from `_listing_item(title="Plan Local d'Urbanisme de Muret", producer='Mairie de Muret', projectionCode='EPSG:2154', publicationDate='26/03/2024 08:52:34', updateDate='26/03/2024 08:52:34', metadata='fr-000031395-plu20240215', archiveUrl='https://www.geoportail-urbanisme.gouv.fr/api/document/doc-1/download/31395_PLU_2024021…`.
2. Calls `result.update(overrides)` for its validation or side effect.
3. Returns `result`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_listing_item`, `result.update`.

**Known repository callers**

- `tests/unit/test_gpu_fr.py` — `_document`
- `tests/unit/test_gpu_fr.py` — `test_discovery_rejects_unsafe_archive_name`
- `tests/unit/test_gpu_fr.py` — `test_document_details_commune_must_match_selected_listing`
- `tests/unit/test_gpu_fr.py` — `test_document_details_must_match_selected_listing`
- `tests/unit/test_gpu_fr.py` — `test_written_material_fallback_rejects_unsafe_archive_url_provenance`
- `tests/unit/test_gpu_fr.py` — `test_written_material_url_must_be_exact_official_https_api_url`

**Tests**

- `tests/unit/test_gpu_fr.py::test_discovery_rejects_unsafe_archive_name`
- `tests/unit/test_gpu_fr.py::test_document_details_commune_must_match_selected_listing`
- `tests/unit/test_gpu_fr.py::test_document_details_must_match_selected_listing`
- `tests/unit/test_gpu_fr.py::test_written_material_fallback_rejects_unsafe_archive_url_provenance`
- `tests/unit/test_gpu_fr.py::test_written_material_url_must_be_exact_official_https_api_url`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_files`

**Signature**

```python
def _files() -> list[dict[str, object]]:
```

**Purpose**

Implements files according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `list[dict[str, object]]`. Observed return expression(s): `[{'name': 'reglement.pdf', 'title': 'Règlement écrit', 'path': 'Règlements'}]`.

**Algorithm**

1. Returns `[{'name': 'reglement.pdf', 'title': 'Règlement écrit', 'path': 'Règlements'}]`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

- `tests/unit/test_gpu_fr.py` — `_document`
- `tests/unit/test_gpu_fr.py` — `test_discovery_rejects_unsafe_archive_name`
- `tests/unit/test_gpu_fr.py` — `test_document_details_commune_must_match_selected_listing`
- `tests/unit/test_gpu_fr.py` — `test_document_details_must_match_selected_listing`
- `tests/unit/test_gpu_fr.py` — `test_written_material_fallback_rejects_unsafe_archive_url_provenance`
- `tests/unit/test_gpu_fr.py` — `test_written_material_url_must_be_exact_official_https_api_url`

**Tests**

- `tests/unit/test_gpu_fr.py::test_discovery_rejects_unsafe_archive_name`
- `tests/unit/test_gpu_fr.py::test_document_details_commune_must_match_selected_listing`
- `tests/unit/test_gpu_fr.py::test_document_details_must_match_selected_listing`
- `tests/unit/test_gpu_fr.py::test_written_material_fallback_rejects_unsafe_archive_url_provenance`
- `tests/unit/test_gpu_fr.py::test_written_material_url_must_be_exact_official_https_api_url`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_patch_json_responses`

**Signature**

```python
def _patch_json_responses(monkeypatch: pytest.MonkeyPatch, values: list[object]) -> None:
```

**Purpose**

Implements patch json responses according to the exact implementation and guards in this file.

**Inputs**

- `monkeypatch` (`pytest.MonkeyPatch`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `values` (`list[object]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. Observed return expression(s): `_Response(json.dumps(next(responses)).encode())`.

**Algorithm**

1. Computes `responses` from `iter(values)`.
2. Defines the local helper `opener`; its behavior is documented with the parent function's nested helpers.
3. Calls `monkeypatch.setattr(gpu, 'open_safe_https', opener)` for its validation or side effect.

**Meaningful nested/local helpers**

- `opener` — `def opener(*args: object, **kwargs: object) -> _Response:`. It executes 1 top-level statement(s), uses `_Response`, `json.dumps`, `json.dumps(next(responses)).encode`, `next`, and has no explicit raises. Trivial test callbacks are intentionally grouped here with their parent.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_Response`, `iter`, `json.dumps`, `json.dumps(next(responses)).encode`, `monkeypatch.setattr`, `next`.

**Known repository callers**

- `tests/unit/test_gpu_fr.py` — `_document`
- `tests/unit/test_gpu_fr.py` — `test_ambiguous_current_documents_are_rejected`
- `tests/unit/test_gpu_fr.py` — `test_discovery_rejects_unsafe_archive_name`
- `tests/unit/test_gpu_fr.py` — `test_document_details_commune_must_match_selected_listing`
- `tests/unit/test_gpu_fr.py` — `test_document_details_must_match_selected_listing`
- `tests/unit/test_gpu_fr.py` — `test_missing_document_identity_is_rejected`
- `tests/unit/test_gpu_fr.py` — `test_no_current_document_is_rejected`
- `tests/unit/test_gpu_fr.py` — `test_written_material_fallback_rejects_unsafe_archive_url_provenance`
- `tests/unit/test_gpu_fr.py` — `test_written_material_url_must_be_exact_official_https_api_url`

**Tests**

- `tests/unit/test_gpu_fr.py::test_ambiguous_current_documents_are_rejected`
- `tests/unit/test_gpu_fr.py::test_discovery_rejects_unsafe_archive_name`
- `tests/unit/test_gpu_fr.py::test_document_details_commune_must_match_selected_listing`
- `tests/unit/test_gpu_fr.py::test_document_details_must_match_selected_listing`
- `tests/unit/test_gpu_fr.py::test_missing_document_identity_is_rejected`
- `tests/unit/test_gpu_fr.py::test_no_current_document_is_rejected`
- `tests/unit/test_gpu_fr.py::test_written_material_fallback_rejects_unsafe_archive_url_provenance`
- `tests/unit/test_gpu_fr.py::test_written_material_url_must_be_exact_official_https_api_url`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_patch_json_responses.opener`

**Signature**

```python
def opener(*args: object, **kwargs: object) -> _Response:
```

**Purpose**

Implements opener according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `_Response`. Observed return expression(s): `_Response(json.dumps(next(responses)).encode())`.

**Algorithm**

1. Returns `_Response(json.dumps(next(responses)).encode())`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_Response`, `json.dumps`, `json.dumps(next(responses)).encode`, `next`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_document`

**Signature**

```python
def _document(monkeypatch: pytest.MonkeyPatch):
```

**Purpose**

Implements document according to the exact implementation and guards in this file.

**Inputs**

- `monkeypatch` (`pytest.MonkeyPatch`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `unannotated`. Observed return expression(s): `discover_current_gpu_document(_config())`.

**Algorithm**

1. Calls `_patch_json_responses(monkeypatch, [[_listing_item()], _details(), _files()])` for its validation or side effect.
2. Returns `discover_current_gpu_document(_config())`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_config`, `_details`, `_files`, `_listing_item`, `_patch_json_responses`, `discover_current_gpu_document`.

**Known repository callers**

- `tests/unit/test_gpu_fr.py` — `_download`
- `tests/unit/test_gpu_fr.py` — `test_archive_name_with_one_zip_suffix_is_not_duplicated`
- `tests/unit/test_gpu_fr.py` — `test_corrupt_download_is_rejected`
- `tests/unit/test_gpu_fr.py` — `test_document_discovery_success`
- `tests/unit/test_gpu_fr.py` — `test_download_rejects_document_inconsistent_with_config`
- `tests/unit/test_gpu_fr.py` — `test_download_rejects_forged_unsafe_archive_name_before_io`
- `tests/unit/test_gpu_fr.py` — `test_download_rejects_forged_written_file_provenance_before_network`
- `tests/unit/test_gpu_fr.py` — `test_preexisting_temporary_archive_symlink_cannot_modify_target`

**Tests**

- `tests/unit/test_gpu_fr.py::test_archive_name_with_one_zip_suffix_is_not_duplicated`
- `tests/unit/test_gpu_fr.py::test_corrupt_download_is_rejected`
- `tests/unit/test_gpu_fr.py::test_document_discovery_success`
- `tests/unit/test_gpu_fr.py::test_download_rejects_document_inconsistent_with_config`
- `tests/unit/test_gpu_fr.py::test_download_rejects_forged_unsafe_archive_name_before_io`
- `tests/unit/test_gpu_fr.py::test_download_rejects_forged_written_file_provenance_before_network`
- `tests/unit/test_gpu_fr.py::test_preexisting_temporary_archive_symlink_cannot_modify_target`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_zip_bytes`

**Signature**

```python
def _zip_bytes(files: dict[str, bytes] | None = None) -> bytes:
```

**Purpose**

Implements zip bytes according to the exact implementation and guards in this file.

**Inputs**

- `files` (`dict[str, bytes] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bytes`. Observed return expression(s): `stream.getvalue()`.

**Algorithm**

1. Computes `stream` from `io.BytesIO()`.
2. Enters managed context(s) `zipfile.ZipFile(stream, 'w', compression=zipfile.ZIP_DEFLATED)` and executes: Iterates `(name, content)` over `(files or {'document/readme.txt': b'GPU'}).items()`. For each value: Calls `archive.writestr(name, content)` for its validation or side effect.
3. Returns `stream.getvalue()`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `archive.writestr`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `(files or {'document/readme.txt': b'GPU'}).items`, `archive.writestr`, `io.BytesIO`, `stream.getvalue`, `zipfile.ZipFile`.

**Known repository callers**

- `tests/unit/test_gpu_fr.py` — `_download`
- `tests/unit/test_gpu_fr.py` — `test_archive_name_with_one_zip_suffix_is_not_duplicated`
- `tests/unit/test_gpu_fr.py` — `test_archive_path_traversal_is_rejected`
- `tests/unit/test_gpu_fr.py` — `test_cached_document_lineage_change_forces_refresh`
- `tests/unit/test_gpu_fr.py` — `test_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_gpu_fr.py` — `test_expired_cache_is_refreshed`
- `tests/unit/test_gpu_fr.py` — `test_extraction_inventory_and_cache`
- `tests/unit/test_gpu_fr.py` — `test_metadata_publication_failure_rolls_back_both_cache_files`
- `tests/unit/test_gpu_fr.py` — `test_preexisting_temporary_archive_symlink_cannot_modify_target.record_network`
- `tests/unit/test_gpu_fr.py` — `test_preexisting_temporary_archive_symlink_cannot_modify_target`
- `tests/unit/test_gpu_fr.py` — `test_stale_download_object_rejects_replaced_valid_archive`
- `tests/unit/test_gpu_fr.py` — `test_tampered_extraction_is_rebuilt_from_verified_archive`
- `tests/unit/test_gpu_fr.py` — `test_tampered_sidecar_invalidates_cache`
- `tests/unit/test_gpu_fr.py` — `test_zip_cannot_claim_extraction_manifest_path`

**Tests**

- `tests/unit/test_gpu_fr.py::test_archive_name_with_one_zip_suffix_is_not_duplicated`
- `tests/unit/test_gpu_fr.py::test_archive_path_traversal_is_rejected`
- `tests/unit/test_gpu_fr.py::test_cached_document_lineage_change_forces_refresh`
- `tests/unit/test_gpu_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_gpu_fr.py::test_expired_cache_is_refreshed`
- `tests/unit/test_gpu_fr.py::test_extraction_inventory_and_cache`
- `tests/unit/test_gpu_fr.py::test_metadata_publication_failure_rolls_back_both_cache_files`
- `tests/unit/test_gpu_fr.py::test_preexisting_temporary_archive_symlink_cannot_modify_target`
- `tests/unit/test_gpu_fr.py::test_stale_download_object_rejects_replaced_valid_archive`
- `tests/unit/test_gpu_fr.py::test_tampered_extraction_is_rebuilt_from_verified_archive`
- `tests/unit/test_gpu_fr.py::test_tampered_sidecar_invalidates_cache`
- `tests/unit/test_gpu_fr.py::test_zip_cannot_claim_extraction_manifest_path`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_zip_member_bytes`

**Signature**

```python
def _zip_member_bytes(members: list[tuple[str, bytes]]) -> bytes:
```

**Purpose**

Implements zip member bytes according to the exact implementation and guards in this file.

**Inputs**

- `members` (`list[tuple[str, bytes]]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bytes`. Observed return expression(s): `stream.getvalue()`.

**Algorithm**

1. Computes `stream` from `io.BytesIO()`.
2. Enters managed context(s) `warnings.catch_warnings()` and executes: Calls `warnings.simplefilter('ignore', UserWarning)` for its validation or side effect. Enters managed context(s) `zipfile.ZipFile(stream, 'w', compression=zipfile.ZIP_DEFLATED)` and executes: Iterates `(name, content)` over `members`. For each value: Calls `archive.writestr(name, content)` for its validation or side effect.
3. Returns `stream.getvalue()`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `archive.writestr`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `archive.writestr`, `io.BytesIO`, `stream.getvalue`, `warnings.catch_warnings`, `warnings.simplefilter`, `zipfile.ZipFile`.

**Known repository callers**

- `tests/unit/test_gpu_fr.py` — `test_duplicate_zip_extraction_targets_are_rejected`
- `tests/unit/test_gpu_fr.py` — `test_zip_file_directory_target_collision_is_rejected`

**Tests**

- `tests/unit/test_gpu_fr.py::test_duplicate_zip_extraction_targets_are_rejected`
- `tests/unit/test_gpu_fr.py::test_zip_file_directory_target_collision_is_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_download`

**Signature**

```python
def _download(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    archive_bytes: bytes | None = None,
) -> GpuArchiveDownload:
```

**Purpose**

Downloads and validates download according to the exact implementation and guards in this file.

**Inputs**

- `tmp_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `monkeypatch` (`pytest.MonkeyPatch`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `archive_bytes` (`bytes | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuArchiveDownload`. Observed return expression(s): `download_gpu_document(document, _config(), tmp_path)`.

**Algorithm**

1. Computes `document` from `_document(monkeypatch)`.
2. Calls `monkeypatch.setattr(gpu, 'open_safe_https', lambda *args, **kwargs: _Response(archive_bytes or _zip_bytes()))` for its validation or side effect.
3. Returns `download_gpu_document(document, _config(), tmp_path)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `download_gpu_document`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_Response`, `_config`, `_document`, `_zip_bytes`, `download_gpu_document`, `monkeypatch.setattr`.

**Known repository callers**

- `tests/unit/test_gpu_fr.py` — `test_cached_document_lineage_change_forces_refresh`
- `tests/unit/test_gpu_fr.py` — `test_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_gpu_fr.py` — `test_expired_cache_is_refreshed`
- `tests/unit/test_gpu_fr.py` — `test_extraction_inventory_and_cache`
- `tests/unit/test_gpu_fr.py` — `test_extraction_rejects_archive_object_inconsistent_with_path`
- `tests/unit/test_gpu_fr.py` — `test_failed_refresh_preserves_previous_cache`
- `tests/unit/test_gpu_fr.py` — `test_fresh_cache_is_reused`
- `tests/unit/test_gpu_fr.py` — `test_metadata_publication_failure_rolls_back_both_cache_files`
- `tests/unit/test_gpu_fr.py` — `test_stale_download_object_rejects_replaced_valid_archive`
- `tests/unit/test_gpu_fr.py` — `test_stale_recovery_backup_rejects_cache_before_network`
- `tests/unit/test_gpu_fr.py` — `test_successful_download_persists_sha_and_sidecar`
- `tests/unit/test_gpu_fr.py` — `test_tampered_extraction_is_rebuilt_from_verified_archive`
- `tests/unit/test_gpu_fr.py` — `test_tampered_sidecar_invalidates_cache`

**Tests**

- `tests/unit/test_gpu_fr.py::test_cached_document_lineage_change_forces_refresh`
- `tests/unit/test_gpu_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_gpu_fr.py::test_expired_cache_is_refreshed`
- `tests/unit/test_gpu_fr.py::test_extraction_inventory_and_cache`
- `tests/unit/test_gpu_fr.py::test_extraction_rejects_archive_object_inconsistent_with_path`
- `tests/unit/test_gpu_fr.py::test_failed_refresh_preserves_previous_cache`
- `tests/unit/test_gpu_fr.py::test_fresh_cache_is_reused`
- `tests/unit/test_gpu_fr.py::test_metadata_publication_failure_rolls_back_both_cache_files`
- `tests/unit/test_gpu_fr.py::test_stale_download_object_rejects_replaced_valid_archive`
- `tests/unit/test_gpu_fr.py::test_stale_recovery_backup_rejects_cache_before_network`
- `tests/unit/test_gpu_fr.py::test_successful_download_persists_sha_and_sidecar`
- `tests/unit/test_gpu_fr.py::test_tampered_extraction_is_rebuilt_from_verified_archive`
- `tests/unit/test_gpu_fr.py::test_tampered_sidecar_invalidates_cache`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_planning_archive`

**Signature**

```python
def _planning_archive(tmp_path: Path) -> Path:
```

**Purpose**

Implements planning archive according to the exact implementation and guards in this file.

**Inputs**

- `tmp_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Path`. Observed return expression(s): `archive_path`.

**Algorithm**

1. Computes `package` from `tmp_path / 'package'`.
2. Calls `package.mkdir()` for its validation or side effect.
3. Computes `gpkg` from `package / 'planning.gpkg'`.
4. Computes `valid` from `Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])`.
5. Computes `invalid` from `Polygon([(0, 0), (10, 10), (10, 0), (0, 10), (0, 0)])`.
6. Computes `zoning` from `gpd.GeoDataFrame({'LIBELLE': ['U', 'N', None], 'TYPEZONE': ['U', 'N', 'AU']}, geometry=[valid, invalid, None], crs='EPSG:2154')`.
7. Computes `prescription` from `gpd.GeoDataFrame({'TYPEPSC': [5]}, geometry=[valid], crs='EPSG:2154')`.
8. Calls `zoning.to_file(gpkg, layer='zone_urba', driver='GPKG', engine='pyogrio')` for its validation or side effect.
9. Calls `prescription.to_file(gpkg, layer='prescription_surf', driver='GPKG', engine='pyogrio', mode='a')` for its validation or side effect.
10. Calls `(package / '31395_reglement.pdf').write_bytes(b'%PDF synthetic')` for its validation or side effect.
11. Calls `(package / 'metadata.xml').write_text('<metadata><standard>CNIG PLU v2017</standard></metadata>', encoding='utf-8')` for its validation or side effect.
12. Computes `archive_path` from `tmp_path / 'planning.zip'`.
13. Enters managed context(s) `zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED)` and executes: Iterates `path` over `package.rglob('*')`. For each value: Checks `path.is_file()`. When true: Calls `archive.write(path, path.relative_to(package).as_posix())` for its validation or side effect.
14. Returns `archive_path`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `(package / '31395_reglement.pdf').write_bytes`, `(package / 'metadata.xml').write_text`, `archive.write`, `package.mkdir`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `(package / '31395_reglement.pdf').write_bytes`, `(package / 'metadata.xml').write_text`, `Polygon`, `archive.write`, `gpd.GeoDataFrame`, `package.mkdir`, `package.rglob`, `path.is_file`, `path.relative_to`, `path.relative_to(package).as_posix`, `prescription.to_file`, `zipfile.ZipFile`, `zoning.to_file`.

**Known repository callers**

- `tests/unit/test_gpu_fr.py` — `test_ambiguous_zoning_layer_fails_clearly`
- `tests/unit/test_gpu_fr.py` — `test_missing_zoning_layer_fails_clearly`
- `tests/unit/test_gpu_fr.py` — `test_spatial_inventory_and_inspection_preserve_source_quality`

**Tests**

- `tests/unit/test_gpu_fr.py::test_ambiguous_zoning_layer_fails_clearly`
- `tests/unit/test_gpu_fr.py::test_missing_zoning_layer_fails_clearly`
- `tests/unit/test_gpu_fr.py::test_spatial_inventory_and_inspection_preserve_source_quality`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_mutated_loaded_api_origin_is_rejected_before_discovery_network.fail_network`

**Signature**

```python
def fail_network(*args: object, **kwargs: object) -> object:
```

**Purpose**

Implements fail network according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Executes `nonlocal network_calls`.
2. Updates `network_calls` using `` and `1`.
3. Raises `AssertionError('network used after GPU origin mutation')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `AssertionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `AssertionError`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_download_rejects_forged_written_file_provenance_before_network.fail_network`

**Signature**

```python
def fail_network(*args: object, **kwargs: object) -> object:
```

**Purpose**

Implements fail network according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Executes `nonlocal network_calls`.
2. Updates `network_calls` using `` and `1`.
3. Raises `AssertionError('forged written-file provenance reached network')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `AssertionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `AssertionError`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_stale_recovery_backup_rejects_cache_before_network.fail_network`

**Signature**

```python
def fail_network(*args: object, **kwargs: object) -> _Response:
```

**Purpose**

Implements fail network according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `_Response`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Calls `pytest.fail('stale recovery must fail before network')` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `pytest.fail`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_failed_refresh_preserves_previous_cache.fail`

**Signature**

```python
def fail(*args: object, **kwargs: object) -> _Response:
```

**Purpose**

Implements fail according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `_Response`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Raises `URLError('offline')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `URLError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `URLError`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_metadata_publication_failure_rolls_back_both_cache_files.fail_new_metadata_once`

**Signature**

```python
def fail_new_metadata_once(source: Path, target: Path) -> None:
```

**Purpose**

Implements fail new metadata once according to the exact implementation and guards in this file.

**Inputs**

- `source` (`Path`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `target` (`Path`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Executes `nonlocal failed`.
2. Checks `source.suffix == '.part' and target == sidecar_path and (not failed)`. When true: Computes `failed` from `True`. Raises `OSError('simulated metadata lock')`.
3. Calls `original_replace(source, target)` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `source.suffix == '.part' and target == sidecar_path and (not failed)` is true.

**Exceptions**

- Explicitly raises: `OSError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `original_replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `OSError`, `original_replace`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_publication_and_rollback_failure_preserves_exact_recovery_backups.fail_publication_and_rollback`

**Signature**

```python
def fail_publication_and_rollback(source: Path, target: Path) -> None:
```

**Purpose**

Implements fail publication and rollback according to the exact implementation and guards in this file.

**Inputs**

- `source` (`Path`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `target` (`Path`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `source == temporary_metadata and target == metadata_path`. When true: Raises `OSError('simulated metadata publication failure')`.
2. Checks `source == archive_backup and target == archive_path`. When true: Raises `OSError('simulated archive rollback failure')`.
3. Calls `original_replace(source, target)` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `source == temporary_metadata and target == metadata_path` is true.
- Rejects or diverts the path when `source == archive_backup and target == archive_path` is true.

**Exceptions**

- Explicitly raises: `OSError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `original_replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `OSError`, `original_replace`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_cleanup_failure_does_not_mask_double_failure_recovery_error.fail_publication_and_rollback`

**Signature**

```python
def fail_publication_and_rollback(source: Path, target: Path) -> None:
```

**Purpose**

Implements fail publication and rollback according to the exact implementation and guards in this file.

**Inputs**

- `source` (`Path`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `target` (`Path`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Executes `nonlocal rollback_failed`.
2. Checks `source == temporary_metadata and target == metadata_path`. When true: Raises `OSError('simulated metadata publication failure')`.
3. Checks `source == archive_backup and target == first.path`. When true: Computes `rollback_failed` from `True`. Raises `OSError('simulated archive rollback failure')`.
4. Calls `original_replace(source, target)` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `source == temporary_metadata and target == metadata_path` is true.
- Rejects or diverts the path when `source == archive_backup and target == first.path` is true.

**Exceptions**

- Explicitly raises: `OSError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `original_replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `OSError`, `original_replace`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_cleanup_failure_does_not_mask_double_failure_recovery_error.fail_temporary_cleanup`

**Signature**

```python
def fail_temporary_cleanup(path: Path, *, missing_ok: bool = False) -> None:
```

**Purpose**

Implements fail temporary cleanup according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `missing_ok` (`bool`; optional/default `False`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `rollback_failed and path == temporary_metadata`. When true: Raises `PermissionError('simulated temporary cleanup failure')`.
2. Calls `original_unlink(path, missing_ok=missing_ok)` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `rollback_failed and path == temporary_metadata` is true.

**Exceptions**

- Explicitly raises: `PermissionError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `original_unlink`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `PermissionError`, `original_unlink`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_preexisting_temporary_archive_symlink_cannot_modify_target.simulated_is_symlink`

**Signature**

```python
def simulated_is_symlink(path: Path) -> bool:
```

**Purpose**

Implements simulated is symlink according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `path == temporary_archive or original_is_symlink(path)`.

**Algorithm**

1. Returns `path == temporary_archive or original_is_symlink(path)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `original_is_symlink`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_preexisting_temporary_archive_symlink_cannot_modify_target.simulated_symlink_open`

**Signature**

```python
def simulated_symlink_open(
        path: Path, *args: object, **kwargs: object
    ) -> object:
```

**Purpose**

Implements simulated symlink open according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. Observed return expression(s): `original_open(path, *args, **kwargs)`; `original_open(sentinel, *args, **kwargs)`.

**Algorithm**

1. Checks `path == temporary_archive`. When true: Returns `original_open(sentinel, *args, **kwargs)`.
2. Returns `original_open(path, *args, **kwargs)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `original_open`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `original_open`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_preexisting_temporary_archive_symlink_cannot_modify_target.record_network`

**Signature**

```python
def record_network(*args: object, **kwargs: object) -> _Response:
```

**Purpose**

Implements record network according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `_Response`. Observed return expression(s): `_Response(_zip_bytes())`.

**Algorithm**

1. Executes `nonlocal opener_calls`.
2. Updates `opener_calls` using `` and `1`.
3. Returns `_Response(_zip_bytes())`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_Response`, `_zip_bytes`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_extraction_from_archive`

**Signature**

```python
def _extraction_from_archive(path: Path, tmp_path: Path) -> GpuExtraction:
```

**Purpose**

Implements extraction from archive according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `tmp_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuExtraction`. Observed return expression(s): `extract_gpu_document(download, tmp_path / 'cache')`.

**Algorithm**

1. Computes `document` from `gpu.GpuDocumentMetadata(provider='GPU', portal='GPU', commune_code='31395', partition='DU_31395', document_id='doc-1', document_family='DU', document_type='PLU', document_title=None, status='document.production', legal_status='APPROVED', effective_status='EN_VIGUEUR', version=None, archive_name=path.stem, publication_…`.
2. Computes `download` from `GpuArchiveDownload(document=document, download_timestamp=datetime.now(UTC).isoformat(), filename=path.name, archive_format='zip', file_size=path.stat().st_size, sha256=gpu._sha256(path), path=path, cache_hit=False)`.
3. Returns `extract_gpu_document(download, tmp_path / 'cache')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `GpuArchiveDownload`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GpuArchiveDownload`, `datetime.now`, `datetime.now(UTC).isoformat`, `extract_gpu_document`, `gpu.GpuDocumentMetadata`, `gpu._sha256`, `path.stat`.

**Known repository callers**

- `tests/unit/test_gpu_fr.py` — `test_ambiguous_zoning_layer_fails_clearly`
- `tests/unit/test_gpu_fr.py` — `test_missing_zoning_layer_fails_clearly`
- `tests/unit/test_gpu_fr.py` — `test_spatial_inventory_and_inspection_preserve_source_quality`

**Tests**

- `tests/unit/test_gpu_fr.py::test_ambiguous_zoning_layer_fails_clearly`
- `tests/unit/test_gpu_fr.py::test_missing_zoning_layer_fails_clearly`
- `tests/unit/test_gpu_fr.py::test_spatial_inventory_and_inspection_preserve_source_quality`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_config_and_urls`

**Signature**

```python
def test_valid_config_and_urls() -> None:
```

**Purpose**

Protects the `valid config and urls` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `config` from `_config()`.

**Action**

- Calls `_config`, `build_gpu_document_list_url`, `build_gpu_partition`, `build_gpu_partition_download_url`, `build_gpu_partition_download_url(config).endswith`.

**Expected result**

- Direct assertions: `assert build_gpu_partition(config) == 'DU_31395'`; `assert 'partition=DU_31395' in build_gpu_document_list_url(config)`; `assert build_gpu_partition_download_url(config).endswith('/document/download-by-partition/DU_31395')`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `valid config and urls` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `build_gpu_document_list_url`, `build_gpu_partition`, `build_gpu_partition_download_url`, `build_gpu_partition_download_url(config).endswith`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_config_values_are_rejected`

**Signature**

```python
def test_invalid_config_values_are_rejected(path: tuple[str, str], value: object) -> None:
```

**Purpose**

Protects the `invalid config values are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `path`, `value`.
- Contains 3 explicit setup/context statement(s).
- Computes `payload` from `_config().model_dump(mode='json')`.
- Computes `payload[path[0]][path[1]]` from `value`.
- Enters managed context(s) `pytest.raises(ValidationError)` and executes: Calls `GpuSourceConfig.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `GpuSourceConfig.model_validate`, `_config`, `_config().model_dump`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError): GpuSourceConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `invalid config values are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `GpuSourceConfig.model_validate`, `_config`, `_config().model_dump`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_mutated_loaded_api_origin_is_rejected_before_discovery_network`

**Signature**

```python
def test_mutated_loaded_api_origin_is_rejected_before_discovery_network(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `mutated loaded api origin is rejected before discovery network` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 4 explicit setup/context statement(s).
- Computes `config` from `_config()`.
- Computes `config.api.base_url` from `HttpUrl('https://unrelated.example/api')`.
- Computes `network_calls` from `0`.
- Enters managed context(s) `pytest.raises(GpuDiscoveryError, match='config|official|origin')` and executes: Calls `discover_current_gpu_document(config)` for its validation or side effect.

**Action**

- Calls `AssertionError`, `HttpUrl`, `_config`, `discover_current_gpu_document`, `monkeypatch.setattr`.

**Expected result**

- Direct assertions: `assert network_calls == 0`.
- Expected exception contexts: `with pytest.raises(GpuDiscoveryError, match='config|official|origin'): discover_current_gpu_document(config)`.

**Regression protected**

- Protects the exact `mutated loaded api origin is rejected before discovery network` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `AssertionError`, `HttpUrl`, `_config`, `discover_current_gpu_document`, `monkeypatch.setattr`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unknown_config_field_is_rejected`

**Signature**

```python
def test_unknown_config_field_is_rejected() -> None:
```

**Purpose**

Protects the `unknown config field is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `payload` from `_config().model_dump(mode='json')`.
- Computes `payload['unexpected']` from `True`.
- Enters managed context(s) `pytest.raises(ValidationError)` and executes: Calls `GpuSourceConfig.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `GpuSourceConfig.model_validate`, `_config`, `_config().model_dump`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError): GpuSourceConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `unknown config field is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `GpuSourceConfig.model_validate`, `_config`, `_config().model_dump`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_document_discovery_success`

**Signature**

```python
def test_document_discovery_success(monkeypatch: pytest.MonkeyPatch) -> None:
```

**Purpose**

Protects the `document discovery success` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 1 explicit setup/context statement(s).
- Computes `document` from `_document(monkeypatch)`.

**Action**

- Calls `_document`.

**Expected result**

- Direct assertions: `assert document.document_id == 'doc-1'`; `assert document.document_type == 'PLU'`; `assert document.effective_status == 'EN_VIGUEUR'`; `assert document.archive_name == '31395_PLU_20240215'`; `assert document.version is None`; `assert document.written_files[0].title == 'Règlement écrit'`; `assert document.written_files[0].source_url == 'https://www.geoportail-urbanisme.gouv.fr/api/document/doc-1/files/reglement.pdf'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `document discovery success` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_document`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_written_material_url_must_be_exact_official_https_api_url`

**Signature**

```python
def test_written_material_url_must_be_exact_official_https_api_url(
    monkeypatch: pytest.MonkeyPatch,
    source_url: str,
) -> None:
```

**Purpose**

Protects the `written material url must be exact official https api url` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`, `source_url`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(GpuDiscoveryError, match='written material URL')` and executes: Calls `discover_current_gpu_document(_config())` for its validation or side effect.

**Action**

- Calls `_config`, `_details`, `_files`, `_listing_item`, `_patch_json_responses`, `discover_current_gpu_document`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GpuDiscoveryError, match='written material URL'): discover_current_gpu_document(_config())`.

**Regression protected**

- Protects the exact `written material url must be exact official https api url` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_details`, `_files`, `_listing_item`, `_patch_json_responses`, `discover_current_gpu_document`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_written_material_fallback_rejects_unsafe_archive_url_provenance`

**Signature**

```python
def test_written_material_fallback_rejects_unsafe_archive_url_provenance(
    monkeypatch: pytest.MonkeyPatch,
    archive_url: str,
) -> None:
```

**Purpose**

Protects the `written material fallback rejects unsafe archive url provenance` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`, `archive_url`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(GpuDiscoveryError, match='archive URL')` and executes: Calls `discover_current_gpu_document(_config())` for its validation or side effect.

**Action**

- Calls `_config`, `_details`, `_files`, `_listing_item`, `_patch_json_responses`, `discover_current_gpu_document`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GpuDiscoveryError, match='archive URL'): discover_current_gpu_document(_config())`.

**Regression protected**

- Protects the exact `written material fallback rejects unsafe archive url provenance` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_details`, `_files`, `_listing_item`, `_patch_json_responses`, `discover_current_gpu_document`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_no_current_document_is_rejected`

**Signature**

```python
def test_no_current_document_is_rejected(monkeypatch: pytest.MonkeyPatch) -> None:
```

**Purpose**

Protects the `no current document is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(GpuDiscoveryError, match='No current')` and executes: Calls `discover_current_gpu_document(_config())` for its validation or side effect.

**Action**

- Calls `_config`, `_listing_item`, `_patch_json_responses`, `discover_current_gpu_document`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GpuDiscoveryError, match='No current'): discover_current_gpu_document(_config())`.

**Regression protected**

- Protects the exact `no current document is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_listing_item`, `_patch_json_responses`, `discover_current_gpu_document`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_ambiguous_current_documents_are_rejected`

**Signature**

```python
def test_ambiguous_current_documents_are_rejected(monkeypatch: pytest.MonkeyPatch) -> None:
```

**Purpose**

Protects the `ambiguous current documents are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(GpuDiscoveryError, match='Ambiguous')` and executes: Calls `discover_current_gpu_document(_config())` for its validation or side effect.

**Action**

- Calls `_config`, `_listing_item`, `_patch_json_responses`, `discover_current_gpu_document`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GpuDiscoveryError, match='Ambiguous'): discover_current_gpu_document(_config())`.

**Regression protected**

- Protects the exact `ambiguous current documents are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_listing_item`, `_patch_json_responses`, `discover_current_gpu_document`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_document_identity_is_rejected`

**Signature**

```python
def test_missing_document_identity_is_rejected(
    monkeypatch: pytest.MonkeyPatch, field: str
) -> None:
```

**Purpose**

Protects the `missing document identity is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`, `field`.
- Contains 2 explicit setup/context statement(s).
- Computes `item` from `_listing_item()`.
- Enters managed context(s) `pytest.raises(GpuDiscoveryError, match='missing')` and executes: Calls `discover_current_gpu_document(_config())` for its validation or side effect.

**Action**

- Calls `_config`, `_listing_item`, `_patch_json_responses`, `discover_current_gpu_document`, `item.pop`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GpuDiscoveryError, match='missing'): discover_current_gpu_document(_config())`.

**Regression protected**

- Protects the exact `missing document identity is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_listing_item`, `_patch_json_responses`, `discover_current_gpu_document`, `item.pop`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_document_details_must_match_selected_listing`

**Signature**

```python
def test_document_details_must_match_selected_listing(
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    different_value: str,
) -> None:
```

**Purpose**

Protects the `document details must match selected listing` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`, `field`, `different_value`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(GpuDiscoveryError, match='match|changed|current')` and executes: Calls `discover_current_gpu_document(_config())` for its validation or side effect.

**Action**

- Calls `_config`, `_details`, `_files`, `_listing_item`, `_patch_json_responses`, `discover_current_gpu_document`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GpuDiscoveryError, match='match|changed|current'): discover_current_gpu_document(_config())`.

**Regression protected**

- Protects the exact `document details must match selected listing` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_details`, `_files`, `_listing_item`, `_patch_json_responses`, `discover_current_gpu_document`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_document_details_commune_must_match_selected_listing`

**Signature**

```python
def test_document_details_commune_must_match_selected_listing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `document details commune must match selected listing` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(GpuDiscoveryError, match='match')` and executes: Calls `discover_current_gpu_document(_config())` for its validation or side effect.

**Action**

- Calls `_config`, `_details`, `_files`, `_listing_item`, `_patch_json_responses`, `discover_current_gpu_document`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GpuDiscoveryError, match='match'): discover_current_gpu_document(_config())`.

**Regression protected**

- Protects the exact `document details commune must match selected listing` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_details`, `_files`, `_listing_item`, `_patch_json_responses`, `discover_current_gpu_document`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_discovery_rejects_unsafe_archive_name`

**Signature**

```python
def test_discovery_rejects_unsafe_archive_name(
    monkeypatch: pytest.MonkeyPatch,
    archive_name: str,
) -> None:
```

**Purpose**

Protects the `discovery rejects unsafe archive name` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`, `archive_name`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(GpuDiscoveryError, match='archive name|safe')` and executes: Calls `discover_current_gpu_document(_config())` for its validation or side effect.

**Action**

- Calls `_config`, `_details`, `_files`, `_listing_item`, `_patch_json_responses`, `discover_current_gpu_document`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GpuDiscoveryError, match='archive name|safe'): discover_current_gpu_document(_config())`.

**Regression protected**

- Protects the exact `discovery rejects unsafe archive name` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_details`, `_files`, `_listing_item`, `_patch_json_responses`, `discover_current_gpu_document`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_successful_download_persists_sha_and_sidecar`

**Signature**

```python
def test_successful_download_persists_sha_and_sidecar(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

**Purpose**

Protects the `successful download persists sha and sidecar` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_download(tmp_path, monkeypatch)`.
- Computes `sidecar` from `json.loads((tmp_path / f'{result.filename}.metadata.json').read_text())`.

**Action**

- Calls `(tmp_path / f'{result.filename}.metadata.json').read_text`, `_download`, `json.loads`, `result.path.is_file`, `tmp_path.glob`.

**Expected result**

- Direct assertions: `assert result.path.is_file()`; `assert result.file_size > 0`; `assert len(result.sha256) == 64`; `assert sidecar['sha256'] == result.sha256`; `assert sidecar['document']['document_id'] == 'doc-1'`; `assert not list(tmp_path.glob('*.part'))`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `successful download persists sha and sidecar` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `(tmp_path / f'{result.filename}.metadata.json').read_text`, `_download`, `json.loads`, `len`, `list`, `result.path.is_file`, `tmp_path.glob`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_download_rejects_document_inconsistent_with_config`

**Signature**

```python
def test_download_rejects_document_inconsistent_with_config(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    different_value: str,
) -> None:
```

**Purpose**

Protects the `download rejects document inconsistent with config` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`, `field`, `different_value`.
- Contains 2 explicit setup/context statement(s).
- Computes `document` from `replace(_document(monkeypatch), **{field: different_value})`.
- Enters managed context(s) `pytest.raises(GpuDownloadError, match='document|identity|config')` and executes: Calls `download_gpu_document(document, _config(), tmp_path)` for its validation or side effect.

**Action**

- Calls `_config`, `_document`, `any`, `download_gpu_document`, `monkeypatch.setattr`, `replace`, `tmp_path.iterdir`.

**Expected result**

- Direct assertions: `assert not any(tmp_path.iterdir())`.
- Expected exception contexts: `with pytest.raises(GpuDownloadError, match='document|identity|config'): download_gpu_document(document, _config(), tmp_path)`.

**Regression protected**

- Protects the exact `download rejects document inconsistent with config` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_document`, `any`, `download_gpu_document`, `monkeypatch.setattr`, `pytest.fail`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `tmp_path.iterdir`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_download_rejects_forged_written_file_provenance_before_network`

**Signature**

```python
def test_download_rejects_forged_written_file_provenance_before_network(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation: str,
) -> None:
```

**Purpose**

Protects the `download rejects forged written file provenance before network` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`, `mutation`.
- Contains 4 explicit setup/context statement(s).
- Computes `original` from `_document(monkeypatch)`.
- Computes `document` from `replace(original, written_files=written_files)`.
- Computes `network_calls` from `0`.
- Enters managed context(s) `pytest.raises(GpuDownloadError, match='written|document|source|URL')` and executes: Calls `download_gpu_document(document, _config(), tmp_path)` for its validation or side effect.

**Action**

- Calls `AssertionError`, `_config`, `_document`, `download_gpu_document`, `monkeypatch.setattr`, `object`, `replace`.

**Expected result**

- Direct assertions: `assert network_calls == 0`.
- Expected exception contexts: `with pytest.raises(GpuDownloadError, match='written|document|source|URL'): download_gpu_document(document, _config(), tmp_path)`.

**Regression protected**

- Protects the exact `download rejects forged written file provenance before network` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `AssertionError`, `_config`, `_document`, `download_gpu_document`, `monkeypatch.setattr`, `object`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_download_rejects_forged_unsafe_archive_name_before_io`

**Signature**

```python
def test_download_rejects_forged_unsafe_archive_name_before_io(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    archive_name: str,
) -> None:
```

**Purpose**

Protects the `download rejects forged unsafe archive name before io` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`, `archive_name`.
- Contains 2 explicit setup/context statement(s).
- Computes `document` from `replace(_document(monkeypatch), archive_name=archive_name)`.
- Enters managed context(s) `pytest.raises(GpuDownloadError, match='archive name|archive filename|safe')` and executes: Calls `download_gpu_document(document, _config(), tmp_path / 'cache')` for its validation or side effect.

**Action**

- Calls `(tmp_path / 'escape.zip').exists`, `_config`, `_document`, `download_gpu_document`, `monkeypatch.setattr`, `replace`.

**Expected result**

- Direct assertions: `assert not (tmp_path / 'escape.zip').exists()`.
- Expected exception contexts: `with pytest.raises(GpuDownloadError, match='archive name|archive filename|safe'): download_gpu_document(document, _config(), tmp_path / 'cache')`.

**Regression protected**

- Protects the exact `download rejects forged unsafe archive name before io` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `(tmp_path / 'escape.zip').exists`, `_config`, `_document`, `download_gpu_document`, `monkeypatch.setattr`, `pytest.fail`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_archive_name_with_one_zip_suffix_is_not_duplicated`

**Signature**

```python
def test_archive_name_with_one_zip_suffix_is_not_duplicated(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `archive name with one zip suffix is not duplicated` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 2 explicit setup/context statement(s).
- Computes `document` from `replace(_document(monkeypatch), archive_name='safe-name.zip')`.
- Computes `result` from `download_gpu_document(document, _config(), tmp_path)`.

**Action**

- Calls `_Response`, `_config`, `_document`, `_zip_bytes`, `download_gpu_document`, `monkeypatch.setattr`, `replace`.

**Expected result**

- Direct assertions: `assert result.filename == 'safe-name.zip'`; `assert result.path == tmp_path / 'safe-name.zip'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `archive name with one zip suffix is not duplicated` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_Response`, `_config`, `_document`, `_zip_bytes`, `download_gpu_document`, `monkeypatch.setattr`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_fresh_cache_is_reused`

**Signature**

```python
def test_fresh_cache_is_reused(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

**Purpose**

Protects the `fresh cache is reused` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 2 explicit setup/context statement(s).
- Computes `first` from `_download(tmp_path, monkeypatch)`.
- Computes `second` from `download_gpu_document(first.document, _config(), tmp_path)`.

**Action**

- Calls `_config`, `_download`, `download_gpu_document`, `monkeypatch.setattr`.

**Expected result**

- Direct assertions: `assert second.cache_hit`; `assert second.sha256 == first.sha256`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `fresh cache is reused` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_download`, `download_gpu_document`, `monkeypatch.setattr`, `pytest.fail`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_stale_recovery_backup_rejects_cache_before_network`

**Signature**

```python
def test_stale_recovery_backup_rejects_cache_before_network(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

**Purpose**

Protects the `stale recovery backup rejects cache before network` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 4 explicit setup/context statement(s).
- Computes `first` from `_download(tmp_path, monkeypatch)`.
- Computes `recovery_path` from `first.path.with_suffix(f'{first.path.suffix}.bak')`.
- Computes `recovery_bytes` from `b'manual GPU recovery material'`.
- Enters managed context(s) `pytest.raises(GpuDownloadError, match='backup|recovery|manual')` and executes: Calls `download_gpu_document(first.document, _config(), tmp_path)` for its validation or side effect.

**Action**

- Calls `_config`, `_download`, `download_gpu_document`, `first.path.with_suffix`, `monkeypatch.setattr`, `recovery_path.read_bytes`, `recovery_path.write_bytes`.

**Expected result**

- Direct assertions: `assert recovery_path.read_bytes() == recovery_bytes`.
- Expected exception contexts: `with pytest.raises(GpuDownloadError, match='backup|recovery|manual'): download_gpu_document(first.document, _config(), tmp_path)`.

**Regression protected**

- Protects the exact `stale recovery backup rejects cache before network` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_download`, `download_gpu_document`, `first.path.with_suffix`, `monkeypatch.setattr`, `pytest.fail`, `pytest.raises`, `recovery_path.read_bytes`, `recovery_path.write_bytes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_expired_cache_is_refreshed`

**Signature**

```python
def test_expired_cache_is_refreshed(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

**Purpose**

Protects the `expired cache is refreshed` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 6 explicit setup/context statement(s).
- Computes `first` from `_download(tmp_path, monkeypatch)`.
- Computes `sidecar_path` from `tmp_path / f'{first.filename}.metadata.json'`.
- Computes `sidecar` from `json.loads(sidecar_path.read_text())`.
- Computes `sidecar['download_timestamp']` from `(datetime.now(UTC) - timedelta(days=8)).isoformat()`.
- Computes `fresh_bytes` from `_zip_bytes({'fresh.txt': b'fresh'})`.
- Computes `refreshed` from `download_gpu_document(first.document, _config(), tmp_path)`.

**Action**

- Calls `(datetime.now(UTC) - timedelta(days=8)).isoformat`, `_Response`, `_config`, `_download`, `_zip_bytes`, `datetime.now`, `download_gpu_document`, `json.dumps`, `json.loads`, `monkeypatch.setattr`, `sidecar_path.read_text`, `sidecar_path.write_text`, `timedelta`.

**Expected result**

- Direct assertions: `assert not refreshed.cache_hit`; `assert refreshed.sha256 != first.sha256`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `expired cache is refreshed` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `(datetime.now(UTC) - timedelta(days=8)).isoformat`, `_Response`, `_config`, `_download`, `_zip_bytes`, `datetime.now`, `download_gpu_document`, `json.dumps`, `json.loads`, `monkeypatch.setattr`, `sidecar_path.read_text`, `sidecar_path.write_text`, `timedelta`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_failed_refresh_preserves_previous_cache`

**Signature**

```python
def test_failed_refresh_preserves_previous_cache(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

**Purpose**

Protects the `failed refresh preserves previous cache` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 7 explicit setup/context statement(s).
- Computes `first` from `_download(tmp_path, monkeypatch)`.
- Computes `sidecar_path` from `tmp_path / f'{first.filename}.metadata.json'`.
- Computes `sidecar` from `json.loads(sidecar_path.read_text())`.
- Computes `sidecar['download_timestamp']` from `(datetime.now(UTC) - timedelta(days=8)).isoformat()`.
- Computes `old_archive` from `first.path.read_bytes()`.
- Computes `old_sidecar` from `sidecar_path.read_bytes()`.
- Enters managed context(s) `pytest.raises(GpuDownloadError)` and executes: Calls `download_gpu_document(first.document, _config(), tmp_path)` for its validation or side effect.

**Action**

- Calls `(datetime.now(UTC) - timedelta(days=8)).isoformat`, `URLError`, `_config`, `_download`, `datetime.now`, `download_gpu_document`, `first.path.read_bytes`, `json.dumps`, `json.loads`, `monkeypatch.setattr`, `sidecar_path.read_bytes`, `sidecar_path.read_text`, `sidecar_path.write_text`, `timedelta`, `tmp_path.glob`.

**Expected result**

- Direct assertions: `assert first.path.read_bytes() == old_archive`; `assert sidecar_path.read_bytes() == old_sidecar`; `assert not list(tmp_path.glob('*.part'))`.
- Expected exception contexts: `with pytest.raises(GpuDownloadError): download_gpu_document(first.document, _config(), tmp_path)`.

**Regression protected**

- Protects the exact `failed refresh preserves previous cache` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `(datetime.now(UTC) - timedelta(days=8)).isoformat`, `URLError`, `_config`, `_download`, `datetime.now`, `download_gpu_document`, `first.path.read_bytes`, `json.dumps`, `json.loads`, `list`, `monkeypatch.setattr`, `pytest.raises`, `sidecar_path.read_bytes`, `sidecar_path.read_text`, `sidecar_path.write_text`, `timedelta`, `tmp_path.glob`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_metadata_publication_failure_rolls_back_both_cache_files`

**Signature**

```python
def test_metadata_publication_failure_rolls_back_both_cache_files(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

**Purpose**

Protects the `metadata publication failure rolls back both cache files` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 9 explicit setup/context statement(s).
- Computes `first` from `_download(tmp_path, monkeypatch)`.
- Computes `sidecar_path` from `tmp_path / f'{first.filename}.metadata.json'`.
- Computes `sidecar` from `json.loads(sidecar_path.read_text())`.
- Computes `sidecar['download_timestamp']` from `(datetime.now(UTC) - timedelta(days=8)).isoformat()`.
- Computes `old_archive` from `first.path.read_bytes()`.
- Computes `old_sidecar` from `sidecar_path.read_bytes()`.
- Computes `original_replace` from `gpu._replace_file`.
- Computes `failed` from `False`.
- Enters managed context(s) `pytest.raises(GpuDownloadError)` and executes: Calls `download_gpu_document(first.document, _config(), tmp_path)` for its validation or side effect.

**Action**

- Calls `(datetime.now(UTC) - timedelta(days=8)).isoformat`, `OSError`, `_Response`, `_config`, `_download`, `_zip_bytes`, `datetime.now`, `download_gpu_document`, `first.path.read_bytes`, `json.dumps`, `json.loads`, `monkeypatch.setattr`, `original_replace`, `sidecar_path.read_bytes`, `sidecar_path.read_text`, `sidecar_path.write_text`, `timedelta`, `tmp_path.glob`.

**Expected result**

- Direct assertions: `assert first.path.read_bytes() == old_archive`; `assert sidecar_path.read_bytes() == old_sidecar`; `assert not list(tmp_path.glob('*.part'))`; `assert not list(tmp_path.glob('*.bak'))`.
- Expected exception contexts: `with pytest.raises(GpuDownloadError): download_gpu_document(first.document, _config(), tmp_path)`.

**Regression protected**

- Protects the exact `metadata publication failure rolls back both cache files` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `(datetime.now(UTC) - timedelta(days=8)).isoformat`, `OSError`, `_Response`, `_config`, `_download`, `_zip_bytes`, `datetime.now`, `download_gpu_document`, `first.path.read_bytes`, `json.dumps`, `json.loads`, `list`, `monkeypatch.setattr`, `original_replace`, `pytest.raises`, `sidecar_path.read_bytes`, `sidecar_path.read_text`, `sidecar_path.write_text`, `timedelta`, `tmp_path.glob`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_publication_and_rollback_failure_preserves_exact_recovery_backups`

**Signature**

```python
def test_publication_and_rollback_failure_preserves_exact_recovery_backups(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

**Purpose**

Protects the `publication and rollback failure preserves exact recovery backups` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 10 explicit setup/context statement(s).
- Computes `archive_path` from `tmp_path / 'cached.zip'`.
- Computes `metadata_path` from `tmp_path / 'cached.zip.metadata.json'`.
- Computes `temporary_archive` from `tmp_path / 'cached.zip.part'`.
- Computes `temporary_metadata` from `tmp_path / 'cached.zip.metadata.json.part'`.
- Computes `old_archive` from `b'exact old archive'`.
- Computes `old_metadata` from `b'exact old metadata'`.
- Computes `archive_backup` from `archive_path.with_suffix(f'{archive_path.suffix}.bak')`.
- Computes `metadata_backup` from `metadata_path.with_suffix(f'{metadata_path.suffix}.bak')`.
- Computes `original_replace` from `gpu._replace_file`.
- Enters managed context(s) `pytest.raises(GpuDownloadError, match='rollback')` and executes: Calls `gpu._publish_cache_pair(temporary_archive, temporary_metadata, archive_path, metadata_path)` for its validation or side effect.

**Action**

- Calls `OSError`, `archive_backup.read_bytes`, `archive_path.with_suffix`, `archive_path.write_bytes`, `gpu._publish_cache_pair`, `metadata_backup.read_bytes`, `metadata_path.with_suffix`, `metadata_path.write_bytes`, `monkeypatch.setattr`, `original_replace`, `temporary_archive.write_bytes`, `temporary_metadata.write_bytes`.

**Expected result**

- Direct assertions: `assert archive_backup.read_bytes() == old_archive`; `assert metadata_backup.read_bytes() == old_metadata`.
- Expected exception contexts: `with pytest.raises(GpuDownloadError, match='rollback'): gpu._publish_cache_pair(temporary_archive, temporary_metadata, archive_path, metadata_path)`.

**Regression protected**

- Protects the exact `publication and rollback failure preserves exact recovery backups` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `OSError`, `archive_backup.read_bytes`, `archive_path.with_suffix`, `archive_path.write_bytes`, `gpu._publish_cache_pair`, `metadata_backup.read_bytes`, `metadata_path.with_suffix`, `metadata_path.write_bytes`, `monkeypatch.setattr`, `original_replace`, `pytest.raises`, `temporary_archive.write_bytes`, `temporary_metadata.write_bytes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_cleanup_failure_does_not_mask_double_failure_recovery_error`

**Signature**

```python
def test_cleanup_failure_does_not_mask_double_failure_recovery_error(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

**Purpose**

Protects the `cleanup failure does not mask double failure recovery error` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 13 explicit setup/context statement(s).
- Computes `first` from `_download(tmp_path, monkeypatch)`.
- Computes `metadata_path` from `tmp_path / f'{first.filename}.metadata.json'`.
- Computes `metadata` from `json.loads(metadata_path.read_text())`.
- Computes `metadata['download_timestamp']` from `(datetime.now(UTC) - timedelta(days=8)).isoformat()`.
- Computes `old_archive` from `first.path.read_bytes()`.
- Computes `old_metadata` from `metadata_path.read_bytes()`.
- Computes `temporary_metadata` from `metadata_path.with_suffix(f'{metadata_path.suffix}.part')`.
- Computes `archive_backup` from `first.path.with_suffix(f'{first.path.suffix}.bak')`.
- Computes `metadata_backup` from `metadata_path.with_suffix(f'{metadata_path.suffix}.bak')`.
- Computes `original_replace` from `gpu._replace_file`.
- Computes `original_unlink` from `Path.unlink`.
- Computes `rollback_failed` from `False`.

**Action**

- Calls `(datetime.now(UTC) - timedelta(days=8)).isoformat`, `OSError`, `PermissionError`, `_Response`, `_config`, `_download`, `_zip_bytes`, `archive_backup.read_bytes`, `datetime.now`, `download_gpu_document`, `first.path.read_bytes`, `first.path.with_suffix`, `json.dumps`, `json.loads`, `metadata_backup.read_bytes`, `metadata_path.read_bytes`, `metadata_path.read_text`, `metadata_path.with_suffix`, `metadata_path.write_text`, `monkeypatch.setattr`, `original_replace`, `original_unlink`, `timedelta`.

**Expected result**

- Direct assertions: `assert archive_backup.read_bytes() == old_archive`; `assert metadata_backup.read_bytes() == old_metadata`.
- Expected exception contexts: `with pytest.raises(GpuDownloadError, match='rollback'): download_gpu_document(first.document, _config(), tmp_path)`.

**Regression protected**

- Protects the exact `cleanup failure does not mask double failure recovery error` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `(datetime.now(UTC) - timedelta(days=8)).isoformat`, `OSError`, `PermissionError`, `_Response`, `_config`, `_download`, `_zip_bytes`, `archive_backup.read_bytes`, `datetime.now`, `download_gpu_document`, `first.path.read_bytes`, `first.path.with_suffix`, `json.dumps`, `json.loads`, `metadata_backup.read_bytes`, `metadata_path.read_bytes`, `metadata_path.read_text`, `metadata_path.with_suffix`, `metadata_path.write_text`, `monkeypatch.setattr`, `original_replace`, `original_unlink`, `pytest.raises`, `timedelta`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_stale_cache_recovery_backup_fails_closed_without_destroying_it`

**Signature**

```python
def test_stale_cache_recovery_backup_fails_closed_without_destroying_it(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `stale cache recovery backup fails closed without destroying it` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 6 explicit setup/context statement(s).
- Computes `archive_path` from `tmp_path / 'cached.zip'`.
- Computes `metadata_path` from `tmp_path / 'cached.zip.metadata.json'`.
- Computes `temporary_archive` from `tmp_path / 'cached.zip.part'`.
- Computes `temporary_metadata` from `tmp_path / 'cached.zip.metadata.json.part'`.
- Computes `archive_backup` from `tmp_path / 'cached.zip.bak'`.
- Enters managed context(s) `pytest.raises(GpuDownloadError, match='backup|recovery|manual')` and executes: Calls `gpu._publish_cache_pair(temporary_archive, temporary_metadata, archive_path, metadata_path)` for its validation or side effect.

**Action**

- Calls `archive_backup.read_bytes`, `archive_backup.write_bytes`, `archive_path.read_bytes`, `archive_path.write_bytes`, `gpu._publish_cache_pair`, `metadata_path.read_bytes`, `metadata_path.write_bytes`, `temporary_archive.write_bytes`, `temporary_metadata.write_bytes`.

**Expected result**

- Direct assertions: `assert archive_path.read_bytes() == b'old archive'`; `assert metadata_path.read_bytes() == b'old metadata'`; `assert archive_backup.read_bytes() == b'manual recovery archive'`.
- Expected exception contexts: `with pytest.raises(GpuDownloadError, match='backup|recovery|manual'): gpu._publish_cache_pair(temporary_archive, temporary_metadata, archive_path, metadata_path)`.

**Regression protected**

- Protects the exact `stale cache recovery backup fails closed without destroying it` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `archive_backup.read_bytes`, `archive_backup.write_bytes`, `archive_path.read_bytes`, `archive_path.write_bytes`, `gpu._publish_cache_pair`, `metadata_path.read_bytes`, `metadata_path.write_bytes`, `pytest.raises`, `temporary_archive.write_bytes`, `temporary_metadata.write_bytes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_preexisting_temporary_archive_symlink_cannot_modify_target`

**Signature**

```python
def test_preexisting_temporary_archive_symlink_cannot_modify_target(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

**Purpose**

Protects the `preexisting temporary archive symlink cannot modify target` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 9 explicit setup/context statement(s).
- Computes `document` from `_document(monkeypatch)`.
- Computes `filename` from `gpu._safe_gpu_archive_filename(document.archive_name)`.
- Computes `temporary_archive` from `tmp_path / f'{filename}.part'`.
- Computes `sentinel` from `tmp_path / 'do-not-overwrite.txt'`.
- Computes `sentinel_bytes` from `b'irreplaceable sentinel bytes'`.
- Computes `original_is_symlink` from `Path.is_symlink`.
- Computes `original_open` from `Path.open`.
- Computes `opener_calls` from `0`.
- Enters managed context(s) `pytest.raises(GpuDownloadError)` and executes: Calls `download_gpu_document(document, _config(), tmp_path)` for its validation or side effect.

**Action**

- Calls `_Response`, `_config`, `_document`, `_zip_bytes`, `download_gpu_document`, `gpu._safe_gpu_archive_filename`, `monkeypatch.setattr`, `original_is_symlink`, `original_open`, `sentinel.read_bytes`, `sentinel.write_bytes`.

**Expected result**

- Direct assertions: `assert opener_calls == 0`; `assert sentinel.read_bytes() == sentinel_bytes`.
- Expected exception contexts: `with pytest.raises(GpuDownloadError): download_gpu_document(document, _config(), tmp_path)`.

**Regression protected**

- Protects the exact `preexisting temporary archive symlink cannot modify target` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_Response`, `_config`, `_document`, `_zip_bytes`, `download_gpu_document`, `gpu._safe_gpu_archive_filename`, `monkeypatch.setattr`, `original_is_symlink`, `original_open`, `pytest.raises`, `sentinel.read_bytes`, `sentinel.write_bytes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_corrupt_download_is_rejected`

**Signature**

```python
def test_corrupt_download_is_rejected(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

**Purpose**

Protects the `corrupt download is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 2 explicit setup/context statement(s).
- Computes `document` from `_document(monkeypatch)`.
- Enters managed context(s) `pytest.raises(GpuDownloadError)` and executes: Calls `download_gpu_document(document, _config(), tmp_path)` for its validation or side effect.

**Action**

- Calls `_Response`, `_config`, `_document`, `download_gpu_document`, `monkeypatch.setattr`, `tmp_path.glob`.

**Expected result**

- Direct assertions: `assert not list(tmp_path.glob('*.part'))`.
- Expected exception contexts: `with pytest.raises(GpuDownloadError): download_gpu_document(document, _config(), tmp_path)`.

**Regression protected**

- Protects the exact `corrupt download is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_Response`, `_config`, `_document`, `download_gpu_document`, `list`, `monkeypatch.setattr`, `pytest.raises`, `tmp_path.glob`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_tampered_sidecar_invalidates_cache`

**Signature**

```python
def test_tampered_sidecar_invalidates_cache(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

**Purpose**

Protects the `tampered sidecar invalidates cache` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 4 explicit setup/context statement(s).
- Computes `first` from `_download(tmp_path, monkeypatch)`.
- Computes `sidecar_path` from `tmp_path / f'{first.filename}.metadata.json'`.
- Computes `sidecar` from `json.loads(sidecar_path.read_text())`.
- Computes `sidecar['sha256']` from `'0' * 64`.

**Action**

- Calls `_Response`, `_config`, `_download`, `_zip_bytes`, `download_gpu_document`, `json.dumps`, `json.loads`, `monkeypatch.setattr`, `sidecar_path.read_text`, `sidecar_path.write_text`.

**Expected result**

- Direct assertions: `assert not download_gpu_document(first.document, _config(), tmp_path).cache_hit`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `tampered sidecar invalidates cache` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_Response`, `_config`, `_download`, `_zip_bytes`, `download_gpu_document`, `json.dumps`, `json.loads`, `monkeypatch.setattr`, `sidecar_path.read_text`, `sidecar_path.write_text`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_archive_path_traversal_is_rejected`

**Signature**

```python
def test_archive_path_traversal_is_rejected(tmp_path: Path) -> None:
```

**Purpose**

Protects the `archive path traversal is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `path` from `tmp_path / 'unsafe.zip'`.
- Enters managed context(s) `pytest.raises(GpuArchiveError, match='Unsafe')` and executes: Calls `validate_gpu_archive(path)` for its validation or side effect.

**Action**

- Calls `_zip_bytes`, `path.write_bytes`, `validate_gpu_archive`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GpuArchiveError, match='Unsafe'): validate_gpu_archive(path)`.

**Regression protected**

- Protects the exact `archive path traversal is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_zip_bytes`, `path.write_bytes`, `pytest.raises`, `validate_gpu_archive`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_archive_symlink_is_rejected`

**Signature**

```python
def test_archive_symlink_is_rejected(tmp_path: Path) -> None:
```

**Purpose**

Protects the `archive symlink is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 3 explicit setup/context statement(s).
- Computes `path` from `tmp_path / 'unsafe.zip'`.
- Enters managed context(s) `zipfile.ZipFile(path, 'w')` and executes: Computes `entry` from `zipfile.ZipInfo('link')`. Computes `entry.create_system` from `3`. Computes `entry.external_attr` from `41471 << 16 | 40960`. Calls `archive.writestr(entry, 'target')` for its validation or side effect.
- Enters managed context(s) `pytest.raises(GpuArchiveError, match='Symbolic')` and executes: Calls `validate_gpu_archive(path)` for its validation or side effect.

**Action**

- Calls `archive.writestr`, `validate_gpu_archive`, `zipfile.ZipFile`, `zipfile.ZipInfo`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GpuArchiveError, match='Symbolic'): validate_gpu_archive(path)`.

**Regression protected**

- Protects the exact `archive symlink is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `archive.writestr`, `pytest.raises`, `validate_gpu_archive`, `zipfile.ZipFile`, `zipfile.ZipInfo`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_zip_extraction_targets_are_rejected`

**Signature**

```python
def test_duplicate_zip_extraction_targets_are_rejected(
    tmp_path: Path,
    members: list[tuple[str, bytes]],
) -> None:
```

**Purpose**

Protects the `duplicate zip extraction targets are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `members`.
- Contains 2 explicit setup/context statement(s).
- Computes `path` from `tmp_path / 'collision.zip'`.
- Enters managed context(s) `pytest.raises(GpuArchiveError, match='(?i)duplicate|collid')` and executes: Calls `validate_gpu_archive(path)` for its validation or side effect.

**Action**

- Calls `_zip_member_bytes`, `path.write_bytes`, `validate_gpu_archive`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GpuArchiveError, match='(?i)duplicate|collid'): validate_gpu_archive(path)`.

**Regression protected**

- Protects the exact `duplicate zip extraction targets are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_zip_member_bytes`, `path.write_bytes`, `pytest.mark.parametrize`, `pytest.raises`, `validate_gpu_archive`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_zip_file_directory_target_collision_is_rejected`

**Signature**

```python
def test_zip_file_directory_target_collision_is_rejected(tmp_path: Path) -> None:
```

**Purpose**

Protects the `zip file directory target collision is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `path` from `tmp_path / 'collision.zip'`.
- Enters managed context(s) `pytest.raises(GpuArchiveError, match='collision|target')` and executes: Calls `validate_gpu_archive(path)` for its validation or side effect.

**Action**

- Calls `_zip_member_bytes`, `path.write_bytes`, `validate_gpu_archive`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GpuArchiveError, match='collision|target'): validate_gpu_archive(path)`.

**Regression protected**

- Protects the exact `zip file directory target collision is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_zip_member_bytes`, `path.write_bytes`, `pytest.raises`, `validate_gpu_archive`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_zip_cannot_claim_extraction_manifest_path`

**Signature**

```python
def test_zip_cannot_claim_extraction_manifest_path(tmp_path: Path) -> None:
```

**Purpose**

Protects the `zip cannot claim extraction manifest path` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `path` from `tmp_path / 'collision.zip'`.
- Enters managed context(s) `pytest.raises(GpuArchiveError, match='manifest')` and executes: Calls `validate_gpu_archive(path)` for its validation or side effect.

**Action**

- Calls `_zip_bytes`, `path.write_bytes`, `validate_gpu_archive`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GpuArchiveError, match='manifest'): validate_gpu_archive(path)`.

**Regression protected**

- Protects the exact `zip cannot claim extraction manifest path` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_zip_bytes`, `path.write_bytes`, `pytest.raises`, `validate_gpu_archive`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_extraction_inventory_and_cache`

**Signature**

```python
def test_extraction_inventory_and_cache(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

**Purpose**

Protects the `extraction inventory and cache` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 3 explicit setup/context statement(s).
- Computes `first` from `_download(tmp_path / 'cache', monkeypatch, _zip_bytes({'data/a.txt': b'x', 'docs/reglement.pdf': b'pdf'}))`.
- Computes `extracted` from `extract_gpu_document(first, tmp_path / 'cache')`.
- Computes `manifest` from `json.loads((extracted.extraction_root / gpu.EXTRACTION_MANIFEST_NAME).read_text(encoding='utf-8'))`.

**Action**

- Calls `(extracted.extraction_root / gpu.EXTRACTION_MANIFEST_NAME).read_text`, `(tmp_path / 'cache' / 'x').glob`, `_download`, `_zip_bytes`, `extract_gpu_document`, `json.loads`.

**Expected result**

- Direct assertions: `assert [item.relative_path for item in extracted.files] == ['data/a.txt', 'docs/reglement.pdf']`; `assert {item.category for item in extracted.files} == {'METADATA', 'WRITTEN_REGULATION'}`; `assert extract_gpu_document(first, tmp_path / 'cache').cache_hit`; `assert manifest['schema_version'] == 2`; `assert manifest['archive_sha256'] == first.sha256`; `assert manifest['files'] == [{'relative_path': item.relative_path, 'size_bytes': item.size_bytes, 'sha256': item.sha256} for item in extracted.files]`; `assert not list((tmp_path / 'cache' / 'x').glob('*.part'))`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `extraction inventory and cache` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `(extracted.extraction_root / gpu.EXTRACTION_MANIFEST_NAME).read_text`, `(tmp_path / 'cache' / 'x').glob`, `_download`, `_zip_bytes`, `extract_gpu_document`, `json.loads`, `list`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_stale_download_object_rejects_replaced_valid_archive`

**Signature**

```python
def test_stale_download_object_rejects_replaced_valid_archive(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `stale download object rejects replaced valid archive` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 3 explicit setup/context statement(s).
- Computes `download` from `_download(tmp_path / 'cache', monkeypatch, _zip_bytes({'data/value.txt': b'A'}))`.
- Computes `replacement` from `_zip_bytes({'data/value.txt': b'B'})`.
- Enters managed context(s) `pytest.raises(GpuArchiveError, match='checksum|SHA|stale|metadata')` and executes: Calls `extract_gpu_document(download, tmp_path / 'cache')` for its validation or side effect.

**Action**

- Calls `(tmp_path / 'cache' / 'x' / download.sha256[:16]).exists`, `_download`, `_zip_bytes`, `download.path.write_bytes`, `extract_gpu_document`.

**Expected result**

- Direct assertions: `assert len(replacement) == download.file_size`; `assert not (tmp_path / 'cache' / 'x' / download.sha256[:16]).exists()`.
- Expected exception contexts: `with pytest.raises(GpuArchiveError, match='checksum|SHA|stale|metadata'): extract_gpu_document(download, tmp_path / 'cache')`.

**Regression protected**

- Protects the exact `stale download object rejects replaced valid archive` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `(tmp_path / 'cache' / 'x' / download.sha256[:16]).exists`, `_download`, `_zip_bytes`, `download.path.write_bytes`, `extract_gpu_document`, `len`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_extraction_rejects_archive_object_inconsistent_with_path`

**Signature**

```python
def test_extraction_rejects_archive_object_inconsistent_with_path(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    value: object,
) -> None:
```

**Purpose**

Protects the `extraction rejects archive object inconsistent with path` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`, `field`, `value`.
- Contains 3 explicit setup/context statement(s).
- Computes `download` from `_download(tmp_path / 'cache', monkeypatch)`.
- Computes `stale` from `replace(download, **{field: value})`.
- Enters managed context(s) `pytest.raises(GpuArchiveError, match='archive|metadata|checksum|size')` and executes: Calls `extract_gpu_document(stale, tmp_path / 'cache')` for its validation or side effect.

**Action**

- Calls `_download`, `extract_gpu_document`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GpuArchiveError, match='archive|metadata|checksum|size'): extract_gpu_document(stale, tmp_path / 'cache')`.

**Regression protected**

- Protects the exact `extraction rejects archive object inconsistent with path` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_download`, `extract_gpu_document`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_tampered_extraction_is_rebuilt_from_verified_archive`

**Signature**

```python
def test_tampered_extraction_is_rebuilt_from_verified_archive(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation: str,
) -> None:
```

**Purpose**

Protects the `tampered extraction is rebuilt from verified archive` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`, `mutation`.
- Contains 4 explicit setup/context statement(s).
- Computes `download` from `_download(tmp_path / 'cache', monkeypatch, _zip_bytes({'data/value.txt': b'source', 'docs/reglement.pdf': b'pdf'}))`.
- Computes `first` from `extract_gpu_document(download, tmp_path / 'cache')`.
- Computes `original` from `first.extraction_root / 'data' / 'value.txt'`.
- Computes `refreshed` from `extract_gpu_document(download, tmp_path / 'cache')`.

**Action**

- Calls `(first.extraction_root / 'unexpected.txt').write_bytes`, `(refreshed.extraction_root / 'data' / 'renamed.txt').exists`, `(refreshed.extraction_root / 'data' / 'value.txt').read_bytes`, `(refreshed.extraction_root / 'unexpected.txt').exists`, `_download`, `_zip_bytes`, `extract_gpu_document`, `original.rename`, `original.unlink`, `original.with_name`, `original.write_bytes`.

**Expected result**

- Direct assertions: `assert not refreshed.cache_hit`; `assert (refreshed.extraction_root / 'data' / 'value.txt').read_bytes() == b'source'`; `assert not (refreshed.extraction_root / 'data' / 'renamed.txt').exists()`; `assert not (refreshed.extraction_root / 'unexpected.txt').exists()`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `tampered extraction is rebuilt from verified archive` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `(first.extraction_root / 'unexpected.txt').write_bytes`, `(refreshed.extraction_root / 'data' / 'renamed.txt').exists`, `(refreshed.extraction_root / 'data' / 'value.txt').read_bytes`, `(refreshed.extraction_root / 'unexpected.txt').exists`, `_download`, `_zip_bytes`, `extract_gpu_document`, `original.rename`, `original.unlink`, `original.with_name`, `original.write_bytes`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_spatial_inventory_and_inspection_preserve_source_quality`

**Signature**

```python
def test_spatial_inventory_and_inspection_preserve_source_quality(tmp_path: Path) -> None:
```

**Purpose**

Protects the `spatial inventory and inspection preserve source quality` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 3 explicit setup/context statement(s).
- Computes `extraction` from `_extraction_from_archive(_planning_archive(tmp_path), tmp_path)`.
- Computes `references` from `discover_gpu_spatial_layers(extraction)`.
- Computes `result` from `inspect_gpu_planning_document(extraction, _config())`.

**Action**

- Calls `_config`, `_extraction_from_archive`, `_planning_archive`, `discover_gpu_spatial_layers`, `inspect_gpu_planning_document`, `sorted`.

**Expected result**

- Direct assertions: `assert [item.source_layer for item in references] == ['prescription_surf', 'zone_urba']`; `assert result.zoning.reference.source_layer == 'zone_urba'`; `assert result.zoning.summary.crs == 'EPSG:2154'`; `assert result.zoning.summary.feature_count == 3`; `assert result.zoning.summary.null_geometry_count == 1`; `assert result.zoning.summary.invalid_geometry_count == 1`; `assert not result.zoning.data.geometry.iloc[1].is_valid`; `assert result.related_layers[0].logical_name == 'prescription_surface'`; `assert extraction.standard_models == ('CNIG PLU v2017',)`; `assert [item.relative_path for item in extraction.files] == sorted((item.relative_path for item in extraction.files))`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `spatial inventory and inspection preserve source quality` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_extraction_from_archive`, `_planning_archive`, `discover_gpu_spatial_layers`, `inspect_gpu_planning_document`, `sorted`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_zoning_layer_fails_clearly`

**Signature**

```python
def test_missing_zoning_layer_fails_clearly(tmp_path: Path) -> None:
```

**Purpose**

Protects the `missing zoning layer fails clearly` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 5 explicit setup/context statement(s).
- Computes `source` from `_planning_archive(tmp_path)`.
- Computes `extraction` from `_extraction_from_archive(source, tmp_path)`.
- Computes `payload` from `_config().model_dump(mode='json')`.
- Computes `payload['spatial_layers']['zoning']['match_tokens']` from `['missing']`.
- Enters managed context(s) `pytest.raises(GpuSpatialInspectionError, match='zoning')` and executes: Calls `inspect_gpu_planning_document(extraction, GpuSourceConfig.model_validate(payload))` for its validation or side effect.

**Action**

- Calls `GpuSourceConfig.model_validate`, `_config`, `_config().model_dump`, `_extraction_from_archive`, `_planning_archive`, `inspect_gpu_planning_document`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GpuSpatialInspectionError, match='zoning'): inspect_gpu_planning_document(extraction, GpuSourceConfig.model_validate(payload))`.

**Regression protected**

- Protects the exact `missing zoning layer fails clearly` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `GpuSourceConfig.model_validate`, `_config`, `_config().model_dump`, `_extraction_from_archive`, `_planning_archive`, `inspect_gpu_planning_document`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_ambiguous_zoning_layer_fails_clearly`

**Signature**

```python
def test_ambiguous_zoning_layer_fails_clearly(tmp_path: Path) -> None:
```

**Purpose**

Protects the `ambiguous zoning layer fails clearly` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 4 explicit setup/context statement(s).
- Computes `extraction` from `_extraction_from_archive(_planning_archive(tmp_path), tmp_path)`.
- Computes `payload` from `_config().model_dump(mode='json')`.
- Computes `payload['spatial_layers']['zoning']['match_tokens']` from `['zone_urba', 'prescription_surf']`.
- Enters managed context(s) `pytest.raises(GpuSpatialInspectionError, match='found 2')` and executes: Calls `inspect_gpu_planning_document(extraction, GpuSourceConfig.model_validate(payload))` for its validation or side effect.

**Action**

- Calls `GpuSourceConfig.model_validate`, `_config`, `_config().model_dump`, `_extraction_from_archive`, `_planning_archive`, `inspect_gpu_planning_document`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GpuSpatialInspectionError, match='found 2'): inspect_gpu_planning_document(extraction, GpuSourceConfig.model_validate(payload))`.

**Regression protected**

- Protects the exact `ambiguous zoning layer fails clearly` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `GpuSourceConfig.model_validate`, `_config`, `_config().model_dump`, `_extraction_from_archive`, `_planning_archive`, `inspect_gpu_planning_document`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_cached_document_lineage_change_forces_refresh`

**Signature**

```python
def test_cached_document_lineage_change_forces_refresh(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

**Purpose**

Protects the `cached document lineage change forces refresh` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 2 explicit setup/context statement(s).
- Computes `first` from `_download(tmp_path, monkeypatch)`.
- Computes `changed` from `replace(first.document, document_id='doc-2', written_files=tuple((replace(item, source_url=item.source_url.replace('/doc-1/', '/doc-2/') if item.source_url is not None else None) for item in first.document.written_files)))`.

**Action**

- Calls `_Response`, `_config`, `_download`, `_zip_bytes`, `download_gpu_document`, `item.source_url.replace`, `monkeypatch.setattr`, `replace`.

**Expected result**

- Direct assertions: `assert not download_gpu_document(changed, _config(), tmp_path).cache_hit`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `cached document lineage change forces refresh` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_Response`, `_config`, `_download`, `_zip_bytes`, `download_gpu_document`, `item.source_url.replace`, `monkeypatch.setattr`, `replace`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `LIBELLE` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `TYPEPSC` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `TYPEZONE` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `document` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `document_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `download_timestamp` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `files` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `match_tokens` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `schema_version` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `sha256` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `spatial_layers` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `unexpected` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `zoning` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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

This file contributes to LandScout's `test` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.

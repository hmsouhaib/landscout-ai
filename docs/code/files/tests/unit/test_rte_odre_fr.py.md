# `tests/unit/test_rte_odre_fr.py`

## File identity

- Repository path: `tests/unit/test_rte_odre_fr.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `rte_odre_fr` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `f437738409f25094f06ca20da5b68afc673ce5b4efb3e8879c1a0b1956700263`

## 1. Purpose

Provides complete unit and regression coverage for the `rte_odre_fr` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `import io` — required by the implementation paths and symbols documented below.
- `import json` — required by the implementation paths and symbols documented below.
- `from datetime import UTC, datetime, timedelta` — required by the implementation paths and symbols documented below.
- `from hashlib import sha256` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.
- `from urllib.error import HTTPError` — required by the implementation paths and symbols documented below.

### Third-party

- `from unittest.mock import patch` — required by the implementation paths and symbols documented below.
- `import pytest` — required by the implementation paths and symbols documented below.
- `import yaml` — required by the implementation paths and symbols documented below.
- `from pydantic import HttpUrl, ValidationError` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.sources import rte_odre_fr` — required by the implementation paths and symbols documented below.
- `from landscout.sources.rte_odre_fr import ( RteOdreDownloadError, RteOdreExportSummary, RteOdreSourceConfig, build_rte_odre_export_url, build_rte_odre_metadata_url, download_rte_odre_dataset, fetch_rte_odre_dataset_metadata, load_rte_odre_source_config, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `PROJECT_ROOT` | `Path(__file__).parents[2]` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `CONFIG_PATH` | `PROJECT_ROOT / "configs/sources/rte_odre_fr.yaml"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `BASE_URL` | `"https://odre.opendatasoft.com/api/explore/v2.1"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `DATASET_IDS` | `{ "sites": "postes-electriques-rte", "overhead_lines": "lignes-aeriennes-rte-nv", "underground_lines": "lignes-souterraines-rte-nv", }` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `_config_data`

**Signature**

```python
def _config_data() -> dict:
```

**Purpose**

Implements config data according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `dict`. Observed return expression(s): `yaml.safe_load(stream)`.

**Algorithm**

1. Enters managed context(s) `CONFIG_PATH.open(encoding='utf-8')` and executes: Returns `yaml.safe_load(stream)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `CONFIG_PATH.open`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `CONFIG_PATH.open`, `yaml.safe_load`.

**Known repository callers**

- `tests/unit/test_rte_odre_fr.py` — `test_api_base_is_pinned_to_the_official_https_origin_and_path`
- `tests/unit/test_rte_odre_fr.py` — `test_empty_base_url_fails`
- `tests/unit/test_rte_odre_fr.py` — `test_export_url_uses_configured_dataset_id`
- `tests/unit/test_rte_odre_fr.py` — `test_missing_dataset_id_fails`
- `tests/unit/test_rte_odre_fr.py` — `test_negative_cache_age_fails`
- `tests/unit/test_rte_odre_fr.py` — `test_unsupported_export_format_fails`

**Tests**

- `tests/unit/test_rte_odre_fr.py::test_api_base_is_pinned_to_the_official_https_origin_and_path`
- `tests/unit/test_rte_odre_fr.py::test_empty_base_url_fails`
- `tests/unit/test_rte_odre_fr.py::test_export_url_uses_configured_dataset_id`
- `tests/unit/test_rte_odre_fr.py::test_missing_dataset_id_fails`
- `tests/unit/test_rte_odre_fr.py::test_negative_cache_age_fails`
- `tests/unit/test_rte_odre_fr.py::test_unsupported_export_format_fails`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_metadata_content`

**Signature**

```python
def _metadata_content(dataset_id: str, records_count: int | None = 2) -> bytes:
```

**Purpose**

Implements metadata content according to the exact implementation and guards in this file.

**Inputs**

- `dataset_id` (`str`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `records_count` (`int | None`; optional/default `2`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bytes`. Observed return expression(s): `json.dumps(payload, ensure_ascii=False).encode('utf-8')`.

**Algorithm**

1. Computes `payload` from `{'dataset_id': dataset_id, 'metas': {'default': {'title': 'Official RTE dataset', 'publisher': 'RTE', 'modified': '2026-06-16T12:00:00+00:00', 'data_processed': '2026-06-16T12:01:00+00:00', 'metadata_processed': '2026-06-16T12:01:01+00:00', 'license': 'Licence Ouverte v2.0 (Etalab)', 'records_count': records_count, 'd…`.
2. Returns `json.dumps(payload, ensure_ascii=False).encode('utf-8')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `json.dumps`, `json.dumps(payload, ensure_ascii=False).encode`.

**Known repository callers**

- `tests/unit/test_rte_odre_fr.py` — `test_cached_export_summary_mismatch_invalidates_cache`
- `tests/unit/test_rte_odre_fr.py` — `test_corrupted_cached_export_triggers_refresh`
- `tests/unit/test_rte_odre_fr.py` — `test_corrupted_refresh_preserves_previous_valid_cache`
- `tests/unit/test_rte_odre_fr.py` — `test_double_failure_preserves_recovery_and_next_run_uses_zero_network.response_for_url`
- `tests/unit/test_rte_odre_fr.py` — `test_double_failure_preserves_recovery_and_next_run_uses_zero_network`
- `tests/unit/test_rte_odre_fr.py` — `test_expired_cache_is_refreshed`
- `tests/unit/test_rte_odre_fr.py` — `test_failed_refresh_preserves_previous_valid_cache`
- `tests/unit/test_rte_odre_fr.py` — `test_fresh_cache_is_reused`
- `tests/unit/test_rte_odre_fr.py` — `test_http_failure_raises_and_cleans_temporary_files`
- `tests/unit/test_rte_odre_fr.py` — `test_invalid_cached_record_count_invalidates_cache`
- `tests/unit/test_rte_odre_fr.py` — `test_invalid_geojson_download_is_rejected`
- `tests/unit/test_rte_odre_fr.py` — `test_lineage_sidecar_records_integrity`
- `tests/unit/test_rte_odre_fr.py` — `test_metadata_export_record_count_mismatch_is_rejected`
- `tests/unit/test_rte_odre_fr.py` — `test_metadata_is_captured_without_fabrication`
- `tests/unit/test_rte_odre_fr.py` — `test_metadata_publication_failure_restores_previous_pair`
- `tests/unit/test_rte_odre_fr.py` — `test_negative_source_record_count_is_rejected`
- `tests/unit/test_rte_odre_fr.py` — `test_null_feature_geometries_are_accepted`
- `tests/unit/test_rte_odre_fr.py` — `test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error.response_for_url`
- `tests/unit/test_rte_odre_fr.py` — `test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_rte_odre_fr.py` — `test_successful_download`
- `tests/unit/test_rte_odre_fr.py` — `test_temporary_link_or_junction_cannot_modify_target_before_rte_network.record_network`
- `tests/unit/test_rte_odre_fr.py` — `test_temporary_link_or_junction_cannot_modify_target_before_rte_network`
- `tests/unit/test_rte_odre_fr.py` — `test_unavailable_metadata_record_count_is_accepted`

**Tests**

- `tests/unit/test_rte_odre_fr.py::test_cached_export_summary_mismatch_invalidates_cache`
- `tests/unit/test_rte_odre_fr.py::test_corrupted_cached_export_triggers_refresh`
- `tests/unit/test_rte_odre_fr.py::test_corrupted_refresh_preserves_previous_valid_cache`
- `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network`
- `tests/unit/test_rte_odre_fr.py::test_expired_cache_is_refreshed`
- `tests/unit/test_rte_odre_fr.py::test_failed_refresh_preserves_previous_valid_cache`
- `tests/unit/test_rte_odre_fr.py::test_fresh_cache_is_reused`
- `tests/unit/test_rte_odre_fr.py::test_http_failure_raises_and_cleans_temporary_files`
- `tests/unit/test_rte_odre_fr.py::test_invalid_cached_record_count_invalidates_cache`
- `tests/unit/test_rte_odre_fr.py::test_invalid_geojson_download_is_rejected`
- `tests/unit/test_rte_odre_fr.py::test_lineage_sidecar_records_integrity`
- `tests/unit/test_rte_odre_fr.py::test_metadata_export_record_count_mismatch_is_rejected`
- `tests/unit/test_rte_odre_fr.py::test_metadata_is_captured_without_fabrication`
- `tests/unit/test_rte_odre_fr.py::test_metadata_publication_failure_restores_previous_pair`
- `tests/unit/test_rte_odre_fr.py::test_negative_source_record_count_is_rejected`
- `tests/unit/test_rte_odre_fr.py::test_null_feature_geometries_are_accepted`
- `tests/unit/test_rte_odre_fr.py::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_rte_odre_fr.py::test_successful_download`
- `tests/unit/test_rte_odre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_rte_network`
- `tests/unit/test_rte_odre_fr.py::test_unavailable_metadata_record_count_is_accepted`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_feature_collection`

**Signature**

```python
def _feature_collection(*, all_null_geometry: bool = False) -> bytes:
```

**Purpose**

Implements feature collection according to the exact implementation and guards in this file.

**Inputs**

- `all_null_geometry` (`bool`; optional/default `False`) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bytes`. Observed return expression(s): `json.dumps(payload).encode('utf-8')`.

**Algorithm**

1. Computes `geometry` from `None if all_null_geometry else {'type': 'Point', 'coordinates': [1, 2]}`.
2. Computes `payload` from `{'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'properties': {'code': 'A'}, 'geometry': geometry}, {'type': 'Feature', 'properties': {'code': 'B'}, 'geometry': None}]}`.
3. Returns `json.dumps(payload).encode('utf-8')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `json.dumps`, `json.dumps(payload).encode`.

**Known repository callers**

- `tests/unit/test_rte_odre_fr.py` — `test_cached_export_summary_mismatch_invalidates_cache`
- `tests/unit/test_rte_odre_fr.py` — `test_corrupted_cached_export_triggers_refresh`
- `tests/unit/test_rte_odre_fr.py` — `test_corrupted_refresh_preserves_previous_valid_cache`
- `tests/unit/test_rte_odre_fr.py` — `test_double_failure_preserves_recovery_and_next_run_uses_zero_network.response_for_url`
- `tests/unit/test_rte_odre_fr.py` — `test_double_failure_preserves_recovery_and_next_run_uses_zero_network`
- `tests/unit/test_rte_odre_fr.py` — `test_expired_cache_is_refreshed`
- `tests/unit/test_rte_odre_fr.py` — `test_failed_refresh_preserves_previous_valid_cache`
- `tests/unit/test_rte_odre_fr.py` — `test_fresh_cache_is_reused`
- `tests/unit/test_rte_odre_fr.py` — `test_invalid_cached_record_count_invalidates_cache`
- `tests/unit/test_rte_odre_fr.py` — `test_lineage_sidecar_records_integrity`
- `tests/unit/test_rte_odre_fr.py` — `test_metadata_export_record_count_mismatch_is_rejected`
- `tests/unit/test_rte_odre_fr.py` — `test_metadata_publication_failure_restores_previous_pair`
- `tests/unit/test_rte_odre_fr.py` — `test_null_feature_geometries_are_accepted`
- `tests/unit/test_rte_odre_fr.py` — `test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error.response_for_url`
- `tests/unit/test_rte_odre_fr.py` — `test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_rte_odre_fr.py` — `test_successful_download`
- `tests/unit/test_rte_odre_fr.py` — `test_temporary_link_or_junction_cannot_modify_target_before_rte_network.record_network`
- `tests/unit/test_rte_odre_fr.py` — `test_temporary_link_or_junction_cannot_modify_target_before_rte_network`
- `tests/unit/test_rte_odre_fr.py` — `test_unavailable_metadata_record_count_is_accepted`

**Tests**

- `tests/unit/test_rte_odre_fr.py::test_cached_export_summary_mismatch_invalidates_cache`
- `tests/unit/test_rte_odre_fr.py::test_corrupted_cached_export_triggers_refresh`
- `tests/unit/test_rte_odre_fr.py::test_corrupted_refresh_preserves_previous_valid_cache`
- `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network`
- `tests/unit/test_rte_odre_fr.py::test_expired_cache_is_refreshed`
- `tests/unit/test_rte_odre_fr.py::test_failed_refresh_preserves_previous_valid_cache`
- `tests/unit/test_rte_odre_fr.py::test_fresh_cache_is_reused`
- `tests/unit/test_rte_odre_fr.py::test_invalid_cached_record_count_invalidates_cache`
- `tests/unit/test_rte_odre_fr.py::test_lineage_sidecar_records_integrity`
- `tests/unit/test_rte_odre_fr.py::test_metadata_export_record_count_mismatch_is_rejected`
- `tests/unit/test_rte_odre_fr.py::test_metadata_publication_failure_restores_previous_pair`
- `tests/unit/test_rte_odre_fr.py::test_null_feature_geometries_are_accepted`
- `tests/unit/test_rte_odre_fr.py::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_rte_odre_fr.py::test_successful_download`
- `tests/unit/test_rte_odre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_rte_network`
- `tests/unit/test_rte_odre_fr.py::test_unavailable_metadata_record_count_is_accepted`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_response`

**Signature**

```python
def _response(content: bytes) -> io.BytesIO:
```

**Purpose**

Implements response according to the exact implementation and guards in this file.

**Inputs**

- `content` (`bytes`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `io.BytesIO`. Observed return expression(s): `io.BytesIO(content)`.

**Algorithm**

1. Returns `io.BytesIO(content)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `io.BytesIO`.

**Known repository callers**

- `tests/unit/test_rte_odre_fr.py` — `test_cached_export_summary_mismatch_invalidates_cache`
- `tests/unit/test_rte_odre_fr.py` — `test_corrupted_cached_export_triggers_refresh`
- `tests/unit/test_rte_odre_fr.py` — `test_corrupted_refresh_preserves_previous_valid_cache`
- `tests/unit/test_rte_odre_fr.py` — `test_double_failure_preserves_recovery_and_next_run_uses_zero_network.response_for_url`
- `tests/unit/test_rte_odre_fr.py` — `test_double_failure_preserves_recovery_and_next_run_uses_zero_network`
- `tests/unit/test_rte_odre_fr.py` — `test_expired_cache_is_refreshed`
- `tests/unit/test_rte_odre_fr.py` — `test_failed_refresh_preserves_previous_valid_cache`
- `tests/unit/test_rte_odre_fr.py` — `test_fresh_cache_is_reused`
- `tests/unit/test_rte_odre_fr.py` — `test_http_failure_raises_and_cleans_temporary_files`
- `tests/unit/test_rte_odre_fr.py` — `test_invalid_cached_record_count_invalidates_cache`
- `tests/unit/test_rte_odre_fr.py` — `test_invalid_geojson_download_is_rejected`
- `tests/unit/test_rte_odre_fr.py` — `test_lineage_sidecar_records_integrity`
- `tests/unit/test_rte_odre_fr.py` — `test_metadata_export_record_count_mismatch_is_rejected`
- `tests/unit/test_rte_odre_fr.py` — `test_metadata_is_captured_without_fabrication`
- `tests/unit/test_rte_odre_fr.py` — `test_metadata_publication_failure_restores_previous_pair`
- `tests/unit/test_rte_odre_fr.py` — `test_negative_source_record_count_is_rejected`
- `tests/unit/test_rte_odre_fr.py` — `test_null_feature_geometries_are_accepted`
- `tests/unit/test_rte_odre_fr.py` — `test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error.response_for_url`
- `tests/unit/test_rte_odre_fr.py` — `test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_rte_odre_fr.py` — `test_successful_download`
- `tests/unit/test_rte_odre_fr.py` — `test_temporary_link_or_junction_cannot_modify_target_before_rte_network.record_network`
- `tests/unit/test_rte_odre_fr.py` — `test_temporary_link_or_junction_cannot_modify_target_before_rte_network`
- `tests/unit/test_rte_odre_fr.py` — `test_unavailable_metadata_record_count_is_accepted`

**Tests**

- `tests/unit/test_rte_odre_fr.py::test_cached_export_summary_mismatch_invalidates_cache`
- `tests/unit/test_rte_odre_fr.py::test_corrupted_cached_export_triggers_refresh`
- `tests/unit/test_rte_odre_fr.py::test_corrupted_refresh_preserves_previous_valid_cache`
- `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network`
- `tests/unit/test_rte_odre_fr.py::test_expired_cache_is_refreshed`
- `tests/unit/test_rte_odre_fr.py::test_failed_refresh_preserves_previous_valid_cache`
- `tests/unit/test_rte_odre_fr.py::test_fresh_cache_is_reused`
- `tests/unit/test_rte_odre_fr.py::test_http_failure_raises_and_cleans_temporary_files`
- `tests/unit/test_rte_odre_fr.py::test_invalid_cached_record_count_invalidates_cache`
- `tests/unit/test_rte_odre_fr.py::test_invalid_geojson_download_is_rejected`
- `tests/unit/test_rte_odre_fr.py::test_lineage_sidecar_records_integrity`
- `tests/unit/test_rte_odre_fr.py::test_metadata_export_record_count_mismatch_is_rejected`
- `tests/unit/test_rte_odre_fr.py::test_metadata_is_captured_without_fabrication`
- `tests/unit/test_rte_odre_fr.py::test_metadata_publication_failure_restores_previous_pair`
- `tests/unit/test_rte_odre_fr.py::test_negative_source_record_count_is_rejected`
- `tests/unit/test_rte_odre_fr.py::test_null_feature_geometries_are_accepted`
- `tests/unit/test_rte_odre_fr.py::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_rte_odre_fr.py::test_successful_download`
- `tests/unit/test_rte_odre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_rte_network`
- `tests/unit/test_rte_odre_fr.py::test_unavailable_metadata_record_count_is_accepted`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_metadata_path`

**Signature**

```python
def _metadata_path(cache_dir: Path, dataset_id: str) -> Path:
```

**Purpose**

Implements metadata path according to the exact implementation and guards in this file.

**Inputs**

- `cache_dir` (`Path`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `dataset_id` (`str`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Path`. Observed return expression(s): `cache_dir / f'{dataset_id}.geojson.metadata.json'`.

**Algorithm**

1. Returns `cache_dir / f'{dataset_id}.geojson.metadata.json'`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

- `tests/unit/test_rte_odre_fr.py` — `test_cached_export_summary_mismatch_invalidates_cache`
- `tests/unit/test_rte_odre_fr.py` — `test_corrupted_refresh_preserves_previous_valid_cache`
- `tests/unit/test_rte_odre_fr.py` — `test_double_failure_preserves_recovery_and_next_run_uses_zero_network`
- `tests/unit/test_rte_odre_fr.py` — `test_expired_cache_is_refreshed`
- `tests/unit/test_rte_odre_fr.py` — `test_failed_refresh_preserves_previous_valid_cache`
- `tests/unit/test_rte_odre_fr.py` — `test_invalid_cached_record_count_invalidates_cache`
- `tests/unit/test_rte_odre_fr.py` — `test_lineage_sidecar_records_integrity`
- `tests/unit/test_rte_odre_fr.py` — `test_metadata_publication_failure_restores_previous_pair`
- `tests/unit/test_rte_odre_fr.py` — `test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_rte_odre_fr.py` — `test_temporary_link_or_junction_cannot_modify_target_before_rte_network`

**Tests**

- `tests/unit/test_rte_odre_fr.py::test_cached_export_summary_mismatch_invalidates_cache`
- `tests/unit/test_rte_odre_fr.py::test_corrupted_refresh_preserves_previous_valid_cache`
- `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network`
- `tests/unit/test_rte_odre_fr.py::test_expired_cache_is_refreshed`
- `tests/unit/test_rte_odre_fr.py::test_failed_refresh_preserves_previous_valid_cache`
- `tests/unit/test_rte_odre_fr.py::test_invalid_cached_record_count_invalidates_cache`
- `tests/unit/test_rte_odre_fr.py::test_lineage_sidecar_records_integrity`
- `tests/unit/test_rte_odre_fr.py::test_metadata_publication_failure_restores_previous_pair`
- `tests/unit/test_rte_odre_fr.py::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_rte_odre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_rte_network`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_expire_cache`

**Signature**

```python
def _expire_cache(metadata_path: Path) -> None:
```

**Purpose**

Implements expire cache according to the exact implementation and guards in this file.

**Inputs**

- `metadata_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `metadata` from `json.loads(metadata_path.read_text(encoding='utf-8'))`.
2. Computes `metadata['download_timestamp']` from `(datetime.now(UTC) - timedelta(hours=169)).isoformat()`.
3. Calls `metadata_path.write_text(json.dumps(metadata), encoding='utf-8')` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `metadata_path.read_text`, `metadata_path.write_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `(datetime.now(UTC) - timedelta(hours=169)).isoformat`, `datetime.now`, `json.dumps`, `json.loads`, `metadata_path.read_text`, `metadata_path.write_text`, `timedelta`.

**Known repository callers**

- `tests/unit/test_rte_odre_fr.py` — `test_corrupted_refresh_preserves_previous_valid_cache`
- `tests/unit/test_rte_odre_fr.py` — `test_double_failure_preserves_recovery_and_next_run_uses_zero_network`
- `tests/unit/test_rte_odre_fr.py` — `test_expired_cache_is_refreshed`
- `tests/unit/test_rte_odre_fr.py` — `test_failed_refresh_preserves_previous_valid_cache`
- `tests/unit/test_rte_odre_fr.py` — `test_metadata_publication_failure_restores_previous_pair`
- `tests/unit/test_rte_odre_fr.py` — `test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error`

**Tests**

- `tests/unit/test_rte_odre_fr.py::test_corrupted_refresh_preserves_previous_valid_cache`
- `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network`
- `tests/unit/test_rte_odre_fr.py::test_expired_cache_is_refreshed`
- `tests/unit/test_rte_odre_fr.py::test_failed_refresh_preserves_previous_valid_cache`
- `tests/unit/test_rte_odre_fr.py::test_metadata_publication_failure_restores_previous_pair`
- `tests/unit/test_rte_odre_fr.py::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `source_config`

**Signature**

```python
def source_config() -> RteOdreSourceConfig:
```

**Purpose**

Implements source config according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `RteOdreSourceConfig`. Observed return expression(s): `load_rte_odre_source_config(CONFIG_PATH)`.

**Algorithm**

1. Returns `load_rte_odre_source_config(CONFIG_PATH)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `load_rte_odre_source_config`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `load_rte_odre_source_config`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_mutated_loaded_api_origin_is_rejected_before_metadata_network.fail_network`

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
3. Raises `AssertionError('network used after ODRE origin mutation')`.

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

### `test_metadata_publication_failure_restores_previous_pair.fail_metadata_publication`

**Signature**

```python
def fail_metadata_publication(source: Path, target: Path) -> None:
```

**Purpose**

Implements fail metadata publication according to the exact implementation and guards in this file.

**Inputs**

- `source` (`Path`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `target` (`Path`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Executes `nonlocal failure_injected`.
2. Checks `source == temporary_metadata and target == metadata_path`. When true: Computes `failure_injected` from `True`. Raises `PermissionError('simulated persistent metadata file lock')`.
3. Calls `original_replace(source, target)` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `source == temporary_metadata and target == metadata_path` is true.

**Exceptions**

- Explicitly raises: `PermissionError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `original_replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `PermissionError`, `original_replace`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_double_failure_preserves_recovery_and_next_run_uses_zero_network.fail_publication_and_rollback`

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

1. Checks `source == temporary_metadata and target == metadata_path`. When true: Raises `OSError('publication failed')`.
2. Checks `source == archive_backup and target == first.path`. When true: Raises `OSError('rollback failed')`.
3. Calls `original_replace(source, target)` for its validation or side effect.

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

### `test_double_failure_preserves_recovery_and_next_run_uses_zero_network.response_for_url`

**Signature**

```python
def response_for_url(url: str, *args: object, **kwargs: object) -> io.BytesIO:
```

**Purpose**

Implements response for url according to the exact implementation and guards in this file.

**Inputs**

- `url` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `io.BytesIO`. Observed return expression(s): `_response(_metadata_content(dataset_id))`; `_response(_feature_collection())`.

**Algorithm**

1. Checks `url.endswith('/exports/geojson')`. When true: Returns `_response(_feature_collection())`.
2. Returns `_response(_metadata_content(dataset_id))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_feature_collection`, `_metadata_content`, `_response`, `url.endswith`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_double_failure_preserves_recovery_and_next_run_uses_zero_network.fail_network`

**Signature**

```python
def fail_network(url: str, *args: object, **kwargs: object) -> io.BytesIO:
```

**Purpose**

Implements fail network according to the exact implementation and guards in this file.

**Inputs**

- `url` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `io.BytesIO`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Calls `network_calls.append(url)` for its validation or side effect.
2. Raises `AssertionError('manual recovery state must fail before HTTP')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `AssertionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `AssertionError`, `network_calls.append`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_temporary_link_or_junction_cannot_modify_target_before_rte_network.simulated_is_symlink`

**Signature**

```python
def simulated_is_symlink(path: Path) -> bool:
```

**Purpose**

Implements simulated is symlink according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `link_kind == 'symlink' and path == unsafe_path or original_is_symlink(path)`.

**Algorithm**

1. Returns `link_kind == 'symlink' and path == unsafe_path or original_is_symlink(path)`.

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

### `test_temporary_link_or_junction_cannot_modify_target_before_rte_network.simulated_is_junction`

**Signature**

```python
def simulated_is_junction(path: Path) -> bool:
```

**Purpose**

Implements simulated is junction according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `link_kind == 'junction' and path == unsafe_path or original_is_junction(path)`.

**Algorithm**

1. Returns `link_kind == 'junction' and path == unsafe_path or original_is_junction(path)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `original_is_junction`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_temporary_link_or_junction_cannot_modify_target_before_rte_network.simulated_symlink_open`

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

1. Checks `path == unsafe_path`. When true: Returns `original_open(sentinel, *args, **kwargs)`.
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

### `test_temporary_link_or_junction_cannot_modify_target_before_rte_network.record_network`

**Signature**

```python
def record_network(url: str, *args: object, **kwargs: object) -> io.BytesIO:
```

**Purpose**

Implements record network according to the exact implementation and guards in this file.

**Inputs**

- `url` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `io.BytesIO`. Observed return expression(s): `_response(_metadata_content(dataset_id))`; `_response(_feature_collection())`.

**Algorithm**

1. Executes `nonlocal network_calls`.
2. Updates `network_calls` using `` and `1`.
3. Checks `url.endswith('/exports/geojson')`. When true: Returns `_response(_feature_collection())`.
4. Returns `_response(_metadata_content(dataset_id))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_feature_collection`, `_metadata_content`, `_response`, `url.endswith`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_broken_recovery_symlink_rejects_rte_before_network.simulated_is_symlink`

**Signature**

```python
def simulated_is_symlink(path: Path) -> bool:
```

**Purpose**

Implements simulated is symlink according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `path == recovery_path or original_is_symlink(path)`.

**Algorithm**

1. Returns `path == recovery_path or original_is_symlink(path)`.

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

### `test_broken_recovery_symlink_rejects_rte_before_network.fail_network`

**Signature**

```python
def fail_network(url: str, *args: object, **kwargs: object) -> io.BytesIO:
```

**Purpose**

Implements fail network according to the exact implementation and guards in this file.

**Inputs**

- `url` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `io.BytesIO`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Calls `network_calls.append(url)` for its validation or side effect.
2. Raises `AssertionError('broken recovery link must fail before HTTP')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `AssertionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `AssertionError`, `network_calls.append`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error.fail_publication_and_rollback`

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
2. Checks `source == temporary_metadata and target == metadata_path`. When true: Raises `OSError('publication failed')`.
3. Checks `source == archive_backup and target == first.path`. When true: Computes `rollback_failed` from `True`. Raises `OSError('rollback failed')`.
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

### `test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error.fail_temporary_cleanup`

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

1. Checks `rollback_failed and path == temporary_metadata`. When true: Raises `PermissionError('temporary cleanup failed')`.
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

### `test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error.response_for_url`

**Signature**

```python
def response_for_url(url: str, *args: object, **kwargs: object) -> io.BytesIO:
```

**Purpose**

Implements response for url according to the exact implementation and guards in this file.

**Inputs**

- `url` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `io.BytesIO`. Observed return expression(s): `_response(_metadata_content(dataset_id))`; `_response(_feature_collection())`.

**Algorithm**

1. Checks `url.endswith('/exports/geojson')`. When true: Returns `_response(_feature_collection())`.
2. Returns `_response(_metadata_content(dataset_id))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_feature_collection`, `_metadata_content`, `_response`, `url.endswith`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_source_config_loads`

**Signature**

```python
def test_valid_source_config_loads(source_config: RteOdreSourceConfig) -> None:
```

**Purpose**

Protects the `valid source config loads` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `source_config`.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls only local assertions/expressions.

**Expected result**

- Direct assertions: `assert source_config.provider == 'RTE'`; `assert source_config.portal == 'ODRE'`; `assert source_config.datasets.sites.dataset_id == 'postes-electriques-rte'`; `assert source_config.cache.max_age_hours == 168`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `valid source config loads` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- No calls.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_dataset_id_fails`

**Signature**

```python
def test_missing_dataset_id_fails() -> None:
```

**Purpose**

Protects the `missing dataset id fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `config_data` from `_config_data()`.
- Enters managed context(s) `pytest.raises(ValidationError)` and executes: Calls `RteOdreSourceConfig.model_validate(config_data)` for its validation or side effect.

**Action**

- Calls `RteOdreSourceConfig.model_validate`, `_config_data`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError): RteOdreSourceConfig.model_validate(config_data)`.

**Regression protected**

- Protects the exact `missing dataset id fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `RteOdreSourceConfig.model_validate`, `_config_data`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_empty_base_url_fails`

**Signature**

```python
def test_empty_base_url_fails() -> None:
```

**Purpose**

Protects the `empty base url fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `config_data` from `_config_data()`.
- Computes `config_data['api']['base_url']` from `''`.
- Enters managed context(s) `pytest.raises(ValidationError)` and executes: Calls `RteOdreSourceConfig.model_validate(config_data)` for its validation or side effect.

**Action**

- Calls `RteOdreSourceConfig.model_validate`, `_config_data`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError): RteOdreSourceConfig.model_validate(config_data)`.

**Regression protected**

- Protects the exact `empty base url fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `RteOdreSourceConfig.model_validate`, `_config_data`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_api_base_is_pinned_to_the_official_https_origin_and_path`

**Signature**

```python
def test_api_base_is_pinned_to_the_official_https_origin_and_path(
    base_url: str,
) -> None:
```

**Purpose**

Protects the `api base is pinned to the official https origin and path` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `base_url`.
- Contains 3 explicit setup/context statement(s).
- Computes `config_data` from `_config_data()`.
- Computes `config_data['api']['base_url']` from `base_url`.
- Enters managed context(s) `pytest.raises(ValidationError)` and executes: Calls `RteOdreSourceConfig.model_validate(config_data)` for its validation or side effect.

**Action**

- Calls `RteOdreSourceConfig.model_validate`, `_config_data`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError): RteOdreSourceConfig.model_validate(config_data)`.

**Regression protected**

- Protects the exact `api base is pinned to the official https origin and path` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `RteOdreSourceConfig.model_validate`, `_config_data`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_mutated_loaded_api_origin_is_rejected_before_metadata_network`

**Signature**

```python
def test_mutated_loaded_api_origin_is_rejected_before_metadata_network(
    source_config: RteOdreSourceConfig,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `mutated loaded api origin is rejected before metadata network` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `source_config`, `monkeypatch`.
- Contains 3 explicit setup/context statement(s).
- Computes `source_config.api.base_url` from `HttpUrl('https://unrelated.example/api/explore/v2.1')`.
- Computes `network_calls` from `0`.
- Enters managed context(s) `pytest.raises(RteOdreDownloadError, match='config|official|origin')` and executes: Calls `fetch_rte_odre_dataset_metadata(source_config, 'sites')` for its validation or side effect.

**Action**

- Calls `AssertionError`, `HttpUrl`, `fetch_rte_odre_dataset_metadata`, `monkeypatch.setattr`.

**Expected result**

- Direct assertions: `assert network_calls == 0`.
- Expected exception contexts: `with pytest.raises(RteOdreDownloadError, match='config|official|origin'): fetch_rte_odre_dataset_metadata(source_config, 'sites')`.

**Regression protected**

- Protects the exact `mutated loaded api origin is rejected before metadata network` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `AssertionError`, `HttpUrl`, `fetch_rte_odre_dataset_metadata`, `monkeypatch.setattr`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_negative_cache_age_fails`

**Signature**

```python
def test_negative_cache_age_fails() -> None:
```

**Purpose**

Protects the `negative cache age fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `config_data` from `_config_data()`.
- Computes `config_data['cache']['max_age_hours']` from `-1`.
- Enters managed context(s) `pytest.raises(ValidationError)` and executes: Calls `RteOdreSourceConfig.model_validate(config_data)` for its validation or side effect.

**Action**

- Calls `RteOdreSourceConfig.model_validate`, `_config_data`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError): RteOdreSourceConfig.model_validate(config_data)`.

**Regression protected**

- Protects the exact `negative cache age fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `RteOdreSourceConfig.model_validate`, `_config_data`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unsupported_export_format_fails`

**Signature**

```python
def test_unsupported_export_format_fails() -> None:
```

**Purpose**

Protects the `unsupported export format fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `config_data` from `_config_data()`.
- Computes `config_data['datasets']['sites']['preferred_format']` from `'csv'`.
- Enters managed context(s) `pytest.raises(ValidationError)` and executes: Calls `RteOdreSourceConfig.model_validate(config_data)` for its validation or side effect.

**Action**

- Calls `RteOdreSourceConfig.model_validate`, `_config_data`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError): RteOdreSourceConfig.model_validate(config_data)`.

**Regression protected**

- Protects the exact `unsupported export format fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `RteOdreSourceConfig.model_validate`, `_config_data`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_build_export_url`

**Signature**

```python
def test_build_export_url(
    source_config: RteOdreSourceConfig, logical_name: str, dataset_id: str
) -> None:
```

**Purpose**

Protects the `build export url` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `source_config`, `logical_name`, `dataset_id`.
- Contains 1 explicit setup/context statement(s).
- Computes `url` from `build_rte_odre_export_url(source_config, logical_name)`.

**Action**

- Calls `DATASET_IDS.items`, `build_rte_odre_export_url`.

**Expected result**

- Direct assertions: `assert url == f'{BASE_URL}/catalog/datasets/{dataset_id}/exports/geojson'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `build export url` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `DATASET_IDS.items`, `build_rte_odre_export_url`, `list`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_build_metadata_url`

**Signature**

```python
def test_build_metadata_url(source_config: RteOdreSourceConfig) -> None:
```

**Purpose**

Protects the `build metadata url` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `source_config`.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `build_rte_odre_metadata_url`.

**Expected result**

- Direct assertions: `assert build_rte_odre_metadata_url(source_config, 'sites') == f'{BASE_URL}/catalog/datasets/postes-electriques-rte'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `build metadata url` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `build_rte_odre_metadata_url`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_export_url_uses_configured_dataset_id`

**Signature**

```python
def test_export_url_uses_configured_dataset_id() -> None:
```

**Purpose**

Protects the `export url uses configured dataset id` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `config_data` from `_config_data()`.
- Computes `config_data['datasets']['sites']['dataset_id']` from `'configured-sites'`.
- Computes `config` from `RteOdreSourceConfig.model_validate(config_data)`.

**Action**

- Calls `RteOdreSourceConfig.model_validate`, `_config_data`, `build_rte_odre_export_url`, `build_rte_odre_export_url(config, 'sites').endswith`.

**Expected result**

- Direct assertions: `assert build_rte_odre_export_url(config, 'sites').endswith('/catalog/datasets/configured-sites/exports/geojson')`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `export url uses configured dataset id` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `RteOdreSourceConfig.model_validate`, `_config_data`, `build_rte_odre_export_url`, `build_rte_odre_export_url(config, 'sites').endswith`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_metadata_is_captured_without_fabrication`

**Signature**

```python
def test_metadata_is_captured_without_fabrication(
    source_config: RteOdreSourceConfig,
) -> None:
```

**Purpose**

Protects the `metadata is captured without fabrication` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `source_config`.
- Contains 2 explicit setup/context statement(s).
- Computes `content` from `_metadata_content(DATASET_IDS['sites'])`.
- Enters managed context(s) `patch('landscout.sources.rte_odre_fr.open_safe_https', return_value=_response(content))` and executes: Computes `metadata` from `fetch_rte_odre_dataset_metadata(source_config, 'sites')`.

**Action**

- Calls `_metadata_content`, `_response`, `fetch_rte_odre_dataset_metadata`.

**Expected result**

- Direct assertions: `assert metadata.title == 'Official RTE dataset'`; `assert metadata.publisher == 'RTE'`; `assert metadata.modified == '2026-06-16T12:00:00+00:00'`; `assert metadata.data_processed == '2026-06-16T12:01:00+00:00'`; `assert metadata.metadata_processed == '2026-06-16T12:01:01+00:00'`; `assert metadata.license == 'Licence Ouverte v2.0 (Etalab)'`; `assert metadata.records_count == 2`; `assert metadata.geometry_precision_status == 'GENERALIZED_OR_RESTRICTED'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `metadata is captured without fabrication` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_metadata_content`, `_response`, `fetch_rte_odre_dataset_metadata`, `patch`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_successful_download`

**Signature**

```python
def test_successful_download(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
```

**Purpose**

Protects the `successful download` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 3 explicit setup/context statement(s).
- Computes `dataset_id` from `DATASET_IDS['sites']`.
- Computes `export_content` from `_feature_collection()`.
- Enters managed context(s) `patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=[_response(_metadata_content(dataset_id)), _response(export_content)])` and executes: Computes `result` from `download_rte_odre_dataset('sites', source_config, tmp_path)`.

**Action**

- Calls `RteOdreExportSummary`, `_feature_collection`, `_metadata_content`, `_response`, `download_rte_odre_dataset`, `result.path.read_bytes`, `sha256`, `sha256(export_content).hexdigest`.

**Expected result**

- Direct assertions: `assert result.logical_name == 'sites'`; `assert result.dataset_id == dataset_id`; `assert result.provider == 'RTE'`; `assert result.portal == 'ODRE'`; `assert result.export_format == 'geojson'`; `assert result.path.read_bytes() == export_content`; `assert result.file_size == len(export_content)`; `assert result.sha256 == sha256(export_content).hexdigest()`; `assert result.cache_hit is False`; `assert result.dataset_metadata.title == 'Official RTE dataset'`; `assert result.dataset_metadata.records_count == result.export_summary.feature_count`; `assert result.export_summary == RteOdreExportSummary(feature_count=2, null_geometry_count=1, non_null_geometry_count=1, geometry_types=('Point',))`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `successful download` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `RteOdreExportSummary`, `_feature_collection`, `_metadata_content`, `_response`, `download_rte_odre_dataset`, `len`, `patch`, `result.path.read_bytes`, `sha256`, `sha256(export_content).hexdigest`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_metadata_export_record_count_mismatch_is_rejected`

**Signature**

```python
def test_metadata_export_record_count_mismatch_is_rejected(
    tmp_path: Path,
    source_config: RteOdreSourceConfig,
    records_count: int,
) -> None:
```

**Purpose**

Protects the `metadata export record count mismatch is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`, `records_count`.
- Contains 2 explicit setup/context statement(s).
- Computes `dataset_id` from `DATASET_IDS['sites']`.
- Enters managed context(s) `patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=[_response(_metadata_content(dataset_id, records_count)), _response(_feature_collection())]), pytest.raises(RteOdreDownloadError, match='records_count')` and executes: Calls `download_rte_odre_dataset('sites', source_config, tmp_path)` for its validation or side effect.

**Action**

- Calls `_feature_collection`, `_metadata_content`, `_response`, `download_rte_odre_dataset`, `tmp_path.glob`.

**Expected result**

- Direct assertions: `assert not list(tmp_path.glob('*.geojson'))`; `assert not list(tmp_path.glob('*.part'))`; `assert not list(tmp_path.glob('*.bak'))`.
- Expected exception contexts: `with patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=[_response(_metadata_content(dataset_id, records_count)), _response(_feature_collection())]), pytest.raises(RteOdreDownloadError, match='records_count'): download_rte_odre_dataset('sites', source_config, tmp_path)`.

**Regression protected**

- Protects the exact `metadata export record count mismatch is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_feature_collection`, `_metadata_content`, `_response`, `download_rte_odre_dataset`, `list`, `patch`, `pytest.mark.parametrize`, `pytest.raises`, `tmp_path.glob`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unavailable_metadata_record_count_is_accepted`

**Signature**

```python
def test_unavailable_metadata_record_count_is_accepted(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
```

**Purpose**

Protects the `unavailable metadata record count is accepted` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 2 explicit setup/context statement(s).
- Computes `dataset_id` from `DATASET_IDS['sites']`.
- Enters managed context(s) `patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=[_response(_metadata_content(dataset_id, records_count=None)), _response(_feature_collection())])` and executes: Computes `result` from `download_rte_odre_dataset('sites', source_config, tmp_path)`.

**Action**

- Calls `_feature_collection`, `_metadata_content`, `_response`, `download_rte_odre_dataset`.

**Expected result**

- Direct assertions: `assert result.dataset_metadata.records_count is None`; `assert result.export_summary.feature_count == 2`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `unavailable metadata record count is accepted` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_feature_collection`, `_metadata_content`, `_response`, `download_rte_odre_dataset`, `patch`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_negative_source_record_count_is_rejected`

**Signature**

```python
def test_negative_source_record_count_is_rejected(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
```

**Purpose**

Protects the `negative source record count is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 2 explicit setup/context statement(s).
- Computes `dataset_id` from `DATASET_IDS['sites']`.
- Enters managed context(s) `patch('landscout.sources.rte_odre_fr.open_safe_https', return_value=_response(_metadata_content(dataset_id, records_count=-1))), pytest.raises(RteOdreDownloadError, match='must not be negative')` and executes: Calls `download_rte_odre_dataset('sites', source_config, tmp_path)` for its validation or side effect.

**Action**

- Calls `_metadata_content`, `_response`, `download_rte_odre_dataset`, `tmp_path.glob`.

**Expected result**

- Direct assertions: `assert not list(tmp_path.glob('*.part'))`; `assert not list(tmp_path.glob('*.bak'))`.
- Expected exception contexts: `with patch('landscout.sources.rte_odre_fr.open_safe_https', return_value=_response(_metadata_content(dataset_id, records_count=-1))), pytest.raises(RteOdreDownloadError, match='must not be negative'): download_rte_odre_dataset('sites', source_config, tmp_path)`.

**Regression protected**

- Protects the exact `negative source record count is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_metadata_content`, `_response`, `download_rte_odre_dataset`, `list`, `patch`, `pytest.raises`, `tmp_path.glob`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_export_summary_rejects_invalid_geometry_counts`

**Signature**

```python
def test_export_summary_rejects_invalid_geometry_counts(
    feature_count: int,
    null_geometry_count: int,
    non_null_geometry_count: int,
) -> None:
```

**Purpose**

Protects the `export summary rejects invalid geometry counts` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `feature_count`, `null_geometry_count`, `non_null_geometry_count`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(ValueError)` and executes: Calls `RteOdreExportSummary(feature_count=feature_count, null_geometry_count=null_geometry_count, non_null_geometry_count=non_null_geometry_count, geometry_types=())` for its validation or side effect.

**Action**

- Calls `RteOdreExportSummary`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError): RteOdreExportSummary(feature_count=feature_count, null_geometry_count=null_geometry_count, non_null_geometry_count=non_null_geometry_count, geometry_types=())`.

**Regression protected**

- Protects the exact `export summary rejects invalid geometry counts` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `RteOdreExportSummary`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_fresh_cache_is_reused`

**Signature**

```python
def test_fresh_cache_is_reused(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
```

**Purpose**

Protects the `fresh cache is reused` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 2 explicit setup/context statement(s).
- Computes `dataset_id` from `DATASET_IDS['sites']`.
- Enters managed context(s) `patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=[_response(_metadata_content(dataset_id)), _response(_feature_collection())])` and executes: Computes `first` from `download_rte_odre_dataset('sites', source_config, tmp_path)`. Computes `second` from `download_rte_odre_dataset('sites', source_config, tmp_path)`.

**Action**

- Calls `_feature_collection`, `_metadata_content`, `_response`, `download_rte_odre_dataset`.

**Expected result**

- Direct assertions: `assert opener.call_count == 2`; `assert first.cache_hit is False`; `assert second.cache_hit is True`; `assert second.download_timestamp == first.download_timestamp`; `assert second.sha256 == first.sha256`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `fresh cache is reused` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_feature_collection`, `_metadata_content`, `_response`, `download_rte_odre_dataset`, `patch`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_expired_cache_is_refreshed`

**Signature**

```python
def test_expired_cache_is_refreshed(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
```

**Purpose**

Protects the `expired cache is refreshed` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 6 explicit setup/context statement(s).
- Computes `dataset_id` from `DATASET_IDS['sites']`.
- Computes `initial_content` from `_feature_collection()`.
- Computes `refreshed_payload` from `json.loads(initial_content)`.
- Computes `refreshed_content` from `json.dumps(refreshed_payload).encode('utf-8')`.
- Enters managed context(s) `patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=[_response(_metadata_content(dataset_id)), _response(initial_content)])` and executes: Computes `first` from `download_rte_odre_dataset('sites', source_config, tmp_path)`.
- Enters managed context(s) `patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=[_response(_metadata_content(dataset_id, records_count=3)), _response(refreshed_content)])` and executes: Computes `refreshed` from `download_rte_odre_dataset('sites', source_config, tmp_path)`.

**Action**

- Calls `_expire_cache`, `_feature_collection`, `_metadata_content`, `_metadata_path`, `_response`, `download_rte_odre_dataset`, `json.dumps`, `json.dumps(refreshed_payload).encode`, `json.loads`, `refreshed.path.read_bytes`, `refreshed_payload['features'].append`, `tmp_path.glob`.

**Expected result**

- Direct assertions: `assert opener.call_count == 2`; `assert refreshed.cache_hit is False`; `assert refreshed.path.read_bytes() == refreshed_content`; `assert refreshed.sha256 != first.sha256`; `assert refreshed.export_summary.feature_count == 3`; `assert not list(tmp_path.glob('*.bak'))`; `assert not list(tmp_path.glob('*.part'))`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `expired cache is refreshed` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_expire_cache`, `_feature_collection`, `_metadata_content`, `_metadata_path`, `_response`, `download_rte_odre_dataset`, `json.dumps`, `json.dumps(refreshed_payload).encode`, `json.loads`, `list`, `patch`, `refreshed.path.read_bytes`, `refreshed_payload['features'].append`, `tmp_path.glob`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_http_failure_raises_and_cleans_temporary_files`

**Signature**

```python
def test_http_failure_raises_and_cleans_temporary_files(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
```

**Purpose**

Protects the `http failure raises and cleans temporary files` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 4 explicit setup/context statement(s).
- Computes `dataset_id` from `DATASET_IDS['sites']`.
- Computes `source_url` from `build_rte_odre_export_url(source_config, 'sites')`.
- Computes `error` from `HTTPError(source_url, 503, 'Unavailable', hdrs=None, fp=None)`.
- Enters managed context(s) `patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=[_response(_metadata_content(dataset_id)), error]), pytest.raises(RteOdreDownloadError)` and executes: Calls `download_rte_odre_dataset('sites', source_config, tmp_path)` for its validation or side effect.

**Action**

- Calls `HTTPError`, `_metadata_content`, `_response`, `build_rte_odre_export_url`, `download_rte_odre_dataset`, `tmp_path.glob`.

**Expected result**

- Direct assertions: `assert not list(tmp_path.glob('*.part'))`; `assert not list(tmp_path.glob('*.geojson'))`.
- Expected exception contexts: `with patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=[_response(_metadata_content(dataset_id)), error]), pytest.raises(RteOdreDownloadError): download_rte_odre_dataset('sites', source_config, tmp_path)`.

**Regression protected**

- Protects the exact `http failure raises and cleans temporary files` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `HTTPError`, `_metadata_content`, `_response`, `build_rte_odre_export_url`, `download_rte_odre_dataset`, `list`, `patch`, `pytest.raises`, `tmp_path.glob`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_failed_refresh_preserves_previous_valid_cache`

**Signature**

```python
def test_failed_refresh_preserves_previous_valid_cache(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
```

**Purpose**

Protects the `failed refresh preserves previous valid cache` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 9 explicit setup/context statement(s).
- Computes `dataset_id` from `DATASET_IDS['sites']`.
- Enters managed context(s) `patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=[_response(_metadata_content(dataset_id)), _response(_feature_collection())])` and executes: Computes `first` from `download_rte_odre_dataset('sites', source_config, tmp_path)`.
- Computes `original_archive` from `first.path.read_bytes()`.
- Computes `metadata_path` from `_metadata_path(tmp_path, dataset_id)`.
- Computes `original_metadata` from `metadata_path.read_bytes()`.
- Computes `expired_metadata` from `metadata_path.read_bytes()`.
- Computes `metadata_url` from `build_rte_odre_metadata_url(source_config, 'sites')`.
- Computes `error` from `HTTPError(metadata_url, 503, 'Unavailable', hdrs=None, fp=None)`.
- Enters managed context(s) `patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=error), pytest.raises(RteOdreDownloadError)` and executes: Calls `download_rte_odre_dataset('sites', source_config, tmp_path)` for its validation or side effect.

**Action**

- Calls `HTTPError`, `_expire_cache`, `_feature_collection`, `_metadata_content`, `_metadata_path`, `_response`, `build_rte_odre_metadata_url`, `download_rte_odre_dataset`, `first.path.read_bytes`, `metadata_path.read_bytes`, `tmp_path.glob`.

**Expected result**

- Direct assertions: `assert first.path.read_bytes() == original_archive`; `assert metadata_path.read_bytes() == expired_metadata`; `assert metadata_path.read_bytes() != original_metadata`; `assert not list(tmp_path.glob('*.part'))`.
- Expected exception contexts: `with patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=error), pytest.raises(RteOdreDownloadError): download_rte_odre_dataset('sites', source_config, tmp_path)`.

**Regression protected**

- Protects the exact `failed refresh preserves previous valid cache` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `HTTPError`, `_expire_cache`, `_feature_collection`, `_metadata_content`, `_metadata_path`, `_response`, `build_rte_odre_metadata_url`, `download_rte_odre_dataset`, `first.path.read_bytes`, `list`, `metadata_path.read_bytes`, `patch`, `pytest.raises`, `tmp_path.glob`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_corrupted_refresh_preserves_previous_valid_cache`

**Signature**

```python
def test_corrupted_refresh_preserves_previous_valid_cache(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
```

**Purpose**

Protects the `corrupted refresh preserves previous valid cache` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 6 explicit setup/context statement(s).
- Computes `dataset_id` from `DATASET_IDS['sites']`.
- Enters managed context(s) `patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=[_response(_metadata_content(dataset_id)), _response(_feature_collection())])` and executes: Computes `first` from `download_rte_odre_dataset('sites', source_config, tmp_path)`.
- Computes `original_archive` from `first.path.read_bytes()`.
- Computes `metadata_path` from `_metadata_path(tmp_path, dataset_id)`.
- Computes `expired_metadata` from `metadata_path.read_bytes()`.
- Enters managed context(s) `patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=[_response(_metadata_content(dataset_id)), _response(b'{corrupted')]), pytest.raises(RteOdreDownloadError)` and executes: Calls `download_rte_odre_dataset('sites', source_config, tmp_path)` for its validation or side effect.

**Action**

- Calls `_expire_cache`, `_feature_collection`, `_metadata_content`, `_metadata_path`, `_response`, `download_rte_odre_dataset`, `first.path.read_bytes`, `metadata_path.read_bytes`, `tmp_path.glob`.

**Expected result**

- Direct assertions: `assert first.path.read_bytes() == original_archive`; `assert metadata_path.read_bytes() == expired_metadata`; `assert not list(tmp_path.glob('*.part'))`.
- Expected exception contexts: `with patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=[_response(_metadata_content(dataset_id)), _response(b'{corrupted')]), pytest.raises(RteOdreDownloadError): download_rte_odre_dataset('sites', source_config, tmp_path)`.

**Regression protected**

- Protects the exact `corrupted refresh preserves previous valid cache` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_expire_cache`, `_feature_collection`, `_metadata_content`, `_metadata_path`, `_response`, `download_rte_odre_dataset`, `first.path.read_bytes`, `list`, `metadata_path.read_bytes`, `patch`, `pytest.raises`, `tmp_path.glob`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_metadata_publication_failure_restores_previous_pair`

**Signature**

```python
def test_metadata_publication_failure_restores_previous_pair(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
```

**Purpose**

Protects the `metadata publication failure restores previous pair` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 9 explicit setup/context statement(s).
- Computes `dataset_id` from `DATASET_IDS['sites']`.
- Enters managed context(s) `patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=[_response(_metadata_content(dataset_id)), _response(_feature_collection())])` and executes: Computes `first` from `download_rte_odre_dataset('sites', source_config, tmp_path)`.
- Computes `metadata_path` from `_metadata_path(tmp_path, dataset_id)`.
- Computes `old_archive` from `first.path.read_bytes()`.
- Computes `old_metadata` from `metadata_path.read_bytes()`.
- Computes `temporary_metadata` from `metadata_path.with_suffix(f'{metadata_path.suffix}.part')`.
- Computes `original_replace` from `rte_odre_fr._replace_file`.
- Computes `failure_injected` from `False`.
- Enters managed context(s) `patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=[_response(_metadata_content(dataset_id)), _response(_feature_collection(all_null_geometry=True))]), patch.object(rte_odre_fr, '_replace_file', side_effect=fail_metadata_publication), pytest.raises(RteOdreDownloadError)` and executes: Calls `download_rte_odre_dataset('sites', source_config, tmp_path)` for its validation or side effect.

**Action**

- Calls `PermissionError`, `_expire_cache`, `_feature_collection`, `_metadata_content`, `_metadata_path`, `_response`, `download_rte_odre_dataset`, `first.path.read_bytes`, `metadata_path.read_bytes`, `metadata_path.with_suffix`, `original_replace`, `tmp_path.glob`.

**Expected result**

- Direct assertions: `assert failure_injected`; `assert first.path.read_bytes() == old_archive`; `assert metadata_path.read_bytes() == old_metadata`; `assert not list(tmp_path.glob('*.part'))`; `assert not list(tmp_path.glob('*.bak'))`.
- Expected exception contexts: `with patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=[_response(_metadata_content(dataset_id)), _response(_feature_collection(all_null_geometry=True))]), patch.object(rte_odre_fr, '_replace_file', side_effect=fail_metadata_publication), pytest.raises(RteOdreDownloadError): download_rte_odre_dataset('sites', source_config, tmp_path)`.

**Regression protected**

- Protects the exact `metadata publication failure restores previous pair` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `PermissionError`, `_expire_cache`, `_feature_collection`, `_metadata_content`, `_metadata_path`, `_response`, `download_rte_odre_dataset`, `first.path.read_bytes`, `list`, `metadata_path.read_bytes`, `metadata_path.with_suffix`, `original_replace`, `patch`, `patch.object`, `pytest.raises`, `tmp_path.glob`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_geojson_download_is_rejected`

**Signature**

```python
def test_invalid_geojson_download_is_rejected(
    tmp_path: Path,
    source_config: RteOdreSourceConfig,
    invalid_content: bytes,
) -> None:
```

**Purpose**

Protects the `invalid geojson download is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`, `invalid_content`.
- Contains 2 explicit setup/context statement(s).
- Computes `dataset_id` from `DATASET_IDS['sites']`.
- Enters managed context(s) `patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=[_response(_metadata_content(dataset_id)), _response(invalid_content)]), pytest.raises(RteOdreDownloadError)` and executes: Calls `download_rte_odre_dataset('sites', source_config, tmp_path)` for its validation or side effect.

**Action**

- Calls `_metadata_content`, `_response`, `download_rte_odre_dataset`, `json.dumps`, `json.dumps({'type': 'FeatureCollection'}).encode`, `json.dumps({'type': 'Point', 'coordinates': [1, 2]}).encode`, `tmp_path.glob`.

**Expected result**

- Direct assertions: `assert not list(tmp_path.glob('*.part'))`; `assert not list(tmp_path.glob('*.geojson'))`.
- Expected exception contexts: `with patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=[_response(_metadata_content(dataset_id)), _response(invalid_content)]), pytest.raises(RteOdreDownloadError): download_rte_odre_dataset('sites', source_config, tmp_path)`.

**Regression protected**

- Protects the exact `invalid geojson download is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_metadata_content`, `_response`, `download_rte_odre_dataset`, `json.dumps`, `json.dumps({'type': 'FeatureCollection'}).encode`, `json.dumps({'type': 'Point', 'coordinates': [1, 2]}).encode`, `list`, `patch`, `pytest.mark.parametrize`, `pytest.raises`, `tmp_path.glob`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_geojson_feature_or_geometry_is_rejected`

**Signature**

```python
def test_malformed_geojson_feature_or_geometry_is_rejected(
    tmp_path: Path,
    feature: object,
) -> None:
```

**Purpose**

Protects the `malformed geojson feature or geometry is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `feature`.
- Contains 2 explicit setup/context statement(s).
- Computes `path` from `tmp_path / 'malformed.geojson'`.
- Enters managed context(s) `pytest.raises(RteOdreDownloadError)` and executes: Calls `rte_odre_fr._validate_geojson(path)` for its validation or side effect.

**Action**

- Calls `json.dumps`, `path.write_text`, `rte_odre_fr._validate_geojson`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(RteOdreDownloadError): rte_odre_fr._validate_geojson(path)`.

**Regression protected**

- Protects the exact `malformed geojson feature or geometry is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `json.dumps`, `path.write_text`, `pytest.mark.parametrize`, `pytest.raises`, `rte_odre_fr._validate_geojson`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_standard_geojson_geometry_types_are_summarized`

**Signature**

```python
def test_standard_geojson_geometry_types_are_summarized(tmp_path: Path) -> None:
```

**Purpose**

Protects the `standard geojson geometry types are summarized` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 4 explicit setup/context statement(s).
- Computes `coordinate_types` from `{'Point': [1, 2], 'MultiPoint': [[1, 2]], 'LineString': [[1, 2], [2, 3]], 'MultiLineString': [[[1, 2], [2, 3]]], 'Polygon': [[[1, 2], [2, 3], [1, 2]]], 'MultiPolygon': [[[[1, 2], [2, 3], [1, 2]]]]}`.
- Computes `features` from `[{'type': 'Feature', 'geometry': {'type': geometry_type, 'coordinates': coordinates}} for geometry_type, coordinates in coordinate_types.items()]`.
- Computes `path` from `tmp_path / 'valid.geojson'`.
- Computes `summary` from `rte_odre_fr._validate_geojson(path)`.

**Action**

- Calls `coordinate_types.items`, `features.extend`, `json.dumps`, `path.write_text`, `rte_odre_fr._validate_geojson`, `sorted`.

**Expected result**

- Direct assertions: `assert summary.feature_count == 8`; `assert summary.null_geometry_count == 1`; `assert summary.non_null_geometry_count == 7`; `assert summary.geometry_types == tuple(sorted((*coordinate_types, 'GeometryCollection')))`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `standard geojson geometry types are summarized` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `coordinate_types.items`, `features.extend`, `json.dumps`, `path.write_text`, `rte_odre_fr._validate_geojson`, `sorted`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_point_requires_a_finite_numeric_position`

**Signature**

```python
def test_point_requires_a_finite_numeric_position(
    tmp_path: Path,
    coordinates: object,
) -> None:
```

**Purpose**

Protects the `point requires a finite numeric position` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `coordinates`.
- Contains 2 explicit setup/context statement(s).
- Computes `path` from `tmp_path / 'bad-point.geojson'`.
- Enters managed context(s) `pytest.raises(RteOdreDownloadError, match='coordinate|Point|finite')` and executes: Calls `rte_odre_fr._validate_geojson(path)` for its validation or side effect.

**Action**

- Calls `float`, `json.dumps`, `path.write_text`, `rte_odre_fr._validate_geojson`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(RteOdreDownloadError, match='coordinate|Point|finite'): rte_odre_fr._validate_geojson(path)`.

**Regression protected**

- Protects the exact `point requires a finite numeric position` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `float`, `json.dumps`, `path.write_text`, `pytest.mark.parametrize`, `pytest.raises`, `rte_odre_fr._validate_geojson`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_nested_coordinate_geometries_reject_obvious_invalid_structure`

**Signature**

```python
def test_nested_coordinate_geometries_reject_obvious_invalid_structure(
    tmp_path: Path,
    geometry_type: str,
    coordinates: object,
) -> None:
```

**Purpose**

Protects the `nested coordinate geometries reject obvious invalid structure` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `geometry_type`, `coordinates`.
- Contains 2 explicit setup/context statement(s).
- Computes `path` from `tmp_path / 'bad-nested.geojson'`.
- Enters managed context(s) `pytest.raises(RteOdreDownloadError, match='coordinate|structure|finite')` and executes: Calls `rte_odre_fr._validate_geojson(path)` for its validation or side effect.

**Action**

- Calls `float`, `json.dumps`, `path.write_text`, `rte_odre_fr._validate_geojson`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(RteOdreDownloadError, match='coordinate|structure|finite'): rte_odre_fr._validate_geojson(path)`.

**Regression protected**

- Protects the exact `nested coordinate geometries reject obvious invalid structure` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `float`, `json.dumps`, `path.write_text`, `pytest.mark.parametrize`, `pytest.raises`, `rte_odre_fr._validate_geojson`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_geometry_collection_members_are_validated_recursively`

**Signature**

```python
def test_geometry_collection_members_are_validated_recursively(tmp_path: Path) -> None:
```

**Purpose**

Protects the `geometry collection members are validated recursively` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `path` from `tmp_path / 'bad-collection.geojson'`.
- Enters managed context(s) `pytest.raises(RteOdreDownloadError, match='coordinate|Point')` and executes: Calls `rte_odre_fr._validate_geojson(path)` for its validation or side effect.

**Action**

- Calls `json.dumps`, `path.write_text`, `rte_odre_fr._validate_geojson`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(RteOdreDownloadError, match='coordinate|Point'): rte_odre_fr._validate_geojson(path)`.

**Regression protected**

- Protects the exact `geometry collection members are validated recursively` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `json.dumps`, `path.write_text`, `pytest.raises`, `rte_odre_fr._validate_geojson`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_null_feature_geometries_are_accepted`

**Signature**

```python
def test_null_feature_geometries_are_accepted(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
```

**Purpose**

Protects the `null feature geometries are accepted` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 3 explicit setup/context statement(s).
- Computes `dataset_id` from `DATASET_IDS['sites']`.
- Computes `export_content` from `_feature_collection(all_null_geometry=True)`.
- Enters managed context(s) `patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=[_response(_metadata_content(dataset_id)), _response(export_content)])` and executes: Computes `result` from `download_rte_odre_dataset('sites', source_config, tmp_path)`.

**Action**

- Calls `RteOdreExportSummary`, `_feature_collection`, `_metadata_content`, `_response`, `download_rte_odre_dataset`, `result.path.is_file`.

**Expected result**

- Direct assertions: `assert result.path.is_file()`; `assert result.dataset_metadata.geometry_precision_status == 'MISSING'`; `assert result.export_summary == RteOdreExportSummary(feature_count=2, null_geometry_count=2, non_null_geometry_count=0, geometry_types=())`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `null feature geometries are accepted` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `RteOdreExportSummary`, `_feature_collection`, `_metadata_content`, `_response`, `download_rte_odre_dataset`, `patch`, `result.path.is_file`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_lineage_sidecar_records_integrity`

**Signature**

```python
def test_lineage_sidecar_records_integrity(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
```

**Purpose**

Protects the `lineage sidecar records integrity` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 5 explicit setup/context statement(s).
- Computes `dataset_id` from `DATASET_IDS['sites']`.
- Computes `export_content` from `_feature_collection()`.
- Enters managed context(s) `patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=[_response(_metadata_content(dataset_id)), _response(export_content)])` and executes: Computes `result` from `download_rte_odre_dataset('sites', source_config, tmp_path)`.
- Computes `metadata_path` from `_metadata_path(tmp_path, dataset_id)`.
- Computes `lineage` from `json.loads(metadata_path.read_text(encoding='utf-8'))`.

**Action**

- Calls `_feature_collection`, `_metadata_content`, `_metadata_path`, `_response`, `download_rte_odre_dataset`, `json.loads`, `metadata_path.read_text`, `sha256`, `sha256(export_content).hexdigest`.

**Expected result**

- Direct assertions: `assert lineage['source_url'] == result.source_url`; `assert lineage['file_size'] == len(export_content)`; `assert lineage['sha256'] == sha256(export_content).hexdigest()`; `assert lineage['dataset_metadata']['publisher'] == 'RTE'`; `assert lineage['export_summary'] == {'feature_count': 2, 'geometry_types': ['Point'], 'non_null_geometry_count': 1, 'null_geometry_count': 1}`; `assert lineage['export_summary']['null_geometry_count'] + lineage['export_summary']['non_null_geometry_count'] == lineage['export_summary']['feature_count']`; `assert 'path' not in lineage`; `assert 'cache_hit' not in lineage`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `lineage sidecar records integrity` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_feature_collection`, `_metadata_content`, `_metadata_path`, `_response`, `download_rte_odre_dataset`, `json.loads`, `len`, `metadata_path.read_text`, `patch`, `sha256`, `sha256(export_content).hexdigest`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_cached_record_count_invalidates_cache`

**Signature**

```python
def test_invalid_cached_record_count_invalidates_cache(
    tmp_path: Path,
    source_config: RteOdreSourceConfig,
    cached_records_count: int,
) -> None:
```

**Purpose**

Protects the `invalid cached record count invalidates cache` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`, `cached_records_count`.
- Contains 7 explicit setup/context statement(s).
- Computes `dataset_id` from `DATASET_IDS['sites']`.
- Computes `valid_content` from `_feature_collection()`.
- Enters managed context(s) `patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=[_response(_metadata_content(dataset_id)), _response(valid_content)])` and executes: Computes `first` from `download_rte_odre_dataset('sites', source_config, tmp_path)`.
- Computes `metadata_path` from `_metadata_path(tmp_path, dataset_id)`.
- Computes `lineage` from `json.loads(metadata_path.read_text(encoding='utf-8'))`.
- Computes `lineage['dataset_metadata']['records_count']` from `cached_records_count`.
- Enters managed context(s) `patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=[_response(_metadata_content(dataset_id)), _response(valid_content)])` and executes: Computes `refreshed` from `download_rte_odre_dataset('sites', source_config, tmp_path)`.

**Action**

- Calls `_feature_collection`, `_metadata_content`, `_metadata_path`, `_response`, `download_rte_odre_dataset`, `first.path.read_bytes`, `json.dumps`, `json.loads`, `metadata_path.read_text`, `metadata_path.write_text`, `refreshed.path.read_bytes`.

**Expected result**

- Direct assertions: `assert opener.call_count == 2`; `assert refreshed.cache_hit is False`; `assert refreshed.path.read_bytes() == first.path.read_bytes()`; `assert refreshed.dataset_metadata.records_count == 2`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `invalid cached record count invalidates cache` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_feature_collection`, `_metadata_content`, `_metadata_path`, `_response`, `download_rte_odre_dataset`, `first.path.read_bytes`, `json.dumps`, `json.loads`, `metadata_path.read_text`, `metadata_path.write_text`, `patch`, `pytest.mark.parametrize`, `refreshed.path.read_bytes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_cached_export_summary_mismatch_invalidates_cache`

**Signature**

```python
def test_cached_export_summary_mismatch_invalidates_cache(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
```

**Purpose**

Protects the `cached export summary mismatch invalidates cache` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 9 explicit setup/context statement(s).
- Computes `dataset_id` from `DATASET_IDS['sites']`.
- Computes `valid_content` from `_feature_collection()`.
- Enters managed context(s) `patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=[_response(_metadata_content(dataset_id)), _response(valid_content)])` and executes: Calls `download_rte_odre_dataset('sites', source_config, tmp_path)` for its validation or side effect.
- Computes `metadata_path` from `_metadata_path(tmp_path, dataset_id)`.
- Computes `lineage` from `json.loads(metadata_path.read_text(encoding='utf-8'))`.
- Computes `lineage['export_summary']['null_geometry_count']` from `2`.
- Computes `lineage['export_summary']['non_null_geometry_count']` from `0`.
- Computes `lineage['export_summary']['geometry_types']` from `[]`.
- Enters managed context(s) `patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=[_response(_metadata_content(dataset_id)), _response(valid_content)])` and executes: Computes `refreshed` from `download_rte_odre_dataset('sites', source_config, tmp_path)`.

**Action**

- Calls `_feature_collection`, `_metadata_content`, `_metadata_path`, `_response`, `download_rte_odre_dataset`, `json.dumps`, `json.loads`, `metadata_path.read_text`, `metadata_path.write_text`.

**Expected result**

- Direct assertions: `assert opener.call_count == 2`; `assert refreshed.cache_hit is False`; `assert refreshed.export_summary.geometry_types == ('Point',)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `cached export summary mismatch invalidates cache` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_feature_collection`, `_metadata_content`, `_metadata_path`, `_response`, `download_rte_odre_dataset`, `json.dumps`, `json.loads`, `metadata_path.read_text`, `metadata_path.write_text`, `patch`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_corrupted_cached_export_triggers_refresh`

**Signature**

```python
def test_corrupted_cached_export_triggers_refresh(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
```

**Purpose**

Protects the `corrupted cached export triggers refresh` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 4 explicit setup/context statement(s).
- Computes `dataset_id` from `DATASET_IDS['sites']`.
- Computes `valid_content` from `_feature_collection()`.
- Enters managed context(s) `patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=[_response(_metadata_content(dataset_id)), _response(valid_content)])` and executes: Computes `first` from `download_rte_odre_dataset('sites', source_config, tmp_path)`.
- Enters managed context(s) `patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=[_response(_metadata_content(dataset_id)), _response(valid_content)])` and executes: Computes `refreshed` from `download_rte_odre_dataset('sites', source_config, tmp_path)`.

**Action**

- Calls `_feature_collection`, `_metadata_content`, `_response`, `download_rte_odre_dataset`, `first.path.write_bytes`, `refreshed.path.read_bytes`.

**Expected result**

- Direct assertions: `assert opener.call_count == 2`; `assert refreshed.cache_hit is False`; `assert refreshed.path.read_bytes() == valid_content`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `corrupted cached export triggers refresh` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_feature_collection`, `_metadata_content`, `_response`, `download_rte_odre_dataset`, `first.path.write_bytes`, `patch`, `refreshed.path.read_bytes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_double_failure_preserves_recovery_and_next_run_uses_zero_network`

**Signature**

```python
def test_double_failure_preserves_recovery_and_next_run_uses_zero_network(
    tmp_path: Path,
    source_config: RteOdreSourceConfig,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `double failure preserves recovery and next run uses zero network` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`, `monkeypatch`.
- Contains 14 explicit setup/context statement(s).
- Computes `dataset_id` from `DATASET_IDS['sites']`.
- Enters managed context(s) `patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=[_response(_metadata_content(dataset_id)), _response(_feature_collection())])` and executes: Computes `first` from `download_rte_odre_dataset('sites', source_config, tmp_path)`.
- Computes `metadata_path` from `_metadata_path(tmp_path, dataset_id)`.
- Computes `old_archive` from `first.path.read_bytes()`.
- Computes `old_metadata` from `metadata_path.read_bytes()`.
- Computes `temporary_metadata` from `metadata_path.with_suffix(f'{metadata_path.suffix}.part')`.
- Computes `archive_backup` from `first.path.with_suffix(f'{first.path.suffix}.bak')`.
- Computes `metadata_backup` from `metadata_path.with_suffix(f'{metadata_path.suffix}.bak')`.
- Computes `original_replace` from `rte_odre_fr._replace_file`.
- Enters managed context(s) `pytest.raises(RteOdreDownloadError, match='rollback')` and executes: Calls `download_rte_odre_dataset('sites', source_config, tmp_path)` for its validation or side effect.
- Computes `archive_recovery` from `archive_backup.read_bytes()`.
- Computes `metadata_recovery` from `metadata_backup.read_bytes()`.

**Action**

- Calls `AssertionError`, `OSError`, `_expire_cache`, `_feature_collection`, `_metadata_content`, `_metadata_path`, `_response`, `archive_backup.read_bytes`, `download_rte_odre_dataset`, `first.path.read_bytes`, `first.path.with_suffix`, `metadata_backup.read_bytes`, `metadata_path.read_bytes`, `metadata_path.with_suffix`, `monkeypatch.setattr`, `network_calls.append`, `original_replace`, `url.endswith`.

**Expected result**

- Direct assertions: `assert archive_backup.read_bytes() == old_archive`; `assert metadata_backup.read_bytes() == old_metadata`; `assert network_calls == []`; `assert archive_backup.read_bytes() == archive_recovery`; `assert metadata_backup.read_bytes() == metadata_recovery`.
- Expected exception contexts: `with pytest.raises(RteOdreDownloadError, match='rollback'): download_rte_odre_dataset('sites', source_config, tmp_path)`; `with pytest.raises(RteOdreDownloadError, match='backup|recovery|manual'): download_rte_odre_dataset('sites', source_config, tmp_path)`.

**Regression protected**

- Protects the exact `double failure preserves recovery and next run uses zero network` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks; fake/blocked network. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `AssertionError`, `OSError`, `_expire_cache`, `_feature_collection`, `_metadata_content`, `_metadata_path`, `_response`, `archive_backup.read_bytes`, `download_rte_odre_dataset`, `first.path.read_bytes`, `first.path.with_suffix`, `metadata_backup.read_bytes`, `metadata_path.read_bytes`, `metadata_path.with_suffix`, `monkeypatch.setattr`, `network_calls.append`, `original_replace`, `patch`, `pytest.raises`, `url.endswith`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_temporary_link_or_junction_cannot_modify_target_before_rte_network`

**Signature**

```python
def test_temporary_link_or_junction_cannot_modify_target_before_rte_network(
    tmp_path: Path,
    source_config: RteOdreSourceConfig,
    monkeypatch: pytest.MonkeyPatch,
    temporary_role: str,
    link_kind: str,
) -> None:
```

**Purpose**

Protects the `temporary link or junction cannot modify target before rte network` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`, `monkeypatch`, `temporary_role`, `link_kind`.
- Contains 12 explicit setup/context statement(s).
- Computes `dataset_id` from `DATASET_IDS['sites']`.
- Computes `archive_path` from `tmp_path / f'{dataset_id}.geojson'`.
- Computes `metadata_path` from `_metadata_path(tmp_path, dataset_id)`.
- Computes `temporary_paths` from `{'archive': archive_path.with_suffix(f'{archive_path.suffix}.part'), 'metadata': metadata_path.with_suffix(f'{metadata_path.suffix}.part')}`.
- Computes `unsafe_path` from `temporary_paths[temporary_role]`.
- Computes `sentinel` from `tmp_path / 'do-not-overwrite.txt'`.
- Computes `sentinel_bytes` from `b'irreplaceable RTE sentinel'`.
- Computes `original_is_symlink` from `Path.is_symlink`.
- Computes `original_is_junction` from `Path.is_junction`.
- Computes `original_open` from `Path.open`.
- Computes `network_calls` from `0`.
- Enters managed context(s) `pytest.raises(RteOdreDownloadError, match='temporary|link|cache')` and executes: Calls `download_rte_odre_dataset('sites', source_config, tmp_path)` for its validation or side effect.

**Action**

- Calls `_feature_collection`, `_metadata_content`, `_metadata_path`, `_response`, `archive_path.with_suffix`, `download_rte_odre_dataset`, `metadata_path.with_suffix`, `monkeypatch.setattr`, `original_is_junction`, `original_is_symlink`, `original_open`, `sentinel.read_bytes`, `sentinel.write_bytes`, `url.endswith`.

**Expected result**

- Direct assertions: `assert network_calls == 0`; `assert sentinel.read_bytes() == sentinel_bytes`.
- Expected exception contexts: `with pytest.raises(RteOdreDownloadError, match='temporary|link|cache'): download_rte_odre_dataset('sites', source_config, tmp_path)`.

**Regression protected**

- Protects the exact `temporary link or junction cannot modify target before rte network` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_feature_collection`, `_metadata_content`, `_metadata_path`, `_response`, `archive_path.with_suffix`, `download_rte_odre_dataset`, `metadata_path.with_suffix`, `monkeypatch.setattr`, `original_is_junction`, `original_is_symlink`, `original_open`, `pytest.mark.parametrize`, `pytest.raises`, `sentinel.read_bytes`, `sentinel.write_bytes`, `url.endswith`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_broken_recovery_symlink_rejects_rte_before_network`

**Signature**

```python
def test_broken_recovery_symlink_rejects_rte_before_network(
    tmp_path: Path,
    source_config: RteOdreSourceConfig,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `broken recovery symlink rejects rte before network` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`, `monkeypatch`.
- Contains 6 explicit setup/context statement(s).
- Computes `dataset_id` from `DATASET_IDS['sites']`.
- Computes `archive_path` from `tmp_path / f'{dataset_id}.geojson'`.
- Computes `recovery_path` from `archive_path.with_suffix(f'{archive_path.suffix}.bak')`.
- Computes `original_is_symlink` from `Path.is_symlink`.
- Defines `network_calls` with annotation `list[str]` from `[]`.
- Enters managed context(s) `pytest.raises(RteOdreDownloadError, match='backup|recovery|manual')` and executes: Calls `download_rte_odre_dataset('sites', source_config, tmp_path)` for its validation or side effect.

**Action**

- Calls `AssertionError`, `archive_path.with_suffix`, `download_rte_odre_dataset`, `monkeypatch.setattr`, `network_calls.append`, `original_is_symlink`.

**Expected result**

- Direct assertions: `assert network_calls == []`.
- Expected exception contexts: `with pytest.raises(RteOdreDownloadError, match='backup|recovery|manual'): download_rte_odre_dataset('sites', source_config, tmp_path)`.

**Regression protected**

- Protects the exact `broken recovery symlink rejects rte before network` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks; fake/blocked network. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `AssertionError`, `archive_path.with_suffix`, `download_rte_odre_dataset`, `monkeypatch.setattr`, `network_calls.append`, `original_is_symlink`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error`

**Signature**

```python
def test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error(
    tmp_path: Path,
    source_config: RteOdreSourceConfig,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `rte cleanup failure does not mask double failure recovery error` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`, `monkeypatch`.
- Contains 12 explicit setup/context statement(s).
- Computes `dataset_id` from `DATASET_IDS['sites']`.
- Enters managed context(s) `patch('landscout.sources.rte_odre_fr.open_safe_https', side_effect=[_response(_metadata_content(dataset_id)), _response(_feature_collection())])` and executes: Computes `first` from `download_rte_odre_dataset('sites', source_config, tmp_path)`.
- Computes `metadata_path` from `_metadata_path(tmp_path, dataset_id)`.
- Computes `old_archive` from `first.path.read_bytes()`.
- Computes `old_metadata` from `metadata_path.read_bytes()`.
- Computes `temporary_metadata` from `metadata_path.with_suffix(f'{metadata_path.suffix}.part')`.
- Computes `archive_backup` from `first.path.with_suffix(f'{first.path.suffix}.bak')`.
- Computes `metadata_backup` from `metadata_path.with_suffix(f'{metadata_path.suffix}.bak')`.
- Computes `original_replace` from `rte_odre_fr._replace_file`.
- Computes `original_unlink` from `Path.unlink`.
- Computes `rollback_failed` from `False`.
- Enters managed context(s) `pytest.raises(RteOdreDownloadError, match='rollback')` and executes: Calls `download_rte_odre_dataset('sites', source_config, tmp_path)` for its validation or side effect.

**Action**

- Calls `OSError`, `PermissionError`, `_expire_cache`, `_feature_collection`, `_metadata_content`, `_metadata_path`, `_response`, `archive_backup.read_bytes`, `download_rte_odre_dataset`, `first.path.read_bytes`, `first.path.with_suffix`, `metadata_backup.read_bytes`, `metadata_path.read_bytes`, `metadata_path.with_suffix`, `monkeypatch.setattr`, `original_replace`, `original_unlink`, `url.endswith`.

**Expected result**

- Direct assertions: `assert archive_backup.read_bytes() == old_archive`; `assert metadata_backup.read_bytes() == old_metadata`.
- Expected exception contexts: `with pytest.raises(RteOdreDownloadError, match='rollback'): download_rte_odre_dataset('sites', source_config, tmp_path)`.

**Regression protected**

- Protects the exact `rte cleanup failure does not mask double failure recovery error` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `OSError`, `PermissionError`, `_expire_cache`, `_feature_collection`, `_metadata_content`, `_metadata_path`, `_response`, `archive_backup.read_bytes`, `download_rte_odre_dataset`, `first.path.read_bytes`, `first.path.with_suffix`, `metadata_backup.read_bytes`, `metadata_path.read_bytes`, `metadata_path.with_suffix`, `monkeypatch.setattr`, `original_replace`, `original_unlink`, `patch`, `pytest.raises`, `url.endswith`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `api` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `base_url` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `cache` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `dataset_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `dataset_metadata` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `datasets` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `download_timestamp` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `export_summary` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `feature_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `features` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `file_size` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_types` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `max_age_hours` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `non_null_geometry_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `null_geometry_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `preferred_format` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `publisher` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `records_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `sha256` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `sites` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_url` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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

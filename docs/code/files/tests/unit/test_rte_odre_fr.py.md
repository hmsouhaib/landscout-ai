# `tests/unit/test_rte_odre_fr.py`

## File identity

- Repository path: `tests/unit/test_rte_odre_fr.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `rte_odre_fr` contracts exercised in this file.
- Source SHA256: `f437738409f25094f06ca20da5b68afc673ce5b4efb3e8879c1a0b1956700263`

## 1. Purpose

Provides complete unit and regression coverage for the `rte_odre_fr` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `import io`
- `import json`
- `from datetime import UTC, datetime, timedelta`
- `from hashlib import sha256`
- `from pathlib import Path`
- `from unittest.mock import patch`
- `from urllib.error import HTTPError`

### Third-party packages

- `import pytest`
- `import yaml`
- `from pydantic import HttpUrl, ValidationError`

### Internal LandScout imports

- `from landscout.sources import rte_odre_fr`
- `from landscout.sources.rte_odre_fr import (
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`

## 4. Contract taxonomy

### A. Python constants

#### `PROJECT_ROOT`

```python
PROJECT_ROOT = Path(__file__).parents[2]
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `CONFIG_PATH`

```python
CONFIG_PATH = PROJECT_ROOT / "configs/sources/rte_odre_fr.yaml"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_ign_bdtopo_fr.py::source_config` (value argument/reference), `tests/unit/test_rte_odre_fr.py::source_config` (value argument/reference).

#### `BASE_URL`

```python
BASE_URL = "https://odre.opendatasoft.com/api/explore/v2.1"
```

Configured/constructed URL component or origin constraint; it is textual identity until the transport/source validator proves bytes.

#### `DATASET_IDS`

```python
DATASET_IDS = {
    "sites": "postes-electriques-rte",
    "overhead_lines": "lignes-aeriennes-rte-nv",
    "underground_lines": "lignes-souterraines-rte-nv",
}
```

Module-level technical/source/policy constant consumed by the exact references below.


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

### `_config_data`

**Exact signature**

```python
def _config_data() -> dict:
```

**Purpose**

Private `test` helper for config data; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict`.
- Every observed return expression is reproduced without truncation:
```python
yaml.safe_load(stream)
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

- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_invalid_department_coverage_config_fails` via `_config_data`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_missing_required_source_field_fails` via `_config_data`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_invalid_source_configuration_fails` via `_config_data`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_unknown_source_config_field_is_rejected` via `_config_data`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_missing_dataset_id_fails` via `_config_data`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_empty_base_url_fails` via `_config_data`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_api_base_is_pinned_to_the_official_https_origin_and_path` via `_config_data`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_negative_cache_age_fails` via `_config_data`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_unsupported_export_format_fails` via `_config_data`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_export_url_uses_configured_dataset_id` via `_config_data`.

**Complete source-ordered implementation**

```python
def _config_data() -> dict:
    with CONFIG_PATH.open(encoding="utf-8") as stream:
        return yaml.safe_load(stream)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_metadata_content`

**Exact signature**

```python
def _metadata_content(dataset_id: str, records_count: int | None = 2) -> bytes:
```

**Purpose**

Private `test` helper for metadata content; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bytes`.
- Every observed return expression is reproduced without truncation:
```python
json.dumps(payload, ensure_ascii=False).encode('utf-8')
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

- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_metadata_is_captured_without_fabrication` via `_metadata_content`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_successful_download` via `_metadata_content`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_metadata_export_record_count_mismatch_is_rejected` via `_metadata_content`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_unavailable_metadata_record_count_is_accepted` via `_metadata_content`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_negative_source_record_count_is_rejected` via `_metadata_content`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_fresh_cache_is_reused` via `_metadata_content`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_expired_cache_is_refreshed` via `_metadata_content`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_http_failure_raises_and_cleans_temporary_files` via `_metadata_content`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_failed_refresh_preserves_previous_valid_cache` via `_metadata_content`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_corrupted_refresh_preserves_previous_valid_cache` via `_metadata_content`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_metadata_publication_failure_restores_previous_pair` via `_metadata_content`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_invalid_geojson_download_is_rejected` via `_metadata_content`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_null_feature_geometries_are_accepted` via `_metadata_content`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_lineage_sidecar_records_integrity` via `_metadata_content`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_invalid_cached_record_count_invalidates_cache` via `_metadata_content`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_cached_export_summary_mismatch_invalidates_cache` via `_metadata_content`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_corrupted_cached_export_triggers_refresh` via `_metadata_content`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `_metadata_content`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network.response_for_url` via `_metadata_content`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_rte_network.record_network` via `_metadata_content`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_metadata_content`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error.response_for_url` via `_metadata_content`.

**Complete source-ordered implementation**

```python
def _metadata_content(dataset_id: str, records_count: int | None = 2) -> bytes:
    payload = {
        "dataset_id": dataset_id,
        "metas": {
            "default": {
                "title": "Official RTE dataset",
                "publisher": "RTE",
                "modified": "2026-06-16T12:00:00+00:00",
                "data_processed": "2026-06-16T12:01:00+00:00",
                "metadata_processed": "2026-06-16T12:01:01+00:00",
                "license": "Licence Ouverte v2.0 (Etalab)",
                "records_count": records_count,
                "description": (
                    "RTE a fait évoluer l'accès aux données GPS pour des raisons "
                    "de sécurité publique."
                ),
            }
        },
    }
    return json.dumps(payload, ensure_ascii=False).encode("utf-8")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_feature_collection`

**Exact signature**

```python
def _feature_collection(*, all_null_geometry: bool = False) -> bytes:
```

**Purpose**

Private `test` helper for feature collection; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bytes`.
- Every observed return expression is reproduced without truncation:
```python
json.dumps(payload).encode('utf-8')
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

- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_successful_download` via `_feature_collection`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_metadata_export_record_count_mismatch_is_rejected` via `_feature_collection`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_unavailable_metadata_record_count_is_accepted` via `_feature_collection`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_fresh_cache_is_reused` via `_feature_collection`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_expired_cache_is_refreshed` via `_feature_collection`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_failed_refresh_preserves_previous_valid_cache` via `_feature_collection`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_corrupted_refresh_preserves_previous_valid_cache` via `_feature_collection`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_metadata_publication_failure_restores_previous_pair` via `_feature_collection`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_null_feature_geometries_are_accepted` via `_feature_collection`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_lineage_sidecar_records_integrity` via `_feature_collection`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_invalid_cached_record_count_invalidates_cache` via `_feature_collection`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_cached_export_summary_mismatch_invalidates_cache` via `_feature_collection`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_corrupted_cached_export_triggers_refresh` via `_feature_collection`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `_feature_collection`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network.response_for_url` via `_feature_collection`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_rte_network.record_network` via `_feature_collection`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_feature_collection`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error.response_for_url` via `_feature_collection`.

**Complete source-ordered implementation**

```python
def _feature_collection(*, all_null_geometry: bool = False) -> bytes:
    geometry = None if all_null_geometry else {"type": "Point", "coordinates": [1, 2]}
    payload = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {"code": "A"},
                "geometry": geometry,
            },
            {
                "type": "Feature",
                "properties": {"code": "B"},
                "geometry": None,
            },
        ],
    }
    return json.dumps(payload).encode("utf-8")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_response`

**Exact signature**

```python
def _response(content: bytes) -> io.BytesIO:
```

**Purpose**

Private `test` helper for response; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `io.BytesIO`.
- Every observed return expression is reproduced without truncation:
```python
io.BytesIO(content)
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

- property/attribute access: `src/landscout/common/safe_http.py::SafeHttpsResponse.read` via `self._response`.
- property/attribute access: `src/landscout/common/safe_http.py::SafeHttpsResponse.close` via `self._response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::_extracted_fixture` via `_response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_successful_archive_download_persists_sha256` via `_response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_fresh_cache_is_reused_without_network` via `_response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_stale_recovery_backup_rejects_cache_before_network` via `_response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_expired_cache_is_refreshed` via `_response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_failed_refresh_preserves_valid_cache` via `_response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned` via `_response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_corrupt_refresh_preserves_valid_cache` via `_response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_metadata_publication_failure_restores_previous_cache_pair` via `_response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_official_checksum_mismatch_is_rejected` via `_response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_unsafe_parent_archive_member_is_rejected` via `_response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_synthetic_archive_extracts_and_discovers_required_layers` via `_response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_default_extraction_path_is_short_and_content_addressed` via `_response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_electricity_loader_retains_both_layer_counts` via `_response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_road_layer_discovery_loads_selected_physical_layer` via `_response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_missing_road_layer_fails_safely` via `_response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_ambiguous_road_layer_fails_safely` via `_response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_wrong_archive_config_department` via `_response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_changed_layer_inventory` via `_response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_geographic_crs` via `_response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_preserves_lambert93_lines_unchanged` via `_response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_road_layer_does_not_change_electricity_loading_or_cache_shape` via `_response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_loader_selects_configured_identity` via `_response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_one_authoritative_feature` via `_response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_configured_identity_field` via `_response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_missing_department_coverage_layer_fails` via `_response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_layer_discovery_must_be_unambiguous` via `_response`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_direct_consumers_reject_same_inventory_content_tampering` via `_response`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_metadata_is_captured_without_fabrication` via `_response`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_successful_download` via `_response`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_metadata_export_record_count_mismatch_is_rejected` via `_response`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_unavailable_metadata_record_count_is_accepted` via `_response`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_negative_source_record_count_is_rejected` via `_response`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_fresh_cache_is_reused` via `_response`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_expired_cache_is_refreshed` via `_response`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_http_failure_raises_and_cleans_temporary_files` via `_response`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_failed_refresh_preserves_previous_valid_cache` via `_response`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_corrupted_refresh_preserves_previous_valid_cache` via `_response`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_metadata_publication_failure_restores_previous_pair` via `_response`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_invalid_geojson_download_is_rejected` via `_response`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_null_feature_geometries_are_accepted` via `_response`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_lineage_sidecar_records_integrity` via `_response`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_invalid_cached_record_count_invalidates_cache` via `_response`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_cached_export_summary_mismatch_invalidates_cache` via `_response`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_corrupted_cached_export_triggers_refresh` via `_response`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `_response`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network.response_for_url` via `_response`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_rte_network.record_network` via `_response`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_response`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error.response_for_url` via `_response`.

**Complete source-ordered implementation**

```python
def _response(content: bytes) -> io.BytesIO:
    return io.BytesIO(content)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_metadata_path`

**Exact signature**

```python
def _metadata_path(cache_dir: Path, dataset_id: str) -> Path:
```

**Purpose**

Private `test` helper for metadata path; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Path`.
- Every observed return expression is reproduced without truncation:
```python
cache_dir / f'{dataset_id}.geojson.metadata.json'
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

- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::download_inpn_protected_areas_archive` via `_metadata_path`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_successful_archive_download_persists_sha256` via `_metadata_path`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_expired_cache_is_refreshed` via `_metadata_path`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_failed_refresh_preserves_valid_cache` via `_metadata_path`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_corrupt_refresh_preserves_valid_cache` via `_metadata_path`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_metadata_publication_failure_restores_previous_cache_pair` via `_metadata_path`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_metadata_path`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_expired_cache_is_refreshed` via `_metadata_path`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_failed_refresh_preserves_previous_valid_cache` via `_metadata_path`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_corrupted_refresh_preserves_previous_valid_cache` via `_metadata_path`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_metadata_publication_failure_restores_previous_pair` via `_metadata_path`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_lineage_sidecar_records_integrity` via `_metadata_path`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_invalid_cached_record_count_invalidates_cache` via `_metadata_path`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_cached_export_summary_mismatch_invalidates_cache` via `_metadata_path`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `_metadata_path`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_rte_network` via `_metadata_path`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_metadata_path`.

**Complete source-ordered implementation**

```python
def _metadata_path(cache_dir: Path, dataset_id: str) -> Path:
    return cache_dir / f"{dataset_id}.geojson.metadata.json"
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_expire_cache`

**Exact signature**

```python
def _expire_cache(metadata_path: Path) -> None:
```

**Purpose**

Private `test` helper for expire cache; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: `metadata_path.read_text`.
- Filesystem write: `metadata_path.write_text`.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `metadata['download_timestamp']`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_expired_cache_is_refreshed` via `_expire_cache`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_failed_refresh_preserves_valid_cache` via `_expire_cache`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_corrupt_refresh_preserves_valid_cache` via `_expire_cache`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_metadata_publication_failure_restores_previous_cache_pair` via `_expire_cache`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_expire_cache`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_expired_cache_is_refreshed` via `_expire_cache`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_failed_refresh_preserves_previous_valid_cache` via `_expire_cache`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_corrupted_refresh_preserves_previous_valid_cache` via `_expire_cache`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_metadata_publication_failure_restores_previous_pair` via `_expire_cache`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `_expire_cache`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_expire_cache`.

**Complete source-ordered implementation**

```python
def _expire_cache(metadata_path: Path) -> None:
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["download_timestamp"] = (
        datetime.now(UTC) - timedelta(hours=169)
    ).isoformat()
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `source_config` — pytest fixture

- Scope: `function` (decorator `pytest.fixture`).
- Returned/yielded object expression(s): `load_rte_odre_source_config(CONFIG_PATH)`.
- Tests requesting it by parameter injection: `test_valid_source_config_loads`, `test_mutated_loaded_api_origin_is_rejected_before_metadata_network`, `test_build_export_url`, `test_build_metadata_url`, `test_metadata_is_captured_without_fabrication`, `test_successful_download`, `test_metadata_export_record_count_mismatch_is_rejected`, `test_unavailable_metadata_record_count_is_accepted`, `test_negative_source_record_count_is_rejected`, `test_fresh_cache_is_reused`, `test_expired_cache_is_refreshed`, `test_http_failure_raises_and_cleans_temporary_files`, `test_failed_refresh_preserves_previous_valid_cache`, `test_corrupted_refresh_preserves_previous_valid_cache`, `test_metadata_publication_failure_restores_previous_pair`, `test_invalid_geojson_download_is_rejected`, `test_null_feature_geometries_are_accepted`, `test_lineage_sidecar_records_integrity`, `test_invalid_cached_record_count_invalidates_cache`, `test_cached_export_summary_mismatch_invalidates_cache`, `test_corrupted_cached_export_triggers_refresh`, `test_double_failure_preserves_recovery_and_next_run_uses_zero_network`, `test_temporary_link_or_junction_cannot_modify_target_before_rte_network`, `test_broken_recovery_symlink_rejects_rte_before_network`, `test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error`.

**Complete fixture implementation**

```python
def source_config() -> RteOdreSourceConfig:
    return load_rte_odre_source_config(CONFIG_PATH)
```

### `test_valid_source_config_loads`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert source_config.provider == "RTE"
assert source_config.portal == "ODRE"
assert source_config.datasets.sites.dataset_id == "postes-electriques-rte"
assert source_config.cache.max_age_hours == 168
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_valid_source_config_loads(source_config: RteOdreSourceConfig) -> None:
    assert source_config.provider == "RTE"
    assert source_config.portal == "ODRE"
    assert source_config.datasets.sites.dataset_id == "postes-electriques-rte"
    assert source_config.cache.max_age_hours == 168
```

### `test_missing_dataset_id_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
config_data = _config_data()
del config_data["datasets"]["sites"]["dataset_id"]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError):
        RteOdreSourceConfig.model_validate(config_data)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_missing_dataset_id_fails() -> None:
    config_data = _config_data()
    del config_data["datasets"]["sites"]["dataset_id"]

    with pytest.raises(ValidationError):
        RteOdreSourceConfig.model_validate(config_data)
```

### `test_empty_base_url_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
config_data = _config_data()
config_data["api"]["base_url"] = ""
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError):
        RteOdreSourceConfig.model_validate(config_data)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_empty_base_url_fails() -> None:
    config_data = _config_data()
    config_data["api"]["base_url"] = ""

    with pytest.raises(ValidationError):
        RteOdreSourceConfig.model_validate(config_data)
```

### `test_api_base_is_pinned_to_the_official_https_origin_and_path`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `base_url`.

**Setup**

```python
config_data = _config_data()
config_data["api"]["base_url"] = base_url
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError):
        RteOdreSourceConfig.model_validate(config_data)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_api_base_is_pinned_to_the_official_https_origin_and_path(
    base_url: str,
) -> None:
    config_data = _config_data()
    config_data["api"]["base_url"] = base_url

    with pytest.raises(ValidationError):
        RteOdreSourceConfig.model_validate(config_data)
```

### `test_mutated_loaded_api_origin_is_rejected_before_metadata_network`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `source_config` (local fixture, scope `function`), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source_config.api.base_url = HttpUrl(
        "https://unrelated.example/api/explore/v2.1"
    )
network_calls = 0
def fail_network(*args: object, **kwargs: object) -> object:
        nonlocal network_calls
        network_calls += 1
        raise AssertionError("network used after ODRE origin mutation")
monkeypatch.setattr(rte_odre_fr, "open_safe_https", fail_network)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RteOdreDownloadError, match="config|official|origin"):
        fetch_rte_odre_dataset_metadata(source_config, "sites")
assert network_calls == 0
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_mutated_loaded_api_origin_is_rejected_before_metadata_network(
    source_config: RteOdreSourceConfig,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source_config.api.base_url = HttpUrl(
        "https://unrelated.example/api/explore/v2.1"
    )
    network_calls = 0

    def fail_network(*args: object, **kwargs: object) -> object:
        nonlocal network_calls
        network_calls += 1
        raise AssertionError("network used after ODRE origin mutation")

    monkeypatch.setattr(rte_odre_fr, "open_safe_https", fail_network)

    with pytest.raises(RteOdreDownloadError, match="config|official|origin"):
        fetch_rte_odre_dataset_metadata(source_config, "sites")

    assert network_calls == 0
```

### `test_mutated_loaded_api_origin_is_rejected_before_metadata_network.fail_network`

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
- Explicit raise expressions: `AssertionError('network used after ODRE origin mutation')`.

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

- callback/function object: `tests/unit/test_cadastre_fr.py::test_broken_recovery_symlink_is_rejected_before_network` via `monkeypatch.setattr(cadastre_fr, 'open_safe_https', fail_network)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_mutated_loaded_api_origin_is_rejected_before_discovery_network` via `monkeypatch.setattr(gpu, 'open_safe_https', fail_network)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_download_rejects_forged_written_file_provenance_before_network` via `monkeypatch.setattr(gpu, 'open_safe_https', fail_network)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_stale_recovery_backup_rejects_cache_before_network` via `monkeypatch.setattr(gpu, 'open_safe_https', fail_network)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_mutated_loaded_api_origin_is_rejected_before_metadata_network` via `monkeypatch.setattr(rte_odre_fr, 'open_safe_https', fail_network)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `monkeypatch.setattr(rte_odre_fr, 'open_safe_https', fail_network)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_broken_recovery_symlink_rejects_rte_before_network` via `monkeypatch.setattr(rte_odre_fr, 'open_safe_https', fail_network)`.

**Complete source-ordered implementation**

```python
def fail_network(*args: object, **kwargs: object) -> object:
        nonlocal network_calls
        network_calls += 1
        raise AssertionError("network used after ODRE origin mutation")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_negative_cache_age_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
config_data = _config_data()
config_data["cache"]["max_age_hours"] = -1
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError):
        RteOdreSourceConfig.model_validate(config_data)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_negative_cache_age_fails() -> None:
    config_data = _config_data()
    config_data["cache"]["max_age_hours"] = -1

    with pytest.raises(ValidationError):
        RteOdreSourceConfig.model_validate(config_data)
```

### `test_unsupported_export_format_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
config_data = _config_data()
config_data["datasets"]["sites"]["preferred_format"] = "csv"
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError):
        RteOdreSourceConfig.model_validate(config_data)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_unsupported_export_format_fails() -> None:
    config_data = _config_data()
    config_data["datasets"]["sites"]["preferred_format"] = "csv"

    with pytest.raises(ValidationError):
        RteOdreSourceConfig.model_validate(config_data)
```

### `test_build_export_url`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `dataset_id`, `logical_name`.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
url = build_rte_odre_export_url(source_config, logical_name)
```

**Expected result**

```python
assert url == f"{BASE_URL}/catalog/datasets/{dataset_id}/exports/geojson"
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_build_export_url(
    source_config: RteOdreSourceConfig, logical_name: str, dataset_id: str
) -> None:
    url = build_rte_odre_export_url(source_config, logical_name)  # type: ignore[arg-type]

    assert url == f"{BASE_URL}/catalog/datasets/{dataset_id}/exports/geojson"
```

### `test_build_metadata_url`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert build_rte_odre_metadata_url(source_config, "sites") == (
        f"{BASE_URL}/catalog/datasets/postes-electriques-rte"
    )
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_build_metadata_url(source_config: RteOdreSourceConfig) -> None:
    assert build_rte_odre_metadata_url(source_config, "sites") == (
        f"{BASE_URL}/catalog/datasets/postes-electriques-rte"
    )
```

### `test_export_url_uses_configured_dataset_id`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
config_data = _config_data()
config_data["datasets"]["sites"]["dataset_id"] = "configured-sites"
config = RteOdreSourceConfig.model_validate(config_data)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert build_rte_odre_export_url(config, "sites").endswith(
        "/catalog/datasets/configured-sites/exports/geojson"
    )
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_export_url_uses_configured_dataset_id() -> None:
    config_data = _config_data()
    config_data["datasets"]["sites"]["dataset_id"] = "configured-sites"
    config = RteOdreSourceConfig.model_validate(config_data)

    assert build_rte_odre_export_url(config, "sites").endswith(
        "/catalog/datasets/configured-sites/exports/geojson"
    )
```

### `test_metadata_is_captured_without_fabrication`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
content = _metadata_content(DATASET_IDS["sites"])
```

**Action**

```python
with patch(
        "landscout.sources.rte_odre_fr.open_safe_https", return_value=_response(content)
    ):
        metadata = fetch_rte_odre_dataset_metadata(source_config, "sites")
```

**Expected result**

```python
assert metadata.title == "Official RTE dataset"
assert metadata.publisher == "RTE"
assert metadata.modified == "2026-06-16T12:00:00+00:00"
assert metadata.data_processed == "2026-06-16T12:01:00+00:00"
assert metadata.metadata_processed == "2026-06-16T12:01:01+00:00"
assert metadata.license == "Licence Ouverte v2.0 (Etalab)"
assert metadata.records_count == 2
assert metadata.geometry_precision_status == "GENERALIZED_OR_RESTRICTED"
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_metadata_is_captured_without_fabrication(
    source_config: RteOdreSourceConfig,
) -> None:
    content = _metadata_content(DATASET_IDS["sites"])
    with patch(
        "landscout.sources.rte_odre_fr.open_safe_https", return_value=_response(content)
    ):
        metadata = fetch_rte_odre_dataset_metadata(source_config, "sites")

    assert metadata.title == "Official RTE dataset"
    assert metadata.publisher == "RTE"
    assert metadata.modified == "2026-06-16T12:00:00+00:00"
    assert metadata.data_processed == "2026-06-16T12:01:00+00:00"
    assert metadata.metadata_processed == "2026-06-16T12:01:01+00:00"
    assert metadata.license == "Licence Ouverte v2.0 (Etalab)"
    assert metadata.records_count == 2
    assert metadata.geometry_precision_status == "GENERALIZED_OR_RESTRICTED"
```

### `test_successful_download`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
dataset_id = DATASET_IDS["sites"]
export_content = _feature_collection()
```

**Action**

```python
with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(export_content),
        ],
    ):
        result = download_rte_odre_dataset("sites", source_config, tmp_path)
```

**Expected result**

```python
assert result.logical_name == "sites"
assert result.dataset_id == dataset_id
assert result.provider == "RTE"
assert result.portal == "ODRE"
assert result.export_format == "geojson"
assert result.path.read_bytes() == export_content
assert result.file_size == len(export_content)
assert result.sha256 == sha256(export_content).hexdigest()
assert result.cache_hit is False
assert result.dataset_metadata.title == "Official RTE dataset"
assert result.dataset_metadata.records_count == result.export_summary.feature_count
assert result.export_summary == RteOdreExportSummary(
        feature_count=2,
        null_geometry_count=1,
        non_null_geometry_count=1,
        geometry_types=("Point",),
    )
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_successful_download(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
    dataset_id = DATASET_IDS["sites"]
    export_content = _feature_collection()
    with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(export_content),
        ],
    ):
        result = download_rte_odre_dataset("sites", source_config, tmp_path)

    assert result.logical_name == "sites"
    assert result.dataset_id == dataset_id
    assert result.provider == "RTE"
    assert result.portal == "ODRE"
    assert result.export_format == "geojson"
    assert result.path.read_bytes() == export_content
    assert result.file_size == len(export_content)
    assert result.sha256 == sha256(export_content).hexdigest()
    assert result.cache_hit is False
    assert result.dataset_metadata.title == "Official RTE dataset"
    assert result.dataset_metadata.records_count == result.export_summary.feature_count
    assert result.export_summary == RteOdreExportSummary(
        feature_count=2,
        null_geometry_count=1,
        non_null_geometry_count=1,
        geometry_types=("Point",),
    )
```

### `test_metadata_export_record_count_mismatch_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `records_count`.

**Setup**

```python
dataset_id = DATASET_IDS["sites"]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with (
        patch(
            "landscout.sources.rte_odre_fr.open_safe_https",
            side_effect=[
                _response(_metadata_content(dataset_id, records_count)),
                _response(_feature_collection()),
            ],
        ),
        pytest.raises(RteOdreDownloadError, match="records_count"),
    ):
        download_rte_odre_dataset("sites", source_config, tmp_path)
assert not list(tmp_path.glob("*.geojson"))
assert not list(tmp_path.glob("*.part"))
assert not list(tmp_path.glob("*.bak"))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_metadata_export_record_count_mismatch_is_rejected(
    tmp_path: Path,
    source_config: RteOdreSourceConfig,
    records_count: int,
) -> None:
    dataset_id = DATASET_IDS["sites"]
    with (
        patch(
            "landscout.sources.rte_odre_fr.open_safe_https",
            side_effect=[
                _response(_metadata_content(dataset_id, records_count)),
                _response(_feature_collection()),
            ],
        ),
        pytest.raises(RteOdreDownloadError, match="records_count"),
    ):
        download_rte_odre_dataset("sites", source_config, tmp_path)

    assert not list(tmp_path.glob("*.geojson"))
    assert not list(tmp_path.glob("*.part"))
    assert not list(tmp_path.glob("*.bak"))
```

### `test_unavailable_metadata_record_count_is_accepted`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
dataset_id = DATASET_IDS["sites"]
```

**Action**

```python
with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id, records_count=None)),
            _response(_feature_collection()),
        ],
    ):
        result = download_rte_odre_dataset("sites", source_config, tmp_path)
```

**Expected result**

```python
assert result.dataset_metadata.records_count is None
assert result.export_summary.feature_count == 2
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_unavailable_metadata_record_count_is_accepted(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
    dataset_id = DATASET_IDS["sites"]
    with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id, records_count=None)),
            _response(_feature_collection()),
        ],
    ):
        result = download_rte_odre_dataset("sites", source_config, tmp_path)

    assert result.dataset_metadata.records_count is None
    assert result.export_summary.feature_count == 2
```

### `test_negative_source_record_count_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
dataset_id = DATASET_IDS["sites"]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with (
        patch(
            "landscout.sources.rte_odre_fr.open_safe_https",
            return_value=_response(_metadata_content(dataset_id, records_count=-1)),
        ),
        pytest.raises(RteOdreDownloadError, match="must not be negative"),
    ):
        download_rte_odre_dataset("sites", source_config, tmp_path)
assert not list(tmp_path.glob("*.part"))
assert not list(tmp_path.glob("*.bak"))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_negative_source_record_count_is_rejected(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
    dataset_id = DATASET_IDS["sites"]
    with (
        patch(
            "landscout.sources.rte_odre_fr.open_safe_https",
            return_value=_response(_metadata_content(dataset_id, records_count=-1)),
        ),
        pytest.raises(RteOdreDownloadError, match="must not be negative"),
    ):
        download_rte_odre_dataset("sites", source_config, tmp_path)

    assert not list(tmp_path.glob("*.part"))
    assert not list(tmp_path.glob("*.bak"))
```

### `test_export_summary_rejects_invalid_geometry_counts`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `feature_count`, `non_null_geometry_count`, `null_geometry_count`.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValueError):
        RteOdreExportSummary(
            feature_count=feature_count,
            null_geometry_count=null_geometry_count,
            non_null_geometry_count=non_null_geometry_count,
            geometry_types=(),
        )
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_export_summary_rejects_invalid_geometry_counts(
    feature_count: int,
    null_geometry_count: int,
    non_null_geometry_count: int,
) -> None:
    with pytest.raises(ValueError):
        RteOdreExportSummary(
            feature_count=feature_count,
            null_geometry_count=null_geometry_count,
            non_null_geometry_count=non_null_geometry_count,
            geometry_types=(),
        )
```

### `test_fresh_cache_is_reused`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
dataset_id = DATASET_IDS["sites"]
```

**Action**

```python
with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(_feature_collection()),
        ],
    ) as opener:
        first = download_rte_odre_dataset("sites", source_config, tmp_path)
        second = download_rte_odre_dataset("sites", source_config, tmp_path)
```

**Expected result**

```python
assert opener.call_count == 2
assert first.cache_hit is False
assert second.cache_hit is True
assert second.download_timestamp == first.download_timestamp
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
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
    dataset_id = DATASET_IDS["sites"]
    with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(_feature_collection()),
        ],
    ) as opener:
        first = download_rte_odre_dataset("sites", source_config, tmp_path)
        second = download_rte_odre_dataset("sites", source_config, tmp_path)

    assert opener.call_count == 2
    assert first.cache_hit is False
    assert second.cache_hit is True
    assert second.download_timestamp == first.download_timestamp
    assert second.sha256 == first.sha256
```

### `test_expired_cache_is_refreshed`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
dataset_id = DATASET_IDS["sites"]
initial_content = _feature_collection()
refreshed_payload = json.loads(initial_content)
refreshed_payload["features"].append(
        {"type": "Feature", "properties": {"code": "C"}, "geometry": None}
    )
refreshed_content = json.dumps(refreshed_payload).encode("utf-8")
_expire_cache(_metadata_path(tmp_path, dataset_id))
```

**Action**

```python
with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(initial_content),
        ],
    ):
        first = download_rte_odre_dataset("sites", source_config, tmp_path)
with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id, records_count=3)),
            _response(refreshed_content),
        ],
    ) as opener:
        refreshed = download_rte_odre_dataset("sites", source_config, tmp_path)
```

**Expected result**

```python
assert opener.call_count == 2
assert refreshed.cache_hit is False
assert refreshed.path.read_bytes() == refreshed_content
assert refreshed.sha256 != first.sha256
assert refreshed.export_summary.feature_count == 3
assert not list(tmp_path.glob("*.bak"))
assert not list(tmp_path.glob("*.part"))
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_expired_cache_is_refreshed(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
    dataset_id = DATASET_IDS["sites"]
    initial_content = _feature_collection()
    refreshed_payload = json.loads(initial_content)
    refreshed_payload["features"].append(
        {"type": "Feature", "properties": {"code": "C"}, "geometry": None}
    )
    refreshed_content = json.dumps(refreshed_payload).encode("utf-8")
    with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(initial_content),
        ],
    ):
        first = download_rte_odre_dataset("sites", source_config, tmp_path)
    _expire_cache(_metadata_path(tmp_path, dataset_id))

    with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id, records_count=3)),
            _response(refreshed_content),
        ],
    ) as opener:
        refreshed = download_rte_odre_dataset("sites", source_config, tmp_path)

    assert opener.call_count == 2
    assert refreshed.cache_hit is False
    assert refreshed.path.read_bytes() == refreshed_content
    assert refreshed.sha256 != first.sha256
    assert refreshed.export_summary.feature_count == 3
    assert not list(tmp_path.glob("*.bak"))
    assert not list(tmp_path.glob("*.part"))
```

### `test_http_failure_raises_and_cleans_temporary_files`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
dataset_id = DATASET_IDS["sites"]
error = HTTPError(source_url, 503, "Unavailable", hdrs=None, fp=None)
```

**Action**

```python
source_url = build_rte_odre_export_url(source_config, "sites")
```

**Expected result**

```python
with (
        patch(
            "landscout.sources.rte_odre_fr.open_safe_https",
            side_effect=[_response(_metadata_content(dataset_id)), error],
        ),
        pytest.raises(RteOdreDownloadError),
    ):
        download_rte_odre_dataset("sites", source_config, tmp_path)
assert not list(tmp_path.glob("*.part"))
assert not list(tmp_path.glob("*.geojson"))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_http_failure_raises_and_cleans_temporary_files(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
    dataset_id = DATASET_IDS["sites"]
    source_url = build_rte_odre_export_url(source_config, "sites")
    error = HTTPError(source_url, 503, "Unavailable", hdrs=None, fp=None)
    with (
        patch(
            "landscout.sources.rte_odre_fr.open_safe_https",
            side_effect=[_response(_metadata_content(dataset_id)), error],
        ),
        pytest.raises(RteOdreDownloadError),
    ):
        download_rte_odre_dataset("sites", source_config, tmp_path)

    assert not list(tmp_path.glob("*.part"))
    assert not list(tmp_path.glob("*.geojson"))
```

### `test_failed_refresh_preserves_previous_valid_cache`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
dataset_id = DATASET_IDS["sites"]
original_archive = first.path.read_bytes()
metadata_path = _metadata_path(tmp_path, dataset_id)
original_metadata = metadata_path.read_bytes()
_expire_cache(metadata_path)
expired_metadata = metadata_path.read_bytes()
error = HTTPError(metadata_url, 503, "Unavailable", hdrs=None, fp=None)
```

**Action**

```python
with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(_feature_collection()),
        ],
    ):
        first = download_rte_odre_dataset("sites", source_config, tmp_path)
metadata_url = build_rte_odre_metadata_url(source_config, "sites")
```

**Expected result**

```python
with (
        patch("landscout.sources.rte_odre_fr.open_safe_https", side_effect=error),
        pytest.raises(RteOdreDownloadError),
    ):
        download_rte_odre_dataset("sites", source_config, tmp_path)
assert first.path.read_bytes() == original_archive
assert metadata_path.read_bytes() == expired_metadata
assert metadata_path.read_bytes() != original_metadata
assert not list(tmp_path.glob("*.part"))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_failed_refresh_preserves_previous_valid_cache(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
    dataset_id = DATASET_IDS["sites"]
    with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(_feature_collection()),
        ],
    ):
        first = download_rte_odre_dataset("sites", source_config, tmp_path)
    original_archive = first.path.read_bytes()
    metadata_path = _metadata_path(tmp_path, dataset_id)
    original_metadata = metadata_path.read_bytes()
    _expire_cache(metadata_path)
    expired_metadata = metadata_path.read_bytes()
    metadata_url = build_rte_odre_metadata_url(source_config, "sites")
    error = HTTPError(metadata_url, 503, "Unavailable", hdrs=None, fp=None)

    with (
        patch("landscout.sources.rte_odre_fr.open_safe_https", side_effect=error),
        pytest.raises(RteOdreDownloadError),
    ):
        download_rte_odre_dataset("sites", source_config, tmp_path)

    assert first.path.read_bytes() == original_archive
    assert metadata_path.read_bytes() == expired_metadata
    assert metadata_path.read_bytes() != original_metadata
    assert not list(tmp_path.glob("*.part"))
```

### `test_corrupted_refresh_preserves_previous_valid_cache`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
dataset_id = DATASET_IDS["sites"]
original_archive = first.path.read_bytes()
metadata_path = _metadata_path(tmp_path, dataset_id)
_expire_cache(metadata_path)
expired_metadata = metadata_path.read_bytes()
```

**Action**

```python
with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(_feature_collection()),
        ],
    ):
        first = download_rte_odre_dataset("sites", source_config, tmp_path)
```

**Expected result**

```python
with (
        patch(
            "landscout.sources.rte_odre_fr.open_safe_https",
            side_effect=[
                _response(_metadata_content(dataset_id)),
                _response(b"{corrupted"),
            ],
        ),
        pytest.raises(RteOdreDownloadError),
    ):
        download_rte_odre_dataset("sites", source_config, tmp_path)
assert first.path.read_bytes() == original_archive
assert metadata_path.read_bytes() == expired_metadata
assert not list(tmp_path.glob("*.part"))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_corrupted_refresh_preserves_previous_valid_cache(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
    dataset_id = DATASET_IDS["sites"]
    with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(_feature_collection()),
        ],
    ):
        first = download_rte_odre_dataset("sites", source_config, tmp_path)
    original_archive = first.path.read_bytes()
    metadata_path = _metadata_path(tmp_path, dataset_id)
    _expire_cache(metadata_path)
    expired_metadata = metadata_path.read_bytes()

    with (
        patch(
            "landscout.sources.rte_odre_fr.open_safe_https",
            side_effect=[
                _response(_metadata_content(dataset_id)),
                _response(b"{corrupted"),
            ],
        ),
        pytest.raises(RteOdreDownloadError),
    ):
        download_rte_odre_dataset("sites", source_config, tmp_path)

    assert first.path.read_bytes() == original_archive
    assert metadata_path.read_bytes() == expired_metadata
    assert not list(tmp_path.glob("*.part"))
```

### `test_metadata_publication_failure_restores_previous_pair`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
dataset_id = DATASET_IDS["sites"]
metadata_path = _metadata_path(tmp_path, dataset_id)
_expire_cache(metadata_path)
old_archive = first.path.read_bytes()
old_metadata = metadata_path.read_bytes()
temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
original_replace = rte_odre_fr._replace_file
failure_injected = False
def fail_metadata_publication(source: Path, target: Path) -> None:
        nonlocal failure_injected
        if source == temporary_metadata and target == metadata_path:
            failure_injected = True
            raise PermissionError("simulated persistent metadata file lock")
        original_replace(source, target)
```

**Action**

```python
with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(_feature_collection()),
        ],
    ):
        first = download_rte_odre_dataset("sites", source_config, tmp_path)
```

**Expected result**

```python
with (
        patch(
            "landscout.sources.rte_odre_fr.open_safe_https",
            side_effect=[
                _response(_metadata_content(dataset_id)),
                _response(_feature_collection(all_null_geometry=True)),
            ],
        ),
        patch.object(
            rte_odre_fr,
            "_replace_file",
            side_effect=fail_metadata_publication,
        ),
        pytest.raises(RteOdreDownloadError),
    ):
        download_rte_odre_dataset("sites", source_config, tmp_path)
assert failure_injected
assert first.path.read_bytes() == old_archive
assert metadata_path.read_bytes() == old_metadata
assert not list(tmp_path.glob("*.part"))
assert not list(tmp_path.glob("*.bak"))
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_metadata_publication_failure_restores_previous_pair(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
    dataset_id = DATASET_IDS["sites"]
    with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(_feature_collection()),
        ],
    ):
        first = download_rte_odre_dataset("sites", source_config, tmp_path)
    metadata_path = _metadata_path(tmp_path, dataset_id)
    _expire_cache(metadata_path)
    old_archive = first.path.read_bytes()
    old_metadata = metadata_path.read_bytes()
    temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
    original_replace = rte_odre_fr._replace_file
    failure_injected = False

    def fail_metadata_publication(source: Path, target: Path) -> None:
        nonlocal failure_injected
        if source == temporary_metadata and target == metadata_path:
            failure_injected = True
            raise PermissionError("simulated persistent metadata file lock")
        original_replace(source, target)

    with (
        patch(
            "landscout.sources.rte_odre_fr.open_safe_https",
            side_effect=[
                _response(_metadata_content(dataset_id)),
                _response(_feature_collection(all_null_geometry=True)),
            ],
        ),
        patch.object(
            rte_odre_fr,
            "_replace_file",
            side_effect=fail_metadata_publication,
        ),
        pytest.raises(RteOdreDownloadError),
    ):
        download_rte_odre_dataset("sites", source_config, tmp_path)

    assert failure_injected
    assert first.path.read_bytes() == old_archive
    assert metadata_path.read_bytes() == old_metadata
    assert not list(tmp_path.glob("*.part"))
    assert not list(tmp_path.glob("*.bak"))
```

### `test_metadata_publication_failure_restores_previous_pair.fail_metadata_publication`

**Exact signature**

```python
def fail_metadata_publication(source: Path, target: Path) -> None:
```

**Purpose**

Private `test` helper for fail metadata publication; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `source == temporary_metadata and target == metadata_path`.
- Explicit raise expressions: `PermissionError('simulated persistent metadata file lock')`.

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

- callback/function object: `tests/unit/test_cadastre_fr.py::test_metadata_publication_failure_restores_previous_cache_pair` via `patch('landscout.sources.cadastre_fr._replace_file', side_effect=fail_metadata_publication)`.
- callback/function object: `tests/unit/test_cadastre_fr.py::test_first_metadata_publication_failure_leaves_no_half_pair` via `patch('landscout.sources.cadastre_fr._replace_file', side_effect=fail_metadata_publication)`.
- callback/function object: `tests/unit/test_ign_bdtopo_fr.py::test_metadata_publication_failure_restores_previous_cache_pair` via `patch.object(ign_bdtopo_fr, '_replace_file', side_effect=fail_metadata_publication)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_metadata_publication_failure_restores_previous_pair` via `patch.object(rte_odre_fr, '_replace_file', side_effect=fail_metadata_publication)`.

**Complete source-ordered implementation**

```python
def fail_metadata_publication(source: Path, target: Path) -> None:
        nonlocal failure_injected
        if source == temporary_metadata and target == metadata_path:
            failure_injected = True
            raise PermissionError("simulated persistent metadata file lock")
        original_replace(source, target)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_geojson_download_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `invalid_content`.

**Setup**

```python
dataset_id = DATASET_IDS["sites"]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with (
        patch(
            "landscout.sources.rte_odre_fr.open_safe_https",
            side_effect=[
                _response(_metadata_content(dataset_id)),
                _response(invalid_content),
            ],
        ),
        pytest.raises(RteOdreDownloadError),
    ):
        download_rte_odre_dataset("sites", source_config, tmp_path)
assert not list(tmp_path.glob("*.part"))
assert not list(tmp_path.glob("*.geojson"))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_invalid_geojson_download_is_rejected(
    tmp_path: Path,
    source_config: RteOdreSourceConfig,
    invalid_content: bytes,
) -> None:
    dataset_id = DATASET_IDS["sites"]
    with (
        patch(
            "landscout.sources.rte_odre_fr.open_safe_https",
            side_effect=[
                _response(_metadata_content(dataset_id)),
                _response(invalid_content),
            ],
        ),
        pytest.raises(RteOdreDownloadError),
    ):
        download_rte_odre_dataset("sites", source_config, tmp_path)

    assert not list(tmp_path.glob("*.part"))
    assert not list(tmp_path.glob("*.geojson"))
```

### `test_malformed_geojson_feature_or_geometry_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `feature`.

**Setup**

```python
path = tmp_path / "malformed.geojson"
path.write_text(
        json.dumps({"type": "FeatureCollection", "features": [feature]}),
        encoding="utf-8",
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RteOdreDownloadError):
        rte_odre_fr._validate_geojson(path)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_malformed_geojson_feature_or_geometry_is_rejected(
    tmp_path: Path,
    feature: object,
) -> None:
    path = tmp_path / "malformed.geojson"
    path.write_text(
        json.dumps({"type": "FeatureCollection", "features": [feature]}),
        encoding="utf-8",
    )

    with pytest.raises(RteOdreDownloadError):
        rte_odre_fr._validate_geojson(path)
```

### `test_standard_geojson_geometry_types_are_summarized`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
coordinate_types = {
        "Point": [1, 2],
        "MultiPoint": [[1, 2]],
        "LineString": [[1, 2], [2, 3]],
        "MultiLineString": [[[1, 2], [2, 3]]],
        "Polygon": [[[1, 2], [2, 3], [1, 2]]],
        "MultiPolygon": [[[[1, 2], [2, 3], [1, 2]]]],
    }
features = [
        {
            "type": "Feature",
            "geometry": {"type": geometry_type, "coordinates": coordinates},
        }
        for geometry_type, coordinates in coordinate_types.items()
    ]
features.extend(
        [
            {
                "type": "Feature",
                "geometry": {"type": "GeometryCollection", "geometries": []},
            },
            {"type": "Feature", "geometry": None},
        ]
    )
path = tmp_path / "valid.geojson"
path.write_text(
        json.dumps({"type": "FeatureCollection", "features": features}),
        encoding="utf-8",
    )
summary = rte_odre_fr._validate_geojson(path)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert summary.feature_count == 8
assert summary.null_geometry_count == 1
assert summary.non_null_geometry_count == 7
assert summary.geometry_types == tuple(sorted((*coordinate_types, "GeometryCollection")))
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_standard_geojson_geometry_types_are_summarized(tmp_path: Path) -> None:
    coordinate_types = {
        "Point": [1, 2],
        "MultiPoint": [[1, 2]],
        "LineString": [[1, 2], [2, 3]],
        "MultiLineString": [[[1, 2], [2, 3]]],
        "Polygon": [[[1, 2], [2, 3], [1, 2]]],
        "MultiPolygon": [[[[1, 2], [2, 3], [1, 2]]]],
    }
    features = [
        {
            "type": "Feature",
            "geometry": {"type": geometry_type, "coordinates": coordinates},
        }
        for geometry_type, coordinates in coordinate_types.items()
    ]
    features.extend(
        [
            {
                "type": "Feature",
                "geometry": {"type": "GeometryCollection", "geometries": []},
            },
            {"type": "Feature", "geometry": None},
        ]
    )
    path = tmp_path / "valid.geojson"
    path.write_text(
        json.dumps({"type": "FeatureCollection", "features": features}),
        encoding="utf-8",
    )

    summary = rte_odre_fr._validate_geojson(path)

    assert summary.feature_count == 8
    assert summary.null_geometry_count == 1
    assert summary.non_null_geometry_count == 7
    assert summary.geometry_types == tuple(sorted((*coordinate_types, "GeometryCollection")))
```

### `test_point_requires_a_finite_numeric_position`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `coordinates`.

**Setup**

```python
path = tmp_path / "bad-point.geojson"
path.write_text(
        json.dumps(
            {
                "type": "FeatureCollection",
                "features": [
                    {
                        "type": "Feature",
                        "geometry": {"type": "Point", "coordinates": coordinates},
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RteOdreDownloadError, match="coordinate|Point|finite"):
        rte_odre_fr._validate_geojson(path)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_point_requires_a_finite_numeric_position(
    tmp_path: Path,
    coordinates: object,
) -> None:
    path = tmp_path / "bad-point.geojson"
    path.write_text(
        json.dumps(
            {
                "type": "FeatureCollection",
                "features": [
                    {
                        "type": "Feature",
                        "geometry": {"type": "Point", "coordinates": coordinates},
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    with pytest.raises(RteOdreDownloadError, match="coordinate|Point|finite"):
        rte_odre_fr._validate_geojson(path)
```

### `test_nested_coordinate_geometries_reject_obvious_invalid_structure`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `coordinates`, `geometry_type`.

**Setup**

```python
path = tmp_path / "bad-nested.geojson"
path.write_text(
        json.dumps(
            {
                "type": "FeatureCollection",
                "features": [
                    {
                        "type": "Feature",
                        "geometry": {
                            "type": geometry_type,
                            "coordinates": coordinates,
                        },
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RteOdreDownloadError, match="coordinate|structure|finite"):
        rte_odre_fr._validate_geojson(path)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_nested_coordinate_geometries_reject_obvious_invalid_structure(
    tmp_path: Path,
    geometry_type: str,
    coordinates: object,
) -> None:
    path = tmp_path / "bad-nested.geojson"
    path.write_text(
        json.dumps(
            {
                "type": "FeatureCollection",
                "features": [
                    {
                        "type": "Feature",
                        "geometry": {
                            "type": geometry_type,
                            "coordinates": coordinates,
                        },
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    with pytest.raises(RteOdreDownloadError, match="coordinate|structure|finite"):
        rte_odre_fr._validate_geojson(path)
```

### `test_geometry_collection_members_are_validated_recursively`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
path = tmp_path / "bad-collection.geojson"
path.write_text(
        json.dumps(
            {
                "type": "FeatureCollection",
                "features": [
                    {
                        "type": "Feature",
                        "geometry": {
                            "type": "GeometryCollection",
                            "geometries": [
                                {"type": "Point", "coordinates": None}
                            ],
                        },
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RteOdreDownloadError, match="coordinate|Point"):
        rte_odre_fr._validate_geojson(path)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_geometry_collection_members_are_validated_recursively(tmp_path: Path) -> None:
    path = tmp_path / "bad-collection.geojson"
    path.write_text(
        json.dumps(
            {
                "type": "FeatureCollection",
                "features": [
                    {
                        "type": "Feature",
                        "geometry": {
                            "type": "GeometryCollection",
                            "geometries": [
                                {"type": "Point", "coordinates": None}
                            ],
                        },
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    with pytest.raises(RteOdreDownloadError, match="coordinate|Point"):
        rte_odre_fr._validate_geojson(path)
```

### `test_null_feature_geometries_are_accepted`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
dataset_id = DATASET_IDS["sites"]
export_content = _feature_collection(all_null_geometry=True)
```

**Action**

```python
with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(export_content),
        ],
    ):
        result = download_rte_odre_dataset("sites", source_config, tmp_path)
```

**Expected result**

```python
assert result.path.is_file()
assert result.dataset_metadata.geometry_precision_status == "MISSING"
assert result.export_summary == RteOdreExportSummary(
        feature_count=2,
        null_geometry_count=2,
        non_null_geometry_count=0,
        geometry_types=(),
    )
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_null_feature_geometries_are_accepted(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
    dataset_id = DATASET_IDS["sites"]
    export_content = _feature_collection(all_null_geometry=True)
    with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(export_content),
        ],
    ):
        result = download_rte_odre_dataset("sites", source_config, tmp_path)

    assert result.path.is_file()
    assert result.dataset_metadata.geometry_precision_status == "MISSING"
    assert result.export_summary == RteOdreExportSummary(
        feature_count=2,
        null_geometry_count=2,
        non_null_geometry_count=0,
        geometry_types=(),
    )
```

### `test_lineage_sidecar_records_integrity`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
dataset_id = DATASET_IDS["sites"]
export_content = _feature_collection()
metadata_path = _metadata_path(tmp_path, dataset_id)
lineage = json.loads(metadata_path.read_text(encoding="utf-8"))
```

**Action**

```python
with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(export_content),
        ],
    ):
        result = download_rte_odre_dataset("sites", source_config, tmp_path)
```

**Expected result**

```python
assert lineage["source_url"] == result.source_url
assert lineage["file_size"] == len(export_content)
assert lineage["sha256"] == sha256(export_content).hexdigest()
assert lineage["dataset_metadata"]["publisher"] == "RTE"
assert lineage["export_summary"] == {
        "feature_count": 2,
        "geometry_types": ["Point"],
        "non_null_geometry_count": 1,
        "null_geometry_count": 1,
    }
assert (
        lineage["export_summary"]["null_geometry_count"]
        + lineage["export_summary"]["non_null_geometry_count"]
        == lineage["export_summary"]["feature_count"]
    )
assert "path" not in lineage
assert "cache_hit" not in lineage
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_lineage_sidecar_records_integrity(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
    dataset_id = DATASET_IDS["sites"]
    export_content = _feature_collection()
    with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(export_content),
        ],
    ):
        result = download_rte_odre_dataset("sites", source_config, tmp_path)

    metadata_path = _metadata_path(tmp_path, dataset_id)
    lineage = json.loads(metadata_path.read_text(encoding="utf-8"))
    assert lineage["source_url"] == result.source_url
    assert lineage["file_size"] == len(export_content)
    assert lineage["sha256"] == sha256(export_content).hexdigest()
    assert lineage["dataset_metadata"]["publisher"] == "RTE"
    assert lineage["export_summary"] == {
        "feature_count": 2,
        "geometry_types": ["Point"],
        "non_null_geometry_count": 1,
        "null_geometry_count": 1,
    }
    assert (
        lineage["export_summary"]["null_geometry_count"]
        + lineage["export_summary"]["non_null_geometry_count"]
        == lineage["export_summary"]["feature_count"]
    )
    assert "path" not in lineage
    assert "cache_hit" not in lineage
```

### `test_invalid_cached_record_count_invalidates_cache`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `cached_records_count`.

**Setup**

```python
dataset_id = DATASET_IDS["sites"]
valid_content = _feature_collection()
metadata_path = _metadata_path(tmp_path, dataset_id)
lineage = json.loads(metadata_path.read_text(encoding="utf-8"))
lineage["dataset_metadata"]["records_count"] = cached_records_count
metadata_path.write_text(json.dumps(lineage), encoding="utf-8")
```

**Action**

```python
with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(valid_content),
        ],
    ):
        first = download_rte_odre_dataset("sites", source_config, tmp_path)
with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(valid_content),
        ],
    ) as opener:
        refreshed = download_rte_odre_dataset("sites", source_config, tmp_path)
```

**Expected result**

```python
assert opener.call_count == 2
assert refreshed.cache_hit is False
assert refreshed.path.read_bytes() == first.path.read_bytes()
assert refreshed.dataset_metadata.records_count == 2
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_invalid_cached_record_count_invalidates_cache(
    tmp_path: Path,
    source_config: RteOdreSourceConfig,
    cached_records_count: int,
) -> None:
    dataset_id = DATASET_IDS["sites"]
    valid_content = _feature_collection()
    with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(valid_content),
        ],
    ):
        first = download_rte_odre_dataset("sites", source_config, tmp_path)
    metadata_path = _metadata_path(tmp_path, dataset_id)
    lineage = json.loads(metadata_path.read_text(encoding="utf-8"))
    lineage["dataset_metadata"]["records_count"] = cached_records_count
    metadata_path.write_text(json.dumps(lineage), encoding="utf-8")

    with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(valid_content),
        ],
    ) as opener:
        refreshed = download_rte_odre_dataset("sites", source_config, tmp_path)

    assert opener.call_count == 2
    assert refreshed.cache_hit is False
    assert refreshed.path.read_bytes() == first.path.read_bytes()
    assert refreshed.dataset_metadata.records_count == 2
```

### `test_cached_export_summary_mismatch_invalidates_cache`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
dataset_id = DATASET_IDS["sites"]
valid_content = _feature_collection()
metadata_path = _metadata_path(tmp_path, dataset_id)
lineage = json.loads(metadata_path.read_text(encoding="utf-8"))
lineage["export_summary"]["null_geometry_count"] = 2
lineage["export_summary"]["non_null_geometry_count"] = 0
lineage["export_summary"]["geometry_types"] = []
metadata_path.write_text(json.dumps(lineage), encoding="utf-8")
```

**Action**

```python
with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(valid_content),
        ],
    ):
        download_rte_odre_dataset("sites", source_config, tmp_path)
with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(valid_content),
        ],
    ) as opener:
        refreshed = download_rte_odre_dataset("sites", source_config, tmp_path)
```

**Expected result**

```python
assert opener.call_count == 2
assert refreshed.cache_hit is False
assert refreshed.export_summary.geometry_types == ("Point",)
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_cached_export_summary_mismatch_invalidates_cache(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
    dataset_id = DATASET_IDS["sites"]
    valid_content = _feature_collection()
    with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(valid_content),
        ],
    ):
        download_rte_odre_dataset("sites", source_config, tmp_path)
    metadata_path = _metadata_path(tmp_path, dataset_id)
    lineage = json.loads(metadata_path.read_text(encoding="utf-8"))
    lineage["export_summary"]["null_geometry_count"] = 2
    lineage["export_summary"]["non_null_geometry_count"] = 0
    lineage["export_summary"]["geometry_types"] = []
    metadata_path.write_text(json.dumps(lineage), encoding="utf-8")

    with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(valid_content),
        ],
    ) as opener:
        refreshed = download_rte_odre_dataset("sites", source_config, tmp_path)

    assert opener.call_count == 2
    assert refreshed.cache_hit is False
    assert refreshed.export_summary.geometry_types == ("Point",)
```

### `test_corrupted_cached_export_triggers_refresh`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
dataset_id = DATASET_IDS["sites"]
valid_content = _feature_collection()
first.path.write_bytes(b"corrupted")
```

**Action**

```python
with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(valid_content),
        ],
    ):
        first = download_rte_odre_dataset("sites", source_config, tmp_path)
with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(valid_content),
        ],
    ) as opener:
        refreshed = download_rte_odre_dataset("sites", source_config, tmp_path)
```

**Expected result**

```python
assert opener.call_count == 2
assert refreshed.cache_hit is False
assert refreshed.path.read_bytes() == valid_content
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_corrupted_cached_export_triggers_refresh(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
    dataset_id = DATASET_IDS["sites"]
    valid_content = _feature_collection()
    with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(valid_content),
        ],
    ):
        first = download_rte_odre_dataset("sites", source_config, tmp_path)
    first.path.write_bytes(b"corrupted")

    with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(valid_content),
        ],
    ) as opener:
        refreshed = download_rte_odre_dataset("sites", source_config, tmp_path)

    assert opener.call_count == 2
    assert refreshed.cache_hit is False
    assert refreshed.path.read_bytes() == valid_content
```

### `test_double_failure_preserves_recovery_and_next_run_uses_zero_network`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
dataset_id = DATASET_IDS["sites"]
metadata_path = _metadata_path(tmp_path, dataset_id)
_expire_cache(metadata_path)
old_archive = first.path.read_bytes()
old_metadata = metadata_path.read_bytes()
temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
archive_backup = first.path.with_suffix(f"{first.path.suffix}.bak")
metadata_backup = metadata_path.with_suffix(f"{metadata_path.suffix}.bak")
original_replace = rte_odre_fr._replace_file
def fail_publication_and_rollback(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("publication failed")
        if source == archive_backup and target == first.path:
            raise OSError("rollback failed")
        original_replace(source, target)
def response_for_url(url: str, *args: object, **kwargs: object) -> io.BytesIO:
        if url.endswith("/exports/geojson"):
            return _response(_feature_collection())
        return _response(_metadata_content(dataset_id))
monkeypatch.setattr(rte_odre_fr, "_replace_file", fail_publication_and_rollback)
monkeypatch.setattr(rte_odre_fr, "open_safe_https", response_for_url)
archive_recovery = archive_backup.read_bytes()
metadata_recovery = metadata_backup.read_bytes()
network_calls: list[str] = []
def fail_network(url: str, *args: object, **kwargs: object) -> io.BytesIO:
        network_calls.append(url)
        raise AssertionError("manual recovery state must fail before HTTP")
monkeypatch.setattr(rte_odre_fr, "open_safe_https", fail_network)
```

**Action**

```python
with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(_feature_collection()),
        ],
    ):
        first = download_rte_odre_dataset("sites", source_config, tmp_path)
```

**Expected result**

```python
with pytest.raises(RteOdreDownloadError, match="rollback"):
        download_rte_odre_dataset("sites", source_config, tmp_path)
assert archive_backup.read_bytes() == old_archive
assert metadata_backup.read_bytes() == old_metadata
with pytest.raises(RteOdreDownloadError, match="backup|recovery|manual"):
        download_rte_odre_dataset("sites", source_config, tmp_path)
assert network_calls == []
assert archive_backup.read_bytes() == archive_recovery
assert metadata_backup.read_bytes() == metadata_recovery
```

**Regression protected**

Prevents failed cache publication and failed rollback from deleting the last recoverable backup bytes.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_double_failure_preserves_recovery_and_next_run_uses_zero_network(
    tmp_path: Path,
    source_config: RteOdreSourceConfig,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    dataset_id = DATASET_IDS["sites"]
    with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(_feature_collection()),
        ],
    ):
        first = download_rte_odre_dataset("sites", source_config, tmp_path)
    metadata_path = _metadata_path(tmp_path, dataset_id)
    _expire_cache(metadata_path)
    old_archive = first.path.read_bytes()
    old_metadata = metadata_path.read_bytes()
    temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
    archive_backup = first.path.with_suffix(f"{first.path.suffix}.bak")
    metadata_backup = metadata_path.with_suffix(f"{metadata_path.suffix}.bak")
    original_replace = rte_odre_fr._replace_file

    def fail_publication_and_rollback(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("publication failed")
        if source == archive_backup and target == first.path:
            raise OSError("rollback failed")
        original_replace(source, target)

    def response_for_url(url: str, *args: object, **kwargs: object) -> io.BytesIO:
        if url.endswith("/exports/geojson"):
            return _response(_feature_collection())
        return _response(_metadata_content(dataset_id))

    monkeypatch.setattr(rte_odre_fr, "_replace_file", fail_publication_and_rollback)
    monkeypatch.setattr(rte_odre_fr, "open_safe_https", response_for_url)

    with pytest.raises(RteOdreDownloadError, match="rollback"):
        download_rte_odre_dataset("sites", source_config, tmp_path)

    assert archive_backup.read_bytes() == old_archive
    assert metadata_backup.read_bytes() == old_metadata
    archive_recovery = archive_backup.read_bytes()
    metadata_recovery = metadata_backup.read_bytes()
    network_calls: list[str] = []

    def fail_network(url: str, *args: object, **kwargs: object) -> io.BytesIO:
        network_calls.append(url)
        raise AssertionError("manual recovery state must fail before HTTP")

    monkeypatch.setattr(rte_odre_fr, "open_safe_https", fail_network)

    with pytest.raises(RteOdreDownloadError, match="backup|recovery|manual"):
        download_rte_odre_dataset("sites", source_config, tmp_path)

    assert network_calls == []
    assert archive_backup.read_bytes() == archive_recovery
    assert metadata_backup.read_bytes() == metadata_recovery
```

### `test_double_failure_preserves_recovery_and_next_run_uses_zero_network.fail_publication_and_rollback`

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
- Explicit raise expressions: `OSError('publication failed')`, `OSError('rollback failed')`.

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

- callback/function object: `tests/unit/test_cadastre_fr.py::test_publication_and_rollback_failure_preserves_recovery_backup` via `patch.object(cadastre_fr, '_replace_file', side_effect=fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_cadastre_fr.py::test_next_run_after_double_failure_preserves_recovery_before_network` via `patch.object(cadastre_fr, '_replace_file', side_effect=fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_cadastre_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `monkeypatch.setattr(cadastre_fr, '_replace_file', fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_publication_and_rollback_failure_preserves_exact_recovery_backups` via `monkeypatch.setattr(gpu, '_replace_file', fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `monkeypatch.setattr(gpu, '_replace_file', fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_ign_bdtopo_fr.py::test_publication_and_rollback_failure_preserves_exact_recovery_backups` via `patch.object(ign_bdtopo_fr, '_replace_file', side_effect=fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_ign_bdtopo_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `patch.object(ign_bdtopo_fr, '_replace_file', side_effect=fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_rollback_failure_preserves_recovery_material` via `monkeypatch.setattr(inpn, '_replace_file', fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `monkeypatch.setattr(rte_odre_fr, '_replace_file', fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `monkeypatch.setattr(rte_odre_fr, '_replace_file', fail_publication_and_rollback)`.

**Complete source-ordered implementation**

```python
def fail_publication_and_rollback(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("publication failed")
        if source == archive_backup and target == first.path:
            raise OSError("rollback failed")
        original_replace(source, target)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_double_failure_preserves_recovery_and_next_run_uses_zero_network.response_for_url`

**Exact signature**

```python
def response_for_url(url: str, *args: object, **kwargs: object) -> io.BytesIO:
```

**Purpose**

Private `test` helper for response for url; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `io.BytesIO`.
- Every observed return expression is reproduced without truncation:
```python
_response(_metadata_content(dataset_id))

_response(_feature_collection())
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

- callback/function object: `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `monkeypatch.setattr(rte_odre_fr, 'open_safe_https', response_for_url)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `monkeypatch.setattr(rte_odre_fr, 'open_safe_https', response_for_url)`.

**Complete source-ordered implementation**

```python
def response_for_url(url: str, *args: object, **kwargs: object) -> io.BytesIO:
        if url.endswith("/exports/geojson"):
            return _response(_feature_collection())
        return _response(_metadata_content(dataset_id))
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_double_failure_preserves_recovery_and_next_run_uses_zero_network.fail_network`

**Exact signature**

```python
def fail_network(url: str, *args: object, **kwargs: object) -> io.BytesIO:
```

**Purpose**

Private `test` helper for fail network; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `io.BytesIO`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `AssertionError('manual recovery state must fail before HTTP')`.

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

- callback/function object: `tests/unit/test_cadastre_fr.py::test_broken_recovery_symlink_is_rejected_before_network` via `monkeypatch.setattr(cadastre_fr, 'open_safe_https', fail_network)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_mutated_loaded_api_origin_is_rejected_before_discovery_network` via `monkeypatch.setattr(gpu, 'open_safe_https', fail_network)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_download_rejects_forged_written_file_provenance_before_network` via `monkeypatch.setattr(gpu, 'open_safe_https', fail_network)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_stale_recovery_backup_rejects_cache_before_network` via `monkeypatch.setattr(gpu, 'open_safe_https', fail_network)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_mutated_loaded_api_origin_is_rejected_before_metadata_network` via `monkeypatch.setattr(rte_odre_fr, 'open_safe_https', fail_network)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `monkeypatch.setattr(rte_odre_fr, 'open_safe_https', fail_network)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_broken_recovery_symlink_rejects_rte_before_network` via `monkeypatch.setattr(rte_odre_fr, 'open_safe_https', fail_network)`.

**Complete source-ordered implementation**

```python
def fail_network(url: str, *args: object, **kwargs: object) -> io.BytesIO:
        network_calls.append(url)
        raise AssertionError("manual recovery state must fail before HTTP")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_temporary_link_or_junction_cannot_modify_target_before_rte_network`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `link_kind`, `temporary_role`.

**Setup**

```python
dataset_id = DATASET_IDS["sites"]
archive_path = tmp_path / f"{dataset_id}.geojson"
metadata_path = _metadata_path(tmp_path, dataset_id)
temporary_paths = {
        "archive": archive_path.with_suffix(f"{archive_path.suffix}.part"),
        "metadata": metadata_path.with_suffix(f"{metadata_path.suffix}.part"),
    }
unsafe_path = temporary_paths[temporary_role]
sentinel = tmp_path / "do-not-overwrite.txt"
sentinel_bytes = b"irreplaceable RTE sentinel"
sentinel.write_bytes(sentinel_bytes)
original_is_symlink = Path.is_symlink
original_is_junction = Path.is_junction
original_open = Path.open
def simulated_is_symlink(path: Path) -> bool:
        return (
            link_kind == "symlink" and path == unsafe_path
        ) or original_is_symlink(path)
def simulated_is_junction(path: Path) -> bool:
        return (
            link_kind == "junction" and path == unsafe_path
        ) or original_is_junction(path)
def simulated_symlink_open(
        path: Path, *args: object, **kwargs: object
    ) -> object:
        if path == unsafe_path:
            return original_open(sentinel, *args, **kwargs)
        return original_open(path, *args, **kwargs)
network_calls = 0
def record_network(url: str, *args: object, **kwargs: object) -> io.BytesIO:
        nonlocal network_calls
        network_calls += 1
        if url.endswith("/exports/geojson"):
            return _response(_feature_collection())
        return _response(_metadata_content(dataset_id))
monkeypatch.setattr(Path, "is_symlink", simulated_is_symlink)
monkeypatch.setattr(Path, "is_junction", simulated_is_junction)
monkeypatch.setattr(Path, "open", simulated_symlink_open)
monkeypatch.setattr(rte_odre_fr, "open_safe_https", record_network)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RteOdreDownloadError, match="temporary|link|cache"):
        download_rte_odre_dataset("sites", source_config, tmp_path)
assert network_calls == 0
assert sentinel.read_bytes() == sentinel_bytes
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_temporary_link_or_junction_cannot_modify_target_before_rte_network(
    tmp_path: Path,
    source_config: RteOdreSourceConfig,
    monkeypatch: pytest.MonkeyPatch,
    temporary_role: str,
    link_kind: str,
) -> None:
    dataset_id = DATASET_IDS["sites"]
    archive_path = tmp_path / f"{dataset_id}.geojson"
    metadata_path = _metadata_path(tmp_path, dataset_id)
    temporary_paths = {
        "archive": archive_path.with_suffix(f"{archive_path.suffix}.part"),
        "metadata": metadata_path.with_suffix(f"{metadata_path.suffix}.part"),
    }
    unsafe_path = temporary_paths[temporary_role]
    sentinel = tmp_path / "do-not-overwrite.txt"
    sentinel_bytes = b"irreplaceable RTE sentinel"
    sentinel.write_bytes(sentinel_bytes)
    original_is_symlink = Path.is_symlink
    original_is_junction = Path.is_junction
    original_open = Path.open

    def simulated_is_symlink(path: Path) -> bool:
        return (
            link_kind == "symlink" and path == unsafe_path
        ) or original_is_symlink(path)

    def simulated_is_junction(path: Path) -> bool:
        return (
            link_kind == "junction" and path == unsafe_path
        ) or original_is_junction(path)

    def simulated_symlink_open(
        path: Path, *args: object, **kwargs: object
    ) -> object:
        if path == unsafe_path:
            return original_open(sentinel, *args, **kwargs)
        return original_open(path, *args, **kwargs)

    network_calls = 0

    def record_network(url: str, *args: object, **kwargs: object) -> io.BytesIO:
        nonlocal network_calls
        network_calls += 1
        if url.endswith("/exports/geojson"):
            return _response(_feature_collection())
        return _response(_metadata_content(dataset_id))

    monkeypatch.setattr(Path, "is_symlink", simulated_is_symlink)
    monkeypatch.setattr(Path, "is_junction", simulated_is_junction)
    monkeypatch.setattr(Path, "open", simulated_symlink_open)
    monkeypatch.setattr(rte_odre_fr, "open_safe_https", record_network)

    with pytest.raises(RteOdreDownloadError, match="temporary|link|cache"):
        download_rte_odre_dataset("sites", source_config, tmp_path)

    assert network_calls == 0
    assert sentinel.read_bytes() == sentinel_bytes
```

### `test_temporary_link_or_junction_cannot_modify_target_before_rte_network.simulated_is_symlink`

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
link_kind == 'symlink' and path == unsafe_path or original_is_symlink(path)
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

- callback/function object: `tests/unit/test_cadastre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_network` via `monkeypatch.setattr(Path, 'is_symlink', simulated_is_symlink)`.
- callback/function object: `tests/unit/test_cadastre_fr.py::test_broken_recovery_symlink_is_rejected_before_network` via `monkeypatch.setattr(Path, 'is_symlink', simulated_is_symlink)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_preexisting_temporary_archive_symlink_cannot_modify_target` via `monkeypatch.setattr(Path, 'is_symlink', simulated_is_symlink)`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_broken_download_recovery_symlink_is_rejected` via `monkeypatch.setattr(Path, 'is_symlink', simulated_is_symlink)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_rte_network` via `monkeypatch.setattr(Path, 'is_symlink', simulated_is_symlink)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_broken_recovery_symlink_rejects_rte_before_network` via `monkeypatch.setattr(Path, 'is_symlink', simulated_is_symlink)`.

**Complete source-ordered implementation**

```python
def simulated_is_symlink(path: Path) -> bool:
        return (
            link_kind == "symlink" and path == unsafe_path
        ) or original_is_symlink(path)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_temporary_link_or_junction_cannot_modify_target_before_rte_network.simulated_is_junction`

**Exact signature**

```python
def simulated_is_junction(path: Path) -> bool:
```

**Purpose**

Private `test` helper for simulated is junction; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
link_kind == 'junction' and path == unsafe_path or original_is_junction(path)
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

- callback/function object: `tests/unit/test_cadastre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_network` via `monkeypatch.setattr(Path, 'is_junction', simulated_is_junction)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_rte_network` via `monkeypatch.setattr(Path, 'is_junction', simulated_is_junction)`.

**Complete source-ordered implementation**

```python
def simulated_is_junction(path: Path) -> bool:
        return (
            link_kind == "junction" and path == unsafe_path
        ) or original_is_junction(path)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_temporary_link_or_junction_cannot_modify_target_before_rte_network.simulated_symlink_open`

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- callback/function object: `tests/unit/test_cadastre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_network` via `monkeypatch.setattr(Path, 'open', simulated_symlink_open)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_preexisting_temporary_archive_symlink_cannot_modify_target` via `monkeypatch.setattr(Path, 'open', simulated_symlink_open)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_rte_network` via `monkeypatch.setattr(Path, 'open', simulated_symlink_open)`.

**Complete source-ordered implementation**

```python
def simulated_symlink_open(
        path: Path, *args: object, **kwargs: object
    ) -> object:
        if path == unsafe_path:
            return original_open(sentinel, *args, **kwargs)
        return original_open(path, *args, **kwargs)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_temporary_link_or_junction_cannot_modify_target_before_rte_network.record_network`

**Exact signature**

```python
def record_network(url: str, *args: object, **kwargs: object) -> io.BytesIO:
```

**Purpose**

Private `test` helper for record network; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `io.BytesIO`.
- Every observed return expression is reproduced without truncation:
```python
_response(_metadata_content(dataset_id))

_response(_feature_collection())
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

- callback/function object: `tests/unit/test_cadastre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_network` via `monkeypatch.setattr(cadastre_fr, 'open_safe_https', record_network)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_preexisting_temporary_archive_symlink_cannot_modify_target` via `monkeypatch.setattr(gpu, 'open_safe_https', record_network)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_rte_network` via `monkeypatch.setattr(rte_odre_fr, 'open_safe_https', record_network)`.

**Complete source-ordered implementation**

```python
def record_network(url: str, *args: object, **kwargs: object) -> io.BytesIO:
        nonlocal network_calls
        network_calls += 1
        if url.endswith("/exports/geojson"):
            return _response(_feature_collection())
        return _response(_metadata_content(dataset_id))
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_broken_recovery_symlink_rejects_rte_before_network`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
dataset_id = DATASET_IDS["sites"]
archive_path = tmp_path / f"{dataset_id}.geojson"
recovery_path = archive_path.with_suffix(f"{archive_path.suffix}.bak")
original_is_symlink = Path.is_symlink
def simulated_is_symlink(path: Path) -> bool:
        return path == recovery_path or original_is_symlink(path)
network_calls: list[str] = []
def fail_network(url: str, *args: object, **kwargs: object) -> io.BytesIO:
        network_calls.append(url)
        raise AssertionError("broken recovery link must fail before HTTP")
monkeypatch.setattr(Path, "is_symlink", simulated_is_symlink)
monkeypatch.setattr(rte_odre_fr, "open_safe_https", fail_network)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RteOdreDownloadError, match="backup|recovery|manual"):
        download_rte_odre_dataset("sites", source_config, tmp_path)
assert network_calls == []
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_broken_recovery_symlink_rejects_rte_before_network(
    tmp_path: Path,
    source_config: RteOdreSourceConfig,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    dataset_id = DATASET_IDS["sites"]
    archive_path = tmp_path / f"{dataset_id}.geojson"
    recovery_path = archive_path.with_suffix(f"{archive_path.suffix}.bak")
    original_is_symlink = Path.is_symlink

    def simulated_is_symlink(path: Path) -> bool:
        return path == recovery_path or original_is_symlink(path)

    network_calls: list[str] = []

    def fail_network(url: str, *args: object, **kwargs: object) -> io.BytesIO:
        network_calls.append(url)
        raise AssertionError("broken recovery link must fail before HTTP")

    monkeypatch.setattr(Path, "is_symlink", simulated_is_symlink)
    monkeypatch.setattr(rte_odre_fr, "open_safe_https", fail_network)

    with pytest.raises(RteOdreDownloadError, match="backup|recovery|manual"):
        download_rte_odre_dataset("sites", source_config, tmp_path)

    assert network_calls == []
```

### `test_broken_recovery_symlink_rejects_rte_before_network.simulated_is_symlink`

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
path == recovery_path or original_is_symlink(path)
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

- callback/function object: `tests/unit/test_cadastre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_network` via `monkeypatch.setattr(Path, 'is_symlink', simulated_is_symlink)`.
- callback/function object: `tests/unit/test_cadastre_fr.py::test_broken_recovery_symlink_is_rejected_before_network` via `monkeypatch.setattr(Path, 'is_symlink', simulated_is_symlink)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_preexisting_temporary_archive_symlink_cannot_modify_target` via `monkeypatch.setattr(Path, 'is_symlink', simulated_is_symlink)`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_broken_download_recovery_symlink_is_rejected` via `monkeypatch.setattr(Path, 'is_symlink', simulated_is_symlink)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_rte_network` via `monkeypatch.setattr(Path, 'is_symlink', simulated_is_symlink)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_broken_recovery_symlink_rejects_rte_before_network` via `monkeypatch.setattr(Path, 'is_symlink', simulated_is_symlink)`.

**Complete source-ordered implementation**

```python
def simulated_is_symlink(path: Path) -> bool:
        return path == recovery_path or original_is_symlink(path)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_broken_recovery_symlink_rejects_rte_before_network.fail_network`

**Exact signature**

```python
def fail_network(url: str, *args: object, **kwargs: object) -> io.BytesIO:
```

**Purpose**

Private `test` helper for fail network; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `io.BytesIO`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `AssertionError('broken recovery link must fail before HTTP')`.

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

- callback/function object: `tests/unit/test_cadastre_fr.py::test_broken_recovery_symlink_is_rejected_before_network` via `monkeypatch.setattr(cadastre_fr, 'open_safe_https', fail_network)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_mutated_loaded_api_origin_is_rejected_before_discovery_network` via `monkeypatch.setattr(gpu, 'open_safe_https', fail_network)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_download_rejects_forged_written_file_provenance_before_network` via `monkeypatch.setattr(gpu, 'open_safe_https', fail_network)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_stale_recovery_backup_rejects_cache_before_network` via `monkeypatch.setattr(gpu, 'open_safe_https', fail_network)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_mutated_loaded_api_origin_is_rejected_before_metadata_network` via `monkeypatch.setattr(rte_odre_fr, 'open_safe_https', fail_network)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `monkeypatch.setattr(rte_odre_fr, 'open_safe_https', fail_network)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_broken_recovery_symlink_rejects_rte_before_network` via `monkeypatch.setattr(rte_odre_fr, 'open_safe_https', fail_network)`.

**Complete source-ordered implementation**

```python
def fail_network(url: str, *args: object, **kwargs: object) -> io.BytesIO:
        network_calls.append(url)
        raise AssertionError("broken recovery link must fail before HTTP")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
dataset_id = DATASET_IDS["sites"]
metadata_path = _metadata_path(tmp_path, dataset_id)
_expire_cache(metadata_path)
old_archive = first.path.read_bytes()
old_metadata = metadata_path.read_bytes()
temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
archive_backup = first.path.with_suffix(f"{first.path.suffix}.bak")
metadata_backup = metadata_path.with_suffix(f"{metadata_path.suffix}.bak")
original_replace = rte_odre_fr._replace_file
original_unlink = Path.unlink
rollback_failed = False
def fail_publication_and_rollback(source: Path, target: Path) -> None:
        nonlocal rollback_failed
        if source == temporary_metadata and target == metadata_path:
            raise OSError("publication failed")
        if source == archive_backup and target == first.path:
            rollback_failed = True
            raise OSError("rollback failed")
        original_replace(source, target)
def fail_temporary_cleanup(path: Path, *, missing_ok: bool = False) -> None:
        if rollback_failed and path == temporary_metadata:
            raise PermissionError("temporary cleanup failed")
        original_unlink(path, missing_ok=missing_ok)
def response_for_url(url: str, *args: object, **kwargs: object) -> io.BytesIO:
        if url.endswith("/exports/geojson"):
            return _response(_feature_collection())
        return _response(_metadata_content(dataset_id))
monkeypatch.setattr(rte_odre_fr, "open_safe_https", response_for_url)
monkeypatch.setattr(rte_odre_fr, "_replace_file", fail_publication_and_rollback)
monkeypatch.setattr(Path, "unlink", fail_temporary_cleanup)
```

**Action**

```python
with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(_feature_collection()),
        ],
    ):
        first = download_rte_odre_dataset("sites", source_config, tmp_path)
```

**Expected result**

```python
with pytest.raises(RteOdreDownloadError, match="rollback"):
        download_rte_odre_dataset("sites", source_config, tmp_path)
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
def test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error(
    tmp_path: Path,
    source_config: RteOdreSourceConfig,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    dataset_id = DATASET_IDS["sites"]
    with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(_feature_collection()),
        ],
    ):
        first = download_rte_odre_dataset("sites", source_config, tmp_path)
    metadata_path = _metadata_path(tmp_path, dataset_id)
    _expire_cache(metadata_path)
    old_archive = first.path.read_bytes()
    old_metadata = metadata_path.read_bytes()
    temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
    archive_backup = first.path.with_suffix(f"{first.path.suffix}.bak")
    metadata_backup = metadata_path.with_suffix(f"{metadata_path.suffix}.bak")
    original_replace = rte_odre_fr._replace_file
    original_unlink = Path.unlink
    rollback_failed = False

    def fail_publication_and_rollback(source: Path, target: Path) -> None:
        nonlocal rollback_failed
        if source == temporary_metadata and target == metadata_path:
            raise OSError("publication failed")
        if source == archive_backup and target == first.path:
            rollback_failed = True
            raise OSError("rollback failed")
        original_replace(source, target)

    def fail_temporary_cleanup(path: Path, *, missing_ok: bool = False) -> None:
        if rollback_failed and path == temporary_metadata:
            raise PermissionError("temporary cleanup failed")
        original_unlink(path, missing_ok=missing_ok)

    def response_for_url(url: str, *args: object, **kwargs: object) -> io.BytesIO:
        if url.endswith("/exports/geojson"):
            return _response(_feature_collection())
        return _response(_metadata_content(dataset_id))

    monkeypatch.setattr(rte_odre_fr, "open_safe_https", response_for_url)
    monkeypatch.setattr(rte_odre_fr, "_replace_file", fail_publication_and_rollback)
    monkeypatch.setattr(Path, "unlink", fail_temporary_cleanup)

    with pytest.raises(RteOdreDownloadError, match="rollback"):
        download_rte_odre_dataset("sites", source_config, tmp_path)

    assert archive_backup.read_bytes() == old_archive
    assert metadata_backup.read_bytes() == old_metadata
```

### `test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error.fail_publication_and_rollback`

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
- Explicit raise expressions: `OSError('publication failed')`, `OSError('rollback failed')`.

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

- callback/function object: `tests/unit/test_cadastre_fr.py::test_publication_and_rollback_failure_preserves_recovery_backup` via `patch.object(cadastre_fr, '_replace_file', side_effect=fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_cadastre_fr.py::test_next_run_after_double_failure_preserves_recovery_before_network` via `patch.object(cadastre_fr, '_replace_file', side_effect=fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_cadastre_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `monkeypatch.setattr(cadastre_fr, '_replace_file', fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_publication_and_rollback_failure_preserves_exact_recovery_backups` via `monkeypatch.setattr(gpu, '_replace_file', fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `monkeypatch.setattr(gpu, '_replace_file', fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_ign_bdtopo_fr.py::test_publication_and_rollback_failure_preserves_exact_recovery_backups` via `patch.object(ign_bdtopo_fr, '_replace_file', side_effect=fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_ign_bdtopo_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `patch.object(ign_bdtopo_fr, '_replace_file', side_effect=fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_rollback_failure_preserves_recovery_material` via `monkeypatch.setattr(inpn, '_replace_file', fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `monkeypatch.setattr(rte_odre_fr, '_replace_file', fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `monkeypatch.setattr(rte_odre_fr, '_replace_file', fail_publication_and_rollback)`.

**Complete source-ordered implementation**

```python
def fail_publication_and_rollback(source: Path, target: Path) -> None:
        nonlocal rollback_failed
        if source == temporary_metadata and target == metadata_path:
            raise OSError("publication failed")
        if source == archive_backup and target == first.path:
            rollback_failed = True
            raise OSError("rollback failed")
        original_replace(source, target)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error.fail_temporary_cleanup`

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
- Explicit raise expressions: `PermissionError('temporary cleanup failed')`.

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

- callback/function object: `tests/unit/test_cadastre_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `monkeypatch.setattr(Path, 'unlink', fail_temporary_cleanup)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `monkeypatch.setattr(Path, 'unlink', fail_temporary_cleanup)`.
- callback/function object: `tests/unit/test_ign_bdtopo_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `patch.object(Path, 'unlink', new=fail_temporary_cleanup)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `monkeypatch.setattr(Path, 'unlink', fail_temporary_cleanup)`.

**Complete source-ordered implementation**

```python
def fail_temporary_cleanup(path: Path, *, missing_ok: bool = False) -> None:
        if rollback_failed and path == temporary_metadata:
            raise PermissionError("temporary cleanup failed")
        original_unlink(path, missing_ok=missing_ok)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error.response_for_url`

**Exact signature**

```python
def response_for_url(url: str, *args: object, **kwargs: object) -> io.BytesIO:
```

**Purpose**

Private `test` helper for response for url; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `io.BytesIO`.
- Every observed return expression is reproduced without truncation:
```python
_response(_metadata_content(dataset_id))

_response(_feature_collection())
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

- callback/function object: `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `monkeypatch.setattr(rte_odre_fr, 'open_safe_https', response_for_url)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `monkeypatch.setattr(rte_odre_fr, 'open_safe_https', response_for_url)`.

**Complete source-ordered implementation**

```python
def response_for_url(url: str, *args: object, **kwargs: object) -> io.BytesIO:
        if url.endswith("/exports/geojson"):
            return _response(_feature_collection())
        return _response(_metadata_content(dataset_id))
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.


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

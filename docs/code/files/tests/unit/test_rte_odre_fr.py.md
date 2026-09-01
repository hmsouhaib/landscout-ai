# `tests/unit/test_rte_odre_fr.py`

## File identity

- Repository path: `tests/unit/test_rte_odre_fr.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Provides complete unit and regression coverage for the `rte_odre_fr` contracts exercised in this file.
- Source SHA256: `30bf71ecb360553cdcd1efd6e797379d16668f346f4ef59bfa7b22d2569cdd46`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for rte odre fr; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Provides complete unit and regression coverage for the `rte_odre_fr` contracts exercised in this file.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

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

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `PROJECT_ROOT`

- Category: module constant or closed domain.
- Exact declaration:

```python
PROJECT_ROOT = Path(__file__).parents[2]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `CONFIG_PATH`

- Category: module constant or closed domain.
- Exact declaration:

```python
CONFIG_PATH = PROJECT_ROOT / "configs/sources/rte_odre_fr.yaml"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `BASE_URL`

- Category: module constant or closed domain.
- Exact declaration:

```python
BASE_URL = "https://odre.opendatasoft.com/api/explore/v2.1"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `DATASET_IDS`

- Category: module constant or closed domain.
- Exact declaration:

```python
DATASET_IDS = {
    "sites": "postes-electriques-rte",
    "overhead_lines": "lignes-aeriennes-rte-nv",
    "underground_lines": "lignes-souterraines-rte-nv",
}
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact mapping keys:
  - `sites`
  - `overhead_lines`
  - `underground_lines`


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

No top-level class/model/dataclass is declared.

## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_config_data`

**Purpose:** Implements `config data` within the file role: Provides complete unit and regression coverage for the `rte_odre_fr` contracts exercised in this file.

**Exact signature**

```python
def _config_data() -> dict:
```

- Exact decorators: none.
- Declared return annotation: `dict`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `yaml.safe_load(stream)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_rte_odre_fr::test_source_identity_is_exact` via `_config_data`
- value/type reference: `tests.unit.test_rte_odre_fr::test_source_identity_is_exact` via `_config_data`
- direct call: `tests.unit.test_rte_odre_fr::test_cache_age_is_a_strict_finite_number` via `_config_data`
- value/type reference: `tests.unit.test_rte_odre_fr::test_cache_age_is_a_strict_finite_number` via `_config_data`
- direct call: `tests.unit.test_rte_odre_fr::test_missing_dataset_id_fails` via `_config_data`
- value/type reference: `tests.unit.test_rte_odre_fr::test_missing_dataset_id_fails` via `_config_data`
- direct call: `tests.unit.test_rte_odre_fr::test_empty_base_url_fails` via `_config_data`
- value/type reference: `tests.unit.test_rte_odre_fr::test_empty_base_url_fails` via `_config_data`
- direct call: `tests.unit.test_rte_odre_fr::test_api_base_is_pinned_to_the_official_https_origin_and_path` via `_config_data`
- value/type reference: `tests.unit.test_rte_odre_fr::test_api_base_is_pinned_to_the_official_https_origin_and_path` via `_config_data`
- direct call: `tests.unit.test_rte_odre_fr::test_negative_cache_age_fails` via `_config_data`
- value/type reference: `tests.unit.test_rte_odre_fr::test_negative_cache_age_fails` via `_config_data`
- direct call: `tests.unit.test_rte_odre_fr::test_unsupported_export_format_fails` via `_config_data`
- value/type reference: `tests.unit.test_rte_odre_fr::test_unsupported_export_format_fails` via `_config_data`
- direct call: `tests.unit.test_rte_odre_fr::test_export_url_uses_configured_dataset_id` via `_config_data`
- value/type reference: `tests.unit.test_rte_odre_fr::test_export_url_uses_configured_dataset_id` via `_config_data`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `CONFIG_PATH.open` | `unresolved local/third-party receiver; no ownership inferred` |
| `yaml.safe_load` | `yaml.safe_load` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `CONFIG_PATH.open` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _config_data() -> dict:
    with CONFIG_PATH.open(encoding="utf-8") as stream:
        return yaml.safe_load(stream)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_metadata_content`

**Purpose:** Implements `metadata content` within the file role: Provides complete unit and regression coverage for the `rte_odre_fr` contracts exercised in this file.

**Exact signature**

```python
def _metadata_content(dataset_id: str, records_count: int | None = 2) -> bytes:
```

- Exact decorators: none.
- Declared return annotation: `bytes`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `dataset_id` | positional-or-keyword | `str` | `required` |
| `records_count` | positional-or-keyword | `int \| None` | `2` |

**Return and exception contract**

- Exact observed return expressions:
  - `json.dumps(payload, ensure_ascii=False).encode("utf-8")`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_rte_odre_fr::test_metadata_is_captured_without_fabrication` via `_metadata_content`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_is_captured_without_fabrication` via `_metadata_content`
- direct call: `tests.unit.test_rte_odre_fr::test_metadata_response_rejects_duplicate_json_keys` via `_metadata_content`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_response_rejects_duplicate_json_keys` via `_metadata_content`
- direct call: `tests.unit.test_rte_odre_fr::test_metadata_response_rejects_nonfinite_json_constants` via `_metadata_content`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_response_rejects_nonfinite_json_constants` via `_metadata_content`
- direct call: `tests.unit.test_rte_odre_fr::test_successful_download` via `_metadata_content`
- value/type reference: `tests.unit.test_rte_odre_fr::test_successful_download` via `_metadata_content`
- direct call: `tests.unit.test_rte_odre_fr::test_metadata_export_record_count_mismatch_is_rejected` via `_metadata_content`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_export_record_count_mismatch_is_rejected` via `_metadata_content`
- direct call: `tests.unit.test_rte_odre_fr::test_unavailable_metadata_record_count_is_accepted` via `_metadata_content`
- value/type reference: `tests.unit.test_rte_odre_fr::test_unavailable_metadata_record_count_is_accepted` via `_metadata_content`
- direct call: `tests.unit.test_rte_odre_fr::test_negative_source_record_count_is_rejected` via `_metadata_content`
- value/type reference: `tests.unit.test_rte_odre_fr::test_negative_source_record_count_is_rejected` via `_metadata_content`
- direct call: `tests.unit.test_rte_odre_fr::test_fresh_cache_is_reused` via `_metadata_content`
- value/type reference: `tests.unit.test_rte_odre_fr::test_fresh_cache_is_reused` via `_metadata_content`
- direct call: `tests.unit.test_rte_odre_fr::test_untrusted_cache_metadata_is_rejected_and_refreshed` via `_metadata_content`
- value/type reference: `tests.unit.test_rte_odre_fr::test_untrusted_cache_metadata_is_rejected_and_refreshed` via `_metadata_content`
- direct call: `tests.unit.test_rte_odre_fr::test_expired_cache_is_refreshed` via `_metadata_content`
- value/type reference: `tests.unit.test_rte_odre_fr::test_expired_cache_is_refreshed` via `_metadata_content`
- direct call: `tests.unit.test_rte_odre_fr::test_http_failure_raises_and_cleans_temporary_files` via `_metadata_content`
- value/type reference: `tests.unit.test_rte_odre_fr::test_http_failure_raises_and_cleans_temporary_files` via `_metadata_content`
- direct call: `tests.unit.test_rte_odre_fr::test_failed_refresh_preserves_previous_valid_cache` via `_metadata_content`
- value/type reference: `tests.unit.test_rte_odre_fr::test_failed_refresh_preserves_previous_valid_cache` via `_metadata_content`
- direct call: `tests.unit.test_rte_odre_fr::test_corrupted_refresh_preserves_previous_valid_cache` via `_metadata_content`
- value/type reference: `tests.unit.test_rte_odre_fr::test_corrupted_refresh_preserves_previous_valid_cache` via `_metadata_content`
- direct call: `tests.unit.test_rte_odre_fr::test_metadata_publication_failure_restores_previous_pair` via `_metadata_content`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_publication_failure_restores_previous_pair` via `_metadata_content`
- direct call: `tests.unit.test_rte_odre_fr::test_invalid_geojson_download_is_rejected` via `_metadata_content`
- value/type reference: `tests.unit.test_rte_odre_fr::test_invalid_geojson_download_is_rejected` via `_metadata_content`
- direct call: `tests.unit.test_rte_odre_fr::test_null_feature_geometries_are_accepted` via `_metadata_content`
- value/type reference: `tests.unit.test_rte_odre_fr::test_null_feature_geometries_are_accepted` via `_metadata_content`
- direct call: `tests.unit.test_rte_odre_fr::test_lineage_sidecar_records_integrity` via `_metadata_content`
- value/type reference: `tests.unit.test_rte_odre_fr::test_lineage_sidecar_records_integrity` via `_metadata_content`
- direct call: `tests.unit.test_rte_odre_fr::test_invalid_cached_record_count_invalidates_cache` via `_metadata_content`
- value/type reference: `tests.unit.test_rte_odre_fr::test_invalid_cached_record_count_invalidates_cache` via `_metadata_content`
- direct call: `tests.unit.test_rte_odre_fr::test_cached_export_summary_mismatch_invalidates_cache` via `_metadata_content`
- value/type reference: `tests.unit.test_rte_odre_fr::test_cached_export_summary_mismatch_invalidates_cache` via `_metadata_content`
- direct call: `tests.unit.test_rte_odre_fr::test_corrupted_cached_export_triggers_refresh` via `_metadata_content`
- value/type reference: `tests.unit.test_rte_odre_fr::test_corrupted_cached_export_triggers_refresh` via `_metadata_content`
- direct call: `tests.unit.test_rte_odre_fr::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `_metadata_content`
- value/type reference: `tests.unit.test_rte_odre_fr::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `_metadata_content`
- direct call: `tests.unit.test_rte_odre_fr::test_double_failure_preserves_recovery_and_next_run_uses_zero_network.response_for_url` via `_metadata_content`
- value/type reference: `tests.unit.test_rte_odre_fr::test_double_failure_preserves_recovery_and_next_run_uses_zero_network.response_for_url` via `_metadata_content`
- direct call: `tests.unit.test_rte_odre_fr::test_temporary_link_or_junction_cannot_modify_target_before_rte_network.record_network` via `_metadata_content`
- value/type reference: `tests.unit.test_rte_odre_fr::test_temporary_link_or_junction_cannot_modify_target_before_rte_network.record_network` via `_metadata_content`
- direct call: `tests.unit.test_rte_odre_fr::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_metadata_content`
- value/type reference: `tests.unit.test_rte_odre_fr::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_metadata_content`
- direct call: `tests.unit.test_rte_odre_fr::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error.response_for_url` via `_metadata_content`
- value/type reference: `tests.unit.test_rte_odre_fr::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error.response_for_url` via `_metadata_content`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `json.dumps(payload, ensure_ascii=False).encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_feature_collection`

**Purpose:** Implements `feature collection` within the file role: Provides complete unit and regression coverage for the `rte_odre_fr` contracts exercised in this file.

**Exact signature**

```python
def _feature_collection(*, all_null_geometry: bool = False) -> bytes:
```

- Exact decorators: none.
- Declared return annotation: `bytes`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `all_null_geometry` | keyword-only | `bool` | `False` |

**Return and exception contract**

- Exact observed return expressions:
  - `json.dumps(payload).encode("utf-8")`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_rte_odre_fr::test_successful_download` via `_feature_collection`
- value/type reference: `tests.unit.test_rte_odre_fr::test_successful_download` via `_feature_collection`
- direct call: `tests.unit.test_rte_odre_fr::test_metadata_export_record_count_mismatch_is_rejected` via `_feature_collection`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_export_record_count_mismatch_is_rejected` via `_feature_collection`
- direct call: `tests.unit.test_rte_odre_fr::test_unavailable_metadata_record_count_is_accepted` via `_feature_collection`
- value/type reference: `tests.unit.test_rte_odre_fr::test_unavailable_metadata_record_count_is_accepted` via `_feature_collection`
- direct call: `tests.unit.test_rte_odre_fr::test_fresh_cache_is_reused` via `_feature_collection`
- value/type reference: `tests.unit.test_rte_odre_fr::test_fresh_cache_is_reused` via `_feature_collection`
- direct call: `tests.unit.test_rte_odre_fr::test_untrusted_cache_metadata_is_rejected_and_refreshed` via `_feature_collection`
- value/type reference: `tests.unit.test_rte_odre_fr::test_untrusted_cache_metadata_is_rejected_and_refreshed` via `_feature_collection`
- direct call: `tests.unit.test_rte_odre_fr::test_expired_cache_is_refreshed` via `_feature_collection`
- value/type reference: `tests.unit.test_rte_odre_fr::test_expired_cache_is_refreshed` via `_feature_collection`
- direct call: `tests.unit.test_rte_odre_fr::test_failed_refresh_preserves_previous_valid_cache` via `_feature_collection`
- value/type reference: `tests.unit.test_rte_odre_fr::test_failed_refresh_preserves_previous_valid_cache` via `_feature_collection`
- direct call: `tests.unit.test_rte_odre_fr::test_corrupted_refresh_preserves_previous_valid_cache` via `_feature_collection`
- value/type reference: `tests.unit.test_rte_odre_fr::test_corrupted_refresh_preserves_previous_valid_cache` via `_feature_collection`
- direct call: `tests.unit.test_rte_odre_fr::test_metadata_publication_failure_restores_previous_pair` via `_feature_collection`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_publication_failure_restores_previous_pair` via `_feature_collection`
- direct call: `tests.unit.test_rte_odre_fr::test_null_feature_geometries_are_accepted` via `_feature_collection`
- value/type reference: `tests.unit.test_rte_odre_fr::test_null_feature_geometries_are_accepted` via `_feature_collection`
- direct call: `tests.unit.test_rte_odre_fr::test_lineage_sidecar_records_integrity` via `_feature_collection`
- value/type reference: `tests.unit.test_rte_odre_fr::test_lineage_sidecar_records_integrity` via `_feature_collection`
- direct call: `tests.unit.test_rte_odre_fr::test_invalid_cached_record_count_invalidates_cache` via `_feature_collection`
- value/type reference: `tests.unit.test_rte_odre_fr::test_invalid_cached_record_count_invalidates_cache` via `_feature_collection`
- direct call: `tests.unit.test_rte_odre_fr::test_cached_export_summary_mismatch_invalidates_cache` via `_feature_collection`
- value/type reference: `tests.unit.test_rte_odre_fr::test_cached_export_summary_mismatch_invalidates_cache` via `_feature_collection`
- direct call: `tests.unit.test_rte_odre_fr::test_corrupted_cached_export_triggers_refresh` via `_feature_collection`
- value/type reference: `tests.unit.test_rte_odre_fr::test_corrupted_cached_export_triggers_refresh` via `_feature_collection`
- direct call: `tests.unit.test_rte_odre_fr::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `_feature_collection`
- value/type reference: `tests.unit.test_rte_odre_fr::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `_feature_collection`
- direct call: `tests.unit.test_rte_odre_fr::test_double_failure_preserves_recovery_and_next_run_uses_zero_network.response_for_url` via `_feature_collection`
- value/type reference: `tests.unit.test_rte_odre_fr::test_double_failure_preserves_recovery_and_next_run_uses_zero_network.response_for_url` via `_feature_collection`
- direct call: `tests.unit.test_rte_odre_fr::test_temporary_link_or_junction_cannot_modify_target_before_rte_network.record_network` via `_feature_collection`
- value/type reference: `tests.unit.test_rte_odre_fr::test_temporary_link_or_junction_cannot_modify_target_before_rte_network.record_network` via `_feature_collection`
- direct call: `tests.unit.test_rte_odre_fr::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_feature_collection`
- value/type reference: `tests.unit.test_rte_odre_fr::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_feature_collection`
- direct call: `tests.unit.test_rte_odre_fr::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error.response_for_url` via `_feature_collection`
- value/type reference: `tests.unit.test_rte_odre_fr::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error.response_for_url` via `_feature_collection`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `json.dumps(payload).encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_response`

**Purpose:** Implements `response` within the file role: Provides complete unit and regression coverage for the `rte_odre_fr` contracts exercised in this file.

**Exact signature**

```python
def _response(content: bytes) -> io.BytesIO:
```

- Exact decorators: none.
- Declared return annotation: `io.BytesIO`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `content` | positional-or-keyword | `bytes` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `io.BytesIO(content)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_rte_odre_fr::test_metadata_is_captured_without_fabrication` via `_response`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_is_captured_without_fabrication` via `_response`
- direct call: `tests.unit.test_rte_odre_fr::test_metadata_response_rejects_duplicate_json_keys` via `_response`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_response_rejects_duplicate_json_keys` via `_response`
- direct call: `tests.unit.test_rte_odre_fr::test_metadata_response_rejects_nonfinite_json_constants` via `_response`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_response_rejects_nonfinite_json_constants` via `_response`
- direct call: `tests.unit.test_rte_odre_fr::test_successful_download` via `_response`
- value/type reference: `tests.unit.test_rte_odre_fr::test_successful_download` via `_response`
- direct call: `tests.unit.test_rte_odre_fr::test_metadata_export_record_count_mismatch_is_rejected` via `_response`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_export_record_count_mismatch_is_rejected` via `_response`
- direct call: `tests.unit.test_rte_odre_fr::test_unavailable_metadata_record_count_is_accepted` via `_response`
- value/type reference: `tests.unit.test_rte_odre_fr::test_unavailable_metadata_record_count_is_accepted` via `_response`
- direct call: `tests.unit.test_rte_odre_fr::test_negative_source_record_count_is_rejected` via `_response`
- value/type reference: `tests.unit.test_rte_odre_fr::test_negative_source_record_count_is_rejected` via `_response`
- direct call: `tests.unit.test_rte_odre_fr::test_fresh_cache_is_reused` via `_response`
- value/type reference: `tests.unit.test_rte_odre_fr::test_fresh_cache_is_reused` via `_response`
- direct call: `tests.unit.test_rte_odre_fr::test_untrusted_cache_metadata_is_rejected_and_refreshed` via `_response`
- value/type reference: `tests.unit.test_rte_odre_fr::test_untrusted_cache_metadata_is_rejected_and_refreshed` via `_response`
- direct call: `tests.unit.test_rte_odre_fr::test_expired_cache_is_refreshed` via `_response`
- value/type reference: `tests.unit.test_rte_odre_fr::test_expired_cache_is_refreshed` via `_response`
- direct call: `tests.unit.test_rte_odre_fr::test_http_failure_raises_and_cleans_temporary_files` via `_response`
- value/type reference: `tests.unit.test_rte_odre_fr::test_http_failure_raises_and_cleans_temporary_files` via `_response`
- direct call: `tests.unit.test_rte_odre_fr::test_failed_refresh_preserves_previous_valid_cache` via `_response`
- value/type reference: `tests.unit.test_rte_odre_fr::test_failed_refresh_preserves_previous_valid_cache` via `_response`
- direct call: `tests.unit.test_rte_odre_fr::test_corrupted_refresh_preserves_previous_valid_cache` via `_response`
- value/type reference: `tests.unit.test_rte_odre_fr::test_corrupted_refresh_preserves_previous_valid_cache` via `_response`
- direct call: `tests.unit.test_rte_odre_fr::test_metadata_publication_failure_restores_previous_pair` via `_response`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_publication_failure_restores_previous_pair` via `_response`
- direct call: `tests.unit.test_rte_odre_fr::test_invalid_geojson_download_is_rejected` via `_response`
- value/type reference: `tests.unit.test_rte_odre_fr::test_invalid_geojson_download_is_rejected` via `_response`
- direct call: `tests.unit.test_rte_odre_fr::test_null_feature_geometries_are_accepted` via `_response`
- value/type reference: `tests.unit.test_rte_odre_fr::test_null_feature_geometries_are_accepted` via `_response`
- direct call: `tests.unit.test_rte_odre_fr::test_lineage_sidecar_records_integrity` via `_response`
- value/type reference: `tests.unit.test_rte_odre_fr::test_lineage_sidecar_records_integrity` via `_response`
- direct call: `tests.unit.test_rte_odre_fr::test_invalid_cached_record_count_invalidates_cache` via `_response`
- value/type reference: `tests.unit.test_rte_odre_fr::test_invalid_cached_record_count_invalidates_cache` via `_response`
- direct call: `tests.unit.test_rte_odre_fr::test_cached_export_summary_mismatch_invalidates_cache` via `_response`
- value/type reference: `tests.unit.test_rte_odre_fr::test_cached_export_summary_mismatch_invalidates_cache` via `_response`
- direct call: `tests.unit.test_rte_odre_fr::test_corrupted_cached_export_triggers_refresh` via `_response`
- value/type reference: `tests.unit.test_rte_odre_fr::test_corrupted_cached_export_triggers_refresh` via `_response`
- direct call: `tests.unit.test_rte_odre_fr::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `_response`
- value/type reference: `tests.unit.test_rte_odre_fr::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `_response`
- direct call: `tests.unit.test_rte_odre_fr::test_double_failure_preserves_recovery_and_next_run_uses_zero_network.response_for_url` via `_response`
- value/type reference: `tests.unit.test_rte_odre_fr::test_double_failure_preserves_recovery_and_next_run_uses_zero_network.response_for_url` via `_response`
- direct call: `tests.unit.test_rte_odre_fr::test_temporary_link_or_junction_cannot_modify_target_before_rte_network.record_network` via `_response`
- value/type reference: `tests.unit.test_rte_odre_fr::test_temporary_link_or_junction_cannot_modify_target_before_rte_network.record_network` via `_response`
- direct call: `tests.unit.test_rte_odre_fr::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_response`
- value/type reference: `tests.unit.test_rte_odre_fr::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_response`
- direct call: `tests.unit.test_rte_odre_fr::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error.response_for_url` via `_response`
- value/type reference: `tests.unit.test_rte_odre_fr::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error.response_for_url` via `_response`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `io.BytesIO` | `io.BytesIO` |

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
def _response(content: bytes) -> io.BytesIO:
    return io.BytesIO(content)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_metadata_path`

**Purpose:** Implements `metadata path` within the file role: Provides complete unit and regression coverage for the `rte_odre_fr` contracts exercised in this file.

**Exact signature**

```python
def _metadata_path(cache_dir: Path, dataset_id: str) -> Path:
```

- Exact decorators: none.
- Declared return annotation: `Path`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `cache_dir` | positional-or-keyword | `Path` | `required` |
| `dataset_id` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `cache_dir / f"{dataset_id}.geojson.metadata.json"`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_rte_odre_fr::test_untrusted_cache_metadata_is_rejected_and_refreshed` via `_metadata_path`
- value/type reference: `tests.unit.test_rte_odre_fr::test_untrusted_cache_metadata_is_rejected_and_refreshed` via `_metadata_path`
- direct call: `tests.unit.test_rte_odre_fr::test_expired_cache_is_refreshed` via `_metadata_path`
- value/type reference: `tests.unit.test_rte_odre_fr::test_expired_cache_is_refreshed` via `_metadata_path`
- direct call: `tests.unit.test_rte_odre_fr::test_failed_refresh_preserves_previous_valid_cache` via `_metadata_path`
- value/type reference: `tests.unit.test_rte_odre_fr::test_failed_refresh_preserves_previous_valid_cache` via `_metadata_path`
- direct call: `tests.unit.test_rte_odre_fr::test_corrupted_refresh_preserves_previous_valid_cache` via `_metadata_path`
- value/type reference: `tests.unit.test_rte_odre_fr::test_corrupted_refresh_preserves_previous_valid_cache` via `_metadata_path`
- direct call: `tests.unit.test_rte_odre_fr::test_metadata_publication_failure_restores_previous_pair` via `_metadata_path`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_publication_failure_restores_previous_pair` via `_metadata_path`
- direct call: `tests.unit.test_rte_odre_fr::test_lineage_sidecar_records_integrity` via `_metadata_path`
- value/type reference: `tests.unit.test_rte_odre_fr::test_lineage_sidecar_records_integrity` via `_metadata_path`
- direct call: `tests.unit.test_rte_odre_fr::test_invalid_cached_record_count_invalidates_cache` via `_metadata_path`
- value/type reference: `tests.unit.test_rte_odre_fr::test_invalid_cached_record_count_invalidates_cache` via `_metadata_path`
- direct call: `tests.unit.test_rte_odre_fr::test_cached_export_summary_mismatch_invalidates_cache` via `_metadata_path`
- value/type reference: `tests.unit.test_rte_odre_fr::test_cached_export_summary_mismatch_invalidates_cache` via `_metadata_path`
- direct call: `tests.unit.test_rte_odre_fr::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `_metadata_path`
- value/type reference: `tests.unit.test_rte_odre_fr::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `_metadata_path`
- direct call: `tests.unit.test_rte_odre_fr::test_temporary_link_or_junction_cannot_modify_target_before_rte_network` via `_metadata_path`
- value/type reference: `tests.unit.test_rte_odre_fr::test_temporary_link_or_junction_cannot_modify_target_before_rte_network` via `_metadata_path`
- direct call: `tests.unit.test_rte_odre_fr::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_metadata_path`
- value/type reference: `tests.unit.test_rte_odre_fr::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_metadata_path`

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
def _metadata_path(cache_dir: Path, dataset_id: str) -> Path:
    return cache_dir / f"{dataset_id}.geojson.metadata.json"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_expire_cache`

**Purpose:** Implements `expire cache` within the file role: Provides complete unit and regression coverage for the `rte_odre_fr` contracts exercised in this file.

**Exact signature**

```python
def _expire_cache(metadata_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `metadata_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_rte_odre_fr::test_expired_cache_is_refreshed` via `_expire_cache`
- value/type reference: `tests.unit.test_rte_odre_fr::test_expired_cache_is_refreshed` via `_expire_cache`
- direct call: `tests.unit.test_rte_odre_fr::test_failed_refresh_preserves_previous_valid_cache` via `_expire_cache`
- value/type reference: `tests.unit.test_rte_odre_fr::test_failed_refresh_preserves_previous_valid_cache` via `_expire_cache`
- direct call: `tests.unit.test_rte_odre_fr::test_corrupted_refresh_preserves_previous_valid_cache` via `_expire_cache`
- value/type reference: `tests.unit.test_rte_odre_fr::test_corrupted_refresh_preserves_previous_valid_cache` via `_expire_cache`
- direct call: `tests.unit.test_rte_odre_fr::test_metadata_publication_failure_restores_previous_pair` via `_expire_cache`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_publication_failure_restores_previous_pair` via `_expire_cache`
- direct call: `tests.unit.test_rte_odre_fr::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `_expire_cache`
- value/type reference: `tests.unit.test_rte_odre_fr::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `_expire_cache`
- direct call: `tests.unit.test_rte_odre_fr::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_expire_cache`
- value/type reference: `tests.unit.test_rte_odre_fr::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_expire_cache`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `json.loads` | `json.loads` |
| `metadata_path.read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `(<br>        datetime.now(UTC) - timedelta(hours=169)<br>    ).isoformat` | `unresolved local/third-party receiver; no ownership inferred` |
| `datetime.now` | `datetime.datetime.now` |
| `timedelta` | `datetime.timedelta` |
| `metadata_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |

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
| In-memory mutation | `metadata["download_timestamp"] = (<br>        datetime.now(UTC) - timedelta(hours=169)<br>    ).isoformat()` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `source_config`

**Purpose:** Implements `source config` within the file role: Provides complete unit and regression coverage for the `rte_odre_fr` contracts exercised in this file.

**Exact signature**

```python
def source_config() -> RteOdreSourceConfig:
```

- Exact decorators: `pytest.fixture`.
- Declared return annotation: `RteOdreSourceConfig`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `load_rte_odre_source_config(CONFIG_PATH)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- value/type reference: `tests.unit.test_rte_odre_fr::test_valid_source_config_loads` via `source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_loaded_source_config_is_immutable` via `source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_mutated_loaded_api_origin_is_rejected_before_metadata_network` via `source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_build_export_url` via `source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_build_metadata_url` via `source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_is_captured_without_fabrication` via `source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_response_rejects_duplicate_json_keys` via `source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_response_rejects_nonfinite_json_constants` via `source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_successful_download` via `source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_export_record_count_mismatch_is_rejected` via `source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_unavailable_metadata_record_count_is_accepted` via `source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_negative_source_record_count_is_rejected` via `source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_fresh_cache_is_reused` via `source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_untrusted_cache_metadata_is_rejected_and_refreshed` via `source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_expired_cache_is_refreshed` via `source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_http_failure_raises_and_cleans_temporary_files` via `source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_failed_refresh_preserves_previous_valid_cache` via `source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_corrupted_refresh_preserves_previous_valid_cache` via `source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_publication_failure_restores_previous_pair` via `source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_invalid_geojson_download_is_rejected` via `source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_null_feature_geometries_are_accepted` via `source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_lineage_sidecar_records_integrity` via `source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_invalid_cached_record_count_invalidates_cache` via `source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_cached_export_summary_mismatch_invalidates_cache` via `source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_corrupted_cached_export_triggers_refresh` via `source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_temporary_link_or_junction_cannot_modify_target_before_rte_network` via `source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_broken_recovery_symlink_rejects_rte_before_network` via `source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `source_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_rte_odre_source_config` | `landscout.sources.rte_odre_fr.load_rte_odre_source_config` |

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
def source_config() -> RteOdreSourceConfig:
    return load_rte_odre_source_config(CONFIG_PATH)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_source_config_loads`

**Purpose:** Regression invariant: valid source config loads. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_source_config_loads(source_config: RteOdreSourceConfig) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert source_config.provider == "RTE"`
  - `assert source_config.portal == "ODRE"`
  - `assert source_config.datasets.sites.dataset_id == "postes-electriques-rte"`
  - `assert source_config.cache.max_age_hours == 168`

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
def test_valid_source_config_loads(source_config: RteOdreSourceConfig) -> None:
    assert source_config.provider == "RTE"
    assert source_config.portal == "ODRE"
    assert source_config.datasets.sites.dataset_id == "postes-electriques-rte"
    assert source_config.cache.max_age_hours == 168
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_config_yaml_rejects_duplicate_keys`

**Purpose:** Regression invariant: source config yaml rejects duplicate keys. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_config_yaml_rejects_duplicate_keys(tmp_path: Path) -> None:
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
  - `pytest.raises(ValueError, match="Duplicate YAML key")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `CONFIG_PATH.read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `load_rte_odre_source_config` | `landscout.sources.rte_odre_fr.load_rte_odre_source_config` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `CONFIG_PATH.read_text` |
| Filesystem/archive write or publication | `path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_config_yaml_rejects_duplicate_keys(tmp_path: Path) -> None:
    path = tmp_path / "rte.yaml"
    path.write_text(
        CONFIG_PATH.read_text(encoding="utf-8") + "\nprovider: RTE\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Duplicate YAML key"):
        load_rte_odre_source_config(path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_loaded_source_config_is_immutable`

**Purpose:** Regression invariant: loaded source config is immutable. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_loaded_source_config_is_immutable(
    source_config: RteOdreSourceConfig,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError, match="frozen")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
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
| In-memory mutation | `source_config.provider = "UNTRUSTED"` |
| Direct parameter mutation | `source_config.provider = "UNTRUSTED"` |

**Complete source-ordered implementation**

```python
def test_loaded_source_config_is_immutable(
    source_config: RteOdreSourceConfig,
) -> None:
    with pytest.raises(ValidationError, match="frozen"):
        source_config.provider = "UNTRUSTED"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_identity_is_exact`

**Purpose:** Regression invariant: source identity is exact. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_identity_is_exact(field: str, value: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(("field", "value"), [("provider", "IGN"), ("portal", "OTHER")])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `field` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `str` | `required` |

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
| `_config_data` | `tests.unit.test_rte_odre_fr._config_data` |
| `pytest.raises` | `pytest.raises` |
| `RteOdreSourceConfig.model_validate` | `landscout.sources.rte_odre_fr.RteOdreSourceConfig.model_validate` |
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
| In-memory mutation | `payload[field] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_identity_is_exact(field: str, value: str) -> None:
    payload = _config_data()
    payload[field] = value

    with pytest.raises(ValidationError):
        RteOdreSourceConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_cache_age_is_a_strict_finite_number`

**Purpose:** Regression invariant: cache age is a strict finite number. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_cache_age_is_a_strict_finite_number(value: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "value",
    [True, "168", float("nan"), float("inf"), float("-inf")],
)`.
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
| `_config_data` | `tests.unit.test_rte_odre_fr._config_data` |
| `pytest.raises` | `pytest.raises` |
| `RteOdreSourceConfig.model_validate` | `landscout.sources.rte_odre_fr.RteOdreSourceConfig.model_validate` |
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
def test_cache_age_is_a_strict_finite_number(value: object) -> None:
    payload = _config_data()
    payload["cache"]["max_age_hours"] = value

    with pytest.raises(ValidationError):
        RteOdreSourceConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_dataset_id_fails`

**Purpose:** Regression invariant: missing dataset id fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_missing_dataset_id_fails() -> None:
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
| `_config_data` | `tests.unit.test_rte_odre_fr._config_data` |
| `pytest.raises` | `pytest.raises` |
| `RteOdreSourceConfig.model_validate` | `landscout.sources.rte_odre_fr.RteOdreSourceConfig.model_validate` |

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
def test_missing_dataset_id_fails() -> None:
    config_data = _config_data()
    del config_data["datasets"]["sites"]["dataset_id"]

    with pytest.raises(ValidationError):
        RteOdreSourceConfig.model_validate(config_data)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_empty_base_url_fails`

**Purpose:** Regression invariant: empty base url fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_empty_base_url_fails() -> None:
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
| `_config_data` | `tests.unit.test_rte_odre_fr._config_data` |
| `pytest.raises` | `pytest.raises` |
| `RteOdreSourceConfig.model_validate` | `landscout.sources.rte_odre_fr.RteOdreSourceConfig.model_validate` |

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
| In-memory mutation | `config_data["api"]["base_url"] = ""` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_empty_base_url_fails() -> None:
    config_data = _config_data()
    config_data["api"]["base_url"] = ""

    with pytest.raises(ValidationError):
        RteOdreSourceConfig.model_validate(config_data)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_api_base_is_pinned_to_the_official_https_origin_and_path`

**Purpose:** Regression invariant: api base is pinned to the official https origin and path. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_api_base_is_pinned_to_the_official_https_origin_and_path(
    base_url: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "base_url",
    [
        "http://odre.opendatasoft.com/api/explore/v2.1",
        "https://example.com/api/explore/v2.1",
        "https://odre.opendatasoft.com/api/explore/v2.0",
        "https://user:secret@odre.opendatasoft.com/api/explore/v2.1",
        "https://odre.opendatasoft.com:8443/api/explore/v2.1",
        "https://odre.opendatasoft.com/api/explore/v2.1?redirect=elsewhere",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `base_url` | positional-or-keyword | `str` | `required` |

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
| `_config_data` | `tests.unit.test_rte_odre_fr._config_data` |
| `pytest.raises` | `pytest.raises` |
| `RteOdreSourceConfig.model_validate` | `landscout.sources.rte_odre_fr.RteOdreSourceConfig.model_validate` |
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
| In-memory mutation | `config_data["api"]["base_url"] = base_url` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_api_base_is_pinned_to_the_official_https_origin_and_path(
    base_url: str,
) -> None:
    config_data = _config_data()
    config_data["api"]["base_url"] = base_url

    with pytest.raises(ValidationError):
        RteOdreSourceConfig.model_validate(config_data)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_mutated_loaded_api_origin_is_rejected_before_metadata_network`

**Purpose:** Regression invariant: mutated loaded api origin is rejected before metadata network. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_mutated_loaded_api_origin_is_rejected_before_metadata_network(
    source_config: RteOdreSourceConfig,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RteOdreDownloadError, match="config\|official\|origin")`
- Exact assertions:
  - `assert network_calls == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `source_config.api.model_copy` | `tests.unit.test_rte_odre_fr.source_config.api.model_copy` |
| `HttpUrl` | `pydantic.HttpUrl` |
| `source_config.model_copy` | `tests.unit.test_rte_odre_fr.source_config.model_copy` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `fetch_rte_odre_dataset_metadata` | `landscout.sources.rte_odre_fr.fetch_rte_odre_dataset_metadata` |

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
def test_mutated_loaded_api_origin_is_rejected_before_metadata_network(
    source_config: RteOdreSourceConfig,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    invalid_api = source_config.api.model_copy(
        update={"base_url": HttpUrl("https://unrelated.example/api/explore/v2.1")}
    )
    untrusted = source_config.model_copy(update={"api": invalid_api})
    network_calls = 0

    def fail_network(*args: object, **kwargs: object) -> object:
        nonlocal network_calls
        network_calls += 1
        raise AssertionError("network used after ODRE origin mutation")

    monkeypatch.setattr(rte_odre_fr, "open_safe_https", fail_network)

    with pytest.raises(RteOdreDownloadError, match="config|official|origin"):
        fetch_rte_odre_dataset_metadata(untrusted, "sites")

    assert network_calls == 0
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_mutated_loaded_api_origin_is_rejected_before_metadata_network.fail_network`

**Purpose:** Implements `fail network` within the file role: Provides complete unit and regression coverage for the `rte_odre_fr` contracts exercised in this file.

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
  - `AssertionError("network used after ODRE origin mutation")`.

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
        raise AssertionError("network used after ODRE origin mutation")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_negative_cache_age_fails`

**Purpose:** Regression invariant: negative cache age fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_negative_cache_age_fails() -> None:
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
| `_config_data` | `tests.unit.test_rte_odre_fr._config_data` |
| `pytest.raises` | `pytest.raises` |
| `RteOdreSourceConfig.model_validate` | `landscout.sources.rte_odre_fr.RteOdreSourceConfig.model_validate` |

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
| In-memory mutation | `config_data["cache"]["max_age_hours"] = -1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_negative_cache_age_fails() -> None:
    config_data = _config_data()
    config_data["cache"]["max_age_hours"] = -1

    with pytest.raises(ValidationError):
        RteOdreSourceConfig.model_validate(config_data)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unsupported_export_format_fails`

**Purpose:** Regression invariant: unsupported export format fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unsupported_export_format_fails() -> None:
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
| `_config_data` | `tests.unit.test_rte_odre_fr._config_data` |
| `pytest.raises` | `pytest.raises` |
| `RteOdreSourceConfig.model_validate` | `landscout.sources.rte_odre_fr.RteOdreSourceConfig.model_validate` |

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
| In-memory mutation | `config_data["datasets"]["sites"]["preferred_format"] = "csv"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_unsupported_export_format_fails() -> None:
    config_data = _config_data()
    config_data["datasets"]["sites"]["preferred_format"] = "csv"

    with pytest.raises(ValidationError):
        RteOdreSourceConfig.model_validate(config_data)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_build_export_url`

**Purpose:** Regression invariant: build export url. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_build_export_url(
    source_config: RteOdreSourceConfig, logical_name: str, dataset_id: str
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("logical_name", "dataset_id"),
    list(DATASET_IDS.items()),
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |
| `logical_name` | positional-or-keyword | `str` | `required` |
| `dataset_id` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert url == f"{BASE_URL}/catalog/datasets/{dataset_id}/exports/geojson"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `build_rte_odre_export_url` | `landscout.sources.rte_odre_fr.build_rte_odre_export_url` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `DATASET_IDS.items` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_build_export_url(
    source_config: RteOdreSourceConfig, logical_name: str, dataset_id: str
) -> None:
    url = build_rte_odre_export_url(source_config, logical_name)  # type: ignore[arg-type]

    assert url == f"{BASE_URL}/catalog/datasets/{dataset_id}/exports/geojson"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_build_metadata_url`

**Purpose:** Regression invariant: build metadata url. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_build_metadata_url(source_config: RteOdreSourceConfig) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert build_rte_odre_metadata_url(source_config, "sites") == (<br>        f"{BASE_URL}/catalog/datasets/postes-electriques-rte"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `build_rte_odre_metadata_url` | `landscout.sources.rte_odre_fr.build_rte_odre_metadata_url` |

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
def test_build_metadata_url(source_config: RteOdreSourceConfig) -> None:
    assert build_rte_odre_metadata_url(source_config, "sites") == (
        f"{BASE_URL}/catalog/datasets/postes-electriques-rte"
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_export_url_uses_configured_dataset_id`

**Purpose:** Regression invariant: export url uses configured dataset id. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_export_url_uses_configured_dataset_id() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert build_rte_odre_export_url(config, "sites").endswith(<br>        "/catalog/datasets/configured-sites/exports/geojson"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_config_data` | `tests.unit.test_rte_odre_fr._config_data` |
| `RteOdreSourceConfig.model_validate` | `landscout.sources.rte_odre_fr.RteOdreSourceConfig.model_validate` |
| `build_rte_odre_export_url(config, "sites").endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `build_rte_odre_export_url` | `landscout.sources.rte_odre_fr.build_rte_odre_export_url` |

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
| In-memory mutation | `config_data["datasets"]["sites"]["dataset_id"] = "configured-sites"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_export_url_uses_configured_dataset_id() -> None:
    config_data = _config_data()
    config_data["datasets"]["sites"]["dataset_id"] = "configured-sites"
    config = RteOdreSourceConfig.model_validate(config_data)

    assert build_rte_odre_export_url(config, "sites").endswith(
        "/catalog/datasets/configured-sites/exports/geojson"
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_metadata_is_captured_without_fabrication`

**Purpose:** Regression invariant: metadata is captured without fabrication. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_metadata_is_captured_without_fabrication(
    source_config: RteOdreSourceConfig,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert metadata.title == "Official RTE dataset"`
  - `assert metadata.publisher == "RTE"`
  - `assert metadata.modified == "2026-06-16T12:00:00+00:00"`
  - `assert metadata.data_processed == "2026-06-16T12:01:00+00:00"`
  - `assert metadata.metadata_processed == "2026-06-16T12:01:01+00:00"`
  - `assert metadata.license == "Licence Ouverte v2.0 (Etalab)"`
  - `assert metadata.records_count == 2`
  - `assert metadata.geometry_precision_status == "GENERALIZED_OR_RESTRICTED"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_metadata_content` | `tests.unit.test_rte_odre_fr._metadata_content` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_rte_odre_fr._response` |
| `fetch_rte_odre_dataset_metadata` | `landscout.sources.rte_odre_fr.fetch_rte_odre_dataset_metadata` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_metadata_response_rejects_duplicate_json_keys`

**Purpose:** Regression invariant: metadata response rejects duplicate json keys. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_metadata_response_rejects_duplicate_json_keys(
    source_config: RteOdreSourceConfig,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RteOdreDownloadError, match="request\|JSON")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_metadata_content(dataset_id).decode` | `unresolved local/third-party receiver; no ownership inferred` |
| `_metadata_content` | `tests.unit.test_rte_odre_fr._metadata_content` |
| `content.replace` | `unresolved local/third-party receiver; no ownership inferred` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_rte_odre_fr._response` |
| `content.encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `fetch_rte_odre_dataset_metadata` | `landscout.sources.rte_odre_fr.fetch_rte_odre_dataset_metadata` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `content.replace` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_metadata_response_rejects_duplicate_json_keys(
    source_config: RteOdreSourceConfig,
) -> None:
    dataset_id = DATASET_IDS["sites"]
    content = _metadata_content(dataset_id).decode("utf-8")
    marker = f'"dataset_id": "{dataset_id}"'
    content = content.replace(marker, f"{marker}, {marker}", 1)
    with (
        patch(
            "landscout.sources.rte_odre_fr.open_safe_https",
            return_value=_response(content.encode("utf-8")),
        ),
        pytest.raises(RteOdreDownloadError, match="request|JSON"),
    ):
        fetch_rte_odre_dataset_metadata(source_config, "sites")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_metadata_response_rejects_nonfinite_json_constants`

**Purpose:** Regression invariant: metadata response rejects nonfinite json constants. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_metadata_response_rejects_nonfinite_json_constants(
    source_config: RteOdreSourceConfig,
    constant: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("constant", ["NaN", "Infinity", "-Infinity"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |
| `constant` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RteOdreDownloadError, match="request\|JSON")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_metadata_content(dataset_id).decode` | `unresolved local/third-party receiver; no ownership inferred` |
| `_metadata_content` | `tests.unit.test_rte_odre_fr._metadata_content` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_rte_odre_fr._response` |
| `content.encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `fetch_rte_odre_dataset_metadata` | `landscout.sources.rte_odre_fr.fetch_rte_odre_dataset_metadata` |
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
def test_metadata_response_rejects_nonfinite_json_constants(
    source_config: RteOdreSourceConfig,
    constant: str,
) -> None:
    dataset_id = DATASET_IDS["sites"]
    content = _metadata_content(dataset_id).decode("utf-8")
    content = content[:-1] + f', "untrusted": {constant}}}'
    with (
        patch(
            "landscout.sources.rte_odre_fr.open_safe_https",
            return_value=_response(content.encode("utf-8")),
        ),
        pytest.raises(RteOdreDownloadError, match="request|JSON"),
    ):
        fetch_rte_odre_dataset_metadata(source_config, "sites")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_successful_download`

**Purpose:** Regression invariant: successful download. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_successful_download(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.logical_name == "sites"`
  - `assert result.dataset_id == dataset_id`
  - `assert result.provider == "RTE"`
  - `assert result.portal == "ODRE"`
  - `assert result.export_format == "geojson"`
  - `assert result.path.read_bytes() == export_content`
  - `assert result.file_size == len(export_content)`
  - `assert result.sha256 == sha256(export_content).hexdigest()`
  - `assert result.cache_hit is False`
  - `assert result.dataset_metadata.title == "Official RTE dataset"`
  - `assert result.dataset_metadata.records_count == result.export_summary.feature_count`
  - `assert result.export_summary == RteOdreExportSummary(<br>        feature_count=2,<br>        null_geometry_count=1,<br>        non_null_geometry_count=1,<br>        geometry_types=("Point",),<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_feature_collection` | `tests.unit.test_rte_odre_fr._feature_collection` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_rte_odre_fr._response` |
| `_metadata_content` | `tests.unit.test_rte_odre_fr._metadata_content` |
| `download_rte_odre_dataset` | `landscout.sources.rte_odre_fr.download_rte_odre_dataset` |
| `result.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(export_content).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `RteOdreExportSummary` | `landscout.sources.rte_odre_fr.RteOdreExportSummary` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `result.path.read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(export_content).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_metadata_export_record_count_mismatch_is_rejected`

**Purpose:** Regression invariant: metadata export record count mismatch is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_metadata_export_record_count_mismatch_is_rejected(
    tmp_path: Path,
    source_config: RteOdreSourceConfig,
    records_count: int,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("records_count", [1, 3])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |
| `records_count` | positional-or-keyword | `int` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RteOdreDownloadError, match="records_count")`
- Exact assertions:
  - `assert not list(tmp_path.glob("*.geojson"))`
  - `assert not list(tmp_path.glob("*.part"))`
  - `assert not list(tmp_path.glob("*.bak"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_rte_odre_fr._response` |
| `_metadata_content` | `tests.unit.test_rte_odre_fr._metadata_content` |
| `_feature_collection` | `tests.unit.test_rte_odre_fr._feature_collection` |
| `pytest.raises` | `pytest.raises` |
| `download_rte_odre_dataset` | `landscout.sources.rte_odre_fr.download_rte_odre_dataset` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `tmp_path.glob` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unavailable_metadata_record_count_is_accepted`

**Purpose:** Regression invariant: unavailable metadata record count is accepted. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unavailable_metadata_record_count_is_accepted(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.dataset_metadata.records_count is None`
  - `assert result.export_summary.feature_count == 2`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_rte_odre_fr._response` |
| `_metadata_content` | `tests.unit.test_rte_odre_fr._metadata_content` |
| `_feature_collection` | `tests.unit.test_rte_odre_fr._feature_collection` |
| `download_rte_odre_dataset` | `landscout.sources.rte_odre_fr.download_rte_odre_dataset` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_negative_source_record_count_is_rejected`

**Purpose:** Regression invariant: negative source record count is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_negative_source_record_count_is_rejected(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RteOdreDownloadError, match="must not be negative")`
- Exact assertions:
  - `assert not list(tmp_path.glob("*.part"))`
  - `assert not list(tmp_path.glob("*.bak"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_rte_odre_fr._response` |
| `_metadata_content` | `tests.unit.test_rte_odre_fr._metadata_content` |
| `pytest.raises` | `pytest.raises` |
| `download_rte_odre_dataset` | `landscout.sources.rte_odre_fr.download_rte_odre_dataset` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_export_summary_rejects_invalid_geometry_counts`

**Purpose:** Regression invariant: export summary rejects invalid geometry counts. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_export_summary_rejects_invalid_geometry_counts(
    feature_count: int,
    null_geometry_count: int,
    non_null_geometry_count: int,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("feature_count", "null_geometry_count", "non_null_geometry_count"),
    [
        (-1, 0, 0),
        (1, -1, 2),
        (1, 0, -1),
        (2, 0, 1),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `feature_count` | positional-or-keyword | `int` | `required` |
| `null_geometry_count` | positional-or-keyword | `int` | `required` |
| `non_null_geometry_count` | positional-or-keyword | `int` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `RteOdreExportSummary` | `landscout.sources.rte_odre_fr.RteOdreExportSummary` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_fresh_cache_is_reused`

**Purpose:** Regression invariant: fresh cache is reused. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_fresh_cache_is_reused(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert opener.call_count == 2`
  - `assert first.cache_hit is False`
  - `assert second.cache_hit is True`
  - `assert second.download_timestamp == first.download_timestamp`
  - `assert second.sha256 == first.sha256`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_rte_odre_fr._response` |
| `_metadata_content` | `tests.unit.test_rte_odre_fr._metadata_content` |
| `_feature_collection` | `tests.unit.test_rte_odre_fr._feature_collection` |
| `download_rte_odre_dataset` | `landscout.sources.rte_odre_fr.download_rte_odre_dataset` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_untrusted_cache_metadata_is_rejected_and_refreshed`

**Purpose:** Regression invariant: untrusted cache metadata is rejected and refreshed. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_untrusted_cache_metadata_is_rejected_and_refreshed(
    tmp_path: Path,
    source_config: RteOdreSourceConfig,
    mutation: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("mutation", ["duplicate_key", "nonexact_file_size"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |
| `mutation` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert opener.call_count == 4`
  - `assert refreshed.cache_hit is False`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_response` | `tests.unit.test_rte_odre_fr._response` |
| `_metadata_content` | `tests.unit.test_rte_odre_fr._metadata_content` |
| `_feature_collection` | `tests.unit.test_rte_odre_fr._feature_collection` |
| `patch` | `unittest.mock.patch` |
| `download_rte_odre_dataset` | `landscout.sources.rte_odre_fr.download_rte_odre_dataset` |
| `_metadata_path` | `tests.unit.test_rte_odre_fr._metadata_path` |
| `json.loads` | `json.loads` |
| `metadata_path.read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `metadata_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `encoded.replace` | `unresolved local/third-party receiver; no ownership inferred` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `metadata_path.read_text` |
| Filesystem/archive write or publication | `metadata_path.write_text`<br>`encoded.replace` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `metadata["file_size"] = float(first.file_size)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_untrusted_cache_metadata_is_rejected_and_refreshed(
    tmp_path: Path,
    source_config: RteOdreSourceConfig,
    mutation: str,
) -> None:
    dataset_id = DATASET_IDS["sites"]
    responses = [
        _response(_metadata_content(dataset_id)),
        _response(_feature_collection()),
        _response(_metadata_content(dataset_id)),
        _response(_feature_collection()),
    ]
    with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=responses,
    ) as opener:
        first = download_rte_odre_dataset("sites", source_config, tmp_path)
        metadata_path = _metadata_path(tmp_path, dataset_id)
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        if mutation == "duplicate_key":
            encoded = json.dumps(metadata, separators=(",", ":"))
            marker = f'"sha256":"{first.sha256}"'
            metadata_path.write_text(
                encoded.replace(marker, f"{marker},{marker}", 1),
                encoding="utf-8",
            )
        else:
            metadata["file_size"] = float(first.file_size)
            metadata_path.write_text(json.dumps(metadata), encoding="utf-8")

        refreshed = download_rte_odre_dataset("sites", source_config, tmp_path)

    assert opener.call_count == 4
    assert refreshed.cache_hit is False
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_expired_cache_is_refreshed`

**Purpose:** Regression invariant: expired cache is refreshed. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_expired_cache_is_refreshed(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert opener.call_count == 2`
  - `assert refreshed.cache_hit is False`
  - `assert refreshed.path.read_bytes() == refreshed_content`
  - `assert refreshed.sha256 != first.sha256`
  - `assert refreshed.export_summary.feature_count == 3`
  - `assert not list(tmp_path.glob("*.bak"))`
  - `assert not list(tmp_path.glob("*.part"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_feature_collection` | `tests.unit.test_rte_odre_fr._feature_collection` |
| `json.loads` | `json.loads` |
| `refreshed_payload["features"].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps(refreshed_payload).encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_rte_odre_fr._response` |
| `_metadata_content` | `tests.unit.test_rte_odre_fr._metadata_content` |
| `download_rte_odre_dataset` | `landscout.sources.rte_odre_fr.download_rte_odre_dataset` |
| `_expire_cache` | `tests.unit.test_rte_odre_fr._expire_cache` |
| `_metadata_path` | `tests.unit.test_rte_odre_fr._metadata_path` |
| `refreshed.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `tmp_path.glob` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `refreshed.path.read_bytes`<br>`tmp_path.glob` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `refreshed_payload["features"].append(<br>        {"type": "Feature", "properties": {"code": "C"}, "geometry": None}<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_http_failure_raises_and_cleans_temporary_files`

**Purpose:** Regression invariant: http failure raises and cleans temporary files. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_http_failure_raises_and_cleans_temporary_files(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RteOdreDownloadError)`
- Exact assertions:
  - `assert not list(tmp_path.glob("*.part"))`
  - `assert not list(tmp_path.glob("*.geojson"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `build_rte_odre_export_url` | `landscout.sources.rte_odre_fr.build_rte_odre_export_url` |
| `HTTPError` | `urllib.error.HTTPError` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_rte_odre_fr._response` |
| `_metadata_content` | `tests.unit.test_rte_odre_fr._metadata_content` |
| `pytest.raises` | `pytest.raises` |
| `download_rte_odre_dataset` | `landscout.sources.rte_odre_fr.download_rte_odre_dataset` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_failed_refresh_preserves_previous_valid_cache`

**Purpose:** Regression invariant: failed refresh preserves previous valid cache. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_failed_refresh_preserves_previous_valid_cache(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RteOdreDownloadError)`
- Exact assertions:
  - `assert first.path.read_bytes() == original_archive`
  - `assert metadata_path.read_bytes() == expired_metadata`
  - `assert metadata_path.read_bytes() != original_metadata`
  - `assert not list(tmp_path.glob("*.part"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_rte_odre_fr._response` |
| `_metadata_content` | `tests.unit.test_rte_odre_fr._metadata_content` |
| `_feature_collection` | `tests.unit.test_rte_odre_fr._feature_collection` |
| `download_rte_odre_dataset` | `landscout.sources.rte_odre_fr.download_rte_odre_dataset` |
| `first.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_metadata_path` | `tests.unit.test_rte_odre_fr._metadata_path` |
| `metadata_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_expire_cache` | `tests.unit.test_rte_odre_fr._expire_cache` |
| `build_rte_odre_metadata_url` | `landscout.sources.rte_odre_fr.build_rte_odre_metadata_url` |
| `HTTPError` | `urllib.error.HTTPError` |
| `pytest.raises` | `pytest.raises` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `tmp_path.glob` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `first.path.read_bytes`<br>`metadata_path.read_bytes`<br>`tmp_path.glob` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_corrupted_refresh_preserves_previous_valid_cache`

**Purpose:** Regression invariant: corrupted refresh preserves previous valid cache. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_corrupted_refresh_preserves_previous_valid_cache(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RteOdreDownloadError)`
- Exact assertions:
  - `assert first.path.read_bytes() == original_archive`
  - `assert metadata_path.read_bytes() == expired_metadata`
  - `assert not list(tmp_path.glob("*.part"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_rte_odre_fr._response` |
| `_metadata_content` | `tests.unit.test_rte_odre_fr._metadata_content` |
| `_feature_collection` | `tests.unit.test_rte_odre_fr._feature_collection` |
| `download_rte_odre_dataset` | `landscout.sources.rte_odre_fr.download_rte_odre_dataset` |
| `first.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_metadata_path` | `tests.unit.test_rte_odre_fr._metadata_path` |
| `_expire_cache` | `tests.unit.test_rte_odre_fr._expire_cache` |
| `metadata_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `tmp_path.glob` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `first.path.read_bytes`<br>`metadata_path.read_bytes`<br>`tmp_path.glob` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_metadata_publication_failure_restores_previous_pair`

**Purpose:** Regression invariant: metadata publication failure restores previous pair. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_metadata_publication_failure_restores_previous_pair(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RteOdreDownloadError)`
- Exact assertions:
  - `assert failure_injected`
  - `assert first.path.read_bytes() == old_archive`
  - `assert metadata_path.read_bytes() == old_metadata`
  - `assert not list(tmp_path.glob("*.part"))`
  - `assert not list(tmp_path.glob("*.bak"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_rte_odre_fr._response` |
| `_metadata_content` | `tests.unit.test_rte_odre_fr._metadata_content` |
| `_feature_collection` | `tests.unit.test_rte_odre_fr._feature_collection` |
| `download_rte_odre_dataset` | `landscout.sources.rte_odre_fr.download_rte_odre_dataset` |
| `_metadata_path` | `tests.unit.test_rte_odre_fr._metadata_path` |
| `_expire_cache` | `tests.unit.test_rte_odre_fr._expire_cache` |
| `first.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `patch.object` | `unittest.mock.patch.object` |
| `pytest.raises` | `pytest.raises` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `tmp_path.glob` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `first.path.read_bytes`<br>`metadata_path.read_bytes`<br>`tmp_path.glob` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_metadata_publication_failure_restores_previous_pair.fail_metadata_publication`

**Purpose:** Implements `fail metadata publication` within the file role: Provides complete unit and regression coverage for the `rte_odre_fr` contracts exercised in this file.

**Exact signature**

```python
def fail_metadata_publication(source: Path, target: Path) -> None:
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
  - `PermissionError("simulated persistent metadata file lock")` under lexical guard `source == temporary_metadata and target == metadata_path`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `PermissionError` | `unresolved local/third-party receiver; no ownership inferred` |
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
def fail_metadata_publication(source: Path, target: Path) -> None:
        nonlocal failure_injected
        if source == temporary_metadata and target == metadata_path:
            failure_injected = True
            raise PermissionError("simulated persistent metadata file lock")
        original_replace(source, target)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_geojson_download_is_rejected`

**Purpose:** Regression invariant: invalid geojson download is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_geojson_download_is_rejected(
    tmp_path: Path,
    source_config: RteOdreSourceConfig,
    invalid_content: bytes,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "invalid_content",
    [
        b"{not-json",
        json.dumps({"type": "Point", "coordinates": [1, 2]}).encode(),
        json.dumps({"type": "FeatureCollection"}).encode(),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |
| `invalid_content` | positional-or-keyword | `bytes` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RteOdreDownloadError)`
- Exact assertions:
  - `assert not list(tmp_path.glob("*.part"))`
  - `assert not list(tmp_path.glob("*.geojson"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_rte_odre_fr._response` |
| `_metadata_content` | `tests.unit.test_rte_odre_fr._metadata_content` |
| `pytest.raises` | `pytest.raises` |
| `download_rte_odre_dataset` | `landscout.sources.rte_odre_fr.download_rte_odre_dataset` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `tmp_path.glob` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `json.dumps({"type": "Point", "coordinates": [1, 2]}).encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `json.dumps({"type": "FeatureCollection"}).encode` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_geojson_export_rejects_duplicate_json_keys`

**Purpose:** Regression invariant: geojson export rejects duplicate json keys. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_geojson_export_rejects_duplicate_json_keys(tmp_path: Path) -> None:
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
  - `pytest.raises(RteOdreDownloadError, match="JSON")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `rte_odre_fr._validate_geojson` | `landscout.sources.rte_odre_fr._validate_geojson` |

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
def test_geojson_export_rejects_duplicate_json_keys(tmp_path: Path) -> None:
    path = tmp_path / "duplicate.geojson"
    path.write_bytes(
        b'{"type":"FeatureCollection","type":"FeatureCollection","features":[]}'
    )

    with pytest.raises(RteOdreDownloadError, match="JSON"):
        rte_odre_fr._validate_geojson(path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_malformed_geojson_feature_or_geometry_is_rejected`

**Purpose:** Regression invariant: malformed geojson feature or geometry is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_malformed_geojson_feature_or_geometry_is_rejected(
    tmp_path: Path,
    feature: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "feature",
    [
        123,
        "feature",
        {"geometry": None},
        {"type": "NotFeature", "geometry": None},
        {"type": "Feature", "geometry": {}},
        {"type": "Feature", "geometry": {"type": ""}},
        {"type": "Feature", "geometry": {"type": "SOMETHING_RANDOM"}},
        {"type": "Feature", "geometry": {"type": "Point"}},
        {"type": "Feature", "geometry": {"type": "GeometryCollection"}},
        {"type": "Feature", "geometry": 123},
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `feature` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RteOdreDownloadError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `pytest.raises` | `pytest.raises` |
| `rte_odre_fr._validate_geojson` | `landscout.sources.rte_odre_fr._validate_geojson` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_standard_geojson_geometry_types_are_summarized`

**Purpose:** Regression invariant: standard geojson geometry types are summarized. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_standard_geojson_geometry_types_are_summarized(tmp_path: Path) -> None:
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
  - `assert summary.feature_count == 8`
  - `assert summary.null_geometry_count == 1`
  - `assert summary.non_null_geometry_count == 7`
  - `assert summary.geometry_types == tuple(<br>        sorted((*coordinate_types, "GeometryCollection"))<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `coordinate_types.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `features.extend` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `rte_odre_fr._validate_geojson` | `landscout.sources.rte_odre_fr._validate_geojson` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `features.extend(<br>        [<br>            {<br>                "type": "Feature",<br>                "geometry": {"type": "GeometryCollection", "geometries": []},<br>            },<br>            {"type": "Feature", "geometry": None},<br>        ]<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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
    assert summary.geometry_types == tuple(
        sorted((*coordinate_types, "GeometryCollection"))
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_point_requires_a_finite_numeric_position`

**Purpose:** Regression invariant: point requires a finite numeric position. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_point_requires_a_finite_numeric_position(
    tmp_path: Path,
    coordinates: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "coordinates",
    [None, "x", {}, [True, 2], [1, float("nan")], [1, float("inf")], [1]],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `coordinates` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RteOdreDownloadError, match="coordinate\|Point\|finite")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `pytest.raises` | `pytest.raises` |
| `rte_odre_fr._validate_geojson` | `landscout.sources.rte_odre_fr._validate_geojson` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_nested_coordinate_geometries_reject_obvious_invalid_structure`

**Purpose:** Regression invariant: nested coordinate geometries reject obvious invalid structure. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_nested_coordinate_geometries_reject_obvious_invalid_structure(
    tmp_path: Path,
    geometry_type: str,
    coordinates: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("geometry_type", "coordinates"),
    [
        ("MultiPoint", None),
        ("LineString", "x"),
        ("MultiLineString", {}),
        ("Polygon", [1, 2]),
        ("MultiPolygon", [[[1, float("inf")]]]),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `geometry_type` | positional-or-keyword | `str` | `required` |
| `coordinates` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RteOdreDownloadError, match="coordinate\|structure\|finite")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `pytest.raises` | `pytest.raises` |
| `rte_odre_fr._validate_geojson` | `landscout.sources.rte_odre_fr._validate_geojson` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_geometry_collection_members_are_validated_recursively`

**Purpose:** Regression invariant: geometry collection members are validated recursively. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_geometry_collection_members_are_validated_recursively(tmp_path: Path) -> None:
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
  - `pytest.raises(RteOdreDownloadError, match="coordinate\|Point")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `pytest.raises` | `pytest.raises` |
| `rte_odre_fr._validate_geojson` | `landscout.sources.rte_odre_fr._validate_geojson` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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
                            "geometries": [{"type": "Point", "coordinates": None}],
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_null_feature_geometries_are_accepted`

**Purpose:** Regression invariant: null feature geometries are accepted. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_null_feature_geometries_are_accepted(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.path.is_file()`
  - `assert result.dataset_metadata.geometry_precision_status == "MISSING"`
  - `assert result.export_summary == RteOdreExportSummary(<br>        feature_count=2,<br>        null_geometry_count=2,<br>        non_null_geometry_count=0,<br>        geometry_types=(),<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_feature_collection` | `tests.unit.test_rte_odre_fr._feature_collection` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_rte_odre_fr._response` |
| `_metadata_content` | `tests.unit.test_rte_odre_fr._metadata_content` |
| `download_rte_odre_dataset` | `landscout.sources.rte_odre_fr.download_rte_odre_dataset` |
| `result.path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `RteOdreExportSummary` | `landscout.sources.rte_odre_fr.RteOdreExportSummary` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `result.path.is_file` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_lineage_sidecar_records_integrity`

**Purpose:** Regression invariant: lineage sidecar records integrity. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_lineage_sidecar_records_integrity(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert lineage["source_url"] == result.source_url`
  - `assert lineage["file_size"] == len(export_content)`
  - `assert lineage["sha256"] == sha256(export_content).hexdigest()`
  - `assert lineage["dataset_metadata"]["publisher"] == "RTE"`
  - `assert lineage["export_summary"] == {<br>        "feature_count": 2,<br>        "geometry_types": ["Point"],<br>        "non_null_geometry_count": 1,<br>        "null_geometry_count": 1,<br>    }`
  - `assert (<br>        lineage["export_summary"]["null_geometry_count"]<br>        + lineage["export_summary"]["non_null_geometry_count"]<br>        == lineage["export_summary"]["feature_count"]<br>    )`
  - `assert "path" not in lineage`
  - `assert "cache_hit" not in lineage`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_feature_collection` | `tests.unit.test_rte_odre_fr._feature_collection` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_rte_odre_fr._response` |
| `_metadata_content` | `tests.unit.test_rte_odre_fr._metadata_content` |
| `download_rte_odre_dataset` | `landscout.sources.rte_odre_fr.download_rte_odre_dataset` |
| `_metadata_path` | `tests.unit.test_rte_odre_fr._metadata_path` |
| `json.loads` | `json.loads` |
| `metadata_path.read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(export_content).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `metadata_path.read_text` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(export_content).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_cached_record_count_invalidates_cache`

**Purpose:** Regression invariant: invalid cached record count invalidates cache. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_cached_record_count_invalidates_cache(
    tmp_path: Path,
    source_config: RteOdreSourceConfig,
    cached_records_count: int,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("cached_records_count", [-1, 1])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |
| `cached_records_count` | positional-or-keyword | `int` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert opener.call_count == 2`
  - `assert refreshed.cache_hit is False`
  - `assert refreshed.path.read_bytes() == first.path.read_bytes()`
  - `assert refreshed.dataset_metadata.records_count == 2`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_feature_collection` | `tests.unit.test_rte_odre_fr._feature_collection` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_rte_odre_fr._response` |
| `_metadata_content` | `tests.unit.test_rte_odre_fr._metadata_content` |
| `download_rte_odre_dataset` | `landscout.sources.rte_odre_fr.download_rte_odre_dataset` |
| `_metadata_path` | `tests.unit.test_rte_odre_fr._metadata_path` |
| `json.loads` | `json.loads` |
| `metadata_path.read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `refreshed.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `first.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `metadata_path.read_text`<br>`refreshed.path.read_bytes`<br>`first.path.read_bytes` |
| Filesystem/archive write or publication | `metadata_path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `lineage["dataset_metadata"]["records_count"] = cached_records_count` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_cached_export_summary_mismatch_invalidates_cache`

**Purpose:** Regression invariant: cached export summary mismatch invalidates cache. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_cached_export_summary_mismatch_invalidates_cache(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert opener.call_count == 2`
  - `assert refreshed.cache_hit is False`
  - `assert refreshed.export_summary.geometry_types == ("Point",)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_feature_collection` | `tests.unit.test_rte_odre_fr._feature_collection` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_rte_odre_fr._response` |
| `_metadata_content` | `tests.unit.test_rte_odre_fr._metadata_content` |
| `download_rte_odre_dataset` | `landscout.sources.rte_odre_fr.download_rte_odre_dataset` |
| `_metadata_path` | `tests.unit.test_rte_odre_fr._metadata_path` |
| `json.loads` | `json.loads` |
| `metadata_path.read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |

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
| In-memory mutation | `lineage["export_summary"]["null_geometry_count"] = 2`<br>`lineage["export_summary"]["non_null_geometry_count"] = 0`<br>`lineage["export_summary"]["geometry_types"] = []` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_corrupted_cached_export_triggers_refresh`

**Purpose:** Regression invariant: corrupted cached export triggers refresh. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_corrupted_cached_export_triggers_refresh(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert opener.call_count == 2`
  - `assert refreshed.cache_hit is False`
  - `assert refreshed.path.read_bytes() == valid_content`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_feature_collection` | `tests.unit.test_rte_odre_fr._feature_collection` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_rte_odre_fr._response` |
| `_metadata_content` | `tests.unit.test_rte_odre_fr._metadata_content` |
| `download_rte_odre_dataset` | `landscout.sources.rte_odre_fr.download_rte_odre_dataset` |
| `first.path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `refreshed.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `refreshed.path.read_bytes` |
| Filesystem/archive write or publication | `first.path.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_double_failure_preserves_recovery_and_next_run_uses_zero_network`

**Purpose:** Regression invariant: double failure preserves recovery and next run uses zero network. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_double_failure_preserves_recovery_and_next_run_uses_zero_network(
    tmp_path: Path,
    source_config: RteOdreSourceConfig,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RteOdreDownloadError, match="rollback")`
  - `pytest.raises(RteOdreDownloadError, match="backup\|recovery\|manual")`
- Exact assertions:
  - `assert archive_backup.read_bytes() == old_archive`
  - `assert metadata_backup.read_bytes() == old_metadata`
  - `assert network_calls == []`
  - `assert archive_backup.read_bytes() == archive_recovery`
  - `assert metadata_backup.read_bytes() == metadata_recovery`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_rte_odre_fr._response` |
| `_metadata_content` | `tests.unit.test_rte_odre_fr._metadata_content` |
| `_feature_collection` | `tests.unit.test_rte_odre_fr._feature_collection` |
| `download_rte_odre_dataset` | `landscout.sources.rte_odre_fr.download_rte_odre_dataset` |
| `_metadata_path` | `tests.unit.test_rte_odre_fr._metadata_path` |
| `_expire_cache` | `tests.unit.test_rte_odre_fr._expire_cache` |
| `first.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `first.path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `archive_backup.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_backup.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `first.path.read_bytes`<br>`metadata_path.read_bytes`<br>`archive_backup.read_bytes`<br>`metadata_backup.read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_double_failure_preserves_recovery_and_next_run_uses_zero_network.fail_publication_and_rollback`

**Purpose:** Implements `fail publication and rollback` within the file role: Provides complete unit and regression coverage for the `rte_odre_fr` contracts exercised in this file.

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
  - `OSError("publication failed")` under lexical guard `source == temporary_metadata and target == metadata_path`.
  - `OSError("rollback failed")` under lexical guard `source == archive_backup and target == first.path`.

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
            raise OSError("publication failed")
        if source == archive_backup and target == first.path:
            raise OSError("rollback failed")
        original_replace(source, target)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_double_failure_preserves_recovery_and_next_run_uses_zero_network.response_for_url`

**Purpose:** Implements `response for url` within the file role: Provides complete unit and regression coverage for the `rte_odre_fr` contracts exercised in this file.

**Exact signature**

```python
def response_for_url(url: str, *args: object, **kwargs: object) -> io.BytesIO:
```

- Exact decorators: none.
- Declared return annotation: `io.BytesIO`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `url` | positional-or-keyword | `str` | `required` |
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `_response(_feature_collection())`
  - `_response(_metadata_content(dataset_id))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `url.endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `_response` | `tests.unit.test_rte_odre_fr._response` |
| `_feature_collection` | `tests.unit.test_rte_odre_fr._feature_collection` |
| `_metadata_content` | `tests.unit.test_rte_odre_fr._metadata_content` |

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
def response_for_url(url: str, *args: object, **kwargs: object) -> io.BytesIO:
        if url.endswith("/exports/geojson"):
            return _response(_feature_collection())
        return _response(_metadata_content(dataset_id))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_double_failure_preserves_recovery_and_next_run_uses_zero_network.fail_network`

**Purpose:** Implements `fail network` within the file role: Provides complete unit and regression coverage for the `rte_odre_fr` contracts exercised in this file.

**Exact signature**

```python
def fail_network(url: str, *args: object, **kwargs: object) -> io.BytesIO:
```

- Exact decorators: none.
- Declared return annotation: `io.BytesIO`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `url` | positional-or-keyword | `str` | `required` |
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `AssertionError("manual recovery state must fail before HTTP")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `network_calls.append` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | `network_calls.append(url)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def fail_network(url: str, *args: object, **kwargs: object) -> io.BytesIO:
        network_calls.append(url)
        raise AssertionError("manual recovery state must fail before HTTP")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_temporary_link_or_junction_cannot_modify_target_before_rte_network`

**Purpose:** Regression invariant: temporary link or junction cannot modify target before rte network. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_temporary_link_or_junction_cannot_modify_target_before_rte_network(
    tmp_path: Path,
    source_config: RteOdreSourceConfig,
    monkeypatch: pytest.MonkeyPatch,
    temporary_role: str,
    link_kind: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("temporary_role", ["archive", "metadata"])`, `pytest.mark.parametrize("link_kind", ["symlink", "junction"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `temporary_role` | positional-or-keyword | `str` | `required` |
| `link_kind` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RteOdreDownloadError, match="temporary\|link\|cache")`
- Exact assertions:
  - `assert network_calls == 0`
  - `assert sentinel.read_bytes() == sentinel_bytes`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_metadata_path` | `tests.unit.test_rte_odre_fr._metadata_path` |
| `archive_path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `sentinel.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `download_rte_odre_dataset` | `landscout.sources.rte_odre_fr.download_rte_odre_dataset` |
| `sentinel.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
        return (link_kind == "symlink" and path == unsafe_path) or original_is_symlink(
            path
        )

    def simulated_is_junction(path: Path) -> bool:
        return (
            link_kind == "junction" and path == unsafe_path
        ) or original_is_junction(path)

    def simulated_symlink_open(path: Path, *args: object, **kwargs: object) -> object:
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_temporary_link_or_junction_cannot_modify_target_before_rte_network.simulated_is_symlink`

**Purpose:** Implements `simulated is symlink` within the file role: Provides complete unit and regression coverage for the `rte_odre_fr` contracts exercised in this file.

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
  - `(link_kind == "symlink" and path == unsafe_path) or original_is_symlink(<br>            path<br>        )`
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
        return (link_kind == "symlink" and path == unsafe_path) or original_is_symlink(
            path
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_temporary_link_or_junction_cannot_modify_target_before_rte_network.simulated_is_junction`

**Purpose:** Implements `simulated is junction` within the file role: Provides complete unit and regression coverage for the `rte_odre_fr` contracts exercised in this file.

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
  - `(<br>            link_kind == "junction" and path == unsafe_path<br>        ) or original_is_junction(path)`
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
        return (
            link_kind == "junction" and path == unsafe_path
        ) or original_is_junction(path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_temporary_link_or_junction_cannot_modify_target_before_rte_network.simulated_symlink_open`

**Purpose:** Implements `simulated symlink open` within the file role: Provides complete unit and regression coverage for the `rte_odre_fr` contracts exercised in this file.

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
        if path == unsafe_path:
            return original_open(sentinel, *args, **kwargs)
        return original_open(path, *args, **kwargs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_temporary_link_or_junction_cannot_modify_target_before_rte_network.record_network`

**Purpose:** Implements `record network` within the file role: Provides complete unit and regression coverage for the `rte_odre_fr` contracts exercised in this file.

**Exact signature**

```python
def record_network(url: str, *args: object, **kwargs: object) -> io.BytesIO:
```

- Exact decorators: none.
- Declared return annotation: `io.BytesIO`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `url` | positional-or-keyword | `str` | `required` |
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `_response(_feature_collection())`
  - `_response(_metadata_content(dataset_id))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `url.endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `_response` | `tests.unit.test_rte_odre_fr._response` |
| `_feature_collection` | `tests.unit.test_rte_odre_fr._feature_collection` |
| `_metadata_content` | `tests.unit.test_rte_odre_fr._metadata_content` |

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
def record_network(url: str, *args: object, **kwargs: object) -> io.BytesIO:
        nonlocal network_calls
        network_calls += 1
        if url.endswith("/exports/geojson"):
            return _response(_feature_collection())
        return _response(_metadata_content(dataset_id))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_broken_recovery_symlink_rejects_rte_before_network`

**Purpose:** Regression invariant: broken recovery symlink rejects rte before network. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_broken_recovery_symlink_rejects_rte_before_network(
    tmp_path: Path,
    source_config: RteOdreSourceConfig,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RteOdreDownloadError, match="backup\|recovery\|manual")`
- Exact assertions:
  - `assert network_calls == []`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `archive_path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `download_rte_odre_dataset` | `landscout.sources.rte_odre_fr.download_rte_odre_dataset` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_broken_recovery_symlink_rejects_rte_before_network.simulated_is_symlink`

**Purpose:** Implements `simulated is symlink` within the file role: Provides complete unit and regression coverage for the `rte_odre_fr` contracts exercised in this file.

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
  - `path == recovery_path or original_is_symlink(path)`
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
        return path == recovery_path or original_is_symlink(path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_broken_recovery_symlink_rejects_rte_before_network.fail_network`

**Purpose:** Implements `fail network` within the file role: Provides complete unit and regression coverage for the `rte_odre_fr` contracts exercised in this file.

**Exact signature**

```python
def fail_network(url: str, *args: object, **kwargs: object) -> io.BytesIO:
```

- Exact decorators: none.
- Declared return annotation: `io.BytesIO`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `url` | positional-or-keyword | `str` | `required` |
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `AssertionError("broken recovery link must fail before HTTP")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `network_calls.append` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | `network_calls.append(url)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def fail_network(url: str, *args: object, **kwargs: object) -> io.BytesIO:
        network_calls.append(url)
        raise AssertionError("broken recovery link must fail before HTTP")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error`

**Purpose:** Regression invariant: rte cleanup failure does not mask double failure recovery error. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error(
    tmp_path: Path,
    source_config: RteOdreSourceConfig,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RteOdreDownloadError, match="rollback")`
- Exact assertions:
  - `assert archive_backup.read_bytes() == old_archive`
  - `assert metadata_backup.read_bytes() == old_metadata`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_rte_odre_fr._response` |
| `_metadata_content` | `tests.unit.test_rte_odre_fr._metadata_content` |
| `_feature_collection` | `tests.unit.test_rte_odre_fr._feature_collection` |
| `download_rte_odre_dataset` | `landscout.sources.rte_odre_fr.download_rte_odre_dataset` |
| `_metadata_path` | `tests.unit.test_rte_odre_fr._metadata_path` |
| `_expire_cache` | `tests.unit.test_rte_odre_fr._expire_cache` |
| `first.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `first.path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `archive_backup.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_backup.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `first.path.read_bytes`<br>`metadata_path.read_bytes`<br>`archive_backup.read_bytes`<br>`metadata_backup.read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error.fail_publication_and_rollback`

**Purpose:** Implements `fail publication and rollback` within the file role: Provides complete unit and regression coverage for the `rte_odre_fr` contracts exercised in this file.

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
  - `OSError("publication failed")` under lexical guard `source == temporary_metadata and target == metadata_path`.
  - `OSError("rollback failed")` under lexical guard `source == archive_backup and target == first.path`.

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
            raise OSError("publication failed")
        if source == archive_backup and target == first.path:
            rollback_failed = True
            raise OSError("rollback failed")
        original_replace(source, target)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error.fail_temporary_cleanup`

**Purpose:** Implements `fail temporary cleanup` within the file role: Provides complete unit and regression coverage for the `rte_odre_fr` contracts exercised in this file.

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
  - `PermissionError("temporary cleanup failed")` under lexical guard `rollback_failed and path == temporary_metadata`.

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
            raise PermissionError("temporary cleanup failed")
        original_unlink(path, missing_ok=missing_ok)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error.response_for_url`

**Purpose:** Implements `response for url` within the file role: Provides complete unit and regression coverage for the `rte_odre_fr` contracts exercised in this file.

**Exact signature**

```python
def response_for_url(url: str, *args: object, **kwargs: object) -> io.BytesIO:
```

- Exact decorators: none.
- Declared return annotation: `io.BytesIO`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `url` | positional-or-keyword | `str` | `required` |
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `_response(_feature_collection())`
  - `_response(_metadata_content(dataset_id))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `url.endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `_response` | `tests.unit.test_rte_odre_fr._response` |
| `_feature_collection` | `tests.unit.test_rte_odre_fr._feature_collection` |
| `_metadata_content` | `tests.unit.test_rte_odre_fr._metadata_content` |

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
def response_for_url(url: str, *args: object, **kwargs: object) -> io.BytesIO:
        if url.endswith("/exports/geojson"):
            return _response(_feature_collection())
        return _response(_metadata_content(dataset_id))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **45**.
- Pytest fixtures (decorator-proven): **1**.

### Fixtures

- `source_config` — decorators: `pytest.fixture`.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_valid_source_config_loads` | none | none | 4 | Proves valid source config loads using the exact source reproduced in section 7. |
| `test_source_config_yaml_rejects_duplicate_keys` | none | pytest.raises(ValueError, match="Duplicate YAML key") | 0 | Proves source config yaml rejects duplicate keys using the exact source reproduced in section 7. |
| `test_loaded_source_config_is_immutable` | none | pytest.raises(ValidationError, match="frozen") | 0 | Proves loaded source config is immutable using the exact source reproduced in section 7. |
| `test_source_identity_is_exact` | pytest.mark.parametrize(("field", "value"), [("provider", "IGN"), ("portal", "OTHER")]) | pytest.raises(ValidationError) | 0 | Proves source identity is exact using the exact source reproduced in section 7. |
| `test_cache_age_is_a_strict_finite_number` | pytest.mark.parametrize(<br>    "value",<br>    [True, "168", float("nan"), float("inf"), float("-inf")],<br>) | pytest.raises(ValidationError) | 0 | Proves cache age is a strict finite number using the exact source reproduced in section 7. |
| `test_missing_dataset_id_fails` | none | pytest.raises(ValidationError) | 0 | Proves missing dataset id fails using the exact source reproduced in section 7. |
| `test_empty_base_url_fails` | none | pytest.raises(ValidationError) | 0 | Proves empty base url fails using the exact source reproduced in section 7. |
| `test_api_base_is_pinned_to_the_official_https_origin_and_path` | pytest.mark.parametrize(<br>    "base_url",<br>    [<br>        "http://odre.opendatasoft.com/api/explore/v2.1",<br>        "https://example.com/api/explore/v2.1",<br>        "https://odre.opendatasoft.com/api/explore/v2.0",<br>        "https://user:secret@odre.opendatasoft.com/api/explore/v2.1",<br>        "https://odre.opendatasoft.com:8443/api/explore/v2.1",<br>        "https://odre.opendatasoft.com/api/explore/v2.1?redirect=elsewhere",<br>    ],<br>) | pytest.raises(ValidationError) | 0 | Proves api base is pinned to the official https origin and path using the exact source reproduced in section 7. |
| `test_mutated_loaded_api_origin_is_rejected_before_metadata_network` | none | pytest.raises(RteOdreDownloadError, match="config\|official\|origin") | 1 | Proves mutated loaded api origin is rejected before metadata network using the exact source reproduced in section 7. |
| `test_negative_cache_age_fails` | none | pytest.raises(ValidationError) | 0 | Proves negative cache age fails using the exact source reproduced in section 7. |
| `test_unsupported_export_format_fails` | none | pytest.raises(ValidationError) | 0 | Proves unsupported export format fails using the exact source reproduced in section 7. |
| `test_build_export_url` | pytest.mark.parametrize(<br>    ("logical_name", "dataset_id"),<br>    list(DATASET_IDS.items()),<br>) | none | 1 | Proves build export url using the exact source reproduced in section 7. |
| `test_build_metadata_url` | none | none | 1 | Proves build metadata url using the exact source reproduced in section 7. |
| `test_export_url_uses_configured_dataset_id` | none | none | 1 | Proves export url uses configured dataset id using the exact source reproduced in section 7. |
| `test_metadata_is_captured_without_fabrication` | none | none | 8 | Proves metadata is captured without fabrication using the exact source reproduced in section 7. |
| `test_metadata_response_rejects_duplicate_json_keys` | none | pytest.raises(RteOdreDownloadError, match="request\|JSON") | 0 | Proves metadata response rejects duplicate json keys using the exact source reproduced in section 7. |
| `test_metadata_response_rejects_nonfinite_json_constants` | pytest.mark.parametrize("constant", ["NaN", "Infinity", "-Infinity"]) | pytest.raises(RteOdreDownloadError, match="request\|JSON") | 0 | Proves metadata response rejects nonfinite json constants using the exact source reproduced in section 7. |
| `test_successful_download` | none | none | 12 | Proves successful download using the exact source reproduced in section 7. |
| `test_metadata_export_record_count_mismatch_is_rejected` | pytest.mark.parametrize("records_count", [1, 3]) | pytest.raises(RteOdreDownloadError, match="records_count") | 3 | Proves metadata export record count mismatch is rejected using the exact source reproduced in section 7. |
| `test_unavailable_metadata_record_count_is_accepted` | none | none | 2 | Proves unavailable metadata record count is accepted using the exact source reproduced in section 7. |
| `test_negative_source_record_count_is_rejected` | none | pytest.raises(RteOdreDownloadError, match="must not be negative") | 2 | Proves negative source record count is rejected using the exact source reproduced in section 7. |
| `test_export_summary_rejects_invalid_geometry_counts` | pytest.mark.parametrize(<br>    ("feature_count", "null_geometry_count", "non_null_geometry_count"),<br>    [<br>        (-1, 0, 0),<br>        (1, -1, 2),<br>        (1, 0, -1),<br>        (2, 0, 1),<br>    ],<br>) | pytest.raises(ValueError) | 0 | Proves export summary rejects invalid geometry counts using the exact source reproduced in section 7. |
| `test_fresh_cache_is_reused` | none | none | 5 | Proves fresh cache is reused using the exact source reproduced in section 7. |
| `test_untrusted_cache_metadata_is_rejected_and_refreshed` | pytest.mark.parametrize("mutation", ["duplicate_key", "nonexact_file_size"]) | none | 2 | Proves untrusted cache metadata is rejected and refreshed using the exact source reproduced in section 7. |
| `test_expired_cache_is_refreshed` | none | none | 7 | Proves expired cache is refreshed using the exact source reproduced in section 7. |
| `test_http_failure_raises_and_cleans_temporary_files` | none | pytest.raises(RteOdreDownloadError) | 2 | Proves http failure raises and cleans temporary files using the exact source reproduced in section 7. |
| `test_failed_refresh_preserves_previous_valid_cache` | none | pytest.raises(RteOdreDownloadError) | 4 | Proves failed refresh preserves previous valid cache using the exact source reproduced in section 7. |
| `test_corrupted_refresh_preserves_previous_valid_cache` | none | pytest.raises(RteOdreDownloadError) | 3 | Proves corrupted refresh preserves previous valid cache using the exact source reproduced in section 7. |
| `test_metadata_publication_failure_restores_previous_pair` | none | pytest.raises(RteOdreDownloadError) | 5 | Proves metadata publication failure restores previous pair using the exact source reproduced in section 7. |
| `test_invalid_geojson_download_is_rejected` | pytest.mark.parametrize(<br>    "invalid_content",<br>    [<br>        b"{not-json",<br>        json.dumps({"type": "Point", "coordinates": [1, 2]}).encode(),<br>        json.dumps({"type": "FeatureCollection"}).encode(),<br>    ],<br>) | pytest.raises(RteOdreDownloadError) | 2 | Proves invalid geojson download is rejected using the exact source reproduced in section 7. |
| `test_geojson_export_rejects_duplicate_json_keys` | none | pytest.raises(RteOdreDownloadError, match="JSON") | 0 | Proves geojson export rejects duplicate json keys using the exact source reproduced in section 7. |
| `test_malformed_geojson_feature_or_geometry_is_rejected` | pytest.mark.parametrize(<br>    "feature",<br>    [<br>        123,<br>        "feature",<br>        {"geometry": None},<br>        {"type": "NotFeature", "geometry": None},<br>        {"type": "Feature", "geometry": {}},<br>        {"type": "Feature", "geometry": {"type": ""}},<br>        {"type": "Feature", "geometry": {"type": "SOMETHING_RANDOM"}},<br>        {"type": "Feature", "geometry": {"type": "Point"}},<br>        {"type": "Feature", "geometry": {"type": "GeometryCollection"}},<br>        {"type": "Feature", "geometry": 123},<br>    ],<br>) | pytest.raises(RteOdreDownloadError) | 0 | Proves malformed geojson feature or geometry is rejected using the exact source reproduced in section 7. |
| `test_standard_geojson_geometry_types_are_summarized` | none | none | 4 | Proves standard geojson geometry types are summarized using the exact source reproduced in section 7. |
| `test_point_requires_a_finite_numeric_position` | pytest.mark.parametrize(<br>    "coordinates",<br>    [None, "x", {}, [True, 2], [1, float("nan")], [1, float("inf")], [1]],<br>) | pytest.raises(RteOdreDownloadError, match="coordinate\|Point\|finite") | 0 | Proves point requires a finite numeric position using the exact source reproduced in section 7. |
| `test_nested_coordinate_geometries_reject_obvious_invalid_structure` | pytest.mark.parametrize(<br>    ("geometry_type", "coordinates"),<br>    [<br>        ("MultiPoint", None),<br>        ("LineString", "x"),<br>        ("MultiLineString", {}),<br>        ("Polygon", [1, 2]),<br>        ("MultiPolygon", [[[1, float("inf")]]]),<br>    ],<br>) | pytest.raises(RteOdreDownloadError, match="coordinate\|structure\|finite") | 0 | Proves nested coordinate geometries reject obvious invalid structure using the exact source reproduced in section 7. |
| `test_geometry_collection_members_are_validated_recursively` | none | pytest.raises(RteOdreDownloadError, match="coordinate\|Point") | 0 | Proves geometry collection members are validated recursively using the exact source reproduced in section 7. |
| `test_null_feature_geometries_are_accepted` | none | none | 3 | Proves null feature geometries are accepted using the exact source reproduced in section 7. |
| `test_lineage_sidecar_records_integrity` | none | none | 8 | Proves lineage sidecar records integrity using the exact source reproduced in section 7. |
| `test_invalid_cached_record_count_invalidates_cache` | pytest.mark.parametrize("cached_records_count", [-1, 1]) | none | 4 | Proves invalid cached record count invalidates cache using the exact source reproduced in section 7. |
| `test_cached_export_summary_mismatch_invalidates_cache` | none | none | 3 | Proves cached export summary mismatch invalidates cache using the exact source reproduced in section 7. |
| `test_corrupted_cached_export_triggers_refresh` | none | none | 3 | Proves corrupted cached export triggers refresh using the exact source reproduced in section 7. |
| `test_double_failure_preserves_recovery_and_next_run_uses_zero_network` | none | pytest.raises(RteOdreDownloadError, match="rollback"); pytest.raises(RteOdreDownloadError, match="backup\|recovery\|manual") | 5 | Proves double failure preserves recovery and next run uses zero network using the exact source reproduced in section 7. |
| `test_temporary_link_or_junction_cannot_modify_target_before_rte_network` | pytest.mark.parametrize("temporary_role", ["archive", "metadata"]); pytest.mark.parametrize("link_kind", ["symlink", "junction"]) | pytest.raises(RteOdreDownloadError, match="temporary\|link\|cache") | 2 | Proves temporary link or junction cannot modify target before rte network using the exact source reproduced in section 7. |
| `test_broken_recovery_symlink_rejects_rte_before_network` | none | pytest.raises(RteOdreDownloadError, match="backup\|recovery\|manual") | 1 | Proves broken recovery symlink rejects rte before network using the exact source reproduced in section 7. |
| `test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` | none | pytest.raises(RteOdreDownloadError, match="rollback") | 2 | Proves rte cleanup failure does not mask double failure recovery error using the exact source reproduced in section 7. |

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
import io
import json
from datetime import UTC, datetime, timedelta
from hashlib import sha256
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError

import pytest
import yaml
from pydantic import HttpUrl, ValidationError

from landscout.sources import rte_odre_fr
from landscout.sources.rte_odre_fr import (
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)

PROJECT_ROOT = Path(__file__).parents[2]
CONFIG_PATH = PROJECT_ROOT / "configs/sources/rte_odre_fr.yaml"
BASE_URL = "https://odre.opendatasoft.com/api/explore/v2.1"
DATASET_IDS = {
    "sites": "postes-electriques-rte",
    "overhead_lines": "lignes-aeriennes-rte-nv",
    "underground_lines": "lignes-souterraines-rte-nv",
}


def _config_data() -> dict:
    with CONFIG_PATH.open(encoding="utf-8") as stream:
        return yaml.safe_load(stream)


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


def _response(content: bytes) -> io.BytesIO:
    return io.BytesIO(content)


def _metadata_path(cache_dir: Path, dataset_id: str) -> Path:
    return cache_dir / f"{dataset_id}.geojson.metadata.json"


def _expire_cache(metadata_path: Path) -> None:
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["download_timestamp"] = (
        datetime.now(UTC) - timedelta(hours=169)
    ).isoformat()
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")


@pytest.fixture
def source_config() -> RteOdreSourceConfig:
    return load_rte_odre_source_config(CONFIG_PATH)


def test_valid_source_config_loads(source_config: RteOdreSourceConfig) -> None:
    assert source_config.provider == "RTE"
    assert source_config.portal == "ODRE"
    assert source_config.datasets.sites.dataset_id == "postes-electriques-rte"
    assert source_config.cache.max_age_hours == 168


def test_source_config_yaml_rejects_duplicate_keys(tmp_path: Path) -> None:
    path = tmp_path / "rte.yaml"
    path.write_text(
        CONFIG_PATH.read_text(encoding="utf-8") + "\nprovider: RTE\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Duplicate YAML key"):
        load_rte_odre_source_config(path)


def test_loaded_source_config_is_immutable(
    source_config: RteOdreSourceConfig,
) -> None:
    with pytest.raises(ValidationError, match="frozen"):
        source_config.provider = "UNTRUSTED"


@pytest.mark.parametrize(("field", "value"), [("provider", "IGN"), ("portal", "OTHER")])
def test_source_identity_is_exact(field: str, value: str) -> None:
    payload = _config_data()
    payload[field] = value

    with pytest.raises(ValidationError):
        RteOdreSourceConfig.model_validate(payload)


@pytest.mark.parametrize(
    "value",
    [True, "168", float("nan"), float("inf"), float("-inf")],
)
def test_cache_age_is_a_strict_finite_number(value: object) -> None:
    payload = _config_data()
    payload["cache"]["max_age_hours"] = value

    with pytest.raises(ValidationError):
        RteOdreSourceConfig.model_validate(payload)


def test_missing_dataset_id_fails() -> None:
    config_data = _config_data()
    del config_data["datasets"]["sites"]["dataset_id"]

    with pytest.raises(ValidationError):
        RteOdreSourceConfig.model_validate(config_data)


def test_empty_base_url_fails() -> None:
    config_data = _config_data()
    config_data["api"]["base_url"] = ""

    with pytest.raises(ValidationError):
        RteOdreSourceConfig.model_validate(config_data)


@pytest.mark.parametrize(
    "base_url",
    [
        "http://odre.opendatasoft.com/api/explore/v2.1",
        "https://example.com/api/explore/v2.1",
        "https://odre.opendatasoft.com/api/explore/v2.0",
        "https://user:secret@odre.opendatasoft.com/api/explore/v2.1",
        "https://odre.opendatasoft.com:8443/api/explore/v2.1",
        "https://odre.opendatasoft.com/api/explore/v2.1?redirect=elsewhere",
    ],
)
def test_api_base_is_pinned_to_the_official_https_origin_and_path(
    base_url: str,
) -> None:
    config_data = _config_data()
    config_data["api"]["base_url"] = base_url

    with pytest.raises(ValidationError):
        RteOdreSourceConfig.model_validate(config_data)


def test_mutated_loaded_api_origin_is_rejected_before_metadata_network(
    source_config: RteOdreSourceConfig,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    invalid_api = source_config.api.model_copy(
        update={"base_url": HttpUrl("https://unrelated.example/api/explore/v2.1")}
    )
    untrusted = source_config.model_copy(update={"api": invalid_api})
    network_calls = 0

    def fail_network(*args: object, **kwargs: object) -> object:
        nonlocal network_calls
        network_calls += 1
        raise AssertionError("network used after ODRE origin mutation")

    monkeypatch.setattr(rte_odre_fr, "open_safe_https", fail_network)

    with pytest.raises(RteOdreDownloadError, match="config|official|origin"):
        fetch_rte_odre_dataset_metadata(untrusted, "sites")

    assert network_calls == 0


def test_negative_cache_age_fails() -> None:
    config_data = _config_data()
    config_data["cache"]["max_age_hours"] = -1

    with pytest.raises(ValidationError):
        RteOdreSourceConfig.model_validate(config_data)


def test_unsupported_export_format_fails() -> None:
    config_data = _config_data()
    config_data["datasets"]["sites"]["preferred_format"] = "csv"

    with pytest.raises(ValidationError):
        RteOdreSourceConfig.model_validate(config_data)


@pytest.mark.parametrize(
    ("logical_name", "dataset_id"),
    list(DATASET_IDS.items()),
)
def test_build_export_url(
    source_config: RteOdreSourceConfig, logical_name: str, dataset_id: str
) -> None:
    url = build_rte_odre_export_url(source_config, logical_name)  # type: ignore[arg-type]

    assert url == f"{BASE_URL}/catalog/datasets/{dataset_id}/exports/geojson"


def test_build_metadata_url(source_config: RteOdreSourceConfig) -> None:
    assert build_rte_odre_metadata_url(source_config, "sites") == (
        f"{BASE_URL}/catalog/datasets/postes-electriques-rte"
    )


def test_export_url_uses_configured_dataset_id() -> None:
    config_data = _config_data()
    config_data["datasets"]["sites"]["dataset_id"] = "configured-sites"
    config = RteOdreSourceConfig.model_validate(config_data)

    assert build_rte_odre_export_url(config, "sites").endswith(
        "/catalog/datasets/configured-sites/exports/geojson"
    )


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


def test_metadata_response_rejects_duplicate_json_keys(
    source_config: RteOdreSourceConfig,
) -> None:
    dataset_id = DATASET_IDS["sites"]
    content = _metadata_content(dataset_id).decode("utf-8")
    marker = f'"dataset_id": "{dataset_id}"'
    content = content.replace(marker, f"{marker}, {marker}", 1)
    with (
        patch(
            "landscout.sources.rte_odre_fr.open_safe_https",
            return_value=_response(content.encode("utf-8")),
        ),
        pytest.raises(RteOdreDownloadError, match="request|JSON"),
    ):
        fetch_rte_odre_dataset_metadata(source_config, "sites")


@pytest.mark.parametrize("constant", ["NaN", "Infinity", "-Infinity"])
def test_metadata_response_rejects_nonfinite_json_constants(
    source_config: RteOdreSourceConfig,
    constant: str,
) -> None:
    dataset_id = DATASET_IDS["sites"]
    content = _metadata_content(dataset_id).decode("utf-8")
    content = content[:-1] + f', "untrusted": {constant}}}'
    with (
        patch(
            "landscout.sources.rte_odre_fr.open_safe_https",
            return_value=_response(content.encode("utf-8")),
        ),
        pytest.raises(RteOdreDownloadError, match="request|JSON"),
    ):
        fetch_rte_odre_dataset_metadata(source_config, "sites")


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


@pytest.mark.parametrize("records_count", [1, 3])
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


@pytest.mark.parametrize(
    ("feature_count", "null_geometry_count", "non_null_geometry_count"),
    [
        (-1, 0, 0),
        (1, -1, 2),
        (1, 0, -1),
        (2, 0, 1),
    ],
)
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


@pytest.mark.parametrize("mutation", ["duplicate_key", "nonexact_file_size"])
def test_untrusted_cache_metadata_is_rejected_and_refreshed(
    tmp_path: Path,
    source_config: RteOdreSourceConfig,
    mutation: str,
) -> None:
    dataset_id = DATASET_IDS["sites"]
    responses = [
        _response(_metadata_content(dataset_id)),
        _response(_feature_collection()),
        _response(_metadata_content(dataset_id)),
        _response(_feature_collection()),
    ]
    with patch(
        "landscout.sources.rte_odre_fr.open_safe_https",
        side_effect=responses,
    ) as opener:
        first = download_rte_odre_dataset("sites", source_config, tmp_path)
        metadata_path = _metadata_path(tmp_path, dataset_id)
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        if mutation == "duplicate_key":
            encoded = json.dumps(metadata, separators=(",", ":"))
            marker = f'"sha256":"{first.sha256}"'
            metadata_path.write_text(
                encoded.replace(marker, f"{marker},{marker}", 1),
                encoding="utf-8",
            )
        else:
            metadata["file_size"] = float(first.file_size)
            metadata_path.write_text(json.dumps(metadata), encoding="utf-8")

        refreshed = download_rte_odre_dataset("sites", source_config, tmp_path)

    assert opener.call_count == 4
    assert refreshed.cache_hit is False


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


@pytest.mark.parametrize(
    "invalid_content",
    [
        b"{not-json",
        json.dumps({"type": "Point", "coordinates": [1, 2]}).encode(),
        json.dumps({"type": "FeatureCollection"}).encode(),
    ],
)
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


def test_geojson_export_rejects_duplicate_json_keys(tmp_path: Path) -> None:
    path = tmp_path / "duplicate.geojson"
    path.write_bytes(
        b'{"type":"FeatureCollection","type":"FeatureCollection","features":[]}'
    )

    with pytest.raises(RteOdreDownloadError, match="JSON"):
        rte_odre_fr._validate_geojson(path)


@pytest.mark.parametrize(
    "feature",
    [
        123,
        "feature",
        {"geometry": None},
        {"type": "NotFeature", "geometry": None},
        {"type": "Feature", "geometry": {}},
        {"type": "Feature", "geometry": {"type": ""}},
        {"type": "Feature", "geometry": {"type": "SOMETHING_RANDOM"}},
        {"type": "Feature", "geometry": {"type": "Point"}},
        {"type": "Feature", "geometry": {"type": "GeometryCollection"}},
        {"type": "Feature", "geometry": 123},
    ],
)
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
    assert summary.geometry_types == tuple(
        sorted((*coordinate_types, "GeometryCollection"))
    )


@pytest.mark.parametrize(
    "coordinates",
    [None, "x", {}, [True, 2], [1, float("nan")], [1, float("inf")], [1]],
)
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


@pytest.mark.parametrize(
    ("geometry_type", "coordinates"),
    [
        ("MultiPoint", None),
        ("LineString", "x"),
        ("MultiLineString", {}),
        ("Polygon", [1, 2]),
        ("MultiPolygon", [[[1, float("inf")]]]),
    ],
)
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
                            "geometries": [{"type": "Point", "coordinates": None}],
                        },
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    with pytest.raises(RteOdreDownloadError, match="coordinate|Point"):
        rte_odre_fr._validate_geojson(path)


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


@pytest.mark.parametrize("cached_records_count", [-1, 1])
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


@pytest.mark.parametrize("temporary_role", ["archive", "metadata"])
@pytest.mark.parametrize("link_kind", ["symlink", "junction"])
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
        return (link_kind == "symlink" and path == unsafe_path) or original_is_symlink(
            path
        )

    def simulated_is_junction(path: Path) -> bool:
        return (
            link_kind == "junction" and path == unsafe_path
        ) or original_is_junction(path)

    def simulated_symlink_open(path: Path, *args: object, **kwargs: object) -> object:
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

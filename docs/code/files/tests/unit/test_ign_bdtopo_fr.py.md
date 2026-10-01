# `tests/unit/test_ign_bdtopo_fr.py`

## File identity

- Repository path: `tests/unit/test_ign_bdtopo_fr.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Exercises the bounded synthetic IGN source contracts and assertions described below, not exhaustive or official-source coverage.
- Source SHA256: `39d0e303aec55a24866a2c41b32bdb215203b4280fb748421454120eae24f078`
- Source SHA256 basis: `git-content`
- R15 verification basis: `8bef62ab9b6eef185bab526a046b4a7dbbea42a1`; source bytes unchanged.

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for ign bdtopo fr; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## R15 fixtures, aliases and proof limits

This module declares 76 top-level test functions and one pytest.fixture (source_config). Other helpers, _FakeArchive and nested callbacks are not additional tests or fixtures. A fixture parameter named source_config is an injected IgnBdTopoSourceConfig instance, not the fixture callable's namespace. load_untrusted_ign_bdtopo_layer is an alias of the private raw reader. Public loading tests are identified separately below.

Most I/O scenarios create genuine temporary GeoPackages with Pyogrio and genuine 7z files with py7zr, using a config derived from the checked-in YAML but a synthetic URL. open_safe_https is replaced by a nondelegating BytesIO return_value or a raising sentinel, so these tests do not exercise live DNS/TLS/redirects or acquire an official archive. _FakeArchive/SimpleNamespace scenarios only exercise private member-metadata validation. Publication callbacks that call original_replace really delegate unaffected filesystem operations; the .part-link test instead returns precomputed archive integrity from a nondelegating mock.

Every verified scenario below states its boundary, mutation and assertions. A Python assert count excludes helper calls such as assert_not_called and assert_geodataframe_equal. Model-only failures, extraction cache rebuilds and public-loader failures are different evidence. Adding a physical layer also changes file bytes and can fail the hash gate before layer-inventory comparison. Byte-string tampering with a stale SHA does not independently test semantic attribute validation. Predicate-simulated links are not actual OS links; no general race-free snapshot or exhaustive Z/M/WKB preservation claim follows.

Exact source blocks remain unchanged. No application behavior, checked-in test, config, schema, snapshot, cache or dependency is changed by this documentary audit. The package/export checks in this file are bounded road API assertions, not complete proof of every source export.

## 2. Purpose and architectural position

Exercises the bounded synthetic IGN source contracts and assertions described below, not exhaustive or official-source coverage.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `import io`
- `import json`
- `from dataclasses import replace`
- `from datetime import UTC, datetime, timedelta`
- `from hashlib import sha256`
- `from pathlib import Path`
- `from types import SimpleNamespace`
- `from unittest.mock import patch`
- `from urllib.error import HTTPError`

### Third-party packages

- `import geopandas as gpd`
- `import py7zr`
- `import pyogrio`
- `import pytest`
- `import yaml`
- `from geopandas.testing import assert_geodataframe_equal`
- `from pydantic import ValidationError`
- `from shapely.geometry import LineString, MultiLineString, MultiPolygon, Polygon`

### Internal LandScout imports

- `from landscout import sources`
- `from landscout.sources import ign_bdtopo_fr`
- `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- `from landscout.sources.ign_bdtopo_fr import (
    _load_untrusted_ign_bdtopo_layer as load_untrusted_ign_bdtopo_layer,
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
CONFIG_PATH = PROJECT_ROOT / "configs/sources/ign_bdtopo_fr.yaml"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `SYNTHETIC_SOURCE_URL`

- Category: module constant or closed domain.
- Exact declaration:

```python
SYNTHETIC_SOURCE_URL = "https://example.test/BDTOPO_TEST_D031.7z"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `LINE_LAYER`

- Category: module constant or closed domain.
- Exact declaration:

```python
LINE_LAYER = "LIGNE_ELECTRIQUE"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `POST_LAYER`

- Category: module constant or closed domain.
- Exact declaration:

```python
POST_LAYER = "POSTE_DE_TRANSFORMATION"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `DEPARTMENT_LAYER`

- Category: module constant or closed domain.
- Exact declaration:

```python
DEPARTMENT_LAYER = "DEPARTEMENT"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `ROAD_LAYER`

- Category: module constant or closed domain.
- Exact declaration:

```python
ROAD_LAYER = "TRONCON_DE_ROUTE"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

<a id="r15--fakearchive"></a>
### `_FakeArchive`

Qualified owner: `tests.unit.test_ign_bdtopo_fr._FakeArchive`. Source lines 1581–1590.

Exact declaration:

```python
class _FakeArchive:
```

**Verified purpose:** Mutable fake implementing only needs_password and list. _infos retains the caller list alias and _encrypted the supplied flag; it is not a validated immutable source envelope, file parser or context manager.

- Exact decorators: none.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `_infos` | `assigned instance field` | `infos` | `self._infos = infos` |
| `_encrypted` | `assigned instance field` | `encrypted` | `self._encrypted = encrypted` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `tests.unit.test_ign_bdtopo_fr::test_7z_windows_unsafe_member_names_fail_closed` via `_FakeArchive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_7z_windows_unsafe_member_names_fail_closed` via `_FakeArchive`
- constructor call: `tests.unit.test_ign_bdtopo_fr::test_7z_casefold_and_nfkc_destination_collisions_fail` via `_FakeArchive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_7z_casefold_and_nfkc_destination_collisions_fail` via `_FakeArchive`
- constructor call: `tests.unit.test_ign_bdtopo_fr::test_7z_nfkc_separator_destinations_fail_closed` via `_FakeArchive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_7z_nfkc_separator_destinations_fail_closed` via `_FakeArchive`
- constructor call: `tests.unit.test_ign_bdtopo_fr::test_7z_parent_file_conflict_fails_closed` via `_FakeArchive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_7z_parent_file_conflict_fails_closed` via `_FakeArchive`
- constructor call: `tests.unit.test_ign_bdtopo_fr::test_7z_encrypted_archive_fails_closed` via `_FakeArchive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_7z_encrypted_archive_fails_closed` via `_FakeArchive`

**Exact class source**

```python
class _FakeArchive:
    def __init__(self, infos: list[SimpleNamespace], *, encrypted: bool = False):
        self._infos = infos
        self._encrypted = encrypted

    def needs_password(self) -> bool:
        return self._encrypted

    def list(self) -> list[SimpleNamespace]:
        return self._infos
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

<a id="r15--config-data"></a>
### `_config_data`

Qualified owner: `tests.unit.test_ign_bdtopo_fr._config_data`. Source lines 52–54.

**Verified purpose:** Read the checked-in YAML through yaml.safe_load into a mutable test payload. This helper does not use the production duplicate-rejecting YAML loader or construct a validated model.

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
- direct call: `tests.unit.test_ign_bdtopo_fr::test_invalid_department_coverage_config_fails` via `_config_data`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_invalid_department_coverage_config_fails` via `_config_data`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_missing_required_source_field_fails` via `_config_data`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_required_source_field_fails` via `_config_data`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_invalid_source_configuration_fails` via `_config_data`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_invalid_source_configuration_fails` via `_config_data`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_unknown_source_config_field_is_rejected` via `_config_data`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_unknown_source_config_field_is_rejected` via `_config_data`

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

<a id="r15--synthetic-config"></a>
### `_synthetic_config`

Qualified owner: `tests.unit.test_ign_bdtopo_fr._synthetic_config`. Source lines 57–74.

**Verified purpose:** Dump the fixture config to JSON-mode values, replace the URL with example.test, remove checksum_url and expected size, optionally pin the supplied SHA256, then model-validate a new config. The original config is not mutated; no network occurs.

**Exact signature**

```python
def _synthetic_config(
    source_config: IgnBdTopoSourceConfig,
    *,
    official_checksum: str | None = None,
) -> IgnBdTopoSourceConfig:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoSourceConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |
| `official_checksum` | keyword-only | `str \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `IgnBdTopoSourceConfig.model_validate(content)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_ign_bdtopo_fr::_extracted_fixture` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::_extracted_fixture` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_successful_archive_download_persists_sha256` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_successful_archive_download_persists_sha256` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_fresh_cache_is_reused_without_network` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_fresh_cache_is_reused_without_network` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_stale_recovery_backup_rejects_cache_before_network` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_stale_recovery_backup_rejects_cache_before_network` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_expired_cache_is_refreshed` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_expired_cache_is_refreshed` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_failed_refresh_preserves_valid_cache` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_failed_refresh_preserves_valid_cache` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_corrupt_refresh_preserves_valid_cache` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_corrupt_refresh_preserves_valid_cache` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_metadata_publication_failure_restores_previous_cache_pair` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_metadata_publication_failure_restores_previous_cache_pair` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_official_checksum_mismatch_is_rejected` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_official_checksum_mismatch_is_rejected` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_unsafe_parent_archive_member_is_rejected` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_unsafe_parent_archive_member_is_rejected` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_synthetic_archive_extracts_and_discovers_required_layers` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_synthetic_archive_extracts_and_discovers_required_layers` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_default_extraction_path_is_short_and_content_addressed` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_default_extraction_path_is_short_and_content_addressed` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_electricity_loader_retains_both_layer_counts` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_electricity_loader_retains_both_layer_counts` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_layer_discovery_loads_selected_physical_layer` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_layer_discovery_loads_selected_physical_layer` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_missing_road_layer_fails_safely` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_road_layer_fails_safely` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_ambiguous_road_layer_fails_safely` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_ambiguous_road_layer_fails_safely` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_wrong_archive_config_department` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_wrong_archive_config_department` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_changed_layer_inventory` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_changed_layer_inventory` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_geographic_crs` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_geographic_crs` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_loader_preserves_lambert93_lines_unchanged` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_preserves_lambert93_lines_unchanged` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_layer_does_not_change_electricity_loading_or_cache_shape` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_layer_does_not_change_electricity_loading_or_cache_shape` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_download_cache_reader_rejects_noncanonical_json_and_refreshes` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_download_cache_reader_rejects_noncanonical_json_and_refreshes` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_loader_selects_configured_identity` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_loader_selects_configured_identity` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_one_authoritative_feature` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_one_authoritative_feature` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_configured_identity_field` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_configured_identity_field` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_missing_department_coverage_layer_fails` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_department_coverage_layer_fails` via `_synthetic_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_layer_discovery_must_be_unambiguous` via `_synthetic_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_layer_discovery_must_be_unambiguous` via `_synthetic_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `source_config.model_dump` | `pydantic.BaseModel.model_dump` (inherited by `landscout.sources.ign_bdtopo_fr.IgnBdTopoSourceConfig`) (inherited Pydantic method on the injected model) |
| `content.update` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoSourceConfig.model_validate` | `pydantic.BaseModel.model_validate` (inherited by `landscout.sources.ign_bdtopo_fr.IgnBdTopoSourceConfig`) |

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
| In-memory mutation | `content.update(<br>        {<br>            "source_url": SYNTHETIC_SOURCE_URL,<br>            "checksum_url": None,<br>            "official_checksum_algorithm": (<br>                "sha256" if official_checksum is not None else None<br>            ),<br>            "official_checksum": official_checksum,<br>            "expected_archive_size_bytes": None,<br>        }<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _synthetic_config(
    source_config: IgnBdTopoSourceConfig,
    *,
    official_checksum: str | None = None,
) -> IgnBdTopoSourceConfig:
    content = source_config.model_dump(mode="json")
    content.update(
        {
            "source_url": SYNTHETIC_SOURCE_URL,
            "checksum_url": None,
            "official_checksum_algorithm": (
                "sha256" if official_checksum is not None else None
            ),
            "official_checksum": official_checksum,
            "expected_archive_size_bytes": None,
        }
    )
    return IgnBdTopoSourceConfig.model_validate(content)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15--write-gpkg"></a>
### `_write_gpkg`

Qualified owner: `tests.unit.test_ign_bdtopo_fr._write_gpkg`. Source lines 77–219.

**Verified purpose:** Create parent directories and real temporary GPKG layers through Pyogrio. Defaults create two electricity layers (valid/null lines and posts); switches add an invalid post, roads and departments. Road kind selects line, multiline or mixed geometries. road_crs or crs and department_codes/geometries or defaults use truthiness, so empty lists select defaults. IDs R_LINE/R_MULTI do not themselves prove geometry kinds. These are synthetic attributes/coordinates, not official IGN data.

**Exact signature**

```python
def _write_gpkg(
    path: Path,
    *,
    include_lines: bool = True,
    include_posts: bool = True,
    line_layer: str = LINE_LAYER,
    post_layer: str = POST_LAYER,
    crs: str | None = "EPSG:2154",
    invalid_post: bool = False,
    include_department: bool = False,
    department_layer: str = DEPARTMENT_LAYER,
    department_codes: list[str] | None = None,
    department_geometries: list[object] | None = None,
    include_roads: bool = False,
    road_layer: str = ROAD_LAYER,
    road_crs: str | None = None,
    road_geometry_kind: str = "mixed",
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |
| `include_lines` | keyword-only | `bool` | `True` |
| `include_posts` | keyword-only | `bool` | `True` |
| `line_layer` | keyword-only | `str` | `LINE_LAYER` |
| `post_layer` | keyword-only | `str` | `POST_LAYER` |
| `crs` | keyword-only | `str \| None` | `'EPSG:2154'` |
| `invalid_post` | keyword-only | `bool` | `False` |
| `include_department` | keyword-only | `bool` | `False` |
| `department_layer` | keyword-only | `str` | `DEPARTMENT_LAYER` |
| `department_codes` | keyword-only | `list[str] \| None` | `None` |
| `department_geometries` | keyword-only | `list[object] \| None` | `None` |
| `include_roads` | keyword-only | `bool` | `False` |
| `road_layer` | keyword-only | `str` | `ROAD_LAYER` |
| `road_crs` | keyword-only | `str \| None` | `None` |
| `road_geometry_kind` | keyword-only | `str` | `'mixed'` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_ign_bdtopo_fr::_synthetic_archive_bytes` via `_write_gpkg`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::_synthetic_archive_bytes` via `_write_gpkg`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_unsafe_parent_archive_member_is_rejected` via `_write_gpkg`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_unsafe_parent_archive_member_is_rejected` via `_write_gpkg`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_geopackage_is_discovered_recursively` via `_write_gpkg`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_geopackage_is_discovered_recursively` via `_write_gpkg`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_multiple_geopackages_are_rejected_as_ambiguous` via `_write_gpkg`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_multiple_geopackages_are_rejected_as_ambiguous` via `_write_gpkg`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_real_layer_names_are_listed_and_discovered` via `_write_gpkg`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_real_layer_names_are_listed_and_discovered` via `_write_gpkg`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_missing_electric_line_layer_fails` via `_write_gpkg`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_electric_line_layer_fails` via `_write_gpkg`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_missing_transformation_post_layer_fails` via `_write_gpkg`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_transformation_post_layer_fails` via `_write_gpkg`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_ambiguous_electric_line_layers_fail` via `_write_gpkg`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_ambiguous_electric_line_layers_fail` via `_write_gpkg`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_layer_loader_retains_crs_counts_and_null_geometries` via `_write_gpkg`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_layer_loader_retains_crs_counts_and_null_geometries` via `_write_gpkg`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_invalid_geometry_is_preserved_without_repair` via `_write_gpkg`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_invalid_geometry_is_preserved_without_repair` via `_write_gpkg`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_geographic_crs_is_rejected` via `_write_gpkg`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_geographic_crs_is_rejected` via `_write_gpkg`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_ambiguous_road_layer_fails_safely` via `_write_gpkg`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_ambiguous_road_layer_fails_safely` via `_write_gpkg`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_one_authoritative_feature` via `_write_gpkg`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_one_authoritative_feature` via `_write_gpkg`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_layer_discovery_must_be_unambiguous` via `_write_gpkg`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_layer_discovery_must_be_unambiguous` via `_write_gpkg`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.parent.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `LineString` | `shapely.geometry.LineString` |
| `pyogrio.write_dataframe` | `pyogrio.write_dataframe` |
| `Polygon` | `shapely.geometry.Polygon` |
| `geometries.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `object_ids.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `MultiLineString` | `shapely.geometry.MultiLineString` |
| `MultiPolygon` | `shapely.geometry.MultiPolygon` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | path.parent.mkdir and pyogrio.write_dataframe create/append genuine synthetic GPKG layers. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | Constructs synthetic LineString/MultiLineString/Polygon/MultiPolygon and GeoDataFrame CRS metadata; no parcel-distance calculation. |
| External process/environment | None directly present. |
| In-memory mutation | `geometries.append(invalid)`<br>`object_ids.append("P_INVALID")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _write_gpkg(
    path: Path,
    *,
    include_lines: bool = True,
    include_posts: bool = True,
    line_layer: str = LINE_LAYER,
    post_layer: str = POST_LAYER,
    crs: str | None = "EPSG:2154",
    invalid_post: bool = False,
    include_department: bool = False,
    department_layer: str = DEPARTMENT_LAYER,
    department_codes: list[str] | None = None,
    department_geometries: list[object] | None = None,
    include_roads: bool = False,
    road_layer: str = ROAD_LAYER,
    road_crs: str | None = None,
    road_geometry_kind: str = "mixed",
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    layer_written = False
    if include_lines:
        lines = gpd.GeoDataFrame(
            {
                "object_id": ["L_VALID", "L_NULL"],
                "nature": ["HT", "UNKNOWN"],
                "tension": ["225 kV", None],
            },
            geometry=[LineString([(0, 0), (100, 100)]), None],
            crs=crs,
        )
        pyogrio.write_dataframe(
            lines,
            path,
            layer=line_layer,
            driver="GPKG",
        )
        layer_written = True
    if include_posts:
        invalid = Polygon([(0, 0), (20, 20), (20, 0), (0, 20), (0, 0)])
        geometries = [
            Polygon([(0, 0), (0, 20), (20, 20), (20, 0), (0, 0)]),
            None,
        ]
        object_ids = ["P_VALID", "P_NULL"]
        if invalid_post:
            geometries.append(invalid)
            object_ids.append("P_INVALID")
        posts = gpd.GeoDataFrame(
            {
                "object_id": object_ids,
                "nature": ["POSTE"] * len(object_ids),
            },
            geometry=geometries,
            crs=crs,
        )
        pyogrio.write_dataframe(
            posts,
            path,
            layer=post_layer,
            driver="GPKG",
            append=layer_written,
        )
        layer_written = True
    if include_roads:
        if road_geometry_kind == "line":
            road_geometries = [
                LineString([(0, 0), (100, 100)]),
                LineString([(200, 200), (300, 260)]),
            ]
        elif road_geometry_kind == "multiline":
            road_geometries = [
                MultiLineString([[(0, 0), (100, 100)]]),
                MultiLineString(
                    [
                        [(200, 200), (250, 250)],
                        [(250, 250), (300, 260)],
                    ]
                ),
            ]
        else:
            road_geometries = [
                LineString([(0, 0), (100, 100)]),
                MultiLineString(
                    [
                        [(200, 200), (250, 250)],
                        [(250, 250), (300, 260)],
                    ]
                ),
            ]
        roads = gpd.GeoDataFrame(
            {
                "object_id": ["R_LINE", "R_MULTI"],
                "nature": ["Route à 1 chaussée", "Bretelle"],
            },
            geometry=road_geometries,
            crs=road_crs or crs,
        )
        pyogrio.write_dataframe(
            roads,
            path,
            layer=road_layer,
            driver="GPKG",
            append=layer_written,
        )
        layer_written = True
    if include_department:
        codes = department_codes or ["31", "32"]
        geometries = (
            department_geometries
            or [
                MultiPolygon(
                    [Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)])]
                ),
                MultiPolygon(
                    [
                        Polygon(
                            [
                                (1000, 0),
                                (1000, 1000),
                                (2000, 1000),
                                (2000, 0),
                                (1000, 0),
                            ]
                        )
                    ]
                ),
            ][: len(codes)]
        )
        departments = gpd.GeoDataFrame(
            {
                "code_insee": codes,
                "nom_officiel": [f"Department {code}" for code in codes],
            },
            geometry=geometries,
            crs=crs,
        )
        pyogrio.write_dataframe(
            departments,
            path,
            layer=department_layer,
            driver="GPKG",
            append=layer_written,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15--pack-7z"></a>
### `_pack_7z`

Qualified owner: `tests.unit.test_ign_bdtopo_fr._pack_7z`. Source lines 222–230.

**Verified purpose:** Create parents, write each supplied path/member-name pair to a real py7zr archive in caller order, then return its bytes. This is in-process compression and filesystem I/O, not a subprocess or download.

**Exact signature**

```python
def _pack_7z(
    archive_path: Path,
    members: list[tuple[Path, str]],
) -> bytes:
```

- Exact decorators: none.
- Declared return annotation: `bytes`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `archive_path` | positional-or-keyword | `Path` | `required` |
| `members` | positional-or-keyword | `list[tuple[Path, str]]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `archive_path.read_bytes()`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_ign_bdtopo_fr::_synthetic_archive_bytes` via `_pack_7z`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::_synthetic_archive_bytes` via `_pack_7z`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_unsafe_parent_archive_member_is_rejected` via `_pack_7z`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_unsafe_parent_archive_member_is_rejected` via `_pack_7z`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_ambiguous_road_layer_fails_safely` via `_pack_7z`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_ambiguous_road_layer_fails_safely` via `_pack_7z`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_one_authoritative_feature` via `_pack_7z`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_one_authoritative_feature` via `_pack_7z`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_layer_discovery_must_be_unambiguous` via `_pack_7z`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_layer_discovery_must_be_unambiguous` via `_pack_7z`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `archive_path.parent.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `py7zr.SevenZipFile` | `py7zr.SevenZipFile` |
| `archive.write` | `unresolved local/third-party receiver; no ownership inferred` |
| `archive_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `py7zr.SevenZipFile`<br>`archive_path.read_bytes` |
| Filesystem/archive write or publication | archive_path.parent.mkdir, py7zr.SevenZipFile(mode="w") and archive.write create the 7z file. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | In-process py7zr compression; no subprocess launch. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _pack_7z(
    archive_path: Path,
    members: list[tuple[Path, str]],
) -> bytes:
    archive_path.parent.mkdir(parents=True, exist_ok=True)
    with py7zr.SevenZipFile(archive_path, "w") as archive:
        for source, archive_name in members:
            archive.write(source, arcname=archive_name)
    return archive_path.read_bytes()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15--synthetic-archive-bytes"></a>
### `_synthetic_archive_bytes`

Qualified owner: `tests.unit.test_ign_bdtopo_fr._synthetic_archive_bytes`. Source lines 233–258.

**Verified purpose:** Write a synthetic GPKG and pack it at BDTOPO_TEST/GPKG/BDTOPO_TEST.gpkg in fixture.7z. Unlike _write_gpkg defaults, this helper defaults to all four physical roles; switches are forwarded. Return real archive bytes, not an official snapshot.

**Exact signature**

```python
def _synthetic_archive_bytes(
    root: Path,
    *,
    include_lines: bool = True,
    include_posts: bool = True,
    invalid_post: bool = False,
    include_department: bool = True,
    include_roads: bool = True,
    road_crs: str | None = None,
    road_geometry_kind: str = "mixed",
) -> bytes:
```

- Exact decorators: none.
- Declared return annotation: `bytes`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `root` | positional-or-keyword | `Path` | `required` |
| `include_lines` | keyword-only | `bool` | `True` |
| `include_posts` | keyword-only | `bool` | `True` |
| `invalid_post` | keyword-only | `bool` | `False` |
| `include_department` | keyword-only | `bool` | `True` |
| `include_roads` | keyword-only | `bool` | `True` |
| `road_crs` | keyword-only | `str \| None` | `None` |
| `road_geometry_kind` | keyword-only | `str` | `'mixed'` |

**Return and exception contract**

- Exact observed return expressions:
  - `_pack_7z(<br>        root / "fixture.7z",<br>        [(gpkg_path, "BDTOPO_TEST/GPKG/BDTOPO_TEST.gpkg")],<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_ign_bdtopo_fr::_extracted_fixture` via `_synthetic_archive_bytes`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::_extracted_fixture` via `_synthetic_archive_bytes`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_successful_archive_download_persists_sha256` via `_synthetic_archive_bytes`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_successful_archive_download_persists_sha256` via `_synthetic_archive_bytes`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum` via `_synthetic_archive_bytes`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum` via `_synthetic_archive_bytes`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_fresh_cache_is_reused_without_network` via `_synthetic_archive_bytes`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_fresh_cache_is_reused_without_network` via `_synthetic_archive_bytes`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_stale_recovery_backup_rejects_cache_before_network` via `_synthetic_archive_bytes`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_stale_recovery_backup_rejects_cache_before_network` via `_synthetic_archive_bytes`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_expired_cache_is_refreshed` via `_synthetic_archive_bytes`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_expired_cache_is_refreshed` via `_synthetic_archive_bytes`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_failed_refresh_preserves_valid_cache` via `_synthetic_archive_bytes`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_failed_refresh_preserves_valid_cache` via `_synthetic_archive_bytes`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_corrupt_refresh_preserves_valid_cache` via `_synthetic_archive_bytes`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_corrupt_refresh_preserves_valid_cache` via `_synthetic_archive_bytes`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_metadata_publication_failure_restores_previous_cache_pair` via `_synthetic_archive_bytes`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_metadata_publication_failure_restores_previous_cache_pair` via `_synthetic_archive_bytes`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_synthetic_archive_bytes`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_synthetic_archive_bytes`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_official_checksum_mismatch_is_rejected` via `_synthetic_archive_bytes`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_official_checksum_mismatch_is_rejected` via `_synthetic_archive_bytes`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_synthetic_archive_extracts_and_discovers_required_layers` via `_synthetic_archive_bytes`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_synthetic_archive_extracts_and_discovers_required_layers` via `_synthetic_archive_bytes`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_default_extraction_path_is_short_and_content_addressed` via `_synthetic_archive_bytes`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_default_extraction_path_is_short_and_content_addressed` via `_synthetic_archive_bytes`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_electricity_loader_retains_both_layer_counts` via `_synthetic_archive_bytes`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_electricity_loader_retains_both_layer_counts` via `_synthetic_archive_bytes`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_layer_discovery_loads_selected_physical_layer` via `_synthetic_archive_bytes`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_layer_discovery_loads_selected_physical_layer` via `_synthetic_archive_bytes`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_missing_road_layer_fails_safely` via `_synthetic_archive_bytes`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_road_layer_fails_safely` via `_synthetic_archive_bytes`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_wrong_archive_config_department` via `_synthetic_archive_bytes`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_wrong_archive_config_department` via `_synthetic_archive_bytes`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_changed_layer_inventory` via `_synthetic_archive_bytes`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_changed_layer_inventory` via `_synthetic_archive_bytes`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_geographic_crs` via `_synthetic_archive_bytes`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_geographic_crs` via `_synthetic_archive_bytes`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_loader_preserves_lambert93_lines_unchanged` via `_synthetic_archive_bytes`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_preserves_lambert93_lines_unchanged` via `_synthetic_archive_bytes`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_layer_does_not_change_electricity_loading_or_cache_shape` via `_synthetic_archive_bytes`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_layer_does_not_change_electricity_loading_or_cache_shape` via `_synthetic_archive_bytes`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_download_cache_reader_rejects_noncanonical_json_and_refreshes` via `_synthetic_archive_bytes`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_download_cache_reader_rejects_noncanonical_json_and_refreshes` via `_synthetic_archive_bytes`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_loader_selects_configured_identity` via `_synthetic_archive_bytes`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_loader_selects_configured_identity` via `_synthetic_archive_bytes`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_configured_identity_field` via `_synthetic_archive_bytes`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_configured_identity_field` via `_synthetic_archive_bytes`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_missing_department_coverage_layer_fails` via `_synthetic_archive_bytes`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_department_coverage_layer_fails` via `_synthetic_archive_bytes`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_direct_consumers_reject_same_inventory_content_tampering` via `_synthetic_archive_bytes`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_direct_consumers_reject_same_inventory_content_tampering` via `_synthetic_archive_bytes`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_write_gpkg` | `tests.unit.test_ign_bdtopo_fr._write_gpkg` |
| `_pack_7z` | `tests.unit.test_ign_bdtopo_fr._pack_7z` |

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
def _synthetic_archive_bytes(
    root: Path,
    *,
    include_lines: bool = True,
    include_posts: bool = True,
    invalid_post: bool = False,
    include_department: bool = True,
    include_roads: bool = True,
    road_crs: str | None = None,
    road_geometry_kind: str = "mixed",
) -> bytes:
    gpkg_path = root / "fixture" / "BDTOPO_TEST.gpkg"
    _write_gpkg(
        gpkg_path,
        include_lines=include_lines,
        include_posts=include_posts,
        invalid_post=invalid_post,
        include_department=include_department,
        include_roads=include_roads,
        road_crs=road_crs,
        road_geometry_kind=road_geometry_kind,
    )
    return _pack_7z(
        root / "fixture.7z",
        [(gpkg_path, "BDTOPO_TEST/GPKG/BDTOPO_TEST.gpkg")],
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15--response"></a>
### `_response`

Qualified owner: `tests.unit.test_ign_bdtopo_fr._response`. Source lines 261–262.

**Verified purpose:** Return a fresh io.BytesIO over supplied bytes for the mocked HTTPS opener. This simulates a context-managed byte stream, not DNS, TLS, response headers, redirects or status validation.

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
- direct call: `tests.unit.test_ign_bdtopo_fr::_extracted_fixture` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::_extracted_fixture` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_successful_archive_download_persists_sha256` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_successful_archive_download_persists_sha256` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_fresh_cache_is_reused_without_network` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_fresh_cache_is_reused_without_network` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_stale_recovery_backup_rejects_cache_before_network` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_stale_recovery_backup_rejects_cache_before_network` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_expired_cache_is_refreshed` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_expired_cache_is_refreshed` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_failed_refresh_preserves_valid_cache` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_failed_refresh_preserves_valid_cache` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_corrupt_refresh_preserves_valid_cache` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_corrupt_refresh_preserves_valid_cache` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_metadata_publication_failure_restores_previous_cache_pair` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_metadata_publication_failure_restores_previous_cache_pair` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_official_checksum_mismatch_is_rejected` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_official_checksum_mismatch_is_rejected` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_unsafe_parent_archive_member_is_rejected` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_unsafe_parent_archive_member_is_rejected` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_synthetic_archive_extracts_and_discovers_required_layers` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_synthetic_archive_extracts_and_discovers_required_layers` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_default_extraction_path_is_short_and_content_addressed` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_default_extraction_path_is_short_and_content_addressed` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_electricity_loader_retains_both_layer_counts` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_electricity_loader_retains_both_layer_counts` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_layer_discovery_loads_selected_physical_layer` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_layer_discovery_loads_selected_physical_layer` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_missing_road_layer_fails_safely` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_road_layer_fails_safely` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_ambiguous_road_layer_fails_safely` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_ambiguous_road_layer_fails_safely` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_wrong_archive_config_department` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_wrong_archive_config_department` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_changed_layer_inventory` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_changed_layer_inventory` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_geographic_crs` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_geographic_crs` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_loader_preserves_lambert93_lines_unchanged` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_preserves_lambert93_lines_unchanged` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_layer_does_not_change_electricity_loading_or_cache_shape` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_layer_does_not_change_electricity_loading_or_cache_shape` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_download_cache_reader_rejects_noncanonical_json_and_refreshes` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_download_cache_reader_rejects_noncanonical_json_and_refreshes` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_loader_selects_configured_identity` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_loader_selects_configured_identity` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_one_authoritative_feature` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_one_authoritative_feature` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_configured_identity_field` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_configured_identity_field` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_missing_department_coverage_layer_fails` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_department_coverage_layer_fails` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_layer_discovery_must_be_unambiguous` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_layer_discovery_must_be_unambiguous` via `_response`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_direct_consumers_reject_same_inventory_content_tampering` via `_response`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_direct_consumers_reject_same_inventory_content_tampering` via `_response`

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

<a id="r15--metadata-path"></a>
### `_metadata_path`

Qualified owner: `tests.unit.test_ign_bdtopo_fr._metadata_path`. Source lines 265–266.

**Verified purpose:** Derive the sibling archive-name.metadata.json Path. No existence check, file read or write.

**Exact signature**

```python
def _metadata_path(archive_path: Path) -> Path:
```

- Exact decorators: none.
- Declared return annotation: `Path`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `archive_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `archive_path.parent / f"{archive_path.name}.metadata.json"`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_ign_bdtopo_fr::test_successful_archive_download_persists_sha256` via `_metadata_path`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_successful_archive_download_persists_sha256` via `_metadata_path`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_expired_cache_is_refreshed` via `_metadata_path`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_expired_cache_is_refreshed` via `_metadata_path`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_failed_refresh_preserves_valid_cache` via `_metadata_path`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_failed_refresh_preserves_valid_cache` via `_metadata_path`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_corrupt_refresh_preserves_valid_cache` via `_metadata_path`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_corrupt_refresh_preserves_valid_cache` via `_metadata_path`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_metadata_publication_failure_restores_previous_cache_pair` via `_metadata_path`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_metadata_publication_failure_restores_previous_cache_pair` via `_metadata_path`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_metadata_path`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_metadata_path`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_download_cache_reader_rejects_noncanonical_json_and_refreshes` via `_metadata_path`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_download_cache_reader_rejects_noncanonical_json_and_refreshes` via `_metadata_path`

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
def _metadata_path(archive_path: Path) -> Path:
    return archive_path.parent / f"{archive_path.name}.metadata.json"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15--extraction-metadata-path"></a>
### `_extraction_metadata_path`

Qualified owner: `tests.unit.test_ign_bdtopo_fr._extraction_metadata_path`. Source lines 269–270.

**Verified purpose:** Derive the .landscout-extraction.json child Path. No existence check, file read or write.

**Exact signature**

```python
def _extraction_metadata_path(extraction_path: Path) -> Path:
```

- Exact decorators: none.
- Declared return annotation: `Path`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `extraction_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `extraction_path / ".landscout-extraction.json"`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_ign_bdtopo_fr::test_schema_v3_extraction_metadata_binds_complete_physical_inventory` via `_extraction_metadata_path`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_schema_v3_extraction_metadata_binds_complete_physical_inventory` via `_extraction_metadata_path`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_forged_extraction_metadata_never_returns_cache_hit` via `_extraction_metadata_path`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_forged_extraction_metadata_never_returns_cache_hit` via `_extraction_metadata_path`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_linked_extraction_metadata_never_returns_cache_hit` via `_extraction_metadata_path`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_linked_extraction_metadata_never_returns_cache_hit` via `_extraction_metadata_path`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_malformed_geopackage_sha_is_not_trusted` via `_extraction_metadata_path`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_malformed_geopackage_sha_is_not_trusted` via `_extraction_metadata_path`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_malformed_geopackage_size_is_not_trusted` via `_extraction_metadata_path`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_malformed_geopackage_size_is_not_trusted` via `_extraction_metadata_path`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_extraction_cache_reader_rejects_noncanonical_json_and_rebuilds` via `_extraction_metadata_path`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_extraction_cache_reader_rejects_noncanonical_json_and_rebuilds` via `_extraction_metadata_path`

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
def _extraction_metadata_path(extraction_path: Path) -> Path:
    return extraction_path / ".landscout-extraction.json"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15--extracted-fixture"></a>
### `_extracted_fixture`

Qualified owner: `tests.unit.test_ign_bdtopo_fr._extracted_fixture`. Source lines 273–294.

**Verified purpose:** Ordinary helper, not a pytest fixture: build genuine synthetic GPKG/7z bytes and derived config, mock open_safe_https with a nondelegating BytesIO return_value, call public download and extraction, and return config/download/extraction. Archive and GPKG validation run locally; DNS/HTTP/TLS are bypassed.

**Exact signature**

```python
def _extracted_fixture(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    *,
    include_roads: bool = True,
) -> tuple[IgnBdTopoSourceConfig, IgnBdTopoDownload, IgnBdTopoExtraction]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[IgnBdTopoSourceConfig, IgnBdTopoDownload, IgnBdTopoExtraction]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |
| `include_roads` | keyword-only | `bool` | `True` |

**Return and exception contract**

- Exact observed return expressions:
  - `config, download, extraction`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_ign_bdtopo_fr::test_schema_v3_extraction_metadata_binds_complete_physical_inventory` via `_extracted_fixture`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_schema_v3_extraction_metadata_binds_complete_physical_inventory` via `_extracted_fixture`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_extraction_rejects_forged_download_lineage_before_archive_open` via `_extracted_fixture`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_extraction_rejects_forged_download_lineage_before_archive_open` via `_extracted_fixture`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_same_size_geopackage_tamper_invalidates_extraction_cache` via `_extracted_fixture`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_same_size_geopackage_tamper_invalidates_extraction_cache` via `_extracted_fixture`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_forged_extraction_metadata_never_returns_cache_hit` via `_extracted_fixture`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_forged_extraction_metadata_never_returns_cache_hit` via `_extracted_fixture`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_linked_extraction_metadata_never_returns_cache_hit` via `_extracted_fixture`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_linked_extraction_metadata_never_returns_cache_hit` via `_extracted_fixture`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_malformed_geopackage_sha_is_not_trusted` via `_extracted_fixture`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_malformed_geopackage_sha_is_not_trusted` via `_extracted_fixture`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_malformed_geopackage_size_is_not_trusted` via `_extracted_fixture`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_malformed_geopackage_size_is_not_trusted` via `_extracted_fixture`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_physical_layer_cannot_collide_with_electricity_roles` via `_extracted_fixture`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_physical_layer_cannot_collide_with_electricity_roles` via `_extracted_fixture`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_physical_layer_cannot_collide_with_road_role` via `_extracted_fixture`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_physical_layer_cannot_collide_with_road_role` via `_extracted_fixture`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_physical_layer_cannot_collide_with_electricity_roles` via `_extracted_fixture`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_physical_layer_cannot_collide_with_electricity_roles` via `_extracted_fixture`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_electricity_physical_layers_must_be_distinct` via `_extracted_fixture`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_electricity_physical_layers_must_be_distinct` via `_extracted_fixture`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_non_electric_layer_loaders_revalidate_mutated_role_config_before_read` via `_extracted_fixture`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_non_electric_layer_loaders_revalidate_mutated_role_config_before_read` via `_extracted_fixture`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_stale_extraction_backup_blocks_before_7z_open` via `_extracted_fixture`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_stale_extraction_backup_blocks_before_7z_open` via `_extracted_fixture`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_extraction_part_link_is_rejected_without_touching_target` via `_extracted_fixture`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_extraction_part_link_is_rejected_without_touching_target` via `_extracted_fixture`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_extraction_cache_reader_rejects_noncanonical_json_and_rebuilds` via `_extracted_fixture`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_extraction_cache_reader_rejects_noncanonical_json_and_rebuilds` via `_extracted_fixture`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_direct_consumers_reject_same_inventory_content_tampering` via `_extracted_fixture`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_direct_consumers_reject_same_inventory_content_tampering` via `_extracted_fixture`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_source_change_after_physical_read` via `_extracted_fixture`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_source_change_after_physical_read` via `_extracted_fixture`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_synthetic_archive_bytes` | `tests.unit.test_ign_bdtopo_fr._synthetic_archive_bytes` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |

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
def _extracted_fixture(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    *,
    include_roads: bool = True,
) -> tuple[IgnBdTopoSourceConfig, IgnBdTopoDownload, IgnBdTopoExtraction]:
    archive_content = _synthetic_archive_bytes(
        tmp_path / "source",
        include_roads=include_roads,
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )
    return config, download, extraction
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15--expire-cache"></a>
### `_expire_cache`

Qualified owner: `tests.unit.test_ign_bdtopo_fr._expire_cache`. Source lines 297–303.

**Verified purpose:** Read the JSON sidecar, replace download_timestamp with UTC now minus 365 days, rewrite it and return the rewritten bytes for exact later comparison. Mutates only the synthetic cache, not the frozen download envelope.

**Exact signature**

```python
def _expire_cache(metadata_path: Path) -> bytes:
```

- Exact decorators: none.
- Declared return annotation: `bytes`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `metadata_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `metadata_path.read_bytes()`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_ign_bdtopo_fr::test_expired_cache_is_refreshed` via `_expire_cache`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_expired_cache_is_refreshed` via `_expire_cache`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_failed_refresh_preserves_valid_cache` via `_expire_cache`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_failed_refresh_preserves_valid_cache` via `_expire_cache`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_corrupt_refresh_preserves_valid_cache` via `_expire_cache`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_corrupt_refresh_preserves_valid_cache` via `_expire_cache`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_metadata_publication_failure_restores_previous_cache_pair` via `_expire_cache`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_metadata_publication_failure_restores_previous_cache_pair` via `_expire_cache`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_expire_cache`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_expire_cache`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `json.loads` | `json.loads` |
| `metadata_path.read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `(<br>        datetime.now(UTC) - timedelta(days=365)<br>    ).isoformat` | `unresolved local/third-party receiver; no ownership inferred` |
| `datetime.now` | `datetime.datetime.now` |
| `timedelta` | `datetime.timedelta` |
| `metadata_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `metadata_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `metadata_path.read_text`<br>`metadata_path.read_bytes` |
| Filesystem/archive write or publication | `metadata_path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `metadata["download_timestamp"] = (<br>        datetime.now(UTC) - timedelta(days=365)<br>    ).isoformat()` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _expire_cache(metadata_path: Path) -> bytes:
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["download_timestamp"] = (
        datetime.now(UTC) - timedelta(days=365)
    ).isoformat()
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
    return metadata_path.read_bytes()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-source-config"></a>
### `source_config`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.source_config`. Source lines 307–308.

**Verified purpose:** The sole pytest.fixture in this module; with no explicit scope argument, each requesting test receives a config loaded from checked-in YAML through the public strict loader. Its parameter names elsewhere denote injected model values, not methods of this fixture function.

**Exact signature**

```python
def source_config() -> IgnBdTopoSourceConfig:
```

- Exact decorators: `pytest.fixture`.
- Declared return annotation: `IgnBdTopoSourceConfig`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `load_ign_bdtopo_source_config(CONFIG_PATH)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::_synthetic_config` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::_extracted_fixture` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_valid_source_config_loads` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_loaded_ign_source_config_and_nested_models_are_frozen` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_download_revalidates_a_tampered_config_before_network` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_successful_archive_download_persists_sha256` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_fresh_cache_is_reused_without_network` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_stale_recovery_backup_rejects_cache_before_network` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_expired_cache_is_refreshed` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_failed_refresh_preserves_valid_cache` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_corrupt_refresh_preserves_valid_cache` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_metadata_publication_failure_restores_previous_cache_pair` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_official_checksum_mismatch_is_rejected` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_unsafe_parent_archive_member_is_rejected` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_real_layer_names_are_listed_and_discovered` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_missing_electric_line_layer_fails` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_missing_transformation_post_layer_fails` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_ambiguous_electric_line_layers_fail` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_synthetic_archive_extracts_and_discovers_required_layers` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_schema_v3_extraction_metadata_binds_complete_physical_inventory` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_extraction_rejects_forged_download_lineage_before_archive_open` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_same_size_geopackage_tamper_invalidates_extraction_cache` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_forged_extraction_metadata_never_returns_cache_hit` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_linked_extraction_metadata_never_returns_cache_hit` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_malformed_geopackage_sha_is_not_trusted` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_malformed_geopackage_size_is_not_trusted` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_default_extraction_path_is_short_and_content_addressed` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_electricity_loader_retains_both_layer_counts` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_road_layer_discovery_loads_selected_physical_layer` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_road_physical_layer_cannot_collide_with_electricity_roles` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_department_physical_layer_cannot_collide_with_road_role` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_department_physical_layer_cannot_collide_with_electricity_roles` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_electricity_physical_layers_must_be_distinct` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_missing_road_layer_fails_safely` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_ambiguous_road_layer_fails_safely` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_wrong_archive_config_department` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_non_electric_layer_loaders_revalidate_mutated_role_config_before_read` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_changed_layer_inventory` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_geographic_crs` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_road_loader_preserves_lambert93_lines_unchanged` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_road_layer_does_not_change_electricity_loading_or_cache_shape` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_stale_extraction_backup_blocks_before_7z_open` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_extraction_part_link_is_rejected_without_touching_target` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_download_cache_reader_rejects_noncanonical_json_and_refreshes` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_extraction_cache_reader_rejects_noncanonical_json_and_rebuilds` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_department_coverage_loader_selects_configured_identity` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_one_authoritative_feature` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_configured_identity_field` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_missing_department_coverage_layer_fails` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_department_coverage_layer_discovery_must_be_unambiguous` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_direct_consumers_reject_same_inventory_content_tampering` via parameter `source_config`
- Fixture-value injection/forwarding (not a direct reference to the fixture callable): `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_source_change_after_physical_read` via parameter `source_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_ign_bdtopo_source_config` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_source_config` |

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
def source_config() -> IgnBdTopoSourceConfig:
    return load_ign_bdtopo_source_config(CONFIG_PATH)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-valid-source-config-loads"></a>
### `test_valid_source_config_loads`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_valid_source_config_loads`. Source lines 311–320.

**Verified purpose:** Inspect the loaded YAML model: provider contains IGN, department 31, EPSG:2154, GPKG, edition 2026-06-15, road label/tokens and department tokens/identity field. Nine assertions, no archive acquisition or physical-source certification.

**Exact signature**

```python
def test_valid_source_config_loads(source_config: IgnBdTopoSourceConfig) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert "IGN" in source_config.provider`
  - `assert source_config.department_code == "31"`
  - `assert source_config.projection == "EPSG:2154"`
  - `assert source_config.format == "GPKG"`
  - `assert source_config.edition == "2026-06-15"`
  - `assert source_config.access.road_segments.class_label == "Tronçon de route"`
  - `assert source_config.access.road_segments.match_tokens == ("tronçon", "route")`
  - `assert source_config.coverage.department_layer.match_tokens == ("departement",)`
  - `assert source_config.coverage.department_layer.department_code_field == "code_insee"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
- No calls.

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_valid_source_config_loads(source_config: IgnBdTopoSourceConfig) -> None:
    assert "IGN" in source_config.provider
    assert source_config.department_code == "31"
    assert source_config.projection == "EPSG:2154"
    assert source_config.format == "GPKG"
    assert source_config.edition == "2026-06-15"
    assert source_config.access.road_segments.class_label == "Tronçon de route"
    assert source_config.access.road_segments.match_tokens == ("tronçon", "route")
    assert source_config.coverage.department_layer.match_tokens == ("departement",)
    assert source_config.coverage.department_layer.department_code_field == "code_insee"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-loaded-ign-source-config-and-nested-models-are-frozen"></a>
### `test_loaded_ign_source_config_and_nested_models_are_frozen`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_loaded_ign_source_config_and_nested_models_are_frozen`. Source lines 323–329.

**Verified purpose:** Attempt assignment to department_code and nested road class_label; each must immediately raise ValidationError. These two assignments do not test every nested collection operation or every metadata model.

**Exact signature**

```python
def test_loaded_ign_source_config_and_nested_models_are_frozen(
    source_config: IgnBdTopoSourceConfig,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

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
| `pytest.raises` | `pytest.raises` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `source_config.department_code = "32"`<br>`source_config.access.road_segments.class_label = "other"` |
| Direct parameter mutation | `source_config.department_code = "32"`<br>`source_config.access.road_segments.class_label = "other"` |

**Complete source-ordered implementation**

```python
def test_loaded_ign_source_config_and_nested_models_are_frozen(
    source_config: IgnBdTopoSourceConfig,
) -> None:
    with pytest.raises(ValidationError):
        source_config.department_code = "32"  # type: ignore[misc]
    with pytest.raises(ValidationError):
        source_config.access.road_segments.class_label = "other"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-download-revalidates-a-tampered-config-before-network"></a>
### `test_download_revalidates_a_tampered_config_before_network`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_download_revalidates_a_tampered_config_before_network`. Source lines 332–348.

**Verified purpose:** Copy the model and bypass freezing with object.__setattr__ to forge provider, then call public download under a raising opener sentinel. Require IgnBdTopoDownloadError matching config and assert the opener was not called; config reconstruction rejects before acquisition.

**Exact signature**

```python
def test_download_revalidates_a_tampered_config_before_network(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoDownloadError, match="config")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `source_config.model_copy` | `pydantic.BaseModel.model_copy` (inherited by `landscout.sources.ign_bdtopo_fr.IgnBdTopoSourceConfig`) (inherited Pydantic method on the injected model) |
| `object.__setattr__` | `unresolved local/third-party receiver; no ownership inferred` |
| `patch` | `unittest.mock.patch` |
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `opener.assert_not_called` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `object.__setattr__(tampered, "provider", "UNTRUSTED")` changes the local deep model copy. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_download_revalidates_a_tampered_config_before_network(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
) -> None:
    tampered = source_config.model_copy(deep=True)
    object.__setattr__(tampered, "provider", "UNTRUSTED")

    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            side_effect=AssertionError("invalid config must fail before network"),
        ) as opener,
        pytest.raises(IgnBdTopoDownloadError, match="config"),
    ):
        download_ign_bdtopo_archive(tampered, tmp_path)

    opener.assert_not_called()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-invalid-department-coverage-config-fails"></a>
### `test_invalid_department_coverage_config_fails`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_invalid_department_coverage_config_fails`. Source lines 352–362.

**Verified purpose:** Mutate the YAML payload in three cases: missing coverage, blank identity field or empty department match_tokens. Direct model_validate must raise ValidationError; no GPKG or transport boundary is exercised.

**Exact signature**

```python
def test_invalid_department_coverage_config_fails(mutation: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("mutation", ["missing", "blank_field", "empty_tokens"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `mutation` | positional-or-keyword | `str` | `required` |

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
| `_config_data` | `tests.unit.test_ign_bdtopo_fr._config_data` |
| `pytest.raises` | `pytest.raises` |
| `IgnBdTopoSourceConfig.model_validate` | `pydantic.BaseModel.model_validate` (inherited by `landscout.sources.ign_bdtopo_fr.IgnBdTopoSourceConfig`) |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `del content["coverage"]`<br>`content["coverage"]["department_layer"]["department_code_field"] = " "`<br>`content["coverage"]["department_layer"]["match_tokens"] = []` change the local `_config_data()` dictionary in separate parameter branches. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_invalid_department_coverage_config_fails(mutation: str) -> None:
    content = _config_data()
    if mutation == "missing":
        del content["coverage"]
    elif mutation == "blank_field":
        content["coverage"]["department_layer"]["department_code_field"] = " "
    else:
        content["coverage"]["department_layer"]["match_tokens"] = []

    with pytest.raises(ValidationError):
        IgnBdTopoSourceConfig.model_validate(content)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-missing-required-source-field-fails"></a>
### `test_missing_required_source_field_fails`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_missing_required_source_field_fails`. Source lines 366–371.

**Verified purpose:** Remove source_url or edition from the YAML payload and require ValidationError from direct source-model validation. No physical or network access.

**Exact signature**

```python
def test_missing_required_source_field_fails(field: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("field", ["source_url", "edition"])`.
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
| `_config_data` | `tests.unit.test_ign_bdtopo_fr._config_data` |
| `pytest.raises` | `pytest.raises` |
| `IgnBdTopoSourceConfig.model_validate` | `pydantic.BaseModel.model_validate` (inherited by `landscout.sources.ign_bdtopo_fr.IgnBdTopoSourceConfig`) |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `del content[field]` removes `source_url` or `edition` from the local `_config_data()` dictionary. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_missing_required_source_field_fails(field: str) -> None:
    content = _config_data()
    del content[field]

    with pytest.raises(ValidationError):
        IgnBdTopoSourceConfig.model_validate(content)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-invalid-source-configuration-fails"></a>
### `test_invalid_source_configuration_fails`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_invalid_source_configuration_fails`. Source lines 384–389.

**Verified purpose:** Direct model validation rejects department 3/XX, EPSG:4326 projection, SHP format or zip archive format. The format Literal can reject before the suffix cross-validator; this is not a transport or archive-content test.

**Exact signature**

```python
def test_invalid_source_configuration_fails(field: str, value: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "value"),
    [
        ("department_code", "3"),
        ("department_code", "XX"),
        ("projection", "EPSG:4326"),
        ("format", "SHP"),
        ("archive_format", "zip"),
    ],
)`.
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
| `_config_data` | `tests.unit.test_ign_bdtopo_fr._config_data` |
| `pytest.raises` | `pytest.raises` |
| `IgnBdTopoSourceConfig.model_validate` | `pydantic.BaseModel.model_validate` (inherited by `landscout.sources.ign_bdtopo_fr.IgnBdTopoSourceConfig`) |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `content[field] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_invalid_source_configuration_fails(field: str, value: str) -> None:
    content = _config_data()
    content[field] = value

    with pytest.raises(ValidationError):
        IgnBdTopoSourceConfig.model_validate(content)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-unknown-source-config-field-is-rejected"></a>
### `test_unknown_source_config_field_is_rejected`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_unknown_source_config_field_is_rejected`. Source lines 392–397.

**Verified purpose:** Add invented to the YAML payload and require ValidationError from the extra-forbid source model. No acquisition.

**Exact signature**

```python
def test_unknown_source_config_field_is_rejected() -> None:
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
| `_config_data` | `tests.unit.test_ign_bdtopo_fr._config_data` |
| `pytest.raises` | `pytest.raises` |
| `IgnBdTopoSourceConfig.model_validate` | `pydantic.BaseModel.model_validate` (inherited by `landscout.sources.ign_bdtopo_fr.IgnBdTopoSourceConfig`) |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `content["invented"] = "not allowed"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_unknown_source_config_field_is_rejected() -> None:
    content = _config_data()
    content["invented"] = "not allowed"

    with pytest.raises(ValidationError):
        IgnBdTopoSourceConfig.model_validate(content)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-successful-archive-download-persists-sha256"></a>
### `test_successful_archive_download_persists_sha256`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_successful_archive_download_persists_sha256`. Source lines 400–419.

**Verified purpose:** Mock the opener with genuine synthetic 7z bytes, run public download, and compare cache_hit=False, saved bytes, size, local SHA and metadata SHA/source URL/absent official checksum. No real HTTPS or positive official-checksum assertion.

**Exact signature**

```python
def test_successful_archive_download_persists_sha256(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.cache_hit is False`
  - `assert result.path.read_bytes() == archive_content`
  - `assert result.file_size == len(archive_content)`
  - `assert result.sha256 == sha256(archive_content).hexdigest()`
  - `assert metadata["sha256"] == result.sha256`
  - `assert metadata["source_url"] == SYNTHETIC_SOURCE_URL`
  - `assert metadata["official_checksum"] is None`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_synthetic_archive_bytes` | `tests.unit.test_ign_bdtopo_fr._synthetic_archive_bytes` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `result.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(archive_content).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `json.loads` | `json.loads` |
| `_metadata_path(result.path).read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `_metadata_path` | `tests.unit.test_ign_bdtopo_fr._metadata_path` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `result.path.read_bytes`<br>`_metadata_path(result.path).read_text` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(archive_content).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_successful_archive_download_persists_sha256(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path)
    config = _synthetic_config(source_config)

    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        result = download_ign_bdtopo_archive(config, tmp_path / "cache")

    assert result.cache_hit is False
    assert result.path.read_bytes() == archive_content
    assert result.file_size == len(archive_content)
    assert result.sha256 == sha256(archive_content).hexdigest()
    metadata = json.loads(_metadata_path(result.path).read_text(encoding="utf-8"))
    assert metadata["sha256"] == result.sha256
    assert metadata["source_url"] == SYNTHETIC_SOURCE_URL
    assert metadata["official_checksum"] is None
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-archive-integrity-reports-local-sha256-and-no-fabricated-checksum"></a>
### `test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum`. Source lines 422–438.

**Verified purpose:** Write genuine synthetic 7z bytes locally and call public archive validation. Assert size/local SHA, both official checksum fields None and official_checksum_validated=False. No network and no invented official pin.

**Exact signature**

```python
def test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert integrity.file_size == len(archive_content)`
  - `assert integrity.sha256 == sha256(archive_content).hexdigest()`
  - `assert integrity.official_checksum is None`
  - `assert integrity.official_checksum_algorithm is None`
  - `assert integrity.official_checksum_validated is False`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_synthetic_archive_bytes` | `tests.unit.test_ign_bdtopo_fr._synthetic_archive_bytes` |
| `archive_path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `validate_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.validate_ign_bdtopo_archive` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(archive_content).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `archive_path.write_bytes` |
| Hashing/byte identity | `sha256(archive_content).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_path = tmp_path / "fixture.7z"
    archive_content = _synthetic_archive_bytes(tmp_path / "source")
    archive_path.write_bytes(archive_content)

    integrity = validate_ign_bdtopo_archive(
        archive_path,
        _synthetic_config(source_config),
    )

    assert integrity.file_size == len(archive_content)
    assert integrity.sha256 == sha256(archive_content).hexdigest()
    assert integrity.official_checksum is None
    assert integrity.official_checksum_algorithm is None
    assert integrity.official_checksum_validated is False
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-fresh-cache-is-reused-without-network"></a>
### `test_fresh_cache_is_reused_without_network`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_fresh_cache_is_reused_without_network`. Source lines 441–462.

**Verified purpose:** Create a synthetic cache with a mocked stream, then replace the opener with an AssertionError sentinel. A second public download returns cache_hit=True and the same path/SHA/timestamp. The sentinel makes any opener call fail; there is no separate call-count assertion and local hashing/CRC still occur.

**Exact signature**

```python
def test_fresh_cache_is_reused_without_network(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert second.cache_hit is True`
  - `assert second.path == first.path`
  - `assert second.sha256 == first.sha256`
  - `assert second.download_timestamp == first.download_timestamp`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_synthetic_archive_bytes` | `tests.unit.test_ign_bdtopo_fr._synthetic_archive_bytes` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_fresh_cache_is_reused_without_network(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    content = _synthetic_archive_bytes(tmp_path)
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(content),
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)

    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        side_effect=AssertionError("network must not be called"),
    ):
        second = download_ign_bdtopo_archive(config, cache_dir)

    assert second.cache_hit is True
    assert second.path == first.path
    assert second.sha256 == first.sha256
    assert second.download_timestamp == first.download_timestamp
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-stale-recovery-backup-rejects-cache-before-network"></a>
### `test_stale_recovery_backup_rejects_cache_before_network`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_stale_recovery_backup_rejects_cache_before_network`. Source lines 465–491.

**Verified purpose:** Create a valid cache then a sibling archive .bak with sentinel bytes. Public download must fail with the backup/recovery/manual error before the raising opener; assert opener uncalled and exact backup/archive bytes preserved.

**Exact signature**

```python
def test_stale_recovery_backup_rejects_cache_before_network(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoDownloadError, match="backup\|recovery\|manual")`
- Exact assertions:
  - `assert recovery_path.read_bytes() == recovery_bytes`
  - `assert first.path.read_bytes() == content`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_synthetic_archive_bytes` | `tests.unit.test_ign_bdtopo_fr._synthetic_archive_bytes` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `first.path.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `recovery_path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `opener.assert_not_called` | `unresolved local/third-party receiver; no ownership inferred` |
| `recovery_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `first.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `recovery_path.read_bytes`<br>`first.path.read_bytes` |
| Filesystem/archive write or publication | `recovery_path.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_stale_recovery_backup_rejects_cache_before_network(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    content = _synthetic_archive_bytes(tmp_path)
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(content),
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
    recovery_path = first.path.with_name(f"{first.path.name}.bak")
    recovery_bytes = b"manual IGN recovery material"
    recovery_path.write_bytes(recovery_bytes)

    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            side_effect=AssertionError("stale recovery must fail before network"),
        ) as opener,
        pytest.raises(IgnBdTopoDownloadError, match="backup|recovery|manual"),
    ):
        download_ign_bdtopo_archive(config, cache_dir)

    opener.assert_not_called()
    assert recovery_path.read_bytes() == recovery_bytes
    assert first.path.read_bytes() == content
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-expired-cache-is-refreshed"></a>
### `test_expired_cache_is_refreshed`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_expired_cache_is_refreshed`. Source lines 494–519.

**Verified purpose:** Create an old synthetic cache, age metadata by 365 days and offer a different real archive (invalid-post fixture). Assert one mocked opener call, cache miss, exact new bytes, changed SHA and no .part/.bak siblings. No live remote refresh.

**Exact signature**

```python
def test_expired_cache_is_refreshed(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert opener.call_count == 1`
  - `assert refreshed.cache_hit is False`
  - `assert refreshed.path.read_bytes() == new_content`
  - `assert refreshed.sha256 != first.sha256`
  - `assert not list(cache_dir.glob("*.part"))`
  - `assert not list(cache_dir.glob("*.bak"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_synthetic_archive_bytes` | `tests.unit.test_ign_bdtopo_fr._synthetic_archive_bytes` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `_expire_cache` | `tests.unit.test_ign_bdtopo_fr._expire_cache` |
| `_metadata_path` | `tests.unit.test_ign_bdtopo_fr._metadata_path` |
| `refreshed.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `cache_dir.glob` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `refreshed.path.read_bytes`<br>`cache_dir.glob` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_expired_cache_is_refreshed(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    old_content = _synthetic_archive_bytes(tmp_path / "v1")
    new_content = _synthetic_archive_bytes(tmp_path / "v2", invalid_post=True)
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(old_content),
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
    _expire_cache(_metadata_path(first.path))

    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(new_content),
    ) as opener:
        refreshed = download_ign_bdtopo_archive(config, cache_dir)

    assert opener.call_count == 1
    assert refreshed.cache_hit is False
    assert refreshed.path.read_bytes() == new_content
    assert refreshed.sha256 != first.sha256
    assert not list(cache_dir.glob("*.part"))
    assert not list(cache_dir.glob("*.bak"))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-failed-refresh-preserves-valid-cache"></a>
### `test_failed_refresh_preserves_valid_cache`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_failed_refresh_preserves_valid_cache`. Source lines 522–547.

**Verified purpose:** After expiring a valid synthetic cache, make the opener raise HTTPError 503. Require IgnBdTopoDownloadError, exact old archive and expired metadata bytes, and no .part/.bak files.

**Exact signature**

```python
def test_failed_refresh_preserves_valid_cache(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoDownloadError)`
- Exact assertions:
  - `assert first.path.read_bytes() == old_archive`
  - `assert metadata_path.read_bytes() == expired_metadata`
  - `assert not list(cache_dir.glob("*.part"))`
  - `assert not list(cache_dir.glob("*.bak"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_synthetic_archive_bytes` | `tests.unit.test_ign_bdtopo_fr._synthetic_archive_bytes` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `_metadata_path` | `tests.unit.test_ign_bdtopo_fr._metadata_path` |
| `first.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_expire_cache` | `tests.unit.test_ign_bdtopo_fr._expire_cache` |
| `HTTPError` | `urllib.error.HTTPError` |
| `pytest.raises` | `pytest.raises` |
| `metadata_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `cache_dir.glob` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `first.path.read_bytes`<br>`metadata_path.read_bytes`<br>`cache_dir.glob` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_failed_refresh_preserves_valid_cache(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    content = _synthetic_archive_bytes(tmp_path)
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(content),
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
    metadata_path = _metadata_path(first.path)
    old_archive = first.path.read_bytes()
    expired_metadata = _expire_cache(metadata_path)
    error = HTTPError(SYNTHETIC_SOURCE_URL, 503, "Unavailable", None, None)

    with (
        patch("landscout.sources.ign_bdtopo_fr.open_safe_https", side_effect=error),
        pytest.raises(IgnBdTopoDownloadError),
    ):
        download_ign_bdtopo_archive(config, cache_dir)

    assert first.path.read_bytes() == old_archive
    assert metadata_path.read_bytes() == expired_metadata
    assert not list(cache_dir.glob("*.part"))
    assert not list(cache_dir.glob("*.bak"))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-corrupt-new-archive-is-rejected-and-temporary-files-are-cleaned"></a>
### `test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned`. Source lines 550–566.

**Verified purpose:** Offer b"not a 7z archive" through the mocked opener to a new cache. Require IgnBdTopoArchiveError and absence of .7z, .part and .bak files; metadata absence is not separately asserted.

**Exact signature**

```python
def test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoArchiveError)`
- Exact assertions:
  - `assert not list(cache_dir.glob("*.7z"))`
  - `assert not list(cache_dir.glob("*.part"))`
  - `assert not list(cache_dir.glob("*.bak"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `pytest.raises` | `pytest.raises` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `cache_dir.glob` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `cache_dir.glob` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(b"not a 7z archive"),
        ),
        pytest.raises(IgnBdTopoArchiveError),
    ):
        download_ign_bdtopo_archive(config, cache_dir)

    assert not list(cache_dir.glob("*.7z"))
    assert not list(cache_dir.glob("*.part"))
    assert not list(cache_dir.glob("*.bak"))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-corrupt-refresh-preserves-valid-cache"></a>
### `test_corrupt_refresh_preserves_valid_cache`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_corrupt_refresh_preserves_valid_cache`. Source lines 569–595.

**Verified purpose:** Expire a synthetic cache and offer b"broken refresh". Require IgnBdTopoArchiveError, exact old archive/expired metadata and no .part files. This test has no .bak-absence assertion.

**Exact signature**

```python
def test_corrupt_refresh_preserves_valid_cache(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoArchiveError)`
- Exact assertions:
  - `assert first.path.read_bytes() == old_archive`
  - `assert metadata_path.read_bytes() == expired_metadata`
  - `assert not list(cache_dir.glob("*.part"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_synthetic_archive_bytes` | `tests.unit.test_ign_bdtopo_fr._synthetic_archive_bytes` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `_metadata_path` | `tests.unit.test_ign_bdtopo_fr._metadata_path` |
| `first.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_expire_cache` | `tests.unit.test_ign_bdtopo_fr._expire_cache` |
| `pytest.raises` | `pytest.raises` |
| `metadata_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `cache_dir.glob` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `first.path.read_bytes`<br>`metadata_path.read_bytes`<br>`cache_dir.glob` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_corrupt_refresh_preserves_valid_cache(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    content = _synthetic_archive_bytes(tmp_path)
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(content),
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
    metadata_path = _metadata_path(first.path)
    old_archive = first.path.read_bytes()
    expired_metadata = _expire_cache(metadata_path)

    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(b"broken refresh"),
        ),
        pytest.raises(IgnBdTopoArchiveError),
    ):
        download_ign_bdtopo_archive(config, cache_dir)

    assert first.path.read_bytes() == old_archive
    assert metadata_path.read_bytes() == expired_metadata
    assert not list(cache_dir.glob("*.part"))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-metadata-publication-failure-restores-previous-cache-pair"></a>
### `test_metadata_publication_failure_restores_previous_cache_pair`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_metadata_publication_failure_restores_previous_cache_pair`. Source lines 598–641.

**Verified purpose:** Refresh a real synthetic cache while a delegating _replace_file callback persistently rejects metadata publication. Require IgnBdTopoDownloadError, injection flag, exact old archive/expired metadata and no .part/.bak siblings. Archive rollback and unchanged old metadata yield the pair; this does not prove a metadata-backup restore operation.

**Exact signature**

```python
def test_metadata_publication_failure_restores_previous_cache_pair(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoDownloadError)`
- Exact assertions:
  - `assert failure_injected`
  - `assert first.path.read_bytes() == old_archive`
  - `assert metadata_path.read_bytes() == expired_metadata`
  - `assert not list(cache_dir.glob("*.part"))`
  - `assert not list(cache_dir.glob("*.bak"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_synthetic_archive_bytes` | `tests.unit.test_ign_bdtopo_fr._synthetic_archive_bytes` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `_metadata_path` | `tests.unit.test_ign_bdtopo_fr._metadata_path` |
| `first.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_expire_cache` | `tests.unit.test_ign_bdtopo_fr._expire_cache` |
| `patch.object` | `unittest.mock.patch.object` |
| `pytest.raises` | `pytest.raises` |
| `metadata_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `cache_dir.glob` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `first.path.read_bytes`<br>`metadata_path.read_bytes`<br>`cache_dir.glob` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_metadata_publication_failure_restores_previous_cache_pair(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    old_content = _synthetic_archive_bytes(tmp_path / "v1")
    new_content = _synthetic_archive_bytes(tmp_path / "v2", invalid_post=True)
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(old_content),
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
    metadata_path = _metadata_path(first.path)
    old_archive = first.path.read_bytes()
    expired_metadata = _expire_cache(metadata_path)
    original_replace = ign_bdtopo_fr._replace_file
    failure_injected = False

    def fail_metadata_publication(source: Path, target: Path) -> None:
        nonlocal failure_injected
        if source.name.endswith(".metadata.json.part") and target == metadata_path:
            failure_injected = True
            raise PermissionError("simulated persistent metadata lock")
        original_replace(source, target)

    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(new_content),
        ),
        patch.object(
            ign_bdtopo_fr,
            "_replace_file",
            side_effect=fail_metadata_publication,
        ),
        pytest.raises(IgnBdTopoDownloadError),
    ):
        download_ign_bdtopo_archive(config, cache_dir)

    assert failure_injected
    assert first.path.read_bytes() == old_archive
    assert metadata_path.read_bytes() == expired_metadata
    assert not list(cache_dir.glob("*.part"))
    assert not list(cache_dir.glob("*.bak"))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-metadata-publication-failure-restores-previous-cache-pair-fail-metadata-publication"></a>
### `test_metadata_publication_failure_restores_previous_cache_pair.fail_metadata_publication`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_metadata_publication_failure_restores_previous_cache_pair.fail_metadata_publication`. Source lines 616–621.

**Verified purpose:** Intercept only .metadata.json.part to the metadata target, set the nonlocal flag and raise PermissionError. Delegate every other replacement to the captured real _replace_file, including archive publication/rollback; not a return_value mock.

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
  - `PermissionError("simulated persistent metadata lock")` under lexical guard `source.name.endswith(".metadata.json.part") and target == metadata_path`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `source.name.endswith` | `unresolved local/third-party receiver; no ownership inferred` |
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
        if source.name.endswith(".metadata.json.part") and target == metadata_path:
            failure_injected = True
            raise PermissionError("simulated persistent metadata lock")
        original_replace(source, target)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-publication-and-rollback-failure-preserves-exact-recovery-backups"></a>
### `test_publication_and_rollback_failure_preserves_exact_recovery_backups`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_publication_and_rollback_failure_preserves_exact_recovery_backups`. Source lines 644–684.

**Verified purpose:** Call private _publish_cache_pair on ordinary byte files, not a valid 7z/cache metadata pair. Inject metadata publication and archive rollback failures, require the controlled rollback error and compare both backup bytes to their old originals. It does not assert restored primaries or cleanup.

**Exact signature**

```python
def test_publication_and_rollback_failure_preserves_exact_recovery_backups(
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
  - `pytest.raises(IgnBdTopoDownloadError, match="rollback")`
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
| `archive_path.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `patch.object` | `unittest.mock.patch.object` |
| `pytest.raises` | `pytest.raises` |
| `ign_bdtopo_fr._publish_cache_pair` | `landscout.sources.ign_bdtopo_fr._publish_cache_pair` |
| `archive_backup.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_backup.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
    tmp_path: Path,
) -> None:
    archive_path = tmp_path / "cached.7z"
    metadata_path = tmp_path / "cached.7z.metadata.json"
    temporary_archive = tmp_path / "cached.7z.part"
    temporary_metadata = tmp_path / "cached.7z.metadata.json.part"
    old_archive = b"exact old archive"
    old_metadata = b"exact old metadata"
    archive_path.write_bytes(old_archive)
    metadata_path.write_bytes(old_metadata)
    temporary_archive.write_bytes(b"replacement archive")
    temporary_metadata.write_bytes(b"replacement metadata")
    archive_backup = archive_path.with_name(f"{archive_path.name}.bak")
    metadata_backup = metadata_path.with_name(f"{metadata_path.name}.bak")
    original_replace = ign_bdtopo_fr._replace_file

    def fail_publication_and_rollback(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        if source == archive_backup and target == archive_path:
            raise OSError("simulated archive rollback failure")
        original_replace(source, target)

    with (
        patch.object(
            ign_bdtopo_fr,
            "_replace_file",
            side_effect=fail_publication_and_rollback,
        ),
        pytest.raises(IgnBdTopoDownloadError, match="rollback"),
    ):
        ign_bdtopo_fr._publish_cache_pair(
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

<a id="r15-test-publication-and-rollback-failure-preserves-exact-recovery-backups-fail-publication-and-rollback"></a>
### `test_publication_and_rollback_failure_preserves_exact_recovery_backups.fail_publication_and_rollback`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_publication_and_rollback_failure_preserves_exact_recovery_backups.fail_publication_and_rollback`. Source lines 661–666.

**Verified purpose:** Raise OSError for temporary metadata publication and archive-backup restoration, otherwise delegate to the captured _replace_file. Distinct failure branches force publication plus rollback failure.

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

<a id="r15-test-cleanup-failure-does-not-mask-double-failure-recovery-error"></a>
### `test_cleanup_failure_does_not_mask_double_failure_recovery_error`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_cleanup_failure_does_not_mask_double_failure_recovery_error`. Source lines 687–739.

**Verified purpose:** Refresh a genuine synthetic cache with delegating publication/rollback failure injection plus conditional Path.unlink failure for temporary metadata. Require the original controlled rollback error and exact two recovery backups, not successful temporary cleanup.

**Exact signature**

```python
def test_cleanup_failure_does_not_mask_double_failure_recovery_error(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoDownloadError, match="rollback")`
- Exact assertions:
  - `assert archive_backup.read_bytes() == old_archive`
  - `assert metadata_backup.read_bytes() == old_metadata`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_synthetic_archive_bytes` | `tests.unit.test_ign_bdtopo_fr._synthetic_archive_bytes` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `_metadata_path` | `tests.unit.test_ign_bdtopo_fr._metadata_path` |
| `first.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_expire_cache` | `tests.unit.test_ign_bdtopo_fr._expire_cache` |
| `metadata_path.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `first.path.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `patch.object` | `unittest.mock.patch.object` |
| `pytest.raises` | `pytest.raises` |
| `archive_backup.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_backup.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `first.path.read_bytes`<br>`archive_backup.read_bytes`<br>`metadata_backup.read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_cleanup_failure_does_not_mask_double_failure_recovery_error(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    old_content = _synthetic_archive_bytes(tmp_path / "v1")
    new_content = _synthetic_archive_bytes(tmp_path / "v2", invalid_post=True)
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(old_content),
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
    metadata_path = _metadata_path(first.path)
    old_archive = first.path.read_bytes()
    old_metadata = _expire_cache(metadata_path)
    temporary_metadata = metadata_path.with_name(f"{metadata_path.name}.part")
    archive_backup = first.path.with_name(f"{first.path.name}.bak")
    metadata_backup = metadata_path.with_name(f"{metadata_path.name}.bak")
    original_replace = ign_bdtopo_fr._replace_file
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

    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(new_content),
        ),
        patch.object(
            ign_bdtopo_fr,
            "_replace_file",
            side_effect=fail_publication_and_rollback,
        ),
        patch.object(Path, "unlink", new=fail_temporary_cleanup),
        pytest.raises(IgnBdTopoDownloadError, match="rollback"),
    ):
        download_ign_bdtopo_archive(config, cache_dir)

    assert archive_backup.read_bytes() == old_archive
    assert metadata_backup.read_bytes() == old_metadata
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-cleanup-failure-does-not-mask-double-failure-recovery-error-fail-publication-and-rollback"></a>
### `test_cleanup_failure_does_not_mask_double_failure_recovery_error.fail_publication_and_rollback`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_cleanup_failure_does_not_mask_double_failure_recovery_error.fail_publication_and_rollback`. Source lines 709–716.

**Verified purpose:** Reject metadata publication; when archive-backup restoration is attempted set rollback_failed and raise OSError. Delegate other replacements. The flag enables the later cleanup failure.

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

<a id="r15-test-cleanup-failure-does-not-mask-double-failure-recovery-error-fail-temporary-cleanup"></a>
### `test_cleanup_failure_does_not_mask_double_failure_recovery_error.fail_temporary_cleanup`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_cleanup_failure_does_not_mask_double_failure_recovery_error.fail_temporary_cleanup`. Source lines 718–721.

**Verified purpose:** Once rollback_failed is true, deny unlink of exactly temporary_metadata with PermissionError; otherwise delegate original Path.unlink with missing_ok. This callback tests preservation of the primary error, not successful deletion.

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

<a id="r15-test-stale-cache-recovery-backup-fails-closed-without-destroying-it"></a>
### `test_stale_cache_recovery_backup_fails_closed_without_destroying_it`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_stale_cache_recovery_backup_fails_closed_without_destroying_it`. Source lines 742–766.

**Verified purpose:** Use private _publish_cache_pair on ordinary byte files with a preexisting archive .bak. Require backup/recovery/manual error and exact unchanged archive, metadata and recovery bytes. No archive parser or network is involved.

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
  - `pytest.raises(IgnBdTopoDownloadError, match="backup\|recovery\|manual")`
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
| `ign_bdtopo_fr._publish_cache_pair` | `landscout.sources.ign_bdtopo_fr._publish_cache_pair` |
| `archive_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `archive_backup.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
    archive_path = tmp_path / "cached.7z"
    metadata_path = tmp_path / "cached.7z.metadata.json"
    temporary_archive = tmp_path / "cached.7z.part"
    temporary_metadata = tmp_path / "cached.7z.metadata.json.part"
    archive_backup = tmp_path / "cached.7z.bak"
    archive_path.write_bytes(b"old archive")
    metadata_path.write_bytes(b"old metadata")
    temporary_archive.write_bytes(b"new archive")
    temporary_metadata.write_bytes(b"new metadata")
    archive_backup.write_bytes(b"manual recovery archive")

    with pytest.raises(IgnBdTopoDownloadError, match="backup|recovery|manual"):
        ign_bdtopo_fr._publish_cache_pair(
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

<a id="r15-test-official-checksum-mismatch-is-rejected"></a>
### `test_official_checksum_mismatch_is_rejected`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_official_checksum_mismatch_is_rejected`. Source lines 769–786.

**Verified purpose:** Configure a SHA256 pin of 64 zeroes for real synthetic 7z bytes from a mocked opener. Require archive checksum error, no .7z or .part output. This is a negative SHA256 case, not positive MD5/SHA official verification.

**Exact signature**

```python
def test_official_checksum_mismatch_is_rejected(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoArchiveError, match="checksum\|SHA")`
- Exact assertions:
  - `assert not list(cache_dir.glob("*.7z"))`
  - `assert not list(cache_dir.glob("*.part"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_synthetic_archive_bytes` | `tests.unit.test_ign_bdtopo_fr._synthetic_archive_bytes` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `pytest.raises` | `pytest.raises` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `cache_dir.glob` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `cache_dir.glob` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_official_checksum_mismatch_is_rejected(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path)
    config = _synthetic_config(source_config, official_checksum="0" * 64)
    cache_dir = tmp_path / "cache"

    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(archive_content),
        ),
        pytest.raises(IgnBdTopoArchiveError, match="checksum|SHA"),
    ):
        download_ign_bdtopo_archive(config, cache_dir)

    assert not list(cache_dir.glob("*.7z"))
    assert not list(cache_dir.glob("*.part"))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-unsafe-parent-archive-member-is-rejected"></a>
### `test_unsafe_parent_archive_member_is_rejected`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_unsafe_parent_archive_member_is_rejected`. Source lines 789–813.

**Verified purpose:** Pack a real synthetic GPKG under ../escape.gpkg, successfully download its bytes via a mocked stream, then require unsafe-member ArchiveError from extraction. Assert no escaped file and no top-level .part directory; not a live download.

**Exact signature**

```python
def test_unsafe_parent_archive_member_is_rejected(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoArchiveError, match="unsafe\|member\|path")`
- Exact assertions:
  - `assert not (tmp_path / "escape.gpkg").exists()`
  - `assert not list(tmp_path.glob("*.part"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_write_gpkg` | `tests.unit.test_ign_bdtopo_fr._write_gpkg` |
| `_pack_7z` | `tests.unit.test_ign_bdtopo_fr._pack_7z` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `pytest.raises` | `pytest.raises` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |
| `(tmp_path / "escape.gpkg").exists` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `tmp_path.glob` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `(tmp_path / "escape.gpkg").exists`<br>`tmp_path.glob` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_unsafe_parent_archive_member_is_rejected(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    gpkg_path = tmp_path / "unsafe-source.gpkg"
    _write_gpkg(gpkg_path)
    archive_content = _pack_7z(
        tmp_path / "unsafe.7z",
        [(gpkg_path, "../escape.gpkg")],
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")

    with pytest.raises(IgnBdTopoArchiveError, match="unsafe|member|path"):
        extract_ign_bdtopo_archive(
            download,
            config,
            extraction_dir=tmp_path / "extracted",
        )

    assert not (tmp_path / "escape.gpkg").exists()
    assert not list(tmp_path.glob("*.part"))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-geopackage-is-discovered-recursively"></a>
### `test_geopackage_is_discovered_recursively`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_geopackage_is_discovered_recursively`. Source lines 816–820.

**Verified purpose:** Write a genuine synthetic GPKG under nested directories and assert the standalone discovery helper returns exactly that Path. This is discovery, not config/archive-bound loading.

**Exact signature**

```python
def test_geopackage_is_discovered_recursively(tmp_path: Path) -> None:
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
  - `assert discover_ign_bdtopo_geopackage(tmp_path) == gpkg_path`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_write_gpkg` | `tests.unit.test_ign_bdtopo_fr._write_gpkg` |
| `discover_ign_bdtopo_geopackage` | `landscout.sources.ign_bdtopo_fr.discover_ign_bdtopo_geopackage` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_geopackage_is_discovered_recursively(tmp_path: Path) -> None:
    gpkg_path = tmp_path / "nested" / "data" / "bdtopo.gpkg"
    _write_gpkg(gpkg_path)

    assert discover_ign_bdtopo_geopackage(tmp_path) == gpkg_path
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-multiple-geopackages-are-rejected-as-ambiguous"></a>
### `test_multiple_geopackages_are_rejected_as_ambiguous`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_multiple_geopackages_are_rejected_as_ambiguous`. Source lines 823–828.

**Verified purpose:** Write two real synthetic GPKGs and require ArchiveError from standalone recursive discovery. No layer/config provenance validation is asserted.

**Exact signature**

```python
def test_multiple_geopackages_are_rejected_as_ambiguous(tmp_path: Path) -> None:
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
  - `pytest.raises(IgnBdTopoArchiveError, match="GeoPackage\|exactly one\|ambiguous")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_write_gpkg` | `tests.unit.test_ign_bdtopo_fr._write_gpkg` |
| `pytest.raises` | `pytest.raises` |
| `discover_ign_bdtopo_geopackage` | `landscout.sources.ign_bdtopo_fr.discover_ign_bdtopo_geopackage` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_multiple_geopackages_are_rejected_as_ambiguous(tmp_path: Path) -> None:
    _write_gpkg(tmp_path / "a" / "one.gpkg")
    _write_gpkg(tmp_path / "b" / "two.gpkg")

    with pytest.raises(IgnBdTopoArchiveError, match="GeoPackage|exactly one|ambiguous"):
        discover_ign_bdtopo_geopackage(tmp_path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-real-layer-names-are-listed-and-discovered"></a>
### `test_real_layer_names_are_listed_and_discovered`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_real_layer_names_are_listed_and_discovered`. Source lines 831–843.

**Verified purpose:** List/discover a real temporary two-layer GPKG and compare sets of line/post names and the selected names. Real means native physical metadata here, not official IGN bytes; no layer-order or four-role assertion.

**Exact signature**

```python
def test_real_layer_names_are_listed_and_discovered(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert set(all_layers) == {LINE_LAYER, POST_LAYER}`
  - `assert selection.electric_lines_layer == LINE_LAYER`
  - `assert selection.transformation_posts_layer == POST_LAYER`
  - `assert set(selection.all_layer_names) == {LINE_LAYER, POST_LAYER}`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_write_gpkg` | `tests.unit.test_ign_bdtopo_fr._write_gpkg` |
| `list_ign_bdtopo_layers` | `landscout.sources.ign_bdtopo_fr.list_ign_bdtopo_layers` |
| `discover_ign_bdtopo_layers` | `landscout.sources.ign_bdtopo_fr.discover_ign_bdtopo_layers` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_real_layer_names_are_listed_and_discovered(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    gpkg_path = tmp_path / "bdtopo.gpkg"
    _write_gpkg(gpkg_path)

    all_layers = list_ign_bdtopo_layers(gpkg_path)
    selection = discover_ign_bdtopo_layers(gpkg_path, source_config)

    assert set(all_layers) == {LINE_LAYER, POST_LAYER}
    assert selection.electric_lines_layer == LINE_LAYER
    assert selection.transformation_posts_layer == POST_LAYER
    assert set(selection.all_layer_names) == {LINE_LAYER, POST_LAYER}
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-missing-electric-line-layer-fails"></a>
### `test_missing_electric_line_layer_fails`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_missing_electric_line_layer_fails`. Source lines 846–853.

**Verified purpose:** Write a synthetic GPKG without the line layer and require LayerError from the public two-electricity-role discovery helper. No feature loading.

**Exact signature**

```python
def test_missing_electric_line_layer_fails(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoLayerError, match="electric\|line\|Ligne")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_write_gpkg` | `tests.unit.test_ign_bdtopo_fr._write_gpkg` |
| `pytest.raises` | `pytest.raises` |
| `discover_ign_bdtopo_layers` | `landscout.sources.ign_bdtopo_fr.discover_ign_bdtopo_layers` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_missing_electric_line_layer_fails(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    gpkg_path = tmp_path / "posts-only.gpkg"
    _write_gpkg(gpkg_path, include_lines=False)

    with pytest.raises(IgnBdTopoLayerError, match="electric|line|Ligne"):
        discover_ign_bdtopo_layers(gpkg_path, source_config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-missing-transformation-post-layer-fails"></a>
### `test_missing_transformation_post_layer_fails`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_missing_transformation_post_layer_fails`. Source lines 856–863.

**Verified purpose:** Write a synthetic GPKG without posts and require LayerError from two-role discovery. No feature loading.

**Exact signature**

```python
def test_missing_transformation_post_layer_fails(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoLayerError, match="transformation\|post\|Poste")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_write_gpkg` | `tests.unit.test_ign_bdtopo_fr._write_gpkg` |
| `pytest.raises` | `pytest.raises` |
| `discover_ign_bdtopo_layers` | `landscout.sources.ign_bdtopo_fr.discover_ign_bdtopo_layers` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_missing_transformation_post_layer_fails(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    gpkg_path = tmp_path / "lines-only.gpkg"
    _write_gpkg(gpkg_path, include_posts=False)

    with pytest.raises(IgnBdTopoLayerError, match="transformation|post|Poste"):
        discover_ign_bdtopo_layers(gpkg_path, source_config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-ambiguous-electric-line-layers-fail"></a>
### `test_ambiguous_electric_line_layers_fail`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_ambiguous_electric_line_layers_fail`. Source lines 866–885.

**Verified purpose:** Add a second physically matching line layer to a synthetic GPKG and require the ambiguous/found-2 LayerError from electricity discovery.

**Exact signature**

```python
def test_ambiguous_electric_line_layers_fail(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoLayerError, match="unambiguous\|found 2")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_write_gpkg` | `tests.unit.test_ign_bdtopo_fr._write_gpkg` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `LineString` | `shapely.geometry.LineString` |
| `pyogrio.write_dataframe` | `pyogrio.write_dataframe` |
| `pytest.raises` | `pytest.raises` |
| `discover_ign_bdtopo_layers` | `landscout.sources.ign_bdtopo_fr.discover_ign_bdtopo_layers` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `pyogrio.write_dataframe(secondary_lines, gpkg_path, layer="LIGNE_ELECTRIQUE_SECONDAIRE", driver="GPKG", append=True)` adds a layer to the synthetic GeoPackage. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_ambiguous_electric_line_layers_fail(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    gpkg_path = tmp_path / "ambiguous-lines.gpkg"
    _write_gpkg(gpkg_path)
    secondary_lines = gpd.GeoDataFrame(
        {"object_id": ["L_SECONDARY"]},
        geometry=[LineString([(0, 0), (50, 50)])],
        crs="EPSG:2154",
    )
    pyogrio.write_dataframe(
        secondary_lines,
        gpkg_path,
        layer="LIGNE_ELECTRIQUE_SECONDAIRE",
        driver="GPKG",
        append=True,
    )

    with pytest.raises(IgnBdTopoLayerError, match="unambiguous|found 2"):
        discover_ign_bdtopo_layers(gpkg_path, source_config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-synthetic-archive-extracts-and-discovers-required-layers"></a>
### `test_synthetic_archive_extracts_and_discovers_required_layers`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_synthetic_archive_extracts_and_discovers_required_layers`. Source lines 888–907.

**Verified purpose:** Mock transport of a genuine four-role synthetic archive, then call public extraction. Assert GPKG existence and line/post selected names only; no independent exhaustive inventory assertion.

**Exact signature**

```python
def test_synthetic_archive_extracts_and_discovers_required_layers(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert extraction.geopackage_path.is_file()`
  - `assert extraction.electric_lines_layer == LINE_LAYER`
  - `assert extraction.transformation_posts_layer == POST_LAYER`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_synthetic_archive_bytes` | `tests.unit.test_ign_bdtopo_fr._synthetic_archive_bytes` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |
| `extraction.geopackage_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `extraction.geopackage_path.is_file` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_synthetic_archive_extracts_and_discovers_required_layers(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source")
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")

    extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )

    assert extraction.geopackage_path.is_file()
    assert extraction.electric_lines_layer == LINE_LAYER
    assert extraction.transformation_posts_layer == POST_LAYER
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-schema-v3-extraction-metadata-binds-complete-physical-inventory"></a>
### `test_schema_v3_extraction_metadata_binds_complete_physical_inventory`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_schema_v3_extraction_metadata_binds_complete_physical_inventory`. Source lines 910–941.

**Verified purpose:** Read the real synthetic extraction marker: assert schema 3, physical GPKG size/SHA and matching envelope values, road/department names and at least one entry. Reextract and assert a cache hit with matching size/SHA. Eleven assertions do not independently enumerate every inventory entry.

**Exact signature**

```python
def test_schema_v3_extraction_metadata_binds_complete_physical_inventory(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert metadata["schema_version"] == 3`
  - `assert (<br>        metadata["geopackage_size_bytes"] == extraction.geopackage_path.stat().st_size<br>    )`
  - `assert (<br>        metadata["geopackage_sha256"]<br>        == sha256(extraction.geopackage_path.read_bytes()).hexdigest()<br>    )`
  - `assert extraction.geopackage_size_bytes == metadata["geopackage_size_bytes"]`
  - `assert extraction.geopackage_sha256 == metadata["geopackage_sha256"]`
  - `assert metadata["road_segments_layer"] == ROAD_LAYER`
  - `assert metadata["department_layer"] == DEPARTMENT_LAYER`
  - `assert len(metadata["extracted_entries"]) >= 1`
  - `assert cached.cache_hit is True`
  - `assert cached.geopackage_size_bytes == metadata["geopackage_size_bytes"]`
  - `assert cached.geopackage_sha256 == metadata["geopackage_sha256"]`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_extracted_fixture` | `tests.unit.test_ign_bdtopo_fr._extracted_fixture` |
| `json.loads` | `json.loads` |
| `_extraction_metadata_path(extraction.extraction_path).read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `_extraction_metadata_path` | `tests.unit.test_ign_bdtopo_fr._extraction_metadata_path` |
| `extraction.geopackage_path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(extraction.geopackage_path.read_bytes()).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `extraction.geopackage_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `_extraction_metadata_path(extraction.extraction_path).read_text`<br>`extraction.geopackage_path.stat`<br>`sha256(extraction.geopackage_path.read_bytes()).hexdigest`<br>`extraction.geopackage_path.read_bytes` |
| Filesystem/archive write or publication | read_text is read-only. Synthetic fixture setup/download/extraction writes through the called helpers; no direct marker write in this test. |
| Hashing/byte identity | `sha256(extraction.geopackage_path.read_bytes()).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_schema_v3_extraction_metadata_binds_complete_physical_inventory(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    config, download, extraction = _extracted_fixture(tmp_path, source_config)
    metadata = json.loads(
        _extraction_metadata_path(extraction.extraction_path).read_text(
            encoding="utf-8"
        )
    )

    assert metadata["schema_version"] == 3
    assert (
        metadata["geopackage_size_bytes"] == extraction.geopackage_path.stat().st_size
    )
    assert (
        metadata["geopackage_sha256"]
        == sha256(extraction.geopackage_path.read_bytes()).hexdigest()
    )
    assert extraction.geopackage_size_bytes == metadata["geopackage_size_bytes"]
    assert extraction.geopackage_sha256 == metadata["geopackage_sha256"]
    assert metadata["road_segments_layer"] == ROAD_LAYER
    assert metadata["department_layer"] == DEPARTMENT_LAYER
    assert len(metadata["extracted_entries"]) >= 1

    cached = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=extraction.extraction_path,
    )
    assert cached.cache_hit is True
    assert cached.geopackage_size_bytes == metadata["geopackage_size_bytes"]
    assert cached.geopackage_sha256 == metadata["geopackage_sha256"]
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-extraction-rejects-forged-download-lineage-before-archive-open"></a>
### `test_extraction_rejects_forged_download_lineage_before_archive_open`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_extraction_rejects_forged_download_lineage_before_archive_open`. Source lines 956–980.

**Verified purpose:** Use dataclasses.replace to forge one of provider/product/department/edition/source URL/filename/official-checksum flag. Public extraction must raise ArchiveError matching config/envelope; SevenZipFile sentinel is explicitly uncalled. Filename can fail path-name consistency before config equality.

**Exact signature**

```python
def test_extraction_rejects_forged_download_lineage_before_archive_open(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    field: str,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "value"),
    [
        ("provider", "UNTRUSTED"),
        ("product", "OTHER PRODUCT"),
        ("department_code", "32"),
        ("edition", "2025-01-01"),
        ("source_url", "https://example.test/other.7z"),
        ("filename", "other.7z"),
        ("official_checksum_validated", True),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |
| `field` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoArchiveError, match="config\|envelope")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_extracted_fixture` | `tests.unit.test_ign_bdtopo_fr._extracted_fixture` |
| `replace` | `dataclasses.replace` |
| `patch` | `unittest.mock.patch` |
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |
| `seven_zip.assert_not_called` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_extraction_rejects_forged_download_lineage_before_archive_open(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    field: str,
    value: object,
) -> None:
    config, download, extraction = _extracted_fixture(tmp_path, source_config)
    forged = replace(download, **{field: value})

    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.py7zr.SevenZipFile",
            side_effect=AssertionError(
                "forged lineage must fail before archive access"
            ),
        ) as seven_zip,
        pytest.raises(IgnBdTopoArchiveError, match="config|envelope"),
    ):
        extract_ign_bdtopo_archive(
            forged,
            config,
            extraction_dir=extraction.extraction_path,
        )

    seven_zip.assert_not_called()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-same-size-geopackage-tamper-invalidates-extraction-cache"></a>
### `test_same_size_geopackage_tamper_invalidates_extraction_cache`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_same_size_geopackage_tamper_invalidates_extraction_cache`. Source lines 983–1000.

**Verified purpose:** Flip the last GPKG byte without changing size, then reextract from the still-valid synthetic archive. Assert equal tampered size, cache_hit=False and exact restored original GPKG bytes; no repaired geometry or official source.

**Exact signature**

```python
def test_same_size_geopackage_tamper_invalidates_extraction_cache(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert extraction.geopackage_path.stat().st_size == len(original)`
  - `assert rebuilt.cache_hit is False`
  - `assert rebuilt.geopackage_path.read_bytes() == original`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_extracted_fixture` | `tests.unit.test_ign_bdtopo_fr._extracted_fixture` |
| `extraction.geopackage_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `bytearray` | `unresolved local/third-party receiver; no ownership inferred` |
| `extraction.geopackage_path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `extraction.geopackage_path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |
| `rebuilt.geopackage_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `extraction.geopackage_path.read_bytes`<br>`extraction.geopackage_path.stat`<br>`rebuilt.geopackage_path.read_bytes` |
| Filesystem/archive write or publication | `extraction.geopackage_path.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `tampered[-1] ^= 1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_same_size_geopackage_tamper_invalidates_extraction_cache(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    config, download, extraction = _extracted_fixture(tmp_path, source_config)
    original = extraction.geopackage_path.read_bytes()
    tampered = bytearray(original)
    tampered[-1] ^= 1
    extraction.geopackage_path.write_bytes(tampered)
    assert extraction.geopackage_path.stat().st_size == len(original)

    rebuilt = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=extraction.extraction_path,
    )

    assert rebuilt.cache_hit is False
    assert rebuilt.geopackage_path.read_bytes() == original
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-forged-extraction-metadata-never-returns-cache-hit"></a>
### `test_forged_extraction_metadata_never_returns_cache_hit`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_forged_extraction_metadata_never_returns_cache_hit`. Source lines 1014–1032.

**Verified purpose:** Change one marker field: SHA, size, old schema 1, bool/float schema or parent-traversing package path. Public extraction rebuilds and returns cache_hit=False. Cases can fail model parsing or containment before byte comparison; only the miss is asserted.

**Exact signature**

```python
def test_forged_extraction_metadata_never_returns_cache_hit(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    field: str,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "value"),
    [
        ("geopackage_sha256", "0" * 64),
        ("geopackage_size_bytes", 1),
        ("schema_version", 1),
        ("schema_version", True),
        ("schema_version", 1.0),
        ("geopackage_relative_path", "../escape.gpkg"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |
| `field` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert rebuilt.cache_hit is False`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_extracted_fixture` | `tests.unit.test_ign_bdtopo_fr._extracted_fixture` |
| `_extraction_metadata_path` | `tests.unit.test_ign_bdtopo_fr._extraction_metadata_path` |
| `json.loads` | `json.loads` |
| `metadata_path.read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `metadata_path.read_text` |
| Filesystem/archive write or publication | `metadata_path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `metadata[field] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_forged_extraction_metadata_never_returns_cache_hit(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    field: str,
    value: object,
) -> None:
    config, download, extraction = _extracted_fixture(tmp_path, source_config)
    metadata_path = _extraction_metadata_path(extraction.extraction_path)
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata[field] = value
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")

    rebuilt = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=extraction.extraction_path,
    )

    assert rebuilt.cache_hit is False
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-linked-extraction-metadata-never-returns-cache-hit"></a>
### `test_linked_extraction_metadata_never_returns_cache_hit`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_linked_extraction_metadata_never_returns_cache_hit`. Source lines 1036–1074.

**Verified purpose:** Simulate symlink/junction only for the marker with delegating Path predicates. Public extraction rejects the unsafe marker and SevenZipFile is explicitly uncalled. No actual OS link is created and the failure precedes archive-byte validation.

**Exact signature**

```python
def test_linked_extraction_metadata_never_returns_cache_hit(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
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
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `link_kind` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoArchiveError, match="marker\|non-linked")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_extracted_fixture` | `tests.unit.test_ign_bdtopo_fr._extracted_fixture` |
| `_extraction_metadata_path` | `tests.unit.test_ign_bdtopo_fr._extraction_metadata_path` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `patch.object` | `unittest.mock.patch.object` |
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |
| `seven_zip.assert_not_called` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_linked_extraction_metadata_never_returns_cache_hit(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    monkeypatch: pytest.MonkeyPatch,
    link_kind: str,
) -> None:
    config, download, extraction = _extracted_fixture(tmp_path, source_config)
    metadata_path = _extraction_metadata_path(extraction.extraction_path)
    original_is_symlink = Path.is_symlink
    original_is_junction = Path.is_junction

    def simulated_is_symlink(path: Path) -> bool:
        return (link_kind == "symlink" and path == metadata_path) or (
            original_is_symlink(path)
        )

    def simulated_is_junction(path: Path) -> bool:
        return (link_kind == "junction" and path == metadata_path) or (
            original_is_junction(path)
        )

    monkeypatch.setattr(Path, "is_symlink", simulated_is_symlink)
    monkeypatch.setattr(Path, "is_junction", simulated_is_junction)

    with (
        patch.object(
            ign_bdtopo_fr.py7zr,
            "SevenZipFile",
            side_effect=AssertionError("linked marker reached archive extraction"),
        ) as seven_zip,
        pytest.raises(IgnBdTopoArchiveError, match="marker|non-linked"),
    ):
        extract_ign_bdtopo_archive(
            download,
            config,
            extraction_dir=extraction.extraction_path,
        )

    seven_zip.assert_not_called()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-linked-extraction-metadata-never-returns-cache-hit-simulated-is-symlink"></a>
### `test_linked_extraction_metadata_never_returns_cache_hit.simulated_is_symlink`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_linked_extraction_metadata_never_returns_cache_hit.simulated_is_symlink`. Source lines 1047–1050.

**Verified purpose:** Return true for the target marker in the symlink case, otherwise call the original Path.is_symlink. This is a predicate simulation, not link creation.

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
  - `(link_kind == "symlink" and path == metadata_path) or (<br>            original_is_symlink(path)<br>        )`
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
        return (link_kind == "symlink" and path == metadata_path) or (
            original_is_symlink(path)
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-linked-extraction-metadata-never-returns-cache-hit-simulated-is-junction"></a>
### `test_linked_extraction_metadata_never_returns_cache_hit.simulated_is_junction`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_linked_extraction_metadata_never_returns_cache_hit.simulated_is_junction`. Source lines 1052–1055.

**Verified purpose:** Return true for the target marker in the junction case, otherwise call the original Path.is_junction. No actual junction is created.

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
  - `(link_kind == "junction" and path == metadata_path) or (<br>            original_is_junction(path)<br>        )`
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
        return (link_kind == "junction" and path == metadata_path) or (
            original_is_junction(path)
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-malformed-geopackage-sha-is-not-trusted"></a>
### `test_malformed_geopackage_sha_is_not_trusted`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_malformed_geopackage_sha_is_not_trusted`. Source lines 1081–1096.

**Verified purpose:** Set marker SHA to empty, abc, uppercase length-64, length-63 or length-65 text. Public extraction rebuilds; assert only cache_hit=False. Canonical model validation rejects before physical hash comparison.

**Exact signature**

```python
def test_malformed_geopackage_sha_is_not_trusted(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    value: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "value",
    ["", "abc", "A" * 64, "a" * 63, "a" * 65],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert rebuilt.cache_hit is False`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_extracted_fixture` | `tests.unit.test_ign_bdtopo_fr._extracted_fixture` |
| `_extraction_metadata_path` | `tests.unit.test_ign_bdtopo_fr._extraction_metadata_path` |
| `json.loads` | `json.loads` |
| `metadata_path.read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `metadata_path.read_text` |
| Filesystem/archive write or publication | `metadata_path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `metadata["geopackage_sha256"] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_malformed_geopackage_sha_is_not_trusted(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    value: str,
) -> None:
    config, download, extraction = _extracted_fixture(tmp_path, source_config)
    metadata_path = _extraction_metadata_path(extraction.extraction_path)
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["geopackage_sha256"] = value
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")

    rebuilt = extract_ign_bdtopo_archive(
        download, config, extraction_dir=extraction.extraction_path
    )

    assert rebuilt.cache_hit is False
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-malformed-geopackage-size-is-not-trusted"></a>
### `test_malformed_geopackage_size_is_not_trusted`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_malformed_geopackage_size_is_not_trusted`. Source lines 1100–1115.

**Verified purpose:** Set marker size to 0, -1, True or string 100. Strict-positive model parsing rejects before physical comparison; public extraction rebuilds and cache_hit=False is the sole assertion.

**Exact signature**

```python
def test_malformed_geopackage_size_is_not_trusted(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("value", [0, -1, True, "100"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert rebuilt.cache_hit is False`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_extracted_fixture` | `tests.unit.test_ign_bdtopo_fr._extracted_fixture` |
| `_extraction_metadata_path` | `tests.unit.test_ign_bdtopo_fr._extraction_metadata_path` |
| `json.loads` | `json.loads` |
| `metadata_path.read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `metadata_path.read_text` |
| Filesystem/archive write or publication | `metadata_path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `metadata["geopackage_size_bytes"] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_malformed_geopackage_size_is_not_trusted(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    value: object,
) -> None:
    config, download, extraction = _extracted_fixture(tmp_path, source_config)
    metadata_path = _extraction_metadata_path(extraction.extraction_path)
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["geopackage_size_bytes"] = value
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")

    rebuilt = extract_ign_bdtopo_archive(
        download, config, extraction_dir=extraction.extraction_path
    )

    assert rebuilt.cache_hit is False
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-default-extraction-path-is-short-and-content-addressed"></a>
### `test_default_extraction_path_is_short_and_content_addressed`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_default_extraction_path_is_short_and_content_addressed`. Source lines 1118–1134.

**Verified purpose:** Download/extract synthetic bytes without explicit extraction_dir; assert cache/x/first-16-SHA path, a 16-character final component and existing GPKG. This tests the convention, not collision freedom of a truncated digest.

**Exact signature**

```python
def test_default_extraction_path_is_short_and_content_addressed(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert extraction.extraction_path == cache_dir / "x" / download.sha256[:16]`
  - `assert len(extraction.extraction_path.name) == 16`
  - `assert extraction.geopackage_path.is_file()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_synthetic_archive_bytes` | `tests.unit.test_ign_bdtopo_fr._synthetic_archive_bytes` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `extraction.geopackage_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `extraction.geopackage_path.is_file` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_default_extraction_path_is_short_and_content_addressed(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source")
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, cache_dir)

    extraction = extract_ign_bdtopo_archive(download, config)

    assert extraction.extraction_path == cache_dir / "x" / download.sha256[:16]
    assert len(extraction.extraction_path.name) == 16
    assert extraction.geopackage_path.is_file()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-layer-loader-retains-crs-counts-and-null-geometries"></a>
### `test_layer_loader_retains_crs_counts_and_null_geometries`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_layer_loader_retains_crs_counts_and_null_geometries`. Source lines 1137–1156.

**Verified purpose:** Call the private untrusted reader alias on a real temporary line layer. Assert EPSG:2154, two IDs in order, one null geometry and summary counts 2/1/0. No source-config/archive binding is exercised.

**Exact signature**

```python
def test_layer_loader_retains_crs_counts_and_null_geometries(tmp_path: Path) -> None:
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
  - `assert frame.crs is not None`
  - `assert frame.crs.to_epsg() == 2154`
  - `assert len(frame) == 2`
  - `assert frame["object_id"].tolist() == ["L_VALID", "L_NULL"]`
  - `assert frame.geometry.isna().sum() == 1`
  - `assert summary.feature_count == 2`
  - `assert summary.null_geometry_count == 1`
  - `assert summary.invalid_geometry_count == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_write_gpkg` | `tests.unit.test_ign_bdtopo_fr._write_gpkg` |
| `load_untrusted_ign_bdtopo_layer` | `landscout.sources.ign_bdtopo_fr._load_untrusted_ign_bdtopo_layer` |
| `frame.crs.to_epsg` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["object_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.geometry.isna().sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `frame.geometry.isna().sum`<br>`frame.geometry.isna` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_layer_loader_retains_crs_counts_and_null_geometries(tmp_path: Path) -> None:
    gpkg_path = tmp_path / "bdtopo.gpkg"
    _write_gpkg(gpkg_path)

    loaded = load_untrusted_ign_bdtopo_layer(
        gpkg_path,
        LINE_LAYER,
        "electric_lines",
    )
    frame = loaded.data
    summary = loaded.summary

    assert frame.crs is not None
    assert frame.crs.to_epsg() == 2154
    assert len(frame) == 2
    assert frame["object_id"].tolist() == ["L_VALID", "L_NULL"]
    assert frame.geometry.isna().sum() == 1
    assert summary.feature_count == 2
    assert summary.null_geometry_count == 1
    assert summary.invalid_geometry_count == 0
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-invalid-geometry-is-preserved-without-repair"></a>
### `test_invalid_geometry_is_preserved_without_repair`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_invalid_geometry_is_preserved_without_repair`. Source lines 1159–1176.

**Verified purpose:** Call the private untrusted reader on three synthetic posts including null and invalid geometry. Assert three rows, the selected invalid geometry remains invalid and summary counts 3/1/1. There is no independent exact WKB comparison.

**Exact signature**

```python
def test_invalid_geometry_is_preserved_without_repair(tmp_path: Path) -> None:
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
  - `assert len(frame) == 3`
  - `assert invalid_row.geometry.is_valid is False`
  - `assert summary.feature_count == 3`
  - `assert summary.null_geometry_count == 1`
  - `assert summary.invalid_geometry_count == 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_write_gpkg` | `tests.unit.test_ign_bdtopo_fr._write_gpkg` |
| `load_untrusted_ign_bdtopo_layer` | `landscout.sources.ign_bdtopo_fr._load_untrusted_ign_bdtopo_layer` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_invalid_geometry_is_preserved_without_repair(tmp_path: Path) -> None:
    gpkg_path = tmp_path / "bdtopo.gpkg"
    _write_gpkg(gpkg_path, invalid_post=True)

    loaded = load_untrusted_ign_bdtopo_layer(
        gpkg_path,
        POST_LAYER,
        "transformation_posts",
    )
    frame = loaded.data
    summary = loaded.summary

    invalid_row = frame.loc[frame["object_id"] == "P_INVALID"].iloc[0]
    assert len(frame) == 3
    assert invalid_row.geometry.is_valid is False
    assert summary.feature_count == 3
    assert summary.null_geometry_count == 1
    assert summary.invalid_geometry_count == 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-geographic-crs-is-rejected"></a>
### `test_geographic_crs_is_rejected`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_geographic_crs_is_rejected`. Source lines 1179–1184.

**Verified purpose:** Read an EPSG:4326 synthetic line layer through the private untrusted alias and require LayerError matching CRS/projected/Lambert. Not a source-complete public-loader test.

**Exact signature**

```python
def test_geographic_crs_is_rejected(tmp_path: Path) -> None:
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
  - `pytest.raises(IgnBdTopoLayerError, match="2154\|Lambert\|projected\|CRS")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_write_gpkg` | `tests.unit.test_ign_bdtopo_fr._write_gpkg` |
| `pytest.raises` | `pytest.raises` |
| `load_untrusted_ign_bdtopo_layer` | `landscout.sources.ign_bdtopo_fr._load_untrusted_ign_bdtopo_layer` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_geographic_crs_is_rejected(tmp_path: Path) -> None:
    gpkg_path = tmp_path / "geographic.gpkg"
    _write_gpkg(gpkg_path, include_posts=False, crs="EPSG:4326")

    with pytest.raises(IgnBdTopoLayerError, match="2154|Lambert|projected|CRS"):
        load_untrusted_ign_bdtopo_layer(gpkg_path, LINE_LAYER, "electric_lines")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-electricity-loader-retains-both-layer-counts"></a>
### `test_electricity_loader_retains_both_layer_counts`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_electricity_loader_retains_both_layer_counts`. Source lines 1187–1209.

**Verified purpose:** Acquire/extract a synthetic archive with invalid post under mocked transport and call public electricity loading with config. Assert two lines, three posts, both EPSG:2154 and one invalid-post summary count. No official source or exhaustive value equality.

**Exact signature**

```python
def test_electricity_loader_retains_both_layer_counts(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert len(electricity.electric_lines) == 2`
  - `assert len(electricity.transformation_posts) == 3`
  - `assert electricity.electric_lines.crs.to_epsg() == 2154`
  - `assert electricity.transformation_posts.crs.to_epsg() == 2154`
  - `assert electricity.transformation_posts_summary.invalid_geometry_count == 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_synthetic_archive_bytes` | `tests.unit.test_ign_bdtopo_fr._synthetic_archive_bytes` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |
| `load_ign_bdtopo_electricity` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_electricity` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `electricity.electric_lines.crs.to_epsg` | `unresolved local/third-party receiver; no ownership inferred` |
| `electricity.transformation_posts.crs.to_epsg` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_electricity_loader_retains_both_layer_counts(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source", invalid_post=True)
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )

    electricity = load_ign_bdtopo_electricity(extraction, config)

    assert len(electricity.electric_lines) == 2
    assert len(electricity.transformation_posts) == 3
    assert electricity.electric_lines.crs.to_epsg() == 2154
    assert electricity.transformation_posts.crs.to_epsg() == 2154
    assert electricity.transformation_posts_summary.invalid_geometry_count == 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-road-layer-discovery-loads-selected-physical-layer"></a>
### `test_road_layer_discovery_loads_selected_physical_layer`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_road_layer_discovery_loads_selected_physical_layer`. Source lines 1212–1232.

**Verified purpose:** Acquire/extract synthetic four-role data and call public road loading. Assert retained extraction identity, physical/logical road names, R_LINE/R_MULTI order and summary PROXY_GEOMETRY. No road access classification.

**Exact signature**

```python
def test_road_layer_discovery_loads_selected_physical_layer(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert loaded.extraction is extraction`
  - `assert loaded.road_segments_summary.source_layer_name == ROAD_LAYER`
  - `assert loaded.road_segments_summary.logical_name == "road_segments"`
  - `assert loaded.road_segments["object_id"].tolist() == ["R_LINE", "R_MULTI"]`
  - `assert loaded.road_segments_summary.spatial_role == "PROXY_GEOMETRY"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_synthetic_archive_bytes` | `tests.unit.test_ign_bdtopo_fr._synthetic_archive_bytes` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |
| `ign_bdtopo_fr.load_ign_bdtopo_roads` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_roads` |
| `loaded.road_segments["object_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_road_layer_discovery_loads_selected_physical_layer(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source", include_roads=True)
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )

    loaded = ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)

    assert loaded.extraction is extraction
    assert loaded.road_segments_summary.source_layer_name == ROAD_LAYER
    assert loaded.road_segments_summary.logical_name == "road_segments"
    assert loaded.road_segments["object_id"].tolist() == ["R_LINE", "R_MULTI"]
    assert loaded.road_segments_summary.spatial_role == "PROXY_GEOMETRY"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-road-physical-layer-cannot-collide-with-electricity-roles"></a>
### `test_road_physical_layer_cannot_collide_with_electricity_roles`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_road_physical_layer_cannot_collide_with_electricity_roles`. Source lines 1239–1255.

**Verified purpose:** Copy either electricity selector into the road config, reconstruct a valid model and call public road loading on the synthetic extraction. Require LayerError at physical role distinctness; distinct config containers alone do not establish distinct layers.

**Exact signature**

```python
def test_road_physical_layer_cannot_collide_with_electricity_roles(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    role: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "role",
    ["electric_lines", "transformation_posts"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |
| `role` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoLayerError, match="same layer\|collid\|role")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_extracted_fixture` | `tests.unit.test_ign_bdtopo_fr._extracted_fixture` |
| `config.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoSourceConfig.model_validate` | `pydantic.BaseModel.model_validate` (inherited by `landscout.sources.ign_bdtopo_fr.IgnBdTopoSourceConfig`) |
| `pytest.raises` | `pytest.raises` |
| `ign_bdtopo_fr.load_ign_bdtopo_roads` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_roads` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `content["access"]["road_segments"] = selected` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_road_physical_layer_cannot_collide_with_electricity_roles(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    role: str,
) -> None:
    config, _, extraction = _extracted_fixture(
        tmp_path,
        source_config,
        include_roads=True,
    )
    content = config.model_dump(mode="json")
    selected = content["logical_layers"][role]
    content["access"]["road_segments"] = selected
    colliding = IgnBdTopoSourceConfig.model_validate(content)

    with pytest.raises(IgnBdTopoLayerError, match="same layer|collid|role"):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, colliding)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-department-physical-layer-cannot-collide-with-road-role"></a>
### `test_department_physical_layer_cannot_collide_with_road_role`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_department_physical_layer_cannot_collide_with_road_role`. Source lines 1258–1274.

**Verified purpose:** Replace department match_tokens with road tokens, reconstruct the model and call public coverage loading. Physical discovery selects the road twice and raises LayerError before department feature selection.

**Exact signature**

```python
def test_department_physical_layer_cannot_collide_with_road_role(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoLayerError, match="distinct\|role\|same layer")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_extracted_fixture` | `tests.unit.test_ign_bdtopo_fr._extracted_fixture` |
| `config.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoSourceConfig.model_validate` | `pydantic.BaseModel.model_validate` (inherited by `landscout.sources.ign_bdtopo_fr.IgnBdTopoSourceConfig`) |
| `pytest.raises` | `pytest.raises` |
| `load_ign_bdtopo_department_coverage` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_department_coverage` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `content["coverage"]["department_layer"]["match_tokens"] = content["access"][<br>        "road_segments"<br>    ]["match_tokens"]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_department_physical_layer_cannot_collide_with_road_role(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
) -> None:
    config, _, extraction = _extracted_fixture(
        tmp_path,
        source_config,
        include_roads=True,
    )
    content = config.model_dump(mode="json")
    content["coverage"]["department_layer"]["match_tokens"] = content["access"][
        "road_segments"
    ]["match_tokens"]
    colliding = IgnBdTopoSourceConfig.model_validate(content)

    with pytest.raises(IgnBdTopoLayerError, match="distinct|role|same layer"):
        load_ign_bdtopo_department_coverage(extraction, colliding)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-department-physical-layer-cannot-collide-with-electricity-roles"></a>
### `test_department_physical_layer_cannot_collide_with_electricity_roles`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_department_physical_layer_cannot_collide_with_electricity_roles`. Source lines 1281–1298.

**Verified purpose:** Replace department tokens with line or post tokens; public coverage loading rejects four-role collision after config validation and physical discovery, before selected-feature checks.

**Exact signature**

```python
def test_department_physical_layer_cannot_collide_with_electricity_roles(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    role: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "role",
    ["electric_lines", "transformation_posts"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |
| `role` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoLayerError, match="distinct\|role\|same layer")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_extracted_fixture` | `tests.unit.test_ign_bdtopo_fr._extracted_fixture` |
| `config.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoSourceConfig.model_validate` | `pydantic.BaseModel.model_validate` (inherited by `landscout.sources.ign_bdtopo_fr.IgnBdTopoSourceConfig`) |
| `pytest.raises` | `pytest.raises` |
| `load_ign_bdtopo_department_coverage` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_department_coverage` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `content["coverage"]["department_layer"]["match_tokens"] = content["logical_layers"][<br>        role<br>    ]["match_tokens"]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_department_physical_layer_cannot_collide_with_electricity_roles(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    role: str,
) -> None:
    config, _, extraction = _extracted_fixture(
        tmp_path,
        source_config,
        include_roads=True,
    )
    content = config.model_dump(mode="json")
    content["coverage"]["department_layer"]["match_tokens"] = content["logical_layers"][
        role
    ]["match_tokens"]
    colliding = IgnBdTopoSourceConfig.model_validate(content)

    with pytest.raises(IgnBdTopoLayerError, match="distinct|role|same layer"):
        load_ign_bdtopo_department_coverage(extraction, colliding)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-electricity-physical-layers-must-be-distinct"></a>
### `test_electricity_physical_layers_must_be_distinct`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_electricity_physical_layers_must_be_distinct`. Source lines 1301–1315.

**Verified purpose:** Give the post selector the single token ligne while line tokens remain distinct as phrases. Config validation succeeds but both selectors resolve to the same physical layer; public electricity loading raises LayerError.

**Exact signature**

```python
def test_electricity_physical_layers_must_be_distinct(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoLayerError, match="distinct\|role\|same layer")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_extracted_fixture` | `tests.unit.test_ign_bdtopo_fr._extracted_fixture` |
| `config.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoSourceConfig.model_validate` | `pydantic.BaseModel.model_validate` (inherited by `landscout.sources.ign_bdtopo_fr.IgnBdTopoSourceConfig`) |
| `pytest.raises` | `pytest.raises` |
| `load_ign_bdtopo_electricity` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_electricity` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `content["logical_layers"]["transformation_posts"]["match_tokens"] = ["ligne"]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_electricity_physical_layers_must_be_distinct(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
) -> None:
    config, _, extraction = _extracted_fixture(
        tmp_path,
        source_config,
        include_roads=True,
    )
    content = config.model_dump(mode="json")
    content["logical_layers"]["transformation_posts"]["match_tokens"] = ["ligne"]
    colliding = IgnBdTopoSourceConfig.model_validate(content)

    with pytest.raises(IgnBdTopoLayerError, match="distinct|role|same layer"):
        load_ign_bdtopo_electricity(extraction, colliding)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-missing-road-layer-fails-safely"></a>
### `test_missing_road_layer_fails_safely`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_missing_road_layer_fails_safely`. Source lines 1318–1336.

**Verified purpose:** Download a genuine synthetic archive omitting roads, then require LayerError from extraction discovery (not from load_ign_bdtopo_roads). Transport is mocked.

**Exact signature**

```python
def test_missing_road_layer_fails_safely(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoLayerError, match="road\|route\|found 0")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_synthetic_archive_bytes` | `tests.unit.test_ign_bdtopo_fr._synthetic_archive_bytes` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `pytest.raises` | `pytest.raises` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_missing_road_layer_fails_safely(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(
        tmp_path / "source",
        include_roads=False,
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    with pytest.raises(IgnBdTopoLayerError, match="road|route|found 0"):
        extract_ign_bdtopo_archive(
            download,
            config,
            extraction_dir=tmp_path / "extracted",
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-ambiguous-road-layer-fails-safely"></a>
### `test_ambiguous_road_layer_fails_safely`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_ambiguous_road_layer_fails_safely`. Source lines 1339–1371.

**Verified purpose:** Add a second road match to a synthetic GPKG, pack/download it with mocked transport and require LayerError during extraction. The fixture also lacks the default-disabled department layer; road ambiguity is checked first and is not an isolated otherwise-valid four-role package.

**Exact signature**

```python
def test_ambiguous_road_layer_fails_safely(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoLayerError, match="road\|route\|found 2")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_write_gpkg` | `tests.unit.test_ign_bdtopo_fr._write_gpkg` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `LineString` | `shapely.geometry.LineString` |
| `pyogrio.write_dataframe` | `pyogrio.write_dataframe` |
| `_pack_7z` | `tests.unit.test_ign_bdtopo_fr._pack_7z` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `pytest.raises` | `pytest.raises` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `pyogrio.write_dataframe(secondary, gpkg_path, layer="TRONCON_DE_ROUTE_SECONDAIRE", driver="GPKG", append=True)` adds a layer to the synthetic GeoPackage. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_ambiguous_road_layer_fails_safely(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    gpkg_path = tmp_path / "source" / "ambiguous-roads.gpkg"
    _write_gpkg(gpkg_path, include_roads=True)
    secondary = gpd.GeoDataFrame(
        {"object_id": ["R_SECONDARY"]},
        geometry=[LineString([(0, 0), (10, 10)])],
        crs="EPSG:2154",
    )
    pyogrio.write_dataframe(
        secondary,
        gpkg_path,
        layer="TRONCON_DE_ROUTE_SECONDAIRE",
        driver="GPKG",
        append=True,
    )
    archive_content = _pack_7z(
        tmp_path / "ambiguous-roads.7z",
        [(gpkg_path, "PACKAGE/ambiguous-roads.gpkg")],
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    with pytest.raises(IgnBdTopoLayerError, match="road|route|found 2"):
        extract_ign_bdtopo_archive(
            download,
            config,
            extraction_dir=tmp_path / "extracted",
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-road-loader-rejects-wrong-archive-config-department"></a>
### `test_road_loader_rejects_wrong_archive_config_department`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_road_loader_rejects_wrong_archive_config_department`. Source lines 1374–1392.

**Verified purpose:** Extract synthetic department-31 data then supply a reconstructed department-32 config to public road loading. Archive/config lineage rejects before current physical GPKG loading; no road attribute is changed.

**Exact signature**

```python
def test_road_loader_rejects_wrong_archive_config_department(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoLayerError, match="department\|archive\|lineage")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_synthetic_archive_bytes` | `tests.unit.test_ign_bdtopo_fr._synthetic_archive_bytes` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |
| `IgnBdTopoSourceConfig.model_validate` | `pydantic.BaseModel.model_validate` (inherited by `landscout.sources.ign_bdtopo_fr.IgnBdTopoSourceConfig`) |
| `config.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `ign_bdtopo_fr.load_ign_bdtopo_roads` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_roads` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_road_loader_rejects_wrong_archive_config_department(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source", include_roads=True)
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )
    other_department = IgnBdTopoSourceConfig.model_validate(
        {**config.model_dump(mode="json"), "department_code": "32"}
    )

    with pytest.raises(IgnBdTopoLayerError, match="department|archive|lineage"):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, other_department)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-non-electric-layer-loaders-revalidate-mutated-role-config-before-read"></a>
### `test_non_electric_layer_loaders_revalidate_mutated_role_config_before_read`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_non_electric_layer_loaders_revalidate_mutated_role_config_before_read`. Source lines 1396–1425.

**Verified purpose:** Bypass nested model freezing to inject empty road tokens or a blank coverage identity field, then call the corresponding public loader. Require config LayerError and explicitly uncalled gpd.read_file sentinel. This checks boundary reconstruction, not normal assignment mutability.

**Exact signature**

```python
def test_non_electric_layer_loaders_revalidate_mutated_role_config_before_read(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    logical_role: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("logical_role", ["road", "coverage"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |
| `logical_role` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoLayerError, match="config")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_extracted_fixture` | `tests.unit.test_ign_bdtopo_fr._extracted_fixture` |
| `config.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `object.__setattr__` | `unresolved local/third-party receiver; no ownership inferred` |
| `patch.object` | `unittest.mock.patch.object` |
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `ign_bdtopo_fr.load_ign_bdtopo_roads` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_roads` |
| `load_ign_bdtopo_department_coverage` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_department_coverage` |
| `reader.assert_not_called` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `object.__setattr__(tampered.access.road_segments, "match_tokens", ())` in the road branch, or `object.__setattr__(tampered.coverage.department_layer, "department_code_field", " ")` in the coverage branch, changes a nested model of the local deep copy. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_non_electric_layer_loaders_revalidate_mutated_role_config_before_read(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    logical_role: str,
) -> None:
    config, _, extraction = _extracted_fixture(tmp_path, source_config)
    tampered = config.model_copy(deep=True)
    if logical_role == "road":
        object.__setattr__(tampered.access.road_segments, "match_tokens", ())
    else:
        object.__setattr__(
            tampered.coverage.department_layer,
            "department_code_field",
            " ",
        )

    with (
        patch.object(
            ign_bdtopo_fr.gpd,
            "read_file",
            side_effect=AssertionError("invalid config reached physical layer read"),
        ) as reader,
        pytest.raises(IgnBdTopoLayerError, match="config"),
    ):
        if logical_role == "road":
            ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, tampered)
        else:
            load_ign_bdtopo_department_coverage(extraction, tampered)

    reader.assert_not_called()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-road-loader-rejects-changed-layer-inventory"></a>
### `test_road_loader_rejects_changed_layer_inventory`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_road_loader_rejects_changed_layer_inventory`. Source lines 1428–1455.

**Verified purpose:** Append a new layer to the physical synthetic GPKG after extraction and call public road loading. Require inventory/changed LayerError. The stale envelope size/SHA makes physical integrity fail before the inventory comparison; the latter is not independently isolated.

**Exact signature**

```python
def test_road_loader_rejects_changed_layer_inventory(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoLayerError, match="inventory\|changed")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_synthetic_archive_bytes` | `tests.unit.test_ign_bdtopo_fr._synthetic_archive_bytes` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `LineString` | `shapely.geometry.LineString` |
| `pyogrio.write_dataframe` | `pyogrio.write_dataframe` |
| `pytest.raises` | `pytest.raises` |
| `ign_bdtopo_fr.load_ign_bdtopo_roads` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_roads` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `pyogrio.write_dataframe(added, extraction.geopackage_path, layer="ADDED_AFTER_EXTRACTION", driver="GPKG", append=True)` adds a layer to the extracted synthetic GeoPackage. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_road_loader_rejects_changed_layer_inventory(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source", include_roads=True)
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )
    added = gpd.GeoDataFrame(
        {"object_id": ["ADDED"]},
        geometry=[LineString([(0, 0), (1, 1)])],
        crs="EPSG:2154",
    )
    pyogrio.write_dataframe(
        added,
        extraction.geopackage_path,
        layer="ADDED_AFTER_EXTRACTION",
        driver="GPKG",
        append=True,
    )

    with pytest.raises(IgnBdTopoLayerError, match="inventory|changed"):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-road-loader-rejects-geographic-crs"></a>
### `test_road_loader_rejects_geographic_crs`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_road_loader_rejects_geographic_crs`. Source lines 1458–1475.

**Verified purpose:** Extract a synthetic archive whose road layer alone uses EPSG:4326, then require CRS LayerError from public road loading. Metadata extraction may succeed; feature CRS is checked by loading.

**Exact signature**

```python
def test_road_loader_rejects_geographic_crs(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoLayerError, match="2154\|Lambert\|projected\|CRS")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_synthetic_archive_bytes` | `tests.unit.test_ign_bdtopo_fr._synthetic_archive_bytes` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |
| `pytest.raises` | `pytest.raises` |
| `ign_bdtopo_fr.load_ign_bdtopo_roads` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_roads` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_road_loader_rejects_geographic_crs(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(
        tmp_path / "source", include_roads=True, road_crs="EPSG:4326"
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )

    with pytest.raises(IgnBdTopoLayerError, match="2154|Lambert|projected|CRS"):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-road-loader-preserves-lambert93-lines-unchanged"></a>
### `test_road_loader_preserves_lambert93_lines_unchanged`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_road_loader_preserves_lambert93_lines_unchanged`. Source lines 1482–1510.

**Verified purpose:** For homogeneous LineString and MultiLineString fixtures, compare public loaded roads with an independent gpd.read_file using assert_geodataframe_equal(check_crs=True), then assert EPSG:2154 and summary geometry type. Not an explicit byte-WKB/Z/M preservation proof.

**Exact signature**

```python
def test_road_loader_preserves_lambert93_lines_unchanged(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    road_geometry_kind: str,
    expected_geometry_type: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("road_geometry_kind", "expected_geometry_type"),
    [("line", "LineString"), ("multiline", "MultiLineString")],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |
| `road_geometry_kind` | positional-or-keyword | `str` | `required` |
| `expected_geometry_type` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert loaded.road_segments.crs.to_epsg() == 2154`
  - `assert loaded.road_segments_summary.geometry_types == (expected_geometry_type,)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_synthetic_archive_bytes` | `tests.unit.test_ign_bdtopo_fr._synthetic_archive_bytes` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |
| `gpd.read_file` | `geopandas.read_file` |
| `ign_bdtopo_fr.load_ign_bdtopo_roads` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_roads` |
| `assert_geodataframe_equal` | `geopandas.testing.assert_geodataframe_equal` |
| `loaded.road_segments.crs.to_epsg` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `gpd.read_file` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_road_loader_preserves_lambert93_lines_unchanged(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    road_geometry_kind: str,
    expected_geometry_type: str,
) -> None:
    archive_content = _synthetic_archive_bytes(
        tmp_path / "source",
        include_roads=True,
        road_geometry_kind=road_geometry_kind,
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )
    expected = gpd.read_file(
        extraction.geopackage_path, layer=ROAD_LAYER, engine="pyogrio"
    )

    loaded = ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)

    assert_geodataframe_equal(loaded.road_segments, expected, check_crs=True)
    assert loaded.road_segments.crs.to_epsg() == 2154
    assert loaded.road_segments_summary.geometry_types == (expected_geometry_type,)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-road-layer-does-not-change-electricity-loading-or-cache-shape"></a>
### `test_road_layer_does_not_change_electricity_loading_or_cache_shape`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_road_layer_does_not_change_electricity_loading_or_cache_shape`. Source lines 1513–1553.

**Verified purpose:** Load electricity from a four-role synthetic extraction. Assert two lines/two posts and their names, road/department marker names and the exact twelve-key schema-3 marker set. Does not test schema-1 download keys or every marker value.

**Exact signature**

```python
def test_road_layer_does_not_change_electricity_loading_or_cache_shape(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert len(electricity.electric_lines) == 2`
  - `assert len(electricity.transformation_posts) == 2`
  - `assert electricity.electric_lines_summary.source_layer_name == LINE_LAYER`
  - `assert electricity.transformation_posts_summary.source_layer_name == POST_LAYER`
  - `assert metadata["road_segments_layer"] == ROAD_LAYER`
  - `assert metadata["department_layer"] == DEPARTMENT_LAYER`
  - `assert set(metadata) == {<br>        "schema_version",<br>        "archive_sha256",<br>        "geopackage_relative_path",<br>        "geopackage_size_bytes",<br>        "geopackage_sha256",<br>        "all_layer_names",<br>        "electric_lines_layer",<br>        "transformation_posts_layer",<br>        "road_segments_layer",<br>        "department_layer",<br>        "extracted_entries",<br>        "spatial_role",<br>    }`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_synthetic_archive_bytes` | `tests.unit.test_ign_bdtopo_fr._synthetic_archive_bytes` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |
| `load_ign_bdtopo_electricity` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_electricity` |
| `json.loads` | `json.loads` |
| `(extraction.extraction_path / ".landscout-extraction.json").read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `(extraction.extraction_path / ".landscout-extraction.json").read_text` |
| Filesystem/archive write or publication | read_text is read-only. Synthetic fixture setup/download/extraction writes through the called helpers; no direct marker write in this test. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_road_layer_does_not_change_electricity_loading_or_cache_shape(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source", include_roads=True)
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )

    electricity = load_ign_bdtopo_electricity(extraction, config)
    metadata = json.loads(
        (extraction.extraction_path / ".landscout-extraction.json").read_text(
            encoding="utf-8"
        )
    )

    assert len(electricity.electric_lines) == 2
    assert len(electricity.transformation_posts) == 2
    assert electricity.electric_lines_summary.source_layer_name == LINE_LAYER
    assert electricity.transformation_posts_summary.source_layer_name == POST_LAYER
    assert metadata["road_segments_layer"] == ROAD_LAYER
    assert metadata["department_layer"] == DEPARTMENT_LAYER
    assert set(metadata) == {
        "schema_version",
        "archive_sha256",
        "geopackage_relative_path",
        "geopackage_size_bytes",
        "geopackage_sha256",
        "all_layer_names",
        "electric_lines_layer",
        "transformation_posts_layer",
        "road_segments_layer",
        "department_layer",
        "extracted_entries",
        "spatial_role",
    }
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-public-sources-export-only-stable-road-api"></a>
### `test_public_sources_export_only_stable_road_api`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_public_sources_export_only_stable_road_api`. Source lines 1556–1562.

**Verified purpose:** Assert package identity and __all__ membership for IgnBdTopoRoadData/load_ign_bdtopo_roads, and absence of _discover_road_layer and obsolete load_ign_bdtopo_layer. These six checks are not an exhaustive audit of every package export.

**Exact signature**

```python
def test_public_sources_export_only_stable_road_api() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert sources.IgnBdTopoRoadData is ign_bdtopo_fr.IgnBdTopoRoadData`
  - `assert sources.load_ign_bdtopo_roads is ign_bdtopo_fr.load_ign_bdtopo_roads`
  - `assert "IgnBdTopoRoadData" in sources.__all__`
  - `assert "load_ign_bdtopo_roads" in sources.__all__`
  - `assert not hasattr(sources, "_discover_road_layer")`
  - `assert not hasattr(sources, "load_ign_bdtopo_layer")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `hasattr` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_public_sources_export_only_stable_road_api() -> None:
    assert sources.IgnBdTopoRoadData is ign_bdtopo_fr.IgnBdTopoRoadData
    assert sources.load_ign_bdtopo_roads is ign_bdtopo_fr.load_ign_bdtopo_roads
    assert "IgnBdTopoRoadData" in sources.__all__
    assert "load_ign_bdtopo_roads" in sources.__all__
    assert not hasattr(sources, "_discover_road_layer")
    assert not hasattr(sources, "load_ign_bdtopo_layer")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15--archive-info"></a>
### `_archive_info`

Qualified owner: `tests.unit.test_ign_bdtopo_fr._archive_info`. Source lines 1565–1578.

**Verified purpose:** Build SimpleNamespace fake member metadata with filename, complementary file/directory flags, no symlink/encryption, and size or None for directories. No actual archive or filesystem inspection.

**Exact signature**

```python
def _archive_info(
    name: str,
    *,
    directory: bool = False,
    size: int = 1,
) -> SimpleNamespace:
```

- Exact decorators: none.
- Declared return annotation: `SimpleNamespace`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `name` | positional-or-keyword | `str` | `required` |
| `directory` | keyword-only | `bool` | `False` |
| `size` | keyword-only | `int` | `1` |

**Return and exception contract**

- Exact observed return expressions:
  - `SimpleNamespace(<br>        filename=name,<br>        is_file=not directory,<br>        is_directory=directory,<br>        is_symlink=False,<br>        encrypted=False,<br>        uncompressed=None if directory else size,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_ign_bdtopo_fr::test_7z_windows_unsafe_member_names_fail_closed` via `_archive_info`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_7z_windows_unsafe_member_names_fail_closed` via `_archive_info`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_7z_casefold_and_nfkc_destination_collisions_fail` via `_archive_info`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_7z_casefold_and_nfkc_destination_collisions_fail` via `_archive_info`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_7z_nfkc_separator_destinations_fail_closed` via `_archive_info`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_7z_nfkc_separator_destinations_fail_closed` via `_archive_info`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_7z_parent_file_conflict_fails_closed` via `_archive_info`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_7z_parent_file_conflict_fails_closed` via `_archive_info`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_7z_encrypted_archive_fails_closed` via `_archive_info`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_7z_encrypted_archive_fails_closed` via `_archive_info`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `SimpleNamespace` | `types.SimpleNamespace` |

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
def _archive_info(
    name: str,
    *,
    directory: bool = False,
    size: int = 1,
) -> SimpleNamespace:
    return SimpleNamespace(
        filename=name,
        is_file=not directory,
        is_directory=directory,
        is_symlink=False,
        encrypted=False,
        uncompressed=None if directory else size,
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15--fakearchive---init--"></a>
### `_FakeArchive.__init__`

Qualified owner: `tests.unit.test_ign_bdtopo_fr._FakeArchive.__init__`. Source lines 1582–1584.

**Verified purpose:** Assign the supplied infos list by reference and encrypted flag to self. Does not copy, validate or open an archive.

**Exact signature**

```python
def __init__(self, infos: list[SimpleNamespace], *, encrypted: bool = False):
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
| `infos` | positional-or-keyword | `list[SimpleNamespace]` | `required` |
| `encrypted` | keyword-only | `bool` | `False` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
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
| In-memory mutation | `self._infos = infos`<br>`self._encrypted = encrypted` |
| Direct parameter mutation | `self._infos = infos`<br>`self._encrypted = encrypted` |

**Complete source-ordered implementation**

```python
def __init__(self, infos: list[SimpleNamespace], *, encrypted: bool = False):
        self._infos = infos
        self._encrypted = encrypted
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15--fakearchive-needs-password"></a>
### `_FakeArchive.needs_password`

Qualified owner: `tests.unit.test_ign_bdtopo_fr._FakeArchive.needs_password`. Source lines 1586–1587.

**Verified purpose:** Return the stored encryption flag without I/O.

**Exact signature**

```python
def needs_password(self) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self._encrypted`
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
def needs_password(self) -> bool:
        return self._encrypted
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15--fakearchive-list"></a>
### `_FakeArchive.list`

Qualified owner: `tests.unit.test_ign_bdtopo_fr._FakeArchive.list`. Source lines 1589–1590.

**Verified purpose:** Return the same stored mutable member list, not a fresh parsed inventory or copy.

**Exact signature**

```python
def list(self) -> list[SimpleNamespace]:
```

- Exact decorators: none.
- Declared return annotation: `list[SimpleNamespace]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self._infos`
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
def list(self) -> list[SimpleNamespace]:
        return self._infos
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-7z-windows-unsafe-member-names-fail-closed"></a>
### `test_7z_windows_unsafe_member_names_fail_closed`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_7z_windows_unsafe_member_names_fail_closed`. Source lines 1603–1607.

**Verified purpose:** Pass fake inventory containing data.gpkg and one of CON.txt, trailing dot/space, question mark or newline names to private member validation. Require Windows/unsafe/reserved ArchiveError. No py7zr extraction or actual unsafe file creation.

**Exact signature**

```python
def test_7z_windows_unsafe_member_names_fail_closed(unsafe_name: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "unsafe_name",
    [
        "CON.txt",
        "folder/trailing.",
        "folder/edge ",
        "folder/bad?.txt",
        "folder/control\n.txt",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `unsafe_name` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoArchiveError, match="Windows\|unsafe\|reserved")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_FakeArchive` | `tests.unit.test_ign_bdtopo_fr._FakeArchive` |
| `_archive_info` | `tests.unit.test_ign_bdtopo_fr._archive_info` |
| `pytest.raises` | `pytest.raises` |
| `ign_bdtopo_fr._validate_archive_members` | `landscout.sources.ign_bdtopo_fr._validate_archive_members` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_7z_windows_unsafe_member_names_fail_closed(unsafe_name: str) -> None:
    archive = _FakeArchive([_archive_info("data.gpkg"), _archive_info(unsafe_name)])

    with pytest.raises(IgnBdTopoArchiveError, match="Windows|unsafe|reserved"):
        ign_bdtopo_fr._validate_archive_members(archive)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-7z-casefold-and-nfkc-destination-collisions-fail"></a>
### `test_7z_casefold_and_nfkc_destination_collisions_fail`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_7z_casefold_and_nfkc_destination_collisions_fail`. Source lines 1617–1630.

**Verified purpose:** Pass fake inventory with casefold-equivalent paths or composed/decomposed accent names to private validation. Require collision ArchiveError; tests normalization keys, not filesystem behavior.

**Exact signature**

```python
def test_7z_casefold_and_nfkc_destination_collisions_fail(
    first: str,
    second: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("first", "second"),
    [
        ("Folder/value.txt", "folder/VALUE.txt"),
        ("café.txt", "cafe\u0301.txt"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `first` | positional-or-keyword | `str` | `required` |
| `second` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoArchiveError, match="collision")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_FakeArchive` | `tests.unit.test_ign_bdtopo_fr._FakeArchive` |
| `_archive_info` | `tests.unit.test_ign_bdtopo_fr._archive_info` |
| `pytest.raises` | `pytest.raises` |
| `ign_bdtopo_fr._validate_archive_members` | `landscout.sources.ign_bdtopo_fr._validate_archive_members` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_7z_casefold_and_nfkc_destination_collisions_fail(
    first: str,
    second: str,
) -> None:
    archive = _FakeArchive(
        [
            _archive_info("data.gpkg"),
            _archive_info(first),
            _archive_info(second),
        ]
    )

    with pytest.raises(IgnBdTopoArchiveError, match="collision"):
        ign_bdtopo_fr._validate_archive_members(archive)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-7z-nfkc-separator-destinations-fail-closed"></a>
### `test_7z_nfkc_separator_destinations_fail_closed`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_7z_nfkc_separator_destinations_fail_closed`. Source lines 1640–1653.

**Verified purpose:** Pass fake inventory with fullwidth slash/backslash confusable and ordinary paths. NFKC component safety rejects the confusable before an ordinary collision is needed; require Windows/unsafe/collision ArchiveError, not successful extraction.

**Exact signature**

```python
def test_7z_nfkc_separator_destinations_fail_closed(
    confusable: str,
    ordinary: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("confusable", "ordinary"),
    [
        ("folder\uff0fchild.txt", "folder/child.txt"),
        ("folder\uff3cchild.txt", "folder/child.txt"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `confusable` | positional-or-keyword | `str` | `required` |
| `ordinary` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoArchiveError, match="Windows\|unsafe\|collision")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_FakeArchive` | `tests.unit.test_ign_bdtopo_fr._FakeArchive` |
| `_archive_info` | `tests.unit.test_ign_bdtopo_fr._archive_info` |
| `pytest.raises` | `pytest.raises` |
| `ign_bdtopo_fr._validate_archive_members` | `landscout.sources.ign_bdtopo_fr._validate_archive_members` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_7z_nfkc_separator_destinations_fail_closed(
    confusable: str,
    ordinary: str,
) -> None:
    archive = _FakeArchive(
        [
            _archive_info("data.gpkg"),
            _archive_info(confusable),
            _archive_info(ordinary),
        ]
    )

    with pytest.raises(IgnBdTopoArchiveError, match="Windows|unsafe|collision"):
        ign_bdtopo_fr._validate_archive_members(archive)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-7z-parent-file-conflict-fails-closed"></a>
### `test_7z_parent_file_conflict_fails_closed`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_7z_parent_file_conflict_fails_closed`. Source lines 1656–1666.

**Verified purpose:** Fake inventory makes parent a file and also supplies parent/child.txt, plus data.gpkg. Private member validation must raise parent-file ArchiveError; no actual conflicting tree.

**Exact signature**

```python
def test_7z_parent_file_conflict_fails_closed() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoArchiveError, match="parent-file")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_FakeArchive` | `tests.unit.test_ign_bdtopo_fr._FakeArchive` |
| `_archive_info` | `tests.unit.test_ign_bdtopo_fr._archive_info` |
| `pytest.raises` | `pytest.raises` |
| `ign_bdtopo_fr._validate_archive_members` | `landscout.sources.ign_bdtopo_fr._validate_archive_members` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_7z_parent_file_conflict_fails_closed() -> None:
    archive = _FakeArchive(
        [
            _archive_info("data.gpkg"),
            _archive_info("parent"),
            _archive_info("parent/child.txt"),
        ]
    )

    with pytest.raises(IgnBdTopoArchiveError, match="parent-file"):
        ign_bdtopo_fr._validate_archive_members(archive)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-7z-encrypted-archive-fails-closed"></a>
### `test_7z_encrypted_archive_fails_closed`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_7z_encrypted_archive_fails_closed`. Source lines 1669–1673.

**Verified purpose:** Set the fake archive encrypted flag and require encrypted ArchiveError from private validation. It rejects at needs_password, not by decoding encrypted bytes; list call count is not asserted.

**Exact signature**

```python
def test_7z_encrypted_archive_fails_closed() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoArchiveError, match="encrypted")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_FakeArchive` | `tests.unit.test_ign_bdtopo_fr._FakeArchive` |
| `_archive_info` | `tests.unit.test_ign_bdtopo_fr._archive_info` |
| `pytest.raises` | `pytest.raises` |
| `ign_bdtopo_fr._validate_archive_members` | `landscout.sources.ign_bdtopo_fr._validate_archive_members` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_7z_encrypted_archive_fails_closed() -> None:
    archive = _FakeArchive([_archive_info("data.gpkg")], encrypted=True)

    with pytest.raises(IgnBdTopoArchiveError, match="encrypted"):
        ign_bdtopo_fr._validate_archive_members(archive)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-extracted-inventory-mismatch-fails-closed"></a>
### `test_extracted_inventory_mismatch_fails_closed`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_extracted_inventory_mismatch_fails_closed`. Source lines 1676–1681.

**Verified purpose:** Write three bytes b"bad" to data.gpkg but expect a four-byte file in a manually constructed member record. Private tree comparison raises inventory ArchiveError; no GPKG parser or archive-member hash comparison.

**Exact signature**

```python
def test_extracted_inventory_mismatch_fails_closed(tmp_path: Path) -> None:
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
  - `pytest.raises(IgnBdTopoArchiveError, match="inventory")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `ign_bdtopo_fr._ValidatedArchiveMember` | `landscout.sources.ign_bdtopo_fr._ValidatedArchiveMember` |
| `(tmp_path / "data.gpkg").write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `ign_bdtopo_fr._validate_extracted_inventory` | `landscout.sources.ign_bdtopo_fr._validate_extracted_inventory` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `(tmp_path / "data.gpkg").write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_extracted_inventory_mismatch_fails_closed(tmp_path: Path) -> None:
    expected = (ign_bdtopo_fr._ValidatedArchiveMember("data.gpkg", "file", 4),)
    (tmp_path / "data.gpkg").write_bytes(b"bad")

    with pytest.raises(IgnBdTopoArchiveError, match="inventory"):
        ign_bdtopo_fr._validate_extracted_inventory(tmp_path, expected)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-stale-extraction-backup-blocks-before-7z-open"></a>
### `test_stale_extraction_backup_blocks_before_7z_open`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_stale_extraction_backup_blocks_before_7z_open`. Source lines 1684–1710.

**Verified purpose:** Create a sibling extraction .bak with sentinel bytes after a real synthetic extraction. Public reextraction must raise manual-recovery ArchiveError, SevenZipFile is explicitly uncalled and sentinel bytes remain. No recovery deletion.

**Exact signature**

```python
def test_stale_extraction_backup_blocks_before_7z_open(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoArchiveError, match="manual recovery")`
- Exact assertions:
  - `assert sentinel.read_bytes() == b"preserve"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_extracted_fixture` | `tests.unit.test_ign_bdtopo_fr._extracted_fixture` |
| `extraction.extraction_path.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `backup.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `sentinel.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `patch` | `unittest.mock.patch` |
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |
| `seven_zip.assert_not_called` | `unresolved local/third-party receiver; no ownership inferred` |
| `sentinel.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `sentinel.read_bytes` |
| Filesystem/archive write or publication | backup.mkdir and sentinel.write_bytes create recovery material. with_name only derives a Path. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_stale_extraction_backup_blocks_before_7z_open(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
) -> None:
    config, download, extraction = _extracted_fixture(tmp_path, source_config)
    backup = extraction.extraction_path.with_name(
        f"{extraction.extraction_path.name}.bak"
    )
    backup.mkdir()
    sentinel = backup / "manual-recovery.txt"
    sentinel.write_bytes(b"preserve")

    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.py7zr.SevenZipFile",
            side_effect=AssertionError("7z must not open with recovery material"),
        ) as seven_zip,
        pytest.raises(IgnBdTopoArchiveError, match="manual recovery"),
    ):
        extract_ign_bdtopo_archive(
            download,
            config,
            extraction_dir=extraction.extraction_path,
        )

    seven_zip.assert_not_called()
    assert sentinel.read_bytes() == b"preserve"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-extraction-publication-double-failure-preserves-backup"></a>
### `test_extraction_publication_double_failure_preserves_backup`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_extraction_publication_double_failure_preserves_backup`. Source lines 1713–1740.

**Verified purpose:** Use private directory publication with ordinary old.txt/new.txt trees. Delegate the initial target-to-backup rename but fail temporary publication and backup restoration. Require rollback ArchiveError and exact old.txt bytes in backup; not a 7z extraction test.

**Exact signature**

```python
def test_extraction_publication_double_failure_preserves_backup(
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
  - `pytest.raises(IgnBdTopoArchiveError, match="rollback")`
- Exact assertions:
  - `assert (backup / "old.txt").read_bytes() == b"old"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `target.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `temporary.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `(target / "old.txt").write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `(temporary / "new.txt").write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `patch.object` | `unittest.mock.patch.object` |
| `pytest.raises` | `pytest.raises` |
| `ign_bdtopo_fr._publish_extraction_directory` | `landscout.sources.ign_bdtopo_fr._publish_extraction_directory` |
| `(backup / "old.txt").read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `(backup / "old.txt").read_bytes` |
| Filesystem/archive write or publication | `target.mkdir`<br>`temporary.mkdir`<br>`(target / "old.txt").write_bytes`<br>`(temporary / "new.txt").write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_extraction_publication_double_failure_preserves_backup(
    tmp_path: Path,
) -> None:
    target = tmp_path / "extracted"
    temporary = tmp_path / "extracted.part"
    target.mkdir()
    temporary.mkdir()
    (target / "old.txt").write_bytes(b"old")
    (temporary / "new.txt").write_bytes(b"new")
    backup = tmp_path / "extracted.bak"
    original_replace = ign_bdtopo_fr._replace_directory

    def fail_publication_and_rollback(source: Path, destination: Path) -> None:
        if source == temporary or source == backup:
            raise OSError("simulated transaction failure")
        original_replace(source, destination)

    with (
        patch.object(
            ign_bdtopo_fr,
            "_replace_directory",
            side_effect=fail_publication_and_rollback,
        ),
        pytest.raises(IgnBdTopoArchiveError, match="rollback"),
    ):
        ign_bdtopo_fr._publish_extraction_directory(temporary, target)

    assert (backup / "old.txt").read_bytes() == b"old"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-extraction-publication-double-failure-preserves-backup-fail-publication-and-rollback"></a>
### `test_extraction_publication_double_failure_preserves_backup.fail_publication_and_rollback`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_extraction_publication_double_failure_preserves_backup.fail_publication_and_rollback`. Source lines 1725–1728.

**Verified purpose:** Raise OSError when source is the temporary or backup directory; otherwise delegate captured _replace_directory. In particular, the initial old-primary-to-backup rename really occurs.

**Exact signature**

```python
def fail_publication_and_rollback(source: Path, destination: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `Path` | `required` |
| `destination` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `OSError("simulated transaction failure")` under lexical guard `source == temporary or source == backup`.

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
def fail_publication_and_rollback(source: Path, destination: Path) -> None:
        if source == temporary or source == backup:
            raise OSError("simulated transaction failure")
        original_replace(source, destination)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-extraction-part-link-is-rejected-without-touching-target"></a>
### `test_extraction_part_link_is_rejected_without_touching_target`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_extraction_part_link_is_rejected_without_touching_target`. Source lines 1744–1826.

**Verified purpose:** After genuine synthetic fixture setup, simulate a .part symlink/junction via Path predicates. Compute real archive integrity once, then patch validation with that return_value (not delegation) and extraction SevenZipFile with a sentinel. Require safe-directory ArchiveError, validation called once with exact args, SevenZipFile uncalled, zero protected unlink/rmdir/rmtree counts and unchanged sentinel. No real OS link/junction is created.

**Exact signature**

```python
def test_extraction_part_link_is_rejected_without_touching_target(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
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
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `link_kind` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoArchiveError, match="safe ordinary directory")`
- Exact assertions:
  - `assert unlink_calls == 0`
  - `assert rmdir_calls == 0`
  - `assert rmtree_calls == 0`
  - `assert sentinel.read_bytes() == b"preserve"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_extracted_fixture` | `tests.unit.test_ign_bdtopo_fr._extracted_fixture` |
| `extraction_path.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `sentinel.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `validate_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.validate_ign_bdtopo_archive` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `patch.object` | `unittest.mock.patch.object` |
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |
| `archive_validation.assert_called_once_with` | `unresolved local/third-party receiver; no ownership inferred` |
| `seven_zip.assert_not_called` | `unresolved local/third-party receiver; no ownership inferred` |
| `sentinel.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_extraction_part_link_is_rejected_without_touching_target(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    monkeypatch: pytest.MonkeyPatch,
    link_kind: str,
) -> None:
    config, download, _ = _extracted_fixture(tmp_path, source_config)
    extraction_path = tmp_path / "linked-extraction"
    temporary = extraction_path.with_name(f"{extraction_path.name}.part")
    sentinel = tmp_path / "sentinel.txt"
    sentinel.write_bytes(b"preserve")
    integrity = validate_ign_bdtopo_archive(download.path, config)
    original_is_symlink = Path.is_symlink
    original_is_junction = Path.is_junction
    original_unlink = Path.unlink
    original_rmdir = Path.rmdir
    original_rmtree = ign_bdtopo_fr.shutil.rmtree
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
    monkeypatch.setattr(ign_bdtopo_fr.shutil, "rmtree", protected_rmtree)

    with (
        patch.object(
            ign_bdtopo_fr,
            "validate_ign_bdtopo_archive",
            return_value=integrity,
        ) as archive_validation,
        patch.object(
            ign_bdtopo_fr.py7zr,
            "SevenZipFile",
            side_effect=AssertionError("temporary link reached archive extraction"),
        ) as seven_zip,
        pytest.raises(IgnBdTopoArchiveError, match="safe ordinary directory"),
    ):
        extract_ign_bdtopo_archive(
            download,
            config,
            extraction_dir=extraction_path,
        )

    archive_validation.assert_called_once_with(download.path, config)
    seven_zip.assert_not_called()
    assert unlink_calls == 0
    assert rmdir_calls == 0
    assert rmtree_calls == 0
    assert sentinel.read_bytes() == b"preserve"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-extraction-part-link-is-rejected-without-touching-target-simulated-is-symlink"></a>
### `test_extraction_part_link_is_rejected_without_touching_target.simulated_is_symlink`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_extraction_part_link_is_rejected_without_touching_target.simulated_is_symlink`. Source lines 1765–1768.

**Verified purpose:** Report a symlink only for temporary in the symlink case; delegate other paths to the original predicate. No actual link creation.

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

<a id="r15-test-extraction-part-link-is-rejected-without-touching-target-simulated-is-junction"></a>
### `test_extraction_part_link_is_rejected_without_touching_target.simulated_is_junction`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_extraction_part_link_is_rejected_without_touching_target.simulated_is_junction`. Source lines 1770–1773.

**Verified purpose:** Report a junction only for temporary in the junction case; delegate other paths to the original predicate. No actual junction creation.

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

<a id="r15-test-extraction-part-link-is-rejected-without-touching-target-protected-unlink"></a>
### `test_extraction_part_link_is_rejected_without_touching_target.protected_unlink`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_extraction_part_link_is_rejected_without_touching_target.protected_unlink`. Source lines 1775–1780.

**Verified purpose:** If called on temporary, increment the nonlocal unlink counter and raise AssertionError; otherwise delegate original unlink with forwarded args/kwargs. Test asserts the protected branch is never reached.

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

<a id="r15-test-extraction-part-link-is-rejected-without-touching-target-protected-rmdir"></a>
### `test_extraction_part_link_is_rejected_without_touching_target.protected_rmdir`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_extraction_part_link_is_rejected_without_touching_target.protected_rmdir`. Source lines 1782–1787.

**Verified purpose:** If called on temporary, increment rmdir counter and raise AssertionError; otherwise delegate original rmdir. Test asserts zero protected calls.

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

<a id="r15-test-extraction-part-link-is-rejected-without-touching-target-protected-rmtree"></a>
### `test_extraction_part_link_is_rejected_without_touching_target.protected_rmtree`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_extraction_part_link_is_rejected_without_touching_target.protected_rmtree`. Source lines 1789–1794.

**Verified purpose:** Convert path to Path for target comparison; on temporary increment rmtree counter and raise AssertionError, otherwise delegate original shutil.rmtree. Test asserts zero protected calls; no deletion of a real junction is demonstrated.

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

<a id="r15-test-duplicate-ign-yaml-key-is-rejected"></a>
### `test_duplicate_ign_yaml_key_is_rejected`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_duplicate_ign_yaml_key_is_rejected`. Source lines 1829–1839.

**Verified purpose:** Write a two-provider duplicate-key YAML and call the public config loader. Require DownloadError whose cause text contains duplicate. This parse failure precedes validation of the otherwise incomplete model payload.

**Exact signature**

```python
def test_duplicate_ign_yaml_key_is_rejected(tmp_path: Path) -> None:
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
  - `pytest.raises(IgnBdTopoDownloadError)`
- Exact assertions:
  - `assert "duplicate" in str(captured.value.__cause__).casefold()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `config_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `load_ign_bdtopo_source_config` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_source_config` |
| `str(captured.value.__cause__).casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `config_path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_duplicate_ign_yaml_key_is_rejected(tmp_path: Path) -> None:
    config_path = tmp_path / "ign.yaml"
    config_path.write_text(
        "provider: IGN\nprovider: UNTRUSTED\n",
        encoding="utf-8",
    )

    with pytest.raises(IgnBdTopoDownloadError) as captured:
        load_ign_bdtopo_source_config(config_path)

    assert "duplicate" in str(captured.value.__cause__).casefold()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-ign-cache-schema-version-is-a-strict-integer"></a>
### `test_ign_cache_schema_version_is_a_strict_integer`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_ign_cache_schema_version_is_a_strict_integer`. Source lines 1843–1869.

**Verified purpose:** Directly model-validate a complete _CacheMetadata payload with schema True or 1.0 and require TypeError/ValidationError. Tests exact-int schema parsing, not disk cache reuse or source-config equality.

**Exact signature**

```python
def test_ign_cache_schema_version_is_a_strict_integer(
    schema_version: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("schema_version", [True, 1.0])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `schema_version` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises((TypeError, ValidationError))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `ign_bdtopo_fr._CacheMetadata.model_validate` | `pydantic.BaseModel.model_validate` (inherited by `landscout.sources.ign_bdtopo_fr._CacheMetadata`) |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_ign_cache_schema_version_is_a_strict_integer(
    schema_version: object,
) -> None:
    payload = {
        "schema_version": schema_version,
        "provider": "IGN",
        "product": "BD TOPO",
        "department_code": "31",
        "edition": "2026-06-15",
        "product_version": "3.5",
        "projection": "EPSG:2154",
        "package_format": "GPKG",
        "archive_format": "7z",
        "source_url": SYNTHETIC_SOURCE_URL,
        "checksum_url": None,
        "download_timestamp": "2026-08-11T15:32:03+00:00",
        "filename": "BDTOPO_TEST_D031.7z",
        "file_size": 1,
        "sha256": "a" * 64,
        "official_checksum_algorithm": None,
        "official_checksum": None,
        "official_checksum_validated": False,
        "spatial_role": "PROXY_GEOMETRY",
    }

    with pytest.raises((TypeError, ValidationError)):
        ign_bdtopo_fr._CacheMetadata.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-ign-cache-file-size-is-a-strict-integer"></a>
### `test_ign_cache_file_size_is_a_strict_integer`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_ign_cache_file_size_is_a_strict_integer`. Source lines 1873–1897.

**Verified purpose:** Directly validate _CacheMetadata with file_size True, 1.0 or string 1 and require ValidationError. No cache-file or network call.

**Exact signature**

```python
def test_ign_cache_file_size_is_a_strict_integer(value: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize("value", [True, 1.0, "1"])`.
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
| `pytest.raises` | `pytest.raises` |
| `ign_bdtopo_fr._CacheMetadata.model_validate` | `pydantic.BaseModel.model_validate` (inherited by `landscout.sources.ign_bdtopo_fr._CacheMetadata`) |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_ign_cache_file_size_is_a_strict_integer(value: object) -> None:
    payload = {
        "schema_version": 1,
        "provider": "IGN",
        "product": "BD TOPO",
        "department_code": "31",
        "edition": "2026-06-15",
        "product_version": "3.5",
        "projection": "EPSG:2154",
        "package_format": "GPKG",
        "archive_format": "7z",
        "source_url": SYNTHETIC_SOURCE_URL,
        "checksum_url": None,
        "download_timestamp": "2026-08-11T15:32:03+00:00",
        "filename": "BDTOPO_TEST_D031.7z",
        "file_size": value,
        "sha256": "a" * 64,
        "official_checksum_algorithm": None,
        "official_checksum": None,
        "official_checksum_validated": False,
        "spatial_role": "PROXY_GEOMETRY",
    }

    with pytest.raises(ValidationError):
        ign_bdtopo_fr._CacheMetadata.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-ign-cache-json-is-strict-before-model-validation"></a>
### `test_ign_cache_json_is_strict_before_model_validation`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_ign_cache_json_is_strict_before_model_validation`. Source lines 1908–1912.

**Verified purpose:** Directly call the shared loads_strict_json_object imported through the adapter with duplicate keys, NaN or a top-level array. Require ValueError. No metadata model, disk-cache reader or HTTP request is invoked.

**Exact signature**

```python
def test_ign_cache_json_is_strict_before_model_validation(
    invalid_json: bytes,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "invalid_json",
    [
        b'{"schema_version":1,"schema_version":1}',
        b'{"schema_version":NaN}',
        b"[]",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `invalid_json` | positional-or-keyword | `bytes` | `required` |

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
| `ign_bdtopo_fr.loads_strict_json_object` | `landscout.common.strict_json.loads_strict_json_object` (imported through the adapter) |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_ign_cache_json_is_strict_before_model_validation(
    invalid_json: bytes,
) -> None:
    with pytest.raises(ValueError):
        ign_bdtopo_fr.loads_strict_json_object(invalid_json)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-download-cache-reader-rejects-noncanonical-json-and-refreshes"></a>
### `test_download_cache_reader_rejects_noncanonical_json_and_refreshes`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_download_cache_reader_rejects_noncanonical_json_and_refreshes`. Source lines 1923–1945.

**Verified purpose:** Create a valid synthetic cache then replace the whole sidecar with duplicate-key/NaN/array JSON. Public download refreshes through one mocked opener call and returns cache_hit=False. The strict parser fails before incomplete model fields matter; no exact refreshed-byte assertion here.

**Exact signature**

```python
def test_download_cache_reader_rejects_noncanonical_json_and_refreshes(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    invalid_json: bytes,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "invalid_json",
    [
        b'{"schema_version":1,"schema_version":1}',
        b'{"schema_version":NaN}',
        b"[]",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |
| `invalid_json` | positional-or-keyword | `bytes` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert opener.call_count == 1`
  - `assert refreshed.cache_hit is False`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_synthetic_archive_bytes` | `tests.unit.test_ign_bdtopo_fr._synthetic_archive_bytes` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `_metadata_path(first.path).write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_metadata_path` | `tests.unit.test_ign_bdtopo_fr._metadata_path` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `_metadata_path(first.path).write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_download_cache_reader_rejects_noncanonical_json_and_refreshes(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    invalid_json: bytes,
) -> None:
    content = _synthetic_archive_bytes(tmp_path / "source")
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(content),
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
    _metadata_path(first.path).write_bytes(invalid_json)

    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(content),
    ) as opener:
        refreshed = download_ign_bdtopo_archive(config, cache_dir)

    assert opener.call_count == 1
    assert refreshed.cache_hit is False
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-extraction-cache-reader-rejects-noncanonical-json-and-rebuilds"></a>
### `test_extraction_cache_reader_rejects_noncanonical_json_and_rebuilds`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_extraction_cache_reader_rejects_noncanonical_json_and_rebuilds`. Source lines 1956–1970.

**Verified purpose:** Replace the synthetic marker with duplicate-key/Infinity/array JSON. Public extraction rebuilds from the local archive and asserts cache_hit=False only; no new download and no independently isolated model-field failure.

**Exact signature**

```python
def test_extraction_cache_reader_rejects_noncanonical_json_and_rebuilds(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    invalid_json: bytes,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "invalid_json",
    [
        b'{"schema_version":3,"schema_version":3}',
        b'{"schema_version":Infinity}',
        b"[]",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |
| `invalid_json` | positional-or-keyword | `bytes` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert rebuilt.cache_hit is False`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_extracted_fixture` | `tests.unit.test_ign_bdtopo_fr._extracted_fixture` |
| `_extraction_metadata_path(extraction.extraction_path).write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_extraction_metadata_path` | `tests.unit.test_ign_bdtopo_fr._extraction_metadata_path` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `_extraction_metadata_path(extraction.extraction_path).write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_extraction_cache_reader_rejects_noncanonical_json_and_rebuilds(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    invalid_json: bytes,
) -> None:
    config, download, extraction = _extracted_fixture(tmp_path, source_config)
    _extraction_metadata_path(extraction.extraction_path).write_bytes(invalid_json)

    rebuilt = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=extraction.extraction_path,
    )

    assert rebuilt.cache_hit is False
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-department-coverage-loader-selects-configured-identity"></a>
### `test_department_coverage_loader_selects_configured_identity`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_department_coverage_loader_selects_configured_identity`. Source lines 1973–2006.

**Verified purpose:** Acquire/extract synthetic departments 31/32, then public coverage loading selects one row with code 31, mirrored lineage/archive SHA and SOURCE_COVERAGE_BOUNDARY in EPSG:2154. Assert summary source count two, selected count one, identity field and MultiPolygon type. This is source extent, not service capacity.

**Exact signature**

```python
def test_department_coverage_loader_selects_configured_identity(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert loaded.source_layer == DEPARTMENT_LAYER`
  - `assert loaded.source_department_code == "31"`
  - `assert loaded.spatial_role == "SOURCE_COVERAGE_BOUNDARY"`
  - `assert len(loaded.coverage) == 1`
  - `assert loaded.coverage.loc[0, "code_insee"] == "31"`
  - `assert loaded.coverage.loc[0, "source_department_code"] == "31"`
  - `assert loaded.coverage.loc[0, "source_archive_sha256"] == download.sha256`
  - `assert loaded.coverage.loc[0, "spatial_role"] == "SOURCE_COVERAGE_BOUNDARY"`
  - `assert loaded.coverage.crs.to_epsg() == 2154`
  - `assert loaded.summary.source_feature_count == 2`
  - `assert loaded.summary.selected_feature_count == 1`
  - `assert loaded.summary.department_code_field == "code_insee"`
  - `assert loaded.summary.geometry_types == ("MultiPolygon",)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_synthetic_archive_bytes` | `tests.unit.test_ign_bdtopo_fr._synthetic_archive_bytes` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |
| `load_ign_bdtopo_department_coverage` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_department_coverage` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `loaded.coverage.crs.to_epsg` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_department_coverage_loader_selects_configured_identity(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(
        tmp_path / "source",
        include_department=True,
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )

    loaded = load_ign_bdtopo_department_coverage(extraction, config)

    assert loaded.source_layer == DEPARTMENT_LAYER
    assert loaded.source_department_code == "31"
    assert loaded.spatial_role == "SOURCE_COVERAGE_BOUNDARY"
    assert len(loaded.coverage) == 1
    assert loaded.coverage.loc[0, "code_insee"] == "31"
    assert loaded.coverage.loc[0, "source_department_code"] == "31"
    assert loaded.coverage.loc[0, "source_archive_sha256"] == download.sha256
    assert loaded.coverage.loc[0, "spatial_role"] == "SOURCE_COVERAGE_BOUNDARY"
    assert loaded.coverage.crs.to_epsg() == 2154
    assert loaded.summary.source_feature_count == 2
    assert loaded.summary.selected_feature_count == 1
    assert loaded.summary.department_code_field == "code_insee"
    assert loaded.summary.geometry_types == ("MultiPolygon",)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-department-coverage-requires-one-authoritative-feature"></a>
### `test_department_coverage_requires_one_authoritative_feature`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_department_coverage_requires_one_authoritative_feature`. Source lines 2014–2048.

**Verified purpose:** Build genuine synthetic packages with only department 32 or duplicate department 31 features. Public coverage loading must raise exactly-one/found LayerError after extraction; no arbitrary first-row selection.

**Exact signature**

```python
def test_department_coverage_requires_one_authoritative_feature(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    department_codes: list[str],
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "department_codes",
    [["32"], ["31", "31"]],
    ids=["missing", "duplicate"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |
| `department_codes` | positional-or-keyword | `list[str]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoLayerError, match="exactly one\|found")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `_write_gpkg` | `tests.unit.test_ign_bdtopo_fr._write_gpkg` |
| `_pack_7z` | `tests.unit.test_ign_bdtopo_fr._pack_7z` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |
| `pytest.raises` | `pytest.raises` |
| `load_ign_bdtopo_department_coverage` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_department_coverage` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_department_coverage_requires_one_authoritative_feature(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    department_codes: list[str],
) -> None:
    gpkg_path = tmp_path / "source" / "coverage.gpkg"
    geometries = [
        Polygon([(0, 0), (0, 100), (100, 100), (100, 0), (0, 0)])
        for _ in department_codes
    ]
    _write_gpkg(
        gpkg_path,
        include_department=True,
        include_roads=True,
        department_codes=department_codes,
        department_geometries=geometries,
    )
    archive_content = _pack_7z(
        tmp_path / "coverage.7z",
        [(gpkg_path, "PACKAGE/coverage.gpkg")],
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )

    with pytest.raises(IgnBdTopoLayerError, match="exactly one|found"):
        load_ign_bdtopo_department_coverage(extraction, config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-department-coverage-requires-configured-identity-field"></a>
### `test_department_coverage_requires_configured_identity_field`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_department_coverage_requires_configured_identity_field`. Source lines 2051–2073.

**Verified purpose:** Use a model-valid config requesting missing_code, extract a normal synthetic archive, then require identity-field LayerError from public coverage loading. Discovery does not validate feature attribute presence.

**Exact signature**

```python
def test_department_coverage_requires_configured_identity_field(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoLayerError, match="identity field\|missing_code")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_synthetic_archive_bytes` | `tests.unit.test_ign_bdtopo_fr._synthetic_archive_bytes` |
| `_synthetic_config(source_config).model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `IgnBdTopoSourceConfig.model_validate` | `pydantic.BaseModel.model_validate` (inherited by `landscout.sources.ign_bdtopo_fr.IgnBdTopoSourceConfig`) |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |
| `pytest.raises` | `pytest.raises` |
| `load_ign_bdtopo_department_coverage` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_department_coverage` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `content["coverage"]["department_layer"]["department_code_field"] = "missing_code"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_department_coverage_requires_configured_identity_field(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(
        tmp_path / "source",
        include_department=True,
    )
    content = _synthetic_config(source_config).model_dump(mode="json")
    content["coverage"]["department_layer"]["department_code_field"] = "missing_code"
    config = IgnBdTopoSourceConfig.model_validate(content)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )

    with pytest.raises(IgnBdTopoLayerError, match="identity field|missing_code"):
        load_ign_bdtopo_department_coverage(extraction, config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-missing-department-coverage-layer-fails"></a>
### `test_missing_department_coverage_layer_fails`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_missing_department_coverage_layer_fails`. Source lines 2076–2094.

**Verified purpose:** Create a synthetic archive with department layer disabled, mock its transport and require department/found-0 LayerError during extraction, not later coverage selection.

**Exact signature**

```python
def test_missing_department_coverage_layer_fails(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoLayerError, match="department\|found 0")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_synthetic_archive_bytes` | `tests.unit.test_ign_bdtopo_fr._synthetic_archive_bytes` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `pytest.raises` | `pytest.raises` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_missing_department_coverage_layer_fails(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(
        tmp_path / "source",
        include_department=False,
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    with pytest.raises(IgnBdTopoLayerError, match="department|found 0"):
        extract_ign_bdtopo_archive(
            download,
            config,
            extraction_dir=tmp_path / "extracted",
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-department-coverage-layer-discovery-must-be-unambiguous"></a>
### `test_department_coverage_layer_discovery_must_be_unambiguous`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_department_coverage_layer_discovery_must_be_unambiguous`. Source lines 2097–2129.

**Verified purpose:** Add a second matching department layer to a genuine synthetic four-role GPKG, pack/download and require ambiguous/found-2 LayerError during extraction discovery.

**Exact signature**

```python
def test_department_coverage_layer_discovery_must_be_unambiguous(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoLayerError, match="unambiguous\|found 2")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_write_gpkg` | `tests.unit.test_ign_bdtopo_fr._write_gpkg` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `Polygon` | `shapely.geometry.Polygon` |
| `pyogrio.write_dataframe` | `pyogrio.write_dataframe` |
| `_pack_7z` | `tests.unit.test_ign_bdtopo_fr._pack_7z` |
| `_synthetic_config` | `tests.unit.test_ign_bdtopo_fr._synthetic_config` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `pytest.raises` | `pytest.raises` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `pyogrio.write_dataframe(second, gpkg_path, layer="DEPARTEMENT_SECONDAIRE", driver="GPKG", append=True)` adds a layer to the synthetic GeoPackage. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_department_coverage_layer_discovery_must_be_unambiguous(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    gpkg_path = tmp_path / "source" / "ambiguous.gpkg"
    _write_gpkg(gpkg_path, include_department=True, include_roads=True)
    second = gpd.GeoDataFrame(
        {"code_insee": ["31"]},
        geometry=[Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])],
        crs="EPSG:2154",
    )
    pyogrio.write_dataframe(
        second,
        gpkg_path,
        layer="DEPARTEMENT_SECONDAIRE",
        driver="GPKG",
        append=True,
    )
    archive_content = _pack_7z(
        tmp_path / "ambiguous.7z",
        [(gpkg_path, "PACKAGE/ambiguous.gpkg")],
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    with pytest.raises(IgnBdTopoLayerError, match="unambiguous|found 2"):
        extract_ign_bdtopo_archive(
            download,
            config,
            extraction_dir=tmp_path / "extracted",
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-direct-consumers-reject-same-inventory-content-tampering"></a>
### `test_direct_consumers_reject_same_inventory_content_tampering`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_direct_consumers_reject_same_inventory_content_tampering`. Source lines 2140–2183.

**Verified purpose:** For electricity/roads/coverage replace the first HT/Bretelle/Department 31 byte sequence with equal-length text in the physical GPKG, retaining stale integrity metadata. Assert old bytes present and unchanged size, then public loading raises integrity LayerError. The layer parameter is unused and no post-mutation layer relisting is asserted; rejection is physical SHA, not isolated semantic attribute validation. Coverage constructs a second synthetic fixture.

**Exact signature**

```python
def test_direct_consumers_reject_same_inventory_content_tampering(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    consumer: str,
    layer: str,
    old_bytes: bytes,
    new_bytes: bytes,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("consumer", "layer", "old_bytes", "new_bytes"),
    [
        ("electricity", LINE_LAYER, b"HT", b"HX"),
        ("roads", ROAD_LAYER, b"Bretelle", b"BretellX"),
        ("coverage", DEPARTMENT_LAYER, b"Department 31", b"Department 3X"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |
| `consumer` | positional-or-keyword | `str` | `required` |
| `layer` | positional-or-keyword | `str` | `required` |
| `old_bytes` | positional-or-keyword | `bytes` | `required` |
| `new_bytes` | positional-or-keyword | `bytes` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoLayerError, match="integrity\|SHA\|physical\|changed")`
- Exact assertions:
  - `assert old_bytes in content`
  - `assert extraction.geopackage_path.stat().st_size == size_before`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_extracted_fixture` | `tests.unit.test_ign_bdtopo_fr._extracted_fixture` |
| `_synthetic_archive_bytes` | `tests.unit.test_ign_bdtopo_fr._synthetic_archive_bytes` |
| `patch` | `unittest.mock.patch` |
| `_response` | `tests.unit.test_ign_bdtopo_fr._response` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |
| `extraction.geopackage_path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `extraction.geopackage_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `extraction.geopackage_path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `content.replace` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `load_ign_bdtopo_electricity` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_electricity` |
| `ign_bdtopo_fr.load_ign_bdtopo_roads` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_roads` |
| `load_ign_bdtopo_department_coverage` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_department_coverage` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `extraction.geopackage_path.stat`<br>`extraction.geopackage_path.read_bytes` |
| Filesystem/archive write or publication | extraction.geopackage_path.write_bytes changes the file; content.replace only creates an in-memory bytes value. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_direct_consumers_reject_same_inventory_content_tampering(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    consumer: str,
    layer: str,
    old_bytes: bytes,
    new_bytes: bytes,
) -> None:
    config, _, extraction = _extracted_fixture(
        tmp_path,
        source_config,
        include_roads=True,
    )
    if consumer == "coverage":
        # Rebuild once with the configured department layer present.
        archive_content = _synthetic_archive_bytes(
            tmp_path / "coverage-source",
            include_roads=True,
            include_department=True,
        )
        with patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(archive_content),
        ):
            download = download_ign_bdtopo_archive(config, tmp_path / "coverage-cache")
        extraction = extract_ign_bdtopo_archive(
            download,
            config,
            extraction_dir=tmp_path / "coverage-extracted",
        )

    size_before = extraction.geopackage_path.stat().st_size
    content = extraction.geopackage_path.read_bytes()
    assert old_bytes in content
    extraction.geopackage_path.write_bytes(content.replace(old_bytes, new_bytes, 1))
    assert extraction.geopackage_path.stat().st_size == size_before

    with pytest.raises(IgnBdTopoLayerError, match="integrity|SHA|physical|changed"):
        if consumer == "electricity":
            load_ign_bdtopo_electricity(extraction, config)
        elif consumer == "roads":
            ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)
        else:
            load_ign_bdtopo_department_coverage(extraction, config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-road-loader-rejects-source-change-after-physical-read"></a>
### `test_road_loader_rejects_source_change_after_physical_read`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_road_loader_rejects_source_change_after_physical_read`. Source lines 2186–2209.

**Verified purpose:** Patch gpd.read_file with a delegating callback that reads the genuine synthetic frame and then changes GPKG bytes before returning it. Public road loading must raise changed/integrity/SHA LayerError at the postcondition. No reader-count assertion or general concurrent-snapshot guarantee.

**Exact signature**

```python
def test_road_loader_rejects_source_change_after_physical_read(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnBdTopoLayerError, match="changed\|integrity\|SHA")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_extracted_fixture` | `tests.unit.test_ign_bdtopo_fr._extracted_fixture` |
| `patch.object` | `unittest.mock.patch.object` |
| `pytest.raises` | `pytest.raises` |
| `ign_bdtopo_fr.load_ign_bdtopo_roads` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_roads` |

**Source-observed side-effect matrix**

The table lists direct lexical operations, excluding nested callback bodies. Fixture/helpers and public adapter calls can perform delegated synthetic I/O; the verified purpose above states the exercised boundary. No real transport occurs under the opener mocks.

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
def test_road_loader_rejects_source_change_after_physical_read(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
) -> None:
    config, _, extraction = _extracted_fixture(
        tmp_path,
        source_config,
        include_roads=True,
    )
    original_read = ign_bdtopo_fr.gpd.read_file

    def mutate_after_read(*args: object, **kwargs: object) -> gpd.GeoDataFrame:
        frame = original_read(*args, **kwargs)
        content = extraction.geopackage_path.read_bytes()
        extraction.geopackage_path.write_bytes(
            content.replace(b"Bretelle", b"BretellX", 1)
        )
        return frame

    with (
        patch.object(ign_bdtopo_fr.gpd, "read_file", side_effect=mutate_after_read),
        pytest.raises(IgnBdTopoLayerError, match="changed|integrity|SHA"),
    ):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r15-test-road-loader-rejects-source-change-after-physical-read-mutate-after-read"></a>
### `test_road_loader_rejects_source_change_after_physical_read.mutate_after_read`

Qualified owner: `tests.unit.test_ign_bdtopo_fr.test_road_loader_rejects_source_change_after_physical_read.mutate_after_read`. Source lines 2197–2203.

**Verified purpose:** Call the captured real reader with forwarded args/kwargs, read physical GPKG bytes, replace the first Bretelle with BretellX, write them and return the previously read frame. content.replace is an in-memory byte operation; write_bytes mutates the file. It does not update integrity metadata.

**Exact signature**

```python
def mutate_after_read(*args: object, **kwargs: object) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `frame`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `original_read` | `unresolved local/third-party receiver; no ownership inferred` |
| `extraction.geopackage_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `extraction.geopackage_path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `content.replace` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `extraction.geopackage_path.read_bytes` |
| Filesystem/archive write or publication | extraction.geopackage_path.write_bytes changes the file; content.replace only creates an in-memory bytes value. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def mutate_after_read(*args: object, **kwargs: object) -> gpd.GeoDataFrame:
        frame = original_read(*args, **kwargs)
        content = extraction.geopackage_path.read_bytes()
        extraction.geopackage_path.write_bytes(
            content.replace(b"Bretelle", b"BretellX", 1)
        )
        return frame
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **76**.
- Pytest fixtures (decorator-proven): **1**.

### Fixtures

- `source_config` — decorators: `pytest.fixture`.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Python assert statements (excludes assertion helper calls) | Exact regression purpose |
|---|---|---|---:|---|
| `test_valid_source_config_loads` | none | none | 9 | See [verified scenario and limits](#r15-test-valid-source-config-loads). |
| `test_loaded_ign_source_config_and_nested_models_are_frozen` | none | pytest.raises(ValidationError); pytest.raises(ValidationError) | 0 | See [verified scenario and limits](#r15-test-loaded-ign-source-config-and-nested-models-are-frozen). |
| `test_download_revalidates_a_tampered_config_before_network` | none | pytest.raises(IgnBdTopoDownloadError, match="config") | 0 | See [verified scenario and limits](#r15-test-download-revalidates-a-tampered-config-before-network). |
| `test_invalid_department_coverage_config_fails` | pytest.mark.parametrize("mutation", ["missing", "blank_field", "empty_tokens"]) | pytest.raises(ValidationError) | 0 | See [verified scenario and limits](#r15-test-invalid-department-coverage-config-fails). |
| `test_missing_required_source_field_fails` | pytest.mark.parametrize("field", ["source_url", "edition"]) | pytest.raises(ValidationError) | 0 | See [verified scenario and limits](#r15-test-missing-required-source-field-fails). |
| `test_invalid_source_configuration_fails` | pytest.mark.parametrize(<br>    ("field", "value"),<br>    [<br>        ("department_code", "3"),<br>        ("department_code", "XX"),<br>        ("projection", "EPSG:4326"),<br>        ("format", "SHP"),<br>        ("archive_format", "zip"),<br>    ],<br>) | pytest.raises(ValidationError) | 0 | See [verified scenario and limits](#r15-test-invalid-source-configuration-fails). |
| `test_unknown_source_config_field_is_rejected` | none | pytest.raises(ValidationError) | 0 | See [verified scenario and limits](#r15-test-unknown-source-config-field-is-rejected). |
| `test_successful_archive_download_persists_sha256` | none | none | 7 | See [verified scenario and limits](#r15-test-successful-archive-download-persists-sha256). |
| `test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum` | none | none | 5 | See [verified scenario and limits](#r15-test-archive-integrity-reports-local-sha256-and-no-fabricated-checksum). |
| `test_fresh_cache_is_reused_without_network` | none | none | 4 | See [verified scenario and limits](#r15-test-fresh-cache-is-reused-without-network). |
| `test_stale_recovery_backup_rejects_cache_before_network` | none | pytest.raises(IgnBdTopoDownloadError, match="backup\|recovery\|manual") | 2 | See [verified scenario and limits](#r15-test-stale-recovery-backup-rejects-cache-before-network). |
| `test_expired_cache_is_refreshed` | none | none | 6 | See [verified scenario and limits](#r15-test-expired-cache-is-refreshed). |
| `test_failed_refresh_preserves_valid_cache` | none | pytest.raises(IgnBdTopoDownloadError) | 4 | See [verified scenario and limits](#r15-test-failed-refresh-preserves-valid-cache). |
| `test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned` | none | pytest.raises(IgnBdTopoArchiveError) | 3 | See [verified scenario and limits](#r15-test-corrupt-new-archive-is-rejected-and-temporary-files-are-cleaned). |
| `test_corrupt_refresh_preserves_valid_cache` | none | pytest.raises(IgnBdTopoArchiveError) | 3 | See [verified scenario and limits](#r15-test-corrupt-refresh-preserves-valid-cache). |
| `test_metadata_publication_failure_restores_previous_cache_pair` | none | pytest.raises(IgnBdTopoDownloadError) | 5 | See [verified scenario and limits](#r15-test-metadata-publication-failure-restores-previous-cache-pair). |
| `test_publication_and_rollback_failure_preserves_exact_recovery_backups` | none | pytest.raises(IgnBdTopoDownloadError, match="rollback") | 2 | See [verified scenario and limits](#r15-test-publication-and-rollback-failure-preserves-exact-recovery-backups). |
| `test_cleanup_failure_does_not_mask_double_failure_recovery_error` | none | pytest.raises(IgnBdTopoDownloadError, match="rollback") | 2 | See [verified scenario and limits](#r15-test-cleanup-failure-does-not-mask-double-failure-recovery-error). |
| `test_stale_cache_recovery_backup_fails_closed_without_destroying_it` | none | pytest.raises(IgnBdTopoDownloadError, match="backup\|recovery\|manual") | 3 | See [verified scenario and limits](#r15-test-stale-cache-recovery-backup-fails-closed-without-destroying-it). |
| `test_official_checksum_mismatch_is_rejected` | none | pytest.raises(IgnBdTopoArchiveError, match="checksum\|SHA") | 2 | See [verified scenario and limits](#r15-test-official-checksum-mismatch-is-rejected). |
| `test_unsafe_parent_archive_member_is_rejected` | none | pytest.raises(IgnBdTopoArchiveError, match="unsafe\|member\|path") | 2 | See [verified scenario and limits](#r15-test-unsafe-parent-archive-member-is-rejected). |
| `test_geopackage_is_discovered_recursively` | none | none | 1 | See [verified scenario and limits](#r15-test-geopackage-is-discovered-recursively). |
| `test_multiple_geopackages_are_rejected_as_ambiguous` | none | pytest.raises(IgnBdTopoArchiveError, match="GeoPackage\|exactly one\|ambiguous") | 0 | See [verified scenario and limits](#r15-test-multiple-geopackages-are-rejected-as-ambiguous). |
| `test_real_layer_names_are_listed_and_discovered` | none | none | 4 | See [verified scenario and limits](#r15-test-real-layer-names-are-listed-and-discovered). |
| `test_missing_electric_line_layer_fails` | none | pytest.raises(IgnBdTopoLayerError, match="electric\|line\|Ligne") | 0 | See [verified scenario and limits](#r15-test-missing-electric-line-layer-fails). |
| `test_missing_transformation_post_layer_fails` | none | pytest.raises(IgnBdTopoLayerError, match="transformation\|post\|Poste") | 0 | See [verified scenario and limits](#r15-test-missing-transformation-post-layer-fails). |
| `test_ambiguous_electric_line_layers_fail` | none | pytest.raises(IgnBdTopoLayerError, match="unambiguous\|found 2") | 0 | See [verified scenario and limits](#r15-test-ambiguous-electric-line-layers-fail). |
| `test_synthetic_archive_extracts_and_discovers_required_layers` | none | none | 3 | See [verified scenario and limits](#r15-test-synthetic-archive-extracts-and-discovers-required-layers). |
| `test_schema_v3_extraction_metadata_binds_complete_physical_inventory` | none | none | 11 | See [verified scenario and limits](#r15-test-schema-v3-extraction-metadata-binds-complete-physical-inventory). |
| `test_extraction_rejects_forged_download_lineage_before_archive_open` | pytest.mark.parametrize(<br>    ("field", "value"),<br>    [<br>        ("provider", "UNTRUSTED"),<br>        ("product", "OTHER PRODUCT"),<br>        ("department_code", "32"),<br>        ("edition", "2025-01-01"),<br>        ("source_url", "https://example.test/other.7z"),<br>        ("filename", "other.7z"),<br>        ("official_checksum_validated", True),<br>    ],<br>) | pytest.raises(IgnBdTopoArchiveError, match="config\|envelope") | 0 | See [verified scenario and limits](#r15-test-extraction-rejects-forged-download-lineage-before-archive-open). |
| `test_same_size_geopackage_tamper_invalidates_extraction_cache` | none | none | 3 | See [verified scenario and limits](#r15-test-same-size-geopackage-tamper-invalidates-extraction-cache). |
| `test_forged_extraction_metadata_never_returns_cache_hit` | pytest.mark.parametrize(<br>    ("field", "value"),<br>    [<br>        ("geopackage_sha256", "0" * 64),<br>        ("geopackage_size_bytes", 1),<br>        ("schema_version", 1),<br>        ("schema_version", True),<br>        ("schema_version", 1.0),<br>        ("geopackage_relative_path", "../escape.gpkg"),<br>    ],<br>) | none | 1 | See [verified scenario and limits](#r15-test-forged-extraction-metadata-never-returns-cache-hit). |
| `test_linked_extraction_metadata_never_returns_cache_hit` | pytest.mark.parametrize("link_kind", ["symlink", "junction"]) | pytest.raises(IgnBdTopoArchiveError, match="marker\|non-linked") | 0 | See [verified scenario and limits](#r15-test-linked-extraction-metadata-never-returns-cache-hit). |
| `test_malformed_geopackage_sha_is_not_trusted` | pytest.mark.parametrize(<br>    "value",<br>    ["", "abc", "A" * 64, "a" * 63, "a" * 65],<br>) | none | 1 | See [verified scenario and limits](#r15-test-malformed-geopackage-sha-is-not-trusted). |
| `test_malformed_geopackage_size_is_not_trusted` | pytest.mark.parametrize("value", [0, -1, True, "100"]) | none | 1 | See [verified scenario and limits](#r15-test-malformed-geopackage-size-is-not-trusted). |
| `test_default_extraction_path_is_short_and_content_addressed` | none | none | 3 | See [verified scenario and limits](#r15-test-default-extraction-path-is-short-and-content-addressed). |
| `test_layer_loader_retains_crs_counts_and_null_geometries` | none | none | 8 | See [verified scenario and limits](#r15-test-layer-loader-retains-crs-counts-and-null-geometries). |
| `test_invalid_geometry_is_preserved_without_repair` | none | none | 5 | See [verified scenario and limits](#r15-test-invalid-geometry-is-preserved-without-repair). |
| `test_geographic_crs_is_rejected` | none | pytest.raises(IgnBdTopoLayerError, match="2154\|Lambert\|projected\|CRS") | 0 | See [verified scenario and limits](#r15-test-geographic-crs-is-rejected). |
| `test_electricity_loader_retains_both_layer_counts` | none | none | 5 | See [verified scenario and limits](#r15-test-electricity-loader-retains-both-layer-counts). |
| `test_road_layer_discovery_loads_selected_physical_layer` | none | none | 5 | See [verified scenario and limits](#r15-test-road-layer-discovery-loads-selected-physical-layer). |
| `test_road_physical_layer_cannot_collide_with_electricity_roles` | pytest.mark.parametrize(<br>    "role",<br>    ["electric_lines", "transformation_posts"],<br>) | pytest.raises(IgnBdTopoLayerError, match="same layer\|collid\|role") | 0 | See [verified scenario and limits](#r15-test-road-physical-layer-cannot-collide-with-electricity-roles). |
| `test_department_physical_layer_cannot_collide_with_road_role` | none | pytest.raises(IgnBdTopoLayerError, match="distinct\|role\|same layer") | 0 | See [verified scenario and limits](#r15-test-department-physical-layer-cannot-collide-with-road-role). |
| `test_department_physical_layer_cannot_collide_with_electricity_roles` | pytest.mark.parametrize(<br>    "role",<br>    ["electric_lines", "transformation_posts"],<br>) | pytest.raises(IgnBdTopoLayerError, match="distinct\|role\|same layer") | 0 | See [verified scenario and limits](#r15-test-department-physical-layer-cannot-collide-with-electricity-roles). |
| `test_electricity_physical_layers_must_be_distinct` | none | pytest.raises(IgnBdTopoLayerError, match="distinct\|role\|same layer") | 0 | See [verified scenario and limits](#r15-test-electricity-physical-layers-must-be-distinct). |
| `test_missing_road_layer_fails_safely` | none | pytest.raises(IgnBdTopoLayerError, match="road\|route\|found 0") | 0 | See [verified scenario and limits](#r15-test-missing-road-layer-fails-safely). |
| `test_ambiguous_road_layer_fails_safely` | none | pytest.raises(IgnBdTopoLayerError, match="road\|route\|found 2") | 0 | See [verified scenario and limits](#r15-test-ambiguous-road-layer-fails-safely). |
| `test_road_loader_rejects_wrong_archive_config_department` | none | pytest.raises(IgnBdTopoLayerError, match="department\|archive\|lineage") | 0 | See [verified scenario and limits](#r15-test-road-loader-rejects-wrong-archive-config-department). |
| `test_non_electric_layer_loaders_revalidate_mutated_role_config_before_read` | pytest.mark.parametrize("logical_role", ["road", "coverage"]) | pytest.raises(IgnBdTopoLayerError, match="config") | 0 | See [verified scenario and limits](#r15-test-non-electric-layer-loaders-revalidate-mutated-role-config-before-read). |
| `test_road_loader_rejects_changed_layer_inventory` | none | pytest.raises(IgnBdTopoLayerError, match="inventory\|changed") | 0 | See [verified scenario and limits](#r15-test-road-loader-rejects-changed-layer-inventory). |
| `test_road_loader_rejects_geographic_crs` | none | pytest.raises(IgnBdTopoLayerError, match="2154\|Lambert\|projected\|CRS") | 0 | See [verified scenario and limits](#r15-test-road-loader-rejects-geographic-crs). |
| `test_road_loader_preserves_lambert93_lines_unchanged` | pytest.mark.parametrize(<br>    ("road_geometry_kind", "expected_geometry_type"),<br>    [("line", "LineString"), ("multiline", "MultiLineString")],<br>) | none | 2 | See [verified scenario and limits](#r15-test-road-loader-preserves-lambert93-lines-unchanged). |
| `test_road_layer_does_not_change_electricity_loading_or_cache_shape` | none | none | 7 | See [verified scenario and limits](#r15-test-road-layer-does-not-change-electricity-loading-or-cache-shape). |
| `test_public_sources_export_only_stable_road_api` | none | none | 6 | See [verified scenario and limits](#r15-test-public-sources-export-only-stable-road-api). |
| `test_7z_windows_unsafe_member_names_fail_closed` | pytest.mark.parametrize(<br>    "unsafe_name",<br>    [<br>        "CON.txt",<br>        "folder/trailing.",<br>        "folder/edge ",<br>        "folder/bad?.txt",<br>        "folder/control\n.txt",<br>    ],<br>) | pytest.raises(IgnBdTopoArchiveError, match="Windows\|unsafe\|reserved") | 0 | See [verified scenario and limits](#r15-test-7z-windows-unsafe-member-names-fail-closed). |
| `test_7z_casefold_and_nfkc_destination_collisions_fail` | pytest.mark.parametrize(<br>    ("first", "second"),<br>    [<br>        ("Folder/value.txt", "folder/VALUE.txt"),<br>        ("café.txt", "cafe\u0301.txt"),<br>    ],<br>) | pytest.raises(IgnBdTopoArchiveError, match="collision") | 0 | See [verified scenario and limits](#r15-test-7z-casefold-and-nfkc-destination-collisions-fail). |
| `test_7z_nfkc_separator_destinations_fail_closed` | pytest.mark.parametrize(<br>    ("confusable", "ordinary"),<br>    [<br>        ("folder\uff0fchild.txt", "folder/child.txt"),<br>        ("folder\uff3cchild.txt", "folder/child.txt"),<br>    ],<br>) | pytest.raises(IgnBdTopoArchiveError, match="Windows\|unsafe\|collision") | 0 | See [verified scenario and limits](#r15-test-7z-nfkc-separator-destinations-fail-closed). |
| `test_7z_parent_file_conflict_fails_closed` | none | pytest.raises(IgnBdTopoArchiveError, match="parent-file") | 0 | See [verified scenario and limits](#r15-test-7z-parent-file-conflict-fails-closed). |
| `test_7z_encrypted_archive_fails_closed` | none | pytest.raises(IgnBdTopoArchiveError, match="encrypted") | 0 | See [verified scenario and limits](#r15-test-7z-encrypted-archive-fails-closed). |
| `test_extracted_inventory_mismatch_fails_closed` | none | pytest.raises(IgnBdTopoArchiveError, match="inventory") | 0 | See [verified scenario and limits](#r15-test-extracted-inventory-mismatch-fails-closed). |
| `test_stale_extraction_backup_blocks_before_7z_open` | none | pytest.raises(IgnBdTopoArchiveError, match="manual recovery") | 1 | See [verified scenario and limits](#r15-test-stale-extraction-backup-blocks-before-7z-open). |
| `test_extraction_publication_double_failure_preserves_backup` | none | pytest.raises(IgnBdTopoArchiveError, match="rollback") | 1 | See [verified scenario and limits](#r15-test-extraction-publication-double-failure-preserves-backup). |
| `test_extraction_part_link_is_rejected_without_touching_target` | pytest.mark.parametrize("link_kind", ["symlink", "junction"]) | pytest.raises(IgnBdTopoArchiveError, match="safe ordinary directory") | 4 | See [verified scenario and limits](#r15-test-extraction-part-link-is-rejected-without-touching-target). |
| `test_duplicate_ign_yaml_key_is_rejected` | none | pytest.raises(IgnBdTopoDownloadError) | 1 | See [verified scenario and limits](#r15-test-duplicate-ign-yaml-key-is-rejected). |
| `test_ign_cache_schema_version_is_a_strict_integer` | pytest.mark.parametrize("schema_version", [True, 1.0]) | pytest.raises((TypeError, ValidationError)) | 0 | See [verified scenario and limits](#r15-test-ign-cache-schema-version-is-a-strict-integer). |
| `test_ign_cache_file_size_is_a_strict_integer` | pytest.mark.parametrize("value", [True, 1.0, "1"]) | pytest.raises(ValidationError) | 0 | See [verified scenario and limits](#r15-test-ign-cache-file-size-is-a-strict-integer). |
| `test_ign_cache_json_is_strict_before_model_validation` | pytest.mark.parametrize(<br>    "invalid_json",<br>    [<br>        b'{"schema_version":1,"schema_version":1}',<br>        b'{"schema_version":NaN}',<br>        b"[]",<br>    ],<br>) | pytest.raises(ValueError) | 0 | See [verified scenario and limits](#r15-test-ign-cache-json-is-strict-before-model-validation). |
| `test_download_cache_reader_rejects_noncanonical_json_and_refreshes` | pytest.mark.parametrize(<br>    "invalid_json",<br>    [<br>        b'{"schema_version":1,"schema_version":1}',<br>        b'{"schema_version":NaN}',<br>        b"[]",<br>    ],<br>) | none | 2 | See [verified scenario and limits](#r15-test-download-cache-reader-rejects-noncanonical-json-and-refreshes). |
| `test_extraction_cache_reader_rejects_noncanonical_json_and_rebuilds` | pytest.mark.parametrize(<br>    "invalid_json",<br>    [<br>        b'{"schema_version":3,"schema_version":3}',<br>        b'{"schema_version":Infinity}',<br>        b"[]",<br>    ],<br>) | none | 1 | See [verified scenario and limits](#r15-test-extraction-cache-reader-rejects-noncanonical-json-and-rebuilds). |
| `test_department_coverage_loader_selects_configured_identity` | none | none | 13 | See [verified scenario and limits](#r15-test-department-coverage-loader-selects-configured-identity). |
| `test_department_coverage_requires_one_authoritative_feature` | pytest.mark.parametrize(<br>    "department_codes",<br>    [["32"], ["31", "31"]],<br>    ids=["missing", "duplicate"],<br>) | pytest.raises(IgnBdTopoLayerError, match="exactly one\|found") | 0 | See [verified scenario and limits](#r15-test-department-coverage-requires-one-authoritative-feature). |
| `test_department_coverage_requires_configured_identity_field` | none | pytest.raises(IgnBdTopoLayerError, match="identity field\|missing_code") | 0 | See [verified scenario and limits](#r15-test-department-coverage-requires-configured-identity-field). |
| `test_missing_department_coverage_layer_fails` | none | pytest.raises(IgnBdTopoLayerError, match="department\|found 0") | 0 | See [verified scenario and limits](#r15-test-missing-department-coverage-layer-fails). |
| `test_department_coverage_layer_discovery_must_be_unambiguous` | none | pytest.raises(IgnBdTopoLayerError, match="unambiguous\|found 2") | 0 | See [verified scenario and limits](#r15-test-department-coverage-layer-discovery-must-be-unambiguous). |
| `test_direct_consumers_reject_same_inventory_content_tampering` | pytest.mark.parametrize(<br>    ("consumer", "layer", "old_bytes", "new_bytes"),<br>    [<br>        ("electricity", LINE_LAYER, b"HT", b"HX"),<br>        ("roads", ROAD_LAYER, b"Bretelle", b"BretellX"),<br>        ("coverage", DEPARTMENT_LAYER, b"Department 31", b"Department 3X"),<br>    ],<br>) | pytest.raises(IgnBdTopoLayerError, match="integrity\|SHA\|physical\|changed") | 2 | See [verified scenario and limits](#r15-test-direct-consumers-reject-same-inventory-content-tampering). |
| `test_road_loader_rejects_source_change_after_physical_read` | none | pytest.raises(IgnBdTopoLayerError, match="changed\|integrity\|SHA") | 0 | See [verified scenario and limits](#r15-test-road-loader-rejects-source-change-after-physical-read). |

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
from dataclasses import replace
from datetime import UTC, datetime, timedelta
from hashlib import sha256
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
from urllib.error import HTTPError

import geopandas as gpd
import py7zr
import pyogrio
import pytest
import yaml
from geopandas.testing import assert_geodataframe_equal
from pydantic import ValidationError
from shapely.geometry import LineString, MultiLineString, MultiPolygon, Polygon

from landscout import sources
from landscout.sources import ign_bdtopo_fr
from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)
from landscout.sources.ign_bdtopo_fr import (
    _load_untrusted_ign_bdtopo_layer as load_untrusted_ign_bdtopo_layer,
)

PROJECT_ROOT = Path(__file__).parents[2]
CONFIG_PATH = PROJECT_ROOT / "configs/sources/ign_bdtopo_fr.yaml"
SYNTHETIC_SOURCE_URL = "https://example.test/BDTOPO_TEST_D031.7z"
LINE_LAYER = "LIGNE_ELECTRIQUE"
POST_LAYER = "POSTE_DE_TRANSFORMATION"
DEPARTMENT_LAYER = "DEPARTEMENT"
ROAD_LAYER = "TRONCON_DE_ROUTE"


def _config_data() -> dict:
    with CONFIG_PATH.open(encoding="utf-8") as stream:
        return yaml.safe_load(stream)


def _synthetic_config(
    source_config: IgnBdTopoSourceConfig,
    *,
    official_checksum: str | None = None,
) -> IgnBdTopoSourceConfig:
    content = source_config.model_dump(mode="json")
    content.update(
        {
            "source_url": SYNTHETIC_SOURCE_URL,
            "checksum_url": None,
            "official_checksum_algorithm": (
                "sha256" if official_checksum is not None else None
            ),
            "official_checksum": official_checksum,
            "expected_archive_size_bytes": None,
        }
    )
    return IgnBdTopoSourceConfig.model_validate(content)


def _write_gpkg(
    path: Path,
    *,
    include_lines: bool = True,
    include_posts: bool = True,
    line_layer: str = LINE_LAYER,
    post_layer: str = POST_LAYER,
    crs: str | None = "EPSG:2154",
    invalid_post: bool = False,
    include_department: bool = False,
    department_layer: str = DEPARTMENT_LAYER,
    department_codes: list[str] | None = None,
    department_geometries: list[object] | None = None,
    include_roads: bool = False,
    road_layer: str = ROAD_LAYER,
    road_crs: str | None = None,
    road_geometry_kind: str = "mixed",
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    layer_written = False
    if include_lines:
        lines = gpd.GeoDataFrame(
            {
                "object_id": ["L_VALID", "L_NULL"],
                "nature": ["HT", "UNKNOWN"],
                "tension": ["225 kV", None],
            },
            geometry=[LineString([(0, 0), (100, 100)]), None],
            crs=crs,
        )
        pyogrio.write_dataframe(
            lines,
            path,
            layer=line_layer,
            driver="GPKG",
        )
        layer_written = True
    if include_posts:
        invalid = Polygon([(0, 0), (20, 20), (20, 0), (0, 20), (0, 0)])
        geometries = [
            Polygon([(0, 0), (0, 20), (20, 20), (20, 0), (0, 0)]),
            None,
        ]
        object_ids = ["P_VALID", "P_NULL"]
        if invalid_post:
            geometries.append(invalid)
            object_ids.append("P_INVALID")
        posts = gpd.GeoDataFrame(
            {
                "object_id": object_ids,
                "nature": ["POSTE"] * len(object_ids),
            },
            geometry=geometries,
            crs=crs,
        )
        pyogrio.write_dataframe(
            posts,
            path,
            layer=post_layer,
            driver="GPKG",
            append=layer_written,
        )
        layer_written = True
    if include_roads:
        if road_geometry_kind == "line":
            road_geometries = [
                LineString([(0, 0), (100, 100)]),
                LineString([(200, 200), (300, 260)]),
            ]
        elif road_geometry_kind == "multiline":
            road_geometries = [
                MultiLineString([[(0, 0), (100, 100)]]),
                MultiLineString(
                    [
                        [(200, 200), (250, 250)],
                        [(250, 250), (300, 260)],
                    ]
                ),
            ]
        else:
            road_geometries = [
                LineString([(0, 0), (100, 100)]),
                MultiLineString(
                    [
                        [(200, 200), (250, 250)],
                        [(250, 250), (300, 260)],
                    ]
                ),
            ]
        roads = gpd.GeoDataFrame(
            {
                "object_id": ["R_LINE", "R_MULTI"],
                "nature": ["Route à 1 chaussée", "Bretelle"],
            },
            geometry=road_geometries,
            crs=road_crs or crs,
        )
        pyogrio.write_dataframe(
            roads,
            path,
            layer=road_layer,
            driver="GPKG",
            append=layer_written,
        )
        layer_written = True
    if include_department:
        codes = department_codes or ["31", "32"]
        geometries = (
            department_geometries
            or [
                MultiPolygon(
                    [Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)])]
                ),
                MultiPolygon(
                    [
                        Polygon(
                            [
                                (1000, 0),
                                (1000, 1000),
                                (2000, 1000),
                                (2000, 0),
                                (1000, 0),
                            ]
                        )
                    ]
                ),
            ][: len(codes)]
        )
        departments = gpd.GeoDataFrame(
            {
                "code_insee": codes,
                "nom_officiel": [f"Department {code}" for code in codes],
            },
            geometry=geometries,
            crs=crs,
        )
        pyogrio.write_dataframe(
            departments,
            path,
            layer=department_layer,
            driver="GPKG",
            append=layer_written,
        )


def _pack_7z(
    archive_path: Path,
    members: list[tuple[Path, str]],
) -> bytes:
    archive_path.parent.mkdir(parents=True, exist_ok=True)
    with py7zr.SevenZipFile(archive_path, "w") as archive:
        for source, archive_name in members:
            archive.write(source, arcname=archive_name)
    return archive_path.read_bytes()


def _synthetic_archive_bytes(
    root: Path,
    *,
    include_lines: bool = True,
    include_posts: bool = True,
    invalid_post: bool = False,
    include_department: bool = True,
    include_roads: bool = True,
    road_crs: str | None = None,
    road_geometry_kind: str = "mixed",
) -> bytes:
    gpkg_path = root / "fixture" / "BDTOPO_TEST.gpkg"
    _write_gpkg(
        gpkg_path,
        include_lines=include_lines,
        include_posts=include_posts,
        invalid_post=invalid_post,
        include_department=include_department,
        include_roads=include_roads,
        road_crs=road_crs,
        road_geometry_kind=road_geometry_kind,
    )
    return _pack_7z(
        root / "fixture.7z",
        [(gpkg_path, "BDTOPO_TEST/GPKG/BDTOPO_TEST.gpkg")],
    )


def _response(content: bytes) -> io.BytesIO:
    return io.BytesIO(content)


def _metadata_path(archive_path: Path) -> Path:
    return archive_path.parent / f"{archive_path.name}.metadata.json"


def _extraction_metadata_path(extraction_path: Path) -> Path:
    return extraction_path / ".landscout-extraction.json"


def _extracted_fixture(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    *,
    include_roads: bool = True,
) -> tuple[IgnBdTopoSourceConfig, IgnBdTopoDownload, IgnBdTopoExtraction]:
    archive_content = _synthetic_archive_bytes(
        tmp_path / "source",
        include_roads=include_roads,
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )
    return config, download, extraction


def _expire_cache(metadata_path: Path) -> bytes:
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["download_timestamp"] = (
        datetime.now(UTC) - timedelta(days=365)
    ).isoformat()
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
    return metadata_path.read_bytes()


@pytest.fixture
def source_config() -> IgnBdTopoSourceConfig:
    return load_ign_bdtopo_source_config(CONFIG_PATH)


def test_valid_source_config_loads(source_config: IgnBdTopoSourceConfig) -> None:
    assert "IGN" in source_config.provider
    assert source_config.department_code == "31"
    assert source_config.projection == "EPSG:2154"
    assert source_config.format == "GPKG"
    assert source_config.edition == "2026-06-15"
    assert source_config.access.road_segments.class_label == "Tronçon de route"
    assert source_config.access.road_segments.match_tokens == ("tronçon", "route")
    assert source_config.coverage.department_layer.match_tokens == ("departement",)
    assert source_config.coverage.department_layer.department_code_field == "code_insee"


def test_loaded_ign_source_config_and_nested_models_are_frozen(
    source_config: IgnBdTopoSourceConfig,
) -> None:
    with pytest.raises(ValidationError):
        source_config.department_code = "32"  # type: ignore[misc]
    with pytest.raises(ValidationError):
        source_config.access.road_segments.class_label = "other"  # type: ignore[misc]


def test_download_revalidates_a_tampered_config_before_network(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
) -> None:
    tampered = source_config.model_copy(deep=True)
    object.__setattr__(tampered, "provider", "UNTRUSTED")

    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            side_effect=AssertionError("invalid config must fail before network"),
        ) as opener,
        pytest.raises(IgnBdTopoDownloadError, match="config"),
    ):
        download_ign_bdtopo_archive(tampered, tmp_path)

    opener.assert_not_called()


@pytest.mark.parametrize("mutation", ["missing", "blank_field", "empty_tokens"])
def test_invalid_department_coverage_config_fails(mutation: str) -> None:
    content = _config_data()
    if mutation == "missing":
        del content["coverage"]
    elif mutation == "blank_field":
        content["coverage"]["department_layer"]["department_code_field"] = " "
    else:
        content["coverage"]["department_layer"]["match_tokens"] = []

    with pytest.raises(ValidationError):
        IgnBdTopoSourceConfig.model_validate(content)


@pytest.mark.parametrize("field", ["source_url", "edition"])
def test_missing_required_source_field_fails(field: str) -> None:
    content = _config_data()
    del content[field]

    with pytest.raises(ValidationError):
        IgnBdTopoSourceConfig.model_validate(content)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("department_code", "3"),
        ("department_code", "XX"),
        ("projection", "EPSG:4326"),
        ("format", "SHP"),
        ("archive_format", "zip"),
    ],
)
def test_invalid_source_configuration_fails(field: str, value: str) -> None:
    content = _config_data()
    content[field] = value

    with pytest.raises(ValidationError):
        IgnBdTopoSourceConfig.model_validate(content)


def test_unknown_source_config_field_is_rejected() -> None:
    content = _config_data()
    content["invented"] = "not allowed"

    with pytest.raises(ValidationError):
        IgnBdTopoSourceConfig.model_validate(content)


def test_successful_archive_download_persists_sha256(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path)
    config = _synthetic_config(source_config)

    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        result = download_ign_bdtopo_archive(config, tmp_path / "cache")

    assert result.cache_hit is False
    assert result.path.read_bytes() == archive_content
    assert result.file_size == len(archive_content)
    assert result.sha256 == sha256(archive_content).hexdigest()
    metadata = json.loads(_metadata_path(result.path).read_text(encoding="utf-8"))
    assert metadata["sha256"] == result.sha256
    assert metadata["source_url"] == SYNTHETIC_SOURCE_URL
    assert metadata["official_checksum"] is None


def test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_path = tmp_path / "fixture.7z"
    archive_content = _synthetic_archive_bytes(tmp_path / "source")
    archive_path.write_bytes(archive_content)

    integrity = validate_ign_bdtopo_archive(
        archive_path,
        _synthetic_config(source_config),
    )

    assert integrity.file_size == len(archive_content)
    assert integrity.sha256 == sha256(archive_content).hexdigest()
    assert integrity.official_checksum is None
    assert integrity.official_checksum_algorithm is None
    assert integrity.official_checksum_validated is False


def test_fresh_cache_is_reused_without_network(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    content = _synthetic_archive_bytes(tmp_path)
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(content),
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)

    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        side_effect=AssertionError("network must not be called"),
    ):
        second = download_ign_bdtopo_archive(config, cache_dir)

    assert second.cache_hit is True
    assert second.path == first.path
    assert second.sha256 == first.sha256
    assert second.download_timestamp == first.download_timestamp


def test_stale_recovery_backup_rejects_cache_before_network(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    content = _synthetic_archive_bytes(tmp_path)
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(content),
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
    recovery_path = first.path.with_name(f"{first.path.name}.bak")
    recovery_bytes = b"manual IGN recovery material"
    recovery_path.write_bytes(recovery_bytes)

    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            side_effect=AssertionError("stale recovery must fail before network"),
        ) as opener,
        pytest.raises(IgnBdTopoDownloadError, match="backup|recovery|manual"),
    ):
        download_ign_bdtopo_archive(config, cache_dir)

    opener.assert_not_called()
    assert recovery_path.read_bytes() == recovery_bytes
    assert first.path.read_bytes() == content


def test_expired_cache_is_refreshed(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    old_content = _synthetic_archive_bytes(tmp_path / "v1")
    new_content = _synthetic_archive_bytes(tmp_path / "v2", invalid_post=True)
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(old_content),
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
    _expire_cache(_metadata_path(first.path))

    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(new_content),
    ) as opener:
        refreshed = download_ign_bdtopo_archive(config, cache_dir)

    assert opener.call_count == 1
    assert refreshed.cache_hit is False
    assert refreshed.path.read_bytes() == new_content
    assert refreshed.sha256 != first.sha256
    assert not list(cache_dir.glob("*.part"))
    assert not list(cache_dir.glob("*.bak"))


def test_failed_refresh_preserves_valid_cache(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    content = _synthetic_archive_bytes(tmp_path)
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(content),
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
    metadata_path = _metadata_path(first.path)
    old_archive = first.path.read_bytes()
    expired_metadata = _expire_cache(metadata_path)
    error = HTTPError(SYNTHETIC_SOURCE_URL, 503, "Unavailable", None, None)

    with (
        patch("landscout.sources.ign_bdtopo_fr.open_safe_https", side_effect=error),
        pytest.raises(IgnBdTopoDownloadError),
    ):
        download_ign_bdtopo_archive(config, cache_dir)

    assert first.path.read_bytes() == old_archive
    assert metadata_path.read_bytes() == expired_metadata
    assert not list(cache_dir.glob("*.part"))
    assert not list(cache_dir.glob("*.bak"))


def test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(b"not a 7z archive"),
        ),
        pytest.raises(IgnBdTopoArchiveError),
    ):
        download_ign_bdtopo_archive(config, cache_dir)

    assert not list(cache_dir.glob("*.7z"))
    assert not list(cache_dir.glob("*.part"))
    assert not list(cache_dir.glob("*.bak"))


def test_corrupt_refresh_preserves_valid_cache(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    content = _synthetic_archive_bytes(tmp_path)
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(content),
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
    metadata_path = _metadata_path(first.path)
    old_archive = first.path.read_bytes()
    expired_metadata = _expire_cache(metadata_path)

    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(b"broken refresh"),
        ),
        pytest.raises(IgnBdTopoArchiveError),
    ):
        download_ign_bdtopo_archive(config, cache_dir)

    assert first.path.read_bytes() == old_archive
    assert metadata_path.read_bytes() == expired_metadata
    assert not list(cache_dir.glob("*.part"))


def test_metadata_publication_failure_restores_previous_cache_pair(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    old_content = _synthetic_archive_bytes(tmp_path / "v1")
    new_content = _synthetic_archive_bytes(tmp_path / "v2", invalid_post=True)
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(old_content),
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
    metadata_path = _metadata_path(first.path)
    old_archive = first.path.read_bytes()
    expired_metadata = _expire_cache(metadata_path)
    original_replace = ign_bdtopo_fr._replace_file
    failure_injected = False

    def fail_metadata_publication(source: Path, target: Path) -> None:
        nonlocal failure_injected
        if source.name.endswith(".metadata.json.part") and target == metadata_path:
            failure_injected = True
            raise PermissionError("simulated persistent metadata lock")
        original_replace(source, target)

    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(new_content),
        ),
        patch.object(
            ign_bdtopo_fr,
            "_replace_file",
            side_effect=fail_metadata_publication,
        ),
        pytest.raises(IgnBdTopoDownloadError),
    ):
        download_ign_bdtopo_archive(config, cache_dir)

    assert failure_injected
    assert first.path.read_bytes() == old_archive
    assert metadata_path.read_bytes() == expired_metadata
    assert not list(cache_dir.glob("*.part"))
    assert not list(cache_dir.glob("*.bak"))


def test_publication_and_rollback_failure_preserves_exact_recovery_backups(
    tmp_path: Path,
) -> None:
    archive_path = tmp_path / "cached.7z"
    metadata_path = tmp_path / "cached.7z.metadata.json"
    temporary_archive = tmp_path / "cached.7z.part"
    temporary_metadata = tmp_path / "cached.7z.metadata.json.part"
    old_archive = b"exact old archive"
    old_metadata = b"exact old metadata"
    archive_path.write_bytes(old_archive)
    metadata_path.write_bytes(old_metadata)
    temporary_archive.write_bytes(b"replacement archive")
    temporary_metadata.write_bytes(b"replacement metadata")
    archive_backup = archive_path.with_name(f"{archive_path.name}.bak")
    metadata_backup = metadata_path.with_name(f"{metadata_path.name}.bak")
    original_replace = ign_bdtopo_fr._replace_file

    def fail_publication_and_rollback(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        if source == archive_backup and target == archive_path:
            raise OSError("simulated archive rollback failure")
        original_replace(source, target)

    with (
        patch.object(
            ign_bdtopo_fr,
            "_replace_file",
            side_effect=fail_publication_and_rollback,
        ),
        pytest.raises(IgnBdTopoDownloadError, match="rollback"),
    ):
        ign_bdtopo_fr._publish_cache_pair(
            temporary_archive,
            temporary_metadata,
            archive_path,
            metadata_path,
        )

    assert archive_backup.read_bytes() == old_archive
    assert metadata_backup.read_bytes() == old_metadata


def test_cleanup_failure_does_not_mask_double_failure_recovery_error(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    old_content = _synthetic_archive_bytes(tmp_path / "v1")
    new_content = _synthetic_archive_bytes(tmp_path / "v2", invalid_post=True)
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(old_content),
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
    metadata_path = _metadata_path(first.path)
    old_archive = first.path.read_bytes()
    old_metadata = _expire_cache(metadata_path)
    temporary_metadata = metadata_path.with_name(f"{metadata_path.name}.part")
    archive_backup = first.path.with_name(f"{first.path.name}.bak")
    metadata_backup = metadata_path.with_name(f"{metadata_path.name}.bak")
    original_replace = ign_bdtopo_fr._replace_file
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

    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(new_content),
        ),
        patch.object(
            ign_bdtopo_fr,
            "_replace_file",
            side_effect=fail_publication_and_rollback,
        ),
        patch.object(Path, "unlink", new=fail_temporary_cleanup),
        pytest.raises(IgnBdTopoDownloadError, match="rollback"),
    ):
        download_ign_bdtopo_archive(config, cache_dir)

    assert archive_backup.read_bytes() == old_archive
    assert metadata_backup.read_bytes() == old_metadata


def test_stale_cache_recovery_backup_fails_closed_without_destroying_it(
    tmp_path: Path,
) -> None:
    archive_path = tmp_path / "cached.7z"
    metadata_path = tmp_path / "cached.7z.metadata.json"
    temporary_archive = tmp_path / "cached.7z.part"
    temporary_metadata = tmp_path / "cached.7z.metadata.json.part"
    archive_backup = tmp_path / "cached.7z.bak"
    archive_path.write_bytes(b"old archive")
    metadata_path.write_bytes(b"old metadata")
    temporary_archive.write_bytes(b"new archive")
    temporary_metadata.write_bytes(b"new metadata")
    archive_backup.write_bytes(b"manual recovery archive")

    with pytest.raises(IgnBdTopoDownloadError, match="backup|recovery|manual"):
        ign_bdtopo_fr._publish_cache_pair(
            temporary_archive,
            temporary_metadata,
            archive_path,
            metadata_path,
        )

    assert archive_path.read_bytes() == b"old archive"
    assert metadata_path.read_bytes() == b"old metadata"
    assert archive_backup.read_bytes() == b"manual recovery archive"


def test_official_checksum_mismatch_is_rejected(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path)
    config = _synthetic_config(source_config, official_checksum="0" * 64)
    cache_dir = tmp_path / "cache"

    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(archive_content),
        ),
        pytest.raises(IgnBdTopoArchiveError, match="checksum|SHA"),
    ):
        download_ign_bdtopo_archive(config, cache_dir)

    assert not list(cache_dir.glob("*.7z"))
    assert not list(cache_dir.glob("*.part"))


def test_unsafe_parent_archive_member_is_rejected(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    gpkg_path = tmp_path / "unsafe-source.gpkg"
    _write_gpkg(gpkg_path)
    archive_content = _pack_7z(
        tmp_path / "unsafe.7z",
        [(gpkg_path, "../escape.gpkg")],
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")

    with pytest.raises(IgnBdTopoArchiveError, match="unsafe|member|path"):
        extract_ign_bdtopo_archive(
            download,
            config,
            extraction_dir=tmp_path / "extracted",
        )

    assert not (tmp_path / "escape.gpkg").exists()
    assert not list(tmp_path.glob("*.part"))


def test_geopackage_is_discovered_recursively(tmp_path: Path) -> None:
    gpkg_path = tmp_path / "nested" / "data" / "bdtopo.gpkg"
    _write_gpkg(gpkg_path)

    assert discover_ign_bdtopo_geopackage(tmp_path) == gpkg_path


def test_multiple_geopackages_are_rejected_as_ambiguous(tmp_path: Path) -> None:
    _write_gpkg(tmp_path / "a" / "one.gpkg")
    _write_gpkg(tmp_path / "b" / "two.gpkg")

    with pytest.raises(IgnBdTopoArchiveError, match="GeoPackage|exactly one|ambiguous"):
        discover_ign_bdtopo_geopackage(tmp_path)


def test_real_layer_names_are_listed_and_discovered(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    gpkg_path = tmp_path / "bdtopo.gpkg"
    _write_gpkg(gpkg_path)

    all_layers = list_ign_bdtopo_layers(gpkg_path)
    selection = discover_ign_bdtopo_layers(gpkg_path, source_config)

    assert set(all_layers) == {LINE_LAYER, POST_LAYER}
    assert selection.electric_lines_layer == LINE_LAYER
    assert selection.transformation_posts_layer == POST_LAYER
    assert set(selection.all_layer_names) == {LINE_LAYER, POST_LAYER}


def test_missing_electric_line_layer_fails(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    gpkg_path = tmp_path / "posts-only.gpkg"
    _write_gpkg(gpkg_path, include_lines=False)

    with pytest.raises(IgnBdTopoLayerError, match="electric|line|Ligne"):
        discover_ign_bdtopo_layers(gpkg_path, source_config)


def test_missing_transformation_post_layer_fails(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    gpkg_path = tmp_path / "lines-only.gpkg"
    _write_gpkg(gpkg_path, include_posts=False)

    with pytest.raises(IgnBdTopoLayerError, match="transformation|post|Poste"):
        discover_ign_bdtopo_layers(gpkg_path, source_config)


def test_ambiguous_electric_line_layers_fail(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    gpkg_path = tmp_path / "ambiguous-lines.gpkg"
    _write_gpkg(gpkg_path)
    secondary_lines = gpd.GeoDataFrame(
        {"object_id": ["L_SECONDARY"]},
        geometry=[LineString([(0, 0), (50, 50)])],
        crs="EPSG:2154",
    )
    pyogrio.write_dataframe(
        secondary_lines,
        gpkg_path,
        layer="LIGNE_ELECTRIQUE_SECONDAIRE",
        driver="GPKG",
        append=True,
    )

    with pytest.raises(IgnBdTopoLayerError, match="unambiguous|found 2"):
        discover_ign_bdtopo_layers(gpkg_path, source_config)


def test_synthetic_archive_extracts_and_discovers_required_layers(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source")
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")

    extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )

    assert extraction.geopackage_path.is_file()
    assert extraction.electric_lines_layer == LINE_LAYER
    assert extraction.transformation_posts_layer == POST_LAYER


def test_schema_v3_extraction_metadata_binds_complete_physical_inventory(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    config, download, extraction = _extracted_fixture(tmp_path, source_config)
    metadata = json.loads(
        _extraction_metadata_path(extraction.extraction_path).read_text(
            encoding="utf-8"
        )
    )

    assert metadata["schema_version"] == 3
    assert (
        metadata["geopackage_size_bytes"] == extraction.geopackage_path.stat().st_size
    )
    assert (
        metadata["geopackage_sha256"]
        == sha256(extraction.geopackage_path.read_bytes()).hexdigest()
    )
    assert extraction.geopackage_size_bytes == metadata["geopackage_size_bytes"]
    assert extraction.geopackage_sha256 == metadata["geopackage_sha256"]
    assert metadata["road_segments_layer"] == ROAD_LAYER
    assert metadata["department_layer"] == DEPARTMENT_LAYER
    assert len(metadata["extracted_entries"]) >= 1

    cached = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=extraction.extraction_path,
    )
    assert cached.cache_hit is True
    assert cached.geopackage_size_bytes == metadata["geopackage_size_bytes"]
    assert cached.geopackage_sha256 == metadata["geopackage_sha256"]


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("provider", "UNTRUSTED"),
        ("product", "OTHER PRODUCT"),
        ("department_code", "32"),
        ("edition", "2025-01-01"),
        ("source_url", "https://example.test/other.7z"),
        ("filename", "other.7z"),
        ("official_checksum_validated", True),
    ],
)
def test_extraction_rejects_forged_download_lineage_before_archive_open(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    field: str,
    value: object,
) -> None:
    config, download, extraction = _extracted_fixture(tmp_path, source_config)
    forged = replace(download, **{field: value})

    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.py7zr.SevenZipFile",
            side_effect=AssertionError(
                "forged lineage must fail before archive access"
            ),
        ) as seven_zip,
        pytest.raises(IgnBdTopoArchiveError, match="config|envelope"),
    ):
        extract_ign_bdtopo_archive(
            forged,
            config,
            extraction_dir=extraction.extraction_path,
        )

    seven_zip.assert_not_called()


def test_same_size_geopackage_tamper_invalidates_extraction_cache(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    config, download, extraction = _extracted_fixture(tmp_path, source_config)
    original = extraction.geopackage_path.read_bytes()
    tampered = bytearray(original)
    tampered[-1] ^= 1
    extraction.geopackage_path.write_bytes(tampered)
    assert extraction.geopackage_path.stat().st_size == len(original)

    rebuilt = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=extraction.extraction_path,
    )

    assert rebuilt.cache_hit is False
    assert rebuilt.geopackage_path.read_bytes() == original


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("geopackage_sha256", "0" * 64),
        ("geopackage_size_bytes", 1),
        ("schema_version", 1),
        ("schema_version", True),
        ("schema_version", 1.0),
        ("geopackage_relative_path", "../escape.gpkg"),
    ],
)
def test_forged_extraction_metadata_never_returns_cache_hit(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    field: str,
    value: object,
) -> None:
    config, download, extraction = _extracted_fixture(tmp_path, source_config)
    metadata_path = _extraction_metadata_path(extraction.extraction_path)
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata[field] = value
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")

    rebuilt = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=extraction.extraction_path,
    )

    assert rebuilt.cache_hit is False


@pytest.mark.parametrize("link_kind", ["symlink", "junction"])
def test_linked_extraction_metadata_never_returns_cache_hit(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    monkeypatch: pytest.MonkeyPatch,
    link_kind: str,
) -> None:
    config, download, extraction = _extracted_fixture(tmp_path, source_config)
    metadata_path = _extraction_metadata_path(extraction.extraction_path)
    original_is_symlink = Path.is_symlink
    original_is_junction = Path.is_junction

    def simulated_is_symlink(path: Path) -> bool:
        return (link_kind == "symlink" and path == metadata_path) or (
            original_is_symlink(path)
        )

    def simulated_is_junction(path: Path) -> bool:
        return (link_kind == "junction" and path == metadata_path) or (
            original_is_junction(path)
        )

    monkeypatch.setattr(Path, "is_symlink", simulated_is_symlink)
    monkeypatch.setattr(Path, "is_junction", simulated_is_junction)

    with (
        patch.object(
            ign_bdtopo_fr.py7zr,
            "SevenZipFile",
            side_effect=AssertionError("linked marker reached archive extraction"),
        ) as seven_zip,
        pytest.raises(IgnBdTopoArchiveError, match="marker|non-linked"),
    ):
        extract_ign_bdtopo_archive(
            download,
            config,
            extraction_dir=extraction.extraction_path,
        )

    seven_zip.assert_not_called()


@pytest.mark.parametrize(
    "value",
    ["", "abc", "A" * 64, "a" * 63, "a" * 65],
)
def test_malformed_geopackage_sha_is_not_trusted(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    value: str,
) -> None:
    config, download, extraction = _extracted_fixture(tmp_path, source_config)
    metadata_path = _extraction_metadata_path(extraction.extraction_path)
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["geopackage_sha256"] = value
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")

    rebuilt = extract_ign_bdtopo_archive(
        download, config, extraction_dir=extraction.extraction_path
    )

    assert rebuilt.cache_hit is False


@pytest.mark.parametrize("value", [0, -1, True, "100"])
def test_malformed_geopackage_size_is_not_trusted(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    value: object,
) -> None:
    config, download, extraction = _extracted_fixture(tmp_path, source_config)
    metadata_path = _extraction_metadata_path(extraction.extraction_path)
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["geopackage_size_bytes"] = value
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")

    rebuilt = extract_ign_bdtopo_archive(
        download, config, extraction_dir=extraction.extraction_path
    )

    assert rebuilt.cache_hit is False


def test_default_extraction_path_is_short_and_content_addressed(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source")
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, cache_dir)

    extraction = extract_ign_bdtopo_archive(download, config)

    assert extraction.extraction_path == cache_dir / "x" / download.sha256[:16]
    assert len(extraction.extraction_path.name) == 16
    assert extraction.geopackage_path.is_file()


def test_layer_loader_retains_crs_counts_and_null_geometries(tmp_path: Path) -> None:
    gpkg_path = tmp_path / "bdtopo.gpkg"
    _write_gpkg(gpkg_path)

    loaded = load_untrusted_ign_bdtopo_layer(
        gpkg_path,
        LINE_LAYER,
        "electric_lines",
    )
    frame = loaded.data
    summary = loaded.summary

    assert frame.crs is not None
    assert frame.crs.to_epsg() == 2154
    assert len(frame) == 2
    assert frame["object_id"].tolist() == ["L_VALID", "L_NULL"]
    assert frame.geometry.isna().sum() == 1
    assert summary.feature_count == 2
    assert summary.null_geometry_count == 1
    assert summary.invalid_geometry_count == 0


def test_invalid_geometry_is_preserved_without_repair(tmp_path: Path) -> None:
    gpkg_path = tmp_path / "bdtopo.gpkg"
    _write_gpkg(gpkg_path, invalid_post=True)

    loaded = load_untrusted_ign_bdtopo_layer(
        gpkg_path,
        POST_LAYER,
        "transformation_posts",
    )
    frame = loaded.data
    summary = loaded.summary

    invalid_row = frame.loc[frame["object_id"] == "P_INVALID"].iloc[0]
    assert len(frame) == 3
    assert invalid_row.geometry.is_valid is False
    assert summary.feature_count == 3
    assert summary.null_geometry_count == 1
    assert summary.invalid_geometry_count == 1


def test_geographic_crs_is_rejected(tmp_path: Path) -> None:
    gpkg_path = tmp_path / "geographic.gpkg"
    _write_gpkg(gpkg_path, include_posts=False, crs="EPSG:4326")

    with pytest.raises(IgnBdTopoLayerError, match="2154|Lambert|projected|CRS"):
        load_untrusted_ign_bdtopo_layer(gpkg_path, LINE_LAYER, "electric_lines")


def test_electricity_loader_retains_both_layer_counts(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source", invalid_post=True)
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )

    electricity = load_ign_bdtopo_electricity(extraction, config)

    assert len(electricity.electric_lines) == 2
    assert len(electricity.transformation_posts) == 3
    assert electricity.electric_lines.crs.to_epsg() == 2154
    assert electricity.transformation_posts.crs.to_epsg() == 2154
    assert electricity.transformation_posts_summary.invalid_geometry_count == 1


def test_road_layer_discovery_loads_selected_physical_layer(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source", include_roads=True)
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )

    loaded = ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)

    assert loaded.extraction is extraction
    assert loaded.road_segments_summary.source_layer_name == ROAD_LAYER
    assert loaded.road_segments_summary.logical_name == "road_segments"
    assert loaded.road_segments["object_id"].tolist() == ["R_LINE", "R_MULTI"]
    assert loaded.road_segments_summary.spatial_role == "PROXY_GEOMETRY"


@pytest.mark.parametrize(
    "role",
    ["electric_lines", "transformation_posts"],
)
def test_road_physical_layer_cannot_collide_with_electricity_roles(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    role: str,
) -> None:
    config, _, extraction = _extracted_fixture(
        tmp_path,
        source_config,
        include_roads=True,
    )
    content = config.model_dump(mode="json")
    selected = content["logical_layers"][role]
    content["access"]["road_segments"] = selected
    colliding = IgnBdTopoSourceConfig.model_validate(content)

    with pytest.raises(IgnBdTopoLayerError, match="same layer|collid|role"):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, colliding)


def test_department_physical_layer_cannot_collide_with_road_role(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
) -> None:
    config, _, extraction = _extracted_fixture(
        tmp_path,
        source_config,
        include_roads=True,
    )
    content = config.model_dump(mode="json")
    content["coverage"]["department_layer"]["match_tokens"] = content["access"][
        "road_segments"
    ]["match_tokens"]
    colliding = IgnBdTopoSourceConfig.model_validate(content)

    with pytest.raises(IgnBdTopoLayerError, match="distinct|role|same layer"):
        load_ign_bdtopo_department_coverage(extraction, colliding)


@pytest.mark.parametrize(
    "role",
    ["electric_lines", "transformation_posts"],
)
def test_department_physical_layer_cannot_collide_with_electricity_roles(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    role: str,
) -> None:
    config, _, extraction = _extracted_fixture(
        tmp_path,
        source_config,
        include_roads=True,
    )
    content = config.model_dump(mode="json")
    content["coverage"]["department_layer"]["match_tokens"] = content["logical_layers"][
        role
    ]["match_tokens"]
    colliding = IgnBdTopoSourceConfig.model_validate(content)

    with pytest.raises(IgnBdTopoLayerError, match="distinct|role|same layer"):
        load_ign_bdtopo_department_coverage(extraction, colliding)


def test_electricity_physical_layers_must_be_distinct(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
) -> None:
    config, _, extraction = _extracted_fixture(
        tmp_path,
        source_config,
        include_roads=True,
    )
    content = config.model_dump(mode="json")
    content["logical_layers"]["transformation_posts"]["match_tokens"] = ["ligne"]
    colliding = IgnBdTopoSourceConfig.model_validate(content)

    with pytest.raises(IgnBdTopoLayerError, match="distinct|role|same layer"):
        load_ign_bdtopo_electricity(extraction, colliding)


def test_missing_road_layer_fails_safely(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(
        tmp_path / "source",
        include_roads=False,
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    with pytest.raises(IgnBdTopoLayerError, match="road|route|found 0"):
        extract_ign_bdtopo_archive(
            download,
            config,
            extraction_dir=tmp_path / "extracted",
        )


def test_ambiguous_road_layer_fails_safely(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    gpkg_path = tmp_path / "source" / "ambiguous-roads.gpkg"
    _write_gpkg(gpkg_path, include_roads=True)
    secondary = gpd.GeoDataFrame(
        {"object_id": ["R_SECONDARY"]},
        geometry=[LineString([(0, 0), (10, 10)])],
        crs="EPSG:2154",
    )
    pyogrio.write_dataframe(
        secondary,
        gpkg_path,
        layer="TRONCON_DE_ROUTE_SECONDAIRE",
        driver="GPKG",
        append=True,
    )
    archive_content = _pack_7z(
        tmp_path / "ambiguous-roads.7z",
        [(gpkg_path, "PACKAGE/ambiguous-roads.gpkg")],
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    with pytest.raises(IgnBdTopoLayerError, match="road|route|found 2"):
        extract_ign_bdtopo_archive(
            download,
            config,
            extraction_dir=tmp_path / "extracted",
        )


def test_road_loader_rejects_wrong_archive_config_department(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source", include_roads=True)
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )
    other_department = IgnBdTopoSourceConfig.model_validate(
        {**config.model_dump(mode="json"), "department_code": "32"}
    )

    with pytest.raises(IgnBdTopoLayerError, match="department|archive|lineage"):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, other_department)


@pytest.mark.parametrize("logical_role", ["road", "coverage"])
def test_non_electric_layer_loaders_revalidate_mutated_role_config_before_read(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    logical_role: str,
) -> None:
    config, _, extraction = _extracted_fixture(tmp_path, source_config)
    tampered = config.model_copy(deep=True)
    if logical_role == "road":
        object.__setattr__(tampered.access.road_segments, "match_tokens", ())
    else:
        object.__setattr__(
            tampered.coverage.department_layer,
            "department_code_field",
            " ",
        )

    with (
        patch.object(
            ign_bdtopo_fr.gpd,
            "read_file",
            side_effect=AssertionError("invalid config reached physical layer read"),
        ) as reader,
        pytest.raises(IgnBdTopoLayerError, match="config"),
    ):
        if logical_role == "road":
            ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, tampered)
        else:
            load_ign_bdtopo_department_coverage(extraction, tampered)

    reader.assert_not_called()


def test_road_loader_rejects_changed_layer_inventory(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source", include_roads=True)
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )
    added = gpd.GeoDataFrame(
        {"object_id": ["ADDED"]},
        geometry=[LineString([(0, 0), (1, 1)])],
        crs="EPSG:2154",
    )
    pyogrio.write_dataframe(
        added,
        extraction.geopackage_path,
        layer="ADDED_AFTER_EXTRACTION",
        driver="GPKG",
        append=True,
    )

    with pytest.raises(IgnBdTopoLayerError, match="inventory|changed"):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)


def test_road_loader_rejects_geographic_crs(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(
        tmp_path / "source", include_roads=True, road_crs="EPSG:4326"
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )

    with pytest.raises(IgnBdTopoLayerError, match="2154|Lambert|projected|CRS"):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)


@pytest.mark.parametrize(
    ("road_geometry_kind", "expected_geometry_type"),
    [("line", "LineString"), ("multiline", "MultiLineString")],
)
def test_road_loader_preserves_lambert93_lines_unchanged(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    road_geometry_kind: str,
    expected_geometry_type: str,
) -> None:
    archive_content = _synthetic_archive_bytes(
        tmp_path / "source",
        include_roads=True,
        road_geometry_kind=road_geometry_kind,
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )
    expected = gpd.read_file(
        extraction.geopackage_path, layer=ROAD_LAYER, engine="pyogrio"
    )

    loaded = ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)

    assert_geodataframe_equal(loaded.road_segments, expected, check_crs=True)
    assert loaded.road_segments.crs.to_epsg() == 2154
    assert loaded.road_segments_summary.geometry_types == (expected_geometry_type,)


def test_road_layer_does_not_change_electricity_loading_or_cache_shape(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source", include_roads=True)
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )

    electricity = load_ign_bdtopo_electricity(extraction, config)
    metadata = json.loads(
        (extraction.extraction_path / ".landscout-extraction.json").read_text(
            encoding="utf-8"
        )
    )

    assert len(electricity.electric_lines) == 2
    assert len(electricity.transformation_posts) == 2
    assert electricity.electric_lines_summary.source_layer_name == LINE_LAYER
    assert electricity.transformation_posts_summary.source_layer_name == POST_LAYER
    assert metadata["road_segments_layer"] == ROAD_LAYER
    assert metadata["department_layer"] == DEPARTMENT_LAYER
    assert set(metadata) == {
        "schema_version",
        "archive_sha256",
        "geopackage_relative_path",
        "geopackage_size_bytes",
        "geopackage_sha256",
        "all_layer_names",
        "electric_lines_layer",
        "transformation_posts_layer",
        "road_segments_layer",
        "department_layer",
        "extracted_entries",
        "spatial_role",
    }


def test_public_sources_export_only_stable_road_api() -> None:
    assert sources.IgnBdTopoRoadData is ign_bdtopo_fr.IgnBdTopoRoadData
    assert sources.load_ign_bdtopo_roads is ign_bdtopo_fr.load_ign_bdtopo_roads
    assert "IgnBdTopoRoadData" in sources.__all__
    assert "load_ign_bdtopo_roads" in sources.__all__
    assert not hasattr(sources, "_discover_road_layer")
    assert not hasattr(sources, "load_ign_bdtopo_layer")


def _archive_info(
    name: str,
    *,
    directory: bool = False,
    size: int = 1,
) -> SimpleNamespace:
    return SimpleNamespace(
        filename=name,
        is_file=not directory,
        is_directory=directory,
        is_symlink=False,
        encrypted=False,
        uncompressed=None if directory else size,
    )


class _FakeArchive:
    def __init__(self, infos: list[SimpleNamespace], *, encrypted: bool = False):
        self._infos = infos
        self._encrypted = encrypted

    def needs_password(self) -> bool:
        return self._encrypted

    def list(self) -> list[SimpleNamespace]:
        return self._infos


@pytest.mark.parametrize(
    "unsafe_name",
    [
        "CON.txt",
        "folder/trailing.",
        "folder/edge ",
        "folder/bad?.txt",
        "folder/control\n.txt",
    ],
)
def test_7z_windows_unsafe_member_names_fail_closed(unsafe_name: str) -> None:
    archive = _FakeArchive([_archive_info("data.gpkg"), _archive_info(unsafe_name)])

    with pytest.raises(IgnBdTopoArchiveError, match="Windows|unsafe|reserved"):
        ign_bdtopo_fr._validate_archive_members(archive)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    ("first", "second"),
    [
        ("Folder/value.txt", "folder/VALUE.txt"),
        ("café.txt", "cafe\u0301.txt"),
    ],
)
def test_7z_casefold_and_nfkc_destination_collisions_fail(
    first: str,
    second: str,
) -> None:
    archive = _FakeArchive(
        [
            _archive_info("data.gpkg"),
            _archive_info(first),
            _archive_info(second),
        ]
    )

    with pytest.raises(IgnBdTopoArchiveError, match="collision"):
        ign_bdtopo_fr._validate_archive_members(archive)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    ("confusable", "ordinary"),
    [
        ("folder\uff0fchild.txt", "folder/child.txt"),
        ("folder\uff3cchild.txt", "folder/child.txt"),
    ],
)
def test_7z_nfkc_separator_destinations_fail_closed(
    confusable: str,
    ordinary: str,
) -> None:
    archive = _FakeArchive(
        [
            _archive_info("data.gpkg"),
            _archive_info(confusable),
            _archive_info(ordinary),
        ]
    )

    with pytest.raises(IgnBdTopoArchiveError, match="Windows|unsafe|collision"):
        ign_bdtopo_fr._validate_archive_members(archive)  # type: ignore[arg-type]


def test_7z_parent_file_conflict_fails_closed() -> None:
    archive = _FakeArchive(
        [
            _archive_info("data.gpkg"),
            _archive_info("parent"),
            _archive_info("parent/child.txt"),
        ]
    )

    with pytest.raises(IgnBdTopoArchiveError, match="parent-file"):
        ign_bdtopo_fr._validate_archive_members(archive)  # type: ignore[arg-type]


def test_7z_encrypted_archive_fails_closed() -> None:
    archive = _FakeArchive([_archive_info("data.gpkg")], encrypted=True)

    with pytest.raises(IgnBdTopoArchiveError, match="encrypted"):
        ign_bdtopo_fr._validate_archive_members(archive)  # type: ignore[arg-type]


def test_extracted_inventory_mismatch_fails_closed(tmp_path: Path) -> None:
    expected = (ign_bdtopo_fr._ValidatedArchiveMember("data.gpkg", "file", 4),)
    (tmp_path / "data.gpkg").write_bytes(b"bad")

    with pytest.raises(IgnBdTopoArchiveError, match="inventory"):
        ign_bdtopo_fr._validate_extracted_inventory(tmp_path, expected)


def test_stale_extraction_backup_blocks_before_7z_open(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
) -> None:
    config, download, extraction = _extracted_fixture(tmp_path, source_config)
    backup = extraction.extraction_path.with_name(
        f"{extraction.extraction_path.name}.bak"
    )
    backup.mkdir()
    sentinel = backup / "manual-recovery.txt"
    sentinel.write_bytes(b"preserve")

    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.py7zr.SevenZipFile",
            side_effect=AssertionError("7z must not open with recovery material"),
        ) as seven_zip,
        pytest.raises(IgnBdTopoArchiveError, match="manual recovery"),
    ):
        extract_ign_bdtopo_archive(
            download,
            config,
            extraction_dir=extraction.extraction_path,
        )

    seven_zip.assert_not_called()
    assert sentinel.read_bytes() == b"preserve"


def test_extraction_publication_double_failure_preserves_backup(
    tmp_path: Path,
) -> None:
    target = tmp_path / "extracted"
    temporary = tmp_path / "extracted.part"
    target.mkdir()
    temporary.mkdir()
    (target / "old.txt").write_bytes(b"old")
    (temporary / "new.txt").write_bytes(b"new")
    backup = tmp_path / "extracted.bak"
    original_replace = ign_bdtopo_fr._replace_directory

    def fail_publication_and_rollback(source: Path, destination: Path) -> None:
        if source == temporary or source == backup:
            raise OSError("simulated transaction failure")
        original_replace(source, destination)

    with (
        patch.object(
            ign_bdtopo_fr,
            "_replace_directory",
            side_effect=fail_publication_and_rollback,
        ),
        pytest.raises(IgnBdTopoArchiveError, match="rollback"),
    ):
        ign_bdtopo_fr._publish_extraction_directory(temporary, target)

    assert (backup / "old.txt").read_bytes() == b"old"


@pytest.mark.parametrize("link_kind", ["symlink", "junction"])
def test_extraction_part_link_is_rejected_without_touching_target(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    monkeypatch: pytest.MonkeyPatch,
    link_kind: str,
) -> None:
    config, download, _ = _extracted_fixture(tmp_path, source_config)
    extraction_path = tmp_path / "linked-extraction"
    temporary = extraction_path.with_name(f"{extraction_path.name}.part")
    sentinel = tmp_path / "sentinel.txt"
    sentinel.write_bytes(b"preserve")
    integrity = validate_ign_bdtopo_archive(download.path, config)
    original_is_symlink = Path.is_symlink
    original_is_junction = Path.is_junction
    original_unlink = Path.unlink
    original_rmdir = Path.rmdir
    original_rmtree = ign_bdtopo_fr.shutil.rmtree
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
    monkeypatch.setattr(ign_bdtopo_fr.shutil, "rmtree", protected_rmtree)

    with (
        patch.object(
            ign_bdtopo_fr,
            "validate_ign_bdtopo_archive",
            return_value=integrity,
        ) as archive_validation,
        patch.object(
            ign_bdtopo_fr.py7zr,
            "SevenZipFile",
            side_effect=AssertionError("temporary link reached archive extraction"),
        ) as seven_zip,
        pytest.raises(IgnBdTopoArchiveError, match="safe ordinary directory"),
    ):
        extract_ign_bdtopo_archive(
            download,
            config,
            extraction_dir=extraction_path,
        )

    archive_validation.assert_called_once_with(download.path, config)
    seven_zip.assert_not_called()
    assert unlink_calls == 0
    assert rmdir_calls == 0
    assert rmtree_calls == 0
    assert sentinel.read_bytes() == b"preserve"


def test_duplicate_ign_yaml_key_is_rejected(tmp_path: Path) -> None:
    config_path = tmp_path / "ign.yaml"
    config_path.write_text(
        "provider: IGN\nprovider: UNTRUSTED\n",
        encoding="utf-8",
    )

    with pytest.raises(IgnBdTopoDownloadError) as captured:
        load_ign_bdtopo_source_config(config_path)

    assert "duplicate" in str(captured.value.__cause__).casefold()


@pytest.mark.parametrize("schema_version", [True, 1.0])
def test_ign_cache_schema_version_is_a_strict_integer(
    schema_version: object,
) -> None:
    payload = {
        "schema_version": schema_version,
        "provider": "IGN",
        "product": "BD TOPO",
        "department_code": "31",
        "edition": "2026-06-15",
        "product_version": "3.5",
        "projection": "EPSG:2154",
        "package_format": "GPKG",
        "archive_format": "7z",
        "source_url": SYNTHETIC_SOURCE_URL,
        "checksum_url": None,
        "download_timestamp": "2026-08-11T15:32:03+00:00",
        "filename": "BDTOPO_TEST_D031.7z",
        "file_size": 1,
        "sha256": "a" * 64,
        "official_checksum_algorithm": None,
        "official_checksum": None,
        "official_checksum_validated": False,
        "spatial_role": "PROXY_GEOMETRY",
    }

    with pytest.raises((TypeError, ValidationError)):
        ign_bdtopo_fr._CacheMetadata.model_validate(payload)


@pytest.mark.parametrize("value", [True, 1.0, "1"])
def test_ign_cache_file_size_is_a_strict_integer(value: object) -> None:
    payload = {
        "schema_version": 1,
        "provider": "IGN",
        "product": "BD TOPO",
        "department_code": "31",
        "edition": "2026-06-15",
        "product_version": "3.5",
        "projection": "EPSG:2154",
        "package_format": "GPKG",
        "archive_format": "7z",
        "source_url": SYNTHETIC_SOURCE_URL,
        "checksum_url": None,
        "download_timestamp": "2026-08-11T15:32:03+00:00",
        "filename": "BDTOPO_TEST_D031.7z",
        "file_size": value,
        "sha256": "a" * 64,
        "official_checksum_algorithm": None,
        "official_checksum": None,
        "official_checksum_validated": False,
        "spatial_role": "PROXY_GEOMETRY",
    }

    with pytest.raises(ValidationError):
        ign_bdtopo_fr._CacheMetadata.model_validate(payload)


@pytest.mark.parametrize(
    "invalid_json",
    [
        b'{"schema_version":1,"schema_version":1}',
        b'{"schema_version":NaN}',
        b"[]",
    ],
)
def test_ign_cache_json_is_strict_before_model_validation(
    invalid_json: bytes,
) -> None:
    with pytest.raises(ValueError):
        ign_bdtopo_fr.loads_strict_json_object(invalid_json)


@pytest.mark.parametrize(
    "invalid_json",
    [
        b'{"schema_version":1,"schema_version":1}',
        b'{"schema_version":NaN}',
        b"[]",
    ],
)
def test_download_cache_reader_rejects_noncanonical_json_and_refreshes(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    invalid_json: bytes,
) -> None:
    content = _synthetic_archive_bytes(tmp_path / "source")
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(content),
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
    _metadata_path(first.path).write_bytes(invalid_json)

    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(content),
    ) as opener:
        refreshed = download_ign_bdtopo_archive(config, cache_dir)

    assert opener.call_count == 1
    assert refreshed.cache_hit is False


@pytest.mark.parametrize(
    "invalid_json",
    [
        b'{"schema_version":3,"schema_version":3}',
        b'{"schema_version":Infinity}',
        b"[]",
    ],
)
def test_extraction_cache_reader_rejects_noncanonical_json_and_rebuilds(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    invalid_json: bytes,
) -> None:
    config, download, extraction = _extracted_fixture(tmp_path, source_config)
    _extraction_metadata_path(extraction.extraction_path).write_bytes(invalid_json)

    rebuilt = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=extraction.extraction_path,
    )

    assert rebuilt.cache_hit is False


def test_department_coverage_loader_selects_configured_identity(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(
        tmp_path / "source",
        include_department=True,
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )

    loaded = load_ign_bdtopo_department_coverage(extraction, config)

    assert loaded.source_layer == DEPARTMENT_LAYER
    assert loaded.source_department_code == "31"
    assert loaded.spatial_role == "SOURCE_COVERAGE_BOUNDARY"
    assert len(loaded.coverage) == 1
    assert loaded.coverage.loc[0, "code_insee"] == "31"
    assert loaded.coverage.loc[0, "source_department_code"] == "31"
    assert loaded.coverage.loc[0, "source_archive_sha256"] == download.sha256
    assert loaded.coverage.loc[0, "spatial_role"] == "SOURCE_COVERAGE_BOUNDARY"
    assert loaded.coverage.crs.to_epsg() == 2154
    assert loaded.summary.source_feature_count == 2
    assert loaded.summary.selected_feature_count == 1
    assert loaded.summary.department_code_field == "code_insee"
    assert loaded.summary.geometry_types == ("MultiPolygon",)


@pytest.mark.parametrize(
    "department_codes",
    [["32"], ["31", "31"]],
    ids=["missing", "duplicate"],
)
def test_department_coverage_requires_one_authoritative_feature(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    department_codes: list[str],
) -> None:
    gpkg_path = tmp_path / "source" / "coverage.gpkg"
    geometries = [
        Polygon([(0, 0), (0, 100), (100, 100), (100, 0), (0, 0)])
        for _ in department_codes
    ]
    _write_gpkg(
        gpkg_path,
        include_department=True,
        include_roads=True,
        department_codes=department_codes,
        department_geometries=geometries,
    )
    archive_content = _pack_7z(
        tmp_path / "coverage.7z",
        [(gpkg_path, "PACKAGE/coverage.gpkg")],
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )

    with pytest.raises(IgnBdTopoLayerError, match="exactly one|found"):
        load_ign_bdtopo_department_coverage(extraction, config)


def test_department_coverage_requires_configured_identity_field(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(
        tmp_path / "source",
        include_department=True,
    )
    content = _synthetic_config(source_config).model_dump(mode="json")
    content["coverage"]["department_layer"]["department_code_field"] = "missing_code"
    config = IgnBdTopoSourceConfig.model_validate(content)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )

    with pytest.raises(IgnBdTopoLayerError, match="identity field|missing_code"):
        load_ign_bdtopo_department_coverage(extraction, config)


def test_missing_department_coverage_layer_fails(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(
        tmp_path / "source",
        include_department=False,
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    with pytest.raises(IgnBdTopoLayerError, match="department|found 0"):
        extract_ign_bdtopo_archive(
            download,
            config,
            extraction_dir=tmp_path / "extracted",
        )


def test_department_coverage_layer_discovery_must_be_unambiguous(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    gpkg_path = tmp_path / "source" / "ambiguous.gpkg"
    _write_gpkg(gpkg_path, include_department=True, include_roads=True)
    second = gpd.GeoDataFrame(
        {"code_insee": ["31"]},
        geometry=[Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])],
        crs="EPSG:2154",
    )
    pyogrio.write_dataframe(
        second,
        gpkg_path,
        layer="DEPARTEMENT_SECONDAIRE",
        driver="GPKG",
        append=True,
    )
    archive_content = _pack_7z(
        tmp_path / "ambiguous.7z",
        [(gpkg_path, "PACKAGE/ambiguous.gpkg")],
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    with pytest.raises(IgnBdTopoLayerError, match="unambiguous|found 2"):
        extract_ign_bdtopo_archive(
            download,
            config,
            extraction_dir=tmp_path / "extracted",
        )


@pytest.mark.parametrize(
    ("consumer", "layer", "old_bytes", "new_bytes"),
    [
        ("electricity", LINE_LAYER, b"HT", b"HX"),
        ("roads", ROAD_LAYER, b"Bretelle", b"BretellX"),
        ("coverage", DEPARTMENT_LAYER, b"Department 31", b"Department 3X"),
    ],
)
def test_direct_consumers_reject_same_inventory_content_tampering(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    consumer: str,
    layer: str,
    old_bytes: bytes,
    new_bytes: bytes,
) -> None:
    config, _, extraction = _extracted_fixture(
        tmp_path,
        source_config,
        include_roads=True,
    )
    if consumer == "coverage":
        # Rebuild once with the configured department layer present.
        archive_content = _synthetic_archive_bytes(
            tmp_path / "coverage-source",
            include_roads=True,
            include_department=True,
        )
        with patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(archive_content),
        ):
            download = download_ign_bdtopo_archive(config, tmp_path / "coverage-cache")
        extraction = extract_ign_bdtopo_archive(
            download,
            config,
            extraction_dir=tmp_path / "coverage-extracted",
        )

    size_before = extraction.geopackage_path.stat().st_size
    content = extraction.geopackage_path.read_bytes()
    assert old_bytes in content
    extraction.geopackage_path.write_bytes(content.replace(old_bytes, new_bytes, 1))
    assert extraction.geopackage_path.stat().st_size == size_before

    with pytest.raises(IgnBdTopoLayerError, match="integrity|SHA|physical|changed"):
        if consumer == "electricity":
            load_ign_bdtopo_electricity(extraction, config)
        elif consumer == "roads":
            ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)
        else:
            load_ign_bdtopo_department_coverage(extraction, config)


def test_road_loader_rejects_source_change_after_physical_read(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
) -> None:
    config, _, extraction = _extracted_fixture(
        tmp_path,
        source_config,
        include_roads=True,
    )
    original_read = ign_bdtopo_fr.gpd.read_file

    def mutate_after_read(*args: object, **kwargs: object) -> gpd.GeoDataFrame:
        frame = original_read(*args, **kwargs)
        content = extraction.geopackage_path.read_bytes()
        extraction.geopackage_path.write_bytes(
            content.replace(b"Bretelle", b"BretellX", 1)
        )
        return frame

    with (
        patch.object(ign_bdtopo_fr.gpd, "read_file", side_effect=mutate_after_read),
        pytest.raises(IgnBdTopoLayerError, match="changed|integrity|SHA"),
    ):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)
```

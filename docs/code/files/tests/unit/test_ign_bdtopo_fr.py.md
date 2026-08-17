# `tests/unit/test_ign_bdtopo_fr.py`

## File identity

- Repository path: `tests/unit/test_ign_bdtopo_fr.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `ign_bdtopo_fr` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `66176bddf663845755562d64498f79e295a814b911aaed7ae1f0872e4459a9f6`

## 1. Purpose

Provides complete unit and regression coverage for the `ign_bdtopo_fr` contracts exercised in this file.

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
- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import py7zr` — required by the implementation paths and symbols documented below.
- `import pyogrio` — required by the implementation paths and symbols documented below.
- `import pytest` — required by the implementation paths and symbols documented below.
- `import yaml` — required by the implementation paths and symbols documented below.
- `from geopandas.testing import assert_geodataframe_equal` — required by the implementation paths and symbols documented below.
- `from pydantic import ValidationError` — required by the implementation paths and symbols documented below.
- `from shapely.geometry import LineString, MultiLineString, MultiPolygon, Polygon` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout import sources` — required by the implementation paths and symbols documented below.
- `from landscout.sources import ign_bdtopo_fr` — required by the implementation paths and symbols documented below.
- `from landscout.sources.ign_bdtopo_fr import ( IgnBdTopoArchiveError, IgnBdTopoDownload, IgnBdTopoDownloadError, IgnBdTopoExtraction, IgnBdTopoLayerError, IgnBdTopoSourceConfig, discover_ign_bdtopo_geopackage, discover_ign_bdtopo_layers, download_ign_bdtopo_archive, extract_ign_bdtopo_archive, list_…` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `PROJECT_ROOT` | `Path(__file__).parents[2]` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `CONFIG_PATH` | `PROJECT_ROOT / "configs/sources/ign_bdtopo_fr.yaml"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SYNTHETIC_SOURCE_URL` | `"https://example.test/BDTOPO_TEST_D031.7z"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `LINE_LAYER` | `"LIGNE_ELECTRIQUE"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `POST_LAYER` | `"POSTE_DE_TRANSFORMATION"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `DEPARTMENT_LAYER` | `"DEPARTEMENT"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ROAD_LAYER` | `"TRONCON_DE_ROUTE"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

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

- `tests/unit/test_ign_bdtopo_fr.py` — `test_invalid_department_coverage_config_fails`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_invalid_source_configuration_fails`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_missing_required_source_field_fails`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_unknown_source_config_field_is_rejected`

**Tests**

- `tests/unit/test_ign_bdtopo_fr.py::test_invalid_department_coverage_config_fails`
- `tests/unit/test_ign_bdtopo_fr.py::test_invalid_source_configuration_fails`
- `tests/unit/test_ign_bdtopo_fr.py::test_missing_required_source_field_fails`
- `tests/unit/test_ign_bdtopo_fr.py::test_unknown_source_config_field_is_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_synthetic_config`

**Signature**

```python
def _synthetic_config(
    source_config: IgnBdTopoSourceConfig,
    *,
    official_checksum: str | None = None,
) -> IgnBdTopoSourceConfig:
```

**Purpose**

Implements synthetic config according to the exact implementation and guards in this file.

**Inputs**

- `source_config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `official_checksum` (`str | None`; optional/default `None`) — integrity digest used to bind exact bytes or canonical content. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoSourceConfig`. Observed return expression(s): `IgnBdTopoSourceConfig.model_validate(content)`.

**Algorithm**

1. Computes `content` from `source_config.model_dump(mode='json')`.
2. Calls `content.update({'source_url': SYNTHETIC_SOURCE_URL, 'checksum_url': None, 'official_checksum_algorithm': 'sha256' if official_checksum is not None else None, 'official_checksum': official_checksum, 'expected_archive_size_bytes': None})` for its validation or side effect.
3. Returns `IgnBdTopoSourceConfig.model_validate(content)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnBdTopoSourceConfig.model_validate`, `content.update`, `source_config.model_dump`.

**Known repository callers**

- `tests/unit/test_ign_bdtopo_fr.py` — `_extracted_fixture`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_ambiguous_road_layer_fails_safely`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_corrupt_refresh_preserves_valid_cache`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_default_extraction_path_is_short_and_content_addressed`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_department_coverage_layer_discovery_must_be_unambiguous`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_department_coverage_loader_selects_configured_identity`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_department_coverage_requires_configured_identity_field`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_department_coverage_requires_one_authoritative_feature`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_electricity_loader_retains_both_layer_counts`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_expired_cache_is_refreshed`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_failed_refresh_preserves_valid_cache`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_fresh_cache_is_reused_without_network`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_metadata_publication_failure_restores_previous_cache_pair`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_missing_department_coverage_layer_fails`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_missing_road_layer_fails_safely`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_official_checksum_mismatch_is_rejected`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_layer_discovery_loads_selected_physical_layer`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_layer_does_not_change_electricity_loading_or_cache_shape`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_loader_preserves_lambert93_lines_unchanged`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_loader_rejects_changed_layer_inventory`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_loader_rejects_geographic_crs`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_loader_rejects_wrong_archive_config_department`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_stale_recovery_backup_rejects_cache_before_network`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_successful_archive_download_persists_sha256`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_synthetic_archive_extracts_and_discovers_required_layers`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_unsafe_parent_archive_member_is_rejected`

**Tests**

- `tests/unit/test_ign_bdtopo_fr.py::test_ambiguous_road_layer_fails_safely`
- `tests/unit/test_ign_bdtopo_fr.py::test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum`
- `tests/unit/test_ign_bdtopo_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_ign_bdtopo_fr.py::test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned`
- `tests/unit/test_ign_bdtopo_fr.py::test_corrupt_refresh_preserves_valid_cache`
- `tests/unit/test_ign_bdtopo_fr.py::test_default_extraction_path_is_short_and_content_addressed`
- `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_layer_discovery_must_be_unambiguous`
- `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_loader_selects_configured_identity`
- `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_configured_identity_field`
- `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_one_authoritative_feature`
- `tests/unit/test_ign_bdtopo_fr.py::test_electricity_loader_retains_both_layer_counts`
- `tests/unit/test_ign_bdtopo_fr.py::test_expired_cache_is_refreshed`
- `tests/unit/test_ign_bdtopo_fr.py::test_failed_refresh_preserves_valid_cache`
- `tests/unit/test_ign_bdtopo_fr.py::test_fresh_cache_is_reused_without_network`
- `tests/unit/test_ign_bdtopo_fr.py::test_metadata_publication_failure_restores_previous_cache_pair`
- `tests/unit/test_ign_bdtopo_fr.py::test_missing_department_coverage_layer_fails`
- `tests/unit/test_ign_bdtopo_fr.py::test_missing_road_layer_fails_safely`
- `tests/unit/test_ign_bdtopo_fr.py::test_official_checksum_mismatch_is_rejected`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_layer_discovery_loads_selected_physical_layer`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_layer_does_not_change_electricity_loading_or_cache_shape`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_preserves_lambert93_lines_unchanged`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_changed_layer_inventory`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_geographic_crs`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_wrong_archive_config_department`
- `tests/unit/test_ign_bdtopo_fr.py::test_stale_recovery_backup_rejects_cache_before_network`
- `tests/unit/test_ign_bdtopo_fr.py::test_successful_archive_download_persists_sha256`
- `tests/unit/test_ign_bdtopo_fr.py::test_synthetic_archive_extracts_and_discovers_required_layers`
- `tests/unit/test_ign_bdtopo_fr.py::test_unsafe_parent_archive_member_is_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_write_gpkg`

**Signature**

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

**Purpose**

Writes gpkg according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `include_lines` (`bool`; optional/default `True`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `include_posts` (`bool`; optional/default `True`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `line_layer` (`str`; optional/default `LINE_LAYER`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `post_layer` (`str`; optional/default `POST_LAYER`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `crs` (`str | None`; optional/default `'EPSG:2154'`) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.
- `invalid_post` (`bool`; optional/default `False`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `include_department` (`bool`; optional/default `False`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `department_layer` (`str`; optional/default `DEPARTMENT_LAYER`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `department_codes` (`list[str] | None`; optional/default `None`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `department_geometries` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `include_roads` (`bool`; optional/default `False`) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `road_layer` (`str`; optional/default `ROAD_LAYER`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `road_crs` (`str | None`; optional/default `None`) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.
- `road_geometry_kind` (`str`; optional/default `'mixed'`) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Calls `path.parent.mkdir(parents=True, exist_ok=True)` for its validation or side effect.
2. Computes `layer_written` from `False`.
3. Checks `include_lines`. When true: Computes `lines` from `gpd.GeoDataFrame({'object_id': ['L_VALID', 'L_NULL'], 'nature': ['HT', 'UNKNOWN'], 'tension': ['225 kV', None]}, geometry=[LineString([(0, 0), (100, 100)]), None], crs=crs)`. Calls `pyogrio.write_dataframe(lines, path, layer=line_layer, driver='GPKG')` for its validation or side effect. Computes `layer_written` from `True`.
4. Checks `include_posts`. When true: Computes `invalid` from `Polygon([(0, 0), (20, 20), (20, 0), (0, 20), (0, 0)])`. Computes `geometries` from `[Polygon([(0, 0), (0, 20), (20, 20), (20, 0), (0, 0)]), None]`. Computes `object_ids` from `['P_VALID', 'P_NULL']`. Executes 4 additional source-ordered statement(s).
5. Checks `include_roads`. When true: Checks `road_geometry_kind == 'line'`. When true: Computes `road_geometries` from `[LineString([(0, 0), (100, 100)]), LineString([(200, 200), (300, 260)])]`. Otherwise: Checks `road_geometry_kind == 'multiline'`. When true: Computes `road_geometries` from `[MultiLineString([[(0, 0), (100, 100)]]), MultiLineString([[(200, 200), (250, 250)], [(250, 250), (300, 260)]])]`. Otherwise: Computes `road_geometries` from `[LineString([(0, 0), (100, 100)]), MultiLineString([[(200, 200), (250, 250)], [(250, 250), (300, 260)]])]`. Computes `roads` from `gpd.GeoDataFrame({'object_id': ['R_LINE', 'R_MULTI'], 'nature': ['Route à 1 chaussée', 'Bretelle']}, geometry=road_geometries, crs=road_crs or crs)`. Calls `pyogrio.write_dataframe(roads, path, layer=road_layer, driver='GPKG', append=layer_written)` for its validation or side effect. Executes 1 additional source-ordered statement(s).
6. Checks `include_department`. When true: Computes `codes` from `department_codes or ['31', '32']`. Computes `geometries` from `department_geometries or [MultiPolygon([Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)])]), MultiPolygon([Polygon([(1000, 0), (1000, 1000), (2000, 1000), (2000, 0), (1000, 0)])])][:len(codes)]`. Computes `departments` from `gpd.GeoDataFrame({'code_insee': codes, 'nom_officiel': [f'Department {code}' for code in codes]}, geometry=geometries, crs=crs)`. Executes 1 additional source-ordered statement(s).

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `path.parent.mkdir`, `pyogrio.write_dataframe`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `LineString`, `MultiLineString`, `MultiPolygon`, `Polygon`, `geometries.append`, `gpd.GeoDataFrame`, `len`, `object_ids.append`, `path.parent.mkdir`, `pyogrio.write_dataframe`.

**Known repository callers**

- `tests/unit/test_ign_bdtopo_fr.py` — `_synthetic_archive_bytes`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_ambiguous_electric_line_layers_fail`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_ambiguous_road_layer_fails_safely`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_department_coverage_layer_discovery_must_be_unambiguous`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_department_coverage_requires_one_authoritative_feature`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_geographic_crs_is_rejected`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_geopackage_is_discovered_recursively`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_invalid_geometry_is_preserved_without_repair`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_layer_loader_retains_crs_counts_and_null_geometries`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_missing_electric_line_layer_fails`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_missing_transformation_post_layer_fails`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_multiple_geopackages_are_rejected_as_ambiguous`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_real_layer_names_are_listed_and_discovered`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_unsafe_parent_archive_member_is_rejected`

**Tests**

- `tests/unit/test_ign_bdtopo_fr.py::test_ambiguous_electric_line_layers_fail`
- `tests/unit/test_ign_bdtopo_fr.py::test_ambiguous_road_layer_fails_safely`
- `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_layer_discovery_must_be_unambiguous`
- `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_one_authoritative_feature`
- `tests/unit/test_ign_bdtopo_fr.py::test_geographic_crs_is_rejected`
- `tests/unit/test_ign_bdtopo_fr.py::test_geopackage_is_discovered_recursively`
- `tests/unit/test_ign_bdtopo_fr.py::test_invalid_geometry_is_preserved_without_repair`
- `tests/unit/test_ign_bdtopo_fr.py::test_layer_loader_retains_crs_counts_and_null_geometries`
- `tests/unit/test_ign_bdtopo_fr.py::test_missing_electric_line_layer_fails`
- `tests/unit/test_ign_bdtopo_fr.py::test_missing_transformation_post_layer_fails`
- `tests/unit/test_ign_bdtopo_fr.py::test_multiple_geopackages_are_rejected_as_ambiguous`
- `tests/unit/test_ign_bdtopo_fr.py::test_real_layer_names_are_listed_and_discovered`
- `tests/unit/test_ign_bdtopo_fr.py::test_unsafe_parent_archive_member_is_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_pack_7z`

**Signature**

```python
def _pack_7z(
    archive_path: Path,
    members: list[tuple[Path, str]],
) -> bytes:
```

**Purpose**

Implements pack 7z according to the exact implementation and guards in this file.

**Inputs**

- `archive_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `members` (`list[tuple[Path, str]]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bytes`. Observed return expression(s): `archive_path.read_bytes()`.

**Algorithm**

1. Calls `archive_path.parent.mkdir(parents=True, exist_ok=True)` for its validation or side effect.
2. Enters managed context(s) `py7zr.SevenZipFile(archive_path, 'w')` and executes: Iterates `(source, archive_name)` over `members`. For each value: Calls `archive.write(source, arcname=archive_name)` for its validation or side effect.
3. Returns `archive_path.read_bytes()`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `archive.write`, `archive_path.parent.mkdir`, `archive_path.read_bytes`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `archive.write`, `archive_path.parent.mkdir`, `archive_path.read_bytes`, `py7zr.SevenZipFile`.

**Known repository callers**

- `tests/unit/test_ign_bdtopo_fr.py` — `_synthetic_archive_bytes`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_ambiguous_road_layer_fails_safely`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_department_coverage_layer_discovery_must_be_unambiguous`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_department_coverage_requires_one_authoritative_feature`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_unsafe_parent_archive_member_is_rejected`

**Tests**

- `tests/unit/test_ign_bdtopo_fr.py::test_ambiguous_road_layer_fails_safely`
- `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_layer_discovery_must_be_unambiguous`
- `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_one_authoritative_feature`
- `tests/unit/test_ign_bdtopo_fr.py::test_unsafe_parent_archive_member_is_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_synthetic_archive_bytes`

**Signature**

```python
def _synthetic_archive_bytes(
    root: Path,
    *,
    include_lines: bool = True,
    include_posts: bool = True,
    invalid_post: bool = False,
    include_department: bool = False,
    include_roads: bool = False,
    road_crs: str | None = None,
    road_geometry_kind: str = "mixed",
) -> bytes:
```

**Purpose**

Implements synthetic archive bytes according to the exact implementation and guards in this file.

**Inputs**

- `root` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `include_lines` (`bool`; optional/default `True`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `include_posts` (`bool`; optional/default `True`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `invalid_post` (`bool`; optional/default `False`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `include_department` (`bool`; optional/default `False`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `include_roads` (`bool`; optional/default `False`) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `road_crs` (`str | None`; optional/default `None`) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.
- `road_geometry_kind` (`str`; optional/default `'mixed'`) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bytes`. Observed return expression(s): `_pack_7z(root / 'fixture.7z', [(gpkg_path, 'BDTOPO_TEST/GPKG/BDTOPO_TEST.gpkg')])`.

**Algorithm**

1. Computes `gpkg_path` from `root / 'fixture' / 'BDTOPO_TEST.gpkg'`.
2. Calls `_write_gpkg(gpkg_path, include_lines=include_lines, include_posts=include_posts, invalid_post=invalid_post, include_department=include_department, include_roads=include_roads, road_crs=road_crs, road_geometry_kind=road_geometry_kind)` for its validation or side effect.
3. Returns `_pack_7z(root / 'fixture.7z', [(gpkg_path, 'BDTOPO_TEST/GPKG/BDTOPO_TEST.gpkg')])`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `_write_gpkg`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_pack_7z`, `_write_gpkg`.

**Known repository callers**

- `tests/unit/test_ign_bdtopo_fr.py` — `_extracted_fixture`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_corrupt_refresh_preserves_valid_cache`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_default_extraction_path_is_short_and_content_addressed`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_department_coverage_loader_selects_configured_identity`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_department_coverage_requires_configured_identity_field`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_direct_consumers_reject_same_inventory_content_tampering`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_electricity_loader_retains_both_layer_counts`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_expired_cache_is_refreshed`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_failed_refresh_preserves_valid_cache`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_fresh_cache_is_reused_without_network`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_metadata_publication_failure_restores_previous_cache_pair`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_missing_department_coverage_layer_fails`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_missing_road_layer_fails_safely`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_official_checksum_mismatch_is_rejected`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_layer_discovery_loads_selected_physical_layer`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_layer_does_not_change_electricity_loading_or_cache_shape`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_loader_preserves_lambert93_lines_unchanged`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_loader_rejects_changed_layer_inventory`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_loader_rejects_geographic_crs`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_loader_rejects_wrong_archive_config_department`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_stale_recovery_backup_rejects_cache_before_network`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_successful_archive_download_persists_sha256`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_synthetic_archive_extracts_and_discovers_required_layers`

**Tests**

- `tests/unit/test_ign_bdtopo_fr.py::test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum`
- `tests/unit/test_ign_bdtopo_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_ign_bdtopo_fr.py::test_corrupt_refresh_preserves_valid_cache`
- `tests/unit/test_ign_bdtopo_fr.py::test_default_extraction_path_is_short_and_content_addressed`
- `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_loader_selects_configured_identity`
- `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_configured_identity_field`
- `tests/unit/test_ign_bdtopo_fr.py::test_direct_consumers_reject_same_inventory_content_tampering`
- `tests/unit/test_ign_bdtopo_fr.py::test_electricity_loader_retains_both_layer_counts`
- `tests/unit/test_ign_bdtopo_fr.py::test_expired_cache_is_refreshed`
- `tests/unit/test_ign_bdtopo_fr.py::test_failed_refresh_preserves_valid_cache`
- `tests/unit/test_ign_bdtopo_fr.py::test_fresh_cache_is_reused_without_network`
- `tests/unit/test_ign_bdtopo_fr.py::test_metadata_publication_failure_restores_previous_cache_pair`
- `tests/unit/test_ign_bdtopo_fr.py::test_missing_department_coverage_layer_fails`
- `tests/unit/test_ign_bdtopo_fr.py::test_missing_road_layer_fails_safely`
- `tests/unit/test_ign_bdtopo_fr.py::test_official_checksum_mismatch_is_rejected`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_layer_discovery_loads_selected_physical_layer`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_layer_does_not_change_electricity_loading_or_cache_shape`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_preserves_lambert93_lines_unchanged`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_changed_layer_inventory`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_geographic_crs`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_wrong_archive_config_department`
- `tests/unit/test_ign_bdtopo_fr.py::test_stale_recovery_backup_rejects_cache_before_network`
- `tests/unit/test_ign_bdtopo_fr.py::test_successful_archive_download_persists_sha256`
- `tests/unit/test_ign_bdtopo_fr.py::test_synthetic_archive_extracts_and_discovers_required_layers`

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

- `tests/unit/test_ign_bdtopo_fr.py` — `_extracted_fixture`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_ambiguous_road_layer_fails_safely`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_corrupt_refresh_preserves_valid_cache`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_default_extraction_path_is_short_and_content_addressed`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_department_coverage_layer_discovery_must_be_unambiguous`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_department_coverage_loader_selects_configured_identity`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_department_coverage_requires_configured_identity_field`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_department_coverage_requires_one_authoritative_feature`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_direct_consumers_reject_same_inventory_content_tampering`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_electricity_loader_retains_both_layer_counts`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_expired_cache_is_refreshed`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_failed_refresh_preserves_valid_cache`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_fresh_cache_is_reused_without_network`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_metadata_publication_failure_restores_previous_cache_pair`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_missing_department_coverage_layer_fails`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_missing_road_layer_fails_safely`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_official_checksum_mismatch_is_rejected`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_layer_discovery_loads_selected_physical_layer`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_layer_does_not_change_electricity_loading_or_cache_shape`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_loader_preserves_lambert93_lines_unchanged`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_loader_rejects_changed_layer_inventory`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_loader_rejects_geographic_crs`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_loader_rejects_wrong_archive_config_department`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_stale_recovery_backup_rejects_cache_before_network`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_successful_archive_download_persists_sha256`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_synthetic_archive_extracts_and_discovers_required_layers`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_unsafe_parent_archive_member_is_rejected`

**Tests**

- `tests/unit/test_ign_bdtopo_fr.py::test_ambiguous_road_layer_fails_safely`
- `tests/unit/test_ign_bdtopo_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_ign_bdtopo_fr.py::test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned`
- `tests/unit/test_ign_bdtopo_fr.py::test_corrupt_refresh_preserves_valid_cache`
- `tests/unit/test_ign_bdtopo_fr.py::test_default_extraction_path_is_short_and_content_addressed`
- `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_layer_discovery_must_be_unambiguous`
- `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_loader_selects_configured_identity`
- `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_configured_identity_field`
- `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_one_authoritative_feature`
- `tests/unit/test_ign_bdtopo_fr.py::test_direct_consumers_reject_same_inventory_content_tampering`
- `tests/unit/test_ign_bdtopo_fr.py::test_electricity_loader_retains_both_layer_counts`
- `tests/unit/test_ign_bdtopo_fr.py::test_expired_cache_is_refreshed`
- `tests/unit/test_ign_bdtopo_fr.py::test_failed_refresh_preserves_valid_cache`
- `tests/unit/test_ign_bdtopo_fr.py::test_fresh_cache_is_reused_without_network`
- `tests/unit/test_ign_bdtopo_fr.py::test_metadata_publication_failure_restores_previous_cache_pair`
- `tests/unit/test_ign_bdtopo_fr.py::test_missing_department_coverage_layer_fails`
- `tests/unit/test_ign_bdtopo_fr.py::test_missing_road_layer_fails_safely`
- `tests/unit/test_ign_bdtopo_fr.py::test_official_checksum_mismatch_is_rejected`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_layer_discovery_loads_selected_physical_layer`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_layer_does_not_change_electricity_loading_or_cache_shape`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_preserves_lambert93_lines_unchanged`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_changed_layer_inventory`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_geographic_crs`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_wrong_archive_config_department`
- `tests/unit/test_ign_bdtopo_fr.py::test_stale_recovery_backup_rejects_cache_before_network`
- `tests/unit/test_ign_bdtopo_fr.py::test_successful_archive_download_persists_sha256`
- `tests/unit/test_ign_bdtopo_fr.py::test_synthetic_archive_extracts_and_discovers_required_layers`
- `tests/unit/test_ign_bdtopo_fr.py::test_unsafe_parent_archive_member_is_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_metadata_path`

**Signature**

```python
def _metadata_path(archive_path: Path) -> Path:
```

**Purpose**

Implements metadata path according to the exact implementation and guards in this file.

**Inputs**

- `archive_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Path`. Observed return expression(s): `archive_path.parent / f'{archive_path.name}.metadata.json'`.

**Algorithm**

1. Returns `archive_path.parent / f'{archive_path.name}.metadata.json'`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

- `tests/unit/test_ign_bdtopo_fr.py` — `test_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_corrupt_refresh_preserves_valid_cache`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_expired_cache_is_refreshed`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_failed_refresh_preserves_valid_cache`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_metadata_publication_failure_restores_previous_cache_pair`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_successful_archive_download_persists_sha256`

**Tests**

- `tests/unit/test_ign_bdtopo_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_ign_bdtopo_fr.py::test_corrupt_refresh_preserves_valid_cache`
- `tests/unit/test_ign_bdtopo_fr.py::test_expired_cache_is_refreshed`
- `tests/unit/test_ign_bdtopo_fr.py::test_failed_refresh_preserves_valid_cache`
- `tests/unit/test_ign_bdtopo_fr.py::test_metadata_publication_failure_restores_previous_cache_pair`
- `tests/unit/test_ign_bdtopo_fr.py::test_successful_archive_download_persists_sha256`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_extraction_metadata_path`

**Signature**

```python
def _extraction_metadata_path(extraction_path: Path) -> Path:
```

**Purpose**

Implements extraction metadata path according to the exact implementation and guards in this file.

**Inputs**

- `extraction_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Path`. Observed return expression(s): `extraction_path / '.landscout-extraction.json'`.

**Algorithm**

1. Returns `extraction_path / '.landscout-extraction.json'`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

- `tests/unit/test_ign_bdtopo_fr.py` — `test_forged_extraction_metadata_never_returns_cache_hit`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_malformed_geopackage_sha_is_not_trusted`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_malformed_geopackage_size_is_not_trusted`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_schema_v2_extraction_metadata_binds_physical_geopackage`

**Tests**

- `tests/unit/test_ign_bdtopo_fr.py::test_forged_extraction_metadata_never_returns_cache_hit`
- `tests/unit/test_ign_bdtopo_fr.py::test_malformed_geopackage_sha_is_not_trusted`
- `tests/unit/test_ign_bdtopo_fr.py::test_malformed_geopackage_size_is_not_trusted`
- `tests/unit/test_ign_bdtopo_fr.py::test_schema_v2_extraction_metadata_binds_physical_geopackage`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_extracted_fixture`

**Signature**

```python
def _extracted_fixture(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    *,
    include_roads: bool = False,
) -> tuple[IgnBdTopoSourceConfig, IgnBdTopoDownload, IgnBdTopoExtraction]:
```

**Purpose**

Implements extracted fixture according to the exact implementation and guards in this file.

**Inputs**

- `tmp_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `include_roads` (`bool`; optional/default `False`) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[IgnBdTopoSourceConfig, IgnBdTopoDownload, IgnBdTopoExtraction]`. Observed return expression(s): `(config, download, extraction)`.

**Algorithm**

1. Computes `archive_content` from `_synthetic_archive_bytes(tmp_path / 'source', include_roads=include_roads)`.
2. Computes `config` from `_synthetic_config(source_config)`.
3. Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(archive_content))` and executes: Computes `download` from `download_ign_bdtopo_archive(config, tmp_path / 'cache')`.
4. Computes `extraction` from `extract_ign_bdtopo_archive(download, config, extraction_dir=tmp_path / 'extracted')`.
5. Returns `(config, download, extraction)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `download_ign_bdtopo_archive`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `patch`.

**Known repository callers**

- `tests/unit/test_ign_bdtopo_fr.py` — `test_direct_consumers_reject_same_inventory_content_tampering`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_forged_extraction_metadata_never_returns_cache_hit`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_malformed_geopackage_sha_is_not_trusted`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_malformed_geopackage_size_is_not_trusted`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_loader_rejects_source_change_after_physical_read`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_physical_layer_cannot_collide_with_electricity_roles`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_same_size_geopackage_tamper_invalidates_extraction_cache`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_schema_v2_extraction_metadata_binds_physical_geopackage`

**Tests**

- `tests/unit/test_ign_bdtopo_fr.py::test_direct_consumers_reject_same_inventory_content_tampering`
- `tests/unit/test_ign_bdtopo_fr.py::test_forged_extraction_metadata_never_returns_cache_hit`
- `tests/unit/test_ign_bdtopo_fr.py::test_malformed_geopackage_sha_is_not_trusted`
- `tests/unit/test_ign_bdtopo_fr.py::test_malformed_geopackage_size_is_not_trusted`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_source_change_after_physical_read`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_physical_layer_cannot_collide_with_electricity_roles`
- `tests/unit/test_ign_bdtopo_fr.py::test_same_size_geopackage_tamper_invalidates_extraction_cache`
- `tests/unit/test_ign_bdtopo_fr.py::test_schema_v2_extraction_metadata_binds_physical_geopackage`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_expire_cache`

**Signature**

```python
def _expire_cache(metadata_path: Path) -> bytes:
```

**Purpose**

Implements expire cache according to the exact implementation and guards in this file.

**Inputs**

- `metadata_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bytes`. Observed return expression(s): `metadata_path.read_bytes()`.

**Algorithm**

1. Computes `metadata` from `json.loads(metadata_path.read_text(encoding='utf-8'))`.
2. Computes `metadata['download_timestamp']` from `(datetime.now(UTC) - timedelta(days=365)).isoformat()`.
3. Calls `metadata_path.write_text(json.dumps(metadata), encoding='utf-8')` for its validation or side effect.
4. Returns `metadata_path.read_bytes()`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `metadata_path.read_bytes`, `metadata_path.read_text`, `metadata_path.write_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `(datetime.now(UTC) - timedelta(days=365)).isoformat`, `datetime.now`, `json.dumps`, `json.loads`, `metadata_path.read_bytes`, `metadata_path.read_text`, `metadata_path.write_text`, `timedelta`.

**Known repository callers**

- `tests/unit/test_ign_bdtopo_fr.py` — `test_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_corrupt_refresh_preserves_valid_cache`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_expired_cache_is_refreshed`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_failed_refresh_preserves_valid_cache`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_metadata_publication_failure_restores_previous_cache_pair`

**Tests**

- `tests/unit/test_ign_bdtopo_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_ign_bdtopo_fr.py::test_corrupt_refresh_preserves_valid_cache`
- `tests/unit/test_ign_bdtopo_fr.py::test_expired_cache_is_refreshed`
- `tests/unit/test_ign_bdtopo_fr.py::test_failed_refresh_preserves_valid_cache`
- `tests/unit/test_ign_bdtopo_fr.py::test_metadata_publication_failure_restores_previous_cache_pair`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `source_config`

**Signature**

```python
def source_config() -> IgnBdTopoSourceConfig:
```

**Purpose**

Implements source config according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `IgnBdTopoSourceConfig`. Observed return expression(s): `load_ign_bdtopo_source_config(CONFIG_PATH)`.

**Algorithm**

1. Returns `load_ign_bdtopo_source_config(CONFIG_PATH)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `load_ign_bdtopo_source_config`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `load_ign_bdtopo_source_config`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_metadata_publication_failure_restores_previous_cache_pair.fail_metadata_publication`

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
2. Checks `source.name.endswith('.metadata.json.part') and target == metadata_path`. When true: Computes `failure_injected` from `True`. Raises `PermissionError('simulated persistent metadata lock')`.
3. Calls `original_replace(source, target)` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `source.name.endswith('.metadata.json.part') and target == metadata_path` is true.

**Exceptions**

- Explicitly raises: `PermissionError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `original_replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `PermissionError`, `original_replace`, `source.name.endswith`.

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

### `test_road_loader_rejects_source_change_after_physical_read.mutate_after_read`

**Signature**

```python
def mutate_after_read(*args: object, **kwargs: object) -> gpd.GeoDataFrame:
```

**Purpose**

Implements mutate after read according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `frame`.

**Algorithm**

1. Computes `frame` from `original_read(*args, **kwargs)`.
2. Computes `content` from `extraction.geopackage_path.read_bytes()`.
3. Calls `extraction.geopackage_path.write_bytes(content.replace(b'Bretelle', b'BretellX', 1))` for its validation or side effect.
4. Returns `frame`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `content.replace`, `extraction.geopackage_path.read_bytes`, `extraction.geopackage_path.write_bytes`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `content.replace`, `extraction.geopackage_path.read_bytes`, `extraction.geopackage_path.write_bytes`, `original_read`.

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
def test_valid_source_config_loads(source_config: IgnBdTopoSourceConfig) -> None:
```

**Purpose**

Protects the `valid source config loads` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `source_config`.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls only local assertions/expressions.

**Expected result**

- Direct assertions: `assert 'IGN' in source_config.provider`; `assert source_config.department_code == '31'`; `assert source_config.projection == 'EPSG:2154'`; `assert source_config.format == 'GPKG'`; `assert source_config.edition == '2026-06-15'`; `assert source_config.access.road_segments.class_label == 'Tronçon de route'`; `assert source_config.access.road_segments.match_tokens == ('tronçon', 'route')`; `assert source_config.coverage.department_layer.match_tokens == ('departement',)`; `assert source_config.coverage.department_layer.department_code_field == 'code_insee'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `valid source config loads` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- No calls.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_department_coverage_config_fails`

**Signature**

```python
def test_invalid_department_coverage_config_fails(mutation: str) -> None:
```

**Purpose**

Protects the `invalid department coverage config fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `mutation`.
- Contains 2 explicit setup/context statement(s).
- Computes `content` from `_config_data()`.
- Enters managed context(s) `pytest.raises(ValidationError)` and executes: Calls `IgnBdTopoSourceConfig.model_validate(content)` for its validation or side effect.

**Action**

- Calls `IgnBdTopoSourceConfig.model_validate`, `_config_data`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError): IgnBdTopoSourceConfig.model_validate(content)`.

**Regression protected**

- Protects the exact `invalid department coverage config fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `IgnBdTopoSourceConfig.model_validate`, `_config_data`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_required_source_field_fails`

**Signature**

```python
def test_missing_required_source_field_fails(field: str) -> None:
```

**Purpose**

Protects the `missing required source field fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `field`.
- Contains 2 explicit setup/context statement(s).
- Computes `content` from `_config_data()`.
- Enters managed context(s) `pytest.raises(ValidationError)` and executes: Calls `IgnBdTopoSourceConfig.model_validate(content)` for its validation or side effect.

**Action**

- Calls `IgnBdTopoSourceConfig.model_validate`, `_config_data`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError): IgnBdTopoSourceConfig.model_validate(content)`.

**Regression protected**

- Protects the exact `missing required source field fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `IgnBdTopoSourceConfig.model_validate`, `_config_data`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_source_configuration_fails`

**Signature**

```python
def test_invalid_source_configuration_fails(field: str, value: str) -> None:
```

**Purpose**

Protects the `invalid source configuration fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `field`, `value`.
- Contains 3 explicit setup/context statement(s).
- Computes `content` from `_config_data()`.
- Computes `content[field]` from `value`.
- Enters managed context(s) `pytest.raises(ValidationError)` and executes: Calls `IgnBdTopoSourceConfig.model_validate(content)` for its validation or side effect.

**Action**

- Calls `IgnBdTopoSourceConfig.model_validate`, `_config_data`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError): IgnBdTopoSourceConfig.model_validate(content)`.

**Regression protected**

- Protects the exact `invalid source configuration fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `IgnBdTopoSourceConfig.model_validate`, `_config_data`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unknown_source_config_field_is_rejected`

**Signature**

```python
def test_unknown_source_config_field_is_rejected() -> None:
```

**Purpose**

Protects the `unknown source config field is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `content` from `_config_data()`.
- Computes `content['invented']` from `'not allowed'`.
- Enters managed context(s) `pytest.raises(ValidationError)` and executes: Calls `IgnBdTopoSourceConfig.model_validate(content)` for its validation or side effect.

**Action**

- Calls `IgnBdTopoSourceConfig.model_validate`, `_config_data`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError): IgnBdTopoSourceConfig.model_validate(content)`.

**Regression protected**

- Protects the exact `unknown source config field is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `IgnBdTopoSourceConfig.model_validate`, `_config_data`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_successful_archive_download_persists_sha256`

**Signature**

```python
def test_successful_archive_download_persists_sha256(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `successful archive download persists sha256` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 4 explicit setup/context statement(s).
- Computes `archive_content` from `_synthetic_archive_bytes(tmp_path)`.
- Computes `config` from `_synthetic_config(source_config)`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(archive_content))` and executes: Computes `result` from `download_ign_bdtopo_archive(config, tmp_path / 'cache')`.
- Computes `metadata` from `json.loads(_metadata_path(result.path).read_text(encoding='utf-8'))`.

**Action**

- Calls `_metadata_path`, `_metadata_path(result.path).read_text`, `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `download_ign_bdtopo_archive`, `json.loads`, `result.path.read_bytes`, `sha256`, `sha256(archive_content).hexdigest`.

**Expected result**

- Direct assertions: `assert result.cache_hit is False`; `assert result.path.read_bytes() == archive_content`; `assert result.file_size == len(archive_content)`; `assert result.sha256 == sha256(archive_content).hexdigest()`; `assert metadata['sha256'] == result.sha256`; `assert metadata['source_url'] == SYNTHETIC_SOURCE_URL`; `assert metadata['official_checksum'] is None`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `successful archive download persists sha256` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_metadata_path`, `_metadata_path(result.path).read_text`, `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `download_ign_bdtopo_archive`, `json.loads`, `len`, `patch`, `result.path.read_bytes`, `sha256`, `sha256(archive_content).hexdigest`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum`

**Signature**

```python
def test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `archive integrity reports local sha256 and no fabricated checksum` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 3 explicit setup/context statement(s).
- Computes `archive_path` from `tmp_path / 'fixture.7z'`.
- Computes `archive_content` from `_synthetic_archive_bytes(tmp_path / 'source')`.
- Computes `integrity` from `validate_ign_bdtopo_archive(archive_path, _synthetic_config(source_config))`.

**Action**

- Calls `_synthetic_archive_bytes`, `_synthetic_config`, `archive_path.write_bytes`, `sha256`, `sha256(archive_content).hexdigest`, `validate_ign_bdtopo_archive`.

**Expected result**

- Direct assertions: `assert integrity.file_size == len(archive_content)`; `assert integrity.sha256 == sha256(archive_content).hexdigest()`; `assert integrity.official_checksum is None`; `assert integrity.official_checksum_algorithm is None`; `assert integrity.official_checksum_validated is False`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `archive integrity reports local sha256 and no fabricated checksum` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_synthetic_archive_bytes`, `_synthetic_config`, `archive_path.write_bytes`, `len`, `sha256`, `sha256(archive_content).hexdigest`, `validate_ign_bdtopo_archive`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_fresh_cache_is_reused_without_network`

**Signature**

```python
def test_fresh_cache_is_reused_without_network(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `fresh cache is reused without network` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 5 explicit setup/context statement(s).
- Computes `content` from `_synthetic_archive_bytes(tmp_path)`.
- Computes `config` from `_synthetic_config(source_config)`.
- Computes `cache_dir` from `tmp_path / 'cache'`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(content))` and executes: Computes `first` from `download_ign_bdtopo_archive(config, cache_dir)`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', side_effect=AssertionError('network must not be called'))` and executes: Computes `second` from `download_ign_bdtopo_archive(config, cache_dir)`.

**Action**

- Calls `AssertionError`, `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `download_ign_bdtopo_archive`.

**Expected result**

- Direct assertions: `assert second.cache_hit is True`; `assert second.path == first.path`; `assert second.sha256 == first.sha256`; `assert second.download_timestamp == first.download_timestamp`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `fresh cache is reused without network` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `AssertionError`, `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `download_ign_bdtopo_archive`, `patch`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_stale_recovery_backup_rejects_cache_before_network`

**Signature**

```python
def test_stale_recovery_backup_rejects_cache_before_network(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `stale recovery backup rejects cache before network` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 7 explicit setup/context statement(s).
- Computes `content` from `_synthetic_archive_bytes(tmp_path)`.
- Computes `config` from `_synthetic_config(source_config)`.
- Computes `cache_dir` from `tmp_path / 'cache'`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(content))` and executes: Computes `first` from `download_ign_bdtopo_archive(config, cache_dir)`.
- Computes `recovery_path` from `first.path.with_name(f'{first.path.name}.bak')`.
- Computes `recovery_bytes` from `b'manual IGN recovery material'`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', side_effect=AssertionError('stale recovery must fail before network')), pytest.raises(IgnBdTopoDownloadError, match='backup|recovery|manual')` and executes: Calls `download_ign_bdtopo_archive(config, cache_dir)` for its validation or side effect.

**Action**

- Calls `AssertionError`, `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `download_ign_bdtopo_archive`, `first.path.read_bytes`, `first.path.with_name`, `opener.assert_not_called`, `recovery_path.read_bytes`, `recovery_path.write_bytes`.

**Expected result**

- Direct assertions: `assert recovery_path.read_bytes() == recovery_bytes`; `assert first.path.read_bytes() == content`.
- Expected exception contexts: `with patch('landscout.sources.ign_bdtopo_fr.open_safe_https', side_effect=AssertionError('stale recovery must fail before network')) as opener, pytest.raises(IgnBdTopoDownloadError, match='backup|recovery|manual'): download_ign_bdtopo_archive(config, cache_dir)`.

**Regression protected**

- Protects the exact `stale recovery backup rejects cache before network` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `AssertionError`, `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `download_ign_bdtopo_archive`, `first.path.read_bytes`, `first.path.with_name`, `opener.assert_not_called`, `patch`, `pytest.raises`, `recovery_path.read_bytes`, `recovery_path.write_bytes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_expired_cache_is_refreshed`

**Signature**

```python
def test_expired_cache_is_refreshed(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `expired cache is refreshed` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 6 explicit setup/context statement(s).
- Computes `old_content` from `_synthetic_archive_bytes(tmp_path / 'v1')`.
- Computes `new_content` from `_synthetic_archive_bytes(tmp_path / 'v2', invalid_post=True)`.
- Computes `config` from `_synthetic_config(source_config)`.
- Computes `cache_dir` from `tmp_path / 'cache'`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(old_content))` and executes: Computes `first` from `download_ign_bdtopo_archive(config, cache_dir)`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(new_content))` and executes: Computes `refreshed` from `download_ign_bdtopo_archive(config, cache_dir)`.

**Action**

- Calls `_expire_cache`, `_metadata_path`, `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `cache_dir.glob`, `download_ign_bdtopo_archive`, `refreshed.path.read_bytes`.

**Expected result**

- Direct assertions: `assert opener.call_count == 1`; `assert refreshed.cache_hit is False`; `assert refreshed.path.read_bytes() == new_content`; `assert refreshed.sha256 != first.sha256`; `assert not list(cache_dir.glob('*.part'))`; `assert not list(cache_dir.glob('*.bak'))`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `expired cache is refreshed` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_expire_cache`, `_metadata_path`, `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `cache_dir.glob`, `download_ign_bdtopo_archive`, `list`, `patch`, `refreshed.path.read_bytes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_failed_refresh_preserves_valid_cache`

**Signature**

```python
def test_failed_refresh_preserves_valid_cache(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `failed refresh preserves valid cache` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 9 explicit setup/context statement(s).
- Computes `content` from `_synthetic_archive_bytes(tmp_path)`.
- Computes `config` from `_synthetic_config(source_config)`.
- Computes `cache_dir` from `tmp_path / 'cache'`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(content))` and executes: Computes `first` from `download_ign_bdtopo_archive(config, cache_dir)`.
- Computes `metadata_path` from `_metadata_path(first.path)`.
- Computes `old_archive` from `first.path.read_bytes()`.
- Computes `expired_metadata` from `_expire_cache(metadata_path)`.
- Computes `error` from `HTTPError(SYNTHETIC_SOURCE_URL, 503, 'Unavailable', None, None)`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', side_effect=error), pytest.raises(IgnBdTopoDownloadError)` and executes: Calls `download_ign_bdtopo_archive(config, cache_dir)` for its validation or side effect.

**Action**

- Calls `HTTPError`, `_expire_cache`, `_metadata_path`, `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `cache_dir.glob`, `download_ign_bdtopo_archive`, `first.path.read_bytes`, `metadata_path.read_bytes`.

**Expected result**

- Direct assertions: `assert first.path.read_bytes() == old_archive`; `assert metadata_path.read_bytes() == expired_metadata`; `assert not list(cache_dir.glob('*.part'))`; `assert not list(cache_dir.glob('*.bak'))`.
- Expected exception contexts: `with patch('landscout.sources.ign_bdtopo_fr.open_safe_https', side_effect=error), pytest.raises(IgnBdTopoDownloadError): download_ign_bdtopo_archive(config, cache_dir)`.

**Regression protected**

- Protects the exact `failed refresh preserves valid cache` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `HTTPError`, `_expire_cache`, `_metadata_path`, `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `cache_dir.glob`, `download_ign_bdtopo_archive`, `first.path.read_bytes`, `list`, `metadata_path.read_bytes`, `patch`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned`

**Signature**

```python
def test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `corrupt new archive is rejected and temporary files are cleaned` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 3 explicit setup/context statement(s).
- Computes `config` from `_synthetic_config(source_config)`.
- Computes `cache_dir` from `tmp_path / 'cache'`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(b'not a 7z archive')), pytest.raises(IgnBdTopoArchiveError)` and executes: Calls `download_ign_bdtopo_archive(config, cache_dir)` for its validation or side effect.

**Action**

- Calls `_response`, `_synthetic_config`, `cache_dir.glob`, `download_ign_bdtopo_archive`.

**Expected result**

- Direct assertions: `assert not list(cache_dir.glob('*.7z'))`; `assert not list(cache_dir.glob('*.part'))`; `assert not list(cache_dir.glob('*.bak'))`.
- Expected exception contexts: `with patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(b'not a 7z archive')), pytest.raises(IgnBdTopoArchiveError): download_ign_bdtopo_archive(config, cache_dir)`.

**Regression protected**

- Protects the exact `corrupt new archive is rejected and temporary files are cleaned` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_response`, `_synthetic_config`, `cache_dir.glob`, `download_ign_bdtopo_archive`, `list`, `patch`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_corrupt_refresh_preserves_valid_cache`

**Signature**

```python
def test_corrupt_refresh_preserves_valid_cache(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `corrupt refresh preserves valid cache` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 8 explicit setup/context statement(s).
- Computes `content` from `_synthetic_archive_bytes(tmp_path)`.
- Computes `config` from `_synthetic_config(source_config)`.
- Computes `cache_dir` from `tmp_path / 'cache'`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(content))` and executes: Computes `first` from `download_ign_bdtopo_archive(config, cache_dir)`.
- Computes `metadata_path` from `_metadata_path(first.path)`.
- Computes `old_archive` from `first.path.read_bytes()`.
- Computes `expired_metadata` from `_expire_cache(metadata_path)`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(b'broken refresh')), pytest.raises(IgnBdTopoArchiveError)` and executes: Calls `download_ign_bdtopo_archive(config, cache_dir)` for its validation or side effect.

**Action**

- Calls `_expire_cache`, `_metadata_path`, `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `cache_dir.glob`, `download_ign_bdtopo_archive`, `first.path.read_bytes`, `metadata_path.read_bytes`.

**Expected result**

- Direct assertions: `assert first.path.read_bytes() == old_archive`; `assert metadata_path.read_bytes() == expired_metadata`; `assert not list(cache_dir.glob('*.part'))`.
- Expected exception contexts: `with patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(b'broken refresh')), pytest.raises(IgnBdTopoArchiveError): download_ign_bdtopo_archive(config, cache_dir)`.

**Regression protected**

- Protects the exact `corrupt refresh preserves valid cache` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_expire_cache`, `_metadata_path`, `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `cache_dir.glob`, `download_ign_bdtopo_archive`, `first.path.read_bytes`, `list`, `metadata_path.read_bytes`, `patch`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_metadata_publication_failure_restores_previous_cache_pair`

**Signature**

```python
def test_metadata_publication_failure_restores_previous_cache_pair(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `metadata publication failure restores previous cache pair` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 11 explicit setup/context statement(s).
- Computes `old_content` from `_synthetic_archive_bytes(tmp_path / 'v1')`.
- Computes `new_content` from `_synthetic_archive_bytes(tmp_path / 'v2', invalid_post=True)`.
- Computes `config` from `_synthetic_config(source_config)`.
- Computes `cache_dir` from `tmp_path / 'cache'`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(old_content))` and executes: Computes `first` from `download_ign_bdtopo_archive(config, cache_dir)`.
- Computes `metadata_path` from `_metadata_path(first.path)`.
- Computes `old_archive` from `first.path.read_bytes()`.
- Computes `expired_metadata` from `_expire_cache(metadata_path)`.
- Computes `original_replace` from `ign_bdtopo_fr._replace_file`.
- Computes `failure_injected` from `False`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(new_content)), patch.object(ign_bdtopo_fr, '_replace_file', side_effect=fail_metadata_publication), pytest.raises(IgnBdTopoDownloadError)` and executes: Calls `download_ign_bdtopo_archive(config, cache_dir)` for its validation or side effect.

**Action**

- Calls `PermissionError`, `_expire_cache`, `_metadata_path`, `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `cache_dir.glob`, `download_ign_bdtopo_archive`, `first.path.read_bytes`, `metadata_path.read_bytes`, `original_replace`, `source.name.endswith`.

**Expected result**

- Direct assertions: `assert failure_injected`; `assert first.path.read_bytes() == old_archive`; `assert metadata_path.read_bytes() == expired_metadata`; `assert not list(cache_dir.glob('*.part'))`; `assert not list(cache_dir.glob('*.bak'))`.
- Expected exception contexts: `with patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(new_content)), patch.object(ign_bdtopo_fr, '_replace_file', side_effect=fail_metadata_publication), pytest.raises(IgnBdTopoDownloadError): download_ign_bdtopo_archive(config, cache_dir)`.

**Regression protected**

- Protects the exact `metadata publication failure restores previous cache pair` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `PermissionError`, `_expire_cache`, `_metadata_path`, `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `cache_dir.glob`, `download_ign_bdtopo_archive`, `first.path.read_bytes`, `list`, `metadata_path.read_bytes`, `original_replace`, `patch`, `patch.object`, `pytest.raises`, `source.name.endswith`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_publication_and_rollback_failure_preserves_exact_recovery_backups`

**Signature**

```python
def test_publication_and_rollback_failure_preserves_exact_recovery_backups(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `publication and rollback failure preserves exact recovery backups` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 10 explicit setup/context statement(s).
- Computes `archive_path` from `tmp_path / 'cached.7z'`.
- Computes `metadata_path` from `tmp_path / 'cached.7z.metadata.json'`.
- Computes `temporary_archive` from `tmp_path / 'cached.7z.part'`.
- Computes `temporary_metadata` from `tmp_path / 'cached.7z.metadata.json.part'`.
- Computes `old_archive` from `b'exact old archive'`.
- Computes `old_metadata` from `b'exact old metadata'`.
- Computes `archive_backup` from `archive_path.with_name(f'{archive_path.name}.bak')`.
- Computes `metadata_backup` from `metadata_path.with_name(f'{metadata_path.name}.bak')`.
- Computes `original_replace` from `ign_bdtopo_fr._replace_file`.
- Enters managed context(s) `patch.object(ign_bdtopo_fr, '_replace_file', side_effect=fail_publication_and_rollback), pytest.raises(IgnBdTopoDownloadError, match='rollback')` and executes: Calls `ign_bdtopo_fr._publish_cache_pair(temporary_archive, temporary_metadata, archive_path, metadata_path)` for its validation or side effect.

**Action**

- Calls `OSError`, `archive_backup.read_bytes`, `archive_path.with_name`, `archive_path.write_bytes`, `ign_bdtopo_fr._publish_cache_pair`, `metadata_backup.read_bytes`, `metadata_path.with_name`, `metadata_path.write_bytes`, `original_replace`, `temporary_archive.write_bytes`, `temporary_metadata.write_bytes`.

**Expected result**

- Direct assertions: `assert archive_backup.read_bytes() == old_archive`; `assert metadata_backup.read_bytes() == old_metadata`.
- Expected exception contexts: `with patch.object(ign_bdtopo_fr, '_replace_file', side_effect=fail_publication_and_rollback), pytest.raises(IgnBdTopoDownloadError, match='rollback'): ign_bdtopo_fr._publish_cache_pair(temporary_archive, temporary_metadata, archive_path, metadata_path)`.

**Regression protected**

- Protects the exact `publication and rollback failure preserves exact recovery backups` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `OSError`, `archive_backup.read_bytes`, `archive_path.with_name`, `archive_path.write_bytes`, `ign_bdtopo_fr._publish_cache_pair`, `metadata_backup.read_bytes`, `metadata_path.with_name`, `metadata_path.write_bytes`, `original_replace`, `patch.object`, `pytest.raises`, `temporary_archive.write_bytes`, `temporary_metadata.write_bytes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_cleanup_failure_does_not_mask_double_failure_recovery_error`

**Signature**

```python
def test_cleanup_failure_does_not_mask_double_failure_recovery_error(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `cleanup failure does not mask double failure recovery error` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 15 explicit setup/context statement(s).
- Computes `old_content` from `_synthetic_archive_bytes(tmp_path / 'v1')`.
- Computes `new_content` from `_synthetic_archive_bytes(tmp_path / 'v2', invalid_post=True)`.
- Computes `config` from `_synthetic_config(source_config)`.
- Computes `cache_dir` from `tmp_path / 'cache'`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(old_content))` and executes: Computes `first` from `download_ign_bdtopo_archive(config, cache_dir)`.
- Computes `metadata_path` from `_metadata_path(first.path)`.
- Computes `old_archive` from `first.path.read_bytes()`.
- Computes `old_metadata` from `_expire_cache(metadata_path)`.
- Computes `temporary_metadata` from `metadata_path.with_name(f'{metadata_path.name}.part')`.
- Computes `archive_backup` from `first.path.with_name(f'{first.path.name}.bak')`.
- Computes `metadata_backup` from `metadata_path.with_name(f'{metadata_path.name}.bak')`.
- Computes `original_replace` from `ign_bdtopo_fr._replace_file`.

**Action**

- Calls `OSError`, `PermissionError`, `_expire_cache`, `_metadata_path`, `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `archive_backup.read_bytes`, `download_ign_bdtopo_archive`, `first.path.read_bytes`, `first.path.with_name`, `metadata_backup.read_bytes`, `metadata_path.with_name`, `original_replace`, `original_unlink`.

**Expected result**

- Direct assertions: `assert archive_backup.read_bytes() == old_archive`; `assert metadata_backup.read_bytes() == old_metadata`.
- Expected exception contexts: `with patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(new_content)), patch.object(ign_bdtopo_fr, '_replace_file', side_effect=fail_publication_and_rollback), patch.object(Path, 'unlink', new=fail_temporary_cleanup), pytest.raises(IgnBdTopoDownloadError, match='rollback'): download_ign_bdtopo_archive(config, cache_dir)`.

**Regression protected**

- Protects the exact `cleanup failure does not mask double failure recovery error` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `OSError`, `PermissionError`, `_expire_cache`, `_metadata_path`, `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `archive_backup.read_bytes`, `download_ign_bdtopo_archive`, `first.path.read_bytes`, `first.path.with_name`, `metadata_backup.read_bytes`, `metadata_path.with_name`, `original_replace`, `original_unlink`, `patch`, `patch.object`, `pytest.raises`.

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
- Computes `archive_path` from `tmp_path / 'cached.7z'`.
- Computes `metadata_path` from `tmp_path / 'cached.7z.metadata.json'`.
- Computes `temporary_archive` from `tmp_path / 'cached.7z.part'`.
- Computes `temporary_metadata` from `tmp_path / 'cached.7z.metadata.json.part'`.
- Computes `archive_backup` from `tmp_path / 'cached.7z.bak'`.
- Enters managed context(s) `pytest.raises(IgnBdTopoDownloadError, match='backup|recovery|manual')` and executes: Calls `ign_bdtopo_fr._publish_cache_pair(temporary_archive, temporary_metadata, archive_path, metadata_path)` for its validation or side effect.

**Action**

- Calls `archive_backup.read_bytes`, `archive_backup.write_bytes`, `archive_path.read_bytes`, `archive_path.write_bytes`, `ign_bdtopo_fr._publish_cache_pair`, `metadata_path.read_bytes`, `metadata_path.write_bytes`, `temporary_archive.write_bytes`, `temporary_metadata.write_bytes`.

**Expected result**

- Direct assertions: `assert archive_path.read_bytes() == b'old archive'`; `assert metadata_path.read_bytes() == b'old metadata'`; `assert archive_backup.read_bytes() == b'manual recovery archive'`.
- Expected exception contexts: `with pytest.raises(IgnBdTopoDownloadError, match='backup|recovery|manual'): ign_bdtopo_fr._publish_cache_pair(temporary_archive, temporary_metadata, archive_path, metadata_path)`.

**Regression protected**

- Protects the exact `stale cache recovery backup fails closed without destroying it` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `archive_backup.read_bytes`, `archive_backup.write_bytes`, `archive_path.read_bytes`, `archive_path.write_bytes`, `ign_bdtopo_fr._publish_cache_pair`, `metadata_path.read_bytes`, `metadata_path.write_bytes`, `pytest.raises`, `temporary_archive.write_bytes`, `temporary_metadata.write_bytes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_official_checksum_mismatch_is_rejected`

**Signature**

```python
def test_official_checksum_mismatch_is_rejected(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `official checksum mismatch is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 4 explicit setup/context statement(s).
- Computes `archive_content` from `_synthetic_archive_bytes(tmp_path)`.
- Computes `config` from `_synthetic_config(source_config, official_checksum='0' * 64)`.
- Computes `cache_dir` from `tmp_path / 'cache'`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(archive_content)), pytest.raises(IgnBdTopoArchiveError, match='checksum|SHA')` and executes: Calls `download_ign_bdtopo_archive(config, cache_dir)` for its validation or side effect.

**Action**

- Calls `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `cache_dir.glob`, `download_ign_bdtopo_archive`.

**Expected result**

- Direct assertions: `assert not list(cache_dir.glob('*.7z'))`; `assert not list(cache_dir.glob('*.part'))`.
- Expected exception contexts: `with patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(archive_content)), pytest.raises(IgnBdTopoArchiveError, match='checksum|SHA'): download_ign_bdtopo_archive(config, cache_dir)`.

**Regression protected**

- Protects the exact `official checksum mismatch is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `cache_dir.glob`, `download_ign_bdtopo_archive`, `list`, `patch`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unsafe_parent_archive_member_is_rejected`

**Signature**

```python
def test_unsafe_parent_archive_member_is_rejected(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `unsafe parent archive member is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 5 explicit setup/context statement(s).
- Computes `gpkg_path` from `tmp_path / 'unsafe-source.gpkg'`.
- Computes `archive_content` from `_pack_7z(tmp_path / 'unsafe.7z', [(gpkg_path, '../escape.gpkg')])`.
- Computes `config` from `_synthetic_config(source_config)`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(archive_content))` and executes: Computes `download` from `download_ign_bdtopo_archive(config, tmp_path / 'cache')`.
- Enters managed context(s) `pytest.raises(IgnBdTopoArchiveError, match='unsafe|member|path')` and executes: Calls `extract_ign_bdtopo_archive(download, config, extraction_dir=tmp_path / 'extracted')` for its validation or side effect.

**Action**

- Calls `(tmp_path / 'escape.gpkg').exists`, `_pack_7z`, `_response`, `_synthetic_config`, `_write_gpkg`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `tmp_path.glob`.

**Expected result**

- Direct assertions: `assert not (tmp_path / 'escape.gpkg').exists()`; `assert not list(tmp_path.glob('*.part'))`.
- Expected exception contexts: `with pytest.raises(IgnBdTopoArchiveError, match='unsafe|member|path'): extract_ign_bdtopo_archive(download, config, extraction_dir=tmp_path / 'extracted')`.

**Regression protected**

- Protects the exact `unsafe parent archive member is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks; synthetic GeoPackage. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `(tmp_path / 'escape.gpkg').exists`, `_pack_7z`, `_response`, `_synthetic_config`, `_write_gpkg`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `list`, `patch`, `pytest.raises`, `tmp_path.glob`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_geopackage_is_discovered_recursively`

**Signature**

```python
def test_geopackage_is_discovered_recursively(tmp_path: Path) -> None:
```

**Purpose**

Protects the `geopackage is discovered recursively` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 1 explicit setup/context statement(s).
- Computes `gpkg_path` from `tmp_path / 'nested' / 'data' / 'bdtopo.gpkg'`.

**Action**

- Calls `_write_gpkg`, `discover_ign_bdtopo_geopackage`.

**Expected result**

- Direct assertions: `assert discover_ign_bdtopo_geopackage(tmp_path) == gpkg_path`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `geopackage is discovered recursively` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; synthetic GeoPackage. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_write_gpkg`, `discover_ign_bdtopo_geopackage`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_multiple_geopackages_are_rejected_as_ambiguous`

**Signature**

```python
def test_multiple_geopackages_are_rejected_as_ambiguous(tmp_path: Path) -> None:
```

**Purpose**

Protects the `multiple geopackages are rejected as ambiguous` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(IgnBdTopoArchiveError, match='GeoPackage|exactly one|ambiguous')` and executes: Calls `discover_ign_bdtopo_geopackage(tmp_path)` for its validation or side effect.

**Action**

- Calls `_write_gpkg`, `discover_ign_bdtopo_geopackage`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnBdTopoArchiveError, match='GeoPackage|exactly one|ambiguous'): discover_ign_bdtopo_geopackage(tmp_path)`.

**Regression protected**

- Protects the exact `multiple geopackages are rejected as ambiguous` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; synthetic GeoPackage. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_write_gpkg`, `discover_ign_bdtopo_geopackage`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_real_layer_names_are_listed_and_discovered`

**Signature**

```python
def test_real_layer_names_are_listed_and_discovered(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `real layer names are listed and discovered` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 3 explicit setup/context statement(s).
- Computes `gpkg_path` from `tmp_path / 'bdtopo.gpkg'`.
- Computes `all_layers` from `list_ign_bdtopo_layers(gpkg_path)`.
- Computes `selection` from `discover_ign_bdtopo_layers(gpkg_path, source_config)`.

**Action**

- Calls `_write_gpkg`, `discover_ign_bdtopo_layers`.

**Expected result**

- Direct assertions: `assert set(all_layers) == {LINE_LAYER, POST_LAYER}`; `assert selection.electric_lines_layer == LINE_LAYER`; `assert selection.transformation_posts_layer == POST_LAYER`; `assert set(selection.all_layer_names) == {LINE_LAYER, POST_LAYER}`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `real layer names are listed and discovered` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; synthetic GeoPackage. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_write_gpkg`, `discover_ign_bdtopo_layers`, `list_ign_bdtopo_layers`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_electric_line_layer_fails`

**Signature**

```python
def test_missing_electric_line_layer_fails(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `missing electric line layer fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 2 explicit setup/context statement(s).
- Computes `gpkg_path` from `tmp_path / 'posts-only.gpkg'`.
- Enters managed context(s) `pytest.raises(IgnBdTopoLayerError, match='electric|line|Ligne')` and executes: Calls `discover_ign_bdtopo_layers(gpkg_path, source_config)` for its validation or side effect.

**Action**

- Calls `_write_gpkg`, `discover_ign_bdtopo_layers`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnBdTopoLayerError, match='electric|line|Ligne'): discover_ign_bdtopo_layers(gpkg_path, source_config)`.

**Regression protected**

- Protects the exact `missing electric line layer fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; synthetic GeoPackage. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_write_gpkg`, `discover_ign_bdtopo_layers`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_transformation_post_layer_fails`

**Signature**

```python
def test_missing_transformation_post_layer_fails(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `missing transformation post layer fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 2 explicit setup/context statement(s).
- Computes `gpkg_path` from `tmp_path / 'lines-only.gpkg'`.
- Enters managed context(s) `pytest.raises(IgnBdTopoLayerError, match='transformation|post|Poste')` and executes: Calls `discover_ign_bdtopo_layers(gpkg_path, source_config)` for its validation or side effect.

**Action**

- Calls `_write_gpkg`, `discover_ign_bdtopo_layers`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnBdTopoLayerError, match='transformation|post|Poste'): discover_ign_bdtopo_layers(gpkg_path, source_config)`.

**Regression protected**

- Protects the exact `missing transformation post layer fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; synthetic GeoPackage. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_write_gpkg`, `discover_ign_bdtopo_layers`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_ambiguous_electric_line_layers_fail`

**Signature**

```python
def test_ambiguous_electric_line_layers_fail(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `ambiguous electric line layers fail` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 3 explicit setup/context statement(s).
- Computes `gpkg_path` from `tmp_path / 'ambiguous-lines.gpkg'`.
- Computes `secondary_lines` from `gpd.GeoDataFrame({'object_id': ['L_SECONDARY']}, geometry=[LineString([(0, 0), (50, 50)])], crs='EPSG:2154')`.
- Enters managed context(s) `pytest.raises(IgnBdTopoLayerError, match='unambiguous|found 2')` and executes: Calls `discover_ign_bdtopo_layers(gpkg_path, source_config)` for its validation or side effect.

**Action**

- Calls `LineString`, `_write_gpkg`, `discover_ign_bdtopo_layers`, `gpd.GeoDataFrame`, `pyogrio.write_dataframe`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnBdTopoLayerError, match='unambiguous|found 2'): discover_ign_bdtopo_layers(gpkg_path, source_config)`.

**Regression protected**

- Protects the exact `ambiguous electric line layers fail` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; actual in-memory geometry; synthetic GeoPackage. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `_write_gpkg`, `discover_ign_bdtopo_layers`, `gpd.GeoDataFrame`, `pyogrio.write_dataframe`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_synthetic_archive_extracts_and_discovers_required_layers`

**Signature**

```python
def test_synthetic_archive_extracts_and_discovers_required_layers(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `synthetic archive extracts and discovers required layers` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 4 explicit setup/context statement(s).
- Computes `archive_content` from `_synthetic_archive_bytes(tmp_path / 'source')`.
- Computes `config` from `_synthetic_config(source_config)`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(archive_content))` and executes: Computes `download` from `download_ign_bdtopo_archive(config, tmp_path / 'cache')`.
- Computes `extraction` from `extract_ign_bdtopo_archive(download, config, extraction_dir=tmp_path / 'extracted')`.

**Action**

- Calls `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `extraction.geopackage_path.is_file`.

**Expected result**

- Direct assertions: `assert extraction.geopackage_path.is_file()`; `assert extraction.electric_lines_layer == LINE_LAYER`; `assert extraction.transformation_posts_layer == POST_LAYER`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `synthetic archive extracts and discovers required layers` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `extraction.geopackage_path.is_file`, `patch`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_schema_v2_extraction_metadata_binds_physical_geopackage`

**Signature**

```python
def test_schema_v2_extraction_metadata_binds_physical_geopackage(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `schema v2 extraction metadata binds physical geopackage` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 3 explicit setup/context statement(s).
- Computes `(config, download, extraction)` from `_extracted_fixture(tmp_path, source_config)`.
- Computes `metadata` from `json.loads(_extraction_metadata_path(extraction.extraction_path).read_text(encoding='utf-8'))`.
- Computes `cached` from `extract_ign_bdtopo_archive(download, config, extraction_dir=extraction.extraction_path)`.

**Action**

- Calls `_extracted_fixture`, `_extraction_metadata_path`, `_extraction_metadata_path(extraction.extraction_path).read_text`, `extract_ign_bdtopo_archive`, `extraction.geopackage_path.read_bytes`, `extraction.geopackage_path.stat`, `json.loads`, `sha256`, `sha256(extraction.geopackage_path.read_bytes()).hexdigest`.

**Expected result**

- Direct assertions: `assert metadata['schema_version'] == 2`; `assert metadata['geopackage_size_bytes'] == extraction.geopackage_path.stat().st_size`; `assert metadata['geopackage_sha256'] == sha256(extraction.geopackage_path.read_bytes()).hexdigest()`; `assert extraction.geopackage_size_bytes == metadata['geopackage_size_bytes']`; `assert extraction.geopackage_sha256 == metadata['geopackage_sha256']`; `assert cached.cache_hit is True`; `assert cached.geopackage_size_bytes == metadata['geopackage_size_bytes']`; `assert cached.geopackage_sha256 == metadata['geopackage_sha256']`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `schema v2 extraction metadata binds physical geopackage` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_extracted_fixture`, `_extraction_metadata_path`, `_extraction_metadata_path(extraction.extraction_path).read_text`, `extract_ign_bdtopo_archive`, `extraction.geopackage_path.read_bytes`, `extraction.geopackage_path.stat`, `json.loads`, `sha256`, `sha256(extraction.geopackage_path.read_bytes()).hexdigest`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_same_size_geopackage_tamper_invalidates_extraction_cache`

**Signature**

```python
def test_same_size_geopackage_tamper_invalidates_extraction_cache(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `same size geopackage tamper invalidates extraction cache` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 4 explicit setup/context statement(s).
- Computes `(config, download, extraction)` from `_extracted_fixture(tmp_path, source_config)`.
- Computes `original` from `extraction.geopackage_path.read_bytes()`.
- Computes `tampered` from `bytearray(original)`.
- Computes `rebuilt` from `extract_ign_bdtopo_archive(download, config, extraction_dir=extraction.extraction_path)`.

**Action**

- Calls `_extracted_fixture`, `bytearray`, `extract_ign_bdtopo_archive`, `extraction.geopackage_path.read_bytes`, `extraction.geopackage_path.stat`, `extraction.geopackage_path.write_bytes`, `rebuilt.geopackage_path.read_bytes`.

**Expected result**

- Direct assertions: `assert extraction.geopackage_path.stat().st_size == len(original)`; `assert rebuilt.cache_hit is False`; `assert rebuilt.geopackage_path.read_bytes() == original`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `same size geopackage tamper invalidates extraction cache` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_extracted_fixture`, `bytearray`, `extract_ign_bdtopo_archive`, `extraction.geopackage_path.read_bytes`, `extraction.geopackage_path.stat`, `extraction.geopackage_path.write_bytes`, `len`, `rebuilt.geopackage_path.read_bytes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_forged_extraction_metadata_never_returns_cache_hit`

**Signature**

```python
def test_forged_extraction_metadata_never_returns_cache_hit(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    field: str,
    value: object,
) -> None:
```

**Purpose**

Protects the `forged extraction metadata never returns cache hit` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`, `field`, `value`.
- Contains 5 explicit setup/context statement(s).
- Computes `(config, download, extraction)` from `_extracted_fixture(tmp_path, source_config)`.
- Computes `metadata_path` from `_extraction_metadata_path(extraction.extraction_path)`.
- Computes `metadata` from `json.loads(metadata_path.read_text(encoding='utf-8'))`.
- Computes `metadata[field]` from `value`.
- Computes `rebuilt` from `extract_ign_bdtopo_archive(download, config, extraction_dir=extraction.extraction_path)`.

**Action**

- Calls `_extracted_fixture`, `_extraction_metadata_path`, `extract_ign_bdtopo_archive`, `json.dumps`, `json.loads`, `metadata_path.read_text`, `metadata_path.write_text`.

**Expected result**

- Direct assertions: `assert rebuilt.cache_hit is False`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `forged extraction metadata never returns cache hit` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_extracted_fixture`, `_extraction_metadata_path`, `extract_ign_bdtopo_archive`, `json.dumps`, `json.loads`, `metadata_path.read_text`, `metadata_path.write_text`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_geopackage_sha_is_not_trusted`

**Signature**

```python
def test_malformed_geopackage_sha_is_not_trusted(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    value: str,
) -> None:
```

**Purpose**

Protects the `malformed geopackage sha is not trusted` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`, `value`.
- Contains 5 explicit setup/context statement(s).
- Computes `(config, download, extraction)` from `_extracted_fixture(tmp_path, source_config)`.
- Computes `metadata_path` from `_extraction_metadata_path(extraction.extraction_path)`.
- Computes `metadata` from `json.loads(metadata_path.read_text(encoding='utf-8'))`.
- Computes `metadata['geopackage_sha256']` from `value`.
- Computes `rebuilt` from `extract_ign_bdtopo_archive(download, config, extraction_dir=extraction.extraction_path)`.

**Action**

- Calls `_extracted_fixture`, `_extraction_metadata_path`, `extract_ign_bdtopo_archive`, `json.dumps`, `json.loads`, `metadata_path.read_text`, `metadata_path.write_text`.

**Expected result**

- Direct assertions: `assert rebuilt.cache_hit is False`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `malformed geopackage sha is not trusted` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_extracted_fixture`, `_extraction_metadata_path`, `extract_ign_bdtopo_archive`, `json.dumps`, `json.loads`, `metadata_path.read_text`, `metadata_path.write_text`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_geopackage_size_is_not_trusted`

**Signature**

```python
def test_malformed_geopackage_size_is_not_trusted(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    value: object,
) -> None:
```

**Purpose**

Protects the `malformed geopackage size is not trusted` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`, `value`.
- Contains 5 explicit setup/context statement(s).
- Computes `(config, download, extraction)` from `_extracted_fixture(tmp_path, source_config)`.
- Computes `metadata_path` from `_extraction_metadata_path(extraction.extraction_path)`.
- Computes `metadata` from `json.loads(metadata_path.read_text(encoding='utf-8'))`.
- Computes `metadata['geopackage_size_bytes']` from `value`.
- Computes `rebuilt` from `extract_ign_bdtopo_archive(download, config, extraction_dir=extraction.extraction_path)`.

**Action**

- Calls `_extracted_fixture`, `_extraction_metadata_path`, `extract_ign_bdtopo_archive`, `json.dumps`, `json.loads`, `metadata_path.read_text`, `metadata_path.write_text`.

**Expected result**

- Direct assertions: `assert rebuilt.cache_hit is False`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `malformed geopackage size is not trusted` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_extracted_fixture`, `_extraction_metadata_path`, `extract_ign_bdtopo_archive`, `json.dumps`, `json.loads`, `metadata_path.read_text`, `metadata_path.write_text`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_default_extraction_path_is_short_and_content_addressed`

**Signature**

```python
def test_default_extraction_path_is_short_and_content_addressed(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `default extraction path is short and content addressed` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 5 explicit setup/context statement(s).
- Computes `archive_content` from `_synthetic_archive_bytes(tmp_path / 'source')`.
- Computes `config` from `_synthetic_config(source_config)`.
- Computes `cache_dir` from `tmp_path / 'cache'`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(archive_content))` and executes: Computes `download` from `download_ign_bdtopo_archive(config, cache_dir)`.
- Computes `extraction` from `extract_ign_bdtopo_archive(download, config)`.

**Action**

- Calls `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `extraction.geopackage_path.is_file`.

**Expected result**

- Direct assertions: `assert extraction.extraction_path == cache_dir / 'x' / download.sha256[:16]`; `assert len(extraction.extraction_path.name) == 16`; `assert extraction.geopackage_path.is_file()`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `default extraction path is short and content addressed` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `extraction.geopackage_path.is_file`, `len`, `patch`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_layer_loader_retains_crs_counts_and_null_geometries`

**Signature**

```python
def test_layer_loader_retains_crs_counts_and_null_geometries(tmp_path: Path) -> None:
```

**Purpose**

Protects the `layer loader retains crs counts and null geometries` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 4 explicit setup/context statement(s).
- Computes `gpkg_path` from `tmp_path / 'bdtopo.gpkg'`.
- Computes `loaded` from `load_ign_bdtopo_layer(gpkg_path, LINE_LAYER, 'electric_lines')`.
- Computes `frame` from `loaded.data`.
- Computes `summary` from `loaded.summary`.

**Action**

- Calls `_write_gpkg`, `frame.crs.to_epsg`, `frame.geometry.isna`, `frame.geometry.isna().sum`, `frame['object_id'].tolist`, `load_ign_bdtopo_layer`.

**Expected result**

- Direct assertions: `assert frame.crs is not None`; `assert frame.crs.to_epsg() == 2154`; `assert len(frame) == 2`; `assert frame['object_id'].tolist() == ['L_VALID', 'L_NULL']`; `assert frame.geometry.isna().sum() == 1`; `assert summary.feature_count == 2`; `assert summary.null_geometry_count == 1`; `assert summary.invalid_geometry_count == 0`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `layer loader retains crs counts and null geometries` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; actual in-memory geometry; synthetic GeoPackage. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_write_gpkg`, `frame.crs.to_epsg`, `frame.geometry.isna`, `frame.geometry.isna().sum`, `frame['object_id'].tolist`, `len`, `load_ign_bdtopo_layer`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_geometry_is_preserved_without_repair`

**Signature**

```python
def test_invalid_geometry_is_preserved_without_repair(tmp_path: Path) -> None:
```

**Purpose**

Protects the `invalid geometry is preserved without repair` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 5 explicit setup/context statement(s).
- Computes `gpkg_path` from `tmp_path / 'bdtopo.gpkg'`.
- Computes `loaded` from `load_ign_bdtopo_layer(gpkg_path, POST_LAYER, 'transformation_posts')`.
- Computes `frame` from `loaded.data`.
- Computes `summary` from `loaded.summary`.
- Computes `invalid_row` from `frame.loc[frame['object_id'] == 'P_INVALID'].iloc[0]`.

**Action**

- Calls `_write_gpkg`, `load_ign_bdtopo_layer`.

**Expected result**

- Direct assertions: `assert len(frame) == 3`; `assert invalid_row.geometry.is_valid is False`; `assert summary.feature_count == 3`; `assert summary.null_geometry_count == 1`; `assert summary.invalid_geometry_count == 1`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `invalid geometry is preserved without repair` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; synthetic GeoPackage. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_write_gpkg`, `len`, `load_ign_bdtopo_layer`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_geographic_crs_is_rejected`

**Signature**

```python
def test_geographic_crs_is_rejected(tmp_path: Path) -> None:
```

**Purpose**

Protects the `geographic crs is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `gpkg_path` from `tmp_path / 'geographic.gpkg'`.
- Enters managed context(s) `pytest.raises(IgnBdTopoLayerError, match='2154|Lambert|projected|CRS')` and executes: Calls `load_ign_bdtopo_layer(gpkg_path, LINE_LAYER, 'electric_lines')` for its validation or side effect.

**Action**

- Calls `_write_gpkg`, `load_ign_bdtopo_layer`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnBdTopoLayerError, match='2154|Lambert|projected|CRS'): load_ign_bdtopo_layer(gpkg_path, LINE_LAYER, 'electric_lines')`.

**Regression protected**

- Protects the exact `geographic crs is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; synthetic GeoPackage. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_write_gpkg`, `load_ign_bdtopo_layer`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_electricity_loader_retains_both_layer_counts`

**Signature**

```python
def test_electricity_loader_retains_both_layer_counts(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `electricity loader retains both layer counts` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 5 explicit setup/context statement(s).
- Computes `archive_content` from `_synthetic_archive_bytes(tmp_path / 'source', invalid_post=True)`.
- Computes `config` from `_synthetic_config(source_config)`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(archive_content))` and executes: Computes `download` from `download_ign_bdtopo_archive(config, tmp_path / 'cache')`.
- Computes `extraction` from `extract_ign_bdtopo_archive(download, config, extraction_dir=tmp_path / 'extracted')`.
- Computes `electricity` from `load_ign_bdtopo_electricity(extraction, config)`.

**Action**

- Calls `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `download_ign_bdtopo_archive`, `electricity.electric_lines.crs.to_epsg`, `electricity.transformation_posts.crs.to_epsg`, `extract_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`.

**Expected result**

- Direct assertions: `assert len(electricity.electric_lines) == 2`; `assert len(electricity.transformation_posts) == 3`; `assert electricity.electric_lines.crs.to_epsg() == 2154`; `assert electricity.transformation_posts.crs.to_epsg() == 2154`; `assert electricity.transformation_posts_summary.invalid_geometry_count == 1`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `electricity loader retains both layer counts` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `download_ign_bdtopo_archive`, `electricity.electric_lines.crs.to_epsg`, `electricity.transformation_posts.crs.to_epsg`, `extract_ign_bdtopo_archive`, `len`, `load_ign_bdtopo_electricity`, `patch`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_road_layer_discovery_loads_selected_physical_layer`

**Signature**

```python
def test_road_layer_discovery_loads_selected_physical_layer(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `road layer discovery loads selected physical layer` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 5 explicit setup/context statement(s).
- Computes `archive_content` from `_synthetic_archive_bytes(tmp_path / 'source', include_roads=True)`.
- Computes `config` from `_synthetic_config(source_config)`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(archive_content))` and executes: Computes `download` from `download_ign_bdtopo_archive(config, tmp_path / 'cache')`.
- Computes `extraction` from `extract_ign_bdtopo_archive(download, config, extraction_dir=tmp_path / 'extracted')`.
- Computes `loaded` from `ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)`.

**Action**

- Calls `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `ign_bdtopo_fr.load_ign_bdtopo_roads`, `loaded.road_segments['object_id'].tolist`.

**Expected result**

- Direct assertions: `assert loaded.extraction is extraction`; `assert loaded.road_segments_summary.source_layer_name == ROAD_LAYER`; `assert loaded.road_segments_summary.logical_name == 'road_segments'`; `assert loaded.road_segments['object_id'].tolist() == ['R_LINE', 'R_MULTI']`; `assert loaded.road_segments_summary.spatial_role == 'PROXY_GEOMETRY'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `road layer discovery loads selected physical layer` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `ign_bdtopo_fr.load_ign_bdtopo_roads`, `loaded.road_segments['object_id'].tolist`, `patch`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_road_physical_layer_cannot_collide_with_electricity_roles`

**Signature**

```python
def test_road_physical_layer_cannot_collide_with_electricity_roles(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    role: str,
) -> None:
```

**Purpose**

Protects the `road physical layer cannot collide with electricity roles` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`, `role`.
- Contains 6 explicit setup/context statement(s).
- Computes `(config, _, extraction)` from `_extracted_fixture(tmp_path, source_config, include_roads=True)`.
- Computes `content` from `config.model_dump(mode='json')`.
- Computes `selected` from `content['logical_layers'][role]`.
- Computes `content['access']['road_segments']` from `selected`.
- Computes `colliding` from `IgnBdTopoSourceConfig.model_validate(content)`.
- Enters managed context(s) `pytest.raises(IgnBdTopoLayerError, match='same layer|collid|role')` and executes: Calls `ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, colliding)` for its validation or side effect.

**Action**

- Calls `IgnBdTopoSourceConfig.model_validate`, `_extracted_fixture`, `config.model_dump`, `ign_bdtopo_fr.load_ign_bdtopo_roads`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnBdTopoLayerError, match='same layer|collid|role'): ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, colliding)`.

**Regression protected**

- Protects the exact `road physical layer cannot collide with electricity roles` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `IgnBdTopoSourceConfig.model_validate`, `_extracted_fixture`, `config.model_dump`, `ign_bdtopo_fr.load_ign_bdtopo_roads`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_road_layer_fails_safely`

**Signature**

```python
def test_missing_road_layer_fails_safely(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `missing road layer fails safely` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 5 explicit setup/context statement(s).
- Computes `archive_content` from `_synthetic_archive_bytes(tmp_path / 'source')`.
- Computes `config` from `_synthetic_config(source_config)`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(archive_content))` and executes: Computes `download` from `download_ign_bdtopo_archive(config, tmp_path / 'cache')`.
- Computes `extraction` from `extract_ign_bdtopo_archive(download, config, extraction_dir=tmp_path / 'extracted')`.
- Enters managed context(s) `pytest.raises(IgnBdTopoLayerError, match='road|route|found 0')` and executes: Calls `ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)` for its validation or side effect.

**Action**

- Calls `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `ign_bdtopo_fr.load_ign_bdtopo_roads`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnBdTopoLayerError, match='road|route|found 0'): ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)`.

**Regression protected**

- Protects the exact `missing road layer fails safely` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `ign_bdtopo_fr.load_ign_bdtopo_roads`, `patch`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_ambiguous_road_layer_fails_safely`

**Signature**

```python
def test_ambiguous_road_layer_fails_safely(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `ambiguous road layer fails safely` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 7 explicit setup/context statement(s).
- Computes `gpkg_path` from `tmp_path / 'source' / 'ambiguous-roads.gpkg'`.
- Computes `secondary` from `gpd.GeoDataFrame({'object_id': ['R_SECONDARY']}, geometry=[LineString([(0, 0), (10, 10)])], crs='EPSG:2154')`.
- Computes `archive_content` from `_pack_7z(tmp_path / 'ambiguous-roads.7z', [(gpkg_path, 'PACKAGE/ambiguous-roads.gpkg')])`.
- Computes `config` from `_synthetic_config(source_config)`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(archive_content))` and executes: Computes `download` from `download_ign_bdtopo_archive(config, tmp_path / 'cache')`.
- Computes `extraction` from `extract_ign_bdtopo_archive(download, config, extraction_dir=tmp_path / 'extracted')`.
- Enters managed context(s) `pytest.raises(IgnBdTopoLayerError, match='road|route|found 2')` and executes: Calls `ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)` for its validation or side effect.

**Action**

- Calls `LineString`, `_pack_7z`, `_response`, `_synthetic_config`, `_write_gpkg`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `gpd.GeoDataFrame`, `ign_bdtopo_fr.load_ign_bdtopo_roads`, `pyogrio.write_dataframe`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnBdTopoLayerError, match='road|route|found 2'): ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)`.

**Regression protected**

- Protects the exact `ambiguous road layer fails safely` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks; actual in-memory geometry; synthetic GeoPackage. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `_pack_7z`, `_response`, `_synthetic_config`, `_write_gpkg`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `gpd.GeoDataFrame`, `ign_bdtopo_fr.load_ign_bdtopo_roads`, `patch`, `pyogrio.write_dataframe`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_road_loader_rejects_wrong_archive_config_department`

**Signature**

```python
def test_road_loader_rejects_wrong_archive_config_department(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `road loader rejects wrong archive config department` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 6 explicit setup/context statement(s).
- Computes `archive_content` from `_synthetic_archive_bytes(tmp_path / 'source', include_roads=True)`.
- Computes `config` from `_synthetic_config(source_config)`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(archive_content))` and executes: Computes `download` from `download_ign_bdtopo_archive(config, tmp_path / 'cache')`.
- Computes `extraction` from `extract_ign_bdtopo_archive(download, config, extraction_dir=tmp_path / 'extracted')`.
- Computes `other_department` from `IgnBdTopoSourceConfig.model_validate({**config.model_dump(mode='json'), 'department_code': '32'})`.
- Enters managed context(s) `pytest.raises(IgnBdTopoLayerError, match='department|archive|lineage')` and executes: Calls `ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, other_department)` for its validation or side effect.

**Action**

- Calls `IgnBdTopoSourceConfig.model_validate`, `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `config.model_dump`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `ign_bdtopo_fr.load_ign_bdtopo_roads`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnBdTopoLayerError, match='department|archive|lineage'): ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, other_department)`.

**Regression protected**

- Protects the exact `road loader rejects wrong archive config department` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `IgnBdTopoSourceConfig.model_validate`, `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `config.model_dump`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `ign_bdtopo_fr.load_ign_bdtopo_roads`, `patch`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_road_loader_rejects_changed_layer_inventory`

**Signature**

```python
def test_road_loader_rejects_changed_layer_inventory(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `road loader rejects changed layer inventory` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 6 explicit setup/context statement(s).
- Computes `archive_content` from `_synthetic_archive_bytes(tmp_path / 'source', include_roads=True)`.
- Computes `config` from `_synthetic_config(source_config)`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(archive_content))` and executes: Computes `download` from `download_ign_bdtopo_archive(config, tmp_path / 'cache')`.
- Computes `extraction` from `extract_ign_bdtopo_archive(download, config, extraction_dir=tmp_path / 'extracted')`.
- Computes `added` from `gpd.GeoDataFrame({'object_id': ['ADDED']}, geometry=[LineString([(0, 0), (1, 1)])], crs='EPSG:2154')`.
- Enters managed context(s) `pytest.raises(IgnBdTopoLayerError, match='inventory|changed')` and executes: Calls `ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)` for its validation or side effect.

**Action**

- Calls `LineString`, `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `gpd.GeoDataFrame`, `ign_bdtopo_fr.load_ign_bdtopo_roads`, `pyogrio.write_dataframe`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnBdTopoLayerError, match='inventory|changed'): ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)`.

**Regression protected**

- Protects the exact `road loader rejects changed layer inventory` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks; actual in-memory geometry; synthetic GeoPackage. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `gpd.GeoDataFrame`, `ign_bdtopo_fr.load_ign_bdtopo_roads`, `patch`, `pyogrio.write_dataframe`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_road_loader_rejects_geographic_crs`

**Signature**

```python
def test_road_loader_rejects_geographic_crs(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `road loader rejects geographic crs` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 5 explicit setup/context statement(s).
- Computes `archive_content` from `_synthetic_archive_bytes(tmp_path / 'source', include_roads=True, road_crs='EPSG:4326')`.
- Computes `config` from `_synthetic_config(source_config)`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(archive_content))` and executes: Computes `download` from `download_ign_bdtopo_archive(config, tmp_path / 'cache')`.
- Computes `extraction` from `extract_ign_bdtopo_archive(download, config, extraction_dir=tmp_path / 'extracted')`.
- Enters managed context(s) `pytest.raises(IgnBdTopoLayerError, match='2154|Lambert|projected|CRS')` and executes: Calls `ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)` for its validation or side effect.

**Action**

- Calls `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `ign_bdtopo_fr.load_ign_bdtopo_roads`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnBdTopoLayerError, match='2154|Lambert|projected|CRS'): ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)`.

**Regression protected**

- Protects the exact `road loader rejects geographic crs` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `ign_bdtopo_fr.load_ign_bdtopo_roads`, `patch`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_road_loader_preserves_lambert93_lines_unchanged`

**Signature**

```python
def test_road_loader_preserves_lambert93_lines_unchanged(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    road_geometry_kind: str,
    expected_geometry_type: str,
) -> None:
```

**Purpose**

Protects the `road loader preserves lambert93 lines unchanged` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`, `road_geometry_kind`, `expected_geometry_type`.
- Contains 6 explicit setup/context statement(s).
- Computes `archive_content` from `_synthetic_archive_bytes(tmp_path / 'source', include_roads=True, road_geometry_kind=road_geometry_kind)`.
- Computes `config` from `_synthetic_config(source_config)`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(archive_content))` and executes: Computes `download` from `download_ign_bdtopo_archive(config, tmp_path / 'cache')`.
- Computes `extraction` from `extract_ign_bdtopo_archive(download, config, extraction_dir=tmp_path / 'extracted')`.
- Computes `expected` from `gpd.read_file(extraction.geopackage_path, layer=ROAD_LAYER, engine='pyogrio')`.
- Computes `loaded` from `ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)`.

**Action**

- Calls `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `gpd.read_file`, `ign_bdtopo_fr.load_ign_bdtopo_roads`, `loaded.road_segments.crs.to_epsg`.

**Expected result**

- Direct assertions: `assert loaded.road_segments.crs.to_epsg() == 2154`; `assert loaded.road_segments_summary.geometry_types == (expected_geometry_type,)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `road loader preserves lambert93 lines unchanged` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks; actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `assert_geodataframe_equal`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `gpd.read_file`, `ign_bdtopo_fr.load_ign_bdtopo_roads`, `loaded.road_segments.crs.to_epsg`, `patch`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_road_layer_does_not_change_electricity_loading_or_cache_shape`

**Signature**

```python
def test_road_layer_does_not_change_electricity_loading_or_cache_shape(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `road layer does not change electricity loading or cache shape` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 6 explicit setup/context statement(s).
- Computes `archive_content` from `_synthetic_archive_bytes(tmp_path / 'source', include_roads=True)`.
- Computes `config` from `_synthetic_config(source_config)`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(archive_content))` and executes: Computes `download` from `download_ign_bdtopo_archive(config, tmp_path / 'cache')`.
- Computes `extraction` from `extract_ign_bdtopo_archive(download, config, extraction_dir=tmp_path / 'extracted')`.
- Computes `electricity` from `load_ign_bdtopo_electricity(extraction, config)`.
- Computes `metadata` from `json.loads((extraction.extraction_path / '.landscout-extraction.json').read_text(encoding='utf-8'))`.

**Action**

- Calls `(extraction.extraction_path / '.landscout-extraction.json').read_text`, `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `json.loads`, `load_ign_bdtopo_electricity`.

**Expected result**

- Direct assertions: `assert len(electricity.electric_lines) == 2`; `assert len(electricity.transformation_posts) == 2`; `assert electricity.electric_lines_summary.source_layer_name == LINE_LAYER`; `assert electricity.transformation_posts_summary.source_layer_name == POST_LAYER`; `assert 'road_segments_layer' not in metadata`; `assert set(metadata) == {'schema_version', 'archive_sha256', 'geopackage_relative_path', 'geopackage_size_bytes', 'geopackage_sha256', 'all_layer_names', 'electric_lines_layer', 'transformation_posts_layer', 'spatial_role'}`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `road layer does not change electricity loading or cache shape` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `(extraction.extraction_path / '.landscout-extraction.json').read_text`, `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `json.loads`, `len`, `load_ign_bdtopo_electricity`, `patch`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_sources_export_only_stable_road_api`

**Signature**

```python
def test_public_sources_export_only_stable_road_api() -> None:
```

**Purpose**

Protects the `public sources export only stable road api` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `hasattr`.

**Expected result**

- Direct assertions: `assert sources.IgnBdTopoRoadData is ign_bdtopo_fr.IgnBdTopoRoadData`; `assert sources.load_ign_bdtopo_roads is ign_bdtopo_fr.load_ign_bdtopo_roads`; `assert 'IgnBdTopoRoadData' in sources.__all__`; `assert 'load_ign_bdtopo_roads' in sources.__all__`; `assert not hasattr(sources, '_discover_road_layer')`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `public sources export only stable road api` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `hasattr`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_department_coverage_loader_selects_configured_identity`

**Signature**

```python
def test_department_coverage_loader_selects_configured_identity(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `department coverage loader selects configured identity` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 5 explicit setup/context statement(s).
- Computes `archive_content` from `_synthetic_archive_bytes(tmp_path / 'source', include_department=True)`.
- Computes `config` from `_synthetic_config(source_config)`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(archive_content))` and executes: Computes `download` from `download_ign_bdtopo_archive(config, tmp_path / 'cache')`.
- Computes `extraction` from `extract_ign_bdtopo_archive(download, config, extraction_dir=tmp_path / 'extracted')`.
- Computes `loaded` from `load_ign_bdtopo_department_coverage(extraction, config)`.

**Action**

- Calls `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `load_ign_bdtopo_department_coverage`, `loaded.coverage.crs.to_epsg`.

**Expected result**

- Direct assertions: `assert loaded.source_layer == DEPARTMENT_LAYER`; `assert loaded.source_department_code == '31'`; `assert loaded.spatial_role == 'SOURCE_COVERAGE_BOUNDARY'`; `assert len(loaded.coverage) == 1`; `assert loaded.coverage.loc[0, 'code_insee'] == '31'`; `assert loaded.coverage.loc[0, 'source_department_code'] == '31'`; `assert loaded.coverage.loc[0, 'source_archive_sha256'] == download.sha256`; `assert loaded.coverage.loc[0, 'spatial_role'] == 'SOURCE_COVERAGE_BOUNDARY'`; `assert loaded.coverage.crs.to_epsg() == 2154`; `assert loaded.summary.source_feature_count == 2`; `assert loaded.summary.selected_feature_count == 1`; `assert loaded.summary.department_code_field == 'code_insee'`; `assert loaded.summary.geometry_types == ('MultiPolygon',)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `department coverage loader selects configured identity` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `len`, `load_ign_bdtopo_department_coverage`, `loaded.coverage.crs.to_epsg`, `patch`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_department_coverage_requires_one_authoritative_feature`

**Signature**

```python
def test_department_coverage_requires_one_authoritative_feature(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    department_codes: list[str],
) -> None:
```

**Purpose**

Protects the `department coverage requires one authoritative feature` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`, `department_codes`.
- Contains 7 explicit setup/context statement(s).
- Computes `gpkg_path` from `tmp_path / 'source' / 'coverage.gpkg'`.
- Computes `geometries` from `[Polygon([(0, 0), (0, 100), (100, 100), (100, 0), (0, 0)]) for _ in department_codes]`.
- Computes `archive_content` from `_pack_7z(tmp_path / 'coverage.7z', [(gpkg_path, 'PACKAGE/coverage.gpkg')])`.
- Computes `config` from `_synthetic_config(source_config)`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(archive_content))` and executes: Computes `download` from `download_ign_bdtopo_archive(config, tmp_path / 'cache')`.
- Computes `extraction` from `extract_ign_bdtopo_archive(download, config, extraction_dir=tmp_path / 'extracted')`.
- Enters managed context(s) `pytest.raises(IgnBdTopoLayerError, match='exactly one|found')` and executes: Calls `load_ign_bdtopo_department_coverage(extraction, config)` for its validation or side effect.

**Action**

- Calls `Polygon`, `_pack_7z`, `_response`, `_synthetic_config`, `_write_gpkg`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `load_ign_bdtopo_department_coverage`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnBdTopoLayerError, match='exactly one|found'): load_ign_bdtopo_department_coverage(extraction, config)`.

**Regression protected**

- Protects the exact `department coverage requires one authoritative feature` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks; actual in-memory geometry; synthetic GeoPackage. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `_pack_7z`, `_response`, `_synthetic_config`, `_write_gpkg`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `load_ign_bdtopo_department_coverage`, `patch`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_department_coverage_requires_configured_identity_field`

**Signature**

```python
def test_department_coverage_requires_configured_identity_field(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `department coverage requires configured identity field` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 7 explicit setup/context statement(s).
- Computes `archive_content` from `_synthetic_archive_bytes(tmp_path / 'source', include_department=True)`.
- Computes `content` from `_synthetic_config(source_config).model_dump(mode='json')`.
- Computes `content['coverage']['department_layer']['department_code_field']` from `'missing_code'`.
- Computes `config` from `IgnBdTopoSourceConfig.model_validate(content)`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(archive_content))` and executes: Computes `download` from `download_ign_bdtopo_archive(config, tmp_path / 'cache')`.
- Computes `extraction` from `extract_ign_bdtopo_archive(download, config, extraction_dir=tmp_path / 'extracted')`.
- Enters managed context(s) `pytest.raises(IgnBdTopoLayerError, match='identity field|missing_code')` and executes: Calls `load_ign_bdtopo_department_coverage(extraction, config)` for its validation or side effect.

**Action**

- Calls `IgnBdTopoSourceConfig.model_validate`, `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `_synthetic_config(source_config).model_dump`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `load_ign_bdtopo_department_coverage`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnBdTopoLayerError, match='identity field|missing_code'): load_ign_bdtopo_department_coverage(extraction, config)`.

**Regression protected**

- Protects the exact `department coverage requires configured identity field` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `IgnBdTopoSourceConfig.model_validate`, `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `_synthetic_config(source_config).model_dump`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `load_ign_bdtopo_department_coverage`, `patch`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_department_coverage_layer_fails`

**Signature**

```python
def test_missing_department_coverage_layer_fails(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `missing department coverage layer fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 5 explicit setup/context statement(s).
- Computes `archive_content` from `_synthetic_archive_bytes(tmp_path / 'source')`.
- Computes `config` from `_synthetic_config(source_config)`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(archive_content))` and executes: Computes `download` from `download_ign_bdtopo_archive(config, tmp_path / 'cache')`.
- Computes `extraction` from `extract_ign_bdtopo_archive(download, config, extraction_dir=tmp_path / 'extracted')`.
- Enters managed context(s) `pytest.raises(IgnBdTopoLayerError, match='department|found 0')` and executes: Calls `load_ign_bdtopo_department_coverage(extraction, config)` for its validation or side effect.

**Action**

- Calls `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `load_ign_bdtopo_department_coverage`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnBdTopoLayerError, match='department|found 0'): load_ign_bdtopo_department_coverage(extraction, config)`.

**Regression protected**

- Protects the exact `missing department coverage layer fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_response`, `_synthetic_archive_bytes`, `_synthetic_config`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `load_ign_bdtopo_department_coverage`, `patch`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_department_coverage_layer_discovery_must_be_unambiguous`

**Signature**

```python
def test_department_coverage_layer_discovery_must_be_unambiguous(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
```

**Purpose**

Protects the `department coverage layer discovery must be unambiguous` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 7 explicit setup/context statement(s).
- Computes `gpkg_path` from `tmp_path / 'source' / 'ambiguous.gpkg'`.
- Computes `second` from `gpd.GeoDataFrame({'code_insee': ['31']}, geometry=[Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])], crs='EPSG:2154')`.
- Computes `archive_content` from `_pack_7z(tmp_path / 'ambiguous.7z', [(gpkg_path, 'PACKAGE/ambiguous.gpkg')])`.
- Computes `config` from `_synthetic_config(source_config)`.
- Enters managed context(s) `patch('landscout.sources.ign_bdtopo_fr.open_safe_https', return_value=_response(archive_content))` and executes: Computes `download` from `download_ign_bdtopo_archive(config, tmp_path / 'cache')`.
- Computes `extraction` from `extract_ign_bdtopo_archive(download, config, extraction_dir=tmp_path / 'extracted')`.
- Enters managed context(s) `pytest.raises(IgnBdTopoLayerError, match='unambiguous|found 2')` and executes: Calls `load_ign_bdtopo_department_coverage(extraction, config)` for its validation or side effect.

**Action**

- Calls `Polygon`, `_pack_7z`, `_response`, `_synthetic_config`, `_write_gpkg`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `gpd.GeoDataFrame`, `load_ign_bdtopo_department_coverage`, `pyogrio.write_dataframe`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnBdTopoLayerError, match='unambiguous|found 2'): load_ign_bdtopo_department_coverage(extraction, config)`.

**Regression protected**

- Protects the exact `department coverage layer discovery must be unambiguous` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks; actual in-memory geometry; synthetic GeoPackage. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `_pack_7z`, `_response`, `_synthetic_config`, `_write_gpkg`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `gpd.GeoDataFrame`, `load_ign_bdtopo_department_coverage`, `patch`, `pyogrio.write_dataframe`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_direct_consumers_reject_same_inventory_content_tampering`

**Signature**

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

**Purpose**

Protects the `direct consumers reject same inventory content tampering` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`, `consumer`, `layer`, `old_bytes`, `new_bytes`.
- Contains 4 explicit setup/context statement(s).
- Computes `(config, _, extraction)` from `_extracted_fixture(tmp_path, source_config, include_roads=True)`.
- Computes `size_before` from `extraction.geopackage_path.stat().st_size`.
- Computes `content` from `extraction.geopackage_path.read_bytes()`.
- Enters managed context(s) `pytest.raises(IgnBdTopoLayerError, match='integrity|SHA|physical|changed')` and executes: Checks `consumer == 'electricity'`. When true: Calls `load_ign_bdtopo_electricity(extraction, config)` for its validation or side effect. Otherwise: Checks `consumer == 'roads'`. When true: Calls `ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)` for its validation or side effect. Otherwise: Calls `load_ign_bdtopo_department_coverage(extraction, config)` for its validation or side effect.

**Action**

- Calls `_extracted_fixture`, `_response`, `_synthetic_archive_bytes`, `content.replace`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `extraction.geopackage_path.read_bytes`, `extraction.geopackage_path.stat`, `extraction.geopackage_path.write_bytes`, `ign_bdtopo_fr.load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage`, `load_ign_bdtopo_electricity`.

**Expected result**

- Direct assertions: `assert old_bytes in content`; `assert extraction.geopackage_path.stat().st_size == size_before`.
- Expected exception contexts: `with pytest.raises(IgnBdTopoLayerError, match='integrity|SHA|physical|changed'): if consumer == 'electricity': load_ign_bdtopo_electricity(extraction, config) elif consumer == 'roads': ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config) else: load_ign_bdtopo_department_coverage(extraction, config)`.

**Regression protected**

- Protects the exact `direct consumers reject same inventory content tampering` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_extracted_fixture`, `_response`, `_synthetic_archive_bytes`, `content.replace`, `download_ign_bdtopo_archive`, `extract_ign_bdtopo_archive`, `extraction.geopackage_path.read_bytes`, `extraction.geopackage_path.stat`, `extraction.geopackage_path.write_bytes`, `ign_bdtopo_fr.load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage`, `load_ign_bdtopo_electricity`, `patch`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_road_loader_rejects_source_change_after_physical_read`

**Signature**

```python
def test_road_loader_rejects_source_change_after_physical_read(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
) -> None:
```

**Purpose**

Protects the `road loader rejects source change after physical read` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `source_config`.
- Contains 3 explicit setup/context statement(s).
- Computes `(config, _, extraction)` from `_extracted_fixture(tmp_path, source_config, include_roads=True)`.
- Computes `original_read` from `ign_bdtopo_fr.gpd.read_file`.
- Enters managed context(s) `patch.object(ign_bdtopo_fr.gpd, 'read_file', side_effect=mutate_after_read), pytest.raises(IgnBdTopoLayerError, match='changed|integrity|SHA')` and executes: Calls `ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)` for its validation or side effect.

**Action**

- Calls `_extracted_fixture`, `content.replace`, `extraction.geopackage_path.read_bytes`, `extraction.geopackage_path.write_bytes`, `ign_bdtopo_fr.load_ign_bdtopo_roads`, `original_read`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with patch.object(ign_bdtopo_fr.gpd, 'read_file', side_effect=mutate_after_read), pytest.raises(IgnBdTopoLayerError, match='changed|integrity|SHA'): ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)`.

**Regression protected**

- Protects the exact `road loader rejects source change after physical read` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_extracted_fixture`, `content.replace`, `extraction.geopackage_path.read_bytes`, `extraction.geopackage_path.write_bytes`, `ign_bdtopo_fr.load_ign_bdtopo_roads`, `original_read`, `patch.object`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `access` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `code_insee` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `coverage` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `department_code_field` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `department_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `download_timestamp` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `geopackage_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `geopackage_size_bytes` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `invented` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `logical_layers` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `match_tokens` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `nature` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `nom_officiel` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `object_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `official_checksum` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_segments` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `schema_version` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `sha256` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `source_department_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_url` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `spatial_role` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `tension` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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

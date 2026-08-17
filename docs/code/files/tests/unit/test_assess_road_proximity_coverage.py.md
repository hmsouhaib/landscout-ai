# `tests/unit/test_assess_road_proximity_coverage.py`

## File identity

- Repository path: `tests/unit/test_assess_road_proximity_coverage.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `assess_road_proximity_coverage` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `aa04754f7dc742918b0efd586c6c3011ea3a3df7b8bd888a5b804931d84951fa`

## 1. Purpose

Provides complete unit and regression coverage for the `assess_road_proximity_coverage` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `from copy import deepcopy` — required by the implementation paths and symbols documented below.
- `from dataclasses import FrozenInstanceError, replace` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.
- `from typing import Any, cast` — required by the implementation paths and symbols documented below.

### Third-party

- `from importlib import import_module` — required by the implementation paths and symbols documented below.
- `from unittest.mock import patch` — required by the implementation paths and symbols documented below.
- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import numpy as np` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `import pytest` — required by the implementation paths and symbols documented below.
- `from geopandas.testing import assert_geodataframe_equal` — required by the implementation paths and symbols documented below.
- `from pandas.testing import assert_frame_equal` — required by the implementation paths and symbols documented below.
- `from shapely.geometry import LineString, MultiPolygon, Point, Polygon` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout import stages` — required by the implementation paths and symbols documented below.
- `from landscout.sources.ign_bdtopo_fr import ( IgnBdTopoCoverageLayerSummary, IgnBdTopoDepartmentCoverage, IgnBdTopoDownload, IgnBdTopoExtraction, IgnBdTopoLayerSummary, IgnBdTopoRoadData, IgnBdTopoSourceConfig, load_ign_bdtopo_source_config, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.assess_road_proximity_coverage import ( RoadProximityCoverageAssessmentResult, RoadProximityCoverageError, assess_road_proximity_coverage, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.enrich_road_proximity import ( CLASS_PROXIMITY_COLUMNS, ParcelRoadProximityResult, RoadProxyClassCoverage, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.road_vehicle_proxy_policy import ( load_ign_road_vehicle_proxy_policy, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `SOURCE_CONFIG` | `load_ign_bdtopo_source_config()` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ARCHIVE_SHA256` | `"a" * 64` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `GEOPACKAGE_SHA256` | `"b" * 64` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `EDITION` | `"2026-06-15"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ELIGIBLE_CLASSES` | `( "GENERAL_VEHICLE_PROXY", "LIMITED_VEHICLE_PROXY", "RESTRICTED_REVIEW", "NOT_GENERAL_VEHICLE_PROXY", "UNKNOWN_REVIEW", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ALL_CLASSES` | `( "GENERAL_VEHICLE_PROXY", "LIMITED_VEHICLE_PROXY", "RESTRICTED_REVIEW", "NOT_GENERAL_VEHICLE_PROXY", "NOT_DISTANCE_PROXY", "UNKNOWN_REVIEW", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `DIAGNOSTIC_COLUMNS` | `( "road_source_boundary_distance_m", "road_source_coverage_position", "road_proximity_coverage_status", "road_source_coverage_provider", "road_source_coverage_product", "road_source_coverage_department_code", "road_source_coverage_edition", "road_source_coverage_product_version", "road_source_coverage_archive_sha256", "road_source_coverage_layer", "road_source_coverage_spatial_role", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SELECTED_COLUMNS` | `( "nearest_road_proxy_distance_m", "nearest_road_feature_id", "nearest_source_feature_id", "nearest_road_tie_count", "nearest_road_primary_rule", "nearest_road_rule_trace_json", "nearest_road_unknown_fields_json", "nearest_road_toll_evidence", "nearest_nature_raw", "nearest_importance_raw", "nearest_asset_status_raw", "nearest_private_raw", "nearest_light_vehicle_access_raw", "nearest_carriageway_width_raw", "nearest_closure_period_raw", "nearest_restriction_nature_raw", "nearest_source_layer", "nearest_source_department_code", "nearest_source_edition", "nearest_source_archive_sha256", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `_archive`

**Signature**

```python
def _archive() -> IgnBdTopoDownload:
```

**Purpose**

Implements archive according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `IgnBdTopoDownload`. Observed return expression(s): `IgnBdTopoDownload(provider=SOURCE_CONFIG.provider, product=SOURCE_CONFIG.product, department_code='31', edition=EDITION, product_version='3.5', projection='EPSG:2154', package_format='GPKG', archive_format='7z', source_url=str(SOURCE_CONFIG.source_url), checksum_url=None, download_timestamp='2026-08-11T15:32:03+00:00', filename='BDTOPO.7z', file_size=123, sha256=ARCHIVE_SHA256, official_checksum_…`.

**Algorithm**

1. Returns `IgnBdTopoDownload(provider=SOURCE_CONFIG.provider, product=SOURCE_CONFIG.product, department_code='31', edition=EDITION, product_version='3.5', projection='EPSG:2154', package_format='GPKG', archive_format='7z', source_url=str(SOURCE_CONFIG.source_url), checksum_url=None, download_timestamp='2026-08-11T15:32:03+00:00', filename='BDTOPO.7z', file_size=123, s…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `IgnBdTopoDownload`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnBdTopoDownload`, `Path`, `str`.

**Known repository callers**

- `tests/unit/test_assess_road_proximity_coverage.py` — `_extraction`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_extraction`

**Signature**

```python
def _extraction() -> IgnBdTopoExtraction:
```

**Purpose**

Implements extraction according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `IgnBdTopoExtraction`. Observed return expression(s): `IgnBdTopoExtraction(archive=_archive(), extraction_path=Path('synthetic/extracted'), geopackage_path=Path('synthetic/extracted/data.gpkg'), geopackage_filename='data.gpkg', geopackage_size_bytes=456, geopackage_sha256=GEOPACKAGE_SHA256, all_layer_names=('ligne_electrique', 'poste_de_transformation', 'troncon_de_route', 'departement', 'zone_administrative'), electric_lines_layer='ligne_electrique'…`.

**Algorithm**

1. Returns `IgnBdTopoExtraction(archive=_archive(), extraction_path=Path('synthetic/extracted'), geopackage_path=Path('synthetic/extracted/data.gpkg'), geopackage_filename='data.gpkg', geopackage_size_bytes=456, geopackage_sha256=GEOPACKAGE_SHA256, all_layer_names=('ligne_electrique', 'poste_de_transformation', 'troncon_de_route', 'departement', 'zone_administrative'),…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnBdTopoExtraction`, `Path`, `_archive`.

**Known repository callers**

- `tests/unit/test_assess_road_proximity_coverage.py` — `_coverage`
- `tests/unit/test_assess_road_proximity_coverage.py` — `_road_source`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_road_source`

**Signature**

```python
def _road_source(
    extraction: IgnBdTopoExtraction | None = None,
) -> IgnBdTopoRoadData:
```

**Purpose**

Implements road source according to the exact implementation and guards in this file.

**Inputs**

- `extraction` (`IgnBdTopoExtraction | None`; optional/default `None`) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoRoadData`. Observed return expression(s): `IgnBdTopoRoadData(package, roads, summary)`.

**Algorithm**

1. Computes `package` from `extraction or _extraction()`.
2. Computes `roads` from `gpd.GeoDataFrame({'cleabs': ['ROAD-1']}, geometry=[LineString([(0, 0), (1, 1)])], crs='EPSG:2154')`.
3. Computes `summary` from `IgnBdTopoLayerSummary(logical_name='road_segments', source_layer_name='troncon_de_route', crs='EPSG:2154', feature_count=1, columns=tuple((str(column) for column in roads.columns)), dtypes=tuple(((str(column), str(dtype)) for column, dtype in roads.dtypes.items())), null_geometry_count=0, empty_geometry_count=0, inval…`.
4. Returns `IgnBdTopoRoadData(package, roads, summary)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnBdTopoLayerSummary`, `IgnBdTopoRoadData`, `LineString`, `_extraction`, `gpd.GeoDataFrame`, `roads.dtypes.items`, `str`, `tuple`.

**Known repository callers**

- `tests/unit/test_assess_road_proximity_coverage.py` — `_assess`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_configured_coverage_layer_cannot_be_replaced_by_real_alternate_layer`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_coverage_loader_failure_is_controlled`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_coverage_must_retain_same_extraction_object`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_coverage_package_lineage_must_match_road_archive`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_coverage_spatial_role_and_source_type_are_controlled`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_malformed_upstream_result_fails_before_coverage_load`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_proximity_failure_stops_coverage_loading`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_result_preserves_every_upstream_fact_and_input_object`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_source_chain_calls_proximity_then_coverage_exactly_once`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_wrong_public_input_type_is_controlled_and_fast`

**Tests**

- `tests/unit/test_assess_road_proximity_coverage.py::test_configured_coverage_layer_cannot_be_replaced_by_real_alternate_layer`
- `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_loader_failure_is_controlled`
- `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_must_retain_same_extraction_object`
- `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_package_lineage_must_match_road_archive`
- `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_spatial_role_and_source_type_are_controlled`
- `tests/unit/test_assess_road_proximity_coverage.py::test_malformed_upstream_result_fails_before_coverage_load`
- `tests/unit/test_assess_road_proximity_coverage.py::test_proximity_failure_stops_coverage_loading`
- `tests/unit/test_assess_road_proximity_coverage.py::test_result_preserves_every_upstream_fact_and_input_object`
- `tests/unit/test_assess_road_proximity_coverage.py::test_source_chain_calls_proximity_then_coverage_exactly_once`
- `tests/unit/test_assess_road_proximity_coverage.py::test_wrong_public_input_type_is_controlled_and_fast`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_coverage`

**Signature**

```python
def _coverage(
    extraction: IgnBdTopoExtraction | None = None,
    *,
    geometries: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    layer: str = "departement",
    department_code: str = "31",
    provider: str | None = None,
    product: str | None = None,
    edition: str = EDITION,
    product_version: str | None = "3.5",
    archive_sha256: str = ARCHIVE_SHA256,
) -> IgnBdTopoDepartmentCoverage:
```

**Purpose**

Implements coverage according to the exact implementation and guards in this file.

**Inputs**

- `extraction` (`IgnBdTopoExtraction | None`; optional/default `None`) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `geometries` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `crs` (`str | None`; optional/default `'EPSG:2154'`) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.
- `layer` (`str`; optional/default `'departement'`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `department_code` (`str`; optional/default `'31'`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `provider` (`str | None`; optional/default `None`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `product` (`str | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `edition` (`str`; optional/default `EDITION`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `product_version` (`str | None`; optional/default `'3.5'`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `archive_sha256` (`str`; optional/default `ARCHIVE_SHA256`) — integrity digest used to bind exact bytes or canonical content. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoDepartmentCoverage`. Observed return expression(s): `IgnBdTopoDepartmentCoverage(extraction=package, coverage=selected, summary=summary, source_provider=cast(str, lineage['source_provider']), source_product=cast(str, lineage['source_product']), source_department_code=department_code, source_edition=edition, source_product_version=product_version, source_archive_sha256=archive_sha256, source_layer=layer)`.

**Algorithm**

1. Computes `package` from `extraction or _extraction()`.
2. Computes `values` from `geometries`.
3. Checks `values is None`. When true: Computes `values` from `[Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)])]`.
4. Computes `raw` from `gpd.GeoDataFrame({'code_insee': [department_code] * len(values), 'nom_officiel': [f'Department {position}' for position in range(len(values))]}, geometry=values, crs=crs)`.
5. Computes `lineage` from `{'source_provider': provider or package.archive.provider, 'source_product': product or package.archive.product, 'source_department_code': department_code, 'source_edition': edition, 'source_product_version': product_version, 'source_archive_sha256': archive_sha256, 'source_layer': layer, 'spatial_role': 'SOURCE_COVERA…`.
6. Computes `selected` from `raw.copy()`.
7. Iterates `(column, value)` over `lineage.items()`. For each value: Computes `selected[column]` from `value`.
8. Computes `geometry` from `raw.geometry`.
9. Computes `non_null` from `~geometry.isna()`.
10. Computes `non_empty` from `non_null & ~geometry.is_empty`.
11. Computes `summary` from `IgnBdTopoCoverageLayerSummary(source_layer_name=layer, crs='' if crs is None else str(raw.crs), source_feature_count=len(raw), selected_feature_count=len(raw), columns=tuple((str(column) for column in raw.columns)), dtypes=tuple(((str(column), str(dtype)) for column, dtype in raw.dtypes.items())), null_geometry_count=…`.
12. Returns `IgnBdTopoDepartmentCoverage(extraction=package, coverage=selected, summary=summary, source_provider=cast(str, lineage['source_provider']), source_product=cast(str, lineage['source_product']), source_department_code=department_code, source_edition=edition, source_product_version=product_version, source_archive_sha256=archive_sha256, source_layer=layer)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `raw.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `(non_empty & ~geometry.is_valid).sum`, `(non_null & geometry.is_empty).sum`, `IgnBdTopoCoverageLayerSummary`, `IgnBdTopoDepartmentCoverage`, `Polygon`, `_extraction`, `cast`, `geometry.geom_type.dropna`, `geometry.geom_type.dropna().unique`, `geometry.isna`, `geometry.isna().sum`, `gpd.GeoDataFrame`, `int`, `len`, `lineage.items`, `range`, `raw.copy`, `raw.dtypes.items`, `sorted`, `str`, `tuple`.

**Known repository callers**

- `tests/unit/test_assess_road_proximity_coverage.py` — `_assess`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_classes_are_diagnosed_independently`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_configured_coverage_layer_cannot_be_replaced_by_real_alternate_layer`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_coverage_must_retain_same_extraction_object`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_coverage_package_lineage_must_match_road_archive`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_coverage_spatial_role_and_source_type_are_controlled`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_exact_coverage_lineage_is_appended_to_every_row`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_invalid_coverage_geometry_is_rejected`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_polygonal_coverage_geometry_is_accepted`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_result_preserves_every_upstream_fact_and_input_object`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_selected_department_identity_is_exact`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_source_chain_calls_proximity_then_coverage_exactly_once`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_strict_boundary_status_logic`

**Tests**

- `tests/unit/test_assess_road_proximity_coverage.py::test_classes_are_diagnosed_independently`
- `tests/unit/test_assess_road_proximity_coverage.py::test_configured_coverage_layer_cannot_be_replaced_by_real_alternate_layer`
- `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_must_retain_same_extraction_object`
- `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_package_lineage_must_match_road_archive`
- `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_spatial_role_and_source_type_are_controlled`
- `tests/unit/test_assess_road_proximity_coverage.py::test_exact_coverage_lineage_is_appended_to_every_row`
- `tests/unit/test_assess_road_proximity_coverage.py::test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative`
- `tests/unit/test_assess_road_proximity_coverage.py::test_invalid_coverage_geometry_is_rejected`
- `tests/unit/test_assess_road_proximity_coverage.py::test_polygonal_coverage_geometry_is_accepted`
- `tests/unit/test_assess_road_proximity_coverage.py::test_result_preserves_every_upstream_fact_and_input_object`
- `tests/unit/test_assess_road_proximity_coverage.py::test_selected_department_identity_is_exact`
- `tests/unit/test_assess_road_proximity_coverage.py::test_source_chain_calls_proximity_then_coverage_exactly_once`
- `tests/unit/test_assess_road_proximity_coverage.py::test_strict_boundary_status_logic`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_metric_parcels`

**Signature**

```python
def _metric_parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[str] | None = None,
) -> gpd.GeoDataFrame:
```

**Purpose**

Implements metric parcels according to the exact implementation and guards in this file.

**Inputs**

- `geometries` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `identifiers` (`list[str] | None`; optional/default `None`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `gpd.GeoDataFrame({'parcel_id': ids, 'preserved_value': list(range(len(values)))}, geometry=values, crs='EPSG:2154', index=[20 + position for position in range(len(values))])`.

**Algorithm**

1. Computes `values` from `geometries or [Polygon([(100, 100), (100, 200), (200, 200), (200, 100), (100, 100)])]`.
2. Computes `ids` from `identifiers or [f'PARCEL-{position + 1}' for position in range(len(values))]`.
3. Returns `gpd.GeoDataFrame({'parcel_id': ids, 'preserved_value': list(range(len(values)))}, geometry=values, crs='EPSG:2154', index=[20 + position for position in range(len(values))])`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `Polygon`, `gpd.GeoDataFrame`, `len`, `list`, `range`.

**Known repository callers**

- `tests/unit/test_assess_road_proximity_coverage.py` — `_parcels`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_parcels`

**Signature**

```python
def _parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[str] | None = None,
) -> gpd.GeoDataFrame:
```

**Purpose**

Implements parcels according to the exact implementation and guards in this file.

**Inputs**

- `geometries` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `identifiers` (`list[str] | None`; optional/default `None`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `_metric_parcels(geometries, identifiers=identifiers).to_crs('EPSG:4326')`.

**Algorithm**

1. Returns `_metric_parcels(geometries, identifiers=identifiers).to_crs('EPSG:4326')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `_metric_parcels(geometries, identifiers=identifiers).to_crs`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_metric_parcels`, `_metric_parcels(geometries, identifiers=identifiers).to_crs`.

**Known repository callers**

- `tests/unit/test_assess_road_proximity_coverage.py` — `_assess`
- `tests/unit/test_assess_road_proximity_coverage.py` — `_corrupt_generated`
- `tests/unit/test_assess_road_proximity_coverage.py` — `_proximity`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_classes_are_diagnosed_independently`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_coverage_loader_failure_is_controlled`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_coverage_spatial_role_and_source_type_are_controlled`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_full_parcel_coverage_position_is_conservative`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_inconsistent_generated_status_is_rejected`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_malformed_upstream_result_fails_before_coverage_load`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_matched_outside_or_crossing_status`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_no_match_takes_precedence_over_coverage_position`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_position_uses_full_geometry_not_centroid`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_proximity_failure_stops_coverage_loading`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_result_is_frozen_and_has_no_business_decision_fields`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_result_preserves_every_upstream_fact_and_input_object`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_source_chain_calls_proximity_then_coverage_exactly_once`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_strict_boundary_status_logic`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_wrong_public_input_type_is_controlled_and_fast`

**Tests**

- `tests/unit/test_assess_road_proximity_coverage.py::test_classes_are_diagnosed_independently`
- `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_loader_failure_is_controlled`
- `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_spatial_role_and_source_type_are_controlled`
- `tests/unit/test_assess_road_proximity_coverage.py::test_full_parcel_coverage_position_is_conservative`
- `tests/unit/test_assess_road_proximity_coverage.py::test_inconsistent_generated_status_is_rejected`
- `tests/unit/test_assess_road_proximity_coverage.py::test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative`
- `tests/unit/test_assess_road_proximity_coverage.py::test_malformed_upstream_result_fails_before_coverage_load`
- `tests/unit/test_assess_road_proximity_coverage.py::test_matched_outside_or_crossing_status`
- `tests/unit/test_assess_road_proximity_coverage.py::test_no_match_takes_precedence_over_coverage_position`
- `tests/unit/test_assess_road_proximity_coverage.py::test_position_uses_full_geometry_not_centroid`
- `tests/unit/test_assess_road_proximity_coverage.py::test_proximity_failure_stops_coverage_loading`
- `tests/unit/test_assess_road_proximity_coverage.py::test_result_is_frozen_and_has_no_business_decision_fields`
- `tests/unit/test_assess_road_proximity_coverage.py::test_result_preserves_every_upstream_fact_and_input_object`
- `tests/unit/test_assess_road_proximity_coverage.py::test_source_chain_calls_proximity_then_coverage_exactly_once`
- `tests/unit/test_assess_road_proximity_coverage.py::test_strict_boundary_status_logic`
- `tests/unit/test_assess_road_proximity_coverage.py::test_wrong_public_input_type_is_controlled_and_fast`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_proximity`

**Signature**

```python
def _proximity(
    parcels: gpd.GeoDataFrame | None = None,
    *,
    distances: dict[str, float] | None = None,
) -> ParcelRoadProximityResult:
```

**Purpose**

Implements proximity according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`gpd.GeoDataFrame | None`; optional/default `None`) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `distances` (`dict[str, float] | None`; optional/default `None`) — linear quantity, normally metres where the name ends in `_m`. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `ParcelRoadProximityResult`. Observed return expression(s): `ParcelRoadProximityResult(source_parcels.copy(), table, coverage)`.

**Algorithm**

1. Computes `source_parcels` from `parcels if parcels is not None else _parcels()`.
2. Computes `policy` from `load_ign_road_vehicle_proxy_policy()`.
3. Computes `configured_distances` from `distances or {}`.
4. Computes `primary_rules` from `{'GENERAL_VEHICLE_PROXY': 'OPEN_OR_TOLL', 'LIMITED_VEHICLE_PROXY': 'LIMITED_NATURE', 'RESTRICTED_REVIEW': 'PRIVATE_ROAD', 'NOT_GENERAL_VEHICLE_PROXY': 'PHYSICALLY_IMPOSSIBLE', 'UNKNOWN_REVIEW': 'UNKNOWN'}`.
5. Defines `rows` with annotation `list[dict[str, object]]` from `[]`.
6. Iterates `parcel_id` over `source_parcels['parcel_id']`. For each value: Iterates `(position, road_class)` over `enumerate(ELIGIBLE_CLASSES)`. For each value: Computes `distance_m` from `configured_distances.get(road_class, 50.0 + position)`. Computes `primary_rule` from `primary_rules[road_class]`. Calls `rows.append({'parcel_id': parcel_id, 'road_proxy_class': road_class, 'nearest_road_proxy_distance_m': distance_m, 'nearest_road_feature_id': f'ROAD-{road_class}', 'nearest_source_feature_id': f'SOURCE-{road_class}', 'nearest_road_tie_count': 1, 'nearest_road_primary_rule': primary_rule, 'nearest_road_rule_trace_json': f'["{primary_rule}"]', 'nearest_road_un…` for its validation or side effect.
7. Computes `table` from `pd.DataFrame(rows, columns=CLASS_PROXIMITY_COLUMNS)`.
8. Computes `table['nearest_road_proxy_distance_m']` from `table['nearest_road_proxy_distance_m'].astype('float64')`.
9. Computes `table['nearest_road_tie_count']` from `table['nearest_road_tie_count'].astype('Int64')`.
10. Computes `table['nearest_road_toll_evidence']` from `table['nearest_road_toll_evidence'].astype('boolean')`.
11. Computes `coverage` from `tuple((RoadProxyClassCoverage(road_proxy_class=road_class, feature_count=1, distance_eligible=road_class != 'NOT_DISTANCE_PROXY') for road_class in ALL_CLASSES))`.
12. Returns `ParcelRoadProximityResult(source_parcels.copy(), table, coverage)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `load_ign_road_vehicle_proxy_policy`, `source_parcels.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `ParcelRoadProximityResult`, `RoadProxyClassCoverage`, `_parcels`, `configured_distances.get`, `enumerate`, `load_ign_road_vehicle_proxy_policy`, `pd.DataFrame`, `rows.append`, `source_parcels.copy`, `table['nearest_road_proxy_distance_m'].astype`, `table['nearest_road_tie_count'].astype`, `table['nearest_road_toll_evidence'].astype`, `tuple`.

**Known repository callers**

- `tests/unit/test_assess_road_proximity_coverage.py` — `_assess`
- `tests/unit/test_assess_road_proximity_coverage.py` — `_corrupt_generated`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_classes_are_diagnosed_independently`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_coverage_loader_failure_is_controlled`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_coverage_spatial_role_and_source_type_are_controlled`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_full_parcel_coverage_position_is_conservative`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_inconsistent_generated_status_is_rejected`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_malformed_upstream_result_fails_before_coverage_load`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_matched_outside_or_crossing_status`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_matched_road_lineage_must_match_coverage`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_no_match_takes_precedence_over_coverage_position`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_position_uses_full_geometry_not_centroid`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_result_preserves_every_upstream_fact_and_input_object`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_source_chain_calls_proximity_then_coverage_exactly_once`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_strict_boundary_status_logic`

**Tests**

- `tests/unit/test_assess_road_proximity_coverage.py::test_classes_are_diagnosed_independently`
- `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_loader_failure_is_controlled`
- `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_spatial_role_and_source_type_are_controlled`
- `tests/unit/test_assess_road_proximity_coverage.py::test_full_parcel_coverage_position_is_conservative`
- `tests/unit/test_assess_road_proximity_coverage.py::test_inconsistent_generated_status_is_rejected`
- `tests/unit/test_assess_road_proximity_coverage.py::test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative`
- `tests/unit/test_assess_road_proximity_coverage.py::test_malformed_upstream_result_fails_before_coverage_load`
- `tests/unit/test_assess_road_proximity_coverage.py::test_matched_outside_or_crossing_status`
- `tests/unit/test_assess_road_proximity_coverage.py::test_matched_road_lineage_must_match_coverage`
- `tests/unit/test_assess_road_proximity_coverage.py::test_no_match_takes_precedence_over_coverage_position`
- `tests/unit/test_assess_road_proximity_coverage.py::test_position_uses_full_geometry_not_centroid`
- `tests/unit/test_assess_road_proximity_coverage.py::test_result_preserves_every_upstream_fact_and_input_object`
- `tests/unit/test_assess_road_proximity_coverage.py::test_source_chain_calls_proximity_then_coverage_exactly_once`
- `tests/unit/test_assess_road_proximity_coverage.py::test_strict_boundary_status_logic`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_without_match`

**Signature**

```python
def _without_match(
    proximity: ParcelRoadProximityResult,
    road_class: str = "UNKNOWN_REVIEW",
) -> ParcelRoadProximityResult:
```

**Purpose**

Implements without match according to the exact implementation and guards in this file.

**Inputs**

- `proximity` (`ParcelRoadProximityResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `road_class` (`str`; optional/default `'UNKNOWN_REVIEW'`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `ParcelRoadProximityResult`. Observed return expression(s): `replace(proximity, class_proximity=table, class_coverage=coverage)`.

**Algorithm**

1. Computes `table` from `proximity.class_proximity.copy()`.
2. Computes `mask` from `table['road_proxy_class'].eq(road_class)`.
3. Iterates `column` over `SELECTED_COLUMNS`. For each value: Computes `table.loc[mask, column]` from `pd.NA`.
4. Computes `table['nearest_road_proxy_distance_m']` from `table['nearest_road_proxy_distance_m'].astype('float64')`.
5. Computes `table['nearest_road_tie_count']` from `table['nearest_road_tie_count'].astype('Int64')`.
6. Computes `table['nearest_road_toll_evidence']` from `table['nearest_road_toll_evidence'].astype('boolean')`.
7. Computes `coverage` from `tuple((replace(item, feature_count=0) if item.road_proxy_class == road_class else item for item in proximity.class_coverage))`.
8. Returns `replace(proximity, class_proximity=table, class_coverage=coverage)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `proximity.class_proximity.copy`, `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `proximity.class_proximity.copy`, `replace`, `table['nearest_road_proxy_distance_m'].astype`, `table['nearest_road_tie_count'].astype`, `table['nearest_road_toll_evidence'].astype`, `table['road_proxy_class'].eq`, `tuple`.

**Known repository callers**

- `tests/unit/test_assess_road_proximity_coverage.py` — `test_no_match_takes_precedence_over_coverage_position`

**Tests**

- `tests/unit/test_assess_road_proximity_coverage.py::test_no_match_takes_precedence_over_coverage_position`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_measured_boundary_distance`

**Signature**

```python
def _measured_boundary_distance(
    parcels: gpd.GeoDataFrame,
    coverage: IgnBdTopoDepartmentCoverage,
) -> float:
```

**Purpose**

Implements measured boundary distance according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `coverage` (`IgnBdTopoDepartmentCoverage`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `float`. Observed return expression(s): `float(geometry.distance(coverage.coverage.geometry.iloc[0].boundary))`.

**Algorithm**

1. Computes `geometry` from `parcels.to_crs('EPSG:2154').geometry.iloc[0]`.
2. Returns `float(geometry.distance(coverage.coverage.geometry.iloc[0].boundary))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `parcels.to_crs`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `float`, `geometry.distance`, `parcels.to_crs`.

**Known repository callers**

- `tests/unit/test_assess_road_proximity_coverage.py` — `test_classes_are_diagnosed_independently`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_strict_boundary_status_logic`

**Tests**

- `tests/unit/test_assess_road_proximity_coverage.py::test_classes_are_diagnosed_independently`
- `tests/unit/test_assess_road_proximity_coverage.py::test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative`
- `tests/unit/test_assess_road_proximity_coverage.py::test_strict_boundary_status_logic`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_assess`

**Signature**

```python
def _assess(
    *,
    parcels: gpd.GeoDataFrame | None = None,
    proximity: object | None = None,
    coverage: IgnBdTopoDepartmentCoverage | None = None,
    road_source: IgnBdTopoRoadData | None = None,
    source_config: IgnBdTopoSourceConfig = SOURCE_CONFIG,
    policy_path: Path | None = None,
) -> RoadProximityCoverageAssessmentResult:
```

**Purpose**

Assesses assess according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`gpd.GeoDataFrame | None`; optional/default `None`) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `proximity` (`object | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `coverage` (`IgnBdTopoDepartmentCoverage | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `road_source` (`IgnBdTopoRoadData | None`; optional/default `None`) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_config` (`IgnBdTopoSourceConfig`; optional/default `SOURCE_CONFIG`) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_path` (`Path | None`; optional/default `None`) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `RoadProximityCoverageAssessmentResult`. Observed return expression(s): `assess_road_proximity_coverage(selected_parcels, selected_source, source_config, policy_path)`.

**Algorithm**

1. Computes `selected_parcels` from `parcels if parcels is not None else _parcels()`.
2. Computes `selected_proximity` from `proximity if proximity is not None else _proximity(selected_parcels)`.
3. Computes `selected_coverage` from `coverage or _coverage()`.
4. Computes `selected_source` from `road_source or _road_source(selected_coverage.extraction)`.
5. Enters managed context(s) `patch('landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity', return_value=selected_proximity), patch('landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage', return_value=selected_coverage)` and executes: Returns `assess_road_proximity_coverage(selected_parcels, selected_source, source_config, policy_path)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_coverage`, `_parcels`, `_proximity`, `_road_source`, `assess_road_proximity_coverage`, `patch`.

**Known repository callers**

- `tests/unit/test_assess_road_proximity_coverage.py` — `_corrupt_generated`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_classes_are_diagnosed_independently`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_configured_coverage_layer_cannot_be_replaced_by_real_alternate_layer`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_coverage_must_retain_same_extraction_object`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_coverage_package_lineage_must_match_road_archive`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_coverage_spatial_role_and_source_type_are_controlled`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_exact_coverage_lineage_is_appended_to_every_row`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_full_parcel_coverage_position_is_conservative`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_inconsistent_generated_status_is_rejected`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_invalid_coverage_geometry_is_rejected`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_matched_outside_or_crossing_status`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_matched_road_lineage_must_match_coverage`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_no_match_takes_precedence_over_coverage_position`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_polygonal_coverage_geometry_is_accepted`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_position_uses_full_geometry_not_centroid`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_result_is_frozen_and_has_no_business_decision_fields`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_result_preserves_every_upstream_fact_and_input_object`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_selected_department_identity_is_exact`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_stage_does_not_construct_a_road_spatial_index`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_strict_boundary_status_logic`

**Tests**

- `tests/unit/test_assess_road_proximity_coverage.py::test_classes_are_diagnosed_independently`
- `tests/unit/test_assess_road_proximity_coverage.py::test_configured_coverage_layer_cannot_be_replaced_by_real_alternate_layer`
- `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_must_retain_same_extraction_object`
- `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_package_lineage_must_match_road_archive`
- `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_spatial_role_and_source_type_are_controlled`
- `tests/unit/test_assess_road_proximity_coverage.py::test_exact_coverage_lineage_is_appended_to_every_row`
- `tests/unit/test_assess_road_proximity_coverage.py::test_full_parcel_coverage_position_is_conservative`
- `tests/unit/test_assess_road_proximity_coverage.py::test_inconsistent_generated_status_is_rejected`
- `tests/unit/test_assess_road_proximity_coverage.py::test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative`
- `tests/unit/test_assess_road_proximity_coverage.py::test_invalid_coverage_geometry_is_rejected`
- `tests/unit/test_assess_road_proximity_coverage.py::test_matched_outside_or_crossing_status`
- `tests/unit/test_assess_road_proximity_coverage.py::test_matched_road_lineage_must_match_coverage`
- `tests/unit/test_assess_road_proximity_coverage.py::test_no_match_takes_precedence_over_coverage_position`
- `tests/unit/test_assess_road_proximity_coverage.py::test_polygonal_coverage_geometry_is_accepted`
- `tests/unit/test_assess_road_proximity_coverage.py::test_position_uses_full_geometry_not_centroid`
- `tests/unit/test_assess_road_proximity_coverage.py::test_result_is_frozen_and_has_no_business_decision_fields`
- `tests/unit/test_assess_road_proximity_coverage.py::test_result_preserves_every_upstream_fact_and_input_object`
- `tests/unit/test_assess_road_proximity_coverage.py::test_selected_department_identity_is_exact`
- `tests/unit/test_assess_road_proximity_coverage.py::test_stage_does_not_construct_a_road_spatial_index`
- `tests/unit/test_assess_road_proximity_coverage.py::test_strict_boundary_status_logic`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_first_row`

**Signature**

```python
def _first_row(
    result: RoadProximityCoverageAssessmentResult,
    road_class: str = "GENERAL_VEHICLE_PROXY",
) -> pd.Series:
```

**Purpose**

Implements first row according to the exact implementation and guards in this file.

**Inputs**

- `result` (`RoadProximityCoverageAssessmentResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `road_class` (`str`; optional/default `'GENERAL_VEHICLE_PROXY'`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.Series`. Observed return expression(s): `result.class_proximity.loc[result.class_proximity['road_proxy_class'].eq(road_class)].iloc[0]`.

**Algorithm**

1. Returns `result.class_proximity.loc[result.class_proximity['road_proxy_class'].eq(road_class)].iloc[0]`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `result.class_proximity['road_proxy_class'].eq`.

**Known repository callers**

- `tests/unit/test_assess_road_proximity_coverage.py` — `test_classes_are_diagnosed_independently`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_full_parcel_coverage_position_is_conservative`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_no_match_takes_precedence_over_coverage_position`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_position_uses_full_geometry_not_centroid`

**Tests**

- `tests/unit/test_assess_road_proximity_coverage.py::test_classes_are_diagnosed_independently`
- `tests/unit/test_assess_road_proximity_coverage.py::test_full_parcel_coverage_position_is_conservative`
- `tests/unit/test_assess_road_proximity_coverage.py::test_no_match_takes_precedence_over_coverage_position`
- `tests/unit/test_assess_road_proximity_coverage.py::test_position_uses_full_geometry_not_centroid`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_corrupt_generated`

**Signature**

```python
def _corrupt_generated(column: str, value: object, *, outside: bool = False) -> None:
```

**Purpose**

Implements corrupt generated according to the exact implementation and guards in this file.

**Inputs**

- `column` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `outside` (`bool`; optional/default `False`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. Observed return expression(s): `output`.

**Algorithm**

1. Computes `module` from `import_module('landscout.stages.assess_road_proximity_coverage')`.
2. Computes `geometry` from `Polygon([(-200, 100), (-200, 200), (-100, 200), (-100, 100), (-200, 100)]) if outside else None`.
3. Computes `parcels` from `_parcels([geometry]) if geometry is not None else _parcels()`.
4. Computes `proximity` from `_proximity(parcels)`.
5. Computes `original` from `module._diagnosed_class_proximity`.
6. Defines the local helper `corrupt`; its behavior is documented with the parent function's nested helpers.
7. Enters managed context(s) `patch.object(module, '_diagnosed_class_proximity', side_effect=corrupt), pytest.raises(RoadProximityCoverageError)` and executes: Calls `_assess(parcels=parcels, proximity=proximity)` for its validation or side effect.

**Meaningful nested/local helpers**

- `corrupt` — `def corrupt(*args: object, **kwargs: object) -> pd.DataFrame:`. It executes 4 top-level statement(s), uses `original`, `output[column].astype`, and has no explicit raises. Trivial test callbacks are intentionally grouped here with their parent.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `Polygon`, `_assess`, `_parcels`, `_proximity`, `import_module`, `original`, `output[column].astype`, `patch.object`, `pytest.raises`.

**Known repository callers**

- `tests/unit/test_assess_road_proximity_coverage.py` — `test_malformed_generated_value_is_rejected`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_outside_position_requires_zero_boundary_distance`

**Tests**

- `tests/unit/test_assess_road_proximity_coverage.py::test_malformed_generated_value_is_rejected`
- `tests/unit/test_assess_road_proximity_coverage.py::test_outside_position_requires_zero_boundary_distance`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_corrupt_generated.corrupt`

**Signature**

```python
def corrupt(*args: object, **kwargs: object) -> pd.DataFrame:
```

**Purpose**

Implements corrupt according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `output`.

**Algorithm**

1. Computes `output` from `original(*args, **kwargs)`.
2. Computes `output[column]` from `output[column].astype('object')`.
3. Computes `output.at[0, column]` from `value`.
4. Returns `output`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `original`, `output[column].astype`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_inconsistent_generated_status_is_rejected.corrupt`

**Signature**

```python
def corrupt(*args: object, **kwargs: object) -> pd.DataFrame:
```

**Purpose**

Implements corrupt according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `output`.

**Algorithm**

1. Computes `output` from `original(*args, **kwargs)`.
2. Computes `output.at[0, 'road_proximity_coverage_status']` from `wrong_status`.
3. Returns `output`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `original`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_api_exports_only_stable_symbols`

**Signature**

```python
def test_public_api_exports_only_stable_symbols() -> None:
```

**Purpose**

Protects the `public api exports only stable symbols` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `module` from `import_module('landscout.stages.assess_road_proximity_coverage')`.
- Computes `expected` from `{'RoadProximityCoverageError', 'RoadProximityCoverageAssessmentResult', 'assess_road_proximity_coverage'}`.

**Action**

- Calls `all`, `hasattr`, `import_module`.

**Expected result**

- Direct assertions: `assert set(module.__all__) == expected`; `assert expected <= set(stages.__all__)`; `assert all((hasattr(stages, symbol) for symbol in expected))`; `assert not hasattr(stages, '_coverage_positions')`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `public api exports only stable symbols` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `all`, `hasattr`, `import_module`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_wrong_public_input_type_is_controlled_and_fast`

**Signature**

```python
def test_wrong_public_input_type_is_controlled_and_fast(argument: str) -> None:
```

**Purpose**

Protects the `wrong public input type is controlled and fast` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `argument`.
- Contains 3 explicit setup/context statement(s).
- Defines `kwargs` with annotation `dict[str, object]` from `{'parcels': _parcels(), 'road_source': _road_source(), 'source_config': SOURCE_CONFIG, 'policy_path': None}`.
- Computes `kwargs[argument]` from `pd.DataFrame() if argument == 'parcels' else object()`.
- Enters managed context(s) `patch('landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity'), patch('landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage'), pytest.raises(RoadProximityCoverageError)` and executes: Calls `assess_road_proximity_coverage(**cast(Any, kwargs))` for its validation or side effect.

**Action**

- Calls `_parcels`, `_road_source`, `assess_road_proximity_coverage`, `cast`, `coverage_loader.assert_not_called`, `object`, `pd.DataFrame`, `proximity_stage.assert_not_called`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with patch('landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity') as proximity_stage, patch('landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage') as coverage_loader, pytest.raises(RoadProximityCoverageError): assess_road_proximity_coverage(**cast(Any, kwargs))`.

**Regression protected**

- Protects the exact `wrong public input type is controlled and fast` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_road_source`, `assess_road_proximity_coverage`, `cast`, `coverage_loader.assert_not_called`, `object`, `patch`, `pd.DataFrame`, `proximity_stage.assert_not_called`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_chain_calls_proximity_then_coverage_exactly_once`

**Signature**

```python
def test_source_chain_calls_proximity_then_coverage_exactly_once() -> None:
```

**Purpose**

Protects the `source chain calls proximity then coverage exactly once` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 6 explicit setup/context statement(s).
- Computes `coverage` from `_coverage()`.
- Computes `road_source` from `_road_source(coverage.extraction)`.
- Computes `parcels` from `_parcels()`.
- Computes `proximity` from `_proximity(parcels)`.
- Computes `policy_path` from `Path('configs/access/ign_bdtopo_vehicle_proxy_policy.yaml')`.
- Enters managed context(s) `patch('landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity', return_value=proximity), patch('landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage', return_value=coverage)` and executes: Calls `assess_road_proximity_coverage(parcels, road_source, SOURCE_CONFIG, policy_path)` for its validation or side effect.

**Action**

- Calls `Path`, `_coverage`, `_parcels`, `_proximity`, `_road_source`, `assess_road_proximity_coverage`, `coverage_loader.assert_called_once_with`, `proximity_stage.assert_called_once_with`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `source chain calls proximity then coverage exactly once` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Path`, `_coverage`, `_parcels`, `_proximity`, `_road_source`, `assess_road_proximity_coverage`, `coverage_loader.assert_called_once_with`, `patch`, `proximity_stage.assert_called_once_with`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_proximity_failure_stops_coverage_loading`

**Signature**

```python
def test_proximity_failure_stops_coverage_loading() -> None:
```

**Purpose**

Protects the `proximity failure stops coverage loading` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `patch('landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity', side_effect=ValueError('bad proximity')), patch('landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage'), pytest.raises(RoadProximityCoverageError)` and executes: Calls `assess_road_proximity_coverage(_parcels(), _road_source(), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `ValueError`, `_parcels`, `_road_source`, `assess_road_proximity_coverage`, `coverage_loader.assert_not_called`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with patch('landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity', side_effect=ValueError('bad proximity')), patch('landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage') as coverage_loader, pytest.raises(RoadProximityCoverageError): assess_road_proximity_coverage(_parcels(), _road_source(), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `proximity failure stops coverage loading` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `ValueError`, `_parcels`, `_road_source`, `assess_road_proximity_coverage`, `coverage_loader.assert_not_called`, `patch`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coverage_loader_failure_is_controlled`

**Signature**

```python
def test_coverage_loader_failure_is_controlled() -> None:
```

**Purpose**

Protects the `coverage loader failure is controlled` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `parcels` from `_parcels()`.
- Enters managed context(s) `patch('landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity', return_value=_proximity(parcels)), patch('landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage', side_effect=ValueError('bad coverage')), pytest.raises(RoadProximityCoverageError)` and executes: Calls `assess_road_proximity_coverage(parcels, _road_source(), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `ValueError`, `_parcels`, `_proximity`, `_road_source`, `assess_road_proximity_coverage`, `coverage_loader.assert_called_once`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with patch('landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity', return_value=_proximity(parcels)), patch('landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage', side_effect=ValueError('bad coverage')) as coverage_loader, pytest.raises(RoadProximityCoverageError): assess_road_proximity_coverage(parcels, _road_source(), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `coverage loader failure is controlled` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `ValueError`, `_parcels`, `_proximity`, `_road_source`, `assess_road_proximity_coverage`, `coverage_loader.assert_called_once`, `patch`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_stage_does_not_construct_a_road_spatial_index`

**Signature**

```python
def test_stage_does_not_construct_a_road_spatial_index() -> None:
```

**Purpose**

Protects the `stage does not construct a road spatial index` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Enters managed context(s) `patch('shapely.STRtree', side_effect=AssertionError('forbidden'))` and executes: Calls `_assess()` for its validation or side effect.
- Computes `source` from `Path('src/landscout/stages/assess_road_proximity_coverage.py').read_text(encoding='utf-8')`.

**Action**

- Calls `AssertionError`, `Path`, `Path('src/landscout/stages/assess_road_proximity_coverage.py').read_text`, `_assess`.

**Expected result**

- Direct assertions: `assert 'STRtree(' not in source`; `assert 'query_nearest(' not in source`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `stage does not construct a road spatial index` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `AssertionError`, `Path`, `Path('src/landscout/stages/assess_road_proximity_coverage.py').read_text`, `_assess`, `patch`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_upstream_result_fails_before_coverage_load`

**Signature**

```python
def test_malformed_upstream_result_fails_before_coverage_load(mutation: Any) -> None:
```

**Purpose**

Protects the `malformed upstream result fails before coverage load` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `mutation`.
- Contains 3 explicit setup/context statement(s).
- Computes `parcels` from `_parcels()`.
- Computes `malformed` from `mutation(_proximity(parcels))`.
- Enters managed context(s) `patch('landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity', return_value=malformed), patch('landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage'), pytest.raises(RoadProximityCoverageError)` and executes: Calls `assess_road_proximity_coverage(parcels, _road_source(), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_parcels`, `_proximity`, `_road_source`, `assess_road_proximity_coverage`, `coverage_loader.assert_not_called`, `mutation`, `object`, `range`, `replace`, `result.class_proximity.assign`, `result.class_proximity.drop`, `result.class_proximity.iloc[:-1].copy`, `result.class_proximity.iloc[[1, 0, *range(2, 5)]].reset_index`, `result.parcels.drop`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with patch('landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity', return_value=malformed), patch('landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage') as coverage_loader, pytest.raises(RoadProximityCoverageError): assess_road_proximity_coverage(parcels, _road_source(), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `malformed upstream result fails before coverage load` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_proximity`, `_road_source`, `assess_road_proximity_coverage`, `coverage_loader.assert_not_called`, `mutation`, `object`, `patch`, `pytest.mark.parametrize`, `pytest.raises`, `range`, `replace`, `result.class_proximity.assign`, `result.class_proximity.drop`, `result.class_proximity.iloc[:-1].copy`, `result.class_proximity.iloc[[1, 0, *range(2, 5)]].reset_index`, `result.parcels.drop`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coverage_package_lineage_must_match_road_archive`

**Signature**

```python
def test_coverage_package_lineage_must_match_road_archive(
    field: str, value: object
) -> None:
```

**Purpose**

Protects the `coverage package lineage must match road archive` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `field`, `value`.
- Contains 5 explicit setup/context statement(s).
- Computes `coverage` from `_coverage()`.
- Computes `frame` from `coverage.coverage.copy()`.
- Computes `frame[field]` from `value`.
- Computes `forged` from `replace(coverage, coverage=frame, summary=summary, **{field: value})`.
- Enters managed context(s) `pytest.raises(RoadProximityCoverageError, match='package|lineage|provider|product')` and executes: Calls `_assess(coverage=forged, road_source=_road_source(coverage.extraction))` for its validation or side effect.

**Action**

- Calls `_assess`, `_coverage`, `_road_source`, `cast`, `coverage.coverage.copy`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(RoadProximityCoverageError, match='package|lineage|provider|product'): _assess(coverage=forged, road_source=_road_source(coverage.extraction))`.

**Regression protected**

- Protects the exact `coverage package lineage must match road archive` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_assess`, `_coverage`, `_road_source`, `cast`, `coverage.coverage.copy`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_configured_coverage_layer_cannot_be_replaced_by_real_alternate_layer`

**Signature**

```python
def test_configured_coverage_layer_cannot_be_replaced_by_real_alternate_layer() -> None:
```

**Purpose**

Protects the `configured coverage layer cannot be replaced by real alternate layer` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `coverage` from `_coverage(layer='zone_administrative')`.
- Enters managed context(s) `pytest.raises(RoadProximityCoverageError, match='configured|layer')` and executes: Calls `_assess(coverage=coverage, road_source=_road_source(coverage.extraction))` for its validation or side effect.

**Action**

- Calls `_assess`, `_coverage`, `_road_source`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(RoadProximityCoverageError, match='configured|layer'): _assess(coverage=coverage, road_source=_road_source(coverage.extraction))`.

**Regression protected**

- Protects the exact `configured coverage layer cannot be replaced by real alternate layer` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_assess`, `_coverage`, `_road_source`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_selected_department_identity_is_exact`

**Signature**

```python
def test_selected_department_identity_is_exact() -> None:
```

**Purpose**

Protects the `selected department identity is exact` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `coverage` from `_coverage()`.
- Computes `frame` from `coverage.coverage.copy()`.
- Computes `frame[coverage.summary.department_code_field]` from `'32'`.
- Computes `forged` from `replace(coverage, coverage=frame, summary=replace(coverage.summary, selected_department_code='32'))`.
- Enters managed context(s) `pytest.raises(RoadProximityCoverageError, match='department')` and executes: Calls `_assess(coverage=forged)` for its validation or side effect.

**Action**

- Calls `_assess`, `_coverage`, `coverage.coverage.copy`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(RoadProximityCoverageError, match='department'): _assess(coverage=forged)`.

**Regression protected**

- Protects the exact `selected department identity is exact` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_assess`, `_coverage`, `coverage.coverage.copy`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coverage_spatial_role_and_source_type_are_controlled`

**Signature**

```python
def test_coverage_spatial_role_and_source_type_are_controlled() -> None:
```

**Purpose**

Protects the `coverage spatial role and source type are controlled` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 7 explicit setup/context statement(s).
- Computes `coverage` from `_coverage()`.
- Computes `frame` from `coverage.coverage.copy()`.
- Computes `frame['spatial_role']` from `'PROXY_GEOMETRY'`.
- Computes `wrong_role` from `replace(coverage, coverage=frame, summary=replace(coverage.summary, spatial_role=cast(Any, 'PROXY_GEOMETRY')), spatial_role=cast(Any, 'PROXY_GEOMETRY'))`.
- Enters managed context(s) `pytest.raises(RoadProximityCoverageError, match='spatial|lineage')` and executes: Calls `_assess(coverage=wrong_role)` for its validation or side effect.
- Computes `parcels` from `_parcels()`.
- Enters managed context(s) `patch('landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity', return_value=_proximity(parcels)), patch('landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage', return_value=object()), pytest.raises(RoadProximityCoverageError)` and executes: Calls `assess_road_proximity_coverage(parcels, _road_source(), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_assess`, `_coverage`, `_parcels`, `_proximity`, `_road_source`, `assess_road_proximity_coverage`, `cast`, `coverage.coverage.copy`, `object`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(RoadProximityCoverageError, match='spatial|lineage'): _assess(coverage=wrong_role)`; `with patch('landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity', return_value=_proximity(parcels)), patch('landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage', return_value=object()), pytest.raises(RoadProximityCoverageError): assess_road_proximity_coverage(parcels, _road_source(), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `coverage spatial role and source type are controlled` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_assess`, `_coverage`, `_parcels`, `_proximity`, `_road_source`, `assess_road_proximity_coverage`, `cast`, `coverage.coverage.copy`, `object`, `patch`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coverage_must_retain_same_extraction_object`

**Signature**

```python
def test_coverage_must_retain_same_extraction_object() -> None:
```

**Purpose**

Protects the `coverage must retain same extraction object` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `coverage` from `_coverage()`.
- Computes `forged` from `replace(coverage, extraction=replace(coverage.extraction))`.
- Enters managed context(s) `pytest.raises(RoadProximityCoverageError, match='extraction')` and executes: Calls `_assess(coverage=forged, road_source=_road_source(coverage.extraction))` for its validation or side effect.

**Action**

- Calls `_assess`, `_coverage`, `_road_source`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(RoadProximityCoverageError, match='extraction'): _assess(coverage=forged, road_source=_road_source(coverage.extraction))`.

**Regression protected**

- Protects the exact `coverage must retain same extraction object` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_assess`, `_coverage`, `_road_source`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_coverage_geometry_is_rejected`

**Signature**

```python
def test_invalid_coverage_geometry_is_rejected(
    geometries: list[object], crs: str | None, message: str
) -> None:
```

**Purpose**

Protects the `invalid coverage geometry is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometries`, `crs`, `message`.
- Contains 2 explicit setup/context statement(s).
- Computes `coverage` from `_coverage(geometries=geometries, crs=crs)`.
- Enters managed context(s) `pytest.raises(RoadProximityCoverageError, match=message)` and executes: Calls `_assess(coverage=coverage)` for its validation or side effect.

**Action**

- Calls `LineString`, `Point`, `Polygon`, `_assess`, `_coverage`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(RoadProximityCoverageError, match=message): _assess(coverage=coverage)`.

**Regression protected**

- Protects the exact `invalid coverage geometry is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `Point`, `Polygon`, `_assess`, `_coverage`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_polygonal_coverage_geometry_is_accepted`

**Signature**

```python
def test_polygonal_coverage_geometry_is_accepted(geometry: object) -> None:
```

**Purpose**

Protects the `polygonal coverage geometry is accepted` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry`.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `MultiPolygon`, `Polygon`, `_assess`, `_coverage`.

**Expected result**

- Direct assertions: `assert len(_assess(coverage=_coverage(geometries=[geometry])).parcels) == 1`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `polygonal coverage geometry is accepted` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `MultiPolygon`, `Polygon`, `_assess`, `_coverage`, `len`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_full_parcel_coverage_position_is_conservative`

**Signature**

```python
def test_full_parcel_coverage_position_is_conservative(
    geometry: Polygon, position: str
) -> None:
```

**Purpose**

Protects the `full parcel coverage position is conservative` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry`, `position`.
- Contains 2 explicit setup/context statement(s).
- Computes `parcels` from `_parcels([geometry])`.
- Computes `row` from `_first_row(_assess(parcels=parcels, proximity=_proximity(parcels)))`.

**Action**

- Calls `Polygon`, `_assess`, `_first_row`, `_parcels`, `_proximity`.

**Expected result**

- Direct assertions: `assert row.road_source_coverage_position == position`; `assert row.road_source_boundary_distance_m == 0.0`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `full parcel coverage position is conservative` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `_assess`, `_first_row`, `_parcels`, `_proximity`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_position_uses_full_geometry_not_centroid`

**Signature**

```python
def test_position_uses_full_geometry_not_centroid() -> None:
```

**Purpose**

Protects the `position uses full geometry not centroid` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `crossing_with_inside_centroid` from `Polygon([(-10, 100), (-10, 200), (300, 200), (300, 100), (-10, 100)])`.
- Computes `parcels` from `_parcels([crossing_with_inside_centroid])`.
- Computes `row` from `_first_row(_assess(parcels=parcels, proximity=_proximity(parcels)))`.

**Action**

- Calls `Polygon`, `_assess`, `_first_row`, `_parcels`, `_proximity`.

**Expected result**

- Direct assertions: `assert row.road_source_coverage_position == 'OUTSIDE_OR_CROSSING_COVERAGE'`; `assert row.road_source_boundary_distance_m == 0.0`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `position uses full geometry not centroid` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `_assess`, `_first_row`, `_parcels`, `_proximity`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative`

**Signature**

```python
def test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative() -> None:
```

**Purpose**

Protects the `internal boundary distance is full geometry finite and nonnegative` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `parcels` from `_parcels()`.
- Computes `coverage` from `_coverage()`.
- Computes `expected` from `_measured_boundary_distance(parcels, coverage)`.
- Computes `result` from `_assess(parcels=parcels, proximity=_proximity(parcels), coverage=coverage)`.
- Computes `values` from `result.class_proximity['road_source_boundary_distance_m']`.

**Action**

- Calls `_assess`, `_coverage`, `_measured_boundary_distance`, `_parcels`, `_proximity`, `np.isfinite`, `np.isfinite(values).all`, `values.eq`, `values.eq(expected).all`, `values.ge`, `values.ge(0).all`.

**Expected result**

- Direct assertions: `assert values.eq(expected).all()`; `assert np.isfinite(values).all()`; `assert values.ge(0).all()`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `internal boundary distance is full geometry finite and nonnegative` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_assess`, `_coverage`, `_measured_boundary_distance`, `_parcels`, `_proximity`, `np.isfinite`, `np.isfinite(values).all`, `values.eq`, `values.eq(expected).all`, `values.ge`, `values.ge(0).all`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_strict_boundary_status_logic`

**Signature**

```python
def test_strict_boundary_status_logic(offset: float, expected: str) -> None:
```

**Purpose**

Protects the `strict boundary status logic` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `offset`, `expected`.
- Contains 5 explicit setup/context statement(s).
- Computes `parcels` from `_parcels()`.
- Computes `coverage` from `_coverage()`.
- Computes `margin` from `_measured_boundary_distance(parcels, coverage)`.
- Computes `proximity` from `_proximity(parcels, distances={road_class: margin + offset for road_class in ELIGIBLE_CLASSES})`.
- Computes `result` from `_assess(parcels=parcels, proximity=proximity, coverage=coverage)`.

**Action**

- Calls `_assess`, `_coverage`, `_measured_boundary_distance`, `_parcels`, `_proximity`, `result.class_proximity['road_proximity_coverage_status'].eq`, `result.class_proximity['road_proximity_coverage_status'].eq(expected).all`.

**Expected result**

- Direct assertions: `assert result.class_proximity['road_proximity_coverage_status'].eq(expected).all()`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `strict boundary status logic` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_assess`, `_coverage`, `_measured_boundary_distance`, `_parcels`, `_proximity`, `pytest.mark.parametrize`, `result.class_proximity['road_proximity_coverage_status'].eq`, `result.class_proximity['road_proximity_coverage_status'].eq(expected).all`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_matched_outside_or_crossing_status`

**Signature**

```python
def test_matched_outside_or_crossing_status(geometry: Polygon) -> None:
```

**Purpose**

Protects the `matched outside or crossing status` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry`.
- Contains 2 explicit setup/context statement(s).
- Computes `parcels` from `_parcels([geometry])`.
- Computes `result` from `_assess(parcels=parcels, proximity=_proximity(parcels))`.

**Action**

- Calls `Polygon`, `_assess`, `_parcels`, `_proximity`, `result.class_proximity['road_proximity_coverage_status'].eq`, `result.class_proximity['road_proximity_coverage_status'].eq('OUTSIDE_OR_CROSSING_COVERAGE').all`.

**Expected result**

- Direct assertions: `assert result.class_proximity['road_proximity_coverage_status'].eq('OUTSIDE_OR_CROSSING_COVERAGE').all()`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `matched outside or crossing status` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `_assess`, `_parcels`, `_proximity`, `pytest.mark.parametrize`, `result.class_proximity['road_proximity_coverage_status'].eq`, `result.class_proximity['road_proximity_coverage_status'].eq('OUTSIDE_OR_CROSSING_COVERAGE').all`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_no_match_takes_precedence_over_coverage_position`

**Signature**

```python
def test_no_match_takes_precedence_over_coverage_position(geometry: Polygon) -> None:
```

**Purpose**

Protects the `no match takes precedence over coverage position` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry`.
- Contains 3 explicit setup/context statement(s).
- Computes `parcels` from `_parcels([geometry])`.
- Computes `proximity` from `_without_match(_proximity(parcels))`.
- Computes `result` from `_assess(parcels=parcels, proximity=proximity)`.

**Action**

- Calls `Polygon`, `_assess`, `_first_row`, `_parcels`, `_proximity`, `_without_match`.

**Expected result**

- Direct assertions: `assert _first_row(result, 'UNKNOWN_REVIEW').road_proximity_coverage_status == 'NO_MATCH'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `no match takes precedence over coverage position` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `_assess`, `_first_row`, `_parcels`, `_proximity`, `_without_match`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_classes_are_diagnosed_independently`

**Signature**

```python
def test_classes_are_diagnosed_independently() -> None:
```

**Purpose**

Protects the `classes are diagnosed independently` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `parcels` from `_parcels()`.
- Computes `coverage` from `_coverage()`.
- Computes `margin` from `_measured_boundary_distance(parcels, coverage)`.
- Computes `proximity` from `_proximity(parcels, distances={'GENERAL_VEHICLE_PROXY': margin - 1, 'RESTRICTED_REVIEW': margin + 1})`.
- Computes `result` from `_assess(parcels=parcels, proximity=proximity, coverage=coverage)`.

**Action**

- Calls `_assess`, `_coverage`, `_first_row`, `_measured_boundary_distance`, `_parcels`, `_proximity`.

**Expected result**

- Direct assertions: `assert _first_row(result, 'GENERAL_VEHICLE_PROXY').road_proximity_coverage_status == 'NOT_BOUNDARY_LIMITED'`; `assert _first_row(result, 'RESTRICTED_REVIEW').road_proximity_coverage_status == 'BOUNDARY_LIMITED'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `classes are diagnosed independently` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_assess`, `_coverage`, `_first_row`, `_measured_boundary_distance`, `_parcels`, `_proximity`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_exact_coverage_lineage_is_appended_to_every_row`

**Signature**

```python
def test_exact_coverage_lineage_is_appended_to_every_row() -> None:
```

**Purpose**

Protects the `exact coverage lineage is appended to every row` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `coverage` from `_coverage()`.
- Computes `result` from `_assess(coverage=coverage)`.
- Computes `expected` from `{'road_source_coverage_provider': coverage.source_provider, 'road_source_coverage_product': coverage.source_product, 'road_source_coverage_department_code': coverage.source_department_code, 'road_source_coverage_edition': coverage.source_edition, 'road_source_coverage_product_version': coverage.source_product_version,…`.

**Action**

- Calls `_assess`, `_coverage`, `expected.items`, `result.class_proximity[column].eq`, `result.class_proximity[column].eq(value).all`.

**Expected result**

- Direct assertions: `assert result.class_proximity[column].eq(value).all()`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `exact coverage lineage is appended to every row` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_assess`, `_coverage`, `expected.items`, `result.class_proximity[column].eq`, `result.class_proximity[column].eq(value).all`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_matched_road_lineage_must_match_coverage`

**Signature**

```python
def test_matched_road_lineage_must_match_coverage(
    column: str, value: str
) -> None:
```

**Purpose**

Protects the `matched road lineage must match coverage` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`, `value`.
- Contains 4 explicit setup/context statement(s).
- Computes `proximity` from `_proximity()`.
- Computes `table` from `proximity.class_proximity.copy()`.
- Computes `table[column]` from `value`.
- Enters managed context(s) `pytest.raises(RoadProximityCoverageError, match='lineage|package')` and executes: Calls `_assess(proximity=replace(proximity, class_proximity=table))` for its validation or side effect.

**Action**

- Calls `_assess`, `_proximity`, `proximity.class_proximity.copy`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(RoadProximityCoverageError, match='lineage|package'): _assess(proximity=replace(proximity, class_proximity=table))`.

**Regression protected**

- Protects the exact `matched road lineage must match coverage` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_assess`, `_proximity`, `proximity.class_proximity.copy`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_result_preserves_every_upstream_fact_and_input_object`

**Signature**

```python
def test_result_preserves_every_upstream_fact_and_input_object() -> None:
```

**Purpose**

Protects the `result preserves every upstream fact and input object` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 13 explicit setup/context statement(s).
- Computes `parcels` from `_parcels([Polygon([(100, 100), (100, 200), (200, 200), (200, 100), (100, 100)]), Polygon([(300, 300), (300, 400), (400, 400), (400, 300), (300, 300)])], identifiers=['SECOND', 'FIRST'])`.
- Computes `proximity` from `_proximity(parcels)`.
- Computes `coverage` from `_coverage()`.
- Computes `road_source` from `_road_source(coverage.extraction)`.
- Computes `parcels_before` from `deepcopy(parcels)`.
- Computes `proximity_parcels_before` from `deepcopy(proximity.parcels)`.
- Computes `table_before` from `deepcopy(proximity.class_proximity)`.
- Computes `coverage_before` from `deepcopy(coverage.coverage)`.
- Computes `roads_before` from `deepcopy(road_source.road_segments)`.
- Computes `road_summary_before` from `road_source.road_segments_summary`.
- Computes `extraction_before` from `road_source.extraction`.
- Computes `config_before` from `SOURCE_CONFIG.model_dump(mode='python')`.

**Action**

- Calls `Polygon`, `SOURCE_CONFIG.model_dump`, `_assess`, `_coverage`, `_parcels`, `_proximity`, `_road_source`, `deepcopy`.

**Expected result**

- Direct assertions: `assert road_source.road_segments_summary == road_summary_before`; `assert road_source.extraction is extraction_before`; `assert SOURCE_CONFIG.model_dump(mode='python') == config_before`; `assert tuple(result.class_proximity.columns[:len(CLASS_PROXIMITY_COLUMNS)]) == CLASS_PROXIMITY_COLUMNS`; `assert tuple(result.class_proximity.columns[len(CLASS_PROXIMITY_COLUMNS):]) == DIAGNOSTIC_COLUMNS`; `assert result.class_coverage is proximity.class_coverage`; `assert result.source_coverage is coverage`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `result preserves every upstream fact and input object` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `SOURCE_CONFIG.model_dump`, `_assess`, `_coverage`, `_parcels`, `_proximity`, `_road_source`, `assert_frame_equal`, `assert_geodataframe_equal`, `deepcopy`, `len`, `list`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_generated_value_is_rejected`

**Signature**

```python
def test_malformed_generated_value_is_rejected(column: str, value: object) -> None:
```

**Purpose**

Protects the `malformed generated value is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`, `value`.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `_corrupt_generated`, `float`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `malformed generated value is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_corrupt_generated`, `float`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_inconsistent_generated_status_is_rejected`

**Signature**

```python
def test_inconsistent_generated_status_is_rejected(
    distance: float, wrong_status: str
) -> None:
```

**Purpose**

Protects the `inconsistent generated status is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `distance`, `wrong_status`.
- Contains 5 explicit setup/context statement(s).
- Computes `module` from `import_module('landscout.stages.assess_road_proximity_coverage')`.
- Computes `parcels` from `_parcels()`.
- Computes `proximity` from `_proximity(parcels, distances={road_class: distance for road_class in ELIGIBLE_CLASSES})`.
- Computes `original` from `module._diagnosed_class_proximity`.
- Enters managed context(s) `patch.object(module, '_diagnosed_class_proximity', side_effect=corrupt), pytest.raises(RoadProximityCoverageError)` and executes: Calls `_assess(parcels=parcels, proximity=proximity)` for its validation or side effect.

**Action**

- Calls `_assess`, `_parcels`, `_proximity`, `import_module`, `original`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with patch.object(module, '_diagnosed_class_proximity', side_effect=corrupt), pytest.raises(RoadProximityCoverageError): _assess(parcels=parcels, proximity=proximity)`.

**Regression protected**

- Protects the exact `inconsistent generated status is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_assess`, `_parcels`, `_proximity`, `import_module`, `original`, `patch.object`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_outside_position_requires_zero_boundary_distance`

**Signature**

```python
def test_outside_position_requires_zero_boundary_distance() -> None:
```

**Purpose**

Protects the `outside position requires zero boundary distance` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `_corrupt_generated`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `outside position requires zero boundary distance` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_corrupt_generated`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_result_is_frozen_and_has_no_business_decision_fields`

**Signature**

```python
def test_result_is_frozen_and_has_no_business_decision_fields() -> None:
```

**Purpose**

Protects the `result is frozen and has no business decision fields` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `result` from `_assess()`.
- Enters managed context(s) `pytest.raises(FrozenInstanceError)` and executes: Computes `result.parcels` from `_parcels()`.
- Computes `forbidden` from `{'accessible', 'road_access_ok', 'legal_access', 'truck_access', 'bess_access', 'score', 'retained', 'rejected'}`.

**Action**

- Calls `_assess`, `_parcels`, `forbidden.isdisjoint`.

**Expected result**

- Direct assertions: `assert forbidden.isdisjoint(result.parcels.columns)`; `assert forbidden.isdisjoint(result.class_proximity.columns)`.
- Expected exception contexts: `with pytest.raises(FrozenInstanceError): result.parcels = _parcels()`.

**Regression protected**

- Protects the exact `result is frozen and has no business decision fields` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_assess`, `_parcels`, `forbidden.isdisjoint`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `cleabs` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `code_insee` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `columns` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_asset_status_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_carriageway_width_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_closure_period_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_importance_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_light_vehicle_access_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_nature_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_private_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_restriction_nature_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_road_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_road_primary_rule` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_road_proxy_distance_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_road_rule_trace_json` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_road_tie_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_road_toll_evidence` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_road_unknown_fields_json` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_source_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_source_department_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_source_edition` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_source_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_source_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `nom_officiel` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `preserved_value` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `proximity_scope` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_proximity_coverage_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_class` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_policy_config_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `road_source_boundary_distance_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `road_source_coverage_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `road_source_coverage_department_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_source_coverage_edition` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_source_coverage_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_source_coverage_position` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_source_coverage_product` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_source_coverage_product_version` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_source_coverage_provider` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_source_coverage_spatial_role` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `source_product` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_provider` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `spatial_role` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |

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

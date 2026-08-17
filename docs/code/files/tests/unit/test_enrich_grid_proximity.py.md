# `tests/unit/test_enrich_grid_proximity.py`

## File identity

- Repository path: `tests/unit/test_enrich_grid_proximity.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `enrich_grid_proximity` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `14a73d80cd809bf5cc15d7150d7181eab62247772aa8614621b14f48e81ce189`

## 1. Purpose

Provides complete unit and regression coverage for the `enrich_grid_proximity` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import json` — required by the implementation paths and symbols documented below.
- `from copy import deepcopy` — required by the implementation paths and symbols documented below.
- `from dataclasses import replace` — required by the implementation paths and symbols documented below.
- `from hashlib import sha256` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.
- `from typing import Any, cast` — required by the implementation paths and symbols documented below.

### Third-party

- `from unittest.mock import patch` — required by the implementation paths and symbols documented below.
- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import numpy as np` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `import pyogrio` — required by the implementation paths and symbols documented below.
- `import pytest` — required by the implementation paths and symbols documented below.
- `from geopandas.testing import assert_geodataframe_equal` — required by the implementation paths and symbols documented below.
- `from pandas.api.types import is_float_dtype, is_integer_dtype` — required by the implementation paths and symbols documented below.
- `from shapely.geometry import ( GeometryCollection, LineString, MultiLineString, MultiPolygon, Point, Polygon, )` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout import stages` — required by the implementation paths and symbols documented below.
- `from landscout.sources import ( IgnBdTopoDownload, IgnBdTopoElectricityData, IgnBdTopoExtraction, IgnBdTopoLayerSummary, load_ign_bdtopo_source_config, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages import ( GridProximityError, GridProximityResult, VoltageLevelCoverage, profile_grid_proximity, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages import ( enrich_parcel_grid_proximity as public_enrich_parcel_grid_proximity, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.enrich_grid_proximity import ( VOLTAGE_PROXIMITY_COLUMNS, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.enrich_grid_proximity import ( _enrich_parcel_grid_proximity_from_normalized as enrich_parcel_grid_proximity, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.normalize_grid_ign import NormalizedIgnElectricityData` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `OVERFLOWING_INTEGER` | `10**10000` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SOURCE_CONFIG` | `load_ign_bdtopo_source_config()` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `_geometry_status`

**Signature**

```python
def _geometry_status(geometry: object) -> str:
```

**Purpose**

Implements geometry status according to the exact implementation and guards in this file.

**Inputs**

- `geometry` (`object`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `'VALID'`; `'NULL'`; `'EMPTY'`; `'INVALID'`.

**Algorithm**

1. Checks `geometry is None`. When true: Returns `'NULL'`.
2. Checks `geometry.is_empty`. When true: Returns `'EMPTY'`.
3. Checks `not geometry.is_valid`. When true: Returns `'INVALID'`.
4. Returns `'VALID'`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

- `tests/unit/test_enrich_grid_proximity.py` — `_lines`
- `tests/unit/test_enrich_grid_proximity.py` — `_posts`

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
    identifiers: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
```

**Purpose**

Implements parcels according to the exact implementation and guards in this file.

**Inputs**

- `geometries` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `identifiers` (`list[object] | None`; optional/default `None`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `crs` (`str | None`; optional/default `'EPSG:2154'`) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.
- `index` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `gpd.GeoDataFrame({'parcel_id': ids, 'source_value': list(range(count))}, geometry=values, crs=crs, index=source_index)`.

**Algorithm**

1. Computes `values` from `geometries or [Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])]`.
2. Computes `count` from `len(values)`.
3. Computes `ids` from `identifiers or [f'PARCEL-{position + 1}' for position in range(count)]`.
4. Computes `source_index` from `index or [100 + position for position in range(count)]`.
5. Returns `gpd.GeoDataFrame({'parcel_id': ids, 'source_value': list(range(count))}, geometry=values, crs=crs, index=source_index)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `Polygon`, `gpd.GeoDataFrame`, `len`, `list`, `range`.

**Known repository callers**

- `tests/unit/test_enrich_grid_proximity.py` — `_two_parcel_two_voltage_result`
- `tests/unit/test_enrich_grid_proximity.py` — `test_bad_parcel_geometry_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_caller_crafted_normalized_grid_frame_is_not_a_public_source`
- `tests/unit/test_enrich_grid_proximity.py` — `test_cross_voltage_tie_uses_lexical_global_feature_id`
- `tests/unit/test_enrich_grid_proximity.py` — `test_distance_profile_is_threshold_free_and_tracks_ties`
- `tests/unit/test_enrich_grid_proximity.py` — `test_duplicate_grid_feature_id_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_duplicate_parcel_id_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_epsg2154_parcel_input_remains_epsg2154`
- `tests/unit/test_enrich_grid_proximity.py` — `test_epsg4326_input_is_calculated_in_lambert93_and_preserved`
- `tests/unit/test_enrich_grid_proximity.py` — `test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved`
- `tests/unit/test_enrich_grid_proximity.py` — `test_invalid_exact_voltage_values_are_not_used_as_exact`
- `tests/unit/test_enrich_grid_proximity.py` — `test_invalid_parcel_id_hygiene_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_line_tie_is_counted_and_lexical_feature_id_wins`
- `tests/unit/test_enrich_grid_proximity.py` — `test_missing_crs_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_missing_parcel_column_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_nearest_any_line_preserves_every_voltage_status`
- `tests/unit/test_enrich_grid_proximity.py` — `test_nearest_exact_and_voltage_table_exclude_nonexact_lines`
- `tests/unit/test_enrich_grid_proximity.py` — `test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table`
- `tests/unit/test_enrich_grid_proximity.py` — `test_no_valid_required_grid_feature_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_nonvalid_grid_geometries_are_excluded_without_row_loss`
- `tests/unit/test_enrich_grid_proximity.py` — `test_null_parcel_id_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_post_distance_uses_parcel_and_post_polygons`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_allows_consistent_missing_manager_and_asset_status`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_nonnull_exact_field_without_exact_coverage`
- `tests/unit/test_enrich_grid_proximity.py` — `test_public_proximity_normalizes_verified_source_exactly_once`
- `tests/unit/test_enrich_grid_proximity.py` — `test_public_proximity_rejects_archive_lineage_differing_from_config`
- `tests/unit/test_enrich_grid_proximity.py` — `test_public_proximity_rejects_wrong_source_boundary_types`
- `tests/unit/test_enrich_grid_proximity.py` — `test_public_proximity_reproduces_configured_electricity_roles`
- `tests/unit/test_enrich_grid_proximity.py` — `test_semantically_wrong_parcel_geometry_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_separated_distance_uses_parcel_edge_not_centroid`
- `tests/unit/test_enrich_grid_proximity.py` — `test_source_normalization_failure_stops_grid_computation`
- `tests/unit/test_enrich_grid_proximity.py` — `test_supported_multi_geometries_are_accepted`
- `tests/unit/test_enrich_grid_proximity.py` — `test_supported_parcel_polygon_geometry_is_preserved`
- `tests/unit/test_enrich_grid_proximity.py` — `test_touching_line_has_zero_distance`
- `tests/unit/test_enrich_grid_proximity.py` — `test_unsupported_valid_grid_geometry_type_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_valid_parcel_id_is_preserved_exactly`
- `tests/unit/test_enrich_grid_proximity.py` — `test_wrong_grid_crs_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_wrong_grid_feature_type_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_wrong_spatial_role_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_z_line_has_same_horizontal_distance_as_xy_line`

**Tests**

- `tests/unit/test_enrich_grid_proximity.py::test_bad_parcel_geometry_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_caller_crafted_normalized_grid_frame_is_not_a_public_source`
- `tests/unit/test_enrich_grid_proximity.py::test_cross_voltage_tie_uses_lexical_global_feature_id`
- `tests/unit/test_enrich_grid_proximity.py::test_distance_profile_is_threshold_free_and_tracks_ties`
- `tests/unit/test_enrich_grid_proximity.py::test_duplicate_grid_feature_id_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_duplicate_parcel_id_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_epsg2154_parcel_input_remains_epsg2154`
- `tests/unit/test_enrich_grid_proximity.py::test_epsg4326_input_is_calculated_in_lambert93_and_preserved`
- `tests/unit/test_enrich_grid_proximity.py::test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved`
- `tests/unit/test_enrich_grid_proximity.py::test_invalid_exact_voltage_values_are_not_used_as_exact`
- `tests/unit/test_enrich_grid_proximity.py::test_invalid_parcel_id_hygiene_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_line_tie_is_counted_and_lexical_feature_id_wins`
- `tests/unit/test_enrich_grid_proximity.py::test_missing_crs_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_missing_parcel_column_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_nearest_any_line_preserves_every_voltage_status`
- `tests/unit/test_enrich_grid_proximity.py::test_nearest_exact_and_voltage_table_exclude_nonexact_lines`
- `tests/unit/test_enrich_grid_proximity.py::test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table`
- `tests/unit/test_enrich_grid_proximity.py::test_no_valid_required_grid_feature_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_nonvalid_grid_geometries_are_excluded_without_row_loss`
- `tests/unit/test_enrich_grid_proximity.py::test_null_parcel_id_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_post_distance_uses_parcel_and_post_polygons`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_allows_consistent_missing_manager_and_asset_status`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_nonnull_exact_field_without_exact_coverage`
- `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_normalizes_verified_source_exactly_once`
- `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_rejects_archive_lineage_differing_from_config`
- `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_rejects_wrong_source_boundary_types`
- `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_reproduces_configured_electricity_roles`
- `tests/unit/test_enrich_grid_proximity.py::test_semantically_wrong_parcel_geometry_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_separated_distance_uses_parcel_edge_not_centroid`
- `tests/unit/test_enrich_grid_proximity.py::test_source_normalization_failure_stops_grid_computation`
- `tests/unit/test_enrich_grid_proximity.py::test_supported_multi_geometries_are_accepted`
- `tests/unit/test_enrich_grid_proximity.py::test_supported_parcel_polygon_geometry_is_preserved`
- `tests/unit/test_enrich_grid_proximity.py::test_touching_line_has_zero_distance`
- `tests/unit/test_enrich_grid_proximity.py::test_unsupported_valid_grid_geometry_type_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_valid_parcel_id_is_preserved_exactly`
- `tests/unit/test_enrich_grid_proximity.py::test_wrong_grid_crs_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_wrong_grid_feature_type_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_wrong_spatial_role_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_z_line_has_same_horizontal_distance_as_xy_line`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_lines`

**Signature**

```python
def _lines(
    geometries: list[object] | None = None,
    *,
    identifiers: list[str] | None = None,
    statuses: list[str] | None = None,
    voltage_statuses: list[str] | None = None,
    voltages: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    feature_types: list[str] | None = None,
    spatial_roles: list[str] | None = None,
) -> gpd.GeoDataFrame:
```

**Purpose**

Implements lines according to the exact implementation and guards in this file.

**Inputs**

- `geometries` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `identifiers` (`list[str] | None`; optional/default `None`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `statuses` (`list[str] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `voltage_statuses` (`list[str] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `voltages` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `crs` (`str | None`; optional/default `'EPSG:2154'`) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.
- `feature_types` (`list[str] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `spatial_roles` (`list[str] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `gpd.GeoDataFrame({'grid_feature_id': ids, 'grid_feature_type': feature_types or ['ELECTRIC_LINE'] * count, 'source_feature_id': [f'SOURCE-{value}' for value in ids], 'source_department_code': ['31'] * count, 'source_edition': ['2026-06-15'] * count, 'source_archive_sha256': ['a' * 64] * count, 'source_layer': ['CUSTOM_LINE_LAYER'] * count, 'spatial_role': spatial_roles or ['PROXY_GEOMETRY'] * cou…`.

**Algorithm**

1. Computes `values` from `geometries or [LineString([(110, -20), (110, 30)])]`.
2. Computes `count` from `len(values)`.
3. Computes `ids` from `identifiers or [f'LINE-{position + 1}' for position in range(count)]`.
4. Computes `geometry_statuses` from `statuses or [_geometry_status(value) for value in values]`.
5. Computes `normalized_voltage_statuses` from `voltage_statuses or ['EXACT'] * count`.
6. Computes `normalized_voltages` from `voltages or [110.0] * count`.
7. Returns `gpd.GeoDataFrame({'grid_feature_id': ids, 'grid_feature_type': feature_types or ['ELECTRIC_LINE'] * count, 'source_feature_id': [f'SOURCE-{value}' for value in ids], 'source_department_code': ['31'] * count, 'source_edition': ['2026-06-15'] * count, 'source_archive_sha256': ['a' * 64] * count, 'source_layer': ['CUSTOM_LINE_LAYER'] * count, 'spatial_role': s…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `LineString`, `_geometry_status`, `gpd.GeoDataFrame`, `isinstance`, `len`, `range`.

**Known repository callers**

- `tests/unit/test_enrich_grid_proximity.py` — `_electricity_source`
- `tests/unit/test_enrich_grid_proximity.py` — `_two_parcel_two_voltage_result`
- `tests/unit/test_enrich_grid_proximity.py` — `test_bad_parcel_geometry_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_caller_crafted_normalized_grid_frame_is_not_a_public_source`
- `tests/unit/test_enrich_grid_proximity.py` — `test_cross_voltage_tie_uses_lexical_global_feature_id`
- `tests/unit/test_enrich_grid_proximity.py` — `test_distance_profile_is_threshold_free_and_tracks_ties`
- `tests/unit/test_enrich_grid_proximity.py` — `test_duplicate_grid_feature_id_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_duplicate_parcel_id_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_epsg2154_parcel_input_remains_epsg2154`
- `tests/unit/test_enrich_grid_proximity.py` — `test_epsg4326_input_is_calculated_in_lambert93_and_preserved`
- `tests/unit/test_enrich_grid_proximity.py` — `test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved`
- `tests/unit/test_enrich_grid_proximity.py` — `test_invalid_exact_voltage_values_are_not_used_as_exact`
- `tests/unit/test_enrich_grid_proximity.py` — `test_invalid_parcel_id_hygiene_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_line_tie_is_counted_and_lexical_feature_id_wins`
- `tests/unit/test_enrich_grid_proximity.py` — `test_missing_crs_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_missing_parcel_column_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_nearest_any_line_preserves_every_voltage_status`
- `tests/unit/test_enrich_grid_proximity.py` — `test_nearest_exact_and_voltage_table_exclude_nonexact_lines`
- `tests/unit/test_enrich_grid_proximity.py` — `test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table`
- `tests/unit/test_enrich_grid_proximity.py` — `test_no_valid_required_grid_feature_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_nonvalid_grid_geometries_are_excluded_without_row_loss`
- `tests/unit/test_enrich_grid_proximity.py` — `test_null_parcel_id_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_post_distance_uses_parcel_and_post_polygons`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_allows_consistent_missing_manager_and_asset_status`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_nonnull_exact_field_without_exact_coverage`
- `tests/unit/test_enrich_grid_proximity.py` — `test_public_proximity_normalizes_verified_source_exactly_once`
- `tests/unit/test_enrich_grid_proximity.py` — `test_semantically_wrong_parcel_geometry_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_separated_distance_uses_parcel_edge_not_centroid`
- `tests/unit/test_enrich_grid_proximity.py` — `test_supported_multi_geometries_are_accepted`
- `tests/unit/test_enrich_grid_proximity.py` — `test_supported_parcel_polygon_geometry_is_preserved`
- `tests/unit/test_enrich_grid_proximity.py` — `test_touching_line_has_zero_distance`
- `tests/unit/test_enrich_grid_proximity.py` — `test_unsupported_valid_grid_geometry_type_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_valid_parcel_id_is_preserved_exactly`
- `tests/unit/test_enrich_grid_proximity.py` — `test_wrong_grid_crs_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_wrong_grid_feature_type_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_wrong_spatial_role_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_z_line_has_same_horizontal_distance_as_xy_line`

**Tests**

- `tests/unit/test_enrich_grid_proximity.py::test_bad_parcel_geometry_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_caller_crafted_normalized_grid_frame_is_not_a_public_source`
- `tests/unit/test_enrich_grid_proximity.py::test_cross_voltage_tie_uses_lexical_global_feature_id`
- `tests/unit/test_enrich_grid_proximity.py::test_distance_profile_is_threshold_free_and_tracks_ties`
- `tests/unit/test_enrich_grid_proximity.py::test_duplicate_grid_feature_id_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_duplicate_parcel_id_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_epsg2154_parcel_input_remains_epsg2154`
- `tests/unit/test_enrich_grid_proximity.py::test_epsg4326_input_is_calculated_in_lambert93_and_preserved`
- `tests/unit/test_enrich_grid_proximity.py::test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved`
- `tests/unit/test_enrich_grid_proximity.py::test_invalid_exact_voltage_values_are_not_used_as_exact`
- `tests/unit/test_enrich_grid_proximity.py::test_invalid_parcel_id_hygiene_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_line_tie_is_counted_and_lexical_feature_id_wins`
- `tests/unit/test_enrich_grid_proximity.py::test_missing_crs_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_missing_parcel_column_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_nearest_any_line_preserves_every_voltage_status`
- `tests/unit/test_enrich_grid_proximity.py::test_nearest_exact_and_voltage_table_exclude_nonexact_lines`
- `tests/unit/test_enrich_grid_proximity.py::test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table`
- `tests/unit/test_enrich_grid_proximity.py::test_no_valid_required_grid_feature_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_nonvalid_grid_geometries_are_excluded_without_row_loss`
- `tests/unit/test_enrich_grid_proximity.py::test_null_parcel_id_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_post_distance_uses_parcel_and_post_polygons`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_allows_consistent_missing_manager_and_asset_status`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_nonnull_exact_field_without_exact_coverage`
- `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_normalizes_verified_source_exactly_once`
- `tests/unit/test_enrich_grid_proximity.py::test_semantically_wrong_parcel_geometry_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_separated_distance_uses_parcel_edge_not_centroid`
- `tests/unit/test_enrich_grid_proximity.py::test_supported_multi_geometries_are_accepted`
- `tests/unit/test_enrich_grid_proximity.py::test_supported_parcel_polygon_geometry_is_preserved`
- `tests/unit/test_enrich_grid_proximity.py::test_touching_line_has_zero_distance`
- `tests/unit/test_enrich_grid_proximity.py::test_unsupported_valid_grid_geometry_type_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_valid_parcel_id_is_preserved_exactly`
- `tests/unit/test_enrich_grid_proximity.py::test_wrong_grid_crs_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_wrong_grid_feature_type_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_wrong_spatial_role_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_z_line_has_same_horizontal_distance_as_xy_line`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_posts`

**Signature**

```python
def _posts(
    geometries: list[object] | None = None,
    *,
    identifiers: list[str] | None = None,
    statuses: list[str] | None = None,
    crs: str | None = "EPSG:2154",
    feature_types: list[str] | None = None,
    spatial_roles: list[str] | None = None,
) -> gpd.GeoDataFrame:
```

**Purpose**

Implements posts according to the exact implementation and guards in this file.

**Inputs**

- `geometries` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `identifiers` (`list[str] | None`; optional/default `None`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `statuses` (`list[str] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `crs` (`str | None`; optional/default `'EPSG:2154'`) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.
- `feature_types` (`list[str] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `spatial_roles` (`list[str] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `gpd.GeoDataFrame({'grid_feature_id': ids, 'grid_feature_type': feature_types or ['TRANSFORMATION_POST'] * count, 'source_feature_id': [f'SOURCE-{value}' for value in ids], 'source_department_code': ['31'] * count, 'source_edition': ['2026-06-15'] * count, 'source_archive_sha256': ['a' * 64] * count, 'source_layer': ['CUSTOM_POST_LAYER'] * count, 'spatial_role': spatial_roles or ['PROXY_GEOMETRY']…`.

**Algorithm**

1. Computes `values` from `geometries or [Polygon([(110, 0), (110, 10), (120, 10), (120, 0), (110, 0)])]`.
2. Computes `count` from `len(values)`.
3. Computes `ids` from `identifiers or [f'POST-{position + 1}' for position in range(count)]`.
4. Computes `geometry_statuses` from `statuses or [_geometry_status(value) for value in values]`.
5. Returns `gpd.GeoDataFrame({'grid_feature_id': ids, 'grid_feature_type': feature_types or ['TRANSFORMATION_POST'] * count, 'source_feature_id': [f'SOURCE-{value}' for value in ids], 'source_department_code': ['31'] * count, 'source_edition': ['2026-06-15'] * count, 'source_archive_sha256': ['a' * 64] * count, 'source_layer': ['CUSTOM_POST_LAYER'] * count, 'spatial_ro…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `Polygon`, `_geometry_status`, `gpd.GeoDataFrame`, `len`, `range`.

**Known repository callers**

- `tests/unit/test_enrich_grid_proximity.py` — `_electricity_source`
- `tests/unit/test_enrich_grid_proximity.py` — `_two_parcel_two_voltage_result`
- `tests/unit/test_enrich_grid_proximity.py` — `test_bad_parcel_geometry_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_cross_voltage_tie_uses_lexical_global_feature_id`
- `tests/unit/test_enrich_grid_proximity.py` — `test_distance_profile_is_threshold_free_and_tracks_ties`
- `tests/unit/test_enrich_grid_proximity.py` — `test_duplicate_grid_feature_id_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_duplicate_parcel_id_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_epsg2154_parcel_input_remains_epsg2154`
- `tests/unit/test_enrich_grid_proximity.py` — `test_epsg4326_input_is_calculated_in_lambert93_and_preserved`
- `tests/unit/test_enrich_grid_proximity.py` — `test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved`
- `tests/unit/test_enrich_grid_proximity.py` — `test_invalid_exact_voltage_values_are_not_used_as_exact`
- `tests/unit/test_enrich_grid_proximity.py` — `test_invalid_parcel_id_hygiene_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_line_tie_is_counted_and_lexical_feature_id_wins`
- `tests/unit/test_enrich_grid_proximity.py` — `test_missing_crs_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_missing_parcel_column_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_nearest_any_line_preserves_every_voltage_status`
- `tests/unit/test_enrich_grid_proximity.py` — `test_nearest_exact_and_voltage_table_exclude_nonexact_lines`
- `tests/unit/test_enrich_grid_proximity.py` — `test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table`
- `tests/unit/test_enrich_grid_proximity.py` — `test_no_valid_required_grid_feature_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_nonvalid_grid_geometries_are_excluded_without_row_loss`
- `tests/unit/test_enrich_grid_proximity.py` — `test_null_parcel_id_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_post_distance_uses_parcel_and_post_polygons`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_allows_consistent_missing_manager_and_asset_status`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_nonnull_exact_field_without_exact_coverage`
- `tests/unit/test_enrich_grid_proximity.py` — `test_public_proximity_normalizes_verified_source_exactly_once`
- `tests/unit/test_enrich_grid_proximity.py` — `test_semantically_wrong_parcel_geometry_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_separated_distance_uses_parcel_edge_not_centroid`
- `tests/unit/test_enrich_grid_proximity.py` — `test_supported_multi_geometries_are_accepted`
- `tests/unit/test_enrich_grid_proximity.py` — `test_supported_parcel_polygon_geometry_is_preserved`
- `tests/unit/test_enrich_grid_proximity.py` — `test_touching_line_has_zero_distance`
- `tests/unit/test_enrich_grid_proximity.py` — `test_unsupported_valid_grid_geometry_type_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_valid_parcel_id_is_preserved_exactly`
- `tests/unit/test_enrich_grid_proximity.py` — `test_wrong_grid_crs_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_wrong_grid_feature_type_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_wrong_spatial_role_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_z_line_has_same_horizontal_distance_as_xy_line`

**Tests**

- `tests/unit/test_enrich_grid_proximity.py::test_bad_parcel_geometry_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_cross_voltage_tie_uses_lexical_global_feature_id`
- `tests/unit/test_enrich_grid_proximity.py::test_distance_profile_is_threshold_free_and_tracks_ties`
- `tests/unit/test_enrich_grid_proximity.py::test_duplicate_grid_feature_id_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_duplicate_parcel_id_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_epsg2154_parcel_input_remains_epsg2154`
- `tests/unit/test_enrich_grid_proximity.py::test_epsg4326_input_is_calculated_in_lambert93_and_preserved`
- `tests/unit/test_enrich_grid_proximity.py::test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved`
- `tests/unit/test_enrich_grid_proximity.py::test_invalid_exact_voltage_values_are_not_used_as_exact`
- `tests/unit/test_enrich_grid_proximity.py::test_invalid_parcel_id_hygiene_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_line_tie_is_counted_and_lexical_feature_id_wins`
- `tests/unit/test_enrich_grid_proximity.py::test_missing_crs_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_missing_parcel_column_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_nearest_any_line_preserves_every_voltage_status`
- `tests/unit/test_enrich_grid_proximity.py::test_nearest_exact_and_voltage_table_exclude_nonexact_lines`
- `tests/unit/test_enrich_grid_proximity.py::test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table`
- `tests/unit/test_enrich_grid_proximity.py::test_no_valid_required_grid_feature_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_nonvalid_grid_geometries_are_excluded_without_row_loss`
- `tests/unit/test_enrich_grid_proximity.py::test_null_parcel_id_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_post_distance_uses_parcel_and_post_polygons`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_allows_consistent_missing_manager_and_asset_status`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_nonnull_exact_field_without_exact_coverage`
- `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_normalizes_verified_source_exactly_once`
- `tests/unit/test_enrich_grid_proximity.py::test_semantically_wrong_parcel_geometry_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_separated_distance_uses_parcel_edge_not_centroid`
- `tests/unit/test_enrich_grid_proximity.py::test_supported_multi_geometries_are_accepted`
- `tests/unit/test_enrich_grid_proximity.py::test_supported_parcel_polygon_geometry_is_preserved`
- `tests/unit/test_enrich_grid_proximity.py::test_touching_line_has_zero_distance`
- `tests/unit/test_enrich_grid_proximity.py::test_unsupported_valid_grid_geometry_type_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_valid_parcel_id_is_preserved_exactly`
- `tests/unit/test_enrich_grid_proximity.py::test_wrong_grid_crs_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_wrong_grid_feature_type_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_wrong_spatial_role_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_z_line_has_same_horizontal_distance_as_xy_line`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_electricity_source`

**Signature**

```python
def _electricity_source(
    lines: gpd.GeoDataFrame | None = None,
    posts: gpd.GeoDataFrame | None = None,
) -> IgnBdTopoElectricityData:
```

**Purpose**

Implements electricity source according to the exact implementation and guards in this file.

**Inputs**

- `lines` (`gpd.GeoDataFrame | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `posts` (`gpd.GeoDataFrame | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoElectricityData`. Observed return expression(s): `IgnBdTopoElectricityData(extraction=cast(Any, None), electric_lines=lines if lines is not None else _lines(), transformation_posts=posts if posts is not None else _posts(), electric_lines_summary=cast(Any, None), transformation_posts_summary=cast(Any, None))`.

**Algorithm**

1. Returns `IgnBdTopoElectricityData(extraction=cast(Any, None), electric_lines=lines if lines is not None else _lines(), transformation_posts=posts if posts is not None else _posts(), electric_lines_summary=cast(Any, None), transformation_posts_summary=cast(Any, None))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnBdTopoElectricityData`, `_lines`, `_posts`, `cast`.

**Known repository callers**

- `tests/unit/test_enrich_grid_proximity.py` — `test_public_proximity_normalizes_verified_source_exactly_once`
- `tests/unit/test_enrich_grid_proximity.py` — `test_public_proximity_rejects_wrong_source_boundary_types`
- `tests/unit/test_enrich_grid_proximity.py` — `test_source_normalization_failure_stops_grid_computation`

**Tests**

- `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_normalizes_verified_source_exactly_once`
- `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_rejects_wrong_source_boundary_types`
- `tests/unit/test_enrich_grid_proximity.py::test_source_normalization_failure_stops_grid_computation`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_physical_line_source`

**Signature**

```python
def _physical_line_source(
    identifier: str,
    geometry: LineString,
) -> gpd.GeoDataFrame:
```

**Purpose**

Implements physical line source according to the exact implementation and guards in this file.

**Inputs**

- `identifier` (`str`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `geometry` (`LineString`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `gpd.GeoDataFrame({'cleabs': [identifier], 'voltage': ['225 kV'], 'gestionnaire': ['Test manager'], 'siren_gestionnaire': ['444619258'], 'etat_de_l_objet': ['En service'], 'sources': ['Synthetic physical source'], 'identifiants_sources': [f'SOURCE-{identifier}'], 'date_creation': pd.to_datetime(['2024-01-01']), 'date_modification': pd.to_datetime(['2025-01-01']), 'date_de_confirmation': pd.to_date…`.

**Algorithm**

1. Returns `gpd.GeoDataFrame({'cleabs': [identifier], 'voltage': ['225 kV'], 'gestionnaire': ['Test manager'], 'siren_gestionnaire': ['444619258'], 'etat_de_l_objet': ['En service'], 'sources': ['Synthetic physical source'], 'identifiants_sources': [f'SOURCE-{identifier}'], 'date_creation': pd.to_datetime(['2024-01-01']), 'date_modification': pd.to_datetime(['2025-01-0…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `gpd.GeoDataFrame`, `pd.to_datetime`.

**Known repository callers**

- `tests/unit/test_enrich_grid_proximity.py` — `_physical_electricity_source`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_physical_post_source`

**Signature**

```python
def _physical_post_source(
    identifier: str,
    geometry: Polygon,
) -> gpd.GeoDataFrame:
```

**Purpose**

Implements physical post source according to the exact implementation and guards in this file.

**Inputs**

- `identifier` (`str`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `geometry` (`Polygon`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `gpd.GeoDataFrame({'cleabs': [identifier], 'toponyme': ['Test post'], 'statut_du_toponyme': ['Valid'], 'importance': ['5'], 'etat_de_l_objet': ['En service'], 'sources': ['Synthetic physical source'], 'identifiants_sources': [f'SOURCE-{identifier}'], 'date_creation': pd.to_datetime(['2024-01-01']), 'date_modification': pd.to_datetime(['2025-01-01']), 'date_de_confirmation': pd.to_datetime(['2025-0…`.

**Algorithm**

1. Returns `gpd.GeoDataFrame({'cleabs': [identifier], 'toponyme': ['Test post'], 'statut_du_toponyme': ['Valid'], 'importance': ['5'], 'etat_de_l_objet': ['En service'], 'sources': ['Synthetic physical source'], 'identifiants_sources': [f'SOURCE-{identifier}'], 'date_creation': pd.to_datetime(['2024-01-01']), 'date_modification': pd.to_datetime(['2025-01-01']), 'date_d…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `gpd.GeoDataFrame`, `pd.to_datetime`.

**Known repository callers**

- `tests/unit/test_enrich_grid_proximity.py` — `_physical_electricity_source`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_physical_summary`

**Signature**

```python
def _physical_summary(
    frame: gpd.GeoDataFrame,
    *,
    logical_name: str,
    layer_name: str,
) -> IgnBdTopoLayerSummary:
```

**Purpose**

Implements physical summary according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `logical_name` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `layer_name` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoLayerSummary`. Observed return expression(s): `IgnBdTopoLayerSummary(logical_name=cast(Any, logical_name), source_layer_name=layer_name, crs=str(frame.crs), feature_count=len(frame), columns=tuple((str(column) for column in frame.columns)), dtypes=tuple(((str(column), str(dtype)) for column, dtype in frame.dtypes.items())), null_geometry_count=int(null_mask.sum()), empty_geometry_count=int(empty_mask.sum()), invalid_geometry_count=int(invalid…`.

**Algorithm**

1. Computes `geometry` from `frame.geometry`.
2. Computes `null_mask` from `geometry.isna()`.
3. Computes `empty_mask` from `~null_mask & geometry.is_empty`.
4. Computes `invalid_mask` from `~null_mask & ~geometry.is_empty & ~geometry.is_valid`.
5. Returns `IgnBdTopoLayerSummary(logical_name=cast(Any, logical_name), source_layer_name=layer_name, crs=str(frame.crs), feature_count=len(frame), columns=tuple((str(column) for column in frame.columns)), dtypes=tuple(((str(column), str(dtype)) for column, dtype in frame.dtypes.items())), null_geometry_count=int(null_mask.sum()), empty_geometry_count=int(empty_mask.su…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnBdTopoLayerSummary`, `cast`, `empty_mask.sum`, `frame.dtypes.items`, `geometry.isna`, `geometry[~null_mask].geom_type.dropna`, `geometry[~null_mask].geom_type.dropna().unique`, `int`, `invalid_mask.sum`, `len`, `null_mask.sum`, `sorted`, `str`, `tuple`.

**Known repository callers**

- `tests/unit/test_enrich_grid_proximity.py` — `_physical_electricity_source`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_physical_electricity_source`

**Signature**

```python
def _physical_electricity_source(
    tmp_path: Path,
    *,
    alternate_roles: bool,
) -> IgnBdTopoElectricityData:
```

**Purpose**

Implements physical electricity source according to the exact implementation and guards in this file.

**Inputs**

- `tmp_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `alternate_roles` (`bool`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoElectricityData`. Observed return expression(s): `IgnBdTopoElectricityData(extraction=extraction, electric_lines=selected_lines, transformation_posts=selected_posts, electric_lines_summary=_physical_summary(selected_lines, logical_name='electric_lines', layer_name=selected_line_layer), transformation_posts_summary=_physical_summary(selected_posts, logical_name='transformation_posts', layer_name=selected_post_layer))`.

**Algorithm**

1. Computes `configured_line_layer` from `'LIGNE_ELECTRIQUE_CONFIGURED'`.
2. Computes `configured_post_layer` from `'POSTE_DE_TRANSFORMATION_CONFIGURED'`.
3. Computes `alternate_line_layer` from `'CABLE_SOURCE_ALTERNATE'`.
4. Computes `alternate_post_layer` from `'INSTALLATION_SOURCE_ALTERNATE'`.
5. Computes `frames` from `((configured_line_layer, _physical_line_source('CONFIGURED-LINE', LineString([(500, -20), (500, 30)]))), (configured_post_layer, _physical_post_source('CONFIGURED-POST', Polygon([(500, 0), (500, 10), (510, 10), (510, 0), (500, 0)]))), (alternate_line_layer, _physical_line_source('ALTERNATE-LINE', LineString([(10, -20)…`.
6. Computes `selected_line_layer` from `alternate_line_layer if alternate_roles else configured_line_layer`.
7. Computes `selected_post_layer` from `alternate_post_layer if alternate_roles else configured_post_layer`.
8. Computes `extraction_path` from `tmp_path / ('alternate-electricity-extraction' if alternate_roles else 'configured-electricity-extraction')`.
9. Calls `extraction_path.mkdir()` for its validation or side effect.
10. Computes `geopackage_path` from `extraction_path / 'electricity.gpkg'`.
11. Iterates `(position, (layer_name, frame))` over `enumerate(frames)`. For each value: Calls `pyogrio.write_dataframe(frame, geopackage_path, layer=layer_name, driver='GPKG', append=position > 0)` for its validation or side effect.
12. Computes `selected_lines` from `gpd.read_file(geopackage_path, layer=selected_line_layer, engine='pyogrio')`.
13. Computes `selected_posts` from `gpd.read_file(geopackage_path, layer=selected_post_layer, engine='pyogrio')`.
14. Computes `payload` from `geopackage_path.read_bytes()`.
15. Computes `digest` from `sha256(payload).hexdigest()`.
16. Computes `layer_names` from `tuple((str(record[0]) for record in pyogrio.list_layers(geopackage_path)))`.
17. Computes `marker` from `{'schema_version': 2, 'archive_sha256': 'a' * 64, 'geopackage_relative_path': geopackage_path.name, 'geopackage_size_bytes': len(payload), 'geopackage_sha256': digest, 'all_layer_names': list(layer_names), 'electric_lines_layer': selected_line_layer, 'transformation_posts_layer': selected_post_layer, 'spatial_role': '…`.
18. Calls `(extraction_path / '.landscout-extraction.json').write_text(json.dumps(marker), encoding='utf-8')` for its validation or side effect.
19. Computes `archive` from `IgnBdTopoDownload(provider=SOURCE_CONFIG.provider, product=SOURCE_CONFIG.product, department_code=SOURCE_CONFIG.department_code, edition=SOURCE_CONFIG.edition, product_version=SOURCE_CONFIG.product_version, projection=SOURCE_CONFIG.projection, package_format=SOURCE_CONFIG.format, archive_format=SOURCE_CONFIG.archive_f…`.
20. Computes `extraction` from `IgnBdTopoExtraction(archive=archive, extraction_path=extraction_path, geopackage_path=geopackage_path, geopackage_filename=geopackage_path.name, geopackage_size_bytes=len(payload), geopackage_sha256=digest, all_layer_names=layer_names, electric_lines_layer=selected_line_layer, transformation_posts_layer=selected_post_…`.
21. Returns `IgnBdTopoElectricityData(extraction=extraction, electric_lines=selected_lines, transformation_posts=selected_posts, electric_lines_summary=_physical_summary(selected_lines, logical_name='electric_lines', layer_name=selected_line_layer), transformation_posts_summary=_physical_summary(selected_posts, logical_name='transformation_posts', layer_name=selected_po…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `(extraction_path / '.landscout-extraction.json').write_text`, `IgnBdTopoDownload`, `extraction_path.mkdir`, `geopackage_path.read_bytes`, `gpd.read_file`, `pyogrio.write_dataframe`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `(extraction_path / '.landscout-extraction.json').write_text`, `IgnBdTopoDownload`, `IgnBdTopoElectricityData`, `IgnBdTopoExtraction`, `LineString`, `Path`, `Polygon`, `_physical_line_source`, `_physical_post_source`, `_physical_summary`, `enumerate`, `extraction_path.mkdir`, `geopackage_path.read_bytes`, `gpd.read_file`, `json.dumps`, `len`, `list`, `pyogrio.list_layers`, `pyogrio.write_dataframe`, `sha256`, `sha256(payload).hexdigest`, `str`, `tuple`.

**Known repository callers**

- `tests/unit/test_enrich_grid_proximity.py` — `_alternate_role_electricity_source`
- `tests/unit/test_enrich_grid_proximity.py` — `_configured_role_electricity_source`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_alternate_role_electricity_source`

**Signature**

```python
def _alternate_role_electricity_source(
    tmp_path: Path,
) -> IgnBdTopoElectricityData:
```

**Purpose**

Implements alternate role electricity source according to the exact implementation and guards in this file.

**Inputs**

- `tmp_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoElectricityData`. Observed return expression(s): `_physical_electricity_source(tmp_path, alternate_roles=True)`.

**Algorithm**

1. Returns `_physical_electricity_source(tmp_path, alternate_roles=True)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_physical_electricity_source`.

**Known repository callers**

- `tests/unit/test_enrich_grid_proximity.py` — `test_public_proximity_reproduces_configured_electricity_roles`

**Tests**

- `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_reproduces_configured_electricity_roles`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_configured_role_electricity_source`

**Signature**

```python
def _configured_role_electricity_source(
    tmp_path: Path,
) -> IgnBdTopoElectricityData:
```

**Purpose**

Implements configured role electricity source according to the exact implementation and guards in this file.

**Inputs**

- `tmp_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoElectricityData`. Observed return expression(s): `_physical_electricity_source(tmp_path, alternate_roles=False)`.

**Algorithm**

1. Returns `_physical_electricity_source(tmp_path, alternate_roles=False)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_physical_electricity_source`.

**Known repository callers**

- `tests/unit/test_enrich_grid_proximity.py` — `test_public_proximity_rejects_archive_lineage_differing_from_config`

**Tests**

- `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_rejects_archive_lineage_differing_from_config`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_two_parcel_two_voltage_result`

**Signature**

```python
def _two_parcel_two_voltage_result() -> GridProximityResult:
```

**Purpose**

Implements two parcel two voltage result according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `GridProximityResult`. Observed return expression(s): `enrich_parcel_grid_proximity(parcels, lines, _posts())`.

**Algorithm**

1. Computes `parcels` from `_parcels([Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]), Polygon([(40, 0), (40, 10), (50, 10), (50, 0), (40, 0)])], identifiers=['PARCEL-2', 'PARCEL-1'])`.
2. Computes `lines` from `_lines([LineString([(200, -20), (200, 30)]), LineString([(100, -20), (100, 30)])], identifiers=['LINE-275', 'LINE-110'], voltage_statuses=['EXACT', 'EXACT'], voltages=[275.0, 110.0])`.
3. Returns `enrich_parcel_grid_proximity(parcels, lines, _posts())`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `LineString`, `Polygon`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`.

**Known repository callers**

- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_bad_exact_match_voltage`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_bad_long_table_distance`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_bad_long_table_tie_count`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_bad_required_match_distance`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_bad_required_match_tie_count`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_bad_result_parcel_id`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_duplicate_parcel_voltage_pair`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_inconsistent_global_exact_distance`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_inconsistent_global_exact_identity`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_inconsistent_global_exact_metadata`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_inconsistent_global_exact_tie_count`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_invalid_long_table_voltage`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_invalid_voltage_coverage_feature_count`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_invalid_voltage_coverage_level`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_missing_long_table_match_lineage`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_missing_main_match_feature_id`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_missing_required_proximity_column`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_missing_voltage_cartesian_row`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_nondeterministic_or_duplicate_coverage`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_unknown_voltage_parcel_with_same_total_count`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_voltage_rows_out_of_parcel_order`
- `tests/unit/test_enrich_grid_proximity.py` — `test_voltage_table_is_exact_ordered_cartesian_product`

**Tests**

- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_exact_match_voltage`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_long_table_distance`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_long_table_tie_count`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_required_match_distance`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_required_match_tie_count`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_result_parcel_id`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_duplicate_parcel_voltage_pair`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_inconsistent_global_exact_distance`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_inconsistent_global_exact_identity`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_inconsistent_global_exact_metadata`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_inconsistent_global_exact_tie_count`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_invalid_long_table_voltage`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_invalid_voltage_coverage_feature_count`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_invalid_voltage_coverage_level`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_missing_long_table_match_lineage`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_missing_main_match_feature_id`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_missing_required_proximity_column`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_missing_voltage_cartesian_row`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_nondeterministic_or_duplicate_coverage`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_unknown_voltage_parcel_with_same_total_count`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_voltage_rows_out_of_parcel_order`
- `tests/unit/test_enrich_grid_proximity.py::test_voltage_table_is_exact_ordered_cartesian_product`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_mutate_parcel_result`

**Signature**

```python
def _mutate_parcel_result(
    result: GridProximityResult,
    column: str,
    value: object,
) -> GridProximityResult:
```

**Purpose**

Implements mutate parcel result according to the exact implementation and guards in this file.

**Inputs**

- `result` (`GridProximityResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `column` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GridProximityResult`. Observed return expression(s): `replace(result, parcels=parcels)`.

**Algorithm**

1. Computes `parcels` from `result.parcels.copy()`.
2. Computes `parcels[column]` from `parcels[column].astype('object')`.
3. Computes `parcels.at[0, column]` from `value`.
4. Returns `replace(result, parcels=parcels)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `replace`, `result.parcels.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `parcels[column].astype`, `replace`, `result.parcels.copy`.

**Known repository callers**

- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_bad_exact_match_voltage`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_bad_required_match_distance`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_bad_required_match_tie_count`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_bad_result_parcel_id`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_inconsistent_global_exact_distance`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_inconsistent_global_exact_identity`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_inconsistent_global_exact_metadata`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_inconsistent_global_exact_tie_count`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_missing_main_match_feature_id`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_nonnull_exact_field_without_exact_coverage`

**Tests**

- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_exact_match_voltage`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_required_match_distance`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_required_match_tie_count`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_result_parcel_id`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_inconsistent_global_exact_distance`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_inconsistent_global_exact_identity`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_inconsistent_global_exact_metadata`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_inconsistent_global_exact_tie_count`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_missing_main_match_feature_id`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_nonnull_exact_field_without_exact_coverage`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_mutate_voltage_result`

**Signature**

```python
def _mutate_voltage_result(
    result: GridProximityResult,
    column: str,
    value: object,
) -> GridProximityResult:
```

**Purpose**

Implements mutate voltage result according to the exact implementation and guards in this file.

**Inputs**

- `result` (`GridProximityResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `column` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GridProximityResult`. Observed return expression(s): `replace(result, voltage_level_proximity=table)`.

**Algorithm**

1. Computes `table` from `result.voltage_level_proximity.copy()`.
2. Computes `table[column]` from `table[column].astype('object')`.
3. Computes `table.at[0, column]` from `value`.
4. Returns `replace(result, voltage_level_proximity=table)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `replace`, `result.voltage_level_proximity.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `replace`, `result.voltage_level_proximity.copy`, `table[column].astype`.

**Known repository callers**

- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_bad_long_table_distance`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_bad_long_table_tie_count`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_invalid_long_table_voltage`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_missing_long_table_match_lineage`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_unknown_voltage_parcel_with_same_total_count`

**Tests**

- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_long_table_distance`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_long_table_tie_count`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_invalid_long_table_voltage`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_missing_long_table_match_lineage`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_unknown_voltage_parcel_with_same_total_count`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_clean_high_level_api_is_exported`

**Signature**

```python
def test_clean_high_level_api_is_exported() -> None:
```

**Purpose**

Protects the `clean high level api is exported` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls only local assertions/expressions.

**Expected result**

- Direct assertions: `assert stages.enrich_parcel_grid_proximity is public_enrich_parcel_grid_proximity`; `assert stages.profile_grid_proximity is profile_grid_proximity`; `assert 'enrich_parcel_grid_proximity' in stages.__all__`; `assert 'profile_grid_proximity' in stages.__all__`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `clean high level api is exported` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- No calls.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_proximity_normalizes_verified_source_exactly_once`

**Signature**

```python
def test_public_proximity_normalizes_verified_source_exactly_once() -> None:
```

**Purpose**

Protects the `public proximity normalizes verified source exactly once` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 6 explicit setup/context statement(s).
- Computes `parcels` from `_parcels()`.
- Computes `lines` from `_lines()`.
- Computes `posts` from `_posts()`.
- Computes `source` from `_electricity_source(lines, posts)`.
- Computes `normalized` from `NormalizedIgnElectricityData(lines, posts)`.
- Enters managed context(s) `patch('landscout.stages.enrich_grid_proximity.normalize_ign_electricity', return_value=normalized, create=True)` and executes: Computes `result` from `public_enrich_parcel_grid_proximity(parcels, source, SOURCE_CONFIG)`.

**Action**

- Calls `NormalizedIgnElectricityData`, `_electricity_source`, `_lines`, `_parcels`, `_posts`, `normalizer.assert_called_once_with`, `public_enrich_parcel_grid_proximity`.

**Expected result**

- Direct assertions: `assert result.parcels.loc[0, 'nearest_line_grid_feature_id'] == 'LINE-1'`; `assert result.parcels.loc[0, 'nearest_post_grid_feature_id'] == 'POST-1'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `public proximity normalizes verified source exactly once` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `NormalizedIgnElectricityData`, `_electricity_source`, `_lines`, `_parcels`, `_posts`, `normalizer.assert_called_once_with`, `patch`, `public_enrich_parcel_grid_proximity`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_proximity_rejects_wrong_source_boundary_types`

**Signature**

```python
def test_public_proximity_rejects_wrong_source_boundary_types(
    argument: str,
) -> None:
```

**Purpose**

Protects the `public proximity rejects wrong source boundary types` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `argument`.
- Contains 3 explicit setup/context statement(s).
- Defines `kwargs` with annotation `dict[str, object]` from `{'parcels': _parcels(), 'electricity_source': _electricity_source(), 'source_config': SOURCE_CONFIG}`.
- Computes `kwargs[argument]` from `pd.DataFrame() if argument == 'parcels' else object()`.
- Enters managed context(s) `patch('landscout.stages.enrich_grid_proximity.normalize_ign_electricity', create=True), pytest.raises(GridProximityError)` and executes: Calls `public_enrich_parcel_grid_proximity(**cast(Any, kwargs))` for its validation or side effect.

**Action**

- Calls `_electricity_source`, `_parcels`, `cast`, `normalizer.assert_not_called`, `object`, `pd.DataFrame`, `public_enrich_parcel_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with patch('landscout.stages.enrich_grid_proximity.normalize_ign_electricity', create=True) as normalizer, pytest.raises(GridProximityError): public_enrich_parcel_grid_proximity(**cast(Any, kwargs))`.

**Regression protected**

- Protects the exact `public proximity rejects wrong source boundary types` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_electricity_source`, `_parcels`, `cast`, `normalizer.assert_not_called`, `object`, `patch`, `pd.DataFrame`, `public_enrich_parcel_grid_proximity`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_caller_crafted_normalized_grid_frame_is_not_a_public_source`

**Signature**

```python
def test_caller_crafted_normalized_grid_frame_is_not_a_public_source() -> None:
```

**Purpose**

Protects the `caller crafted normalized grid frame is not a public source` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `forged_lines` from `_lines([LineString([(10, -20), (10, 30)])], identifiers=['IGN_BDTOPO:ELECTRIC_LINE:FORGED'])`.
- Enters managed context(s) `patch('landscout.stages.enrich_grid_proximity.normalize_ign_electricity', create=True), pytest.raises(GridProximityError, match='IgnBdTopoElectricityData|electricity source')` and executes: Calls `public_enrich_parcel_grid_proximity(_parcels(), cast(Any, forged_lines), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `LineString`, `_lines`, `_parcels`, `cast`, `forged_lines['source_archive_sha256'].eq`, `forged_lines['source_archive_sha256'].eq('a' * 64).all`, `forged_lines['source_department_code'].eq`, `forged_lines['source_department_code'].eq('31').all`, `forged_lines['source_edition'].eq`, `forged_lines['source_edition'].eq('2026-06-15').all`, `forged_lines['spatial_role'].eq`, `forged_lines['spatial_role'].eq('PROXY_GEOMETRY').all`, `normalizer.assert_not_called`, `public_enrich_parcel_grid_proximity`.

**Expected result**

- Direct assertions: `assert forged_lines['source_department_code'].eq('31').all()`; `assert forged_lines['source_edition'].eq('2026-06-15').all()`; `assert forged_lines['source_archive_sha256'].eq('a' * 64).all()`; `assert forged_lines['spatial_role'].eq('PROXY_GEOMETRY').all()`.
- Expected exception contexts: `with patch('landscout.stages.enrich_grid_proximity.normalize_ign_electricity', create=True) as normalizer, pytest.raises(GridProximityError, match='IgnBdTopoElectricityData|electricity source'): public_enrich_parcel_grid_proximity(_parcels(), cast(Any, forged_lines), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `caller crafted normalized grid frame is not a public source` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks; actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `_lines`, `_parcels`, `cast`, `forged_lines['source_archive_sha256'].eq`, `forged_lines['source_archive_sha256'].eq('a' * 64).all`, `forged_lines['source_department_code'].eq`, `forged_lines['source_department_code'].eq('31').all`, `forged_lines['source_edition'].eq`, `forged_lines['source_edition'].eq('2026-06-15').all`, `forged_lines['spatial_role'].eq`, `forged_lines['spatial_role'].eq('PROXY_GEOMETRY').all`, `normalizer.assert_not_called`, `patch`, `public_enrich_parcel_grid_proximity`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_proximity_reproduces_configured_electricity_roles`

**Signature**

```python
def test_public_proximity_reproduces_configured_electricity_roles(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `public proximity reproduces configured electricity roles` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `forged` from `_alternate_role_electricity_source(tmp_path)`.
- Enters managed context(s) `pytest.raises(GridProximityError)` and executes: Calls `public_enrich_parcel_grid_proximity(_parcels(), forged, SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_alternate_role_electricity_source`, `_parcels`, `public_enrich_parcel_grid_proximity`.

**Expected result**

- Direct assertions: `assert forged.extraction.electric_lines_layer == 'CABLE_SOURCE_ALTERNATE'`; `assert forged.extraction.transformation_posts_layer == 'INSTALLATION_SOURCE_ALTERNATE'`.
- Expected exception contexts: `with pytest.raises(GridProximityError): public_enrich_parcel_grid_proximity(_parcels(), forged, SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `public proximity reproduces configured electricity roles` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_alternate_role_electricity_source`, `_parcels`, `public_enrich_parcel_grid_proximity`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_proximity_rejects_archive_lineage_differing_from_config`

**Signature**

```python
def test_public_proximity_rejects_archive_lineage_differing_from_config(
    tmp_path: Path,
    archive_changes: dict[str, object],
) -> None:
```

**Purpose**

Protects the `public proximity rejects archive lineage differing from config` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `archive_changes`.
- Contains 4 explicit setup/context statement(s).
- Computes `source` from `_configured_role_electricity_source(tmp_path)`.
- Computes `forged_archive` from `replace(source.extraction.archive, **archive_changes)`.
- Computes `forged` from `replace(source, extraction=replace(source.extraction, archive=forged_archive))`.
- Enters managed context(s) `patch('landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized'), pytest.raises(GridProximityError)` and executes: Calls `public_enrich_parcel_grid_proximity(_parcels(), forged, SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_configured_role_electricity_source`, `_parcels`, `computation.assert_not_called`, `public_enrich_parcel_grid_proximity`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with patch('landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized') as computation, pytest.raises(GridProximityError): public_enrich_parcel_grid_proximity(_parcels(), forged, SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `public proximity rejects archive lineage differing from config` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_configured_role_electricity_source`, `_parcels`, `computation.assert_not_called`, `patch`, `public_enrich_parcel_grid_proximity`, `pytest.mark.parametrize`, `pytest.param`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_normalization_failure_stops_grid_computation`

**Signature**

```python
def test_source_normalization_failure_stops_grid_computation() -> None:
```

**Purpose**

Protects the `source normalization failure stops grid computation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `source` from `_electricity_source()`.
- Enters managed context(s) `patch('landscout.stages.enrich_grid_proximity.normalize_ign_electricity', side_effect=ValueError('physical source changed'), create=True), pytest.raises(GridProximityError)` and executes: Calls `public_enrich_parcel_grid_proximity(_parcels(), source, SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `ValueError`, `_electricity_source`, `_parcels`, `normalizer.assert_called_once_with`, `public_enrich_parcel_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with patch('landscout.stages.enrich_grid_proximity.normalize_ign_electricity', side_effect=ValueError('physical source changed'), create=True) as normalizer, pytest.raises(GridProximityError): public_enrich_parcel_grid_proximity(_parcels(), source, SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `source normalization failure stops grid computation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `ValueError`, `_electricity_source`, `_parcels`, `normalizer.assert_called_once_with`, `patch`, `public_enrich_parcel_grid_proximity`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_separated_distance_uses_parcel_edge_not_centroid`

**Signature**

```python
def test_separated_distance_uses_parcel_edge_not_centroid() -> None:
```

**Purpose**

Protects the `separated distance uses parcel edge not centroid` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `result` from `enrich_parcel_grid_proximity(_parcels(), _lines(), _posts())`.

**Action**

- Calls `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`.

**Expected result**

- Direct assertions: `assert result.parcels.loc[0, 'nearest_line_proxy_distance_m'] == pytest.approx(100.0)`; `assert result.parcels.loc[0, 'nearest_post_proxy_distance_m'] == pytest.approx(100.0)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `separated distance uses parcel edge not centroid` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_touching_line_has_zero_distance`

**Signature**

```python
def test_touching_line_has_zero_distance() -> None:
```

**Purpose**

Protects the `touching line has zero distance` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `touching` from `_lines([LineString([(10, -20), (10, 30)])])`.
- Computes `result` from `enrich_parcel_grid_proximity(_parcels(), touching, _posts())`.

**Action**

- Calls `LineString`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`.

**Expected result**

- Direct assertions: `assert result.parcels.loc[0, 'nearest_line_proxy_distance_m'] == 0.0`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `touching line has zero distance` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_post_distance_uses_parcel_and_post_polygons`

**Signature**

```python
def test_post_distance_uses_parcel_and_post_polygons() -> None:
```

**Purpose**

Protects the `post distance uses parcel and post polygons` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `posts` from `_posts([Polygon([(60, 0), (60, 10), (70, 10), (70, 0), (60, 0)])])`.
- Computes `result` from `enrich_parcel_grid_proximity(_parcels(), _lines(), posts)`.

**Action**

- Calls `Polygon`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`.

**Expected result**

- Direct assertions: `assert result.parcels.loc[0, 'nearest_post_proxy_distance_m'] == pytest.approx(50.0)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `post distance uses parcel and post polygons` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_epsg4326_input_is_calculated_in_lambert93_and_preserved`

**Signature**

```python
def test_epsg4326_input_is_calculated_in_lambert93_and_preserved() -> None:
```

**Purpose**

Protects the `epsg4326 input is calculated in lambert93 and preserved` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `projected` from `_parcels()`.
- Computes `geographic` from `projected.to_crs('EPSG:4326')`.
- Computes `before_geometry` from `geographic.geometry.copy()`.
- Computes `result` from `enrich_parcel_grid_proximity(geographic, _lines(), _posts())`.

**Action**

- Calls `_lines`, `_parcels`, `_posts`, `before_geometry.reset_index`, `enrich_parcel_grid_proximity`, `geographic.geometry.copy`, `projected.to_crs`, `result.parcels.geometry.geom_equals_exact`, `result.parcels.geometry.geom_equals_exact(before_geometry.reset_index(drop=True), tolerance=0).all`.

**Expected result**

- Direct assertions: `assert result.parcels.crs == geographic.crs`; `assert result.parcels.loc[0, 'nearest_line_proxy_distance_m'] == pytest.approx(100.0, abs=1e-06)`; `assert result.parcels.geometry.geom_equals_exact(before_geometry.reset_index(drop=True), tolerance=0).all()`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `epsg4326 input is calculated in lambert93 and preserved` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_lines`, `_parcels`, `_posts`, `before_geometry.reset_index`, `enrich_parcel_grid_proximity`, `geographic.geometry.copy`, `projected.to_crs`, `pytest.approx`, `result.parcels.geometry.geom_equals_exact`, `result.parcels.geometry.geom_equals_exact(before_geometry.reset_index(drop=True), tolerance=0).all`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_epsg2154_parcel_input_remains_epsg2154`

**Signature**

```python
def test_epsg2154_parcel_input_remains_epsg2154() -> None:
```

**Purpose**

Protects the `epsg2154 parcel input remains epsg2154` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `result` from `enrich_parcel_grid_proximity(_parcels(), _lines(), _posts())`.

**Action**

- Calls `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `result.parcels.crs.to_epsg`.

**Expected result**

- Direct assertions: `assert result.parcels.crs is not None`; `assert result.parcels.crs.to_epsg() == 2154`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `epsg2154 parcel input remains epsg2154` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `result.parcels.crs.to_epsg`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_parcel_id_is_preserved_exactly`

**Signature**

```python
def test_valid_parcel_id_is_preserved_exactly() -> None:
```

**Purpose**

Protects the `valid parcel id is preserved exactly` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `result` from `enrich_parcel_grid_proximity(_parcels(identifiers=['FR-31-VALID-ID']), _lines(), _posts())`.

**Action**

- Calls `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `result.parcels['parcel_id'].tolist`.

**Expected result**

- Direct assertions: `assert result.parcels['parcel_id'].tolist() == ['FR-31-VALID-ID']`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `valid parcel id is preserved exactly` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `result.parcels['parcel_id'].tolist`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_parcel_id_hygiene_is_rejected`

**Signature**

```python
def test_invalid_parcel_id_hygiene_is_rejected(identifier: object) -> None:
```

**Purpose**

Protects the `invalid parcel id hygiene is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `identifier`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(GridProximityError, match='parcel_id')` and executes: Calls `enrich_parcel_grid_proximity(_parcels(identifiers=[identifier]), _lines(), _posts())` for its validation or side effect.

**Action**

- Calls `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='parcel_id'): enrich_parcel_grid_proximity(_parcels(identifiers=[identifier]), _lines(), _posts())`.

**Regression protected**

- Protects the exact `invalid parcel id hygiene is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_supported_parcel_polygon_geometry_is_preserved`

**Signature**

```python
def test_supported_parcel_polygon_geometry_is_preserved(geometry: object) -> None:
```

**Purpose**

Protects the `supported parcel polygon geometry is preserved` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry`.
- Contains 1 explicit setup/context statement(s).
- Computes `result` from `enrich_parcel_grid_proximity(_parcels([geometry]), _lines(), _posts())`.

**Action**

- Calls `MultiPolygon`, `Polygon`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `result.parcels.geometry.iloc[0].equals_exact`.

**Expected result**

- Direct assertions: `assert result.parcels.geometry.iloc[0].equals_exact(geometry, tolerance=0)`; `assert result.parcels.geometry.iloc[0].has_z == geometry.has_z`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `supported parcel polygon geometry is preserved` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `MultiPolygon`, `Polygon`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `pytest.mark.parametrize`, `result.parcels.geometry.iloc[0].equals_exact`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_semantically_wrong_parcel_geometry_is_rejected`

**Signature**

```python
def test_semantically_wrong_parcel_geometry_is_rejected(geometry: object) -> None:
```

**Purpose**

Protects the `semantically wrong parcel geometry is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(GridProximityError, match='Polygon|MultiPolygon')` and executes: Calls `enrich_parcel_grid_proximity(_parcels([geometry]), _lines(), _posts())` for its validation or side effect.

**Action**

- Calls `GeometryCollection`, `LineString`, `MultiLineString`, `Point`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='Polygon|MultiPolygon'): enrich_parcel_grid_proximity(_parcels([geometry]), _lines(), _posts())`.

**Regression protected**

- Protects the exact `semantically wrong parcel geometry is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `GeometryCollection`, `LineString`, `MultiLineString`, `Point`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_crs_is_rejected`

**Signature**

```python
def test_missing_crs_is_rejected(kind: str) -> None:
```

**Purpose**

Protects the `missing crs is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `kind`.
- Contains 4 explicit setup/context statement(s).
- Computes `parcels` from `_parcels(crs=None if kind == 'parcel' else 'EPSG:2154')`.
- Computes `lines` from `_lines(crs=None if kind == 'line' else 'EPSG:2154')`.
- Computes `posts` from `_posts(crs=None if kind == 'post' else 'EPSG:2154')`.
- Enters managed context(s) `pytest.raises(GridProximityError, match='CRS')` and executes: Calls `enrich_parcel_grid_proximity(parcels, lines, posts)` for its validation or side effect.

**Action**

- Calls `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='CRS'): enrich_parcel_grid_proximity(parcels, lines, posts)`.

**Regression protected**

- Protects the exact `missing crs is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_wrong_grid_crs_is_rejected`

**Signature**

```python
def test_wrong_grid_crs_is_rejected(kind: str) -> None:
```

**Purpose**

Protects the `wrong grid crs is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `kind`.
- Contains 3 explicit setup/context statement(s).
- Computes `lines` from `_lines(crs='EPSG:4326' if kind == 'line' else 'EPSG:2154')`.
- Computes `posts` from `_posts(crs='EPSG:4326' if kind == 'post' else 'EPSG:2154')`.
- Enters managed context(s) `pytest.raises(GridProximityError, match='2154')` and executes: Calls `enrich_parcel_grid_proximity(_parcels(), lines, posts)` for its validation or side effect.

**Action**

- Calls `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='2154'): enrich_parcel_grid_proximity(_parcels(), lines, posts)`.

**Regression protected**

- Protects the exact `wrong grid crs is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_z_line_has_same_horizontal_distance_as_xy_line`

**Signature**

```python
def test_z_line_has_same_horizontal_distance_as_xy_line() -> None:
```

**Purpose**

Protects the `z line has same horizontal distance as xy line` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `xy` from `_lines([LineString([(110, -20), (110, 30)])])`.
- Computes `xyz` from `_lines([LineString([(110, -20, 500), (110, 30, 900)])])`.
- Computes `xy_result` from `enrich_parcel_grid_proximity(_parcels(), xy, _posts())`.
- Computes `xyz_result` from `enrich_parcel_grid_proximity(_parcels(), xyz, _posts())`.

**Action**

- Calls `LineString`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`.

**Expected result**

- Direct assertions: `assert xyz.geometry.iloc[0].has_z`; `assert xyz_result.parcels.loc[0, 'nearest_line_proxy_distance_m'] == pytest.approx(xy_result.parcels.loc[0, 'nearest_line_proxy_distance_m'])`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `z line has same horizontal distance as xy line` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_line_tie_is_counted_and_lexical_feature_id_wins`

**Signature**

```python
def test_line_tie_is_counted_and_lexical_feature_id_wins() -> None:
```

**Purpose**

Protects the `line tie is counted and lexical feature id wins` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `lines` from `_lines([LineString([(-100, -20), (-100, 30)]), LineString([(110, -20), (110, 30)])], identifiers=['Z-LINE', 'A-LINE'])`.
- Computes `result` from `enrich_parcel_grid_proximity(_parcels(), lines, _posts())`.
- Computes `row` from `result.parcels.iloc[0]`.

**Action**

- Calls `LineString`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`.

**Expected result**

- Direct assertions: `assert row['nearest_line_proxy_distance_m'] == pytest.approx(100.0)`; `assert row['nearest_line_tie_count'] == 2`; `assert row['nearest_line_grid_feature_id'] == 'A-LINE'`; `assert row['nearest_exact_line_tie_count'] == 2`; `assert row['nearest_exact_line_grid_feature_id'] == 'A-LINE'`; `assert result.voltage_level_proximity.loc[0, 'tie_count'] == 2`; `assert result.voltage_level_proximity.loc[0, 'nearest_line_grid_feature_id'] == 'A-LINE'`; `assert len(result.parcels) == 1`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `line tie is counted and lexical feature id wins` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `len`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_cross_voltage_tie_uses_lexical_global_feature_id`

**Signature**

```python
def test_cross_voltage_tie_uses_lexical_global_feature_id() -> None:
```

**Purpose**

Protects the `cross voltage tie uses lexical global feature id` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `lines` from `_lines([LineString([(-100, -20), (-100, 30)]), LineString([(110, -20), (110, 30)])], identifiers=['Z-LINE-110', 'A-LINE-275'], voltage_statuses=['EXACT', 'EXACT'], voltages=[110.0, 275.0])`.
- Computes `result` from `enrich_parcel_grid_proximity(_parcels(), lines, _posts())`.
- Computes `profile` from `profile_grid_proximity(result)`.
- Computes `row` from `result.parcels.iloc[0]`.

**Action**

- Calls `LineString`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `profile_grid_proximity`, `result.voltage_level_proximity['nearest_line_proxy_distance_m'].tolist`, `result.voltage_level_proximity['tie_count'].tolist`.

**Expected result**

- Direct assertions: `assert row['nearest_exact_line_proxy_distance_m'] == pytest.approx(100.0)`; `assert row['nearest_exact_line_grid_feature_id'] == 'A-LINE-275'`; `assert row['nearest_exact_line_voltage_kv'] == 275.0`; `assert row['nearest_exact_line_tie_count'] == 2`; `assert result.voltage_level_proximity['nearest_line_proxy_distance_m'].tolist() == pytest.approx([100.0, 100.0])`; `assert result.voltage_level_proximity['tie_count'].tolist() == [1, 1]`; `assert profile.nearest_exact_line.tie_count == 1`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `cross voltage tie uses lexical global feature id` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `profile_grid_proximity`, `pytest.approx`, `result.voltage_level_proximity['nearest_line_proxy_distance_m'].tolist`, `result.voltage_level_proximity['tie_count'].tolist`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_nonvalid_grid_geometries_are_excluded_without_row_loss`

**Signature**

```python
def test_nonvalid_grid_geometries_are_excluded_without_row_loss() -> None:
```

**Purpose**

Protects the `nonvalid grid geometries are excluded without row loss` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `invalid` from `Polygon([(0, 0), (20, 20), (20, 0), (0, 20), (0, 0)])`.
- Computes `lines` from `_lines([None, LineString(), invalid, LineString([(110, -20), (110, 30)])], identifiers=['NULL', 'EMPTY', 'INVALID', 'VALID'], voltage_statuses=['UNKNOWN', 'UNKNOWN', 'UNKNOWN', 'EXACT'], voltages=[None, None, None, 110.0])`.
- Computes `result` from `enrich_parcel_grid_proximity(_parcels(), lines, _posts())`.

**Action**

- Calls `LineString`, `Polygon`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`.

**Expected result**

- Direct assertions: `assert len(result.parcels) == 1`; `assert result.parcels.loc[0, 'nearest_line_grid_feature_id'] == 'VALID'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `nonvalid grid geometries are excluded without row loss` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `Polygon`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `len`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_wrong_grid_feature_type_is_rejected`

**Signature**

```python
def test_wrong_grid_feature_type_is_rejected(kind: str) -> None:
```

**Purpose**

Protects the `wrong grid feature type is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `kind`.
- Contains 3 explicit setup/context statement(s).
- Computes `lines` from `_lines(feature_types=['WRONG'] if kind == 'line' else None)`.
- Computes `posts` from `_posts(feature_types=['WRONG'] if kind == 'post' else None)`.
- Enters managed context(s) `pytest.raises(GridProximityError, match='grid_feature_type')` and executes: Calls `enrich_parcel_grid_proximity(_parcels(), lines, posts)` for its validation or side effect.

**Action**

- Calls `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='grid_feature_type'): enrich_parcel_grid_proximity(_parcels(), lines, posts)`.

**Regression protected**

- Protects the exact `wrong grid feature type is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_grid_feature_id_is_rejected`

**Signature**

```python
def test_duplicate_grid_feature_id_is_rejected(kind: str) -> None:
```

**Purpose**

Protects the `duplicate grid feature id is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `kind`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(GridProximityError, match='unique')` and executes: Calls `enrich_parcel_grid_proximity(_parcels(), lines, posts)` for its validation or side effect.

**Action**

- Calls `LineString`, `Polygon`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='unique'): enrich_parcel_grid_proximity(_parcels(), lines, posts)`.

**Regression protected**

- Protects the exact `duplicate grid feature id is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `Polygon`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_wrong_spatial_role_is_rejected`

**Signature**

```python
def test_wrong_spatial_role_is_rejected(kind: str) -> None:
```

**Purpose**

Protects the `wrong spatial role is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `kind`.
- Contains 3 explicit setup/context statement(s).
- Computes `lines` from `_lines(spatial_roles=['EXACT'] if kind == 'line' else None)`.
- Computes `posts` from `_posts(spatial_roles=['EXACT'] if kind == 'post' else None)`.
- Enters managed context(s) `pytest.raises(GridProximityError, match='PROXY_GEOMETRY')` and executes: Calls `enrich_parcel_grid_proximity(_parcels(), lines, posts)` for its validation or side effect.

**Action**

- Calls `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='PROXY_GEOMETRY'): enrich_parcel_grid_proximity(_parcels(), lines, posts)`.

**Regression protected**

- Protects the exact `wrong spatial role is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unsupported_valid_grid_geometry_type_is_rejected`

**Signature**

```python
def test_unsupported_valid_grid_geometry_type_is_rejected(
    kind: str, geometry: object
) -> None:
```

**Purpose**

Protects the `unsupported valid grid geometry type is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `kind`, `geometry`.
- Contains 3 explicit setup/context statement(s).
- Computes `lines` from `_lines([geometry]) if kind == 'line' else _lines()`.
- Computes `posts` from `_posts([geometry]) if kind == 'post' else _posts()`.
- Enters managed context(s) `pytest.raises(GridProximityError, match='geometry types')` and executes: Calls `enrich_parcel_grid_proximity(_parcels(), lines, posts)` for its validation or side effect.

**Action**

- Calls `LineString`, `Point`, `Polygon`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='geometry types'): enrich_parcel_grid_proximity(_parcels(), lines, posts)`.

**Regression protected**

- Protects the exact `unsupported valid grid geometry type is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `Point`, `Polygon`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_supported_multi_geometries_are_accepted`

**Signature**

```python
def test_supported_multi_geometries_are_accepted() -> None:
```

**Purpose**

Protects the `supported multi geometries are accepted` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `lines` from `_lines([MultiLineString([[(110, -20), (110, 30)], [(120, -20), (120, 30)]])])`.
- Computes `posts` from `_posts([MultiPolygon([Polygon([(110, 0), (110, 5), (115, 5), (115, 0), (110, 0)])])])`.
- Computes `result` from `enrich_parcel_grid_proximity(_parcels(), lines, posts)`.

**Action**

- Calls `MultiLineString`, `MultiPolygon`, `Polygon`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`.

**Expected result**

- Direct assertions: `assert len(result.parcels) == 1`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `supported multi geometries are accepted` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `MultiLineString`, `MultiPolygon`, `Polygon`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `len`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_nearest_any_line_preserves_every_voltage_status`

**Signature**

```python
def test_nearest_any_line_preserves_every_voltage_status(status: str) -> None:
```

**Purpose**

Protects the `nearest any line preserves every voltage status` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `status`.
- Contains 3 explicit setup/context statement(s).
- Computes `voltage` from `110.0 if status == 'EXACT' else None`.
- Computes `lines` from `_lines(voltage_statuses=[status], voltages=[voltage])`.
- Computes `result` from `enrich_parcel_grid_proximity(_parcels(), lines, _posts())`.

**Action**

- Calls `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`.

**Expected result**

- Direct assertions: `assert result.parcels.loc[0, 'nearest_line_voltage_status'] == status`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `nearest any line preserves every voltage status` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_nearest_exact_and_voltage_table_exclude_nonexact_lines`

**Signature**

```python
def test_nearest_exact_and_voltage_table_exclude_nonexact_lines() -> None:
```

**Purpose**

Protects the `nearest exact and voltage table exclude nonexact lines` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `lines` from `_lines([LineString([(20, -20), (20, 30)]), LineString([(110, -20), (110, 30)]), LineString([(210, -20), (210, 30)])], identifiers=['BELOW', 'EXACT-110', 'EXACT-275'], voltage_statuses=['BELOW', 'EXACT', 'EXACT'], voltages=[None, 110.0, 275.0])`.
- Computes `result` from `enrich_parcel_grid_proximity(_parcels(), lines, _posts())`.
- Computes `row` from `result.parcels.iloc[0]`.

**Action**

- Calls `LineString`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `result.voltage_level_proximity['voltage_kv'].tolist`.

**Expected result**

- Direct assertions: `assert row['nearest_line_grid_feature_id'] == 'BELOW'`; `assert row['nearest_exact_line_grid_feature_id'] == 'EXACT-110'`; `assert row['nearest_exact_line_voltage_kv'] == 110.0`; `assert result.voltage_level_proximity['voltage_kv'].tolist() == [110.0, 275.0]`; `assert len(result.voltage_level_proximity) == 2`; `assert list(result.voltage_level_proximity.columns) == list(VOLTAGE_PROXIMITY_COLUMNS)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `nearest exact and voltage table exclude nonexact lines` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `len`, `list`, `result.voltage_level_proximity['voltage_kv'].tolist`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_voltage_table_is_exact_ordered_cartesian_product`

**Signature**

```python
def test_voltage_table_is_exact_ordered_cartesian_product() -> None:
```

**Purpose**

Protects the `voltage table is exact ordered cartesian product` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `result` from `_two_parcel_two_voltage_result()`.

**Action**

- Calls `_two_parcel_two_voltage_result`, `result.voltage_level_proximity.duplicated`, `result.voltage_level_proximity.duplicated(['parcel_id', 'voltage_kv']).any`, `rows['parcel_id'].tolist`.

**Expected result**

- Direct assertions: `assert tuple((item.voltage_kv for item in result.voltage_level_coverage)) == (110.0, 275.0)`; `assert len(result.voltage_level_proximity) == 4`; `assert not result.voltage_level_proximity.duplicated(['parcel_id', 'voltage_kv']).any()`; `assert rows['parcel_id'].tolist() == ['PARCEL-2', 'PARCEL-1']`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `voltage table is exact ordered cartesian product` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_two_parcel_two_voltage_result`, `len`, `result.voltage_level_proximity.duplicated`, `result.voltage_level_proximity.duplicated(['parcel_id', 'voltage_kv']).any`, `rows['parcel_id'].tolist`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_exact_voltage_values_are_not_used_as_exact`

**Signature**

```python
def test_invalid_exact_voltage_values_are_not_used_as_exact() -> None:
```

**Purpose**

Protects the `invalid exact voltage values are not used as exact` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `lines` from `_lines([LineString([(20, -20), (20, 30)])] * 4, identifiers=['ZERO', 'NEGATIVE', 'INFINITE', 'TEXT'], voltage_statuses=['EXACT'] * 4, voltages=[0.0, -1.0, float('inf'), '110'])`.
- Computes `result` from `enrich_parcel_grid_proximity(_parcels(), lines, _posts())`.

**Action**

- Calls `LineString`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `float`, `result.parcels['nearest_exact_line_proxy_distance_m'].isna`, `result.parcels['nearest_exact_line_proxy_distance_m'].isna().all`.

**Expected result**

- Direct assertions: `assert result.parcels['nearest_exact_line_proxy_distance_m'].isna().all()`; `assert result.voltage_level_proximity.empty`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `invalid exact voltage values are not used as exact` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `float`, `result.parcels['nearest_exact_line_proxy_distance_m'].isna`, `result.parcels['nearest_exact_line_proxy_distance_m'].isna().all`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table`

**Signature**

```python
def test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table() -> None:
```

**Purpose**

Protects the `no exact voltage preserves parcels and returns empty long table` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `lines` from `_lines(voltage_statuses=['UNKNOWN'], voltages=[None])`.
- Computes `result` from `enrich_parcel_grid_proximity(_parcels(), lines, _posts())`.
- Computes `profile` from `profile_grid_proximity(result)`.

**Action**

- Calls `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `is_float_dtype`, `is_integer_dtype`, `profile_grid_proximity`, `result.parcels['nearest_exact_line_grid_feature_id'].isna`, `result.parcels['nearest_exact_line_grid_feature_id'].isna().all`, `result.parcels['nearest_exact_line_proxy_distance_m'].isna`, `result.parcels['nearest_exact_line_proxy_distance_m'].isna().all`.

**Expected result**

- Direct assertions: `assert result.parcels.loc[0, 'nearest_line_grid_feature_id'] == 'LINE-1'`; `assert result.parcels['nearest_exact_line_proxy_distance_m'].isna().all()`; `assert result.parcels['nearest_exact_line_grid_feature_id'].isna().all()`; `assert result.voltage_level_proximity.empty`; `assert list(result.voltage_level_proximity.columns) == list(VOLTAGE_PROXIMITY_COLUMNS)`; `assert is_float_dtype(result.parcels['nearest_exact_line_proxy_distance_m'].dtype)`; `assert is_float_dtype(result.parcels['nearest_exact_line_voltage_kv'].dtype)`; `assert is_integer_dtype(result.parcels['nearest_exact_line_tie_count'].dtype)`; `assert str(result.parcels['nearest_exact_line_tie_count'].dtype) == 'Int64'`; `assert is_float_dtype(result.voltage_level_proximity['voltage_kv'].dtype)`; `assert is_float_dtype(result.voltage_level_proximity['nearest_line_proxy_distance_m'].dtype)`; `assert str(result.voltage_level_proximity['tie_count'].dtype) == 'Int64'`; `assert result.voltage_level_coverage == ()`; `assert profile.nearest_exact_line.count == 0`; `assert profile.nearest_exact_line.missing_count == 1`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `no exact voltage preserves parcels and returns empty long table` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `is_float_dtype`, `is_integer_dtype`, `list`, `profile_grid_proximity`, `result.parcels['nearest_exact_line_grid_feature_id'].isna`, `result.parcels['nearest_exact_line_grid_feature_id'].isna().all`, `result.parcels['nearest_exact_line_proxy_distance_m'].isna`, `result.parcels['nearest_exact_line_proxy_distance_m'].isna().all`, `str`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_parcel_column_is_rejected`

**Signature**

```python
def test_missing_parcel_column_is_rejected(column: str) -> None:
```

**Purpose**

Protects the `missing parcel column is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`.
- Contains 2 explicit setup/context statement(s).
- Computes `parcels` from `_parcels().drop(columns=column)`.
- Enters managed context(s) `pytest.raises(GridProximityError, match=column)` and executes: Calls `enrich_parcel_grid_proximity(parcels, _lines(), _posts())` for its validation or side effect.

**Action**

- Calls `_lines`, `_parcels`, `_parcels().drop`, `_posts`, `enrich_parcel_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match=column): enrich_parcel_grid_proximity(parcels, _lines(), _posts())`.

**Regression protected**

- Protects the exact `missing parcel column is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_lines`, `_parcels`, `_parcels().drop`, `_posts`, `enrich_parcel_grid_proximity`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_null_parcel_id_is_rejected`

**Signature**

```python
def test_null_parcel_id_is_rejected() -> None:
```

**Purpose**

Protects the `null parcel id is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(GridProximityError, match='parcel_id')` and executes: Calls `enrich_parcel_grid_proximity(_parcels(identifiers=[None]), _lines(), _posts())` for its validation or side effect.

**Action**

- Calls `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='parcel_id'): enrich_parcel_grid_proximity(_parcels(identifiers=[None]), _lines(), _posts())`.

**Regression protected**

- Protects the exact `null parcel id is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_parcel_id_is_rejected`

**Signature**

```python
def test_duplicate_parcel_id_is_rejected() -> None:
```

**Purpose**

Protects the `duplicate parcel id is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `parcels` from `_parcels([Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]), Polygon([(20, 0), (20, 10), (30, 10), (30, 0), (20, 0)])], identifiers=['DUPLICATE', 'DUPLICATE'])`.
- Enters managed context(s) `pytest.raises(GridProximityError, match='unique')` and executes: Calls `enrich_parcel_grid_proximity(parcels, _lines(), _posts())` for its validation or side effect.

**Action**

- Calls `Polygon`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='unique'): enrich_parcel_grid_proximity(parcels, _lines(), _posts())`.

**Regression protected**

- Protects the exact `duplicate parcel id is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_bad_parcel_geometry_is_rejected`

**Signature**

```python
def test_bad_parcel_geometry_is_rejected(geometry: object, message: str) -> None:
```

**Purpose**

Protects the `bad parcel geometry is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry`, `message`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(GridProximityError, match=message)` and executes: Calls `enrich_parcel_grid_proximity(_parcels([geometry]), _lines(), _posts())` for its validation or side effect.

**Action**

- Calls `Polygon`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match=message): enrich_parcel_grid_proximity(_parcels([geometry]), _lines(), _posts())`.

**Regression protected**

- Protects the exact `bad parcel geometry is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved`

**Signature**

```python
def test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved() -> None:
```

**Purpose**

Protects the `inputs are not mutated and parcel order and ids are preserved` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 7 explicit setup/context statement(s).
- Computes `parcels` from `_parcels([Polygon([(20, 0), (20, 10), (30, 10), (30, 0), (20, 0)]), Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])], identifiers=['SECOND-SPATIAL', 'FIRST-SPATIAL'], index=[99, 99])`.
- Computes `lines` from `_lines()`.
- Computes `posts` from `_posts()`.
- Computes `parcels_before` from `deepcopy(parcels)`.
- Computes `lines_before` from `deepcopy(lines)`.
- Computes `posts_before` from `deepcopy(posts)`.
- Computes `result` from `enrich_parcel_grid_proximity(parcels, lines, posts)`.

**Action**

- Calls `Polygon`, `_lines`, `_parcels`, `_posts`, `deepcopy`, `enrich_parcel_grid_proximity`, `isinstance`, `result.parcels['parcel_id'].tolist`.

**Expected result**

- Direct assertions: `assert result.parcels['parcel_id'].tolist() == ['SECOND-SPATIAL', 'FIRST-SPATIAL']`; `assert isinstance(result.parcels.index, pd.RangeIndex)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `inputs are not mutated and parcel order and ids are preserved` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `_lines`, `_parcels`, `_posts`, `assert_geodataframe_equal`, `deepcopy`, `enrich_parcel_grid_proximity`, `isinstance`, `result.parcels['parcel_id'].tolist`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_distance_profile_is_threshold_free_and_tracks_ties`

**Signature**

```python
def test_distance_profile_is_threshold_free_and_tracks_ties() -> None:
```

**Purpose**

Protects the `distance profile is threshold free and tracks ties` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `parcels` from `_parcels([Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]), Polygon([(50, 0), (50, 10), (60, 10), (60, 0), (50, 0)])])`.
- Computes `lines` from `_lines([LineString([(-100, -20), (-100, 30)]), LineString([(110, -20), (110, 30)])], identifiers=['Z-LINE', 'A-LINE'])`.
- Computes `result` from `enrich_parcel_grid_proximity(parcels, lines, _posts())`.
- Computes `profile` from `profile_grid_proximity(result)`.

**Action**

- Calls `LineString`, `Polygon`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `profile_grid_proximity`.

**Expected result**

- Direct assertions: `assert profile.parcel_count == 2`; `assert profile.nearest_line.count == 2`; `assert profile.nearest_line.missing_count == 0`; `assert profile.nearest_line.minimum == pytest.approx(50.0)`; `assert profile.nearest_line.p50 == pytest.approx(75.0)`; `assert profile.nearest_line.maximum == pytest.approx(100.0)`; `assert profile.nearest_line.tie_count == 1`; `assert profile.voltage_levels[0].voltage_kv == 110.0`; `assert profile.voltage_levels[0].line_feature_count == 2`; `assert profile.voltage_levels[0].parcel_proximity_count == 2`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `distance profile is threshold free and tracks ties` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `Polygon`, `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `profile_grid_proximity`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_profile_rejects_missing_voltage_cartesian_row`

**Signature**

```python
def test_profile_rejects_missing_voltage_cartesian_row() -> None:
```

**Purpose**

Protects the `profile rejects missing voltage cartesian row` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `result` from `_two_parcel_two_voltage_result()`.
- Computes `table` from `result.voltage_level_proximity.iloc[:-1].copy()`.
- Enters managed context(s) `pytest.raises(GridProximityError)` and executes: Calls `profile_grid_proximity(replace(result, voltage_level_proximity=table))` for its validation or side effect.

**Action**

- Calls `_two_parcel_two_voltage_result`, `profile_grid_proximity`, `replace`, `result.voltage_level_proximity.iloc[:-1].copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError): profile_grid_proximity(replace(result, voltage_level_proximity=table))`.

**Regression protected**

- Protects the exact `profile rejects missing voltage cartesian row` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_two_parcel_two_voltage_result`, `profile_grid_proximity`, `pytest.raises`, `replace`, `result.voltage_level_proximity.iloc[:-1].copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_profile_rejects_unknown_voltage_parcel_with_same_total_count`

**Signature**

```python
def test_profile_rejects_unknown_voltage_parcel_with_same_total_count() -> None:
```

**Purpose**

Protects the `profile rejects unknown voltage parcel with same total count` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `result` from `_two_parcel_two_voltage_result()`.
- Computes `corrupted` from `_mutate_voltage_result(result, 'parcel_id', 'UNKNOWN-PARCEL')`.
- Enters managed context(s) `pytest.raises(GridProximityError)` and executes: Calls `profile_grid_proximity(corrupted)` for its validation or side effect.

**Action**

- Calls `_mutate_voltage_result`, `_two_parcel_two_voltage_result`, `profile_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError): profile_grid_proximity(corrupted)`.

**Regression protected**

- Protects the exact `profile rejects unknown voltage parcel with same total count` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_mutate_voltage_result`, `_two_parcel_two_voltage_result`, `profile_grid_proximity`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_profile_rejects_duplicate_parcel_voltage_pair`

**Signature**

```python
def test_profile_rejects_duplicate_parcel_voltage_pair() -> None:
```

**Purpose**

Protects the `profile rejects duplicate parcel voltage pair` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `result` from `_two_parcel_two_voltage_result()`.
- Computes `table` from `result.voltage_level_proximity.copy()`.
- Computes `table.at[1, 'parcel_id']` from `table.at[0, 'parcel_id']`.
- Enters managed context(s) `pytest.raises(GridProximityError, match='unique')` and executes: Calls `profile_grid_proximity(replace(result, voltage_level_proximity=table))` for its validation or side effect.

**Action**

- Calls `_two_parcel_two_voltage_result`, `profile_grid_proximity`, `replace`, `result.voltage_level_proximity.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='unique'): profile_grid_proximity(replace(result, voltage_level_proximity=table))`.

**Regression protected**

- Protects the exact `profile rejects duplicate parcel voltage pair` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_two_parcel_two_voltage_result`, `profile_grid_proximity`, `pytest.raises`, `replace`, `result.voltage_level_proximity.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_profile_rejects_voltage_rows_out_of_parcel_order`

**Signature**

```python
def test_profile_rejects_voltage_rows_out_of_parcel_order() -> None:
```

**Purpose**

Protects the `profile rejects voltage rows out of parcel order` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `result` from `_two_parcel_two_voltage_result()`.
- Computes `table` from `result.voltage_level_proximity.iloc[[1, 0, 2, 3]].reset_index(drop=True)`.
- Enters managed context(s) `pytest.raises(GridProximityError, match='exact parcel set')` and executes: Calls `profile_grid_proximity(replace(result, voltage_level_proximity=table))` for its validation or side effect.

**Action**

- Calls `_two_parcel_two_voltage_result`, `profile_grid_proximity`, `replace`, `result.voltage_level_proximity.iloc[[1, 0, 2, 3]].reset_index`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='exact parcel set'): profile_grid_proximity(replace(result, voltage_level_proximity=table))`.

**Regression protected**

- Protects the exact `profile rejects voltage rows out of parcel order` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_two_parcel_two_voltage_result`, `profile_grid_proximity`, `pytest.raises`, `replace`, `result.voltage_level_proximity.iloc[[1, 0, 2, 3]].reset_index`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_profile_rejects_inconsistent_global_exact_distance`

**Signature**

```python
def test_profile_rejects_inconsistent_global_exact_distance() -> None:
```

**Purpose**

Protects the `profile rejects inconsistent global exact distance` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_two_parcel_two_voltage_result()`.
- Enters managed context(s) `pytest.raises(GridProximityError, match='exact-line distance')` and executes: Calls `profile_grid_proximity(_mutate_parcel_result(result, 'nearest_exact_line_proxy_distance_m', 5000.0))` for its validation or side effect.

**Action**

- Calls `_mutate_parcel_result`, `_two_parcel_two_voltage_result`, `profile_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='exact-line distance'): profile_grid_proximity(_mutate_parcel_result(result, 'nearest_exact_line_proxy_distance_m', 5000.0))`.

**Regression protected**

- Protects the exact `profile rejects inconsistent global exact distance` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_mutate_parcel_result`, `_two_parcel_two_voltage_result`, `profile_grid_proximity`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_profile_rejects_inconsistent_global_exact_identity`

**Signature**

```python
def test_profile_rejects_inconsistent_global_exact_identity(
    column: str,
    value: object,
) -> None:
```

**Purpose**

Protects the `profile rejects inconsistent global exact identity` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`, `value`.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_two_parcel_two_voltage_result()`.
- Enters managed context(s) `pytest.raises(GridProximityError, match='inconsistent')` and executes: Calls `profile_grid_proximity(_mutate_parcel_result(result, column, value))` for its validation or side effect.

**Action**

- Calls `_mutate_parcel_result`, `_two_parcel_two_voltage_result`, `profile_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='inconsistent'): profile_grid_proximity(_mutate_parcel_result(result, column, value))`.

**Regression protected**

- Protects the exact `profile rejects inconsistent global exact identity` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_mutate_parcel_result`, `_two_parcel_two_voltage_result`, `profile_grid_proximity`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_profile_rejects_inconsistent_global_exact_metadata`

**Signature**

```python
def test_profile_rejects_inconsistent_global_exact_metadata(
    column: str,
    value: object,
) -> None:
```

**Purpose**

Protects the `profile rejects inconsistent global exact metadata` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`, `value`.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_two_parcel_two_voltage_result()`.
- Enters managed context(s) `pytest.raises(GridProximityError, match='inconsistent')` and executes: Calls `profile_grid_proximity(_mutate_parcel_result(result, column, value))` for its validation or side effect.

**Action**

- Calls `_mutate_parcel_result`, `_two_parcel_two_voltage_result`, `profile_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='inconsistent'): profile_grid_proximity(_mutate_parcel_result(result, column, value))`.

**Regression protected**

- Protects the exact `profile rejects inconsistent global exact metadata` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_mutate_parcel_result`, `_two_parcel_two_voltage_result`, `profile_grid_proximity`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_profile_rejects_inconsistent_global_exact_tie_count`

**Signature**

```python
def test_profile_rejects_inconsistent_global_exact_tie_count() -> None:
```

**Purpose**

Protects the `profile rejects inconsistent global exact tie count` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_two_parcel_two_voltage_result()`.
- Enters managed context(s) `pytest.raises(GridProximityError, match='tie count')` and executes: Calls `profile_grid_proximity(_mutate_parcel_result(result, 'nearest_exact_line_tie_count', 2))` for its validation or side effect.

**Action**

- Calls `_mutate_parcel_result`, `_two_parcel_two_voltage_result`, `profile_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='tie count'): profile_grid_proximity(_mutate_parcel_result(result, 'nearest_exact_line_tie_count', 2))`.

**Regression protected**

- Protects the exact `profile rejects inconsistent global exact tie count` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_mutate_parcel_result`, `_two_parcel_two_voltage_result`, `profile_grid_proximity`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_profile_rejects_bad_required_match_tie_count`

**Signature**

```python
def test_profile_rejects_bad_required_match_tie_count(
    column: str, value: object
) -> None:
```

**Purpose**

Protects the `profile rejects bad required match tie count` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`, `value`.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_two_parcel_two_voltage_result()`.
- Enters managed context(s) `pytest.raises(GridProximityError, match='tie_count|match')` and executes: Calls `profile_grid_proximity(_mutate_parcel_result(result, column, value))` for its validation or side effect.

**Action**

- Calls `_mutate_parcel_result`, `_two_parcel_two_voltage_result`, `float`, `profile_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='tie_count|match'): profile_grid_proximity(_mutate_parcel_result(result, column, value))`.

**Regression protected**

- Protects the exact `profile rejects bad required match tie count` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_mutate_parcel_result`, `_two_parcel_two_voltage_result`, `float`, `profile_grid_proximity`, `pytest.mark.parametrize`, `pytest.param`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_profile_rejects_bad_long_table_tie_count`

**Signature**

```python
def test_profile_rejects_bad_long_table_tie_count(value: object) -> None:
```

**Purpose**

Protects the `profile rejects bad long table tie count` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `value`.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_two_parcel_two_voltage_result()`.
- Enters managed context(s) `pytest.raises(GridProximityError, match='tie_count|match')` and executes: Calls `profile_grid_proximity(_mutate_voltage_result(result, 'tie_count', value))` for its validation or side effect.

**Action**

- Calls `_mutate_voltage_result`, `_two_parcel_two_voltage_result`, `float`, `profile_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='tie_count|match'): profile_grid_proximity(_mutate_voltage_result(result, 'tie_count', value))`.

**Regression protected**

- Protects the exact `profile rejects bad long table tie count` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_mutate_voltage_result`, `_two_parcel_two_voltage_result`, `float`, `profile_grid_proximity`, `pytest.mark.parametrize`, `pytest.param`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_profile_rejects_missing_main_match_feature_id`

**Signature**

```python
def test_profile_rejects_missing_main_match_feature_id(column: str) -> None:
```

**Purpose**

Protects the `profile rejects missing main match feature id` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_two_parcel_two_voltage_result()`.
- Enters managed context(s) `pytest.raises(GridProximityError, match='require')` and executes: Calls `profile_grid_proximity(_mutate_parcel_result(result, column, None))` for its validation or side effect.

**Action**

- Calls `_mutate_parcel_result`, `_two_parcel_two_voltage_result`, `profile_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='require'): profile_grid_proximity(_mutate_parcel_result(result, column, None))`.

**Regression protected**

- Protects the exact `profile rejects missing main match feature id` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_mutate_parcel_result`, `_two_parcel_two_voltage_result`, `profile_grid_proximity`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_profile_rejects_bad_required_match_distance`

**Signature**

```python
def test_profile_rejects_bad_required_match_distance(
    column: str, value: object
) -> None:
```

**Purpose**

Protects the `profile rejects bad required match distance` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`, `value`.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_two_parcel_two_voltage_result()`.
- Enters managed context(s) `pytest.raises(GridProximityError)` and executes: Calls `profile_grid_proximity(_mutate_parcel_result(result, column, value))` for its validation or side effect.

**Action**

- Calls `_mutate_parcel_result`, `_two_parcel_two_voltage_result`, `float`, `profile_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError): profile_grid_proximity(_mutate_parcel_result(result, column, value))`.

**Regression protected**

- Protects the exact `profile rejects bad required match distance` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_mutate_parcel_result`, `_two_parcel_two_voltage_result`, `float`, `profile_grid_proximity`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_profile_rejects_bad_exact_match_voltage`

**Signature**

```python
def test_profile_rejects_bad_exact_match_voltage(value: object) -> None:
```

**Purpose**

Protects the `profile rejects bad exact match voltage` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `value`.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_two_parcel_two_voltage_result()`.
- Enters managed context(s) `pytest.raises(GridProximityError, match='voltage|match')` and executes: Calls `profile_grid_proximity(_mutate_parcel_result(result, 'nearest_exact_line_voltage_kv', value))` for its validation or side effect.

**Action**

- Calls `_mutate_parcel_result`, `_two_parcel_two_voltage_result`, `float`, `profile_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='voltage|match'): profile_grid_proximity(_mutate_parcel_result(result, 'nearest_exact_line_voltage_kv', value))`.

**Regression protected**

- Protects the exact `profile rejects bad exact match voltage` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_mutate_parcel_result`, `_two_parcel_two_voltage_result`, `float`, `profile_grid_proximity`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_profile_rejects_bad_result_parcel_id`

**Signature**

```python
def test_profile_rejects_bad_result_parcel_id() -> None:
```

**Purpose**

Protects the `profile rejects bad result parcel id` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_two_parcel_two_voltage_result()`.
- Enters managed context(s) `pytest.raises(GridProximityError, match='parcel_id')` and executes: Calls `profile_grid_proximity(_mutate_parcel_result(result, 'parcel_id', ' BAD '))` for its validation or side effect.

**Action**

- Calls `_mutate_parcel_result`, `_two_parcel_two_voltage_result`, `profile_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='parcel_id'): profile_grid_proximity(_mutate_parcel_result(result, 'parcel_id', ' BAD '))`.

**Regression protected**

- Protects the exact `profile rejects bad result parcel id` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_mutate_parcel_result`, `_two_parcel_two_voltage_result`, `profile_grid_proximity`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_profile_rejects_missing_required_proximity_column`

**Signature**

```python
def test_profile_rejects_missing_required_proximity_column() -> None:
```

**Purpose**

Protects the `profile rejects missing required proximity column` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `result` from `_two_parcel_two_voltage_result()`.
- Computes `parcels` from `result.parcels.drop(columns='nearest_line_grid_feature_id')`.
- Enters managed context(s) `pytest.raises(GridProximityError, match='Missing proximity')` and executes: Calls `profile_grid_proximity(replace(result, parcels=parcels))` for its validation or side effect.

**Action**

- Calls `_two_parcel_two_voltage_result`, `profile_grid_proximity`, `replace`, `result.parcels.drop`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='Missing proximity'): profile_grid_proximity(replace(result, parcels=parcels))`.

**Regression protected**

- Protects the exact `profile rejects missing required proximity column` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_two_parcel_two_voltage_result`, `profile_grid_proximity`, `pytest.raises`, `replace`, `result.parcels.drop`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_profile_rejects_nondeterministic_or_duplicate_coverage`

**Signature**

```python
def test_profile_rejects_nondeterministic_or_duplicate_coverage(
    mutation: str,
) -> None:
```

**Purpose**

Protects the `profile rejects nondeterministic or duplicate coverage` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `mutation`.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_two_parcel_two_voltage_result()`.
- Enters managed context(s) `pytest.raises(GridProximityError, match='coverage')` and executes: Calls `profile_grid_proximity(replace(result, voltage_level_coverage=coverage))` for its validation or side effect.

**Action**

- Calls `_two_parcel_two_voltage_result`, `profile_grid_proximity`, `replace`, `reversed`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='coverage'): profile_grid_proximity(replace(result, voltage_level_coverage=coverage))`.

**Regression protected**

- Protects the exact `profile rejects nondeterministic or duplicate coverage` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_two_parcel_two_voltage_result`, `profile_grid_proximity`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `reversed`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_profile_rejects_invalid_voltage_coverage_level`

**Signature**

```python
def test_profile_rejects_invalid_voltage_coverage_level(voltage_kv: object) -> None:
```

**Purpose**

Protects the `profile rejects invalid voltage coverage level` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `voltage_kv`.
- Contains 3 explicit setup/context statement(s).
- Computes `result` from `_two_parcel_two_voltage_result()`.
- Computes `coverage` from `(VoltageLevelCoverage(voltage_kv=voltage_kv, line_feature_count=1),)`.
- Enters managed context(s) `pytest.raises(GridProximityError, match='coverage')` and executes: Calls `profile_grid_proximity(replace(result, voltage_level_coverage=coverage))` for its validation or side effect.

**Action**

- Calls `VoltageLevelCoverage`, `_two_parcel_two_voltage_result`, `float`, `profile_grid_proximity`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='coverage'): profile_grid_proximity(replace(result, voltage_level_coverage=coverage))`.

**Regression protected**

- Protects the exact `profile rejects invalid voltage coverage level` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `VoltageLevelCoverage`, `_two_parcel_two_voltage_result`, `float`, `profile_grid_proximity`, `pytest.mark.parametrize`, `pytest.param`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_profile_rejects_invalid_voltage_coverage_feature_count`

**Signature**

```python
def test_profile_rejects_invalid_voltage_coverage_feature_count(
    feature_count: object,
) -> None:
```

**Purpose**

Protects the `profile rejects invalid voltage coverage feature count` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `feature_count`.
- Contains 3 explicit setup/context statement(s).
- Computes `result` from `_two_parcel_two_voltage_result()`.
- Computes `coverage` from `(VoltageLevelCoverage(voltage_kv=110.0, line_feature_count=feature_count),)`.
- Enters managed context(s) `pytest.raises(GridProximityError, match='line_feature_count')` and executes: Calls `profile_grid_proximity(replace(result, voltage_level_coverage=coverage))` for its validation or side effect.

**Action**

- Calls `VoltageLevelCoverage`, `_two_parcel_two_voltage_result`, `float`, `profile_grid_proximity`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='line_feature_count'): profile_grid_proximity(replace(result, voltage_level_coverage=coverage))`.

**Regression protected**

- Protects the exact `profile rejects invalid voltage coverage feature count` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `VoltageLevelCoverage`, `_two_parcel_two_voltage_result`, `float`, `profile_grid_proximity`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_profile_rejects_invalid_long_table_voltage`

**Signature**

```python
def test_profile_rejects_invalid_long_table_voltage(value: object) -> None:
```

**Purpose**

Protects the `profile rejects invalid long table voltage` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `value`.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_two_parcel_two_voltage_result()`.
- Enters managed context(s) `pytest.raises(GridProximityError, match='Voltage proximity')` and executes: Calls `profile_grid_proximity(_mutate_voltage_result(result, 'voltage_kv', value))` for its validation or side effect.

**Action**

- Calls `_mutate_voltage_result`, `_two_parcel_two_voltage_result`, `float`, `profile_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='Voltage proximity'): profile_grid_proximity(_mutate_voltage_result(result, 'voltage_kv', value))`.

**Regression protected**

- Protects the exact `profile rejects invalid long table voltage` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_mutate_voltage_result`, `_two_parcel_two_voltage_result`, `float`, `profile_grid_proximity`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_profile_rejects_missing_long_table_match_lineage`

**Signature**

```python
def test_profile_rejects_missing_long_table_match_lineage(column: str) -> None:
```

**Purpose**

Protects the `profile rejects missing long table match lineage` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_two_parcel_two_voltage_result()`.
- Enters managed context(s) `pytest.raises(GridProximityError, match='require')` and executes: Calls `profile_grid_proximity(_mutate_voltage_result(result, column, None))` for its validation or side effect.

**Action**

- Calls `_mutate_voltage_result`, `_two_parcel_two_voltage_result`, `profile_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='require'): profile_grid_proximity(_mutate_voltage_result(result, column, None))`.

**Regression protected**

- Protects the exact `profile rejects missing long table match lineage` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_mutate_voltage_result`, `_two_parcel_two_voltage_result`, `profile_grid_proximity`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_profile_rejects_bad_long_table_distance`

**Signature**

```python
def test_profile_rejects_bad_long_table_distance(value: object) -> None:
```

**Purpose**

Protects the `profile rejects bad long table distance` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `value`.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_two_parcel_two_voltage_result()`.
- Enters managed context(s) `pytest.raises(GridProximityError)` and executes: Calls `profile_grid_proximity(_mutate_voltage_result(result, 'nearest_line_proxy_distance_m', value))` for its validation or side effect.

**Action**

- Calls `_mutate_voltage_result`, `_two_parcel_two_voltage_result`, `float`, `profile_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError): profile_grid_proximity(_mutate_voltage_result(result, 'nearest_line_proxy_distance_m', value))`.

**Regression protected**

- Protects the exact `profile rejects bad long table distance` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_mutate_voltage_result`, `_two_parcel_two_voltage_result`, `float`, `profile_grid_proximity`, `pytest.mark.parametrize`, `pytest.param`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_profile_allows_consistent_missing_manager_and_asset_status`

**Signature**

```python
def test_profile_allows_consistent_missing_manager_and_asset_status() -> None:
```

**Purpose**

Protects the `profile allows consistent missing manager and asset status` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `lines` from `_lines()`.
- Computes `lines['manager_name']` from `None`.
- Computes `lines['asset_status_raw']` from `None`.
- Computes `result` from `enrich_parcel_grid_proximity(_parcels(), lines, _posts())`.
- Computes `profile` from `profile_grid_proximity(result)`.

**Action**

- Calls `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `profile_grid_proximity`, `result.parcels['nearest_exact_line_asset_status_raw'].isna`, `result.parcels['nearest_exact_line_asset_status_raw'].isna().all`, `result.parcels['nearest_exact_line_manager_name'].isna`, `result.parcels['nearest_exact_line_manager_name'].isna().all`, `result.voltage_level_proximity['asset_status_raw'].isna`, `result.voltage_level_proximity['asset_status_raw'].isna().all`, `result.voltage_level_proximity['manager_name'].isna`, `result.voltage_level_proximity['manager_name'].isna().all`.

**Expected result**

- Direct assertions: `assert profile.parcel_count == 1`; `assert result.parcels['nearest_exact_line_manager_name'].isna().all()`; `assert result.parcels['nearest_exact_line_asset_status_raw'].isna().all()`; `assert result.voltage_level_proximity['manager_name'].isna().all()`; `assert result.voltage_level_proximity['asset_status_raw'].isna().all()`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `profile allows consistent missing manager and asset status` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `profile_grid_proximity`, `result.parcels['nearest_exact_line_asset_status_raw'].isna`, `result.parcels['nearest_exact_line_asset_status_raw'].isna().all`, `result.parcels['nearest_exact_line_manager_name'].isna`, `result.parcels['nearest_exact_line_manager_name'].isna().all`, `result.voltage_level_proximity['asset_status_raw'].isna`, `result.voltage_level_proximity['asset_status_raw'].isna().all`, `result.voltage_level_proximity['manager_name'].isna`, `result.voltage_level_proximity['manager_name'].isna().all`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_profile_rejects_nonnull_exact_field_without_exact_coverage`

**Signature**

```python
def test_profile_rejects_nonnull_exact_field_without_exact_coverage(
    column: str, value: object
) -> None:
```

**Purpose**

Protects the `profile rejects nonnull exact field without exact coverage` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`, `value`.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `enrich_parcel_grid_proximity(_parcels(), _lines(voltage_statuses=['UNKNOWN'], voltages=[None]), _posts())`.
- Enters managed context(s) `pytest.raises(GridProximityError, match='unmatched|entirely')` and executes: Calls `profile_grid_proximity(_mutate_parcel_result(result, column, value))` for its validation or side effect.

**Action**

- Calls `_lines`, `_mutate_parcel_result`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `profile_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='unmatched|entirely'): profile_grid_proximity(_mutate_parcel_result(result, column, value))`.

**Regression protected**

- Protects the exact `profile rejects nonnull exact field without exact coverage` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_lines`, `_mutate_parcel_result`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `profile_grid_proximity`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_no_valid_required_grid_feature_is_rejected`

**Signature**

```python
def test_no_valid_required_grid_feature_is_rejected(kind: str) -> None:
```

**Purpose**

Protects the `no valid required grid feature is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `kind`.
- Contains 3 explicit setup/context statement(s).
- Computes `lines` from `_lines([None]) if kind == 'line' else _lines()`.
- Computes `posts` from `_posts([None]) if kind == 'post' else _posts()`.
- Enters managed context(s) `pytest.raises(GridProximityError, match='No VALID')` and executes: Calls `enrich_parcel_grid_proximity(_parcels(), lines, posts)` for its validation or side effect.

**Action**

- Calls `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridProximityError, match='No VALID'): enrich_parcel_grid_proximity(_parcels(), lines, posts)`.

**Regression protected**

- Protects the exact `no valid required grid feature is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `asset_status_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `cleabs` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `columns` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `date_creation` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `date_de_confirmation` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `date_modification` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `etat_de_l_objet` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `gestionnaire` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `grid_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `grid_feature_type` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `identifiants_sources` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `importance` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `importance_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `manager_name` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `methode_d_acquisition_planimetrique` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `name` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_exact_line_asset_status_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_exact_line_grid_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_exact_line_manager_name` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_exact_line_proxy_distance_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_exact_line_tie_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_exact_line_voltage_kv` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_line_grid_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_line_proxy_distance_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_line_tie_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_line_voltage_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_post_grid_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_post_proxy_distance_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `precision_planimetrique` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `siren_gestionnaire` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `source_department_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_edition` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_value` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `sources` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `spatial_role` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `statut_du_toponyme` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `tie_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `toponyme` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `voltage` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `voltage_kv` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `voltage_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `voltage_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `voltage_upper_bound_kv` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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

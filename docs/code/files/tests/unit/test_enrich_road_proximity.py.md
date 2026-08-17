# `tests/unit/test_enrich_road_proximity.py`

## File identity

- Repository path: `tests/unit/test_enrich_road_proximity.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `enrich_road_proximity` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `c05463733323609f0b4b5d32e7ee0269b8f951bd12d924cc155b0f6c7c2548ff`

## 1. Purpose

Provides complete unit and regression coverage for the `enrich_road_proximity` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `from copy import deepcopy` — required by the implementation paths and symbols documented below.
- `from dataclasses import FrozenInstanceError` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.
- `from typing import Any, cast` — required by the implementation paths and symbols documented below.

### Third-party

- `from unittest.mock import patch` — required by the implementation paths and symbols documented below.
- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `import pytest` — required by the implementation paths and symbols documented below.
- `from geopandas.testing import assert_geodataframe_equal` — required by the implementation paths and symbols documented below.
- `from pandas.testing import assert_frame_equal` — required by the implementation paths and symbols documented below.
- `from shapely.geometry import LineString, MultiPolygon, Point, Polygon` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout import stages` — required by the implementation paths and symbols documented below.
- `from landscout.sources.ign_bdtopo_fr import ( IgnBdTopoRoadData, load_ign_bdtopo_source_config, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.apply_road_vehicle_proxy_policy import ( IgnRoadVehicleProxyApplicationError, IgnRoadVehicleProxyApplicationResult, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.enrich_road_proximity import ( CLASS_PROXIMITY_COLUMNS, ParcelRoadProximityResult, RoadProximityError, enrich_parcel_road_proximity, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.road_vehicle_proxy_policy import ( load_ign_road_vehicle_proxy_policy, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `SOURCE_CONFIG` | `load_ign_bdtopo_source_config()` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `POLICY_PATH` | `Path("configs/access/ign_bdtopo_vehicle_proxy_policy.yaml")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ELIGIBLE_CLASSES` | `( "GENERAL_VEHICLE_PROXY", "LIMITED_VEHICLE_PROXY", "RESTRICTED_REVIEW", "NOT_GENERAL_VEHICLE_PROXY", "UNKNOWN_REVIEW", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ALL_CLASSES` | `( "GENERAL_VEHICLE_PROXY", "LIMITED_VEHICLE_PROXY", "RESTRICTED_REVIEW", "NOT_GENERAL_VEHICLE_PROXY", "NOT_DISTANCE_PROXY", "UNKNOWN_REVIEW", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SELECTED_COLUMNS` | `( "nearest_road_proxy_distance_m", "nearest_road_feature_id", "nearest_source_feature_id", "nearest_road_tie_count", "nearest_road_primary_rule", "nearest_road_rule_trace_json", "nearest_road_unknown_fields_json", "nearest_road_toll_evidence", "nearest_nature_raw", "nearest_importance_raw", "nearest_asset_status_raw", "nearest_private_raw", "nearest_light_vehicle_access_raw", "nearest_carriageway_width_raw", "nearest_closure_period_raw", "nearest_restriction_nature_raw", "nearest_source_layer", "nearest_source_department_code", "nearest_source_edition", "nearest_source_archive_sha256", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `_metric_parcels`

**Signature**

```python
def _metric_parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
```

**Purpose**

Implements metric parcels according to the exact implementation and guards in this file.

**Inputs**

- `geometries` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `identifiers` (`list[object] | None`; optional/default `None`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `index` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `gpd.GeoDataFrame({'parcel_id': ids, 'source_value': list(range(count))}, geometry=values, crs='EPSG:2154', index=frame_index)`.

**Algorithm**

1. Computes `values` from `geometries or [Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])]`.
2. Computes `count` from `len(values)`.
3. Computes `ids` from `identifiers or [f'PARCEL-{position + 1}' for position in range(count)]`.
4. Computes `frame_index` from `index or [100 + position for position in range(count)]`.
5. Returns `gpd.GeoDataFrame({'parcel_id': ids, 'source_value': list(range(count))}, geometry=values, crs='EPSG:2154', index=frame_index)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `Polygon`, `gpd.GeoDataFrame`, `len`, `list`, `range`.

**Known repository callers**

- `tests/unit/test_enrich_road_proximity.py` — `_parcels`
- `tests/unit/test_enrich_road_proximity.py` — `test_missing_or_wrong_storage_crs_is_rejected`

**Tests**

- `tests/unit/test_enrich_road_proximity.py::test_missing_or_wrong_storage_crs_is_rejected`

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
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
```

**Purpose**

Implements parcels according to the exact implementation and guards in this file.

**Inputs**

- `geometries` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `identifiers` (`list[object] | None`; optional/default `None`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `index` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `_metric_parcels(geometries, identifiers=identifiers, index=index).to_crs('EPSG:4326')`.

**Algorithm**

1. Returns `_metric_parcels(geometries, identifiers=identifiers, index=index).to_crs('EPSG:4326')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `_metric_parcels(geometries, identifiers=identifiers, index=index).to_crs`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_metric_parcels`, `_metric_parcels(geometries, identifiers=identifiers, index=index).to_crs`.

**Known repository callers**

- `tests/unit/test_enrich_road_proximity.py` — `_enrich`
- `tests/unit/test_enrich_road_proximity.py` — `test_application_failure_stops_proximity`
- `tests/unit/test_enrich_road_proximity.py` — `test_application_roads_must_be_geodataframe`
- `tests/unit/test_enrich_road_proximity.py` — `test_application_stage_is_invoked_exactly_once`
- `tests/unit/test_enrich_road_proximity.py` — `test_bad_parcel_geometry_is_rejected`
- `tests/unit/test_enrich_road_proximity.py` — `test_duplicate_parcel_columns_are_rejected`
- `tests/unit/test_enrich_road_proximity.py` — `test_duplicate_parcel_id_is_rejected`
- `tests/unit/test_enrich_road_proximity.py` — `test_empty_eligible_class_emits_null_row_per_parcel`
- `tests/unit/test_enrich_road_proximity.py` — `test_invalid_parcel_identity_is_rejected`
- `tests/unit/test_enrich_road_proximity.py` — `test_malformed_policy_stops_before_application`
- `tests/unit/test_enrich_road_proximity.py` — `test_missing_or_inactive_geometry_is_rejected`
- `tests/unit/test_enrich_road_proximity.py` — `test_missing_or_wrong_storage_crs_is_rejected`
- `tests/unit/test_enrich_road_proximity.py` — `test_output_shape_columns_and_order_are_deterministic`
- `tests/unit/test_enrich_road_proximity.py` — `test_parcel_preservation_uses_exact_non_geometry_values`
- `tests/unit/test_enrich_road_proximity.py` — `test_parcels_and_road_application_are_not_mutated`
- `tests/unit/test_enrich_road_proximity.py` — `test_polygon_and_multipolygon_are_accepted`
- `tests/unit/test_enrich_road_proximity.py` — `test_result_dataclasses_are_frozen`
- `tests/unit/test_enrich_road_proximity.py` — `test_result_parcel_frame_is_an_independent_copy`
- `tests/unit/test_enrich_road_proximity.py` — `test_storage_geometry_stays_epsg4326_while_distance_is_metric`
- `tests/unit/test_enrich_road_proximity.py` — `test_wrong_application_result_type_is_rejected`
- `tests/unit/test_enrich_road_proximity.py` — `test_wrong_parcel_geometry_kind_is_rejected`
- `tests/unit/test_enrich_road_proximity.py` — `test_wrong_policy_path_type_has_controlled_error`
- `tests/unit/test_enrich_road_proximity.py` — `test_wrong_road_source_type_has_controlled_error`
- `tests/unit/test_enrich_road_proximity.py` — `test_wrong_source_config_type_has_controlled_error`

**Tests**

- `tests/unit/test_enrich_road_proximity.py::test_application_failure_stops_proximity`
- `tests/unit/test_enrich_road_proximity.py::test_application_roads_must_be_geodataframe`
- `tests/unit/test_enrich_road_proximity.py::test_application_stage_is_invoked_exactly_once`
- `tests/unit/test_enrich_road_proximity.py::test_bad_parcel_geometry_is_rejected`
- `tests/unit/test_enrich_road_proximity.py::test_duplicate_parcel_columns_are_rejected`
- `tests/unit/test_enrich_road_proximity.py::test_duplicate_parcel_id_is_rejected`
- `tests/unit/test_enrich_road_proximity.py::test_empty_eligible_class_emits_null_row_per_parcel`
- `tests/unit/test_enrich_road_proximity.py::test_invalid_parcel_identity_is_rejected`
- `tests/unit/test_enrich_road_proximity.py::test_malformed_policy_stops_before_application`
- `tests/unit/test_enrich_road_proximity.py::test_missing_or_inactive_geometry_is_rejected`
- `tests/unit/test_enrich_road_proximity.py::test_missing_or_wrong_storage_crs_is_rejected`
- `tests/unit/test_enrich_road_proximity.py::test_output_shape_columns_and_order_are_deterministic`
- `tests/unit/test_enrich_road_proximity.py::test_parcel_preservation_uses_exact_non_geometry_values`
- `tests/unit/test_enrich_road_proximity.py::test_parcels_and_road_application_are_not_mutated`
- `tests/unit/test_enrich_road_proximity.py::test_polygon_and_multipolygon_are_accepted`
- `tests/unit/test_enrich_road_proximity.py::test_result_dataclasses_are_frozen`
- `tests/unit/test_enrich_road_proximity.py::test_result_parcel_frame_is_an_independent_copy`
- `tests/unit/test_enrich_road_proximity.py::test_storage_geometry_stays_epsg4326_while_distance_is_metric`
- `tests/unit/test_enrich_road_proximity.py::test_wrong_application_result_type_is_rejected`
- `tests/unit/test_enrich_road_proximity.py::test_wrong_parcel_geometry_kind_is_rejected`
- `tests/unit/test_enrich_road_proximity.py::test_wrong_policy_path_type_has_controlled_error`
- `tests/unit/test_enrich_road_proximity.py::test_wrong_road_source_type_has_controlled_error`
- `tests/unit/test_enrich_road_proximity.py::test_wrong_source_config_type_has_controlled_error`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_road_row`

**Signature**

```python
def _road_row(
    road_class: str,
    x: float,
    *,
    identifier: str,
    geometry: object | None = None,
) -> dict[str, object]:
```

**Purpose**

Implements road row according to the exact implementation and guards in this file.

**Inputs**

- `road_class` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `x` (`float`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `identifier` (`str`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `geometry` (`object | None`; optional/default `None`) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `{'road_feature_id': identifier, 'source_feature_id': f'SOURCE-{identifier}', 'geometry_status': 'VALID', 'nature_raw': 'Route à 1 chaussée', 'importance_raw': '2', 'asset_status_raw': 'En service', 'private_raw': 0.0, 'light_vehicle_access_raw': 'Libre', 'carriageway_width_raw': 7.0, 'closure_period_raw': None, 'restriction_nature_raw': None, 'source_layer': 'troncon_de_route', 'source_department…`.

**Algorithm**

1. Computes `policy` from `load_ign_road_vehicle_proxy_policy()`.
2. Computes `primary_rule` from `{'GENERAL_VEHICLE_PROXY': 'OPEN_OR_TOLL', 'LIMITED_VEHICLE_PROXY': 'LIMITED_NATURE', 'RESTRICTED_REVIEW': 'PRIVATE_ROAD', 'NOT_GENERAL_VEHICLE_PROXY': 'PHYSICALLY_IMPOSSIBLE', 'NOT_DISTANCE_PROXY': 'FICTITIOUS_GEOMETRY', 'UNKNOWN_REVIEW': 'UNKNOWN'}[road_class]`.
3. Returns `{'road_feature_id': identifier, 'source_feature_id': f'SOURCE-{identifier}', 'geometry_status': 'VALID', 'nature_raw': 'Route à 1 chaussée', 'importance_raw': '2', 'asset_status_raw': 'En service', 'private_raw': 0.0, 'light_vehicle_access_raw': 'Libre', 'carriageway_width_raw': 7.0, 'closure_period_raw': None, 'restriction_nature_raw': None, 'source_layer'…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `load_ign_road_vehicle_proxy_policy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `LineString`, `load_ign_road_vehicle_proxy_policy`.

**Known repository callers**

- `tests/unit/test_enrich_road_proximity.py` — `_roads`
- `tests/unit/test_enrich_road_proximity.py` — `test_exact_tie_counts_two_and_lexical_id_wins`
- `tests/unit/test_enrich_road_proximity.py` — `test_intersecting_or_touching_road_has_zero_distance`
- `tests/unit/test_enrich_road_proximity.py` — `test_tie_winner_is_independent_of_source_order`
- `tests/unit/test_enrich_road_proximity.py` — `test_unequal_distance_wins_regardless_of_identifier`

**Tests**

- `tests/unit/test_enrich_road_proximity.py::test_exact_tie_counts_two_and_lexical_id_wins`
- `tests/unit/test_enrich_road_proximity.py::test_intersecting_or_touching_road_has_zero_distance`
- `tests/unit/test_enrich_road_proximity.py::test_tie_winner_is_independent_of_source_order`
- `tests/unit/test_enrich_road_proximity.py::test_unequal_distance_wins_regardless_of_identifier`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_roads`

**Signature**

```python
def _roads(
    rows: list[dict[str, object]] | None = None,
) -> gpd.GeoDataFrame:
```

**Purpose**

Implements roads according to the exact implementation and guards in this file.

**Inputs**

- `rows` (`list[dict[str, object]] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `gpd.GeoDataFrame(values, geometry='geometry', crs='EPSG:2154')`.

**Algorithm**

1. Computes `values` from `rows or [_road_row('GENERAL_VEHICLE_PROXY', 20, identifier='ROAD-GENERAL'), _road_row('LIMITED_VEHICLE_PROXY', 30, identifier='ROAD-LIMITED'), _road_row('RESTRICTED_REVIEW', 15, identifier='ROAD-RESTRICTED'), _road_row('NOT_GENERAL_VEHICLE_PROXY', 40, identifier='ROAD-NOT-GENERAL'), _road_row('NOT_DISTANCE_PROXY', 11,…`.
2. Returns `gpd.GeoDataFrame(values, geometry='geometry', crs='EPSG:2154')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_road_row`, `gpd.GeoDataFrame`.

**Known repository callers**

- `tests/unit/test_enrich_road_proximity.py` — `_enrich`
- `tests/unit/test_enrich_road_proximity.py` — `_source`
- `tests/unit/test_enrich_road_proximity.py` — `test_application_roads_must_be_geodataframe`
- `tests/unit/test_enrich_road_proximity.py` — `test_application_stage_is_invoked_exactly_once`
- `tests/unit/test_enrich_road_proximity.py` — `test_duplicate_road_feature_id_is_rejected`
- `tests/unit/test_enrich_road_proximity.py` — `test_eligible_class_rejects_unsupported_geometry`
- `tests/unit/test_enrich_road_proximity.py` — `test_eligible_class_requires_valid_geometry_status`
- `tests/unit/test_enrich_road_proximity.py` — `test_empty_eligible_class_emits_null_row_per_parcel`
- `tests/unit/test_enrich_road_proximity.py` — `test_exact_tie_counts_two_and_lexical_id_wins`
- `tests/unit/test_enrich_road_proximity.py` — `test_independent_policy_sha_mismatch_is_rejected`
- `tests/unit/test_enrich_road_proximity.py` — `test_intersecting_or_touching_road_has_zero_distance`
- `tests/unit/test_enrich_road_proximity.py` — `test_missing_road_policy_lineage_is_rejected`
- `tests/unit/test_enrich_road_proximity.py` — `test_not_distance_road_is_counted_but_never_indexed`
- `tests/unit/test_enrich_road_proximity.py` — `test_parcels_and_road_application_are_not_mutated`
- `tests/unit/test_enrich_road_proximity.py` — `test_policy_sha_mismatch_does_not_construct_spatial_index`
- `tests/unit/test_enrich_road_proximity.py` — `test_selected_rows_belong_to_requested_class`
- `tests/unit/test_enrich_road_proximity.py` — `test_tie_winner_is_independent_of_source_order`
- `tests/unit/test_enrich_road_proximity.py` — `test_unequal_distance_wins_regardless_of_identifier`
- `tests/unit/test_enrich_road_proximity.py` — `test_unknown_road_proxy_class_is_rejected`

**Tests**

- `tests/unit/test_enrich_road_proximity.py::test_application_roads_must_be_geodataframe`
- `tests/unit/test_enrich_road_proximity.py::test_application_stage_is_invoked_exactly_once`
- `tests/unit/test_enrich_road_proximity.py::test_duplicate_road_feature_id_is_rejected`
- `tests/unit/test_enrich_road_proximity.py::test_eligible_class_rejects_unsupported_geometry`
- `tests/unit/test_enrich_road_proximity.py::test_eligible_class_requires_valid_geometry_status`
- `tests/unit/test_enrich_road_proximity.py::test_empty_eligible_class_emits_null_row_per_parcel`
- `tests/unit/test_enrich_road_proximity.py::test_exact_tie_counts_two_and_lexical_id_wins`
- `tests/unit/test_enrich_road_proximity.py::test_independent_policy_sha_mismatch_is_rejected`
- `tests/unit/test_enrich_road_proximity.py::test_intersecting_or_touching_road_has_zero_distance`
- `tests/unit/test_enrich_road_proximity.py::test_missing_road_policy_lineage_is_rejected`
- `tests/unit/test_enrich_road_proximity.py::test_not_distance_road_is_counted_but_never_indexed`
- `tests/unit/test_enrich_road_proximity.py::test_parcels_and_road_application_are_not_mutated`
- `tests/unit/test_enrich_road_proximity.py::test_policy_sha_mismatch_does_not_construct_spatial_index`
- `tests/unit/test_enrich_road_proximity.py::test_selected_rows_belong_to_requested_class`
- `tests/unit/test_enrich_road_proximity.py::test_tie_winner_is_independent_of_source_order`
- `tests/unit/test_enrich_road_proximity.py::test_unequal_distance_wins_regardless_of_identifier`
- `tests/unit/test_enrich_road_proximity.py::test_unknown_road_proxy_class_is_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_source`

**Signature**

```python
def _source() -> IgnBdTopoRoadData:
```

**Purpose**

Implements source according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `IgnBdTopoRoadData`. Observed return expression(s): `IgnBdTopoRoadData(extraction=cast(Any, None), road_segments=_roads(), road_segments_summary=cast(Any, None))`.

**Algorithm**

1. Returns `IgnBdTopoRoadData(extraction=cast(Any, None), road_segments=_roads(), road_segments_summary=cast(Any, None))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnBdTopoRoadData`, `_roads`, `cast`.

**Known repository callers**

- `tests/unit/test_enrich_road_proximity.py` — `_enrich`
- `tests/unit/test_enrich_road_proximity.py` — `test_application_failure_stops_proximity`
- `tests/unit/test_enrich_road_proximity.py` — `test_application_roads_must_be_geodataframe`
- `tests/unit/test_enrich_road_proximity.py` — `test_application_stage_is_invoked_exactly_once`
- `tests/unit/test_enrich_road_proximity.py` — `test_malformed_policy_stops_before_application`
- `tests/unit/test_enrich_road_proximity.py` — `test_wrong_application_result_type_is_rejected`
- `tests/unit/test_enrich_road_proximity.py` — `test_wrong_parcel_type_has_controlled_error`
- `tests/unit/test_enrich_road_proximity.py` — `test_wrong_policy_path_type_has_controlled_error`
- `tests/unit/test_enrich_road_proximity.py` — `test_wrong_source_config_type_has_controlled_error`

**Tests**

- `tests/unit/test_enrich_road_proximity.py::test_application_failure_stops_proximity`
- `tests/unit/test_enrich_road_proximity.py::test_application_roads_must_be_geodataframe`
- `tests/unit/test_enrich_road_proximity.py::test_application_stage_is_invoked_exactly_once`
- `tests/unit/test_enrich_road_proximity.py::test_malformed_policy_stops_before_application`
- `tests/unit/test_enrich_road_proximity.py::test_wrong_application_result_type_is_rejected`
- `tests/unit/test_enrich_road_proximity.py::test_wrong_parcel_type_has_controlled_error`
- `tests/unit/test_enrich_road_proximity.py::test_wrong_policy_path_type_has_controlled_error`
- `tests/unit/test_enrich_road_proximity.py::test_wrong_source_config_type_has_controlled_error`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_enrich`

**Signature**

```python
def _enrich(
    parcels: gpd.GeoDataFrame | None = None,
    roads: gpd.GeoDataFrame | None = None,
    *,
    policy_path: Path | None = None,
) -> ParcelRoadProximityResult:
```

**Purpose**

Enriches enrich according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`gpd.GeoDataFrame | None`; optional/default `None`) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `roads` (`gpd.GeoDataFrame | None`; optional/default `None`) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_path` (`Path | None`; optional/default `None`) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `ParcelRoadProximityResult`. Observed return expression(s): `enrich_parcel_road_proximity(parcels if parcels is not None else _parcels(), _source(), SOURCE_CONFIG, policy_path)`.

**Algorithm**

1. Computes `application` from `IgnRoadVehicleProxyApplicationResult(roads if roads is not None else _roads())`.
2. Enters managed context(s) `patch('landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy', return_value=application)` and executes: Returns `enrich_parcel_road_proximity(parcels if parcels is not None else _parcels(), _source(), SOURCE_CONFIG, policy_path)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnRoadVehicleProxyApplicationResult`, `_parcels`, `_roads`, `_source`, `enrich_parcel_road_proximity`, `patch`.

**Known repository callers**

- `tests/unit/test_enrich_road_proximity.py` — `_corrupt_nearest_output`
- `tests/unit/test_enrich_road_proximity.py` — `test_bad_parcel_geometry_is_rejected`
- `tests/unit/test_enrich_road_proximity.py` — `test_class_coverage_is_complete_and_strict`
- `tests/unit/test_enrich_road_proximity.py` — `test_class_proximity_is_plain_dataframe`
- `tests/unit/test_enrich_road_proximity.py` — `test_distance_uses_full_polygon_not_centroid`
- `tests/unit/test_enrich_road_proximity.py` — `test_duplicate_parcel_columns_are_rejected`
- `tests/unit/test_enrich_road_proximity.py` — `test_duplicate_parcel_id_is_rejected`
- `tests/unit/test_enrich_road_proximity.py` — `test_duplicate_road_feature_id_is_rejected`
- `tests/unit/test_enrich_road_proximity.py` — `test_each_eligible_class_has_independent_distance`
- `tests/unit/test_enrich_road_proximity.py` — `test_eligible_class_rejects_unsupported_geometry`
- `tests/unit/test_enrich_road_proximity.py` — `test_eligible_class_requires_valid_geometry_status`
- `tests/unit/test_enrich_road_proximity.py` — `test_empty_eligible_class_emits_null_row_per_parcel`
- `tests/unit/test_enrich_road_proximity.py` — `test_exact_tie_counts_two_and_lexical_id_wins`
- `tests/unit/test_enrich_road_proximity.py` — `test_independent_policy_sha_mismatch_is_rejected`
- `tests/unit/test_enrich_road_proximity.py` — `test_intersecting_or_touching_road_has_zero_distance`
- `tests/unit/test_enrich_road_proximity.py` — `test_invalid_parcel_identity_is_rejected`
- `tests/unit/test_enrich_road_proximity.py` — `test_known_polygon_to_line_distance_is_ten_metres`
- `tests/unit/test_enrich_road_proximity.py` — `test_matched_output_dtypes_are_stable`
- `tests/unit/test_enrich_road_proximity.py` — `test_missing_or_inactive_geometry_is_rejected`
- `tests/unit/test_enrich_road_proximity.py` — `test_missing_or_wrong_storage_crs_is_rejected`
- `tests/unit/test_enrich_road_proximity.py` — `test_missing_road_policy_lineage_is_rejected`
- `tests/unit/test_enrich_road_proximity.py` — `test_near_not_distance_road_cannot_change_general_distance`
- `tests/unit/test_enrich_road_proximity.py` — `test_no_business_decision_columns_or_implementation_exist`
- `tests/unit/test_enrich_road_proximity.py` — `test_not_distance_road_is_counted_but_never_indexed`
- `tests/unit/test_enrich_road_proximity.py` — `test_output_shape_columns_and_order_are_deterministic`
- `tests/unit/test_enrich_road_proximity.py` — `test_parcel_preservation_uses_exact_non_geometry_values`
- `tests/unit/test_enrich_road_proximity.py` — `test_parcels_and_road_application_are_not_mutated`
- `tests/unit/test_enrich_road_proximity.py` — `test_policy_sha_mismatch_does_not_construct_spatial_index`
- `tests/unit/test_enrich_road_proximity.py` — `test_polygon_and_multipolygon_are_accepted`
- `tests/unit/test_enrich_road_proximity.py` — `test_result_dataclasses_are_frozen`
- `tests/unit/test_enrich_road_proximity.py` — `test_result_parcel_frame_is_an_independent_copy`
- `tests/unit/test_enrich_road_proximity.py` — `test_selected_road_evidence_and_lineage_are_exact`
- `tests/unit/test_enrich_road_proximity.py` — `test_selected_rows_belong_to_requested_class`
- `tests/unit/test_enrich_road_proximity.py` — `test_single_nearest_road_has_tie_count_one`
- `tests/unit/test_enrich_road_proximity.py` — `test_storage_geometry_stays_epsg4326_while_distance_is_metric`
- `tests/unit/test_enrich_road_proximity.py` — `test_tie_winner_is_independent_of_source_order`
- `tests/unit/test_enrich_road_proximity.py` — `test_unequal_distance_wins_regardless_of_identifier`
- `tests/unit/test_enrich_road_proximity.py` — `test_unknown_road_proxy_class_is_rejected`
- `tests/unit/test_enrich_road_proximity.py` — `test_wrong_parcel_geometry_kind_is_rejected`

**Tests**

- `tests/unit/test_enrich_road_proximity.py::test_bad_parcel_geometry_is_rejected`
- `tests/unit/test_enrich_road_proximity.py::test_class_coverage_is_complete_and_strict`
- `tests/unit/test_enrich_road_proximity.py::test_class_proximity_is_plain_dataframe`
- `tests/unit/test_enrich_road_proximity.py::test_distance_uses_full_polygon_not_centroid`
- `tests/unit/test_enrich_road_proximity.py::test_duplicate_parcel_columns_are_rejected`
- `tests/unit/test_enrich_road_proximity.py::test_duplicate_parcel_id_is_rejected`
- `tests/unit/test_enrich_road_proximity.py::test_duplicate_road_feature_id_is_rejected`
- `tests/unit/test_enrich_road_proximity.py::test_each_eligible_class_has_independent_distance`
- `tests/unit/test_enrich_road_proximity.py::test_eligible_class_rejects_unsupported_geometry`
- `tests/unit/test_enrich_road_proximity.py::test_eligible_class_requires_valid_geometry_status`
- `tests/unit/test_enrich_road_proximity.py::test_empty_eligible_class_emits_null_row_per_parcel`
- `tests/unit/test_enrich_road_proximity.py::test_exact_tie_counts_two_and_lexical_id_wins`
- `tests/unit/test_enrich_road_proximity.py::test_independent_policy_sha_mismatch_is_rejected`
- `tests/unit/test_enrich_road_proximity.py::test_intersecting_or_touching_road_has_zero_distance`
- `tests/unit/test_enrich_road_proximity.py::test_invalid_parcel_identity_is_rejected`
- `tests/unit/test_enrich_road_proximity.py::test_known_polygon_to_line_distance_is_ten_metres`
- `tests/unit/test_enrich_road_proximity.py::test_matched_output_dtypes_are_stable`
- `tests/unit/test_enrich_road_proximity.py::test_missing_or_inactive_geometry_is_rejected`
- `tests/unit/test_enrich_road_proximity.py::test_missing_or_wrong_storage_crs_is_rejected`
- `tests/unit/test_enrich_road_proximity.py::test_missing_road_policy_lineage_is_rejected`
- `tests/unit/test_enrich_road_proximity.py::test_near_not_distance_road_cannot_change_general_distance`
- `tests/unit/test_enrich_road_proximity.py::test_no_business_decision_columns_or_implementation_exist`
- `tests/unit/test_enrich_road_proximity.py::test_not_distance_road_is_counted_but_never_indexed`
- `tests/unit/test_enrich_road_proximity.py::test_output_shape_columns_and_order_are_deterministic`
- `tests/unit/test_enrich_road_proximity.py::test_parcel_preservation_uses_exact_non_geometry_values`
- `tests/unit/test_enrich_road_proximity.py::test_parcels_and_road_application_are_not_mutated`
- `tests/unit/test_enrich_road_proximity.py::test_policy_sha_mismatch_does_not_construct_spatial_index`
- `tests/unit/test_enrich_road_proximity.py::test_polygon_and_multipolygon_are_accepted`
- `tests/unit/test_enrich_road_proximity.py::test_result_dataclasses_are_frozen`
- `tests/unit/test_enrich_road_proximity.py::test_result_parcel_frame_is_an_independent_copy`
- `tests/unit/test_enrich_road_proximity.py::test_selected_road_evidence_and_lineage_are_exact`
- `tests/unit/test_enrich_road_proximity.py::test_selected_rows_belong_to_requested_class`
- `tests/unit/test_enrich_road_proximity.py::test_single_nearest_road_has_tie_count_one`
- `tests/unit/test_enrich_road_proximity.py::test_storage_geometry_stays_epsg4326_while_distance_is_metric`
- `tests/unit/test_enrich_road_proximity.py::test_tie_winner_is_independent_of_source_order`
- `tests/unit/test_enrich_road_proximity.py::test_unequal_distance_wins_regardless_of_identifier`
- `tests/unit/test_enrich_road_proximity.py::test_unknown_road_proxy_class_is_rejected`
- `tests/unit/test_enrich_road_proximity.py::test_wrong_parcel_geometry_kind_is_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_row`

**Signature**

```python
def _row(result: ParcelRoadProximityResult, road_class: str) -> pd.Series:
```

**Purpose**

Implements row according to the exact implementation and guards in this file.

**Inputs**

- `result` (`ParcelRoadProximityResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `road_class` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

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

- `tests/unit/test_enrich_road_proximity.py` — `test_distance_uses_full_polygon_not_centroid`
- `tests/unit/test_enrich_road_proximity.py` — `test_each_eligible_class_has_independent_distance`
- `tests/unit/test_enrich_road_proximity.py` — `test_exact_tie_counts_two_and_lexical_id_wins`
- `tests/unit/test_enrich_road_proximity.py` — `test_intersecting_or_touching_road_has_zero_distance`
- `tests/unit/test_enrich_road_proximity.py` — `test_known_polygon_to_line_distance_is_ten_metres`
- `tests/unit/test_enrich_road_proximity.py` — `test_near_not_distance_road_cannot_change_general_distance`
- `tests/unit/test_enrich_road_proximity.py` — `test_selected_road_evidence_and_lineage_are_exact`
- `tests/unit/test_enrich_road_proximity.py` — `test_single_nearest_road_has_tie_count_one`
- `tests/unit/test_enrich_road_proximity.py` — `test_storage_geometry_stays_epsg4326_while_distance_is_metric`
- `tests/unit/test_enrich_road_proximity.py` — `test_tie_winner_is_independent_of_source_order`
- `tests/unit/test_enrich_road_proximity.py` — `test_unequal_distance_wins_regardless_of_identifier`

**Tests**

- `tests/unit/test_enrich_road_proximity.py::test_distance_uses_full_polygon_not_centroid`
- `tests/unit/test_enrich_road_proximity.py::test_each_eligible_class_has_independent_distance`
- `tests/unit/test_enrich_road_proximity.py::test_exact_tie_counts_two_and_lexical_id_wins`
- `tests/unit/test_enrich_road_proximity.py::test_intersecting_or_touching_road_has_zero_distance`
- `tests/unit/test_enrich_road_proximity.py::test_known_polygon_to_line_distance_is_ten_metres`
- `tests/unit/test_enrich_road_proximity.py::test_near_not_distance_road_cannot_change_general_distance`
- `tests/unit/test_enrich_road_proximity.py::test_selected_road_evidence_and_lineage_are_exact`
- `tests/unit/test_enrich_road_proximity.py::test_single_nearest_road_has_tie_count_one`
- `tests/unit/test_enrich_road_proximity.py::test_storage_geometry_stays_epsg4326_while_distance_is_metric`
- `tests/unit/test_enrich_road_proximity.py::test_tie_winner_is_independent_of_source_order`
- `tests/unit/test_enrich_road_proximity.py::test_unequal_distance_wins_regardless_of_identifier`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_corrupt_nearest_output`

**Signature**

```python
def _corrupt_nearest_output(column: str, value: object) -> None:
```

**Purpose**

Implements corrupt nearest output according to the exact implementation and guards in this file.

**Inputs**

- `column` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. Observed return expression(s): `output`.

**Algorithm**

1. Executes `import landscout.stages.enrich_road_proximity as module`.
2. Computes `original` from `module._nearest_class_rows`.
3. Defines the local helper `corrupted`; its behavior is documented with the parent function's nested helpers.
4. Enters managed context(s) `patch.object(module, '_nearest_class_rows', side_effect=corrupted), pytest.raises(RoadProximityError)` and executes: Calls `_enrich()` for its validation or side effect.

**Meaningful nested/local helpers**

- `corrupted` — `def corrupted(*args: object, **kwargs: object) -> pd.DataFrame:`. It executes 3 top-level statement(s), uses `original`, `output['distance_m'].notna`, `output['distance_m'].notna().any`, `output[column].astype`, and has no explicit raises. Trivial test callbacks are intentionally grouped here with their parent.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_enrich`, `original`, `output['distance_m'].notna`, `output['distance_m'].notna().any`, `output[column].astype`, `patch.object`, `pytest.raises`.

**Known repository callers**

- `tests/unit/test_enrich_road_proximity.py` — `test_malformed_produced_distance_is_rejected`
- `tests/unit/test_enrich_road_proximity.py` — `test_malformed_produced_tie_count_is_rejected`

**Tests**

- `tests/unit/test_enrich_road_proximity.py::test_malformed_produced_distance_is_rejected`
- `tests/unit/test_enrich_road_proximity.py::test_malformed_produced_tie_count_is_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_corrupt_nearest_output.corrupted`

**Signature**

```python
def corrupted(*args: object, **kwargs: object) -> pd.DataFrame:
```

**Purpose**

Implements corrupted according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `output`.

**Algorithm**

1. Computes `output` from `original(*args, **kwargs)`.
2. Checks `output['distance_m'].notna().any()`. When true: Computes `output[column]` from `output[column].astype('object')`. Computes `output.at[0, column]` from `value`.
3. Returns `output`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `original`, `output['distance_m'].notna`, `output['distance_m'].notna().any`, `output[column].astype`.

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
- Contains 1 explicit setup/context statement(s).
- Computes `expected` from `{'RoadProximityError', 'RoadProxyClassCoverage', 'ParcelRoadProximityResult', 'enrich_parcel_road_proximity'}`.

**Action**

- Calls `all`, `hasattr`.

**Expected result**

- Direct assertions: `assert set(module.__all__) == expected`; `assert expected <= set(stages.__all__)`; `assert all((hasattr(stages, symbol) for symbol in expected))`; `assert not hasattr(stages, '_nearest_class_rows')`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `public api exports only stable symbols` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `all`, `hasattr`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_wrong_parcel_type_has_controlled_error`

**Signature**

```python
def test_wrong_parcel_type_has_controlled_error() -> None:
```

**Purpose**

Protects the `wrong parcel type has controlled error` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(RoadProximityError)` and executes: Calls `enrich_parcel_road_proximity(cast(Any, pd.DataFrame()), _source(), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_source`, `cast`, `enrich_parcel_road_proximity`, `pd.DataFrame`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(RoadProximityError): enrich_parcel_road_proximity(cast(Any, pd.DataFrame()), _source(), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `wrong parcel type has controlled error` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source`, `cast`, `enrich_parcel_road_proximity`, `pd.DataFrame`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_wrong_road_source_type_has_controlled_error`

**Signature**

```python
def test_wrong_road_source_type_has_controlled_error() -> None:
```

**Purpose**

Protects the `wrong road source type has controlled error` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(RoadProximityError)` and executes: Calls `enrich_parcel_road_proximity(_parcels(), cast(Any, object()), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_parcels`, `cast`, `enrich_parcel_road_proximity`, `object`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(RoadProximityError): enrich_parcel_road_proximity(_parcels(), cast(Any, object()), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `wrong road source type has controlled error` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `cast`, `enrich_parcel_road_proximity`, `object`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_wrong_source_config_type_has_controlled_error`

**Signature**

```python
def test_wrong_source_config_type_has_controlled_error() -> None:
```

**Purpose**

Protects the `wrong source config type has controlled error` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(RoadProximityError)` and executes: Calls `enrich_parcel_road_proximity(_parcels(), _source(), cast(Any, object()))` for its validation or side effect.

**Action**

- Calls `_parcels`, `_source`, `cast`, `enrich_parcel_road_proximity`, `object`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(RoadProximityError): enrich_parcel_road_proximity(_parcels(), _source(), cast(Any, object()))`.

**Regression protected**

- Protects the exact `wrong source config type has controlled error` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_source`, `cast`, `enrich_parcel_road_proximity`, `object`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_wrong_policy_path_type_has_controlled_error`

**Signature**

```python
def test_wrong_policy_path_type_has_controlled_error() -> None:
```

**Purpose**

Protects the `wrong policy path type has controlled error` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(RoadProximityError)` and executes: Calls `enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG, cast(Any, 'policy.yaml'))` for its validation or side effect.

**Action**

- Calls `_parcels`, `_source`, `cast`, `enrich_parcel_road_proximity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(RoadProximityError): enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG, cast(Any, 'policy.yaml'))`.

**Regression protected**

- Protects the exact `wrong policy path type has controlled error` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_source`, `cast`, `enrich_parcel_road_proximity`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_stage_is_invoked_exactly_once`

**Signature**

```python
def test_application_stage_is_invoked_exactly_once() -> None:
```

**Purpose**

Protects the `application stage is invoked exactly once` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `application` from `IgnRoadVehicleProxyApplicationResult(_roads())`.
- Enters managed context(s) `patch('landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy', return_value=application)` and executes: Calls `enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `IgnRoadVehicleProxyApplicationResult`, `_parcels`, `_roads`, `_source`, `enrich_parcel_road_proximity`, `source_application.assert_called_once`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `application stage is invoked exactly once` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `IgnRoadVehicleProxyApplicationResult`, `_parcels`, `_roads`, `_source`, `enrich_parcel_road_proximity`, `patch`, `source_application.assert_called_once`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_failure_stops_proximity`

**Signature**

```python
def test_application_failure_stops_proximity() -> None:
```

**Purpose**

Protects the `application failure stops proximity` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `patch('landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy', side_effect=IgnRoadVehicleProxyApplicationError('bad source')), patch('landscout.stages.enrich_road_proximity.STRtree'), pytest.raises(RoadProximityError)` and executes: Calls `enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `IgnRoadVehicleProxyApplicationError`, `_parcels`, `_source`, `enrich_parcel_road_proximity`, `spatial_index.assert_not_called`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with patch('landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy', side_effect=IgnRoadVehicleProxyApplicationError('bad source')), patch('landscout.stages.enrich_road_proximity.STRtree') as spatial_index, pytest.raises(RoadProximityError): enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `application failure stops proximity` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `IgnRoadVehicleProxyApplicationError`, `_parcels`, `_source`, `enrich_parcel_road_proximity`, `patch`, `pytest.raises`, `spatial_index.assert_not_called`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_policy_stops_before_application`

**Signature**

```python
def test_malformed_policy_stops_before_application(tmp_path: Path) -> None:
```

**Purpose**

Protects the `malformed policy stops before application` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `path` from `tmp_path / 'policy.yaml'`.
- Enters managed context(s) `patch('landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy'), pytest.raises(RoadProximityError)` and executes: Calls `enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG, path)` for its validation or side effect.

**Action**

- Calls `_parcels`, `_source`, `enrich_parcel_road_proximity`, `path.write_text`, `source_application.assert_not_called`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with patch('landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy') as source_application, pytest.raises(RoadProximityError): enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG, path)`.

**Regression protected**

- Protects the exact `malformed policy stops before application` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_source`, `enrich_parcel_road_proximity`, `patch`, `path.write_text`, `pytest.raises`, `source_application.assert_not_called`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_independent_policy_sha_mismatch_is_rejected`

**Signature**

```python
def test_independent_policy_sha_mismatch_is_rejected() -> None:
```

**Purpose**

Protects the `independent policy sha mismatch is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `roads` from `_roads()`.
- Computes `roads['road_proxy_policy_config_sha256']` from `'b' * 64`.
- Enters managed context(s) `pytest.raises(RoadProximityError, match='policy|SHA|lineage')` and executes: Calls `_enrich(roads=roads)` for its validation or side effect.

**Action**

- Calls `_enrich`, `_roads`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(RoadProximityError, match='policy|SHA|lineage'): _enrich(roads=roads)`.

**Regression protected**

- Protects the exact `independent policy sha mismatch is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `_roads`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_parcel_identity_is_rejected`

**Signature**

```python
def test_invalid_parcel_identity_is_rejected(
    mutation: Any, message: str
) -> None:
```

**Purpose**

Protects the `invalid parcel identity is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `mutation`, `message`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(RoadProximityError, match=message)` and executes: Calls `_enrich(parcels=mutation(_parcels()))` for its validation or side effect.

**Action**

- Calls `_enrich`, `_parcels`, `frame.assign`, `frame.drop`, `mutation`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(RoadProximityError, match=message): _enrich(parcels=mutation(_parcels()))`.

**Regression protected**

- Protects the exact `invalid parcel identity is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `_parcels`, `frame.assign`, `frame.drop`, `mutation`, `pytest.mark.parametrize`, `pytest.raises`.

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
- Enters managed context(s) `pytest.raises(RoadProximityError, match='unique')` and executes: Calls `_enrich(parcels=parcels)` for its validation or side effect.

**Action**

- Calls `Polygon`, `_enrich`, `_parcels`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(RoadProximityError, match='unique'): _enrich(parcels=parcels)`.

**Regression protected**

- Protects the exact `duplicate parcel id is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `_enrich`, `_parcels`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_parcel_columns_are_rejected`

**Signature**

```python
def test_duplicate_parcel_columns_are_rejected() -> None:
```

**Purpose**

Protects the `duplicate parcel columns are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `parcels` from `_parcels()`.
- Computes `duplicated` from `gpd.GeoDataFrame(pd.concat([parcels, parcels[['parcel_id']]], axis=1), geometry='geometry', crs=parcels.crs)`.
- Enters managed context(s) `pytest.raises(RoadProximityError, match='duplicate')` and executes: Calls `_enrich(parcels=duplicated)` for its validation or side effect.

**Action**

- Calls `_enrich`, `_parcels`, `gpd.GeoDataFrame`, `pd.concat`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(RoadProximityError, match='duplicate'): _enrich(parcels=duplicated)`.

**Regression protected**

- Protects the exact `duplicate parcel columns are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `_parcels`, `gpd.GeoDataFrame`, `pd.concat`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_or_inactive_geometry_is_rejected`

**Signature**

```python
def test_missing_or_inactive_geometry_is_rejected() -> None:
```

**Purpose**

Protects the `missing or inactive geometry is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `parcels` from `_parcels()`.
- Computes `missing` from `parcels.drop(columns='geometry')`.
- Computes `inactive` from `parcels.assign(other_geometry=parcels.geometry).set_geometry('other_geometry')`.
- Enters managed context(s) `pytest.raises(RoadProximityError, match='geometry')` and executes: Calls `_enrich(parcels=missing)` for its validation or side effect.
- Enters managed context(s) `pytest.raises(RoadProximityError, match='active')` and executes: Calls `_enrich(parcels=inactive)` for its validation or side effect.

**Action**

- Calls `_enrich`, `_parcels`, `parcels.assign`, `parcels.assign(other_geometry=parcels.geometry).set_geometry`, `parcels.drop`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(RoadProximityError, match='geometry'): _enrich(parcels=missing)`; `with pytest.raises(RoadProximityError, match='active'): _enrich(parcels=inactive)`.

**Regression protected**

- Protects the exact `missing or inactive geometry is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `_parcels`, `parcels.assign`, `parcels.assign(other_geometry=parcels.geometry).set_geometry`, `parcels.drop`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_or_wrong_storage_crs_is_rejected`

**Signature**

```python
def test_missing_or_wrong_storage_crs_is_rejected() -> None:
```

**Purpose**

Protects the `missing or wrong storage crs is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `missing` from `_parcels().set_crs(None, allow_override=True)`.
- Computes `wrong` from `_metric_parcels()`.
- Enters managed context(s) `pytest.raises(RoadProximityError, match='CRS')` and executes: Calls `_enrich(parcels=missing)` for its validation or side effect.
- Enters managed context(s) `pytest.raises(RoadProximityError, match='4326')` and executes: Calls `_enrich(parcels=wrong)` for its validation or side effect.

**Action**

- Calls `_enrich`, `_metric_parcels`, `_parcels`, `_parcels().set_crs`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(RoadProximityError, match='CRS'): _enrich(parcels=missing)`; `with pytest.raises(RoadProximityError, match='4326'): _enrich(parcels=wrong)`.

**Regression protected**

- Protects the exact `missing or wrong storage crs is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `_metric_parcels`, `_parcels`, `_parcels().set_crs`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_wrong_parcel_geometry_kind_is_rejected`

**Signature**

```python
def test_wrong_parcel_geometry_kind_is_rejected(geometry: object) -> None:
```

**Purpose**

Protects the `wrong parcel geometry kind is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(RoadProximityError, match='Polygon|MultiPolygon')` and executes: Calls `_enrich(parcels=_parcels([geometry]))` for its validation or side effect.

**Action**

- Calls `LineString`, `Point`, `_enrich`, `_parcels`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(RoadProximityError, match='Polygon|MultiPolygon'): _enrich(parcels=_parcels([geometry]))`.

**Regression protected**

- Protects the exact `wrong parcel geometry kind is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `Point`, `_enrich`, `_parcels`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_bad_parcel_geometry_is_rejected`

**Signature**

```python
def test_bad_parcel_geometry_is_rejected(
    geometry: object, message: str
) -> None:
```

**Purpose**

Protects the `bad parcel geometry is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry`, `message`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(RoadProximityError, match=message)` and executes: Calls `_enrich(parcels=_parcels([geometry]))` for its validation or side effect.

**Action**

- Calls `Polygon`, `_enrich`, `_parcels`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(RoadProximityError, match=message): _enrich(parcels=_parcels([geometry]))`.

**Regression protected**

- Protects the exact `bad parcel geometry is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `_enrich`, `_parcels`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_polygon_and_multipolygon_are_accepted`

**Signature**

```python
def test_polygon_and_multipolygon_are_accepted(geometry: object) -> None:
```

**Purpose**

Protects the `polygon and multipolygon are accepted` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry`.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `MultiPolygon`, `Polygon`, `_enrich`, `_parcels`.

**Expected result**

- Direct assertions: `assert len(_enrich(parcels=_parcels([geometry])).parcels) == 1`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `polygon and multipolygon are accepted` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `MultiPolygon`, `Polygon`, `_enrich`, `_parcels`, `len`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_wrong_application_result_type_is_rejected`

**Signature**

```python
def test_wrong_application_result_type_is_rejected() -> None:
```

**Purpose**

Protects the `wrong application result type is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `patch('landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy', return_value=object()), pytest.raises(RoadProximityError)` and executes: Calls `enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_parcels`, `_source`, `enrich_parcel_road_proximity`, `object`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with patch('landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy', return_value=object()), pytest.raises(RoadProximityError): enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `wrong application result type is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_source`, `enrich_parcel_road_proximity`, `object`, `patch`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_roads_must_be_geodataframe`

**Signature**

```python
def test_application_roads_must_be_geodataframe() -> None:
```

**Purpose**

Protects the `application roads must be geodataframe` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `application` from `IgnRoadVehicleProxyApplicationResult(cast(Any, pd.DataFrame(_roads().drop(columns='geometry'))))`.
- Enters managed context(s) `patch('landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy', return_value=application), pytest.raises(RoadProximityError)` and executes: Calls `enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `IgnRoadVehicleProxyApplicationResult`, `_parcels`, `_roads`, `_roads().drop`, `_source`, `cast`, `enrich_parcel_road_proximity`, `pd.DataFrame`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with patch('landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy', return_value=application), pytest.raises(RoadProximityError): enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `application roads must be geodataframe` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `IgnRoadVehicleProxyApplicationResult`, `_parcels`, `_roads`, `_roads().drop`, `_source`, `cast`, `enrich_parcel_road_proximity`, `patch`, `pd.DataFrame`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_road_feature_id_is_rejected`

**Signature**

```python
def test_duplicate_road_feature_id_is_rejected() -> None:
```

**Purpose**

Protects the `duplicate road feature id is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `roads` from `_roads()`.
- Computes `roads.loc[1, 'road_feature_id']` from `roads.loc[0, 'road_feature_id']`.
- Enters managed context(s) `pytest.raises(RoadProximityError, match='unique')` and executes: Calls `_enrich(roads=roads)` for its validation or side effect.

**Action**

- Calls `_enrich`, `_roads`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(RoadProximityError, match='unique'): _enrich(roads=roads)`.

**Regression protected**

- Protects the exact `duplicate road feature id is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `_roads`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unknown_road_proxy_class_is_rejected`

**Signature**

```python
def test_unknown_road_proxy_class_is_rejected() -> None:
```

**Purpose**

Protects the `unknown road proxy class is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `roads` from `_roads()`.
- Computes `roads.loc[0, 'road_proxy_class']` from `'INVENTED'`.
- Enters managed context(s) `pytest.raises(RoadProximityError, match='class')` and executes: Calls `_enrich(roads=roads)` for its validation or side effect.

**Action**

- Calls `_enrich`, `_roads`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(RoadProximityError, match='class'): _enrich(roads=roads)`.

**Regression protected**

- Protects the exact `unknown road proxy class is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `_roads`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_road_policy_lineage_is_rejected`

**Signature**

```python
def test_missing_road_policy_lineage_is_rejected(column: str) -> None:
```

**Purpose**

Protects the `missing road policy lineage is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(RoadProximityError, match='column|lineage')` and executes: Calls `_enrich(roads=_roads().drop(columns=column))` for its validation or side effect.

**Action**

- Calls `_enrich`, `_roads`, `_roads().drop`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(RoadProximityError, match='column|lineage'): _enrich(roads=_roads().drop(columns=column))`.

**Regression protected**

- Protects the exact `missing road policy lineage is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `_roads`, `_roads().drop`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_eligible_class_requires_valid_geometry_status`

**Signature**

```python
def test_eligible_class_requires_valid_geometry_status(status: str) -> None:
```

**Purpose**

Protects the `eligible class requires valid geometry status` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `status`.
- Contains 3 explicit setup/context statement(s).
- Computes `roads` from `_roads()`.
- Computes `roads.loc[0, 'geometry_status']` from `status`.
- Enters managed context(s) `pytest.raises(RoadProximityError, match='VALID')` and executes: Calls `_enrich(roads=roads)` for its validation or side effect.

**Action**

- Calls `_enrich`, `_roads`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(RoadProximityError, match='VALID'): _enrich(roads=roads)`.

**Regression protected**

- Protects the exact `eligible class requires valid geometry status` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `_roads`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_eligible_class_rejects_unsupported_geometry`

**Signature**

```python
def test_eligible_class_rejects_unsupported_geometry() -> None:
```

**Purpose**

Protects the `eligible class rejects unsupported geometry` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `roads` from `_roads()`.
- Computes `roads.at[0, 'geometry']` from `Point(20, 0)`.
- Enters managed context(s) `pytest.raises(RoadProximityError, match='LineString|geometry')` and executes: Calls `_enrich(roads=roads)` for its validation or side effect.

**Action**

- Calls `Point`, `_enrich`, `_roads`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(RoadProximityError, match='LineString|geometry'): _enrich(roads=roads)`.

**Regression protected**

- Protects the exact `eligible class rejects unsupported geometry` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Point`, `_enrich`, `_roads`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_not_distance_road_is_counted_but_never_indexed`

**Signature**

```python
def test_not_distance_road_is_counted_but_never_indexed() -> None:
```

**Purpose**

Protects the `not distance road is counted but never indexed` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `roads` from `_roads()`.
- Computes `roads.loc[roads['road_proxy_class'].eq('NOT_DISTANCE_PROXY'), 'geometry_status']` from `'INVALID'`.
- Computes `result` from `_enrich(roads=roads)`.
- Computes `coverage` from `{item.road_proxy_class: item for item in result.class_coverage}`.

**Action**

- Calls `_enrich`, `_roads`, `roads['road_proxy_class'].eq`.

**Expected result**

- Direct assertions: `assert coverage['NOT_DISTANCE_PROXY'].feature_count == 1`; `assert not coverage['NOT_DISTANCE_PROXY'].distance_eligible`; `assert 'NOT_DISTANCE_PROXY' not in set(result.class_proximity.road_proxy_class)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `not distance road is counted but never indexed` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `_roads`, `roads['road_proxy_class'].eq`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_known_polygon_to_line_distance_is_ten_metres`

**Signature**

```python
def test_known_polygon_to_line_distance_is_ten_metres() -> None:
```

**Purpose**

Protects the `known polygon to line distance is ten metres` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `result` from `_enrich()`.

**Action**

- Calls `_enrich`, `_row`.

**Expected result**

- Direct assertions: `assert _row(result, 'GENERAL_VEHICLE_PROXY').nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-05)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `known polygon to line distance is ten metres` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `_row`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_intersecting_or_touching_road_has_zero_distance`

**Signature**

```python
def test_intersecting_or_touching_road_has_zero_distance(x: float) -> None:
```

**Purpose**

Protects the `intersecting or touching road has zero distance` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `x`.
- Contains 1 explicit setup/context statement(s).
- Computes `roads` from `_roads([_road_row('GENERAL_VEHICLE_PROXY', x, identifier='ROAD-GENERAL')])`.

**Action**

- Calls `_enrich`, `_road_row`, `_roads`, `_row`.

**Expected result**

- Direct assertions: `assert _row(_enrich(roads=roads), 'GENERAL_VEHICLE_PROXY').nearest_road_proxy_distance_m == pytest.approx(0.0, abs=1e-05)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `intersecting or touching road has zero distance` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `_road_row`, `_roads`, `_row`, `pytest.approx`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_distance_uses_full_polygon_not_centroid`

**Signature**

```python
def test_distance_uses_full_polygon_not_centroid() -> None:
```

**Purpose**

Protects the `distance uses full polygon not centroid` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `distance` from `_row(_enrich(), 'GENERAL_VEHICLE_PROXY').nearest_road_proxy_distance_m`.

**Action**

- Calls `_enrich`, `_row`.

**Expected result**

- Direct assertions: `assert distance == pytest.approx(10.0, abs=1e-05)`; `assert distance != pytest.approx(15.0, abs=1e-05)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `distance uses full polygon not centroid` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `_row`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_storage_geometry_stays_epsg4326_while_distance_is_metric`

**Signature**

```python
def test_storage_geometry_stays_epsg4326_while_distance_is_metric() -> None:
```

**Purpose**

Protects the `storage geometry stays epsg4326 while distance is metric` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `parcels` from `_parcels()`.
- Computes `before` from `deepcopy(parcels)`.
- Computes `result` from `_enrich(parcels=parcels)`.

**Action**

- Calls `_enrich`, `_parcels`, `_row`, `deepcopy`, `result.parcels.crs.to_epsg`.

**Expected result**

- Direct assertions: `assert result.parcels.crs == parcels.crs`; `assert result.parcels.crs.to_epsg() == 4326`; `assert _row(result, 'GENERAL_VEHICLE_PROXY').nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-05)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `storage geometry stays epsg4326 while distance is metric` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `_parcels`, `_row`, `assert_geodataframe_equal`, `deepcopy`, `pytest.approx`, `result.parcels.crs.to_epsg`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_each_eligible_class_has_independent_distance`

**Signature**

```python
def test_each_eligible_class_has_independent_distance() -> None:
```

**Purpose**

Protects the `each eligible class has independent distance` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_enrich()`.
- Computes `distances` from `{road_class: _row(result, road_class).nearest_road_proxy_distance_m for road_class in ELIGIBLE_CLASSES}`.

**Action**

- Calls `_enrich`, `_row`.

**Expected result**

- Direct assertions: `assert distances == pytest.approx({'GENERAL_VEHICLE_PROXY': 10.0, 'LIMITED_VEHICLE_PROXY': 20.0, 'RESTRICTED_REVIEW': 5.0, 'NOT_GENERAL_VEHICLE_PROXY': 30.0, 'UNKNOWN_REVIEW': 40.0}, abs=1e-05)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `each eligible class has independent distance` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `_row`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_near_not_distance_road_cannot_change_general_distance`

**Signature**

```python
def test_near_not_distance_road_cannot_change_general_distance() -> None:
```

**Purpose**

Protects the `near not distance road cannot change general distance` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `result` from `_enrich()`.

**Action**

- Calls `_enrich`, `_row`, `result.class_proximity.nearest_road_feature_id.dropna`.

**Expected result**

- Direct assertions: `assert _row(result, 'GENERAL_VEHICLE_PROXY').nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-05)`; `assert 'ROAD-NOT-DISTANCE' not in set(result.class_proximity.nearest_road_feature_id.dropna())`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `near not distance road cannot change general distance` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `_row`, `pytest.approx`, `result.class_proximity.nearest_road_feature_id.dropna`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_single_nearest_road_has_tie_count_one`

**Signature**

```python
def test_single_nearest_road_has_tie_count_one() -> None:
```

**Purpose**

Protects the `single nearest road has tie count one` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `_enrich`, `_row`.

**Expected result**

- Direct assertions: `assert _row(_enrich(), 'GENERAL_VEHICLE_PROXY').nearest_road_tie_count == 1`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `single nearest road has tie count one` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `_row`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_exact_tie_counts_two_and_lexical_id_wins`

**Signature**

```python
def test_exact_tie_counts_two_and_lexical_id_wins() -> None:
```

**Purpose**

Protects the `exact tie counts two and lexical id wins` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `roads` from `_roads([_road_row('GENERAL_VEHICLE_PROXY', -10, identifier='Z-ROAD'), _road_row('GENERAL_VEHICLE_PROXY', 20, identifier='A-ROAD')])`.
- Computes `row` from `_row(_enrich(roads=roads), 'GENERAL_VEHICLE_PROXY')`.

**Action**

- Calls `_enrich`, `_road_row`, `_roads`, `_row`.

**Expected result**

- Direct assertions: `assert row.nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-05)`; `assert row.nearest_road_tie_count == 2`; `assert row.nearest_road_feature_id == 'A-ROAD'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `exact tie counts two and lexical id wins` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `_road_row`, `_roads`, `_row`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_tie_winner_is_independent_of_source_order`

**Signature**

```python
def test_tie_winner_is_independent_of_source_order() -> None:
```

**Purpose**

Protects the `tie winner is independent of source order` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `roads` from `_roads([_road_row('GENERAL_VEHICLE_PROXY', -10, identifier='Z-ROAD'), _road_row('GENERAL_VEHICLE_PROXY', 20, identifier='A-ROAD')])`.
- Computes `forward` from `_row(_enrich(roads=roads), 'GENERAL_VEHICLE_PROXY')`.
- Computes `reverse` from `_row(_enrich(roads=roads.iloc[::-1].reset_index(drop=True)), 'GENERAL_VEHICLE_PROXY')`.

**Action**

- Calls `_enrich`, `_road_row`, `_roads`, `_row`, `roads.iloc[::-1].reset_index`.

**Expected result**

- Direct assertions: `assert forward.nearest_road_feature_id == 'A-ROAD'`; `assert reverse.nearest_road_feature_id == 'A-ROAD'`; `assert forward.nearest_road_tie_count == reverse.nearest_road_tie_count == 2`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `tie winner is independent of source order` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `_road_row`, `_roads`, `_row`, `roads.iloc[::-1].reset_index`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unequal_distance_wins_regardless_of_identifier`

**Signature**

```python
def test_unequal_distance_wins_regardless_of_identifier() -> None:
```

**Purpose**

Protects the `unequal distance wins regardless of identifier` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `roads` from `_roads([_road_row('GENERAL_VEHICLE_PROXY', 20, identifier='Z-NEAR'), _road_row('GENERAL_VEHICLE_PROXY', 30, identifier='A-FAR')])`.

**Action**

- Calls `_enrich`, `_road_row`, `_roads`, `_row`.

**Expected result**

- Direct assertions: `assert _row(_enrich(roads=roads), 'GENERAL_VEHICLE_PROXY').nearest_road_feature_id == 'Z-NEAR'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `unequal distance wins regardless of identifier` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `_road_row`, `_roads`, `_row`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_empty_eligible_class_emits_null_row_per_parcel`

**Signature**

```python
def test_empty_eligible_class_emits_null_row_per_parcel() -> None:
```

**Purpose**

Protects the `empty eligible class emits null row per parcel` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `roads` from `_roads().loc[~_roads()['road_proxy_class'].eq('UNKNOWN_REVIEW')].reset_index(drop=True)`.
- Computes `parcels` from `_parcels([Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]), Polygon([(50, 0), (50, 10), (60, 10), (60, 0), (50, 0)])])`.
- Computes `result` from `_enrich(parcels=parcels, roads=roads)`.
- Computes `rows` from `result.class_proximity.loc[result.class_proximity.road_proxy_class.eq('UNKNOWN_REVIEW')]`.
- Computes `coverage` from `{item.road_proxy_class: item for item in result.class_coverage}`.

**Action**

- Calls `Polygon`, `_enrich`, `_parcels`, `_roads`, `_roads().loc[~_roads()['road_proxy_class'].eq('UNKNOWN_REVIEW')].reset_index`, `_roads()['road_proxy_class'].eq`, `result.class_proximity.road_proxy_class.eq`, `rows.loc[:, list(SELECTED_COLUMNS)].isna`, `rows.loc[:, list(SELECTED_COLUMNS)].isna().all`, `rows.loc[:, list(SELECTED_COLUMNS)].isna().all().all`.

**Expected result**

- Direct assertions: `assert len(rows) == 2`; `assert rows.loc[:, list(SELECTED_COLUMNS)].isna().all().all()`; `assert coverage['UNKNOWN_REVIEW'].feature_count == 0`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `empty eligible class emits null row per parcel` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `_enrich`, `_parcels`, `_roads`, `_roads().loc[~_roads()['road_proxy_class'].eq('UNKNOWN_REVIEW')].reset_index`, `_roads()['road_proxy_class'].eq`, `len`, `list`, `result.class_proximity.road_proxy_class.eq`, `rows.loc[:, list(SELECTED_COLUMNS)].isna`, `rows.loc[:, list(SELECTED_COLUMNS)].isna().all`, `rows.loc[:, list(SELECTED_COLUMNS)].isna().all().all`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_output_shape_columns_and_order_are_deterministic`

**Signature**

```python
def test_output_shape_columns_and_order_are_deterministic() -> None:
```

**Purpose**

Protects the `output shape columns and order are deterministic` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `parcels` from `_parcels([Polygon([(50, 0), (50, 10), (60, 10), (60, 0), (50, 0)]), Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])], identifiers=['SECOND', 'FIRST'])`.
- Computes `result` from `_enrich(parcels=parcels)`.

**Action**

- Calls `Polygon`, `_enrich`, `_parcels`, `result.class_proximity.parcel_id.tolist`, `result.class_proximity.road_proxy_class.tolist`.

**Expected result**

- Direct assertions: `assert len(result.class_proximity) == len(parcels) * 5`; `assert list(result.class_proximity.columns) == list(CLASS_PROXIMITY_COLUMNS)`; `assert result.class_proximity.parcel_id.tolist() == [value for parcel_id in ('SECOND', 'FIRST') for value in [parcel_id] * 5]`; `assert result.class_proximity.road_proxy_class.tolist() == list(ELIGIBLE_CLASSES) * 2`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `output shape columns and order are deterministic` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `_enrich`, `_parcels`, `len`, `list`, `result.class_proximity.parcel_id.tolist`, `result.class_proximity.road_proxy_class.tolist`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_class_coverage_is_complete_and_strict`

**Signature**

```python
def test_class_coverage_is_complete_and_strict() -> None:
```

**Purpose**

Protects the `class coverage is complete and strict` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `result` from `_enrich()`.

**Action**

- Calls `_enrich`, `all`, `sum`.

**Expected result**

- Direct assertions: `assert tuple((item.road_proxy_class for item in result.class_coverage)) == ALL_CLASSES`; `assert sum((item.feature_count for item in result.class_coverage)) == 6`; `assert all((item.distance_eligible == (item.road_proxy_class != 'NOT_DISTANCE_PROXY') for item in result.class_coverage))`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `class coverage is complete and strict` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `all`, `sum`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_selected_road_evidence_and_lineage_are_exact`

**Signature**

```python
def test_selected_road_evidence_and_lineage_are_exact() -> None:
```

**Purpose**

Protects the `selected road evidence and lineage are exact` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `policy` from `load_ign_road_vehicle_proxy_policy()`.
- Computes `row` from `_row(_enrich(), 'GENERAL_VEHICLE_PROXY')`.

**Action**

- Calls `_enrich`, `_row`, `load_ign_road_vehicle_proxy_policy`.

**Expected result**

- Direct assertions: `assert row.nearest_road_feature_id == 'ROAD-GENERAL'`; `assert row.nearest_source_feature_id == 'SOURCE-ROAD-GENERAL'`; `assert row.nearest_road_primary_rule == 'OPEN_OR_TOLL'`; `assert row.nearest_road_rule_trace_json == '["OPEN_OR_TOLL"]'`; `assert row.nearest_road_unknown_fields_json == '[]'`; `assert not row.nearest_road_toll_evidence`; `assert row.nearest_source_archive_sha256 == 'a' * 64`; `assert row.road_proxy_policy_id == policy.policy_id`; `assert row.road_proxy_policy_schema_version == policy.schema_version`; `assert row.road_proxy_policy_config_sha256 == policy.config_sha256`; `assert row.road_proxy_heavy_vehicle_access == 'NOT_PROVEN'`; `assert row.proximity_scope == 'WITHIN_VERIFIED_SOURCE_PACKAGE'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `selected road evidence and lineage are exact` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `_row`, `load_ign_road_vehicle_proxy_policy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_parcels_and_road_application_are_not_mutated`

**Signature**

```python
def test_parcels_and_road_application_are_not_mutated() -> None:
```

**Purpose**

Protects the `parcels and road application are not mutated` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `parcels` from `_parcels(index=[777])`.
- Computes `roads` from `_roads()`.
- Computes `parcels_before` from `deepcopy(parcels)`.
- Computes `roads_before` from `deepcopy(roads)`.
- Computes `result` from `_enrich(parcels=parcels, roads=roads)`.

**Action**

- Calls `_enrich`, `_parcels`, `_roads`, `deepcopy`, `parcels.geometry.to_wkb`, `result.parcels.dtypes.equals`, `result.parcels.geometry.to_wkb`, `result.parcels.geometry.to_wkb().equals`, `result.parcels.index.equals`.

**Expected result**

- Direct assertions: `assert result.parcels.index.equals(parcels.index)`; `assert list(result.parcels.columns) == list(parcels.columns)`; `assert result.parcels.dtypes.equals(parcels.dtypes)`; `assert result.parcels.geometry.to_wkb().equals(parcels.geometry.to_wkb())`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `parcels and road application are not mutated` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `_parcels`, `_roads`, `assert_geodataframe_equal`, `deepcopy`, `list`, `parcels.geometry.to_wkb`, `result.parcels.dtypes.equals`, `result.parcels.geometry.to_wkb`, `result.parcels.geometry.to_wkb().equals`, `result.parcels.index.equals`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_produced_distance_is_rejected`

**Signature**

```python
def test_malformed_produced_distance_is_rejected(value: object) -> None:
```

**Purpose**

Protects the `malformed produced distance is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `value`.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `_corrupt_nearest_output`, `float`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `malformed produced distance is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_corrupt_nearest_output`, `float`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_produced_tie_count_is_rejected`

**Signature**

```python
def test_malformed_produced_tie_count_is_rejected(value: object) -> None:
```

**Purpose**

Protects the `malformed produced tie count is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `value`.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `_corrupt_nearest_output`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `malformed produced tie count is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_corrupt_nearest_output`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_result_dataclasses_are_frozen`

**Signature**

```python
def test_result_dataclasses_are_frozen() -> None:
```

**Purpose**

Protects the `result dataclasses are frozen` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `result` from `_enrich()`.
- Computes `coverage` from `result.class_coverage[0]`.
- Enters managed context(s) `pytest.raises(FrozenInstanceError)` and executes: Computes `result.parcels` from `_parcels()`.
- Enters managed context(s) `pytest.raises(FrozenInstanceError)` and executes: Computes `coverage.feature_count` from `99`.

**Action**

- Calls `_enrich`, `_parcels`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(FrozenInstanceError): result.parcels = _parcels()`; `with pytest.raises(FrozenInstanceError): coverage.feature_count = 99`.

**Regression protected**

- Protects the exact `result dataclasses are frozen` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `_parcels`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_no_business_decision_columns_or_implementation_exist`

**Signature**

```python
def test_no_business_decision_columns_or_implementation_exist() -> None:
```

**Purpose**

Protects the `no business decision columns or implementation exist` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `result` from `_enrich()`.
- Computes `forbidden` from `{'access_score', 'bess_score', 'accessible', 'legal_access', 'parcel_status', 'retained', 'rejected'}`.
- Computes `source` from `Path('src/landscout/stages/enrich_road_proximity.py').read_text(encoding='utf-8')`.

**Action**

- Calls `Path`, `Path('src/landscout/stages/enrich_road_proximity.py').read_text`, `_enrich`, `forbidden.isdisjoint`.

**Expected result**

- Direct assertions: `assert forbidden.isdisjoint(result.parcels.columns)`; `assert forbidden.isdisjoint(result.class_proximity.columns)`; `assert '.iterrows(' not in source`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `no business decision columns or implementation exist` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Path`, `Path('src/landscout/stages/enrich_road_proximity.py').read_text`, `_enrich`, `forbidden.isdisjoint`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_result_parcel_frame_is_an_independent_copy`

**Signature**

```python
def test_result_parcel_frame_is_an_independent_copy() -> None:
```

**Purpose**

Protects the `result parcel frame is an independent copy` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `parcels` from `_parcels()`.
- Computes `result` from `_enrich(parcels=parcels)`.
- Computes `result.parcels.loc[result.parcels.index[0], 'source_value']` from `999`.

**Action**

- Calls `_enrich`, `_parcels`.

**Expected result**

- Direct assertions: `assert parcels.iloc[0].source_value == 0`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `result parcel frame is an independent copy` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `_parcels`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_class_proximity_is_plain_dataframe`

**Signature**

```python
def test_class_proximity_is_plain_dataframe() -> None:
```

**Purpose**

Protects the `class proximity is plain dataframe` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `result` from `_enrich()`.

**Action**

- Calls `_enrich`, `isinstance`, `type`.

**Expected result**

- Direct assertions: `assert type(result.class_proximity) is pd.DataFrame`; `assert not isinstance(result.class_proximity, gpd.GeoDataFrame)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `class proximity is plain dataframe` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `isinstance`, `type`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_selected_rows_belong_to_requested_class`

**Signature**

```python
def test_selected_rows_belong_to_requested_class() -> None:
```

**Purpose**

Protects the `selected rows belong to requested class` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `result` from `_enrich()`.
- Computes `road_classes` from `_roads().set_index('road_feature_id')['road_proxy_class']`.
- Computes `selected` from `result.class_proximity.dropna(subset=['nearest_road_feature_id'])`.

**Action**

- Calls `_enrich`, `_roads`, `_roads().set_index`, `all`, `result.class_proximity.dropna`, `selected.itertuples`.

**Expected result**

- Direct assertions: `assert all((road_classes.loc[row.nearest_road_feature_id] == row.road_proxy_class for row in selected.itertuples(index=False)))`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `selected rows belong to requested class` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `_roads`, `_roads().set_index`, `all`, `result.class_proximity.dropna`, `selected.itertuples`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_policy_sha_mismatch_does_not_construct_spatial_index`

**Signature**

```python
def test_policy_sha_mismatch_does_not_construct_spatial_index() -> None:
```

**Purpose**

Protects the `policy sha mismatch does not construct spatial index` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `roads` from `_roads()`.
- Computes `roads['road_proxy_policy_config_sha256']` from `'b' * 64`.
- Enters managed context(s) `patch('landscout.stages.enrich_road_proximity.STRtree'), pytest.raises(RoadProximityError)` and executes: Calls `_enrich(roads=roads)` for its validation or side effect.

**Action**

- Calls `_enrich`, `_roads`, `spatial_index.assert_not_called`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with patch('landscout.stages.enrich_road_proximity.STRtree') as spatial_index, pytest.raises(RoadProximityError): _enrich(roads=roads)`.

**Regression protected**

- Protects the exact `policy sha mismatch does not construct spatial index` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `_roads`, `patch`, `pytest.raises`, `spatial_index.assert_not_called`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_matched_output_dtypes_are_stable`

**Signature**

```python
def test_matched_output_dtypes_are_stable() -> None:
```

**Purpose**

Protects the `matched output dtypes are stable` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_enrich()`.
- Computes `table` from `result.class_proximity`.

**Action**

- Calls `_enrich`.

**Expected result**

- Direct assertions: `assert str(table.nearest_road_proxy_distance_m.dtype) == 'float64'`; `assert str(table.nearest_road_tie_count.dtype) == 'Int64'`; `assert str(table.nearest_road_toll_evidence.dtype) == 'boolean'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `matched output dtypes are stable` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `str`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_parcel_preservation_uses_exact_non_geometry_values`

**Signature**

```python
def test_parcel_preservation_uses_exact_non_geometry_values() -> None:
```

**Purpose**

Protects the `parcel preservation uses exact non geometry values` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `parcels` from `_parcels()`.
- Computes `result` from `_enrich(parcels=parcels)`.

**Action**

- Calls `_enrich`, `_parcels`, `parcels.drop`, `pd.DataFrame`, `result.parcels.drop`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `parcel preservation uses exact non geometry values` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_enrich`, `_parcels`, `assert_frame_equal`, `parcels.drop`, `pd.DataFrame`, `result.parcels.drop`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `NOT_DISTANCE_PROXY` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `UNKNOWN_REVIEW` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `columns` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `distance_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `geometry` | Logical dtype: GeoPandas active geometry dtype. Nullability: nullable only where the source-stage geometry-status contract explicitly preserves nulls. | source or preserved spatial geometry; never itself a suitability or legal conclusion. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
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
| `other_geometry` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `road_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_class` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_policy_config_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `source_value` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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

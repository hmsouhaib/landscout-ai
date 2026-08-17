# `tests/unit/test_enrich_grid_proximity.py`

## File identity

- Repository path: `tests/unit/test_enrich_grid_proximity.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `enrich_grid_proximity` contracts exercised in this file.
- Source SHA256: `14a73d80cd809bf5cc15d7150d7181eab62247772aa8614621b14f48e81ce189`

## 1. Purpose

Provides complete unit and regression coverage for the `enrich_grid_proximity` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import json`
- `from copy import deepcopy`
- `from dataclasses import replace`
- `from hashlib import sha256`
- `from pathlib import Path`
- `from typing import Any, cast`
- `from unittest.mock import patch`

### Third-party packages

- `import geopandas as gpd`
- `import numpy as np`
- `import pandas as pd`
- `import pyogrio`
- `import pytest`
- `from geopandas.testing import assert_geodataframe_equal`
- `from pandas.api.types import is_float_dtype, is_integer_dtype`
- `from shapely.geometry import (
    GeometryCollection,
    LineString,
    MultiLineString,
    MultiPolygon,
    Point,
    Polygon,
)`

### Internal LandScout imports

- `from landscout import stages`
- `from landscout.sources import (
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    load_ign_bdtopo_source_config,
)`
- `from landscout.stages import (
    GridProximityError,
    GridProximityResult,
    VoltageLevelCoverage,
    profile_grid_proximity,
)`
- `from landscout.stages import (
    enrich_parcel_grid_proximity as public_enrich_parcel_grid_proximity,
)`
- `from landscout.stages.enrich_grid_proximity import (
    VOLTAGE_PROXIMITY_COLUMNS,
)`
- `from landscout.stages.enrich_grid_proximity import (
    _enrich_parcel_grid_proximity_from_normalized as enrich_parcel_grid_proximity,
)`
- `from landscout.stages.normalize_grid_ign import NormalizedIgnElectricityData`

## 4. Contract taxonomy

### A. Python constants

#### `OVERFLOWING_INTEGER`

```python
OVERFLOWING_INTEGER = 10**10000
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_required_match_tie_count` (value argument/reference), `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_long_table_tie_count` (value argument/reference), `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_invalid_voltage_coverage_level` (value argument/reference), `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_long_table_distance` (value argument/reference).

#### `SOURCE_CONFIG`

```python
SOURCE_CONFIG = load_ign_bdtopo_source_config()
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_apply_road_vehicle_proxy_policy.py::_apply` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_wrong_source_type_has_controlled_error` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_malformed_policy_path_has_controlled_error` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_complete_normalization_is_invoked_exactly_once` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_normalization_failure_stops_policy_loading` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_object_is_not_mutated` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_valid_geometry_status_with_unsupported_geometry_is_not_repaired` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_policy_path_must_be_path_or_none` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_public_coverage_proximity_failure_stops_coverage_loading` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_caller_provided_proximity_and_coverage_are_not_public_inputs` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_polygonal_coverage_geometry_is_accepted` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_invalid_coverage_geometry_is_rejected` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_strict_geometric_boundary_proof` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_outside_crossing_or_touching_parcel_is_conservative` (value argument/reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

### `_geometry_status`

**Exact signature**

```python
def _geometry_status(geometry: object) -> str:
```

**Purpose**

Private `test` helper for geometry status; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
'VALID'

'NULL'

'EMPTY'

'INVALID'
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

- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_normalize_road_frame` via `_geometry_status`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_electric_lines` via `_geometry_status`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_transformation_posts` via `_geometry_status`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::_lines` via `_geometry_status`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::_posts` via `_geometry_status`.

**Complete source-ordered implementation**

```python
def _geometry_status(geometry: object) -> str:
    if geometry is None:
        return "NULL"
    if geometry.is_empty:
        return "EMPTY"
    if not geometry.is_valid:
        return "INVALID"
    return "VALID"
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_parcels`

**Exact signature**

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

Private `test` helper for parcels; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
gpd.GeoDataFrame({'parcel_id': ids, 'source_value': list(range(count))}, geometry=values, crs=crs, index=source_index)
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

- direct call or construction: `tests/unit/test_assess_grid_coverage.py::_proximity` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_public_coverage_proximity_failure_stops_coverage_loading` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_geographic_parcel_storage_crs_and_geometry_are_preserved` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_public_assessment_loads_coverage_from_the_physical_source` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::_proximity` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::_assess` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_wrong_public_input_type_is_controlled_and_fast` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_source_chain_calls_proximity_then_coverage_exactly_once` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_proximity_failure_stops_coverage_loading` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_loader_failure_is_controlled` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_malformed_upstream_result_fails_before_coverage_load` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_spatial_role_and_source_type_are_controlled` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_full_parcel_coverage_position_is_conservative` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_position_uses_full_geometry_not_centroid` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_strict_boundary_status_logic` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_matched_outside_or_crossing_status` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_no_match_takes_precedence_over_coverage_position` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_classes_are_diagnosed_independently` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_result_preserves_every_upstream_fact_and_input_object` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::_corrupt_generated` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_inconsistent_generated_status_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_result_is_frozen_and_has_no_business_decision_fields` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::_two_parcel_two_voltage_result` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_normalizes_verified_source_exactly_once` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_rejects_wrong_source_boundary_types` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_caller_crafted_normalized_grid_frame_is_not_a_public_source` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_reproduces_configured_electricity_roles` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_rejects_archive_lineage_differing_from_config` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_source_normalization_failure_stops_grid_computation` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_separated_distance_uses_parcel_edge_not_centroid` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_touching_line_has_zero_distance` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_post_distance_uses_parcel_and_post_polygons` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_epsg4326_input_is_calculated_in_lambert93_and_preserved` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_epsg2154_parcel_input_remains_epsg2154` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_valid_parcel_id_is_preserved_exactly` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_invalid_parcel_id_hygiene_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_supported_parcel_polygon_geometry_is_preserved` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_semantically_wrong_parcel_geometry_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_missing_crs_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_wrong_grid_crs_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_z_line_has_same_horizontal_distance_as_xy_line` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_line_tie_is_counted_and_lexical_feature_id_wins` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_cross_voltage_tie_uses_lexical_global_feature_id` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_nonvalid_grid_geometries_are_excluded_without_row_loss` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_wrong_grid_feature_type_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_duplicate_grid_feature_id_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_wrong_spatial_role_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_unsupported_valid_grid_geometry_type_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_supported_multi_geometries_are_accepted` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_nearest_any_line_preserves_every_voltage_status` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_nearest_exact_and_voltage_table_exclude_nonexact_lines` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_invalid_exact_voltage_values_are_not_used_as_exact` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_missing_parcel_column_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_null_parcel_id_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_duplicate_parcel_id_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_bad_parcel_geometry_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_distance_profile_is_threshold_free_and_tracks_ties` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_allows_consistent_missing_manager_and_asset_status` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_nonnull_exact_field_without_exact_coverage` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_no_valid_required_grid_feature_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_run` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_epsg4326_parcels_are_measured_in_lambert93_but_preserved` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_invalid_parcel_ids_are_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_duplicate_parcel_ids_are_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_missing_crs_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_mutated_source_summary_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_source_summary_counts_are_strict_integers` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_reserved_output_column_collision_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_inputs_and_all_existing_parcel_fields_are_preserved` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_relations_are_unique_deterministic_and_summaries_agree` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_result_frames_are_independent_from_mutable_inputs` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_contract_result` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_source_complete_contract` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_two_parcel_source_complete_contract` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_reordered_physical_gpkg_rows` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_shapefile_source_complete_contract` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_shapefile_ogr_fid_source_complete_contract` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::_run` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_one_parcel_fully_inside_one_zone` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_parcel_split_across_two_zones` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_dominant_zone_tie_is_deterministic` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_touch_only_relation_is_preserved_but_never_dominant` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_parcel_with_no_positive_area_zone_is_preserved` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_parcel_with_no_intersecting_zone_has_zero_coverage` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_overlapping_source_zones_expose_raw_sum_union_and_excess` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_polygon_and_multipolygon_parcels_are_supported` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_polygon_and_multipolygon_zones_are_supported` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_missing_or_unusable_crs_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_invalid_or_non_polygonal_parcel_geometry_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_invalid_or_non_polygonal_zone_geometry_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_invalid_parcel_id_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_duplicate_parcel_id_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_missing_parcel_id_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_geometry_must_be_the_active_parcel_geometry_column` via `_parcels`.

**Complete source-ordered implementation**

```python
def _parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
    values = geometries or [
        Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])
    ]
    count = len(values)
    ids = identifiers or [f"PARCEL-{position + 1}" for position in range(count)]
    source_index = index or [100 + position for position in range(count)]
    return gpd.GeoDataFrame(
        {"parcel_id": ids, "source_value": list(range(count))},
        geometry=values,
        crs=crs,
        index=source_index,
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_lines`

**Exact signature**

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

Private `test` helper for lines; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
gpd.GeoDataFrame({'grid_feature_id': ids, 'grid_feature_type': feature_types or ['ELECTRIC_LINE'] * count, 'source_feature_id': [f'SOURCE-{value}' for value in ids], 'source_department_code': ['31'] * count, 'source_edition': ['2026-06-15'] * count, 'source_archive_sha256': ['a' * 64] * count, 'source_layer': ['CUSTOM_LINE_LAYER'] * count, 'spatial_role': spatial_roles or ['PROXY_GEOMETRY'] * count, 'geometry_status': geometry_statuses, 'voltage_raw': [f'{value:g} kV' if isinstance(value, (int, float)) else None for value in normalized_voltages], 'voltage_status': normalized_voltage_statuses, 'voltage_kv': normalized_voltages, 'voltage_upper_bound_kv': [np.nan] * count, 'manager_name': ['TEST MANAGER'] * count, 'asset_status_raw': ['En service'] * count}, geometry=values, crs=crs)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `_geometry_status`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_assess_grid_coverage.py::_electricity_source` via `_lines`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::_proximity` via `_lines`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_geographic_parcel_storage_crs_and_geometry_are_preserved` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::_electricity_source` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::_two_parcel_two_voltage_result` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_normalizes_verified_source_exactly_once` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_caller_crafted_normalized_grid_frame_is_not_a_public_source` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_separated_distance_uses_parcel_edge_not_centroid` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_touching_line_has_zero_distance` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_post_distance_uses_parcel_and_post_polygons` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_epsg4326_input_is_calculated_in_lambert93_and_preserved` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_epsg2154_parcel_input_remains_epsg2154` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_valid_parcel_id_is_preserved_exactly` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_invalid_parcel_id_hygiene_is_rejected` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_supported_parcel_polygon_geometry_is_preserved` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_semantically_wrong_parcel_geometry_is_rejected` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_missing_crs_is_rejected` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_wrong_grid_crs_is_rejected` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_z_line_has_same_horizontal_distance_as_xy_line` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_line_tie_is_counted_and_lexical_feature_id_wins` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_cross_voltage_tie_uses_lexical_global_feature_id` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_nonvalid_grid_geometries_are_excluded_without_row_loss` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_wrong_grid_feature_type_is_rejected` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_duplicate_grid_feature_id_is_rejected` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_wrong_spatial_role_is_rejected` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_unsupported_valid_grid_geometry_type_is_rejected` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_supported_multi_geometries_are_accepted` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_nearest_any_line_preserves_every_voltage_status` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_nearest_exact_and_voltage_table_exclude_nonexact_lines` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_invalid_exact_voltage_values_are_not_used_as_exact` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_missing_parcel_column_is_rejected` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_null_parcel_id_is_rejected` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_duplicate_parcel_id_is_rejected` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_bad_parcel_geometry_is_rejected` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_distance_profile_is_threshold_free_and_tracks_ties` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_allows_consistent_missing_manager_and_asset_status` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_nonnull_exact_field_without_exact_coverage` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_no_valid_required_grid_feature_is_rejected` via `_lines`.

**Complete source-ordered implementation**

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
    values = geometries or [LineString([(110, -20), (110, 30)])]
    count = len(values)
    ids = identifiers or [f"LINE-{position + 1}" for position in range(count)]
    geometry_statuses = statuses or [_geometry_status(value) for value in values]
    normalized_voltage_statuses = voltage_statuses or ["EXACT"] * count
    normalized_voltages = voltages or [110.0] * count
    return gpd.GeoDataFrame(
        {
            "grid_feature_id": ids,
            "grid_feature_type": feature_types or ["ELECTRIC_LINE"] * count,
            "source_feature_id": [f"SOURCE-{value}" for value in ids],
            "source_department_code": ["31"] * count,
            "source_edition": ["2026-06-15"] * count,
            "source_archive_sha256": ["a" * 64] * count,
            "source_layer": ["CUSTOM_LINE_LAYER"] * count,
            "spatial_role": spatial_roles or ["PROXY_GEOMETRY"] * count,
            "geometry_status": geometry_statuses,
            "voltage_raw": [
                f"{value:g} kV" if isinstance(value, (int, float)) else None
                for value in normalized_voltages
            ],
            "voltage_status": normalized_voltage_statuses,
            "voltage_kv": normalized_voltages,
            "voltage_upper_bound_kv": [np.nan] * count,
            "manager_name": ["TEST MANAGER"] * count,
            "asset_status_raw": ["En service"] * count,
        },
        geometry=values,
        crs=crs,
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_posts`

**Exact signature**

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

Private `test` helper for posts; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
gpd.GeoDataFrame({'grid_feature_id': ids, 'grid_feature_type': feature_types or ['TRANSFORMATION_POST'] * count, 'source_feature_id': [f'SOURCE-{value}' for value in ids], 'source_department_code': ['31'] * count, 'source_edition': ['2026-06-15'] * count, 'source_archive_sha256': ['a' * 64] * count, 'source_layer': ['CUSTOM_POST_LAYER'] * count, 'spatial_role': spatial_roles or ['PROXY_GEOMETRY'] * count, 'geometry_status': geometry_statuses, 'name': ['Test post'] * count, 'importance_raw': ['5'] * count, 'asset_status_raw': ['En service'] * count}, geometry=values, crs=crs)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `_geometry_status`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_assess_grid_coverage.py::_electricity_source` via `_posts`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::_proximity` via `_posts`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_geographic_parcel_storage_crs_and_geometry_are_preserved` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::_electricity_source` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::_two_parcel_two_voltage_result` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_normalizes_verified_source_exactly_once` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_separated_distance_uses_parcel_edge_not_centroid` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_touching_line_has_zero_distance` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_post_distance_uses_parcel_and_post_polygons` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_epsg4326_input_is_calculated_in_lambert93_and_preserved` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_epsg2154_parcel_input_remains_epsg2154` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_valid_parcel_id_is_preserved_exactly` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_invalid_parcel_id_hygiene_is_rejected` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_supported_parcel_polygon_geometry_is_preserved` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_semantically_wrong_parcel_geometry_is_rejected` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_missing_crs_is_rejected` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_wrong_grid_crs_is_rejected` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_z_line_has_same_horizontal_distance_as_xy_line` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_line_tie_is_counted_and_lexical_feature_id_wins` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_cross_voltage_tie_uses_lexical_global_feature_id` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_nonvalid_grid_geometries_are_excluded_without_row_loss` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_wrong_grid_feature_type_is_rejected` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_duplicate_grid_feature_id_is_rejected` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_wrong_spatial_role_is_rejected` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_unsupported_valid_grid_geometry_type_is_rejected` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_supported_multi_geometries_are_accepted` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_nearest_any_line_preserves_every_voltage_status` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_nearest_exact_and_voltage_table_exclude_nonexact_lines` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_invalid_exact_voltage_values_are_not_used_as_exact` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_missing_parcel_column_is_rejected` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_null_parcel_id_is_rejected` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_duplicate_parcel_id_is_rejected` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_bad_parcel_geometry_is_rejected` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_distance_profile_is_threshold_free_and_tracks_ties` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_allows_consistent_missing_manager_and_asset_status` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_nonnull_exact_field_without_exact_coverage` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_no_valid_required_grid_feature_is_rejected` via `_posts`.

**Complete source-ordered implementation**

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
    values = geometries or [
        Polygon([(110, 0), (110, 10), (120, 10), (120, 0), (110, 0)])
    ]
    count = len(values)
    ids = identifiers or [f"POST-{position + 1}" for position in range(count)]
    geometry_statuses = statuses or [_geometry_status(value) for value in values]
    return gpd.GeoDataFrame(
        {
            "grid_feature_id": ids,
            "grid_feature_type": feature_types or ["TRANSFORMATION_POST"] * count,
            "source_feature_id": [f"SOURCE-{value}" for value in ids],
            "source_department_code": ["31"] * count,
            "source_edition": ["2026-06-15"] * count,
            "source_archive_sha256": ["a" * 64] * count,
            "source_layer": ["CUSTOM_POST_LAYER"] * count,
            "spatial_role": spatial_roles or ["PROXY_GEOMETRY"] * count,
            "geometry_status": geometry_statuses,
            "name": ["Test post"] * count,
            "importance_raw": ["5"] * count,
            "asset_status_raw": ["En service"] * count,
        },
        geometry=values,
        crs=crs,
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_electricity_source`

**Exact signature**

```python
def _electricity_source(
    lines: gpd.GeoDataFrame | None = None,
    posts: gpd.GeoDataFrame | None = None,
) -> IgnBdTopoElectricityData:
```

**Purpose**

Private `test` helper for electricity source; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `IgnBdTopoElectricityData`.
- Every observed return expression is reproduced without truncation:
```python
IgnBdTopoElectricityData(extraction=cast(Any, None), electric_lines=lines if lines is not None else _lines(), transformation_posts=posts if posts is not None else _posts(), electric_lines_summary=cast(Any, None), transformation_posts_summary=cast(Any, None))
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

- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once` via `_electricity_source`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_public_coverage_proximity_failure_stops_coverage_loading` via `_electricity_source`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_public_assessment_loads_coverage_from_the_physical_source` via `_electricity_source`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_normalizes_verified_source_exactly_once` via `_electricity_source`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_rejects_wrong_source_boundary_types` via `_electricity_source`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_source_normalization_failure_stops_grid_computation` via `_electricity_source`.

**Complete source-ordered implementation**

```python
def _electricity_source(
    lines: gpd.GeoDataFrame | None = None,
    posts: gpd.GeoDataFrame | None = None,
) -> IgnBdTopoElectricityData:
    return IgnBdTopoElectricityData(
        extraction=cast(Any, None),
        electric_lines=lines if lines is not None else _lines(),
        transformation_posts=posts if posts is not None else _posts(),
        electric_lines_summary=cast(Any, None),
        transformation_posts_summary=cast(Any, None),
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_physical_line_source`

**Exact signature**

```python
def _physical_line_source(
    identifier: str,
    geometry: LineString,
) -> gpd.GeoDataFrame:
```

**Purpose**

Private `test` helper for physical line source; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
gpd.GeoDataFrame({'cleabs': [identifier], 'voltage': ['225 kV'], 'gestionnaire': ['Test manager'], 'siren_gestionnaire': ['444619258'], 'etat_de_l_objet': ['En service'], 'sources': ['Synthetic physical source'], 'identifiants_sources': [f'SOURCE-{identifier}'], 'date_creation': pd.to_datetime(['2024-01-01']), 'date_modification': pd.to_datetime(['2025-01-01']), 'date_de_confirmation': pd.to_datetime(['2025-02-01']), 'methode_d_acquisition_planimetrique': ['Synthetic'], 'precision_planimetrique': [1.0]}, geometry=[geometry], crs='EPSG:2154')
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

- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::_physical_electricity_source` via `_physical_line_source`.

**Complete source-ordered implementation**

```python
def _physical_line_source(
    identifier: str,
    geometry: LineString,
) -> gpd.GeoDataFrame:
    return gpd.GeoDataFrame(
        {
            "cleabs": [identifier],
            "voltage": ["225 kV"],
            "gestionnaire": ["Test manager"],
            "siren_gestionnaire": ["444619258"],
            "etat_de_l_objet": ["En service"],
            "sources": ["Synthetic physical source"],
            "identifiants_sources": [f"SOURCE-{identifier}"],
            "date_creation": pd.to_datetime(["2024-01-01"]),
            "date_modification": pd.to_datetime(["2025-01-01"]),
            "date_de_confirmation": pd.to_datetime(["2025-02-01"]),
            "methode_d_acquisition_planimetrique": ["Synthetic"],
            "precision_planimetrique": [1.0],
        },
        geometry=[geometry],
        crs="EPSG:2154",
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_physical_post_source`

**Exact signature**

```python
def _physical_post_source(
    identifier: str,
    geometry: Polygon,
) -> gpd.GeoDataFrame:
```

**Purpose**

Private `test` helper for physical post source; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
gpd.GeoDataFrame({'cleabs': [identifier], 'toponyme': ['Test post'], 'statut_du_toponyme': ['Valid'], 'importance': ['5'], 'etat_de_l_objet': ['En service'], 'sources': ['Synthetic physical source'], 'identifiants_sources': [f'SOURCE-{identifier}'], 'date_creation': pd.to_datetime(['2024-01-01']), 'date_modification': pd.to_datetime(['2025-01-01']), 'date_de_confirmation': pd.to_datetime(['2025-02-01']), 'methode_d_acquisition_planimetrique': ['Synthetic'], 'precision_planimetrique': [1.0]}, geometry=[geometry], crs='EPSG:2154')
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

- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::_physical_electricity_source` via `_physical_post_source`.

**Complete source-ordered implementation**

```python
def _physical_post_source(
    identifier: str,
    geometry: Polygon,
) -> gpd.GeoDataFrame:
    return gpd.GeoDataFrame(
        {
            "cleabs": [identifier],
            "toponyme": ["Test post"],
            "statut_du_toponyme": ["Valid"],
            "importance": ["5"],
            "etat_de_l_objet": ["En service"],
            "sources": ["Synthetic physical source"],
            "identifiants_sources": [f"SOURCE-{identifier}"],
            "date_creation": pd.to_datetime(["2024-01-01"]),
            "date_modification": pd.to_datetime(["2025-01-01"]),
            "date_de_confirmation": pd.to_datetime(["2025-02-01"]),
            "methode_d_acquisition_planimetrique": ["Synthetic"],
            "precision_planimetrique": [1.0],
        },
        geometry=[geometry],
        crs="EPSG:2154",
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_physical_summary`

**Exact signature**

```python
def _physical_summary(
    frame: gpd.GeoDataFrame,
    *,
    logical_name: str,
    layer_name: str,
) -> IgnBdTopoLayerSummary:
```

**Purpose**

Private `test` helper for physical summary; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `IgnBdTopoLayerSummary`.
- Every observed return expression is reproduced without truncation:
```python
IgnBdTopoLayerSummary(logical_name=cast(Any, logical_name), source_layer_name=layer_name, crs=str(frame.crs), feature_count=len(frame), columns=tuple((str(column) for column in frame.columns)), dtypes=tuple(((str(column), str(dtype)) for column, dtype in frame.dtypes.items())), null_geometry_count=int(null_mask.sum()), empty_geometry_count=int(empty_mask.sum()), invalid_geometry_count=int(invalid_mask.sum()), geometry_types=tuple(sorted((str(value) for value in geometry[~null_mask].geom_type.dropna().unique()))))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `geometry.isna`, `geometry[~null_mask].geom_type.dropna`, `geometry[~null_mask].geom_type.dropna().unique`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::_physical_electricity_source` via `_physical_summary`.

**Complete source-ordered implementation**

```python
def _physical_summary(
    frame: gpd.GeoDataFrame,
    *,
    logical_name: str,
    layer_name: str,
) -> IgnBdTopoLayerSummary:
    geometry = frame.geometry
    null_mask = geometry.isna()
    empty_mask = ~null_mask & geometry.is_empty
    invalid_mask = ~null_mask & ~geometry.is_empty & ~geometry.is_valid
    return IgnBdTopoLayerSummary(
        logical_name=cast(Any, logical_name),
        source_layer_name=layer_name,
        crs=str(frame.crs),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
        null_geometry_count=int(null_mask.sum()),
        empty_geometry_count=int(empty_mask.sum()),
        invalid_geometry_count=int(invalid_mask.sum()),
        geometry_types=tuple(
            sorted(
                str(value)
                for value in geometry[~null_mask].geom_type.dropna().unique()
            )
        ),
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_physical_electricity_source`

**Exact signature**

```python
def _physical_electricity_source(
    tmp_path: Path,
    *,
    alternate_roles: bool,
) -> IgnBdTopoElectricityData:
```

**Purpose**

Private `test` helper for physical electricity source; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `IgnBdTopoElectricityData`.
- Every observed return expression is reproduced without truncation:
```python
IgnBdTopoElectricityData(extraction=extraction, electric_lines=selected_lines, transformation_posts=selected_posts, electric_lines_summary=_physical_summary(selected_lines, logical_name='electric_lines', layer_name=selected_line_layer), transformation_posts_summary=_physical_summary(selected_posts, logical_name='transformation_posts', layer_name=selected_post_layer))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: `IgnBdTopoDownload`.
- Filesystem read: `geopackage_path.read_bytes`, `gpd.read_file`.
- Filesystem write: `(extraction_path / '.landscout-extraction.json').write_text`, `extraction_path.mkdir`.
- CRS/geometry calculation: none directly visible.
- Hashing: `sha256`, `sha256(payload).hexdigest`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::_alternate_role_electricity_source` via `_physical_electricity_source`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::_configured_role_electricity_source` via `_physical_electricity_source`.

**Complete source-ordered implementation**

```python
def _physical_electricity_source(
    tmp_path: Path,
    *,
    alternate_roles: bool,
) -> IgnBdTopoElectricityData:
    configured_line_layer = "LIGNE_ELECTRIQUE_CONFIGURED"
    configured_post_layer = "POSTE_DE_TRANSFORMATION_CONFIGURED"
    alternate_line_layer = "CABLE_SOURCE_ALTERNATE"
    alternate_post_layer = "INSTALLATION_SOURCE_ALTERNATE"
    frames = (
        (
            configured_line_layer,
            _physical_line_source(
                "CONFIGURED-LINE",
                LineString([(500, -20), (500, 30)]),
            ),
        ),
        (
            configured_post_layer,
            _physical_post_source(
                "CONFIGURED-POST",
                Polygon(
                    [(500, 0), (500, 10), (510, 10), (510, 0), (500, 0)]
                ),
            ),
        ),
        (
            alternate_line_layer,
            _physical_line_source(
                "ALTERNATE-LINE",
                LineString([(10, -20), (10, 30)]),
            ),
        ),
        (
            alternate_post_layer,
            _physical_post_source(
                "ALTERNATE-POST",
                Polygon([(10, 0), (10, 10), (20, 10), (20, 0), (10, 0)]),
            ),
        ),
    )
    selected_line_layer = (
        alternate_line_layer if alternate_roles else configured_line_layer
    )
    selected_post_layer = (
        alternate_post_layer if alternate_roles else configured_post_layer
    )
    extraction_path = tmp_path / (
        "alternate-electricity-extraction"
        if alternate_roles
        else "configured-electricity-extraction"
    )
    extraction_path.mkdir()
    geopackage_path = extraction_path / "electricity.gpkg"
    for position, (layer_name, frame) in enumerate(frames):
        pyogrio.write_dataframe(
            frame,
            geopackage_path,
            layer=layer_name,
            driver="GPKG",
            append=position > 0,
        )
    selected_lines = gpd.read_file(
        geopackage_path,
        layer=selected_line_layer,
        engine="pyogrio",
    )
    selected_posts = gpd.read_file(
        geopackage_path,
        layer=selected_post_layer,
        engine="pyogrio",
    )
    payload = geopackage_path.read_bytes()
    digest = sha256(payload).hexdigest()
    layer_names = tuple(
        str(record[0]) for record in pyogrio.list_layers(geopackage_path)
    )
    marker = {
        "schema_version": 2,
        "archive_sha256": "a" * 64,
        "geopackage_relative_path": geopackage_path.name,
        "geopackage_size_bytes": len(payload),
        "geopackage_sha256": digest,
        "all_layer_names": list(layer_names),
        "electric_lines_layer": selected_line_layer,
        "transformation_posts_layer": selected_post_layer,
        "spatial_role": "PROXY_GEOMETRY",
    }
    (extraction_path / ".landscout-extraction.json").write_text(
        json.dumps(marker),
        encoding="utf-8",
    )
    archive = IgnBdTopoDownload(
        provider=SOURCE_CONFIG.provider,
        product=SOURCE_CONFIG.product,
        department_code=SOURCE_CONFIG.department_code,
        edition=SOURCE_CONFIG.edition,
        product_version=SOURCE_CONFIG.product_version,
        projection=SOURCE_CONFIG.projection,
        package_format=SOURCE_CONFIG.format,
        archive_format=SOURCE_CONFIG.archive_format,
        source_url=str(SOURCE_CONFIG.source_url),
        checksum_url=(
            str(SOURCE_CONFIG.checksum_url)
            if SOURCE_CONFIG.checksum_url is not None
            else None
        ),
        download_timestamp="2026-08-11T15:32:03+00:00",
        filename=Path(str(SOURCE_CONFIG.source_url)).name,
        file_size=SOURCE_CONFIG.expected_archive_size_bytes or 1,
        sha256="a" * 64,
        official_checksum_algorithm=SOURCE_CONFIG.official_checksum_algorithm,
        official_checksum=SOURCE_CONFIG.official_checksum,
        official_checksum_validated=(
            SOURCE_CONFIG.official_checksum is not None
        ),
        path=tmp_path / "synthetic.7z",
        cache_hit=True,
    )
    extraction = IgnBdTopoExtraction(
        archive=archive,
        extraction_path=extraction_path,
        geopackage_path=geopackage_path,
        geopackage_filename=geopackage_path.name,
        geopackage_size_bytes=len(payload),
        geopackage_sha256=digest,
        all_layer_names=layer_names,
        electric_lines_layer=selected_line_layer,
        transformation_posts_layer=selected_post_layer,
        cache_hit=True,
    )
    return IgnBdTopoElectricityData(
        extraction=extraction,
        electric_lines=selected_lines,
        transformation_posts=selected_posts,
        electric_lines_summary=_physical_summary(
            selected_lines,
            logical_name="electric_lines",
            layer_name=selected_line_layer,
        ),
        transformation_posts_summary=_physical_summary(
            selected_posts,
            logical_name="transformation_posts",
            layer_name=selected_post_layer,
        ),
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_alternate_role_electricity_source`

**Exact signature**

```python
def _alternate_role_electricity_source(
    tmp_path: Path,
) -> IgnBdTopoElectricityData:
```

**Purpose**

Private `test` helper for alternate role electricity source; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `IgnBdTopoElectricityData`.
- Every observed return expression is reproduced without truncation:
```python
_physical_electricity_source(tmp_path, alternate_roles=True)
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

- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_reproduces_configured_electricity_roles` via `_alternate_role_electricity_source`.

**Complete source-ordered implementation**

```python
def _alternate_role_electricity_source(
    tmp_path: Path,
) -> IgnBdTopoElectricityData:
    return _physical_electricity_source(tmp_path, alternate_roles=True)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_configured_role_electricity_source`

**Exact signature**

```python
def _configured_role_electricity_source(
    tmp_path: Path,
) -> IgnBdTopoElectricityData:
```

**Purpose**

Private `test` helper for configured role electricity source; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `IgnBdTopoElectricityData`.
- Every observed return expression is reproduced without truncation:
```python
_physical_electricity_source(tmp_path, alternate_roles=False)
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

- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_rejects_archive_lineage_differing_from_config` via `_configured_role_electricity_source`.

**Complete source-ordered implementation**

```python
def _configured_role_electricity_source(
    tmp_path: Path,
) -> IgnBdTopoElectricityData:
    return _physical_electricity_source(tmp_path, alternate_roles=False)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_two_parcel_two_voltage_result`

**Exact signature**

```python
def _two_parcel_two_voltage_result() -> GridProximityResult:
```

**Purpose**

Private `test` helper for two parcel two voltage result; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `GridProximityResult`.
- Every observed return expression is reproduced without truncation:
```python
enrich_parcel_grid_proximity(parcels, lines, _posts())
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

- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_voltage_table_is_exact_ordered_cartesian_product` via `_two_parcel_two_voltage_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_missing_voltage_cartesian_row` via `_two_parcel_two_voltage_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_unknown_voltage_parcel_with_same_total_count` via `_two_parcel_two_voltage_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_duplicate_parcel_voltage_pair` via `_two_parcel_two_voltage_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_voltage_rows_out_of_parcel_order` via `_two_parcel_two_voltage_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_inconsistent_global_exact_distance` via `_two_parcel_two_voltage_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_inconsistent_global_exact_identity` via `_two_parcel_two_voltage_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_inconsistent_global_exact_metadata` via `_two_parcel_two_voltage_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_inconsistent_global_exact_tie_count` via `_two_parcel_two_voltage_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_required_match_tie_count` via `_two_parcel_two_voltage_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_long_table_tie_count` via `_two_parcel_two_voltage_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_missing_main_match_feature_id` via `_two_parcel_two_voltage_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_required_match_distance` via `_two_parcel_two_voltage_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_exact_match_voltage` via `_two_parcel_two_voltage_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_result_parcel_id` via `_two_parcel_two_voltage_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_missing_required_proximity_column` via `_two_parcel_two_voltage_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_nondeterministic_or_duplicate_coverage` via `_two_parcel_two_voltage_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_invalid_voltage_coverage_level` via `_two_parcel_two_voltage_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_invalid_voltage_coverage_feature_count` via `_two_parcel_two_voltage_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_invalid_long_table_voltage` via `_two_parcel_two_voltage_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_missing_long_table_match_lineage` via `_two_parcel_two_voltage_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_long_table_distance` via `_two_parcel_two_voltage_result`.

**Complete source-ordered implementation**

```python
def _two_parcel_two_voltage_result() -> GridProximityResult:
    parcels = _parcels(
        [
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
            Polygon([(40, 0), (40, 10), (50, 10), (50, 0), (40, 0)]),
        ],
        identifiers=["PARCEL-2", "PARCEL-1"],
    )
    lines = _lines(
        [
            LineString([(200, -20), (200, 30)]),
            LineString([(100, -20), (100, 30)]),
        ],
        identifiers=["LINE-275", "LINE-110"],
        voltage_statuses=["EXACT", "EXACT"],
        voltages=[275.0, 110.0],
    )
    return enrich_parcel_grid_proximity(parcels, lines, _posts())
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_mutate_parcel_result`

**Exact signature**

```python
def _mutate_parcel_result(
    result: GridProximityResult,
    column: str,
    value: object,
) -> GridProximityResult:
```

**Purpose**

Private `test` helper for mutate parcel result; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `GridProximityResult`.
- Every observed return expression is reproduced without truncation:
```python
replace(result, parcels=parcels)
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
- In-memory mutation: `parcels.at[0, column]`, `parcels[column]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_inconsistent_global_exact_distance` via `_mutate_parcel_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_inconsistent_global_exact_identity` via `_mutate_parcel_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_inconsistent_global_exact_metadata` via `_mutate_parcel_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_inconsistent_global_exact_tie_count` via `_mutate_parcel_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_required_match_tie_count` via `_mutate_parcel_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_missing_main_match_feature_id` via `_mutate_parcel_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_required_match_distance` via `_mutate_parcel_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_exact_match_voltage` via `_mutate_parcel_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_result_parcel_id` via `_mutate_parcel_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_nonnull_exact_field_without_exact_coverage` via `_mutate_parcel_result`.

**Complete source-ordered implementation**

```python
def _mutate_parcel_result(
    result: GridProximityResult,
    column: str,
    value: object,
) -> GridProximityResult:
    parcels = result.parcels.copy()
    parcels[column] = parcels[column].astype("object")
    parcels.at[0, column] = value
    return replace(result, parcels=parcels)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_mutate_voltage_result`

**Exact signature**

```python
def _mutate_voltage_result(
    result: GridProximityResult,
    column: str,
    value: object,
) -> GridProximityResult:
```

**Purpose**

Private `test` helper for mutate voltage result; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `GridProximityResult`.
- Every observed return expression is reproduced without truncation:
```python
replace(result, voltage_level_proximity=table)
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
- In-memory mutation: `table.at[0, column]`, `table[column]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_unknown_voltage_parcel_with_same_total_count` via `_mutate_voltage_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_long_table_tie_count` via `_mutate_voltage_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_invalid_long_table_voltage` via `_mutate_voltage_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_missing_long_table_match_lineage` via `_mutate_voltage_result`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_long_table_distance` via `_mutate_voltage_result`.

**Complete source-ordered implementation**

```python
def _mutate_voltage_result(
    result: GridProximityResult,
    column: str,
    value: object,
) -> GridProximityResult:
    table = result.voltage_level_proximity.copy()
    table[column] = table[column].astype("object")
    table.at[0, column] = value
    return replace(result, voltage_level_proximity=table)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_clean_high_level_api_is_exported`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
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
assert (
        stages.enrich_parcel_grid_proximity
        is public_enrich_parcel_grid_proximity
    )
assert stages.profile_grid_proximity is profile_grid_proximity
assert "enrich_parcel_grid_proximity" in stages.__all__
assert "profile_grid_proximity" in stages.__all__
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_clean_high_level_api_is_exported() -> None:
    assert (
        stages.enrich_parcel_grid_proximity
        is public_enrich_parcel_grid_proximity
    )
    assert stages.profile_grid_proximity is profile_grid_proximity
    assert "enrich_parcel_grid_proximity" in stages.__all__
    assert "profile_grid_proximity" in stages.__all__
```

### `test_public_proximity_normalizes_verified_source_exactly_once`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels()
lines = _lines()
posts = _posts()
source = _electricity_source(lines, posts)
normalizer.assert_called_once_with(source, SOURCE_CONFIG)
```

**Action**

```python
normalized = NormalizedIgnElectricityData(lines, posts)
with patch(
        "landscout.stages.enrich_grid_proximity.normalize_ign_electricity",
        return_value=normalized,
        create=True,
    ) as normalizer:
        result = public_enrich_parcel_grid_proximity(
            parcels, source, SOURCE_CONFIG
        )
```

**Expected result**

```python
assert result.parcels.loc[0, "nearest_line_grid_feature_id"] == "LINE-1"
assert result.parcels.loc[0, "nearest_post_grid_feature_id"] == "POST-1"
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_public_proximity_normalizes_verified_source_exactly_once() -> None:
    parcels = _parcels()
    lines = _lines()
    posts = _posts()
    source = _electricity_source(lines, posts)
    normalized = NormalizedIgnElectricityData(lines, posts)

    with patch(
        "landscout.stages.enrich_grid_proximity.normalize_ign_electricity",
        return_value=normalized,
        create=True,
    ) as normalizer:
        result = public_enrich_parcel_grid_proximity(
            parcels, source, SOURCE_CONFIG
        )

    normalizer.assert_called_once_with(source, SOURCE_CONFIG)
    assert result.parcels.loc[0, "nearest_line_grid_feature_id"] == "LINE-1"
    assert result.parcels.loc[0, "nearest_post_grid_feature_id"] == "POST-1"
```

### `test_public_proximity_rejects_wrong_source_boundary_types`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `argument`.

**Setup**

```python
kwargs: dict[str, object] = {
        "parcels": _parcels(),
        "electricity_source": _electricity_source(),
        "source_config": SOURCE_CONFIG,
    }
kwargs[argument] = pd.DataFrame() if argument == "parcels" else object()
normalizer.assert_not_called()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with patch(
        "landscout.stages.enrich_grid_proximity.normalize_ign_electricity",
        create=True,
    ) as normalizer, pytest.raises(GridProximityError):
        public_enrich_parcel_grid_proximity(**cast(Any, kwargs))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_public_proximity_rejects_wrong_source_boundary_types(
    argument: str,
) -> None:
    kwargs: dict[str, object] = {
        "parcels": _parcels(),
        "electricity_source": _electricity_source(),
        "source_config": SOURCE_CONFIG,
    }
    kwargs[argument] = pd.DataFrame() if argument == "parcels" else object()

    with patch(
        "landscout.stages.enrich_grid_proximity.normalize_ign_electricity",
        create=True,
    ) as normalizer, pytest.raises(GridProximityError):
        public_enrich_parcel_grid_proximity(**cast(Any, kwargs))

    normalizer.assert_not_called()
```

### `test_caller_crafted_normalized_grid_frame_is_not_a_public_source`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
forged_lines = _lines(
        [LineString([(10, -20), (10, 30)])],
        identifiers=["IGN_BDTOPO:ELECTRIC_LINE:FORGED"],
    )
normalizer.assert_not_called()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert forged_lines["source_department_code"].eq("31").all()
assert forged_lines["source_edition"].eq("2026-06-15").all()
assert forged_lines["source_archive_sha256"].eq("a" * 64).all()
assert forged_lines["spatial_role"].eq("PROXY_GEOMETRY").all()
with patch(
        "landscout.stages.enrich_grid_proximity.normalize_ign_electricity",
        create=True,
    ) as normalizer, pytest.raises(
        GridProximityError,
        match="IgnBdTopoElectricityData|electricity source",
    ):
        public_enrich_parcel_grid_proximity(
            _parcels(),
            cast(Any, forged_lines),
            SOURCE_CONFIG,
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_caller_crafted_normalized_grid_frame_is_not_a_public_source() -> None:
    forged_lines = _lines(
        [LineString([(10, -20), (10, 30)])],
        identifiers=["IGN_BDTOPO:ELECTRIC_LINE:FORGED"],
    )
    assert forged_lines["source_department_code"].eq("31").all()
    assert forged_lines["source_edition"].eq("2026-06-15").all()
    assert forged_lines["source_archive_sha256"].eq("a" * 64).all()
    assert forged_lines["spatial_role"].eq("PROXY_GEOMETRY").all()

    with patch(
        "landscout.stages.enrich_grid_proximity.normalize_ign_electricity",
        create=True,
    ) as normalizer, pytest.raises(
        GridProximityError,
        match="IgnBdTopoElectricityData|electricity source",
    ):
        public_enrich_parcel_grid_proximity(
            _parcels(),
            cast(Any, forged_lines),
            SOURCE_CONFIG,
        )

    normalizer.assert_not_called()
```

### `test_public_proximity_reproduces_configured_electricity_roles`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
forged = _alternate_role_electricity_source(tmp_path)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert forged.extraction.electric_lines_layer == "CABLE_SOURCE_ALTERNATE"
assert (
        forged.extraction.transformation_posts_layer
        == "INSTALLATION_SOURCE_ALTERNATE"
    )
with pytest.raises(GridProximityError):
        public_enrich_parcel_grid_proximity(_parcels(), forged, SOURCE_CONFIG)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_public_proximity_reproduces_configured_electricity_roles(
    tmp_path: Path,
) -> None:
    forged = _alternate_role_electricity_source(tmp_path)
    assert forged.extraction.electric_lines_layer == "CABLE_SOURCE_ALTERNATE"
    assert (
        forged.extraction.transformation_posts_layer
        == "INSTALLATION_SOURCE_ALTERNATE"
    )

    with pytest.raises(GridProximityError):
        public_enrich_parcel_grid_proximity(_parcels(), forged, SOURCE_CONFIG)
```

### `test_public_proximity_rejects_archive_lineage_differing_from_config`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `archive_changes`.

**Setup**

```python
source = _configured_role_electricity_source(tmp_path)
forged_archive = replace(source.extraction.archive, **archive_changes)
forged = replace(
        source,
        extraction=replace(source.extraction, archive=forged_archive),
    )
computation.assert_not_called()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with patch(
        "landscout.stages.enrich_grid_proximity."
        "_enrich_parcel_grid_proximity_from_normalized",
    ) as computation, pytest.raises(GridProximityError):
        public_enrich_parcel_grid_proximity(_parcels(), forged, SOURCE_CONFIG)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_public_proximity_rejects_archive_lineage_differing_from_config(
    tmp_path: Path,
    archive_changes: dict[str, object],
) -> None:
    source = _configured_role_electricity_source(tmp_path)
    forged_archive = replace(source.extraction.archive, **archive_changes)
    forged = replace(
        source,
        extraction=replace(source.extraction, archive=forged_archive),
    )

    with patch(
        "landscout.stages.enrich_grid_proximity."
        "_enrich_parcel_grid_proximity_from_normalized",
    ) as computation, pytest.raises(GridProximityError):
        public_enrich_parcel_grid_proximity(_parcels(), forged, SOURCE_CONFIG)

    computation.assert_not_called()
```

### `test_source_normalization_failure_stops_grid_computation`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _electricity_source()
normalizer.assert_called_once_with(source, SOURCE_CONFIG)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with patch(
        "landscout.stages.enrich_grid_proximity.normalize_ign_electricity",
        side_effect=ValueError("physical source changed"),
        create=True,
    ) as normalizer, pytest.raises(GridProximityError):
        public_enrich_parcel_grid_proximity(
            _parcels(), source, SOURCE_CONFIG
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_source_normalization_failure_stops_grid_computation() -> None:
    source = _electricity_source()

    with patch(
        "landscout.stages.enrich_grid_proximity.normalize_ign_electricity",
        side_effect=ValueError("physical source changed"),
        create=True,
    ) as normalizer, pytest.raises(GridProximityError):
        public_enrich_parcel_grid_proximity(
            _parcels(), source, SOURCE_CONFIG
        )

    normalizer.assert_called_once_with(source, SOURCE_CONFIG)
```

### `test_separated_distance_uses_parcel_edge_not_centroid`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
result = enrich_parcel_grid_proximity(_parcels(), _lines(), _posts())
```

**Expected result**

```python
assert result.parcels.loc[0, "nearest_line_proxy_distance_m"] == pytest.approx(
        100.0
    )
assert result.parcels.loc[0, "nearest_post_proxy_distance_m"] == pytest.approx(
        100.0
    )
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_separated_distance_uses_parcel_edge_not_centroid() -> None:
    result = enrich_parcel_grid_proximity(_parcels(), _lines(), _posts())

    assert result.parcels.loc[0, "nearest_line_proxy_distance_m"] == pytest.approx(
        100.0
    )
    assert result.parcels.loc[0, "nearest_post_proxy_distance_m"] == pytest.approx(
        100.0
    )
```

### `test_touching_line_has_zero_distance`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
touching = _lines([LineString([(10, -20), (10, 30)])])
```

**Action**

```python
result = enrich_parcel_grid_proximity(_parcels(), touching, _posts())
```

**Expected result**

```python
assert result.parcels.loc[0, "nearest_line_proxy_distance_m"] == 0.0
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_touching_line_has_zero_distance() -> None:
    touching = _lines([LineString([(10, -20), (10, 30)])])

    result = enrich_parcel_grid_proximity(_parcels(), touching, _posts())

    assert result.parcels.loc[0, "nearest_line_proxy_distance_m"] == 0.0
```

### `test_post_distance_uses_parcel_and_post_polygons`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
posts = _posts(
        [Polygon([(60, 0), (60, 10), (70, 10), (70, 0), (60, 0)])]
    )
```

**Action**

```python
result = enrich_parcel_grid_proximity(_parcels(), _lines(), posts)
```

**Expected result**

```python
assert result.parcels.loc[0, "nearest_post_proxy_distance_m"] == pytest.approx(
        50.0
    )
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_post_distance_uses_parcel_and_post_polygons() -> None:
    posts = _posts(
        [Polygon([(60, 0), (60, 10), (70, 10), (70, 0), (60, 0)])]
    )

    result = enrich_parcel_grid_proximity(_parcels(), _lines(), posts)

    assert result.parcels.loc[0, "nearest_post_proxy_distance_m"] == pytest.approx(
        50.0
    )
```

### `test_epsg4326_input_is_calculated_in_lambert93_and_preserved`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
projected = _parcels()
geographic = projected.to_crs("EPSG:4326")
before_geometry = geographic.geometry.copy()
```

**Action**

```python
result = enrich_parcel_grid_proximity(geographic, _lines(), _posts())
```

**Expected result**

```python
assert result.parcels.crs == geographic.crs
assert result.parcels.loc[0, "nearest_line_proxy_distance_m"] == pytest.approx(
        100.0, abs=1e-6
    )
assert result.parcels.geometry.geom_equals_exact(
        before_geometry.reset_index(drop=True), tolerance=0
    ).all()
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_epsg4326_input_is_calculated_in_lambert93_and_preserved() -> None:
    projected = _parcels()
    geographic = projected.to_crs("EPSG:4326")
    before_geometry = geographic.geometry.copy()

    result = enrich_parcel_grid_proximity(geographic, _lines(), _posts())

    assert result.parcels.crs == geographic.crs
    assert result.parcels.loc[0, "nearest_line_proxy_distance_m"] == pytest.approx(
        100.0, abs=1e-6
    )
    assert result.parcels.geometry.geom_equals_exact(
        before_geometry.reset_index(drop=True), tolerance=0
    ).all()
```

### `test_epsg2154_parcel_input_remains_epsg2154`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
result = enrich_parcel_grid_proximity(_parcels(), _lines(), _posts())
```

**Expected result**

```python
assert result.parcels.crs is not None
assert result.parcels.crs.to_epsg() == 2154
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_epsg2154_parcel_input_remains_epsg2154() -> None:
    result = enrich_parcel_grid_proximity(_parcels(), _lines(), _posts())

    assert result.parcels.crs is not None
    assert result.parcels.crs.to_epsg() == 2154
```

### `test_valid_parcel_id_is_preserved_exactly`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
result = enrich_parcel_grid_proximity(
        _parcels(identifiers=["FR-31-VALID-ID"]), _lines(), _posts()
    )
```

**Expected result**

```python
assert result.parcels["parcel_id"].tolist() == ["FR-31-VALID-ID"]
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_valid_parcel_id_is_preserved_exactly() -> None:
    result = enrich_parcel_grid_proximity(
        _parcels(identifiers=["FR-31-VALID-ID"]), _lines(), _posts()
    )

    assert result.parcels["parcel_id"].tolist() == ["FR-31-VALID-ID"]
```

### `test_invalid_parcel_id_hygiene_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `identifier`.

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
with pytest.raises(GridProximityError, match="parcel_id"):
        enrich_parcel_grid_proximity(
            _parcels(identifiers=[identifier]), _lines(), _posts()
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_invalid_parcel_id_hygiene_is_rejected(identifier: object) -> None:
    with pytest.raises(GridProximityError, match="parcel_id"):
        enrich_parcel_grid_proximity(
            _parcels(identifiers=[identifier]), _lines(), _posts()
        )
```

### `test_supported_parcel_polygon_geometry_is_preserved`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `geometry`.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
result = enrich_parcel_grid_proximity(_parcels([geometry]), _lines(), _posts())
```

**Expected result**

```python
assert result.parcels.geometry.iloc[0].equals_exact(geometry, tolerance=0)
assert result.parcels.geometry.iloc[0].has_z == geometry.has_z
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_supported_parcel_polygon_geometry_is_preserved(geometry: object) -> None:
    result = enrich_parcel_grid_proximity(_parcels([geometry]), _lines(), _posts())

    assert result.parcels.geometry.iloc[0].equals_exact(geometry, tolerance=0)
    assert result.parcels.geometry.iloc[0].has_z == geometry.has_z
```

### `test_semantically_wrong_parcel_geometry_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `geometry`.

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
with pytest.raises(GridProximityError, match="Polygon|MultiPolygon"):
        enrich_parcel_grid_proximity(_parcels([geometry]), _lines(), _posts())
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_semantically_wrong_parcel_geometry_is_rejected(geometry: object) -> None:
    with pytest.raises(GridProximityError, match="Polygon|MultiPolygon"):
        enrich_parcel_grid_proximity(_parcels([geometry]), _lines(), _posts())
```

### `test_missing_crs_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `kind`.

**Setup**

```python
parcels = _parcels(crs=None if kind == "parcel" else "EPSG:2154")
lines = _lines(crs=None if kind == "line" else "EPSG:2154")
posts = _posts(crs=None if kind == "post" else "EPSG:2154")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridProximityError, match="CRS"):
        enrich_parcel_grid_proximity(parcels, lines, posts)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_missing_crs_is_rejected(kind: str) -> None:
    parcels = _parcels(crs=None if kind == "parcel" else "EPSG:2154")
    lines = _lines(crs=None if kind == "line" else "EPSG:2154")
    posts = _posts(crs=None if kind == "post" else "EPSG:2154")

    with pytest.raises(GridProximityError, match="CRS"):
        enrich_parcel_grid_proximity(parcels, lines, posts)
```

### `test_wrong_grid_crs_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `kind`.

**Setup**

```python
lines = _lines(crs="EPSG:4326" if kind == "line" else "EPSG:2154")
posts = _posts(crs="EPSG:4326" if kind == "post" else "EPSG:2154")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridProximityError, match="2154"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_wrong_grid_crs_is_rejected(kind: str) -> None:
    lines = _lines(crs="EPSG:4326" if kind == "line" else "EPSG:2154")
    posts = _posts(crs="EPSG:4326" if kind == "post" else "EPSG:2154")

    with pytest.raises(GridProximityError, match="2154"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)
```

### `test_z_line_has_same_horizontal_distance_as_xy_line`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
xy = _lines([LineString([(110, -20), (110, 30)])])
xyz = _lines([LineString([(110, -20, 500), (110, 30, 900)])])
```

**Action**

```python
xy_result = enrich_parcel_grid_proximity(_parcels(), xy, _posts())
xyz_result = enrich_parcel_grid_proximity(_parcels(), xyz, _posts())
```

**Expected result**

```python
assert xyz.geometry.iloc[0].has_z
assert xyz_result.parcels.loc[
        0, "nearest_line_proxy_distance_m"
    ] == pytest.approx(xy_result.parcels.loc[0, "nearest_line_proxy_distance_m"])
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_z_line_has_same_horizontal_distance_as_xy_line() -> None:
    xy = _lines([LineString([(110, -20), (110, 30)])])
    xyz = _lines([LineString([(110, -20, 500), (110, 30, 900)])])

    xy_result = enrich_parcel_grid_proximity(_parcels(), xy, _posts())
    xyz_result = enrich_parcel_grid_proximity(_parcels(), xyz, _posts())

    assert xyz.geometry.iloc[0].has_z
    assert xyz_result.parcels.loc[
        0, "nearest_line_proxy_distance_m"
    ] == pytest.approx(xy_result.parcels.loc[0, "nearest_line_proxy_distance_m"])
```

### `test_line_tie_is_counted_and_lexical_feature_id_wins`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
lines = _lines(
        [
            LineString([(-100, -20), (-100, 30)]),
            LineString([(110, -20), (110, 30)]),
        ],
        identifiers=["Z-LINE", "A-LINE"],
    )
row = result.parcels.iloc[0]
```

**Action**

```python
result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())
```

**Expected result**

```python
assert row["nearest_line_proxy_distance_m"] == pytest.approx(100.0)
assert row["nearest_line_tie_count"] == 2
assert row["nearest_line_grid_feature_id"] == "A-LINE"
assert row["nearest_exact_line_tie_count"] == 2
assert row["nearest_exact_line_grid_feature_id"] == "A-LINE"
assert result.voltage_level_proximity.loc[0, "tie_count"] == 2
assert (
        result.voltage_level_proximity.loc[
            0, "nearest_line_grid_feature_id"
        ]
        == "A-LINE"
    )
assert len(result.parcels) == 1
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_line_tie_is_counted_and_lexical_feature_id_wins() -> None:
    lines = _lines(
        [
            LineString([(-100, -20), (-100, 30)]),
            LineString([(110, -20), (110, 30)]),
        ],
        identifiers=["Z-LINE", "A-LINE"],
    )

    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())

    row = result.parcels.iloc[0]
    assert row["nearest_line_proxy_distance_m"] == pytest.approx(100.0)
    assert row["nearest_line_tie_count"] == 2
    assert row["nearest_line_grid_feature_id"] == "A-LINE"
    assert row["nearest_exact_line_tie_count"] == 2
    assert row["nearest_exact_line_grid_feature_id"] == "A-LINE"
    assert result.voltage_level_proximity.loc[0, "tie_count"] == 2
    assert (
        result.voltage_level_proximity.loc[
            0, "nearest_line_grid_feature_id"
        ]
        == "A-LINE"
    )
    assert len(result.parcels) == 1
```

### `test_cross_voltage_tie_uses_lexical_global_feature_id`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
lines = _lines(
        [
            LineString([(-100, -20), (-100, 30)]),
            LineString([(110, -20), (110, 30)]),
        ],
        identifiers=["Z-LINE-110", "A-LINE-275"],
        voltage_statuses=["EXACT", "EXACT"],
        voltages=[110.0, 275.0],
    )
row = result.parcels.iloc[0]
```

**Action**

```python
result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())
profile = profile_grid_proximity(result)
```

**Expected result**

```python
assert row["nearest_exact_line_proxy_distance_m"] == pytest.approx(100.0)
assert row["nearest_exact_line_grid_feature_id"] == "A-LINE-275"
assert row["nearest_exact_line_voltage_kv"] == 275.0
assert row["nearest_exact_line_tie_count"] == 2
assert result.voltage_level_proximity[
        "nearest_line_proxy_distance_m"
    ].tolist() == pytest.approx([100.0, 100.0])
assert result.voltage_level_proximity["tie_count"].tolist() == [1, 1]
assert profile.nearest_exact_line.tie_count == 1
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_cross_voltage_tie_uses_lexical_global_feature_id() -> None:
    lines = _lines(
        [
            LineString([(-100, -20), (-100, 30)]),
            LineString([(110, -20), (110, 30)]),
        ],
        identifiers=["Z-LINE-110", "A-LINE-275"],
        voltage_statuses=["EXACT", "EXACT"],
        voltages=[110.0, 275.0],
    )

    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())
    profile = profile_grid_proximity(result)

    row = result.parcels.iloc[0]
    assert row["nearest_exact_line_proxy_distance_m"] == pytest.approx(100.0)
    assert row["nearest_exact_line_grid_feature_id"] == "A-LINE-275"
    assert row["nearest_exact_line_voltage_kv"] == 275.0
    assert row["nearest_exact_line_tie_count"] == 2
    assert result.voltage_level_proximity[
        "nearest_line_proxy_distance_m"
    ].tolist() == pytest.approx([100.0, 100.0])
    assert result.voltage_level_proximity["tie_count"].tolist() == [1, 1]
    assert profile.nearest_exact_line.tie_count == 1
```

### `test_nonvalid_grid_geometries_are_excluded_without_row_loss`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
invalid = Polygon([(0, 0), (20, 20), (20, 0), (0, 20), (0, 0)])
lines = _lines(
        [None, LineString(), invalid, LineString([(110, -20), (110, 30)])],
        identifiers=["NULL", "EMPTY", "INVALID", "VALID"],
        voltage_statuses=["UNKNOWN", "UNKNOWN", "UNKNOWN", "EXACT"],
        voltages=[None, None, None, 110.0],
    )
```

**Action**

```python
result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())
```

**Expected result**

```python
assert len(result.parcels) == 1
assert result.parcels.loc[0, "nearest_line_grid_feature_id"] == "VALID"
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_nonvalid_grid_geometries_are_excluded_without_row_loss() -> None:
    invalid = Polygon([(0, 0), (20, 20), (20, 0), (0, 20), (0, 0)])
    lines = _lines(
        [None, LineString(), invalid, LineString([(110, -20), (110, 30)])],
        identifiers=["NULL", "EMPTY", "INVALID", "VALID"],
        voltage_statuses=["UNKNOWN", "UNKNOWN", "UNKNOWN", "EXACT"],
        voltages=[None, None, None, 110.0],
    )

    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())

    assert len(result.parcels) == 1
    assert result.parcels.loc[0, "nearest_line_grid_feature_id"] == "VALID"
```

### `test_wrong_grid_feature_type_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `kind`.

**Setup**

```python
lines = _lines(feature_types=["WRONG"] if kind == "line" else None)
posts = _posts(feature_types=["WRONG"] if kind == "post" else None)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridProximityError, match="grid_feature_type"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_wrong_grid_feature_type_is_rejected(kind: str) -> None:
    lines = _lines(feature_types=["WRONG"] if kind == "line" else None)
    posts = _posts(feature_types=["WRONG"] if kind == "post" else None)

    with pytest.raises(GridProximityError, match="grid_feature_type"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)
```

### `test_duplicate_grid_feature_id_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `kind`.

**Setup**

```python
if kind == "line":
        lines = _lines(
            [LineString([(100, 0), (100, 10)])] * 2,
            identifiers=["DUPLICATE", "DUPLICATE"],
        )
        posts = _posts()
    else:
        lines = _lines()
        posts = _posts(
            [
                Polygon([(50, 0), (50, 5), (55, 5), (55, 0), (50, 0)]),
                Polygon([(60, 0), (60, 5), (65, 5), (65, 0), (60, 0)]),
            ],
            identifiers=["DUPLICATE", "DUPLICATE"],
        )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridProximityError, match="unique"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_duplicate_grid_feature_id_is_rejected(kind: str) -> None:
    if kind == "line":
        lines = _lines(
            [LineString([(100, 0), (100, 10)])] * 2,
            identifiers=["DUPLICATE", "DUPLICATE"],
        )
        posts = _posts()
    else:
        lines = _lines()
        posts = _posts(
            [
                Polygon([(50, 0), (50, 5), (55, 5), (55, 0), (50, 0)]),
                Polygon([(60, 0), (60, 5), (65, 5), (65, 0), (60, 0)]),
            ],
            identifiers=["DUPLICATE", "DUPLICATE"],
        )

    with pytest.raises(GridProximityError, match="unique"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)
```

### `test_wrong_spatial_role_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `kind`.

**Setup**

```python
lines = _lines(spatial_roles=["EXACT"] if kind == "line" else None)
posts = _posts(spatial_roles=["EXACT"] if kind == "post" else None)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridProximityError, match="PROXY_GEOMETRY"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_wrong_spatial_role_is_rejected(kind: str) -> None:
    lines = _lines(spatial_roles=["EXACT"] if kind == "line" else None)
    posts = _posts(spatial_roles=["EXACT"] if kind == "post" else None)

    with pytest.raises(GridProximityError, match="PROXY_GEOMETRY"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)
```

### `test_unsupported_valid_grid_geometry_type_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `geometry`, `kind`.

**Setup**

```python
lines = _lines([geometry]) if kind == "line" else _lines()
posts = _posts([geometry]) if kind == "post" else _posts()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridProximityError, match="geometry types"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_unsupported_valid_grid_geometry_type_is_rejected(
    kind: str, geometry: object
) -> None:
    lines = _lines([geometry]) if kind == "line" else _lines()
    posts = _posts([geometry]) if kind == "post" else _posts()

    with pytest.raises(GridProximityError, match="geometry types"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)
```

### `test_supported_multi_geometries_are_accepted`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
lines = _lines(
        [MultiLineString([[(110, -20), (110, 30)], [(120, -20), (120, 30)]])]
    )
posts = _posts(
        [
            MultiPolygon(
                [
                    Polygon(
                        [(110, 0), (110, 5), (115, 5), (115, 0), (110, 0)]
                    )
                ]
            )
        ]
    )
```

**Action**

```python
result = enrich_parcel_grid_proximity(_parcels(), lines, posts)
```

**Expected result**

```python
assert len(result.parcels) == 1
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_supported_multi_geometries_are_accepted() -> None:
    lines = _lines(
        [MultiLineString([[(110, -20), (110, 30)], [(120, -20), (120, 30)]])]
    )
    posts = _posts(
        [
            MultiPolygon(
                [
                    Polygon(
                        [(110, 0), (110, 5), (115, 5), (115, 0), (110, 0)]
                    )
                ]
            )
        ]
    )

    result = enrich_parcel_grid_proximity(_parcels(), lines, posts)

    assert len(result.parcels) == 1
```

### `test_nearest_any_line_preserves_every_voltage_status`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `status`.

**Setup**

```python
voltage = 110.0 if status == "EXACT" else None
lines = _lines(voltage_statuses=[status], voltages=[voltage])
```

**Action**

```python
result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())
```

**Expected result**

```python
assert result.parcels.loc[0, "nearest_line_voltage_status"] == status
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_nearest_any_line_preserves_every_voltage_status(status: str) -> None:
    voltage = 110.0 if status == "EXACT" else None
    lines = _lines(voltage_statuses=[status], voltages=[voltage])

    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())

    assert result.parcels.loc[0, "nearest_line_voltage_status"] == status
```

### `test_nearest_exact_and_voltage_table_exclude_nonexact_lines`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
lines = _lines(
        [
            LineString([(20, -20), (20, 30)]),
            LineString([(110, -20), (110, 30)]),
            LineString([(210, -20), (210, 30)]),
        ],
        identifiers=["BELOW", "EXACT-110", "EXACT-275"],
        voltage_statuses=["BELOW", "EXACT", "EXACT"],
        voltages=[None, 110.0, 275.0],
    )
row = result.parcels.iloc[0]
```

**Action**

```python
result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())
```

**Expected result**

```python
assert row["nearest_line_grid_feature_id"] == "BELOW"
assert row["nearest_exact_line_grid_feature_id"] == "EXACT-110"
assert row["nearest_exact_line_voltage_kv"] == 110.0
assert result.voltage_level_proximity["voltage_kv"].tolist() == [110.0, 275.0]
assert len(result.voltage_level_proximity) == 2
assert list(result.voltage_level_proximity.columns) == list(
        VOLTAGE_PROXIMITY_COLUMNS
    )
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_nearest_exact_and_voltage_table_exclude_nonexact_lines() -> None:
    lines = _lines(
        [
            LineString([(20, -20), (20, 30)]),
            LineString([(110, -20), (110, 30)]),
            LineString([(210, -20), (210, 30)]),
        ],
        identifiers=["BELOW", "EXACT-110", "EXACT-275"],
        voltage_statuses=["BELOW", "EXACT", "EXACT"],
        voltages=[None, 110.0, 275.0],
    )

    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())

    row = result.parcels.iloc[0]
    assert row["nearest_line_grid_feature_id"] == "BELOW"
    assert row["nearest_exact_line_grid_feature_id"] == "EXACT-110"
    assert row["nearest_exact_line_voltage_kv"] == 110.0
    assert result.voltage_level_proximity["voltage_kv"].tolist() == [110.0, 275.0]
    assert len(result.voltage_level_proximity) == 2
    assert list(result.voltage_level_proximity.columns) == list(
        VOLTAGE_PROXIMITY_COLUMNS
    )
```

### `test_voltage_table_is_exact_ordered_cartesian_product`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _two_parcel_two_voltage_result()
for voltage_kv in (110.0, 275.0):
        rows = result.voltage_level_proximity.loc[
            result.voltage_level_proximity["voltage_kv"] == voltage_kv
        ]
        assert rows["parcel_id"].tolist() == ["PARCEL-2", "PARCEL-1"]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert tuple(item.voltage_kv for item in result.voltage_level_coverage) == (
        110.0,
        275.0,
    )
assert len(result.voltage_level_proximity) == 4
assert not result.voltage_level_proximity.duplicated(
        ["parcel_id", "voltage_kv"]
    ).any()
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_voltage_table_is_exact_ordered_cartesian_product() -> None:
    result = _two_parcel_two_voltage_result()

    assert tuple(item.voltage_kv for item in result.voltage_level_coverage) == (
        110.0,
        275.0,
    )
    assert len(result.voltage_level_proximity) == 4
    assert not result.voltage_level_proximity.duplicated(
        ["parcel_id", "voltage_kv"]
    ).any()
    for voltage_kv in (110.0, 275.0):
        rows = result.voltage_level_proximity.loc[
            result.voltage_level_proximity["voltage_kv"] == voltage_kv
        ]
        assert rows["parcel_id"].tolist() == ["PARCEL-2", "PARCEL-1"]
```

### `test_invalid_exact_voltage_values_are_not_used_as_exact`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
lines = _lines(
        [LineString([(20, -20), (20, 30)])] * 4,
        identifiers=["ZERO", "NEGATIVE", "INFINITE", "TEXT"],
        voltage_statuses=["EXACT"] * 4,
        voltages=[0.0, -1.0, float("inf"), "110"],
    )
```

**Action**

```python
result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())
```

**Expected result**

```python
assert result.parcels["nearest_exact_line_proxy_distance_m"].isna().all()
assert result.voltage_level_proximity.empty
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_invalid_exact_voltage_values_are_not_used_as_exact() -> None:
    lines = _lines(
        [LineString([(20, -20), (20, 30)])] * 4,
        identifiers=["ZERO", "NEGATIVE", "INFINITE", "TEXT"],
        voltage_statuses=["EXACT"] * 4,
        voltages=[0.0, -1.0, float("inf"), "110"],
    )

    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())

    assert result.parcels["nearest_exact_line_proxy_distance_m"].isna().all()
    assert result.voltage_level_proximity.empty
```

### `test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
lines = _lines(voltage_statuses=["UNKNOWN"], voltages=[None])
```

**Action**

```python
result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())
profile = profile_grid_proximity(result)
```

**Expected result**

```python
assert result.parcels.loc[0, "nearest_line_grid_feature_id"] == "LINE-1"
assert result.parcels["nearest_exact_line_proxy_distance_m"].isna().all()
assert result.parcels["nearest_exact_line_grid_feature_id"].isna().all()
assert result.voltage_level_proximity.empty
assert list(result.voltage_level_proximity.columns) == list(
        VOLTAGE_PROXIMITY_COLUMNS
    )
assert is_float_dtype(
        result.parcels["nearest_exact_line_proxy_distance_m"].dtype
    )
assert is_float_dtype(result.parcels["nearest_exact_line_voltage_kv"].dtype)
assert is_integer_dtype(result.parcels["nearest_exact_line_tie_count"].dtype)
assert str(result.parcels["nearest_exact_line_tie_count"].dtype) == "Int64"
assert is_float_dtype(result.voltage_level_proximity["voltage_kv"].dtype)
assert is_float_dtype(
        result.voltage_level_proximity["nearest_line_proxy_distance_m"].dtype
    )
assert str(result.voltage_level_proximity["tie_count"].dtype) == "Int64"
assert result.voltage_level_coverage == ()
assert profile.nearest_exact_line.count == 0
assert profile.nearest_exact_line.missing_count == 1
```

**Regression protected**

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table() -> None:
    lines = _lines(voltage_statuses=["UNKNOWN"], voltages=[None])

    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())

    assert result.parcels.loc[0, "nearest_line_grid_feature_id"] == "LINE-1"
    assert result.parcels["nearest_exact_line_proxy_distance_m"].isna().all()
    assert result.parcels["nearest_exact_line_grid_feature_id"].isna().all()
    assert result.voltage_level_proximity.empty
    assert list(result.voltage_level_proximity.columns) == list(
        VOLTAGE_PROXIMITY_COLUMNS
    )
    assert is_float_dtype(
        result.parcels["nearest_exact_line_proxy_distance_m"].dtype
    )
    assert is_float_dtype(result.parcels["nearest_exact_line_voltage_kv"].dtype)
    assert is_integer_dtype(result.parcels["nearest_exact_line_tie_count"].dtype)
    assert str(result.parcels["nearest_exact_line_tie_count"].dtype) == "Int64"
    assert is_float_dtype(result.voltage_level_proximity["voltage_kv"].dtype)
    assert is_float_dtype(
        result.voltage_level_proximity["nearest_line_proxy_distance_m"].dtype
    )
    assert str(result.voltage_level_proximity["tie_count"].dtype) == "Int64"
    assert result.voltage_level_coverage == ()
    profile = profile_grid_proximity(result)
    assert profile.nearest_exact_line.count == 0
    assert profile.nearest_exact_line.missing_count == 1
```

### `test_missing_parcel_column_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`.

**Setup**

```python
parcels = _parcels().drop(columns=column)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridProximityError, match=column):
        enrich_parcel_grid_proximity(parcels, _lines(), _posts())
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_missing_parcel_column_is_rejected(column: str) -> None:
    parcels = _parcels().drop(columns=column)

    with pytest.raises(GridProximityError, match=column):
        enrich_parcel_grid_proximity(parcels, _lines(), _posts())
```

### `test_null_parcel_id_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
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
with pytest.raises(GridProximityError, match="parcel_id"):
        enrich_parcel_grid_proximity(
            _parcels(identifiers=[None]), _lines(), _posts()
        )
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_null_parcel_id_is_rejected() -> None:
    with pytest.raises(GridProximityError, match="parcel_id"):
        enrich_parcel_grid_proximity(
            _parcels(identifiers=[None]), _lines(), _posts()
        )
```

### `test_duplicate_parcel_id_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels(
        [
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
            Polygon([(20, 0), (20, 10), (30, 10), (30, 0), (20, 0)]),
        ],
        identifiers=["DUPLICATE", "DUPLICATE"],
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridProximityError, match="unique"):
        enrich_parcel_grid_proximity(parcels, _lines(), _posts())
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_duplicate_parcel_id_is_rejected() -> None:
    parcels = _parcels(
        [
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
            Polygon([(20, 0), (20, 10), (30, 10), (30, 0), (20, 0)]),
        ],
        identifiers=["DUPLICATE", "DUPLICATE"],
    )

    with pytest.raises(GridProximityError, match="unique"):
        enrich_parcel_grid_proximity(parcels, _lines(), _posts())
```

### `test_bad_parcel_geometry_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `geometry`, `message`.

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
with pytest.raises(GridProximityError, match=message):
        enrich_parcel_grid_proximity(
            _parcels([geometry]), _lines(), _posts()
        )
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_bad_parcel_geometry_is_rejected(geometry: object, message: str) -> None:
    with pytest.raises(GridProximityError, match=message):
        enrich_parcel_grid_proximity(
            _parcels([geometry]), _lines(), _posts()
        )
```

### `test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels(
        [
            Polygon([(20, 0), (20, 10), (30, 10), (30, 0), (20, 0)]),
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
        ],
        identifiers=["SECOND-SPATIAL", "FIRST-SPATIAL"],
        index=[99, 99],
    )
lines = _lines()
posts = _posts()
parcels_before = deepcopy(parcels)
lines_before = deepcopy(lines)
posts_before = deepcopy(posts)
assert_geodataframe_equal(parcels, parcels_before)
assert_geodataframe_equal(lines, lines_before)
assert_geodataframe_equal(posts, posts_before)
```

**Action**

```python
result = enrich_parcel_grid_proximity(parcels, lines, posts)
```

**Expected result**

```python
assert result.parcels["parcel_id"].tolist() == [
        "SECOND-SPATIAL",
        "FIRST-SPATIAL",
    ]
assert isinstance(result.parcels.index, pd.RangeIndex)
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved() -> None:
    parcels = _parcels(
        [
            Polygon([(20, 0), (20, 10), (30, 10), (30, 0), (20, 0)]),
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
        ],
        identifiers=["SECOND-SPATIAL", "FIRST-SPATIAL"],
        index=[99, 99],
    )
    lines = _lines()
    posts = _posts()
    parcels_before = deepcopy(parcels)
    lines_before = deepcopy(lines)
    posts_before = deepcopy(posts)

    result = enrich_parcel_grid_proximity(parcels, lines, posts)

    assert_geodataframe_equal(parcels, parcels_before)
    assert_geodataframe_equal(lines, lines_before)
    assert_geodataframe_equal(posts, posts_before)
    assert result.parcels["parcel_id"].tolist() == [
        "SECOND-SPATIAL",
        "FIRST-SPATIAL",
    ]
    assert isinstance(result.parcels.index, pd.RangeIndex)
```

### `test_distance_profile_is_threshold_free_and_tracks_ties`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels(
        [
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
            Polygon([(50, 0), (50, 10), (60, 10), (60, 0), (50, 0)]),
        ]
    )
lines = _lines(
        [
            LineString([(-100, -20), (-100, 30)]),
            LineString([(110, -20), (110, 30)]),
        ],
        identifiers=["Z-LINE", "A-LINE"],
    )
```

**Action**

```python
result = enrich_parcel_grid_proximity(parcels, lines, _posts())
profile = profile_grid_proximity(result)
```

**Expected result**

```python
assert profile.parcel_count == 2
assert profile.nearest_line.count == 2
assert profile.nearest_line.missing_count == 0
assert profile.nearest_line.minimum == pytest.approx(50.0)
assert profile.nearest_line.p50 == pytest.approx(75.0)
assert profile.nearest_line.maximum == pytest.approx(100.0)
assert profile.nearest_line.tie_count == 1
assert profile.voltage_levels[0].voltage_kv == 110.0
assert profile.voltage_levels[0].line_feature_count == 2
assert profile.voltage_levels[0].parcel_proximity_count == 2
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_distance_profile_is_threshold_free_and_tracks_ties() -> None:
    parcels = _parcels(
        [
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
            Polygon([(50, 0), (50, 10), (60, 10), (60, 0), (50, 0)]),
        ]
    )
    lines = _lines(
        [
            LineString([(-100, -20), (-100, 30)]),
            LineString([(110, -20), (110, 30)]),
        ],
        identifiers=["Z-LINE", "A-LINE"],
    )
    result = enrich_parcel_grid_proximity(parcels, lines, _posts())

    profile = profile_grid_proximity(result)

    assert profile.parcel_count == 2
    assert profile.nearest_line.count == 2
    assert profile.nearest_line.missing_count == 0
    assert profile.nearest_line.minimum == pytest.approx(50.0)
    assert profile.nearest_line.p50 == pytest.approx(75.0)
    assert profile.nearest_line.maximum == pytest.approx(100.0)
    assert profile.nearest_line.tie_count == 1
    assert profile.voltage_levels[0].voltage_kv == 110.0
    assert profile.voltage_levels[0].line_feature_count == 2
    assert profile.voltage_levels[0].parcel_proximity_count == 2
```

### `test_profile_rejects_missing_voltage_cartesian_row`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _two_parcel_two_voltage_result()
table = result.voltage_level_proximity.iloc[:-1].copy()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridProximityError):
        profile_grid_proximity(replace(result, voltage_level_proximity=table))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_profile_rejects_missing_voltage_cartesian_row() -> None:
    result = _two_parcel_two_voltage_result()
    table = result.voltage_level_proximity.iloc[:-1].copy()

    with pytest.raises(GridProximityError):
        profile_grid_proximity(replace(result, voltage_level_proximity=table))
```

### `test_profile_rejects_unknown_voltage_parcel_with_same_total_count`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _two_parcel_two_voltage_result()
corrupted = _mutate_voltage_result(result, "parcel_id", "UNKNOWN-PARCEL")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridProximityError):
        profile_grid_proximity(corrupted)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_profile_rejects_unknown_voltage_parcel_with_same_total_count() -> None:
    result = _two_parcel_two_voltage_result()
    corrupted = _mutate_voltage_result(result, "parcel_id", "UNKNOWN-PARCEL")

    with pytest.raises(GridProximityError):
        profile_grid_proximity(corrupted)
```

### `test_profile_rejects_duplicate_parcel_voltage_pair`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _two_parcel_two_voltage_result()
table = result.voltage_level_proximity.copy()
table.at[1, "parcel_id"] = table.at[0, "parcel_id"]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridProximityError, match="unique"):
        profile_grid_proximity(replace(result, voltage_level_proximity=table))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_profile_rejects_duplicate_parcel_voltage_pair() -> None:
    result = _two_parcel_two_voltage_result()
    table = result.voltage_level_proximity.copy()
    table.at[1, "parcel_id"] = table.at[0, "parcel_id"]

    with pytest.raises(GridProximityError, match="unique"):
        profile_grid_proximity(replace(result, voltage_level_proximity=table))
```

### `test_profile_rejects_voltage_rows_out_of_parcel_order`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _two_parcel_two_voltage_result()
table = result.voltage_level_proximity.iloc[[1, 0, 2, 3]].reset_index(drop=True)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridProximityError, match="exact parcel set"):
        profile_grid_proximity(replace(result, voltage_level_proximity=table))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_profile_rejects_voltage_rows_out_of_parcel_order() -> None:
    result = _two_parcel_two_voltage_result()
    table = result.voltage_level_proximity.iloc[[1, 0, 2, 3]].reset_index(drop=True)

    with pytest.raises(GridProximityError, match="exact parcel set"):
        profile_grid_proximity(replace(result, voltage_level_proximity=table))
```

### `test_profile_rejects_inconsistent_global_exact_distance`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _two_parcel_two_voltage_result()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridProximityError, match="exact-line distance"):
        profile_grid_proximity(
            _mutate_parcel_result(
                result,
                "nearest_exact_line_proxy_distance_m",
                5000.0,
            )
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_profile_rejects_inconsistent_global_exact_distance() -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="exact-line distance"):
        profile_grid_proximity(
            _mutate_parcel_result(
                result,
                "nearest_exact_line_proxy_distance_m",
                5000.0,
            )
        )
```

### `test_profile_rejects_inconsistent_global_exact_identity`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`, `value`.

**Setup**

```python
result = _two_parcel_two_voltage_result()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridProximityError, match="inconsistent"):
        profile_grid_proximity(_mutate_parcel_result(result, column, value))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_profile_rejects_inconsistent_global_exact_identity(
    column: str,
    value: object,
) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="inconsistent"):
        profile_grid_proximity(_mutate_parcel_result(result, column, value))
```

### `test_profile_rejects_inconsistent_global_exact_metadata`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`, `value`.

**Setup**

```python
result = _two_parcel_two_voltage_result()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridProximityError, match="inconsistent"):
        profile_grid_proximity(_mutate_parcel_result(result, column, value))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_profile_rejects_inconsistent_global_exact_metadata(
    column: str,
    value: object,
) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="inconsistent"):
        profile_grid_proximity(_mutate_parcel_result(result, column, value))
```

### `test_profile_rejects_inconsistent_global_exact_tie_count`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _two_parcel_two_voltage_result()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridProximityError, match="tie count"):
        profile_grid_proximity(
            _mutate_parcel_result(result, "nearest_exact_line_tie_count", 2)
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_profile_rejects_inconsistent_global_exact_tie_count() -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="tie count"):
        profile_grid_proximity(
            _mutate_parcel_result(result, "nearest_exact_line_tie_count", 2)
        )
```

### `test_profile_rejects_bad_required_match_tie_count`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`, `value`.

**Setup**

```python
result = _two_parcel_two_voltage_result()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridProximityError, match="tie_count|match"):
        profile_grid_proximity(_mutate_parcel_result(result, column, value))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_profile_rejects_bad_required_match_tie_count(
    column: str, value: object
) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="tie_count|match"):
        profile_grid_proximity(_mutate_parcel_result(result, column, value))
```

### `test_profile_rejects_bad_long_table_tie_count`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `value`.

**Setup**

```python
result = _two_parcel_two_voltage_result()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridProximityError, match="tie_count|match"):
        profile_grid_proximity(_mutate_voltage_result(result, "tie_count", value))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_profile_rejects_bad_long_table_tie_count(value: object) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="tie_count|match"):
        profile_grid_proximity(_mutate_voltage_result(result, "tie_count", value))
```

### `test_profile_rejects_missing_main_match_feature_id`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`.

**Setup**

```python
result = _two_parcel_two_voltage_result()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridProximityError, match="require"):
        profile_grid_proximity(_mutate_parcel_result(result, column, None))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_profile_rejects_missing_main_match_feature_id(column: str) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="require"):
        profile_grid_proximity(_mutate_parcel_result(result, column, None))
```

### `test_profile_rejects_bad_required_match_distance`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`, `value`.

**Setup**

```python
result = _two_parcel_two_voltage_result()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridProximityError):
        profile_grid_proximity(_mutate_parcel_result(result, column, value))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_profile_rejects_bad_required_match_distance(
    column: str, value: object
) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError):
        profile_grid_proximity(_mutate_parcel_result(result, column, value))
```

### `test_profile_rejects_bad_exact_match_voltage`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `value`.

**Setup**

```python
result = _two_parcel_two_voltage_result()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridProximityError, match="voltage|match"):
        profile_grid_proximity(
            _mutate_parcel_result(result, "nearest_exact_line_voltage_kv", value)
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_profile_rejects_bad_exact_match_voltage(value: object) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="voltage|match"):
        profile_grid_proximity(
            _mutate_parcel_result(result, "nearest_exact_line_voltage_kv", value)
        )
```

### `test_profile_rejects_bad_result_parcel_id`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _two_parcel_two_voltage_result()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridProximityError, match="parcel_id"):
        profile_grid_proximity(_mutate_parcel_result(result, "parcel_id", " BAD "))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_profile_rejects_bad_result_parcel_id() -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="parcel_id"):
        profile_grid_proximity(_mutate_parcel_result(result, "parcel_id", " BAD "))
```

### `test_profile_rejects_missing_required_proximity_column`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _two_parcel_two_voltage_result()
parcels = result.parcels.drop(columns="nearest_line_grid_feature_id")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridProximityError, match="Missing proximity"):
        profile_grid_proximity(replace(result, parcels=parcels))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_profile_rejects_missing_required_proximity_column() -> None:
    result = _two_parcel_two_voltage_result()
    parcels = result.parcels.drop(columns="nearest_line_grid_feature_id")

    with pytest.raises(GridProximityError, match="Missing proximity"):
        profile_grid_proximity(replace(result, parcels=parcels))
```

### `test_profile_rejects_nondeterministic_or_duplicate_coverage`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `mutation`.

**Setup**

```python
result = _two_parcel_two_voltage_result()
if mutation == "reversed":
        coverage = tuple(reversed(result.voltage_level_coverage))
    else:
        coverage = (*result.voltage_level_coverage, result.voltage_level_coverage[0])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridProximityError, match="coverage"):
        profile_grid_proximity(replace(result, voltage_level_coverage=coverage))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_profile_rejects_nondeterministic_or_duplicate_coverage(
    mutation: str,
) -> None:
    result = _two_parcel_two_voltage_result()
    if mutation == "reversed":
        coverage = tuple(reversed(result.voltage_level_coverage))
    else:
        coverage = (*result.voltage_level_coverage, result.voltage_level_coverage[0])

    with pytest.raises(GridProximityError, match="coverage"):
        profile_grid_proximity(replace(result, voltage_level_coverage=coverage))
```

### `test_profile_rejects_invalid_voltage_coverage_level`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `voltage_kv`.

**Setup**

```python
result = _two_parcel_two_voltage_result()
```

**Action**

```python
coverage = (
        VoltageLevelCoverage(voltage_kv=voltage_kv, line_feature_count=1),
    )
```

**Expected result**

```python
with pytest.raises(GridProximityError, match="coverage"):
        profile_grid_proximity(replace(result, voltage_level_coverage=coverage))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_profile_rejects_invalid_voltage_coverage_level(voltage_kv: object) -> None:
    result = _two_parcel_two_voltage_result()
    coverage = (
        VoltageLevelCoverage(voltage_kv=voltage_kv, line_feature_count=1),
    )

    with pytest.raises(GridProximityError, match="coverage"):
        profile_grid_proximity(replace(result, voltage_level_coverage=coverage))
```

### `test_profile_rejects_invalid_voltage_coverage_feature_count`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `feature_count`.

**Setup**

```python
result = _two_parcel_two_voltage_result()
```

**Action**

```python
coverage = (
        VoltageLevelCoverage(voltage_kv=110.0, line_feature_count=feature_count),
    )
```

**Expected result**

```python
with pytest.raises(GridProximityError, match="line_feature_count"):
        profile_grid_proximity(replace(result, voltage_level_coverage=coverage))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_profile_rejects_invalid_voltage_coverage_feature_count(
    feature_count: object,
) -> None:
    result = _two_parcel_two_voltage_result()
    coverage = (
        VoltageLevelCoverage(voltage_kv=110.0, line_feature_count=feature_count),
    )

    with pytest.raises(GridProximityError, match="line_feature_count"):
        profile_grid_proximity(replace(result, voltage_level_coverage=coverage))
```

### `test_profile_rejects_invalid_long_table_voltage`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `value`.

**Setup**

```python
result = _two_parcel_two_voltage_result()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridProximityError, match="Voltage proximity"):
        profile_grid_proximity(_mutate_voltage_result(result, "voltage_kv", value))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_profile_rejects_invalid_long_table_voltage(value: object) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="Voltage proximity"):
        profile_grid_proximity(_mutate_voltage_result(result, "voltage_kv", value))
```

### `test_profile_rejects_missing_long_table_match_lineage`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`.

**Setup**

```python
result = _two_parcel_two_voltage_result()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridProximityError, match="require"):
        profile_grid_proximity(_mutate_voltage_result(result, column, None))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_profile_rejects_missing_long_table_match_lineage(column: str) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="require"):
        profile_grid_proximity(_mutate_voltage_result(result, column, None))
```

### `test_profile_rejects_bad_long_table_distance`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `value`.

**Setup**

```python
result = _two_parcel_two_voltage_result()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridProximityError):
        profile_grid_proximity(
            _mutate_voltage_result(
                result, "nearest_line_proxy_distance_m", value
            )
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_profile_rejects_bad_long_table_distance(value: object) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError):
        profile_grid_proximity(
            _mutate_voltage_result(
                result, "nearest_line_proxy_distance_m", value
            )
        )
```

### `test_profile_allows_consistent_missing_manager_and_asset_status`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
lines = _lines()
lines["manager_name"] = None
lines["asset_status_raw"] = None
```

**Action**

```python
result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())
profile = profile_grid_proximity(result)
```

**Expected result**

```python
assert profile.parcel_count == 1
assert result.parcels["nearest_exact_line_manager_name"].isna().all()
assert result.parcels["nearest_exact_line_asset_status_raw"].isna().all()
assert result.voltage_level_proximity["manager_name"].isna().all()
assert result.voltage_level_proximity["asset_status_raw"].isna().all()
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_profile_allows_consistent_missing_manager_and_asset_status() -> None:
    lines = _lines()
    lines["manager_name"] = None
    lines["asset_status_raw"] = None
    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())

    profile = profile_grid_proximity(result)

    assert profile.parcel_count == 1
    assert result.parcels["nearest_exact_line_manager_name"].isna().all()
    assert result.parcels["nearest_exact_line_asset_status_raw"].isna().all()
    assert result.voltage_level_proximity["manager_name"].isna().all()
    assert result.voltage_level_proximity["asset_status_raw"].isna().all()
```

### `test_profile_rejects_nonnull_exact_field_without_exact_coverage`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`, `value`.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
result = enrich_parcel_grid_proximity(
        _parcels(),
        _lines(voltage_statuses=["UNKNOWN"], voltages=[None]),
        _posts(),
    )
```

**Expected result**

```python
with pytest.raises(GridProximityError, match="unmatched|entirely"):
        profile_grid_proximity(_mutate_parcel_result(result, column, value))
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_profile_rejects_nonnull_exact_field_without_exact_coverage(
    column: str, value: object
) -> None:
    result = enrich_parcel_grid_proximity(
        _parcels(),
        _lines(voltage_statuses=["UNKNOWN"], voltages=[None]),
        _posts(),
    )

    with pytest.raises(GridProximityError, match="unmatched|entirely"):
        profile_grid_proximity(_mutate_parcel_result(result, column, value))
```

### `test_no_valid_required_grid_feature_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `kind`.

**Setup**

```python
lines = _lines([None]) if kind == "line" else _lines()
posts = _posts([None]) if kind == "post" else _posts()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridProximityError, match="No VALID"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_no_valid_required_grid_feature_is_rejected(kind: str) -> None:
    lines = _lines([None]) if kind == "line" else _lines()
    posts = _posts([None]) if kind == "post" else _posts()

    with pytest.raises(GridProximityError, match="No VALID"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)
```


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

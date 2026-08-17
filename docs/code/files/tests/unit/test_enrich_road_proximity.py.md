# `tests/unit/test_enrich_road_proximity.py`

## File identity

- Repository path: `tests/unit/test_enrich_road_proximity.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `enrich_road_proximity` contracts exercised in this file.
- Source SHA256: `c05463733323609f0b4b5d32e7ee0269b8f951bd12d924cc155b0f6c7c2548ff`

## 1. Purpose

Provides complete unit and regression coverage for the `enrich_road_proximity` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `from copy import deepcopy`
- `from dataclasses import FrozenInstanceError`
- `from pathlib import Path`
- `from typing import Any, cast`
- `from unittest.mock import patch`

### Third-party packages

- `import geopandas as gpd`
- `import pandas as pd`
- `import pytest`
- `from geopandas.testing import assert_geodataframe_equal`
- `from pandas.testing import assert_frame_equal`
- `from shapely.geometry import LineString, MultiPolygon, Point, Polygon`

### Internal LandScout imports

- `from landscout import stages`
- `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    load_ign_bdtopo_source_config,
)`
- `from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationError,
    IgnRoadVehicleProxyApplicationResult,
)`
- `from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProximityError,
    enrich_parcel_road_proximity,
)`
- `from landscout.stages.road_vehicle_proxy_policy import (
    load_ign_road_vehicle_proxy_policy,
)`

## 4. Contract taxonomy

### A. Python constants

#### `SOURCE_CONFIG`

```python
SOURCE_CONFIG = load_ign_bdtopo_source_config()
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_apply_road_vehicle_proxy_policy.py::_apply` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_wrong_source_type_has_controlled_error` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_malformed_policy_path_has_controlled_error` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_complete_normalization_is_invoked_exactly_once` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_normalization_failure_stops_policy_loading` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_object_is_not_mutated` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_valid_geometry_status_with_unsupported_geometry_is_not_repaired` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_policy_path_must_be_path_or_none` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_public_coverage_proximity_failure_stops_coverage_loading` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_caller_provided_proximity_and_coverage_are_not_public_inputs` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_polygonal_coverage_geometry_is_accepted` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_invalid_coverage_geometry_is_rejected` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_strict_geometric_boundary_proof` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_outside_crossing_or_touching_parcel_is_conservative` (value argument/reference).

#### `POLICY_PATH`

```python
POLICY_PATH = Path("configs/access/ign_bdtopo_vehicle_proxy_policy.yaml")
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_policy_path_must_be_path_or_none` (value argument/reference), `tests/unit/test_bess_planning_feature_policy.py::_checked_in_policy_result` (value argument/reference), `tests/unit/test_bess_planning_feature_policy.py::test_checked_in_policy_pins_all_twelve_exact_muret_decisions` (value argument/reference), `tests/unit/test_bess_planning_feature_policy.py::test_checked_in_policy_complete_snapshot_is_immutable` (value argument/reference), `tests/unit/test_bess_planning_feature_policy.py::test_profile_v1_snapshot_detects_policy_text_drift` (value argument/reference), `tests/unit/test_bess_planning_feature_policy.py::test_profile_v1_snapshot_detects_source_lock_drift` (value argument/reference), `tests/unit/test_road_vehicle_proxy_policy.py::test_checked_in_policy_hash_binds_exact_file_bytes` (value argument/reference).

#### `ELIGIBLE_CLASSES`

```python
ELIGIBLE_CLASSES = (
    "GENERAL_VEHICLE_PROXY",
    "LIMITED_VEHICLE_PROXY",
    "RESTRICTED_REVIEW",
    "NOT_GENERAL_VEHICLE_PROXY",
    "UNKNOWN_REVIEW",
)
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_assess_road_proximity_coverage.py::_proximity` (value argument/reference), `tests/unit/test_enrich_road_proximity.py::test_output_shape_columns_and_order_are_deterministic` (value argument/reference).

#### `ALL_CLASSES`

```python
ALL_CLASSES = (
    "GENERAL_VEHICLE_PROXY",
    "LIMITED_VEHICLE_PROXY",
    "RESTRICTED_REVIEW",
    "NOT_GENERAL_VEHICLE_PROXY",
    "NOT_DISTANCE_PROXY",
    "UNKNOWN_REVIEW",
)
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `SELECTED_COLUMNS`

```python
SELECTED_COLUMNS = (
    "nearest_road_proxy_distance_m",
    "nearest_road_feature_id",
    "nearest_source_feature_id",
    "nearest_road_tie_count",
    "nearest_road_primary_rule",
    "nearest_road_rule_trace_json",
    "nearest_road_unknown_fields_json",
    "nearest_road_toll_evidence",
    "nearest_nature_raw",
    "nearest_importance_raw",
    "nearest_asset_status_raw",
    "nearest_private_raw",
    "nearest_light_vehicle_access_raw",
    "nearest_carriageway_width_raw",
    "nearest_closure_period_raw",
    "nearest_restriction_nature_raw",
    "nearest_source_layer",
    "nearest_source_department_code",
    "nearest_source_edition",
    "nearest_source_archive_sha256",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `tests/unit/test_enrich_road_proximity.py::test_empty_eligible_class_emits_null_row_per_parcel` (value argument/reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

### `_metric_parcels`

**Exact signature**

```python
def _metric_parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
```

**Purpose**

Private `test` helper for metric parcels; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
gpd.GeoDataFrame({'parcel_id': ids, 'source_value': list(range(count))}, geometry=values, crs='EPSG:2154', index=frame_index)
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

- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` via `_metric_parcels`.
- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_validate_parcel_summaries` via `_metric_parcels`.
- direct call or construction: `src/landscout/stages/enrich_planning_features.py::intersect_parcels_with_gpu_planning_features` via `_metric_parcels`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::intersect_parcels_with_gpu_zoning` via `_metric_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::_parcels` via `_metric_parcels`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::_parcels` via `_metric_parcels`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_missing_or_wrong_storage_crs_is_rejected` via `_metric_parcels`.

**Complete source-ordered implementation**

```python
def _metric_parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
    values = geometries or [
        Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])
    ]
    count = len(values)
    ids = identifiers or [f"PARCEL-{position + 1}" for position in range(count)]
    frame_index = index or [100 + position for position in range(count)]
    return gpd.GeoDataFrame(
        {"parcel_id": ids, "source_value": list(range(count))},
        geometry=values,
        crs="EPSG:2154",
        index=frame_index,
    )
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
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
```

**Purpose**

Private `test` helper for parcels; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
_metric_parcels(geometries, identifiers=identifiers, index=index).to_crs('EPSG:4326')
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `_metric_parcels(geometries, identifiers=identifiers, index=index).to_crs`.
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
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
    return _metric_parcels(
        geometries, identifiers=identifiers, index=index
    ).to_crs("EPSG:4326")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_road_row`

**Exact signature**

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

Private `test` helper for road row; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
{'road_feature_id': identifier, 'source_feature_id': f'SOURCE-{identifier}', 'geometry_status': 'VALID', 'nature_raw': 'Route à 1 chaussée', 'importance_raw': '2', 'asset_status_raw': 'En service', 'private_raw': 0.0, 'light_vehicle_access_raw': 'Libre', 'carriageway_width_raw': 7.0, 'closure_period_raw': None, 'restriction_nature_raw': None, 'source_layer': 'troncon_de_route', 'source_department_code': '31', 'source_edition': '2026-06-15', 'source_archive_sha256': 'a' * 64, 'road_proxy_primary_rule': primary_rule, 'road_proxy_class': road_class, 'road_proxy_rule_trace_json': f'["{primary_rule}"]', 'road_proxy_unknown_fields_json': '[]', 'road_proxy_toll_evidence': False, 'road_proxy_policy_id': policy.policy_id, 'road_proxy_policy_schema_version': policy.schema_version, 'road_proxy_policy_config_sha256': policy.config_sha256, 'road_proxy_policy_scope': policy.scope, 'road_proxy_heavy_vehicle_access': policy.heavy_vehicle_access, 'geometry': geometry or LineString([(x, -20), (x, 30)])}
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

- direct call or construction: `tests/unit/test_enrich_road_proximity.py::_roads` via `_road_row`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_intersecting_or_touching_road_has_zero_distance` via `_road_row`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_exact_tie_counts_two_and_lexical_id_wins` via `_road_row`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_tie_winner_is_independent_of_source_order` via `_road_row`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_unequal_distance_wins_regardless_of_identifier` via `_road_row`.

**Complete source-ordered implementation**

```python
def _road_row(
    road_class: str,
    x: float,
    *,
    identifier: str,
    geometry: object | None = None,
) -> dict[str, object]:
    policy = load_ign_road_vehicle_proxy_policy()
    primary_rule = {
        "GENERAL_VEHICLE_PROXY": "OPEN_OR_TOLL",
        "LIMITED_VEHICLE_PROXY": "LIMITED_NATURE",
        "RESTRICTED_REVIEW": "PRIVATE_ROAD",
        "NOT_GENERAL_VEHICLE_PROXY": "PHYSICALLY_IMPOSSIBLE",
        "NOT_DISTANCE_PROXY": "FICTITIOUS_GEOMETRY",
        "UNKNOWN_REVIEW": "UNKNOWN",
    }[road_class]
    return {
        "road_feature_id": identifier,
        "source_feature_id": f"SOURCE-{identifier}",
        "geometry_status": "VALID",
        "nature_raw": "Route à 1 chaussée",
        "importance_raw": "2",
        "asset_status_raw": "En service",
        "private_raw": 0.0,
        "light_vehicle_access_raw": "Libre",
        "carriageway_width_raw": 7.0,
        "closure_period_raw": None,
        "restriction_nature_raw": None,
        "source_layer": "troncon_de_route",
        "source_department_code": "31",
        "source_edition": "2026-06-15",
        "source_archive_sha256": "a" * 64,
        "road_proxy_primary_rule": primary_rule,
        "road_proxy_class": road_class,
        "road_proxy_rule_trace_json": f'["{primary_rule}"]',
        "road_proxy_unknown_fields_json": "[]",
        "road_proxy_toll_evidence": False,
        "road_proxy_policy_id": policy.policy_id,
        "road_proxy_policy_schema_version": policy.schema_version,
        "road_proxy_policy_config_sha256": policy.config_sha256,
        "road_proxy_policy_scope": policy.scope,
        "road_proxy_heavy_vehicle_access": policy.heavy_vehicle_access,
        "geometry": geometry or LineString([(x, -20), (x, 30)]),
    }
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_roads`

**Exact signature**

```python
def _roads(
    rows: list[dict[str, object]] | None = None,
) -> gpd.GeoDataFrame:
```

**Purpose**

Private `test` helper for roads; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
gpd.GeoDataFrame(values, geometry='geometry', crs='EPSG:2154')
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

- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::_source` via `_roads`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::_row` via `_roads`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_malformed_policy_path_has_controlled_error` via `_roads`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_complete_normalization_is_invoked_exactly_once` via `_roads`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_normalized_facts_rows_index_crs_and_geometry_are_preserved` via `_roads`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_object_is_not_mutated` via `_roads`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_unknown_geometry_status_is_rejected` via `_roads`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_policy_lineage_is_exact_on_every_row` via `_roads`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_result_is_frozen_and_contains_no_unsafe_claim_vocabulary` via `_roads`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_valid_geometry_status_with_unsupported_geometry_is_not_repaired` via `_roads`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::_source` via `_roads`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::_enrich` via `_roads`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_application_stage_is_invoked_exactly_once` via `_roads`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_independent_policy_sha_mismatch_is_rejected` via `_roads`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_application_roads_must_be_geodataframe` via `_roads`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_duplicate_road_feature_id_is_rejected` via `_roads`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_unknown_road_proxy_class_is_rejected` via `_roads`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_missing_road_policy_lineage_is_rejected` via `_roads`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_eligible_class_requires_valid_geometry_status` via `_roads`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_eligible_class_rejects_unsupported_geometry` via `_roads`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_not_distance_road_is_counted_but_never_indexed` via `_roads`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_intersecting_or_touching_road_has_zero_distance` via `_roads`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_exact_tie_counts_two_and_lexical_id_wins` via `_roads`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_tie_winner_is_independent_of_source_order` via `_roads`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_unequal_distance_wins_regardless_of_identifier` via `_roads`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_empty_eligible_class_emits_null_row_per_parcel` via `_roads`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_parcels_and_road_application_are_not_mutated` via `_roads`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_selected_rows_belong_to_requested_class` via `_roads`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_policy_sha_mismatch_does_not_construct_spatial_index` via `_roads`.

**Complete source-ordered implementation**

```python
def _roads(
    rows: list[dict[str, object]] | None = None,
) -> gpd.GeoDataFrame:
    values = rows or [
        _road_row(
            "GENERAL_VEHICLE_PROXY", 20, identifier="ROAD-GENERAL"
        ),
        _road_row(
            "LIMITED_VEHICLE_PROXY", 30, identifier="ROAD-LIMITED"
        ),
        _road_row("RESTRICTED_REVIEW", 15, identifier="ROAD-RESTRICTED"),
        _road_row(
            "NOT_GENERAL_VEHICLE_PROXY", 40, identifier="ROAD-NOT-GENERAL"
        ),
        _road_row("NOT_DISTANCE_PROXY", 11, identifier="ROAD-NOT-DISTANCE"),
        _road_row("UNKNOWN_REVIEW", 50, identifier="ROAD-UNKNOWN"),
    ]
    return gpd.GeoDataFrame(values, geometry="geometry", crs="EPSG:2154")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_source`

**Exact signature**

```python
def _source() -> IgnBdTopoRoadData:
```

**Purpose**

Private `test` helper for source; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `IgnBdTopoRoadData`.
- Every observed return expression is reproduced without truncation:
```python
IgnBdTopoRoadData(extraction=cast(Any, None), road_segments=_roads(), road_segments_summary=cast(Any, None))
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

- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::_apply` via `_source`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_wrong_source_config_type_has_controlled_error` via `_source`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_malformed_policy_path_has_controlled_error` via `_source`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_complete_normalization_is_invoked_exactly_once` via `_source`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_normalization_failure_stops_policy_loading` via `_source`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_object_is_not_mutated` via `_source`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_valid_geometry_status_with_unsupported_geometry_is_not_repaired` via `_source`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_policy_path_must_be_path_or_none` via `_source`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_config_is_exact_pydantic_type` via `_source`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::_enrich` via `_source`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_wrong_parcel_type_has_controlled_error` via `_source`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_wrong_source_config_type_has_controlled_error` via `_source`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_wrong_policy_path_type_has_controlled_error` via `_source`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_application_stage_is_invoked_exactly_once` via `_source`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_application_failure_stops_proximity` via `_source`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_malformed_policy_stops_before_application` via `_source`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_wrong_application_result_type_is_rejected` via `_source`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_application_roads_must_be_geodataframe` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_road_normalization_reproduces_configured_logical_layer` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_valid_linestring_normalization_has_exact_schema_identity_and_lineage` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_valid_multilinestring_is_preserved` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_z_coordinates_are_preserved_exactly` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_row_count_order_geometry_and_range_index_are_preserved` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_raw_access_and_restriction_values_are_copied_without_interpretation` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_every_raw_field_preserves_source_values_nulls_and_dtype` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_missing_required_source_field_is_rejected` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_null_or_empty_cleabs_is_rejected` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_unsafe_cleabs_is_rejected` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_duplicate_cleabs_is_rejected` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_wrong_or_missing_road_crs_is_rejected` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_wrong_archive_identity_is_rejected` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_wrong_source_spatial_role_is_rejected` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_summary_row_count_mismatch_is_rejected` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_road_summary_requires_strict_structural_types` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_road_archive_sha256_requires_canonical_lowercase` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_summary_crs_mismatch_is_rejected` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_forged_ordered_summary_schema_is_rejected` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_road_source_rejects_physical_role_collision` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_road_source_rejects_duplicate_layer_inventory` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_summary_geometry_facts_mismatch_is_rejected` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_summary_layer_must_exist_in_extraction_inventory` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_summary_layer_and_logical_name_must_be_exact` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_valid_unsupported_geometry_type_is_rejected` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_null_empty_and_invalid_geometry_are_preserved_with_status` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_normalization_does_not_mutate_input` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_high_level_rejects_coordinated_road_frame_and_summary_forgery` via `_source`.

**Complete source-ordered implementation**

```python
def _source() -> IgnBdTopoRoadData:
    return IgnBdTopoRoadData(
        extraction=cast(Any, None),
        road_segments=_roads(),
        road_segments_summary=cast(Any, None),
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_enrich`

**Exact signature**

```python
def _enrich(
    parcels: gpd.GeoDataFrame | None = None,
    roads: gpd.GeoDataFrame | None = None,
    *,
    policy_path: Path | None = None,
) -> ParcelRoadProximityResult:
```

**Purpose**

Copies input evidence and adds enrich; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `ParcelRoadProximityResult`.
- Every observed return expression is reproduced without truncation:
```python
enrich_parcel_road_proximity(parcels if parcels is not None else _parcels(), _source(), SOURCE_CONFIG, policy_path)
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

- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_independent_policy_sha_mismatch_is_rejected` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_invalid_parcel_identity_is_rejected` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_duplicate_parcel_id_is_rejected` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_duplicate_parcel_columns_are_rejected` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_missing_or_inactive_geometry_is_rejected` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_missing_or_wrong_storage_crs_is_rejected` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_wrong_parcel_geometry_kind_is_rejected` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_bad_parcel_geometry_is_rejected` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_polygon_and_multipolygon_are_accepted` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_duplicate_road_feature_id_is_rejected` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_unknown_road_proxy_class_is_rejected` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_missing_road_policy_lineage_is_rejected` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_eligible_class_requires_valid_geometry_status` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_eligible_class_rejects_unsupported_geometry` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_not_distance_road_is_counted_but_never_indexed` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_known_polygon_to_line_distance_is_ten_metres` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_intersecting_or_touching_road_has_zero_distance` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_distance_uses_full_polygon_not_centroid` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_storage_geometry_stays_epsg4326_while_distance_is_metric` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_each_eligible_class_has_independent_distance` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_near_not_distance_road_cannot_change_general_distance` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_single_nearest_road_has_tie_count_one` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_exact_tie_counts_two_and_lexical_id_wins` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_tie_winner_is_independent_of_source_order` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_unequal_distance_wins_regardless_of_identifier` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_empty_eligible_class_emits_null_row_per_parcel` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_output_shape_columns_and_order_are_deterministic` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_class_coverage_is_complete_and_strict` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_selected_road_evidence_and_lineage_are_exact` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_parcels_and_road_application_are_not_mutated` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::_corrupt_nearest_output` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_result_dataclasses_are_frozen` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_no_business_decision_columns_or_implementation_exist` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_result_parcel_frame_is_an_independent_copy` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_class_proximity_is_plain_dataframe` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_selected_rows_belong_to_requested_class` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_policy_sha_mismatch_does_not_construct_spatial_index` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_matched_output_dtypes_are_stable` via `_enrich`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_parcel_preservation_uses_exact_non_geometry_values` via `_enrich`.

**Complete source-ordered implementation**

```python
def _enrich(
    parcels: gpd.GeoDataFrame | None = None,
    roads: gpd.GeoDataFrame | None = None,
    *,
    policy_path: Path | None = None,
) -> ParcelRoadProximityResult:
    application = IgnRoadVehicleProxyApplicationResult(
        roads if roads is not None else _roads()
    )
    with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
        return_value=application,
    ):
        return enrich_parcel_road_proximity(
            parcels if parcels is not None else _parcels(),
            _source(),
            SOURCE_CONFIG,
            policy_path,
        )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_row`

**Exact signature**

```python
def _row(result: ParcelRoadProximityResult, road_class: str) -> pd.Series:
```

**Purpose**

Private `test` helper for row; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.Series`.
- Every observed return expression is reproduced without truncation:
```python
result.class_proximity.loc[result.class_proximity['road_proxy_class'].eq(road_class)].iloc[0]
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

- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_non_valid_geometry_uses_technical_gate` via `_row`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_each_policy_rule_selects_approved_outcome` via `_row`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_policy_precedence_conflicts_select_first_rule` via `_row`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_boolean_like_source_values_are_parsed_without_coercion` via `_row`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_unknown_critical_vocabulary_never_uses_general_fallback` via `_row`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_width_contract` via `_row`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_optional_restriction_source_contract` via `_row`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_every_configured_known_restriction_is_applied` via `_row`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_general_fallback_requires_complete_positive_evidence_and_tracks_toll` via `_row`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_open_access_does_not_hide_unresolved_evidence` via `_row`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_trace_is_complete_unique_and_in_policy_order` via `_row`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_known_higher_rule_remains_primary_while_unknown_is_traced` via `_row`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_unknown_fields_trace_is_fixed_and_deterministic` via `_row`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_known_polygon_to_line_distance_is_ten_metres` via `_row`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_intersecting_or_touching_road_has_zero_distance` via `_row`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_distance_uses_full_polygon_not_centroid` via `_row`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_storage_geometry_stays_epsg4326_while_distance_is_metric` via `_row`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_each_eligible_class_has_independent_distance` via `_row`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_near_not_distance_road_cannot_change_general_distance` via `_row`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_single_nearest_road_has_tie_count_one` via `_row`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_exact_tie_counts_two_and_lexical_id_wins` via `_row`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_tie_winner_is_independent_of_source_order` via `_row`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_unequal_distance_wins_regardless_of_identifier` via `_row`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_selected_road_evidence_and_lineage_are_exact` via `_row`.

**Complete source-ordered implementation**

```python
def _row(result: ParcelRoadProximityResult, road_class: str) -> pd.Series:
    return result.class_proximity.loc[
        result.class_proximity["road_proxy_class"].eq(road_class)
    ].iloc[0]
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_api_exports_only_stable_symbols`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
import landscout.stages.enrich_road_proximity as module
expected = {
        "RoadProximityError",
        "RoadProxyClassCoverage",
        "ParcelRoadProximityResult",
        "enrich_parcel_road_proximity",
    }
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert set(module.__all__) == expected
assert expected <= set(stages.__all__)
assert all(hasattr(stages, symbol) for symbol in expected)
assert not hasattr(stages, "_nearest_class_rows")
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_public_api_exports_only_stable_symbols() -> None:
    import landscout.stages.enrich_road_proximity as module

    expected = {
        "RoadProximityError",
        "RoadProxyClassCoverage",
        "ParcelRoadProximityResult",
        "enrich_parcel_road_proximity",
    }
    assert set(module.__all__) == expected
    assert expected <= set(stages.__all__)
    assert all(hasattr(stages, symbol) for symbol in expected)
    assert not hasattr(stages, "_nearest_class_rows")
```

### `test_wrong_parcel_type_has_controlled_error`

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
with pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(
            cast(Any, pd.DataFrame()), _source(), SOURCE_CONFIG
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_wrong_parcel_type_has_controlled_error() -> None:
    with pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(
            cast(Any, pd.DataFrame()), _source(), SOURCE_CONFIG
        )
```

### `test_wrong_road_source_type_has_controlled_error`

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
with pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(
            _parcels(), cast(Any, object()), SOURCE_CONFIG
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_wrong_road_source_type_has_controlled_error() -> None:
    with pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(
            _parcels(), cast(Any, object()), SOURCE_CONFIG
        )
```

### `test_wrong_source_config_type_has_controlled_error`

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
with pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(
            _parcels(), _source(), cast(Any, object())
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_wrong_source_config_type_has_controlled_error() -> None:
    with pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(
            _parcels(), _source(), cast(Any, object())
        )
```

### `test_wrong_policy_path_type_has_controlled_error`

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
with pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(
            _parcels(), _source(), SOURCE_CONFIG, cast(Any, "policy.yaml")
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_wrong_policy_path_type_has_controlled_error() -> None:
    with pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(
            _parcels(), _source(), SOURCE_CONFIG, cast(Any, "policy.yaml")
        )
```

### `test_application_stage_is_invoked_exactly_once`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source_application.assert_called_once()
```

**Action**

```python
application = IgnRoadVehicleProxyApplicationResult(_roads())
with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
        return_value=application,
    ) as source_application:
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Pins the exact framework interaction and outcome reproduced in the complete test source.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_application_stage_is_invoked_exactly_once() -> None:
    application = IgnRoadVehicleProxyApplicationResult(_roads())
    with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
        return_value=application,
    ) as source_application:
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)

    source_application.assert_called_once()
```

### `test_application_failure_stops_proximity`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
spatial_index.assert_not_called()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
        side_effect=IgnRoadVehicleProxyApplicationError("bad source"),
    ), patch(
        "landscout.stages.enrich_road_proximity.STRtree"
    ) as spatial_index, pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_application_failure_stops_proximity() -> None:
    with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
        side_effect=IgnRoadVehicleProxyApplicationError("bad source"),
    ), patch(
        "landscout.stages.enrich_road_proximity.STRtree"
    ) as spatial_index, pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)

    spatial_index.assert_not_called()
```

### `test_malformed_policy_stops_before_application`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
path = tmp_path / "policy.yaml"
path.write_text("policy_id: [", encoding="utf-8")
source_application.assert_not_called()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy"
    ) as source_application, pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG, path)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_malformed_policy_stops_before_application(tmp_path: Path) -> None:
    path = tmp_path / "policy.yaml"
    path.write_text("policy_id: [", encoding="utf-8")

    with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy"
    ) as source_application, pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG, path)

    source_application.assert_not_called()
```

### `test_independent_policy_sha_mismatch_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
roads = _roads()
roads["road_proxy_policy_config_sha256"] = "b" * 64
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RoadProximityError, match="policy|SHA|lineage"):
        _enrich(roads=roads)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_independent_policy_sha_mismatch_is_rejected() -> None:
    roads = _roads()
    roads["road_proxy_policy_config_sha256"] = "b" * 64

    with pytest.raises(RoadProximityError, match="policy|SHA|lineage"):
        _enrich(roads=roads)
```

### `test_invalid_parcel_identity_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `message`, `mutation`.

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
with pytest.raises(RoadProximityError, match=message):
        _enrich(parcels=mutation(_parcels()))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_invalid_parcel_identity_is_rejected(
    mutation: Any, message: str
) -> None:
    with pytest.raises(RoadProximityError, match=message):
        _enrich(parcels=mutation(_parcels()))
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
with pytest.raises(RoadProximityError, match="unique"):
        _enrich(parcels=parcels)
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

    with pytest.raises(RoadProximityError, match="unique"):
        _enrich(parcels=parcels)
```

### `test_duplicate_parcel_columns_are_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels()
duplicated = gpd.GeoDataFrame(
        pd.concat([parcels, parcels[["parcel_id"]]], axis=1),
        geometry="geometry",
        crs=parcels.crs,
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RoadProximityError, match="duplicate"):
        _enrich(parcels=duplicated)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_duplicate_parcel_columns_are_rejected() -> None:
    parcels = _parcels()
    duplicated = gpd.GeoDataFrame(
        pd.concat([parcels, parcels[["parcel_id"]]], axis=1),
        geometry="geometry",
        crs=parcels.crs,
    )

    with pytest.raises(RoadProximityError, match="duplicate"):
        _enrich(parcels=duplicated)
```

### `test_missing_or_inactive_geometry_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels()
missing = parcels.drop(columns="geometry")
inactive = parcels.assign(other_geometry=parcels.geometry).set_geometry(
        "other_geometry"
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RoadProximityError, match="geometry"):
        _enrich(parcels=missing)
with pytest.raises(RoadProximityError, match="active"):
        _enrich(parcels=inactive)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_missing_or_inactive_geometry_is_rejected() -> None:
    parcels = _parcels()
    missing = parcels.drop(columns="geometry")
    inactive = parcels.assign(other_geometry=parcels.geometry).set_geometry(
        "other_geometry"
    )

    with pytest.raises(RoadProximityError, match="geometry"):
        _enrich(parcels=missing)
    with pytest.raises(RoadProximityError, match="active"):
        _enrich(parcels=inactive)
```

### `test_missing_or_wrong_storage_crs_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
missing = _parcels().set_crs(None, allow_override=True)
wrong = _metric_parcels()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RoadProximityError, match="CRS"):
        _enrich(parcels=missing)
with pytest.raises(RoadProximityError, match="4326"):
        _enrich(parcels=wrong)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_missing_or_wrong_storage_crs_is_rejected() -> None:
    missing = _parcels().set_crs(None, allow_override=True)
    wrong = _metric_parcels()

    with pytest.raises(RoadProximityError, match="CRS"):
        _enrich(parcels=missing)
    with pytest.raises(RoadProximityError, match="4326"):
        _enrich(parcels=wrong)
```

### `test_wrong_parcel_geometry_kind_is_rejected`

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
with pytest.raises(RoadProximityError, match="Polygon|MultiPolygon"):
        _enrich(parcels=_parcels([geometry]))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_wrong_parcel_geometry_kind_is_rejected(geometry: object) -> None:
    with pytest.raises(RoadProximityError, match="Polygon|MultiPolygon"):
        _enrich(parcels=_parcels([geometry]))
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
with pytest.raises(RoadProximityError, match=message):
        _enrich(parcels=_parcels([geometry]))
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_bad_parcel_geometry_is_rejected(
    geometry: object, message: str
) -> None:
    with pytest.raises(RoadProximityError, match=message):
        _enrich(parcels=_parcels([geometry]))
```

### `test_polygon_and_multipolygon_are_accepted`

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
assert len(_enrich(parcels=_parcels([geometry])).parcels) == 1
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_polygon_and_multipolygon_are_accepted(geometry: object) -> None:
    assert len(_enrich(parcels=_parcels([geometry])).parcels) == 1
```

### `test_wrong_application_result_type_is_rejected`

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
with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
        return_value=object(),
    ), pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_wrong_application_result_type_is_rejected() -> None:
    with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
        return_value=object(),
    ), pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)
```

### `test_application_roads_must_be_geodataframe`

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
application = IgnRoadVehicleProxyApplicationResult(
        cast(Any, pd.DataFrame(_roads().drop(columns="geometry")))
    )
```

**Expected result**

```python
with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
        return_value=application,
    ), pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_application_roads_must_be_geodataframe() -> None:
    application = IgnRoadVehicleProxyApplicationResult(
        cast(Any, pd.DataFrame(_roads().drop(columns="geometry")))
    )
    with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
        return_value=application,
    ), pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)
```

### `test_duplicate_road_feature_id_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
roads = _roads()
roads.loc[1, "road_feature_id"] = roads.loc[0, "road_feature_id"]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RoadProximityError, match="unique"):
        _enrich(roads=roads)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_duplicate_road_feature_id_is_rejected() -> None:
    roads = _roads()
    roads.loc[1, "road_feature_id"] = roads.loc[0, "road_feature_id"]

    with pytest.raises(RoadProximityError, match="unique"):
        _enrich(roads=roads)
```

### `test_unknown_road_proxy_class_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
roads = _roads()
roads.loc[0, "road_proxy_class"] = "INVENTED"
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RoadProximityError, match="class"):
        _enrich(roads=roads)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_unknown_road_proxy_class_is_rejected() -> None:
    roads = _roads()
    roads.loc[0, "road_proxy_class"] = "INVENTED"

    with pytest.raises(RoadProximityError, match="class"):
        _enrich(roads=roads)
```

### `test_missing_road_policy_lineage_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`.

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
with pytest.raises(RoadProximityError, match="column|lineage"):
        _enrich(roads=_roads().drop(columns=column))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_missing_road_policy_lineage_is_rejected(column: str) -> None:
    with pytest.raises(RoadProximityError, match="column|lineage"):
        _enrich(roads=_roads().drop(columns=column))
```

### `test_eligible_class_requires_valid_geometry_status`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `status`.

**Setup**

```python
roads = _roads()
roads.loc[0, "geometry_status"] = status
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RoadProximityError, match="VALID"):
        _enrich(roads=roads)
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_eligible_class_requires_valid_geometry_status(status: str) -> None:
    roads = _roads()
    roads.loc[0, "geometry_status"] = status

    with pytest.raises(RoadProximityError, match="VALID"):
        _enrich(roads=roads)
```

### `test_eligible_class_rejects_unsupported_geometry`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
roads = _roads()
roads.at[0, "geometry"] = Point(20, 0)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RoadProximityError, match="LineString|geometry"):
        _enrich(roads=roads)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_eligible_class_rejects_unsupported_geometry() -> None:
    roads = _roads()
    roads.at[0, "geometry"] = Point(20, 0)

    with pytest.raises(RoadProximityError, match="LineString|geometry"):
        _enrich(roads=roads)
```

### `test_not_distance_road_is_counted_but_never_indexed`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
roads = _roads()
roads.loc[
        roads["road_proxy_class"].eq("NOT_DISTANCE_PROXY"), "geometry_status"
    ] = "INVALID"
result = _enrich(roads=roads)
coverage = {item.road_proxy_class: item for item in result.class_coverage}
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert coverage["NOT_DISTANCE_PROXY"].feature_count == 1
assert not coverage["NOT_DISTANCE_PROXY"].distance_eligible
assert "NOT_DISTANCE_PROXY" not in set(result.class_proximity.road_proxy_class)
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_not_distance_road_is_counted_but_never_indexed() -> None:
    roads = _roads()
    roads.loc[
        roads["road_proxy_class"].eq("NOT_DISTANCE_PROXY"), "geometry_status"
    ] = "INVALID"
    result = _enrich(roads=roads)
    coverage = {item.road_proxy_class: item for item in result.class_coverage}

    assert coverage["NOT_DISTANCE_PROXY"].feature_count == 1
    assert not coverage["NOT_DISTANCE_PROXY"].distance_eligible
    assert "NOT_DISTANCE_PROXY" not in set(result.class_proximity.road_proxy_class)
```

### `test_known_polygon_to_line_distance_is_ten_metres`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _enrich()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert _row(
        result, "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_known_polygon_to_line_distance_is_ten_metres() -> None:
    result = _enrich()

    assert _row(
        result, "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)
```

### `test_intersecting_or_touching_road_has_zero_distance`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `x`.

**Setup**

```python
roads = _roads(
        [_road_row("GENERAL_VEHICLE_PROXY", x, identifier="ROAD-GENERAL")]
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert _row(
        _enrich(roads=roads), "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m == pytest.approx(0.0, abs=1e-5)
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_intersecting_or_touching_road_has_zero_distance(x: float) -> None:
    roads = _roads(
        [_road_row("GENERAL_VEHICLE_PROXY", x, identifier="ROAD-GENERAL")]
    )

    assert _row(
        _enrich(roads=roads), "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m == pytest.approx(0.0, abs=1e-5)
```

### `test_distance_uses_full_polygon_not_centroid`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
distance = _row(
        _enrich(), "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert distance == pytest.approx(10.0, abs=1e-5)
assert distance != pytest.approx(15.0, abs=1e-5)
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_distance_uses_full_polygon_not_centroid() -> None:
    distance = _row(
        _enrich(), "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m

    assert distance == pytest.approx(10.0, abs=1e-5)
    assert distance != pytest.approx(15.0, abs=1e-5)
```

### `test_storage_geometry_stays_epsg4326_while_distance_is_metric`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels()
before = deepcopy(parcels)
result = _enrich(parcels=parcels)
assert_geodataframe_equal(result.parcels, before)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert result.parcels.crs == parcels.crs
assert result.parcels.crs.to_epsg() == 4326
assert _row(
        result, "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_storage_geometry_stays_epsg4326_while_distance_is_metric() -> None:
    parcels = _parcels()
    before = deepcopy(parcels)
    result = _enrich(parcels=parcels)

    assert result.parcels.crs == parcels.crs
    assert result.parcels.crs.to_epsg() == 4326
    assert _row(
        result, "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)
    assert_geodataframe_equal(result.parcels, before)
```

### `test_each_eligible_class_has_independent_distance`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _enrich()
distances = {
        road_class: _row(result, road_class).nearest_road_proxy_distance_m
        for road_class in ELIGIBLE_CLASSES
    }
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert distances == pytest.approx(
        {
            "GENERAL_VEHICLE_PROXY": 10.0,
            "LIMITED_VEHICLE_PROXY": 20.0,
            "RESTRICTED_REVIEW": 5.0,
            "NOT_GENERAL_VEHICLE_PROXY": 30.0,
            "UNKNOWN_REVIEW": 40.0,
        },
        abs=1e-5,
    )
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_each_eligible_class_has_independent_distance() -> None:
    result = _enrich()
    distances = {
        road_class: _row(result, road_class).nearest_road_proxy_distance_m
        for road_class in ELIGIBLE_CLASSES
    }

    assert distances == pytest.approx(
        {
            "GENERAL_VEHICLE_PROXY": 10.0,
            "LIMITED_VEHICLE_PROXY": 20.0,
            "RESTRICTED_REVIEW": 5.0,
            "NOT_GENERAL_VEHICLE_PROXY": 30.0,
            "UNKNOWN_REVIEW": 40.0,
        },
        abs=1e-5,
    )
```

### `test_near_not_distance_road_cannot_change_general_distance`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _enrich()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert _row(
        result, "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)
assert "ROAD-NOT-DISTANCE" not in set(
        result.class_proximity.nearest_road_feature_id.dropna()
    )
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_near_not_distance_road_cannot_change_general_distance() -> None:
    result = _enrich()

    assert _row(
        result, "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)
    assert "ROAD-NOT-DISTANCE" not in set(
        result.class_proximity.nearest_road_feature_id.dropna()
    )
```

### `test_single_nearest_road_has_tie_count_one`

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
assert _row(
        _enrich(), "GENERAL_VEHICLE_PROXY"
    ).nearest_road_tie_count == 1
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_single_nearest_road_has_tie_count_one() -> None:
    assert _row(
        _enrich(), "GENERAL_VEHICLE_PROXY"
    ).nearest_road_tie_count == 1
```

### `test_exact_tie_counts_two_and_lexical_id_wins`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
roads = _roads(
        [
            _road_row("GENERAL_VEHICLE_PROXY", -10, identifier="Z-ROAD"),
            _road_row("GENERAL_VEHICLE_PROXY", 20, identifier="A-ROAD"),
        ]
    )
row = _row(_enrich(roads=roads), "GENERAL_VEHICLE_PROXY")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert row.nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)
assert row.nearest_road_tie_count == 2
assert row.nearest_road_feature_id == "A-ROAD"
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_exact_tie_counts_two_and_lexical_id_wins() -> None:
    roads = _roads(
        [
            _road_row("GENERAL_VEHICLE_PROXY", -10, identifier="Z-ROAD"),
            _road_row("GENERAL_VEHICLE_PROXY", 20, identifier="A-ROAD"),
        ]
    )
    row = _row(_enrich(roads=roads), "GENERAL_VEHICLE_PROXY")

    assert row.nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)
    assert row.nearest_road_tie_count == 2
    assert row.nearest_road_feature_id == "A-ROAD"
```

### `test_tie_winner_is_independent_of_source_order`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
roads = _roads(
        [
            _road_row("GENERAL_VEHICLE_PROXY", -10, identifier="Z-ROAD"),
            _road_row("GENERAL_VEHICLE_PROXY", 20, identifier="A-ROAD"),
        ]
    )
forward = _row(_enrich(roads=roads), "GENERAL_VEHICLE_PROXY")
reverse = _row(
        _enrich(roads=roads.iloc[::-1].reset_index(drop=True)),
        "GENERAL_VEHICLE_PROXY",
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert forward.nearest_road_feature_id == "A-ROAD"
assert reverse.nearest_road_feature_id == "A-ROAD"
assert forward.nearest_road_tie_count == reverse.nearest_road_tie_count == 2
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_tie_winner_is_independent_of_source_order() -> None:
    roads = _roads(
        [
            _road_row("GENERAL_VEHICLE_PROXY", -10, identifier="Z-ROAD"),
            _road_row("GENERAL_VEHICLE_PROXY", 20, identifier="A-ROAD"),
        ]
    )
    forward = _row(_enrich(roads=roads), "GENERAL_VEHICLE_PROXY")
    reverse = _row(
        _enrich(roads=roads.iloc[::-1].reset_index(drop=True)),
        "GENERAL_VEHICLE_PROXY",
    )

    assert forward.nearest_road_feature_id == "A-ROAD"
    assert reverse.nearest_road_feature_id == "A-ROAD"
    assert forward.nearest_road_tie_count == reverse.nearest_road_tie_count == 2
```

### `test_unequal_distance_wins_regardless_of_identifier`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
roads = _roads(
        [
            _road_row("GENERAL_VEHICLE_PROXY", 20, identifier="Z-NEAR"),
            _road_row("GENERAL_VEHICLE_PROXY", 30, identifier="A-FAR"),
        ]
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert _row(
        _enrich(roads=roads), "GENERAL_VEHICLE_PROXY"
    ).nearest_road_feature_id == "Z-NEAR"
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_unequal_distance_wins_regardless_of_identifier() -> None:
    roads = _roads(
        [
            _road_row("GENERAL_VEHICLE_PROXY", 20, identifier="Z-NEAR"),
            _road_row("GENERAL_VEHICLE_PROXY", 30, identifier="A-FAR"),
        ]
    )

    assert _row(
        _enrich(roads=roads), "GENERAL_VEHICLE_PROXY"
    ).nearest_road_feature_id == "Z-NEAR"
```

### `test_empty_eligible_class_emits_null_row_per_parcel`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
roads = _roads().loc[
        ~_roads()["road_proxy_class"].eq("UNKNOWN_REVIEW")
    ].reset_index(drop=True)
parcels = _parcels(
        [
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
            Polygon([(50, 0), (50, 10), (60, 10), (60, 0), (50, 0)]),
        ]
    )
result = _enrich(parcels=parcels, roads=roads)
rows = result.class_proximity.loc[
        result.class_proximity.road_proxy_class.eq("UNKNOWN_REVIEW")
    ]
coverage = {item.road_proxy_class: item for item in result.class_coverage}
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert len(rows) == 2
assert rows.loc[:, list(SELECTED_COLUMNS)].isna().all().all()
assert coverage["UNKNOWN_REVIEW"].feature_count == 0
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_empty_eligible_class_emits_null_row_per_parcel() -> None:
    roads = _roads().loc[
        ~_roads()["road_proxy_class"].eq("UNKNOWN_REVIEW")
    ].reset_index(drop=True)
    parcels = _parcels(
        [
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
            Polygon([(50, 0), (50, 10), (60, 10), (60, 0), (50, 0)]),
        ]
    )
    result = _enrich(parcels=parcels, roads=roads)
    rows = result.class_proximity.loc[
        result.class_proximity.road_proxy_class.eq("UNKNOWN_REVIEW")
    ]

    assert len(rows) == 2
    assert rows.loc[:, list(SELECTED_COLUMNS)].isna().all().all()
    coverage = {item.road_proxy_class: item for item in result.class_coverage}
    assert coverage["UNKNOWN_REVIEW"].feature_count == 0
```

### `test_output_shape_columns_and_order_are_deterministic`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels(
        [
            Polygon([(50, 0), (50, 10), (60, 10), (60, 0), (50, 0)]),
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
        ],
        identifiers=["SECOND", "FIRST"],
    )
result = _enrich(parcels=parcels)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert len(result.class_proximity) == len(parcels) * 5
assert list(result.class_proximity.columns) == list(CLASS_PROXIMITY_COLUMNS)
assert result.class_proximity.parcel_id.tolist() == [
        value for parcel_id in ("SECOND", "FIRST") for value in [parcel_id] * 5
    ]
assert result.class_proximity.road_proxy_class.tolist() == list(
        ELIGIBLE_CLASSES
    ) * 2
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_output_shape_columns_and_order_are_deterministic() -> None:
    parcels = _parcels(
        [
            Polygon([(50, 0), (50, 10), (60, 10), (60, 0), (50, 0)]),
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
        ],
        identifiers=["SECOND", "FIRST"],
    )
    result = _enrich(parcels=parcels)

    assert len(result.class_proximity) == len(parcels) * 5
    assert list(result.class_proximity.columns) == list(CLASS_PROXIMITY_COLUMNS)
    assert result.class_proximity.parcel_id.tolist() == [
        value for parcel_id in ("SECOND", "FIRST") for value in [parcel_id] * 5
    ]
    assert result.class_proximity.road_proxy_class.tolist() == list(
        ELIGIBLE_CLASSES
    ) * 2
```

### `test_class_coverage_is_complete_and_strict`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _enrich()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert tuple(item.road_proxy_class for item in result.class_coverage) == (
        ALL_CLASSES
    )
assert sum(item.feature_count for item in result.class_coverage) == 6
assert all(
        item.distance_eligible == (item.road_proxy_class != "NOT_DISTANCE_PROXY")
        for item in result.class_coverage
    )
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_class_coverage_is_complete_and_strict() -> None:
    result = _enrich()

    assert tuple(item.road_proxy_class for item in result.class_coverage) == (
        ALL_CLASSES
    )
    assert sum(item.feature_count for item in result.class_coverage) == 6
    assert all(
        item.distance_eligible == (item.road_proxy_class != "NOT_DISTANCE_PROXY")
        for item in result.class_coverage
    )
```

### `test_selected_road_evidence_and_lineage_are_exact`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
row = _row(_enrich(), "GENERAL_VEHICLE_PROXY")
```

**Action**

```python
policy = load_ign_road_vehicle_proxy_policy()
```

**Expected result**

```python
assert row.nearest_road_feature_id == "ROAD-GENERAL"
assert row.nearest_source_feature_id == "SOURCE-ROAD-GENERAL"
assert row.nearest_road_primary_rule == "OPEN_OR_TOLL"
assert row.nearest_road_rule_trace_json == '["OPEN_OR_TOLL"]'
assert row.nearest_road_unknown_fields_json == "[]"
assert not row.nearest_road_toll_evidence
assert row.nearest_source_archive_sha256 == "a" * 64
assert row.road_proxy_policy_id == policy.policy_id
assert row.road_proxy_policy_schema_version == policy.schema_version
assert row.road_proxy_policy_config_sha256 == policy.config_sha256
assert row.road_proxy_heavy_vehicle_access == "NOT_PROVEN"
assert row.proximity_scope == "WITHIN_VERIFIED_SOURCE_PACKAGE"
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_selected_road_evidence_and_lineage_are_exact() -> None:
    policy = load_ign_road_vehicle_proxy_policy()
    row = _row(_enrich(), "GENERAL_VEHICLE_PROXY")

    assert row.nearest_road_feature_id == "ROAD-GENERAL"
    assert row.nearest_source_feature_id == "SOURCE-ROAD-GENERAL"
    assert row.nearest_road_primary_rule == "OPEN_OR_TOLL"
    assert row.nearest_road_rule_trace_json == '["OPEN_OR_TOLL"]'
    assert row.nearest_road_unknown_fields_json == "[]"
    assert not row.nearest_road_toll_evidence
    assert row.nearest_source_archive_sha256 == "a" * 64
    assert row.road_proxy_policy_id == policy.policy_id
    assert row.road_proxy_policy_schema_version == policy.schema_version
    assert row.road_proxy_policy_config_sha256 == policy.config_sha256
    assert row.road_proxy_heavy_vehicle_access == "NOT_PROVEN"
    assert row.proximity_scope == "WITHIN_VERIFIED_SOURCE_PACKAGE"
```

### `test_parcels_and_road_application_are_not_mutated`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels(index=[777])
roads = _roads()
parcels_before = deepcopy(parcels)
roads_before = deepcopy(roads)
result = _enrich(parcels=parcels, roads=roads)
assert_geodataframe_equal(parcels, parcels_before)
assert_geodataframe_equal(roads, roads_before)
assert_geodataframe_equal(result.parcels, parcels_before)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert result.parcels.index.equals(parcels.index)
assert list(result.parcels.columns) == list(parcels.columns)
assert result.parcels.dtypes.equals(parcels.dtypes)
assert result.parcels.geometry.to_wkb().equals(parcels.geometry.to_wkb())
```

**Regression protected**

Prevents geometry changes from passing a preservation or source-bound comparison merely because other fields were updated coherently.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_parcels_and_road_application_are_not_mutated() -> None:
    parcels = _parcels(index=[777])
    roads = _roads()
    parcels_before = deepcopy(parcels)
    roads_before = deepcopy(roads)
    result = _enrich(parcels=parcels, roads=roads)

    assert_geodataframe_equal(parcels, parcels_before)
    assert_geodataframe_equal(roads, roads_before)
    assert_geodataframe_equal(result.parcels, parcels_before)
    assert result.parcels.index.equals(parcels.index)
    assert list(result.parcels.columns) == list(parcels.columns)
    assert result.parcels.dtypes.equals(parcels.dtypes)
    assert result.parcels.geometry.to_wkb().equals(parcels.geometry.to_wkb())
```

### `_corrupt_nearest_output`

**Exact signature**

```python
def _corrupt_nearest_output(column: str, value: object) -> None:
```

**Purpose**

Private `test` helper for corrupt nearest output; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- Every observed return expression is reproduced without truncation:
```python
output
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `output['distance_m'].notna`, `output['distance_m'].notna().any`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `output.at[0, column]`, `output[column]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_malformed_produced_distance_is_rejected` via `_corrupt_nearest_output`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_malformed_produced_tie_count_is_rejected` via `_corrupt_nearest_output`.

**Complete source-ordered implementation**

```python
def _corrupt_nearest_output(column: str, value: object) -> None:
    import landscout.stages.enrich_road_proximity as module

    original = module._nearest_class_rows

    def corrupted(*args: object, **kwargs: object) -> pd.DataFrame:
        output = original(*args, **kwargs)
        if output["distance_m"].notna().any():
            output[column] = output[column].astype("object")
            output.at[0, column] = value
        return output

    with patch.object(module, "_nearest_class_rows", side_effect=corrupted), pytest.raises(
        RoadProximityError
    ):
        _enrich()
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_corrupt_nearest_output.corrupted`

**Exact signature**

```python
def corrupted(*args: object, **kwargs: object) -> pd.DataFrame:
```

**Purpose**

Private `test` helper for corrupted; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
output
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `output['distance_m'].notna`, `output['distance_m'].notna().any`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `output.at[0, column]`, `output[column]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_local_corruption_fast_fails_before_heavy_validation` via `validate_bess_planning_feature_parcel_aggregation_result(*inputs, coded, config, policy, application, corrupted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_coordinated_local_cross_table_corruption_is_rejected` via `module._validate_result_envelope(corrupted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_selected_relation_role_requires_selected_status_and_priority` via `module._validate_result_envelope(corrupted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_duplicate_output_columns_are_rejected_intrinsically` via `module._validate_result_envelope(corrupted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_only_application_result_schema_two_is_accepted` via `module._validate_result_envelope(corrupted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_authorized_status_artifact_fails_local_verified_byte_loading` via `module._result_with_hashes(corrupted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_authorized_status_artifact_fails_local_verified_byte_loading` via `_write_artifacts(tmp_path, corrupted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_coordinated_relation_identity_artifact_corruption_fails_locally` via `_write_artifacts(tmp_path, corrupted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_controlling_relation_cannot_be_relabelled_contextual_in_artifact` via `_write_artifacts(tmp_path, corrupted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_no_relation_parcel_rejects_textual_null_identity` via `_write_artifacts(tmp_path, corrupted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `validate_bess_planning_feature_parcel_aggregation_result(*inputs, coded, config, policy, application, corrupted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_decision_status_domain_rejects_forbidden_vocabulary` via `module._validate_result_envelope(corrupted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_persisted_feature_id_json_must_be_portable_and_canonical` via `module._validate_result_envelope(corrupted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_in_memory_config_is_revalidated_before_compilation` via `compile_bess_planning_feature_policy(*inputs, coded, corrupted)`.
- callback/function object: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_unknown_voltage_parcel_with_same_total_count` via `profile_grid_proximity(corrupted)`.
- callback/function object: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_unknown_relation_parcel` via `_validate_source_complete(planning_document, parcels, corrupted)`.
- callback/function object: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_coherent_parcel_metric_mutation` via `_validate_source_complete(planning_document, parcels, corrupted)`.
- callback/function object: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_same_area_wrong_parcel_relation` via `_validate_source_complete(planning_document, parcels, corrupted)`.
- callback/function object: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_missing_expected_relation` via `_validate_source_complete(planning_document, parcels, corrupted)`.
- callback/function object: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_extra_geometrically_false_relation` via `_validate_source_complete(planning_document, parcels, corrupted)`.
- callback/function object: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_reordered_relations` via `_validate_source_complete(planning_document, parcels, corrupted)`.
- callback/function object: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_coherent_but_wrong_line_metric` via `_validate_source_complete(planning_document, parcels, corrupted)`.
- callback/function object: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_corrupted_complete_parcel_summaries` via `_validate_source_complete(planning_document, corrupted, result)`.
- callback/function object: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_noncanonical_parcel_summary_dtype` via `_validate_source_complete(planning_document, corrupted, result)`.
- callback/function object: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_each_corrupted_parcel_summary_fact` via `_validate_source_complete(planning_document, corrupted, result)`.
- callback/function object: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_coherently_renamed_feature_identity` via `_validate_source_complete(planning_document, parcels, corrupted)`.
- callback/function object: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_independent_gpu_lineage_mutation` via `_validate_source_complete(planning_document, parcels, corrupted)`.
- callback/function object: `tests/unit/test_enrich_planning_features.py::test_three_dimensional_normalized_catalogs_are_rejected` via `_validate_source_complete(planning_document, parcels, corrupted)`.
- callback/function object: `tests/unit/test_enrich_planning_zoning.py::test_zoning_summary_lineage_and_count_must_match_bundle` via `intersect_parcels_with_gpu_zoning(_parcels(), corrupted)`.
- callback/function object: `tests/unit/test_enrich_road_proximity.py::_corrupt_nearest_output` via `patch.object(module, '_nearest_class_rows', side_effect=corrupted)`.
- callback/function object: `tests/unit/test_index_planning_regulation.py::test_mutated_loaded_nomfic_is_rejected_before_selection` via `index_planning_regulation(corrupted)`.
- callback/function object: `tests/unit/test_index_planning_regulation.py::test_mutated_loaded_zoning_geometry_or_order_is_rejected` via `index_planning_regulation(corrupted)`.
- callback/function object: `tests/unit/test_index_planning_regulation.py::test_zoning_source_inventory_integrity_mismatch_is_rejected` via `index_planning_regulation(corrupted)`.
- callback/function object: `tests/unit/test_index_planning_regulation.py::test_filename_absent_from_inventory_fails` via `index_planning_regulation(corrupted)`.
- callback/function object: `tests/unit/test_index_planning_regulation.py::test_path_outside_root_is_rejected` via `index_planning_regulation(corrupted)`.
- callback/function object: `tests/unit/test_index_planning_regulation.py::test_pdf_inventory_integrity_mismatch_fails` via `index_planning_regulation(corrupted)`.
- callback/function object: `tests/unit/test_index_planning_regulation.py::test_index_integrity_mutations_fail` via `validate_planning_regulation_index(corrupted)`.
- callback/function object: `tests/unit/test_index_planning_regulation.py::test_search_requested_terms_must_be_an_immutable_exact_tuple` via `validate_planning_regulation_search_result(index, corrupted)`.
- callback/function object: `tests/unit/test_index_planning_regulation.py::test_search_result_integrity_mutations_fail` via `validate_planning_regulation_search_result(index, corrupted)`.
- callback/function object: `tests/unit/test_index_planning_regulation.py::test_search_hit_lineage_mutation_fails` via `validate_planning_regulation_search_result(index, corrupted)`.
- callback/function object: `tests/unit/test_index_planning_regulation.py::test_malformed_source_metadata_raises_controlled_index_error` via `index_planning_regulation(corrupted)`.

**Complete source-ordered implementation**

```python
def corrupted(*args: object, **kwargs: object) -> pd.DataFrame:
        output = original(*args, **kwargs)
        if output["distance_m"].notna().any():
            output[column] = output[column].astype("object")
            output.at[0, column] = value
        return output
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_produced_distance_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `value`.

**Setup**

```python
_corrupt_nearest_output("distance_m", value)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Pins the exact framework interaction and outcome reproduced in the complete test source.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_malformed_produced_distance_is_rejected(value: object) -> None:
    _corrupt_nearest_output("distance_m", value)
```

### `test_malformed_produced_tie_count_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `value`.

**Setup**

```python
_corrupt_nearest_output("tie_count", value)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Pins the exact framework interaction and outcome reproduced in the complete test source.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_malformed_produced_tie_count_is_rejected(value: object) -> None:
    _corrupt_nearest_output("tie_count", value)
```

### `test_result_dataclasses_are_frozen`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _enrich()
coverage = result.class_coverage[0]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(FrozenInstanceError):
        result.parcels = _parcels()
with pytest.raises(FrozenInstanceError):
        coverage.feature_count = 99
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_result_dataclasses_are_frozen() -> None:
    result = _enrich()
    coverage = result.class_coverage[0]

    with pytest.raises(FrozenInstanceError):
        result.parcels = _parcels()  # type: ignore[misc]
    with pytest.raises(FrozenInstanceError):
        coverage.feature_count = 99
```

### `test_no_business_decision_columns_or_implementation_exist`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _enrich()
forbidden = {
        "access_score",
        "bess_score",
        "accessible",
        "legal_access",
        "parcel_status",
        "retained",
        "rejected",
    }
source = Path("src/landscout/stages/enrich_road_proximity.py").read_text(
        encoding="utf-8"
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert forbidden.isdisjoint(result.parcels.columns)
assert forbidden.isdisjoint(result.class_proximity.columns)
assert ".iterrows(" not in source
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_no_business_decision_columns_or_implementation_exist() -> None:
    result = _enrich()
    forbidden = {
        "access_score",
        "bess_score",
        "accessible",
        "legal_access",
        "parcel_status",
        "retained",
        "rejected",
    }
    assert forbidden.isdisjoint(result.parcels.columns)
    assert forbidden.isdisjoint(result.class_proximity.columns)

    source = Path("src/landscout/stages/enrich_road_proximity.py").read_text(
        encoding="utf-8"
    )
    assert ".iterrows(" not in source
```

### `test_result_parcel_frame_is_an_independent_copy`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels()
result = _enrich(parcels=parcels)
result.parcels.loc[result.parcels.index[0], "source_value"] = 999
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert parcels.iloc[0].source_value == 0
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_result_parcel_frame_is_an_independent_copy() -> None:
    parcels = _parcels()
    result = _enrich(parcels=parcels)
    result.parcels.loc[result.parcels.index[0], "source_value"] = 999

    assert parcels.iloc[0].source_value == 0
```

### `test_class_proximity_is_plain_dataframe`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _enrich()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert type(result.class_proximity) is pd.DataFrame
assert not isinstance(result.class_proximity, gpd.GeoDataFrame)
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_class_proximity_is_plain_dataframe() -> None:
    result = _enrich()

    assert type(result.class_proximity) is pd.DataFrame
    assert not isinstance(result.class_proximity, gpd.GeoDataFrame)
```

### `test_selected_rows_belong_to_requested_class`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _enrich()
road_classes = _roads().set_index("road_feature_id")["road_proxy_class"]
selected = result.class_proximity.dropna(subset=["nearest_road_feature_id"])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert all(
        road_classes.loc[row.nearest_road_feature_id] == row.road_proxy_class
        for row in selected.itertuples(index=False)
    )
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_selected_rows_belong_to_requested_class() -> None:
    result = _enrich()
    road_classes = _roads().set_index("road_feature_id")["road_proxy_class"]
    selected = result.class_proximity.dropna(subset=["nearest_road_feature_id"])

    assert all(
        road_classes.loc[row.nearest_road_feature_id] == row.road_proxy_class
        for row in selected.itertuples(index=False)
    )
```

### `test_policy_sha_mismatch_does_not_construct_spatial_index`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
roads = _roads()
roads["road_proxy_policy_config_sha256"] = "b" * 64
spatial_index.assert_not_called()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with patch(
        "landscout.stages.enrich_road_proximity.STRtree"
    ) as spatial_index, pytest.raises(RoadProximityError):
        _enrich(roads=roads)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_policy_sha_mismatch_does_not_construct_spatial_index() -> None:
    roads = _roads()
    roads["road_proxy_policy_config_sha256"] = "b" * 64

    with patch(
        "landscout.stages.enrich_road_proximity.STRtree"
    ) as spatial_index, pytest.raises(RoadProximityError):
        _enrich(roads=roads)

    spatial_index.assert_not_called()
```

### `test_matched_output_dtypes_are_stable`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _enrich()
table = result.class_proximity
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert str(table.nearest_road_proxy_distance_m.dtype) == "float64"
assert str(table.nearest_road_tie_count.dtype) == "Int64"
assert str(table.nearest_road_toll_evidence.dtype) == "boolean"
```

**Regression protected**

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_matched_output_dtypes_are_stable() -> None:
    result = _enrich()
    table = result.class_proximity

    assert str(table.nearest_road_proxy_distance_m.dtype) == "float64"
    assert str(table.nearest_road_tie_count.dtype) == "Int64"
    assert str(table.nearest_road_toll_evidence.dtype) == "boolean"
```

### `test_parcel_preservation_uses_exact_non_geometry_values`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels()
result = _enrich(parcels=parcels)
assert_frame_equal(
        pd.DataFrame(result.parcels.drop(columns="geometry")),
        pd.DataFrame(parcels.drop(columns="geometry")),
        check_dtype=True,
        check_index_type=True,
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_parcel_preservation_uses_exact_non_geometry_values() -> None:
    parcels = _parcels()
    result = _enrich(parcels=parcels)

    assert_frame_equal(
        pd.DataFrame(result.parcels.drop(columns="geometry")),
        pd.DataFrame(parcels.drop(columns="geometry")),
        check_dtype=True,
        check_index_type=True,
    )
```


## 7. Data contracts

### `SELECTED_COLUMNS` — canonical or derived frame-column schema

```python
SELECTED_COLUMNS = (
    "nearest_road_proxy_distance_m",
    "nearest_road_feature_id",
    "nearest_source_feature_id",
    "nearest_road_tie_count",
    "nearest_road_primary_rule",
    "nearest_road_rule_trace_json",
    "nearest_road_unknown_fields_json",
    "nearest_road_toll_evidence",
    "nearest_nature_raw",
    "nearest_importance_raw",
    "nearest_asset_status_raw",
    "nearest_private_raw",
    "nearest_light_vehicle_access_raw",
    "nearest_carriageway_width_raw",
    "nearest_closure_period_raw",
    "nearest_restriction_nature_raw",
    "nearest_source_layer",
    "nearest_source_department_code",
    "nearest_source_edition",
    "nearest_source_archive_sha256",
)
```


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

# `tests/unit/test_enrich_planning_zoning.py`

## File identity

- Repository path: `tests/unit/test_enrich_planning_zoning.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `enrich_planning_zoning` contracts exercised in this file.
- Source SHA256: `b3d5429c8456644a97db55f6cf32d282a51549e4e3de81ff1632ca23806abbe7`

## 1. Purpose

Provides complete unit and regression coverage for the `enrich_planning_zoning` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import json`
- `from copy import deepcopy`
- `from dataclasses import FrozenInstanceError, replace`
- `from hashlib import sha256`
- `from pathlib import Path`
- `from unittest.mock import patch`

### Third-party packages

- `import geopandas as gpd`
- `import pandas as pd`
- `import pytest`
- `from geopandas.testing import assert_geodataframe_equal`
- `from pandas.api.types import is_float_dtype, is_integer_dtype`
- `from pandas.testing import assert_frame_equal`
- `from shapely.geometry import (
    LineString,
    MultiPolygon,
    Point,
    Polygon,
)`

### Internal LandScout imports

- `from landscout import stages`
- `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)`
- `from landscout.stages.enrich_planning_zoning import (
    ParcelZoningResult,
    PlanningZoningError,
    _stabilize_area_relationships,
    intersect_parcels_with_gpu_zoning,
    validate_normalized_planning_zoning_inputs,
)`
- `from landscout.stages.planning_overlay import technical_overlay_tolerance`

## 4. Contract taxonomy

### A. Python constants

#### `ARCHIVE_SHA256`

```python
ARCHIVE_SHA256 = "a" * 64
```

Hash identity, algorithm, or canonical-content field used by the named integrity contract. Consumers include `tests/unit/test_assess_grid_coverage.py::_coverage` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::_coverage` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_caller_provided_proximity_and_coverage_are_not_public_inputs` (value argument/reference), `tests/unit/test_assess_road_proximity_coverage.py::_archive` (value argument/reference), `tests/unit/test_enrich_planning_zoning.py::_planning_document` (value argument/reference), `tests/unit/test_enrich_planning_zoning.py::_planning_document` (value argument/reference), `tests/unit/test_normalize_access_ign.py::_source` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::_context` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::_source_bundle` (value argument/reference).

#### `ARCHIVE_NAME`

```python
ARCHIVE_NAME = "31395_PLU_20240215"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_enrich_planning_features.py::_planning_document` (value argument/reference), `tests/unit/test_enrich_planning_features.py::test_source_document_reference_allows_one_archive_zip_suffix` (value argument/reference).

#### `DOCUMENT_ID`

```python
DOCUMENT_ID = "doc-1"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_enrich_planning_features.py::_planning_document` (value argument/reference), `tests/unit/test_index_planning_regulation.py::_summary` (value argument/reference), `tests/unit/test_index_planning_regulation.py::_document` (value argument/reference).

#### `SOURCE_LAYER`

```python
SOURCE_LAYER = "31395_ZONE_URBA_20240215"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_enrich_planning_zoning.py::_physical_planning_document` (value argument/reference), `tests/unit/test_enrich_planning_zoning.py::_physical_planning_document` (value argument/reference), `tests/unit/test_enrich_planning_zoning.py::_physical_planning_document` (value argument/reference), `tests/unit/test_enrich_planning_zoning.py::_physical_planning_document` (value argument/reference).

#### `STANDARD_MODEL`

```python
STANDARD_MODEL = "CNIG PLU v2017"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_enrich_planning_zoning.py::_planning_document` (value argument/reference).

#### `SOURCE_FIELDS`

```python
SOURCE_FIELDS = (
    "LIB_IDZONE",
    "LIBELLE",
    "LIBELONG",
    "TYPEZONE",
    "NOMFIC",
    "URLFIC",
    "IDURBA",
    "DATVALID",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `tests/unit/test_enrich_planning_zoning.py::test_every_source_zoning_field_is_required` (value argument/reference).

#### `LOCAL_ENGINEERING_CRS`

```python
LOCAL_ENGINEERING_CRS = (
    'ENGCRS["Local",EDATUM["Unknown"],CS[Cartesian,2],'
    'AXIS["x",east,LENGTHUNIT["metre",1]],'
    'AXIS["y",north,LENGTHUNIT["metre",1]]]'
)
```

Coordinate-reference-system identity used for an explicit storage, validation, or calculation boundary. Consumers include `tests/unit/test_enrich_planning_features.py::test_unusable_source_crs_is_rejected` (value argument/reference), `tests/unit/test_enrich_planning_zoning.py::test_missing_or_unusable_crs_is_rejected` (value argument/reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

### `test_shared_overlay_tolerance_preserves_zoning_numerical_behavior`

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
covered, gap, excess = _stabilize_area_relationships(
        100.0, 100.0 + 5e-7, 100.0 + 5e-7
    )
```

**Expected result**

```python
assert technical_overlay_tolerance(100.0) == pytest.approx(1e-6)
assert covered == pytest.approx(100.0)
assert gap == pytest.approx(0.0)
assert excess == pytest.approx(5e-7)
with pytest.raises(PlanningZoningError, match="materially exceeds"):
        _stabilize_area_relationships(100.0, 100.0 + 2e-6, 100.0 + 2e-6)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_shared_overlay_tolerance_preserves_zoning_numerical_behavior() -> None:
    assert technical_overlay_tolerance(100.0) == pytest.approx(1e-6)
    covered, gap, excess = _stabilize_area_relationships(
        100.0, 100.0 + 5e-7, 100.0 + 5e-7
    )
    assert covered == pytest.approx(100.0)
    assert gap == pytest.approx(0.0)
    assert excess == pytest.approx(5e-7)
    with pytest.raises(PlanningZoningError, match="materially exceeds"):
        _stabilize_area_relationships(100.0, 100.0 + 2e-6, 100.0 + 2e-6)
```

### `_rectangle`

**Exact signature**

```python
def _rectangle(x_min: float, y_min: float, x_max: float, y_max: float) -> Polygon:
```

**Purpose**

Private `test` helper for rectangle; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Polygon`.
- Every observed return expression is reproduced without truncation:
```python
Polygon([(x_min, y_min), (x_min, y_max), (x_max, y_max), (x_max, y_min), (x_min, y_min)])
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

- direct call or construction: `tests/unit/test_enrich_planning_features.py::_parcels` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_planning_document` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_surface_full_overlap_normalizes_raw_values_and_lineage` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_surface_partial_and_touch_relations` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_overlapping_surface_union_is_not_double_counted` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_polygon_and_multipolygon_surfaces` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_epsg4326_parcels_are_measured_in_lambert93_but_preserved` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_duplicate_parcel_ids_are_rejected` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_duplicate_source_ids_are_rejected` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_null_or_empty_source_geometry_is_rejected` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_inputs_and_all_existing_parcel_fields_are_preserved` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_relations_are_unique_deterministic_and_summaries_agree` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_contract_result` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_source_complete_contract` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_two_parcel_source_complete_contract` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_reloads_and_compares_source_catalog` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_changed_physical_gpkg_geometry` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_reordered_physical_gpkg_rows` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_shapefile_source_complete_contract` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_shapefile_ogr_fid_source_complete_contract` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_shapefile_family_excludes_dotted_sibling_dataset` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::_parcels` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::_zones` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_one_parcel_fully_inside_one_zone` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_parcel_split_across_two_zones` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_dominant_zone_tie_is_deterministic` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_touch_only_relation_is_preserved_but_never_dominant` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_parcel_with_no_positive_area_zone_is_preserved` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_parcel_with_no_intersecting_zone_has_zero_coverage` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_overlapping_source_zones_expose_raw_sum_union_and_excess` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_polygon_and_multipolygon_parcels_are_supported` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_polygon_and_multipolygon_zones_are_supported` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_duplicate_parcel_id_is_rejected` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_duplicate_source_zone_id_is_rejected` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_input_frames_are_not_mutated` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_raw_zoning_values_are_preserved_exactly` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_intersection_table_references_only_known_parcels_and_zones` via `_rectangle`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_rejects_coordinated_mutations` via `_rectangle`.

**Complete source-ordered implementation**

```python
def _rectangle(x_min: float, y_min: float, x_max: float, y_max: float) -> Polygon:
    return Polygon(
        [
            (x_min, y_min),
            (x_min, y_max),
            (x_max, y_max),
            (x_max, y_min),
            (x_min, y_min),
        ]
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
    crs: str | None = "EPSG:2154",
) -> gpd.GeoDataFrame:
```

**Purpose**

Private `test` helper for parcels; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
frame.to_crs(crs)

frame.set_crs(None, allow_override=True)

frame
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `frame.to_crs`.
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
) -> gpd.GeoDataFrame:
    values = geometries or [_rectangle(0, 0, 10, 10)]
    ids = identifiers or [f"PARCEL-{position + 1}" for position in range(len(values))]
    frame = gpd.GeoDataFrame(
        {
            "parcel_id": ids,
            "existing_grid_value": [100 + position for position in range(len(values))],
        },
        geometry=values,
        crs="EPSG:2154",
        index=[50 + position for position in range(len(values))],
    )
    if crs is None:
        return frame.set_crs(None, allow_override=True)
    if crs == "EPSG:2154":
        return frame
    return frame.to_crs(crs)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_zones`

**Exact signature**

```python
def _zones(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    labels: list[object] | None = None,
    long_labels: list[object] | None = None,
    zone_types: list[object] | None = None,
    document_references: list[object] | None = None,
    crs: str | None = "EPSG:2154",
) -> gpd.GeoDataFrame:
```

**Purpose**

Private `test` helper for zones; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
frame.to_crs(crs)

frame.set_crs(None, allow_override=True)

frame

frame.set_crs(crs, allow_override=True)

frame.set_crs(crs, allow_override=True)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `frame.to_crs`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::_planning_document` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::_physical_planning_document` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_one_parcel_fully_inside_one_zone` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_parcel_split_across_two_zones` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_dominant_zone_tie_is_deterministic` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_touch_only_relation_is_preserved_but_never_dominant` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_parcel_with_no_positive_area_zone_is_preserved` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_parcel_with_no_intersecting_zone_has_zero_coverage` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_overlapping_source_zones_expose_raw_sum_union_and_excess` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_polygon_and_multipolygon_parcels_are_supported` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_polygon_and_multipolygon_zones_are_supported` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_missing_or_unusable_crs_is_rejected` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_invalid_or_non_polygonal_parcel_geometry_is_rejected` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_invalid_or_non_polygonal_zone_geometry_is_rejected` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_invalid_parcel_id_is_rejected` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_duplicate_parcel_id_is_rejected` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_missing_parcel_id_is_rejected` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_geometry_must_be_the_active_parcel_geometry_column` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_invalid_source_zone_id_is_rejected` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_duplicate_source_zone_id_is_rejected` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_zoning_document_reference_must_match_loaded_archive` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_existing_parcel_output_field_collision_is_rejected` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_every_source_zoning_field_is_required` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_input_frames_are_not_mutated` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_raw_zoning_values_are_preserved_exactly` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_intersection_table_references_only_known_parcels_and_zones` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_result_frames_are_independent_from_inputs` via `_zones`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_rejects_coordinated_mutations` via `_zones`.
- direct call or construction: `tests/unit/test_interpret_bess_zoning.py::inputs` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::valid_result` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::_validate` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_can_return_validated_fragments` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_document_layout_accepts_real_first_and_last_indexed_pages` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_document_layout_rejects_nonexistent_indexed_pages` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_existing_empty_toc_page_is_valid_not_nonexistent` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_document_lock_mismatch_is_rejected` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_evidence_scope_is_derived_from_exact_section_type` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_reversed_topic_mapping_keys_do_not_change_output_or_hashes` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_equal_length_overlap_uses_configured_term_order_as_tie_break` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_inputs_are_not_mutated` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_dominant_unmapped_zone_stops_processing` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_blank_only_prefix_is_preserved_in_first_actual_section` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_blank_gap_after_toc_is_preserved_without_a_blank_other_section` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::_structure_with_document_layout` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_two_zone_patterns_matching_one_line_are_ambiguous` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_two_article_patterns_matching_one_line_are_ambiguous` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_general_and_article_cross_category_match_is_ambiguous` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_zone_and_general_cross_category_match_is_ambiguous` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_ambiguous_continuation_candidate_fails_with_record_diagnostic` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_rejects_changed_ambiguous_grammar` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_normal_muret_compatible_grammar_remains_deterministic` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_wrong_intersection_source_zone_id_is_rejected` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_intersection_area_cannot_exceed_available_geometry_area` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_intersection_upper_bound_uses_shared_relative_tolerance` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_intersection_hash_columns_are_actual_and_deterministic` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_optional_intersection_metric_change_invalidates_existing_result` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_intersection_hash_column_lineage_mutation_is_rejected` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_alias_chain_resolves_to_final_configured_target` via `_zones`.
- direct call or construction: `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_rejects_post_build_source_change` via `_zones`.

**Complete source-ordered implementation**

```python
def _zones(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    labels: list[object] | None = None,
    long_labels: list[object] | None = None,
    zone_types: list[object] | None = None,
    document_references: list[object] | None = None,
    crs: str | None = "EPSG:2154",
) -> gpd.GeoDataFrame:
    values = geometries or [_rectangle(-10, -10, 20, 20)]
    count = len(values)
    source_ids = identifiers or [f"ZONE-{position + 1}" for position in range(count)]
    source_labels = labels or [f"U{position + 1}" for position in range(count)]
    source_long_labels = long_labels or [
        f"Zone urbaine {position + 1}" for position in range(count)
    ]
    source_types = zone_types or ["U"] * count
    source_documents = document_references or [ARCHIVE_NAME] * count
    frame = gpd.GeoDataFrame(
        {
            "LIB_IDZONE": source_ids,
            "LIBELLE": source_labels,
            "LIBELONG": source_long_labels,
            "TYPEZONE": source_types,
            "NOMFIC": [f"reglement-{position + 1}.pdf" for position in range(count)],
            "URLFIC": [
                f"https://www.geoportail-urbanisme.gouv.fr/reglement/{position + 1}"
                for position in range(count)
            ],
            "IDURBA": source_documents,
            "DATVALID": ["2024-02-15"] * count,
        },
        geometry=values,
        crs="EPSG:2154",
        index=[200 + position for position in range(count)],
    )
    if crs is None:
        return frame.set_crs(None, allow_override=True)
    if crs == "EPSG:2154":
        return frame
    if crs == "IGNF:LAMB93":
        return frame.set_crs(crs, allow_override=True)
    if crs == LOCAL_ENGINEERING_CRS:
        return frame.set_crs(crs, allow_override=True)
    return frame.to_crs(crs)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_planning_document`

**Exact signature**

```python
def _planning_document(
    zoning: gpd.GeoDataFrame | None = None,
    *,
    archive_name: str = ARCHIVE_NAME,
    document_id: str = DOCUMENT_ID,
    source_layer: str = SOURCE_LAYER,
) -> GpuPlanningDocument:
```

**Purpose**

Private `test` helper for planning document; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `GpuPlanningDocument`.
- Every observed return expression is reproduced without truncation:
```python
GpuPlanningDocument(extraction=extraction, all_spatial_layers=(reference,), zoning=inspected, related_layers=())
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: `GpuArchiveDownload`.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `(non_empty & ~geometry.is_valid).sum`, `(non_null & geometry.is_empty).sum`, `geometry[non_null].geom_type.value_counts`, `geometry[non_null].geom_type.value_counts().items`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_enrich_planning_features.py::_run` via `_planning_document`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_mutated_source_summary_is_rejected` via `_planning_document`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_source_summary_counts_are_strict_integers` via `_planning_document`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_inputs_and_all_existing_parcel_fields_are_preserved` via `_planning_document`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_contract_result` via `_planning_document`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_source_complete_contract` via `_planning_document`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_two_parcel_source_complete_contract` via `_planning_document`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_reordered_physical_gpkg_rows` via `_planning_document`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_shapefile_source_complete_contract` via `_planning_document`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_shapefile_ogr_fid_source_complete_contract` via `_planning_document`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::_physical_planning_document` via `_planning_document`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::_run` via `_planning_document`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_zoning_summary_lineage_and_count_must_match_bundle` via `_planning_document`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_input_frames_are_not_mutated` via `_planning_document`.
- direct call or construction: `tests/unit/test_resolve_planning_feature_codes.py::_legacy_inputs` via `_planning_document`.
- direct call or construction: `tests/unit/test_resolve_planning_feature_codes.py::_integration_inputs` via `_planning_document`.
- direct call or construction: `tests/unit/test_resolve_planning_feature_codes.py::test_wrong_planning_standard_is_rejected` via `_planning_document`.
- direct call or construction: `tests/unit/test_resolve_planning_feature_codes.py::test_valid_multi_geometries_are_accepted` via `_planning_document`.
- direct call or construction: `tests/unit/test_resolve_planning_feature_codes.py::test_valid_relation_types_are_retained` via `_planning_document`.

**Complete source-ordered implementation**

```python
def _planning_document(
    zoning: gpd.GeoDataFrame | None = None,
    *,
    archive_name: str = ARCHIVE_NAME,
    document_id: str = DOCUMENT_ID,
    source_layer: str = SOURCE_LAYER,
) -> GpuPlanningDocument:
    data = zoning if zoning is not None else _zones()
    document = GpuDocumentMetadata(
        provider="Géoportail de l'Urbanisme",
        portal="GPU",
        commune_code="31395",
        partition="DU_31395",
        document_id=document_id,
        document_family="DU",
        document_type="PLU",
        document_title="Plan local d'urbanisme de Muret",
        status="document.production",
        legal_status="APPROVED",
        effective_status="EN_VIGUEUR",
        version="10",
        archive_name=archive_name,
        publication_timestamp="2024-03-26T08:52:34+01:00",
        update_timestamp="2024-03-26T08:52:34+01:00",
        revision_date="2024-02-15",
        producer="Mairie de Muret",
        standard_model=STANDARD_MODEL,
        projection="IGNF:LAMB93",
        metadata_identifier="fr-000031395-plu20240215",
        source_url=(
            "https://www.geoportail-urbanisme.gouv.fr/api/"
            "document/download-by-partition/DU_31395"
        ),
        written_files=(),
    )
    archive = GpuArchiveDownload(
        document=document,
        download_timestamp="2026-08-12T10:00:00+00:00",
        filename=f"{archive_name}.zip",
        archive_format="zip",
        file_size=1234,
        sha256=ARCHIVE_SHA256,
        path=Path("data/cache/gpu/synthetic.zip"),
        cache_hit=True,
    )
    extraction = GpuExtraction(
        archive=archive,
        extraction_root=Path("data/cache/gpu/extracted/synthetic"),
        files=(),
        standard_models=(STANDARD_MODEL,),
        cache_hit=True,
    )
    reference = GpuSpatialLayerReference(
        dataset_path=Path("data/cache/gpu/extracted/synthetic/planning.gpkg"),
        source_layer=source_layer,
        driver="GPKG",
    )
    geometry = data.geometry
    non_null = pd.Series(
        [value is not None for value in geometry], index=geometry.index, dtype=bool
    )
    non_empty = non_null & ~geometry.is_empty
    summary = GpuLayerSummary(
        source_document_id=document_id,
        source_archive_sha256=ARCHIVE_SHA256,
        source_layer=source_layer,
        crs="UNKNOWN" if data.crs is None else data.crs.to_string(),
        feature_count=len(data),
        columns=tuple(str(column) for column in data.columns),
        dtypes=tuple((str(column), str(dtype)) for column, dtype in data.dtypes.items()),
        null_counts=tuple(
            (str(column), int(data[column].isna().sum())) for column in data.columns
        ),
        geometry_types=tuple(
            (str(key), int(value))
            for key, value in geometry[non_null].geom_type.value_counts().items()
        ),
        null_geometry_count=int((~non_null).sum()),
        empty_geometry_count=int((non_null & geometry.is_empty).sum()),
        invalid_geometry_count=int((non_empty & ~geometry.is_valid).sum()),
    )
    inspected = GpuInspectedLayer(
        logical_name="zoning",
        reference=reference,
        data=data,
        summary=summary,
    )
    return GpuPlanningDocument(
        extraction=extraction,
        all_spatial_layers=(reference,),
        zoning=inspected,
        related_layers=(),
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_physical_planning_document`

**Exact signature**

```python
def _physical_planning_document(
    tmp_path: Path,
    zoning: gpd.GeoDataFrame | None = None,
) -> GpuPlanningDocument:
```

**Purpose**

Private `test` helper for physical planning document; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `GpuPlanningDocument`.
- Every observed return expression is reproduced without truncation:
```python
replace(base, extraction=extraction, all_spatial_layers=(reference,), zoning=inspected)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: `gpd.read_file`, `path.read_bytes`, `path.stat`, `sha256(path.read_bytes()).hexdigest`.
- Filesystem write: `(root / EXTRACTION_MANIFEST_NAME).write_text`, `root.mkdir`, `source.to_file`.
- CRS/geometry calculation: none directly visible.
- Hashing: `sha256`, `sha256(path.read_bytes()).hexdigest`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_accepts_physical_fixture` via `_physical_planning_document`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_rejects_coordinated_mutations` via `_physical_planning_document`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_rejects_physical_tamper` via `_physical_planning_document`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_revalidates_physical_source_once` via `_physical_planning_document`.

**Complete source-ordered implementation**

```python
def _physical_planning_document(
    tmp_path: Path,
    zoning: gpd.GeoDataFrame | None = None,
) -> GpuPlanningDocument:
    root = tmp_path / "extraction"
    root.mkdir(parents=True)
    path = root / "zoning.gpkg"
    source = zoning if zoning is not None else _zones()
    source.to_file(
        path,
        layer=SOURCE_LAYER,
        driver="GPKG",
        engine="pyogrio",
        index=False,
    )
    reread = gpd.read_file(path, layer=SOURCE_LAYER, engine="pyogrio")
    base = _planning_document(reread)
    reference = replace(
        base.zoning.reference,
        dataset_path=path,
        source_layer=SOURCE_LAYER,
        driver="GPKG",
    )
    inspected = replace(
        base.zoning,
        reference=reference,
        data=reread,
        summary=replace(base.zoning.summary, source_layer=SOURCE_LAYER),
    )
    inventory = (
        GpuExtractedFile(
            relative_path="zoning.gpkg",
            file_type="gpkg",
            size_bytes=path.stat().st_size,
            sha256=sha256(path.read_bytes()).hexdigest(),
            category="SPATIAL_DATA",
        ),
    )
    (root / EXTRACTION_MANIFEST_NAME).write_text(
        json.dumps(
            {
                "schema_version": 2,
                "archive_sha256": ARCHIVE_SHA256,
                "files": [
                    {
                        "relative_path": item.relative_path,
                        "size_bytes": item.size_bytes,
                        "sha256": item.sha256,
                    }
                    for item in inventory
                ],
            },
            sort_keys=True,
            separators=(",", ":"),
        ),
        encoding="utf-8",
    )
    extraction = replace(
        base.extraction,
        extraction_root=root,
        files=inventory,
    )
    return replace(
        base,
        extraction=extraction,
        all_spatial_layers=(reference,),
        zoning=inspected,
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_run`

**Exact signature**

```python
def _run(
    parcels: gpd.GeoDataFrame | None = None,
    zones: gpd.GeoDataFrame | None = None,
) -> ParcelZoningResult:
```

**Purpose**

Private `test` helper for run; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `ParcelZoningResult`.
- Every observed return expression is reproduced without truncation:
```python
intersect_parcels_with_gpu_zoning(parcels if parcels is not None else _parcels(), _planning_document(zones))
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

- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_result_is_frozen` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_surface_full_overlap_normalizes_raw_values_and_lineage` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_surface_partial_and_touch_relations` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_overlapping_surface_union_is_not_double_counted` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_polygon_and_multipolygon_surfaces` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_line_crossing_and_partly_inside` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_line_boundary_touch_is_zero_length` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_linestring_and_multilinestring` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_points_inside_boundary_outside_and_multipoint` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_missing_optional_layer_families_return_stable_empty_catalogs` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_optional_raw_source_fields_are_not_fabricated` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_epsg4326_parcels_are_measured_in_lambert93_but_preserved` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_invalid_parcel_ids_are_rejected` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_duplicate_parcel_ids_are_rejected` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_duplicate_source_ids_are_rejected` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_idurba_mismatch_is_rejected` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_missing_required_source_fields_fail` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_wrong_geometry_kind_is_rejected` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_invalid_surface_geometry_is_rejected_without_repair` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_null_or_empty_source_geometry_is_rejected` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_missing_crs_is_rejected` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_unusable_source_crs_is_rejected` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_reserved_output_column_collision_is_rejected` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_relations_are_unique_deterministic_and_summaries_agree` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_result_frames_are_independent_from_mutable_inputs` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_present_empty_optional_layer_is_valid` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_empty_and_nonempty_catalogs_have_identical_kind_schemas` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_same_source_id_is_allowed_in_distinct_logical_layers` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_geospatial_operation_failure_is_controlled_and_chained` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_gpu_source_z_is_normalized_to_canonical_2d` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_result_container_is_frozen` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_one_parcel_fully_inside_one_zone` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_parcel_split_across_two_zones` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_dominant_zone_tie_is_deterministic` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_touch_only_relation_is_preserved_but_never_dominant` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_parcel_with_no_positive_area_zone_is_preserved` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_parcel_with_no_intersecting_zone_has_zero_coverage` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_overlapping_source_zones_expose_raw_sum_union_and_excess` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_polygon_and_multipolygon_parcels_are_supported` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_polygon_and_multipolygon_zones_are_supported` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_missing_or_unusable_crs_is_rejected` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_invalid_or_non_polygonal_parcel_geometry_is_rejected` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_invalid_or_non_polygonal_zone_geometry_is_rejected` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_invalid_parcel_id_is_rejected` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_duplicate_parcel_id_is_rejected` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_missing_parcel_id_is_rejected` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_geometry_must_be_the_active_parcel_geometry_column` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_invalid_source_zone_id_is_rejected` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_duplicate_source_zone_id_is_rejected` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_zoning_document_reference_must_match_loaded_archive` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_existing_parcel_output_field_collision_is_rejected` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_every_source_zoning_field_is_required` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_raw_zoning_values_are_preserved_exactly` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_intersection_table_references_only_known_parcels_and_zones` via `_run`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_result_frames_are_independent_from_inputs` via `_run`.

**Complete source-ordered implementation**

```python
def _run(
    parcels: gpd.GeoDataFrame | None = None,
    zones: gpd.GeoDataFrame | None = None,
) -> ParcelZoningResult:
    return intersect_parcels_with_gpu_zoning(
        parcels if parcels is not None else _parcels(),
        _planning_document(zones),
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_row_for_source_zone`

**Exact signature**

```python
def _row_for_source_zone(result: ParcelZoningResult, source_id: str) -> pd.Series:
```

**Purpose**

Private `test` helper for row for source zone; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.Series`.
- Every observed return expression is reproduced without truncation:
```python
result.zones.loc[result.zones['source_zone_id'] == source_id].iloc[0]
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

- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_raw_zoning_values_are_preserved_exactly` via `_row_for_source_zone`.

**Complete source-ordered implementation**

```python
def _row_for_source_zone(result: ParcelZoningResult, source_id: str) -> pd.Series:
    return result.zones.loc[result.zones["source_zone_id"] == source_id].iloc[0]
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
assert stages.intersect_parcels_with_gpu_zoning is intersect_parcels_with_gpu_zoning
assert "intersect_parcels_with_gpu_zoning" in stages.__all__
assert not hasattr(stages, "PlanningZoningError")
assert not hasattr(stages, "ParcelZoningResult")
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_clean_high_level_api_is_exported() -> None:
    assert stages.intersect_parcels_with_gpu_zoning is intersect_parcels_with_gpu_zoning
    assert "intersect_parcels_with_gpu_zoning" in stages.__all__
    assert not hasattr(stages, "PlanningZoningError")
    assert not hasattr(stages, "ParcelZoningResult")
```

### `test_result_container_is_frozen`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _run()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(FrozenInstanceError):
        result.parcels = result.parcels.copy()
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_result_container_is_frozen() -> None:
    result = _run()

    with pytest.raises(FrozenInstanceError):
        result.parcels = result.parcels.copy()
```

### `test_one_parcel_fully_inside_one_zone`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _run(
        _parcels([_rectangle(0, 0, 10, 10)], identifiers=["P-1"]),
        _zones(
            [_rectangle(0, 0, 10, 10)],
            identifiers=["SOURCE-ZONE"],
            labels=["UAa"],
            long_labels=["Zone urbaine centrale"],
            zone_types=["U"],
        ),
    )
zone = result.zones.iloc[0]
relation = result.intersections.iloc[0]
parcel = result.parcels.iloc[0]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert isinstance(result, ParcelZoningResult)
assert len(result.parcels) == 1
assert len(result.zones) == 1
assert len(result.intersections) == 1
assert zone["planning_zone_id"] == f"GPU:{DOCUMENT_ID}:ZONE:SOURCE-ZONE"
assert zone["source_zone_id"] == "SOURCE-ZONE"
assert zone["zone_label_raw"] == "UAa"
assert zone["zone_long_label_raw"] == "Zone urbaine centrale"
assert zone["zone_type_raw"] == "U"
assert zone["regulation_filename_raw"] == "reglement-1.pdf"
assert zone["regulation_url_raw"].endswith("/1")
assert zone["source_document_reference_raw"] == ARCHIVE_NAME
assert zone["source_validity_date_raw"] == "2024-02-15"
assert zone["source_provider"] == "Géoportail de l'Urbanisme"
assert zone["source_portal"] == "GPU"
assert zone["source_commune_code"] == "31395"
assert zone["source_document_id"] == DOCUMENT_ID
assert zone["source_document_type"] == "PLU"
assert zone["source_archive_name"] == ARCHIVE_NAME
assert zone["source_archive_sha256"] == ARCHIVE_SHA256
assert zone["source_layer"] == SOURCE_LAYER
assert zone["source_standard_model"] == STANDARD_MODEL
assert zone["zone_area_m2"] == pytest.approx(100.0)
assert zone.geometry.area == pytest.approx(100.0)
assert result.zones.crs.to_epsg() == 2154
assert {
        "parcel_id",
        "planning_zone_id",
        "source_zone_id",
        "zone_type_raw",
        "zone_label_raw",
        "zone_long_label_raw",
        "relation_type",
        "parcel_metric_area_m2",
        "zone_area_m2",
        "intersection_area_m2",
        "parcel_share_pct",
        "zone_share_pct",
        "source_document_id",
        "source_archive_sha256",
        "source_layer",
        "source_validity_date_raw",
        "regulation_filename_raw",
    }.issubset(result.intersections.columns)
assert relation["relation_type"] == "AREA_OVERLAP"
assert relation["parcel_metric_area_m2"] == pytest.approx(100.0)
assert relation["zone_area_m2"] == pytest.approx(100.0)
assert relation["intersection_area_m2"] == pytest.approx(100.0)
assert relation["parcel_share_pct"] == pytest.approx(100.0)
assert relation["zone_share_pct"] == pytest.approx(100.0)
assert relation["source_document_id"] == DOCUMENT_ID
assert relation["source_archive_sha256"] == ARCHIVE_SHA256
assert relation["source_layer"] == SOURCE_LAYER
assert relation["source_validity_date_raw"] == "2024-02-15"
assert relation["regulation_filename_raw"] == "reglement-1.pdf"
assert parcel["zoning_area_match_count"] == 1
assert parcel["zoning_touch_only_count"] == 0
assert parcel["zoning_intersection_area_sum_m2"] == pytest.approx(100.0)
assert parcel["zoning_covered_union_area_m2"] == pytest.approx(100.0)
assert parcel["zoning_coverage_pct"] == pytest.approx(100.0)
assert parcel["zoning_gap_area_m2"] == pytest.approx(0.0)
assert parcel["zoning_overlap_excess_area_m2"] == pytest.approx(0.0)
assert parcel["dominant_source_zone_id"] == "SOURCE-ZONE"
assert parcel["dominant_zone_type_raw"] == "U"
assert parcel["dominant_zone_label_raw"] == "UAa"
assert parcel["dominant_zone_long_label_raw"] == "Zone urbaine centrale"
assert parcel["dominant_zone_intersection_area_m2"] == pytest.approx(100.0)
assert parcel["dominant_zone_share_pct"] == pytest.approx(100.0)
assert parcel["dominant_zone_tie_count"] == 1
assert parcel["planning_document_id"] == DOCUMENT_ID
assert parcel["planning_document_type"] == "PLU"
assert parcel["planning_archive_name"] == ARCHIVE_NAME
assert parcel["planning_archive_sha256"] == ARCHIVE_SHA256
assert parcel["planning_source_layer"] == SOURCE_LAYER
assert parcel["planning_standard_model"] == STANDARD_MODEL
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_one_parcel_fully_inside_one_zone() -> None:
    result = _run(
        _parcels([_rectangle(0, 0, 10, 10)], identifiers=["P-1"]),
        _zones(
            [_rectangle(0, 0, 10, 10)],
            identifiers=["SOURCE-ZONE"],
            labels=["UAa"],
            long_labels=["Zone urbaine centrale"],
            zone_types=["U"],
        ),
    )

    assert isinstance(result, ParcelZoningResult)
    assert len(result.parcels) == 1
    assert len(result.zones) == 1
    assert len(result.intersections) == 1
    zone = result.zones.iloc[0]
    assert zone["planning_zone_id"] == f"GPU:{DOCUMENT_ID}:ZONE:SOURCE-ZONE"
    assert zone["source_zone_id"] == "SOURCE-ZONE"
    assert zone["zone_label_raw"] == "UAa"
    assert zone["zone_long_label_raw"] == "Zone urbaine centrale"
    assert zone["zone_type_raw"] == "U"
    assert zone["regulation_filename_raw"] == "reglement-1.pdf"
    assert zone["regulation_url_raw"].endswith("/1")
    assert zone["source_document_reference_raw"] == ARCHIVE_NAME
    assert zone["source_validity_date_raw"] == "2024-02-15"
    assert zone["source_provider"] == "Géoportail de l'Urbanisme"
    assert zone["source_portal"] == "GPU"
    assert zone["source_commune_code"] == "31395"
    assert zone["source_document_id"] == DOCUMENT_ID
    assert zone["source_document_type"] == "PLU"
    assert zone["source_archive_name"] == ARCHIVE_NAME
    assert zone["source_archive_sha256"] == ARCHIVE_SHA256
    assert zone["source_layer"] == SOURCE_LAYER
    assert zone["source_standard_model"] == STANDARD_MODEL
    assert zone["zone_area_m2"] == pytest.approx(100.0)
    assert zone.geometry.area == pytest.approx(100.0)
    assert result.zones.crs.to_epsg() == 2154

    relation = result.intersections.iloc[0]
    assert {
        "parcel_id",
        "planning_zone_id",
        "source_zone_id",
        "zone_type_raw",
        "zone_label_raw",
        "zone_long_label_raw",
        "relation_type",
        "parcel_metric_area_m2",
        "zone_area_m2",
        "intersection_area_m2",
        "parcel_share_pct",
        "zone_share_pct",
        "source_document_id",
        "source_archive_sha256",
        "source_layer",
        "source_validity_date_raw",
        "regulation_filename_raw",
    }.issubset(result.intersections.columns)
    assert relation["relation_type"] == "AREA_OVERLAP"
    assert relation["parcel_metric_area_m2"] == pytest.approx(100.0)
    assert relation["zone_area_m2"] == pytest.approx(100.0)
    assert relation["intersection_area_m2"] == pytest.approx(100.0)
    assert relation["parcel_share_pct"] == pytest.approx(100.0)
    assert relation["zone_share_pct"] == pytest.approx(100.0)
    assert relation["source_document_id"] == DOCUMENT_ID
    assert relation["source_archive_sha256"] == ARCHIVE_SHA256
    assert relation["source_layer"] == SOURCE_LAYER
    assert relation["source_validity_date_raw"] == "2024-02-15"
    assert relation["regulation_filename_raw"] == "reglement-1.pdf"

    parcel = result.parcels.iloc[0]
    assert parcel["zoning_area_match_count"] == 1
    assert parcel["zoning_touch_only_count"] == 0
    assert parcel["zoning_intersection_area_sum_m2"] == pytest.approx(100.0)
    assert parcel["zoning_covered_union_area_m2"] == pytest.approx(100.0)
    assert parcel["zoning_coverage_pct"] == pytest.approx(100.0)
    assert parcel["zoning_gap_area_m2"] == pytest.approx(0.0)
    assert parcel["zoning_overlap_excess_area_m2"] == pytest.approx(0.0)
    assert parcel["dominant_source_zone_id"] == "SOURCE-ZONE"
    assert parcel["dominant_zone_type_raw"] == "U"
    assert parcel["dominant_zone_label_raw"] == "UAa"
    assert parcel["dominant_zone_long_label_raw"] == "Zone urbaine centrale"
    assert parcel["dominant_zone_intersection_area_m2"] == pytest.approx(100.0)
    assert parcel["dominant_zone_share_pct"] == pytest.approx(100.0)
    assert parcel["dominant_zone_tie_count"] == 1
    assert parcel["planning_document_id"] == DOCUMENT_ID
    assert parcel["planning_document_type"] == "PLU"
    assert parcel["planning_archive_name"] == ARCHIVE_NAME
    assert parcel["planning_archive_sha256"] == ARCHIVE_SHA256
    assert parcel["planning_source_layer"] == SOURCE_LAYER
    assert parcel["planning_standard_model"] == STANDARD_MODEL
```

### `test_parcel_split_across_two_zones`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _run(
        _parcels([_rectangle(0, 0, 10, 10)]),
        _zones(
            [_rectangle(0, 0, 4, 10), _rectangle(4, 0, 10, 10)],
            identifiers=["LEFT", "RIGHT"],
            labels=["UA", "UB"],
        ),
    )
parcel = result.parcels.iloc[0]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert len(result.intersections) == 2
assert set(result.intersections["relation_type"]) == {"AREA_OVERLAP"}
assert sorted(result.intersections["intersection_area_m2"]) == pytest.approx(
        [40.0, 60.0]
    )
assert parcel["zoning_area_match_count"] == 2
assert parcel["zoning_covered_union_area_m2"] == pytest.approx(100.0)
assert parcel["zoning_coverage_pct"] == pytest.approx(100.0)
assert parcel["dominant_source_zone_id"] == "RIGHT"
assert parcel["dominant_zone_share_pct"] == pytest.approx(60.0)
assert parcel["dominant_zone_tie_count"] == 1
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_parcel_split_across_two_zones() -> None:
    result = _run(
        _parcels([_rectangle(0, 0, 10, 10)]),
        _zones(
            [_rectangle(0, 0, 4, 10), _rectangle(4, 0, 10, 10)],
            identifiers=["LEFT", "RIGHT"],
            labels=["UA", "UB"],
        ),
    )

    assert len(result.intersections) == 2
    assert set(result.intersections["relation_type"]) == {"AREA_OVERLAP"}
    assert sorted(result.intersections["intersection_area_m2"]) == pytest.approx(
        [40.0, 60.0]
    )
    parcel = result.parcels.iloc[0]
    assert parcel["zoning_area_match_count"] == 2
    assert parcel["zoning_covered_union_area_m2"] == pytest.approx(100.0)
    assert parcel["zoning_coverage_pct"] == pytest.approx(100.0)
    assert parcel["dominant_source_zone_id"] == "RIGHT"
    assert parcel["dominant_zone_share_pct"] == pytest.approx(60.0)
    assert parcel["dominant_zone_tie_count"] == 1
```

### `test_dominant_zone_tie_is_deterministic`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _run(
        _parcels([_rectangle(0, 0, 10, 10)]),
        _zones(
            [_rectangle(5, 0, 10, 10), _rectangle(0, 0, 5, 10)],
            identifiers=["Z-ZONE", "A-ZONE"],
            labels=["UZ", "UA"],
        ),
    )
parcel = result.parcels.iloc[0]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert parcel["dominant_source_zone_id"] == "A-ZONE"
assert parcel["dominant_planning_zone_id"] == f"GPU:{DOCUMENT_ID}:ZONE:A-ZONE"
assert parcel["dominant_zone_intersection_area_m2"] == pytest.approx(50.0)
assert parcel["dominant_zone_share_pct"] == pytest.approx(50.0)
assert parcel["dominant_zone_tie_count"] == 2
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_dominant_zone_tie_is_deterministic() -> None:
    result = _run(
        _parcels([_rectangle(0, 0, 10, 10)]),
        _zones(
            [_rectangle(5, 0, 10, 10), _rectangle(0, 0, 5, 10)],
            identifiers=["Z-ZONE", "A-ZONE"],
            labels=["UZ", "UA"],
        ),
    )

    parcel = result.parcels.iloc[0]
    assert parcel["dominant_source_zone_id"] == "A-ZONE"
    assert parcel["dominant_planning_zone_id"] == f"GPU:{DOCUMENT_ID}:ZONE:A-ZONE"
    assert parcel["dominant_zone_intersection_area_m2"] == pytest.approx(50.0)
    assert parcel["dominant_zone_share_pct"] == pytest.approx(50.0)
    assert parcel["dominant_zone_tie_count"] == 2
```

### `test_touch_only_relation_is_preserved_but_never_dominant`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _run(
        _parcels([_rectangle(0, 0, 10, 10)]),
        _zones(
            [_rectangle(0, 0, 10, 10), _rectangle(10, 0, 20, 10)],
            identifiers=["AREA", "TOUCH"],
        ),
    )
relations = result.intersections.set_index("source_zone_id")
parcel = result.parcels.iloc[0]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert relations.loc["AREA", "relation_type"] == "AREA_OVERLAP"
assert relations.loc["TOUCH", "relation_type"] == "TOUCH_ONLY"
assert relations.loc["TOUCH", "intersection_area_m2"] == pytest.approx(0.0)
assert relations.loc["TOUCH", "parcel_share_pct"] == pytest.approx(0.0)
assert parcel["zoning_area_match_count"] == 1
assert parcel["zoning_touch_only_count"] == 1
assert parcel["dominant_source_zone_id"] == "AREA"
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_touch_only_relation_is_preserved_but_never_dominant() -> None:
    result = _run(
        _parcels([_rectangle(0, 0, 10, 10)]),
        _zones(
            [_rectangle(0, 0, 10, 10), _rectangle(10, 0, 20, 10)],
            identifiers=["AREA", "TOUCH"],
        ),
    )

    relations = result.intersections.set_index("source_zone_id")
    assert relations.loc["AREA", "relation_type"] == "AREA_OVERLAP"
    assert relations.loc["TOUCH", "relation_type"] == "TOUCH_ONLY"
    assert relations.loc["TOUCH", "intersection_area_m2"] == pytest.approx(0.0)
    assert relations.loc["TOUCH", "parcel_share_pct"] == pytest.approx(0.0)
    parcel = result.parcels.iloc[0]
    assert parcel["zoning_area_match_count"] == 1
    assert parcel["zoning_touch_only_count"] == 1
    assert parcel["dominant_source_zone_id"] == "AREA"
```

### `test_parcel_with_no_positive_area_zone_is_preserved`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _run(
        _parcels([_rectangle(0, 0, 10, 10)]),
        _zones([_rectangle(10, 0, 20, 10)], identifiers=["TOUCH"]),
    )
parcel = result.parcels.iloc[0]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert len(result.intersections) == 1
assert result.intersections.iloc[0]["relation_type"] == "TOUCH_ONLY"
assert parcel["zoning_area_match_count"] == 0
assert parcel["zoning_touch_only_count"] == 1
assert parcel["zoning_intersection_area_sum_m2"] == pytest.approx(0.0)
assert parcel["zoning_covered_union_area_m2"] == pytest.approx(0.0)
assert parcel["zoning_coverage_pct"] == pytest.approx(0.0)
assert parcel["zoning_gap_area_m2"] == pytest.approx(100.0)
assert pd.isna(parcel["dominant_planning_zone_id"])
assert pd.isna(parcel["dominant_source_zone_id"])
assert pd.isna(parcel["dominant_zone_intersection_area_m2"])
assert pd.isna(parcel["dominant_zone_share_pct"])
assert pd.isna(parcel["dominant_zone_tie_count"])
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_parcel_with_no_positive_area_zone_is_preserved() -> None:
    result = _run(
        _parcels([_rectangle(0, 0, 10, 10)]),
        _zones([_rectangle(10, 0, 20, 10)], identifiers=["TOUCH"]),
    )

    assert len(result.intersections) == 1
    assert result.intersections.iloc[0]["relation_type"] == "TOUCH_ONLY"
    parcel = result.parcels.iloc[0]
    assert parcel["zoning_area_match_count"] == 0
    assert parcel["zoning_touch_only_count"] == 1
    assert parcel["zoning_intersection_area_sum_m2"] == pytest.approx(0.0)
    assert parcel["zoning_covered_union_area_m2"] == pytest.approx(0.0)
    assert parcel["zoning_coverage_pct"] == pytest.approx(0.0)
    assert parcel["zoning_gap_area_m2"] == pytest.approx(100.0)
    assert pd.isna(parcel["dominant_planning_zone_id"])
    assert pd.isna(parcel["dominant_source_zone_id"])
    assert pd.isna(parcel["dominant_zone_intersection_area_m2"])
    assert pd.isna(parcel["dominant_zone_share_pct"])
    assert pd.isna(parcel["dominant_zone_tie_count"])
```

### `test_parcel_with_no_intersecting_zone_has_zero_coverage`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _run(
        _parcels([_rectangle(0, 0, 10, 10)]),
        _zones([_rectangle(20, 0, 30, 10)]),
    )
parcel = result.parcels.iloc[0]
for column in (
        "parcel_metric_area_m2",
        "zone_area_m2",
        "intersection_area_m2",
        "parcel_share_pct",
        "zone_share_pct",
    ):
        assert is_float_dtype(result.intersections[column])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert result.intersections.empty
assert parcel["zoning_area_match_count"] == 0
assert parcel["zoning_touch_only_count"] == 0
assert parcel["zoning_coverage_pct"] == pytest.approx(0.0)
assert parcel["zoning_gap_area_m2"] == pytest.approx(100.0)
assert tuple(result.intersections.columns) == (
        "parcel_id",
        "planning_zone_id",
        "source_zone_id",
        "zone_type_raw",
        "zone_label_raw",
        "zone_long_label_raw",
        "relation_type",
        "parcel_metric_area_m2",
        "zone_area_m2",
        "intersection_area_m2",
        "parcel_share_pct",
        "zone_share_pct",
        "source_document_id",
        "source_archive_sha256",
        "source_layer",
        "source_validity_date_raw",
        "regulation_filename_raw",
    )
assert is_integer_dtype(result.parcels["zoning_area_match_count"])
assert is_integer_dtype(result.parcels["zoning_touch_only_count"])
assert str(result.parcels["dominant_zone_tie_count"].dtype) == "Int64"
```

**Regression protected**

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_parcel_with_no_intersecting_zone_has_zero_coverage() -> None:
    result = _run(
        _parcels([_rectangle(0, 0, 10, 10)]),
        _zones([_rectangle(20, 0, 30, 10)]),
    )

    assert result.intersections.empty
    parcel = result.parcels.iloc[0]
    assert parcel["zoning_area_match_count"] == 0
    assert parcel["zoning_touch_only_count"] == 0
    assert parcel["zoning_coverage_pct"] == pytest.approx(0.0)
    assert parcel["zoning_gap_area_m2"] == pytest.approx(100.0)
    assert tuple(result.intersections.columns) == (
        "parcel_id",
        "planning_zone_id",
        "source_zone_id",
        "zone_type_raw",
        "zone_label_raw",
        "zone_long_label_raw",
        "relation_type",
        "parcel_metric_area_m2",
        "zone_area_m2",
        "intersection_area_m2",
        "parcel_share_pct",
        "zone_share_pct",
        "source_document_id",
        "source_archive_sha256",
        "source_layer",
        "source_validity_date_raw",
        "regulation_filename_raw",
    )
    for column in (
        "parcel_metric_area_m2",
        "zone_area_m2",
        "intersection_area_m2",
        "parcel_share_pct",
        "zone_share_pct",
    ):
        assert is_float_dtype(result.intersections[column])
    assert is_integer_dtype(result.parcels["zoning_area_match_count"])
    assert is_integer_dtype(result.parcels["zoning_touch_only_count"])
    assert str(result.parcels["dominant_zone_tie_count"].dtype) == "Int64"
```

### `test_overlapping_source_zones_expose_raw_sum_union_and_excess`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _run(
        _parcels([_rectangle(0, 0, 10, 10)]),
        _zones(
            [_rectangle(0, 0, 10, 10), _rectangle(0, 0, 5, 10)],
            identifiers=["WHOLE", "HALF"],
        ),
    )
parcel = result.parcels.iloc[0]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert parcel["zoning_intersection_area_sum_m2"] == pytest.approx(150.0)
assert parcel["zoning_covered_union_area_m2"] == pytest.approx(100.0)
assert parcel["zoning_overlap_excess_area_m2"] == pytest.approx(50.0)
assert parcel["zoning_coverage_pct"] == pytest.approx(100.0)
assert parcel["zoning_gap_area_m2"] == pytest.approx(0.0)
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_overlapping_source_zones_expose_raw_sum_union_and_excess() -> None:
    result = _run(
        _parcels([_rectangle(0, 0, 10, 10)]),
        _zones(
            [_rectangle(0, 0, 10, 10), _rectangle(0, 0, 5, 10)],
            identifiers=["WHOLE", "HALF"],
        ),
    )

    parcel = result.parcels.iloc[0]
    assert parcel["zoning_intersection_area_sum_m2"] == pytest.approx(150.0)
    assert parcel["zoning_covered_union_area_m2"] == pytest.approx(100.0)
    assert parcel["zoning_overlap_excess_area_m2"] == pytest.approx(50.0)
    assert parcel["zoning_coverage_pct"] == pytest.approx(100.0)
    assert parcel["zoning_gap_area_m2"] == pytest.approx(0.0)
```

### `test_polygon_and_multipolygon_parcels_are_supported`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `parcel_geometry`.

**Setup**

```python
result = _run(
        _parcels([parcel_geometry]),
        _zones([_rectangle(-5, -5, 20, 15)]),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert result.parcels.iloc[0]["zoning_coverage_pct"] == pytest.approx(100.0)
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_polygon_and_multipolygon_parcels_are_supported(
    parcel_geometry: object,
) -> None:
    result = _run(
        _parcels([parcel_geometry]),
        _zones([_rectangle(-5, -5, 20, 15)]),
    )

    assert result.parcels.iloc[0]["zoning_coverage_pct"] == pytest.approx(100.0)
```

### `test_polygon_and_multipolygon_zones_are_supported`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `expected_area`, `expected_coverage`, `zone_geometry`.

**Setup**

```python
result = _run(
        _parcels([_rectangle(0, 0, 10, 10)]),
        _zones([zone_geometry]),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert result.parcels.iloc[0]["zoning_coverage_pct"] == pytest.approx(
        expected_coverage
    )
assert result.zones.iloc[0]["zone_area_m2"] == pytest.approx(expected_area)
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_polygon_and_multipolygon_zones_are_supported(
    zone_geometry: object,
    expected_area: float,
    expected_coverage: float,
) -> None:
    result = _run(
        _parcels([_rectangle(0, 0, 10, 10)]),
        _zones([zone_geometry]),
    )

    assert result.parcels.iloc[0]["zoning_coverage_pct"] == pytest.approx(
        expected_coverage
    )
    assert result.zones.iloc[0]["zone_area_m2"] == pytest.approx(expected_area)
```

### `test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `parcel_crs`.

**Setup**

```python
parcels = _parcels([_rectangle(0, 0, 10, 10)], crs=parcel_crs)
result = _run(parcels, _zones([_rectangle(0, 0, 10, 10)]))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert result.parcels.crs == parcels.crs
assert result.intersections.iloc[0]["parcel_metric_area_m2"] == pytest.approx(
        100.0, abs=1e-5
    )
assert result.intersections.iloc[0]["intersection_area_m2"] == pytest.approx(
        100.0, abs=1e-5
    )
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93(
    parcel_crs: str,
) -> None:
    parcels = _parcels([_rectangle(0, 0, 10, 10)], crs=parcel_crs)
    result = _run(parcels, _zones([_rectangle(0, 0, 10, 10)]))

    assert result.parcels.crs == parcels.crs
    assert result.intersections.iloc[0]["parcel_metric_area_m2"] == pytest.approx(
        100.0, abs=1e-5
    )
    assert result.intersections.iloc[0]["intersection_area_m2"] == pytest.approx(
        100.0, abs=1e-5
    )
```

### `test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _zones([_rectangle(0, 0, 10, 10)], crs="IGNF:LAMB93")
result = _run(_parcels(), source)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert source.crs.to_string() == "IGNF:LAMB93"
assert result.zones.crs.to_epsg() == 2154
assert result.zones.iloc[0].geometry.area == pytest.approx(100.0)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154() -> None:
    source = _zones([_rectangle(0, 0, 10, 10)], crs="IGNF:LAMB93")
    result = _run(_parcels(), source)

    assert source.crs.to_string() == "IGNF:LAMB93"
    assert result.zones.crs.to_epsg() == 2154
    assert result.zones.iloc[0].geometry.area == pytest.approx(100.0)
```

### `test_missing_or_unusable_crs_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `message`, `parcels`, `zones`.

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
with pytest.raises(PlanningZoningError, match=message):
        _run(parcels, zones)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_missing_or_unusable_crs_is_rejected(
    parcels: gpd.GeoDataFrame,
    zones: gpd.GeoDataFrame,
    message: str,
) -> None:
    with pytest.raises(PlanningZoningError, match=message):
        _run(parcels, zones)
```

### `test_invalid_or_non_polygonal_parcel_geometry_is_rejected`

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
with pytest.raises(PlanningZoningError, match="geometry|Polygon"):
        _run(_parcels([geometry]), _zones())
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_invalid_or_non_polygonal_parcel_geometry_is_rejected(
    geometry: object,
) -> None:
    with pytest.raises(PlanningZoningError, match="geometry|Polygon"):
        _run(_parcels([geometry]), _zones())
```

### `test_invalid_or_non_polygonal_zone_geometry_is_rejected`

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
with pytest.raises(PlanningZoningError, match="geometry|Polygon"):
        _run(_parcels(), _zones([geometry]))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_invalid_or_non_polygonal_zone_geometry_is_rejected(
    geometry: object,
) -> None:
    with pytest.raises(PlanningZoningError, match="geometry|Polygon"):
        _run(_parcels(), _zones([geometry]))
```

### `test_invalid_parcel_id_is_rejected`

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
with pytest.raises(PlanningZoningError, match="parcel_id"):
        _run(_parcels(identifiers=[identifier]), _zones())
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_invalid_parcel_id_is_rejected(identifier: object) -> None:
    with pytest.raises(PlanningZoningError, match="parcel_id"):
        _run(_parcels(identifiers=[identifier]), _zones())
```

### `test_duplicate_parcel_id_is_rejected`

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
with pytest.raises(PlanningZoningError, match="parcel_id.*unique|duplicate"):
        _run(
            _parcels(
                [_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)],
                identifiers=["DUPLICATE", "DUPLICATE"],
            ),
            _zones(),
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_duplicate_parcel_id_is_rejected() -> None:
    with pytest.raises(PlanningZoningError, match="parcel_id.*unique|duplicate"):
        _run(
            _parcels(
                [_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)],
                identifiers=["DUPLICATE", "DUPLICATE"],
            ),
            _zones(),
        )
```

### `test_missing_parcel_id_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels().drop(columns=["parcel_id"])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningZoningError, match="parcel_id"):
        _run(parcels, _zones())
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_missing_parcel_id_is_rejected() -> None:
    parcels = _parcels().drop(columns=["parcel_id"])

    with pytest.raises(PlanningZoningError, match="parcel_id"):
        _run(parcels, _zones())
```

### `test_geometry_must_be_the_active_parcel_geometry_column`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels().rename_geometry("shape")
parcels["geometry"] = parcels["shape"]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningZoningError, match="active"):
        _run(parcels, _zones())
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_geometry_must_be_the_active_parcel_geometry_column() -> None:
    parcels = _parcels().rename_geometry("shape")
    parcels["geometry"] = parcels["shape"]

    with pytest.raises(PlanningZoningError, match="active"):
        _run(parcels, _zones())
```

### `test_invalid_source_zone_id_is_rejected`

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
with pytest.raises(PlanningZoningError, match="LIB_IDZONE|zone"):
        _run(_parcels(), _zones(identifiers=[identifier]))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_invalid_source_zone_id_is_rejected(identifier: object) -> None:
    with pytest.raises(PlanningZoningError, match="LIB_IDZONE|zone"):
        _run(_parcels(), _zones(identifiers=[identifier]))
```

### `test_duplicate_source_zone_id_is_rejected`

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
with pytest.raises(PlanningZoningError, match="LIB_IDZONE.*unique|duplicate"):
        _run(
            _parcels(),
            _zones(
                [_rectangle(0, 0, 5, 10), _rectangle(5, 0, 10, 10)],
                identifiers=["DUPLICATE", "DUPLICATE"],
            ),
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_duplicate_source_zone_id_is_rejected() -> None:
    with pytest.raises(PlanningZoningError, match="LIB_IDZONE.*unique|duplicate"):
        _run(
            _parcels(),
            _zones(
                [_rectangle(0, 0, 5, 10), _rectangle(5, 0, 10, 10)],
                identifiers=["DUPLICATE", "DUPLICATE"],
            ),
        )
```

### `test_zoning_document_reference_must_match_loaded_archive`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
zones = _zones(document_references=["31395_PLU_WRONG"])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningZoningError, match="IDURBA|document"):
        _run(_parcels(), zones)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_zoning_document_reference_must_match_loaded_archive() -> None:
    zones = _zones(document_references=["31395_PLU_WRONG"])

    with pytest.raises(PlanningZoningError, match="IDURBA|document"):
        _run(_parcels(), zones)
```

### `test_zoning_summary_lineage_and_count_must_match_bundle`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `bad_value`, `message`, `summary_field`.

**Setup**

```python
document = _planning_document()
summary = replace(document.zoning.summary, **{summary_field: bad_value})
zoning = replace(document.zoning, summary=summary)
corrupted = replace(document, zoning=zoning)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningZoningError, match=message):
        intersect_parcels_with_gpu_zoning(_parcels(), corrupted)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_zoning_summary_lineage_and_count_must_match_bundle(
    summary_field: str,
    bad_value: object,
    message: str,
) -> None:
    document = _planning_document()
    summary = replace(document.zoning.summary, **{summary_field: bad_value})
    zoning = replace(document.zoning, summary=summary)
    corrupted = replace(document, zoning=zoning)

    with pytest.raises(PlanningZoningError, match=message):
        intersect_parcels_with_gpu_zoning(_parcels(), corrupted)
```

### `test_existing_parcel_output_field_collision_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `reserved_column`.

**Setup**

```python
parcels = _parcels()
parcels[reserved_column] = "pre-existing-value"
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningZoningError, match="column|output|reserved|collision"):
        _run(parcels, _zones())
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_existing_parcel_output_field_collision_is_rejected(
    reserved_column: str,
) -> None:
    parcels = _parcels()
    parcels[reserved_column] = "pre-existing-value"

    with pytest.raises(PlanningZoningError, match="column|output|reserved|collision"):
        _run(parcels, _zones())
```

### `test_every_source_zoning_field_is_required`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `field`.

**Setup**

```python
zones = _zones().drop(columns=[field])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningZoningError, match=field):
        _run(_parcels(), zones)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_every_source_zoning_field_is_required(field: str) -> None:
    zones = _zones().drop(columns=[field])

    with pytest.raises(PlanningZoningError, match=field):
        _run(_parcels(), zones)
```

### `test_input_frames_are_not_mutated`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels(
        [_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)],
        identifiers=["P-2", "P-1"],
        crs="EPSG:4326",
    )
zones = _zones(
        [_rectangle(0, 0, 15, 15), _rectangle(20, 0, 35, 15)],
        identifiers=["U-1", "N-1"],
        labels=["UA", "N"],
        zone_types=["U", "N"],
    )
planning_document = _planning_document(zones)
parcels_before = deepcopy(parcels)
zones_before = deepcopy(planning_document.zoning.data)
assert_geodataframe_equal(parcels, parcels_before)
assert_geodataframe_equal(planning_document.zoning.data, zones_before)
```

**Action**

```python
intersect_parcels_with_gpu_zoning(parcels, planning_document)
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_input_frames_are_not_mutated() -> None:
    parcels = _parcels(
        [_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)],
        identifiers=["P-2", "P-1"],
        crs="EPSG:4326",
    )
    zones = _zones(
        [_rectangle(0, 0, 15, 15), _rectangle(20, 0, 35, 15)],
        identifiers=["U-1", "N-1"],
        labels=["UA", "N"],
        zone_types=["U", "N"],
    )
    planning_document = _planning_document(zones)
    parcels_before = deepcopy(parcels)
    zones_before = deepcopy(planning_document.zoning.data)

    intersect_parcels_with_gpu_zoning(parcels, planning_document)

    assert_geodataframe_equal(parcels, parcels_before)
    assert_geodataframe_equal(planning_document.zoning.data, zones_before)
```

### `test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels(
        [_rectangle(20, 0, 30, 10), _rectangle(0, 0, 10, 10)],
        identifiers=["P-2", "P-1"],
        crs="EPSG:4326",
    )
result = _run(
        parcels,
        _zones(
            [_rectangle(-5, -5, 15, 15), _rectangle(15, -5, 35, 15)],
            identifiers=["LEFT", "RIGHT"],
        ),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert len(result.parcels) == len(parcels)
assert result.parcels["parcel_id"].tolist() == parcels["parcel_id"].tolist()
assert result.parcels["existing_grid_value"].tolist() == parcels[
        "existing_grid_value"
    ].tolist()
assert result.parcels.crs == parcels.crs
assert result.parcels.geometry.reset_index(drop=True).equals(
        parcels.geometry.reset_index(drop=True)
    )
assert not result.parcels["parcel_id"].duplicated().any()
assert set(result.intersections["parcel_id"]).issubset(set(parcels["parcel_id"]))
assert not result.intersections.duplicated(
        subset=["parcel_id", "planning_zone_id"]
    ).any()
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved() -> None:
    parcels = _parcels(
        [_rectangle(20, 0, 30, 10), _rectangle(0, 0, 10, 10)],
        identifiers=["P-2", "P-1"],
        crs="EPSG:4326",
    )
    result = _run(
        parcels,
        _zones(
            [_rectangle(-5, -5, 15, 15), _rectangle(15, -5, 35, 15)],
            identifiers=["LEFT", "RIGHT"],
        ),
    )

    assert len(result.parcels) == len(parcels)
    assert result.parcels["parcel_id"].tolist() == parcels["parcel_id"].tolist()
    assert result.parcels["existing_grid_value"].tolist() == parcels[
        "existing_grid_value"
    ].tolist()
    assert result.parcels.crs == parcels.crs
    assert result.parcels.geometry.reset_index(drop=True).equals(
        parcels.geometry.reset_index(drop=True)
    )
    assert not result.parcels["parcel_id"].duplicated().any()
    assert set(result.intersections["parcel_id"]).issubset(set(parcels["parcel_id"]))
    assert not result.intersections.duplicated(
        subset=["parcel_id", "planning_zone_id"]
    ).any()
```

### `test_raw_zoning_values_are_preserved_exactly`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
zones = _zones(
        [_rectangle(0, 0, 5, 10), _rectangle(5, 0, 10, 10)],
        identifiers=["ID-É", "id-lower"],
        labels=["AUf", "Nh"],
        long_labels=["Libellé Étendu", None],
        zone_types=["AUc", "N"],
    )
zones.loc[zones.index[1], "NOMFIC"] = None
zones.loc[zones.index[1], "URLFIC"] = None
result = _run(_parcels(), zones)
first = _row_for_source_zone(result, "ID-É")
second = _row_for_source_zone(result, "id-lower")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert first["source_zone_id"] == "ID-É"
assert first["zone_label_raw"] == "AUf"
assert first["zone_long_label_raw"] == "Libellé Étendu"
assert first["zone_type_raw"] == "AUc"
assert second["source_zone_id"] == "id-lower"
assert second["zone_label_raw"] == "Nh"
assert pd.isna(second["zone_long_label_raw"])
assert second["zone_type_raw"] == "N"
assert pd.isna(second["regulation_filename_raw"])
assert pd.isna(second["regulation_url_raw"])
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_raw_zoning_values_are_preserved_exactly() -> None:
    zones = _zones(
        [_rectangle(0, 0, 5, 10), _rectangle(5, 0, 10, 10)],
        identifiers=["ID-É", "id-lower"],
        labels=["AUf", "Nh"],
        long_labels=["Libellé Étendu", None],
        zone_types=["AUc", "N"],
    )
    zones.loc[zones.index[1], "NOMFIC"] = None
    zones.loc[zones.index[1], "URLFIC"] = None
    result = _run(_parcels(), zones)

    first = _row_for_source_zone(result, "ID-É")
    second = _row_for_source_zone(result, "id-lower")
    assert first["source_zone_id"] == "ID-É"
    assert first["zone_label_raw"] == "AUf"
    assert first["zone_long_label_raw"] == "Libellé Étendu"
    assert first["zone_type_raw"] == "AUc"
    assert second["source_zone_id"] == "id-lower"
    assert second["zone_label_raw"] == "Nh"
    assert pd.isna(second["zone_long_label_raw"])
    assert second["zone_type_raw"] == "N"
    assert pd.isna(second["regulation_filename_raw"])
    assert pd.isna(second["regulation_url_raw"])
```

### `test_intersection_table_references_only_known_parcels_and_zones`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _run(
        _parcels(
            [_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)],
            identifiers=["P-1", "P-2"],
        ),
        _zones(
            [_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)],
            identifiers=["Z-1", "Z-2"],
        ),
    )
numeric = result.intersections[
        [
            "parcel_metric_area_m2",
            "zone_area_m2",
            "intersection_area_m2",
            "parcel_share_pct",
            "zone_share_pct",
        ]
    ]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert set(result.intersections["parcel_id"]) == {"P-1", "P-2"}
assert set(result.intersections["planning_zone_id"]) == set(
        result.zones["planning_zone_id"]
    )
assert not result.intersections.duplicated(
        subset=["parcel_id", "planning_zone_id"]
    ).any()
assert numeric.notna().all().all()
assert (numeric >= 0).all().all()
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_intersection_table_references_only_known_parcels_and_zones() -> None:
    result = _run(
        _parcels(
            [_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)],
            identifiers=["P-1", "P-2"],
        ),
        _zones(
            [_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)],
            identifiers=["Z-1", "Z-2"],
        ),
    )

    assert set(result.intersections["parcel_id"]) == {"P-1", "P-2"}
    assert set(result.intersections["planning_zone_id"]) == set(
        result.zones["planning_zone_id"]
    )
    assert not result.intersections.duplicated(
        subset=["parcel_id", "planning_zone_id"]
    ).any()
    numeric = result.intersections[
        [
            "parcel_metric_area_m2",
            "zone_area_m2",
            "intersection_area_m2",
            "parcel_share_pct",
            "zone_share_pct",
        ]
    ]
    assert numeric.notna().all().all()
    assert (numeric >= 0).all().all()
```

### `test_result_frames_are_independent_from_inputs`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels()
zones = _zones()
result = _run(parcels, zones)
parcel_snapshot = result.parcels.copy(deep=True)
zone_snapshot = result.zones.copy(deep=True)
intersections_snapshot = result.intersections.copy(deep=True)
parcels.loc[parcels.index[0], "existing_grid_value"] = -1
zones.loc[zones.index[0], "LIBELLE"] = "CHANGED"
assert_frame_equal(result.parcels, parcel_snapshot)
assert_frame_equal(result.zones, zone_snapshot)
assert_frame_equal(result.intersections, intersections_snapshot)
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
def test_result_frames_are_independent_from_inputs() -> None:
    parcels = _parcels()
    zones = _zones()
    result = _run(parcels, zones)
    parcel_snapshot = result.parcels.copy(deep=True)
    zone_snapshot = result.zones.copy(deep=True)
    intersections_snapshot = result.intersections.copy(deep=True)

    parcels.loc[parcels.index[0], "existing_grid_value"] = -1
    zones.loc[zones.index[0], "LIBELLE"] = "CHANGED"

    assert_frame_equal(result.parcels, parcel_snapshot)
    assert_frame_equal(result.zones, zone_snapshot)
    assert_frame_equal(result.intersections, intersections_snapshot)
```

### `test_source_complete_zoning_validation_accepts_physical_fixture`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels()
document = _physical_planning_document(tmp_path)
```

**Action**

```python
factual = intersect_parcels_with_gpu_zoning(parcels, document)
validate_normalized_planning_zoning_inputs(
        document,
        factual.parcels,
        factual.zones,
        factual.intersections,
    )
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Prevents a self-consistent but forged local object from bypassing the independent source-complete revalidation boundary.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_source_complete_zoning_validation_accepts_physical_fixture(
    tmp_path: Path,
) -> None:
    parcels = _parcels()
    document = _physical_planning_document(tmp_path)
    factual = intersect_parcels_with_gpu_zoning(parcels, document)

    validate_normalized_planning_zoning_inputs(
        document,
        factual.parcels,
        factual.zones,
        factual.intersections,
    )
```

### `test_source_complete_zoning_validation_rejects_coordinated_mutations`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `mutation`.

**Setup**

```python
source = _zones(
        [_rectangle(0, 0, 5, 10), _rectangle(5, 0, 10, 10)],
        identifiers=["ZONE-A", "ZONE-B"],
        labels=["UA", "UB"],
    )
parcels = _parcels()
document = _physical_planning_document(tmp_path, source)
zones = factual.zones.copy()
relations = factual.intersections.copy()
parcel_output = factual.parcels.copy()
if mutation == "label":
        zones.loc[0, "zone_label_raw"] = "FORGED"
        relations.loc[
            relations["planning_zone_id"].eq(zones.loc[0, "planning_zone_id"]),
            "zone_label_raw",
        ] = "FORGED"
    elif mutation == "source_id":
        old_planning_id = zones.loc[0, "planning_zone_id"]
        zones.loc[0, "source_zone_id"] = "FORGED-ID"
        zones.loc[0, "planning_zone_id"] = f"GPU:{DOCUMENT_ID}:ZONE:FORGED-ID"
        relations.loc[
            relations["planning_zone_id"].eq(old_planning_id),
            ["source_zone_id", "planning_zone_id"],
        ] = ["FORGED-ID", f"GPU:{DOCUMENT_ID}:ZONE:FORGED-ID"]
    elif mutation == "source_layer":
        zones["source_layer"] = "FORGED_LAYER"
        relations["source_layer"] = "FORGED_LAYER"
    elif mutation == "reorder":
        zones = zones.iloc[::-1].reset_index(drop=True)
    elif mutation == "missing_zone":
        zones = zones.iloc[:-1].copy()
    elif mutation == "extra_zone":
        extra = zones.iloc[[0]].copy()
        extra["source_zone_id"] = "EXTRA"
        extra["planning_zone_id"] = f"GPU:{DOCUMENT_ID}:ZONE:EXTRA"
        zones = gpd.GeoDataFrame(
            pd.concat([zones, extra], ignore_index=True),
            geometry="geometry",
            crs=zones.crs,
        )
    elif mutation == "missing_relation":
        relations = relations.iloc[:-1].copy()
    elif mutation == "extra_relation":
        relations = pd.concat([relations, relations.iloc[[0]]], ignore_index=True)
    elif mutation == "coherent_metric":
        relations.loc[0, "intersection_area_m2"] /= 2
        relations.loc[0, "parcel_share_pct"] /= 2
        relations.loc[0, "zone_share_pct"] /= 2
    else:
        parcel_output.loc[
            parcel_output.index[0],
            "dominant_planning_zone_id",
        ] = zones.loc[1, "planning_zone_id"]
```

**Action**

```python
factual = intersect_parcels_with_gpu_zoning(parcels, document)
```

**Expected result**

```python
with pytest.raises(PlanningZoningError, match="source|reconstruction|differs"):
        validate_normalized_planning_zoning_inputs(
            document,
            parcel_output,
            zones,
            relations,
        )
```

**Regression protected**

Prevents a self-consistent but forged local object from bypassing the independent source-complete revalidation boundary.

**Test boundary**

- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_source_complete_zoning_validation_rejects_coordinated_mutations(
    tmp_path: Path,
    mutation: str,
) -> None:
    source = _zones(
        [_rectangle(0, 0, 5, 10), _rectangle(5, 0, 10, 10)],
        identifiers=["ZONE-A", "ZONE-B"],
        labels=["UA", "UB"],
    )
    parcels = _parcels()
    document = _physical_planning_document(tmp_path, source)
    factual = intersect_parcels_with_gpu_zoning(parcels, document)
    zones = factual.zones.copy()
    relations = factual.intersections.copy()
    parcel_output = factual.parcels.copy()

    if mutation == "label":
        zones.loc[0, "zone_label_raw"] = "FORGED"
        relations.loc[
            relations["planning_zone_id"].eq(zones.loc[0, "planning_zone_id"]),
            "zone_label_raw",
        ] = "FORGED"
    elif mutation == "source_id":
        old_planning_id = zones.loc[0, "planning_zone_id"]
        zones.loc[0, "source_zone_id"] = "FORGED-ID"
        zones.loc[0, "planning_zone_id"] = f"GPU:{DOCUMENT_ID}:ZONE:FORGED-ID"
        relations.loc[
            relations["planning_zone_id"].eq(old_planning_id),
            ["source_zone_id", "planning_zone_id"],
        ] = ["FORGED-ID", f"GPU:{DOCUMENT_ID}:ZONE:FORGED-ID"]
    elif mutation == "source_layer":
        zones["source_layer"] = "FORGED_LAYER"
        relations["source_layer"] = "FORGED_LAYER"
    elif mutation == "reorder":
        zones = zones.iloc[::-1].reset_index(drop=True)
    elif mutation == "missing_zone":
        zones = zones.iloc[:-1].copy()
    elif mutation == "extra_zone":
        extra = zones.iloc[[0]].copy()
        extra["source_zone_id"] = "EXTRA"
        extra["planning_zone_id"] = f"GPU:{DOCUMENT_ID}:ZONE:EXTRA"
        zones = gpd.GeoDataFrame(
            pd.concat([zones, extra], ignore_index=True),
            geometry="geometry",
            crs=zones.crs,
        )
    elif mutation == "missing_relation":
        relations = relations.iloc[:-1].copy()
    elif mutation == "extra_relation":
        relations = pd.concat([relations, relations.iloc[[0]]], ignore_index=True)
    elif mutation == "coherent_metric":
        relations.loc[0, "intersection_area_m2"] /= 2
        relations.loc[0, "parcel_share_pct"] /= 2
        relations.loc[0, "zone_share_pct"] /= 2
    else:
        parcel_output.loc[
            parcel_output.index[0],
            "dominant_planning_zone_id",
        ] = zones.loc[1, "planning_zone_id"]

    with pytest.raises(PlanningZoningError, match="source|reconstruction|differs"):
        validate_normalized_planning_zoning_inputs(
            document,
            parcel_output,
            zones,
            relations,
        )
```

### `test_source_complete_zoning_validation_rejects_physical_tamper`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels()
document = _physical_planning_document(tmp_path)
with document.zoning.reference.dataset_path.open("ab") as stream:
        stream.write(b"tamper")
```

**Action**

```python
factual = intersect_parcels_with_gpu_zoning(parcels, document)
```

**Expected result**

```python
with pytest.raises(PlanningZoningError, match="Physical|source"):
        validate_normalized_planning_zoning_inputs(
            document,
            factual.parcels,
            factual.zones,
            factual.intersections,
        )
```

**Regression protected**

Prevents a self-consistent but forged local object from bypassing the independent source-complete revalidation boundary.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_source_complete_zoning_validation_rejects_physical_tamper(
    tmp_path: Path,
) -> None:
    parcels = _parcels()
    document = _physical_planning_document(tmp_path)
    factual = intersect_parcels_with_gpu_zoning(parcels, document)
    with document.zoning.reference.dataset_path.open("ab") as stream:
        stream.write(b"tamper")

    with pytest.raises(PlanningZoningError, match="Physical|source"):
        validate_normalized_planning_zoning_inputs(
            document,
            factual.parcels,
            factual.zones,
            factual.intersections,
        )
```

### `test_source_complete_zoning_validation_revalidates_physical_source_once`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels()
document = _physical_planning_document(tmp_path)
import landscout.stages.enrich_planning_zoning as module
original = module.revalidate_gpu_spatial_layer_sources
```

**Action**

```python
factual = intersect_parcels_with_gpu_zoning(parcels, document)
with patch.object(
        module,
        "revalidate_gpu_spatial_layer_sources",
        wraps=original,
    ) as revalidate:
        validate_normalized_planning_zoning_inputs(
            document,
            factual.parcels,
            factual.zones,
            factual.intersections,
        )
```

**Expected result**

```python
assert revalidate.call_count == 1
```

**Regression protected**

Prevents a self-consistent but forged local object from bypassing the independent source-complete revalidation boundary.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_source_complete_zoning_validation_revalidates_physical_source_once(
    tmp_path: Path,
) -> None:
    parcels = _parcels()
    document = _physical_planning_document(tmp_path)
    factual = intersect_parcels_with_gpu_zoning(parcels, document)
    import landscout.stages.enrich_planning_zoning as module

    original = module.revalidate_gpu_spatial_layer_sources
    with patch.object(
        module,
        "revalidate_gpu_spatial_layer_sources",
        wraps=original,
    ) as revalidate:
        validate_normalized_planning_zoning_inputs(
            document,
            factual.parcels,
            factual.zones,
            factual.intersections,
        )

    assert revalidate.call_count == 1
```


## 7. Data contracts

### `SOURCE_FIELDS` — required input frame fields (unordered when stored as a set)

```python
SOURCE_FIELDS = (
    "LIB_IDZONE",
    "LIBELLE",
    "LIBELONG",
    "TYPEZONE",
    "NOMFIC",
    "URLFIC",
    "IDURBA",
    "DATVALID",
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

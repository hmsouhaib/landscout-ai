# `tests/unit/test_enrich_planning_zoning.py`

## File identity

- Repository path: `tests/unit/test_enrich_planning_zoning.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `enrich_planning_zoning` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `b3d5429c8456644a97db55f6cf32d282a51549e4e3de81ff1632ca23806abbe7`

## 1. Purpose

Provides complete unit and regression coverage for the `enrich_planning_zoning` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import json` — required by the implementation paths and symbols documented below.
- `from copy import deepcopy` — required by the implementation paths and symbols documented below.
- `from dataclasses import FrozenInstanceError, replace` — required by the implementation paths and symbols documented below.
- `from hashlib import sha256` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.

### Third-party

- `from unittest.mock import patch` — required by the implementation paths and symbols documented below.
- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `import pytest` — required by the implementation paths and symbols documented below.
- `from geopandas.testing import assert_geodataframe_equal` — required by the implementation paths and symbols documented below.
- `from pandas.api.types import is_float_dtype, is_integer_dtype` — required by the implementation paths and symbols documented below.
- `from pandas.testing import assert_frame_equal` — required by the implementation paths and symbols documented below.
- `from shapely.geometry import ( LineString, MultiPolygon, Point, Polygon, )` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout import stages` — required by the implementation paths and symbols documented below.
- `from landscout.sources.gpu_fr import ( EXTRACTION_MANIFEST_NAME, GpuArchiveDownload, GpuDocumentMetadata, GpuExtractedFile, GpuExtraction, GpuInspectedLayer, GpuLayerSummary, GpuPlanningDocument, GpuSpatialLayerReference, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.enrich_planning_zoning import ( ParcelZoningResult, PlanningZoningError, _stabilize_area_relationships, intersect_parcels_with_gpu_zoning, validate_normalized_planning_zoning_inputs, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.planning_overlay import technical_overlay_tolerance` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `ARCHIVE_SHA256` | `"a" * 64` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ARCHIVE_NAME` | `"31395_PLU_20240215"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `DOCUMENT_ID` | `"doc-1"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SOURCE_LAYER` | `"31395_ZONE_URBA_20240215"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `STANDARD_MODEL` | `"CNIG PLU v2017"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SOURCE_FIELDS` | `( "LIB_IDZONE", "LIBELLE", "LIBELONG", "TYPEZONE", "NOMFIC", "URLFIC", "IDURBA", "DATVALID", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `LOCAL_ENGINEERING_CRS` | `'ENGCRS["Local",EDATUM["Unknown"],CS[Cartesian,2],' 'AXIS["x",east,LENGTHUNIT["metre",1]],' 'AXIS["y",north,LENGTHUNIT["metre",1]]]'` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `_rectangle`

**Signature**

```python
def _rectangle(x_min: float, y_min: float, x_max: float, y_max: float) -> Polygon:
```

**Purpose**

Implements rectangle according to the exact implementation and guards in this file.

**Inputs**

- `x_min` (`float`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `y_min` (`float`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `x_max` (`float`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `y_max` (`float`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Polygon`. Observed return expression(s): `Polygon([(x_min, y_min), (x_min, y_max), (x_max, y_max), (x_max, y_min), (x_min, y_min)])`.

**Algorithm**

1. Returns `Polygon([(x_min, y_min), (x_min, y_max), (x_max, y_max), (x_max, y_min), (x_min, y_min)])`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `Polygon`.

**Known repository callers**

- `tests/unit/test_enrich_planning_zoning.py` — `_parcels`
- `tests/unit/test_enrich_planning_zoning.py` — `_zones`
- `tests/unit/test_enrich_planning_zoning.py` — `test_dominant_zone_tie_is_deterministic`
- `tests/unit/test_enrich_planning_zoning.py` — `test_duplicate_parcel_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_duplicate_source_zone_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154`
- `tests/unit/test_enrich_planning_zoning.py` — `test_input_frames_are_not_mutated`
- `tests/unit/test_enrich_planning_zoning.py` — `test_intersection_table_references_only_known_parcels_and_zones`
- `tests/unit/test_enrich_planning_zoning.py` — `test_one_parcel_fully_inside_one_zone`
- `tests/unit/test_enrich_planning_zoning.py` — `test_overlapping_source_zones_expose_raw_sum_union_and_excess`
- `tests/unit/test_enrich_planning_zoning.py` — `test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved`
- `tests/unit/test_enrich_planning_zoning.py` — `test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93`
- `tests/unit/test_enrich_planning_zoning.py` — `test_parcel_split_across_two_zones`
- `tests/unit/test_enrich_planning_zoning.py` — `test_parcel_with_no_intersecting_zone_has_zero_coverage`
- `tests/unit/test_enrich_planning_zoning.py` — `test_parcel_with_no_positive_area_zone_is_preserved`
- `tests/unit/test_enrich_planning_zoning.py` — `test_polygon_and_multipolygon_parcels_are_supported`
- `tests/unit/test_enrich_planning_zoning.py` — `test_polygon_and_multipolygon_zones_are_supported`
- `tests/unit/test_enrich_planning_zoning.py` — `test_raw_zoning_values_are_preserved_exactly`
- `tests/unit/test_enrich_planning_zoning.py` — `test_source_complete_zoning_validation_rejects_coordinated_mutations`
- `tests/unit/test_enrich_planning_zoning.py` — `test_touch_only_relation_is_preserved_but_never_dominant`

**Tests**

- `tests/unit/test_enrich_planning_zoning.py::test_dominant_zone_tie_is_deterministic`
- `tests/unit/test_enrich_planning_zoning.py::test_duplicate_parcel_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_duplicate_source_zone_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154`
- `tests/unit/test_enrich_planning_zoning.py::test_input_frames_are_not_mutated`
- `tests/unit/test_enrich_planning_zoning.py::test_intersection_table_references_only_known_parcels_and_zones`
- `tests/unit/test_enrich_planning_zoning.py::test_one_parcel_fully_inside_one_zone`
- `tests/unit/test_enrich_planning_zoning.py::test_overlapping_source_zones_expose_raw_sum_union_and_excess`
- `tests/unit/test_enrich_planning_zoning.py::test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved`
- `tests/unit/test_enrich_planning_zoning.py::test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93`
- `tests/unit/test_enrich_planning_zoning.py::test_parcel_split_across_two_zones`
- `tests/unit/test_enrich_planning_zoning.py::test_parcel_with_no_intersecting_zone_has_zero_coverage`
- `tests/unit/test_enrich_planning_zoning.py::test_parcel_with_no_positive_area_zone_is_preserved`
- `tests/unit/test_enrich_planning_zoning.py::test_polygon_and_multipolygon_parcels_are_supported`
- `tests/unit/test_enrich_planning_zoning.py::test_polygon_and_multipolygon_zones_are_supported`
- `tests/unit/test_enrich_planning_zoning.py::test_raw_zoning_values_are_preserved_exactly`
- `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_rejects_coordinated_mutations`
- `tests/unit/test_enrich_planning_zoning.py::test_touch_only_relation_is_preserved_but_never_dominant`

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
) -> gpd.GeoDataFrame:
```

**Purpose**

Implements parcels according to the exact implementation and guards in this file.

**Inputs**

- `geometries` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `identifiers` (`list[object] | None`; optional/default `None`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `crs` (`str | None`; optional/default `'EPSG:2154'`) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `frame.to_crs(crs)`; `frame.set_crs(None, allow_override=True)`; `frame`.

**Algorithm**

1. Computes `values` from `geometries or [_rectangle(0, 0, 10, 10)]`.
2. Computes `ids` from `identifiers or [f'PARCEL-{position + 1}' for position in range(len(values))]`.
3. Computes `frame` from `gpd.GeoDataFrame({'parcel_id': ids, 'existing_grid_value': [100 + position for position in range(len(values))]}, geometry=values, crs='EPSG:2154', index=[50 + position for position in range(len(values))])`.
4. Checks `crs is None`. When true: Returns `frame.set_crs(None, allow_override=True)`.
5. Checks `crs == 'EPSG:2154'`. When true: Returns `frame`.
6. Returns `frame.to_crs(crs)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `frame.to_crs`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_rectangle`, `frame.set_crs`, `frame.to_crs`, `gpd.GeoDataFrame`, `len`, `range`.

**Known repository callers**

- `tests/unit/test_enrich_planning_zoning.py` — `_run`
- `tests/unit/test_enrich_planning_zoning.py` — `test_dominant_zone_tie_is_deterministic`
- `tests/unit/test_enrich_planning_zoning.py` — `test_duplicate_parcel_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_duplicate_source_zone_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_every_source_zoning_field_is_required`
- `tests/unit/test_enrich_planning_zoning.py` — `test_existing_parcel_output_field_collision_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_geometry_must_be_the_active_parcel_geometry_column`
- `tests/unit/test_enrich_planning_zoning.py` — `test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154`
- `tests/unit/test_enrich_planning_zoning.py` — `test_input_frames_are_not_mutated`
- `tests/unit/test_enrich_planning_zoning.py` — `test_intersection_table_references_only_known_parcels_and_zones`
- `tests/unit/test_enrich_planning_zoning.py` — `test_invalid_or_non_polygonal_parcel_geometry_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_invalid_or_non_polygonal_zone_geometry_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_invalid_parcel_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_invalid_source_zone_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_missing_or_unusable_crs_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_missing_parcel_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_one_parcel_fully_inside_one_zone`
- `tests/unit/test_enrich_planning_zoning.py` — `test_overlapping_source_zones_expose_raw_sum_union_and_excess`
- `tests/unit/test_enrich_planning_zoning.py` — `test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved`
- `tests/unit/test_enrich_planning_zoning.py` — `test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93`
- `tests/unit/test_enrich_planning_zoning.py` — `test_parcel_split_across_two_zones`
- `tests/unit/test_enrich_planning_zoning.py` — `test_parcel_with_no_intersecting_zone_has_zero_coverage`
- `tests/unit/test_enrich_planning_zoning.py` — `test_parcel_with_no_positive_area_zone_is_preserved`
- `tests/unit/test_enrich_planning_zoning.py` — `test_polygon_and_multipolygon_parcels_are_supported`
- `tests/unit/test_enrich_planning_zoning.py` — `test_polygon_and_multipolygon_zones_are_supported`
- `tests/unit/test_enrich_planning_zoning.py` — `test_raw_zoning_values_are_preserved_exactly`
- `tests/unit/test_enrich_planning_zoning.py` — `test_result_frames_are_independent_from_inputs`
- `tests/unit/test_enrich_planning_zoning.py` — `test_source_complete_zoning_validation_accepts_physical_fixture`
- `tests/unit/test_enrich_planning_zoning.py` — `test_source_complete_zoning_validation_rejects_coordinated_mutations`
- `tests/unit/test_enrich_planning_zoning.py` — `test_source_complete_zoning_validation_rejects_physical_tamper`
- `tests/unit/test_enrich_planning_zoning.py` — `test_source_complete_zoning_validation_revalidates_physical_source_once`
- `tests/unit/test_enrich_planning_zoning.py` — `test_touch_only_relation_is_preserved_but_never_dominant`
- `tests/unit/test_enrich_planning_zoning.py` — `test_zoning_document_reference_must_match_loaded_archive`
- `tests/unit/test_enrich_planning_zoning.py` — `test_zoning_summary_lineage_and_count_must_match_bundle`

**Tests**

- `tests/unit/test_enrich_planning_zoning.py::test_dominant_zone_tie_is_deterministic`
- `tests/unit/test_enrich_planning_zoning.py::test_duplicate_parcel_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_duplicate_source_zone_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_every_source_zoning_field_is_required`
- `tests/unit/test_enrich_planning_zoning.py::test_existing_parcel_output_field_collision_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_geometry_must_be_the_active_parcel_geometry_column`
- `tests/unit/test_enrich_planning_zoning.py::test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154`
- `tests/unit/test_enrich_planning_zoning.py::test_input_frames_are_not_mutated`
- `tests/unit/test_enrich_planning_zoning.py::test_intersection_table_references_only_known_parcels_and_zones`
- `tests/unit/test_enrich_planning_zoning.py::test_invalid_or_non_polygonal_parcel_geometry_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_invalid_or_non_polygonal_zone_geometry_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_invalid_parcel_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_invalid_source_zone_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_missing_or_unusable_crs_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_missing_parcel_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_one_parcel_fully_inside_one_zone`
- `tests/unit/test_enrich_planning_zoning.py::test_overlapping_source_zones_expose_raw_sum_union_and_excess`
- `tests/unit/test_enrich_planning_zoning.py::test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved`
- `tests/unit/test_enrich_planning_zoning.py::test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93`
- `tests/unit/test_enrich_planning_zoning.py::test_parcel_split_across_two_zones`
- `tests/unit/test_enrich_planning_zoning.py::test_parcel_with_no_intersecting_zone_has_zero_coverage`
- `tests/unit/test_enrich_planning_zoning.py::test_parcel_with_no_positive_area_zone_is_preserved`
- `tests/unit/test_enrich_planning_zoning.py::test_polygon_and_multipolygon_parcels_are_supported`
- `tests/unit/test_enrich_planning_zoning.py::test_polygon_and_multipolygon_zones_are_supported`
- `tests/unit/test_enrich_planning_zoning.py::test_raw_zoning_values_are_preserved_exactly`
- `tests/unit/test_enrich_planning_zoning.py::test_result_frames_are_independent_from_inputs`
- `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_accepts_physical_fixture`
- `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_rejects_coordinated_mutations`
- `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_rejects_physical_tamper`
- `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_revalidates_physical_source_once`
- `tests/unit/test_enrich_planning_zoning.py::test_touch_only_relation_is_preserved_but_never_dominant`
- `tests/unit/test_enrich_planning_zoning.py::test_zoning_document_reference_must_match_loaded_archive`
- `tests/unit/test_enrich_planning_zoning.py::test_zoning_summary_lineage_and_count_must_match_bundle`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_zones`

**Signature**

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

Implements zones according to the exact implementation and guards in this file.

**Inputs**

- `geometries` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `identifiers` (`list[object] | None`; optional/default `None`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `labels` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `long_labels` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zone_types` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `document_references` (`list[object] | None`; optional/default `None`) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `crs` (`str | None`; optional/default `'EPSG:2154'`) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `frame.to_crs(crs)`; `frame.set_crs(None, allow_override=True)`; `frame`; `frame.set_crs(crs, allow_override=True)`.

**Algorithm**

1. Computes `values` from `geometries or [_rectangle(-10, -10, 20, 20)]`.
2. Computes `count` from `len(values)`.
3. Computes `source_ids` from `identifiers or [f'ZONE-{position + 1}' for position in range(count)]`.
4. Computes `source_labels` from `labels or [f'U{position + 1}' for position in range(count)]`.
5. Computes `source_long_labels` from `long_labels or [f'Zone urbaine {position + 1}' for position in range(count)]`.
6. Computes `source_types` from `zone_types or ['U'] * count`.
7. Computes `source_documents` from `document_references or [ARCHIVE_NAME] * count`.
8. Computes `frame` from `gpd.GeoDataFrame({'LIB_IDZONE': source_ids, 'LIBELLE': source_labels, 'LIBELONG': source_long_labels, 'TYPEZONE': source_types, 'NOMFIC': [f'reglement-{position + 1}.pdf' for position in range(count)], 'URLFIC': [f'https://www.geoportail-urbanisme.gouv.fr/reglement/{position + 1}' for position in range(count)], 'IDURB…`.
9. Checks `crs is None`. When true: Returns `frame.set_crs(None, allow_override=True)`.
10. Checks `crs == 'EPSG:2154'`. When true: Returns `frame`.
11. Checks `crs == 'IGNF:LAMB93'`. When true: Returns `frame.set_crs(crs, allow_override=True)`.
12. Checks `crs == LOCAL_ENGINEERING_CRS`. When true: Returns `frame.set_crs(crs, allow_override=True)`.
13. Returns `frame.to_crs(crs)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `frame.to_crs`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_rectangle`, `frame.set_crs`, `frame.to_crs`, `gpd.GeoDataFrame`, `len`, `range`.

**Known repository callers**

- `tests/unit/test_enrich_planning_zoning.py` — `_physical_planning_document`
- `tests/unit/test_enrich_planning_zoning.py` — `_planning_document`
- `tests/unit/test_enrich_planning_zoning.py` — `test_dominant_zone_tie_is_deterministic`
- `tests/unit/test_enrich_planning_zoning.py` — `test_duplicate_parcel_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_duplicate_source_zone_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_every_source_zoning_field_is_required`
- `tests/unit/test_enrich_planning_zoning.py` — `test_existing_parcel_output_field_collision_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_geometry_must_be_the_active_parcel_geometry_column`
- `tests/unit/test_enrich_planning_zoning.py` — `test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154`
- `tests/unit/test_enrich_planning_zoning.py` — `test_input_frames_are_not_mutated`
- `tests/unit/test_enrich_planning_zoning.py` — `test_intersection_table_references_only_known_parcels_and_zones`
- `tests/unit/test_enrich_planning_zoning.py` — `test_invalid_or_non_polygonal_parcel_geometry_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_invalid_or_non_polygonal_zone_geometry_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_invalid_parcel_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_invalid_source_zone_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_missing_or_unusable_crs_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_missing_parcel_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_one_parcel_fully_inside_one_zone`
- `tests/unit/test_enrich_planning_zoning.py` — `test_overlapping_source_zones_expose_raw_sum_union_and_excess`
- `tests/unit/test_enrich_planning_zoning.py` — `test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved`
- `tests/unit/test_enrich_planning_zoning.py` — `test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93`
- `tests/unit/test_enrich_planning_zoning.py` — `test_parcel_split_across_two_zones`
- `tests/unit/test_enrich_planning_zoning.py` — `test_parcel_with_no_intersecting_zone_has_zero_coverage`
- `tests/unit/test_enrich_planning_zoning.py` — `test_parcel_with_no_positive_area_zone_is_preserved`
- `tests/unit/test_enrich_planning_zoning.py` — `test_polygon_and_multipolygon_parcels_are_supported`
- `tests/unit/test_enrich_planning_zoning.py` — `test_polygon_and_multipolygon_zones_are_supported`
- `tests/unit/test_enrich_planning_zoning.py` — `test_raw_zoning_values_are_preserved_exactly`
- `tests/unit/test_enrich_planning_zoning.py` — `test_result_frames_are_independent_from_inputs`
- `tests/unit/test_enrich_planning_zoning.py` — `test_source_complete_zoning_validation_rejects_coordinated_mutations`
- `tests/unit/test_enrich_planning_zoning.py` — `test_touch_only_relation_is_preserved_but_never_dominant`
- `tests/unit/test_enrich_planning_zoning.py` — `test_zoning_document_reference_must_match_loaded_archive`

**Tests**

- `tests/unit/test_enrich_planning_zoning.py::test_dominant_zone_tie_is_deterministic`
- `tests/unit/test_enrich_planning_zoning.py::test_duplicate_parcel_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_duplicate_source_zone_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_every_source_zoning_field_is_required`
- `tests/unit/test_enrich_planning_zoning.py::test_existing_parcel_output_field_collision_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_geometry_must_be_the_active_parcel_geometry_column`
- `tests/unit/test_enrich_planning_zoning.py::test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154`
- `tests/unit/test_enrich_planning_zoning.py::test_input_frames_are_not_mutated`
- `tests/unit/test_enrich_planning_zoning.py::test_intersection_table_references_only_known_parcels_and_zones`
- `tests/unit/test_enrich_planning_zoning.py::test_invalid_or_non_polygonal_parcel_geometry_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_invalid_or_non_polygonal_zone_geometry_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_invalid_parcel_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_invalid_source_zone_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_missing_or_unusable_crs_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_missing_parcel_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_one_parcel_fully_inside_one_zone`
- `tests/unit/test_enrich_planning_zoning.py::test_overlapping_source_zones_expose_raw_sum_union_and_excess`
- `tests/unit/test_enrich_planning_zoning.py::test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved`
- `tests/unit/test_enrich_planning_zoning.py::test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93`
- `tests/unit/test_enrich_planning_zoning.py::test_parcel_split_across_two_zones`
- `tests/unit/test_enrich_planning_zoning.py::test_parcel_with_no_intersecting_zone_has_zero_coverage`
- `tests/unit/test_enrich_planning_zoning.py::test_parcel_with_no_positive_area_zone_is_preserved`
- `tests/unit/test_enrich_planning_zoning.py::test_polygon_and_multipolygon_parcels_are_supported`
- `tests/unit/test_enrich_planning_zoning.py::test_polygon_and_multipolygon_zones_are_supported`
- `tests/unit/test_enrich_planning_zoning.py::test_raw_zoning_values_are_preserved_exactly`
- `tests/unit/test_enrich_planning_zoning.py::test_result_frames_are_independent_from_inputs`
- `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_rejects_coordinated_mutations`
- `tests/unit/test_enrich_planning_zoning.py::test_touch_only_relation_is_preserved_but_never_dominant`
- `tests/unit/test_enrich_planning_zoning.py::test_zoning_document_reference_must_match_loaded_archive`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_planning_document`

**Signature**

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

Implements planning document according to the exact implementation and guards in this file.

**Inputs**

- `zoning` (`gpd.GeoDataFrame | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `archive_name` (`str`; optional/default `ARCHIVE_NAME`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `document_id` (`str`; optional/default `DOCUMENT_ID`) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_layer` (`str`; optional/default `SOURCE_LAYER`) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuPlanningDocument`. Observed return expression(s): `GpuPlanningDocument(extraction=extraction, all_spatial_layers=(reference,), zoning=inspected, related_layers=())`.

**Algorithm**

1. Computes `data` from `zoning if zoning is not None else _zones()`.
2. Computes `document` from `GpuDocumentMetadata(provider="Géoportail de l'Urbanisme", portal='GPU', commune_code='31395', partition='DU_31395', document_id=document_id, document_family='DU', document_type='PLU', document_title="Plan local d'urbanisme de Muret", status='document.production', legal_status='APPROVED', effective_status='EN_VIGUEUR',…`.
3. Computes `archive` from `GpuArchiveDownload(document=document, download_timestamp='2026-08-12T10:00:00+00:00', filename=f'{archive_name}.zip', archive_format='zip', file_size=1234, sha256=ARCHIVE_SHA256, path=Path('data/cache/gpu/synthetic.zip'), cache_hit=True)`.
4. Computes `extraction` from `GpuExtraction(archive=archive, extraction_root=Path('data/cache/gpu/extracted/synthetic'), files=(), standard_models=(STANDARD_MODEL,), cache_hit=True)`.
5. Computes `reference` from `GpuSpatialLayerReference(dataset_path=Path('data/cache/gpu/extracted/synthetic/planning.gpkg'), source_layer=source_layer, driver='GPKG')`.
6. Computes `geometry` from `data.geometry`.
7. Computes `non_null` from `pd.Series([value is not None for value in geometry], index=geometry.index, dtype=bool)`.
8. Computes `non_empty` from `non_null & ~geometry.is_empty`.
9. Computes `summary` from `GpuLayerSummary(source_document_id=document_id, source_archive_sha256=ARCHIVE_SHA256, source_layer=source_layer, crs='UNKNOWN' if data.crs is None else data.crs.to_string(), feature_count=len(data), columns=tuple((str(column) for column in data.columns)), dtypes=tuple(((str(column), str(dtype)) for column, dtype in da…`.
10. Computes `inspected` from `GpuInspectedLayer(logical_name='zoning', reference=reference, data=data, summary=summary)`.
11. Returns `GpuPlanningDocument(extraction=extraction, all_spatial_layers=(reference,), zoning=inspected, related_layers=())`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `GpuArchiveDownload`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `(non_empty & ~geometry.is_valid).sum`, `(non_null & geometry.is_empty).sum`, `(~non_null).sum`, `GpuArchiveDownload`, `GpuDocumentMetadata`, `GpuExtraction`, `GpuInspectedLayer`, `GpuLayerSummary`, `GpuPlanningDocument`, `GpuSpatialLayerReference`, `Path`, `_zones`, `data.crs.to_string`, `data.dtypes.items`, `data[column].isna`, `data[column].isna().sum`, `geometry[non_null].geom_type.value_counts`, `geometry[non_null].geom_type.value_counts().items`, `int`, `len`, `pd.Series`, `str`, `tuple`.

**Known repository callers**

- `tests/unit/test_enrich_planning_zoning.py` — `_physical_planning_document`
- `tests/unit/test_enrich_planning_zoning.py` — `_run`
- `tests/unit/test_enrich_planning_zoning.py` — `test_input_frames_are_not_mutated`
- `tests/unit/test_enrich_planning_zoning.py` — `test_zoning_summary_lineage_and_count_must_match_bundle`

**Tests**

- `tests/unit/test_enrich_planning_zoning.py::test_input_frames_are_not_mutated`
- `tests/unit/test_enrich_planning_zoning.py::test_zoning_summary_lineage_and_count_must_match_bundle`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_physical_planning_document`

**Signature**

```python
def _physical_planning_document(
    tmp_path: Path,
    zoning: gpd.GeoDataFrame | None = None,
) -> GpuPlanningDocument:
```

**Purpose**

Implements physical planning document according to the exact implementation and guards in this file.

**Inputs**

- `tmp_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zoning` (`gpd.GeoDataFrame | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuPlanningDocument`. Observed return expression(s): `replace(base, extraction=extraction, all_spatial_layers=(reference,), zoning=inspected)`.

**Algorithm**

1. Computes `root` from `tmp_path / 'extraction'`.
2. Calls `root.mkdir(parents=True)` for its validation or side effect.
3. Computes `path` from `root / 'zoning.gpkg'`.
4. Computes `source` from `zoning if zoning is not None else _zones()`.
5. Calls `source.to_file(path, layer=SOURCE_LAYER, driver='GPKG', engine='pyogrio', index=False)` for its validation or side effect.
6. Computes `reread` from `gpd.read_file(path, layer=SOURCE_LAYER, engine='pyogrio')`.
7. Computes `base` from `_planning_document(reread)`.
8. Computes `reference` from `replace(base.zoning.reference, dataset_path=path, source_layer=SOURCE_LAYER, driver='GPKG')`.
9. Computes `inspected` from `replace(base.zoning, reference=reference, data=reread, summary=replace(base.zoning.summary, source_layer=SOURCE_LAYER))`.
10. Computes `inventory` from `(GpuExtractedFile(relative_path='zoning.gpkg', file_type='gpkg', size_bytes=path.stat().st_size, sha256=sha256(path.read_bytes()).hexdigest(), category='SPATIAL_DATA'),)`.
11. Calls `(root / EXTRACTION_MANIFEST_NAME).write_text(json.dumps({'schema_version': 2, 'archive_sha256': ARCHIVE_SHA256, 'files': [{'relative_path': item.relative_path, 'size_bytes': item.size_bytes, 'sha256': item.sha256} for item in inventory]}, sort_keys=True, separators=(',', ':')), encoding='utf-8')` for its validation or side effect.
12. Computes `extraction` from `replace(base.extraction, extraction_root=root, files=inventory)`.
13. Returns `replace(base, extraction=extraction, all_spatial_layers=(reference,), zoning=inspected)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `(root / EXTRACTION_MANIFEST_NAME).write_text`, `gpd.read_file`, `path.read_bytes`, `replace`, `root.mkdir`, `sha256(path.read_bytes()).hexdigest`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `(root / EXTRACTION_MANIFEST_NAME).write_text`, `GpuExtractedFile`, `_planning_document`, `_zones`, `gpd.read_file`, `json.dumps`, `path.read_bytes`, `path.stat`, `replace`, `root.mkdir`, `sha256`, `sha256(path.read_bytes()).hexdigest`, `source.to_file`.

**Known repository callers**

- `tests/unit/test_enrich_planning_zoning.py` — `test_source_complete_zoning_validation_accepts_physical_fixture`
- `tests/unit/test_enrich_planning_zoning.py` — `test_source_complete_zoning_validation_rejects_coordinated_mutations`
- `tests/unit/test_enrich_planning_zoning.py` — `test_source_complete_zoning_validation_rejects_physical_tamper`
- `tests/unit/test_enrich_planning_zoning.py` — `test_source_complete_zoning_validation_revalidates_physical_source_once`

**Tests**

- `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_accepts_physical_fixture`
- `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_rejects_coordinated_mutations`
- `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_rejects_physical_tamper`
- `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_revalidates_physical_source_once`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_run`

**Signature**

```python
def _run(
    parcels: gpd.GeoDataFrame | None = None,
    zones: gpd.GeoDataFrame | None = None,
) -> ParcelZoningResult:
```

**Purpose**

Implements run according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`gpd.GeoDataFrame | None`; optional/default `None`) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zones` (`gpd.GeoDataFrame | None`; optional/default `None`) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `ParcelZoningResult`. Observed return expression(s): `intersect_parcels_with_gpu_zoning(parcels if parcels is not None else _parcels(), _planning_document(zones))`.

**Algorithm**

1. Returns `intersect_parcels_with_gpu_zoning(parcels if parcels is not None else _parcels(), _planning_document(zones))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_parcels`, `_planning_document`, `intersect_parcels_with_gpu_zoning`.

**Known repository callers**

- `tests/unit/test_enrich_planning_zoning.py` — `test_dominant_zone_tie_is_deterministic`
- `tests/unit/test_enrich_planning_zoning.py` — `test_duplicate_parcel_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_duplicate_source_zone_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_every_source_zoning_field_is_required`
- `tests/unit/test_enrich_planning_zoning.py` — `test_existing_parcel_output_field_collision_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_geometry_must_be_the_active_parcel_geometry_column`
- `tests/unit/test_enrich_planning_zoning.py` — `test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154`
- `tests/unit/test_enrich_planning_zoning.py` — `test_intersection_table_references_only_known_parcels_and_zones`
- `tests/unit/test_enrich_planning_zoning.py` — `test_invalid_or_non_polygonal_parcel_geometry_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_invalid_or_non_polygonal_zone_geometry_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_invalid_parcel_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_invalid_source_zone_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_missing_or_unusable_crs_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_missing_parcel_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py` — `test_one_parcel_fully_inside_one_zone`
- `tests/unit/test_enrich_planning_zoning.py` — `test_overlapping_source_zones_expose_raw_sum_union_and_excess`
- `tests/unit/test_enrich_planning_zoning.py` — `test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved`
- `tests/unit/test_enrich_planning_zoning.py` — `test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93`
- `tests/unit/test_enrich_planning_zoning.py` — `test_parcel_split_across_two_zones`
- `tests/unit/test_enrich_planning_zoning.py` — `test_parcel_with_no_intersecting_zone_has_zero_coverage`
- `tests/unit/test_enrich_planning_zoning.py` — `test_parcel_with_no_positive_area_zone_is_preserved`
- `tests/unit/test_enrich_planning_zoning.py` — `test_polygon_and_multipolygon_parcels_are_supported`
- `tests/unit/test_enrich_planning_zoning.py` — `test_polygon_and_multipolygon_zones_are_supported`
- `tests/unit/test_enrich_planning_zoning.py` — `test_raw_zoning_values_are_preserved_exactly`
- `tests/unit/test_enrich_planning_zoning.py` — `test_result_container_is_frozen`
- `tests/unit/test_enrich_planning_zoning.py` — `test_result_frames_are_independent_from_inputs`
- `tests/unit/test_enrich_planning_zoning.py` — `test_touch_only_relation_is_preserved_but_never_dominant`
- `tests/unit/test_enrich_planning_zoning.py` — `test_zoning_document_reference_must_match_loaded_archive`

**Tests**

- `tests/unit/test_enrich_planning_zoning.py::test_dominant_zone_tie_is_deterministic`
- `tests/unit/test_enrich_planning_zoning.py::test_duplicate_parcel_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_duplicate_source_zone_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_every_source_zoning_field_is_required`
- `tests/unit/test_enrich_planning_zoning.py::test_existing_parcel_output_field_collision_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_geometry_must_be_the_active_parcel_geometry_column`
- `tests/unit/test_enrich_planning_zoning.py::test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154`
- `tests/unit/test_enrich_planning_zoning.py::test_intersection_table_references_only_known_parcels_and_zones`
- `tests/unit/test_enrich_planning_zoning.py::test_invalid_or_non_polygonal_parcel_geometry_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_invalid_or_non_polygonal_zone_geometry_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_invalid_parcel_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_invalid_source_zone_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_missing_or_unusable_crs_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_missing_parcel_id_is_rejected`
- `tests/unit/test_enrich_planning_zoning.py::test_one_parcel_fully_inside_one_zone`
- `tests/unit/test_enrich_planning_zoning.py::test_overlapping_source_zones_expose_raw_sum_union_and_excess`
- `tests/unit/test_enrich_planning_zoning.py::test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved`
- `tests/unit/test_enrich_planning_zoning.py::test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93`
- `tests/unit/test_enrich_planning_zoning.py::test_parcel_split_across_two_zones`
- `tests/unit/test_enrich_planning_zoning.py::test_parcel_with_no_intersecting_zone_has_zero_coverage`
- `tests/unit/test_enrich_planning_zoning.py::test_parcel_with_no_positive_area_zone_is_preserved`
- `tests/unit/test_enrich_planning_zoning.py::test_polygon_and_multipolygon_parcels_are_supported`
- `tests/unit/test_enrich_planning_zoning.py::test_polygon_and_multipolygon_zones_are_supported`
- `tests/unit/test_enrich_planning_zoning.py::test_raw_zoning_values_are_preserved_exactly`
- `tests/unit/test_enrich_planning_zoning.py::test_result_container_is_frozen`
- `tests/unit/test_enrich_planning_zoning.py::test_result_frames_are_independent_from_inputs`
- `tests/unit/test_enrich_planning_zoning.py::test_touch_only_relation_is_preserved_but_never_dominant`
- `tests/unit/test_enrich_planning_zoning.py::test_zoning_document_reference_must_match_loaded_archive`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_row_for_source_zone`

**Signature**

```python
def _row_for_source_zone(result: ParcelZoningResult, source_id: str) -> pd.Series:
```

**Purpose**

Implements row for source zone according to the exact implementation and guards in this file.

**Inputs**

- `result` (`ParcelZoningResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_id` (`str`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.Series`. Observed return expression(s): `result.zones.loc[result.zones['source_zone_id'] == source_id].iloc[0]`.

**Algorithm**

1. Returns `result.zones.loc[result.zones['source_zone_id'] == source_id].iloc[0]`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

- `tests/unit/test_enrich_planning_zoning.py` — `test_raw_zoning_values_are_preserved_exactly`

**Tests**

- `tests/unit/test_enrich_planning_zoning.py::test_raw_zoning_values_are_preserved_exactly`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_shared_overlay_tolerance_preserves_zoning_numerical_behavior`

**Signature**

```python
def test_shared_overlay_tolerance_preserves_zoning_numerical_behavior() -> None:
```

**Purpose**

Protects the `shared overlay tolerance preserves zoning numerical behavior` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `(covered, gap, excess)` from `_stabilize_area_relationships(100.0, 100.0 + 5e-07, 100.0 + 5e-07)`.
- Enters managed context(s) `pytest.raises(PlanningZoningError, match='materially exceeds')` and executes: Calls `_stabilize_area_relationships(100.0, 100.0 + 2e-06, 100.0 + 2e-06)` for its validation or side effect.

**Action**

- Calls `_stabilize_area_relationships`, `technical_overlay_tolerance`.

**Expected result**

- Direct assertions: `assert technical_overlay_tolerance(100.0) == pytest.approx(1e-06)`; `assert covered == pytest.approx(100.0)`; `assert gap == pytest.approx(0.0)`; `assert excess == pytest.approx(5e-07)`.
- Expected exception contexts: `with pytest.raises(PlanningZoningError, match='materially exceeds'): _stabilize_area_relationships(100.0, 100.0 + 2e-06, 100.0 + 2e-06)`.

**Regression protected**

- Protects the exact `shared overlay tolerance preserves zoning numerical behavior` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_stabilize_area_relationships`, `pytest.approx`, `pytest.raises`, `technical_overlay_tolerance`.

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

- Calls `hasattr`.

**Expected result**

- Direct assertions: `assert stages.intersect_parcels_with_gpu_zoning is intersect_parcels_with_gpu_zoning`; `assert 'intersect_parcels_with_gpu_zoning' in stages.__all__`; `assert not hasattr(stages, 'PlanningZoningError')`; `assert not hasattr(stages, 'ParcelZoningResult')`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `clean high level api is exported` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `hasattr`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_result_container_is_frozen`

**Signature**

```python
def test_result_container_is_frozen() -> None:
```

**Purpose**

Protects the `result container is frozen` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_run()`.
- Enters managed context(s) `pytest.raises(FrozenInstanceError)` and executes: Computes `result.parcels` from `result.parcels.copy()`.

**Action**

- Calls `_run`, `result.parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(FrozenInstanceError): result.parcels = result.parcels.copy()`.

**Regression protected**

- Protects the exact `result container is frozen` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_run`, `pytest.raises`, `result.parcels.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_one_parcel_fully_inside_one_zone`

**Signature**

```python
def test_one_parcel_fully_inside_one_zone() -> None:
```

**Purpose**

Protects the `one parcel fully inside one zone` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `result` from `_run(_parcels([_rectangle(0, 0, 10, 10)], identifiers=['P-1']), _zones([_rectangle(0, 0, 10, 10)], identifiers=['SOURCE-ZONE'], labels=['UAa'], long_labels=['Zone urbaine centrale'], zone_types=['U']))`.
- Computes `zone` from `result.zones.iloc[0]`.
- Computes `relation` from `result.intersections.iloc[0]`.
- Computes `parcel` from `result.parcels.iloc[0]`.

**Action**

- Calls `_parcels`, `_rectangle`, `_run`, `_zones`, `isinstance`, `result.zones.crs.to_epsg`, `zone['regulation_url_raw'].endswith`, `{'parcel_id', 'planning_zone_id', 'source_zone_id', 'zone_type_raw', 'zone_label_raw', 'zone_long_label_raw', 'relation_type', 'parcel_metric_area_m2', 'zone_area_m2', 'intersection_area_m2', 'parcel_share_pct', 'zone_share_pct', 'source_document_id', 'source_archive_sha256', 'source_layer', 'source_validity_date_raw', 'regulation_filename_raw'}.issubset`.

**Expected result**

- Direct assertions: `assert isinstance(result, ParcelZoningResult)`; `assert len(result.parcels) == 1`; `assert len(result.zones) == 1`; `assert len(result.intersections) == 1`; `assert zone['planning_zone_id'] == f'GPU:{DOCUMENT_ID}:ZONE:SOURCE-ZONE'`; `assert zone['source_zone_id'] == 'SOURCE-ZONE'`; `assert zone['zone_label_raw'] == 'UAa'`; `assert zone['zone_long_label_raw'] == 'Zone urbaine centrale'`; `assert zone['zone_type_raw'] == 'U'`; `assert zone['regulation_filename_raw'] == 'reglement-1.pdf'`; `assert zone['regulation_url_raw'].endswith('/1')`; `assert zone['source_document_reference_raw'] == ARCHIVE_NAME`; `assert zone['source_validity_date_raw'] == '2024-02-15'`; `assert zone['source_provider'] == "Géoportail de l'Urbanisme"`; `assert zone['source_portal'] == 'GPU'`; `assert zone['source_commune_code'] == '31395'`; `assert zone['source_document_id'] == DOCUMENT_ID`; `assert zone['source_document_type'] == 'PLU'`; `assert zone['source_archive_name'] == ARCHIVE_NAME`; `assert zone['source_archive_sha256'] == ARCHIVE_SHA256`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `one parcel fully inside one zone` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_rectangle`, `_run`, `_zones`, `isinstance`, `len`, `pytest.approx`, `result.zones.crs.to_epsg`, `zone['regulation_url_raw'].endswith`, `{'parcel_id', 'planning_zone_id', 'source_zone_id', 'zone_type_raw', 'zone_label_raw', 'zone_long_label_raw', 'relation_type', 'parcel_metric_area_m2', 'zone_area_m2', 'intersection_area_m2', 'parcel_share_pct', 'zone_share_pct', 'source_document_id', 'source_archive_sha256', 'source_layer', 'source_validity_date_raw', 'regulation_filename_raw'}.issubset`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_parcel_split_across_two_zones`

**Signature**

```python
def test_parcel_split_across_two_zones() -> None:
```

**Purpose**

Protects the `parcel split across two zones` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_run(_parcels([_rectangle(0, 0, 10, 10)]), _zones([_rectangle(0, 0, 4, 10), _rectangle(4, 0, 10, 10)], identifiers=['LEFT', 'RIGHT'], labels=['UA', 'UB']))`.
- Computes `parcel` from `result.parcels.iloc[0]`.

**Action**

- Calls `_parcels`, `_rectangle`, `_run`, `_zones`, `sorted`.

**Expected result**

- Direct assertions: `assert len(result.intersections) == 2`; `assert set(result.intersections['relation_type']) == {'AREA_OVERLAP'}`; `assert sorted(result.intersections['intersection_area_m2']) == pytest.approx([40.0, 60.0])`; `assert parcel['zoning_area_match_count'] == 2`; `assert parcel['zoning_covered_union_area_m2'] == pytest.approx(100.0)`; `assert parcel['zoning_coverage_pct'] == pytest.approx(100.0)`; `assert parcel['dominant_source_zone_id'] == 'RIGHT'`; `assert parcel['dominant_zone_share_pct'] == pytest.approx(60.0)`; `assert parcel['dominant_zone_tie_count'] == 1`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `parcel split across two zones` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_rectangle`, `_run`, `_zones`, `len`, `pytest.approx`, `set`, `sorted`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_dominant_zone_tie_is_deterministic`

**Signature**

```python
def test_dominant_zone_tie_is_deterministic() -> None:
```

**Purpose**

Protects the `dominant zone tie is deterministic` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_run(_parcels([_rectangle(0, 0, 10, 10)]), _zones([_rectangle(5, 0, 10, 10), _rectangle(0, 0, 5, 10)], identifiers=['Z-ZONE', 'A-ZONE'], labels=['UZ', 'UA']))`.
- Computes `parcel` from `result.parcels.iloc[0]`.

**Action**

- Calls `_parcels`, `_rectangle`, `_run`, `_zones`.

**Expected result**

- Direct assertions: `assert parcel['dominant_source_zone_id'] == 'A-ZONE'`; `assert parcel['dominant_planning_zone_id'] == f'GPU:{DOCUMENT_ID}:ZONE:A-ZONE'`; `assert parcel['dominant_zone_intersection_area_m2'] == pytest.approx(50.0)`; `assert parcel['dominant_zone_share_pct'] == pytest.approx(50.0)`; `assert parcel['dominant_zone_tie_count'] == 2`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `dominant zone tie is deterministic` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_rectangle`, `_run`, `_zones`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_touch_only_relation_is_preserved_but_never_dominant`

**Signature**

```python
def test_touch_only_relation_is_preserved_but_never_dominant() -> None:
```

**Purpose**

Protects the `touch only relation is preserved but never dominant` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `result` from `_run(_parcels([_rectangle(0, 0, 10, 10)]), _zones([_rectangle(0, 0, 10, 10), _rectangle(10, 0, 20, 10)], identifiers=['AREA', 'TOUCH']))`.
- Computes `relations` from `result.intersections.set_index('source_zone_id')`.
- Computes `parcel` from `result.parcels.iloc[0]`.

**Action**

- Calls `_parcels`, `_rectangle`, `_run`, `_zones`, `result.intersections.set_index`.

**Expected result**

- Direct assertions: `assert relations.loc['AREA', 'relation_type'] == 'AREA_OVERLAP'`; `assert relations.loc['TOUCH', 'relation_type'] == 'TOUCH_ONLY'`; `assert relations.loc['TOUCH', 'intersection_area_m2'] == pytest.approx(0.0)`; `assert relations.loc['TOUCH', 'parcel_share_pct'] == pytest.approx(0.0)`; `assert parcel['zoning_area_match_count'] == 1`; `assert parcel['zoning_touch_only_count'] == 1`; `assert parcel['dominant_source_zone_id'] == 'AREA'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `touch only relation is preserved but never dominant` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_rectangle`, `_run`, `_zones`, `pytest.approx`, `result.intersections.set_index`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_parcel_with_no_positive_area_zone_is_preserved`

**Signature**

```python
def test_parcel_with_no_positive_area_zone_is_preserved() -> None:
```

**Purpose**

Protects the `parcel with no positive area zone is preserved` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_run(_parcels([_rectangle(0, 0, 10, 10)]), _zones([_rectangle(10, 0, 20, 10)], identifiers=['TOUCH']))`.
- Computes `parcel` from `result.parcels.iloc[0]`.

**Action**

- Calls `_parcels`, `_rectangle`, `_run`, `_zones`, `pd.isna`.

**Expected result**

- Direct assertions: `assert len(result.intersections) == 1`; `assert result.intersections.iloc[0]['relation_type'] == 'TOUCH_ONLY'`; `assert parcel['zoning_area_match_count'] == 0`; `assert parcel['zoning_touch_only_count'] == 1`; `assert parcel['zoning_intersection_area_sum_m2'] == pytest.approx(0.0)`; `assert parcel['zoning_covered_union_area_m2'] == pytest.approx(0.0)`; `assert parcel['zoning_coverage_pct'] == pytest.approx(0.0)`; `assert parcel['zoning_gap_area_m2'] == pytest.approx(100.0)`; `assert pd.isna(parcel['dominant_planning_zone_id'])`; `assert pd.isna(parcel['dominant_source_zone_id'])`; `assert pd.isna(parcel['dominant_zone_intersection_area_m2'])`; `assert pd.isna(parcel['dominant_zone_share_pct'])`; `assert pd.isna(parcel['dominant_zone_tie_count'])`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `parcel with no positive area zone is preserved` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_rectangle`, `_run`, `_zones`, `len`, `pd.isna`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_parcel_with_no_intersecting_zone_has_zero_coverage`

**Signature**

```python
def test_parcel_with_no_intersecting_zone_has_zero_coverage() -> None:
```

**Purpose**

Protects the `parcel with no intersecting zone has zero coverage` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_run(_parcels([_rectangle(0, 0, 10, 10)]), _zones([_rectangle(20, 0, 30, 10)]))`.
- Computes `parcel` from `result.parcels.iloc[0]`.

**Action**

- Calls `_parcels`, `_rectangle`, `_run`, `_zones`, `is_float_dtype`, `is_integer_dtype`.

**Expected result**

- Direct assertions: `assert result.intersections.empty`; `assert parcel['zoning_area_match_count'] == 0`; `assert parcel['zoning_touch_only_count'] == 0`; `assert parcel['zoning_coverage_pct'] == pytest.approx(0.0)`; `assert parcel['zoning_gap_area_m2'] == pytest.approx(100.0)`; `assert tuple(result.intersections.columns) == ('parcel_id', 'planning_zone_id', 'source_zone_id', 'zone_type_raw', 'zone_label_raw', 'zone_long_label_raw', 'relation_type', 'parcel_metric_area_m2', 'zone_area_m2', 'intersection_area_m2', 'parcel_share_pct', 'zone_share_pct', 'source_document_id', 'source_archive_sha256', 'source_layer', 'source_validity_date_raw', 'regulation_filename_raw')`; `assert is_integer_dtype(result.parcels['zoning_area_match_count'])`; `assert is_integer_dtype(result.parcels['zoning_touch_only_count'])`; `assert str(result.parcels['dominant_zone_tie_count'].dtype) == 'Int64'`; `assert is_float_dtype(result.intersections[column])`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `parcel with no intersecting zone has zero coverage` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_rectangle`, `_run`, `_zones`, `is_float_dtype`, `is_integer_dtype`, `pytest.approx`, `str`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_overlapping_source_zones_expose_raw_sum_union_and_excess`

**Signature**

```python
def test_overlapping_source_zones_expose_raw_sum_union_and_excess() -> None:
```

**Purpose**

Protects the `overlapping source zones expose raw sum union and excess` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_run(_parcels([_rectangle(0, 0, 10, 10)]), _zones([_rectangle(0, 0, 10, 10), _rectangle(0, 0, 5, 10)], identifiers=['WHOLE', 'HALF']))`.
- Computes `parcel` from `result.parcels.iloc[0]`.

**Action**

- Calls `_parcels`, `_rectangle`, `_run`, `_zones`.

**Expected result**

- Direct assertions: `assert parcel['zoning_intersection_area_sum_m2'] == pytest.approx(150.0)`; `assert parcel['zoning_covered_union_area_m2'] == pytest.approx(100.0)`; `assert parcel['zoning_overlap_excess_area_m2'] == pytest.approx(50.0)`; `assert parcel['zoning_coverage_pct'] == pytest.approx(100.0)`; `assert parcel['zoning_gap_area_m2'] == pytest.approx(0.0)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `overlapping source zones expose raw sum union and excess` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_rectangle`, `_run`, `_zones`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_polygon_and_multipolygon_parcels_are_supported`

**Signature**

```python
def test_polygon_and_multipolygon_parcels_are_supported(
    parcel_geometry: object,
) -> None:
```

**Purpose**

Protects the `polygon and multipolygon parcels are supported` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcel_geometry`.
- Contains 1 explicit setup/context statement(s).
- Computes `result` from `_run(_parcels([parcel_geometry]), _zones([_rectangle(-5, -5, 20, 15)]))`.

**Action**

- Calls `MultiPolygon`, `_parcels`, `_rectangle`, `_run`, `_zones`.

**Expected result**

- Direct assertions: `assert result.parcels.iloc[0]['zoning_coverage_pct'] == pytest.approx(100.0)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `polygon and multipolygon parcels are supported` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `MultiPolygon`, `_parcels`, `_rectangle`, `_run`, `_zones`, `pytest.approx`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_polygon_and_multipolygon_zones_are_supported`

**Signature**

```python
def test_polygon_and_multipolygon_zones_are_supported(
    zone_geometry: object,
    expected_area: float,
    expected_coverage: float,
) -> None:
```

**Purpose**

Protects the `polygon and multipolygon zones are supported` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `zone_geometry`, `expected_area`, `expected_coverage`.
- Contains 1 explicit setup/context statement(s).
- Computes `result` from `_run(_parcels([_rectangle(0, 0, 10, 10)]), _zones([zone_geometry]))`.

**Action**

- Calls `MultiPolygon`, `_parcels`, `_rectangle`, `_run`, `_zones`.

**Expected result**

- Direct assertions: `assert result.parcels.iloc[0]['zoning_coverage_pct'] == pytest.approx(expected_coverage)`; `assert result.zones.iloc[0]['zone_area_m2'] == pytest.approx(expected_area)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `polygon and multipolygon zones are supported` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `MultiPolygon`, `_parcels`, `_rectangle`, `_run`, `_zones`, `pytest.approx`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93`

**Signature**

```python
def test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93(
    parcel_crs: str,
) -> None:
```

**Purpose**

Protects the `parcel crs is preserved while metric calculation uses lambert93` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcel_crs`.
- Contains 2 explicit setup/context statement(s).
- Computes `parcels` from `_parcels([_rectangle(0, 0, 10, 10)], crs=parcel_crs)`.
- Computes `result` from `_run(parcels, _zones([_rectangle(0, 0, 10, 10)]))`.

**Action**

- Calls `_parcels`, `_rectangle`, `_run`, `_zones`.

**Expected result**

- Direct assertions: `assert result.parcels.crs == parcels.crs`; `assert result.intersections.iloc[0]['parcel_metric_area_m2'] == pytest.approx(100.0, abs=1e-05)`; `assert result.intersections.iloc[0]['intersection_area_m2'] == pytest.approx(100.0, abs=1e-05)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `parcel crs is preserved while metric calculation uses lambert93` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_rectangle`, `_run`, `_zones`, `pytest.approx`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154`

**Signature**

```python
def test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154() -> None:
```

**Purpose**

Protects the `ignf lamb93 source zoning is normalized to epsg2154` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `source` from `_zones([_rectangle(0, 0, 10, 10)], crs='IGNF:LAMB93')`.
- Computes `result` from `_run(_parcels(), source)`.

**Action**

- Calls `_parcels`, `_rectangle`, `_run`, `_zones`, `result.zones.crs.to_epsg`, `source.crs.to_string`.

**Expected result**

- Direct assertions: `assert source.crs.to_string() == 'IGNF:LAMB93'`; `assert result.zones.crs.to_epsg() == 2154`; `assert result.zones.iloc[0].geometry.area == pytest.approx(100.0)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `ignf lamb93 source zoning is normalized to epsg2154` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_rectangle`, `_run`, `_zones`, `pytest.approx`, `result.zones.crs.to_epsg`, `source.crs.to_string`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_or_unusable_crs_is_rejected`

**Signature**

```python
def test_missing_or_unusable_crs_is_rejected(
    parcels: gpd.GeoDataFrame,
    zones: gpd.GeoDataFrame,
    message: str,
) -> None:
```

**Purpose**

Protects the `missing or unusable crs is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `zones`, `message`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(PlanningZoningError, match=message)` and executes: Calls `_run(parcels, zones)` for its validation or side effect.

**Action**

- Calls `_parcels`, `_run`, `_zones`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningZoningError, match=message): _run(parcels, zones)`.

**Regression protected**

- Protects the exact `missing or unusable crs is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_run`, `_zones`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_or_non_polygonal_parcel_geometry_is_rejected`

**Signature**

```python
def test_invalid_or_non_polygonal_parcel_geometry_is_rejected(
    geometry: object,
) -> None:
```

**Purpose**

Protects the `invalid or non polygonal parcel geometry is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(PlanningZoningError, match='geometry|Polygon')` and executes: Calls `_run(_parcels([geometry]), _zones())` for its validation or side effect.

**Action**

- Calls `LineString`, `Point`, `Polygon`, `_parcels`, `_run`, `_zones`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningZoningError, match='geometry|Polygon'): _run(_parcels([geometry]), _zones())`.

**Regression protected**

- Protects the exact `invalid or non polygonal parcel geometry is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `Point`, `Polygon`, `_parcels`, `_run`, `_zones`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_or_non_polygonal_zone_geometry_is_rejected`

**Signature**

```python
def test_invalid_or_non_polygonal_zone_geometry_is_rejected(
    geometry: object,
) -> None:
```

**Purpose**

Protects the `invalid or non polygonal zone geometry is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(PlanningZoningError, match='geometry|Polygon')` and executes: Calls `_run(_parcels(), _zones([geometry]))` for its validation or side effect.

**Action**

- Calls `LineString`, `Point`, `Polygon`, `_parcels`, `_run`, `_zones`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningZoningError, match='geometry|Polygon'): _run(_parcels(), _zones([geometry]))`.

**Regression protected**

- Protects the exact `invalid or non polygonal zone geometry is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `Point`, `Polygon`, `_parcels`, `_run`, `_zones`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_parcel_id_is_rejected`

**Signature**

```python
def test_invalid_parcel_id_is_rejected(identifier: object) -> None:
```

**Purpose**

Protects the `invalid parcel id is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `identifier`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(PlanningZoningError, match='parcel_id')` and executes: Calls `_run(_parcels(identifiers=[identifier]), _zones())` for its validation or side effect.

**Action**

- Calls `_parcels`, `_run`, `_zones`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningZoningError, match='parcel_id'): _run(_parcels(identifiers=[identifier]), _zones())`.

**Regression protected**

- Protects the exact `invalid parcel id is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_run`, `_zones`, `pytest.mark.parametrize`, `pytest.raises`.

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
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(PlanningZoningError, match='parcel_id.*unique|duplicate')` and executes: Calls `_run(_parcels([_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)], identifiers=['DUPLICATE', 'DUPLICATE']), _zones())` for its validation or side effect.

**Action**

- Calls `_parcels`, `_rectangle`, `_run`, `_zones`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningZoningError, match='parcel_id.*unique|duplicate'): _run(_parcels([_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)], identifiers=['DUPLICATE', 'DUPLICATE']), _zones())`.

**Regression protected**

- Protects the exact `duplicate parcel id is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_rectangle`, `_run`, `_zones`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_parcel_id_is_rejected`

**Signature**

```python
def test_missing_parcel_id_is_rejected() -> None:
```

**Purpose**

Protects the `missing parcel id is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `parcels` from `_parcels().drop(columns=['parcel_id'])`.
- Enters managed context(s) `pytest.raises(PlanningZoningError, match='parcel_id')` and executes: Calls `_run(parcels, _zones())` for its validation or side effect.

**Action**

- Calls `_parcels`, `_parcels().drop`, `_run`, `_zones`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningZoningError, match='parcel_id'): _run(parcels, _zones())`.

**Regression protected**

- Protects the exact `missing parcel id is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_parcels().drop`, `_run`, `_zones`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_geometry_must_be_the_active_parcel_geometry_column`

**Signature**

```python
def test_geometry_must_be_the_active_parcel_geometry_column() -> None:
```

**Purpose**

Protects the `geometry must be the active parcel geometry column` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `parcels` from `_parcels().rename_geometry('shape')`.
- Computes `parcels['geometry']` from `parcels['shape']`.
- Enters managed context(s) `pytest.raises(PlanningZoningError, match='active')` and executes: Calls `_run(parcels, _zones())` for its validation or side effect.

**Action**

- Calls `_parcels`, `_parcels().rename_geometry`, `_run`, `_zones`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningZoningError, match='active'): _run(parcels, _zones())`.

**Regression protected**

- Protects the exact `geometry must be the active parcel geometry column` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_parcels().rename_geometry`, `_run`, `_zones`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_source_zone_id_is_rejected`

**Signature**

```python
def test_invalid_source_zone_id_is_rejected(identifier: object) -> None:
```

**Purpose**

Protects the `invalid source zone id is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `identifier`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(PlanningZoningError, match='LIB_IDZONE|zone')` and executes: Calls `_run(_parcels(), _zones(identifiers=[identifier]))` for its validation or side effect.

**Action**

- Calls `_parcels`, `_run`, `_zones`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningZoningError, match='LIB_IDZONE|zone'): _run(_parcels(), _zones(identifiers=[identifier]))`.

**Regression protected**

- Protects the exact `invalid source zone id is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_run`, `_zones`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_source_zone_id_is_rejected`

**Signature**

```python
def test_duplicate_source_zone_id_is_rejected() -> None:
```

**Purpose**

Protects the `duplicate source zone id is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(PlanningZoningError, match='LIB_IDZONE.*unique|duplicate')` and executes: Calls `_run(_parcels(), _zones([_rectangle(0, 0, 5, 10), _rectangle(5, 0, 10, 10)], identifiers=['DUPLICATE', 'DUPLICATE']))` for its validation or side effect.

**Action**

- Calls `_parcels`, `_rectangle`, `_run`, `_zones`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningZoningError, match='LIB_IDZONE.*unique|duplicate'): _run(_parcels(), _zones([_rectangle(0, 0, 5, 10), _rectangle(5, 0, 10, 10)], identifiers=['DUPLICATE', 'DUPLICATE']))`.

**Regression protected**

- Protects the exact `duplicate source zone id is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_rectangle`, `_run`, `_zones`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_zoning_document_reference_must_match_loaded_archive`

**Signature**

```python
def test_zoning_document_reference_must_match_loaded_archive() -> None:
```

**Purpose**

Protects the `zoning document reference must match loaded archive` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `zones` from `_zones(document_references=['31395_PLU_WRONG'])`.
- Enters managed context(s) `pytest.raises(PlanningZoningError, match='IDURBA|document')` and executes: Calls `_run(_parcels(), zones)` for its validation or side effect.

**Action**

- Calls `_parcels`, `_run`, `_zones`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningZoningError, match='IDURBA|document'): _run(_parcels(), zones)`.

**Regression protected**

- Protects the exact `zoning document reference must match loaded archive` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_run`, `_zones`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_zoning_summary_lineage_and_count_must_match_bundle`

**Signature**

```python
def test_zoning_summary_lineage_and_count_must_match_bundle(
    summary_field: str,
    bad_value: object,
    message: str,
) -> None:
```

**Purpose**

Protects the `zoning summary lineage and count must match bundle` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `summary_field`, `bad_value`, `message`.
- Contains 5 explicit setup/context statement(s).
- Computes `document` from `_planning_document()`.
- Computes `summary` from `replace(document.zoning.summary, **{summary_field: bad_value})`.
- Computes `zoning` from `replace(document.zoning, summary=summary)`.
- Computes `corrupted` from `replace(document, zoning=zoning)`.
- Enters managed context(s) `pytest.raises(PlanningZoningError, match=message)` and executes: Calls `intersect_parcels_with_gpu_zoning(_parcels(), corrupted)` for its validation or side effect.

**Action**

- Calls `_parcels`, `_planning_document`, `intersect_parcels_with_gpu_zoning`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningZoningError, match=message): intersect_parcels_with_gpu_zoning(_parcels(), corrupted)`.

**Regression protected**

- Protects the exact `zoning summary lineage and count must match bundle` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_planning_document`, `intersect_parcels_with_gpu_zoning`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_existing_parcel_output_field_collision_is_rejected`

**Signature**

```python
def test_existing_parcel_output_field_collision_is_rejected(
    reserved_column: str,
) -> None:
```

**Purpose**

Protects the `existing parcel output field collision is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `reserved_column`.
- Contains 3 explicit setup/context statement(s).
- Computes `parcels` from `_parcels()`.
- Computes `parcels[reserved_column]` from `'pre-existing-value'`.
- Enters managed context(s) `pytest.raises(PlanningZoningError, match='column|output|reserved|collision')` and executes: Calls `_run(parcels, _zones())` for its validation or side effect.

**Action**

- Calls `_parcels`, `_run`, `_zones`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningZoningError, match='column|output|reserved|collision'): _run(parcels, _zones())`.

**Regression protected**

- Protects the exact `existing parcel output field collision is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_run`, `_zones`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_every_source_zoning_field_is_required`

**Signature**

```python
def test_every_source_zoning_field_is_required(field: str) -> None:
```

**Purpose**

Protects the `every source zoning field is required` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `field`.
- Contains 2 explicit setup/context statement(s).
- Computes `zones` from `_zones().drop(columns=[field])`.
- Enters managed context(s) `pytest.raises(PlanningZoningError, match=field)` and executes: Calls `_run(_parcels(), zones)` for its validation or side effect.

**Action**

- Calls `_parcels`, `_run`, `_zones`, `_zones().drop`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningZoningError, match=field): _run(_parcels(), zones)`.

**Regression protected**

- Protects the exact `every source zoning field is required` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_run`, `_zones`, `_zones().drop`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_input_frames_are_not_mutated`

**Signature**

```python
def test_input_frames_are_not_mutated() -> None:
```

**Purpose**

Protects the `input frames are not mutated` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `parcels` from `_parcels([_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)], identifiers=['P-2', 'P-1'], crs='EPSG:4326')`.
- Computes `zones` from `_zones([_rectangle(0, 0, 15, 15), _rectangle(20, 0, 35, 15)], identifiers=['U-1', 'N-1'], labels=['UA', 'N'], zone_types=['U', 'N'])`.
- Computes `planning_document` from `_planning_document(zones)`.
- Computes `parcels_before` from `deepcopy(parcels)`.
- Computes `zones_before` from `deepcopy(planning_document.zoning.data)`.

**Action**

- Calls `_parcels`, `_planning_document`, `_rectangle`, `_zones`, `deepcopy`, `intersect_parcels_with_gpu_zoning`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `input frames are not mutated` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_planning_document`, `_rectangle`, `_zones`, `assert_geodataframe_equal`, `deepcopy`, `intersect_parcels_with_gpu_zoning`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved`

**Signature**

```python
def test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved() -> None:
```

**Purpose**

Protects the `parcel count order geometry crs and existing columns are preserved` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `parcels` from `_parcels([_rectangle(20, 0, 30, 10), _rectangle(0, 0, 10, 10)], identifiers=['P-2', 'P-1'], crs='EPSG:4326')`.
- Computes `result` from `_run(parcels, _zones([_rectangle(-5, -5, 15, 15), _rectangle(15, -5, 35, 15)], identifiers=['LEFT', 'RIGHT']))`.

**Action**

- Calls `_parcels`, `_rectangle`, `_run`, `_zones`, `parcels.geometry.reset_index`, `parcels['existing_grid_value'].tolist`, `parcels['parcel_id'].tolist`, `result.intersections.duplicated`, `result.intersections.duplicated(subset=['parcel_id', 'planning_zone_id']).any`, `result.parcels.geometry.reset_index`, `result.parcels.geometry.reset_index(drop=True).equals`, `result.parcels['existing_grid_value'].tolist`, `result.parcels['parcel_id'].duplicated`, `result.parcels['parcel_id'].duplicated().any`, `result.parcels['parcel_id'].tolist`.

**Expected result**

- Direct assertions: `assert len(result.parcels) == len(parcels)`; `assert result.parcels['parcel_id'].tolist() == parcels['parcel_id'].tolist()`; `assert result.parcels['existing_grid_value'].tolist() == parcels['existing_grid_value'].tolist()`; `assert result.parcels.crs == parcels.crs`; `assert result.parcels.geometry.reset_index(drop=True).equals(parcels.geometry.reset_index(drop=True))`; `assert not result.parcels['parcel_id'].duplicated().any()`; `assert set(result.intersections['parcel_id']).issubset(set(parcels['parcel_id']))`; `assert not result.intersections.duplicated(subset=['parcel_id', 'planning_zone_id']).any()`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `parcel count order geometry crs and existing columns are preserved` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_rectangle`, `_run`, `_zones`, `len`, `parcels.geometry.reset_index`, `parcels['existing_grid_value'].tolist`, `parcels['parcel_id'].tolist`, `result.intersections.duplicated`, `result.intersections.duplicated(subset=['parcel_id', 'planning_zone_id']).any`, `result.parcels.geometry.reset_index`, `result.parcels.geometry.reset_index(drop=True).equals`, `result.parcels['existing_grid_value'].tolist`, `result.parcels['parcel_id'].duplicated`, `result.parcels['parcel_id'].duplicated().any`, `result.parcels['parcel_id'].tolist`, `set`, `set(result.intersections['parcel_id']).issubset`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_raw_zoning_values_are_preserved_exactly`

**Signature**

```python
def test_raw_zoning_values_are_preserved_exactly() -> None:
```

**Purpose**

Protects the `raw zoning values are preserved exactly` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 6 explicit setup/context statement(s).
- Computes `zones` from `_zones([_rectangle(0, 0, 5, 10), _rectangle(5, 0, 10, 10)], identifiers=['ID-É', 'id-lower'], labels=['AUf', 'Nh'], long_labels=['Libellé Étendu', None], zone_types=['AUc', 'N'])`.
- Computes `zones.loc[zones.index[1], 'NOMFIC']` from `None`.
- Computes `zones.loc[zones.index[1], 'URLFIC']` from `None`.
- Computes `result` from `_run(_parcels(), zones)`.
- Computes `first` from `_row_for_source_zone(result, 'ID-É')`.
- Computes `second` from `_row_for_source_zone(result, 'id-lower')`.

**Action**

- Calls `_parcels`, `_rectangle`, `_row_for_source_zone`, `_run`, `_zones`, `pd.isna`.

**Expected result**

- Direct assertions: `assert first['source_zone_id'] == 'ID-É'`; `assert first['zone_label_raw'] == 'AUf'`; `assert first['zone_long_label_raw'] == 'Libellé Étendu'`; `assert first['zone_type_raw'] == 'AUc'`; `assert second['source_zone_id'] == 'id-lower'`; `assert second['zone_label_raw'] == 'Nh'`; `assert pd.isna(second['zone_long_label_raw'])`; `assert second['zone_type_raw'] == 'N'`; `assert pd.isna(second['regulation_filename_raw'])`; `assert pd.isna(second['regulation_url_raw'])`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `raw zoning values are preserved exactly` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_rectangle`, `_row_for_source_zone`, `_run`, `_zones`, `pd.isna`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_intersection_table_references_only_known_parcels_and_zones`

**Signature**

```python
def test_intersection_table_references_only_known_parcels_and_zones() -> None:
```

**Purpose**

Protects the `intersection table references only known parcels and zones` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_run(_parcels([_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)], identifiers=['P-1', 'P-2']), _zones([_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)], identifiers=['Z-1', 'Z-2']))`.
- Computes `numeric` from `result.intersections[['parcel_metric_area_m2', 'zone_area_m2', 'intersection_area_m2', 'parcel_share_pct', 'zone_share_pct']]`.

**Action**

- Calls `(numeric >= 0).all`, `(numeric >= 0).all().all`, `_parcels`, `_rectangle`, `_run`, `_zones`, `numeric.notna`, `numeric.notna().all`, `numeric.notna().all().all`, `result.intersections.duplicated`, `result.intersections.duplicated(subset=['parcel_id', 'planning_zone_id']).any`.

**Expected result**

- Direct assertions: `assert set(result.intersections['parcel_id']) == {'P-1', 'P-2'}`; `assert set(result.intersections['planning_zone_id']) == set(result.zones['planning_zone_id'])`; `assert not result.intersections.duplicated(subset=['parcel_id', 'planning_zone_id']).any()`; `assert numeric.notna().all().all()`; `assert (numeric >= 0).all().all()`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `intersection table references only known parcels and zones` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `(numeric >= 0).all`, `(numeric >= 0).all().all`, `_parcels`, `_rectangle`, `_run`, `_zones`, `numeric.notna`, `numeric.notna().all`, `numeric.notna().all().all`, `result.intersections.duplicated`, `result.intersections.duplicated(subset=['parcel_id', 'planning_zone_id']).any`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_result_frames_are_independent_from_inputs`

**Signature**

```python
def test_result_frames_are_independent_from_inputs() -> None:
```

**Purpose**

Protects the `result frames are independent from inputs` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 8 explicit setup/context statement(s).
- Computes `parcels` from `_parcels()`.
- Computes `zones` from `_zones()`.
- Computes `result` from `_run(parcels, zones)`.
- Computes `parcel_snapshot` from `result.parcels.copy(deep=True)`.
- Computes `zone_snapshot` from `result.zones.copy(deep=True)`.
- Computes `intersections_snapshot` from `result.intersections.copy(deep=True)`.
- Computes `parcels.loc[parcels.index[0], 'existing_grid_value']` from `-1`.
- Computes `zones.loc[zones.index[0], 'LIBELLE']` from `'CHANGED'`.

**Action**

- Calls `_parcels`, `_run`, `_zones`, `result.intersections.copy`, `result.parcels.copy`, `result.zones.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `result frames are independent from inputs` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_run`, `_zones`, `assert_frame_equal`, `result.intersections.copy`, `result.parcels.copy`, `result.zones.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_zoning_validation_accepts_physical_fixture`

**Signature**

```python
def test_source_complete_zoning_validation_accepts_physical_fixture(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `source complete zoning validation accepts physical fixture` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 3 explicit setup/context statement(s).
- Computes `parcels` from `_parcels()`.
- Computes `document` from `_physical_planning_document(tmp_path)`.
- Computes `factual` from `intersect_parcels_with_gpu_zoning(parcels, document)`.

**Action**

- Calls `_parcels`, `_physical_planning_document`, `intersect_parcels_with_gpu_zoning`, `validate_normalized_planning_zoning_inputs`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `source complete zoning validation accepts physical fixture` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_physical_planning_document`, `intersect_parcels_with_gpu_zoning`, `validate_normalized_planning_zoning_inputs`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_zoning_validation_rejects_coordinated_mutations`

**Signature**

```python
def test_source_complete_zoning_validation_rejects_coordinated_mutations(
    tmp_path: Path,
    mutation: str,
) -> None:
```

**Purpose**

Protects the `source complete zoning validation rejects coordinated mutations` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `mutation`.
- Contains 8 explicit setup/context statement(s).
- Computes `source` from `_zones([_rectangle(0, 0, 5, 10), _rectangle(5, 0, 10, 10)], identifiers=['ZONE-A', 'ZONE-B'], labels=['UA', 'UB'])`.
- Computes `parcels` from `_parcels()`.
- Computes `document` from `_physical_planning_document(tmp_path, source)`.
- Computes `factual` from `intersect_parcels_with_gpu_zoning(parcels, document)`.
- Computes `zones` from `factual.zones.copy()`.
- Computes `relations` from `factual.intersections.copy()`.
- Computes `parcel_output` from `factual.parcels.copy()`.
- Enters managed context(s) `pytest.raises(PlanningZoningError, match='source|reconstruction|differs')` and executes: Calls `validate_normalized_planning_zoning_inputs(document, parcel_output, zones, relations)` for its validation or side effect.

**Action**

- Calls `_parcels`, `_physical_planning_document`, `_rectangle`, `_zones`, `factual.intersections.copy`, `factual.parcels.copy`, `factual.zones.copy`, `gpd.GeoDataFrame`, `intersect_parcels_with_gpu_zoning`, `pd.concat`, `relations.iloc[:-1].copy`, `relations['planning_zone_id'].eq`, `validate_normalized_planning_zoning_inputs`, `zones.iloc[:-1].copy`, `zones.iloc[::-1].reset_index`, `zones.iloc[[0]].copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningZoningError, match='source|reconstruction|differs'): validate_normalized_planning_zoning_inputs(document, parcel_output, zones, relations)`.

**Regression protected**

- Protects the exact `source complete zoning validation rejects coordinated mutations` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_physical_planning_document`, `_rectangle`, `_zones`, `factual.intersections.copy`, `factual.parcels.copy`, `factual.zones.copy`, `gpd.GeoDataFrame`, `intersect_parcels_with_gpu_zoning`, `pd.concat`, `pytest.mark.parametrize`, `pytest.raises`, `relations.iloc[:-1].copy`, `relations['planning_zone_id'].eq`, `validate_normalized_planning_zoning_inputs`, `zones.iloc[:-1].copy`, `zones.iloc[::-1].reset_index`, `zones.iloc[[0]].copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_zoning_validation_rejects_physical_tamper`

**Signature**

```python
def test_source_complete_zoning_validation_rejects_physical_tamper(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `source complete zoning validation rejects physical tamper` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 5 explicit setup/context statement(s).
- Computes `parcels` from `_parcels()`.
- Computes `document` from `_physical_planning_document(tmp_path)`.
- Computes `factual` from `intersect_parcels_with_gpu_zoning(parcels, document)`.
- Enters managed context(s) `document.zoning.reference.dataset_path.open('ab')` and executes: Calls `stream.write(b'tamper')` for its validation or side effect.
- Enters managed context(s) `pytest.raises(PlanningZoningError, match='Physical|source')` and executes: Calls `validate_normalized_planning_zoning_inputs(document, factual.parcels, factual.zones, factual.intersections)` for its validation or side effect.

**Action**

- Calls `_parcels`, `_physical_planning_document`, `document.zoning.reference.dataset_path.open`, `intersect_parcels_with_gpu_zoning`, `validate_normalized_planning_zoning_inputs`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningZoningError, match='Physical|source'): validate_normalized_planning_zoning_inputs(document, factual.parcels, factual.zones, factual.intersections)`.

**Regression protected**

- Protects the exact `source complete zoning validation rejects physical tamper` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_physical_planning_document`, `document.zoning.reference.dataset_path.open`, `intersect_parcels_with_gpu_zoning`, `pytest.raises`, `stream.write`, `validate_normalized_planning_zoning_inputs`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_zoning_validation_revalidates_physical_source_once`

**Signature**

```python
def test_source_complete_zoning_validation_revalidates_physical_source_once(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `source complete zoning validation revalidates physical source once` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 5 explicit setup/context statement(s).
- Computes `parcels` from `_parcels()`.
- Computes `document` from `_physical_planning_document(tmp_path)`.
- Computes `factual` from `intersect_parcels_with_gpu_zoning(parcels, document)`.
- Computes `original` from `module.revalidate_gpu_spatial_layer_sources`.
- Enters managed context(s) `patch.object(module, 'revalidate_gpu_spatial_layer_sources', wraps=original)` and executes: Calls `validate_normalized_planning_zoning_inputs(document, factual.parcels, factual.zones, factual.intersections)` for its validation or side effect.

**Action**

- Calls `_parcels`, `_physical_planning_document`, `intersect_parcels_with_gpu_zoning`, `validate_normalized_planning_zoning_inputs`.

**Expected result**

- Direct assertions: `assert revalidate.call_count == 1`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `source complete zoning validation revalidates physical source once` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_physical_planning_document`, `intersect_parcels_with_gpu_zoning`, `patch.object`, `validate_normalized_planning_zoning_inputs`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `AREA` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `DATVALID` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `IDURBA` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `LIBELLE` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `LIBELONG` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `LIB_IDZONE` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `NOMFIC` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `TOUCH` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `TYPEZONE` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `URLFIC` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `columns` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `dominant_planning_zone_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `dominant_source_zone_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `dominant_zone_intersection_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `dominant_zone_label_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `dominant_zone_long_label_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `dominant_zone_share_pct` | Logical dtype: float64. Nullability: determined by the owning schema/dtype map and explicit null guards. | percentage derived from the exact numerator/denominator named by its stage. Consumers and exact calculations are the functions that reference this column above. |
| `dominant_zone_tie_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `dominant_zone_type_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `existing_grid_value` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `geometry` | Logical dtype: GeoPandas active geometry dtype. Nullability: nullable only where the source-stage geometry-status contract explicitly preserves nulls. | source or preserved spatial geometry; never itself a suitability or legal conclusion. Consumers and exact calculations are the functions that reference this column above. |
| `intersection_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_metric_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_share_pct` | Logical dtype: float64. Nullability: determined by the owning schema/dtype map and explicit null guards. | percentage derived from the exact numerator/denominator named by its stage. Consumers and exact calculations are the functions that reference this column above. |
| `planning_archive_name` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `planning_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `planning_document_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `planning_document_type` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `planning_source_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `planning_standard_model` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `planning_zone_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `regulation_filename_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `regulation_url_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `relation_type` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `shape` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_archive_name` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `source_commune_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_document_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_document_reference_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `source_document_type` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `source_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_portal` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_provider` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_standard_model` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_validity_date_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `source_zone_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `zone_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `zone_label_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `zone_long_label_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `zone_share_pct` | Logical dtype: float64. Nullability: determined by the owning schema/dtype map and explicit null guards. | percentage derived from the exact numerator/denominator named by its stage. Consumers and exact calculations are the functions that reference this column above. |
| `zone_type_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `zoning_area_match_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `zoning_coverage_pct` | Logical dtype: float64. Nullability: determined by the owning schema/dtype map and explicit null guards. | percentage derived from the exact numerator/denominator named by its stage. Consumers and exact calculations are the functions that reference this column above. |
| `zoning_covered_union_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `zoning_gap_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `zoning_intersection_area_sum_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `zoning_overlap_excess_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `zoning_touch_only_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |

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

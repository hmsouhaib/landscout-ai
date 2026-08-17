# `tests/unit/test_enrich_planning_features.py`

## File identity

- Repository path: `tests/unit/test_enrich_planning_features.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `enrich_planning_features` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `861b34c1fc71b98446c43397978183fc48e71bba80ffb92f0319f827b9c15fab`

## 1. Purpose

Provides complete unit and regression coverage for the `enrich_planning_features` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import json` — required by the implementation paths and symbols documented below.
- `import shutil` — required by the implementation paths and symbols documented below.
- `import sys` — required by the implementation paths and symbols documented below.
- `import tempfile` — required by the implementation paths and symbols documented below.
- `from copy import deepcopy` — required by the implementation paths and symbols documented below.
- `from dataclasses import FrozenInstanceError, replace` — required by the implementation paths and symbols documented below.
- `from hashlib import sha256` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.

### Third-party

- `import subprocess` — required by the implementation paths and symbols documented below.
- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import numpy as np` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `import pytest` — required by the implementation paths and symbols documented below.
- `from geopandas.testing import assert_geodataframe_equal` — required by the implementation paths and symbols documented below.
- `from pandas.testing import assert_frame_equal` — required by the implementation paths and symbols documented below.
- `from shapely.geometry import ( LineString, MultiLineString, MultiPoint, MultiPolygon, Point, Polygon, )` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout import stages` — required by the implementation paths and symbols documented below.
- `from landscout.common.planning_feature_contract import ( validate_intrinsic_planning_feature_relations, )` — required by the implementation paths and symbols documented below.
- `from landscout.sources import gpu_fr as gpu_source_module` — required by the implementation paths and symbols documented below.
- `from landscout.sources.gpu_fr import ( EXTRACTION_MANIFEST_NAME, GpuArchiveDownload, GpuDocumentMetadata, GpuExtractedFile, GpuExtraction, GpuInspectedLayer, GpuLayerSummary, GpuPlanningDocument, GpuSpatialLayerReference, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages import enrich_planning_features as planning_features_module` — required by the implementation paths and symbols documented below.
- `from landscout.stages.enrich_planning_features import ( ParcelPlanningFeaturesResult, PlanningFeatureInputValidation, PlanningFeaturesError, _validate_result, intersect_parcels_with_gpu_planning_features, validate_normalized_planning_feature_inputs, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `DOCUMENT_ID` | `"doc-1"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ARCHIVE_NAME` | `"31395_PLU_20240215"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ARCHIVE_SHA` | `"a" * 64` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `STANDARD` | `"CNIG PLU v2017"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `LOCAL_ENGINEERING_CRS` | `'ENGCRS["Local",EDATUM["Unknown"],CS[Cartesian,2],' 'AXIS["x",east,LENGTHUNIT["metre",1]],' 'AXIS["y",north,LENGTHUNIT["metre",1]]]'` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `_rectangle`

**Signature**

```python
def _rectangle(x1: float, y1: float, x2: float, y2: float) -> Polygon:
```

**Purpose**

Implements rectangle according to the exact implementation and guards in this file.

**Inputs**

- `x1` (`float`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `y1` (`float`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `x2` (`float`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `y2` (`float`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Polygon`. Observed return expression(s): `Polygon([(x1, y1), (x1, y2), (x2, y2), (x2, y1), (x1, y1)])`.

**Algorithm**

1. Returns `Polygon([(x1, y1), (x1, y2), (x2, y2), (x2, y1), (x1, y1)])`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `Polygon`.

**Known repository callers**

- `tests/unit/test_enrich_planning_features.py` — `_contract_result`
- `tests/unit/test_enrich_planning_features.py` — `_parcels`
- `tests/unit/test_enrich_planning_features.py` — `_planning_document`
- `tests/unit/test_enrich_planning_features.py` — `_shapefile_ogr_fid_source_complete_contract`
- `tests/unit/test_enrich_planning_features.py` — `_shapefile_source_complete_contract`
- `tests/unit/test_enrich_planning_features.py` — `_source_complete_contract`
- `tests/unit/test_enrich_planning_features.py` — `_two_parcel_source_complete_contract`
- `tests/unit/test_enrich_planning_features.py` — `test_duplicate_parcel_ids_are_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_duplicate_source_ids_are_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_epsg4326_parcels_are_measured_in_lambert93_but_preserved`
- `tests/unit/test_enrich_planning_features.py` — `test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback`
- `tests/unit/test_enrich_planning_features.py` — `test_inputs_and_all_existing_parcel_fields_are_preserved`
- `tests/unit/test_enrich_planning_features.py` — `test_null_or_empty_source_geometry_is_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_overlapping_surface_union_is_not_double_counted`
- `tests/unit/test_enrich_planning_features.py` — `test_polygon_and_multipolygon_surfaces`
- `tests/unit/test_enrich_planning_features.py` — `test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent`
- `tests/unit/test_enrich_planning_features.py` — `test_relations_are_unique_deterministic_and_summaries_agree`
- `tests/unit/test_enrich_planning_features.py` — `test_shapefile_family_excludes_dotted_sibling_dataset`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_changed_physical_gpkg_geometry`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_reordered_physical_gpkg_rows`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_reloads_and_compares_source_catalog`
- `tests/unit/test_enrich_planning_features.py` — `test_surface_full_overlap_normalizes_raw_values_and_lineage`
- `tests/unit/test_enrich_planning_features.py` — `test_surface_partial_and_touch_relations`

**Tests**

- `tests/unit/test_enrich_planning_features.py::test_duplicate_parcel_ids_are_rejected`
- `tests/unit/test_enrich_planning_features.py::test_duplicate_source_ids_are_rejected`
- `tests/unit/test_enrich_planning_features.py::test_epsg4326_parcels_are_measured_in_lambert93_but_preserved`
- `tests/unit/test_enrich_planning_features.py::test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback`
- `tests/unit/test_enrich_planning_features.py::test_inputs_and_all_existing_parcel_fields_are_preserved`
- `tests/unit/test_enrich_planning_features.py::test_null_or_empty_source_geometry_is_rejected`
- `tests/unit/test_enrich_planning_features.py::test_overlapping_surface_union_is_not_double_counted`
- `tests/unit/test_enrich_planning_features.py::test_polygon_and_multipolygon_surfaces`
- `tests/unit/test_enrich_planning_features.py::test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent`
- `tests/unit/test_enrich_planning_features.py::test_relations_are_unique_deterministic_and_summaries_agree`
- `tests/unit/test_enrich_planning_features.py::test_shapefile_family_excludes_dotted_sibling_dataset`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_changed_physical_gpkg_geometry`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_reordered_physical_gpkg_rows`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_reloads_and_compares_source_catalog`
- `tests/unit/test_enrich_planning_features.py::test_surface_full_overlap_normalizes_raw_values_and_lineage`
- `tests/unit/test_enrich_planning_features.py::test_surface_partial_and_touch_relations`

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
    ids: list[object] | None = None,
    crs: str | None = "EPSG:2154",
) -> gpd.GeoDataFrame:
```

**Purpose**

Implements parcels according to the exact implementation and guards in this file.

**Inputs**

- `geometries` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `ids` (`list[object] | None`; optional/default `None`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `crs` (`str | None`; optional/default `'EPSG:2154'`) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `frame if crs == 'EPSG:2154' else frame.to_crs(crs)`; `frame.set_crs(None, allow_override=True)`.

**Algorithm**

1. Computes `values` from `geometries or [_rectangle(0, 0, 10, 10)]`.
2. Computes `frame` from `gpd.GeoDataFrame({'parcel_id': ids or [f'P-{index + 1}' for index in range(len(values))], 'existing_zoning_fact': np.arange(len(values), dtype='int64') + 7}, geometry=values, crs='EPSG:2154', index=[50 + index for index in range(len(values))])`.
3. Checks `crs is None`. When true: Returns `frame.set_crs(None, allow_override=True)`.
4. Returns `frame if crs == 'EPSG:2154' else frame.to_crs(crs)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `frame.to_crs`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_rectangle`, `frame.set_crs`, `frame.to_crs`, `gpd.GeoDataFrame`, `len`, `np.arange`, `range`.

**Known repository callers**

- `tests/unit/test_enrich_planning_features.py` — `_contract_result`
- `tests/unit/test_enrich_planning_features.py` — `_run`
- `tests/unit/test_enrich_planning_features.py` — `_shapefile_ogr_fid_source_complete_contract`
- `tests/unit/test_enrich_planning_features.py` — `_shapefile_source_complete_contract`
- `tests/unit/test_enrich_planning_features.py` — `_source_complete_contract`
- `tests/unit/test_enrich_planning_features.py` — `_two_parcel_source_complete_contract`
- `tests/unit/test_enrich_planning_features.py` — `test_duplicate_parcel_ids_are_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_epsg4326_parcels_are_measured_in_lambert93_but_preserved`
- `tests/unit/test_enrich_planning_features.py` — `test_inputs_and_all_existing_parcel_fields_are_preserved`
- `tests/unit/test_enrich_planning_features.py` — `test_invalid_parcel_ids_are_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_missing_crs_is_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_mutated_source_summary_is_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_relations_are_unique_deterministic_and_summaries_agree`
- `tests/unit/test_enrich_planning_features.py` — `test_reserved_output_column_collision_is_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_result_frames_are_independent_from_mutable_inputs`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_reordered_physical_gpkg_rows`
- `tests/unit/test_enrich_planning_features.py` — `test_source_summary_counts_are_strict_integers`

**Tests**

- `tests/unit/test_enrich_planning_features.py::test_duplicate_parcel_ids_are_rejected`
- `tests/unit/test_enrich_planning_features.py::test_epsg4326_parcels_are_measured_in_lambert93_but_preserved`
- `tests/unit/test_enrich_planning_features.py::test_inputs_and_all_existing_parcel_fields_are_preserved`
- `tests/unit/test_enrich_planning_features.py::test_invalid_parcel_ids_are_rejected`
- `tests/unit/test_enrich_planning_features.py::test_missing_crs_is_rejected`
- `tests/unit/test_enrich_planning_features.py::test_mutated_source_summary_is_rejected`
- `tests/unit/test_enrich_planning_features.py::test_relations_are_unique_deterministic_and_summaries_agree`
- `tests/unit/test_enrich_planning_features.py::test_reserved_output_column_collision_is_rejected`
- `tests/unit/test_enrich_planning_features.py::test_result_frames_are_independent_from_mutable_inputs`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_reordered_physical_gpkg_rows`
- `tests/unit/test_enrich_planning_features.py::test_source_summary_counts_are_strict_integers`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_source_frame`

**Signature**

```python
def _source_frame(
    logical: str,
    geometries: list[object],
    *,
    ids: list[object] | None = None,
    type_codes: list[object] | None = None,
    subtype_codes: list[object] | None = None,
    document_refs: list[object] | None = None,
    crs: str | None = "EPSG:2154",
) -> gpd.GeoDataFrame:
```

**Purpose**

Implements source frame according to the exact implementation and guards in this file.

**Inputs**

- `logical` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `geometries` (`list[object]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `ids` (`list[object] | None`; optional/default `None`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `type_codes` (`list[object] | None`; optional/default `None`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `subtype_codes` (`list[object] | None`; optional/default `None`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `document_refs` (`list[object] | None`; optional/default `None`) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `crs` (`str | None`; optional/default `'EPSG:2154'`) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `frame if crs == 'EPSG:2154' else frame.to_crs(crs)`; `frame.set_crs(None, allow_override=True)`; `frame.set_crs(crs, allow_override=True)`.

**Algorithm**

1. Computes `count` from `len(geometries)`.
2. Computes `prescription` from `logical.startswith('prescription')`.
3. Computes `identity` from `'LIB_IDPSC' if prescription else 'LIB_IDINFO'`.
4. Computes `type_field` from `'TYPEPSC' if prescription else 'TYPEINF'`.
5. Computes `subtype_field` from `'STYPEPSC' if prescription else 'STYPEINF'`.
6. Defines `data` with annotation `dict[str, object]` from `{'LIBELLE': [f'Label {index}' for index in range(count)], 'TXT': [None if index % 2 else f'Text {index}' for index in range(count)], type_field: type_codes or [f'T{index}' for index in range(count)], subtype_field: subtype_codes or [f'S{index}' for index in range(count)], 'NOMFIC': [None if index % 2 else f'rule-{inde…`.
7. Computes `frame` from `gpd.GeoDataFrame(data, geometry=geometries, crs='EPSG:2154')`.
8. Checks `crs is None`. When true: Returns `frame.set_crs(None, allow_override=True)`.
9. Checks `crs == 'IGNF:LAMB93'`. When true: Returns `frame.set_crs(crs, allow_override=True)`.
10. Returns `frame if crs == 'EPSG:2154' else frame.to_crs(crs)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `frame.to_crs`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `frame.set_crs`, `frame.to_crs`, `gpd.GeoDataFrame`, `len`, `logical.startswith`, `range`.

**Known repository callers**

- `tests/unit/test_enrich_planning_features.py` — `_contract_result`
- `tests/unit/test_enrich_planning_features.py` — `_shapefile_ogr_fid_source_complete_contract`
- `tests/unit/test_enrich_planning_features.py` — `_shapefile_source_complete_contract`
- `tests/unit/test_enrich_planning_features.py` — `_source_complete_contract`
- `tests/unit/test_enrich_planning_features.py` — `_two_parcel_source_complete_contract`
- `tests/unit/test_enrich_planning_features.py` — `test_duplicate_source_ids_are_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_epsg4326_parcels_are_measured_in_lambert93_but_preserved`
- `tests/unit/test_enrich_planning_features.py` — `test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback`
- `tests/unit/test_enrich_planning_features.py` — `test_geospatial_operation_failure_is_controlled_and_chained`
- `tests/unit/test_enrich_planning_features.py` — `test_gpu_source_z_is_normalized_to_canonical_2d`
- `tests/unit/test_enrich_planning_features.py` — `test_idurba_mismatch_is_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_inputs_and_all_existing_parcel_fields_are_preserved`
- `tests/unit/test_enrich_planning_features.py` — `test_invalid_surface_geometry_is_rejected_without_repair`
- `tests/unit/test_enrich_planning_features.py` — `test_line_boundary_touch_is_zero_length`
- `tests/unit/test_enrich_planning_features.py` — `test_line_crossing_and_partly_inside`
- `tests/unit/test_enrich_planning_features.py` — `test_linestring_and_multilinestring`
- `tests/unit/test_enrich_planning_features.py` — `test_missing_crs_is_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_missing_required_source_fields_fail`
- `tests/unit/test_enrich_planning_features.py` — `test_mutated_source_summary_is_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_null_or_empty_source_geometry_is_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_optional_raw_source_fields_are_not_fabricated`
- `tests/unit/test_enrich_planning_features.py` — `test_overlapping_surface_union_is_not_double_counted`
- `tests/unit/test_enrich_planning_features.py` — `test_points_inside_boundary_outside_and_multipoint`
- `tests/unit/test_enrich_planning_features.py` — `test_polygon_and_multipolygon_surfaces`
- `tests/unit/test_enrich_planning_features.py` — `test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent`
- `tests/unit/test_enrich_planning_features.py` — `test_present_empty_optional_layer_is_valid`
- `tests/unit/test_enrich_planning_features.py` — `test_relations_are_unique_deterministic_and_summaries_agree`
- `tests/unit/test_enrich_planning_features.py` — `test_result_frames_are_independent_from_mutable_inputs`
- `tests/unit/test_enrich_planning_features.py` — `test_same_source_id_is_allowed_in_distinct_logical_layers`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_reordered_physical_gpkg_rows`
- `tests/unit/test_enrich_planning_features.py` — `test_source_summary_counts_are_strict_integers`
- `tests/unit/test_enrich_planning_features.py` — `test_surface_full_overlap_normalizes_raw_values_and_lineage`
- `tests/unit/test_enrich_planning_features.py` — `test_surface_partial_and_touch_relations`
- `tests/unit/test_enrich_planning_features.py` — `test_unusable_source_crs_is_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_wrong_geometry_kind_is_rejected`

**Tests**

- `tests/unit/test_enrich_planning_features.py::test_duplicate_source_ids_are_rejected`
- `tests/unit/test_enrich_planning_features.py::test_epsg4326_parcels_are_measured_in_lambert93_but_preserved`
- `tests/unit/test_enrich_planning_features.py::test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback`
- `tests/unit/test_enrich_planning_features.py::test_geospatial_operation_failure_is_controlled_and_chained`
- `tests/unit/test_enrich_planning_features.py::test_gpu_source_z_is_normalized_to_canonical_2d`
- `tests/unit/test_enrich_planning_features.py::test_idurba_mismatch_is_rejected`
- `tests/unit/test_enrich_planning_features.py::test_inputs_and_all_existing_parcel_fields_are_preserved`
- `tests/unit/test_enrich_planning_features.py::test_invalid_surface_geometry_is_rejected_without_repair`
- `tests/unit/test_enrich_planning_features.py::test_line_boundary_touch_is_zero_length`
- `tests/unit/test_enrich_planning_features.py::test_line_crossing_and_partly_inside`
- `tests/unit/test_enrich_planning_features.py::test_linestring_and_multilinestring`
- `tests/unit/test_enrich_planning_features.py::test_missing_crs_is_rejected`
- `tests/unit/test_enrich_planning_features.py::test_missing_required_source_fields_fail`
- `tests/unit/test_enrich_planning_features.py::test_mutated_source_summary_is_rejected`
- `tests/unit/test_enrich_planning_features.py::test_null_or_empty_source_geometry_is_rejected`
- `tests/unit/test_enrich_planning_features.py::test_optional_raw_source_fields_are_not_fabricated`
- `tests/unit/test_enrich_planning_features.py::test_overlapping_surface_union_is_not_double_counted`
- `tests/unit/test_enrich_planning_features.py::test_points_inside_boundary_outside_and_multipoint`
- `tests/unit/test_enrich_planning_features.py::test_polygon_and_multipolygon_surfaces`
- `tests/unit/test_enrich_planning_features.py::test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent`
- `tests/unit/test_enrich_planning_features.py::test_present_empty_optional_layer_is_valid`
- `tests/unit/test_enrich_planning_features.py::test_relations_are_unique_deterministic_and_summaries_agree`
- `tests/unit/test_enrich_planning_features.py::test_result_frames_are_independent_from_mutable_inputs`
- `tests/unit/test_enrich_planning_features.py::test_same_source_id_is_allowed_in_distinct_logical_layers`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_reordered_physical_gpkg_rows`
- `tests/unit/test_enrich_planning_features.py::test_source_summary_counts_are_strict_integers`
- `tests/unit/test_enrich_planning_features.py::test_surface_full_overlap_normalizes_raw_values_and_lineage`
- `tests/unit/test_enrich_planning_features.py::test_surface_partial_and_touch_relations`
- `tests/unit/test_enrich_planning_features.py::test_unusable_source_crs_is_rejected`
- `tests/unit/test_enrich_planning_features.py::test_wrong_geometry_kind_is_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_summary`

**Signature**

```python
def _summary(
    frame: gpd.GeoDataFrame,
    source_layer: str,
    *,
    document_id: str = DOCUMENT_ID,
    archive_sha: str = ARCHIVE_SHA,
) -> GpuLayerSummary:
```

**Purpose**

Implements summary according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_layer` (`str`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `document_id` (`str`; optional/default `DOCUMENT_ID`) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `archive_sha` (`str`; optional/default `ARCHIVE_SHA`) — integrity digest used to bind exact bytes or canonical content. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuLayerSummary`. Observed return expression(s): `GpuLayerSummary(source_document_id=document_id, source_archive_sha256=archive_sha, source_layer=source_layer, crs='UNKNOWN' if frame.crs is None else frame.crs.to_string(), feature_count=len(frame), columns=tuple((str(column) for column in frame.columns)), dtypes=tuple(((str(column), str(dtype)) for column, dtype in frame.dtypes.items())), null_counts=tuple(((str(column), int(frame[column].isna()…`.

**Algorithm**

1. Computes `geometry` from `frame.geometry`.
2. Computes `non_null` from `~geometry.isna()`.
3. Computes `non_empty` from `non_null & ~geometry.is_empty`.
4. Returns `GpuLayerSummary(source_document_id=document_id, source_archive_sha256=archive_sha, source_layer=source_layer, crs='UNKNOWN' if frame.crs is None else frame.crs.to_string(), feature_count=len(frame), columns=tuple((str(column) for column in frame.columns)), dtypes=tuple(((str(column), str(dtype)) for column, dtype in frame.dtypes.items())), null_counts=tuple…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `(non_empty & ~geometry.is_valid).sum`, `(non_null & geometry.is_empty).sum`, `(~non_null).sum`, `GpuLayerSummary`, `frame.crs.to_string`, `frame.dtypes.items`, `frame[column].isna`, `frame[column].isna().sum`, `geometry.geom_type.value_counts`, `geometry.geom_type.value_counts().sort_index`, `geometry.geom_type.value_counts().sort_index().items`, `geometry.isna`, `int`, `len`, `str`, `tuple`.

**Known repository callers**

- `tests/unit/test_enrich_planning_features.py` — `_inspected`
- `tests/unit/test_enrich_planning_features.py` — `_materialize_layer`
- `tests/unit/test_enrich_planning_features.py` — `_planning_document`
- `tests/unit/test_enrich_planning_features.py` — `_replace_related_layer`
- `tests/unit/test_enrich_planning_features.py` — `_shapefile_ogr_fid_source_complete_contract`
- `tests/unit/test_enrich_planning_features.py` — `_shapefile_source_complete_contract`
- `tests/unit/test_enrich_planning_features.py` — `test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent`

**Tests**

- `tests/unit/test_enrich_planning_features.py::test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_inspected`

**Signature**

```python
def _inspected(logical: str, frame: gpd.GeoDataFrame) -> GpuInspectedLayer:
```

**Purpose**

Implements inspected according to the exact implementation and guards in this file.

**Inputs**

- `logical` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuInspectedLayer`. Observed return expression(s): `GpuInspectedLayer(logical_name=logical, reference=reference, data=frame, summary=_summary(frame, source_layer))`.

**Algorithm**

1. Computes `source_layer` from `f'SOURCE_{logical.upper()}'`.
2. Computes `reference` from `GpuSpatialLayerReference(dataset_path=Path(f'synthetic-{logical}.gpkg'), source_layer=source_layer, driver='GPKG')`.
3. Returns `GpuInspectedLayer(logical_name=logical, reference=reference, data=frame, summary=_summary(frame, source_layer))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GpuInspectedLayer`, `GpuSpatialLayerReference`, `Path`, `_summary`, `logical.upper`.

**Known repository callers**

- `tests/unit/test_enrich_planning_features.py` — `_contract_result`
- `tests/unit/test_enrich_planning_features.py` — `_shapefile_ogr_fid_source_complete_contract`
- `tests/unit/test_enrich_planning_features.py` — `_shapefile_source_complete_contract`
- `tests/unit/test_enrich_planning_features.py` — `_source_complete_contract`
- `tests/unit/test_enrich_planning_features.py` — `_two_parcel_source_complete_contract`
- `tests/unit/test_enrich_planning_features.py` — `test_duplicate_source_ids_are_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_epsg4326_parcels_are_measured_in_lambert93_but_preserved`
- `tests/unit/test_enrich_planning_features.py` — `test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback`
- `tests/unit/test_enrich_planning_features.py` — `test_geospatial_operation_failure_is_controlled_and_chained`
- `tests/unit/test_enrich_planning_features.py` — `test_gpu_source_z_is_normalized_to_canonical_2d`
- `tests/unit/test_enrich_planning_features.py` — `test_idurba_mismatch_is_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_inputs_and_all_existing_parcel_fields_are_preserved`
- `tests/unit/test_enrich_planning_features.py` — `test_invalid_surface_geometry_is_rejected_without_repair`
- `tests/unit/test_enrich_planning_features.py` — `test_line_boundary_touch_is_zero_length`
- `tests/unit/test_enrich_planning_features.py` — `test_line_crossing_and_partly_inside`
- `tests/unit/test_enrich_planning_features.py` — `test_linestring_and_multilinestring`
- `tests/unit/test_enrich_planning_features.py` — `test_missing_crs_is_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_missing_required_source_fields_fail`
- `tests/unit/test_enrich_planning_features.py` — `test_mutated_source_summary_is_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_null_or_empty_source_geometry_is_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_optional_raw_source_fields_are_not_fabricated`
- `tests/unit/test_enrich_planning_features.py` — `test_overlapping_surface_union_is_not_double_counted`
- `tests/unit/test_enrich_planning_features.py` — `test_points_inside_boundary_outside_and_multipoint`
- `tests/unit/test_enrich_planning_features.py` — `test_polygon_and_multipolygon_surfaces`
- `tests/unit/test_enrich_planning_features.py` — `test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent`
- `tests/unit/test_enrich_planning_features.py` — `test_present_empty_optional_layer_is_valid`
- `tests/unit/test_enrich_planning_features.py` — `test_relations_are_unique_deterministic_and_summaries_agree`
- `tests/unit/test_enrich_planning_features.py` — `test_result_frames_are_independent_from_mutable_inputs`
- `tests/unit/test_enrich_planning_features.py` — `test_same_source_id_is_allowed_in_distinct_logical_layers`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_reordered_physical_gpkg_rows`
- `tests/unit/test_enrich_planning_features.py` — `test_source_summary_counts_are_strict_integers`
- `tests/unit/test_enrich_planning_features.py` — `test_surface_full_overlap_normalizes_raw_values_and_lineage`
- `tests/unit/test_enrich_planning_features.py` — `test_surface_partial_and_touch_relations`
- `tests/unit/test_enrich_planning_features.py` — `test_unusable_source_crs_is_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_wrong_geometry_kind_is_rejected`

**Tests**

- `tests/unit/test_enrich_planning_features.py::test_duplicate_source_ids_are_rejected`
- `tests/unit/test_enrich_planning_features.py::test_epsg4326_parcels_are_measured_in_lambert93_but_preserved`
- `tests/unit/test_enrich_planning_features.py::test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback`
- `tests/unit/test_enrich_planning_features.py::test_geospatial_operation_failure_is_controlled_and_chained`
- `tests/unit/test_enrich_planning_features.py::test_gpu_source_z_is_normalized_to_canonical_2d`
- `tests/unit/test_enrich_planning_features.py::test_idurba_mismatch_is_rejected`
- `tests/unit/test_enrich_planning_features.py::test_inputs_and_all_existing_parcel_fields_are_preserved`
- `tests/unit/test_enrich_planning_features.py::test_invalid_surface_geometry_is_rejected_without_repair`
- `tests/unit/test_enrich_planning_features.py::test_line_boundary_touch_is_zero_length`
- `tests/unit/test_enrich_planning_features.py::test_line_crossing_and_partly_inside`
- `tests/unit/test_enrich_planning_features.py::test_linestring_and_multilinestring`
- `tests/unit/test_enrich_planning_features.py::test_missing_crs_is_rejected`
- `tests/unit/test_enrich_planning_features.py::test_missing_required_source_fields_fail`
- `tests/unit/test_enrich_planning_features.py::test_mutated_source_summary_is_rejected`
- `tests/unit/test_enrich_planning_features.py::test_null_or_empty_source_geometry_is_rejected`
- `tests/unit/test_enrich_planning_features.py::test_optional_raw_source_fields_are_not_fabricated`
- `tests/unit/test_enrich_planning_features.py::test_overlapping_surface_union_is_not_double_counted`
- `tests/unit/test_enrich_planning_features.py::test_points_inside_boundary_outside_and_multipoint`
- `tests/unit/test_enrich_planning_features.py::test_polygon_and_multipolygon_surfaces`
- `tests/unit/test_enrich_planning_features.py::test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent`
- `tests/unit/test_enrich_planning_features.py::test_present_empty_optional_layer_is_valid`
- `tests/unit/test_enrich_planning_features.py::test_relations_are_unique_deterministic_and_summaries_agree`
- `tests/unit/test_enrich_planning_features.py::test_result_frames_are_independent_from_mutable_inputs`
- `tests/unit/test_enrich_planning_features.py::test_same_source_id_is_allowed_in_distinct_logical_layers`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_reordered_physical_gpkg_rows`
- `tests/unit/test_enrich_planning_features.py::test_source_summary_counts_are_strict_integers`
- `tests/unit/test_enrich_planning_features.py::test_surface_full_overlap_normalizes_raw_values_and_lineage`
- `tests/unit/test_enrich_planning_features.py::test_surface_partial_and_touch_relations`
- `tests/unit/test_enrich_planning_features.py::test_unusable_source_crs_is_rejected`
- `tests/unit/test_enrich_planning_features.py::test_wrong_geometry_kind_is_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_physical_inventory`

**Signature**

```python
def _physical_inventory(root: Path) -> tuple[GpuExtractedFile, ...]:
```

**Purpose**

Implements physical inventory according to the exact implementation and guards in this file.

**Inputs**

- `root` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[GpuExtractedFile, ...]`. Observed return expression(s): `tuple(records)`.

**Algorithm**

1. Defines `records` with annotation `list[GpuExtractedFile]` from `[]`.
2. Iterates `path` over `sorted((item for item in root.rglob('*') if item.is_file()), key=str)`. For each value: Checks `path.parent == root and path.name == EXTRACTION_MANIFEST_NAME`. When true: Executes `continue` control flow. Computes `suffix` from `path.suffix.casefold()`. Calls `records.append(GpuExtractedFile(relative_path=path.relative_to(root).as_posix(), file_type=suffix.lstrip('.') or 'none', size_bytes=path.stat().st_size, sha256=sha256(path.read_bytes()).hexdigest(), category='SPATIAL_DATA'))` for its validation or side effect.
3. Returns `tuple(records)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `path.read_bytes`, `sha256(path.read_bytes()).hexdigest`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GpuExtractedFile`, `item.is_file`, `path.read_bytes`, `path.relative_to`, `path.relative_to(root).as_posix`, `path.stat`, `path.suffix.casefold`, `records.append`, `root.rglob`, `sha256`, `sha256(path.read_bytes()).hexdigest`, `sorted`, `suffix.lstrip`, `tuple`.

**Known repository callers**

- `tests/unit/test_enrich_planning_features.py` — `_planning_document`
- `tests/unit/test_enrich_planning_features.py` — `_refresh_extraction_inventory`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_write_extraction_manifest`

**Signature**

```python
def _write_extraction_manifest(
    root: Path,
    archive_sha256: str,
    files: tuple[GpuExtractedFile, ...],
) -> None:
```

**Purpose**

Writes extraction manifest according to the exact implementation and guards in this file.

**Inputs**

- `root` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `archive_sha256` (`str`; required) — integrity digest used to bind exact bytes or canonical content. Nullability and accepted values are exactly those enforced by the guards listed below.
- `files` (`tuple[GpuExtractedFile, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `payload` from `{'schema_version': 2, 'archive_sha256': archive_sha256, 'files': [{'relative_path': item.relative_path, 'size_bytes': item.size_bytes, 'sha256': item.sha256} for item in files]}`.
2. Calls `(root / EXTRACTION_MANIFEST_NAME).write_text(json.dumps(payload, sort_keys=True, separators=(',', ':')), encoding='utf-8')` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `(root / EXTRACTION_MANIFEST_NAME).write_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `(root / EXTRACTION_MANIFEST_NAME).write_text`, `json.dumps`.

**Known repository callers**

- `tests/unit/test_enrich_planning_features.py` — `_planning_document`
- `tests/unit/test_enrich_planning_features.py` — `_refresh_extraction_inventory`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_materialize_layer`

**Signature**

```python
def _materialize_layer(root: Path, layer: GpuInspectedLayer) -> GpuInspectedLayer:
```

**Purpose**

Implements materialize layer according to the exact implementation and guards in this file.

**Inputs**

- `root` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `layer` (`GpuInspectedLayer`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuInspectedLayer`. Observed return expression(s): `replace(layer, reference=replace(reference, dataset_path=path), data=reread, summary=_summary(reread, reference.source_layer))`.

**Algorithm**

1. Computes `reference` from `layer.reference`.
2. Checks `reference.dataset_path.is_file()`. When true: Computes `path` from `reference.dataset_path.resolve()`. Otherwise: Computes `path` from `root / f'{layer.logical_name}.gpkg'`. Calls `layer.data.to_file(path, layer=reference.source_layer, driver='GPKG', engine='pyogrio', index=False)` for its validation or side effect. Executes 1 additional source-ordered statement(s).
3. Computes `reread` from `gpd.read_file(path, layer=reference.source_layer if reference.driver == 'GPKG' else None, engine='pyogrio')`.
4. Returns `replace(layer, reference=replace(reference, dataset_path=path), data=reread, summary=_summary(reread, reference.source_layer))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `gpd.read_file`, `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_summary`, `gpd.read_file`, `layer.data.to_file`, `reference.dataset_path.is_file`, `reference.dataset_path.resolve`, `replace`.

**Known repository callers**

- `tests/unit/test_enrich_planning_features.py` — `_planning_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_planning_document`

**Signature**

```python
def _planning_document(
    layers: list[GpuInspectedLayer] | None = None,
) -> GpuPlanningDocument:
```

**Purpose**

Implements planning document according to the exact implementation and guards in this file.

**Inputs**

- `layers` (`list[GpuInspectedLayer] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuPlanningDocument`. Observed return expression(s): `GpuPlanningDocument(extraction=extraction, all_spatial_layers=(zoning_ref, *(layer.reference for layer in related)), zoning=zoning, related_layers=related)`.

**Algorithm**

1. Computes `requested_layers` from `list(layers or [])`.
2. Computes `existing_paths` from `[layer.reference.dataset_path.resolve() for layer in requested_layers if layer.reference.dataset_path.is_file()]`.
3. Computes `extraction_root` from `existing_paths[0].parent if existing_paths else Path(tempfile.mkdtemp(prefix='landscout-feature-source-'))`.
4. Computes `related` from `tuple((_materialize_layer(extraction_root, layer) for layer in requested_layers))`.
5. Computes `metadata` from `GpuDocumentMetadata(provider="Géoportail de l'Urbanisme", portal='GPU', commune_code='31395', partition='DU_31395', document_id=DOCUMENT_ID, document_family='DU', document_type='PLU', document_title='Muret PLU', status='document.production', legal_status='APPROVED', effective_status='EN_VIGUEUR', version='10', archive…`.
6. Computes `archive` from `GpuArchiveDownload(document=metadata, download_timestamp='2026-08-12T12:00:00+00:00', filename=f'{ARCHIVE_NAME}.zip', archive_format='zip', file_size=1, sha256=ARCHIVE_SHA, path=Path('synthetic.zip'), cache_hit=True)`.
7. Computes `zoning_frame` from `gpd.GeoDataFrame({'zone': ['Z']}, geometry=[_rectangle(-10, -10, 20, 20)], crs='EPSG:2154')`.
8. Computes `zoning_path` from `extraction_root / 'zoning.gpkg'`.
9. Calls `zoning_frame.to_file(zoning_path, layer='ZONING', driver='GPKG', engine='pyogrio', index=False)` for its validation or side effect.
10. Computes `zoning_frame` from `gpd.read_file(zoning_path, layer='ZONING', engine='pyogrio')`.
11. Computes `zoning_ref` from `GpuSpatialLayerReference(zoning_path, 'ZONING', 'GPKG')`.
12. Computes `zoning` from `GpuInspectedLayer(logical_name='zoning', reference=zoning_ref, data=zoning_frame, summary=_summary(zoning_frame, 'ZONING'))`.
13. Computes `inventory` from `_physical_inventory(extraction_root)`.
14. Calls `_write_extraction_manifest(extraction_root, ARCHIVE_SHA, inventory)` for its validation or side effect.
15. Computes `extraction` from `GpuExtraction(archive=archive, extraction_root=extraction_root, files=inventory, standard_models=(STANDARD,), cache_hit=True)`.
16. Returns `GpuPlanningDocument(extraction=extraction, all_spatial_layers=(zoning_ref, *(layer.reference for layer in related)), zoning=zoning, related_layers=related)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `GpuArchiveDownload`, `_write_extraction_manifest`, `gpd.read_file`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GpuArchiveDownload`, `GpuDocumentMetadata`, `GpuExtraction`, `GpuInspectedLayer`, `GpuPlanningDocument`, `GpuSpatialLayerReference`, `Path`, `_materialize_layer`, `_physical_inventory`, `_rectangle`, `_summary`, `_write_extraction_manifest`, `gpd.GeoDataFrame`, `gpd.read_file`, `layer.reference.dataset_path.is_file`, `layer.reference.dataset_path.resolve`, `list`, `tempfile.mkdtemp`, `tuple`, `zoning_frame.to_file`.

**Known repository callers**

- `tests/unit/test_enrich_planning_features.py` — `_contract_result`
- `tests/unit/test_enrich_planning_features.py` — `_run`
- `tests/unit/test_enrich_planning_features.py` — `_shapefile_ogr_fid_source_complete_contract`
- `tests/unit/test_enrich_planning_features.py` — `_shapefile_source_complete_contract`
- `tests/unit/test_enrich_planning_features.py` — `_source_complete_contract`
- `tests/unit/test_enrich_planning_features.py` — `_two_parcel_source_complete_contract`
- `tests/unit/test_enrich_planning_features.py` — `test_inputs_and_all_existing_parcel_fields_are_preserved`
- `tests/unit/test_enrich_planning_features.py` — `test_mutated_source_summary_is_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_reordered_physical_gpkg_rows`
- `tests/unit/test_enrich_planning_features.py` — `test_source_summary_counts_are_strict_integers`

**Tests**

- `tests/unit/test_enrich_planning_features.py::test_inputs_and_all_existing_parcel_fields_are_preserved`
- `tests/unit/test_enrich_planning_features.py::test_mutated_source_summary_is_rejected`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_reordered_physical_gpkg_rows`
- `tests/unit/test_enrich_planning_features.py::test_source_summary_counts_are_strict_integers`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_run`

**Signature**

```python
def _run(
    layers: list[GpuInspectedLayer],
    parcels: gpd.GeoDataFrame | None = None,
) -> ParcelPlanningFeaturesResult:
```

**Purpose**

Implements run according to the exact implementation and guards in this file.

**Inputs**

- `layers` (`list[GpuInspectedLayer]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcels` (`gpd.GeoDataFrame | None`; optional/default `None`) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `ParcelPlanningFeaturesResult`. Observed return expression(s): `intersect_parcels_with_gpu_planning_features(parcels if parcels is not None else _parcels(), _planning_document(layers))`.

**Algorithm**

1. Returns `intersect_parcels_with_gpu_planning_features(parcels if parcels is not None else _parcels(), _planning_document(layers))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_parcels`, `_planning_document`, `intersect_parcels_with_gpu_planning_features`.

**Known repository callers**

- `tests/unit/test_enrich_planning_features.py` — `test_duplicate_parcel_ids_are_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_duplicate_source_ids_are_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_empty_and_nonempty_catalogs_have_identical_kind_schemas`
- `tests/unit/test_enrich_planning_features.py` — `test_epsg4326_parcels_are_measured_in_lambert93_but_preserved`
- `tests/unit/test_enrich_planning_features.py` — `test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback`
- `tests/unit/test_enrich_planning_features.py` — `test_geospatial_operation_failure_is_controlled_and_chained`
- `tests/unit/test_enrich_planning_features.py` — `test_gpu_source_z_is_normalized_to_canonical_2d`
- `tests/unit/test_enrich_planning_features.py` — `test_idurba_mismatch_is_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_invalid_parcel_ids_are_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_invalid_surface_geometry_is_rejected_without_repair`
- `tests/unit/test_enrich_planning_features.py` — `test_line_boundary_touch_is_zero_length`
- `tests/unit/test_enrich_planning_features.py` — `test_line_crossing_and_partly_inside`
- `tests/unit/test_enrich_planning_features.py` — `test_linestring_and_multilinestring`
- `tests/unit/test_enrich_planning_features.py` — `test_missing_crs_is_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_missing_optional_layer_families_return_stable_empty_catalogs`
- `tests/unit/test_enrich_planning_features.py` — `test_missing_required_source_fields_fail`
- `tests/unit/test_enrich_planning_features.py` — `test_null_or_empty_source_geometry_is_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_optional_raw_source_fields_are_not_fabricated`
- `tests/unit/test_enrich_planning_features.py` — `test_overlapping_surface_union_is_not_double_counted`
- `tests/unit/test_enrich_planning_features.py` — `test_points_inside_boundary_outside_and_multipoint`
- `tests/unit/test_enrich_planning_features.py` — `test_polygon_and_multipolygon_surfaces`
- `tests/unit/test_enrich_planning_features.py` — `test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent`
- `tests/unit/test_enrich_planning_features.py` — `test_present_empty_optional_layer_is_valid`
- `tests/unit/test_enrich_planning_features.py` — `test_relations_are_unique_deterministic_and_summaries_agree`
- `tests/unit/test_enrich_planning_features.py` — `test_reserved_output_column_collision_is_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_result_frames_are_independent_from_mutable_inputs`
- `tests/unit/test_enrich_planning_features.py` — `test_result_is_frozen`
- `tests/unit/test_enrich_planning_features.py` — `test_same_source_id_is_allowed_in_distinct_logical_layers`
- `tests/unit/test_enrich_planning_features.py` — `test_surface_full_overlap_normalizes_raw_values_and_lineage`
- `tests/unit/test_enrich_planning_features.py` — `test_surface_partial_and_touch_relations`
- `tests/unit/test_enrich_planning_features.py` — `test_unusable_source_crs_is_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_wrong_geometry_kind_is_rejected`

**Tests**

- `tests/unit/test_enrich_planning_features.py::test_duplicate_parcel_ids_are_rejected`
- `tests/unit/test_enrich_planning_features.py::test_duplicate_source_ids_are_rejected`
- `tests/unit/test_enrich_planning_features.py::test_empty_and_nonempty_catalogs_have_identical_kind_schemas`
- `tests/unit/test_enrich_planning_features.py::test_epsg4326_parcels_are_measured_in_lambert93_but_preserved`
- `tests/unit/test_enrich_planning_features.py::test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback`
- `tests/unit/test_enrich_planning_features.py::test_geospatial_operation_failure_is_controlled_and_chained`
- `tests/unit/test_enrich_planning_features.py::test_gpu_source_z_is_normalized_to_canonical_2d`
- `tests/unit/test_enrich_planning_features.py::test_idurba_mismatch_is_rejected`
- `tests/unit/test_enrich_planning_features.py::test_invalid_parcel_ids_are_rejected`
- `tests/unit/test_enrich_planning_features.py::test_invalid_surface_geometry_is_rejected_without_repair`
- `tests/unit/test_enrich_planning_features.py::test_line_boundary_touch_is_zero_length`
- `tests/unit/test_enrich_planning_features.py::test_line_crossing_and_partly_inside`
- `tests/unit/test_enrich_planning_features.py::test_linestring_and_multilinestring`
- `tests/unit/test_enrich_planning_features.py::test_missing_crs_is_rejected`
- `tests/unit/test_enrich_planning_features.py::test_missing_optional_layer_families_return_stable_empty_catalogs`
- `tests/unit/test_enrich_planning_features.py::test_missing_required_source_fields_fail`
- `tests/unit/test_enrich_planning_features.py::test_null_or_empty_source_geometry_is_rejected`
- `tests/unit/test_enrich_planning_features.py::test_optional_raw_source_fields_are_not_fabricated`
- `tests/unit/test_enrich_planning_features.py::test_overlapping_surface_union_is_not_double_counted`
- `tests/unit/test_enrich_planning_features.py::test_points_inside_boundary_outside_and_multipoint`
- `tests/unit/test_enrich_planning_features.py::test_polygon_and_multipolygon_surfaces`
- `tests/unit/test_enrich_planning_features.py::test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent`
- `tests/unit/test_enrich_planning_features.py::test_present_empty_optional_layer_is_valid`
- `tests/unit/test_enrich_planning_features.py::test_relations_are_unique_deterministic_and_summaries_agree`
- `tests/unit/test_enrich_planning_features.py::test_reserved_output_column_collision_is_rejected`
- `tests/unit/test_enrich_planning_features.py::test_result_frames_are_independent_from_mutable_inputs`
- `tests/unit/test_enrich_planning_features.py::test_result_is_frozen`
- `tests/unit/test_enrich_planning_features.py::test_same_source_id_is_allowed_in_distinct_logical_layers`
- `tests/unit/test_enrich_planning_features.py::test_surface_full_overlap_normalizes_raw_values_and_lineage`
- `tests/unit/test_enrich_planning_features.py::test_surface_partial_and_touch_relations`
- `tests/unit/test_enrich_planning_features.py::test_unusable_source_crs_is_rejected`
- `tests/unit/test_enrich_planning_features.py::test_wrong_geometry_kind_is_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_contract_result`

**Signature**

```python
def _contract_result() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    ParcelPlanningFeaturesResult,
]:
```

**Purpose**

Implements contract result according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `tuple[GpuPlanningDocument, gpd.GeoDataFrame, ParcelPlanningFeaturesResult]`. Observed return expression(s): `(planning_document, parcels, intersect_parcels_with_gpu_planning_features(parcels, planning_document))`.

**Algorithm**

1. Computes `parcels` from `_parcels()`.
2. Computes `layers` from `[_inspected('prescription_surface', _source_frame('prescription_surface', [_rectangle(0, 0, 10, 10)], ids=['SURFACE'])), _inspected('prescription_line', _source_frame('prescription_line', [LineString([(-1, 5), (11, 5)])], ids=['LINE'])), _inspected('prescription_point', _source_frame('prescription_point', [Point(5, 5)…`.
3. Computes `planning_document` from `_planning_document(layers)`.
4. Returns `(planning_document, parcels, intersect_parcels_with_gpu_planning_features(parcels, planning_document))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `LineString`, `Point`, `_inspected`, `_parcels`, `_planning_document`, `_rectangle`, `_source_frame`, `intersect_parcels_with_gpu_planning_features`.

**Known repository callers**

- `tests/unit/test_enrich_planning_features.py` — `test_corrupted_parcel_summary_is_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_corrupted_relation_semantics_are_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_corrupted_surface_union_contract_is_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_empty_and_nonempty_catalogs_have_identical_kind_schemas`
- `tests/unit/test_enrich_planning_features.py` — `test_feature_ids_are_globally_unique_across_catalogs`
- `tests/unit/test_enrich_planning_features.py` — `test_point_member_relation_semantics_are_exact`
- `tests/unit/test_enrich_planning_features.py` — `test_relation_must_match_feature_catalog`
- `tests/unit/test_enrich_planning_features.py` — `test_shared_intrinsic_relation_semantics_reject_every_invalid_case`
- `tests/unit/test_enrich_planning_features.py` — `test_strict_parcel_summary_integer_counts_are_enforced`
- `tests/unit/test_enrich_planning_features.py` — `test_strict_relation_integer_counts_are_enforced`

**Tests**

- `tests/unit/test_enrich_planning_features.py::test_corrupted_parcel_summary_is_rejected`
- `tests/unit/test_enrich_planning_features.py::test_corrupted_relation_semantics_are_rejected`
- `tests/unit/test_enrich_planning_features.py::test_corrupted_surface_union_contract_is_rejected`
- `tests/unit/test_enrich_planning_features.py::test_empty_and_nonempty_catalogs_have_identical_kind_schemas`
- `tests/unit/test_enrich_planning_features.py::test_feature_ids_are_globally_unique_across_catalogs`
- `tests/unit/test_enrich_planning_features.py::test_point_member_relation_semantics_are_exact`
- `tests/unit/test_enrich_planning_features.py::test_relation_must_match_feature_catalog`
- `tests/unit/test_enrich_planning_features.py::test_shared_intrinsic_relation_semantics_reject_every_invalid_case`
- `tests/unit/test_enrich_planning_features.py::test_strict_parcel_summary_integer_counts_are_enforced`
- `tests/unit/test_enrich_planning_features.py::test_strict_relation_integer_counts_are_enforced`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_source_complete_contract`

**Signature**

```python
def _source_complete_contract() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    ParcelPlanningFeaturesResult,
]:
```

**Purpose**

Implements source complete contract according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `tuple[GpuPlanningDocument, gpd.GeoDataFrame, ParcelPlanningFeaturesResult]`. Observed return expression(s): `(planning_document, parcels, result)`.

**Algorithm**

1. Computes `parcels` from `_parcels()`.
2. Computes `layers` from `[_inspected('prescription_surface', _source_frame('prescription_surface', [_rectangle(0, 0, 10, 10)], ids=['SURFACE'], type_codes=['07'], subtype_codes=['04'])), _inspected('prescription_line', _source_frame('prescription_line', [LineString([(-1, 5), (11, 5)])], ids=['LINE'], type_codes=['15'], subtype_codes=['00'])),…`.
3. Computes `planning_document` from `_planning_document(layers)`.
4. Computes `result` from `intersect_parcels_with_gpu_planning_features(parcels, planning_document)`.
5. Returns `(planning_document, parcels, result)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `LineString`, `Point`, `_inspected`, `_parcels`, `_planning_document`, `_rectangle`, `_source_frame`, `intersect_parcels_with_gpu_planning_features`.

**Known repository callers**

- `tests/unit/test_enrich_planning_features.py` — `test_batch_gpu_revalidation_rejects_duplicate_logical_name`
- `tests/unit/test_enrich_planning_features.py` — `test_batch_gpu_revalidation_rejects_malformed_layer_items`
- `tests/unit/test_enrich_planning_features.py` — `test_expected_relation_hash_binds_dtype_and_index_metadata`
- `tests/unit/test_enrich_planning_features.py` — `test_public_normalized_input_contract_rejects_stripped_catalog`
- `tests/unit/test_enrich_planning_features.py` — `test_public_normalized_input_contract_validates_step_7d_3_1_result`
- `tests/unit/test_enrich_planning_features.py` — `test_public_normalized_input_contract_wraps_malformed_document_context`
- `tests/unit/test_enrich_planning_features.py` — `test_public_source_validation_hashes_survive_parquet_readback`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_accepts_complete_parcel_output_summaries`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_accepts_epsg4326_parcels`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_binds_gpu_document_context`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_binds_inspected_spatial_inventory`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_catalog_for_absent_gpu_layer`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_changed_gpkg_bytes`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_changed_physical_gpkg_geometry`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_coherent_parcel_metric_mutation`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_coherently_changed_physical_gpkg`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_coherently_renamed_feature_identity`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_corrupted_complete_parcel_summaries`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_dataset_outside_extraction_root`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_duplicate_parcel_ids`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_each_corrupted_parcel_summary_fact`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_independent_gpu_lineage_mutation`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_invalid_parcel_geometry`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_linked_spatial_dataset`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_loaded_source_attrs_not_on_disk`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_noncanonical_parcel_summary_dtype`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_noncanonical_relation_dtype`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_partial_parcel_output_columns`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_relation_index_class_change`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_relation_index_dtype_change`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_relation_index_name_change`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_same_size_gpkg_byte_tamper`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_tampered_gpkg_inventory_hash`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_tampered_gpkg_size`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_unknown_relation_parcel`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_reloads_and_compares_source_catalog`
- `tests/unit/test_enrich_planning_features.py` — `test_source_document_reference_allows_one_archive_zip_suffix`
- `tests/unit/test_enrich_planning_features.py` — `test_three_dimensional_normalized_catalogs_are_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_two_dimensional_normalized_catalogs_remain_valid`

**Tests**

- `tests/unit/test_enrich_planning_features.py::test_batch_gpu_revalidation_rejects_duplicate_logical_name`
- `tests/unit/test_enrich_planning_features.py::test_batch_gpu_revalidation_rejects_malformed_layer_items`
- `tests/unit/test_enrich_planning_features.py::test_expected_relation_hash_binds_dtype_and_index_metadata`
- `tests/unit/test_enrich_planning_features.py::test_public_normalized_input_contract_rejects_stripped_catalog`
- `tests/unit/test_enrich_planning_features.py::test_public_normalized_input_contract_validates_step_7d_3_1_result`
- `tests/unit/test_enrich_planning_features.py::test_public_normalized_input_contract_wraps_malformed_document_context`
- `tests/unit/test_enrich_planning_features.py::test_public_source_validation_hashes_survive_parquet_readback`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_accepts_complete_parcel_output_summaries`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_accepts_epsg4326_parcels`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_binds_gpu_document_context`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_binds_inspected_spatial_inventory`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_catalog_for_absent_gpu_layer`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_changed_gpkg_bytes`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_changed_physical_gpkg_geometry`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_coherent_parcel_metric_mutation`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_coherently_changed_physical_gpkg`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_coherently_renamed_feature_identity`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_corrupted_complete_parcel_summaries`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_dataset_outside_extraction_root`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_duplicate_parcel_ids`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_each_corrupted_parcel_summary_fact`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_independent_gpu_lineage_mutation`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_invalid_parcel_geometry`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_linked_spatial_dataset`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_loaded_source_attrs_not_on_disk`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_noncanonical_parcel_summary_dtype`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_noncanonical_relation_dtype`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_partial_parcel_output_columns`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_relation_index_class_change`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_relation_index_dtype_change`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_relation_index_name_change`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_same_size_gpkg_byte_tamper`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_tampered_gpkg_inventory_hash`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_tampered_gpkg_size`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_unknown_relation_parcel`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_reloads_and_compares_source_catalog`
- `tests/unit/test_enrich_planning_features.py::test_source_document_reference_allows_one_archive_zip_suffix`
- `tests/unit/test_enrich_planning_features.py::test_three_dimensional_normalized_catalogs_are_rejected`
- `tests/unit/test_enrich_planning_features.py::test_two_dimensional_normalized_catalogs_remain_valid`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_two_parcel_source_complete_contract`

**Signature**

```python
def _two_parcel_source_complete_contract() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    ParcelPlanningFeaturesResult,
]:
```

**Purpose**

Build equal-area parcels so relation identity cannot hide behind area checks.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `tuple[GpuPlanningDocument, gpd.GeoDataFrame, ParcelPlanningFeaturesResult]`. Observed return expression(s): `(planning_document, parcels, result)`.

**Algorithm**

1. Computes `parcels` from `_parcels([_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)], ids=['P-1', 'P-2'])`.
2. Computes `layers` from `[_inspected('prescription_surface', _source_frame('prescription_surface', [_rectangle(0, 0, 10, 10)], ids=['SURFACE'], type_codes=['07'], subtype_codes=['04'])), _inspected('prescription_line', _source_frame('prescription_line', [LineString([(0, 5), (10, 5)])], ids=['LINE'], type_codes=['15'], subtype_codes=['00']))]`.
3. Computes `planning_document` from `_planning_document(layers)`.
4. Computes `result` from `intersect_parcels_with_gpu_planning_features(parcels, planning_document)`.
5. Returns `(planning_document, parcels, result)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `LineString`, `_inspected`, `_parcels`, `_planning_document`, `_rectangle`, `_source_frame`, `intersect_parcels_with_gpu_planning_features`.

**Known repository callers**

- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_coherent_but_wrong_line_metric`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_extra_geometrically_false_relation`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_missing_expected_relation`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_reordered_relations`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_same_area_wrong_parcel_relation`

**Tests**

- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_coherent_but_wrong_line_metric`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_extra_geometrically_false_relation`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_missing_expected_relation`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_reordered_relations`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_same_area_wrong_parcel_relation`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_validate_source_complete`

**Signature**

```python
def _validate_source_complete(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    result: ParcelPlanningFeaturesResult,
) -> PlanningFeatureInputValidation:
```

**Purpose**

Validates and rejects malformed source complete according to the exact implementation and guards in this file.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`ParcelPlanningFeaturesResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `PlanningFeatureInputValidation`. Observed return expression(s): `validate_normalized_planning_feature_inputs(planning_document, parcels, result.surface_features, result.line_features, result.point_features, result.relations)`.

**Algorithm**

1. Returns `validate_normalized_planning_feature_inputs(planning_document, parcels, result.surface_features, result.line_features, result.point_features, result.relations)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `validate_normalized_planning_feature_inputs`.

**Known repository callers**

- `tests/unit/test_enrich_planning_features.py` — `test_public_normalized_input_contract_wraps_malformed_document_context`
- `tests/unit/test_enrich_planning_features.py` — `test_public_source_validation_hashes_survive_parquet_readback`
- `tests/unit/test_enrich_planning_features.py` — `test_shapefile_family_excludes_dotted_sibling_dataset`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_accepts_complete_parcel_output_summaries`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_accepts_epsg4326_parcels`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_binds_every_shapefile_sidecar`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_binds_gpu_document_context`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_binds_inspected_spatial_inventory`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_catalog_for_absent_gpu_layer`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_changed_gpkg_bytes`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_changed_or_reordered_ogr_fids`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_changed_physical_gpkg_geometry`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_changed_shapefile_sidecar_bytes`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_coherent_but_wrong_line_metric`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_coherent_parcel_metric_mutation`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_coherently_changed_physical_gpkg`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_coherently_renamed_feature_identity`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_corrupted_complete_parcel_summaries`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_dataset_outside_extraction_root`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_duplicate_parcel_ids`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_each_corrupted_parcel_summary_fact`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_extra_geometrically_false_relation`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_independent_gpu_lineage_mutation`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_invalid_parcel_geometry`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_linked_spatial_dataset`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_loaded_source_attrs_not_on_disk`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_missing_expected_relation`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_noncanonical_parcel_summary_dtype`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_noncanonical_relation_dtype`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_partial_parcel_output_columns`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_relation_index_dtype_change`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_relation_index_name_change`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_reordered_physical_gpkg_rows`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_reordered_relations`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_same_area_wrong_parcel_relation`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_same_size_gpkg_byte_tamper`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_tampered_gpkg_inventory_hash`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_tampered_gpkg_size`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_unknown_relation_parcel`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_reloads_and_compares_source_catalog`
- 4 additional static callers are indexed by the completeness audit.

**Tests**

- `tests/unit/test_enrich_planning_features.py::test_public_normalized_input_contract_wraps_malformed_document_context`
- `tests/unit/test_enrich_planning_features.py::test_public_source_validation_hashes_survive_parquet_readback`
- `tests/unit/test_enrich_planning_features.py::test_shapefile_family_excludes_dotted_sibling_dataset`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_accepts_complete_parcel_output_summaries`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_accepts_epsg4326_parcels`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_binds_every_shapefile_sidecar`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_binds_gpu_document_context`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_binds_inspected_spatial_inventory`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_catalog_for_absent_gpu_layer`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_changed_gpkg_bytes`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_changed_or_reordered_ogr_fids`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_changed_physical_gpkg_geometry`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_changed_shapefile_sidecar_bytes`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_coherent_but_wrong_line_metric`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_coherent_parcel_metric_mutation`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_coherently_changed_physical_gpkg`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_coherently_renamed_feature_identity`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_corrupted_complete_parcel_summaries`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_dataset_outside_extraction_root`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_duplicate_parcel_ids`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_each_corrupted_parcel_summary_fact`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_extra_geometrically_false_relation`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_independent_gpu_lineage_mutation`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_invalid_parcel_geometry`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_linked_spatial_dataset`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_loaded_source_attrs_not_on_disk`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_missing_expected_relation`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_noncanonical_parcel_summary_dtype`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_noncanonical_relation_dtype`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_partial_parcel_output_columns`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_relation_index_dtype_change`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_relation_index_name_change`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_reordered_physical_gpkg_rows`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_reordered_relations`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_same_area_wrong_parcel_relation`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_same_size_gpkg_byte_tamper`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_tampered_gpkg_inventory_hash`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_tampered_gpkg_size`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_unknown_relation_parcel`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_reloads_and_compares_source_catalog`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_requires_shapefile_core_members`
- `tests/unit/test_enrich_planning_features.py::test_source_document_reference_allows_one_archive_zip_suffix`
- `tests/unit/test_enrich_planning_features.py::test_three_dimensional_normalized_catalogs_are_rejected`
- `tests/unit/test_enrich_planning_features.py::test_two_dimensional_normalized_catalogs_remain_valid`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_replace_related_layer`

**Signature**

```python
def _replace_related_layer(
    planning_document: GpuPlanningDocument,
    logical_name: str,
    frame: gpd.GeoDataFrame,
) -> GpuPlanningDocument:
```

**Purpose**

Implements replace related layer according to the exact implementation and guards in this file.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `logical_name` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuPlanningDocument`. Observed return expression(s): `replace(planning_document, related_layers=tuple(related))`.

**Algorithm**

1. Defines `related` with annotation `list[GpuInspectedLayer]` from `[]`.
2. Iterates `layer` over `planning_document.related_layers`. For each value: Checks `layer.logical_name != logical_name`. When true: Calls `related.append(layer)` for its validation or side effect. Executes `continue` control flow. Calls `related.append(replace(layer, data=frame, summary=_summary(frame, layer.reference.source_layer)))` for its validation or side effect.
3. Returns `replace(planning_document, related_layers=tuple(related))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_summary`, `related.append`, `replace`, `tuple`.

**Known repository callers**

- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_reloads_and_compares_source_catalog`

**Tests**

- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_reloads_and_compares_source_catalog`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_without_related_layer`

**Signature**

```python
def _without_related_layer(
    planning_document: GpuPlanningDocument,
    logical_name: str,
) -> GpuPlanningDocument:
```

**Purpose**

Implements without related layer according to the exact implementation and guards in this file.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `logical_name` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuPlanningDocument`. Observed return expression(s): `replace(planning_document, related_layers=tuple((layer for layer in planning_document.related_layers if layer.logical_name != logical_name)))`.

**Algorithm**

1. Returns `replace(planning_document, related_layers=tuple((layer for layer in planning_document.related_layers if layer.logical_name != logical_name)))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `replace`, `tuple`.

**Known repository callers**

- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_catalog_for_absent_gpu_layer`

**Tests**

- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_catalog_for_absent_gpu_layer`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_refresh_extraction_inventory`

**Signature**

```python
def _refresh_extraction_inventory(
    planning_document: GpuPlanningDocument,
) -> GpuPlanningDocument:
```

**Purpose**

Implements refresh extraction inventory according to the exact implementation and guards in this file.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuPlanningDocument`. Observed return expression(s): `replace(planning_document, extraction=replace(extraction, files=files))`.

**Algorithm**

1. Computes `extraction` from `planning_document.extraction`.
2. Computes `files` from `_physical_inventory(extraction.extraction_root)`.
3. Calls `_write_extraction_manifest(extraction.extraction_root, extraction.archive.sha256, files)` for its validation or side effect.
4. Returns `replace(planning_document, extraction=replace(extraction, files=files))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `_write_extraction_manifest`, `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_physical_inventory`, `_write_extraction_manifest`, `replace`.

**Known repository callers**

- `tests/unit/test_enrich_planning_features.py` — `test_shapefile_family_excludes_dotted_sibling_dataset`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_changed_physical_gpkg_geometry`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_coherently_changed_physical_gpkg`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_reordered_physical_gpkg_rows`

**Tests**

- `tests/unit/test_enrich_planning_features.py::test_shapefile_family_excludes_dotted_sibling_dataset`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_changed_physical_gpkg_geometry`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_coherently_changed_physical_gpkg`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_reordered_physical_gpkg_rows`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_replace_layer_reference`

**Signature**

```python
def _replace_layer_reference(
    planning_document: GpuPlanningDocument,
    logical_name: str,
    reference: GpuSpatialLayerReference,
) -> GpuPlanningDocument:
```

**Purpose**

Implements replace layer reference according to the exact implementation and guards in this file.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `logical_name` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `reference` (`GpuSpatialLayerReference`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuPlanningDocument`. Observed return expression(s): `replace(planning_document, related_layers=related, all_spatial_layers=spatial)`.

**Algorithm**

1. Computes `related` from `tuple((replace(layer, reference=reference) if layer.logical_name == logical_name else layer for layer in planning_document.related_layers))`.
2. Computes `old_reference` from `next((layer.reference for layer in planning_document.related_layers if layer.logical_name == logical_name))`.
3. Computes `spatial` from `tuple((reference if item == old_reference else item for item in planning_document.all_spatial_layers))`.
4. Returns `replace(planning_document, related_layers=related, all_spatial_layers=spatial)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `next`, `replace`, `tuple`.

**Known repository callers**

- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_dataset_outside_extraction_root`

**Tests**

- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_dataset_outside_extraction_root`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_geospatial_operation_failure_is_controlled_and_chained.fail_join`

**Signature**

```python
def fail_join(*args: object, **kwargs: object) -> object:
```

**Purpose**

Implements fail join according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Raises `RuntimeError('synthetic spatial-index failure')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `RuntimeError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `RuntimeError`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_linked_spatial_dataset.synthetic_link`

**Signature**

```python
def synthetic_link(path: Path) -> bool:
```

**Purpose**

Implements synthetic link according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `path == dataset or actual_link_check(path)`.

**Algorithm**

1. Returns `path == dataset or actual_link_check(path)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `actual_link_check`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_shapefile_source_complete_contract`

**Signature**

```python
def _shapefile_source_complete_contract(
    root: Path,
) -> tuple[GpuPlanningDocument, gpd.GeoDataFrame, ParcelPlanningFeaturesResult]:
```

**Purpose**

Implements shapefile source complete contract according to the exact implementation and guards in this file.

**Inputs**

- `root` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[GpuPlanningDocument, gpd.GeoDataFrame, ParcelPlanningFeaturesResult]`. Observed return expression(s): `(document, parcels, result)`.

**Algorithm**

1. Computes `source_layer` from `'PRESCRIPTION_SURFACE'`.
2. Computes `path` from `root / f'{source_layer}.shp'`.
3. Computes `frame` from `_source_frame('prescription_surface', [_rectangle(0, 0, 10, 10)], ids=['SHAPE-1'], type_codes=['07'], subtype_codes=['04'])`.
4. Calls `frame.to_file(path, driver='ESRI Shapefile', engine='pyogrio', index=False)` for its validation or side effect.
5. Computes `loaded` from `gpd.read_file(path, engine='pyogrio')`.
6. Computes `layer` from `replace(_inspected('prescription_surface', loaded), reference=GpuSpatialLayerReference(path, source_layer, 'ESRI Shapefile'), summary=_summary(loaded, source_layer))`.
7. Computes `document` from `_planning_document([layer])`.
8. Computes `parcels` from `_parcels()`.
9. Computes `result` from `intersect_parcels_with_gpu_planning_features(parcels, document)`.
10. Returns `(document, parcels, result)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `gpd.read_file`, `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GpuSpatialLayerReference`, `_inspected`, `_parcels`, `_planning_document`, `_rectangle`, `_source_frame`, `_summary`, `frame.to_file`, `gpd.read_file`, `intersect_parcels_with_gpu_planning_features`, `replace`.

**Known repository callers**

- `tests/unit/test_enrich_planning_features.py` — `test_shapefile_family_excludes_dotted_sibling_dataset`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_binds_every_shapefile_sidecar`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_changed_shapefile_sidecar_bytes`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_requires_shapefile_core_members`

**Tests**

- `tests/unit/test_enrich_planning_features.py::test_shapefile_family_excludes_dotted_sibling_dataset`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_binds_every_shapefile_sidecar`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_changed_shapefile_sidecar_bytes`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_requires_shapefile_core_members`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_shapefile_ogr_fid_source_complete_contract`

**Signature**

```python
def _shapefile_ogr_fid_source_complete_contract(
    root: Path,
) -> tuple[GpuPlanningDocument, gpd.GeoDataFrame, ParcelPlanningFeaturesResult]:
```

**Purpose**

Implements shapefile ogr fid source complete contract according to the exact implementation and guards in this file.

**Inputs**

- `root` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[GpuPlanningDocument, gpd.GeoDataFrame, ParcelPlanningFeaturesResult]`. Observed return expression(s): `(document, parcels, result)`.

**Algorithm**

1. Computes `source_layer` from `'PRESCRIPTION_SURFACE'`.
2. Computes `path` from `root / f'{source_layer}.shp'`.
3. Computes `frame` from `_source_frame('prescription_surface', [_rectangle(0, 0, 5, 10), _rectangle(5, 0, 10, 10)], ids=['DROP-ONE', 'DROP-TWO'], type_codes=['07', '07'], subtype_codes=['04', '04']).drop(columns='LIB_IDPSC')`.
4. Calls `frame.to_file(path, driver='ESRI Shapefile', engine='pyogrio', index=False)` for its validation or side effect.
5. Computes `loaded` from `gpd.read_file(path, engine='pyogrio')`.
6. Computes `layer` from `replace(_inspected('prescription_surface', loaded), reference=GpuSpatialLayerReference(path, source_layer, 'ESRI Shapefile'), summary=_summary(loaded, source_layer))`.
7. Computes `document` from `_planning_document([layer])`.
8. Computes `parcels` from `_parcels()`.
9. Computes `result` from `intersect_parcels_with_gpu_planning_features(parcels, document)`.
10. Returns `(document, parcels, result)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `gpd.read_file`, `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GpuSpatialLayerReference`, `_inspected`, `_parcels`, `_planning_document`, `_rectangle`, `_source_frame`, `_source_frame('prescription_surface', [_rectangle(0, 0, 5, 10), _rectangle(5, 0, 10, 10)], ids=['DROP-ONE', 'DROP-TWO'], type_codes=['07', '07'], subtype_codes=['04', '04']).drop`, `_summary`, `frame.to_file`, `gpd.read_file`, `intersect_parcels_with_gpu_planning_features`, `replace`.

**Known repository callers**

- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_changed_or_reordered_ogr_fids`

**Tests**

- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_changed_or_reordered_ogr_fids`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_changed_or_reordered_ogr_fids.changed_fid_read`

**Signature**

```python
def changed_fid_read(*args: object, **kwargs: object) -> gpd.GeoDataFrame:
```

**Purpose**

Implements changed fid read according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `reread`.

**Algorithm**

1. Computes `reread` from `actual_read(*args, **kwargs)`.
2. Checks `kwargs.get('fid_as_index')`. When true: Computes `reread.index` from `pd.Index(changed_fids, name='fid')`.
3. Returns `reread`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `actual_read`, `kwargs.get`, `pd.Index`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_only_high_level_api_is_exported`

**Signature**

```python
def test_only_high_level_api_is_exported() -> None:
```

**Purpose**

Protects the `only high level api is exported` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls only local assertions/expressions.

**Expected result**

- Direct assertions: `assert stages.intersect_parcels_with_gpu_planning_features is intersect_parcels_with_gpu_planning_features`; `assert 'intersect_parcels_with_gpu_planning_features' in stages.__all__`; `assert stages.PlanningFeaturesError is PlanningFeaturesError`; `assert stages.ParcelPlanningFeaturesResult is ParcelPlanningFeaturesResult`; `assert 'PlanningFeaturesError' in stages.__all__`; `assert 'ParcelPlanningFeaturesResult' in stages.__all__`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `only high level api is exported` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- No calls.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_result_is_frozen`

**Signature**

```python
def test_result_is_frozen() -> None:
```

**Purpose**

Protects the `result is frozen` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_run([])`.
- Enters managed context(s) `pytest.raises(FrozenInstanceError)` and executes: Computes `result.parcels` from `result.parcels.copy()`.

**Action**

- Calls `_run`, `result.parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(FrozenInstanceError): result.parcels = result.parcels.copy()`.

**Regression protected**

- Protects the exact `result is frozen` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_run`, `pytest.raises`, `result.parcels.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_surface_full_overlap_normalizes_raw_values_and_lineage`

**Signature**

```python
def test_surface_full_overlap_normalizes_raw_values_and_lineage() -> None:
```

**Purpose**

Protects the `surface full overlap normalizes raw values and lineage` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `layer` from `_inspected('prescription_surface', _source_frame('prescription_surface', [_rectangle(0, 0, 10, 10)], ids=['PSC-1'], type_codes=['DYNAMIC-18'], subtype_codes=['04'], crs='IGNF:LAMB93'))`.
- Computes `result` from `_run([layer])`.
- Computes `feature` from `result.surface_features.iloc[0]`.
- Computes `relation` from `result.relations.iloc[0]`.
- Computes `parcel` from `result.parcels.iloc[0]`.

**Action**

- Calls `_inspected`, `_rectangle`, `_run`, `_source_frame`, `pd.isna`, `result.surface_features.crs.to_epsg`.

**Expected result**

- Direct assertions: `assert feature['planning_feature_id'] == f'GPU:{DOCUMENT_ID}:prescription_surface:PSC-1'`; `assert feature['source_feature_id'] == 'PSC-1'`; `assert feature['source_identity_kind'] == 'CNIG_ATTRIBUTE'`; `assert feature['source_identity_field'] == 'LIB_IDPSC'`; `assert feature['feature_family'] == 'PRESCRIPTION'`; `assert feature['geometry_kind'] == 'SURFACE'`; `assert feature['type_code_raw'] == 'DYNAMIC-18'`; `assert feature['subtype_code_raw'] == '04'`; `assert feature['label_raw'] == 'Label 0'`; `assert feature['text_raw'] == 'Text 0'`; `assert feature['source_document_id'] == DOCUMENT_ID`; `assert feature['source_archive_sha256'] == ARCHIVE_SHA`; `assert feature['source_layer'] == 'SOURCE_PRESCRIPTION_SURFACE'`; `assert feature['source_crs'] == 'EPSG:2154'`; `assert feature['feature_area_m2'] == pytest.approx(100.0)`; `assert result.surface_features.crs.to_epsg() == 2154`; `assert relation['source_identity_kind'] == 'CNIG_ATTRIBUTE'`; `assert relation['source_identity_field'] == 'LIB_IDPSC'`; `assert relation['relation_type'] == 'AREA_OVERLAP'`; `assert relation['intersection_area_m2'] == pytest.approx(100.0)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `surface full overlap normalizes raw values and lineage` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inspected`, `_rectangle`, `_run`, `_source_frame`, `pd.isna`, `pytest.approx`, `result.surface_features.crs.to_epsg`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_surface_partial_and_touch_relations`

**Signature**

```python
def test_surface_partial_and_touch_relations() -> None:
```

**Purpose**

Protects the `surface partial and touch relations` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `frame` from `_source_frame('prescription_surface', [_rectangle(0, 0, 5, 10), _rectangle(10, 0, 20, 10)], ids=['PART', 'TOUCH'])`.
- Computes `result` from `_run([_inspected('prescription_surface', frame)])`.
- Computes `relations` from `result.relations.set_index('source_feature_id')`.

**Action**

- Calls `_inspected`, `_rectangle`, `_run`, `_source_frame`, `result.relations.set_index`.

**Expected result**

- Direct assertions: `assert relations.loc['PART', 'relation_type'] == 'AREA_OVERLAP'`; `assert relations.loc['PART', 'intersection_area_m2'] == pytest.approx(50.0)`; `assert relations.loc['TOUCH', 'relation_type'] == 'TOUCH_ONLY'`; `assert relations.loc['TOUCH', 'intersection_area_m2'] == pytest.approx(0.0)`; `assert result.parcels.iloc[0]['planning_surface_touch_count'] == 1`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `surface partial and touch relations` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inspected`, `_rectangle`, `_run`, `_source_frame`, `pytest.approx`, `result.relations.set_index`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_overlapping_surface_union_is_not_double_counted`

**Signature**

```python
def test_overlapping_surface_union_is_not_double_counted() -> None:
```

**Purpose**

Protects the `overlapping surface union is not double counted` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `prescription` from `_inspected('prescription_surface', _source_frame('prescription_surface', [_rectangle(0, 0, 10, 10)], ids=['WHOLE']))`.
- Computes `information` from `_inspected('information_surface', _source_frame('information_surface', [_rectangle(0, 0, 5, 10)], ids=['HALF'], type_codes=['99'], subtype_codes=['00']))`.
- Computes `parcel` from `_run([prescription, information]).parcels.iloc[0]`.

**Action**

- Calls `_inspected`, `_rectangle`, `_run`, `_source_frame`.

**Expected result**

- Direct assertions: `assert parcel['planning_surface_intersection_area_sum_m2'] == pytest.approx(150.0)`; `assert parcel['planning_surface_covered_union_area_m2'] == pytest.approx(100.0)`; `assert parcel['planning_surface_covered_pct'] == pytest.approx(100.0)`; `assert parcel['prescription_surface_covered_union_area_m2'] == pytest.approx(100.0)`; `assert parcel['information_surface_covered_union_area_m2'] == pytest.approx(50.0)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `overlapping surface union is not double counted` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inspected`, `_rectangle`, `_run`, `_source_frame`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_polygon_and_multipolygon_surfaces`

**Signature**

```python
def test_polygon_and_multipolygon_surfaces(geometry: object) -> None:
```

**Purpose**

Protects the `polygon and multipolygon surfaces` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry`.
- Contains 1 explicit setup/context statement(s).
- Computes `result` from `_run([_inspected('information_surface', _source_frame('information_surface', [geometry]))])`.

**Action**

- Calls `MultiPolygon`, `_inspected`, `_rectangle`, `_run`, `_source_frame`.

**Expected result**

- Direct assertions: `assert len(result.relations) == 1`; `assert result.relations.iloc[0]['intersection_area_m2'] > 0`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `polygon and multipolygon surfaces` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `MultiPolygon`, `_inspected`, `_rectangle`, `_run`, `_source_frame`, `len`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_line_crossing_and_partly_inside`

**Signature**

```python
def test_line_crossing_and_partly_inside() -> None:
```

**Purpose**

Protects the `line crossing and partly inside` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `frame` from `_source_frame('prescription_line', [LineString([(-5, 5), (15, 5)]), LineString([(5, 5), (15, 5)])], ids=['CROSS', 'PART'], type_codes=['15', '15'], subtype_codes=['01', '00'])`.
- Computes `result` from `_run([_inspected('prescription_line', frame)])`.
- Computes `relations` from `result.relations.set_index('source_feature_id')`.
- Computes `parcel` from `result.parcels.iloc[0]`.

**Action**

- Calls `LineString`, `_inspected`, `_run`, `_source_frame`, `result.relations.set_index`.

**Expected result**

- Direct assertions: `assert relations.loc['CROSS', 'relation_type'] == 'LENGTH_OVERLAP'`; `assert relations.loc['CROSS', 'intersection_length_m'] == pytest.approx(10.0)`; `assert relations.loc['CROSS', 'source_line_length_m'] == pytest.approx(20.0)`; `assert relations.loc['PART', 'intersection_length_m'] == pytest.approx(5.0)`; `assert parcel['planning_line_relation_count'] == 2`; `assert parcel['planning_line_intersection_length_sum_m'] == pytest.approx(15.0)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `line crossing and partly inside` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `_inspected`, `_run`, `_source_frame`, `pytest.approx`, `result.relations.set_index`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_line_boundary_touch_is_zero_length`

**Signature**

```python
def test_line_boundary_touch_is_zero_length() -> None:
```

**Purpose**

Protects the `line boundary touch is zero length` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `frame` from `_source_frame('prescription_line', [LineString([(10, 5), (15, 5)])], ids=['TOUCH'])`.
- Computes `result` from `_run([_inspected('prescription_line', frame)])`.

**Action**

- Calls `LineString`, `_inspected`, `_run`, `_source_frame`.

**Expected result**

- Direct assertions: `assert result.relations.iloc[0]['relation_type'] == 'TOUCH_ONLY'`; `assert result.relations.iloc[0]['intersection_length_m'] == pytest.approx(0.0)`; `assert result.parcels.iloc[0]['planning_line_touch_count'] == 1`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `line boundary touch is zero length` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `_inspected`, `_run`, `_source_frame`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_linestring_and_multilinestring`

**Signature**

```python
def test_linestring_and_multilinestring(geometry: object) -> None:
```

**Purpose**

Protects the `linestring and multilinestring` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry`.
- Contains 1 explicit setup/context statement(s).
- Computes `result` from `_run([_inspected('prescription_line', _source_frame('prescription_line', [geometry]))])`.

**Action**

- Calls `LineString`, `MultiLineString`, `_inspected`, `_run`, `_source_frame`.

**Expected result**

- Direct assertions: `assert result.relations.iloc[0]['intersection_length_m'] > 0`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `linestring and multilinestring` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `MultiLineString`, `_inspected`, `_run`, `_source_frame`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_points_inside_boundary_outside_and_multipoint`

**Signature**

```python
def test_points_inside_boundary_outside_and_multipoint() -> None:
```

**Purpose**

Protects the `points inside boundary outside and multipoint` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `frame` from `_source_frame('prescription_point', [Point(5, 5), Point(10, 5), Point(20, 20), MultiPoint([(3, 3), (10, 4), (30, 30)])], ids=['IN', 'BOUNDARY', 'OUT', 'MULTI'], type_codes=['07'] * 4, subtype_codes=['00'] * 4)`.
- Computes `result` from `_run([_inspected('prescription_point', frame)])`.
- Computes `relations` from `result.relations.set_index('source_feature_id')`.
- Computes `parcel` from `result.parcels.iloc[0]`.

**Action**

- Calls `MultiPoint`, `Point`, `_inspected`, `_run`, `_source_frame`, `result.relations.set_index`.

**Expected result**

- Direct assertions: `assert set(relations.index) == {'IN', 'BOUNDARY', 'MULTI'}`; `assert relations.loc['IN', 'relation_type'] == 'INSIDE'`; `assert relations.loc['BOUNDARY', 'relation_type'] == 'BOUNDARY_TOUCH'`; `assert relations.loc['MULTI', 'point_member_count'] == 3`; `assert relations.loc['MULTI', 'point_members_inside_count'] == 1`; `assert relations.loc['MULTI', 'point_members_boundary_count'] == 1`; `assert parcel['planning_point_relation_count'] == 3`; `assert parcel['planning_point_inside_count'] == 2`; `assert parcel['planning_point_boundary_count'] == 2`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `points inside boundary outside and multipoint` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `MultiPoint`, `Point`, `_inspected`, `_run`, `_source_frame`, `result.relations.set_index`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_optional_layer_families_return_stable_empty_catalogs`

**Signature**

```python
def test_missing_optional_layer_families_return_stable_empty_catalogs() -> None:
```

**Purpose**

Protects the `missing optional layer families return stable empty catalogs` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `result` from `_run([])`.

**Action**

- Calls `_run`, `result.surface_features.crs.to_epsg`.

**Expected result**

- Direct assertions: `assert result.surface_features.empty`; `assert result.line_features.empty`; `assert result.point_features.empty`; `assert result.relations.empty`; `assert result.surface_features.crs.to_epsg() == 2154`; `assert str(result.relations['point_member_count'].dtype) == 'Int64'`; `assert result.parcels.iloc[0]['planning_surface_relation_count'] == 0`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `missing optional layer families return stable empty catalogs` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_run`, `result.surface_features.crs.to_epsg`, `str`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_optional_raw_source_fields_are_not_fabricated`

**Signature**

```python
def test_optional_raw_source_fields_are_not_fabricated() -> None:
```

**Purpose**

Protects the `optional raw source fields are not fabricated` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `frame` from `_source_frame('prescription_line', [LineString([(0, 5), (10, 5)])]).drop(columns=['LIBELLE', 'TXT', 'NOMFIC', 'URLFIC', 'DATVALID'])`.
- Computes `result` from `_run([_inspected('prescription_line', frame)])`.
- Computes `feature` from `result.line_features.iloc[0]`.

**Action**

- Calls `LineString`, `_inspected`, `_run`, `_source_frame`, `_source_frame('prescription_line', [LineString([(0, 5), (10, 5)])]).drop`, `pd.isna`.

**Expected result**

- Direct assertions: `assert pd.isna(feature[column])`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `optional raw source fields are not fabricated` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `_inspected`, `_run`, `_source_frame`, `_source_frame('prescription_line', [LineString([(0, 5), (10, 5)])]).drop`, `pd.isna`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_epsg4326_parcels_are_measured_in_lambert93_but_preserved`

**Signature**

```python
def test_epsg4326_parcels_are_measured_in_lambert93_but_preserved() -> None:
```

**Purpose**

Protects the `epsg4326 parcels are measured in lambert93 but preserved` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `parcel` from `_parcels(crs='EPSG:4326')`.
- Computes `original` from `parcel.copy(deep=True)`.
- Computes `result` from `_run([_inspected('prescription_surface', _source_frame('prescription_surface', [_rectangle(0, 0, 10, 10)]))], parcel)`.

**Action**

- Calls `_inspected`, `_parcels`, `_rectangle`, `_run`, `_source_frame`, `np.array_equal`, `original.geometry.to_wkb`, `parcel.copy`, `result.parcels.geometry.to_wkb`.

**Expected result**

- Direct assertions: `assert result.parcels.crs == original.crs`; `assert np.array_equal(result.parcels.geometry.to_wkb(), original.geometry.to_wkb())`; `assert result.relations.iloc[0]['intersection_area_m2'] == pytest.approx(100.0)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `epsg4326 parcels are measured in lambert93 but preserved` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inspected`, `_parcels`, `_rectangle`, `_run`, `_source_frame`, `np.array_equal`, `original.geometry.to_wkb`, `parcel.copy`, `pytest.approx`, `result.parcels.geometry.to_wkb`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_parcel_ids_are_rejected`

**Signature**

```python
def test_invalid_parcel_ids_are_rejected(bad_id: object) -> None:
```

**Purpose**

Protects the `invalid parcel ids are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `bad_id`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='parcel_id')` and executes: Calls `_run([], _parcels(ids=[bad_id]))` for its validation or side effect.

**Action**

- Calls `_parcels`, `_run`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='parcel_id'): _run([], _parcels(ids=[bad_id]))`.

**Regression protected**

- Protects the exact `invalid parcel ids are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_run`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_parcel_ids_are_rejected`

**Signature**

```python
def test_duplicate_parcel_ids_are_rejected() -> None:
```

**Purpose**

Protects the `duplicate parcel ids are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='unique')` and executes: Calls `_run([], _parcels([_rectangle(0, 0, 2, 2), _rectangle(3, 3, 4, 4)], ids=['P', 'P']))` for its validation or side effect.

**Action**

- Calls `_parcels`, `_rectangle`, `_run`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='unique'): _run([], _parcels([_rectangle(0, 0, 2, 2), _rectangle(3, 3, 4, 4)], ids=['P', 'P']))`.

**Regression protected**

- Protects the exact `duplicate parcel ids are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_rectangle`, `_run`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_source_ids_are_rejected`

**Signature**

```python
def test_duplicate_source_ids_are_rejected() -> None:
```

**Purpose**

Protects the `duplicate source ids are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `frame` from `_source_frame('information_surface', [_rectangle(0, 0, 2, 2), _rectangle(3, 3, 4, 4)], ids=['SAME', 'SAME'])`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='unique')` and executes: Calls `_run([_inspected('information_surface', frame)])` for its validation or side effect.

**Action**

- Calls `_inspected`, `_rectangle`, `_run`, `_source_frame`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='unique'): _run([_inspected('information_surface', frame)])`.

**Regression protected**

- Protects the exact `duplicate source ids are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inspected`, `_rectangle`, `_run`, `_source_frame`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent`

**Signature**

```python
def test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `prescription surface uses validated source ogr fid when cnig id absent` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 8 explicit setup/context statement(s).
- Computes `source_layer` from `'PRESCRIPTION_SURFACE'`.
- Computes `path` from `tmp_path / f'{source_layer}.shp'`.
- Computes `frame` from `_source_frame('prescription_surface', [_rectangle(0, 0, 10, 10)]).drop(columns='LIB_IDPSC')`.
- Computes `loaded` from `gpd.read_file(path, engine='pyogrio')`.
- Computes `layer` from `_inspected('prescription_surface', loaded)`.
- Computes `reference` from `replace(layer.reference, dataset_path=path, source_layer=source_layer, driver='ESRI Shapefile')`.
- Computes `layer` from `replace(layer, reference=reference, summary=_summary(loaded, source_layer))`.
- Computes `result` from `_run([layer])`.

**Action**

- Calls `_inspected`, `_rectangle`, `_run`, `_source_frame`, `_source_frame('prescription_surface', [_rectangle(0, 0, 10, 10)]).drop`, `_summary`, `frame.to_file`, `gpd.read_file`, `replace`.

**Expected result**

- Direct assertions: `assert result.surface_features.iloc[0]['source_feature_id'] == 'OGR_FID:0'`; `assert result.surface_features.iloc[0]['source_identity_kind'] == 'ARCHIVE_SCOPED_OGR_FID'`; `assert result.surface_features.iloc[0]['source_identity_field'] == 'OGR_FID'`; `assert result.surface_features.iloc[0]['planning_feature_id'] == f'GPU:{DOCUMENT_ID}:prescription_surface:OGR_FID:0'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `prescription surface uses validated source ogr fid when cnig id absent` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; synthetic GeoPackage. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inspected`, `_rectangle`, `_run`, `_source_frame`, `_source_frame('prescription_surface', [_rectangle(0, 0, 10, 10)]).drop`, `_summary`, `frame.to_file`, `gpd.read_file`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback`

**Signature**

```python
def test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback() -> None:
```

**Purpose**

Protects the `geopackage prescription surface uses sealed ogr fid fallback` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `frame` from `_source_frame('prescription_surface', [_rectangle(0, 0, 10, 10)]).drop(columns='LIB_IDPSC')`.
- Computes `result` from `_run([_inspected('prescription_surface', frame)])`.
- Computes `feature` from `result.surface_features.iloc[0]`.

**Action**

- Calls `_inspected`, `_rectangle`, `_run`, `_source_frame`, `_source_frame('prescription_surface', [_rectangle(0, 0, 10, 10)]).drop`.

**Expected result**

- Direct assertions: `assert feature['source_feature_id'] == 'OGR_FID:1'`; `assert feature['source_identity_kind'] == 'ARCHIVE_SCOPED_OGR_FID'`; `assert feature['source_identity_field'] == 'OGR_FID'`; `assert feature['planning_feature_id'] == f'GPU:{DOCUMENT_ID}:prescription_surface:OGR_FID:1'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `geopackage prescription surface uses sealed ogr fid fallback` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inspected`, `_rectangle`, `_run`, `_source_frame`, `_source_frame('prescription_surface', [_rectangle(0, 0, 10, 10)]).drop`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_idurba_mismatch_is_rejected`

**Signature**

```python
def test_idurba_mismatch_is_rejected() -> None:
```

**Purpose**

Protects the `idurba mismatch is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `frame` from `_source_frame('prescription_line', [LineString([(0, 5), (10, 5)])], document_refs=['OTHER'])`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='IDURBA')` and executes: Calls `_run([_inspected('prescription_line', frame)])` for its validation or side effect.

**Action**

- Calls `LineString`, `_inspected`, `_run`, `_source_frame`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='IDURBA'): _run([_inspected('prescription_line', frame)])`.

**Regression protected**

- Protects the exact `idurba mismatch is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `_inspected`, `_run`, `_source_frame`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_required_source_fields_fail`

**Signature**

```python
def test_missing_required_source_fields_fail(missing: str) -> None:
```

**Purpose**

Protects the `missing required source fields fail` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `missing`.
- Contains 2 explicit setup/context statement(s).
- Computes `frame` from `_source_frame('prescription_line', [LineString([(0, 5), (10, 5)])]).drop(columns=missing)`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match=missing)` and executes: Calls `_run([_inspected('prescription_line', frame)])` for its validation or side effect.

**Action**

- Calls `LineString`, `_inspected`, `_run`, `_source_frame`, `_source_frame('prescription_line', [LineString([(0, 5), (10, 5)])]).drop`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match=missing): _run([_inspected('prescription_line', frame)])`.

**Regression protected**

- Protects the exact `missing required source fields fail` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `_inspected`, `_run`, `_source_frame`, `_source_frame('prescription_line', [LineString([(0, 5), (10, 5)])]).drop`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_wrong_geometry_kind_is_rejected`

**Signature**

```python
def test_wrong_geometry_kind_is_rejected(logical: str, geometry: object) -> None:
```

**Purpose**

Protects the `wrong geometry kind is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `logical`, `geometry`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='geometry')` and executes: Calls `_run([_inspected(logical, _source_frame(logical, [geometry]))])` for its validation or side effect.

**Action**

- Calls `LineString`, `Point`, `_inspected`, `_run`, `_source_frame`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='geometry'): _run([_inspected(logical, _source_frame(logical, [geometry]))])`.

**Regression protected**

- Protects the exact `wrong geometry kind is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `Point`, `_inspected`, `_run`, `_source_frame`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_surface_geometry_is_rejected_without_repair`

**Signature**

```python
def test_invalid_surface_geometry_is_rejected_without_repair() -> None:
```

**Purpose**

Protects the `invalid surface geometry is rejected without repair` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `bowtie` from `Polygon([(0, 0), (2, 2), (2, 0), (0, 2), (0, 0)])`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='valid')` and executes: Calls `_run([_inspected('information_surface', _source_frame('information_surface', [bowtie]))])` for its validation or side effect.

**Action**

- Calls `Polygon`, `_inspected`, `_run`, `_source_frame`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='valid'): _run([_inspected('information_surface', _source_frame('information_surface', [bowtie]))])`.

**Regression protected**

- Protects the exact `invalid surface geometry is rejected without repair` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `_inspected`, `_run`, `_source_frame`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_null_or_empty_source_geometry_is_rejected`

**Signature**

```python
def test_null_or_empty_source_geometry_is_rejected(geometry: object) -> None:
```

**Purpose**

Protects the `null or empty source geometry is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry`.
- Contains 4 explicit setup/context statement(s).
- Computes `frame` from `_source_frame('information_surface', [_rectangle(0, 0, 1, 1)])`.
- Computes `frame.geometry` from `[geometry]`.
- Computes `layer` from `_inspected('information_surface', frame)`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='geometry')` and executes: Calls `_run([layer])` for its validation or side effect.

**Action**

- Calls `Polygon`, `_inspected`, `_rectangle`, `_run`, `_source_frame`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='geometry'): _run([layer])`.

**Regression protected**

- Protects the exact `null or empty source geometry is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `_inspected`, `_rectangle`, `_run`, `_source_frame`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_crs_is_rejected`

**Signature**

```python
def test_missing_crs_is_rejected(target: str) -> None:
```

**Purpose**

Protects the `missing crs is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `target`.
- Contains 3 explicit setup/context statement(s).
- Computes `parcel` from `_parcels(crs=None) if target == 'parcel' else _parcels()`.
- Computes `frame` from `_source_frame('prescription_line', [LineString([(0, 5), (10, 5)])], crs=None if target == 'source' else 'EPSG:2154')`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='CRS|physical revalidation')` and executes: Calls `_run([_inspected('prescription_line', frame)], parcel)` for its validation or side effect.

**Action**

- Calls `LineString`, `_inspected`, `_parcels`, `_run`, `_source_frame`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='CRS|physical revalidation'): _run([_inspected('prescription_line', frame)], parcel)`.

**Regression protected**

- Protects the exact `missing crs is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `_inspected`, `_parcels`, `_run`, `_source_frame`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unusable_source_crs_is_rejected`

**Signature**

```python
def test_unusable_source_crs_is_rejected() -> None:
```

**Purpose**

Protects the `unusable source crs is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `frame` from `_source_frame('prescription_line', [LineString([(0, 5), (10, 5)])]).set_crs(LOCAL_ENGINEERING_CRS, allow_override=True)`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='CRS')` and executes: Calls `_run([_inspected('prescription_line', frame)])` for its validation or side effect.

**Action**

- Calls `LineString`, `_inspected`, `_run`, `_source_frame`, `_source_frame('prescription_line', [LineString([(0, 5), (10, 5)])]).set_crs`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='CRS'): _run([_inspected('prescription_line', frame)])`.

**Regression protected**

- Protects the exact `unusable source crs is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `_inspected`, `_run`, `_source_frame`, `_source_frame('prescription_line', [LineString([(0, 5), (10, 5)])]).set_crs`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_mutated_source_summary_is_rejected`

**Signature**

```python
def test_mutated_source_summary_is_rejected(field: str, value: object) -> None:
```

**Purpose**

Protects the `mutated source summary is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `field`, `value`.
- Contains 6 explicit setup/context statement(s).
- Computes `layer` from `_inspected('prescription_line', _source_frame('prescription_line', [LineString([(0, 5), (10, 5)])]))`.
- Computes `planning_document` from `_planning_document([layer])`.
- Computes `stored` from `planning_document.related_layers[0]`.
- Computes `corrupted` from `replace(stored, summary=replace(stored.summary, **{field: value}))`.
- Computes `changed` from `replace(planning_document, related_layers=(corrupted,))`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='summary|physical revalidation')` and executes: Calls `intersect_parcels_with_gpu_planning_features(_parcels(), changed)` for its validation or side effect.

**Action**

- Calls `LineString`, `_inspected`, `_parcels`, `_planning_document`, `_source_frame`, `intersect_parcels_with_gpu_planning_features`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='summary|physical revalidation'): intersect_parcels_with_gpu_planning_features(_parcels(), changed)`.

**Regression protected**

- Protects the exact `mutated source summary is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `_inspected`, `_parcels`, `_planning_document`, `_source_frame`, `intersect_parcels_with_gpu_planning_features`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_summary_counts_are_strict_integers`

**Signature**

```python
def test_source_summary_counts_are_strict_integers(bad_count: object) -> None:
```

**Purpose**

Protects the `source summary counts are strict integers` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `bad_count`.
- Contains 6 explicit setup/context statement(s).
- Computes `layer` from `_inspected('prescription_line', _source_frame('prescription_line', [LineString([(0, 5), (10, 5)])]))`.
- Computes `planning_document` from `_planning_document([layer])`.
- Computes `stored` from `planning_document.related_layers[0]`.
- Computes `corrupted` from `replace(stored, summary=replace(stored.summary, feature_count=bad_count))`.
- Computes `changed` from `replace(planning_document, related_layers=(corrupted,))`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='integer count|non-negative|summary|physical revalidation')` and executes: Calls `intersect_parcels_with_gpu_planning_features(_parcels(), changed)` for its validation or side effect.

**Action**

- Calls `LineString`, `_inspected`, `_parcels`, `_planning_document`, `_source_frame`, `float`, `intersect_parcels_with_gpu_planning_features`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='integer count|non-negative|summary|physical revalidation'): intersect_parcels_with_gpu_planning_features(_parcels(), changed)`.

**Regression protected**

- Protects the exact `source summary counts are strict integers` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `_inspected`, `_parcels`, `_planning_document`, `_source_frame`, `float`, `intersect_parcels_with_gpu_planning_features`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_reserved_output_column_collision_is_rejected`

**Signature**

```python
def test_reserved_output_column_collision_is_rejected() -> None:
```

**Purpose**

Protects the `reserved output column collision is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `parcels` from `_parcels()`.
- Computes `parcels['planning_surface_relation_count']` from `99`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='output columns')` and executes: Calls `_run([], parcels)` for its validation or side effect.

**Action**

- Calls `_parcels`, `_run`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='output columns'): _run([], parcels)`.

**Regression protected**

- Protects the exact `reserved output column collision is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_parcels`, `_run`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_inputs_and_all_existing_parcel_fields_are_preserved`

**Signature**

```python
def test_inputs_and_all_existing_parcel_fields_are_preserved() -> None:
```

**Purpose**

Protects the `inputs and all existing parcel fields are preserved` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 6 explicit setup/context statement(s).
- Computes `parcels` from `_parcels([_rectangle(0, 0, 10, 10), _rectangle(20, 20, 30, 30)])`.
- Computes `frame` from `_source_frame('prescription_surface', [_rectangle(0, 0, 5, 10)], ids=['PSC'])`.
- Computes `planning` from `_planning_document([_inspected('prescription_surface', frame)])`.
- Computes `parcels_before` from `parcels.copy(deep=True)`.
- Computes `zoning_before` from `planning.related_layers[0].data.copy(deep=True)`.
- Computes `result` from `intersect_parcels_with_gpu_planning_features(parcels, planning)`.

**Action**

- Calls `_inspected`, `_parcels`, `_planning_document`, `_rectangle`, `_source_frame`, `intersect_parcels_with_gpu_planning_features`, `np.array_equal`, `parcels.copy`, `parcels.geometry.to_wkb`, `parcels['parcel_id'].tolist`, `planning.related_layers[0].data.copy`, `result.parcels.geometry.to_wkb`, `result.parcels.index.equals`, `result.parcels['existing_zoning_fact'].equals`, `result.parcels['parcel_id'].tolist`.

**Expected result**

- Direct assertions: `assert result.parcels['parcel_id'].tolist() == parcels['parcel_id'].tolist()`; `assert result.parcels.index.equals(parcels.index)`; `assert result.parcels['existing_zoning_fact'].equals(parcels['existing_zoning_fact'])`; `assert np.array_equal(result.parcels.geometry.to_wkb(), parcels.geometry.to_wkb())`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `inputs and all existing parcel fields are preserved` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inspected`, `_parcels`, `_planning_document`, `_rectangle`, `_source_frame`, `assert_geodataframe_equal`, `intersect_parcels_with_gpu_planning_features`, `np.array_equal`, `parcels.copy`, `parcels.geometry.to_wkb`, `parcels['parcel_id'].tolist`, `planning.related_layers[0].data.copy`, `result.parcels.geometry.to_wkb`, `result.parcels.index.equals`, `result.parcels['existing_zoning_fact'].equals`, `result.parcels['parcel_id'].tolist`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_relations_are_unique_deterministic_and_summaries_agree`

**Signature**

```python
def test_relations_are_unique_deterministic_and_summaries_agree() -> None:
```

**Purpose**

Protects the `relations are unique deterministic and summaries agree` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `parcels` from `_parcels([_rectangle(0, 0, 10, 10), _rectangle(20, 20, 30, 30)], ids=['P-B', 'P-A'])`.
- Computes `surface` from `_inspected('information_surface', _source_frame('information_surface', [_rectangle(-1, -1, 31, 31)], ids=['I']))`.
- Computes `line` from `_inspected('prescription_line', _source_frame('prescription_line', [LineString([(-1, 5), (11, 5)])], ids=['L']))`.
- Computes `result` from `_run([surface, line], parcels)`.
- Computes `first` from `result.parcels.iloc[0]`.

**Action**

- Calls `((result.relations['parcel_id'] == 'P-B') & (result.relations['geometry_kind'] == 'SURFACE')).sum`, `LineString`, `_inspected`, `_parcels`, `_rectangle`, `_run`, `_source_frame`, `int`, `result.relations.duplicated`, `result.relations.duplicated(['parcel_id', 'planning_feature_id']).any`, `result.relations.loc[(result.relations['parcel_id'] == 'P-B') & (result.relations['geometry_kind'] == 'LINE'), 'intersection_length_m'].sum`, `result.relations['parcel_id'].tolist`.

**Expected result**

- Direct assertions: `assert not result.relations.duplicated(['parcel_id', 'planning_feature_id']).any()`; `assert result.relations['parcel_id'].tolist() == ['P-B', 'P-B', 'P-A']`; `assert first['planning_surface_relation_count'] == int(((result.relations['parcel_id'] == 'P-B') & (result.relations['geometry_kind'] == 'SURFACE')).sum())`; `assert first['planning_line_intersection_length_sum_m'] == pytest.approx(result.relations.loc[(result.relations['parcel_id'] == 'P-B') & (result.relations['geometry_kind'] == 'LINE'), 'intersection_length_m'].sum())`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `relations are unique deterministic and summaries agree` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `((result.relations['parcel_id'] == 'P-B') & (result.relations['geometry_kind'] == 'SURFACE')).sum`, `LineString`, `_inspected`, `_parcels`, `_rectangle`, `_run`, `_source_frame`, `int`, `pytest.approx`, `result.relations.duplicated`, `result.relations.duplicated(['parcel_id', 'planning_feature_id']).any`, `result.relations.loc[(result.relations['parcel_id'] == 'P-B') & (result.relations['geometry_kind'] == 'LINE'), 'intersection_length_m'].sum`, `result.relations['parcel_id'].tolist`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_result_frames_are_independent_from_mutable_inputs`

**Signature**

```python
def test_result_frames_are_independent_from_mutable_inputs() -> None:
```

**Purpose**

Protects the `result frames are independent from mutable inputs` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 6 explicit setup/context statement(s).
- Computes `parcels` from `_parcels()`.
- Computes `layer` from `_inspected('prescription_line', _source_frame('prescription_line', [LineString([(0, 5), (10, 5)])]))`.
- Computes `result` from `_run([layer], parcels)`.
- Computes `snapshot` from `deepcopy(result.relations)`.
- Computes `parcels.loc[50, 'existing_zoning_fact']` from `-1`.
- Computes `layer.data.loc[0, 'LIBELLE']` from `'mutated'`.

**Action**

- Calls `LineString`, `_inspected`, `_parcels`, `_run`, `_source_frame`, `deepcopy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `result frames are independent from mutable inputs` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `_inspected`, `_parcels`, `_run`, `_source_frame`, `assert_frame_equal`, `deepcopy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_present_empty_optional_layer_is_valid`

**Signature**

```python
def test_present_empty_optional_layer_is_valid(
    logical: str,
    catalog_name: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `present empty optional layer is valid` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `logical`, `catalog_name`, `monkeypatch`.
- Contains 4 explicit setup/context statement(s).
- Computes `frame` from `_source_frame(logical, [])`.
- Computes `fid_reads` from `0`.
- Computes `result` from `_run([_inspected(logical, frame)])`.
- Computes `catalog` from `getattr(result, catalog_name)`.

**Action**

- Calls `_inspected`, `_run`, `_source_frame`, `catalog.crs.to_epsg`, `frame.drop`, `getattr`, `kwargs.get`, `monkeypatch.setattr`, `real_read_dataframe`.

**Expected result**

- Direct assertions: `assert catalog.empty`; `assert catalog.crs.to_epsg() == 2154`; `assert result.relations.empty`; `assert len(result.parcels) == 1`; `assert result.parcels.iloc[0]['planning_feature_document_id'] == DOCUMENT_ID`; `assert fid_reads == 1`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `present empty optional layer is valid` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inspected`, `_run`, `_source_frame`, `catalog.crs.to_epsg`, `frame.drop`, `getattr`, `kwargs.get`, `len`, `monkeypatch.setattr`, `pytest.mark.parametrize`, `real_read_dataframe`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_normalized_input_contract_validates_step_7d_3_1_result`

**Signature**

```python
def test_public_normalized_input_contract_validates_step_7d_3_1_result() -> None:
```

**Purpose**

Protects the `public normalized input contract validates step 7d 3 1 result` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `validation` from `validate_normalized_planning_feature_inputs(planning_document, parcels, result.surface_features, result.line_features, result.point_features, result.relations)`.

**Action**

- Calls `_source_complete_contract`, `int`, `isinstance`, `validate_normalized_planning_feature_inputs`.

**Expected result**

- Direct assertions: `assert isinstance(validation, PlanningFeatureInputValidation)`; `assert validation.related_source_layer_count == 3`; `assert validation.related_source_file_count == 3`; `assert validation.expected_relation_count == len(result.relations)`; `assert len(value) == 64`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `public normalized input contract validates step 7d 3 1 result` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `int`, `isinstance`, `len`, `validate_normalized_planning_feature_inputs`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_normalized_input_contract_wraps_malformed_document_context`

**Signature**

```python
def test_public_normalized_input_contract_wraps_malformed_document_context() -> None:
```

**Purpose**

Protects the `public normalized input contract wraps malformed document context` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `malformed` from `replace(planning_document, related_layers=(None,))`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError)` and executes: Calls `_validate_source_complete(malformed, parcels, result)` for its validation or side effect.

**Action**

- Calls `_source_complete_contract`, `_validate_source_complete`, `isinstance`, `replace`.

**Expected result**

- Direct assertions: `assert isinstance(caught.value.__cause__, (AttributeError, TypeError))`.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError) as caught: _validate_source_complete(malformed, parcels, result)`.

**Regression protected**

- Protects the exact `public normalized input contract wraps malformed document context` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `_validate_source_complete`, `isinstance`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_binds_inspected_spatial_inventory`

**Signature**

```python
def test_source_complete_contract_binds_inspected_spatial_inventory() -> None:
```

**Purpose**

Protects the `source complete contract binds inspected spatial inventory` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `missing_inventory` from `replace(planning_document, all_spatial_layers=())`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='inventory|reference')` and executes: Calls `_validate_source_complete(missing_inventory, parcels, result)` for its validation or side effect.

**Action**

- Calls `_source_complete_contract`, `_validate_source_complete`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='inventory|reference'): _validate_source_complete(missing_inventory, parcels, result)`.

**Regression protected**

- Protects the exact `source complete contract binds inspected spatial inventory` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `_validate_source_complete`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_normalized_input_contract_is_exported`

**Signature**

```python
def test_public_normalized_input_contract_is_exported() -> None:
```

**Purpose**

Protects the `public normalized input contract is exported` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls only local assertions/expressions.

**Expected result**

- Direct assertions: `assert stages.validate_normalized_planning_feature_inputs is validate_normalized_planning_feature_inputs`; `assert 'validate_normalized_planning_feature_inputs' in stages.__all__`; `assert stages.PlanningFeatureInputValidation is PlanningFeatureInputValidation`; `assert 'PlanningFeatureInputValidation' in stages.__all__`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `public normalized input contract is exported` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- No calls.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_source_validation_hashes_survive_parquet_readback`

**Signature**

```python
def test_public_source_validation_hashes_survive_parquet_readback(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `public source validation hashes survive parquet readback` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 4 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `original` from `_validate_source_complete(planning_document, parcels, result)`.
- Computes `paths` from `{'surface_features': tmp_path / 'surface.parquet', 'line_features': tmp_path / 'line.parquet', 'point_features': tmp_path / 'point.parquet', 'relations': tmp_path / 'relations.parquet'}`.
- Computes `validation` from `validate_normalized_planning_feature_inputs(planning_document, parcels, gpd.read_parquet(paths['surface_features']), gpd.read_parquet(paths['line_features']), gpd.read_parquet(paths['point_features']), pd.read_parquet(paths['relations']))`.

**Action**

- Calls `_source_complete_contract`, `_validate_source_complete`, `gpd.read_parquet`, `pd.read_parquet`, `result.line_features.to_parquet`, `result.point_features.to_parquet`, `result.relations.to_parquet`, `result.surface_features.to_parquet`, `validate_normalized_planning_feature_inputs`.

**Expected result**

- Direct assertions: `assert validation == original`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `public source validation hashes survive parquet readback` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `_validate_source_complete`, `gpd.read_parquet`, `pd.read_parquet`, `result.line_features.to_parquet`, `result.point_features.to_parquet`, `result.relations.to_parquet`, `result.surface_features.to_parquet`, `validate_normalized_planning_feature_inputs`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_normalized_input_contract_rejects_stripped_catalog`

**Signature**

```python
def test_public_normalized_input_contract_rejects_stripped_catalog() -> None:
```

**Purpose**

Protects the `public normalized input contract rejects stripped catalog` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `surface` from `result.surface_features.drop(columns='label_raw')`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='schema|label_raw')` and executes: Calls `validate_normalized_planning_feature_inputs(planning_document, parcels, surface, result.line_features, result.point_features, result.relations)` for its validation or side effect.

**Action**

- Calls `_source_complete_contract`, `result.surface_features.drop`, `validate_normalized_planning_feature_inputs`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='schema|label_raw'): validate_normalized_planning_feature_inputs(planning_document, parcels, surface, result.line_features, result.point_features, result.relations)`.

**Regression protected**

- Protects the exact `public normalized input contract rejects stripped catalog` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `pytest.raises`, `result.surface_features.drop`, `validate_normalized_planning_feature_inputs`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_empty_and_nonempty_catalogs_have_identical_kind_schemas`

**Signature**

```python
def test_empty_and_nonempty_catalogs_have_identical_kind_schemas() -> None:
```

**Purpose**

Protects the `empty and nonempty catalogs have identical kind schemas` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `(_, _, populated)` from `_contract_result()`.
- Computes `empty` from `_run([])`.

**Action**

- Calls `_contract_result`, `_run`, `zip`.

**Expected result**

- Direct assertions: `assert list(empty_catalog.columns) == list(populated_catalog.columns)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `empty and nonempty catalogs have identical kind schemas` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_contract_result`, `_run`, `list`, `zip`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_strict_relation_integer_counts_are_enforced`

**Signature**

```python
def test_strict_relation_integer_counts_are_enforced(bad_count: object) -> None:
```

**Purpose**

Protects the `strict relation integer counts are enforced` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `bad_count`.
- Contains 6 explicit setup/context statement(s).
- Computes `(planning_document, source, result)` from `_contract_result()`.
- Computes `relations` from `result.relations.copy(deep=True)`.
- Computes `relations['point_member_count']` from `relations['point_member_count'].astype(object)`.
- Computes `point_index` from `relations.index[relations['geometry_kind'] == 'POINT'][0]`.
- Computes `relations.loc[point_index, 'point_member_count']` from `bad_count`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='integer count|non-negative|dtype|schema')` and executes: Calls `_validate_result(source, replace(result, relations=relations), planning_document=planning_document)` for its validation or side effect.

**Action**

- Calls `_contract_result`, `_validate_result`, `float`, `relations['point_member_count'].astype`, `replace`, `result.relations.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='integer count|non-negative|dtype|schema'): _validate_result(source, replace(result, relations=relations), planning_document=planning_document)`.

**Regression protected**

- Protects the exact `strict relation integer counts are enforced` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_contract_result`, `_validate_result`, `float`, `pytest.mark.parametrize`, `pytest.raises`, `relations['point_member_count'].astype`, `replace`, `result.relations.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_strict_parcel_summary_integer_counts_are_enforced`

**Signature**

```python
def test_strict_parcel_summary_integer_counts_are_enforced(
    bad_count: object,
) -> None:
```

**Purpose**

Protects the `strict parcel summary integer counts are enforced` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `bad_count`.
- Contains 5 explicit setup/context statement(s).
- Computes `(planning_document, source, result)` from `_contract_result()`.
- Computes `parcels` from `result.parcels.copy(deep=True)`.
- Computes `parcels['planning_line_relation_count']` from `parcels['planning_line_relation_count'].astype(object)`.
- Computes `parcels.loc[parcels.index[0], 'planning_line_relation_count']` from `bad_count`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='integer count|non-negative')` and executes: Calls `_validate_result(source, replace(result, parcels=parcels), planning_document=planning_document)` for its validation or side effect.

**Action**

- Calls `_contract_result`, `_validate_result`, `float`, `parcels['planning_line_relation_count'].astype`, `replace`, `result.parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='integer count|non-negative'): _validate_result(source, replace(result, parcels=parcels), planning_document=planning_document)`.

**Regression protected**

- Protects the exact `strict parcel summary integer counts are enforced` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_contract_result`, `_validate_result`, `float`, `parcels['planning_line_relation_count'].astype`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `result.parcels.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_corrupted_relation_semantics_are_rejected`

**Signature**

```python
def test_corrupted_relation_semantics_are_rejected(
    kind: str,
    column: str,
    value: object,
) -> None:
```

**Purpose**

Protects the `corrupted relation semantics are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `kind`, `column`, `value`.
- Contains 6 explicit setup/context statement(s).
- Computes `(planning_document, source, result)` from `_contract_result()`.
- Computes `relations` from `result.relations.copy(deep=True)`.
- Computes `index` from `relations.index[relations['geometry_kind'] == kind][0]`.
- Computes `relations[column]` from `relations[column].astype(object)`.
- Computes `relations.loc[index, column]` from `value`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError)` and executes: Calls `_validate_result(source, replace(result, relations=relations), planning_document=planning_document)` for its validation or side effect.

**Action**

- Calls `_contract_result`, `_validate_result`, `relations[column].astype`, `replace`, `result.relations.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError): _validate_result(source, replace(result, relations=relations), planning_document=planning_document)`.

**Regression protected**

- Protects the exact `corrupted relation semantics are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_contract_result`, `_validate_result`, `pytest.mark.parametrize`, `pytest.raises`, `relations[column].astype`, `replace`, `result.relations.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_point_member_relation_semantics_are_exact`

**Signature**

```python
def test_point_member_relation_semantics_are_exact() -> None:
```

**Purpose**

Protects the `point member relation semantics are exact` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 6 explicit setup/context statement(s).
- Computes `(planning_document, source, result)` from `_contract_result()`.
- Computes `relations` from `result.relations.copy(deep=True)`.
- Computes `index` from `relations.index[relations['geometry_kind'] == 'POINT'][0]`.
- Computes `relations.loc[index, 'point_members_inside_count']` from `0`.
- Computes `relations.loc[index, 'point_members_boundary_count']` from `1`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='relation type')` and executes: Calls `_validate_result(source, replace(result, relations=relations), planning_document=planning_document)` for its validation or side effect.

**Action**

- Calls `_contract_result`, `_validate_result`, `replace`, `result.relations.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='relation type'): _validate_result(source, replace(result, relations=relations), planning_document=planning_document)`.

**Regression protected**

- Protects the exact `point member relation semantics are exact` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_contract_result`, `_validate_result`, `pytest.raises`, `replace`, `result.relations.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_shared_intrinsic_relation_semantics_reject_every_invalid_case`

**Signature**

```python
def test_shared_intrinsic_relation_semantics_reject_every_invalid_case(
    case: str,
) -> None:
```

**Purpose**

Protects the `shared intrinsic relation semantics reject every invalid case` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `case`.
- Contains 6 explicit setup/context statement(s).
- Computes `(_, _, result)` from `_contract_result()`.
- Computes `relations` from `result.relations.copy(deep=True)`.
- Computes `surface` from `relations.index[relations['geometry_kind'].eq('SURFACE')][0]`.
- Computes `line` from `relations.index[relations['geometry_kind'].eq('LINE')][0]`.
- Computes `point` from `relations.index[relations['geometry_kind'].eq('POINT')][0]`.
- Enters managed context(s) `pytest.raises((TypeError, ValueError))` and executes: Calls `validate_intrinsic_planning_feature_relations(relations)` for its validation or side effect.

**Action**

- Calls `_contract_result`, `float`, `relations['geometry_kind'].eq`, `result.relations.copy`, `validate_intrinsic_planning_feature_relations`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises((TypeError, ValueError)): validate_intrinsic_planning_feature_relations(relations)`.

**Regression protected**

- Protects the exact `shared intrinsic relation semantics reject every invalid case` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_contract_result`, `float`, `pytest.mark.parametrize`, `pytest.raises`, `relations['geometry_kind'].eq`, `result.relations.copy`, `validate_intrinsic_planning_feature_relations`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_relation_must_match_feature_catalog`

**Signature**

```python
def test_relation_must_match_feature_catalog(
    column: str,
    value: object,
) -> None:
```

**Purpose**

Protects the `relation must match feature catalog` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`, `value`.
- Contains 5 explicit setup/context statement(s).
- Computes `(planning_document, source, result)` from `_contract_result()`.
- Computes `relations` from `result.relations.copy(deep=True)`.
- Computes `index` from `relations.index[0]`.
- Computes `relations.loc[index, column]` from `value`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='catalog|geometry kind|LINE relation|unrelated metric')` and executes: Calls `_validate_result(source, replace(result, relations=relations), planning_document=planning_document)` for its validation or side effect.

**Action**

- Calls `_contract_result`, `_validate_result`, `relations['geometry_kind'].eq`, `replace`, `result.relations.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='catalog|geometry kind|LINE relation|unrelated metric'): _validate_result(source, replace(result, relations=relations), planning_document=planning_document)`.

**Regression protected**

- Protects the exact `relation must match feature catalog` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_contract_result`, `_validate_result`, `pytest.mark.parametrize`, `pytest.raises`, `relations['geometry_kind'].eq`, `replace`, `result.relations.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_feature_ids_are_globally_unique_across_catalogs`

**Signature**

```python
def test_feature_ids_are_globally_unique_across_catalogs() -> None:
```

**Purpose**

Protects the `feature ids are globally unique across catalogs` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `(planning_document, source, result)` from `_contract_result()`.
- Computes `points` from `result.point_features.copy(deep=True)`.
- Computes `points.loc[points.index[0], 'planning_feature_id']` from `result.surface_features.iloc[0]['planning_feature_id']`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='globally unique|deterministic')` and executes: Calls `_validate_result(source, replace(result, point_features=points), planning_document=planning_document)` for its validation or side effect.

**Action**

- Calls `_contract_result`, `_validate_result`, `replace`, `result.point_features.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='globally unique|deterministic'): _validate_result(source, replace(result, point_features=points), planning_document=planning_document)`.

**Regression protected**

- Protects the exact `feature ids are globally unique across catalogs` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_contract_result`, `_validate_result`, `pytest.raises`, `replace`, `result.point_features.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_same_source_id_is_allowed_in_distinct_logical_layers`

**Signature**

```python
def test_same_source_id_is_allowed_in_distinct_logical_layers() -> None:
```

**Purpose**

Protects the `same source id is allowed in distinct logical layers` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `result` from `_run([_inspected('prescription_line', _source_frame('prescription_line', [LineString([(0, 2), (10, 2)])], ids=['SHARED'])), _inspected('prescription_point', _source_frame('prescription_point', [Point(5, 5)], ids=['SHARED']))])`.

**Action**

- Calls `LineString`, `Point`, `_inspected`, `_run`, `_source_frame`, `result.relations['planning_feature_id'].nunique`.

**Expected result**

- Direct assertions: `assert len(result.relations) == 2`; `assert result.relations['planning_feature_id'].nunique() == 2`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `same source id is allowed in distinct logical layers` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `Point`, `_inspected`, `_run`, `_source_frame`, `len`, `result.relations['planning_feature_id'].nunique`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_corrupted_parcel_summary_is_rejected`

**Signature**

```python
def test_corrupted_parcel_summary_is_rejected() -> None:
```

**Purpose**

Protects the `corrupted parcel summary is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `(planning_document, source, result)` from `_contract_result()`.
- Computes `parcels` from `result.parcels.copy(deep=True)`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='inconsistent with relations')` and executes: Calls `_validate_result(source, replace(result, parcels=parcels), planning_document=planning_document)` for its validation or side effect.

**Action**

- Calls `_contract_result`, `_validate_result`, `replace`, `result.parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='inconsistent with relations'): _validate_result(source, replace(result, parcels=parcels), planning_document=planning_document)`.

**Regression protected**

- Protects the exact `corrupted parcel summary is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_contract_result`, `_validate_result`, `pytest.raises`, `replace`, `result.parcels.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_corrupted_surface_union_contract_is_rejected`

**Signature**

```python
def test_corrupted_surface_union_contract_is_rejected() -> None:
```

**Purpose**

Protects the `corrupted surface union contract is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `(planning_document, source, result)` from `_contract_result()`.
- Computes `parcels` from `result.parcels.copy(deep=True)`.
- Computes `parcels.loc[parcels.index[0], 'planning_surface_covered_union_area_m2']` from `1000.0`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='union')` and executes: Calls `_validate_result(source, replace(result, parcels=parcels), planning_document=planning_document)` for its validation or side effect.

**Action**

- Calls `_contract_result`, `_validate_result`, `replace`, `result.parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='union'): _validate_result(source, replace(result, parcels=parcels), planning_document=planning_document)`.

**Regression protected**

- Protects the exact `corrupted surface union contract is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_contract_result`, `_validate_result`, `pytest.raises`, `replace`, `result.parcels.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_geospatial_operation_failure_is_controlled_and_chained`

**Signature**

```python
def test_geospatial_operation_failure_is_controlled_and_chained(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `geospatial operation failure is controlled and chained` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 2 explicit setup/context statement(s).
- Computes `layer` from `_inspected('prescription_line', _source_frame('prescription_line', [LineString([(0, 5), (10, 5)])]))`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='spatial join')` and executes: Calls `_run([layer])` for its validation or side effect.

**Action**

- Calls `LineString`, `RuntimeError`, `_inspected`, `_run`, `_source_frame`, `isinstance`, `monkeypatch.setattr`.

**Expected result**

- Direct assertions: `assert isinstance(caught.value.__cause__, RuntimeError)`.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='spatial join') as caught: _run([layer])`.

**Regression protected**

- Protects the exact `geospatial operation failure is controlled and chained` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `RuntimeError`, `_inspected`, `_run`, `_source_frame`, `isinstance`, `monkeypatch.setattr`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_unknown_relation_parcel`

**Signature**

```python
def test_source_complete_contract_rejects_unknown_relation_parcel() -> None:
```

**Purpose**

Protects the `source complete contract rejects unknown relation parcel` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `relations` from `result.relations.copy(deep=True)`.
- Computes `relations.loc[relations.index[0], 'parcel_id']` from `'NOT-A-SOURCE-PARCEL'`.
- Computes `corrupted` from `replace(result, relations=relations)`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='parcel|source')` and executes: Calls `_validate_source_complete(planning_document, parcels, corrupted)` for its validation or side effect.

**Action**

- Calls `_source_complete_contract`, `_validate_source_complete`, `replace`, `result.relations.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='parcel|source'): _validate_source_complete(planning_document, parcels, corrupted)`.

**Regression protected**

- Protects the exact `source complete contract rejects unknown relation parcel` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `_validate_source_complete`, `pytest.raises`, `replace`, `result.relations.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_coherent_parcel_metric_mutation`

**Signature**

```python
def test_source_complete_contract_rejects_coherent_parcel_metric_mutation() -> None:
```

**Purpose**

Protects the `source complete contract rejects coherent parcel metric mutation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 7 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `relations` from `result.relations.copy(deep=True)`.
- Computes `surface_mask` from `relations['geometry_kind'].eq('SURFACE')`.
- Computes `relations.loc[surface_mask, 'parcel_metric_area_m2']` from `200.0`.
- Computes `relations.loc[surface_mask, 'parcel_share_pct']` from `50.0`.
- Computes `corrupted` from `replace(result, relations=relations)`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='parcel|metric|source')` and executes: Calls `_validate_source_complete(planning_document, parcels, corrupted)` for its validation or side effect.

**Action**

- Calls `_source_complete_contract`, `_validate_source_complete`, `relations['geometry_kind'].eq`, `replace`, `result.relations.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='parcel|metric|source'): _validate_source_complete(planning_document, parcels, corrupted)`.

**Regression protected**

- Protects the exact `source complete contract rejects coherent parcel metric mutation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `_validate_source_complete`, `pytest.raises`, `relations['geometry_kind'].eq`, `replace`, `result.relations.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_same_area_wrong_parcel_relation`

**Signature**

```python
def test_source_complete_contract_rejects_same_area_wrong_parcel_relation() -> None:
```

**Purpose**

Protects the `source complete contract rejects same area wrong parcel relation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_two_parcel_source_complete_contract()`.
- Computes `relations` from `result.relations.copy(deep=True)`.
- Computes `relations.loc[relations.index[0], 'parcel_id']` from `'P-2'`.
- Computes `corrupted` from `replace(result, relations=relations)`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='relation|parcel|rebuilt|source')` and executes: Calls `_validate_source_complete(planning_document, parcels, corrupted)` for its validation or side effect.

**Action**

- Calls `_two_parcel_source_complete_contract`, `_validate_source_complete`, `replace`, `result.relations.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='relation|parcel|rebuilt|source'): _validate_source_complete(planning_document, parcels, corrupted)`.

**Regression protected**

- Protects the exact `source complete contract rejects same area wrong parcel relation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_two_parcel_source_complete_contract`, `_validate_source_complete`, `pytest.raises`, `replace`, `result.relations.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_missing_expected_relation`

**Signature**

```python
def test_source_complete_contract_rejects_missing_expected_relation() -> None:
```

**Purpose**

Protects the `source complete contract rejects missing expected relation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_two_parcel_source_complete_contract()`.
- Computes `corrupted` from `replace(result, relations=result.relations.iloc[1:].copy())`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='relation|rebuilt|source')` and executes: Calls `_validate_source_complete(planning_document, parcels, corrupted)` for its validation or side effect.

**Action**

- Calls `_two_parcel_source_complete_contract`, `_validate_source_complete`, `replace`, `result.relations.iloc[1:].copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='relation|rebuilt|source'): _validate_source_complete(planning_document, parcels, corrupted)`.

**Regression protected**

- Protects the exact `source complete contract rejects missing expected relation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_two_parcel_source_complete_contract`, `_validate_source_complete`, `pytest.raises`, `replace`, `result.relations.iloc[1:].copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_extra_geometrically_false_relation`

**Signature**

```python
def test_source_complete_contract_rejects_extra_geometrically_false_relation() -> None:
```

**Purpose**

Protects the `source complete contract rejects extra geometrically false relation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 6 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_two_parcel_source_complete_contract()`.
- Computes `extra` from `result.relations.iloc[[0]].copy(deep=True)`.
- Computes `extra.loc[extra.index[0], 'parcel_id']` from `'P-2'`.
- Computes `relations` from `pd.concat([result.relations, extra], ignore_index=True)`.
- Computes `corrupted` from `replace(result, relations=relations)`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='relation|rebuilt|source')` and executes: Calls `_validate_source_complete(planning_document, parcels, corrupted)` for its validation or side effect.

**Action**

- Calls `_two_parcel_source_complete_contract`, `_validate_source_complete`, `pd.concat`, `replace`, `result.relations.iloc[[0]].copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='relation|rebuilt|source'): _validate_source_complete(planning_document, parcels, corrupted)`.

**Regression protected**

- Protects the exact `source complete contract rejects extra geometrically false relation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_two_parcel_source_complete_contract`, `_validate_source_complete`, `pd.concat`, `pytest.raises`, `replace`, `result.relations.iloc[[0]].copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_reordered_relations`

**Signature**

```python
def test_source_complete_contract_rejects_reordered_relations() -> None:
```

**Purpose**

Protects the `source complete contract rejects reordered relations` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_two_parcel_source_complete_contract()`.
- Computes `relations` from `result.relations.iloc[::-1].reset_index(drop=True)`.
- Computes `corrupted` from `replace(result, relations=relations)`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='relation|order|rebuilt')` and executes: Calls `_validate_source_complete(planning_document, parcels, corrupted)` for its validation or side effect.

**Action**

- Calls `_two_parcel_source_complete_contract`, `_validate_source_complete`, `replace`, `result.relations.iloc[::-1].reset_index`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='relation|order|rebuilt'): _validate_source_complete(planning_document, parcels, corrupted)`.

**Regression protected**

- Protects the exact `source complete contract rejects reordered relations` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_two_parcel_source_complete_contract`, `_validate_source_complete`, `pytest.raises`, `replace`, `result.relations.iloc[::-1].reset_index`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_noncanonical_relation_dtype`

**Signature**

```python
def test_source_complete_contract_rejects_noncanonical_relation_dtype(
    column: str,
    dtype: str,
) -> None:
```

**Purpose**

Protects the `source complete contract rejects noncanonical relation dtype` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`, `dtype`.
- Contains 4 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `relations` from `result.relations.copy(deep=True)`.
- Computes `relations[column]` from `relations[column].astype(dtype)`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='schema|dtype|relation')` and executes: Calls `_validate_source_complete(planning_document, parcels, replace(result, relations=relations))` for its validation or side effect.

**Action**

- Calls `_source_complete_contract`, `_validate_source_complete`, `relations[column].astype`, `replace`, `result.relations.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='schema|dtype|relation'): _validate_source_complete(planning_document, parcels, replace(result, relations=relations))`.

**Regression protected**

- Protects the exact `source complete contract rejects noncanonical relation dtype` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `_validate_source_complete`, `pytest.mark.parametrize`, `pytest.raises`, `relations[column].astype`, `replace`, `result.relations.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_relation_index_name_change`

**Signature**

```python
def test_source_complete_contract_rejects_relation_index_name_change() -> None:
```

**Purpose**

Protects the `source complete contract rejects relation index name change` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `relations` from `result.relations.copy(deep=True)`.
- Computes `relations.index` from `relations.index.rename('changed_relation_row')`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='schema|index|relation')` and executes: Calls `_validate_source_complete(planning_document, parcels, replace(result, relations=relations))` for its validation or side effect.

**Action**

- Calls `_source_complete_contract`, `_validate_source_complete`, `relations.index.rename`, `replace`, `result.relations.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='schema|index|relation'): _validate_source_complete(planning_document, parcels, replace(result, relations=relations))`.

**Regression protected**

- Protects the exact `source complete contract rejects relation index name change` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `_validate_source_complete`, `pytest.raises`, `relations.index.rename`, `replace`, `result.relations.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_relation_index_dtype_change`

**Signature**

```python
def test_source_complete_contract_rejects_relation_index_dtype_change() -> None:
```

**Purpose**

Protects the `source complete contract rejects relation index dtype change` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `relations` from `result.relations.copy(deep=True)`.
- Computes `relations.index` from `pd.Index(np.asarray(relations.index, dtype='int32'), name=relations.index.name)`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='schema|index|relation')` and executes: Calls `_validate_source_complete(planning_document, parcels, replace(result, relations=relations))` for its validation or side effect.

**Action**

- Calls `_source_complete_contract`, `_validate_source_complete`, `np.asarray`, `pd.Index`, `replace`, `result.relations.copy`.

**Expected result**

- Direct assertions: `assert str(relations.index.dtype) == 'int32'`.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='schema|index|relation'): _validate_source_complete(planning_document, parcels, replace(result, relations=relations))`.

**Regression protected**

- Protects the exact `source complete contract rejects relation index dtype change` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `_validate_source_complete`, `np.asarray`, `pd.Index`, `pytest.raises`, `replace`, `result.relations.copy`, `str`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_relation_index_class_change`

**Signature**

```python
def test_source_complete_contract_rejects_relation_index_class_change() -> None:
```

**Purpose**

Protects the `source complete contract rejects relation index class change` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `relations` from `result.relations.copy(deep=True)`.
- Computes `relations.index` from `pd.Index(relations.index.to_numpy(), dtype='int64')`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='schema|index|relation')` and executes: Calls `validate_normalized_planning_feature_inputs(planning_document, parcels, result.surface_features, result.line_features, result.point_features, relations)` for its validation or side effect.

**Action**

- Calls `_source_complete_contract`, `pd.Index`, `relations.index.to_numpy`, `result.relations.copy`, `type`, `validate_normalized_planning_feature_inputs`.

**Expected result**

- Direct assertions: `assert type(result.relations.index) is pd.RangeIndex`; `assert type(relations.index) is pd.Index`.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='schema|index|relation'): validate_normalized_planning_feature_inputs(planning_document, parcels, result.surface_features, result.line_features, result.point_features, relations)`.

**Regression protected**

- Protects the exact `source complete contract rejects relation index class change` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `pd.Index`, `pytest.raises`, `relations.index.to_numpy`, `result.relations.copy`, `type`, `validate_normalized_planning_feature_inputs`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_expected_relation_hash_binds_dtype_and_index_metadata`

**Signature**

```python
def test_expected_relation_hash_binds_dtype_and_index_metadata() -> None:
```

**Purpose**

Protects the `expected relation hash binds dtype and index metadata` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 10 explicit setup/context statement(s).
- Computes `(_, _, result)` from `_source_complete_contract()`.
- Computes `original` from `planning_features_module._expected_relations_content_sha256(result.relations)`.
- Computes `object_dtype` from `result.relations.copy(deep=True)`.
- Computes `object_dtype['intersection_area_m2']` from `object_dtype['intersection_area_m2'].astype('object')`.
- Computes `named_index` from `result.relations.copy(deep=True)`.
- Computes `named_index.index` from `named_index.index.rename('relation_row')`.
- Computes `int32_index` from `result.relations.copy(deep=True)`.
- Computes `int32_index.index` from `pd.Index(np.asarray(int32_index.index, dtype='int32'), name=int32_index.index.name)`.
- Computes `index_class` from `result.relations.copy(deep=True)`.
- Computes `index_class.index` from `pd.Index(index_class.index.to_numpy(), dtype='int64')`.

**Action**

- Calls `_source_complete_contract`, `index_class.index.to_numpy`, `named_index.index.rename`, `np.asarray`, `object_dtype['intersection_area_m2'].astype`, `pd.Index`, `planning_features_module._expected_relations_content_sha256`, `result.relations.copy`.

**Expected result**

- Direct assertions: `assert original != planning_features_module._expected_relations_content_sha256(object_dtype)`; `assert original != planning_features_module._expected_relations_content_sha256(named_index)`; `assert original != planning_features_module._expected_relations_content_sha256(int32_index)`; `assert original != planning_features_module._expected_relations_content_sha256(index_class)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `expected relation hash binds dtype and index metadata` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `index_class.index.to_numpy`, `named_index.index.rename`, `np.asarray`, `object_dtype['intersection_area_m2'].astype`, `pd.Index`, `planning_features_module._expected_relations_content_sha256`, `result.relations.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_coherent_but_wrong_line_metric`

**Signature**

```python
def test_source_complete_contract_rejects_coherent_but_wrong_line_metric() -> None:
```

**Purpose**

Protects the `source complete contract rejects coherent but wrong line metric` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 6 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_two_parcel_source_complete_contract()`.
- Computes `relations` from `result.relations.copy(deep=True)`.
- Computes `line_mask` from `relations['geometry_kind'].eq('LINE')`.
- Computes `relations.loc[line_mask, 'intersection_length_m']` from `5.0`.
- Computes `corrupted` from `replace(result, relations=relations)`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='relation|metric|rebuilt')` and executes: Calls `_validate_source_complete(planning_document, parcels, corrupted)` for its validation or side effect.

**Action**

- Calls `_two_parcel_source_complete_contract`, `_validate_source_complete`, `relations['geometry_kind'].eq`, `replace`, `result.relations.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='relation|metric|rebuilt'): _validate_source_complete(planning_document, parcels, corrupted)`.

**Regression protected**

- Protects the exact `source complete contract rejects coherent but wrong line metric` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_two_parcel_source_complete_contract`, `_validate_source_complete`, `pytest.raises`, `relations['geometry_kind'].eq`, `replace`, `result.relations.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_accepts_complete_parcel_output_summaries`

**Signature**

```python
def test_source_complete_contract_accepts_complete_parcel_output_summaries() -> None:
```

**Purpose**

Protects the `source complete contract accepts complete parcel output summaries` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `(planning_document, _, result)` from `_source_complete_contract()`.

**Action**

- Calls `_source_complete_contract`, `_validate_source_complete`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `source complete contract accepts complete parcel output summaries` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `_validate_source_complete`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_partial_parcel_output_columns`

**Signature**

```python
def test_source_complete_contract_rejects_partial_parcel_output_columns() -> None:
```

**Purpose**

Protects the `source complete contract rejects partial parcel output columns` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `partial` from `parcels.copy(deep=True)`.
- Computes `partial['planning_surface_relation_count']` from `1`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='[Pp]arcel|output|summary|columns')` and executes: Calls `_validate_source_complete(planning_document, partial, result)` for its validation or side effect.

**Action**

- Calls `_source_complete_contract`, `_validate_source_complete`, `parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='[Pp]arcel|output|summary|columns'): _validate_source_complete(planning_document, partial, result)`.

**Regression protected**

- Protects the exact `source complete contract rejects partial parcel output columns` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `_validate_source_complete`, `parcels.copy`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_corrupted_complete_parcel_summaries`

**Signature**

```python
def test_source_complete_contract_rejects_corrupted_complete_parcel_summaries() -> None:
```

**Purpose**

Protects the `source complete contract rejects corrupted complete parcel summaries` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `(planning_document, _, result)` from `_source_complete_contract()`.
- Computes `corrupted` from `result.parcels.copy(deep=True)`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='parcel|summary|relation')` and executes: Calls `_validate_source_complete(planning_document, corrupted, result)` for its validation or side effect.

**Action**

- Calls `_source_complete_contract`, `_validate_source_complete`, `result.parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='parcel|summary|relation'): _validate_source_complete(planning_document, corrupted, result)`.

**Regression protected**

- Protects the exact `source complete contract rejects corrupted complete parcel summaries` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `_validate_source_complete`, `pytest.raises`, `result.parcels.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_noncanonical_parcel_summary_dtype`

**Signature**

```python
def test_source_complete_contract_rejects_noncanonical_parcel_summary_dtype() -> None:
```

**Purpose**

Protects the `source complete contract rejects noncanonical parcel summary dtype` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `(planning_document, _, result)` from `_source_complete_contract()`.
- Computes `corrupted` from `result.parcels.copy(deep=True)`.
- Computes `corrupted['planning_surface_covered_pct']` from `corrupted['planning_surface_covered_pct'].astype('float32')`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='parcel|schema|dtype|summary')` and executes: Calls `_validate_source_complete(planning_document, corrupted, result)` for its validation or side effect.

**Action**

- Calls `_source_complete_contract`, `_validate_source_complete`, `corrupted['planning_surface_covered_pct'].astype`, `result.parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='parcel|schema|dtype|summary'): _validate_source_complete(planning_document, corrupted, result)`.

**Regression protected**

- Protects the exact `source complete contract rejects noncanonical parcel summary dtype` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `_validate_source_complete`, `corrupted['planning_surface_covered_pct'].astype`, `pytest.raises`, `result.parcels.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_each_corrupted_parcel_summary_fact`

**Signature**

```python
def test_source_complete_contract_rejects_each_corrupted_parcel_summary_fact(
    column: str,
    value: object,
) -> None:
```

**Purpose**

Protects the `source complete contract rejects each corrupted parcel summary fact` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`, `value`.
- Contains 4 explicit setup/context statement(s).
- Computes `(planning_document, _, result)` from `_source_complete_contract()`.
- Computes `corrupted` from `result.parcels.copy(deep=True)`.
- Computes `corrupted.loc[corrupted.index[0], column]` from `value`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='parcel|summary|relation|lineage|document|archive|union|percentage')` and executes: Calls `_validate_source_complete(planning_document, corrupted, result)` for its validation or side effect.

**Action**

- Calls `_source_complete_contract`, `_validate_source_complete`, `result.parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='parcel|summary|relation|lineage|document|archive|union|percentage'): _validate_source_complete(planning_document, corrupted, result)`.

**Regression protected**

- Protects the exact `source complete contract rejects each corrupted parcel summary fact` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `_validate_source_complete`, `pytest.mark.parametrize`, `pytest.raises`, `result.parcels.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_duplicate_parcel_ids`

**Signature**

```python
def test_source_complete_contract_rejects_duplicate_parcel_ids() -> None:
```

**Purpose**

Protects the `source complete contract rejects duplicate parcel ids` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `duplicate` from `pd.concat([parcels, parcels], ignore_index=True)`.
- Computes `duplicate` from `gpd.GeoDataFrame(duplicate, geometry='geometry', crs=parcels.crs)`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='parcel_id|unique')` and executes: Calls `_validate_source_complete(planning_document, duplicate, result)` for its validation or side effect.

**Action**

- Calls `_source_complete_contract`, `_validate_source_complete`, `gpd.GeoDataFrame`, `pd.concat`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='parcel_id|unique'): _validate_source_complete(planning_document, duplicate, result)`.

**Regression protected**

- Protects the exact `source complete contract rejects duplicate parcel ids` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `_validate_source_complete`, `gpd.GeoDataFrame`, `pd.concat`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_invalid_parcel_geometry`

**Signature**

```python
def test_source_complete_contract_rejects_invalid_parcel_geometry() -> None:
```

**Purpose**

Protects the `source complete contract rejects invalid parcel geometry` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `invalid` from `parcels.copy(deep=True)`.
- Computes `invalid.at[invalid.index[0], 'geometry']` from `Polygon([(0, 0), (10, 10), (10, 0), (0, 10), (0, 0)])`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='valid|geometry')` and executes: Calls `_validate_source_complete(planning_document, invalid, result)` for its validation or side effect.

**Action**

- Calls `Polygon`, `_source_complete_contract`, `_validate_source_complete`, `parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='valid|geometry'): _validate_source_complete(planning_document, invalid, result)`.

**Regression protected**

- Protects the exact `source complete contract rejects invalid parcel geometry` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `_source_complete_contract`, `_validate_source_complete`, `parcels.copy`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_accepts_epsg4326_parcels`

**Signature**

```python
def test_source_complete_contract_accepts_epsg4326_parcels() -> None:
```

**Purpose**

Protects the `source complete contract accepts epsg4326 parcels` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `(planning_document, parcels, _)` from `_source_complete_contract()`.
- Computes `geographic` from `parcels.to_crs('EPSG:4326')`.
- Computes `result` from `intersect_parcels_with_gpu_planning_features(geographic, planning_document)`.

**Action**

- Calls `_source_complete_contract`, `_validate_source_complete`, `intersect_parcels_with_gpu_planning_features`, `parcels.to_crs`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `source complete contract accepts epsg4326 parcels` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `_validate_source_complete`, `intersect_parcels_with_gpu_planning_features`, `parcels.to_crs`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_document_reference_allows_one_archive_zip_suffix`

**Signature**

```python
def test_source_document_reference_allows_one_archive_zip_suffix() -> None:
```

**Purpose**

Protects the `source document reference allows one archive zip suffix` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `(planning_document, parcels, _)` from `_source_complete_contract()`.
- Computes `archive` from `planning_document.extraction.archive`.
- Computes `metadata` from `replace(archive.document, archive_name=f'{ARCHIVE_NAME}.zip')`.
- Computes `suffixed` from `replace(planning_document, extraction=replace(planning_document.extraction, archive=replace(archive, document=metadata)))`.
- Computes `result` from `intersect_parcels_with_gpu_planning_features(parcels, suffixed)`.

**Action**

- Calls `_source_complete_contract`, `_validate_source_complete`, `intersect_parcels_with_gpu_planning_features`, `replace`, `result.surface_features['source_archive_name'].eq`, `result.surface_features['source_archive_name'].eq(f'{ARCHIVE_NAME}.zip').all`, `result.surface_features['source_document_reference_raw'].eq`, `result.surface_features['source_document_reference_raw'].eq(ARCHIVE_NAME).all`.

**Expected result**

- Direct assertions: `assert result.surface_features['source_archive_name'].eq(f'{ARCHIVE_NAME}.zip').all()`; `assert result.surface_features['source_document_reference_raw'].eq(ARCHIVE_NAME).all()`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `source document reference allows one archive zip suffix` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `_validate_source_complete`, `intersect_parcels_with_gpu_planning_features`, `replace`, `result.surface_features['source_archive_name'].eq`, `result.surface_features['source_archive_name'].eq(f'{ARCHIVE_NAME}.zip').all`, `result.surface_features['source_document_reference_raw'].eq`, `result.surface_features['source_document_reference_raw'].eq(ARCHIVE_NAME).all`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_coherently_renamed_feature_identity`

**Signature**

```python
def test_source_complete_contract_rejects_coherently_renamed_feature_identity(
    identity_column: str,
) -> None:
```

**Purpose**

Protects the `source complete contract rejects coherently renamed feature identity` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `identity_column`.
- Contains 9 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `surface` from `result.surface_features.copy(deep=True)`.
- Computes `relations` from `result.relations.copy(deep=True)`.
- Computes `old` from `surface.iloc[0][identity_column]`.
- Computes `new` from `f'GPU:{DOCUMENT_ID}:prescription_surface:RENAMED' if identity_column == 'planning_feature_id' else 'RENAMED'`.
- Computes `surface.loc[surface.index[0], identity_column]` from `new`.
- Computes `relations.loc[relations[identity_column].eq(old), identity_column]` from `new`.
- Computes `corrupted` from `replace(result, surface_features=surface, relations=relations)`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='source|identity|rebuilt|catalog')` and executes: Calls `_validate_source_complete(planning_document, parcels, corrupted)` for its validation or side effect.

**Action**

- Calls `_source_complete_contract`, `_validate_source_complete`, `relations[identity_column].eq`, `replace`, `result.relations.copy`, `result.surface_features.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='source|identity|rebuilt|catalog'): _validate_source_complete(planning_document, parcels, corrupted)`.

**Regression protected**

- Protects the exact `source complete contract rejects coherently renamed feature identity` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `_validate_source_complete`, `pytest.mark.parametrize`, `pytest.raises`, `relations[identity_column].eq`, `replace`, `result.relations.copy`, `result.surface_features.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_independent_gpu_lineage_mutation`

**Signature**

```python
def test_source_complete_contract_rejects_independent_gpu_lineage_mutation(
    column: str,
    value: str,
) -> None:
```

**Purpose**

Protects the `source complete contract rejects independent gpu lineage mutation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`, `value`.
- Contains 6 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `surface` from `result.surface_features.copy(deep=True)`.
- Computes `relations` from `result.relations.copy(deep=True)`.
- Computes `surface.loc[surface.index[0], column]` from `value`.
- Computes `corrupted` from `replace(result, surface_features=surface, relations=relations)`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='source|lineage|catalog|rebuilt')` and executes: Calls `_validate_source_complete(planning_document, parcels, corrupted)` for its validation or side effect.

**Action**

- Calls `_source_complete_contract`, `_validate_source_complete`, `relations['planning_feature_id'].eq`, `replace`, `result.relations.copy`, `result.surface_features.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='source|lineage|catalog|rebuilt'): _validate_source_complete(planning_document, parcels, corrupted)`.

**Regression protected**

- Protects the exact `source complete contract rejects independent gpu lineage mutation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `_validate_source_complete`, `pytest.mark.parametrize`, `pytest.raises`, `relations['planning_feature_id'].eq`, `replace`, `result.relations.copy`, `result.surface_features.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_binds_gpu_document_context`

**Signature**

```python
def test_source_complete_contract_binds_gpu_document_context(
    metadata_field: str,
    value: str,
) -> None:
```

**Purpose**

Protects the `source complete contract binds gpu document context` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `metadata_field`, `value`.
- Contains 5 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `archive` from `planning_document.extraction.archive`.
- Computes `metadata` from `replace(archive.document, **{metadata_field: value})`.
- Computes `changed` from `replace(planning_document, extraction=replace(planning_document.extraction, archive=replace(archive, document=metadata)))`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='source|lineage|document|rebuilt|IDURBA|archive')` and executes: Calls `_validate_source_complete(changed, parcels, result)` for its validation or side effect.

**Action**

- Calls `_source_complete_contract`, `_validate_source_complete`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='source|lineage|document|rebuilt|IDURBA|archive'): _validate_source_complete(changed, parcels, result)`.

**Regression protected**

- Protects the exact `source complete contract binds gpu document context` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `_validate_source_complete`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_reloads_and_compares_source_catalog`

**Signature**

```python
def test_source_complete_contract_reloads_and_compares_source_catalog(
    mutation: str,
) -> None:
```

**Purpose**

Protects the `source complete contract reloads and compares source catalog` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `mutation`.
- Contains 5 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `layer` from `next((layer for layer in planning_document.related_layers if layer.logical_name == 'prescription_surface'))`.
- Computes `frame` from `layer.data.copy(deep=True)`.
- Computes `changed` from `_replace_related_layer(planning_document, 'prescription_surface', frame)`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='source|catalog|rebuilt|normalized')` and executes: Calls `_validate_source_complete(changed, parcels, result)` for its validation or side effect.

**Action**

- Calls `_rectangle`, `_replace_related_layer`, `_source_complete_contract`, `_validate_source_complete`, `frame.copy`, `frame.iloc[0:0].copy`, `gpd.GeoDataFrame`, `layer.data.copy`, `next`, `pd.concat`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='source|catalog|rebuilt|normalized'): _validate_source_complete(changed, parcels, result)`.

**Regression protected**

- Protects the exact `source complete contract reloads and compares source catalog` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_rectangle`, `_replace_related_layer`, `_source_complete_contract`, `_validate_source_complete`, `frame.copy`, `frame.iloc[0:0].copy`, `gpd.GeoDataFrame`, `layer.data.copy`, `next`, `pd.concat`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_catalog_for_absent_gpu_layer`

**Signature**

```python
def test_source_complete_contract_rejects_catalog_for_absent_gpu_layer() -> None:
```

**Purpose**

Protects the `source complete contract rejects catalog for absent gpu layer` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `changed` from `_without_related_layer(planning_document, 'prescription_surface')`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='source|layer|catalog|rebuilt')` and executes: Calls `_validate_source_complete(changed, parcels, result)` for its validation or side effect.

**Action**

- Calls `_source_complete_contract`, `_validate_source_complete`, `_without_related_layer`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='source|layer|catalog|rebuilt'): _validate_source_complete(changed, parcels, result)`.

**Regression protected**

- Protects the exact `source complete contract rejects catalog for absent gpu layer` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `_validate_source_complete`, `_without_related_layer`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_three_dimensional_normalized_catalogs_are_rejected`

**Signature**

```python
def test_three_dimensional_normalized_catalogs_are_rejected(
    catalog_name: str,
    geometry: object,
) -> None:
```

**Purpose**

Protects the `three dimensional normalized catalogs are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `catalog_name`, `geometry`.
- Contains 5 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `catalog` from `getattr(result, catalog_name).copy(deep=True)`.
- Computes `catalog.at[catalog.index[0], 'geometry']` from `geometry`.
- Computes `corrupted` from `replace(result, **{catalog_name: catalog})`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='2D|dimensional|Z')` and executes: Calls `_validate_source_complete(planning_document, parcels, corrupted)` for its validation or side effect.

**Action**

- Calls `LineString`, `Point`, `Polygon`, `_source_complete_contract`, `_validate_source_complete`, `getattr`, `getattr(result, catalog_name).copy`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='2D|dimensional|Z'): _validate_source_complete(planning_document, parcels, corrupted)`.

**Regression protected**

- Protects the exact `three dimensional normalized catalogs are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `Point`, `Polygon`, `_source_complete_contract`, `_validate_source_complete`, `getattr`, `getattr(result, catalog_name).copy`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_two_dimensional_normalized_catalogs_remain_valid`

**Signature**

```python
def test_two_dimensional_normalized_catalogs_remain_valid() -> None:
```

**Purpose**

Protects the `two dimensional normalized catalogs remain valid` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.

**Action**

- Calls `_source_complete_contract`, `_validate_source_complete`, `catalog.geometry.has_z.any`.

**Expected result**

- Direct assertions: `assert not catalog.geometry.has_z.any()`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `two dimensional normalized catalogs remain valid` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `_validate_source_complete`, `catalog.geometry.has_z.any`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_gpu_source_z_is_normalized_to_canonical_2d`

**Signature**

```python
def test_gpu_source_z_is_normalized_to_canonical_2d(
    logical: str,
    geometry: object,
    catalog_name: str,
) -> None:
```

**Purpose**

Protects the `gpu source z is normalized to canonical 2d` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `logical`, `geometry`, `catalog_name`.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_run([_inspected(logical, _source_frame(logical, [geometry]))])`.
- Computes `catalog` from `getattr(result, catalog_name)`.

**Action**

- Calls `LineString`, `Point`, `Polygon`, `_inspected`, `_run`, `_source_frame`, `catalog.geometry.has_z.any`, `getattr`.

**Expected result**

- Direct assertions: `assert not catalog.geometry.has_z.any()`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `gpu source z is normalized to canonical 2d` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `Point`, `Polygon`, `_inspected`, `_run`, `_source_frame`, `catalog.geometry.has_z.any`, `getattr`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_tampered_gpkg_inventory_hash`

**Signature**

```python
def test_source_complete_contract_rejects_tampered_gpkg_inventory_hash() -> None:
```

**Purpose**

Protects the `source complete contract rejects tampered gpkg inventory hash` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 6 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `layer` from `planning_document.related_layers[0]`.
- Computes `relative` from `layer.reference.dataset_path.relative_to(planning_document.extraction.extraction_root).as_posix()`.
- Computes `files` from `tuple((replace(item, sha256='f' * 64) if item.relative_path == relative else item for item in planning_document.extraction.files))`.
- Computes `changed` from `replace(planning_document, extraction=replace(planning_document.extraction, files=files))`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='source|file|inventory|SHA')` and executes: Calls `_validate_source_complete(changed, parcels, result)` for its validation or side effect.

**Action**

- Calls `_source_complete_contract`, `_validate_source_complete`, `layer.reference.dataset_path.relative_to`, `layer.reference.dataset_path.relative_to(planning_document.extraction.extraction_root).as_posix`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='source|file|inventory|SHA'): _validate_source_complete(changed, parcels, result)`.

**Regression protected**

- Protects the exact `source complete contract rejects tampered gpkg inventory hash` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `_validate_source_complete`, `layer.reference.dataset_path.relative_to`, `layer.reference.dataset_path.relative_to(planning_document.extraction.extraction_root).as_posix`, `pytest.raises`, `replace`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_tampered_gpkg_size`

**Signature**

```python
def test_source_complete_contract_rejects_tampered_gpkg_size() -> None:
```

**Purpose**

Protects the `source complete contract rejects tampered gpkg size` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 6 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `layer` from `planning_document.related_layers[0]`.
- Computes `relative` from `layer.reference.dataset_path.relative_to(planning_document.extraction.extraction_root).as_posix()`.
- Computes `files` from `tuple((replace(item, size_bytes=item.size_bytes + 1) if item.relative_path == relative else item for item in planning_document.extraction.files))`.
- Computes `changed` from `replace(planning_document, extraction=replace(planning_document.extraction, files=files))`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='source|file|inventory|size')` and executes: Calls `_validate_source_complete(changed, parcels, result)` for its validation or side effect.

**Action**

- Calls `_source_complete_contract`, `_validate_source_complete`, `layer.reference.dataset_path.relative_to`, `layer.reference.dataset_path.relative_to(planning_document.extraction.extraction_root).as_posix`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='source|file|inventory|size'): _validate_source_complete(changed, parcels, result)`.

**Regression protected**

- Protects the exact `source complete contract rejects tampered gpkg size` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `_validate_source_complete`, `layer.reference.dataset_path.relative_to`, `layer.reference.dataset_path.relative_to(planning_document.extraction.extraction_root).as_posix`, `pytest.raises`, `replace`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_changed_gpkg_bytes`

**Signature**

```python
def test_source_complete_contract_rejects_changed_gpkg_bytes() -> None:
```

**Purpose**

Protects the `source complete contract rejects changed gpkg bytes` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `path` from `planning_document.related_layers[0].reference.dataset_path`.
- Enters managed context(s) `path.open('ab')` and executes: Calls `stream.write(b'tamper')` for its validation or side effect.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='source|file|inventory|size|SHA')` and executes: Calls `_validate_source_complete(planning_document, parcels, result)` for its validation or side effect.

**Action**

- Calls `_source_complete_contract`, `_validate_source_complete`, `path.open`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='source|file|inventory|size|SHA'): _validate_source_complete(planning_document, parcels, result)`.

**Regression protected**

- Protects the exact `source complete contract rejects changed gpkg bytes` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `_validate_source_complete`, `path.open`, `pytest.raises`, `stream.write`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_same_size_gpkg_byte_tamper`

**Signature**

```python
def test_source_complete_contract_rejects_same_size_gpkg_byte_tamper() -> None:
```

**Purpose**

Protects the `source complete contract rejects same size gpkg byte tamper` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `path` from `planning_document.related_layers[0].reference.dataset_path`.
- Computes `payload` from `bytearray(path.read_bytes())`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='source|file|inventory|SHA')` and executes: Calls `_validate_source_complete(planning_document, parcels, result)` for its validation or side effect.

**Action**

- Calls `_source_complete_contract`, `_validate_source_complete`, `bytearray`, `path.read_bytes`, `path.write_bytes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='source|file|inventory|SHA'): _validate_source_complete(planning_document, parcels, result)`.

**Regression protected**

- Protects the exact `source complete contract rejects same size gpkg byte tamper` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `_validate_source_complete`, `bytearray`, `path.read_bytes`, `path.write_bytes`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_coherently_changed_physical_gpkg`

**Signature**

```python
def test_source_complete_contract_rejects_coherently_changed_physical_gpkg() -> None:
```

**Purpose**

Protects the `source complete contract rejects coherently changed physical gpkg` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 6 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `layer` from `planning_document.related_layers[0]`.
- Computes `changed_source` from `layer.data.copy(deep=True)`.
- Computes `changed_source.loc[changed_source.index[0], 'LIBELLE']` from `'Changed on disk'`.
- Computes `coherent_inventory` from `_refresh_extraction_inventory(planning_document)`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='source|file|loaded|changed')` and executes: Calls `_validate_source_complete(coherent_inventory, parcels, result)` for its validation or side effect.

**Action**

- Calls `_refresh_extraction_inventory`, `_source_complete_contract`, `_validate_source_complete`, `changed_source.to_file`, `layer.data.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='source|file|loaded|changed'): _validate_source_complete(coherent_inventory, parcels, result)`.

**Regression protected**

- Protects the exact `source complete contract rejects coherently changed physical gpkg` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic GeoPackage. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_refresh_extraction_inventory`, `_source_complete_contract`, `_validate_source_complete`, `changed_source.to_file`, `layer.data.copy`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_changed_physical_gpkg_geometry`

**Signature**

```python
def test_source_complete_contract_rejects_changed_physical_gpkg_geometry() -> None:
```

**Purpose**

Protects the `source complete contract rejects changed physical gpkg geometry` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 6 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `layer` from `planning_document.related_layers[0]`.
- Computes `changed_source` from `layer.data.copy(deep=True)`.
- Computes `changed_source.at[changed_source.index[0], 'geometry']` from `_rectangle(0, 0, 5, 10)`.
- Computes `coherent_inventory` from `_refresh_extraction_inventory(planning_document)`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='source|geometry|loaded|changed')` and executes: Calls `_validate_source_complete(coherent_inventory, parcels, result)` for its validation or side effect.

**Action**

- Calls `_rectangle`, `_refresh_extraction_inventory`, `_source_complete_contract`, `_validate_source_complete`, `changed_source.to_file`, `layer.data.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='source|geometry|loaded|changed'): _validate_source_complete(coherent_inventory, parcels, result)`.

**Regression protected**

- Protects the exact `source complete contract rejects changed physical gpkg geometry` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic GeoPackage. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_rectangle`, `_refresh_extraction_inventory`, `_source_complete_contract`, `_validate_source_complete`, `changed_source.to_file`, `layer.data.copy`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_reordered_physical_gpkg_rows`

**Signature**

```python
def test_source_complete_contract_rejects_reordered_physical_gpkg_rows() -> None:
```

**Purpose**

Protects the `source complete contract rejects reordered physical gpkg rows` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 7 explicit setup/context statement(s).
- Computes `parcels` from `_parcels([_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)], ids=['P-1', 'P-2'])`.
- Computes `layer` from `_inspected('prescription_surface', _source_frame('prescription_surface', [_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)], ids=['ONE', 'TWO'], type_codes=['07', '07'], subtype_codes=['04', '04']))`.
- Computes `planning_document` from `_planning_document([layer])`.
- Computes `result` from `intersect_parcels_with_gpu_planning_features(parcels, planning_document)`.
- Computes `stored` from `planning_document.related_layers[0]`.
- Computes `coherent_inventory` from `_refresh_extraction_inventory(planning_document)`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='source|order|loaded|changed')` and executes: Calls `_validate_source_complete(coherent_inventory, parcels, result)` for its validation or side effect.

**Action**

- Calls `_inspected`, `_parcels`, `_planning_document`, `_rectangle`, `_refresh_extraction_inventory`, `_source_frame`, `_validate_source_complete`, `intersect_parcels_with_gpu_planning_features`, `stored.data.iloc[::-1].reset_index`, `stored.data.iloc[::-1].reset_index(drop=True).to_file`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='source|order|loaded|changed'): _validate_source_complete(coherent_inventory, parcels, result)`.

**Regression protected**

- Protects the exact `source complete contract rejects reordered physical gpkg rows` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic GeoPackage. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inspected`, `_parcels`, `_planning_document`, `_rectangle`, `_refresh_extraction_inventory`, `_source_frame`, `_validate_source_complete`, `intersect_parcels_with_gpu_planning_features`, `pytest.raises`, `stored.data.iloc[::-1].reset_index`, `stored.data.iloc[::-1].reset_index(drop=True).to_file`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_loaded_source_attrs_not_on_disk`

**Signature**

```python
def test_source_complete_contract_rejects_loaded_source_attrs_not_on_disk() -> None:
```

**Purpose**

Protects the `source complete contract rejects loaded source attrs not on disk` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 6 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `layer` from `planning_document.related_layers[0]`.
- Computes `loaded` from `layer.data.copy(deep=True)`.
- Computes `loaded.attrs['unpersisted_source_note']` from `'tampered'`.
- Computes `changed` from `replace(planning_document, related_layers=tuple((replace(item, data=loaded) if item is layer else item for item in planning_document.related_layers)))`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='source|attrs|metadata|loaded')` and executes: Calls `_validate_source_complete(changed, parcels, result)` for its validation or side effect.

**Action**

- Calls `_source_complete_contract`, `_validate_source_complete`, `layer.data.copy`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='source|attrs|metadata|loaded'): _validate_source_complete(changed, parcels, result)`.

**Regression protected**

- Protects the exact `source complete contract rejects loaded source attrs not on disk` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `_validate_source_complete`, `layer.data.copy`, `pytest.raises`, `replace`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_dataset_outside_extraction_root`

**Signature**

```python
def test_source_complete_contract_rejects_dataset_outside_extraction_root(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `source complete contract rejects dataset outside extraction root` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 6 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `layer` from `planning_document.related_layers[0]`.
- Computes `outside` from `tmp_path / 'outside.gpkg'`.
- Computes `reference` from `replace(layer.reference, dataset_path=outside)`.
- Computes `changed` from `_replace_layer_reference(planning_document, layer.logical_name, reference)`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='source|root|outside|contain')` and executes: Calls `_validate_source_complete(changed, parcels, result)` for its validation or side effect.

**Action**

- Calls `_replace_layer_reference`, `_source_complete_contract`, `_validate_source_complete`, `replace`, `shutil.copyfile`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='source|root|outside|contain'): _validate_source_complete(changed, parcels, result)`.

**Regression protected**

- Protects the exact `source complete contract rejects dataset outside extraction root` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_replace_layer_reference`, `_source_complete_contract`, `_validate_source_complete`, `pytest.raises`, `replace`, `shutil.copyfile`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_linked_spatial_dataset`

**Signature**

```python
def test_source_complete_contract_rejects_linked_spatial_dataset(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `source complete contract rejects linked spatial dataset` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 4 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_source_complete_contract()`.
- Computes `dataset` from `planning_document.related_layers[0].reference.dataset_path`.
- Computes `actual_link_check` from `gpu_source_module._is_link_or_junction`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='source|link|junction|dataset')` and executes: Calls `_validate_source_complete(planning_document, parcels, result)` for its validation or side effect.

**Action**

- Calls `_source_complete_contract`, `_validate_source_complete`, `actual_link_check`, `monkeypatch.setattr`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='source|link|junction|dataset'): _validate_source_complete(planning_document, parcels, result)`.

**Regression protected**

- Protects the exact `source complete contract rejects linked spatial dataset` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `_validate_source_complete`, `actual_link_check`, `monkeypatch.setattr`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_binds_every_shapefile_sidecar`

**Signature**

```python
def test_source_complete_contract_binds_every_shapefile_sidecar(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `source complete contract binds every shapefile sidecar` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 5 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_shapefile_source_complete_contract(tmp_path)`.
- Computes `sidecar` from `next((item for item in planning_document.extraction.files if item.relative_path.casefold().endswith('.prj')))`.
- Computes `files` from `tuple((item for item in planning_document.extraction.files if item.relative_path != sidecar.relative_path))`.
- Computes `changed` from `replace(planning_document, extraction=replace(planning_document.extraction, files=files))`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='shapefile|sidecar|inventory|physical revalidation')` and executes: Calls `_validate_source_complete(changed, parcels, result)` for its validation or side effect.

**Action**

- Calls `_shapefile_source_complete_contract`, `_validate_source_complete`, `item.relative_path.casefold`, `item.relative_path.casefold().endswith`, `next`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='shapefile|sidecar|inventory|physical revalidation'): _validate_source_complete(changed, parcels, result)`.

**Regression protected**

- Protects the exact `source complete contract binds every shapefile sidecar` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_shapefile_source_complete_contract`, `_validate_source_complete`, `item.relative_path.casefold`, `item.relative_path.casefold().endswith`, `next`, `pytest.raises`, `replace`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_changed_or_reordered_ogr_fids`

**Signature**

```python
def test_source_complete_contract_rejects_changed_or_reordered_ogr_fids(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    changed_fids: tuple[int, int],
) -> None:
```

**Purpose**

Protects the `source complete contract rejects changed or reordered ogr fids` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`, `changed_fids`.
- Contains 3 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_shapefile_ogr_fid_source_complete_contract(tmp_path)`.
- Computes `actual_read` from `gpu_source_module.pyogrio.read_dataframe`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='source|FID|identity|catalog')` and executes: Calls `_validate_source_complete(planning_document, parcels, result)` for its validation or side effect.

**Action**

- Calls `_shapefile_ogr_fid_source_complete_contract`, `_validate_source_complete`, `actual_read`, `kwargs.get`, `monkeypatch.setattr`, `pd.Index`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='source|FID|identity|catalog'): _validate_source_complete(planning_document, parcels, result)`.

**Regression protected**

- Protects the exact `source complete contract rejects changed or reordered ogr fids` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_shapefile_ogr_fid_source_complete_contract`, `_validate_source_complete`, `actual_read`, `kwargs.get`, `monkeypatch.setattr`, `pd.Index`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_requires_shapefile_core_members`

**Signature**

```python
def test_source_complete_contract_requires_shapefile_core_members(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `source complete contract requires shapefile core members` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 3 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_shapefile_source_complete_contract(tmp_path)`.
- Computes `layer` from `planning_document.related_layers[0]`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='shapefile|shx|source|file')` and executes: Calls `_validate_source_complete(planning_document, parcels, result)` for its validation or side effect.

**Action**

- Calls `_shapefile_source_complete_contract`, `_validate_source_complete`, `layer.reference.dataset_path.with_suffix`, `layer.reference.dataset_path.with_suffix('.shx').unlink`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='shapefile|shx|source|file'): _validate_source_complete(planning_document, parcels, result)`.

**Regression protected**

- Protects the exact `source complete contract requires shapefile core members` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_shapefile_source_complete_contract`, `_validate_source_complete`, `layer.reference.dataset_path.with_suffix`, `layer.reference.dataset_path.with_suffix('.shx').unlink`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_contract_rejects_changed_shapefile_sidecar_bytes`

**Signature**

```python
def test_source_complete_contract_rejects_changed_shapefile_sidecar_bytes(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `source complete contract rejects changed shapefile sidecar bytes` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 4 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_shapefile_source_complete_contract(tmp_path)`.
- Computes `layer` from `planning_document.related_layers[0]`.
- Computes `cpg` from `layer.reference.dataset_path.with_suffix('.cpg')`.
- Enters managed context(s) `pytest.raises(PlanningFeaturesError, match='shapefile|sidecar|size|SHA|physical revalidation')` and executes: Calls `_validate_source_complete(planning_document, parcels, result)` for its validation or side effect.

**Action**

- Calls `_shapefile_source_complete_contract`, `_validate_source_complete`, `cpg.write_text`, `layer.reference.dataset_path.with_suffix`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeaturesError, match='shapefile|sidecar|size|SHA|physical revalidation'): _validate_source_complete(planning_document, parcels, result)`.

**Regression protected**

- Protects the exact `source complete contract rejects changed shapefile sidecar bytes` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_shapefile_source_complete_contract`, `_validate_source_complete`, `cpg.write_text`, `layer.reference.dataset_path.with_suffix`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_shapefile_family_excludes_dotted_sibling_dataset`

**Signature**

```python
def test_shapefile_family_excludes_dotted_sibling_dataset(tmp_path: Path) -> None:
```

**Purpose**

Protects the `shapefile family excludes dotted sibling dataset` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 6 explicit setup/context statement(s).
- Computes `(planning_document, parcels, result)` from `_shapefile_source_complete_contract(tmp_path)`.
- Computes `before` from `_validate_source_complete(planning_document, parcels, result)`.
- Computes `primary` from `planning_document.related_layers[0].reference.dataset_path`.
- Computes `sibling` from `primary.with_name(f'{primary.stem}.archive.shp')`.
- Computes `refreshed` from `_refresh_extraction_inventory(planning_document)`.
- Computes `after` from `_validate_source_complete(refreshed, parcels, result)`.

**Action**

- Calls `_rectangle`, `_refresh_extraction_inventory`, `_shapefile_source_complete_contract`, `_validate_source_complete`, `gpd.GeoDataFrame`, `gpd.GeoDataFrame({'sibling': [1]}, geometry=[_rectangle(20, 20, 21, 21)], crs='EPSG:2154').to_file`, `primary.with_name`.

**Expected result**

- Direct assertions: `assert after.related_source_file_count == before.related_source_file_count`; `assert after.gpu_related_source_files_sha256 == before.gpu_related_source_files_sha256`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `shapefile family excludes dotted sibling dataset` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; actual in-memory geometry; synthetic GeoPackage. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_rectangle`, `_refresh_extraction_inventory`, `_shapefile_source_complete_contract`, `_validate_source_complete`, `gpd.GeoDataFrame`, `gpd.GeoDataFrame({'sibling': [1]}, geometry=[_rectangle(20, 20, 21, 21)], crs='EPSG:2154').to_file`, `primary.with_name`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_batch_gpu_revalidation_rejects_malformed_layer_items`

**Signature**

```python
def test_batch_gpu_revalidation_rejects_malformed_layer_items(
    bad_item: object,
) -> None:
```

**Purpose**

Protects the `batch gpu revalidation rejects malformed layer items` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `bad_item`.
- Contains 2 explicit setup/context statement(s).
- Computes `(planning_document, _, _)` from `_source_complete_contract()`.
- Enters managed context(s) `pytest.raises(gpu_source_module.GpuSpatialInspectionError)` and executes: Calls `gpu_source_module.revalidate_gpu_spatial_layer_sources(planning_document, (bad_item,))` for its validation or side effect.

**Action**

- Calls `_source_complete_contract`, `gpu_source_module.revalidate_gpu_spatial_layer_sources`, `object`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(gpu_source_module.GpuSpatialInspectionError): gpu_source_module.revalidate_gpu_spatial_layer_sources(planning_document, (bad_item,))`.

**Regression protected**

- Protects the exact `batch gpu revalidation rejects malformed layer items` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `gpu_source_module.revalidate_gpu_spatial_layer_sources`, `object`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_batch_gpu_revalidation_rejects_malformed_planning_document`

**Signature**

```python
def test_batch_gpu_revalidation_rejects_malformed_planning_document() -> None:
```

**Purpose**

Protects the `batch gpu revalidation rejects malformed planning document` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(gpu_source_module.GpuSpatialInspectionError)` and executes: Calls `gpu_source_module.revalidate_gpu_spatial_layer_sources(object(), ())` for its validation or side effect.

**Action**

- Calls `gpu_source_module.revalidate_gpu_spatial_layer_sources`, `object`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(gpu_source_module.GpuSpatialInspectionError): gpu_source_module.revalidate_gpu_spatial_layer_sources(object(), ())`.

**Regression protected**

- Protects the exact `batch gpu revalidation rejects malformed planning document` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `gpu_source_module.revalidate_gpu_spatial_layer_sources`, `object`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_batch_gpu_revalidation_rejects_duplicate_logical_name`

**Signature**

```python
def test_batch_gpu_revalidation_rejects_duplicate_logical_name() -> None:
```

**Purpose**

Protects the `batch gpu revalidation rejects duplicate logical name` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `(planning_document, _, _)` from `_source_complete_contract()`.
- Computes `layer` from `planning_document.related_layers[0]`.
- Enters managed context(s) `pytest.raises(gpu_source_module.GpuSpatialInspectionError, match='duplicate')` and executes: Calls `gpu_source_module.revalidate_gpu_spatial_layer_sources(planning_document, (layer, layer))` for its validation or side effect.

**Action**

- Calls `_source_complete_contract`, `gpu_source_module.revalidate_gpu_spatial_layer_sources`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(gpu_source_module.GpuSpatialInspectionError, match='duplicate'): gpu_source_module.revalidate_gpu_spatial_layer_sources(planning_document, (layer, layer))`.

**Regression protected**

- Protects the exact `batch gpu revalidation rejects duplicate logical name` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_complete_contract`, `gpu_source_module.revalidate_gpu_spatial_layer_sources`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_common_planning_contracts_import_without_initializing_stages`

**Signature**

```python
def test_common_planning_contracts_import_without_initializing_stages(
    statement: str,
) -> None:
```

**Purpose**

Protects the `common planning contracts import without initializing stages` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `statement`.
- Contains 1 explicit setup/context statement(s).
- Computes `completed` from `subprocess.run([sys.executable, '-c', f"import sys; {statement}; assert 'landscout.stages' not in sys.modules"], cwd=Path(__file__).resolve().parents[2], capture_output=True, check=False, text=True)`.

**Action**

- Calls `Path`, `Path(__file__).resolve`, `subprocess.run`.

**Expected result**

- Direct assertions: `assert completed.returncode == 0, completed.stderr`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `common planning contracts import without initializing stages` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Path`, `Path(__file__).resolve`, `pytest.mark.parametrize`, `subprocess.run`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `BOUNDARY` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `CROSS` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `IN` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `LIBELLE` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `LIB_IDPSC` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `MULTI` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `PART` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `TOUCH` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `columns` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `existing_zoning_fact` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `feature_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `feature_family` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `feature_share_pct` | Logical dtype: float64. Nullability: determined by the owning schema/dtype map and explicit null guards. | percentage derived from the exact numerator/denominator named by its stage. Consumers and exact calculations are the functions that reference this column above. |
| `geometry` | Logical dtype: GeoPandas active geometry dtype. Nullability: nullable only where the source-stage geometry-status contract explicitly preserves nulls. | source or preserved spatial geometry; never itself a suitability or legal conclusion. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_kind` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `information_surface_covered_union_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `information_surface_relation_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `intersection_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `intersection_length_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `label_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `line_features` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_metric_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_share_pct` | Logical dtype: float64. Nullability: determined by the owning schema/dtype map and explicit null guards. | percentage derived from the exact numerator/denominator named by its stage. Consumers and exact calculations are the functions that reference this column above. |
| `planning_feature_document_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `planning_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `planning_line_intersection_length_sum_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `planning_line_relation_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `planning_line_touch_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `planning_point_boundary_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `planning_point_inside_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `planning_point_relation_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `planning_surface_area_overlap_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `planning_surface_covered_pct` | Logical dtype: float64. Nullability: determined by the owning schema/dtype map and explicit null guards. | percentage derived from the exact numerator/denominator named by its stage. Consumers and exact calculations are the functions that reference this column above. |
| `planning_surface_covered_union_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `planning_surface_intersection_area_sum_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `planning_surface_relation_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `planning_surface_touch_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `point_features` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `point_member_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `point_members_boundary_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `point_members_inside_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `prescription_surface_covered_union_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `prescription_surface_relation_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `relation_type` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `relations` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `sibling` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_archive_name` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `source_crs` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_document_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_document_reference_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `source_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_identity_field` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_identity_kind` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `source_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_line_length_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `subtype_code_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `surface_features` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `text_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `type_code_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `unpersisted_source_note` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `zone` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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

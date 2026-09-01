# `tests/unit/test_enrich_planning_features.py`

## File identity

- Repository path: `tests/unit/test_enrich_planning_features.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Provides complete unit and regression coverage for the `enrich_planning_features` contracts exercised in this file.
- Source SHA256: `f742a30c7921e83fd28114c7419ba0d4c2ca36aa0aed5d04c8881cad1feaef57`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for enrich planning features; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Provides complete unit and regression coverage for the `enrich_planning_features` contracts exercised in this file.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import json`
- `import shutil`
- `import subprocess`
- `import sys`
- `import tempfile`
- `from copy import deepcopy`
- `from dataclasses import FrozenInstanceError, replace`
- `from hashlib import sha256`
- `from pathlib import Path`

### Third-party packages

- `import geopandas as gpd`
- `import numpy as np`
- `import pandas as pd`
- `import pytest`
- `from geopandas.testing import assert_geodataframe_equal`
- `from pandas.testing import assert_frame_equal`
- `from shapely.geometry import (
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
)`

### Internal LandScout imports

- `from landscout import stages`
- `from landscout.common.planning_feature_contract import (
    validate_intrinsic_planning_feature_relations,
)`
- `from landscout.sources import gpu_fr as gpu_source_module`
- `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- `from landscout.stages import enrich_planning_features as planning_features_module`
- `from landscout.stages.enrich_planning_features import (
    ParcelPlanningFeaturesResult,
    PlanningFeatureInputValidation,
    PlanningFeaturesError,
    _validate_result,
    intersect_parcels_with_gpu_planning_features,
    validate_normalized_planning_feature_inputs,
)`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `DOCUMENT_ID`

- Category: module constant or closed domain.
- Exact declaration:

```python
DOCUMENT_ID = "doc-1"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `ARCHIVE_NAME`

- Category: module constant or closed domain.
- Exact declaration:

```python
ARCHIVE_NAME = "31395_PLU_20240215"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `ARCHIVE_SHA`

- Category: module constant or closed domain.
- Exact declaration:

```python
ARCHIVE_SHA = "a" * 64
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `STANDARD`

- Category: module constant or closed domain.
- Exact declaration:

```python
STANDARD = "CNIG PLU v2017"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `LOCAL_ENGINEERING_CRS`

- Category: module constant or closed domain.
- Exact declaration:

```python
LOCAL_ENGINEERING_CRS = (
    'ENGCRS["Local",EDATUM["Unknown"],CS[Cartesian,2],'
    'AXIS["x",east,LENGTHUNIT["metre",1]],'
    'AXIS["y",north,LENGTHUNIT["metre",1]]]'
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

No top-level class/model/dataclass is declared.

## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_rectangle`

**Purpose:** Implements `rectangle` within the file role: Provides complete unit and regression coverage for the `enrich_planning_features` contracts exercised in this file.

**Exact signature**

```python
def _rectangle(x1: float, y1: float, x2: float, y2: float) -> Polygon:
```

- Exact decorators: none.
- Declared return annotation: `Polygon`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `x1` | positional-or-keyword | `float` | `required` |
| `y1` | positional-or-keyword | `float` | `required` |
| `x2` | positional-or-keyword | `float` | `required` |
| `y2` | positional-or-keyword | `float` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `Polygon([(x1, y1), (x1, y2), (x2, y2), (x2, y1), (x1, y1)])`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_planning_features::_parcels` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_features::_parcels` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_features::_planning_document` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_features::_planning_document` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_features::test_surface_full_overlap_normalizes_raw_values_and_lineage` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_features::test_surface_full_overlap_normalizes_raw_values_and_lineage` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_features::test_surface_partial_and_touch_relations` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_features::test_surface_partial_and_touch_relations` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_features::test_overlapping_surface_union_is_not_double_counted` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_features::test_overlapping_surface_union_is_not_double_counted` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_features::test_polygon_and_multipolygon_surfaces` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_features::test_polygon_and_multipolygon_surfaces` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_features::test_epsg4326_parcels_are_measured_in_lambert93_but_preserved` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_features::test_epsg4326_parcels_are_measured_in_lambert93_but_preserved` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_features::test_duplicate_parcel_ids_are_rejected` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_features::test_duplicate_parcel_ids_are_rejected` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_features::test_duplicate_source_ids_are_rejected` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_features::test_duplicate_source_ids_are_rejected` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_features::test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_features::test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_features::test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_features::test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_features::test_null_or_empty_source_geometry_is_rejected` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_features::test_null_or_empty_source_geometry_is_rejected` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_features::test_inputs_and_all_existing_parcel_fields_are_preserved` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_features::test_inputs_and_all_existing_parcel_fields_are_preserved` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_features::test_relations_are_unique_deterministic_and_summaries_agree` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_features::test_relations_are_unique_deterministic_and_summaries_agree` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_features::_contract_result` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_features::_contract_result` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_features::_source_complete_contract` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_features::_source_complete_contract` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_features::_two_parcel_source_complete_contract` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_features::_two_parcel_source_complete_contract` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_reloads_and_compares_source_catalog` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_reloads_and_compares_source_catalog` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_changed_physical_gpkg_geometry` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_changed_physical_gpkg_geometry` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_reordered_physical_gpkg_rows` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_reordered_physical_gpkg_rows` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_features::_shapefile_source_complete_contract` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_features::_shapefile_source_complete_contract` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_features::_shapefile_ogr_fid_source_complete_contract` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_features::_shapefile_ogr_fid_source_complete_contract` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_features::test_dotted_sibling_dataset_is_not_a_sidecar_and_makes_role_ambiguous` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_features::test_dotted_sibling_dataset_is_not_a_sidecar_and_makes_role_ambiguous` via `_rectangle`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |

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
def _rectangle(x1: float, y1: float, x2: float, y2: float) -> Polygon:
    return Polygon([(x1, y1), (x1, y2), (x2, y2), (x2, y1), (x1, y1)])
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_parcels`

**Purpose:** Implements `parcels` within the file role: Provides complete unit and regression coverage for the `enrich_planning_features` contracts exercised in this file.

**Exact signature**

```python
def _parcels(
    geometries: list[object] | None = None,
    *,
    ids: list[object] | None = None,
    crs: str | None = "EPSG:2154",
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometries` | positional-or-keyword | `list[object] \| None` | `None` |
| `ids` | keyword-only | `list[object] \| None` | `None` |
| `crs` | keyword-only | `str \| None` | `'EPSG:2154'` |

**Return and exception contract**

- Exact observed return expressions:
  - `frame.set_crs(None, allow_override=True)`
  - `frame if crs == "EPSG:2154" else frame.to_crs(crs)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_planning_features::_run` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_features::_run` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_features::test_epsg4326_parcels_are_measured_in_lambert93_but_preserved` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_features::test_epsg4326_parcels_are_measured_in_lambert93_but_preserved` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_features::test_invalid_parcel_ids_are_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_features::test_invalid_parcel_ids_are_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_features::test_duplicate_parcel_ids_are_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_features::test_duplicate_parcel_ids_are_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_features::test_missing_crs_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_features::test_missing_crs_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_features::test_mutated_source_summary_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_features::test_mutated_source_summary_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_features::test_source_summary_counts_are_strict_integers` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_summary_counts_are_strict_integers` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_features::test_reserved_output_column_collision_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_features::test_reserved_output_column_collision_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_features::test_inputs_and_all_existing_parcel_fields_are_preserved` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_features::test_inputs_and_all_existing_parcel_fields_are_preserved` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_features::test_relations_are_unique_deterministic_and_summaries_agree` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_features::test_relations_are_unique_deterministic_and_summaries_agree` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_features::test_result_frames_are_independent_from_mutable_inputs` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_features::test_result_frames_are_independent_from_mutable_inputs` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_features::_contract_result` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_features::_contract_result` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_features::_source_complete_contract` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_features::_source_complete_contract` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_features::_two_parcel_source_complete_contract` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_features::_two_parcel_source_complete_contract` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_reordered_physical_gpkg_rows` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_reordered_physical_gpkg_rows` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_features::_shapefile_source_complete_contract` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_features::_shapefile_source_complete_contract` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_features::_shapefile_ogr_fid_source_complete_contract` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_features::_shapefile_ogr_fid_source_complete_contract` via `_parcels`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_rectangle` | `tests.unit.test_enrich_planning_features._rectangle` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.arange` | `numpy.arange` |
| `frame.set_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.to_crs` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `frame.set_crs`<br>`frame.to_crs` |
| External process/environment | None directly present. |
| In-memory mutation | `frame.set_crs(None, allow_override=True)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _parcels(
    geometries: list[object] | None = None,
    *,
    ids: list[object] | None = None,
    crs: str | None = "EPSG:2154",
) -> gpd.GeoDataFrame:
    values = geometries or [_rectangle(0, 0, 10, 10)]
    frame = gpd.GeoDataFrame(
        {
            "parcel_id": ids or [f"P-{index + 1}" for index in range(len(values))],
            "existing_zoning_fact": np.arange(len(values), dtype="int64") + 7,
        },
        geometry=values,
        crs="EPSG:2154",
        index=[50 + index for index in range(len(values))],
    )
    if crs is None:
        return frame.set_crs(None, allow_override=True)
    return frame if crs == "EPSG:2154" else frame.to_crs(crs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_source_frame`

**Purpose:** Implements `source frame` within the file role: Provides complete unit and regression coverage for the `enrich_planning_features` contracts exercised in this file.

**Exact signature**

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

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `logical` | positional-or-keyword | `str` | `required` |
| `geometries` | positional-or-keyword | `list[object]` | `required` |
| `ids` | keyword-only | `list[object] \| None` | `None` |
| `type_codes` | keyword-only | `list[object] \| None` | `None` |
| `subtype_codes` | keyword-only | `list[object] \| None` | `None` |
| `document_refs` | keyword-only | `list[object] \| None` | `None` |
| `crs` | keyword-only | `str \| None` | `'EPSG:2154'` |

**Return and exception contract**

- Exact observed return expressions:
  - `frame.set_crs(None, allow_override=True)`
  - `frame.set_crs(crs, allow_override=True)`
  - `frame if crs == "EPSG:2154" else frame.to_crs(crs)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_planning_features::test_surface_full_overlap_normalizes_raw_values_and_lineage` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_surface_full_overlap_normalizes_raw_values_and_lineage` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_surface_partial_and_touch_relations` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_surface_partial_and_touch_relations` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_overlapping_surface_union_is_not_double_counted` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_overlapping_surface_union_is_not_double_counted` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_polygon_and_multipolygon_surfaces` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_polygon_and_multipolygon_surfaces` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_line_crossing_and_partly_inside` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_line_crossing_and_partly_inside` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_line_boundary_touch_is_zero_length` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_line_boundary_touch_is_zero_length` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_linestring_and_multilinestring` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_linestring_and_multilinestring` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_points_inside_boundary_outside_and_multipoint` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_points_inside_boundary_outside_and_multipoint` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_optional_raw_source_fields_are_not_fabricated` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_optional_raw_source_fields_are_not_fabricated` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_epsg4326_parcels_are_measured_in_lambert93_but_preserved` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_epsg4326_parcels_are_measured_in_lambert93_but_preserved` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_duplicate_source_ids_are_rejected` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_duplicate_source_ids_are_rejected` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_idurba_mismatch_is_rejected` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_idurba_mismatch_is_rejected` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_missing_required_source_fields_fail` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_missing_required_source_fields_fail` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_wrong_geometry_kind_is_rejected` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_wrong_geometry_kind_is_rejected` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_invalid_surface_geometry_is_rejected_without_repair` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_invalid_surface_geometry_is_rejected_without_repair` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_null_or_empty_source_geometry_is_rejected` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_null_or_empty_source_geometry_is_rejected` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_missing_crs_is_rejected` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_missing_crs_is_rejected` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_unusable_source_crs_is_rejected` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_unusable_source_crs_is_rejected` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_mutated_source_summary_is_rejected` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_mutated_source_summary_is_rejected` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_source_summary_counts_are_strict_integers` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_summary_counts_are_strict_integers` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_inputs_and_all_existing_parcel_fields_are_preserved` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_inputs_and_all_existing_parcel_fields_are_preserved` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_relations_are_unique_deterministic_and_summaries_agree` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_relations_are_unique_deterministic_and_summaries_agree` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_result_frames_are_independent_from_mutable_inputs` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_result_frames_are_independent_from_mutable_inputs` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_present_empty_optional_layer_is_valid` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_present_empty_optional_layer_is_valid` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::_contract_result` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::_contract_result` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::_source_complete_contract` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::_source_complete_contract` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::_two_parcel_source_complete_contract` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::_two_parcel_source_complete_contract` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_same_source_id_is_allowed_in_distinct_logical_layers` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_same_source_id_is_allowed_in_distinct_logical_layers` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_geospatial_operation_failure_is_controlled_and_chained` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_geospatial_operation_failure_is_controlled_and_chained` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_gpu_source_z_is_normalized_to_canonical_2d` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_gpu_source_z_is_normalized_to_canonical_2d` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_reordered_physical_gpkg_rows` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_reordered_physical_gpkg_rows` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::_shapefile_source_complete_contract` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::_shapefile_source_complete_contract` via `_source_frame`
- direct call: `tests.unit.test_enrich_planning_features::_shapefile_ogr_fid_source_complete_contract` via `_source_frame`
- value/type reference: `tests.unit.test_enrich_planning_features::_shapefile_ogr_fid_source_complete_contract` via `_source_frame`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `logical.startswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `frame.set_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.to_crs` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `frame.set_crs`<br>`frame.to_crs` |
| External process/environment | None directly present. |
| In-memory mutation | `frame.set_crs(None, allow_override=True)`<br>`frame.set_crs(crs, allow_override=True)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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
    count = len(geometries)
    prescription = logical.startswith("prescription")
    identity = "LIB_IDPSC" if prescription else "LIB_IDINFO"
    type_field = "TYPEPSC" if prescription else "TYPEINF"
    subtype_field = "STYPEPSC" if prescription else "STYPEINF"
    data: dict[str, object] = {
        "LIBELLE": [f"Label {index}" for index in range(count)],
        "TXT": [None if index % 2 else f"Text {index}" for index in range(count)],
        type_field: type_codes or [f"T{index}" for index in range(count)],
        subtype_field: subtype_codes or [f"S{index}" for index in range(count)],
        "NOMFIC": [
            None if index % 2 else f"rule-{index}.pdf" for index in range(count)
        ],
        "URLFIC": [None] * count,
        "IDURBA": document_refs or [ARCHIVE_NAME] * count,
        "DATVALID": ["20240215"] * count,
        identity: ids or [f"SRC-{logical}-{index}" for index in range(count)],
    }
    frame = gpd.GeoDataFrame(data, geometry=geometries, crs="EPSG:2154")
    if crs is None:
        return frame.set_crs(None, allow_override=True)
    if crs == "IGNF:LAMB93":
        return frame.set_crs(crs, allow_override=True)
    return frame if crs == "EPSG:2154" else frame.to_crs(crs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_summary`

**Purpose:** Implements `summary` within the file role: Provides complete unit and regression coverage for the `enrich_planning_features` contracts exercised in this file.

**Exact signature**

```python
def _summary(
    frame: gpd.GeoDataFrame,
    source_layer: str,
    *,
    document_id: str = DOCUMENT_ID,
    archive_sha: str = ARCHIVE_SHA,
) -> GpuLayerSummary:
```

- Exact decorators: none.
- Declared return annotation: `GpuLayerSummary`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `source_layer` | positional-or-keyword | `str` | `required` |
| `document_id` | keyword-only | `str` | `DOCUMENT_ID` |
| `archive_sha` | keyword-only | `str` | `ARCHIVE_SHA` |

**Return and exception contract**

- Exact observed return expressions:
  - `GpuLayerSummary(<br>        source_document_id=document_id,<br>        source_archive_sha256=archive_sha,<br>        source_layer=source_layer,<br>        crs="UNKNOWN" if frame.crs is None else frame.crs.to_string(),<br>        feature_count=len(frame),<br>        columns=tuple(str(column) for column in frame.columns),<br>        dtypes=tuple(<br>            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()<br>        ),<br>        null_counts=tuple(<br>            (str(column), int(frame[column].isna().sum())) for column in frame.columns<br>        ),<br>        geometry_types=tuple(<br>            (str(key), int(value))<br>            for key, value in geometry.geom_type.value_counts().sort_index().items()<br>        ),<br>        null_geometry_count=int((~non_null).sum()),<br>        empty_geometry_count=int((non_null & geometry.is_empty).sum()),<br>        invalid_geometry_count=int((non_empty & ~geometry.is_valid).sum()),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_planning_features::_inspected` via `_summary`
- value/type reference: `tests.unit.test_enrich_planning_features::_inspected` via `_summary`
- direct call: `tests.unit.test_enrich_planning_features::_materialize_layer` via `_summary`
- value/type reference: `tests.unit.test_enrich_planning_features::_materialize_layer` via `_summary`
- direct call: `tests.unit.test_enrich_planning_features::_planning_document` via `_summary`
- value/type reference: `tests.unit.test_enrich_planning_features::_planning_document` via `_summary`
- direct call: `tests.unit.test_enrich_planning_features::test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent` via `_summary`
- value/type reference: `tests.unit.test_enrich_planning_features::test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent` via `_summary`
- direct call: `tests.unit.test_enrich_planning_features::_replace_related_layer` via `_summary`
- value/type reference: `tests.unit.test_enrich_planning_features::_replace_related_layer` via `_summary`
- direct call: `tests.unit.test_enrich_planning_features::_shapefile_source_complete_contract` via `_summary`
- value/type reference: `tests.unit.test_enrich_planning_features::_shapefile_source_complete_contract` via `_summary`
- direct call: `tests.unit.test_enrich_planning_features::_shapefile_ogr_fid_source_complete_contract` via `_summary`
- value/type reference: `tests.unit.test_enrich_planning_features::_shapefile_ogr_fid_source_complete_contract` via `_summary`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuLayerSummary` | `landscout.sources.gpu_fr.GpuLayerSummary` |
| `frame.crs.to_string` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.dtypes.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame[column].isna().sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame[column].isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.geom_type.value_counts().sort_index().items` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.geom_type.value_counts().sort_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.geom_type.value_counts` | `unresolved local/third-party receiver; no ownership inferred` |
| `(~non_null).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `(non_null & geometry.is_empty).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `(non_empty & ~geometry.is_valid).sum` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `geometry.isna`<br>`geometry.geom_type.value_counts().sort_index().items`<br>`geometry.geom_type.value_counts().sort_index`<br>`geometry.geom_type.value_counts`<br>`(non_null & geometry.is_empty).sum`<br>`(non_empty & ~geometry.is_valid).sum` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _summary(
    frame: gpd.GeoDataFrame,
    source_layer: str,
    *,
    document_id: str = DOCUMENT_ID,
    archive_sha: str = ARCHIVE_SHA,
) -> GpuLayerSummary:
    geometry = frame.geometry
    non_null = ~geometry.isna()
    non_empty = non_null & ~geometry.is_empty
    return GpuLayerSummary(
        source_document_id=document_id,
        source_archive_sha256=archive_sha,
        source_layer=source_layer,
        crs="UNKNOWN" if frame.crs is None else frame.crs.to_string(),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
        null_counts=tuple(
            (str(column), int(frame[column].isna().sum())) for column in frame.columns
        ),
        geometry_types=tuple(
            (str(key), int(value))
            for key, value in geometry.geom_type.value_counts().sort_index().items()
        ),
        null_geometry_count=int((~non_null).sum()),
        empty_geometry_count=int((non_null & geometry.is_empty).sum()),
        invalid_geometry_count=int((non_empty & ~geometry.is_valid).sum()),
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_inspected`

**Purpose:** Implements `inspected` within the file role: Provides complete unit and regression coverage for the `enrich_planning_features` contracts exercised in this file.

**Exact signature**

```python
def _inspected(logical: str, frame: gpd.GeoDataFrame) -> GpuInspectedLayer:
```

- Exact decorators: none.
- Declared return annotation: `GpuInspectedLayer`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `logical` | positional-or-keyword | `str` | `required` |
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `GpuInspectedLayer(<br>        logical_name=logical,  # type: ignore[arg-type]<br>        reference=reference,<br>        data=frame,<br>        summary=_summary(frame, source_layer),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_planning_features::test_surface_full_overlap_normalizes_raw_values_and_lineage` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_surface_full_overlap_normalizes_raw_values_and_lineage` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_surface_partial_and_touch_relations` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_surface_partial_and_touch_relations` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_overlapping_surface_union_is_not_double_counted` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_overlapping_surface_union_is_not_double_counted` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_polygon_and_multipolygon_surfaces` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_polygon_and_multipolygon_surfaces` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_line_crossing_and_partly_inside` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_line_crossing_and_partly_inside` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_line_boundary_touch_is_zero_length` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_line_boundary_touch_is_zero_length` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_linestring_and_multilinestring` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_linestring_and_multilinestring` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_points_inside_boundary_outside_and_multipoint` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_points_inside_boundary_outside_and_multipoint` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_optional_raw_source_fields_are_not_fabricated` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_optional_raw_source_fields_are_not_fabricated` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_epsg4326_parcels_are_measured_in_lambert93_but_preserved` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_epsg4326_parcels_are_measured_in_lambert93_but_preserved` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_duplicate_source_ids_are_rejected` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_duplicate_source_ids_are_rejected` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_idurba_mismatch_is_rejected` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_idurba_mismatch_is_rejected` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_missing_required_source_fields_fail` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_missing_required_source_fields_fail` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_wrong_geometry_kind_is_rejected` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_wrong_geometry_kind_is_rejected` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_invalid_surface_geometry_is_rejected_without_repair` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_invalid_surface_geometry_is_rejected_without_repair` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_null_or_empty_source_geometry_is_rejected` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_null_or_empty_source_geometry_is_rejected` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_missing_crs_is_rejected` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_missing_crs_is_rejected` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_unusable_source_crs_is_rejected` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_unusable_source_crs_is_rejected` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_mutated_source_summary_is_rejected` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_mutated_source_summary_is_rejected` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_source_summary_counts_are_strict_integers` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_summary_counts_are_strict_integers` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_inputs_and_all_existing_parcel_fields_are_preserved` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_inputs_and_all_existing_parcel_fields_are_preserved` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_relations_are_unique_deterministic_and_summaries_agree` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_relations_are_unique_deterministic_and_summaries_agree` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_result_frames_are_independent_from_mutable_inputs` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_result_frames_are_independent_from_mutable_inputs` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_present_empty_optional_layer_is_valid` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_present_empty_optional_layer_is_valid` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::_contract_result` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::_contract_result` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::_source_complete_contract` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::_source_complete_contract` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::_two_parcel_source_complete_contract` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::_two_parcel_source_complete_contract` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_same_source_id_is_allowed_in_distinct_logical_layers` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_same_source_id_is_allowed_in_distinct_logical_layers` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_geospatial_operation_failure_is_controlled_and_chained` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_geospatial_operation_failure_is_controlled_and_chained` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_gpu_source_z_is_normalized_to_canonical_2d` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_gpu_source_z_is_normalized_to_canonical_2d` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_reordered_physical_gpkg_rows` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_reordered_physical_gpkg_rows` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::_shapefile_source_complete_contract` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::_shapefile_source_complete_contract` via `_inspected`
- direct call: `tests.unit.test_enrich_planning_features::_shapefile_ogr_fid_source_complete_contract` via `_inspected`
- value/type reference: `tests.unit.test_enrich_planning_features::_shapefile_ogr_fid_source_complete_contract` via `_inspected`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `logical.upper` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuSpatialLayerReference` | `landscout.sources.gpu_fr.GpuSpatialLayerReference` |
| `Path` | `pathlib.Path` |
| `GpuInspectedLayer` | `landscout.sources.gpu_fr.GpuInspectedLayer` |
| `_summary` | `tests.unit.test_enrich_planning_features._summary` |

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
def _inspected(logical: str, frame: gpd.GeoDataFrame) -> GpuInspectedLayer:
    source_layer = f"SOURCE_{logical.upper()}"
    reference = GpuSpatialLayerReference(
        dataset_path=Path(f"synthetic-{logical}.gpkg"),
        source_layer=source_layer,
        driver="GPKG",
    )
    return GpuInspectedLayer(
        logical_name=logical,  # type: ignore[arg-type]
        reference=reference,
        data=frame,
        summary=_summary(frame, source_layer),
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_physical_inventory`

**Purpose:** Implements `physical inventory` within the file role: Provides complete unit and regression coverage for the `enrich_planning_features` contracts exercised in this file.

**Exact signature**

```python
def _physical_inventory(root: Path) -> tuple[GpuExtractedFile, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[GpuExtractedFile, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `root` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `tuple(records)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_planning_features::_planning_document` via `_physical_inventory`
- value/type reference: `tests.unit.test_enrich_planning_features::_planning_document` via `_physical_inventory`
- direct call: `tests.unit.test_enrich_planning_features::_refresh_extraction_inventory` via `_physical_inventory`
- value/type reference: `tests.unit.test_enrich_planning_features::_refresh_extraction_inventory` via `_physical_inventory`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `root.rglob` | `unresolved local/third-party receiver; no ownership inferred` |
| `item.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.suffix.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `records.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuExtractedFile` | `landscout.sources.gpu_fr.GpuExtractedFile` |
| `path.relative_to(root).as_posix` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.relative_to` | `unresolved local/third-party receiver; no ownership inferred` |
| `suffix.lstrip` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(path.read_bytes()).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `item.is_file`<br>`path.stat`<br>`sha256(path.read_bytes()).hexdigest`<br>`path.read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(path.read_bytes()).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `records.append(<br>            GpuExtractedFile(<br>                relative_path=path.relative_to(root).as_posix(),<br>                file_type=suffix.lstrip(".") or "none",<br>                size_bytes=path.stat().st_size,<br>                sha256=sha256(path.read_bytes()).hexdigest(),<br>                category="SPATIAL_DATA",<br>            )<br>        )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _physical_inventory(root: Path) -> tuple[GpuExtractedFile, ...]:
    records: list[GpuExtractedFile] = []
    for path in sorted((item for item in root.rglob("*") if item.is_file()), key=str):
        if path.parent == root and path.name == EXTRACTION_MANIFEST_NAME:
            continue
        suffix = path.suffix.casefold()
        records.append(
            GpuExtractedFile(
                relative_path=path.relative_to(root).as_posix(),
                file_type=suffix.lstrip(".") or "none",
                size_bytes=path.stat().st_size,
                sha256=sha256(path.read_bytes()).hexdigest(),
                category="SPATIAL_DATA",
            )
        )
    return tuple(records)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_write_extraction_manifest`

**Purpose:** Implements `write extraction manifest` within the file role: Provides complete unit and regression coverage for the `enrich_planning_features` contracts exercised in this file.

**Exact signature**

```python
def _write_extraction_manifest(
    root: Path,
    archive_sha256: str,
    files: tuple[GpuExtractedFile, ...],
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `root` | positional-or-keyword | `Path` | `required` |
| `archive_sha256` | positional-or-keyword | `str` | `required` |
| `files` | positional-or-keyword | `tuple[GpuExtractedFile, ...]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_planning_features::_planning_document` via `_write_extraction_manifest`
- value/type reference: `tests.unit.test_enrich_planning_features::_planning_document` via `_write_extraction_manifest`
- direct call: `tests.unit.test_enrich_planning_features::_refresh_extraction_inventory` via `_write_extraction_manifest`
- value/type reference: `tests.unit.test_enrich_planning_features::_refresh_extraction_inventory` via `_write_extraction_manifest`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `(root / EXTRACTION_MANIFEST_NAME).write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `(root / EXTRACTION_MANIFEST_NAME).write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _write_extraction_manifest(
    root: Path,
    archive_sha256: str,
    files: tuple[GpuExtractedFile, ...],
) -> None:
    payload = {
        "schema_version": 2,
        "archive_sha256": archive_sha256,
        "files": [
            {
                "relative_path": item.relative_path,
                "size_bytes": item.size_bytes,
                "sha256": item.sha256,
            }
            for item in files
        ],
    }
    (root / EXTRACTION_MANIFEST_NAME).write_text(
        json.dumps(payload, sort_keys=True, separators=(",", ":")),
        encoding="utf-8",
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_materialize_layer`

**Purpose:** Implements `materialize layer` within the file role: Provides complete unit and regression coverage for the `enrich_planning_features` contracts exercised in this file.

**Exact signature**

```python
def _materialize_layer(root: Path, layer: GpuInspectedLayer) -> GpuInspectedLayer:
```

- Exact decorators: none.
- Declared return annotation: `GpuInspectedLayer`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `root` | positional-or-keyword | `Path` | `required` |
| `layer` | positional-or-keyword | `GpuInspectedLayer` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `replace(<br>        layer,<br>        reference=replace(reference, dataset_path=path),<br>        data=reread,<br>        summary=_summary(reread, reference.source_layer),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_planning_features::_planning_document` via `_materialize_layer`
- value/type reference: `tests.unit.test_enrich_planning_features::_planning_document` via `_materialize_layer`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `reference.dataset_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `reference.dataset_path.resolve` | `unresolved local/third-party receiver; no ownership inferred` |
| `layer.data.to_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `gpd.read_file` | `geopandas.read_file` |
| `_summary` | `tests.unit.test_enrich_planning_features._summary` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `reference.dataset_path.is_file`<br>`gpd.read_file` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _materialize_layer(root: Path, layer: GpuInspectedLayer) -> GpuInspectedLayer:
    reference = layer.reference
    if reference.dataset_path.is_file():
        path = reference.dataset_path.resolve()
    else:
        path = root / f"{layer.logical_name}.gpkg"
        layer.data.to_file(
            path,
            layer=reference.source_layer,
            driver="GPKG",
            engine="pyogrio",
            index=False,
        )
        reference = replace(reference, dataset_path=path, driver="GPKG")
    reread = gpd.read_file(
        path,
        layer=reference.source_layer if reference.driver == "GPKG" else None,
        engine="pyogrio",
    )
    return replace(
        layer,
        reference=replace(reference, dataset_path=path),
        data=reread,
        summary=_summary(reread, reference.source_layer),
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_planning_document`

**Purpose:** Implements `planning document` within the file role: Provides complete unit and regression coverage for the `enrich_planning_features` contracts exercised in this file.

**Exact signature**

```python
def _planning_document(
    layers: list[GpuInspectedLayer] | None = None,
) -> GpuPlanningDocument:
```

- Exact decorators: none.
- Declared return annotation: `GpuPlanningDocument`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `layers` | positional-or-keyword | `list[GpuInspectedLayer] \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `GpuPlanningDocument(<br>        source_config=source_config,<br>        source_config_sha256=gpu_source_module._source_config_sha256(source_config),<br>        extraction=extraction,<br>        all_spatial_layers=gpu_source_module.discover_gpu_spatial_layers(extraction),<br>        zoning=zoning,<br>        related_layers=related,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_planning_features::_run` via `_planning_document`
- value/type reference: `tests.unit.test_enrich_planning_features::_run` via `_planning_document`
- direct call: `tests.unit.test_enrich_planning_features::test_mutated_source_summary_is_rejected` via `_planning_document`
- value/type reference: `tests.unit.test_enrich_planning_features::test_mutated_source_summary_is_rejected` via `_planning_document`
- direct call: `tests.unit.test_enrich_planning_features::test_source_summary_counts_are_strict_integers` via `_planning_document`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_summary_counts_are_strict_integers` via `_planning_document`
- direct call: `tests.unit.test_enrich_planning_features::test_inputs_and_all_existing_parcel_fields_are_preserved` via `_planning_document`
- value/type reference: `tests.unit.test_enrich_planning_features::test_inputs_and_all_existing_parcel_fields_are_preserved` via `_planning_document`
- direct call: `tests.unit.test_enrich_planning_features::_contract_result` via `_planning_document`
- value/type reference: `tests.unit.test_enrich_planning_features::_contract_result` via `_planning_document`
- direct call: `tests.unit.test_enrich_planning_features::_source_complete_contract` via `_planning_document`
- value/type reference: `tests.unit.test_enrich_planning_features::_source_complete_contract` via `_planning_document`
- direct call: `tests.unit.test_enrich_planning_features::_two_parcel_source_complete_contract` via `_planning_document`
- value/type reference: `tests.unit.test_enrich_planning_features::_two_parcel_source_complete_contract` via `_planning_document`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_reordered_physical_gpkg_rows` via `_planning_document`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_reordered_physical_gpkg_rows` via `_planning_document`
- direct call: `tests.unit.test_enrich_planning_features::_shapefile_source_complete_contract` via `_planning_document`
- value/type reference: `tests.unit.test_enrich_planning_features::_shapefile_source_complete_contract` via `_planning_document`
- direct call: `tests.unit.test_enrich_planning_features::_shapefile_ogr_fid_source_complete_contract` via `_planning_document`
- value/type reference: `tests.unit.test_enrich_planning_features::_shapefile_ogr_fid_source_complete_contract` via `_planning_document`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `layer.reference.dataset_path.resolve` | `unresolved local/third-party receiver; no ownership inferred` |
| `layer.reference.dataset_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path` | `pathlib.Path` |
| `tempfile.mkdtemp` | `tempfile.mkdtemp` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `_materialize_layer` | `tests.unit.test_enrich_planning_features._materialize_layer` |
| `GpuDocumentMetadata` | `landscout.sources.gpu_fr.GpuDocumentMetadata` |
| `GpuArchiveDownload` | `landscout.sources.gpu_fr.GpuArchiveDownload` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `_rectangle` | `tests.unit.test_enrich_planning_features._rectangle` |
| `zoning_frame.to_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.read_file` | `geopandas.read_file` |
| `GpuSpatialLayerReference` | `landscout.sources.gpu_fr.GpuSpatialLayerReference` |
| `GpuInspectedLayer` | `landscout.sources.gpu_fr.GpuInspectedLayer` |
| `_summary` | `tests.unit.test_enrich_planning_features._summary` |
| `_physical_inventory` | `tests.unit.test_enrich_planning_features._physical_inventory` |
| `_write_extraction_manifest` | `tests.unit.test_enrich_planning_features._write_extraction_manifest` |
| `GpuExtraction` | `landscout.sources.gpu_fr.GpuExtraction` |
| `load_gpu_source_config(<br>        Path("configs/sources/gpu_fr.yaml")<br>    ).model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `load_gpu_source_config` | `landscout.sources.gpu_fr.load_gpu_source_config` |
| `GpuSourceConfig.model_validate` | `landscout.sources.gpu_fr.GpuSourceConfig.model_validate` |
| `GpuPlanningDocument` | `landscout.sources.gpu_fr.GpuPlanningDocument` |
| `gpu_source_module._source_config_sha256` | `landscout.sources.gpu_fr._source_config_sha256` |
| `gpu_source_module.discover_gpu_spatial_layers` | `landscout.sources.gpu_fr.discover_gpu_spatial_layers` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `layer.reference.dataset_path.is_file`<br>`gpd.read_file` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `gpu_source_module._source_config_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `config_payload["spatial_layers"][role]["match_tokens"] = [f"unused_{role}"]`<br>`config_payload["spatial_layers"]["zoning"]["match_tokens"] = ["ZONING"]`<br>`config_payload["spatial_layers"][layer.logical_name]["match_tokens"] = [<br>            layer.reference.source_layer<br>        ]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _planning_document(
    layers: list[GpuInspectedLayer] | None = None,
) -> GpuPlanningDocument:
    requested_layers = list(layers or [])
    existing_paths = [
        layer.reference.dataset_path.resolve()
        for layer in requested_layers
        if layer.reference.dataset_path.is_file()
    ]
    extraction_root = (
        existing_paths[0].parent
        if existing_paths
        else Path(tempfile.mkdtemp(prefix="landscout-feature-source-"))
    )
    related = tuple(
        _materialize_layer(extraction_root, layer) for layer in requested_layers
    )
    metadata = GpuDocumentMetadata(
        provider="Géoportail de l'Urbanisme",
        portal="G\u00e9oportail de l'Urbanisme",
        commune_code="31395",
        partition="DU_31395",
        document_id=DOCUMENT_ID,
        document_family="DU",
        document_type="PLU",
        document_title="Muret PLU",
        status="document.production",
        legal_status="APPROVED",
        effective_status="EN_VIGUEUR",
        version="10",
        archive_name=ARCHIVE_NAME,
        publication_timestamp=None,
        update_timestamp=None,
        revision_date=None,
        producer=None,
        standard_model=STANDARD,
        projection="EPSG:2154",
        metadata_identifier=None,
        source_url="https://www.geoportail-urbanisme.gouv.fr/api/document/download-by-partition/DU_31395",
        written_files=(),
    )
    archive = GpuArchiveDownload(
        document=metadata,
        download_timestamp="2026-08-12T12:00:00+00:00",
        filename=f"{ARCHIVE_NAME}.zip",
        archive_format="zip",
        file_size=1,
        sha256=ARCHIVE_SHA,
        path=Path("synthetic.zip"),
        cache_hit=True,
    )
    zoning_frame = gpd.GeoDataFrame(
        {"zone": ["Z"]}, geometry=[_rectangle(-10, -10, 20, 20)], crs="EPSG:2154"
    )
    zoning_path = extraction_root / "zoning.gpkg"
    zoning_frame.to_file(
        zoning_path,
        layer="ZONING",
        driver="GPKG",
        engine="pyogrio",
        index=False,
    )
    zoning_frame = gpd.read_file(zoning_path, layer="ZONING", engine="pyogrio")
    zoning_ref = GpuSpatialLayerReference(zoning_path, "ZONING", "GPKG")
    zoning = GpuInspectedLayer(
        logical_name="zoning",
        reference=zoning_ref,
        data=zoning_frame,
        summary=_summary(zoning_frame, "ZONING"),
    )
    inventory = _physical_inventory(extraction_root)
    _write_extraction_manifest(extraction_root, ARCHIVE_SHA, inventory)
    extraction = GpuExtraction(
        archive=archive,
        extraction_root=extraction_root,
        files=inventory,
        standard_models=(STANDARD,),
        cache_hit=True,
    )
    config_payload = load_gpu_source_config(
        Path("configs/sources/gpu_fr.yaml")
    ).model_dump(mode="python")
    for role in config_payload["spatial_layers"]:
        config_payload["spatial_layers"][role]["match_tokens"] = [f"unused_{role}"]
    config_payload["spatial_layers"]["zoning"]["match_tokens"] = ["ZONING"]
    for layer in related:
        config_payload["spatial_layers"][layer.logical_name]["match_tokens"] = [
            layer.reference.source_layer
        ]
    source_config = GpuSourceConfig.model_validate(config_payload)
    related_by_logical_name = {layer.logical_name: layer for layer in related}
    related = tuple(
        related_by_logical_name[logical_name]
        for logical_name in gpu_source_module._GPU_LOGICAL_LAYER_NAMES
        if logical_name != "zoning" and logical_name in related_by_logical_name
    )
    return GpuPlanningDocument(
        source_config=source_config,
        source_config_sha256=gpu_source_module._source_config_sha256(source_config),
        extraction=extraction,
        all_spatial_layers=gpu_source_module.discover_gpu_spatial_layers(extraction),
        zoning=zoning,
        related_layers=related,
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_run`

**Purpose:** Implements `run` within the file role: Provides complete unit and regression coverage for the `enrich_planning_features` contracts exercised in this file.

**Exact signature**

```python
def _run(
    layers: list[GpuInspectedLayer],
    parcels: gpd.GeoDataFrame | None = None,
) -> ParcelPlanningFeaturesResult:
```

- Exact decorators: none.
- Declared return annotation: `ParcelPlanningFeaturesResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `layers` | positional-or-keyword | `list[GpuInspectedLayer]` | `required` |
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `intersect_parcels_with_gpu_planning_features(<br>        parcels if parcels is not None else _parcels(),<br>        _planning_document(layers),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_planning_features::test_result_is_frozen` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_result_is_frozen` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_surface_full_overlap_normalizes_raw_values_and_lineage` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_surface_full_overlap_normalizes_raw_values_and_lineage` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_surface_partial_and_touch_relations` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_surface_partial_and_touch_relations` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_overlapping_surface_union_is_not_double_counted` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_overlapping_surface_union_is_not_double_counted` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_polygon_and_multipolygon_surfaces` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_polygon_and_multipolygon_surfaces` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_line_crossing_and_partly_inside` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_line_crossing_and_partly_inside` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_line_boundary_touch_is_zero_length` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_line_boundary_touch_is_zero_length` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_linestring_and_multilinestring` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_linestring_and_multilinestring` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_points_inside_boundary_outside_and_multipoint` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_points_inside_boundary_outside_and_multipoint` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_missing_optional_layer_families_return_stable_empty_catalogs` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_missing_optional_layer_families_return_stable_empty_catalogs` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_optional_raw_source_fields_are_not_fabricated` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_optional_raw_source_fields_are_not_fabricated` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_epsg4326_parcels_are_measured_in_lambert93_but_preserved` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_epsg4326_parcels_are_measured_in_lambert93_but_preserved` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_invalid_parcel_ids_are_rejected` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_invalid_parcel_ids_are_rejected` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_duplicate_parcel_ids_are_rejected` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_duplicate_parcel_ids_are_rejected` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_duplicate_source_ids_are_rejected` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_duplicate_source_ids_are_rejected` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_idurba_mismatch_is_rejected` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_idurba_mismatch_is_rejected` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_missing_required_source_fields_fail` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_missing_required_source_fields_fail` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_wrong_geometry_kind_is_rejected` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_wrong_geometry_kind_is_rejected` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_invalid_surface_geometry_is_rejected_without_repair` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_invalid_surface_geometry_is_rejected_without_repair` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_null_or_empty_source_geometry_is_rejected` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_null_or_empty_source_geometry_is_rejected` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_missing_crs_is_rejected` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_missing_crs_is_rejected` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_unusable_source_crs_is_rejected` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_unusable_source_crs_is_rejected` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_reserved_output_column_collision_is_rejected` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_reserved_output_column_collision_is_rejected` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_relations_are_unique_deterministic_and_summaries_agree` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_relations_are_unique_deterministic_and_summaries_agree` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_result_frames_are_independent_from_mutable_inputs` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_result_frames_are_independent_from_mutable_inputs` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_present_empty_optional_layer_is_valid` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_present_empty_optional_layer_is_valid` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_empty_and_nonempty_catalogs_have_identical_kind_schemas` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_empty_and_nonempty_catalogs_have_identical_kind_schemas` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_same_source_id_is_allowed_in_distinct_logical_layers` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_same_source_id_is_allowed_in_distinct_logical_layers` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_geospatial_operation_failure_is_controlled_and_chained` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_geospatial_operation_failure_is_controlled_and_chained` via `_run`
- direct call: `tests.unit.test_enrich_planning_features::test_gpu_source_z_is_normalized_to_canonical_2d` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_features::test_gpu_source_z_is_normalized_to_canonical_2d` via `_run`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `intersect_parcels_with_gpu_planning_features` | `landscout.stages.enrich_planning_features.intersect_parcels_with_gpu_planning_features` |
| `_parcels` | `tests.unit.test_enrich_planning_features._parcels` |
| `_planning_document` | `tests.unit.test_enrich_planning_features._planning_document` |

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
def _run(
    layers: list[GpuInspectedLayer],
    parcels: gpd.GeoDataFrame | None = None,
) -> ParcelPlanningFeaturesResult:
    return intersect_parcels_with_gpu_planning_features(
        parcels if parcels is not None else _parcels(),
        _planning_document(layers),
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_only_high_level_api_is_exported`

**Purpose:** Regression invariant: only high level api is exported. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_only_high_level_api_is_exported() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert (<br>        stages.intersect_parcels_with_gpu_planning_features<br>        is intersect_parcels_with_gpu_planning_features<br>    )`
  - `assert "intersect_parcels_with_gpu_planning_features" in stages.__all__`
  - `assert stages.PlanningFeaturesError is PlanningFeaturesError`
  - `assert stages.ParcelPlanningFeaturesResult is ParcelPlanningFeaturesResult`
  - `assert "PlanningFeaturesError" in stages.__all__`
  - `assert "ParcelPlanningFeaturesResult" in stages.__all__`

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
def test_only_high_level_api_is_exported() -> None:
    assert (
        stages.intersect_parcels_with_gpu_planning_features
        is intersect_parcels_with_gpu_planning_features
    )
    assert "intersect_parcels_with_gpu_planning_features" in stages.__all__
    assert stages.PlanningFeaturesError is PlanningFeaturesError
    assert stages.ParcelPlanningFeaturesResult is ParcelPlanningFeaturesResult
    assert "PlanningFeaturesError" in stages.__all__
    assert "ParcelPlanningFeaturesResult" in stages.__all__
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_result_is_frozen`

**Purpose:** Regression invariant: result is frozen. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_result_is_frozen() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(FrozenInstanceError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `pytest.raises` | `pytest.raises` |
| `result.parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `result.parcels = result.parcels.copy()` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_result_is_frozen() -> None:
    result = _run([])
    with pytest.raises(FrozenInstanceError):
        result.parcels = result.parcels.copy()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_surface_full_overlap_normalizes_raw_values_and_lineage`

**Purpose:** Regression invariant: surface full overlap normalizes raw values and lineage. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_surface_full_overlap_normalizes_raw_values_and_lineage() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert feature["planning_feature_id"] == (<br>        f"GPU:{DOCUMENT_ID}:prescription_surface:PSC-1"<br>    )`
  - `assert feature["source_feature_id"] == "PSC-1"`
  - `assert feature["source_identity_kind"] == "CNIG_ATTRIBUTE"`
  - `assert feature["source_identity_field"] == "LIB_IDPSC"`
  - `assert feature["feature_family"] == "PRESCRIPTION"`
  - `assert feature["geometry_kind"] == "SURFACE"`
  - `assert feature["type_code_raw"] == "DYNAMIC-18"`
  - `assert feature["subtype_code_raw"] == "04"`
  - `assert feature["label_raw"] == "Label 0"`
  - `assert feature["text_raw"] == "Text 0"`
  - `assert feature["source_document_id"] == DOCUMENT_ID`
  - `assert feature["source_archive_sha256"] == ARCHIVE_SHA`
  - `assert feature["source_layer"] == "SOURCE_PRESCRIPTION_SURFACE"`
  - `assert feature["source_crs"] == "EPSG:2154"`
  - `assert feature["feature_area_m2"] == pytest.approx(100.0)`
  - `assert result.surface_features.crs.to_epsg() == 2154`
  - `assert relation["source_identity_kind"] == "CNIG_ATTRIBUTE"`
  - `assert relation["source_identity_field"] == "LIB_IDPSC"`
  - `assert relation["relation_type"] == "AREA_OVERLAP"`
  - `assert relation["intersection_area_m2"] == pytest.approx(100.0)`
  - `assert relation["parcel_share_pct"] == pytest.approx(100.0)`
  - `assert relation["feature_share_pct"] == pytest.approx(100.0)`
  - `assert pd.isna(relation["intersection_length_m"])`
  - `assert parcel["planning_surface_relation_count"] == 1`
  - `assert parcel["planning_surface_area_overlap_count"] == 1`
  - `assert parcel["planning_surface_covered_union_area_m2"] == pytest.approx(100.0)`
  - `assert parcel["planning_surface_covered_pct"] == pytest.approx(100.0)`
  - `assert parcel["prescription_surface_relation_count"] == 1`
  - `assert parcel["information_surface_relation_count"] == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `_rectangle` | `tests.unit.test_enrich_planning_features._rectangle` |
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `pytest.approx` | `pytest.approx` |
| `result.surface_features.crs.to_epsg` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.isna` | `pandas.isna` |

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
def test_surface_full_overlap_normalizes_raw_values_and_lineage() -> None:
    layer = _inspected(
        "prescription_surface",
        _source_frame(
            "prescription_surface",
            [_rectangle(0, 0, 10, 10)],
            ids=["PSC-1"],
            type_codes=["DYNAMIC-18"],
            subtype_codes=["04"],
            crs="IGNF:LAMB93",
        ),
    )
    result = _run([layer])

    feature = result.surface_features.iloc[0]
    assert feature["planning_feature_id"] == (
        f"GPU:{DOCUMENT_ID}:prescription_surface:PSC-1"
    )
    assert feature["source_feature_id"] == "PSC-1"
    assert feature["source_identity_kind"] == "CNIG_ATTRIBUTE"
    assert feature["source_identity_field"] == "LIB_IDPSC"
    assert feature["feature_family"] == "PRESCRIPTION"
    assert feature["geometry_kind"] == "SURFACE"
    assert feature["type_code_raw"] == "DYNAMIC-18"
    assert feature["subtype_code_raw"] == "04"
    assert feature["label_raw"] == "Label 0"
    assert feature["text_raw"] == "Text 0"
    assert feature["source_document_id"] == DOCUMENT_ID
    assert feature["source_archive_sha256"] == ARCHIVE_SHA
    assert feature["source_layer"] == "SOURCE_PRESCRIPTION_SURFACE"
    # The physical GPKG round-trip exposes the equivalent canonical CRS identity.
    assert feature["source_crs"] == "EPSG:2154"
    assert feature["feature_area_m2"] == pytest.approx(100.0)
    assert result.surface_features.crs.to_epsg() == 2154

    relation = result.relations.iloc[0]
    assert relation["source_identity_kind"] == "CNIG_ATTRIBUTE"
    assert relation["source_identity_field"] == "LIB_IDPSC"
    assert relation["relation_type"] == "AREA_OVERLAP"
    assert relation["intersection_area_m2"] == pytest.approx(100.0)
    assert relation["parcel_share_pct"] == pytest.approx(100.0)
    assert relation["feature_share_pct"] == pytest.approx(100.0)
    assert pd.isna(relation["intersection_length_m"])
    parcel = result.parcels.iloc[0]
    assert parcel["planning_surface_relation_count"] == 1
    assert parcel["planning_surface_area_overlap_count"] == 1
    assert parcel["planning_surface_covered_union_area_m2"] == pytest.approx(100.0)
    assert parcel["planning_surface_covered_pct"] == pytest.approx(100.0)
    assert parcel["prescription_surface_relation_count"] == 1
    assert parcel["information_surface_relation_count"] == 0
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_surface_partial_and_touch_relations`

**Purpose:** Regression invariant: surface partial and touch relations. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_surface_partial_and_touch_relations() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert relations.loc["PART", "relation_type"] == "AREA_OVERLAP"`
  - `assert relations.loc["PART", "intersection_area_m2"] == pytest.approx(50.0)`
  - `assert relations.loc["TOUCH", "relation_type"] == "TOUCH_ONLY"`
  - `assert relations.loc["TOUCH", "intersection_area_m2"] == pytest.approx(0.0)`
  - `assert result.parcels.iloc[0]["planning_surface_touch_count"] == 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `_rectangle` | `tests.unit.test_enrich_planning_features._rectangle` |
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `result.relations.set_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.approx` | `pytest.approx` |

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
def test_surface_partial_and_touch_relations() -> None:
    frame = _source_frame(
        "prescription_surface",
        [_rectangle(0, 0, 5, 10), _rectangle(10, 0, 20, 10)],
        ids=["PART", "TOUCH"],
    )
    result = _run([_inspected("prescription_surface", frame)])
    relations = result.relations.set_index("source_feature_id")
    assert relations.loc["PART", "relation_type"] == "AREA_OVERLAP"
    assert relations.loc["PART", "intersection_area_m2"] == pytest.approx(50.0)
    assert relations.loc["TOUCH", "relation_type"] == "TOUCH_ONLY"
    assert relations.loc["TOUCH", "intersection_area_m2"] == pytest.approx(0.0)
    assert result.parcels.iloc[0]["planning_surface_touch_count"] == 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_overlapping_surface_union_is_not_double_counted`

**Purpose:** Regression invariant: overlapping surface union is not double counted. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_overlapping_surface_union_is_not_double_counted() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert parcel["planning_surface_intersection_area_sum_m2"] == pytest.approx(150.0)`
  - `assert parcel["planning_surface_covered_union_area_m2"] == pytest.approx(100.0)`
  - `assert parcel["planning_surface_covered_pct"] == pytest.approx(100.0)`
  - `assert parcel["prescription_surface_covered_union_area_m2"] == pytest.approx(100.0)`
  - `assert parcel["information_surface_covered_union_area_m2"] == pytest.approx(50.0)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `_rectangle` | `tests.unit.test_enrich_planning_features._rectangle` |
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `pytest.approx` | `pytest.approx` |

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
def test_overlapping_surface_union_is_not_double_counted() -> None:
    prescription = _inspected(
        "prescription_surface",
        _source_frame(
            "prescription_surface",
            [_rectangle(0, 0, 10, 10)],
            ids=["WHOLE"],
        ),
    )
    information = _inspected(
        "information_surface",
        _source_frame(
            "information_surface",
            [_rectangle(0, 0, 5, 10)],
            ids=["HALF"],
            type_codes=["99"],
            subtype_codes=["00"],
        ),
    )
    parcel = _run([prescription, information]).parcels.iloc[0]
    assert parcel["planning_surface_intersection_area_sum_m2"] == pytest.approx(150.0)
    assert parcel["planning_surface_covered_union_area_m2"] == pytest.approx(100.0)
    assert parcel["planning_surface_covered_pct"] == pytest.approx(100.0)
    assert parcel["prescription_surface_covered_union_area_m2"] == pytest.approx(100.0)
    assert parcel["information_surface_covered_union_area_m2"] == pytest.approx(50.0)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_polygon_and_multipolygon_surfaces`

**Purpose:** Regression invariant: polygon and multipolygon surfaces. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_polygon_and_multipolygon_surfaces(geometry: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "geometry",
    [
        _rectangle(0, 0, 10, 10),
        MultiPolygon([_rectangle(0, 0, 4, 10), _rectangle(6, 0, 10, 10)]),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert len(result.relations) == 1`
  - `assert result.relations.iloc[0]["intersection_area_m2"] > 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `_rectangle` | `tests.unit.test_enrich_planning_features._rectangle` |
| `MultiPolygon` | `shapely.geometry.MultiPolygon` |

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
def test_polygon_and_multipolygon_surfaces(geometry: object) -> None:
    result = _run(
        [
            _inspected(
                "information_surface", _source_frame("information_surface", [geometry])
            )
        ]
    )
    assert len(result.relations) == 1
    assert result.relations.iloc[0]["intersection_area_m2"] > 0
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_line_crossing_and_partly_inside`

**Purpose:** Regression invariant: line crossing and partly inside. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_line_crossing_and_partly_inside() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert relations.loc["CROSS", "relation_type"] == "LENGTH_OVERLAP"`
  - `assert relations.loc["CROSS", "intersection_length_m"] == pytest.approx(10.0)`
  - `assert relations.loc["CROSS", "source_line_length_m"] == pytest.approx(20.0)`
  - `assert relations.loc["PART", "intersection_length_m"] == pytest.approx(5.0)`
  - `assert parcel["planning_line_relation_count"] == 2`
  - `assert parcel["planning_line_intersection_length_sum_m"] == pytest.approx(15.0)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `LineString` | `shapely.geometry.LineString` |
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `result.relations.set_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.approx` | `pytest.approx` |

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
def test_line_crossing_and_partly_inside() -> None:
    frame = _source_frame(
        "prescription_line",
        [LineString([(-5, 5), (15, 5)]), LineString([(5, 5), (15, 5)])],
        ids=["CROSS", "PART"],
        type_codes=["15", "15"],
        subtype_codes=["01", "00"],
    )
    result = _run([_inspected("prescription_line", frame)])
    relations = result.relations.set_index("source_feature_id")
    assert relations.loc["CROSS", "relation_type"] == "LENGTH_OVERLAP"
    assert relations.loc["CROSS", "intersection_length_m"] == pytest.approx(10.0)
    assert relations.loc["CROSS", "source_line_length_m"] == pytest.approx(20.0)
    assert relations.loc["PART", "intersection_length_m"] == pytest.approx(5.0)
    parcel = result.parcels.iloc[0]
    assert parcel["planning_line_relation_count"] == 2
    assert parcel["planning_line_intersection_length_sum_m"] == pytest.approx(15.0)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_line_boundary_touch_is_zero_length`

**Purpose:** Regression invariant: line boundary touch is zero length. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_line_boundary_touch_is_zero_length() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.relations.iloc[0]["relation_type"] == "TOUCH_ONLY"`
  - `assert result.relations.iloc[0]["intersection_length_m"] == pytest.approx(0.0)`
  - `assert result.parcels.iloc[0]["planning_line_touch_count"] == 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `LineString` | `shapely.geometry.LineString` |
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `pytest.approx` | `pytest.approx` |

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
def test_line_boundary_touch_is_zero_length() -> None:
    frame = _source_frame(
        "prescription_line",
        [LineString([(10, 5), (15, 5)])],
        ids=["TOUCH"],
    )
    result = _run([_inspected("prescription_line", frame)])
    assert result.relations.iloc[0]["relation_type"] == "TOUCH_ONLY"
    assert result.relations.iloc[0]["intersection_length_m"] == pytest.approx(0.0)
    assert result.parcels.iloc[0]["planning_line_touch_count"] == 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_linestring_and_multilinestring`

**Purpose:** Regression invariant: linestring and multilinestring. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_linestring_and_multilinestring(geometry: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "geometry",
    [
        LineString([(-1, 5), (11, 5)]),
        MultiLineString([[(-1, 2), (11, 2)], [(-1, 8), (11, 8)]]),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.relations.iloc[0]["intersection_length_m"] > 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `LineString` | `shapely.geometry.LineString` |
| `MultiLineString` | `shapely.geometry.MultiLineString` |

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
def test_linestring_and_multilinestring(geometry: object) -> None:
    result = _run(
        [
            _inspected(
                "prescription_line", _source_frame("prescription_line", [geometry])
            )
        ]
    )
    assert result.relations.iloc[0]["intersection_length_m"] > 0
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_points_inside_boundary_outside_and_multipoint`

**Purpose:** Regression invariant: points inside boundary outside and multipoint. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_points_inside_boundary_outside_and_multipoint() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert set(relations.index) == {"IN", "BOUNDARY", "MULTI"}`
  - `assert relations.loc["IN", "relation_type"] == "INSIDE"`
  - `assert relations.loc["BOUNDARY", "relation_type"] == "BOUNDARY_TOUCH"`
  - `assert relations.loc["MULTI", "point_member_count"] == 3`
  - `assert relations.loc["MULTI", "point_members_inside_count"] == 1`
  - `assert relations.loc["MULTI", "point_members_boundary_count"] == 1`
  - `assert parcel["planning_point_relation_count"] == 3`
  - `assert parcel["planning_point_inside_count"] == 2`
  - `assert parcel["planning_point_boundary_count"] == 2`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `Point` | `shapely.geometry.Point` |
| `MultiPoint` | `shapely.geometry.MultiPoint` |
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `result.relations.set_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_points_inside_boundary_outside_and_multipoint() -> None:
    frame = _source_frame(
        "prescription_point",
        [
            Point(5, 5),
            Point(10, 5),
            Point(20, 20),
            MultiPoint([(3, 3), (10, 4), (30, 30)]),
        ],
        ids=["IN", "BOUNDARY", "OUT", "MULTI"],
        type_codes=["07"] * 4,
        subtype_codes=["00"] * 4,
    )
    result = _run([_inspected("prescription_point", frame)])
    relations = result.relations.set_index("source_feature_id")
    assert set(relations.index) == {"IN", "BOUNDARY", "MULTI"}
    assert relations.loc["IN", "relation_type"] == "INSIDE"
    assert relations.loc["BOUNDARY", "relation_type"] == "BOUNDARY_TOUCH"
    assert relations.loc["MULTI", "point_member_count"] == 3
    assert relations.loc["MULTI", "point_members_inside_count"] == 1
    assert relations.loc["MULTI", "point_members_boundary_count"] == 1
    parcel = result.parcels.iloc[0]
    assert parcel["planning_point_relation_count"] == 3
    assert parcel["planning_point_inside_count"] == 2
    assert parcel["planning_point_boundary_count"] == 2
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_optional_layer_families_return_stable_empty_catalogs`

**Purpose:** Regression invariant: missing optional layer families return stable empty catalogs. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_missing_optional_layer_families_return_stable_empty_catalogs() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.surface_features.empty`
  - `assert result.line_features.empty`
  - `assert result.point_features.empty`
  - `assert result.relations.empty`
  - `assert result.surface_features.crs.to_epsg() == 2154`
  - `assert str(result.relations["point_member_count"].dtype) == "Int64"`
  - `assert result.parcels.iloc[0]["planning_surface_relation_count"] == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `result.surface_features.crs.to_epsg` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_missing_optional_layer_families_return_stable_empty_catalogs() -> None:
    result = _run([])
    assert result.surface_features.empty
    assert result.line_features.empty
    assert result.point_features.empty
    assert result.relations.empty
    assert result.surface_features.crs.to_epsg() == 2154
    assert str(result.relations["point_member_count"].dtype) == "Int64"
    assert result.parcels.iloc[0]["planning_surface_relation_count"] == 0
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_optional_raw_source_fields_are_not_fabricated`

**Purpose:** Regression invariant: optional raw source fields are not fabricated. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_optional_raw_source_fields_are_not_fabricated() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert pd.isna(feature[column])`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]).drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `LineString` | `shapely.geometry.LineString` |
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `pd.isna` | `pandas.isna` |

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
| In-memory mutation | `_source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]).drop(<br>        columns=["LIBELLE", "TXT", "NOMFIC", "URLFIC", "DATVALID"]<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_optional_raw_source_fields_are_not_fabricated() -> None:
    frame = _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]).drop(
        columns=["LIBELLE", "TXT", "NOMFIC", "URLFIC", "DATVALID"]
    )
    result = _run([_inspected("prescription_line", frame)])
    feature = result.line_features.iloc[0]
    for column in (
        "label_raw",
        "text_raw",
        "regulation_filename_raw",
        "regulation_url_raw",
        "source_validity_date_raw",
    ):
        assert pd.isna(feature[column])
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_epsg4326_parcels_are_measured_in_lambert93_but_preserved`

**Purpose:** Regression invariant: epsg4326 parcels are measured in lambert93 but preserved. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_epsg4326_parcels_are_measured_in_lambert93_but_preserved() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.parcels.crs == original.crs`
  - `assert np.array_equal(result.parcels.geometry.to_wkb(), original.geometry.to_wkb())`
  - `assert result.relations.iloc[0]["intersection_area_m2"] == pytest.approx(100.0)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_planning_features._parcels` |
| `parcel.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `_rectangle` | `tests.unit.test_enrich_planning_features._rectangle` |
| `np.array_equal` | `numpy.array_equal` |
| `result.parcels.geometry.to_wkb` | `unresolved local/third-party receiver; no ownership inferred` |
| `original.geometry.to_wkb` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.approx` | `pytest.approx` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `result.parcels.geometry.to_wkb`<br>`original.geometry.to_wkb` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_epsg4326_parcels_are_measured_in_lambert93_but_preserved() -> None:
    parcel = _parcels(crs="EPSG:4326")
    original = parcel.copy(deep=True)
    result = _run(
        [
            _inspected(
                "prescription_surface",
                _source_frame("prescription_surface", [_rectangle(0, 0, 10, 10)]),
            )
        ],
        parcel,
    )
    assert result.parcels.crs == original.crs
    assert np.array_equal(result.parcels.geometry.to_wkb(), original.geometry.to_wkb())
    assert result.relations.iloc[0]["intersection_area_m2"] == pytest.approx(100.0)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_parcel_ids_are_rejected`

**Purpose:** Regression invariant: invalid parcel ids are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_parcel_ids_are_rejected(bad_id: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize("bad_id", [None, "", "   ", " X", "X ", 7])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `bad_id` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="parcel_id")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `_parcels` | `tests.unit.test_enrich_planning_features._parcels` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
def test_invalid_parcel_ids_are_rejected(bad_id: object) -> None:
    with pytest.raises(PlanningFeaturesError, match="parcel_id"):
        _run([], _parcels(ids=[bad_id]))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_parcel_ids_are_rejected`

**Purpose:** Regression invariant: duplicate parcel ids are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_parcel_ids_are_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="unique")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `_parcels` | `tests.unit.test_enrich_planning_features._parcels` |
| `_rectangle` | `tests.unit.test_enrich_planning_features._rectangle` |

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
def test_duplicate_parcel_ids_are_rejected() -> None:
    with pytest.raises(PlanningFeaturesError, match="unique"):
        _run(
            [],
            _parcels([_rectangle(0, 0, 2, 2), _rectangle(3, 3, 4, 4)], ids=["P", "P"]),
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_source_ids_are_rejected`

**Purpose:** Regression invariant: duplicate source ids are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_source_ids_are_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="unique")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `_rectangle` | `tests.unit.test_enrich_planning_features._rectangle` |
| `pytest.raises` | `pytest.raises` |
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |

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
def test_duplicate_source_ids_are_rejected() -> None:
    frame = _source_frame(
        "information_surface",
        [_rectangle(0, 0, 2, 2), _rectangle(3, 3, 4, 4)],
        ids=["SAME", "SAME"],
    )
    with pytest.raises(PlanningFeaturesError, match="unique"):
        _run([_inspected("information_surface", frame)])
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent`

**Purpose:** Regression invariant: prescription surface uses validated source ogr fid when cnig id absent. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent(
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
- Exact assertions:
  - `assert result.surface_features.iloc[0]["source_feature_id"] == "OGR_FID:0"`
  - `assert (<br>        result.surface_features.iloc[0]["source_identity_kind"]<br>        == "ARCHIVE_SCOPED_OGR_FID"<br>    )`
  - `assert result.surface_features.iloc[0]["source_identity_field"] == "OGR_FID"`
  - `assert result.surface_features.iloc[0]["planning_feature_id"] == (<br>        f"GPU:{DOCUMENT_ID}:prescription_surface:OGR_FID:0"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_frame("prescription_surface", [_rectangle(0, 0, 10, 10)]).drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `_rectangle` | `tests.unit.test_enrich_planning_features._rectangle` |
| `frame.to_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.read_file` | `geopandas.read_file` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `replace` | `dataclasses.replace` |
| `_summary` | `tests.unit.test_enrich_planning_features._summary` |
| `_run` | `tests.unit.test_enrich_planning_features._run` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `gpd.read_file` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `_source_frame("prescription_surface", [_rectangle(0, 0, 10, 10)]).drop(<br>        columns="LIB_IDPSC"<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent(
    tmp_path: Path,
) -> None:
    source_layer = "PRESCRIPTION_SURFACE"
    path = tmp_path / f"{source_layer}.shp"
    frame = _source_frame("prescription_surface", [_rectangle(0, 0, 10, 10)]).drop(
        columns="LIB_IDPSC"
    )
    frame.to_file(path, engine="pyogrio")
    loaded = gpd.read_file(path, engine="pyogrio")
    layer = _inspected("prescription_surface", loaded)
    reference = replace(
        layer.reference,
        dataset_path=path,
        source_layer=source_layer,
        driver="ESRI Shapefile",
    )
    layer = replace(
        layer,
        reference=reference,
        summary=_summary(loaded, source_layer),
    )
    result = _run([layer])
    assert result.surface_features.iloc[0]["source_feature_id"] == "OGR_FID:0"
    assert (
        result.surface_features.iloc[0]["source_identity_kind"]
        == "ARCHIVE_SCOPED_OGR_FID"
    )
    assert result.surface_features.iloc[0]["source_identity_field"] == "OGR_FID"
    assert result.surface_features.iloc[0]["planning_feature_id"] == (
        f"GPU:{DOCUMENT_ID}:prescription_surface:OGR_FID:0"
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback`

**Purpose:** Regression invariant: geopackage prescription surface uses sealed ogr fid fallback. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert feature["source_feature_id"] == "OGR_FID:1"`
  - `assert feature["source_identity_kind"] == "ARCHIVE_SCOPED_OGR_FID"`
  - `assert feature["source_identity_field"] == "OGR_FID"`
  - `assert feature["planning_feature_id"] == (<br>        f"GPU:{DOCUMENT_ID}:prescription_surface:OGR_FID:1"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_frame("prescription_surface", [_rectangle(0, 0, 10, 10)]).drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `_rectangle` | `tests.unit.test_enrich_planning_features._rectangle` |
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |

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
| In-memory mutation | `_source_frame("prescription_surface", [_rectangle(0, 0, 10, 10)]).drop(<br>        columns="LIB_IDPSC"<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback() -> None:
    frame = _source_frame("prescription_surface", [_rectangle(0, 0, 10, 10)]).drop(
        columns="LIB_IDPSC"
    )
    result = _run([_inspected("prescription_surface", frame)])
    feature = result.surface_features.iloc[0]
    assert feature["source_feature_id"] == "OGR_FID:1"
    assert feature["source_identity_kind"] == "ARCHIVE_SCOPED_OGR_FID"
    assert feature["source_identity_field"] == "OGR_FID"
    assert feature["planning_feature_id"] == (
        f"GPU:{DOCUMENT_ID}:prescription_surface:OGR_FID:1"
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_idurba_mismatch_is_rejected`

**Purpose:** Regression invariant: idurba mismatch is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_idurba_mismatch_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="IDURBA")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `LineString` | `shapely.geometry.LineString` |
| `pytest.raises` | `pytest.raises` |
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |

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
def test_idurba_mismatch_is_rejected() -> None:
    frame = _source_frame(
        "prescription_line", [LineString([(0, 5), (10, 5)])], document_refs=["OTHER"]
    )
    with pytest.raises(PlanningFeaturesError, match="IDURBA"):
        _run([_inspected("prescription_line", frame)])
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_required_source_fields_fail`

**Purpose:** Regression invariant: missing required source fields fail. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_missing_required_source_fields_fail(missing: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("missing", ["TYPEPSC", "STYPEPSC", "IDURBA", "LIB_IDPSC"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `missing` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match=missing)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]).drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `LineString` | `shapely.geometry.LineString` |
| `pytest.raises` | `pytest.raises` |
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
| In-memory mutation | `_source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]).drop(<br>        columns=missing<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_missing_required_source_fields_fail(missing: str) -> None:
    frame = _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]).drop(
        columns=missing
    )
    with pytest.raises(PlanningFeaturesError, match=missing):
        _run([_inspected("prescription_line", frame)])
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_wrong_geometry_kind_is_rejected`

**Purpose:** Regression invariant: wrong geometry kind is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_wrong_geometry_kind_is_rejected(logical: str, geometry: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("logical", "geometry"),
    [
        ("prescription_surface", LineString([(0, 0), (1, 1)])),
        ("prescription_line", Point(1, 1)),
        ("prescription_point", LineString([(0, 0), (1, 1)])),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `logical` | positional-or-keyword | `str` | `required` |
| `geometry` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="geometry")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `LineString` | `shapely.geometry.LineString` |
| `Point` | `shapely.geometry.Point` |

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
def test_wrong_geometry_kind_is_rejected(logical: str, geometry: object) -> None:
    with pytest.raises(PlanningFeaturesError, match="geometry"):
        _run([_inspected(logical, _source_frame(logical, [geometry]))])
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_surface_geometry_is_rejected_without_repair`

**Purpose:** Regression invariant: invalid surface geometry is rejected without repair. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_surface_geometry_is_rejected_without_repair() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="valid")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `pytest.raises` | `pytest.raises` |
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |

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
def test_invalid_surface_geometry_is_rejected_without_repair() -> None:
    bowtie = Polygon([(0, 0), (2, 2), (2, 0), (0, 2), (0, 0)])
    with pytest.raises(PlanningFeaturesError, match="valid"):
        _run(
            [
                _inspected(
                    "information_surface",
                    _source_frame("information_surface", [bowtie]),
                )
            ]
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_null_or_empty_source_geometry_is_rejected`

**Purpose:** Regression invariant: null or empty source geometry is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_null_or_empty_source_geometry_is_rejected(geometry: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize("geometry", [None, Polygon()])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="geometry")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `_rectangle` | `tests.unit.test_enrich_planning_features._rectangle` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `pytest.raises` | `pytest.raises` |
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `Polygon` | `shapely.geometry.Polygon` |

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
| In-memory mutation | `frame.geometry = [geometry]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_null_or_empty_source_geometry_is_rejected(geometry: object) -> None:
    frame = _source_frame("information_surface", [_rectangle(0, 0, 1, 1)])
    frame.geometry = [geometry]
    layer = _inspected("information_surface", frame)
    with pytest.raises(PlanningFeaturesError, match="geometry"):
        _run([layer])
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_crs_is_rejected`

**Purpose:** Regression invariant: missing crs is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_missing_crs_is_rejected(target: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("target", ["parcel", "source"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `target` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="CRS\|physical revalidation")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_planning_features._parcels` |
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `LineString` | `shapely.geometry.LineString` |
| `pytest.raises` | `pytest.raises` |
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
def test_missing_crs_is_rejected(target: str) -> None:
    parcel = _parcels(crs=None) if target == "parcel" else _parcels()
    frame = _source_frame(
        "prescription_line",
        [LineString([(0, 5), (10, 5)])],
        crs=None if target == "source" else "EPSG:2154",
    )
    with pytest.raises(PlanningFeaturesError, match="CRS|physical revalidation"):
        _run([_inspected("prescription_line", frame)], parcel)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unusable_source_crs_is_rejected`

**Purpose:** Regression invariant: unusable source crs is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unusable_source_crs_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="CRS")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]).set_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `LineString` | `shapely.geometry.LineString` |
| `pytest.raises` | `pytest.raises` |
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]).set_crs` |
| External process/environment | None directly present. |
| In-memory mutation | `_source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]).set_crs(<br>        LOCAL_ENGINEERING_CRS, allow_override=True<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_unusable_source_crs_is_rejected() -> None:
    frame = _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]).set_crs(
        LOCAL_ENGINEERING_CRS, allow_override=True
    )
    with pytest.raises(PlanningFeaturesError, match="CRS"):
        _run([_inspected("prescription_line", frame)])
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_mutated_source_summary_is_rejected`

**Purpose:** Regression invariant: mutated source summary is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_mutated_source_summary_is_rejected(field: str, value: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "value"),
    [
        ("source_document_id", "other"),
        ("source_archive_sha256", "b" * 64),
        ("source_layer", "other"),
        ("feature_count", 99),
        ("geometry_types", (("Point", 1),)),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `field` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="summary\|physical revalidation")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `LineString` | `shapely.geometry.LineString` |
| `_planning_document` | `tests.unit.test_enrich_planning_features._planning_document` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `intersect_parcels_with_gpu_planning_features` | `landscout.stages.enrich_planning_features.intersect_parcels_with_gpu_planning_features` |
| `_parcels` | `tests.unit.test_enrich_planning_features._parcels` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
def test_mutated_source_summary_is_rejected(field: str, value: object) -> None:
    layer = _inspected(
        "prescription_line",
        _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]),
    )
    planning_document = _planning_document([layer])
    stored = planning_document.related_layers[0]
    corrupted = replace(stored, summary=replace(stored.summary, **{field: value}))
    changed = replace(planning_document, related_layers=(corrupted,))
    with pytest.raises(PlanningFeaturesError, match="summary|physical revalidation"):
        intersect_parcels_with_gpu_planning_features(_parcels(), changed)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_summary_counts_are_strict_integers`

**Purpose:** Regression invariant: source summary counts are strict integers. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_summary_counts_are_strict_integers(bad_count: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize("bad_count", [True, -1, 1.5, float("inf"), "1"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `bad_count` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        PlanningFeaturesError,<br>        match="integer count\|non-negative\|summary\|physical revalidation",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `LineString` | `shapely.geometry.LineString` |
| `_planning_document` | `tests.unit.test_enrich_planning_features._planning_document` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `intersect_parcels_with_gpu_planning_features` | `landscout.stages.enrich_planning_features.intersect_parcels_with_gpu_planning_features` |
| `_parcels` | `tests.unit.test_enrich_planning_features._parcels` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_source_summary_counts_are_strict_integers(bad_count: object) -> None:
    layer = _inspected(
        "prescription_line",
        _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]),
    )
    planning_document = _planning_document([layer])
    stored = planning_document.related_layers[0]
    corrupted = replace(
        stored, summary=replace(stored.summary, feature_count=bad_count)
    )
    changed = replace(planning_document, related_layers=(corrupted,))
    with pytest.raises(
        PlanningFeaturesError,
        match="integer count|non-negative|summary|physical revalidation",
    ):
        intersect_parcels_with_gpu_planning_features(_parcels(), changed)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_reserved_output_column_collision_is_rejected`

**Purpose:** Regression invariant: reserved output column collision is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_reserved_output_column_collision_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="output columns")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_planning_features._parcels` |
| `pytest.raises` | `pytest.raises` |
| `_run` | `tests.unit.test_enrich_planning_features._run` |

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
| In-memory mutation | `parcels["planning_surface_relation_count"] = 99` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_reserved_output_column_collision_is_rejected() -> None:
    parcels = _parcels()
    parcels["planning_surface_relation_count"] = 99
    with pytest.raises(PlanningFeaturesError, match="output columns"):
        _run([], parcels)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_inputs_and_all_existing_parcel_fields_are_preserved`

**Purpose:** Regression invariant: inputs and all existing parcel fields are preserved. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_inputs_and_all_existing_parcel_fields_are_preserved() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.parcels["parcel_id"].tolist() == parcels["parcel_id"].tolist()`
  - `assert result.parcels.index.equals(parcels.index)`
  - `assert result.parcels["existing_zoning_fact"].equals(<br>        parcels["existing_zoning_fact"]<br>    )`
  - `assert np.array_equal(result.parcels.geometry.to_wkb(), parcels.geometry.to_wkb())`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_planning_features._parcels` |
| `_rectangle` | `tests.unit.test_enrich_planning_features._rectangle` |
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `_planning_document` | `tests.unit.test_enrich_planning_features._planning_document` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `planning.related_layers[0].data.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `intersect_parcels_with_gpu_planning_features` | `landscout.stages.enrich_planning_features.intersect_parcels_with_gpu_planning_features` |
| `assert_geodataframe_equal` | `geopandas.testing.assert_geodataframe_equal` |
| `result.parcels["parcel_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels["parcel_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels.index.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels["existing_zoning_fact"].equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.array_equal` | `numpy.array_equal` |
| `result.parcels.geometry.to_wkb` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.geometry.to_wkb` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `result.parcels.geometry.to_wkb`<br>`parcels.geometry.to_wkb` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_inputs_and_all_existing_parcel_fields_are_preserved() -> None:
    parcels = _parcels([_rectangle(0, 0, 10, 10), _rectangle(20, 20, 30, 30)])
    frame = _source_frame(
        "prescription_surface", [_rectangle(0, 0, 5, 10)], ids=["PSC"]
    )
    planning = _planning_document([_inspected("prescription_surface", frame)])
    parcels_before = parcels.copy(deep=True)
    zoning_before = planning.related_layers[0].data.copy(deep=True)
    result = intersect_parcels_with_gpu_planning_features(parcels, planning)
    assert_geodataframe_equal(parcels, parcels_before)
    assert_geodataframe_equal(planning.related_layers[0].data, zoning_before)
    assert result.parcels["parcel_id"].tolist() == parcels["parcel_id"].tolist()
    assert result.parcels.index.equals(parcels.index)
    assert result.parcels["existing_zoning_fact"].equals(
        parcels["existing_zoning_fact"]
    )
    assert np.array_equal(result.parcels.geometry.to_wkb(), parcels.geometry.to_wkb())
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_relations_are_unique_deterministic_and_summaries_agree`

**Purpose:** Regression invariant: relations are unique deterministic and summaries agree. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_relations_are_unique_deterministic_and_summaries_agree() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert not result.relations.duplicated(["parcel_id", "planning_feature_id"]).any()`
  - `assert result.relations["parcel_id"].tolist() == ["P-B", "P-B", "P-A"]`
  - `assert first["planning_surface_relation_count"] == int(<br>        (<br>            (result.relations["parcel_id"] == "P-B")<br>            & (result.relations["geometry_kind"] == "SURFACE")<br>        ).sum()<br>    )`
  - `assert first["planning_line_intersection_length_sum_m"] == pytest.approx(<br>        result.relations.loc[<br>            (result.relations["parcel_id"] == "P-B")<br>            & (result.relations["geometry_kind"] == "LINE"),<br>            "intersection_length_m",<br>        ].sum()<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_planning_features._parcels` |
| `_rectangle` | `tests.unit.test_enrich_planning_features._rectangle` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `LineString` | `shapely.geometry.LineString` |
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `result.relations.duplicated(["parcel_id", "planning_feature_id"]).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.relations.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.relations["parcel_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `(<br>            (result.relations["parcel_id"] == "P-B")<br>            & (result.relations["geometry_kind"] == "SURFACE")<br>        ).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.approx` | `pytest.approx` |
| `result.relations.loc[<br>            (result.relations["parcel_id"] == "P-B")<br>            & (result.relations["geometry_kind"] == "LINE"),<br>            "intersection_length_m",<br>        ].sum` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `(<br>            (result.relations["parcel_id"] == "P-B")<br>            & (result.relations["geometry_kind"] == "SURFACE")<br>        ).sum`<br>`result.relations.loc[<br>            (result.relations["parcel_id"] == "P-B")<br>            & (result.relations["geometry_kind"] == "LINE"),<br>            "intersection_length_m",<br>        ].sum` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_relations_are_unique_deterministic_and_summaries_agree() -> None:
    parcels = _parcels(
        [_rectangle(0, 0, 10, 10), _rectangle(20, 20, 30, 30)], ids=["P-B", "P-A"]
    )
    surface = _inspected(
        "information_surface",
        _source_frame("information_surface", [_rectangle(-1, -1, 31, 31)], ids=["I"]),
    )
    line = _inspected(
        "prescription_line",
        _source_frame("prescription_line", [LineString([(-1, 5), (11, 5)])], ids=["L"]),
    )
    result = _run([surface, line], parcels)
    assert not result.relations.duplicated(["parcel_id", "planning_feature_id"]).any()
    assert result.relations["parcel_id"].tolist() == ["P-B", "P-B", "P-A"]
    first = result.parcels.iloc[0]
    assert first["planning_surface_relation_count"] == int(
        (
            (result.relations["parcel_id"] == "P-B")
            & (result.relations["geometry_kind"] == "SURFACE")
        ).sum()
    )
    assert first["planning_line_intersection_length_sum_m"] == pytest.approx(
        result.relations.loc[
            (result.relations["parcel_id"] == "P-B")
            & (result.relations["geometry_kind"] == "LINE"),
            "intersection_length_m",
        ].sum()
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_result_frames_are_independent_from_mutable_inputs`

**Purpose:** Regression invariant: result frames are independent from mutable inputs. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_result_frames_are_independent_from_mutable_inputs() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_planning_features._parcels` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `LineString` | `shapely.geometry.LineString` |
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `deepcopy` | `copy.deepcopy` |
| `assert_frame_equal` | `pandas.testing.assert_frame_equal` |

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
| In-memory mutation | `parcels.loc[50, "existing_zoning_fact"] = -1`<br>`layer.data.loc[0, "LIBELLE"] = "mutated"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_result_frames_are_independent_from_mutable_inputs() -> None:
    parcels = _parcels()
    layer = _inspected(
        "prescription_line",
        _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]),
    )
    result = _run([layer], parcels)
    snapshot = deepcopy(result.relations)
    parcels.loc[50, "existing_zoning_fact"] = -1
    layer.data.loc[0, "LIBELLE"] = "mutated"
    assert_frame_equal(result.relations, snapshot)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_present_empty_optional_layer_is_valid`

**Purpose:** Regression invariant: present empty optional layer is valid. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_present_empty_optional_layer_is_valid(
    logical: str,
    catalog_name: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("logical", "catalog_name"),
    [
        ("prescription_surface", "surface_features"),
        ("prescription_line", "line_features"),
        ("prescription_point", "point_features"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `logical` | positional-or-keyword | `str` | `required` |
| `catalog_name` | positional-or-keyword | `str` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert catalog.empty`
  - `assert catalog.crs.to_epsg() == 2154`
  - `assert result.relations.empty`
  - `assert len(result.parcels) == 1`
  - `assert result.parcels.iloc[0]["planning_feature_document_id"] == DOCUMENT_ID`
  - `assert fid_reads == 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `frame.drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `catalog.crs.to_epsg` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
| In-memory mutation | `frame.drop(columns="LIB_IDPSC")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_present_empty_optional_layer_is_valid(
    logical: str,
    catalog_name: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    frame = _source_frame(logical, [])
    fid_reads = 0
    if logical == "prescription_surface":
        frame = frame.drop(columns="LIB_IDPSC")
        real_read_dataframe = gpu_source_module.pyogrio.read_dataframe

        def unexpected_fid_read(*args: object, **kwargs: object) -> object:
            nonlocal fid_reads
            if kwargs.get("fid_as_index"):
                fid_reads += 1
            return real_read_dataframe(*args, **kwargs)

        monkeypatch.setattr(
            gpu_source_module.pyogrio,
            "read_dataframe",
            unexpected_fid_read,
        )
    result = _run([_inspected(logical, frame)])
    catalog = getattr(result, catalog_name)
    assert catalog.empty
    assert catalog.crs.to_epsg() == 2154
    assert result.relations.empty
    assert len(result.parcels) == 1
    assert result.parcels.iloc[0]["planning_feature_document_id"] == DOCUMENT_ID
    if logical == "prescription_surface":
        assert fid_reads == 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_present_empty_optional_layer_is_valid.unexpected_fid_read`

**Purpose:** Implements `unexpected fid read` within the file role: Provides complete unit and regression coverage for the `enrich_planning_features` contracts exercised in this file.

**Exact signature**

```python
def unexpected_fid_read(*args: object, **kwargs: object) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `real_read_dataframe(*args, **kwargs)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `kwargs.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `real_read_dataframe` | `unresolved local/third-party receiver; no ownership inferred` |

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
def unexpected_fid_read(*args: object, **kwargs: object) -> object:
            nonlocal fid_reads
            if kwargs.get("fid_as_index"):
                fid_reads += 1
            return real_read_dataframe(*args, **kwargs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_contract_result`

**Purpose:** Implements `contract result` within the file role: Provides complete unit and regression coverage for the `enrich_planning_features` contracts exercised in this file.

**Exact signature**

```python
def _contract_result() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    ParcelPlanningFeaturesResult,
]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[GpuPlanningDocument, gpd.GeoDataFrame, ParcelPlanningFeaturesResult]`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `(<br>        planning_document,<br>        parcels,<br>        intersect_parcels_with_gpu_planning_features(parcels, planning_document),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_planning_features::test_empty_and_nonempty_catalogs_have_identical_kind_schemas` via `_contract_result`
- value/type reference: `tests.unit.test_enrich_planning_features::test_empty_and_nonempty_catalogs_have_identical_kind_schemas` via `_contract_result`
- direct call: `tests.unit.test_enrich_planning_features::test_strict_relation_integer_counts_are_enforced` via `_contract_result`
- value/type reference: `tests.unit.test_enrich_planning_features::test_strict_relation_integer_counts_are_enforced` via `_contract_result`
- direct call: `tests.unit.test_enrich_planning_features::test_strict_parcel_summary_integer_counts_are_enforced` via `_contract_result`
- value/type reference: `tests.unit.test_enrich_planning_features::test_strict_parcel_summary_integer_counts_are_enforced` via `_contract_result`
- direct call: `tests.unit.test_enrich_planning_features::test_corrupted_relation_semantics_are_rejected` via `_contract_result`
- value/type reference: `tests.unit.test_enrich_planning_features::test_corrupted_relation_semantics_are_rejected` via `_contract_result`
- direct call: `tests.unit.test_enrich_planning_features::test_point_member_relation_semantics_are_exact` via `_contract_result`
- value/type reference: `tests.unit.test_enrich_planning_features::test_point_member_relation_semantics_are_exact` via `_contract_result`
- direct call: `tests.unit.test_enrich_planning_features::test_shared_intrinsic_relation_semantics_reject_every_invalid_case` via `_contract_result`
- value/type reference: `tests.unit.test_enrich_planning_features::test_shared_intrinsic_relation_semantics_reject_every_invalid_case` via `_contract_result`
- direct call: `tests.unit.test_enrich_planning_features::test_relation_must_match_feature_catalog` via `_contract_result`
- value/type reference: `tests.unit.test_enrich_planning_features::test_relation_must_match_feature_catalog` via `_contract_result`
- direct call: `tests.unit.test_enrich_planning_features::test_feature_ids_are_globally_unique_across_catalogs` via `_contract_result`
- value/type reference: `tests.unit.test_enrich_planning_features::test_feature_ids_are_globally_unique_across_catalogs` via `_contract_result`
- direct call: `tests.unit.test_enrich_planning_features::test_corrupted_parcel_summary_is_rejected` via `_contract_result`
- value/type reference: `tests.unit.test_enrich_planning_features::test_corrupted_parcel_summary_is_rejected` via `_contract_result`
- direct call: `tests.unit.test_enrich_planning_features::test_corrupted_surface_union_contract_is_rejected` via `_contract_result`
- value/type reference: `tests.unit.test_enrich_planning_features::test_corrupted_surface_union_contract_is_rejected` via `_contract_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_planning_features._parcels` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `_rectangle` | `tests.unit.test_enrich_planning_features._rectangle` |
| `LineString` | `shapely.geometry.LineString` |
| `Point` | `shapely.geometry.Point` |
| `_planning_document` | `tests.unit.test_enrich_planning_features._planning_document` |
| `intersect_parcels_with_gpu_planning_features` | `landscout.stages.enrich_planning_features.intersect_parcels_with_gpu_planning_features` |

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
def _contract_result() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    ParcelPlanningFeaturesResult,
]:
    parcels = _parcels()
    layers = [
        _inspected(
            "prescription_surface",
            _source_frame(
                "prescription_surface",
                [_rectangle(0, 0, 10, 10)],
                ids=["SURFACE"],
            ),
        ),
        _inspected(
            "prescription_line",
            _source_frame(
                "prescription_line",
                [LineString([(-1, 5), (11, 5)])],
                ids=["LINE"],
            ),
        ),
        _inspected(
            "prescription_point",
            _source_frame("prescription_point", [Point(5, 5)], ids=["POINT"]),
        ),
    ]
    planning_document = _planning_document(layers)
    return (
        planning_document,
        parcels,
        intersect_parcels_with_gpu_planning_features(parcels, planning_document),
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_source_complete_contract`

**Purpose:** Implements `source complete contract` within the file role: Provides complete unit and regression coverage for the `enrich_planning_features` contracts exercised in this file.

**Exact signature**

```python
def _source_complete_contract() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    ParcelPlanningFeaturesResult,
]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[GpuPlanningDocument, gpd.GeoDataFrame, ParcelPlanningFeaturesResult]`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `planning_document, parcels, result`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_planning_features::test_public_normalized_input_contract_validates_step_7d_3_1_result` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_public_normalized_input_contract_validates_step_7d_3_1_result` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_public_normalized_input_contract_wraps_malformed_document_context` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_public_normalized_input_contract_wraps_malformed_document_context` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_binds_inspected_spatial_inventory` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_binds_inspected_spatial_inventory` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_public_source_validation_hashes_survive_parquet_readback` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_public_source_validation_hashes_survive_parquet_readback` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_public_normalized_input_contract_rejects_stripped_catalog` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_public_normalized_input_contract_rejects_stripped_catalog` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_unknown_relation_parcel` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_unknown_relation_parcel` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_coherent_parcel_metric_mutation` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_coherent_parcel_metric_mutation` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_noncanonical_relation_dtype` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_noncanonical_relation_dtype` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_relation_index_name_change` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_relation_index_name_change` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_relation_index_dtype_change` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_relation_index_dtype_change` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_relation_index_class_change` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_relation_index_class_change` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_expected_relation_hash_binds_dtype_and_index_metadata` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_expected_relation_hash_binds_dtype_and_index_metadata` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_accepts_complete_parcel_output_summaries` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_accepts_complete_parcel_output_summaries` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_partial_parcel_output_columns` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_partial_parcel_output_columns` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_corrupted_complete_parcel_summaries` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_corrupted_complete_parcel_summaries` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_noncanonical_parcel_summary_dtype` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_noncanonical_parcel_summary_dtype` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_each_corrupted_parcel_summary_fact` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_each_corrupted_parcel_summary_fact` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_duplicate_parcel_ids` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_duplicate_parcel_ids` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_invalid_parcel_geometry` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_invalid_parcel_geometry` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_accepts_epsg4326_parcels` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_accepts_epsg4326_parcels` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_document_reference_allows_one_archive_zip_suffix` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_document_reference_allows_one_archive_zip_suffix` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_coherently_renamed_feature_identity` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_coherently_renamed_feature_identity` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_independent_gpu_lineage_mutation` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_independent_gpu_lineage_mutation` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_binds_gpu_document_context` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_binds_gpu_document_context` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_reloads_and_compares_source_catalog` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_reloads_and_compares_source_catalog` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_catalog_for_absent_gpu_layer` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_catalog_for_absent_gpu_layer` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_three_dimensional_normalized_catalogs_are_rejected` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_three_dimensional_normalized_catalogs_are_rejected` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_two_dimensional_normalized_catalogs_remain_valid` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_two_dimensional_normalized_catalogs_remain_valid` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_tampered_gpkg_inventory_hash` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_tampered_gpkg_inventory_hash` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_tampered_gpkg_size` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_tampered_gpkg_size` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_changed_gpkg_bytes` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_changed_gpkg_bytes` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_same_size_gpkg_byte_tamper` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_same_size_gpkg_byte_tamper` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_coherently_changed_physical_gpkg` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_coherently_changed_physical_gpkg` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_changed_physical_gpkg_geometry` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_changed_physical_gpkg_geometry` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_loaded_source_attrs_not_on_disk` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_loaded_source_attrs_not_on_disk` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_dataset_outside_extraction_root` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_dataset_outside_extraction_root` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_linked_spatial_dataset` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_linked_spatial_dataset` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_batch_gpu_revalidation_rejects_malformed_layer_items` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_batch_gpu_revalidation_rejects_malformed_layer_items` via `_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_batch_gpu_revalidation_rejects_duplicate_logical_name` via `_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_batch_gpu_revalidation_rejects_duplicate_logical_name` via `_source_complete_contract`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_planning_features._parcels` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `_rectangle` | `tests.unit.test_enrich_planning_features._rectangle` |
| `LineString` | `shapely.geometry.LineString` |
| `Point` | `shapely.geometry.Point` |
| `_planning_document` | `tests.unit.test_enrich_planning_features._planning_document` |
| `intersect_parcels_with_gpu_planning_features` | `landscout.stages.enrich_planning_features.intersect_parcels_with_gpu_planning_features` |

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
def _source_complete_contract() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    ParcelPlanningFeaturesResult,
]:
    parcels = _parcels()
    layers = [
        _inspected(
            "prescription_surface",
            _source_frame(
                "prescription_surface",
                [_rectangle(0, 0, 10, 10)],
                ids=["SURFACE"],
                type_codes=["07"],
                subtype_codes=["04"],
            ),
        ),
        _inspected(
            "prescription_line",
            _source_frame(
                "prescription_line",
                [LineString([(-1, 5), (11, 5)])],
                ids=["LINE"],
                type_codes=["15"],
                subtype_codes=["00"],
            ),
        ),
        _inspected(
            "prescription_point",
            _source_frame(
                "prescription_point",
                [Point(5, 5)],
                ids=["POINT"],
                type_codes=["07"],
                subtype_codes=["00"],
            ),
        ),
    ]
    planning_document = _planning_document(layers)
    result = intersect_parcels_with_gpu_planning_features(parcels, planning_document)
    return planning_document, parcels, result
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_two_parcel_source_complete_contract`

**Purpose:** Build equal-area parcels so relation identity cannot hide behind area checks.

**Exact signature**

```python
def _two_parcel_source_complete_contract() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    ParcelPlanningFeaturesResult,
]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[GpuPlanningDocument, gpd.GeoDataFrame, ParcelPlanningFeaturesResult]`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `planning_document, parcels, result`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_same_area_wrong_parcel_relation` via `_two_parcel_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_same_area_wrong_parcel_relation` via `_two_parcel_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_missing_expected_relation` via `_two_parcel_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_missing_expected_relation` via `_two_parcel_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_extra_geometrically_false_relation` via `_two_parcel_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_extra_geometrically_false_relation` via `_two_parcel_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_reordered_relations` via `_two_parcel_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_reordered_relations` via `_two_parcel_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_coherent_but_wrong_line_metric` via `_two_parcel_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_coherent_but_wrong_line_metric` via `_two_parcel_source_complete_contract`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_planning_features._parcels` |
| `_rectangle` | `tests.unit.test_enrich_planning_features._rectangle` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `LineString` | `shapely.geometry.LineString` |
| `_planning_document` | `tests.unit.test_enrich_planning_features._planning_document` |
| `intersect_parcels_with_gpu_planning_features` | `landscout.stages.enrich_planning_features.intersect_parcels_with_gpu_planning_features` |

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
def _two_parcel_source_complete_contract() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    ParcelPlanningFeaturesResult,
]:
    """Build equal-area parcels so relation identity cannot hide behind area checks."""

    parcels = _parcels(
        [_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)],
        ids=["P-1", "P-2"],
    )
    layers = [
        _inspected(
            "prescription_surface",
            _source_frame(
                "prescription_surface",
                [_rectangle(0, 0, 10, 10)],
                ids=["SURFACE"],
                type_codes=["07"],
                subtype_codes=["04"],
            ),
        ),
        _inspected(
            "prescription_line",
            _source_frame(
                "prescription_line",
                [LineString([(0, 5), (10, 5)])],
                ids=["LINE"],
                type_codes=["15"],
                subtype_codes=["00"],
            ),
        ),
    ]
    planning_document = _planning_document(layers)
    result = intersect_parcels_with_gpu_planning_features(parcels, planning_document)
    return planning_document, parcels, result
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_validate_source_complete`

**Purpose:** Implements `validate source complete` within the file role: Provides complete unit and regression coverage for the `enrich_planning_features` contracts exercised in this file.

**Exact signature**

```python
def _validate_source_complete(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    result: ParcelPlanningFeaturesResult,
) -> PlanningFeatureInputValidation:
```

- Exact decorators: none.
- Declared return annotation: `PlanningFeatureInputValidation`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `result` | positional-or-keyword | `ParcelPlanningFeaturesResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `validate_normalized_planning_feature_inputs(<br>        planning_document,<br>        parcels,<br>        result.surface_features,<br>        result.line_features,<br>        result.point_features,<br>        result.relations,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_planning_features::test_public_normalized_input_contract_wraps_malformed_document_context` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_public_normalized_input_contract_wraps_malformed_document_context` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_binds_inspected_spatial_inventory` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_binds_inspected_spatial_inventory` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_public_source_validation_hashes_survive_parquet_readback` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_public_source_validation_hashes_survive_parquet_readback` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_unknown_relation_parcel` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_unknown_relation_parcel` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_coherent_parcel_metric_mutation` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_coherent_parcel_metric_mutation` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_same_area_wrong_parcel_relation` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_same_area_wrong_parcel_relation` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_missing_expected_relation` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_missing_expected_relation` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_extra_geometrically_false_relation` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_extra_geometrically_false_relation` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_reordered_relations` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_reordered_relations` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_noncanonical_relation_dtype` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_noncanonical_relation_dtype` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_relation_index_name_change` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_relation_index_name_change` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_relation_index_dtype_change` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_relation_index_dtype_change` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_coherent_but_wrong_line_metric` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_coherent_but_wrong_line_metric` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_accepts_complete_parcel_output_summaries` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_accepts_complete_parcel_output_summaries` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_partial_parcel_output_columns` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_partial_parcel_output_columns` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_corrupted_complete_parcel_summaries` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_corrupted_complete_parcel_summaries` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_noncanonical_parcel_summary_dtype` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_noncanonical_parcel_summary_dtype` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_each_corrupted_parcel_summary_fact` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_each_corrupted_parcel_summary_fact` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_duplicate_parcel_ids` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_duplicate_parcel_ids` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_invalid_parcel_geometry` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_invalid_parcel_geometry` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_accepts_epsg4326_parcels` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_accepts_epsg4326_parcels` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_document_reference_allows_one_archive_zip_suffix` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_document_reference_allows_one_archive_zip_suffix` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_coherently_renamed_feature_identity` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_coherently_renamed_feature_identity` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_independent_gpu_lineage_mutation` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_independent_gpu_lineage_mutation` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_binds_gpu_document_context` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_binds_gpu_document_context` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_reloads_and_compares_source_catalog` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_reloads_and_compares_source_catalog` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_catalog_for_absent_gpu_layer` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_catalog_for_absent_gpu_layer` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_three_dimensional_normalized_catalogs_are_rejected` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_three_dimensional_normalized_catalogs_are_rejected` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_two_dimensional_normalized_catalogs_remain_valid` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_two_dimensional_normalized_catalogs_remain_valid` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_tampered_gpkg_inventory_hash` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_tampered_gpkg_inventory_hash` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_tampered_gpkg_size` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_tampered_gpkg_size` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_changed_gpkg_bytes` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_changed_gpkg_bytes` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_same_size_gpkg_byte_tamper` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_same_size_gpkg_byte_tamper` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_coherently_changed_physical_gpkg` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_coherently_changed_physical_gpkg` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_changed_physical_gpkg_geometry` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_changed_physical_gpkg_geometry` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_reordered_physical_gpkg_rows` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_reordered_physical_gpkg_rows` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_loaded_source_attrs_not_on_disk` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_loaded_source_attrs_not_on_disk` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_dataset_outside_extraction_root` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_dataset_outside_extraction_root` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_linked_spatial_dataset` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_linked_spatial_dataset` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_binds_every_shapefile_sidecar` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_binds_every_shapefile_sidecar` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_changed_or_reordered_ogr_fids` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_changed_or_reordered_ogr_fids` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_requires_shapefile_core_members` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_requires_shapefile_core_members` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_changed_shapefile_sidecar_bytes` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_changed_shapefile_sidecar_bytes` via `_validate_source_complete`
- direct call: `tests.unit.test_enrich_planning_features::test_dotted_sibling_dataset_is_not_a_sidecar_and_makes_role_ambiguous` via `_validate_source_complete`
- value/type reference: `tests.unit.test_enrich_planning_features::test_dotted_sibling_dataset_is_not_a_sidecar_and_makes_role_ambiguous` via `_validate_source_complete`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `validate_normalized_planning_feature_inputs` | `landscout.stages.enrich_planning_features.validate_normalized_planning_feature_inputs` |

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
def _validate_source_complete(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    result: ParcelPlanningFeaturesResult,
) -> PlanningFeatureInputValidation:
    return validate_normalized_planning_feature_inputs(
        planning_document,
        parcels,
        result.surface_features,
        result.line_features,
        result.point_features,
        result.relations,
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_replace_related_layer`

**Purpose:** Implements `replace related layer` within the file role: Provides complete unit and regression coverage for the `enrich_planning_features` contracts exercised in this file.

**Exact signature**

```python
def _replace_related_layer(
    planning_document: GpuPlanningDocument,
    logical_name: str,
    frame: gpd.GeoDataFrame,
) -> GpuPlanningDocument:
```

- Exact decorators: none.
- Declared return annotation: `GpuPlanningDocument`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |
| `logical_name` | positional-or-keyword | `str` | `required` |
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `replace(planning_document, related_layers=tuple(related))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_reloads_and_compares_source_catalog` via `_replace_related_layer`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_reloads_and_compares_source_catalog` via `_replace_related_layer`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `related.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `_summary` | `tests.unit.test_enrich_planning_features._summary` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `related.append(layer)`<br>`related.append(<br>            replace(<br>                layer,<br>                data=frame,<br>                summary=_summary(frame, layer.reference.source_layer),<br>            )<br>        )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _replace_related_layer(
    planning_document: GpuPlanningDocument,
    logical_name: str,
    frame: gpd.GeoDataFrame,
) -> GpuPlanningDocument:
    related: list[GpuInspectedLayer] = []
    for layer in planning_document.related_layers:
        if layer.logical_name != logical_name:
            related.append(layer)
            continue
        related.append(
            replace(
                layer,
                data=frame,
                summary=_summary(frame, layer.reference.source_layer),
            )
        )
    return replace(planning_document, related_layers=tuple(related))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_without_related_layer`

**Purpose:** Implements `without related layer` within the file role: Provides complete unit and regression coverage for the `enrich_planning_features` contracts exercised in this file.

**Exact signature**

```python
def _without_related_layer(
    planning_document: GpuPlanningDocument,
    logical_name: str,
) -> GpuPlanningDocument:
```

- Exact decorators: none.
- Declared return annotation: `GpuPlanningDocument`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |
| `logical_name` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `replace(<br>        planning_document,<br>        related_layers=tuple(<br>            layer<br>            for layer in planning_document.related_layers<br>            if layer.logical_name != logical_name<br>        ),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_catalog_for_absent_gpu_layer` via `_without_related_layer`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_catalog_for_absent_gpu_layer` via `_without_related_layer`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `replace` | `dataclasses.replace` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _without_related_layer(
    planning_document: GpuPlanningDocument,
    logical_name: str,
) -> GpuPlanningDocument:
    return replace(
        planning_document,
        related_layers=tuple(
            layer
            for layer in planning_document.related_layers
            if layer.logical_name != logical_name
        ),
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_refresh_extraction_inventory`

**Purpose:** Implements `refresh extraction inventory` within the file role: Provides complete unit and regression coverage for the `enrich_planning_features` contracts exercised in this file.

**Exact signature**

```python
def _refresh_extraction_inventory(
    planning_document: GpuPlanningDocument,
) -> GpuPlanningDocument:
```

- Exact decorators: none.
- Declared return annotation: `GpuPlanningDocument`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `replace(<br>        planning_document,<br>        extraction=updated_extraction,<br>        all_spatial_layers=gpu_source_module.discover_gpu_spatial_layers(<br>            updated_extraction<br>        ),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_coherently_changed_physical_gpkg` via `_refresh_extraction_inventory`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_coherently_changed_physical_gpkg` via `_refresh_extraction_inventory`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_changed_physical_gpkg_geometry` via `_refresh_extraction_inventory`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_changed_physical_gpkg_geometry` via `_refresh_extraction_inventory`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_reordered_physical_gpkg_rows` via `_refresh_extraction_inventory`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_reordered_physical_gpkg_rows` via `_refresh_extraction_inventory`
- direct call: `tests.unit.test_enrich_planning_features::test_dotted_sibling_dataset_is_not_a_sidecar_and_makes_role_ambiguous` via `_refresh_extraction_inventory`
- value/type reference: `tests.unit.test_enrich_planning_features::test_dotted_sibling_dataset_is_not_a_sidecar_and_makes_role_ambiguous` via `_refresh_extraction_inventory`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_physical_inventory` | `tests.unit.test_enrich_planning_features._physical_inventory` |
| `_write_extraction_manifest` | `tests.unit.test_enrich_planning_features._write_extraction_manifest` |
| `replace` | `dataclasses.replace` |
| `gpu_source_module.discover_gpu_spatial_layers` | `landscout.sources.gpu_fr.discover_gpu_spatial_layers` |

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
def _refresh_extraction_inventory(
    planning_document: GpuPlanningDocument,
) -> GpuPlanningDocument:
    extraction = planning_document.extraction
    files = _physical_inventory(extraction.extraction_root)
    _write_extraction_manifest(
        extraction.extraction_root,
        extraction.archive.sha256,
        files,
    )
    updated_extraction = replace(extraction, files=files)
    return replace(
        planning_document,
        extraction=updated_extraction,
        all_spatial_layers=gpu_source_module.discover_gpu_spatial_layers(
            updated_extraction
        ),
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_replace_layer_reference`

**Purpose:** Implements `replace layer reference` within the file role: Provides complete unit and regression coverage for the `enrich_planning_features` contracts exercised in this file.

**Exact signature**

```python
def _replace_layer_reference(
    planning_document: GpuPlanningDocument,
    logical_name: str,
    reference: GpuSpatialLayerReference,
) -> GpuPlanningDocument:
```

- Exact decorators: none.
- Declared return annotation: `GpuPlanningDocument`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |
| `logical_name` | positional-or-keyword | `str` | `required` |
| `reference` | positional-or-keyword | `GpuSpatialLayerReference` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `replace(<br>        planning_document,<br>        related_layers=related,<br>        all_spatial_layers=spatial,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_dataset_outside_extraction_root` via `_replace_layer_reference`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_dataset_outside_extraction_root` via `_replace_layer_reference`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `next` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _replace_layer_reference(
    planning_document: GpuPlanningDocument,
    logical_name: str,
    reference: GpuSpatialLayerReference,
) -> GpuPlanningDocument:
    related = tuple(
        replace(layer, reference=reference)
        if layer.logical_name == logical_name
        else layer
        for layer in planning_document.related_layers
    )
    old_reference = next(
        layer.reference
        for layer in planning_document.related_layers
        if layer.logical_name == logical_name
    )
    spatial = tuple(
        reference if item == old_reference else item
        for item in planning_document.all_spatial_layers
    )
    return replace(
        planning_document,
        related_layers=related,
        all_spatial_layers=spatial,
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_public_normalized_input_contract_validates_step_7d_3_1_result`

**Purpose:** Regression invariant: public normalized input contract validates step 7d 3 1 result. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_public_normalized_input_contract_validates_step_7d_3_1_result() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert isinstance(validation, PlanningFeatureInputValidation)`
  - `assert validation.related_source_layer_count == 3`
  - `assert validation.related_source_file_count == 3`
  - `assert validation.expected_relation_count == len(result.relations)`
  - `assert len(value) == 64`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `validate_normalized_planning_feature_inputs` | `landscout.stages.enrich_planning_features.validate_normalized_planning_feature_inputs` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_public_normalized_input_contract_validates_step_7d_3_1_result() -> None:
    planning_document, parcels, result = _source_complete_contract()
    validation = validate_normalized_planning_feature_inputs(
        planning_document,
        parcels,
        result.surface_features,
        result.line_features,
        result.point_features,
        result.relations,
    )
    assert isinstance(validation, PlanningFeatureInputValidation)
    assert validation.related_source_layer_count == 3
    assert validation.related_source_file_count == 3
    assert validation.expected_relation_count == len(result.relations)
    for value in (
        validation.gpu_related_source_files_sha256,
        validation.expected_relations_content_sha256,
    ):
        assert len(value) == 64
        int(value, 16)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_public_normalized_input_contract_wraps_malformed_document_context`

**Purpose:** Regression invariant: public normalized input contract wraps malformed document context. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_public_normalized_input_contract_wraps_malformed_document_context() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError)`
- Exact assertions:
  - `assert isinstance(caught.value.__cause__, (AttributeError, TypeError))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_public_normalized_input_contract_wraps_malformed_document_context() -> None:
    planning_document, parcels, result = _source_complete_contract()
    malformed = replace(planning_document, related_layers=(None,))  # type: ignore[arg-type]
    with pytest.raises(PlanningFeaturesError) as caught:
        _validate_source_complete(malformed, parcels, result)
    assert isinstance(caught.value.__cause__, (AttributeError, TypeError))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_binds_inspected_spatial_inventory`

**Purpose:** Regression invariant: source complete contract binds inspected spatial inventory. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_binds_inspected_spatial_inventory() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="inventory\|reference")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

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
def test_source_complete_contract_binds_inspected_spatial_inventory() -> None:
    planning_document, parcels, result = _source_complete_contract()
    missing_inventory = replace(planning_document, all_spatial_layers=())
    with pytest.raises(PlanningFeaturesError, match="inventory|reference"):
        _validate_source_complete(missing_inventory, parcels, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_public_normalized_input_contract_is_exported`

**Purpose:** Regression invariant: public normalized input contract is exported. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_public_normalized_input_contract_is_exported() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert (<br>        stages.validate_normalized_planning_feature_inputs<br>        is validate_normalized_planning_feature_inputs<br>    )`
  - `assert "validate_normalized_planning_feature_inputs" in stages.__all__`
  - `assert stages.PlanningFeatureInputValidation is PlanningFeatureInputValidation`
  - `assert "PlanningFeatureInputValidation" in stages.__all__`

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
def test_public_normalized_input_contract_is_exported() -> None:
    from landscout import stages

    assert (
        stages.validate_normalized_planning_feature_inputs
        is validate_normalized_planning_feature_inputs
    )
    assert "validate_normalized_planning_feature_inputs" in stages.__all__
    assert stages.PlanningFeatureInputValidation is PlanningFeatureInputValidation
    assert "PlanningFeatureInputValidation" in stages.__all__
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_public_source_validation_hashes_survive_parquet_readback`

**Purpose:** Regression invariant: public source validation hashes survive parquet readback. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_public_source_validation_hashes_survive_parquet_readback(
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
- Exact assertions:
  - `assert validation == original`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |
| `result.surface_features.to_parquet` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.line_features.to_parquet` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.point_features.to_parquet` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.relations.to_parquet` | `unresolved local/third-party receiver; no ownership inferred` |
| `validate_normalized_planning_feature_inputs` | `landscout.stages.enrich_planning_features.validate_normalized_planning_feature_inputs` |
| `gpd.read_parquet` | `geopandas.read_parquet` |
| `pd.read_parquet` | `pandas.read_parquet` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `gpd.read_parquet`<br>`pd.read_parquet` |
| Filesystem/archive write or publication | `result.surface_features.to_parquet`<br>`result.line_features.to_parquet`<br>`result.point_features.to_parquet`<br>`result.relations.to_parquet` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_public_source_validation_hashes_survive_parquet_readback(
    tmp_path: Path,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    original = _validate_source_complete(planning_document, parcels, result)
    paths = {
        "surface_features": tmp_path / "surface.parquet",
        "line_features": tmp_path / "line.parquet",
        "point_features": tmp_path / "point.parquet",
        "relations": tmp_path / "relations.parquet",
    }
    result.surface_features.to_parquet(paths["surface_features"], index=False)
    result.line_features.to_parquet(paths["line_features"], index=False)
    result.point_features.to_parquet(paths["point_features"], index=False)
    result.relations.to_parquet(paths["relations"], index=False)
    validation = validate_normalized_planning_feature_inputs(
        planning_document,
        parcels,
        gpd.read_parquet(paths["surface_features"]),
        gpd.read_parquet(paths["line_features"]),
        gpd.read_parquet(paths["point_features"]),
        pd.read_parquet(paths["relations"]),
    )
    assert validation == original
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_public_normalized_input_contract_rejects_stripped_catalog`

**Purpose:** Regression invariant: public normalized input contract rejects stripped catalog. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_public_normalized_input_contract_rejects_stripped_catalog() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="schema\|label_raw")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `result.surface_features.drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `validate_normalized_planning_feature_inputs` | `landscout.stages.enrich_planning_features.validate_normalized_planning_feature_inputs` |

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
| In-memory mutation | `result.surface_features.drop(columns="label_raw")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_public_normalized_input_contract_rejects_stripped_catalog() -> None:
    planning_document, parcels, result = _source_complete_contract()
    surface = result.surface_features.drop(columns="label_raw")
    with pytest.raises(PlanningFeaturesError, match="schema|label_raw"):
        validate_normalized_planning_feature_inputs(
            planning_document,
            parcels,
            surface,
            result.line_features,
            result.point_features,
            result.relations,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_empty_and_nonempty_catalogs_have_identical_kind_schemas`

**Purpose:** Regression invariant: empty and nonempty catalogs have identical kind schemas. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_empty_and_nonempty_catalogs_have_identical_kind_schemas() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert list(empty_catalog.columns) == list(populated_catalog.columns)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_contract_result` | `tests.unit.test_enrich_planning_features._contract_result` |
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `zip` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_empty_and_nonempty_catalogs_have_identical_kind_schemas() -> None:
    _, _, populated = _contract_result()
    empty = _run([])
    for populated_catalog, empty_catalog in zip(
        (
            populated.surface_features,
            populated.line_features,
            populated.point_features,
        ),
        (empty.surface_features, empty.line_features, empty.point_features),
        strict=True,
    ):
        assert list(empty_catalog.columns) == list(populated_catalog.columns)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_strict_relation_integer_counts_are_enforced`

**Purpose:** Regression invariant: strict relation integer counts are enforced. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_strict_relation_integer_counts_are_enforced(bad_count: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize("bad_count", [-1, 1.5, float("inf"), "2", True])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `bad_count` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        PlanningFeaturesError, match="integer count\|non-negative\|dtype\|schema"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_contract_result` | `tests.unit.test_enrich_planning_features._contract_result` |
| `result.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations["point_member_count"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate_result` | `landscout.stages.enrich_planning_features._validate_result` |
| `replace` | `dataclasses.replace` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `relations["point_member_count"] = relations["point_member_count"].astype(object)`<br>`relations.loc[point_index, "point_member_count"] = bad_count` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_strict_relation_integer_counts_are_enforced(bad_count: object) -> None:
    planning_document, source, result = _contract_result()
    relations = result.relations.copy(deep=True)
    relations["point_member_count"] = relations["point_member_count"].astype(object)
    point_index = relations.index[relations["geometry_kind"] == "POINT"][0]
    relations.loc[point_index, "point_member_count"] = bad_count
    with pytest.raises(
        PlanningFeaturesError, match="integer count|non-negative|dtype|schema"
    ):
        _validate_result(
            source,
            replace(result, relations=relations),
            planning_document=planning_document,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_strict_parcel_summary_integer_counts_are_enforced`

**Purpose:** Regression invariant: strict parcel summary integer counts are enforced. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_strict_parcel_summary_integer_counts_are_enforced(
    bad_count: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("bad_count", [-1, 1.5, float("inf"), "2", True])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `bad_count` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="integer count\|non-negative")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_contract_result` | `tests.unit.test_enrich_planning_features._contract_result` |
| `result.parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels[<br>        "planning_line_relation_count"<br>    ].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate_result` | `landscout.stages.enrich_planning_features._validate_result` |
| `replace` | `dataclasses.replace` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `parcels["planning_line_relation_count"] = parcels[<br>        "planning_line_relation_count"<br>    ].astype(object)`<br>`parcels.loc[parcels.index[0], "planning_line_relation_count"] = bad_count` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_strict_parcel_summary_integer_counts_are_enforced(
    bad_count: object,
) -> None:
    planning_document, source, result = _contract_result()
    parcels = result.parcels.copy(deep=True)
    parcels["planning_line_relation_count"] = parcels[
        "planning_line_relation_count"
    ].astype(object)
    parcels.loc[parcels.index[0], "planning_line_relation_count"] = bad_count
    with pytest.raises(PlanningFeaturesError, match="integer count|non-negative"):
        _validate_result(
            source,
            replace(result, parcels=parcels),
            planning_document=planning_document,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_corrupted_relation_semantics_are_rejected`

**Purpose:** Regression invariant: corrupted relation semantics are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_corrupted_relation_semantics_are_rejected(
    kind: str,
    column: str,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("kind", "column", "value"),
    [
        ("SURFACE", "relation_type", "TOUCH_ONLY"),
        ("SURFACE", "parcel_share_pct", 42.0),
        ("SURFACE", "intersection_area_m2", None),
        ("SURFACE", "source_line_length_m", 0.0),
        ("LINE", "relation_type", "TOUCH_ONLY"),
        ("LINE", "intersection_length_m", 999.0),
        ("POINT", "relation_type", "BOUNDARY_TOUCH"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `kind` | positional-or-keyword | `str` | `required` |
| `column` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_contract_result` | `tests.unit.test_enrich_planning_features._contract_result` |
| `result.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations[column].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate_result` | `landscout.stages.enrich_planning_features._validate_result` |
| `replace` | `dataclasses.replace` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
| In-memory mutation | `relations[column] = relations[column].astype(object)`<br>`relations.loc[index, column] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_corrupted_relation_semantics_are_rejected(
    kind: str,
    column: str,
    value: object,
) -> None:
    planning_document, source, result = _contract_result()
    relations = result.relations.copy(deep=True)
    index = relations.index[relations["geometry_kind"] == kind][0]
    relations[column] = relations[column].astype(object)
    relations.loc[index, column] = value
    with pytest.raises(PlanningFeaturesError):
        _validate_result(
            source,
            replace(result, relations=relations),
            planning_document=planning_document,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_point_member_relation_semantics_are_exact`

**Purpose:** Regression invariant: point member relation semantics are exact. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_point_member_relation_semantics_are_exact() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="relation type")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_contract_result` | `tests.unit.test_enrich_planning_features._contract_result` |
| `result.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate_result` | `landscout.stages.enrich_planning_features._validate_result` |
| `replace` | `dataclasses.replace` |

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
| In-memory mutation | `relations.loc[index, "point_members_inside_count"] = 0`<br>`relations.loc[index, "point_members_boundary_count"] = 1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_point_member_relation_semantics_are_exact() -> None:
    planning_document, source, result = _contract_result()
    relations = result.relations.copy(deep=True)
    index = relations.index[relations["geometry_kind"] == "POINT"][0]
    relations.loc[index, "point_members_inside_count"] = 0
    relations.loc[index, "point_members_boundary_count"] = 1
    with pytest.raises(PlanningFeaturesError, match="relation type"):
        _validate_result(
            source,
            replace(result, relations=relations),
            planning_document=planning_document,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_shared_intrinsic_relation_semantics_reject_every_invalid_case`

**Purpose:** Regression invariant: shared intrinsic relation semantics reject every invalid case. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_shared_intrinsic_relation_semantics_reject_every_invalid_case(
    case: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "case",
    [
        "surface-inside",
        "line-area",
        "point-touch",
        "area-zero",
        "surface-touch-positive",
        "length-zero",
        "line-touch-positive",
        "inside-zero",
        "boundary-with-inside",
        "area-exceeds-feature",
        "share-inconsistent",
        "non-finite",
        "negative",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `case` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises((TypeError, ValueError))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_contract_result` | `tests.unit.test_enrich_planning_features._contract_result` |
| `result.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations["geometry_kind"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `validate_intrinsic_planning_feature_relations` | `landscout.common.planning_feature_contract.validate_intrinsic_planning_feature_relations` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `relations["geometry_kind"].eq` |
| External process/environment | None directly present. |
| In-memory mutation | `relations.loc[surface, "relation_type"] = "INSIDE"`<br>`relations.loc[line, "relation_type"] = "AREA_OVERLAP"`<br>`relations.loc[point, "relation_type"] = "TOUCH_ONLY"`<br>`relations.loc[<br>            surface, ["intersection_area_m2", "parcel_share_pct", "feature_share_pct"]<br>        ] = 0.0`<br>`relations.loc[surface, "relation_type"] = "TOUCH_ONLY"`<br>`relations.loc[line, "intersection_length_m"] = 0.0`<br>`relations.loc[line, "relation_type"] = "TOUCH_ONLY"`<br>`relations.loc[point, "point_members_inside_count"] = 0`<br>`relations.loc[point, "relation_type"] = "BOUNDARY_TOUCH"`<br>`relations.loc[point, "point_members_boundary_count"] = 1`<br>`relations.loc[surface, "intersection_area_m2"] = (<br>            float(relations.loc[surface, "feature_area_m2"]) + 1.0<br>        )`<br>`relations.loc[surface, "parcel_share_pct"] = 42.0`<br>`relations.loc[surface, "feature_share_pct"] = float("inf")`<br>`relations.loc[surface, "intersection_area_m2"] = -1.0` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_shared_intrinsic_relation_semantics_reject_every_invalid_case(
    case: str,
) -> None:
    _, _, result = _contract_result()
    relations = result.relations.copy(deep=True)
    surface = relations.index[relations["geometry_kind"].eq("SURFACE")][0]
    line = relations.index[relations["geometry_kind"].eq("LINE")][0]
    point = relations.index[relations["geometry_kind"].eq("POINT")][0]
    if case == "surface-inside":
        relations.loc[surface, "relation_type"] = "INSIDE"
    elif case == "line-area":
        relations.loc[line, "relation_type"] = "AREA_OVERLAP"
    elif case == "point-touch":
        relations.loc[point, "relation_type"] = "TOUCH_ONLY"
    elif case == "area-zero":
        relations.loc[
            surface, ["intersection_area_m2", "parcel_share_pct", "feature_share_pct"]
        ] = 0.0
    elif case == "surface-touch-positive":
        relations.loc[surface, "relation_type"] = "TOUCH_ONLY"
    elif case == "length-zero":
        relations.loc[line, "intersection_length_m"] = 0.0
    elif case == "line-touch-positive":
        relations.loc[line, "relation_type"] = "TOUCH_ONLY"
    elif case == "inside-zero":
        relations.loc[point, "point_members_inside_count"] = 0
    elif case == "boundary-with-inside":
        relations.loc[point, "relation_type"] = "BOUNDARY_TOUCH"
        relations.loc[point, "point_members_boundary_count"] = 1
    elif case == "area-exceeds-feature":
        relations.loc[surface, "intersection_area_m2"] = (
            float(relations.loc[surface, "feature_area_m2"]) + 1.0
        )
    elif case == "share-inconsistent":
        relations.loc[surface, "parcel_share_pct"] = 42.0
    elif case == "non-finite":
        relations.loc[surface, "feature_share_pct"] = float("inf")
    else:
        relations.loc[surface, "intersection_area_m2"] = -1.0
    with pytest.raises((TypeError, ValueError)):
        validate_intrinsic_planning_feature_relations(relations)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_relation_must_match_feature_catalog`

**Purpose:** Regression invariant: relation must match feature catalog. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_relation_must_match_feature_catalog(
    column: str,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("column", "value"),
    [
        ("source_identity_kind", "NOT_A_KIND"),
        ("source_identity_field", "WRONG_FIELD"),
        ("feature_family", "INFORMATION"),
        ("geometry_kind", "LINE"),
        ("type_code_raw", "MUTATED"),
        ("source_archive_sha256", "b" * 64),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `column` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        PlanningFeaturesError,<br>        match="catalog\|geometry kind\|LINE relation\|unrelated metric",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_contract_result` | `tests.unit.test_enrich_planning_features._contract_result` |
| `result.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations["geometry_kind"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate_result` | `landscout.stages.enrich_planning_features._validate_result` |
| `replace` | `dataclasses.replace` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `relations["geometry_kind"].eq` |
| External process/environment | None directly present. |
| In-memory mutation | `relations.loc[index, column] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_relation_must_match_feature_catalog(
    column: str,
    value: object,
) -> None:
    planning_document, source, result = _contract_result()
    relations = result.relations.copy(deep=True)
    index = relations.index[0]
    if column == "geometry_kind":
        index = relations.index[relations["geometry_kind"].eq("SURFACE")][0]
    relations.loc[index, column] = value
    with pytest.raises(
        PlanningFeaturesError,
        match="catalog|geometry kind|LINE relation|unrelated metric",
    ):
        _validate_result(
            source,
            replace(result, relations=relations),
            planning_document=planning_document,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_feature_ids_are_globally_unique_across_catalogs`

**Purpose:** Regression invariant: feature ids are globally unique across catalogs. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_feature_ids_are_globally_unique_across_catalogs() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="globally unique\|deterministic")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_contract_result` | `tests.unit.test_enrich_planning_features._contract_result` |
| `result.point_features.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate_result` | `landscout.stages.enrich_planning_features._validate_result` |
| `replace` | `dataclasses.replace` |

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
| In-memory mutation | `points.loc[points.index[0], "planning_feature_id"] = result.surface_features.iloc[<br>        0<br>    ]["planning_feature_id"]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_feature_ids_are_globally_unique_across_catalogs() -> None:
    planning_document, source, result = _contract_result()
    points = result.point_features.copy(deep=True)
    points.loc[points.index[0], "planning_feature_id"] = result.surface_features.iloc[
        0
    ]["planning_feature_id"]
    with pytest.raises(PlanningFeaturesError, match="globally unique|deterministic"):
        _validate_result(
            source,
            replace(result, point_features=points),
            planning_document=planning_document,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_same_source_id_is_allowed_in_distinct_logical_layers`

**Purpose:** Regression invariant: same source id is allowed in distinct logical layers. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_same_source_id_is_allowed_in_distinct_logical_layers() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert len(result.relations) == 2`
  - `assert result.relations["planning_feature_id"].nunique() == 2`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `LineString` | `shapely.geometry.LineString` |
| `Point` | `shapely.geometry.Point` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.relations["planning_feature_id"].nunique` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_same_source_id_is_allowed_in_distinct_logical_layers() -> None:
    result = _run(
        [
            _inspected(
                "prescription_line",
                _source_frame(
                    "prescription_line",
                    [LineString([(0, 2), (10, 2)])],
                    ids=["SHARED"],
                ),
            ),
            _inspected(
                "prescription_point",
                _source_frame("prescription_point", [Point(5, 5)], ids=["SHARED"]),
            ),
        ]
    )
    assert len(result.relations) == 2
    assert result.relations["planning_feature_id"].nunique() == 2
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_corrupted_parcel_summary_is_rejected`

**Purpose:** Regression invariant: corrupted parcel summary is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_corrupted_parcel_summary_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="inconsistent with relations")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_contract_result` | `tests.unit.test_enrich_planning_features._contract_result` |
| `result.parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate_result` | `landscout.stages.enrich_planning_features._validate_result` |
| `replace` | `dataclasses.replace` |

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
| In-memory mutation | `parcels.loc[parcels.index[0], "planning_surface_relation_count"] += 1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_corrupted_parcel_summary_is_rejected() -> None:
    planning_document, source, result = _contract_result()
    parcels = result.parcels.copy(deep=True)
    parcels.loc[parcels.index[0], "planning_surface_relation_count"] += 1
    with pytest.raises(PlanningFeaturesError, match="inconsistent with relations"):
        _validate_result(
            source,
            replace(result, parcels=parcels),
            planning_document=planning_document,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_corrupted_surface_union_contract_is_rejected`

**Purpose:** Regression invariant: corrupted surface union contract is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_corrupted_surface_union_contract_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="union")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_contract_result` | `tests.unit.test_enrich_planning_features._contract_result` |
| `result.parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate_result` | `landscout.stages.enrich_planning_features._validate_result` |
| `replace` | `dataclasses.replace` |

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
| In-memory mutation | `parcels.loc[parcels.index[0], "planning_surface_covered_union_area_m2"] = 1000.0` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_corrupted_surface_union_contract_is_rejected() -> None:
    planning_document, source, result = _contract_result()
    parcels = result.parcels.copy(deep=True)
    parcels.loc[parcels.index[0], "planning_surface_covered_union_area_m2"] = 1000.0
    with pytest.raises(PlanningFeaturesError, match="union"):
        _validate_result(
            source,
            replace(result, parcels=parcels),
            planning_document=planning_document,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_geospatial_operation_failure_is_controlled_and_chained`

**Purpose:** Regression invariant: geospatial operation failure is controlled and chained. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_geospatial_operation_failure_is_controlled_and_chained(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="spatial join")`
- Exact assertions:
  - `assert isinstance(caught.value.__cause__, RuntimeError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `LineString` | `shapely.geometry.LineString` |
| `pytest.raises` | `pytest.raises` |
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_geospatial_operation_failure_is_controlled_and_chained(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fail_join(*args: object, **kwargs: object) -> object:
        raise RuntimeError("synthetic spatial-index failure")

    monkeypatch.setattr(planning_features_module.gpd, "sjoin", fail_join)
    layer = _inspected(
        "prescription_line",
        _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]),
    )
    with pytest.raises(PlanningFeaturesError, match="spatial join") as caught:
        _run([layer])
    assert isinstance(caught.value.__cause__, RuntimeError)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_geospatial_operation_failure_is_controlled_and_chained.fail_join`

**Purpose:** Implements `fail join` within the file role: Provides complete unit and regression coverage for the `enrich_planning_features` contracts exercised in this file.

**Exact signature**

```python
def fail_join(*args: object, **kwargs: object) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `RuntimeError("synthetic spatial-index failure")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `RuntimeError` | `unresolved local/third-party receiver; no ownership inferred` |

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
def fail_join(*args: object, **kwargs: object) -> object:
        raise RuntimeError("synthetic spatial-index failure")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_unknown_relation_parcel`

**Purpose:** Regression invariant: source complete contract rejects unknown relation parcel. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_unknown_relation_parcel() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="parcel\|source")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `result.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

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
| In-memory mutation | `relations.loc[relations.index[0], "parcel_id"] = "NOT-A-SOURCE-PARCEL"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_contract_rejects_unknown_relation_parcel() -> None:
    planning_document, parcels, result = _source_complete_contract()
    relations = result.relations.copy(deep=True)
    relations.loc[relations.index[0], "parcel_id"] = "NOT-A-SOURCE-PARCEL"
    corrupted = replace(result, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="parcel|source"):
        _validate_source_complete(planning_document, parcels, corrupted)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_coherent_parcel_metric_mutation`

**Purpose:** Regression invariant: source complete contract rejects coherent parcel metric mutation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_coherent_parcel_metric_mutation() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="parcel\|metric\|source")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `result.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations["geometry_kind"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `relations["geometry_kind"].eq` |
| External process/environment | None directly present. |
| In-memory mutation | `relations.loc[surface_mask, "parcel_metric_area_m2"] = 200.0`<br>`relations.loc[surface_mask, "parcel_share_pct"] = 50.0` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_contract_rejects_coherent_parcel_metric_mutation() -> None:
    planning_document, parcels, result = _source_complete_contract()
    relations = result.relations.copy(deep=True)
    surface_mask = relations["geometry_kind"].eq("SURFACE")
    relations.loc[surface_mask, "parcel_metric_area_m2"] = 200.0
    relations.loc[surface_mask, "parcel_share_pct"] = 50.0
    corrupted = replace(result, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="parcel|metric|source"):
        _validate_source_complete(planning_document, parcels, corrupted)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_same_area_wrong_parcel_relation`

**Purpose:** Regression invariant: source complete contract rejects same area wrong parcel relation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_same_area_wrong_parcel_relation() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="relation\|parcel\|rebuilt\|source")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_two_parcel_source_complete_contract` | `tests.unit.test_enrich_planning_features._two_parcel_source_complete_contract` |
| `result.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

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
| In-memory mutation | `relations.loc[relations.index[0], "parcel_id"] = "P-2"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_contract_rejects_same_area_wrong_parcel_relation() -> None:
    planning_document, parcels, result = _two_parcel_source_complete_contract()
    relations = result.relations.copy(deep=True)
    relations.loc[relations.index[0], "parcel_id"] = "P-2"
    corrupted = replace(result, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="relation|parcel|rebuilt|source"):
        _validate_source_complete(planning_document, parcels, corrupted)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_missing_expected_relation`

**Purpose:** Regression invariant: source complete contract rejects missing expected relation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_missing_expected_relation() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="relation\|rebuilt\|source")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_two_parcel_source_complete_contract` | `tests.unit.test_enrich_planning_features._two_parcel_source_complete_contract` |
| `replace` | `dataclasses.replace` |
| `result.relations.iloc[1:].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

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
def test_source_complete_contract_rejects_missing_expected_relation() -> None:
    planning_document, parcels, result = _two_parcel_source_complete_contract()
    corrupted = replace(result, relations=result.relations.iloc[1:].copy())
    with pytest.raises(PlanningFeaturesError, match="relation|rebuilt|source"):
        _validate_source_complete(planning_document, parcels, corrupted)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_extra_geometrically_false_relation`

**Purpose:** Regression invariant: source complete contract rejects extra geometrically false relation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_extra_geometrically_false_relation() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="relation\|rebuilt\|source")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_two_parcel_source_complete_contract` | `tests.unit.test_enrich_planning_features._two_parcel_source_complete_contract` |
| `result.relations.iloc[[0]].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.concat` | `pandas.concat` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

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
| In-memory mutation | `extra.loc[extra.index[0], "parcel_id"] = "P-2"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_contract_rejects_extra_geometrically_false_relation() -> None:
    planning_document, parcels, result = _two_parcel_source_complete_contract()
    extra = result.relations.iloc[[0]].copy(deep=True)
    extra.loc[extra.index[0], "parcel_id"] = "P-2"
    relations = pd.concat([result.relations, extra], ignore_index=True)
    corrupted = replace(result, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="relation|rebuilt|source"):
        _validate_source_complete(planning_document, parcels, corrupted)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_reordered_relations`

**Purpose:** Regression invariant: source complete contract rejects reordered relations. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_reordered_relations() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="relation\|order\|rebuilt")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_two_parcel_source_complete_contract` | `tests.unit.test_enrich_planning_features._two_parcel_source_complete_contract` |
| `result.relations.iloc[::-1].reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

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
def test_source_complete_contract_rejects_reordered_relations() -> None:
    planning_document, parcels, result = _two_parcel_source_complete_contract()
    relations = result.relations.iloc[::-1].reset_index(drop=True)
    corrupted = replace(result, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="relation|order|rebuilt"):
        _validate_source_complete(planning_document, parcels, corrupted)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_noncanonical_relation_dtype`

**Purpose:** Regression invariant: source complete contract rejects noncanonical relation dtype. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_noncanonical_relation_dtype(
    column: str,
    dtype: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("column", "dtype"),
    [
        ("intersection_area_m2", "object"),
        ("point_member_count", "object"),
        ("relation_type", "category"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `column` | positional-or-keyword | `str` | `required` |
| `dtype` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="schema\|dtype\|relation")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `result.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations[column].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |
| `replace` | `dataclasses.replace` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
| In-memory mutation | `relations[column] = relations[column].astype(dtype)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_contract_rejects_noncanonical_relation_dtype(
    column: str,
    dtype: str,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    relations = result.relations.copy(deep=True)
    relations[column] = relations[column].astype(dtype)
    with pytest.raises(PlanningFeaturesError, match="schema|dtype|relation"):
        _validate_source_complete(
            planning_document, parcels, replace(result, relations=relations)
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_relation_index_name_change`

**Purpose:** Regression invariant: source complete contract rejects relation index name change. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_relation_index_name_change() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="schema\|index\|relation")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `result.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations.index.rename` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |
| `replace` | `dataclasses.replace` |

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
| In-memory mutation | `relations.index = relations.index.rename("changed_relation_row")`<br>`relations.index.rename("changed_relation_row")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_contract_rejects_relation_index_name_change() -> None:
    planning_document, parcels, result = _source_complete_contract()
    relations = result.relations.copy(deep=True)
    relations.index = relations.index.rename("changed_relation_row")
    with pytest.raises(PlanningFeaturesError, match="schema|index|relation"):
        _validate_source_complete(
            planning_document, parcels, replace(result, relations=relations)
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_relation_index_dtype_change`

**Purpose:** Regression invariant: source complete contract rejects relation index dtype change. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_relation_index_dtype_change() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="schema\|index\|relation")`
- Exact assertions:
  - `assert str(relations.index.dtype) == "int32"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `result.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.Index` | `pandas.Index` |
| `np.asarray` | `numpy.asarray` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |
| `replace` | `dataclasses.replace` |

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
| In-memory mutation | `relations.index = pd.Index(<br>        np.asarray(relations.index, dtype="int32"),<br>        name=relations.index.name,<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_contract_rejects_relation_index_dtype_change() -> None:
    planning_document, parcels, result = _source_complete_contract()
    relations = result.relations.copy(deep=True)
    relations.index = pd.Index(
        np.asarray(relations.index, dtype="int32"),
        name=relations.index.name,
    )
    assert str(relations.index.dtype) == "int32"
    with pytest.raises(PlanningFeaturesError, match="schema|index|relation"):
        _validate_source_complete(
            planning_document, parcels, replace(result, relations=relations)
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_relation_index_class_change`

**Purpose:** Regression invariant: source complete contract rejects relation index class change. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_relation_index_class_change() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="schema\|index\|relation")`
- Exact assertions:
  - `assert type(result.relations.index) is pd.RangeIndex`
  - `assert type(relations.index) is pd.Index`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.Index` | `pandas.Index` |
| `relations.index.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `validate_normalized_planning_feature_inputs` | `landscout.stages.enrich_planning_features.validate_normalized_planning_feature_inputs` |

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
| In-memory mutation | `relations.index = pd.Index(relations.index.to_numpy(), dtype="int64")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_contract_rejects_relation_index_class_change() -> None:
    planning_document, parcels, result = _source_complete_contract()
    assert type(result.relations.index) is pd.RangeIndex
    relations = result.relations.copy(deep=True)
    relations.index = pd.Index(relations.index.to_numpy(), dtype="int64")
    assert type(relations.index) is pd.Index
    with pytest.raises(PlanningFeaturesError, match="schema|index|relation"):
        validate_normalized_planning_feature_inputs(
            planning_document,
            parcels,
            result.surface_features,
            result.line_features,
            result.point_features,
            relations,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_expected_relation_hash_binds_dtype_and_index_metadata`

**Purpose:** Regression invariant: expected relation hash binds dtype and index metadata. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_expected_relation_hash_binds_dtype_and_index_metadata() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert original != planning_features_module._expected_relations_content_sha256(<br>        object_dtype<br>    )`
  - `assert original != planning_features_module._expected_relations_content_sha256(<br>        named_index<br>    )`
  - `assert original != planning_features_module._expected_relations_content_sha256(<br>        int32_index<br>    )`
  - `assert original != planning_features_module._expected_relations_content_sha256(<br>        index_class<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `planning_features_module._expected_relations_content_sha256` | `landscout.stages.enrich_planning_features._expected_relations_content_sha256` |
| `result.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `object_dtype["intersection_area_m2"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `named_index.index.rename` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.Index` | `pandas.Index` |
| `np.asarray` | `numpy.asarray` |
| `index_class.index.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `planning_features_module._expected_relations_content_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `object_dtype["intersection_area_m2"] = object_dtype["intersection_area_m2"].astype(<br>        "object"<br>    )`<br>`named_index.index = named_index.index.rename("relation_row")`<br>`named_index.index.rename("relation_row")`<br>`int32_index.index = pd.Index(<br>        np.asarray(int32_index.index, dtype="int32"),<br>        name=int32_index.index.name,<br>    )`<br>`index_class.index = pd.Index(index_class.index.to_numpy(), dtype="int64")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_expected_relation_hash_binds_dtype_and_index_metadata() -> None:
    _, _, result = _source_complete_contract()
    original = planning_features_module._expected_relations_content_sha256(
        result.relations
    )
    object_dtype = result.relations.copy(deep=True)
    object_dtype["intersection_area_m2"] = object_dtype["intersection_area_m2"].astype(
        "object"
    )
    named_index = result.relations.copy(deep=True)
    named_index.index = named_index.index.rename("relation_row")
    int32_index = result.relations.copy(deep=True)
    int32_index.index = pd.Index(
        np.asarray(int32_index.index, dtype="int32"),
        name=int32_index.index.name,
    )
    index_class = result.relations.copy(deep=True)
    index_class.index = pd.Index(index_class.index.to_numpy(), dtype="int64")
    assert original != planning_features_module._expected_relations_content_sha256(
        object_dtype
    )
    assert original != planning_features_module._expected_relations_content_sha256(
        named_index
    )
    assert original != planning_features_module._expected_relations_content_sha256(
        int32_index
    )
    assert original != planning_features_module._expected_relations_content_sha256(
        index_class
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_coherent_but_wrong_line_metric`

**Purpose:** Regression invariant: source complete contract rejects coherent but wrong line metric. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_coherent_but_wrong_line_metric() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="relation\|metric\|rebuilt")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_two_parcel_source_complete_contract` | `tests.unit.test_enrich_planning_features._two_parcel_source_complete_contract` |
| `result.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations["geometry_kind"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `relations["geometry_kind"].eq` |
| External process/environment | None directly present. |
| In-memory mutation | `relations.loc[line_mask, "intersection_length_m"] = 5.0` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_contract_rejects_coherent_but_wrong_line_metric() -> None:
    planning_document, parcels, result = _two_parcel_source_complete_contract()
    relations = result.relations.copy(deep=True)
    line_mask = relations["geometry_kind"].eq("LINE")
    relations.loc[line_mask, "intersection_length_m"] = 5.0
    corrupted = replace(result, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="relation|metric|rebuilt"):
        _validate_source_complete(planning_document, parcels, corrupted)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_accepts_complete_parcel_output_summaries`

**Purpose:** Regression invariant: source complete contract accepts complete parcel output summaries. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_accepts_complete_parcel_output_summaries() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

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
def test_source_complete_contract_accepts_complete_parcel_output_summaries() -> None:
    planning_document, _, result = _source_complete_contract()
    _validate_source_complete(planning_document, result.parcels, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_partial_parcel_output_columns`

**Purpose:** Regression invariant: source complete contract rejects partial parcel output columns. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_partial_parcel_output_columns() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="[Pp]arcel\|output\|summary\|columns")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

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
| In-memory mutation | `partial["planning_surface_relation_count"] = 1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_contract_rejects_partial_parcel_output_columns() -> None:
    planning_document, parcels, result = _source_complete_contract()
    partial = parcels.copy(deep=True)
    partial["planning_surface_relation_count"] = 1
    with pytest.raises(PlanningFeaturesError, match="[Pp]arcel|output|summary|columns"):
        _validate_source_complete(planning_document, partial, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_corrupted_complete_parcel_summaries`

**Purpose:** Regression invariant: source complete contract rejects corrupted complete parcel summaries. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_corrupted_complete_parcel_summaries() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="parcel\|summary\|relation")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `result.parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

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
| In-memory mutation | `corrupted.loc[corrupted.index[0], "planning_surface_relation_count"] += 1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_contract_rejects_corrupted_complete_parcel_summaries() -> None:
    planning_document, _, result = _source_complete_contract()
    corrupted = result.parcels.copy(deep=True)
    corrupted.loc[corrupted.index[0], "planning_surface_relation_count"] += 1
    with pytest.raises(PlanningFeaturesError, match="parcel|summary|relation"):
        _validate_source_complete(planning_document, corrupted, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_noncanonical_parcel_summary_dtype`

**Purpose:** Regression invariant: source complete contract rejects noncanonical parcel summary dtype. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_noncanonical_parcel_summary_dtype() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="parcel\|schema\|dtype\|summary")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `result.parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `corrupted[<br>        "planning_surface_covered_pct"<br>    ].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

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
| In-memory mutation | `corrupted["planning_surface_covered_pct"] = corrupted[<br>        "planning_surface_covered_pct"<br>    ].astype("float32")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_contract_rejects_noncanonical_parcel_summary_dtype() -> None:
    planning_document, _, result = _source_complete_contract()
    corrupted = result.parcels.copy(deep=True)
    corrupted["planning_surface_covered_pct"] = corrupted[
        "planning_surface_covered_pct"
    ].astype("float32")
    with pytest.raises(PlanningFeaturesError, match="parcel|schema|dtype|summary"):
        _validate_source_complete(planning_document, corrupted, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_each_corrupted_parcel_summary_fact`

**Purpose:** Regression invariant: source complete contract rejects each corrupted parcel summary fact. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_each_corrupted_parcel_summary_fact(
    column: str,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("column", "value"),
    [
        ("planning_feature_document_id", "other-document"),
        ("planning_feature_archive_sha256", "f" * 64),
        ("planning_surface_covered_union_area_m2", 50.0),
        ("planning_surface_covered_pct", 50.0),
        ("planning_line_intersection_length_sum_m", 5.0),
        ("planning_point_inside_count", 0),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `column` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        PlanningFeaturesError,<br>        match="parcel\|summary\|relation\|lineage\|document\|archive\|union\|percentage",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `result.parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
| In-memory mutation | `corrupted.loc[corrupted.index[0], column] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_contract_rejects_each_corrupted_parcel_summary_fact(
    column: str,
    value: object,
) -> None:
    planning_document, _, result = _source_complete_contract()
    corrupted = result.parcels.copy(deep=True)
    corrupted.loc[corrupted.index[0], column] = value
    with pytest.raises(
        PlanningFeaturesError,
        match="parcel|summary|relation|lineage|document|archive|union|percentage",
    ):
        _validate_source_complete(planning_document, corrupted, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_duplicate_parcel_ids`

**Purpose:** Regression invariant: source complete contract rejects duplicate parcel ids. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_duplicate_parcel_ids() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="parcel_id\|unique")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `pd.concat` | `pandas.concat` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

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
def test_source_complete_contract_rejects_duplicate_parcel_ids() -> None:
    planning_document, parcels, result = _source_complete_contract()
    duplicate = pd.concat([parcels, parcels], ignore_index=True)
    duplicate = gpd.GeoDataFrame(duplicate, geometry="geometry", crs=parcels.crs)
    with pytest.raises(PlanningFeaturesError, match="parcel_id|unique"):
        _validate_source_complete(planning_document, duplicate, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_invalid_parcel_geometry`

**Purpose:** Regression invariant: source complete contract rejects invalid parcel geometry. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_invalid_parcel_geometry() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="valid\|geometry")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `Polygon` | `shapely.geometry.Polygon` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

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
| In-memory mutation | `invalid.at[invalid.index[0], "geometry"] = Polygon(<br>        [(0, 0), (10, 10), (10, 0), (0, 10), (0, 0)]<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_contract_rejects_invalid_parcel_geometry() -> None:
    planning_document, parcels, result = _source_complete_contract()
    invalid = parcels.copy(deep=True)
    invalid.at[invalid.index[0], "geometry"] = Polygon(
        [(0, 0), (10, 10), (10, 0), (0, 10), (0, 0)]
    )
    with pytest.raises(PlanningFeaturesError, match="valid|geometry"):
        _validate_source_complete(planning_document, invalid, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_accepts_epsg4326_parcels`

**Purpose:** Regression invariant: source complete contract accepts epsg4326 parcels. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_accepts_epsg4326_parcels() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `parcels.to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `intersect_parcels_with_gpu_planning_features` | `landscout.stages.enrich_planning_features.intersect_parcels_with_gpu_planning_features` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `parcels.to_crs` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_contract_accepts_epsg4326_parcels() -> None:
    planning_document, parcels, _ = _source_complete_contract()
    geographic = parcels.to_crs("EPSG:4326")
    result = intersect_parcels_with_gpu_planning_features(geographic, planning_document)
    _validate_source_complete(planning_document, geographic, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_document_reference_allows_one_archive_zip_suffix`

**Purpose:** Regression invariant: source document reference allows one archive zip suffix. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_document_reference_allows_one_archive_zip_suffix() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert (<br>        result.surface_features["source_archive_name"].eq(f"{ARCHIVE_NAME}.zip").all()<br>    )`
  - `assert (<br>        result.surface_features["source_document_reference_raw"].eq(ARCHIVE_NAME).all()<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `replace` | `dataclasses.replace` |
| `intersect_parcels_with_gpu_planning_features` | `landscout.stages.enrich_planning_features.intersect_parcels_with_gpu_planning_features` |
| `result.surface_features["source_archive_name"].eq(f"{ARCHIVE_NAME}.zip").all` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.surface_features["source_archive_name"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.surface_features["source_document_reference_raw"].eq(ARCHIVE_NAME).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.surface_features["source_document_reference_raw"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

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
def test_source_document_reference_allows_one_archive_zip_suffix() -> None:
    planning_document, parcels, _ = _source_complete_contract()
    archive = planning_document.extraction.archive
    metadata = replace(archive.document, archive_name=f"{ARCHIVE_NAME}.zip")
    suffixed = replace(
        planning_document,
        extraction=replace(
            planning_document.extraction,
            archive=replace(archive, document=metadata),
        ),
    )
    result = intersect_parcels_with_gpu_planning_features(parcels, suffixed)
    assert (
        result.surface_features["source_archive_name"].eq(f"{ARCHIVE_NAME}.zip").all()
    )
    assert (
        result.surface_features["source_document_reference_raw"].eq(ARCHIVE_NAME).all()
    )
    _validate_source_complete(suffixed, parcels, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_coherently_renamed_feature_identity`

**Purpose:** Regression invariant: source complete contract rejects coherently renamed feature identity. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_coherently_renamed_feature_identity(
    identity_column: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "identity_column", ["planning_feature_id", "source_feature_id"]
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `identity_column` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="source\|identity\|rebuilt\|catalog")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `result.surface_features.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations[identity_column].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
| In-memory mutation | `surface.loc[surface.index[0], identity_column] = new`<br>`relations.loc[relations[identity_column].eq(old), identity_column] = new` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_contract_rejects_coherently_renamed_feature_identity(
    identity_column: str,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    surface = result.surface_features.copy(deep=True)
    relations = result.relations.copy(deep=True)
    old = surface.iloc[0][identity_column]
    new = (
        f"GPU:{DOCUMENT_ID}:prescription_surface:RENAMED"
        if identity_column == "planning_feature_id"
        else "RENAMED"
    )
    surface.loc[surface.index[0], identity_column] = new
    relations.loc[relations[identity_column].eq(old), identity_column] = new
    corrupted = replace(result, surface_features=surface, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="source|identity|rebuilt|catalog"):
        _validate_source_complete(planning_document, parcels, corrupted)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_independent_gpu_lineage_mutation`

**Purpose:** Regression invariant: source complete contract rejects independent gpu lineage mutation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_independent_gpu_lineage_mutation(
    column: str,
    value: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("column", "value"),
    [
        ("source_provider", "Another provider"),
        ("source_portal", "https://example.invalid"),
        ("source_commune_code", "99999"),
        ("source_document_type", "CC"),
        ("source_archive_name", "OTHER_ARCHIVE"),
        ("source_document_reference_raw", "OTHER_ARCHIVE"),
        ("source_layer", "OTHER_SOURCE_LAYER"),
        ("source_crs", "EPSG:4326"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `column` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="source\|lineage\|catalog\|rebuilt")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `result.surface_features.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations["planning_feature_id"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
| In-memory mutation | `surface.loc[surface.index[0], column] = value`<br>`relations.loc[relations["planning_feature_id"].eq(feature_id), column] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_contract_rejects_independent_gpu_lineage_mutation(
    column: str,
    value: str,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    surface = result.surface_features.copy(deep=True)
    relations = result.relations.copy(deep=True)
    surface.loc[surface.index[0], column] = value
    if column in relations.columns:
        feature_id = result.surface_features.iloc[0]["planning_feature_id"]
        relations.loc[relations["planning_feature_id"].eq(feature_id), column] = value
    corrupted = replace(result, surface_features=surface, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="source|lineage|catalog|rebuilt"):
        _validate_source_complete(planning_document, parcels, corrupted)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_binds_gpu_document_context`

**Purpose:** Regression invariant: source complete contract binds gpu document context. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_binds_gpu_document_context(
    metadata_field: str,
    value: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("metadata_field", "value"),
    [
        ("provider", "Another provider"),
        ("portal", "https://example.invalid"),
        ("commune_code", "99999"),
        ("document_type", "CC"),
        ("archive_name", "OTHER_ARCHIVE"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `metadata_field` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        PlanningFeaturesError,<br>        match="source\|lineage\|document\|rebuilt\|IDURBA\|archive",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
def test_source_complete_contract_binds_gpu_document_context(
    metadata_field: str,
    value: str,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    archive = planning_document.extraction.archive
    metadata = replace(archive.document, **{metadata_field: value})
    changed = replace(
        planning_document,
        extraction=replace(
            planning_document.extraction,
            archive=replace(archive, document=metadata),
        ),
    )
    with pytest.raises(
        PlanningFeaturesError,
        match="source|lineage|document|rebuilt|IDURBA|archive",
    ):
        _validate_source_complete(changed, parcels, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_reloads_and_compares_source_catalog`

**Purpose:** Regression invariant: source complete contract reloads and compares source catalog. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_reloads_and_compares_source_catalog(
    mutation: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("mutation", ["geometry", "raw", "code", "remove", "extra"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `mutation` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        PlanningFeaturesError, match="source\|catalog\|rebuilt\|normalized"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `next` | `unresolved local/third-party receiver; no ownership inferred` |
| `layer.data.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_rectangle` | `tests.unit.test_enrich_planning_features._rectangle` |
| `frame.iloc[0:0].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `pd.concat` | `pandas.concat` |
| `_replace_related_layer` | `tests.unit.test_enrich_planning_features._replace_related_layer` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
| In-memory mutation | `frame.at[frame.index[0], "geometry"] = _rectangle(0, 0, 5, 10)`<br>`frame.loc[frame.index[0], "LIBELLE"] = "Changed source label"`<br>`frame.loc[frame.index[0], ["TYPEPSC", "STYPEPSC"]] = ["01", "00"]`<br>`extra.loc[extra.index[0], "LIB_IDPSC"] = "EXTRA"`<br>`extra.at[extra.index[0], "geometry"] = _rectangle(20, 20, 21, 21)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_contract_reloads_and_compares_source_catalog(
    mutation: str,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    layer = next(
        layer
        for layer in planning_document.related_layers
        if layer.logical_name == "prescription_surface"
    )
    frame = layer.data.copy(deep=True)
    if mutation == "geometry":
        frame.at[frame.index[0], "geometry"] = _rectangle(0, 0, 5, 10)
    elif mutation == "raw":
        frame.loc[frame.index[0], "LIBELLE"] = "Changed source label"
    elif mutation == "code":
        frame.loc[frame.index[0], ["TYPEPSC", "STYPEPSC"]] = ["01", "00"]
    elif mutation == "remove":
        frame = frame.iloc[0:0].copy()
    else:
        extra = frame.copy(deep=True)
        extra.loc[extra.index[0], "LIB_IDPSC"] = "EXTRA"
        extra.at[extra.index[0], "geometry"] = _rectangle(20, 20, 21, 21)
        frame = gpd.GeoDataFrame(
            pd.concat([frame, extra], ignore_index=True),
            geometry="geometry",
            crs=frame.crs,
        )
    changed = _replace_related_layer(planning_document, "prescription_surface", frame)
    with pytest.raises(
        PlanningFeaturesError, match="source|catalog|rebuilt|normalized"
    ):
        _validate_source_complete(changed, parcels, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_catalog_for_absent_gpu_layer`

**Purpose:** Regression invariant: source complete contract rejects catalog for absent gpu layer. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_catalog_for_absent_gpu_layer() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="source\|layer\|catalog\|rebuilt")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `_without_related_layer` | `tests.unit.test_enrich_planning_features._without_related_layer` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

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
def test_source_complete_contract_rejects_catalog_for_absent_gpu_layer() -> None:
    planning_document, parcels, result = _source_complete_contract()
    changed = _without_related_layer(planning_document, "prescription_surface")
    with pytest.raises(PlanningFeaturesError, match="source|layer|catalog|rebuilt"):
        _validate_source_complete(changed, parcels, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_three_dimensional_normalized_catalogs_are_rejected`

**Purpose:** Regression invariant: three dimensional normalized catalogs are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_three_dimensional_normalized_catalogs_are_rejected(
    catalog_name: str,
    geometry: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("catalog_name", "geometry"),
    [
        (
            "surface_features",
            Polygon([(0, 0, 1), (0, 10, 1), (10, 10, 1), (10, 0, 1)]),
        ),
        ("line_features", LineString([(-1, 5, 1), (11, 5, 1)])),
        ("point_features", Point(5, 5, 1)),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `catalog_name` | positional-or-keyword | `str` | `required` |
| `geometry` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="2D\|dimensional\|Z")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `getattr(result, catalog_name).copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `Polygon` | `shapely.geometry.Polygon` |
| `LineString` | `shapely.geometry.LineString` |
| `Point` | `shapely.geometry.Point` |

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
| In-memory mutation | `catalog.at[catalog.index[0], "geometry"] = geometry` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_three_dimensional_normalized_catalogs_are_rejected(
    catalog_name: str,
    geometry: object,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    catalog = getattr(result, catalog_name).copy(deep=True)
    catalog.at[catalog.index[0], "geometry"] = geometry
    corrupted = replace(result, **{catalog_name: catalog})
    with pytest.raises(PlanningFeaturesError, match="2D|dimensional|Z"):
        _validate_source_complete(planning_document, parcels, corrupted)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_two_dimensional_normalized_catalogs_remain_valid`

**Purpose:** Regression invariant: two dimensional normalized catalogs remain valid. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_two_dimensional_normalized_catalogs_remain_valid() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert not catalog.geometry.has_z.any()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `catalog.geometry.has_z.any` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `catalog.geometry.has_z.any` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_two_dimensional_normalized_catalogs_remain_valid() -> None:
    planning_document, parcels, result = _source_complete_contract()
    for catalog in (
        result.surface_features,
        result.line_features,
        result.point_features,
    ):
        assert not catalog.geometry.has_z.any()
    _validate_source_complete(planning_document, parcels, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_gpu_source_z_is_normalized_to_canonical_2d`

**Purpose:** Regression invariant: gpu source z is normalized to canonical 2d. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_gpu_source_z_is_normalized_to_canonical_2d(
    logical: str,
    geometry: object,
    catalog_name: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("logical", "geometry", "catalog_name"),
    [
        (
            "prescription_surface",
            Polygon([(0, 0, 1), (0, 10, 1), (10, 10, 1), (10, 0, 1)]),
            "surface_features",
        ),
        (
            "prescription_line",
            LineString([(0, 5, 1), (10, 5, 1)]),
            "line_features",
        ),
        ("prescription_point", Point(5, 5, 1), "point_features"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `logical` | positional-or-keyword | `str` | `required` |
| `geometry` | positional-or-keyword | `object` | `required` |
| `catalog_name` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert not catalog.geometry.has_z.any()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_run` | `tests.unit.test_enrich_planning_features._run` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `catalog.geometry.has_z.any` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `Polygon` | `shapely.geometry.Polygon` |
| `LineString` | `shapely.geometry.LineString` |
| `Point` | `shapely.geometry.Point` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `catalog.geometry.has_z.any` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_gpu_source_z_is_normalized_to_canonical_2d(
    logical: str,
    geometry: object,
    catalog_name: str,
) -> None:
    result = _run([_inspected(logical, _source_frame(logical, [geometry]))])
    catalog = getattr(result, catalog_name)
    assert not catalog.geometry.has_z.any()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_tampered_gpkg_inventory_hash`

**Purpose:** Regression invariant: source complete contract rejects tampered gpkg inventory hash. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_tampered_gpkg_inventory_hash() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="source\|file\|inventory\|SHA")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `layer.reference.dataset_path.relative_to(<br>        planning_document.extraction.extraction_root<br>    ).as_posix` | `unresolved local/third-party receiver; no ownership inferred` |
| `layer.reference.dataset_path.relative_to` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `layer.reference.dataset_path.relative_to(<br>        planning_document.extraction.extraction_root<br>    ).as_posix` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_contract_rejects_tampered_gpkg_inventory_hash() -> None:
    planning_document, parcels, result = _source_complete_contract()
    layer = planning_document.related_layers[0]
    relative = layer.reference.dataset_path.relative_to(
        planning_document.extraction.extraction_root
    ).as_posix()
    files = tuple(
        replace(item, sha256="f" * 64) if item.relative_path == relative else item
        for item in planning_document.extraction.files
    )
    changed = replace(
        planning_document,
        extraction=replace(planning_document.extraction, files=files),
    )
    with pytest.raises(PlanningFeaturesError, match="source|file|inventory|SHA"):
        _validate_source_complete(changed, parcels, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_tampered_gpkg_size`

**Purpose:** Regression invariant: source complete contract rejects tampered gpkg size. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_tampered_gpkg_size() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="source\|file\|inventory\|size")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `layer.reference.dataset_path.relative_to(<br>        planning_document.extraction.extraction_root<br>    ).as_posix` | `unresolved local/third-party receiver; no ownership inferred` |
| `layer.reference.dataset_path.relative_to` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `layer.reference.dataset_path.relative_to(<br>        planning_document.extraction.extraction_root<br>    ).as_posix` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_contract_rejects_tampered_gpkg_size() -> None:
    planning_document, parcels, result = _source_complete_contract()
    layer = planning_document.related_layers[0]
    relative = layer.reference.dataset_path.relative_to(
        planning_document.extraction.extraction_root
    ).as_posix()
    files = tuple(
        replace(item, size_bytes=item.size_bytes + 1)
        if item.relative_path == relative
        else item
        for item in planning_document.extraction.files
    )
    changed = replace(
        planning_document,
        extraction=replace(planning_document.extraction, files=files),
    )
    with pytest.raises(PlanningFeaturesError, match="source|file|inventory|size"):
        _validate_source_complete(changed, parcels, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_changed_gpkg_bytes`

**Purpose:** Regression invariant: source complete contract rejects changed gpkg bytes. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_changed_gpkg_bytes() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="source\|file\|inventory\|size\|SHA")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `path.open` | `unresolved local/third-party receiver; no ownership inferred` |
| `stream.write` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.open` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_contract_rejects_changed_gpkg_bytes() -> None:
    planning_document, parcels, result = _source_complete_contract()
    path = planning_document.related_layers[0].reference.dataset_path
    with path.open("ab") as stream:
        stream.write(b"tamper")
    with pytest.raises(PlanningFeaturesError, match="source|file|inventory|size|SHA"):
        _validate_source_complete(planning_document, parcels, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_same_size_gpkg_byte_tamper`

**Purpose:** Regression invariant: source complete contract rejects same size gpkg byte tamper. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_same_size_gpkg_byte_tamper() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="source\|file\|inventory\|SHA")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `bytearray` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.read_bytes` |
| Filesystem/archive write or publication | `path.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `payload[-1] ^= 1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_contract_rejects_same_size_gpkg_byte_tamper() -> None:
    planning_document, parcels, result = _source_complete_contract()
    path = planning_document.related_layers[0].reference.dataset_path
    payload = bytearray(path.read_bytes())
    payload[-1] ^= 1
    path.write_bytes(payload)
    with pytest.raises(PlanningFeaturesError, match="source|file|inventory|SHA"):
        _validate_source_complete(planning_document, parcels, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_coherently_changed_physical_gpkg`

**Purpose:** Regression invariant: source complete contract rejects coherently changed physical gpkg. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_coherently_changed_physical_gpkg() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="source\|file\|loaded\|changed")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `layer.data.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `changed_source.to_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `_refresh_extraction_inventory` | `tests.unit.test_enrich_planning_features._refresh_extraction_inventory` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

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
| In-memory mutation | `changed_source.loc[changed_source.index[0], "LIBELLE"] = "Changed on disk"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_contract_rejects_coherently_changed_physical_gpkg() -> None:
    planning_document, parcels, result = _source_complete_contract()
    layer = planning_document.related_layers[0]
    changed_source = layer.data.copy(deep=True)
    changed_source.loc[changed_source.index[0], "LIBELLE"] = "Changed on disk"
    changed_source.to_file(
        layer.reference.dataset_path,
        layer=layer.reference.source_layer,
        driver="GPKG",
        engine="pyogrio",
        index=False,
    )
    coherent_inventory = _refresh_extraction_inventory(planning_document)
    with pytest.raises(PlanningFeaturesError, match="source|file|loaded|changed"):
        _validate_source_complete(coherent_inventory, parcels, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_changed_physical_gpkg_geometry`

**Purpose:** Regression invariant: source complete contract rejects changed physical gpkg geometry. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_changed_physical_gpkg_geometry() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="source\|geometry\|loaded\|changed")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `layer.data.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_rectangle` | `tests.unit.test_enrich_planning_features._rectangle` |
| `changed_source.to_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `_refresh_extraction_inventory` | `tests.unit.test_enrich_planning_features._refresh_extraction_inventory` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

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
| In-memory mutation | `changed_source.at[changed_source.index[0], "geometry"] = _rectangle(0, 0, 5, 10)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_contract_rejects_changed_physical_gpkg_geometry() -> None:
    planning_document, parcels, result = _source_complete_contract()
    layer = planning_document.related_layers[0]
    changed_source = layer.data.copy(deep=True)
    changed_source.at[changed_source.index[0], "geometry"] = _rectangle(0, 0, 5, 10)
    changed_source.to_file(
        layer.reference.dataset_path,
        layer=layer.reference.source_layer,
        driver="GPKG",
        engine="pyogrio",
        index=False,
    )
    coherent_inventory = _refresh_extraction_inventory(planning_document)
    with pytest.raises(PlanningFeaturesError, match="source|geometry|loaded|changed"):
        _validate_source_complete(coherent_inventory, parcels, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_reordered_physical_gpkg_rows`

**Purpose:** Regression invariant: source complete contract rejects reordered physical gpkg rows. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_reordered_physical_gpkg_rows() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="source\|order\|loaded\|changed")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_planning_features._parcels` |
| `_rectangle` | `tests.unit.test_enrich_planning_features._rectangle` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `_planning_document` | `tests.unit.test_enrich_planning_features._planning_document` |
| `intersect_parcels_with_gpu_planning_features` | `landscout.stages.enrich_planning_features.intersect_parcels_with_gpu_planning_features` |
| `stored.data.iloc[::-1].reset_index(drop=True).to_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `stored.data.iloc[::-1].reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `_refresh_extraction_inventory` | `tests.unit.test_enrich_planning_features._refresh_extraction_inventory` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

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
def test_source_complete_contract_rejects_reordered_physical_gpkg_rows() -> None:
    parcels = _parcels(
        [_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)],
        ids=["P-1", "P-2"],
    )
    layer = _inspected(
        "prescription_surface",
        _source_frame(
            "prescription_surface",
            [_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)],
            ids=["ONE", "TWO"],
            type_codes=["07", "07"],
            subtype_codes=["04", "04"],
        ),
    )
    planning_document = _planning_document([layer])
    result = intersect_parcels_with_gpu_planning_features(parcels, planning_document)
    stored = planning_document.related_layers[0]
    stored.data.iloc[::-1].reset_index(drop=True).to_file(
        stored.reference.dataset_path,
        layer=stored.reference.source_layer,
        driver="GPKG",
        engine="pyogrio",
        index=False,
    )
    coherent_inventory = _refresh_extraction_inventory(planning_document)
    with pytest.raises(PlanningFeaturesError, match="source|order|loaded|changed"):
        _validate_source_complete(coherent_inventory, parcels, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_loaded_source_attrs_not_on_disk`

**Purpose:** Regression invariant: source complete contract rejects loaded source attrs not on disk. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_loaded_source_attrs_not_on_disk() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="source\|attrs\|metadata\|loaded")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `layer.data.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

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
| In-memory mutation | `loaded.attrs["unpersisted_source_note"] = "tampered"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_contract_rejects_loaded_source_attrs_not_on_disk() -> None:
    planning_document, parcels, result = _source_complete_contract()
    layer = planning_document.related_layers[0]
    loaded = layer.data.copy(deep=True)
    loaded.attrs["unpersisted_source_note"] = "tampered"
    changed = replace(
        planning_document,
        related_layers=tuple(
            replace(item, data=loaded) if item is layer else item
            for item in planning_document.related_layers
        ),
    )
    with pytest.raises(PlanningFeaturesError, match="source|attrs|metadata|loaded"):
        _validate_source_complete(changed, parcels, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_dataset_outside_extraction_root`

**Purpose:** Regression invariant: source complete contract rejects dataset outside extraction root. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_dataset_outside_extraction_root(
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
  - `pytest.raises(PlanningFeaturesError, match="source\|root\|outside\|contain")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `shutil.copyfile` | `shutil.copyfile` |
| `replace` | `dataclasses.replace` |
| `_replace_layer_reference` | `tests.unit.test_enrich_planning_features._replace_layer_reference` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `shutil.copyfile` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_contract_rejects_dataset_outside_extraction_root(
    tmp_path: Path,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    layer = planning_document.related_layers[0]
    outside = tmp_path / "outside.gpkg"
    shutil.copyfile(layer.reference.dataset_path, outside)
    reference = replace(layer.reference, dataset_path=outside)
    changed = _replace_layer_reference(planning_document, layer.logical_name, reference)
    with pytest.raises(PlanningFeaturesError, match="source|root|outside|contain"):
        _validate_source_complete(changed, parcels, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_linked_spatial_dataset`

**Purpose:** Regression invariant: source complete contract rejects linked spatial dataset. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_linked_spatial_dataset(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="source\|link\|junction\|dataset")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

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
def test_source_complete_contract_rejects_linked_spatial_dataset(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    dataset = planning_document.related_layers[0].reference.dataset_path
    actual_link_check = gpu_source_module._is_link_or_junction

    def synthetic_link(path: Path) -> bool:
        return path == dataset or actual_link_check(path)

    monkeypatch.setattr(
        gpu_source_module,
        "_is_link_or_junction",
        synthetic_link,
    )
    with pytest.raises(PlanningFeaturesError, match="source|link|junction|dataset"):
        _validate_source_complete(planning_document, parcels, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_linked_spatial_dataset.synthetic_link`

**Purpose:** Implements `synthetic link` within the file role: Provides complete unit and regression coverage for the `enrich_planning_features` contracts exercised in this file.

**Exact signature**

```python
def synthetic_link(path: Path) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `path == dataset or actual_link_check(path)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `actual_link_check` | `unresolved local/third-party receiver; no ownership inferred` |

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
def synthetic_link(path: Path) -> bool:
        return path == dataset or actual_link_check(path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_shapefile_source_complete_contract`

**Purpose:** Implements `shapefile source complete contract` within the file role: Provides complete unit and regression coverage for the `enrich_planning_features` contracts exercised in this file.

**Exact signature**

```python
def _shapefile_source_complete_contract(
    root: Path,
) -> tuple[GpuPlanningDocument, gpd.GeoDataFrame, ParcelPlanningFeaturesResult]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[GpuPlanningDocument, gpd.GeoDataFrame, ParcelPlanningFeaturesResult]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `root` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `document, parcels, result`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_binds_every_shapefile_sidecar` via `_shapefile_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_binds_every_shapefile_sidecar` via `_shapefile_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_requires_shapefile_core_members` via `_shapefile_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_requires_shapefile_core_members` via `_shapefile_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_changed_shapefile_sidecar_bytes` via `_shapefile_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_changed_shapefile_sidecar_bytes` via `_shapefile_source_complete_contract`
- direct call: `tests.unit.test_enrich_planning_features::test_dotted_sibling_dataset_is_not_a_sidecar_and_makes_role_ambiguous` via `_shapefile_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_dotted_sibling_dataset_is_not_a_sidecar_and_makes_role_ambiguous` via `_shapefile_source_complete_contract`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `_rectangle` | `tests.unit.test_enrich_planning_features._rectangle` |
| `frame.to_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.read_file` | `geopandas.read_file` |
| `replace` | `dataclasses.replace` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `GpuSpatialLayerReference` | `landscout.sources.gpu_fr.GpuSpatialLayerReference` |
| `_summary` | `tests.unit.test_enrich_planning_features._summary` |
| `_planning_document` | `tests.unit.test_enrich_planning_features._planning_document` |
| `_parcels` | `tests.unit.test_enrich_planning_features._parcels` |
| `intersect_parcels_with_gpu_planning_features` | `landscout.stages.enrich_planning_features.intersect_parcels_with_gpu_planning_features` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

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
def _shapefile_source_complete_contract(
    root: Path,
) -> tuple[GpuPlanningDocument, gpd.GeoDataFrame, ParcelPlanningFeaturesResult]:
    source_layer = "PRESCRIPTION_SURFACE"
    path = root / f"{source_layer}.shp"
    frame = _source_frame(
        "prescription_surface",
        [_rectangle(0, 0, 10, 10)],
        ids=["SHAPE-1"],
        type_codes=["07"],
        subtype_codes=["04"],
    )
    frame.to_file(path, driver="ESRI Shapefile", engine="pyogrio", index=False)
    loaded = gpd.read_file(path, engine="pyogrio")
    layer = replace(
        _inspected("prescription_surface", loaded),
        reference=GpuSpatialLayerReference(path, source_layer, "ESRI Shapefile"),
        summary=_summary(loaded, source_layer),
    )
    document = _planning_document([layer])
    parcels = _parcels()
    result = intersect_parcels_with_gpu_planning_features(parcels, document)
    return document, parcels, result
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_shapefile_ogr_fid_source_complete_contract`

**Purpose:** Implements `shapefile ogr fid source complete contract` within the file role: Provides complete unit and regression coverage for the `enrich_planning_features` contracts exercised in this file.

**Exact signature**

```python
def _shapefile_ogr_fid_source_complete_contract(
    root: Path,
) -> tuple[GpuPlanningDocument, gpd.GeoDataFrame, ParcelPlanningFeaturesResult]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[GpuPlanningDocument, gpd.GeoDataFrame, ParcelPlanningFeaturesResult]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `root` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `document, parcels, result`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_changed_or_reordered_ogr_fids` via `_shapefile_ogr_fid_source_complete_contract`
- value/type reference: `tests.unit.test_enrich_planning_features::test_source_complete_contract_rejects_changed_or_reordered_ogr_fids` via `_shapefile_ogr_fid_source_complete_contract`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_frame(<br>        "prescription_surface",<br>        [_rectangle(0, 0, 5, 10), _rectangle(5, 0, 10, 10)],<br>        ids=["DROP-ONE", "DROP-TWO"],<br>        type_codes=["07", "07"],<br>        subtype_codes=["04", "04"],<br>    ).drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `_source_frame` | `tests.unit.test_enrich_planning_features._source_frame` |
| `_rectangle` | `tests.unit.test_enrich_planning_features._rectangle` |
| `frame.to_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.read_file` | `geopandas.read_file` |
| `replace` | `dataclasses.replace` |
| `_inspected` | `tests.unit.test_enrich_planning_features._inspected` |
| `GpuSpatialLayerReference` | `landscout.sources.gpu_fr.GpuSpatialLayerReference` |
| `_summary` | `tests.unit.test_enrich_planning_features._summary` |
| `_planning_document` | `tests.unit.test_enrich_planning_features._planning_document` |
| `_parcels` | `tests.unit.test_enrich_planning_features._parcels` |
| `intersect_parcels_with_gpu_planning_features` | `landscout.stages.enrich_planning_features.intersect_parcels_with_gpu_planning_features` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `gpd.read_file` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `_source_frame(<br>        "prescription_surface",<br>        [_rectangle(0, 0, 5, 10), _rectangle(5, 0, 10, 10)],<br>        ids=["DROP-ONE", "DROP-TWO"],<br>        type_codes=["07", "07"],<br>        subtype_codes=["04", "04"],<br>    ).drop(columns="LIB_IDPSC")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _shapefile_ogr_fid_source_complete_contract(
    root: Path,
) -> tuple[GpuPlanningDocument, gpd.GeoDataFrame, ParcelPlanningFeaturesResult]:
    source_layer = "PRESCRIPTION_SURFACE"
    path = root / f"{source_layer}.shp"
    frame = _source_frame(
        "prescription_surface",
        [_rectangle(0, 0, 5, 10), _rectangle(5, 0, 10, 10)],
        ids=["DROP-ONE", "DROP-TWO"],
        type_codes=["07", "07"],
        subtype_codes=["04", "04"],
    ).drop(columns="LIB_IDPSC")
    frame.to_file(path, driver="ESRI Shapefile", engine="pyogrio", index=False)
    loaded = gpd.read_file(path, engine="pyogrio")
    layer = replace(
        _inspected("prescription_surface", loaded),
        reference=GpuSpatialLayerReference(path, source_layer, "ESRI Shapefile"),
        summary=_summary(loaded, source_layer),
    )
    document = _planning_document([layer])
    parcels = _parcels()
    result = intersect_parcels_with_gpu_planning_features(parcels, document)
    return document, parcels, result
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_binds_every_shapefile_sidecar`

**Purpose:** Regression invariant: source complete contract binds every shapefile sidecar. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_binds_every_shapefile_sidecar(
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
  - `pytest.raises(<br>        PlanningFeaturesError,<br>        match="shapefile\|sidecar\|inventory\|physical revalidation",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_shapefile_source_complete_contract` | `tests.unit.test_enrich_planning_features._shapefile_source_complete_contract` |
| `next` | `unresolved local/third-party receiver; no ownership inferred` |
| `item.relative_path.casefold().endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `item.relative_path.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

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
def test_source_complete_contract_binds_every_shapefile_sidecar(
    tmp_path: Path,
) -> None:
    planning_document, parcels, result = _shapefile_source_complete_contract(tmp_path)
    sidecar = next(
        item
        for item in planning_document.extraction.files
        if item.relative_path.casefold().endswith(".prj")
    )
    files = tuple(
        item
        for item in planning_document.extraction.files
        if item.relative_path != sidecar.relative_path
    )
    changed = replace(
        planning_document,
        extraction=replace(planning_document.extraction, files=files),
    )
    with pytest.raises(
        PlanningFeaturesError,
        match="shapefile|sidecar|inventory|physical revalidation",
    ):
        _validate_source_complete(changed, parcels, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_changed_or_reordered_ogr_fids`

**Purpose:** Regression invariant: source complete contract rejects changed or reordered ogr fids. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_changed_or_reordered_ogr_fids(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    changed_fids: tuple[int, int],
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("changed_fids", [(10, 11), (1, 0)])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `changed_fids` | positional-or-keyword | `tuple[int, int]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeaturesError, match="source\|FID\|identity\|catalog")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_shapefile_ogr_fid_source_complete_contract` | `tests.unit.test_enrich_planning_features._shapefile_ogr_fid_source_complete_contract` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
def test_source_complete_contract_rejects_changed_or_reordered_ogr_fids(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    changed_fids: tuple[int, int],
) -> None:
    planning_document, parcels, result = _shapefile_ogr_fid_source_complete_contract(
        tmp_path
    )
    actual_read = gpu_source_module.pyogrio.read_dataframe

    def changed_fid_read(*args: object, **kwargs: object) -> gpd.GeoDataFrame:
        reread = actual_read(*args, **kwargs)
        if kwargs.get("fid_as_index"):
            reread.index = pd.Index(changed_fids, name="fid")
        return reread

    monkeypatch.setattr(
        gpu_source_module.pyogrio,
        "read_dataframe",
        changed_fid_read,
    )
    with pytest.raises(PlanningFeaturesError, match="source|FID|identity|catalog"):
        _validate_source_complete(planning_document, parcels, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_changed_or_reordered_ogr_fids.changed_fid_read`

**Purpose:** Implements `changed fid read` within the file role: Provides complete unit and regression coverage for the `enrich_planning_features` contracts exercised in this file.

**Exact signature**

```python
def changed_fid_read(*args: object, **kwargs: object) -> gpd.GeoDataFrame:
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
  - `reread`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `actual_read` | `unresolved local/third-party receiver; no ownership inferred` |
| `kwargs.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.Index` | `pandas.Index` |

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
| In-memory mutation | `reread.index = pd.Index(changed_fids, name="fid")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def changed_fid_read(*args: object, **kwargs: object) -> gpd.GeoDataFrame:
        reread = actual_read(*args, **kwargs)
        if kwargs.get("fid_as_index"):
            reread.index = pd.Index(changed_fids, name="fid")
        return reread
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_requires_shapefile_core_members`

**Purpose:** Regression invariant: source complete contract requires shapefile core members. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_requires_shapefile_core_members(
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
  - `pytest.raises(PlanningFeaturesError, match="shapefile\|shx\|source\|file")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_shapefile_source_complete_contract` | `tests.unit.test_enrich_planning_features._shapefile_source_complete_contract` |
| `layer.reference.dataset_path.with_suffix(".shx").unlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `layer.reference.dataset_path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `layer.reference.dataset_path.with_suffix(".shx").unlink` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_contract_requires_shapefile_core_members(
    tmp_path: Path,
) -> None:
    planning_document, parcels, result = _shapefile_source_complete_contract(tmp_path)
    layer = planning_document.related_layers[0]
    layer.reference.dataset_path.with_suffix(".shx").unlink()
    with pytest.raises(PlanningFeaturesError, match="shapefile|shx|source|file"):
        _validate_source_complete(planning_document, parcels, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_contract_rejects_changed_shapefile_sidecar_bytes`

**Purpose:** Regression invariant: source complete contract rejects changed shapefile sidecar bytes. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_contract_rejects_changed_shapefile_sidecar_bytes(
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
  - `pytest.raises(<br>        PlanningFeaturesError,<br>        match="shapefile\|sidecar\|size\|SHA\|physical revalidation",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_shapefile_source_complete_contract` | `tests.unit.test_enrich_planning_features._shapefile_source_complete_contract` |
| `layer.reference.dataset_path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `cpg.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `cpg.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_contract_rejects_changed_shapefile_sidecar_bytes(
    tmp_path: Path,
) -> None:
    planning_document, parcels, result = _shapefile_source_complete_contract(tmp_path)
    layer = planning_document.related_layers[0]
    cpg = layer.reference.dataset_path.with_suffix(".cpg")
    cpg.write_text("UTF-8\n", encoding="utf-8")
    with pytest.raises(
        PlanningFeaturesError,
        match="shapefile|sidecar|size|SHA|physical revalidation",
    ):
        _validate_source_complete(planning_document, parcels, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_dotted_sibling_dataset_is_not_a_sidecar_and_makes_role_ambiguous`

**Purpose:** Regression invariant: dotted sibling dataset is not a sidecar and makes role ambiguous. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_dotted_sibling_dataset_is_not_a_sidecar_and_makes_role_ambiguous(
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
  - `pytest.raises(<br>        PlanningFeaturesError,<br>        match="Related GPU spatial sources failed physical revalidation",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_shapefile_source_complete_contract` | `tests.unit.test_enrich_planning_features._shapefile_source_complete_contract` |
| `_validate_source_complete` | `tests.unit.test_enrich_planning_features._validate_source_complete` |
| `primary.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoDataFrame(<br>        {"sibling": [1]},<br>        geometry=[_rectangle(20, 20, 21, 21)],<br>        crs="EPSG:2154",<br>    ).to_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `_rectangle` | `tests.unit.test_enrich_planning_features._rectangle` |
| `_refresh_extraction_inventory` | `tests.unit.test_enrich_planning_features._refresh_extraction_inventory` |
| `pytest.raises` | `pytest.raises` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `gpd.GeoDataFrame(<br>        {"sibling": [1]},<br>        geometry=[_rectangle(20, 20, 21, 21)],<br>        crs="EPSG:2154",<br>    ).to_file` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_dotted_sibling_dataset_is_not_a_sidecar_and_makes_role_ambiguous(
    tmp_path: Path,
) -> None:
    planning_document, parcels, result = _shapefile_source_complete_contract(tmp_path)
    _validate_source_complete(planning_document, parcels, result)
    primary = planning_document.related_layers[0].reference.dataset_path
    sibling = primary.with_name(f"{primary.stem}.archive.shp")
    gpd.GeoDataFrame(
        {"sibling": [1]},
        geometry=[_rectangle(20, 20, 21, 21)],
        crs="EPSG:2154",
    ).to_file(sibling, driver="ESRI Shapefile", engine="pyogrio", index=False)
    refreshed = _refresh_extraction_inventory(planning_document)
    with pytest.raises(
        PlanningFeaturesError,
        match="Related GPU spatial sources failed physical revalidation",
    ):
        _validate_source_complete(refreshed, parcels, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_batch_gpu_revalidation_rejects_malformed_layer_items`

**Purpose:** Regression invariant: batch gpu revalidation rejects malformed layer items. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_batch_gpu_revalidation_rejects_malformed_layer_items(
    bad_item: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("bad_item", [None, object()])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `bad_item` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(gpu_source_module.GpuSpatialInspectionError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `pytest.raises` | `pytest.raises` |
| `gpu_source_module.revalidate_gpu_spatial_layer_sources` | `landscout.sources.gpu_fr.revalidate_gpu_spatial_layer_sources` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `object` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_batch_gpu_revalidation_rejects_malformed_layer_items(
    bad_item: object,
) -> None:
    planning_document, _, _ = _source_complete_contract()
    with pytest.raises(gpu_source_module.GpuSpatialInspectionError):
        gpu_source_module.revalidate_gpu_spatial_layer_sources(
            planning_document,
            (bad_item,),  # type: ignore[arg-type]
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_batch_gpu_revalidation_rejects_malformed_planning_document`

**Purpose:** Regression invariant: batch gpu revalidation rejects malformed planning document. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_batch_gpu_revalidation_rejects_malformed_planning_document() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(gpu_source_module.GpuSpatialInspectionError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `gpu_source_module.revalidate_gpu_spatial_layer_sources` | `landscout.sources.gpu_fr.revalidate_gpu_spatial_layer_sources` |
| `object` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_batch_gpu_revalidation_rejects_malformed_planning_document() -> None:
    with pytest.raises(gpu_source_module.GpuSpatialInspectionError):
        gpu_source_module.revalidate_gpu_spatial_layer_sources(
            object(),  # type: ignore[arg-type]
            (),
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_batch_gpu_revalidation_rejects_duplicate_logical_name`

**Purpose:** Regression invariant: batch gpu revalidation rejects duplicate logical name. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_batch_gpu_revalidation_rejects_duplicate_logical_name() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(gpu_source_module.GpuSpatialInspectionError, match="duplicate")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_complete_contract` | `tests.unit.test_enrich_planning_features._source_complete_contract` |
| `pytest.raises` | `pytest.raises` |
| `gpu_source_module.revalidate_gpu_spatial_layer_sources` | `landscout.sources.gpu_fr.revalidate_gpu_spatial_layer_sources` |

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
def test_batch_gpu_revalidation_rejects_duplicate_logical_name() -> None:
    planning_document, _, _ = _source_complete_contract()
    layer = planning_document.related_layers[0]
    with pytest.raises(gpu_source_module.GpuSpatialInspectionError, match="duplicate"):
        gpu_source_module.revalidate_gpu_spatial_layer_sources(
            planning_document,
            (layer, layer),
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_common_planning_contracts_import_without_initializing_stages`

**Purpose:** Regression invariant: common planning contracts import without initializing stages. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_common_planning_contracts_import_without_initializing_stages(
    statement: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "statement",
    [
        (
            "from landscout.common.planning_feature_contract import "
            "validate_intrinsic_planning_feature_relations"
        ),
        (
            "from landscout.common.bess_application_contract import "
            "validate_bess_application_feature_catalogs"
        ),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `statement` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert completed.returncode == 0, completed.stderr`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `subprocess.run` | `subprocess.run` |
| `Path(__file__).resolve` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path` | `pathlib.Path` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | `subprocess.run` |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_common_planning_contracts_import_without_initializing_stages(
    statement: str,
) -> None:
    completed = subprocess.run(
        [
            sys.executable,
            "-c",
            f"import sys; {statement}; assert 'landscout.stages' not in sys.modules",
        ],
        cwd=Path(__file__).resolve().parents[2],
        capture_output=True,
        check=False,
        text=True,
    )
    assert completed.returncode == 0, completed.stderr
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **98**.
- Pytest fixtures (decorator-proven): **0**.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_only_high_level_api_is_exported` | none | none | 6 | Proves only high level api is exported using the exact source reproduced in section 7. |
| `test_result_is_frozen` | none | pytest.raises(FrozenInstanceError) | 0 | Proves result is frozen using the exact source reproduced in section 7. |
| `test_surface_full_overlap_normalizes_raw_values_and_lineage` | none | none | 29 | Proves surface full overlap normalizes raw values and lineage using the exact source reproduced in section 7. |
| `test_surface_partial_and_touch_relations` | none | none | 5 | Proves surface partial and touch relations using the exact source reproduced in section 7. |
| `test_overlapping_surface_union_is_not_double_counted` | none | none | 5 | Proves overlapping surface union is not double counted using the exact source reproduced in section 7. |
| `test_polygon_and_multipolygon_surfaces` | pytest.mark.parametrize(<br>    "geometry",<br>    [<br>        _rectangle(0, 0, 10, 10),<br>        MultiPolygon([_rectangle(0, 0, 4, 10), _rectangle(6, 0, 10, 10)]),<br>    ],<br>) | none | 2 | Proves polygon and multipolygon surfaces using the exact source reproduced in section 7. |
| `test_line_crossing_and_partly_inside` | none | none | 6 | Proves line crossing and partly inside using the exact source reproduced in section 7. |
| `test_line_boundary_touch_is_zero_length` | none | none | 3 | Proves line boundary touch is zero length using the exact source reproduced in section 7. |
| `test_linestring_and_multilinestring` | pytest.mark.parametrize(<br>    "geometry",<br>    [<br>        LineString([(-1, 5), (11, 5)]),<br>        MultiLineString([[(-1, 2), (11, 2)], [(-1, 8), (11, 8)]]),<br>    ],<br>) | none | 1 | Proves linestring and multilinestring using the exact source reproduced in section 7. |
| `test_points_inside_boundary_outside_and_multipoint` | none | none | 9 | Proves points inside boundary outside and multipoint using the exact source reproduced in section 7. |
| `test_missing_optional_layer_families_return_stable_empty_catalogs` | none | none | 7 | Proves missing optional layer families return stable empty catalogs using the exact source reproduced in section 7. |
| `test_optional_raw_source_fields_are_not_fabricated` | none | none | 1 | Proves optional raw source fields are not fabricated using the exact source reproduced in section 7. |
| `test_epsg4326_parcels_are_measured_in_lambert93_but_preserved` | none | none | 3 | Proves epsg4326 parcels are measured in lambert93 but preserved using the exact source reproduced in section 7. |
| `test_invalid_parcel_ids_are_rejected` | pytest.mark.parametrize("bad_id", [None, "", "   ", " X", "X ", 7]) | pytest.raises(PlanningFeaturesError, match="parcel_id") | 0 | Proves invalid parcel ids are rejected using the exact source reproduced in section 7. |
| `test_duplicate_parcel_ids_are_rejected` | none | pytest.raises(PlanningFeaturesError, match="unique") | 0 | Proves duplicate parcel ids are rejected using the exact source reproduced in section 7. |
| `test_duplicate_source_ids_are_rejected` | none | pytest.raises(PlanningFeaturesError, match="unique") | 0 | Proves duplicate source ids are rejected using the exact source reproduced in section 7. |
| `test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent` | none | none | 4 | Proves prescription surface uses validated source ogr fid when cnig id absent using the exact source reproduced in section 7. |
| `test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback` | none | none | 4 | Proves geopackage prescription surface uses sealed ogr fid fallback using the exact source reproduced in section 7. |
| `test_idurba_mismatch_is_rejected` | none | pytest.raises(PlanningFeaturesError, match="IDURBA") | 0 | Proves idurba mismatch is rejected using the exact source reproduced in section 7. |
| `test_missing_required_source_fields_fail` | pytest.mark.parametrize("missing", ["TYPEPSC", "STYPEPSC", "IDURBA", "LIB_IDPSC"]) | pytest.raises(PlanningFeaturesError, match=missing) | 0 | Proves missing required source fields fail using the exact source reproduced in section 7. |
| `test_wrong_geometry_kind_is_rejected` | pytest.mark.parametrize(<br>    ("logical", "geometry"),<br>    [<br>        ("prescription_surface", LineString([(0, 0), (1, 1)])),<br>        ("prescription_line", Point(1, 1)),<br>        ("prescription_point", LineString([(0, 0), (1, 1)])),<br>    ],<br>) | pytest.raises(PlanningFeaturesError, match="geometry") | 0 | Proves wrong geometry kind is rejected using the exact source reproduced in section 7. |
| `test_invalid_surface_geometry_is_rejected_without_repair` | none | pytest.raises(PlanningFeaturesError, match="valid") | 0 | Proves invalid surface geometry is rejected without repair using the exact source reproduced in section 7. |
| `test_null_or_empty_source_geometry_is_rejected` | pytest.mark.parametrize("geometry", [None, Polygon()]) | pytest.raises(PlanningFeaturesError, match="geometry") | 0 | Proves null or empty source geometry is rejected using the exact source reproduced in section 7. |
| `test_missing_crs_is_rejected` | pytest.mark.parametrize("target", ["parcel", "source"]) | pytest.raises(PlanningFeaturesError, match="CRS\|physical revalidation") | 0 | Proves missing crs is rejected using the exact source reproduced in section 7. |
| `test_unusable_source_crs_is_rejected` | none | pytest.raises(PlanningFeaturesError, match="CRS") | 0 | Proves unusable source crs is rejected using the exact source reproduced in section 7. |
| `test_mutated_source_summary_is_rejected` | pytest.mark.parametrize(<br>    ("field", "value"),<br>    [<br>        ("source_document_id", "other"),<br>        ("source_archive_sha256", "b" * 64),<br>        ("source_layer", "other"),<br>        ("feature_count", 99),<br>        ("geometry_types", (("Point", 1),)),<br>    ],<br>) | pytest.raises(PlanningFeaturesError, match="summary\|physical revalidation") | 0 | Proves mutated source summary is rejected using the exact source reproduced in section 7. |
| `test_source_summary_counts_are_strict_integers` | pytest.mark.parametrize("bad_count", [True, -1, 1.5, float("inf"), "1"]) | pytest.raises(<br>        PlanningFeaturesError,<br>        match="integer count\|non-negative\|summary\|physical revalidation",<br>    ) | 0 | Proves source summary counts are strict integers using the exact source reproduced in section 7. |
| `test_reserved_output_column_collision_is_rejected` | none | pytest.raises(PlanningFeaturesError, match="output columns") | 0 | Proves reserved output column collision is rejected using the exact source reproduced in section 7. |
| `test_inputs_and_all_existing_parcel_fields_are_preserved` | none | none | 4 | Proves inputs and all existing parcel fields are preserved using the exact source reproduced in section 7. |
| `test_relations_are_unique_deterministic_and_summaries_agree` | none | none | 4 | Proves relations are unique deterministic and summaries agree using the exact source reproduced in section 7. |
| `test_result_frames_are_independent_from_mutable_inputs` | none | none | 0 | Proves result frames are independent from mutable inputs using the exact source reproduced in section 7. |
| `test_present_empty_optional_layer_is_valid` | pytest.mark.parametrize(<br>    ("logical", "catalog_name"),<br>    [<br>        ("prescription_surface", "surface_features"),<br>        ("prescription_line", "line_features"),<br>        ("prescription_point", "point_features"),<br>    ],<br>) | none | 6 | Proves present empty optional layer is valid using the exact source reproduced in section 7. |
| `test_public_normalized_input_contract_validates_step_7d_3_1_result` | none | none | 5 | Proves public normalized input contract validates step 7d 3 1 result using the exact source reproduced in section 7. |
| `test_public_normalized_input_contract_wraps_malformed_document_context` | none | pytest.raises(PlanningFeaturesError) | 1 | Proves public normalized input contract wraps malformed document context using the exact source reproduced in section 7. |
| `test_source_complete_contract_binds_inspected_spatial_inventory` | none | pytest.raises(PlanningFeaturesError, match="inventory\|reference") | 0 | Proves source complete contract binds inspected spatial inventory using the exact source reproduced in section 7. |
| `test_public_normalized_input_contract_is_exported` | none | none | 4 | Proves public normalized input contract is exported using the exact source reproduced in section 7. |
| `test_public_source_validation_hashes_survive_parquet_readback` | none | none | 1 | Proves public source validation hashes survive parquet readback using the exact source reproduced in section 7. |
| `test_public_normalized_input_contract_rejects_stripped_catalog` | none | pytest.raises(PlanningFeaturesError, match="schema\|label_raw") | 0 | Proves public normalized input contract rejects stripped catalog using the exact source reproduced in section 7. |
| `test_empty_and_nonempty_catalogs_have_identical_kind_schemas` | none | none | 1 | Proves empty and nonempty catalogs have identical kind schemas using the exact source reproduced in section 7. |
| `test_strict_relation_integer_counts_are_enforced` | pytest.mark.parametrize("bad_count", [-1, 1.5, float("inf"), "2", True]) | pytest.raises(<br>        PlanningFeaturesError, match="integer count\|non-negative\|dtype\|schema"<br>    ) | 0 | Proves strict relation integer counts are enforced using the exact source reproduced in section 7. |
| `test_strict_parcel_summary_integer_counts_are_enforced` | pytest.mark.parametrize("bad_count", [-1, 1.5, float("inf"), "2", True]) | pytest.raises(PlanningFeaturesError, match="integer count\|non-negative") | 0 | Proves strict parcel summary integer counts are enforced using the exact source reproduced in section 7. |
| `test_corrupted_relation_semantics_are_rejected` | pytest.mark.parametrize(<br>    ("kind", "column", "value"),<br>    [<br>        ("SURFACE", "relation_type", "TOUCH_ONLY"),<br>        ("SURFACE", "parcel_share_pct", 42.0),<br>        ("SURFACE", "intersection_area_m2", None),<br>        ("SURFACE", "source_line_length_m", 0.0),<br>        ("LINE", "relation_type", "TOUCH_ONLY"),<br>        ("LINE", "intersection_length_m", 999.0),<br>        ("POINT", "relation_type", "BOUNDARY_TOUCH"),<br>    ],<br>) | pytest.raises(PlanningFeaturesError) | 0 | Proves corrupted relation semantics are rejected using the exact source reproduced in section 7. |
| `test_point_member_relation_semantics_are_exact` | none | pytest.raises(PlanningFeaturesError, match="relation type") | 0 | Proves point member relation semantics are exact using the exact source reproduced in section 7. |
| `test_shared_intrinsic_relation_semantics_reject_every_invalid_case` | pytest.mark.parametrize(<br>    "case",<br>    [<br>        "surface-inside",<br>        "line-area",<br>        "point-touch",<br>        "area-zero",<br>        "surface-touch-positive",<br>        "length-zero",<br>        "line-touch-positive",<br>        "inside-zero",<br>        "boundary-with-inside",<br>        "area-exceeds-feature",<br>        "share-inconsistent",<br>        "non-finite",<br>        "negative",<br>    ],<br>) | pytest.raises((TypeError, ValueError)) | 0 | Proves shared intrinsic relation semantics reject every invalid case using the exact source reproduced in section 7. |
| `test_relation_must_match_feature_catalog` | pytest.mark.parametrize(<br>    ("column", "value"),<br>    [<br>        ("source_identity_kind", "NOT_A_KIND"),<br>        ("source_identity_field", "WRONG_FIELD"),<br>        ("feature_family", "INFORMATION"),<br>        ("geometry_kind", "LINE"),<br>        ("type_code_raw", "MUTATED"),<br>        ("source_archive_sha256", "b" * 64),<br>    ],<br>) | pytest.raises(<br>        PlanningFeaturesError,<br>        match="catalog\|geometry kind\|LINE relation\|unrelated metric",<br>    ) | 0 | Proves relation must match feature catalog using the exact source reproduced in section 7. |
| `test_feature_ids_are_globally_unique_across_catalogs` | none | pytest.raises(PlanningFeaturesError, match="globally unique\|deterministic") | 0 | Proves feature ids are globally unique across catalogs using the exact source reproduced in section 7. |
| `test_same_source_id_is_allowed_in_distinct_logical_layers` | none | none | 2 | Proves same source id is allowed in distinct logical layers using the exact source reproduced in section 7. |
| `test_corrupted_parcel_summary_is_rejected` | none | pytest.raises(PlanningFeaturesError, match="inconsistent with relations") | 0 | Proves corrupted parcel summary is rejected using the exact source reproduced in section 7. |
| `test_corrupted_surface_union_contract_is_rejected` | none | pytest.raises(PlanningFeaturesError, match="union") | 0 | Proves corrupted surface union contract is rejected using the exact source reproduced in section 7. |
| `test_geospatial_operation_failure_is_controlled_and_chained` | none | pytest.raises(PlanningFeaturesError, match="spatial join") | 1 | Proves geospatial operation failure is controlled and chained using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_unknown_relation_parcel` | none | pytest.raises(PlanningFeaturesError, match="parcel\|source") | 0 | Proves source complete contract rejects unknown relation parcel using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_coherent_parcel_metric_mutation` | none | pytest.raises(PlanningFeaturesError, match="parcel\|metric\|source") | 0 | Proves source complete contract rejects coherent parcel metric mutation using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_same_area_wrong_parcel_relation` | none | pytest.raises(PlanningFeaturesError, match="relation\|parcel\|rebuilt\|source") | 0 | Proves source complete contract rejects same area wrong parcel relation using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_missing_expected_relation` | none | pytest.raises(PlanningFeaturesError, match="relation\|rebuilt\|source") | 0 | Proves source complete contract rejects missing expected relation using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_extra_geometrically_false_relation` | none | pytest.raises(PlanningFeaturesError, match="relation\|rebuilt\|source") | 0 | Proves source complete contract rejects extra geometrically false relation using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_reordered_relations` | none | pytest.raises(PlanningFeaturesError, match="relation\|order\|rebuilt") | 0 | Proves source complete contract rejects reordered relations using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_noncanonical_relation_dtype` | pytest.mark.parametrize(<br>    ("column", "dtype"),<br>    [<br>        ("intersection_area_m2", "object"),<br>        ("point_member_count", "object"),<br>        ("relation_type", "category"),<br>    ],<br>) | pytest.raises(PlanningFeaturesError, match="schema\|dtype\|relation") | 0 | Proves source complete contract rejects noncanonical relation dtype using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_relation_index_name_change` | none | pytest.raises(PlanningFeaturesError, match="schema\|index\|relation") | 0 | Proves source complete contract rejects relation index name change using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_relation_index_dtype_change` | none | pytest.raises(PlanningFeaturesError, match="schema\|index\|relation") | 1 | Proves source complete contract rejects relation index dtype change using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_relation_index_class_change` | none | pytest.raises(PlanningFeaturesError, match="schema\|index\|relation") | 2 | Proves source complete contract rejects relation index class change using the exact source reproduced in section 7. |
| `test_expected_relation_hash_binds_dtype_and_index_metadata` | none | none | 4 | Proves expected relation hash binds dtype and index metadata using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_coherent_but_wrong_line_metric` | none | pytest.raises(PlanningFeaturesError, match="relation\|metric\|rebuilt") | 0 | Proves source complete contract rejects coherent but wrong line metric using the exact source reproduced in section 7. |
| `test_source_complete_contract_accepts_complete_parcel_output_summaries` | none | none | 0 | Proves source complete contract accepts complete parcel output summaries using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_partial_parcel_output_columns` | none | pytest.raises(PlanningFeaturesError, match="[Pp]arcel\|output\|summary\|columns") | 0 | Proves source complete contract rejects partial parcel output columns using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_corrupted_complete_parcel_summaries` | none | pytest.raises(PlanningFeaturesError, match="parcel\|summary\|relation") | 0 | Proves source complete contract rejects corrupted complete parcel summaries using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_noncanonical_parcel_summary_dtype` | none | pytest.raises(PlanningFeaturesError, match="parcel\|schema\|dtype\|summary") | 0 | Proves source complete contract rejects noncanonical parcel summary dtype using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_each_corrupted_parcel_summary_fact` | pytest.mark.parametrize(<br>    ("column", "value"),<br>    [<br>        ("planning_feature_document_id", "other-document"),<br>        ("planning_feature_archive_sha256", "f" * 64),<br>        ("planning_surface_covered_union_area_m2", 50.0),<br>        ("planning_surface_covered_pct", 50.0),<br>        ("planning_line_intersection_length_sum_m", 5.0),<br>        ("planning_point_inside_count", 0),<br>    ],<br>) | pytest.raises(<br>        PlanningFeaturesError,<br>        match="parcel\|summary\|relation\|lineage\|document\|archive\|union\|percentage",<br>    ) | 0 | Proves source complete contract rejects each corrupted parcel summary fact using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_duplicate_parcel_ids` | none | pytest.raises(PlanningFeaturesError, match="parcel_id\|unique") | 0 | Proves source complete contract rejects duplicate parcel ids using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_invalid_parcel_geometry` | none | pytest.raises(PlanningFeaturesError, match="valid\|geometry") | 0 | Proves source complete contract rejects invalid parcel geometry using the exact source reproduced in section 7. |
| `test_source_complete_contract_accepts_epsg4326_parcels` | none | none | 0 | Proves source complete contract accepts epsg4326 parcels using the exact source reproduced in section 7. |
| `test_source_document_reference_allows_one_archive_zip_suffix` | none | none | 2 | Proves source document reference allows one archive zip suffix using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_coherently_renamed_feature_identity` | pytest.mark.parametrize(<br>    "identity_column", ["planning_feature_id", "source_feature_id"]<br>) | pytest.raises(PlanningFeaturesError, match="source\|identity\|rebuilt\|catalog") | 0 | Proves source complete contract rejects coherently renamed feature identity using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_independent_gpu_lineage_mutation` | pytest.mark.parametrize(<br>    ("column", "value"),<br>    [<br>        ("source_provider", "Another provider"),<br>        ("source_portal", "https://example.invalid"),<br>        ("source_commune_code", "99999"),<br>        ("source_document_type", "CC"),<br>        ("source_archive_name", "OTHER_ARCHIVE"),<br>        ("source_document_reference_raw", "OTHER_ARCHIVE"),<br>        ("source_layer", "OTHER_SOURCE_LAYER"),<br>        ("source_crs", "EPSG:4326"),<br>    ],<br>) | pytest.raises(PlanningFeaturesError, match="source\|lineage\|catalog\|rebuilt") | 0 | Proves source complete contract rejects independent gpu lineage mutation using the exact source reproduced in section 7. |
| `test_source_complete_contract_binds_gpu_document_context` | pytest.mark.parametrize(<br>    ("metadata_field", "value"),<br>    [<br>        ("provider", "Another provider"),<br>        ("portal", "https://example.invalid"),<br>        ("commune_code", "99999"),<br>        ("document_type", "CC"),<br>        ("archive_name", "OTHER_ARCHIVE"),<br>    ],<br>) | pytest.raises(<br>        PlanningFeaturesError,<br>        match="source\|lineage\|document\|rebuilt\|IDURBA\|archive",<br>    ) | 0 | Proves source complete contract binds gpu document context using the exact source reproduced in section 7. |
| `test_source_complete_contract_reloads_and_compares_source_catalog` | pytest.mark.parametrize("mutation", ["geometry", "raw", "code", "remove", "extra"]) | pytest.raises(<br>        PlanningFeaturesError, match="source\|catalog\|rebuilt\|normalized"<br>    ) | 0 | Proves source complete contract reloads and compares source catalog using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_catalog_for_absent_gpu_layer` | none | pytest.raises(PlanningFeaturesError, match="source\|layer\|catalog\|rebuilt") | 0 | Proves source complete contract rejects catalog for absent gpu layer using the exact source reproduced in section 7. |
| `test_three_dimensional_normalized_catalogs_are_rejected` | pytest.mark.parametrize(<br>    ("catalog_name", "geometry"),<br>    [<br>        (<br>            "surface_features",<br>            Polygon([(0, 0, 1), (0, 10, 1), (10, 10, 1), (10, 0, 1)]),<br>        ),<br>        ("line_features", LineString([(-1, 5, 1), (11, 5, 1)])),<br>        ("point_features", Point(5, 5, 1)),<br>    ],<br>) | pytest.raises(PlanningFeaturesError, match="2D\|dimensional\|Z") | 0 | Proves three dimensional normalized catalogs are rejected using the exact source reproduced in section 7. |
| `test_two_dimensional_normalized_catalogs_remain_valid` | none | none | 1 | Proves two dimensional normalized catalogs remain valid using the exact source reproduced in section 7. |
| `test_gpu_source_z_is_normalized_to_canonical_2d` | pytest.mark.parametrize(<br>    ("logical", "geometry", "catalog_name"),<br>    [<br>        (<br>            "prescription_surface",<br>            Polygon([(0, 0, 1), (0, 10, 1), (10, 10, 1), (10, 0, 1)]),<br>            "surface_features",<br>        ),<br>        (<br>            "prescription_line",<br>            LineString([(0, 5, 1), (10, 5, 1)]),<br>            "line_features",<br>        ),<br>        ("prescription_point", Point(5, 5, 1), "point_features"),<br>    ],<br>) | none | 1 | Proves gpu source z is normalized to canonical 2d using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_tampered_gpkg_inventory_hash` | none | pytest.raises(PlanningFeaturesError, match="source\|file\|inventory\|SHA") | 0 | Proves source complete contract rejects tampered gpkg inventory hash using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_tampered_gpkg_size` | none | pytest.raises(PlanningFeaturesError, match="source\|file\|inventory\|size") | 0 | Proves source complete contract rejects tampered gpkg size using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_changed_gpkg_bytes` | none | pytest.raises(PlanningFeaturesError, match="source\|file\|inventory\|size\|SHA") | 0 | Proves source complete contract rejects changed gpkg bytes using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_same_size_gpkg_byte_tamper` | none | pytest.raises(PlanningFeaturesError, match="source\|file\|inventory\|SHA") | 0 | Proves source complete contract rejects same size gpkg byte tamper using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_coherently_changed_physical_gpkg` | none | pytest.raises(PlanningFeaturesError, match="source\|file\|loaded\|changed") | 0 | Proves source complete contract rejects coherently changed physical gpkg using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_changed_physical_gpkg_geometry` | none | pytest.raises(PlanningFeaturesError, match="source\|geometry\|loaded\|changed") | 0 | Proves source complete contract rejects changed physical gpkg geometry using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_reordered_physical_gpkg_rows` | none | pytest.raises(PlanningFeaturesError, match="source\|order\|loaded\|changed") | 0 | Proves source complete contract rejects reordered physical gpkg rows using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_loaded_source_attrs_not_on_disk` | none | pytest.raises(PlanningFeaturesError, match="source\|attrs\|metadata\|loaded") | 0 | Proves source complete contract rejects loaded source attrs not on disk using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_dataset_outside_extraction_root` | none | pytest.raises(PlanningFeaturesError, match="source\|root\|outside\|contain") | 0 | Proves source complete contract rejects dataset outside extraction root using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_linked_spatial_dataset` | none | pytest.raises(PlanningFeaturesError, match="source\|link\|junction\|dataset") | 0 | Proves source complete contract rejects linked spatial dataset using the exact source reproduced in section 7. |
| `test_source_complete_contract_binds_every_shapefile_sidecar` | none | pytest.raises(<br>        PlanningFeaturesError,<br>        match="shapefile\|sidecar\|inventory\|physical revalidation",<br>    ) | 0 | Proves source complete contract binds every shapefile sidecar using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_changed_or_reordered_ogr_fids` | pytest.mark.parametrize("changed_fids", [(10, 11), (1, 0)]) | pytest.raises(PlanningFeaturesError, match="source\|FID\|identity\|catalog") | 0 | Proves source complete contract rejects changed or reordered ogr fids using the exact source reproduced in section 7. |
| `test_source_complete_contract_requires_shapefile_core_members` | none | pytest.raises(PlanningFeaturesError, match="shapefile\|shx\|source\|file") | 0 | Proves source complete contract requires shapefile core members using the exact source reproduced in section 7. |
| `test_source_complete_contract_rejects_changed_shapefile_sidecar_bytes` | none | pytest.raises(<br>        PlanningFeaturesError,<br>        match="shapefile\|sidecar\|size\|SHA\|physical revalidation",<br>    ) | 0 | Proves source complete contract rejects changed shapefile sidecar bytes using the exact source reproduced in section 7. |
| `test_dotted_sibling_dataset_is_not_a_sidecar_and_makes_role_ambiguous` | none | pytest.raises(<br>        PlanningFeaturesError,<br>        match="Related GPU spatial sources failed physical revalidation",<br>    ) | 0 | Proves dotted sibling dataset is not a sidecar and makes role ambiguous using the exact source reproduced in section 7. |
| `test_batch_gpu_revalidation_rejects_malformed_layer_items` | pytest.mark.parametrize("bad_item", [None, object()]) | pytest.raises(gpu_source_module.GpuSpatialInspectionError) | 0 | Proves batch gpu revalidation rejects malformed layer items using the exact source reproduced in section 7. |
| `test_batch_gpu_revalidation_rejects_malformed_planning_document` | none | pytest.raises(gpu_source_module.GpuSpatialInspectionError) | 0 | Proves batch gpu revalidation rejects malformed planning document using the exact source reproduced in section 7. |
| `test_batch_gpu_revalidation_rejects_duplicate_logical_name` | none | pytest.raises(gpu_source_module.GpuSpatialInspectionError, match="duplicate") | 0 | Proves batch gpu revalidation rejects duplicate logical name using the exact source reproduced in section 7. |
| `test_common_planning_contracts_import_without_initializing_stages` | pytest.mark.parametrize(<br>    "statement",<br>    [<br>        (<br>            "from landscout.common.planning_feature_contract import "<br>            "validate_intrinsic_planning_feature_relations"<br>        ),<br>        (<br>            "from landscout.common.bess_application_contract import "<br>            "validate_bess_application_feature_catalogs"<br>        ),<br>    ],<br>) | none | 1 | Proves common planning contracts import without initializing stages using the exact source reproduced in section 7. |

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
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from copy import deepcopy
from dataclasses import FrozenInstanceError, replace
from hashlib import sha256
from pathlib import Path

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd
import pytest
from geopandas.testing import assert_geodataframe_equal
from pandas.testing import assert_frame_equal
from shapely.geometry import (
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
)

from landscout import stages
from landscout.common.planning_feature_contract import (
    validate_intrinsic_planning_feature_relations,
)
from landscout.sources import gpu_fr as gpu_source_module
from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)
from landscout.stages import enrich_planning_features as planning_features_module
from landscout.stages.enrich_planning_features import (
    ParcelPlanningFeaturesResult,
    PlanningFeatureInputValidation,
    PlanningFeaturesError,
    _validate_result,
    intersect_parcels_with_gpu_planning_features,
    validate_normalized_planning_feature_inputs,
)

DOCUMENT_ID = "doc-1"
ARCHIVE_NAME = "31395_PLU_20240215"
ARCHIVE_SHA = "a" * 64
STANDARD = "CNIG PLU v2017"
LOCAL_ENGINEERING_CRS = (
    'ENGCRS["Local",EDATUM["Unknown"],CS[Cartesian,2],'
    'AXIS["x",east,LENGTHUNIT["metre",1]],'
    'AXIS["y",north,LENGTHUNIT["metre",1]]]'
)


def _rectangle(x1: float, y1: float, x2: float, y2: float) -> Polygon:
    return Polygon([(x1, y1), (x1, y2), (x2, y2), (x2, y1), (x1, y1)])


def _parcels(
    geometries: list[object] | None = None,
    *,
    ids: list[object] | None = None,
    crs: str | None = "EPSG:2154",
) -> gpd.GeoDataFrame:
    values = geometries or [_rectangle(0, 0, 10, 10)]
    frame = gpd.GeoDataFrame(
        {
            "parcel_id": ids or [f"P-{index + 1}" for index in range(len(values))],
            "existing_zoning_fact": np.arange(len(values), dtype="int64") + 7,
        },
        geometry=values,
        crs="EPSG:2154",
        index=[50 + index for index in range(len(values))],
    )
    if crs is None:
        return frame.set_crs(None, allow_override=True)
    return frame if crs == "EPSG:2154" else frame.to_crs(crs)


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
    count = len(geometries)
    prescription = logical.startswith("prescription")
    identity = "LIB_IDPSC" if prescription else "LIB_IDINFO"
    type_field = "TYPEPSC" if prescription else "TYPEINF"
    subtype_field = "STYPEPSC" if prescription else "STYPEINF"
    data: dict[str, object] = {
        "LIBELLE": [f"Label {index}" for index in range(count)],
        "TXT": [None if index % 2 else f"Text {index}" for index in range(count)],
        type_field: type_codes or [f"T{index}" for index in range(count)],
        subtype_field: subtype_codes or [f"S{index}" for index in range(count)],
        "NOMFIC": [
            None if index % 2 else f"rule-{index}.pdf" for index in range(count)
        ],
        "URLFIC": [None] * count,
        "IDURBA": document_refs or [ARCHIVE_NAME] * count,
        "DATVALID": ["20240215"] * count,
        identity: ids or [f"SRC-{logical}-{index}" for index in range(count)],
    }
    frame = gpd.GeoDataFrame(data, geometry=geometries, crs="EPSG:2154")
    if crs is None:
        return frame.set_crs(None, allow_override=True)
    if crs == "IGNF:LAMB93":
        return frame.set_crs(crs, allow_override=True)
    return frame if crs == "EPSG:2154" else frame.to_crs(crs)


def _summary(
    frame: gpd.GeoDataFrame,
    source_layer: str,
    *,
    document_id: str = DOCUMENT_ID,
    archive_sha: str = ARCHIVE_SHA,
) -> GpuLayerSummary:
    geometry = frame.geometry
    non_null = ~geometry.isna()
    non_empty = non_null & ~geometry.is_empty
    return GpuLayerSummary(
        source_document_id=document_id,
        source_archive_sha256=archive_sha,
        source_layer=source_layer,
        crs="UNKNOWN" if frame.crs is None else frame.crs.to_string(),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
        null_counts=tuple(
            (str(column), int(frame[column].isna().sum())) for column in frame.columns
        ),
        geometry_types=tuple(
            (str(key), int(value))
            for key, value in geometry.geom_type.value_counts().sort_index().items()
        ),
        null_geometry_count=int((~non_null).sum()),
        empty_geometry_count=int((non_null & geometry.is_empty).sum()),
        invalid_geometry_count=int((non_empty & ~geometry.is_valid).sum()),
    )


def _inspected(logical: str, frame: gpd.GeoDataFrame) -> GpuInspectedLayer:
    source_layer = f"SOURCE_{logical.upper()}"
    reference = GpuSpatialLayerReference(
        dataset_path=Path(f"synthetic-{logical}.gpkg"),
        source_layer=source_layer,
        driver="GPKG",
    )
    return GpuInspectedLayer(
        logical_name=logical,  # type: ignore[arg-type]
        reference=reference,
        data=frame,
        summary=_summary(frame, source_layer),
    )


def _physical_inventory(root: Path) -> tuple[GpuExtractedFile, ...]:
    records: list[GpuExtractedFile] = []
    for path in sorted((item for item in root.rglob("*") if item.is_file()), key=str):
        if path.parent == root and path.name == EXTRACTION_MANIFEST_NAME:
            continue
        suffix = path.suffix.casefold()
        records.append(
            GpuExtractedFile(
                relative_path=path.relative_to(root).as_posix(),
                file_type=suffix.lstrip(".") or "none",
                size_bytes=path.stat().st_size,
                sha256=sha256(path.read_bytes()).hexdigest(),
                category="SPATIAL_DATA",
            )
        )
    return tuple(records)


def _write_extraction_manifest(
    root: Path,
    archive_sha256: str,
    files: tuple[GpuExtractedFile, ...],
) -> None:
    payload = {
        "schema_version": 2,
        "archive_sha256": archive_sha256,
        "files": [
            {
                "relative_path": item.relative_path,
                "size_bytes": item.size_bytes,
                "sha256": item.sha256,
            }
            for item in files
        ],
    }
    (root / EXTRACTION_MANIFEST_NAME).write_text(
        json.dumps(payload, sort_keys=True, separators=(",", ":")),
        encoding="utf-8",
    )


def _materialize_layer(root: Path, layer: GpuInspectedLayer) -> GpuInspectedLayer:
    reference = layer.reference
    if reference.dataset_path.is_file():
        path = reference.dataset_path.resolve()
    else:
        path = root / f"{layer.logical_name}.gpkg"
        layer.data.to_file(
            path,
            layer=reference.source_layer,
            driver="GPKG",
            engine="pyogrio",
            index=False,
        )
        reference = replace(reference, dataset_path=path, driver="GPKG")
    reread = gpd.read_file(
        path,
        layer=reference.source_layer if reference.driver == "GPKG" else None,
        engine="pyogrio",
    )
    return replace(
        layer,
        reference=replace(reference, dataset_path=path),
        data=reread,
        summary=_summary(reread, reference.source_layer),
    )


def _planning_document(
    layers: list[GpuInspectedLayer] | None = None,
) -> GpuPlanningDocument:
    requested_layers = list(layers or [])
    existing_paths = [
        layer.reference.dataset_path.resolve()
        for layer in requested_layers
        if layer.reference.dataset_path.is_file()
    ]
    extraction_root = (
        existing_paths[0].parent
        if existing_paths
        else Path(tempfile.mkdtemp(prefix="landscout-feature-source-"))
    )
    related = tuple(
        _materialize_layer(extraction_root, layer) for layer in requested_layers
    )
    metadata = GpuDocumentMetadata(
        provider="Géoportail de l'Urbanisme",
        portal="G\u00e9oportail de l'Urbanisme",
        commune_code="31395",
        partition="DU_31395",
        document_id=DOCUMENT_ID,
        document_family="DU",
        document_type="PLU",
        document_title="Muret PLU",
        status="document.production",
        legal_status="APPROVED",
        effective_status="EN_VIGUEUR",
        version="10",
        archive_name=ARCHIVE_NAME,
        publication_timestamp=None,
        update_timestamp=None,
        revision_date=None,
        producer=None,
        standard_model=STANDARD,
        projection="EPSG:2154",
        metadata_identifier=None,
        source_url="https://www.geoportail-urbanisme.gouv.fr/api/document/download-by-partition/DU_31395",
        written_files=(),
    )
    archive = GpuArchiveDownload(
        document=metadata,
        download_timestamp="2026-08-12T12:00:00+00:00",
        filename=f"{ARCHIVE_NAME}.zip",
        archive_format="zip",
        file_size=1,
        sha256=ARCHIVE_SHA,
        path=Path("synthetic.zip"),
        cache_hit=True,
    )
    zoning_frame = gpd.GeoDataFrame(
        {"zone": ["Z"]}, geometry=[_rectangle(-10, -10, 20, 20)], crs="EPSG:2154"
    )
    zoning_path = extraction_root / "zoning.gpkg"
    zoning_frame.to_file(
        zoning_path,
        layer="ZONING",
        driver="GPKG",
        engine="pyogrio",
        index=False,
    )
    zoning_frame = gpd.read_file(zoning_path, layer="ZONING", engine="pyogrio")
    zoning_ref = GpuSpatialLayerReference(zoning_path, "ZONING", "GPKG")
    zoning = GpuInspectedLayer(
        logical_name="zoning",
        reference=zoning_ref,
        data=zoning_frame,
        summary=_summary(zoning_frame, "ZONING"),
    )
    inventory = _physical_inventory(extraction_root)
    _write_extraction_manifest(extraction_root, ARCHIVE_SHA, inventory)
    extraction = GpuExtraction(
        archive=archive,
        extraction_root=extraction_root,
        files=inventory,
        standard_models=(STANDARD,),
        cache_hit=True,
    )
    config_payload = load_gpu_source_config(
        Path("configs/sources/gpu_fr.yaml")
    ).model_dump(mode="python")
    for role in config_payload["spatial_layers"]:
        config_payload["spatial_layers"][role]["match_tokens"] = [f"unused_{role}"]
    config_payload["spatial_layers"]["zoning"]["match_tokens"] = ["ZONING"]
    for layer in related:
        config_payload["spatial_layers"][layer.logical_name]["match_tokens"] = [
            layer.reference.source_layer
        ]
    source_config = GpuSourceConfig.model_validate(config_payload)
    related_by_logical_name = {layer.logical_name: layer for layer in related}
    related = tuple(
        related_by_logical_name[logical_name]
        for logical_name in gpu_source_module._GPU_LOGICAL_LAYER_NAMES
        if logical_name != "zoning" and logical_name in related_by_logical_name
    )
    return GpuPlanningDocument(
        source_config=source_config,
        source_config_sha256=gpu_source_module._source_config_sha256(source_config),
        extraction=extraction,
        all_spatial_layers=gpu_source_module.discover_gpu_spatial_layers(extraction),
        zoning=zoning,
        related_layers=related,
    )


def _run(
    layers: list[GpuInspectedLayer],
    parcels: gpd.GeoDataFrame | None = None,
) -> ParcelPlanningFeaturesResult:
    return intersect_parcels_with_gpu_planning_features(
        parcels if parcels is not None else _parcels(),
        _planning_document(layers),
    )


def test_only_high_level_api_is_exported() -> None:
    assert (
        stages.intersect_parcels_with_gpu_planning_features
        is intersect_parcels_with_gpu_planning_features
    )
    assert "intersect_parcels_with_gpu_planning_features" in stages.__all__
    assert stages.PlanningFeaturesError is PlanningFeaturesError
    assert stages.ParcelPlanningFeaturesResult is ParcelPlanningFeaturesResult
    assert "PlanningFeaturesError" in stages.__all__
    assert "ParcelPlanningFeaturesResult" in stages.__all__


def test_result_is_frozen() -> None:
    result = _run([])
    with pytest.raises(FrozenInstanceError):
        result.parcels = result.parcels.copy()  # type: ignore[misc]


def test_surface_full_overlap_normalizes_raw_values_and_lineage() -> None:
    layer = _inspected(
        "prescription_surface",
        _source_frame(
            "prescription_surface",
            [_rectangle(0, 0, 10, 10)],
            ids=["PSC-1"],
            type_codes=["DYNAMIC-18"],
            subtype_codes=["04"],
            crs="IGNF:LAMB93",
        ),
    )
    result = _run([layer])

    feature = result.surface_features.iloc[0]
    assert feature["planning_feature_id"] == (
        f"GPU:{DOCUMENT_ID}:prescription_surface:PSC-1"
    )
    assert feature["source_feature_id"] == "PSC-1"
    assert feature["source_identity_kind"] == "CNIG_ATTRIBUTE"
    assert feature["source_identity_field"] == "LIB_IDPSC"
    assert feature["feature_family"] == "PRESCRIPTION"
    assert feature["geometry_kind"] == "SURFACE"
    assert feature["type_code_raw"] == "DYNAMIC-18"
    assert feature["subtype_code_raw"] == "04"
    assert feature["label_raw"] == "Label 0"
    assert feature["text_raw"] == "Text 0"
    assert feature["source_document_id"] == DOCUMENT_ID
    assert feature["source_archive_sha256"] == ARCHIVE_SHA
    assert feature["source_layer"] == "SOURCE_PRESCRIPTION_SURFACE"
    # The physical GPKG round-trip exposes the equivalent canonical CRS identity.
    assert feature["source_crs"] == "EPSG:2154"
    assert feature["feature_area_m2"] == pytest.approx(100.0)
    assert result.surface_features.crs.to_epsg() == 2154

    relation = result.relations.iloc[0]
    assert relation["source_identity_kind"] == "CNIG_ATTRIBUTE"
    assert relation["source_identity_field"] == "LIB_IDPSC"
    assert relation["relation_type"] == "AREA_OVERLAP"
    assert relation["intersection_area_m2"] == pytest.approx(100.0)
    assert relation["parcel_share_pct"] == pytest.approx(100.0)
    assert relation["feature_share_pct"] == pytest.approx(100.0)
    assert pd.isna(relation["intersection_length_m"])
    parcel = result.parcels.iloc[0]
    assert parcel["planning_surface_relation_count"] == 1
    assert parcel["planning_surface_area_overlap_count"] == 1
    assert parcel["planning_surface_covered_union_area_m2"] == pytest.approx(100.0)
    assert parcel["planning_surface_covered_pct"] == pytest.approx(100.0)
    assert parcel["prescription_surface_relation_count"] == 1
    assert parcel["information_surface_relation_count"] == 0


def test_surface_partial_and_touch_relations() -> None:
    frame = _source_frame(
        "prescription_surface",
        [_rectangle(0, 0, 5, 10), _rectangle(10, 0, 20, 10)],
        ids=["PART", "TOUCH"],
    )
    result = _run([_inspected("prescription_surface", frame)])
    relations = result.relations.set_index("source_feature_id")
    assert relations.loc["PART", "relation_type"] == "AREA_OVERLAP"
    assert relations.loc["PART", "intersection_area_m2"] == pytest.approx(50.0)
    assert relations.loc["TOUCH", "relation_type"] == "TOUCH_ONLY"
    assert relations.loc["TOUCH", "intersection_area_m2"] == pytest.approx(0.0)
    assert result.parcels.iloc[0]["planning_surface_touch_count"] == 1


def test_overlapping_surface_union_is_not_double_counted() -> None:
    prescription = _inspected(
        "prescription_surface",
        _source_frame(
            "prescription_surface",
            [_rectangle(0, 0, 10, 10)],
            ids=["WHOLE"],
        ),
    )
    information = _inspected(
        "information_surface",
        _source_frame(
            "information_surface",
            [_rectangle(0, 0, 5, 10)],
            ids=["HALF"],
            type_codes=["99"],
            subtype_codes=["00"],
        ),
    )
    parcel = _run([prescription, information]).parcels.iloc[0]
    assert parcel["planning_surface_intersection_area_sum_m2"] == pytest.approx(150.0)
    assert parcel["planning_surface_covered_union_area_m2"] == pytest.approx(100.0)
    assert parcel["planning_surface_covered_pct"] == pytest.approx(100.0)
    assert parcel["prescription_surface_covered_union_area_m2"] == pytest.approx(100.0)
    assert parcel["information_surface_covered_union_area_m2"] == pytest.approx(50.0)


@pytest.mark.parametrize(
    "geometry",
    [
        _rectangle(0, 0, 10, 10),
        MultiPolygon([_rectangle(0, 0, 4, 10), _rectangle(6, 0, 10, 10)]),
    ],
)
def test_polygon_and_multipolygon_surfaces(geometry: object) -> None:
    result = _run(
        [
            _inspected(
                "information_surface", _source_frame("information_surface", [geometry])
            )
        ]
    )
    assert len(result.relations) == 1
    assert result.relations.iloc[0]["intersection_area_m2"] > 0


def test_line_crossing_and_partly_inside() -> None:
    frame = _source_frame(
        "prescription_line",
        [LineString([(-5, 5), (15, 5)]), LineString([(5, 5), (15, 5)])],
        ids=["CROSS", "PART"],
        type_codes=["15", "15"],
        subtype_codes=["01", "00"],
    )
    result = _run([_inspected("prescription_line", frame)])
    relations = result.relations.set_index("source_feature_id")
    assert relations.loc["CROSS", "relation_type"] == "LENGTH_OVERLAP"
    assert relations.loc["CROSS", "intersection_length_m"] == pytest.approx(10.0)
    assert relations.loc["CROSS", "source_line_length_m"] == pytest.approx(20.0)
    assert relations.loc["PART", "intersection_length_m"] == pytest.approx(5.0)
    parcel = result.parcels.iloc[0]
    assert parcel["planning_line_relation_count"] == 2
    assert parcel["planning_line_intersection_length_sum_m"] == pytest.approx(15.0)


def test_line_boundary_touch_is_zero_length() -> None:
    frame = _source_frame(
        "prescription_line",
        [LineString([(10, 5), (15, 5)])],
        ids=["TOUCH"],
    )
    result = _run([_inspected("prescription_line", frame)])
    assert result.relations.iloc[0]["relation_type"] == "TOUCH_ONLY"
    assert result.relations.iloc[0]["intersection_length_m"] == pytest.approx(0.0)
    assert result.parcels.iloc[0]["planning_line_touch_count"] == 1


@pytest.mark.parametrize(
    "geometry",
    [
        LineString([(-1, 5), (11, 5)]),
        MultiLineString([[(-1, 2), (11, 2)], [(-1, 8), (11, 8)]]),
    ],
)
def test_linestring_and_multilinestring(geometry: object) -> None:
    result = _run(
        [
            _inspected(
                "prescription_line", _source_frame("prescription_line", [geometry])
            )
        ]
    )
    assert result.relations.iloc[0]["intersection_length_m"] > 0


def test_points_inside_boundary_outside_and_multipoint() -> None:
    frame = _source_frame(
        "prescription_point",
        [
            Point(5, 5),
            Point(10, 5),
            Point(20, 20),
            MultiPoint([(3, 3), (10, 4), (30, 30)]),
        ],
        ids=["IN", "BOUNDARY", "OUT", "MULTI"],
        type_codes=["07"] * 4,
        subtype_codes=["00"] * 4,
    )
    result = _run([_inspected("prescription_point", frame)])
    relations = result.relations.set_index("source_feature_id")
    assert set(relations.index) == {"IN", "BOUNDARY", "MULTI"}
    assert relations.loc["IN", "relation_type"] == "INSIDE"
    assert relations.loc["BOUNDARY", "relation_type"] == "BOUNDARY_TOUCH"
    assert relations.loc["MULTI", "point_member_count"] == 3
    assert relations.loc["MULTI", "point_members_inside_count"] == 1
    assert relations.loc["MULTI", "point_members_boundary_count"] == 1
    parcel = result.parcels.iloc[0]
    assert parcel["planning_point_relation_count"] == 3
    assert parcel["planning_point_inside_count"] == 2
    assert parcel["planning_point_boundary_count"] == 2


def test_missing_optional_layer_families_return_stable_empty_catalogs() -> None:
    result = _run([])
    assert result.surface_features.empty
    assert result.line_features.empty
    assert result.point_features.empty
    assert result.relations.empty
    assert result.surface_features.crs.to_epsg() == 2154
    assert str(result.relations["point_member_count"].dtype) == "Int64"
    assert result.parcels.iloc[0]["planning_surface_relation_count"] == 0


def test_optional_raw_source_fields_are_not_fabricated() -> None:
    frame = _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]).drop(
        columns=["LIBELLE", "TXT", "NOMFIC", "URLFIC", "DATVALID"]
    )
    result = _run([_inspected("prescription_line", frame)])
    feature = result.line_features.iloc[0]
    for column in (
        "label_raw",
        "text_raw",
        "regulation_filename_raw",
        "regulation_url_raw",
        "source_validity_date_raw",
    ):
        assert pd.isna(feature[column])


def test_epsg4326_parcels_are_measured_in_lambert93_but_preserved() -> None:
    parcel = _parcels(crs="EPSG:4326")
    original = parcel.copy(deep=True)
    result = _run(
        [
            _inspected(
                "prescription_surface",
                _source_frame("prescription_surface", [_rectangle(0, 0, 10, 10)]),
            )
        ],
        parcel,
    )
    assert result.parcels.crs == original.crs
    assert np.array_equal(result.parcels.geometry.to_wkb(), original.geometry.to_wkb())
    assert result.relations.iloc[0]["intersection_area_m2"] == pytest.approx(100.0)


@pytest.mark.parametrize("bad_id", [None, "", "   ", " X", "X ", 7])
def test_invalid_parcel_ids_are_rejected(bad_id: object) -> None:
    with pytest.raises(PlanningFeaturesError, match="parcel_id"):
        _run([], _parcels(ids=[bad_id]))


def test_duplicate_parcel_ids_are_rejected() -> None:
    with pytest.raises(PlanningFeaturesError, match="unique"):
        _run(
            [],
            _parcels([_rectangle(0, 0, 2, 2), _rectangle(3, 3, 4, 4)], ids=["P", "P"]),
        )


def test_duplicate_source_ids_are_rejected() -> None:
    frame = _source_frame(
        "information_surface",
        [_rectangle(0, 0, 2, 2), _rectangle(3, 3, 4, 4)],
        ids=["SAME", "SAME"],
    )
    with pytest.raises(PlanningFeaturesError, match="unique"):
        _run([_inspected("information_surface", frame)])


def test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent(
    tmp_path: Path,
) -> None:
    source_layer = "PRESCRIPTION_SURFACE"
    path = tmp_path / f"{source_layer}.shp"
    frame = _source_frame("prescription_surface", [_rectangle(0, 0, 10, 10)]).drop(
        columns="LIB_IDPSC"
    )
    frame.to_file(path, engine="pyogrio")
    loaded = gpd.read_file(path, engine="pyogrio")
    layer = _inspected("prescription_surface", loaded)
    reference = replace(
        layer.reference,
        dataset_path=path,
        source_layer=source_layer,
        driver="ESRI Shapefile",
    )
    layer = replace(
        layer,
        reference=reference,
        summary=_summary(loaded, source_layer),
    )
    result = _run([layer])
    assert result.surface_features.iloc[0]["source_feature_id"] == "OGR_FID:0"
    assert (
        result.surface_features.iloc[0]["source_identity_kind"]
        == "ARCHIVE_SCOPED_OGR_FID"
    )
    assert result.surface_features.iloc[0]["source_identity_field"] == "OGR_FID"
    assert result.surface_features.iloc[0]["planning_feature_id"] == (
        f"GPU:{DOCUMENT_ID}:prescription_surface:OGR_FID:0"
    )


def test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback() -> None:
    frame = _source_frame("prescription_surface", [_rectangle(0, 0, 10, 10)]).drop(
        columns="LIB_IDPSC"
    )
    result = _run([_inspected("prescription_surface", frame)])
    feature = result.surface_features.iloc[0]
    assert feature["source_feature_id"] == "OGR_FID:1"
    assert feature["source_identity_kind"] == "ARCHIVE_SCOPED_OGR_FID"
    assert feature["source_identity_field"] == "OGR_FID"
    assert feature["planning_feature_id"] == (
        f"GPU:{DOCUMENT_ID}:prescription_surface:OGR_FID:1"
    )


def test_idurba_mismatch_is_rejected() -> None:
    frame = _source_frame(
        "prescription_line", [LineString([(0, 5), (10, 5)])], document_refs=["OTHER"]
    )
    with pytest.raises(PlanningFeaturesError, match="IDURBA"):
        _run([_inspected("prescription_line", frame)])


@pytest.mark.parametrize("missing", ["TYPEPSC", "STYPEPSC", "IDURBA", "LIB_IDPSC"])
def test_missing_required_source_fields_fail(missing: str) -> None:
    frame = _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]).drop(
        columns=missing
    )
    with pytest.raises(PlanningFeaturesError, match=missing):
        _run([_inspected("prescription_line", frame)])


@pytest.mark.parametrize(
    ("logical", "geometry"),
    [
        ("prescription_surface", LineString([(0, 0), (1, 1)])),
        ("prescription_line", Point(1, 1)),
        ("prescription_point", LineString([(0, 0), (1, 1)])),
    ],
)
def test_wrong_geometry_kind_is_rejected(logical: str, geometry: object) -> None:
    with pytest.raises(PlanningFeaturesError, match="geometry"):
        _run([_inspected(logical, _source_frame(logical, [geometry]))])


def test_invalid_surface_geometry_is_rejected_without_repair() -> None:
    bowtie = Polygon([(0, 0), (2, 2), (2, 0), (0, 2), (0, 0)])
    with pytest.raises(PlanningFeaturesError, match="valid"):
        _run(
            [
                _inspected(
                    "information_surface",
                    _source_frame("information_surface", [bowtie]),
                )
            ]
        )


@pytest.mark.parametrize("geometry", [None, Polygon()])
def test_null_or_empty_source_geometry_is_rejected(geometry: object) -> None:
    frame = _source_frame("information_surface", [_rectangle(0, 0, 1, 1)])
    frame.geometry = [geometry]
    layer = _inspected("information_surface", frame)
    with pytest.raises(PlanningFeaturesError, match="geometry"):
        _run([layer])


@pytest.mark.parametrize("target", ["parcel", "source"])
def test_missing_crs_is_rejected(target: str) -> None:
    parcel = _parcels(crs=None) if target == "parcel" else _parcels()
    frame = _source_frame(
        "prescription_line",
        [LineString([(0, 5), (10, 5)])],
        crs=None if target == "source" else "EPSG:2154",
    )
    with pytest.raises(PlanningFeaturesError, match="CRS|physical revalidation"):
        _run([_inspected("prescription_line", frame)], parcel)


def test_unusable_source_crs_is_rejected() -> None:
    frame = _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]).set_crs(
        LOCAL_ENGINEERING_CRS, allow_override=True
    )
    with pytest.raises(PlanningFeaturesError, match="CRS"):
        _run([_inspected("prescription_line", frame)])


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("source_document_id", "other"),
        ("source_archive_sha256", "b" * 64),
        ("source_layer", "other"),
        ("feature_count", 99),
        ("geometry_types", (("Point", 1),)),
    ],
)
def test_mutated_source_summary_is_rejected(field: str, value: object) -> None:
    layer = _inspected(
        "prescription_line",
        _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]),
    )
    planning_document = _planning_document([layer])
    stored = planning_document.related_layers[0]
    corrupted = replace(stored, summary=replace(stored.summary, **{field: value}))
    changed = replace(planning_document, related_layers=(corrupted,))
    with pytest.raises(PlanningFeaturesError, match="summary|physical revalidation"):
        intersect_parcels_with_gpu_planning_features(_parcels(), changed)


@pytest.mark.parametrize("bad_count", [True, -1, 1.5, float("inf"), "1"])
def test_source_summary_counts_are_strict_integers(bad_count: object) -> None:
    layer = _inspected(
        "prescription_line",
        _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]),
    )
    planning_document = _planning_document([layer])
    stored = planning_document.related_layers[0]
    corrupted = replace(
        stored, summary=replace(stored.summary, feature_count=bad_count)
    )
    changed = replace(planning_document, related_layers=(corrupted,))
    with pytest.raises(
        PlanningFeaturesError,
        match="integer count|non-negative|summary|physical revalidation",
    ):
        intersect_parcels_with_gpu_planning_features(_parcels(), changed)


def test_reserved_output_column_collision_is_rejected() -> None:
    parcels = _parcels()
    parcels["planning_surface_relation_count"] = 99
    with pytest.raises(PlanningFeaturesError, match="output columns"):
        _run([], parcels)


def test_inputs_and_all_existing_parcel_fields_are_preserved() -> None:
    parcels = _parcels([_rectangle(0, 0, 10, 10), _rectangle(20, 20, 30, 30)])
    frame = _source_frame(
        "prescription_surface", [_rectangle(0, 0, 5, 10)], ids=["PSC"]
    )
    planning = _planning_document([_inspected("prescription_surface", frame)])
    parcels_before = parcels.copy(deep=True)
    zoning_before = planning.related_layers[0].data.copy(deep=True)
    result = intersect_parcels_with_gpu_planning_features(parcels, planning)
    assert_geodataframe_equal(parcels, parcels_before)
    assert_geodataframe_equal(planning.related_layers[0].data, zoning_before)
    assert result.parcels["parcel_id"].tolist() == parcels["parcel_id"].tolist()
    assert result.parcels.index.equals(parcels.index)
    assert result.parcels["existing_zoning_fact"].equals(
        parcels["existing_zoning_fact"]
    )
    assert np.array_equal(result.parcels.geometry.to_wkb(), parcels.geometry.to_wkb())


def test_relations_are_unique_deterministic_and_summaries_agree() -> None:
    parcels = _parcels(
        [_rectangle(0, 0, 10, 10), _rectangle(20, 20, 30, 30)], ids=["P-B", "P-A"]
    )
    surface = _inspected(
        "information_surface",
        _source_frame("information_surface", [_rectangle(-1, -1, 31, 31)], ids=["I"]),
    )
    line = _inspected(
        "prescription_line",
        _source_frame("prescription_line", [LineString([(-1, 5), (11, 5)])], ids=["L"]),
    )
    result = _run([surface, line], parcels)
    assert not result.relations.duplicated(["parcel_id", "planning_feature_id"]).any()
    assert result.relations["parcel_id"].tolist() == ["P-B", "P-B", "P-A"]
    first = result.parcels.iloc[0]
    assert first["planning_surface_relation_count"] == int(
        (
            (result.relations["parcel_id"] == "P-B")
            & (result.relations["geometry_kind"] == "SURFACE")
        ).sum()
    )
    assert first["planning_line_intersection_length_sum_m"] == pytest.approx(
        result.relations.loc[
            (result.relations["parcel_id"] == "P-B")
            & (result.relations["geometry_kind"] == "LINE"),
            "intersection_length_m",
        ].sum()
    )


def test_result_frames_are_independent_from_mutable_inputs() -> None:
    parcels = _parcels()
    layer = _inspected(
        "prescription_line",
        _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]),
    )
    result = _run([layer], parcels)
    snapshot = deepcopy(result.relations)
    parcels.loc[50, "existing_zoning_fact"] = -1
    layer.data.loc[0, "LIBELLE"] = "mutated"
    assert_frame_equal(result.relations, snapshot)


@pytest.mark.parametrize(
    ("logical", "catalog_name"),
    [
        ("prescription_surface", "surface_features"),
        ("prescription_line", "line_features"),
        ("prescription_point", "point_features"),
    ],
)
def test_present_empty_optional_layer_is_valid(
    logical: str,
    catalog_name: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    frame = _source_frame(logical, [])
    fid_reads = 0
    if logical == "prescription_surface":
        frame = frame.drop(columns="LIB_IDPSC")
        real_read_dataframe = gpu_source_module.pyogrio.read_dataframe

        def unexpected_fid_read(*args: object, **kwargs: object) -> object:
            nonlocal fid_reads
            if kwargs.get("fid_as_index"):
                fid_reads += 1
            return real_read_dataframe(*args, **kwargs)

        monkeypatch.setattr(
            gpu_source_module.pyogrio,
            "read_dataframe",
            unexpected_fid_read,
        )
    result = _run([_inspected(logical, frame)])
    catalog = getattr(result, catalog_name)
    assert catalog.empty
    assert catalog.crs.to_epsg() == 2154
    assert result.relations.empty
    assert len(result.parcels) == 1
    assert result.parcels.iloc[0]["planning_feature_document_id"] == DOCUMENT_ID
    if logical == "prescription_surface":
        assert fid_reads == 1


def _contract_result() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    ParcelPlanningFeaturesResult,
]:
    parcels = _parcels()
    layers = [
        _inspected(
            "prescription_surface",
            _source_frame(
                "prescription_surface",
                [_rectangle(0, 0, 10, 10)],
                ids=["SURFACE"],
            ),
        ),
        _inspected(
            "prescription_line",
            _source_frame(
                "prescription_line",
                [LineString([(-1, 5), (11, 5)])],
                ids=["LINE"],
            ),
        ),
        _inspected(
            "prescription_point",
            _source_frame("prescription_point", [Point(5, 5)], ids=["POINT"]),
        ),
    ]
    planning_document = _planning_document(layers)
    return (
        planning_document,
        parcels,
        intersect_parcels_with_gpu_planning_features(parcels, planning_document),
    )


def _source_complete_contract() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    ParcelPlanningFeaturesResult,
]:
    parcels = _parcels()
    layers = [
        _inspected(
            "prescription_surface",
            _source_frame(
                "prescription_surface",
                [_rectangle(0, 0, 10, 10)],
                ids=["SURFACE"],
                type_codes=["07"],
                subtype_codes=["04"],
            ),
        ),
        _inspected(
            "prescription_line",
            _source_frame(
                "prescription_line",
                [LineString([(-1, 5), (11, 5)])],
                ids=["LINE"],
                type_codes=["15"],
                subtype_codes=["00"],
            ),
        ),
        _inspected(
            "prescription_point",
            _source_frame(
                "prescription_point",
                [Point(5, 5)],
                ids=["POINT"],
                type_codes=["07"],
                subtype_codes=["00"],
            ),
        ),
    ]
    planning_document = _planning_document(layers)
    result = intersect_parcels_with_gpu_planning_features(parcels, planning_document)
    return planning_document, parcels, result


def _two_parcel_source_complete_contract() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    ParcelPlanningFeaturesResult,
]:
    """Build equal-area parcels so relation identity cannot hide behind area checks."""

    parcels = _parcels(
        [_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)],
        ids=["P-1", "P-2"],
    )
    layers = [
        _inspected(
            "prescription_surface",
            _source_frame(
                "prescription_surface",
                [_rectangle(0, 0, 10, 10)],
                ids=["SURFACE"],
                type_codes=["07"],
                subtype_codes=["04"],
            ),
        ),
        _inspected(
            "prescription_line",
            _source_frame(
                "prescription_line",
                [LineString([(0, 5), (10, 5)])],
                ids=["LINE"],
                type_codes=["15"],
                subtype_codes=["00"],
            ),
        ),
    ]
    planning_document = _planning_document(layers)
    result = intersect_parcels_with_gpu_planning_features(parcels, planning_document)
    return planning_document, parcels, result


def _validate_source_complete(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    result: ParcelPlanningFeaturesResult,
) -> PlanningFeatureInputValidation:
    return validate_normalized_planning_feature_inputs(
        planning_document,
        parcels,
        result.surface_features,
        result.line_features,
        result.point_features,
        result.relations,
    )


def _replace_related_layer(
    planning_document: GpuPlanningDocument,
    logical_name: str,
    frame: gpd.GeoDataFrame,
) -> GpuPlanningDocument:
    related: list[GpuInspectedLayer] = []
    for layer in planning_document.related_layers:
        if layer.logical_name != logical_name:
            related.append(layer)
            continue
        related.append(
            replace(
                layer,
                data=frame,
                summary=_summary(frame, layer.reference.source_layer),
            )
        )
    return replace(planning_document, related_layers=tuple(related))


def _without_related_layer(
    planning_document: GpuPlanningDocument,
    logical_name: str,
) -> GpuPlanningDocument:
    return replace(
        planning_document,
        related_layers=tuple(
            layer
            for layer in planning_document.related_layers
            if layer.logical_name != logical_name
        ),
    )


def _refresh_extraction_inventory(
    planning_document: GpuPlanningDocument,
) -> GpuPlanningDocument:
    extraction = planning_document.extraction
    files = _physical_inventory(extraction.extraction_root)
    _write_extraction_manifest(
        extraction.extraction_root,
        extraction.archive.sha256,
        files,
    )
    updated_extraction = replace(extraction, files=files)
    return replace(
        planning_document,
        extraction=updated_extraction,
        all_spatial_layers=gpu_source_module.discover_gpu_spatial_layers(
            updated_extraction
        ),
    )


def _replace_layer_reference(
    planning_document: GpuPlanningDocument,
    logical_name: str,
    reference: GpuSpatialLayerReference,
) -> GpuPlanningDocument:
    related = tuple(
        replace(layer, reference=reference)
        if layer.logical_name == logical_name
        else layer
        for layer in planning_document.related_layers
    )
    old_reference = next(
        layer.reference
        for layer in planning_document.related_layers
        if layer.logical_name == logical_name
    )
    spatial = tuple(
        reference if item == old_reference else item
        for item in planning_document.all_spatial_layers
    )
    return replace(
        planning_document,
        related_layers=related,
        all_spatial_layers=spatial,
    )


def test_public_normalized_input_contract_validates_step_7d_3_1_result() -> None:
    planning_document, parcels, result = _source_complete_contract()
    validation = validate_normalized_planning_feature_inputs(
        planning_document,
        parcels,
        result.surface_features,
        result.line_features,
        result.point_features,
        result.relations,
    )
    assert isinstance(validation, PlanningFeatureInputValidation)
    assert validation.related_source_layer_count == 3
    assert validation.related_source_file_count == 3
    assert validation.expected_relation_count == len(result.relations)
    for value in (
        validation.gpu_related_source_files_sha256,
        validation.expected_relations_content_sha256,
    ):
        assert len(value) == 64
        int(value, 16)


def test_public_normalized_input_contract_wraps_malformed_document_context() -> None:
    planning_document, parcels, result = _source_complete_contract()
    malformed = replace(planning_document, related_layers=(None,))  # type: ignore[arg-type]
    with pytest.raises(PlanningFeaturesError) as caught:
        _validate_source_complete(malformed, parcels, result)
    assert isinstance(caught.value.__cause__, (AttributeError, TypeError))


def test_source_complete_contract_binds_inspected_spatial_inventory() -> None:
    planning_document, parcels, result = _source_complete_contract()
    missing_inventory = replace(planning_document, all_spatial_layers=())
    with pytest.raises(PlanningFeaturesError, match="inventory|reference"):
        _validate_source_complete(missing_inventory, parcels, result)


def test_public_normalized_input_contract_is_exported() -> None:
    from landscout import stages

    assert (
        stages.validate_normalized_planning_feature_inputs
        is validate_normalized_planning_feature_inputs
    )
    assert "validate_normalized_planning_feature_inputs" in stages.__all__
    assert stages.PlanningFeatureInputValidation is PlanningFeatureInputValidation
    assert "PlanningFeatureInputValidation" in stages.__all__


def test_public_source_validation_hashes_survive_parquet_readback(
    tmp_path: Path,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    original = _validate_source_complete(planning_document, parcels, result)
    paths = {
        "surface_features": tmp_path / "surface.parquet",
        "line_features": tmp_path / "line.parquet",
        "point_features": tmp_path / "point.parquet",
        "relations": tmp_path / "relations.parquet",
    }
    result.surface_features.to_parquet(paths["surface_features"], index=False)
    result.line_features.to_parquet(paths["line_features"], index=False)
    result.point_features.to_parquet(paths["point_features"], index=False)
    result.relations.to_parquet(paths["relations"], index=False)
    validation = validate_normalized_planning_feature_inputs(
        planning_document,
        parcels,
        gpd.read_parquet(paths["surface_features"]),
        gpd.read_parquet(paths["line_features"]),
        gpd.read_parquet(paths["point_features"]),
        pd.read_parquet(paths["relations"]),
    )
    assert validation == original


def test_public_normalized_input_contract_rejects_stripped_catalog() -> None:
    planning_document, parcels, result = _source_complete_contract()
    surface = result.surface_features.drop(columns="label_raw")
    with pytest.raises(PlanningFeaturesError, match="schema|label_raw"):
        validate_normalized_planning_feature_inputs(
            planning_document,
            parcels,
            surface,
            result.line_features,
            result.point_features,
            result.relations,
        )


def test_empty_and_nonempty_catalogs_have_identical_kind_schemas() -> None:
    _, _, populated = _contract_result()
    empty = _run([])
    for populated_catalog, empty_catalog in zip(
        (
            populated.surface_features,
            populated.line_features,
            populated.point_features,
        ),
        (empty.surface_features, empty.line_features, empty.point_features),
        strict=True,
    ):
        assert list(empty_catalog.columns) == list(populated_catalog.columns)


@pytest.mark.parametrize("bad_count", [-1, 1.5, float("inf"), "2", True])
def test_strict_relation_integer_counts_are_enforced(bad_count: object) -> None:
    planning_document, source, result = _contract_result()
    relations = result.relations.copy(deep=True)
    relations["point_member_count"] = relations["point_member_count"].astype(object)
    point_index = relations.index[relations["geometry_kind"] == "POINT"][0]
    relations.loc[point_index, "point_member_count"] = bad_count
    with pytest.raises(
        PlanningFeaturesError, match="integer count|non-negative|dtype|schema"
    ):
        _validate_result(
            source,
            replace(result, relations=relations),
            planning_document=planning_document,
        )


@pytest.mark.parametrize("bad_count", [-1, 1.5, float("inf"), "2", True])
def test_strict_parcel_summary_integer_counts_are_enforced(
    bad_count: object,
) -> None:
    planning_document, source, result = _contract_result()
    parcels = result.parcels.copy(deep=True)
    parcels["planning_line_relation_count"] = parcels[
        "planning_line_relation_count"
    ].astype(object)
    parcels.loc[parcels.index[0], "planning_line_relation_count"] = bad_count
    with pytest.raises(PlanningFeaturesError, match="integer count|non-negative"):
        _validate_result(
            source,
            replace(result, parcels=parcels),
            planning_document=planning_document,
        )


@pytest.mark.parametrize(
    ("kind", "column", "value"),
    [
        ("SURFACE", "relation_type", "TOUCH_ONLY"),
        ("SURFACE", "parcel_share_pct", 42.0),
        ("SURFACE", "intersection_area_m2", None),
        ("SURFACE", "source_line_length_m", 0.0),
        ("LINE", "relation_type", "TOUCH_ONLY"),
        ("LINE", "intersection_length_m", 999.0),
        ("POINT", "relation_type", "BOUNDARY_TOUCH"),
    ],
)
def test_corrupted_relation_semantics_are_rejected(
    kind: str,
    column: str,
    value: object,
) -> None:
    planning_document, source, result = _contract_result()
    relations = result.relations.copy(deep=True)
    index = relations.index[relations["geometry_kind"] == kind][0]
    relations[column] = relations[column].astype(object)
    relations.loc[index, column] = value
    with pytest.raises(PlanningFeaturesError):
        _validate_result(
            source,
            replace(result, relations=relations),
            planning_document=planning_document,
        )


def test_point_member_relation_semantics_are_exact() -> None:
    planning_document, source, result = _contract_result()
    relations = result.relations.copy(deep=True)
    index = relations.index[relations["geometry_kind"] == "POINT"][0]
    relations.loc[index, "point_members_inside_count"] = 0
    relations.loc[index, "point_members_boundary_count"] = 1
    with pytest.raises(PlanningFeaturesError, match="relation type"):
        _validate_result(
            source,
            replace(result, relations=relations),
            planning_document=planning_document,
        )


@pytest.mark.parametrize(
    "case",
    [
        "surface-inside",
        "line-area",
        "point-touch",
        "area-zero",
        "surface-touch-positive",
        "length-zero",
        "line-touch-positive",
        "inside-zero",
        "boundary-with-inside",
        "area-exceeds-feature",
        "share-inconsistent",
        "non-finite",
        "negative",
    ],
)
def test_shared_intrinsic_relation_semantics_reject_every_invalid_case(
    case: str,
) -> None:
    _, _, result = _contract_result()
    relations = result.relations.copy(deep=True)
    surface = relations.index[relations["geometry_kind"].eq("SURFACE")][0]
    line = relations.index[relations["geometry_kind"].eq("LINE")][0]
    point = relations.index[relations["geometry_kind"].eq("POINT")][0]
    if case == "surface-inside":
        relations.loc[surface, "relation_type"] = "INSIDE"
    elif case == "line-area":
        relations.loc[line, "relation_type"] = "AREA_OVERLAP"
    elif case == "point-touch":
        relations.loc[point, "relation_type"] = "TOUCH_ONLY"
    elif case == "area-zero":
        relations.loc[
            surface, ["intersection_area_m2", "parcel_share_pct", "feature_share_pct"]
        ] = 0.0
    elif case == "surface-touch-positive":
        relations.loc[surface, "relation_type"] = "TOUCH_ONLY"
    elif case == "length-zero":
        relations.loc[line, "intersection_length_m"] = 0.0
    elif case == "line-touch-positive":
        relations.loc[line, "relation_type"] = "TOUCH_ONLY"
    elif case == "inside-zero":
        relations.loc[point, "point_members_inside_count"] = 0
    elif case == "boundary-with-inside":
        relations.loc[point, "relation_type"] = "BOUNDARY_TOUCH"
        relations.loc[point, "point_members_boundary_count"] = 1
    elif case == "area-exceeds-feature":
        relations.loc[surface, "intersection_area_m2"] = (
            float(relations.loc[surface, "feature_area_m2"]) + 1.0
        )
    elif case == "share-inconsistent":
        relations.loc[surface, "parcel_share_pct"] = 42.0
    elif case == "non-finite":
        relations.loc[surface, "feature_share_pct"] = float("inf")
    else:
        relations.loc[surface, "intersection_area_m2"] = -1.0
    with pytest.raises((TypeError, ValueError)):
        validate_intrinsic_planning_feature_relations(relations)


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("source_identity_kind", "NOT_A_KIND"),
        ("source_identity_field", "WRONG_FIELD"),
        ("feature_family", "INFORMATION"),
        ("geometry_kind", "LINE"),
        ("type_code_raw", "MUTATED"),
        ("source_archive_sha256", "b" * 64),
    ],
)
def test_relation_must_match_feature_catalog(
    column: str,
    value: object,
) -> None:
    planning_document, source, result = _contract_result()
    relations = result.relations.copy(deep=True)
    index = relations.index[0]
    if column == "geometry_kind":
        index = relations.index[relations["geometry_kind"].eq("SURFACE")][0]
    relations.loc[index, column] = value
    with pytest.raises(
        PlanningFeaturesError,
        match="catalog|geometry kind|LINE relation|unrelated metric",
    ):
        _validate_result(
            source,
            replace(result, relations=relations),
            planning_document=planning_document,
        )


def test_feature_ids_are_globally_unique_across_catalogs() -> None:
    planning_document, source, result = _contract_result()
    points = result.point_features.copy(deep=True)
    points.loc[points.index[0], "planning_feature_id"] = result.surface_features.iloc[
        0
    ]["planning_feature_id"]
    with pytest.raises(PlanningFeaturesError, match="globally unique|deterministic"):
        _validate_result(
            source,
            replace(result, point_features=points),
            planning_document=planning_document,
        )


def test_same_source_id_is_allowed_in_distinct_logical_layers() -> None:
    result = _run(
        [
            _inspected(
                "prescription_line",
                _source_frame(
                    "prescription_line",
                    [LineString([(0, 2), (10, 2)])],
                    ids=["SHARED"],
                ),
            ),
            _inspected(
                "prescription_point",
                _source_frame("prescription_point", [Point(5, 5)], ids=["SHARED"]),
            ),
        ]
    )
    assert len(result.relations) == 2
    assert result.relations["planning_feature_id"].nunique() == 2


def test_corrupted_parcel_summary_is_rejected() -> None:
    planning_document, source, result = _contract_result()
    parcels = result.parcels.copy(deep=True)
    parcels.loc[parcels.index[0], "planning_surface_relation_count"] += 1
    with pytest.raises(PlanningFeaturesError, match="inconsistent with relations"):
        _validate_result(
            source,
            replace(result, parcels=parcels),
            planning_document=planning_document,
        )


def test_corrupted_surface_union_contract_is_rejected() -> None:
    planning_document, source, result = _contract_result()
    parcels = result.parcels.copy(deep=True)
    parcels.loc[parcels.index[0], "planning_surface_covered_union_area_m2"] = 1000.0
    with pytest.raises(PlanningFeaturesError, match="union"):
        _validate_result(
            source,
            replace(result, parcels=parcels),
            planning_document=planning_document,
        )


def test_geospatial_operation_failure_is_controlled_and_chained(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fail_join(*args: object, **kwargs: object) -> object:
        raise RuntimeError("synthetic spatial-index failure")

    monkeypatch.setattr(planning_features_module.gpd, "sjoin", fail_join)
    layer = _inspected(
        "prescription_line",
        _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]),
    )
    with pytest.raises(PlanningFeaturesError, match="spatial join") as caught:
        _run([layer])
    assert isinstance(caught.value.__cause__, RuntimeError)


def test_source_complete_contract_rejects_unknown_relation_parcel() -> None:
    planning_document, parcels, result = _source_complete_contract()
    relations = result.relations.copy(deep=True)
    relations.loc[relations.index[0], "parcel_id"] = "NOT-A-SOURCE-PARCEL"
    corrupted = replace(result, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="parcel|source"):
        _validate_source_complete(planning_document, parcels, corrupted)


def test_source_complete_contract_rejects_coherent_parcel_metric_mutation() -> None:
    planning_document, parcels, result = _source_complete_contract()
    relations = result.relations.copy(deep=True)
    surface_mask = relations["geometry_kind"].eq("SURFACE")
    relations.loc[surface_mask, "parcel_metric_area_m2"] = 200.0
    relations.loc[surface_mask, "parcel_share_pct"] = 50.0
    corrupted = replace(result, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="parcel|metric|source"):
        _validate_source_complete(planning_document, parcels, corrupted)


def test_source_complete_contract_rejects_same_area_wrong_parcel_relation() -> None:
    planning_document, parcels, result = _two_parcel_source_complete_contract()
    relations = result.relations.copy(deep=True)
    relations.loc[relations.index[0], "parcel_id"] = "P-2"
    corrupted = replace(result, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="relation|parcel|rebuilt|source"):
        _validate_source_complete(planning_document, parcels, corrupted)


def test_source_complete_contract_rejects_missing_expected_relation() -> None:
    planning_document, parcels, result = _two_parcel_source_complete_contract()
    corrupted = replace(result, relations=result.relations.iloc[1:].copy())
    with pytest.raises(PlanningFeaturesError, match="relation|rebuilt|source"):
        _validate_source_complete(planning_document, parcels, corrupted)


def test_source_complete_contract_rejects_extra_geometrically_false_relation() -> None:
    planning_document, parcels, result = _two_parcel_source_complete_contract()
    extra = result.relations.iloc[[0]].copy(deep=True)
    extra.loc[extra.index[0], "parcel_id"] = "P-2"
    relations = pd.concat([result.relations, extra], ignore_index=True)
    corrupted = replace(result, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="relation|rebuilt|source"):
        _validate_source_complete(planning_document, parcels, corrupted)


def test_source_complete_contract_rejects_reordered_relations() -> None:
    planning_document, parcels, result = _two_parcel_source_complete_contract()
    relations = result.relations.iloc[::-1].reset_index(drop=True)
    corrupted = replace(result, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="relation|order|rebuilt"):
        _validate_source_complete(planning_document, parcels, corrupted)


@pytest.mark.parametrize(
    ("column", "dtype"),
    [
        ("intersection_area_m2", "object"),
        ("point_member_count", "object"),
        ("relation_type", "category"),
    ],
)
def test_source_complete_contract_rejects_noncanonical_relation_dtype(
    column: str,
    dtype: str,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    relations = result.relations.copy(deep=True)
    relations[column] = relations[column].astype(dtype)
    with pytest.raises(PlanningFeaturesError, match="schema|dtype|relation"):
        _validate_source_complete(
            planning_document, parcels, replace(result, relations=relations)
        )


def test_source_complete_contract_rejects_relation_index_name_change() -> None:
    planning_document, parcels, result = _source_complete_contract()
    relations = result.relations.copy(deep=True)
    relations.index = relations.index.rename("changed_relation_row")
    with pytest.raises(PlanningFeaturesError, match="schema|index|relation"):
        _validate_source_complete(
            planning_document, parcels, replace(result, relations=relations)
        )


def test_source_complete_contract_rejects_relation_index_dtype_change() -> None:
    planning_document, parcels, result = _source_complete_contract()
    relations = result.relations.copy(deep=True)
    relations.index = pd.Index(
        np.asarray(relations.index, dtype="int32"),
        name=relations.index.name,
    )
    assert str(relations.index.dtype) == "int32"
    with pytest.raises(PlanningFeaturesError, match="schema|index|relation"):
        _validate_source_complete(
            planning_document, parcels, replace(result, relations=relations)
        )


def test_source_complete_contract_rejects_relation_index_class_change() -> None:
    planning_document, parcels, result = _source_complete_contract()
    assert type(result.relations.index) is pd.RangeIndex
    relations = result.relations.copy(deep=True)
    relations.index = pd.Index(relations.index.to_numpy(), dtype="int64")
    assert type(relations.index) is pd.Index
    with pytest.raises(PlanningFeaturesError, match="schema|index|relation"):
        validate_normalized_planning_feature_inputs(
            planning_document,
            parcels,
            result.surface_features,
            result.line_features,
            result.point_features,
            relations,
        )


def test_expected_relation_hash_binds_dtype_and_index_metadata() -> None:
    _, _, result = _source_complete_contract()
    original = planning_features_module._expected_relations_content_sha256(
        result.relations
    )
    object_dtype = result.relations.copy(deep=True)
    object_dtype["intersection_area_m2"] = object_dtype["intersection_area_m2"].astype(
        "object"
    )
    named_index = result.relations.copy(deep=True)
    named_index.index = named_index.index.rename("relation_row")
    int32_index = result.relations.copy(deep=True)
    int32_index.index = pd.Index(
        np.asarray(int32_index.index, dtype="int32"),
        name=int32_index.index.name,
    )
    index_class = result.relations.copy(deep=True)
    index_class.index = pd.Index(index_class.index.to_numpy(), dtype="int64")
    assert original != planning_features_module._expected_relations_content_sha256(
        object_dtype
    )
    assert original != planning_features_module._expected_relations_content_sha256(
        named_index
    )
    assert original != planning_features_module._expected_relations_content_sha256(
        int32_index
    )
    assert original != planning_features_module._expected_relations_content_sha256(
        index_class
    )


def test_source_complete_contract_rejects_coherent_but_wrong_line_metric() -> None:
    planning_document, parcels, result = _two_parcel_source_complete_contract()
    relations = result.relations.copy(deep=True)
    line_mask = relations["geometry_kind"].eq("LINE")
    relations.loc[line_mask, "intersection_length_m"] = 5.0
    corrupted = replace(result, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="relation|metric|rebuilt"):
        _validate_source_complete(planning_document, parcels, corrupted)


def test_source_complete_contract_accepts_complete_parcel_output_summaries() -> None:
    planning_document, _, result = _source_complete_contract()
    _validate_source_complete(planning_document, result.parcels, result)


def test_source_complete_contract_rejects_partial_parcel_output_columns() -> None:
    planning_document, parcels, result = _source_complete_contract()
    partial = parcels.copy(deep=True)
    partial["planning_surface_relation_count"] = 1
    with pytest.raises(PlanningFeaturesError, match="[Pp]arcel|output|summary|columns"):
        _validate_source_complete(planning_document, partial, result)


def test_source_complete_contract_rejects_corrupted_complete_parcel_summaries() -> None:
    planning_document, _, result = _source_complete_contract()
    corrupted = result.parcels.copy(deep=True)
    corrupted.loc[corrupted.index[0], "planning_surface_relation_count"] += 1
    with pytest.raises(PlanningFeaturesError, match="parcel|summary|relation"):
        _validate_source_complete(planning_document, corrupted, result)


def test_source_complete_contract_rejects_noncanonical_parcel_summary_dtype() -> None:
    planning_document, _, result = _source_complete_contract()
    corrupted = result.parcels.copy(deep=True)
    corrupted["planning_surface_covered_pct"] = corrupted[
        "planning_surface_covered_pct"
    ].astype("float32")
    with pytest.raises(PlanningFeaturesError, match="parcel|schema|dtype|summary"):
        _validate_source_complete(planning_document, corrupted, result)


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("planning_feature_document_id", "other-document"),
        ("planning_feature_archive_sha256", "f" * 64),
        ("planning_surface_covered_union_area_m2", 50.0),
        ("planning_surface_covered_pct", 50.0),
        ("planning_line_intersection_length_sum_m", 5.0),
        ("planning_point_inside_count", 0),
    ],
)
def test_source_complete_contract_rejects_each_corrupted_parcel_summary_fact(
    column: str,
    value: object,
) -> None:
    planning_document, _, result = _source_complete_contract()
    corrupted = result.parcels.copy(deep=True)
    corrupted.loc[corrupted.index[0], column] = value
    with pytest.raises(
        PlanningFeaturesError,
        match="parcel|summary|relation|lineage|document|archive|union|percentage",
    ):
        _validate_source_complete(planning_document, corrupted, result)


def test_source_complete_contract_rejects_duplicate_parcel_ids() -> None:
    planning_document, parcels, result = _source_complete_contract()
    duplicate = pd.concat([parcels, parcels], ignore_index=True)
    duplicate = gpd.GeoDataFrame(duplicate, geometry="geometry", crs=parcels.crs)
    with pytest.raises(PlanningFeaturesError, match="parcel_id|unique"):
        _validate_source_complete(planning_document, duplicate, result)


def test_source_complete_contract_rejects_invalid_parcel_geometry() -> None:
    planning_document, parcels, result = _source_complete_contract()
    invalid = parcels.copy(deep=True)
    invalid.at[invalid.index[0], "geometry"] = Polygon(
        [(0, 0), (10, 10), (10, 0), (0, 10), (0, 0)]
    )
    with pytest.raises(PlanningFeaturesError, match="valid|geometry"):
        _validate_source_complete(planning_document, invalid, result)


def test_source_complete_contract_accepts_epsg4326_parcels() -> None:
    planning_document, parcels, _ = _source_complete_contract()
    geographic = parcels.to_crs("EPSG:4326")
    result = intersect_parcels_with_gpu_planning_features(geographic, planning_document)
    _validate_source_complete(planning_document, geographic, result)


def test_source_document_reference_allows_one_archive_zip_suffix() -> None:
    planning_document, parcels, _ = _source_complete_contract()
    archive = planning_document.extraction.archive
    metadata = replace(archive.document, archive_name=f"{ARCHIVE_NAME}.zip")
    suffixed = replace(
        planning_document,
        extraction=replace(
            planning_document.extraction,
            archive=replace(archive, document=metadata),
        ),
    )
    result = intersect_parcels_with_gpu_planning_features(parcels, suffixed)
    assert (
        result.surface_features["source_archive_name"].eq(f"{ARCHIVE_NAME}.zip").all()
    )
    assert (
        result.surface_features["source_document_reference_raw"].eq(ARCHIVE_NAME).all()
    )
    _validate_source_complete(suffixed, parcels, result)


@pytest.mark.parametrize(
    "identity_column", ["planning_feature_id", "source_feature_id"]
)
def test_source_complete_contract_rejects_coherently_renamed_feature_identity(
    identity_column: str,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    surface = result.surface_features.copy(deep=True)
    relations = result.relations.copy(deep=True)
    old = surface.iloc[0][identity_column]
    new = (
        f"GPU:{DOCUMENT_ID}:prescription_surface:RENAMED"
        if identity_column == "planning_feature_id"
        else "RENAMED"
    )
    surface.loc[surface.index[0], identity_column] = new
    relations.loc[relations[identity_column].eq(old), identity_column] = new
    corrupted = replace(result, surface_features=surface, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="source|identity|rebuilt|catalog"):
        _validate_source_complete(planning_document, parcels, corrupted)


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("source_provider", "Another provider"),
        ("source_portal", "https://example.invalid"),
        ("source_commune_code", "99999"),
        ("source_document_type", "CC"),
        ("source_archive_name", "OTHER_ARCHIVE"),
        ("source_document_reference_raw", "OTHER_ARCHIVE"),
        ("source_layer", "OTHER_SOURCE_LAYER"),
        ("source_crs", "EPSG:4326"),
    ],
)
def test_source_complete_contract_rejects_independent_gpu_lineage_mutation(
    column: str,
    value: str,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    surface = result.surface_features.copy(deep=True)
    relations = result.relations.copy(deep=True)
    surface.loc[surface.index[0], column] = value
    if column in relations.columns:
        feature_id = result.surface_features.iloc[0]["planning_feature_id"]
        relations.loc[relations["planning_feature_id"].eq(feature_id), column] = value
    corrupted = replace(result, surface_features=surface, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="source|lineage|catalog|rebuilt"):
        _validate_source_complete(planning_document, parcels, corrupted)


@pytest.mark.parametrize(
    ("metadata_field", "value"),
    [
        ("provider", "Another provider"),
        ("portal", "https://example.invalid"),
        ("commune_code", "99999"),
        ("document_type", "CC"),
        ("archive_name", "OTHER_ARCHIVE"),
    ],
)
def test_source_complete_contract_binds_gpu_document_context(
    metadata_field: str,
    value: str,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    archive = planning_document.extraction.archive
    metadata = replace(archive.document, **{metadata_field: value})
    changed = replace(
        planning_document,
        extraction=replace(
            planning_document.extraction,
            archive=replace(archive, document=metadata),
        ),
    )
    with pytest.raises(
        PlanningFeaturesError,
        match="source|lineage|document|rebuilt|IDURBA|archive",
    ):
        _validate_source_complete(changed, parcels, result)


@pytest.mark.parametrize("mutation", ["geometry", "raw", "code", "remove", "extra"])
def test_source_complete_contract_reloads_and_compares_source_catalog(
    mutation: str,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    layer = next(
        layer
        for layer in planning_document.related_layers
        if layer.logical_name == "prescription_surface"
    )
    frame = layer.data.copy(deep=True)
    if mutation == "geometry":
        frame.at[frame.index[0], "geometry"] = _rectangle(0, 0, 5, 10)
    elif mutation == "raw":
        frame.loc[frame.index[0], "LIBELLE"] = "Changed source label"
    elif mutation == "code":
        frame.loc[frame.index[0], ["TYPEPSC", "STYPEPSC"]] = ["01", "00"]
    elif mutation == "remove":
        frame = frame.iloc[0:0].copy()
    else:
        extra = frame.copy(deep=True)
        extra.loc[extra.index[0], "LIB_IDPSC"] = "EXTRA"
        extra.at[extra.index[0], "geometry"] = _rectangle(20, 20, 21, 21)
        frame = gpd.GeoDataFrame(
            pd.concat([frame, extra], ignore_index=True),
            geometry="geometry",
            crs=frame.crs,
        )
    changed = _replace_related_layer(planning_document, "prescription_surface", frame)
    with pytest.raises(
        PlanningFeaturesError, match="source|catalog|rebuilt|normalized"
    ):
        _validate_source_complete(changed, parcels, result)


def test_source_complete_contract_rejects_catalog_for_absent_gpu_layer() -> None:
    planning_document, parcels, result = _source_complete_contract()
    changed = _without_related_layer(planning_document, "prescription_surface")
    with pytest.raises(PlanningFeaturesError, match="source|layer|catalog|rebuilt"):
        _validate_source_complete(changed, parcels, result)


@pytest.mark.parametrize(
    ("catalog_name", "geometry"),
    [
        (
            "surface_features",
            Polygon([(0, 0, 1), (0, 10, 1), (10, 10, 1), (10, 0, 1)]),
        ),
        ("line_features", LineString([(-1, 5, 1), (11, 5, 1)])),
        ("point_features", Point(5, 5, 1)),
    ],
)
def test_three_dimensional_normalized_catalogs_are_rejected(
    catalog_name: str,
    geometry: object,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    catalog = getattr(result, catalog_name).copy(deep=True)
    catalog.at[catalog.index[0], "geometry"] = geometry
    corrupted = replace(result, **{catalog_name: catalog})
    with pytest.raises(PlanningFeaturesError, match="2D|dimensional|Z"):
        _validate_source_complete(planning_document, parcels, corrupted)


def test_two_dimensional_normalized_catalogs_remain_valid() -> None:
    planning_document, parcels, result = _source_complete_contract()
    for catalog in (
        result.surface_features,
        result.line_features,
        result.point_features,
    ):
        assert not catalog.geometry.has_z.any()
    _validate_source_complete(planning_document, parcels, result)


@pytest.mark.parametrize(
    ("logical", "geometry", "catalog_name"),
    [
        (
            "prescription_surface",
            Polygon([(0, 0, 1), (0, 10, 1), (10, 10, 1), (10, 0, 1)]),
            "surface_features",
        ),
        (
            "prescription_line",
            LineString([(0, 5, 1), (10, 5, 1)]),
            "line_features",
        ),
        ("prescription_point", Point(5, 5, 1), "point_features"),
    ],
)
def test_gpu_source_z_is_normalized_to_canonical_2d(
    logical: str,
    geometry: object,
    catalog_name: str,
) -> None:
    result = _run([_inspected(logical, _source_frame(logical, [geometry]))])
    catalog = getattr(result, catalog_name)
    assert not catalog.geometry.has_z.any()


def test_source_complete_contract_rejects_tampered_gpkg_inventory_hash() -> None:
    planning_document, parcels, result = _source_complete_contract()
    layer = planning_document.related_layers[0]
    relative = layer.reference.dataset_path.relative_to(
        planning_document.extraction.extraction_root
    ).as_posix()
    files = tuple(
        replace(item, sha256="f" * 64) if item.relative_path == relative else item
        for item in planning_document.extraction.files
    )
    changed = replace(
        planning_document,
        extraction=replace(planning_document.extraction, files=files),
    )
    with pytest.raises(PlanningFeaturesError, match="source|file|inventory|SHA"):
        _validate_source_complete(changed, parcels, result)


def test_source_complete_contract_rejects_tampered_gpkg_size() -> None:
    planning_document, parcels, result = _source_complete_contract()
    layer = planning_document.related_layers[0]
    relative = layer.reference.dataset_path.relative_to(
        planning_document.extraction.extraction_root
    ).as_posix()
    files = tuple(
        replace(item, size_bytes=item.size_bytes + 1)
        if item.relative_path == relative
        else item
        for item in planning_document.extraction.files
    )
    changed = replace(
        planning_document,
        extraction=replace(planning_document.extraction, files=files),
    )
    with pytest.raises(PlanningFeaturesError, match="source|file|inventory|size"):
        _validate_source_complete(changed, parcels, result)


def test_source_complete_contract_rejects_changed_gpkg_bytes() -> None:
    planning_document, parcels, result = _source_complete_contract()
    path = planning_document.related_layers[0].reference.dataset_path
    with path.open("ab") as stream:
        stream.write(b"tamper")
    with pytest.raises(PlanningFeaturesError, match="source|file|inventory|size|SHA"):
        _validate_source_complete(planning_document, parcels, result)


def test_source_complete_contract_rejects_same_size_gpkg_byte_tamper() -> None:
    planning_document, parcels, result = _source_complete_contract()
    path = planning_document.related_layers[0].reference.dataset_path
    payload = bytearray(path.read_bytes())
    payload[-1] ^= 1
    path.write_bytes(payload)
    with pytest.raises(PlanningFeaturesError, match="source|file|inventory|SHA"):
        _validate_source_complete(planning_document, parcels, result)


def test_source_complete_contract_rejects_coherently_changed_physical_gpkg() -> None:
    planning_document, parcels, result = _source_complete_contract()
    layer = planning_document.related_layers[0]
    changed_source = layer.data.copy(deep=True)
    changed_source.loc[changed_source.index[0], "LIBELLE"] = "Changed on disk"
    changed_source.to_file(
        layer.reference.dataset_path,
        layer=layer.reference.source_layer,
        driver="GPKG",
        engine="pyogrio",
        index=False,
    )
    coherent_inventory = _refresh_extraction_inventory(planning_document)
    with pytest.raises(PlanningFeaturesError, match="source|file|loaded|changed"):
        _validate_source_complete(coherent_inventory, parcels, result)


def test_source_complete_contract_rejects_changed_physical_gpkg_geometry() -> None:
    planning_document, parcels, result = _source_complete_contract()
    layer = planning_document.related_layers[0]
    changed_source = layer.data.copy(deep=True)
    changed_source.at[changed_source.index[0], "geometry"] = _rectangle(0, 0, 5, 10)
    changed_source.to_file(
        layer.reference.dataset_path,
        layer=layer.reference.source_layer,
        driver="GPKG",
        engine="pyogrio",
        index=False,
    )
    coherent_inventory = _refresh_extraction_inventory(planning_document)
    with pytest.raises(PlanningFeaturesError, match="source|geometry|loaded|changed"):
        _validate_source_complete(coherent_inventory, parcels, result)


def test_source_complete_contract_rejects_reordered_physical_gpkg_rows() -> None:
    parcels = _parcels(
        [_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)],
        ids=["P-1", "P-2"],
    )
    layer = _inspected(
        "prescription_surface",
        _source_frame(
            "prescription_surface",
            [_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)],
            ids=["ONE", "TWO"],
            type_codes=["07", "07"],
            subtype_codes=["04", "04"],
        ),
    )
    planning_document = _planning_document([layer])
    result = intersect_parcels_with_gpu_planning_features(parcels, planning_document)
    stored = planning_document.related_layers[0]
    stored.data.iloc[::-1].reset_index(drop=True).to_file(
        stored.reference.dataset_path,
        layer=stored.reference.source_layer,
        driver="GPKG",
        engine="pyogrio",
        index=False,
    )
    coherent_inventory = _refresh_extraction_inventory(planning_document)
    with pytest.raises(PlanningFeaturesError, match="source|order|loaded|changed"):
        _validate_source_complete(coherent_inventory, parcels, result)


def test_source_complete_contract_rejects_loaded_source_attrs_not_on_disk() -> None:
    planning_document, parcels, result = _source_complete_contract()
    layer = planning_document.related_layers[0]
    loaded = layer.data.copy(deep=True)
    loaded.attrs["unpersisted_source_note"] = "tampered"
    changed = replace(
        planning_document,
        related_layers=tuple(
            replace(item, data=loaded) if item is layer else item
            for item in planning_document.related_layers
        ),
    )
    with pytest.raises(PlanningFeaturesError, match="source|attrs|metadata|loaded"):
        _validate_source_complete(changed, parcels, result)


def test_source_complete_contract_rejects_dataset_outside_extraction_root(
    tmp_path: Path,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    layer = planning_document.related_layers[0]
    outside = tmp_path / "outside.gpkg"
    shutil.copyfile(layer.reference.dataset_path, outside)
    reference = replace(layer.reference, dataset_path=outside)
    changed = _replace_layer_reference(planning_document, layer.logical_name, reference)
    with pytest.raises(PlanningFeaturesError, match="source|root|outside|contain"):
        _validate_source_complete(changed, parcels, result)


def test_source_complete_contract_rejects_linked_spatial_dataset(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    dataset = planning_document.related_layers[0].reference.dataset_path
    actual_link_check = gpu_source_module._is_link_or_junction

    def synthetic_link(path: Path) -> bool:
        return path == dataset or actual_link_check(path)

    monkeypatch.setattr(
        gpu_source_module,
        "_is_link_or_junction",
        synthetic_link,
    )
    with pytest.raises(PlanningFeaturesError, match="source|link|junction|dataset"):
        _validate_source_complete(planning_document, parcels, result)


def _shapefile_source_complete_contract(
    root: Path,
) -> tuple[GpuPlanningDocument, gpd.GeoDataFrame, ParcelPlanningFeaturesResult]:
    source_layer = "PRESCRIPTION_SURFACE"
    path = root / f"{source_layer}.shp"
    frame = _source_frame(
        "prescription_surface",
        [_rectangle(0, 0, 10, 10)],
        ids=["SHAPE-1"],
        type_codes=["07"],
        subtype_codes=["04"],
    )
    frame.to_file(path, driver="ESRI Shapefile", engine="pyogrio", index=False)
    loaded = gpd.read_file(path, engine="pyogrio")
    layer = replace(
        _inspected("prescription_surface", loaded),
        reference=GpuSpatialLayerReference(path, source_layer, "ESRI Shapefile"),
        summary=_summary(loaded, source_layer),
    )
    document = _planning_document([layer])
    parcels = _parcels()
    result = intersect_parcels_with_gpu_planning_features(parcels, document)
    return document, parcels, result


def _shapefile_ogr_fid_source_complete_contract(
    root: Path,
) -> tuple[GpuPlanningDocument, gpd.GeoDataFrame, ParcelPlanningFeaturesResult]:
    source_layer = "PRESCRIPTION_SURFACE"
    path = root / f"{source_layer}.shp"
    frame = _source_frame(
        "prescription_surface",
        [_rectangle(0, 0, 5, 10), _rectangle(5, 0, 10, 10)],
        ids=["DROP-ONE", "DROP-TWO"],
        type_codes=["07", "07"],
        subtype_codes=["04", "04"],
    ).drop(columns="LIB_IDPSC")
    frame.to_file(path, driver="ESRI Shapefile", engine="pyogrio", index=False)
    loaded = gpd.read_file(path, engine="pyogrio")
    layer = replace(
        _inspected("prescription_surface", loaded),
        reference=GpuSpatialLayerReference(path, source_layer, "ESRI Shapefile"),
        summary=_summary(loaded, source_layer),
    )
    document = _planning_document([layer])
    parcels = _parcels()
    result = intersect_parcels_with_gpu_planning_features(parcels, document)
    return document, parcels, result


def test_source_complete_contract_binds_every_shapefile_sidecar(
    tmp_path: Path,
) -> None:
    planning_document, parcels, result = _shapefile_source_complete_contract(tmp_path)
    sidecar = next(
        item
        for item in planning_document.extraction.files
        if item.relative_path.casefold().endswith(".prj")
    )
    files = tuple(
        item
        for item in planning_document.extraction.files
        if item.relative_path != sidecar.relative_path
    )
    changed = replace(
        planning_document,
        extraction=replace(planning_document.extraction, files=files),
    )
    with pytest.raises(
        PlanningFeaturesError,
        match="shapefile|sidecar|inventory|physical revalidation",
    ):
        _validate_source_complete(changed, parcels, result)


@pytest.mark.parametrize("changed_fids", [(10, 11), (1, 0)])
def test_source_complete_contract_rejects_changed_or_reordered_ogr_fids(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    changed_fids: tuple[int, int],
) -> None:
    planning_document, parcels, result = _shapefile_ogr_fid_source_complete_contract(
        tmp_path
    )
    actual_read = gpu_source_module.pyogrio.read_dataframe

    def changed_fid_read(*args: object, **kwargs: object) -> gpd.GeoDataFrame:
        reread = actual_read(*args, **kwargs)
        if kwargs.get("fid_as_index"):
            reread.index = pd.Index(changed_fids, name="fid")
        return reread

    monkeypatch.setattr(
        gpu_source_module.pyogrio,
        "read_dataframe",
        changed_fid_read,
    )
    with pytest.raises(PlanningFeaturesError, match="source|FID|identity|catalog"):
        _validate_source_complete(planning_document, parcels, result)


def test_source_complete_contract_requires_shapefile_core_members(
    tmp_path: Path,
) -> None:
    planning_document, parcels, result = _shapefile_source_complete_contract(tmp_path)
    layer = planning_document.related_layers[0]
    layer.reference.dataset_path.with_suffix(".shx").unlink()
    with pytest.raises(PlanningFeaturesError, match="shapefile|shx|source|file"):
        _validate_source_complete(planning_document, parcels, result)


def test_source_complete_contract_rejects_changed_shapefile_sidecar_bytes(
    tmp_path: Path,
) -> None:
    planning_document, parcels, result = _shapefile_source_complete_contract(tmp_path)
    layer = planning_document.related_layers[0]
    cpg = layer.reference.dataset_path.with_suffix(".cpg")
    cpg.write_text("UTF-8\n", encoding="utf-8")
    with pytest.raises(
        PlanningFeaturesError,
        match="shapefile|sidecar|size|SHA|physical revalidation",
    ):
        _validate_source_complete(planning_document, parcels, result)


def test_dotted_sibling_dataset_is_not_a_sidecar_and_makes_role_ambiguous(
    tmp_path: Path,
) -> None:
    planning_document, parcels, result = _shapefile_source_complete_contract(tmp_path)
    _validate_source_complete(planning_document, parcels, result)
    primary = planning_document.related_layers[0].reference.dataset_path
    sibling = primary.with_name(f"{primary.stem}.archive.shp")
    gpd.GeoDataFrame(
        {"sibling": [1]},
        geometry=[_rectangle(20, 20, 21, 21)],
        crs="EPSG:2154",
    ).to_file(sibling, driver="ESRI Shapefile", engine="pyogrio", index=False)
    refreshed = _refresh_extraction_inventory(planning_document)
    with pytest.raises(
        PlanningFeaturesError,
        match="Related GPU spatial sources failed physical revalidation",
    ):
        _validate_source_complete(refreshed, parcels, result)


@pytest.mark.parametrize("bad_item", [None, object()])
def test_batch_gpu_revalidation_rejects_malformed_layer_items(
    bad_item: object,
) -> None:
    planning_document, _, _ = _source_complete_contract()
    with pytest.raises(gpu_source_module.GpuSpatialInspectionError):
        gpu_source_module.revalidate_gpu_spatial_layer_sources(
            planning_document,
            (bad_item,),  # type: ignore[arg-type]
        )


def test_batch_gpu_revalidation_rejects_malformed_planning_document() -> None:
    with pytest.raises(gpu_source_module.GpuSpatialInspectionError):
        gpu_source_module.revalidate_gpu_spatial_layer_sources(
            object(),  # type: ignore[arg-type]
            (),
        )


def test_batch_gpu_revalidation_rejects_duplicate_logical_name() -> None:
    planning_document, _, _ = _source_complete_contract()
    layer = planning_document.related_layers[0]
    with pytest.raises(gpu_source_module.GpuSpatialInspectionError, match="duplicate"):
        gpu_source_module.revalidate_gpu_spatial_layer_sources(
            planning_document,
            (layer, layer),
        )


@pytest.mark.parametrize(
    "statement",
    [
        (
            "from landscout.common.planning_feature_contract import "
            "validate_intrinsic_planning_feature_relations"
        ),
        (
            "from landscout.common.bess_application_contract import "
            "validate_bess_application_feature_catalogs"
        ),
    ],
)
def test_common_planning_contracts_import_without_initializing_stages(
    statement: str,
) -> None:
    completed = subprocess.run(
        [
            sys.executable,
            "-c",
            f"import sys; {statement}; assert 'landscout.stages' not in sys.modules",
        ],
        cwd=Path(__file__).resolve().parents[2],
        capture_output=True,
        check=False,
        text=True,
    )
    assert completed.returncode == 0, completed.stderr
```

# `tests/unit/test_enrich_planning_zoning.py`

## File identity

- Repository path: `tests/unit/test_enrich_planning_zoning.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Provides complete unit and regression coverage for the `enrich_planning_zoning` contracts exercised in this file.
- Source SHA256: `0a5dfb7650061c6492f0d298c9dbd43d011a715c12fd6eb135347e5e6185b821`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for enrich planning zoning; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Provides complete unit and regression coverage for the `enrich_planning_zoning` contracts exercised in this file.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import importlib`
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
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- `from landscout.stages.enrich_planning_zoning import (
    PARCEL_ZONING_OUTPUT_COLUMNS,
    ParcelZoningResult,
    PlanningZoningError,
    _stabilize_area_relationships,
    intersect_parcels_with_gpu_zoning,
    validate_normalized_planning_zoning_inputs,
)`
- `from landscout.stages.planning_overlay import technical_overlay_tolerance`
- `import landscout.stages.enrich_planning_zoning as module`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `ARCHIVE_SHA256`

- Category: module constant or closed domain.
- Exact declaration:

```python
ARCHIVE_SHA256 = "a" * 64
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

### `DOCUMENT_ID`

- Category: module constant or closed domain.
- Exact declaration:

```python
DOCUMENT_ID = "doc-1"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `SOURCE_LAYER`

- Category: module constant or closed domain.
- Exact declaration:

```python
SOURCE_LAYER = "31395_ZONE_URBA_20240215"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `STANDARD_MODEL`

- Category: module constant or closed domain.
- Exact declaration:

```python
STANDARD_MODEL = "CNIG PLU v2017"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `SOURCE_FIELDS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `LIB_IDZONE`
  - `LIBELLE`
  - `LIBELONG`
  - `TYPEZONE`
  - `NOMFIC`
  - `URLFIC`
  - `IDURBA`
  - `DATVALID`

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

### `test_shared_overlay_tolerance_preserves_zoning_numerical_behavior`

**Purpose:** Regression invariant: shared overlay tolerance preserves zoning numerical behavior. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_shared_overlay_tolerance_preserves_zoning_numerical_behavior() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningZoningError, match="materially exceeds")`
- Exact assertions:
  - `assert technical_overlay_tolerance(100.0) == pytest.approx(1e-6)`
  - `assert covered == pytest.approx(100.0)`
  - `assert gap == pytest.approx(0.0)`
  - `assert excess == pytest.approx(5e-7)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `technical_overlay_tolerance` | `landscout.stages.planning_overlay.technical_overlay_tolerance` |
| `pytest.approx` | `pytest.approx` |
| `_stabilize_area_relationships` | `landscout.stages.enrich_planning_zoning._stabilize_area_relationships` |
| `pytest.raises` | `pytest.raises` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `technical_overlay_tolerance` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_rectangle`

**Purpose:** Implements `rectangle` within the file role: Provides complete unit and regression coverage for the `enrich_planning_zoning` contracts exercised in this file.

**Exact signature**

```python
def _rectangle(x_min: float, y_min: float, x_max: float, y_max: float) -> Polygon:
```

- Exact decorators: none.
- Declared return annotation: `Polygon`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `x_min` | positional-or-keyword | `float` | `required` |
| `y_min` | positional-or-keyword | `float` | `required` |
| `x_max` | positional-or-keyword | `float` | `required` |
| `y_max` | positional-or-keyword | `float` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `Polygon(<br>        [<br>            (x_min, y_min),<br>            (x_min, y_max),<br>            (x_max, y_max),<br>            (x_max, y_min),<br>            (x_min, y_min),<br>        ]<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_planning_zoning::_parcels` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_zoning::_parcels` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_zoning::_zones` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_zoning::_zones` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_zoning::test_one_parcel_fully_inside_one_zone` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_one_parcel_fully_inside_one_zone` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_zoning::test_parcel_split_across_two_zones` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_parcel_split_across_two_zones` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_zoning::test_dominant_zone_tie_is_deterministic` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_dominant_zone_tie_is_deterministic` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_zoning::test_touch_only_relation_is_preserved_but_never_dominant` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_touch_only_relation_is_preserved_but_never_dominant` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_zoning::test_parcel_with_no_positive_area_zone_is_preserved` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_parcel_with_no_positive_area_zone_is_preserved` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_zoning::test_parcel_with_no_intersecting_zone_has_zero_coverage` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_parcel_with_no_intersecting_zone_has_zero_coverage` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_zoning::test_overlapping_source_zones_expose_raw_sum_union_and_excess` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_overlapping_source_zones_expose_raw_sum_union_and_excess` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_zoning::test_polygon_and_multipolygon_parcels_are_supported` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_polygon_and_multipolygon_parcels_are_supported` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_zoning::test_polygon_and_multipolygon_zones_are_supported` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_polygon_and_multipolygon_zones_are_supported` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_zoning::test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_zoning::test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_zoning::test_duplicate_parcel_id_is_rejected` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_duplicate_parcel_id_is_rejected` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_zoning::test_duplicate_source_zone_id_is_rejected` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_duplicate_source_zone_id_is_rejected` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_zoning::test_input_frames_are_not_mutated` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_input_frames_are_not_mutated` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_zoning::test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_zoning::test_raw_zoning_values_are_preserved_exactly` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_raw_zoning_values_are_preserved_exactly` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_zoning::test_intersection_table_references_only_known_parcels_and_zones` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_intersection_table_references_only_known_parcels_and_zones` via `_rectangle`
- direct call: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_coordinated_mutations` via `_rectangle`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_coordinated_mutations` via `_rectangle`

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_parcels`

**Purpose:** Implements `parcels` within the file role: Provides complete unit and regression coverage for the `enrich_planning_zoning` contracts exercised in this file.

**Exact signature**

```python
def _parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    crs: str | None = "EPSG:2154",
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometries` | positional-or-keyword | `list[object] \| None` | `None` |
| `identifiers` | keyword-only | `list[object] \| None` | `None` |
| `crs` | keyword-only | `str \| None` | `'EPSG:2154'` |

**Return and exception contract**

- Exact observed return expressions:
  - `frame.set_crs(None, allow_override=True)`
  - `frame`
  - `frame.to_crs(crs)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_planning_zoning::_run` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::_run` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_one_parcel_fully_inside_one_zone` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_one_parcel_fully_inside_one_zone` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_parcel_split_across_two_zones` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_parcel_split_across_two_zones` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_dominant_zone_tie_is_deterministic` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_dominant_zone_tie_is_deterministic` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_touch_only_relation_is_preserved_but_never_dominant` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_touch_only_relation_is_preserved_but_never_dominant` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_parcel_with_no_positive_area_zone_is_preserved` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_parcel_with_no_positive_area_zone_is_preserved` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_parcel_with_no_intersecting_zone_has_zero_coverage` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_parcel_with_no_intersecting_zone_has_zero_coverage` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_overlapping_source_zones_expose_raw_sum_union_and_excess` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_overlapping_source_zones_expose_raw_sum_union_and_excess` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_polygon_and_multipolygon_parcels_are_supported` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_polygon_and_multipolygon_parcels_are_supported` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_polygon_and_multipolygon_zones_are_supported` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_polygon_and_multipolygon_zones_are_supported` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_missing_or_unusable_crs_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_missing_or_unusable_crs_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_invalid_or_non_polygonal_parcel_geometry_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_invalid_or_non_polygonal_parcel_geometry_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_invalid_or_non_polygonal_zone_geometry_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_invalid_or_non_polygonal_zone_geometry_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_invalid_parcel_id_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_invalid_parcel_id_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_duplicate_parcel_id_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_duplicate_parcel_id_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_missing_parcel_id_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_missing_parcel_id_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_geometry_must_be_the_active_parcel_geometry_column` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_geometry_must_be_the_active_parcel_geometry_column` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_invalid_source_zone_id_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_invalid_source_zone_id_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_duplicate_source_zone_id_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_duplicate_source_zone_id_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_zoning_document_reference_must_match_loaded_archive` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_zoning_document_reference_must_match_loaded_archive` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_zoning_summary_lineage_and_count_must_match_bundle` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_zoning_summary_lineage_and_count_must_match_bundle` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_existing_parcel_output_field_collision_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_existing_parcel_output_field_collision_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_every_source_zoning_field_is_required` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_every_source_zoning_field_is_required` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_input_frames_are_not_mutated` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_input_frames_are_not_mutated` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_raw_zoning_values_are_preserved_exactly` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_raw_zoning_values_are_preserved_exactly` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_intersection_table_references_only_known_parcels_and_zones` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_intersection_table_references_only_known_parcels_and_zones` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_result_frames_are_independent_from_inputs` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_result_frames_are_independent_from_inputs` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_accepts_physical_fixture` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_accepts_physical_fixture` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_requires_every_parcel_summary_column` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_requires_every_parcel_summary_column` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_all_missing_parcel_summaries` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_all_missing_parcel_summaries` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_coordinated_mutations` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_coordinated_mutations` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_physical_tamper` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_physical_tamper` via `_parcels`
- direct call: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_revalidates_physical_source_once` via `_parcels`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_revalidates_physical_source_once` via `_parcels`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_rectangle` | `tests.unit.test_enrich_planning_zoning._rectangle` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | `frame.set_crs(None, allow_override=True)` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_zones`

**Purpose:** Implements `zones` within the file role: Provides complete unit and regression coverage for the `enrich_planning_zoning` contracts exercised in this file.

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

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometries` | positional-or-keyword | `list[object] \| None` | `None` |
| `identifiers` | keyword-only | `list[object] \| None` | `None` |
| `labels` | keyword-only | `list[object] \| None` | `None` |
| `long_labels` | keyword-only | `list[object] \| None` | `None` |
| `zone_types` | keyword-only | `list[object] \| None` | `None` |
| `document_references` | keyword-only | `list[object] \| None` | `None` |
| `crs` | keyword-only | `str \| None` | `'EPSG:2154'` |

**Return and exception contract**

- Exact observed return expressions:
  - `frame.set_crs(None, allow_override=True)`
  - `frame`
  - `frame.set_crs(crs, allow_override=True)`
  - `frame.to_crs(crs)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_planning_zoning::_planning_document` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::_planning_document` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::_physical_planning_document` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::_physical_planning_document` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_one_parcel_fully_inside_one_zone` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_one_parcel_fully_inside_one_zone` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_parcel_split_across_two_zones` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_parcel_split_across_two_zones` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_dominant_zone_tie_is_deterministic` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_dominant_zone_tie_is_deterministic` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_touch_only_relation_is_preserved_but_never_dominant` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_touch_only_relation_is_preserved_but_never_dominant` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_parcel_with_no_positive_area_zone_is_preserved` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_parcel_with_no_positive_area_zone_is_preserved` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_parcel_with_no_intersecting_zone_has_zero_coverage` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_parcel_with_no_intersecting_zone_has_zero_coverage` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_overlapping_source_zones_expose_raw_sum_union_and_excess` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_overlapping_source_zones_expose_raw_sum_union_and_excess` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_polygon_and_multipolygon_parcels_are_supported` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_polygon_and_multipolygon_parcels_are_supported` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_polygon_and_multipolygon_zones_are_supported` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_polygon_and_multipolygon_zones_are_supported` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_missing_or_unusable_crs_is_rejected` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_missing_or_unusable_crs_is_rejected` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_invalid_or_non_polygonal_parcel_geometry_is_rejected` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_invalid_or_non_polygonal_parcel_geometry_is_rejected` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_invalid_or_non_polygonal_zone_geometry_is_rejected` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_invalid_or_non_polygonal_zone_geometry_is_rejected` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_invalid_parcel_id_is_rejected` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_invalid_parcel_id_is_rejected` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_duplicate_parcel_id_is_rejected` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_duplicate_parcel_id_is_rejected` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_missing_parcel_id_is_rejected` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_missing_parcel_id_is_rejected` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_geometry_must_be_the_active_parcel_geometry_column` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_geometry_must_be_the_active_parcel_geometry_column` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_invalid_source_zone_id_is_rejected` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_invalid_source_zone_id_is_rejected` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_duplicate_source_zone_id_is_rejected` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_duplicate_source_zone_id_is_rejected` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_zoning_document_reference_must_match_loaded_archive` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_zoning_document_reference_must_match_loaded_archive` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_existing_parcel_output_field_collision_is_rejected` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_existing_parcel_output_field_collision_is_rejected` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_every_source_zoning_field_is_required` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_every_source_zoning_field_is_required` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_input_frames_are_not_mutated` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_input_frames_are_not_mutated` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_raw_zoning_values_are_preserved_exactly` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_raw_zoning_values_are_preserved_exactly` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_intersection_table_references_only_known_parcels_and_zones` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_intersection_table_references_only_known_parcels_and_zones` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_result_frames_are_independent_from_inputs` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_result_frames_are_independent_from_inputs` via `_zones`
- direct call: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_coordinated_mutations` via `_zones`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_coordinated_mutations` via `_zones`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_rectangle` | `tests.unit.test_enrich_planning_zoning._rectangle` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_planning_document`

**Purpose:** Implements `planning document` within the file role: Provides complete unit and regression coverage for the `enrich_planning_zoning` contracts exercised in this file.

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

- Exact decorators: none.
- Declared return annotation: `GpuPlanningDocument`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `zoning` | positional-or-keyword | `gpd.GeoDataFrame \| None` | `None` |
| `archive_name` | keyword-only | `str` | `ARCHIVE_NAME` |
| `document_id` | keyword-only | `str` | `DOCUMENT_ID` |
| `source_layer` | keyword-only | `str` | `SOURCE_LAYER` |

**Return and exception contract**

- Exact observed return expressions:
  - `GpuPlanningDocument(<br>        source_config=source_config,<br>        source_config_sha256=gpu_source_module._source_config_sha256(source_config),<br>        extraction=extraction,<br>        all_spatial_layers=(reference,),<br>        zoning=inspected,<br>        related_layers=(),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_planning_zoning::_physical_planning_document` via `_planning_document`
- value/type reference: `tests.unit.test_enrich_planning_zoning::_physical_planning_document` via `_planning_document`
- direct call: `tests.unit.test_enrich_planning_zoning::_run` via `_planning_document`
- value/type reference: `tests.unit.test_enrich_planning_zoning::_run` via `_planning_document`
- direct call: `tests.unit.test_enrich_planning_zoning::test_zoning_summary_lineage_and_count_must_match_bundle` via `_planning_document`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_zoning_summary_lineage_and_count_must_match_bundle` via `_planning_document`
- direct call: `tests.unit.test_enrich_planning_zoning::test_input_frames_are_not_mutated` via `_planning_document`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_input_frames_are_not_mutated` via `_planning_document`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |
| `load_gpu_source_config` | `landscout.sources.gpu_fr.load_gpu_source_config` |
| `Path` | `pathlib.Path` |
| `GpuDocumentMetadata` | `landscout.sources.gpu_fr.GpuDocumentMetadata` |
| `GpuArchiveDownload` | `landscout.sources.gpu_fr.GpuArchiveDownload` |
| `GpuExtraction` | `landscout.sources.gpu_fr.GpuExtraction` |
| `GpuSpatialLayerReference` | `landscout.sources.gpu_fr.GpuSpatialLayerReference` |
| `pd.Series` | `pandas.Series` |
| `GpuLayerSummary` | `landscout.sources.gpu_fr.GpuLayerSummary` |
| `data.crs.to_string` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `data.dtypes.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `data[column].isna().sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `data[column].isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry[non_null].geom_type.value_counts().items` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry[non_null].geom_type.value_counts` | `unresolved local/third-party receiver; no ownership inferred` |
| `(~non_null).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `(non_null & geometry.is_empty).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `(non_empty & ~geometry.is_valid).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuInspectedLayer` | `landscout.sources.gpu_fr.GpuInspectedLayer` |
| `GpuPlanningDocument` | `landscout.sources.gpu_fr.GpuPlanningDocument` |
| `gpu_source_module._source_config_sha256` | `landscout.sources.gpu_fr._source_config_sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `gpu_source_module._source_config_sha256` |
| CRS/geometry/spatial calculation | `geometry[non_null].geom_type.value_counts().items`<br>`geometry[non_null].geom_type.value_counts`<br>`(non_null & geometry.is_empty).sum`<br>`(non_empty & ~geometry.is_valid).sum` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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
    source_config = load_gpu_source_config(Path("configs/sources/gpu_fr.yaml"))
    document = GpuDocumentMetadata(
        provider=source_config.provider,
        portal=source_config.portal,
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
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in data.dtypes.items()
        ),
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
        source_config=source_config,
        source_config_sha256=gpu_source_module._source_config_sha256(source_config),
        extraction=extraction,
        all_spatial_layers=(reference,),
        zoning=inspected,
        related_layers=(),
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_physical_planning_document`

**Purpose:** Implements `physical planning document` within the file role: Provides complete unit and regression coverage for the `enrich_planning_zoning` contracts exercised in this file.

**Exact signature**

```python
def _physical_planning_document(
    tmp_path: Path,
    zoning: gpd.GeoDataFrame | None = None,
) -> GpuPlanningDocument:
```

- Exact decorators: none.
- Declared return annotation: `GpuPlanningDocument`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `zoning` | positional-or-keyword | `gpd.GeoDataFrame \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `replace(<br>        base,<br>        extraction=extraction,<br>        all_spatial_layers=(reference,),<br>        zoning=inspected,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_accepts_physical_fixture` via `_physical_planning_document`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_accepts_physical_fixture` via `_physical_planning_document`
- direct call: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_requires_every_parcel_summary_column` via `_physical_planning_document`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_requires_every_parcel_summary_column` via `_physical_planning_document`
- direct call: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_all_missing_parcel_summaries` via `_physical_planning_document`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_all_missing_parcel_summaries` via `_physical_planning_document`
- direct call: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_coordinated_mutations` via `_physical_planning_document`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_coordinated_mutations` via `_physical_planning_document`
- direct call: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_physical_tamper` via `_physical_planning_document`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_physical_tamper` via `_physical_planning_document`
- direct call: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_revalidates_physical_source_once` via `_physical_planning_document`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_revalidates_physical_source_once` via `_physical_planning_document`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `root.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |
| `source.to_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.read_file` | `geopandas.read_file` |
| `_planning_document` | `tests.unit.test_enrich_planning_zoning._planning_document` |
| `replace` | `dataclasses.replace` |
| `GpuExtractedFile` | `landscout.sources.gpu_fr.GpuExtractedFile` |
| `path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(path.read_bytes()).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `(root / EXTRACTION_MANIFEST_NAME).write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `gpd.read_file`<br>`path.stat`<br>`sha256(path.read_bytes()).hexdigest`<br>`path.read_bytes` |
| Filesystem/archive write or publication | `root.mkdir`<br>`(root / EXTRACTION_MANIFEST_NAME).write_text` |
| Hashing/byte identity | `sha256(path.read_bytes()).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_run`

**Purpose:** Implements `run` within the file role: Provides complete unit and regression coverage for the `enrich_planning_zoning` contracts exercised in this file.

**Exact signature**

```python
def _run(
    parcels: gpd.GeoDataFrame | None = None,
    zones: gpd.GeoDataFrame | None = None,
) -> ParcelZoningResult:
```

- Exact decorators: none.
- Declared return annotation: `ParcelZoningResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame \| None` | `None` |
| `zones` | positional-or-keyword | `gpd.GeoDataFrame \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `intersect_parcels_with_gpu_zoning(<br>        parcels if parcels is not None else _parcels(),<br>        _planning_document(zones),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_planning_zoning::test_result_container_is_frozen` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_result_container_is_frozen` via `_run`
- direct call: `tests.unit.test_enrich_planning_zoning::test_one_parcel_fully_inside_one_zone` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_one_parcel_fully_inside_one_zone` via `_run`
- direct call: `tests.unit.test_enrich_planning_zoning::test_parcel_split_across_two_zones` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_parcel_split_across_two_zones` via `_run`
- direct call: `tests.unit.test_enrich_planning_zoning::test_dominant_zone_tie_is_deterministic` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_dominant_zone_tie_is_deterministic` via `_run`
- direct call: `tests.unit.test_enrich_planning_zoning::test_touch_only_relation_is_preserved_but_never_dominant` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_touch_only_relation_is_preserved_but_never_dominant` via `_run`
- direct call: `tests.unit.test_enrich_planning_zoning::test_parcel_with_no_positive_area_zone_is_preserved` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_parcel_with_no_positive_area_zone_is_preserved` via `_run`
- direct call: `tests.unit.test_enrich_planning_zoning::test_parcel_with_no_intersecting_zone_has_zero_coverage` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_parcel_with_no_intersecting_zone_has_zero_coverage` via `_run`
- direct call: `tests.unit.test_enrich_planning_zoning::test_overlapping_source_zones_expose_raw_sum_union_and_excess` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_overlapping_source_zones_expose_raw_sum_union_and_excess` via `_run`
- direct call: `tests.unit.test_enrich_planning_zoning::test_polygon_and_multipolygon_parcels_are_supported` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_polygon_and_multipolygon_parcels_are_supported` via `_run`
- direct call: `tests.unit.test_enrich_planning_zoning::test_polygon_and_multipolygon_zones_are_supported` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_polygon_and_multipolygon_zones_are_supported` via `_run`
- direct call: `tests.unit.test_enrich_planning_zoning::test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93` via `_run`
- direct call: `tests.unit.test_enrich_planning_zoning::test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154` via `_run`
- direct call: `tests.unit.test_enrich_planning_zoning::test_missing_or_unusable_crs_is_rejected` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_missing_or_unusable_crs_is_rejected` via `_run`
- direct call: `tests.unit.test_enrich_planning_zoning::test_invalid_or_non_polygonal_parcel_geometry_is_rejected` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_invalid_or_non_polygonal_parcel_geometry_is_rejected` via `_run`
- direct call: `tests.unit.test_enrich_planning_zoning::test_invalid_or_non_polygonal_zone_geometry_is_rejected` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_invalid_or_non_polygonal_zone_geometry_is_rejected` via `_run`
- direct call: `tests.unit.test_enrich_planning_zoning::test_invalid_parcel_id_is_rejected` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_invalid_parcel_id_is_rejected` via `_run`
- direct call: `tests.unit.test_enrich_planning_zoning::test_duplicate_parcel_id_is_rejected` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_duplicate_parcel_id_is_rejected` via `_run`
- direct call: `tests.unit.test_enrich_planning_zoning::test_missing_parcel_id_is_rejected` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_missing_parcel_id_is_rejected` via `_run`
- direct call: `tests.unit.test_enrich_planning_zoning::test_geometry_must_be_the_active_parcel_geometry_column` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_geometry_must_be_the_active_parcel_geometry_column` via `_run`
- direct call: `tests.unit.test_enrich_planning_zoning::test_invalid_source_zone_id_is_rejected` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_invalid_source_zone_id_is_rejected` via `_run`
- direct call: `tests.unit.test_enrich_planning_zoning::test_duplicate_source_zone_id_is_rejected` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_duplicate_source_zone_id_is_rejected` via `_run`
- direct call: `tests.unit.test_enrich_planning_zoning::test_zoning_document_reference_must_match_loaded_archive` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_zoning_document_reference_must_match_loaded_archive` via `_run`
- direct call: `tests.unit.test_enrich_planning_zoning::test_existing_parcel_output_field_collision_is_rejected` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_existing_parcel_output_field_collision_is_rejected` via `_run`
- direct call: `tests.unit.test_enrich_planning_zoning::test_every_source_zoning_field_is_required` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_every_source_zoning_field_is_required` via `_run`
- direct call: `tests.unit.test_enrich_planning_zoning::test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved` via `_run`
- direct call: `tests.unit.test_enrich_planning_zoning::test_raw_zoning_values_are_preserved_exactly` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_raw_zoning_values_are_preserved_exactly` via `_run`
- direct call: `tests.unit.test_enrich_planning_zoning::test_intersection_table_references_only_known_parcels_and_zones` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_intersection_table_references_only_known_parcels_and_zones` via `_run`
- direct call: `tests.unit.test_enrich_planning_zoning::test_result_frames_are_independent_from_inputs` via `_run`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_result_frames_are_independent_from_inputs` via `_run`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `intersect_parcels_with_gpu_zoning` | `landscout.stages.enrich_planning_zoning.intersect_parcels_with_gpu_zoning` |
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_planning_document` | `tests.unit.test_enrich_planning_zoning._planning_document` |

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
    parcels: gpd.GeoDataFrame | None = None,
    zones: gpd.GeoDataFrame | None = None,
) -> ParcelZoningResult:
    return intersect_parcels_with_gpu_zoning(
        parcels if parcels is not None else _parcels(),
        _planning_document(zones),
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_row_for_source_zone`

**Purpose:** Implements `row for source zone` within the file role: Provides complete unit and regression coverage for the `enrich_planning_zoning` contracts exercised in this file.

**Exact signature**

```python
def _row_for_source_zone(result: ParcelZoningResult, source_id: str) -> pd.Series:
```

- Exact decorators: none.
- Declared return annotation: `pd.Series`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `ParcelZoningResult` | `required` |
| `source_id` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result.zones.loc[result.zones["source_zone_id"] == source_id].iloc[0]`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_planning_zoning::test_raw_zoning_values_are_preserved_exactly` via `_row_for_source_zone`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_raw_zoning_values_are_preserved_exactly` via `_row_for_source_zone`

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
def _row_for_source_zone(result: ParcelZoningResult, source_id: str) -> pd.Series:
    return result.zones.loc[result.zones["source_zone_id"] == source_id].iloc[0]
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_clean_high_level_api_is_exported`

**Purpose:** Regression invariant: clean high level api is exported. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_clean_high_level_api_is_exported() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert stages.intersect_parcels_with_gpu_zoning is intersect_parcels_with_gpu_zoning`
  - `assert "intersect_parcels_with_gpu_zoning" in stages.__all__`
  - `assert stages.PlanningZoningError is PlanningZoningError`
  - `assert stages.ParcelZoningResult is ParcelZoningResult`
  - `assert "PlanningZoningError" in stages.__all__`
  - `assert "ParcelZoningResult" in stages.__all__`
  - `assert "PlanningZoningError" in module.__all__`
  - `assert "ParcelZoningResult" in module.__all__`
  - `assert set(module.__all__) == expected`
  - `assert getattr(stages, name) is getattr(module, name)`
  - `assert name in stages.__all__`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_clean_high_level_api_is_exported() -> None:
    module = importlib.import_module("landscout.stages.enrich_planning_zoning")
    expected = {
        "ParcelZoningResult",
        "PlanningZoningError",
        "intersect_parcels_with_gpu_zoning",
        "validate_normalized_planning_zoning_inputs",
    }
    assert stages.intersect_parcels_with_gpu_zoning is intersect_parcels_with_gpu_zoning
    assert "intersect_parcels_with_gpu_zoning" in stages.__all__
    assert stages.PlanningZoningError is PlanningZoningError
    assert stages.ParcelZoningResult is ParcelZoningResult
    assert "PlanningZoningError" in stages.__all__
    assert "ParcelZoningResult" in stages.__all__
    assert "PlanningZoningError" in module.__all__
    assert "ParcelZoningResult" in module.__all__
    assert set(module.__all__) == expected
    for name in expected:
        assert getattr(stages, name) is getattr(module, name)
        assert name in stages.__all__
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_result_container_is_frozen`

**Purpose:** Regression invariant: result container is frozen. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_result_container_is_frozen() -> None:
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
| `_run` | `tests.unit.test_enrich_planning_zoning._run` |
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
def test_result_container_is_frozen() -> None:
    result = _run()

    with pytest.raises(FrozenInstanceError):
        result.parcels = result.parcels.copy()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_one_parcel_fully_inside_one_zone`

**Purpose:** Regression invariant: one parcel fully inside one zone. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_one_parcel_fully_inside_one_zone() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert isinstance(result, ParcelZoningResult)`
  - `assert len(result.parcels) == 1`
  - `assert len(result.zones) == 1`
  - `assert len(result.intersections) == 1`
  - `assert zone["planning_zone_id"] == f"GPU:{DOCUMENT_ID}:ZONE:SOURCE-ZONE"`
  - `assert zone["source_zone_id"] == "SOURCE-ZONE"`
  - `assert zone["zone_label_raw"] == "UAa"`
  - `assert zone["zone_long_label_raw"] == "Zone urbaine centrale"`
  - `assert zone["zone_type_raw"] == "U"`
  - `assert zone["regulation_filename_raw"] == "reglement-1.pdf"`
  - `assert zone["regulation_url_raw"].endswith("/1")`
  - `assert zone["source_document_reference_raw"] == ARCHIVE_NAME`
  - `assert zone["source_validity_date_raw"] == "2024-02-15"`
  - `assert zone["source_provider"] == "Géoportail de l'Urbanisme"`
  - `assert (<br>        zone["source_portal"]<br>        == load_gpu_source_config(Path("configs/sources/gpu_fr.yaml")).portal<br>    )`
  - `assert zone["source_commune_code"] == "31395"`
  - `assert zone["source_document_id"] == DOCUMENT_ID`
  - `assert zone["source_document_type"] == "PLU"`
  - `assert zone["source_archive_name"] == ARCHIVE_NAME`
  - `assert zone["source_archive_sha256"] == ARCHIVE_SHA256`
  - `assert zone["source_layer"] == SOURCE_LAYER`
  - `assert zone["source_standard_model"] == STANDARD_MODEL`
  - `assert zone["zone_area_m2"] == pytest.approx(100.0)`
  - `assert zone.geometry.area == pytest.approx(100.0)`
  - `assert result.zones.crs.to_epsg() == 2154`
  - `assert {<br>        "parcel_id",<br>        "planning_zone_id",<br>        "source_zone_id",<br>        "zone_type_raw",<br>        "zone_label_raw",<br>        "zone_long_label_raw",<br>        "relation_type",<br>        "parcel_metric_area_m2",<br>        "zone_area_m2",<br>        "intersection_area_m2",<br>        "parcel_share_pct",<br>        "zone_share_pct",<br>        "source_document_id",<br>        "source_archive_sha256",<br>        "source_layer",<br>        "source_validity_date_raw",<br>        "regulation_filename_raw",<br>    }.issubset(result.intersections.columns)`
  - `assert relation["relation_type"] == "AREA_OVERLAP"`
  - `assert relation["parcel_metric_area_m2"] == pytest.approx(100.0)`
  - `assert relation["zone_area_m2"] == pytest.approx(100.0)`
  - `assert relation["intersection_area_m2"] == pytest.approx(100.0)`
  - `assert relation["parcel_share_pct"] == pytest.approx(100.0)`
  - `assert relation["zone_share_pct"] == pytest.approx(100.0)`
  - `assert relation["source_document_id"] == DOCUMENT_ID`
  - `assert relation["source_archive_sha256"] == ARCHIVE_SHA256`
  - `assert relation["source_layer"] == SOURCE_LAYER`
  - `assert relation["source_validity_date_raw"] == "2024-02-15"`
  - `assert relation["regulation_filename_raw"] == "reglement-1.pdf"`
  - `assert parcel["zoning_area_match_count"] == 1`
  - `assert parcel["zoning_touch_only_count"] == 0`
  - `assert parcel["zoning_intersection_area_sum_m2"] == pytest.approx(100.0)`
  - `assert parcel["zoning_covered_union_area_m2"] == pytest.approx(100.0)`
  - `assert parcel["zoning_coverage_pct"] == pytest.approx(100.0)`
  - `assert parcel["zoning_gap_area_m2"] == pytest.approx(0.0)`
  - `assert parcel["zoning_overlap_excess_area_m2"] == pytest.approx(0.0)`
  - `assert parcel["dominant_source_zone_id"] == "SOURCE-ZONE"`
  - `assert parcel["dominant_zone_type_raw"] == "U"`
  - `assert parcel["dominant_zone_label_raw"] == "UAa"`
  - `assert parcel["dominant_zone_long_label_raw"] == "Zone urbaine centrale"`
  - `assert parcel["dominant_zone_intersection_area_m2"] == pytest.approx(100.0)`
  - `assert parcel["dominant_zone_share_pct"] == pytest.approx(100.0)`
  - `assert parcel["dominant_zone_tie_count"] == 1`
  - `assert parcel["planning_document_id"] == DOCUMENT_ID`
  - `assert parcel["planning_document_type"] == "PLU"`
  - `assert parcel["planning_archive_name"] == ARCHIVE_NAME`
  - `assert parcel["planning_archive_sha256"] == ARCHIVE_SHA256`
  - `assert parcel["planning_source_layer"] == SOURCE_LAYER`
  - `assert parcel["planning_standard_model"] == STANDARD_MODEL`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_run` | `tests.unit.test_enrich_planning_zoning._run` |
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_rectangle` | `tests.unit.test_enrich_planning_zoning._rectangle` |
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `zone["regulation_url_raw"].endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `load_gpu_source_config` | `landscout.sources.gpu_fr.load_gpu_source_config` |
| `Path` | `pathlib.Path` |
| `pytest.approx` | `pytest.approx` |
| `result.zones.crs.to_epsg` | `unresolved local/third-party receiver; no ownership inferred` |
| `{<br>        "parcel_id",<br>        "planning_zone_id",<br>        "source_zone_id",<br>        "zone_type_raw",<br>        "zone_label_raw",<br>        "zone_long_label_raw",<br>        "relation_type",<br>        "parcel_metric_area_m2",<br>        "zone_area_m2",<br>        "intersection_area_m2",<br>        "parcel_share_pct",<br>        "zone_share_pct",<br>        "source_document_id",<br>        "source_archive_sha256",<br>        "source_layer",<br>        "source_validity_date_raw",<br>        "regulation_filename_raw",<br>    }.issubset` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `{<br>        "parcel_id",<br>        "planning_zone_id",<br>        "source_zone_id",<br>        "zone_type_raw",<br>        "zone_label_raw",<br>        "zone_long_label_raw",<br>        "relation_type",<br>        "parcel_metric_area_m2",<br>        "zone_area_m2",<br>        "intersection_area_m2",<br>        "parcel_share_pct",<br>        "zone_share_pct",<br>        "source_document_id",<br>        "source_archive_sha256",<br>        "source_layer",<br>        "source_validity_date_raw",<br>        "regulation_filename_raw",<br>    }.issubset` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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
    assert (
        zone["source_portal"]
        == load_gpu_source_config(Path("configs/sources/gpu_fr.yaml")).portal
    )
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_parcel_split_across_two_zones`

**Purpose:** Regression invariant: parcel split across two zones. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_parcel_split_across_two_zones() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert len(result.intersections) == 2`
  - `assert set(result.intersections["relation_type"]) == {"AREA_OVERLAP"}`
  - `assert sorted(result.intersections["intersection_area_m2"]) == pytest.approx(<br>        [40.0, 60.0]<br>    )`
  - `assert parcel["zoning_area_match_count"] == 2`
  - `assert parcel["zoning_covered_union_area_m2"] == pytest.approx(100.0)`
  - `assert parcel["zoning_coverage_pct"] == pytest.approx(100.0)`
  - `assert parcel["dominant_source_zone_id"] == "RIGHT"`
  - `assert parcel["dominant_zone_share_pct"] == pytest.approx(60.0)`
  - `assert parcel["dominant_zone_tie_count"] == 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_run` | `tests.unit.test_enrich_planning_zoning._run` |
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_rectangle` | `tests.unit.test_enrich_planning_zoning._rectangle` |
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_dominant_zone_tie_is_deterministic`

**Purpose:** Regression invariant: dominant zone tie is deterministic. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_dominant_zone_tie_is_deterministic() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert parcel["dominant_source_zone_id"] == "A-ZONE"`
  - `assert parcel["dominant_planning_zone_id"] == f"GPU:{DOCUMENT_ID}:ZONE:A-ZONE"`
  - `assert parcel["dominant_zone_intersection_area_m2"] == pytest.approx(50.0)`
  - `assert parcel["dominant_zone_share_pct"] == pytest.approx(50.0)`
  - `assert parcel["dominant_zone_tie_count"] == 2`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_run` | `tests.unit.test_enrich_planning_zoning._run` |
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_rectangle` | `tests.unit.test_enrich_planning_zoning._rectangle` |
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_touch_only_relation_is_preserved_but_never_dominant`

**Purpose:** Regression invariant: touch only relation is preserved but never dominant. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_touch_only_relation_is_preserved_but_never_dominant() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert relations.loc["AREA", "relation_type"] == "AREA_OVERLAP"`
  - `assert relations.loc["TOUCH", "relation_type"] == "TOUCH_ONLY"`
  - `assert relations.loc["TOUCH", "intersection_area_m2"] == pytest.approx(0.0)`
  - `assert relations.loc["TOUCH", "parcel_share_pct"] == pytest.approx(0.0)`
  - `assert parcel["zoning_area_match_count"] == 1`
  - `assert parcel["zoning_touch_only_count"] == 1`
  - `assert parcel["dominant_source_zone_id"] == "AREA"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_run` | `tests.unit.test_enrich_planning_zoning._run` |
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_rectangle` | `tests.unit.test_enrich_planning_zoning._rectangle` |
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |
| `result.intersections.set_index` | `unresolved local/third-party receiver; no ownership inferred` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_parcel_with_no_positive_area_zone_is_preserved`

**Purpose:** Regression invariant: parcel with no positive area zone is preserved. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_parcel_with_no_positive_area_zone_is_preserved() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert len(result.intersections) == 1`
  - `assert result.intersections.iloc[0]["relation_type"] == "TOUCH_ONLY"`
  - `assert parcel["zoning_area_match_count"] == 0`
  - `assert parcel["zoning_touch_only_count"] == 1`
  - `assert parcel["zoning_intersection_area_sum_m2"] == pytest.approx(0.0)`
  - `assert parcel["zoning_covered_union_area_m2"] == pytest.approx(0.0)`
  - `assert parcel["zoning_coverage_pct"] == pytest.approx(0.0)`
  - `assert parcel["zoning_gap_area_m2"] == pytest.approx(100.0)`
  - `assert pd.isna(parcel["dominant_planning_zone_id"])`
  - `assert pd.isna(parcel["dominant_source_zone_id"])`
  - `assert pd.isna(parcel["dominant_zone_intersection_area_m2"])`
  - `assert pd.isna(parcel["dominant_zone_share_pct"])`
  - `assert pd.isna(parcel["dominant_zone_tie_count"])`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_run` | `tests.unit.test_enrich_planning_zoning._run` |
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_rectangle` | `tests.unit.test_enrich_planning_zoning._rectangle` |
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.approx` | `pytest.approx` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_parcel_with_no_intersecting_zone_has_zero_coverage`

**Purpose:** Regression invariant: parcel with no intersecting zone has zero coverage. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_parcel_with_no_intersecting_zone_has_zero_coverage() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.intersections.empty`
  - `assert parcel["zoning_area_match_count"] == 0`
  - `assert parcel["zoning_touch_only_count"] == 0`
  - `assert parcel["zoning_coverage_pct"] == pytest.approx(0.0)`
  - `assert parcel["zoning_gap_area_m2"] == pytest.approx(100.0)`
  - `assert tuple(result.intersections.columns) == (<br>        "parcel_id",<br>        "planning_zone_id",<br>        "source_zone_id",<br>        "zone_type_raw",<br>        "zone_label_raw",<br>        "zone_long_label_raw",<br>        "relation_type",<br>        "parcel_metric_area_m2",<br>        "zone_area_m2",<br>        "intersection_area_m2",<br>        "parcel_share_pct",<br>        "zone_share_pct",<br>        "source_document_id",<br>        "source_archive_sha256",<br>        "source_layer",<br>        "source_validity_date_raw",<br>        "regulation_filename_raw",<br>    )`
  - `assert is_float_dtype(result.intersections[column])`
  - `assert is_integer_dtype(result.parcels["zoning_area_match_count"])`
  - `assert is_integer_dtype(result.parcels["zoning_touch_only_count"])`
  - `assert str(result.parcels["dominant_zone_tie_count"].dtype) == "Int64"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_run` | `tests.unit.test_enrich_planning_zoning._run` |
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_rectangle` | `tests.unit.test_enrich_planning_zoning._rectangle` |
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |
| `pytest.approx` | `pytest.approx` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `is_float_dtype` | `pandas.api.types.is_float_dtype` |
| `is_integer_dtype` | `pandas.api.types.is_integer_dtype` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_overlapping_source_zones_expose_raw_sum_union_and_excess`

**Purpose:** Regression invariant: overlapping source zones expose raw sum union and excess. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_overlapping_source_zones_expose_raw_sum_union_and_excess() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert parcel["zoning_intersection_area_sum_m2"] == pytest.approx(150.0)`
  - `assert parcel["zoning_covered_union_area_m2"] == pytest.approx(100.0)`
  - `assert parcel["zoning_overlap_excess_area_m2"] == pytest.approx(50.0)`
  - `assert parcel["zoning_coverage_pct"] == pytest.approx(100.0)`
  - `assert parcel["zoning_gap_area_m2"] == pytest.approx(0.0)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_run` | `tests.unit.test_enrich_planning_zoning._run` |
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_rectangle` | `tests.unit.test_enrich_planning_zoning._rectangle` |
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_polygon_and_multipolygon_parcels_are_supported`

**Purpose:** Regression invariant: polygon and multipolygon parcels are supported. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_polygon_and_multipolygon_parcels_are_supported(
    parcel_geometry: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "parcel_geometry",
    [
        _rectangle(0, 0, 10, 10),
        MultiPolygon([_rectangle(0, 0, 5, 10), _rectangle(10, 0, 15, 10)]),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcel_geometry` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.parcels.iloc[0]["zoning_coverage_pct"] == pytest.approx(100.0)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_run` | `tests.unit.test_enrich_planning_zoning._run` |
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |
| `_rectangle` | `tests.unit.test_enrich_planning_zoning._rectangle` |
| `pytest.approx` | `pytest.approx` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
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
def test_polygon_and_multipolygon_parcels_are_supported(
    parcel_geometry: object,
) -> None:
    result = _run(
        _parcels([parcel_geometry]),
        _zones([_rectangle(-5, -5, 20, 15)]),
    )

    assert result.parcels.iloc[0]["zoning_coverage_pct"] == pytest.approx(100.0)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_polygon_and_multipolygon_zones_are_supported`

**Purpose:** Regression invariant: polygon and multipolygon zones are supported. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_polygon_and_multipolygon_zones_are_supported(
    zone_geometry: object,
    expected_area: float,
    expected_coverage: float,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("zone_geometry", "expected_area", "expected_coverage"),
    [
        (_rectangle(0, 0, 10, 10), 100.0, 100.0),
        (
            MultiPolygon([_rectangle(0, 0, 4, 10), _rectangle(6, 0, 10, 10)]),
            80.0,
            80.0,
        ),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `zone_geometry` | positional-or-keyword | `object` | `required` |
| `expected_area` | positional-or-keyword | `float` | `required` |
| `expected_coverage` | positional-or-keyword | `float` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.parcels.iloc[0]["zoning_coverage_pct"] == pytest.approx(<br>        expected_coverage<br>    )`
  - `assert result.zones.iloc[0]["zone_area_m2"] == pytest.approx(expected_area)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_run` | `tests.unit.test_enrich_planning_zoning._run` |
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_rectangle` | `tests.unit.test_enrich_planning_zoning._rectangle` |
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |
| `pytest.approx` | `pytest.approx` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93`

**Purpose:** Regression invariant: parcel crs is preserved while metric calculation uses lambert93. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93(
    parcel_crs: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("parcel_crs", ["EPSG:2154", "EPSG:4326"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcel_crs` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.parcels.crs == parcels.crs`
  - `assert result.intersections.iloc[0]["parcel_metric_area_m2"] == pytest.approx(<br>        100.0, abs=1e-5<br>    )`
  - `assert result.intersections.iloc[0]["intersection_area_m2"] == pytest.approx(<br>        100.0, abs=1e-5<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_rectangle` | `tests.unit.test_enrich_planning_zoning._rectangle` |
| `_run` | `tests.unit.test_enrich_planning_zoning._run` |
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |
| `pytest.approx` | `pytest.approx` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154`

**Purpose:** Regression invariant: ignf lamb93 source zoning is normalized to epsg2154. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert source.crs.to_string() == "IGNF:LAMB93"`
  - `assert result.zones.crs.to_epsg() == 2154`
  - `assert result.zones.iloc[0].geometry.area == pytest.approx(100.0)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |
| `_rectangle` | `tests.unit.test_enrich_planning_zoning._rectangle` |
| `_run` | `tests.unit.test_enrich_planning_zoning._run` |
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `source.crs.to_string` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.zones.crs.to_epsg` | `unresolved local/third-party receiver; no ownership inferred` |
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
def test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154() -> None:
    source = _zones([_rectangle(0, 0, 10, 10)], crs="IGNF:LAMB93")
    result = _run(_parcels(), source)

    assert source.crs.to_string() == "IGNF:LAMB93"
    assert result.zones.crs.to_epsg() == 2154
    assert result.zones.iloc[0].geometry.area == pytest.approx(100.0)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_or_unusable_crs_is_rejected`

**Purpose:** Regression invariant: missing or unusable crs is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_missing_or_unusable_crs_is_rejected(
    parcels: gpd.GeoDataFrame,
    zones: gpd.GeoDataFrame,
    message: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("parcels", "zones", "message"),
    [
        (_parcels(crs=None), _zones(), "CRS"),
        (_parcels(), _zones(crs=None), "CRS"),
        (_parcels(), _zones(crs=LOCAL_ENGINEERING_CRS), "CRS"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `zones` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `message` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningZoningError, match=message)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `_run` | `tests.unit.test_enrich_planning_zoning._run` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |

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
def test_missing_or_unusable_crs_is_rejected(
    parcels: gpd.GeoDataFrame,
    zones: gpd.GeoDataFrame,
    message: str,
) -> None:
    with pytest.raises(PlanningZoningError, match=message):
        _run(parcels, zones)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_or_non_polygonal_parcel_geometry_is_rejected`

**Purpose:** Regression invariant: invalid or non polygonal parcel geometry is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_or_non_polygonal_parcel_geometry_is_rejected(
    geometry: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "geometry",
    [
        None,
        Polygon(),
        Polygon([(0, 0), (10, 10), (10, 0), (0, 10), (0, 0)]),
        Point(0, 0),
        LineString([(0, 0), (10, 10)]),
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
- Exact expected-exception contexts:
  - `pytest.raises(PlanningZoningError, match="geometry\|Polygon")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `_run` | `tests.unit.test_enrich_planning_zoning._run` |
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `Polygon` | `shapely.geometry.Polygon` |
| `Point` | `shapely.geometry.Point` |
| `LineString` | `shapely.geometry.LineString` |

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
def test_invalid_or_non_polygonal_parcel_geometry_is_rejected(
    geometry: object,
) -> None:
    with pytest.raises(PlanningZoningError, match="geometry|Polygon"):
        _run(_parcels([geometry]), _zones())
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_or_non_polygonal_zone_geometry_is_rejected`

**Purpose:** Regression invariant: invalid or non polygonal zone geometry is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_or_non_polygonal_zone_geometry_is_rejected(
    geometry: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "geometry",
    [
        None,
        Polygon(),
        Polygon([(0, 0), (10, 10), (10, 0), (0, 10), (0, 0)]),
        Point(0, 0),
        LineString([(0, 0), (10, 10)]),
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
- Exact expected-exception contexts:
  - `pytest.raises(PlanningZoningError, match="geometry\|Polygon")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `_run` | `tests.unit.test_enrich_planning_zoning._run` |
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `Polygon` | `shapely.geometry.Polygon` |
| `Point` | `shapely.geometry.Point` |
| `LineString` | `shapely.geometry.LineString` |

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
def test_invalid_or_non_polygonal_zone_geometry_is_rejected(
    geometry: object,
) -> None:
    with pytest.raises(PlanningZoningError, match="geometry|Polygon"):
        _run(_parcels(), _zones([geometry]))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_parcel_id_is_rejected`

**Purpose:** Regression invariant: invalid parcel id is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_parcel_id_is_rejected(identifier: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "identifier",
    [None, "", "   ", " PARCEL", "PARCEL ", 123],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `identifier` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningZoningError, match="parcel_id")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `_run` | `tests.unit.test_enrich_planning_zoning._run` |
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |
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
def test_invalid_parcel_id_is_rejected(identifier: object) -> None:
    with pytest.raises(PlanningZoningError, match="parcel_id"):
        _run(_parcels(identifiers=[identifier]), _zones())
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_parcel_id_is_rejected`

**Purpose:** Regression invariant: duplicate parcel id is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_parcel_id_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningZoningError, match="parcel_id.*unique\|duplicate")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `_run` | `tests.unit.test_enrich_planning_zoning._run` |
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_rectangle` | `tests.unit.test_enrich_planning_zoning._rectangle` |
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_parcel_id_is_rejected`

**Purpose:** Regression invariant: missing parcel id is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_missing_parcel_id_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningZoningError, match="parcel_id")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels().drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `pytest.raises` | `pytest.raises` |
| `_run` | `tests.unit.test_enrich_planning_zoning._run` |
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |

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
| In-memory mutation | `_parcels().drop(columns=["parcel_id"])` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_missing_parcel_id_is_rejected() -> None:
    parcels = _parcels().drop(columns=["parcel_id"])

    with pytest.raises(PlanningZoningError, match="parcel_id"):
        _run(parcels, _zones())
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_geometry_must_be_the_active_parcel_geometry_column`

**Purpose:** Regression invariant: geometry must be the active parcel geometry column. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_geometry_must_be_the_active_parcel_geometry_column() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningZoningError, match="active")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels().rename_geometry` | `unresolved local/third-party receiver; no ownership inferred` |
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `pytest.raises` | `pytest.raises` |
| `_run` | `tests.unit.test_enrich_planning_zoning._run` |
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_parcels().rename_geometry` |
| External process/environment | None directly present. |
| In-memory mutation | `parcels["geometry"] = parcels["shape"]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_geometry_must_be_the_active_parcel_geometry_column() -> None:
    parcels = _parcels().rename_geometry("shape")
    parcels["geometry"] = parcels["shape"]

    with pytest.raises(PlanningZoningError, match="active"):
        _run(parcels, _zones())
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_source_zone_id_is_rejected`

**Purpose:** Regression invariant: invalid source zone id is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_source_zone_id_is_rejected(identifier: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "identifier",
    [None, "", "   ", " ZONE", "ZONE ", 123],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `identifier` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningZoningError, match="LIB_IDZONE\|zone")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `_run` | `tests.unit.test_enrich_planning_zoning._run` |
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |
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
def test_invalid_source_zone_id_is_rejected(identifier: object) -> None:
    with pytest.raises(PlanningZoningError, match="LIB_IDZONE|zone"):
        _run(_parcels(), _zones(identifiers=[identifier]))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_source_zone_id_is_rejected`

**Purpose:** Regression invariant: duplicate source zone id is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_source_zone_id_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningZoningError, match="LIB_IDZONE.*unique\|duplicate")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `_run` | `tests.unit.test_enrich_planning_zoning._run` |
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |
| `_rectangle` | `tests.unit.test_enrich_planning_zoning._rectangle` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_zoning_document_reference_must_match_loaded_archive`

**Purpose:** Regression invariant: zoning document reference must match loaded archive. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_zoning_document_reference_must_match_loaded_archive() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningZoningError, match="IDURBA\|document")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |
| `pytest.raises` | `pytest.raises` |
| `_run` | `tests.unit.test_enrich_planning_zoning._run` |
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |

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
def test_zoning_document_reference_must_match_loaded_archive() -> None:
    zones = _zones(document_references=["31395_PLU_WRONG"])

    with pytest.raises(PlanningZoningError, match="IDURBA|document"):
        _run(_parcels(), zones)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_zoning_summary_lineage_and_count_must_match_bundle`

**Purpose:** Regression invariant: zoning summary lineage and count must match bundle. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_zoning_summary_lineage_and_count_must_match_bundle(
    summary_field: str,
    bad_value: object,
    message: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("summary_field", "bad_value", "message"),
    [
        ("source_document_id", "different-document", "document lineage"),
        ("source_archive_sha256", "b" * 64, "archive lineage"),
        ("source_layer", "different_layer", "source layer"),
        ("feature_count", 999, "feature count"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `summary_field` | positional-or-keyword | `str` | `required` |
| `bad_value` | positional-or-keyword | `object` | `required` |
| `message` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningZoningError, match=message)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_planning_document` | `tests.unit.test_enrich_planning_zoning._planning_document` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `intersect_parcels_with_gpu_zoning` | `landscout.stages.enrich_planning_zoning.intersect_parcels_with_gpu_zoning` |
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_existing_parcel_output_field_collision_is_rejected`

**Purpose:** Regression invariant: existing parcel output field collision is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_existing_parcel_output_field_collision_is_rejected(
    reserved_column: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "reserved_column",
    [
        "zoning_coverage_pct",
        "dominant_zone_label_raw",
        "planning_document_id",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `reserved_column` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningZoningError, match="column\|output\|reserved\|collision")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `pytest.raises` | `pytest.raises` |
| `_run` | `tests.unit.test_enrich_planning_zoning._run` |
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |
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
| In-memory mutation | `parcels[reserved_column] = "pre-existing-value"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_existing_parcel_output_field_collision_is_rejected(
    reserved_column: str,
) -> None:
    parcels = _parcels()
    parcels[reserved_column] = "pre-existing-value"

    with pytest.raises(PlanningZoningError, match="column|output|reserved|collision"):
        _run(parcels, _zones())
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_every_source_zoning_field_is_required`

**Purpose:** Regression invariant: every source zoning field is required. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_every_source_zoning_field_is_required(field: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("field", SOURCE_FIELDS)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `field` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningZoningError, match=field)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_zones().drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |
| `pytest.raises` | `pytest.raises` |
| `_run` | `tests.unit.test_enrich_planning_zoning._run` |
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
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
| In-memory mutation | `_zones().drop(columns=[field])` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_every_source_zoning_field_is_required(field: str) -> None:
    zones = _zones().drop(columns=[field])

    with pytest.raises(PlanningZoningError, match=field):
        _run(_parcels(), zones)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_input_frames_are_not_mutated`

**Purpose:** Regression invariant: input frames are not mutated. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_input_frames_are_not_mutated() -> None:
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
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_rectangle` | `tests.unit.test_enrich_planning_zoning._rectangle` |
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |
| `_planning_document` | `tests.unit.test_enrich_planning_zoning._planning_document` |
| `deepcopy` | `copy.deepcopy` |
| `intersect_parcels_with_gpu_zoning` | `landscout.stages.enrich_planning_zoning.intersect_parcels_with_gpu_zoning` |
| `assert_geodataframe_equal` | `geopandas.testing.assert_geodataframe_equal` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved`

**Purpose:** Regression invariant: parcel count order geometry crs and existing columns are preserved. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert len(result.parcels) == len(parcels)`
  - `assert result.parcels["parcel_id"].tolist() == parcels["parcel_id"].tolist()`
  - `assert (<br>        result.parcels["existing_grid_value"].tolist()<br>        == parcels["existing_grid_value"].tolist()<br>    )`
  - `assert result.parcels.crs == parcels.crs`
  - `assert result.parcels.geometry.reset_index(drop=True).equals(<br>        parcels.geometry.reset_index(drop=True)<br>    )`
  - `assert not result.parcels["parcel_id"].duplicated().any()`
  - `assert set(result.intersections["parcel_id"]).issubset(set(parcels["parcel_id"]))`
  - `assert not result.intersections.duplicated(<br>        subset=["parcel_id", "planning_zone_id"]<br>    ).any()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_rectangle` | `tests.unit.test_enrich_planning_zoning._rectangle` |
| `_run` | `tests.unit.test_enrich_planning_zoning._run` |
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels["parcel_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels["parcel_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels["existing_grid_value"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels["existing_grid_value"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels.geometry.reset_index(drop=True).equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels.geometry.reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.geometry.reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels["parcel_id"].duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels["parcel_id"].duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `set(result.intersections["parcel_id"]).issubset` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.intersections.duplicated(<br>        subset=["parcel_id", "planning_zone_id"]<br>    ).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.intersections.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `result.parcels.geometry.reset_index(drop=True).equals`<br>`result.parcels.geometry.reset_index`<br>`parcels.geometry.reset_index` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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
    assert (
        result.parcels["existing_grid_value"].tolist()
        == parcels["existing_grid_value"].tolist()
    )
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_raw_zoning_values_are_preserved_exactly`

**Purpose:** Regression invariant: raw zoning values are preserved exactly. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_raw_zoning_values_are_preserved_exactly() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert first["source_zone_id"] == "ID-É"`
  - `assert first["zone_label_raw"] == "AUf"`
  - `assert first["zone_long_label_raw"] == "Libellé Étendu"`
  - `assert first["zone_type_raw"] == "AUc"`
  - `assert second["source_zone_id"] == "id-lower"`
  - `assert second["zone_label_raw"] == "Nh"`
  - `assert pd.isna(second["zone_long_label_raw"])`
  - `assert second["zone_type_raw"] == "N"`
  - `assert pd.isna(second["regulation_filename_raw"])`
  - `assert pd.isna(second["regulation_url_raw"])`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |
| `_rectangle` | `tests.unit.test_enrich_planning_zoning._rectangle` |
| `_run` | `tests.unit.test_enrich_planning_zoning._run` |
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_row_for_source_zone` | `tests.unit.test_enrich_planning_zoning._row_for_source_zone` |
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
| In-memory mutation | `zones.loc[zones.index[1], "NOMFIC"] = None`<br>`zones.loc[zones.index[1], "URLFIC"] = None` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_intersection_table_references_only_known_parcels_and_zones`

**Purpose:** Regression invariant: intersection table references only known parcels and zones. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_intersection_table_references_only_known_parcels_and_zones() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert set(result.intersections["parcel_id"]) == {"P-1", "P-2"}`
  - `assert set(result.intersections["planning_zone_id"]) == set(<br>        result.zones["planning_zone_id"]<br>    )`
  - `assert not result.intersections.duplicated(<br>        subset=["parcel_id", "planning_zone_id"]<br>    ).any()`
  - `assert numeric.notna().all().all()`
  - `assert (numeric >= 0).all().all()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_run` | `tests.unit.test_enrich_planning_zoning._run` |
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_rectangle` | `tests.unit.test_enrich_planning_zoning._rectangle` |
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.intersections.duplicated(<br>        subset=["parcel_id", "planning_zone_id"]<br>    ).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.intersections.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `numeric.notna().all().all` | `unresolved local/third-party receiver; no ownership inferred` |
| `numeric.notna().all` | `unresolved local/third-party receiver; no ownership inferred` |
| `numeric.notna` | `unresolved local/third-party receiver; no ownership inferred` |
| `(numeric >= 0).all().all` | `unresolved local/third-party receiver; no ownership inferred` |
| `(numeric >= 0).all` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_result_frames_are_independent_from_inputs`

**Purpose:** Regression invariant: result frames are independent from inputs. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_result_frames_are_independent_from_inputs() -> None:
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
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |
| `_run` | `tests.unit.test_enrich_planning_zoning._run` |
| `result.parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.zones.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.intersections.copy` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | `parcels.loc[parcels.index[0], "existing_grid_value"] = -1`<br>`zones.loc[zones.index[0], "LIBELLE"] = "CHANGED"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_zoning_validation_accepts_physical_fixture`

**Purpose:** Regression invariant: source complete zoning validation accepts physical fixture. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_zoning_validation_accepts_physical_fixture(
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

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_physical_planning_document` | `tests.unit.test_enrich_planning_zoning._physical_planning_document` |
| `intersect_parcels_with_gpu_zoning` | `landscout.stages.enrich_planning_zoning.intersect_parcels_with_gpu_zoning` |
| `validate_normalized_planning_zoning_inputs` | `landscout.stages.enrich_planning_zoning.validate_normalized_planning_zoning_inputs` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_zoning_validation_requires_every_parcel_summary_column`

**Purpose:** Regression invariant: source complete zoning validation requires every parcel summary column. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_zoning_validation_requires_every_parcel_summary_column(
    tmp_path: Path,
    missing_column: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("missing_column", sorted(PARCEL_ZONING_OUTPUT_COLUMNS))`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `missing_column` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningZoningError, match="parcel zoning.*column")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_physical_planning_document` | `tests.unit.test_enrich_planning_zoning._physical_planning_document` |
| `intersect_parcels_with_gpu_zoning` | `landscout.stages.enrich_planning_zoning.intersect_parcels_with_gpu_zoning` |
| `pytest.raises` | `pytest.raises` |
| `validate_normalized_planning_zoning_inputs` | `landscout.stages.enrich_planning_zoning.validate_normalized_planning_zoning_inputs` |
| `factual.parcels.drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `factual.parcels.drop(columns=[missing_column])` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_zoning_validation_requires_every_parcel_summary_column(
    tmp_path: Path,
    missing_column: str,
) -> None:
    parcels = _parcels()
    document = _physical_planning_document(tmp_path)
    factual = intersect_parcels_with_gpu_zoning(parcels, document)

    with pytest.raises(PlanningZoningError, match="parcel zoning.*column"):
        validate_normalized_planning_zoning_inputs(
            document,
            factual.parcels.drop(columns=[missing_column]),
            factual.zones,
            factual.intersections,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_zoning_validation_rejects_all_missing_parcel_summaries`

**Purpose:** Regression invariant: source complete zoning validation rejects all missing parcel summaries. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_zoning_validation_rejects_all_missing_parcel_summaries(
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
  - `pytest.raises(PlanningZoningError, match="parcel zoning.*column")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_physical_planning_document` | `tests.unit.test_enrich_planning_zoning._physical_planning_document` |
| `intersect_parcels_with_gpu_zoning` | `landscout.stages.enrich_planning_zoning.intersect_parcels_with_gpu_zoning` |
| `pytest.raises` | `pytest.raises` |
| `validate_normalized_planning_zoning_inputs` | `landscout.stages.enrich_planning_zoning.validate_normalized_planning_zoning_inputs` |
| `factual.parcels.drop` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | `factual.parcels.drop(columns=list(PARCEL_ZONING_OUTPUT_COLUMNS))` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_zoning_validation_rejects_all_missing_parcel_summaries(
    tmp_path: Path,
) -> None:
    parcels = _parcels()
    document = _physical_planning_document(tmp_path)
    factual = intersect_parcels_with_gpu_zoning(parcels, document)

    with pytest.raises(PlanningZoningError, match="parcel zoning.*column"):
        validate_normalized_planning_zoning_inputs(
            document,
            factual.parcels.drop(columns=list(PARCEL_ZONING_OUTPUT_COLUMNS)),
            factual.zones,
            factual.intersections,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_zoning_validation_rejects_coordinated_mutations`

**Purpose:** Regression invariant: source complete zoning validation rejects coordinated mutations. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_zoning_validation_rejects_coordinated_mutations(
    tmp_path: Path,
    mutation: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "mutation",
    [
        "label",
        "source_id",
        "source_layer",
        "reorder",
        "missing_zone",
        "extra_zone",
        "missing_relation",
        "extra_relation",
        "coherent_metric",
        "dominant_zone",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `mutation` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningZoningError, match="source\|reconstruction\|differs")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_zones` | `tests.unit.test_enrich_planning_zoning._zones` |
| `_rectangle` | `tests.unit.test_enrich_planning_zoning._rectangle` |
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_physical_planning_document` | `tests.unit.test_enrich_planning_zoning._physical_planning_document` |
| `intersect_parcels_with_gpu_zoning` | `landscout.stages.enrich_planning_zoning.intersect_parcels_with_gpu_zoning` |
| `factual.zones.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `factual.intersections.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `factual.parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations["planning_zone_id"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `zones.iloc[::-1].reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `zones.iloc[:-1].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `zones.iloc[[0]].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `pd.concat` | `pandas.concat` |
| `relations.iloc[:-1].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `validate_normalized_planning_zoning_inputs` | `landscout.stages.enrich_planning_zoning.validate_normalized_planning_zoning_inputs` |
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
| In-memory mutation | `zones.loc[0, "zone_label_raw"] = "FORGED"`<br>`relations.loc[<br>            relations["planning_zone_id"].eq(zones.loc[0, "planning_zone_id"]),<br>            "zone_label_raw",<br>        ] = "FORGED"`<br>`zones.loc[0, "source_zone_id"] = "FORGED-ID"`<br>`zones.loc[0, "planning_zone_id"] = f"GPU:{DOCUMENT_ID}:ZONE:FORGED-ID"`<br>`relations.loc[<br>            relations["planning_zone_id"].eq(old_planning_id),<br>            ["source_zone_id", "planning_zone_id"],<br>        ] = ["FORGED-ID", f"GPU:{DOCUMENT_ID}:ZONE:FORGED-ID"]`<br>`zones["source_layer"] = "FORGED_LAYER"`<br>`relations["source_layer"] = "FORGED_LAYER"`<br>`extra["source_zone_id"] = "EXTRA"`<br>`extra["planning_zone_id"] = f"GPU:{DOCUMENT_ID}:ZONE:EXTRA"`<br>`relations.loc[0, "intersection_area_m2"] /= 2`<br>`relations.loc[0, "parcel_share_pct"] /= 2`<br>`relations.loc[0, "zone_share_pct"] /= 2`<br>`parcel_output.loc[<br>            parcel_output.index[0],<br>            "dominant_planning_zone_id",<br>        ] = zones.loc[1, "planning_zone_id"]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_zoning_validation_rejects_physical_tamper`

**Purpose:** Regression invariant: source complete zoning validation rejects physical tamper. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_zoning_validation_rejects_physical_tamper(
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
  - `pytest.raises(PlanningZoningError, match="Physical\|source")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_physical_planning_document` | `tests.unit.test_enrich_planning_zoning._physical_planning_document` |
| `intersect_parcels_with_gpu_zoning` | `landscout.stages.enrich_planning_zoning.intersect_parcels_with_gpu_zoning` |
| `document.zoning.reference.dataset_path.open` | `unresolved local/third-party receiver; no ownership inferred` |
| `stream.write` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `validate_normalized_planning_zoning_inputs` | `landscout.stages.enrich_planning_zoning.validate_normalized_planning_zoning_inputs` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `document.zoning.reference.dataset_path.open` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_zoning_validation_revalidates_physical_source_once`

**Purpose:** Regression invariant: source complete zoning validation revalidates physical source once. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_zoning_validation_revalidates_physical_source_once(
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
  - `assert revalidate.call_count == 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_planning_zoning._parcels` |
| `_physical_planning_document` | `tests.unit.test_enrich_planning_zoning._physical_planning_document` |
| `intersect_parcels_with_gpu_zoning` | `landscout.stages.enrich_planning_zoning.intersect_parcels_with_gpu_zoning` |
| `patch.object` | `unittest.mock.patch.object` |
| `validate_normalized_planning_zoning_inputs` | `landscout.stages.enrich_planning_zoning.validate_normalized_planning_zoning_inputs` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **38**.
- Pytest fixtures (decorator-proven): **0**.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_shared_overlay_tolerance_preserves_zoning_numerical_behavior` | none | pytest.raises(PlanningZoningError, match="materially exceeds") | 4 | Proves shared overlay tolerance preserves zoning numerical behavior using the exact source reproduced in section 7. |
| `test_clean_high_level_api_is_exported` | none | none | 11 | Proves clean high level api is exported using the exact source reproduced in section 7. |
| `test_result_container_is_frozen` | none | pytest.raises(FrozenInstanceError) | 0 | Proves result container is frozen using the exact source reproduced in section 7. |
| `test_one_parcel_fully_inside_one_zone` | none | none | 57 | Proves one parcel fully inside one zone using the exact source reproduced in section 7. |
| `test_parcel_split_across_two_zones` | none | none | 9 | Proves parcel split across two zones using the exact source reproduced in section 7. |
| `test_dominant_zone_tie_is_deterministic` | none | none | 5 | Proves dominant zone tie is deterministic using the exact source reproduced in section 7. |
| `test_touch_only_relation_is_preserved_but_never_dominant` | none | none | 7 | Proves touch only relation is preserved but never dominant using the exact source reproduced in section 7. |
| `test_parcel_with_no_positive_area_zone_is_preserved` | none | none | 13 | Proves parcel with no positive area zone is preserved using the exact source reproduced in section 7. |
| `test_parcel_with_no_intersecting_zone_has_zero_coverage` | none | none | 10 | Proves parcel with no intersecting zone has zero coverage using the exact source reproduced in section 7. |
| `test_overlapping_source_zones_expose_raw_sum_union_and_excess` | none | none | 5 | Proves overlapping source zones expose raw sum union and excess using the exact source reproduced in section 7. |
| `test_polygon_and_multipolygon_parcels_are_supported` | pytest.mark.parametrize(<br>    "parcel_geometry",<br>    [<br>        _rectangle(0, 0, 10, 10),<br>        MultiPolygon([_rectangle(0, 0, 5, 10), _rectangle(10, 0, 15, 10)]),<br>    ],<br>) | none | 1 | Proves polygon and multipolygon parcels are supported using the exact source reproduced in section 7. |
| `test_polygon_and_multipolygon_zones_are_supported` | pytest.mark.parametrize(<br>    ("zone_geometry", "expected_area", "expected_coverage"),<br>    [<br>        (_rectangle(0, 0, 10, 10), 100.0, 100.0),<br>        (<br>            MultiPolygon([_rectangle(0, 0, 4, 10), _rectangle(6, 0, 10, 10)]),<br>            80.0,<br>            80.0,<br>        ),<br>    ],<br>) | none | 2 | Proves polygon and multipolygon zones are supported using the exact source reproduced in section 7. |
| `test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93` | pytest.mark.parametrize("parcel_crs", ["EPSG:2154", "EPSG:4326"]) | none | 3 | Proves parcel crs is preserved while metric calculation uses lambert93 using the exact source reproduced in section 7. |
| `test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154` | none | none | 3 | Proves ignf lamb93 source zoning is normalized to epsg2154 using the exact source reproduced in section 7. |
| `test_missing_or_unusable_crs_is_rejected` | pytest.mark.parametrize(<br>    ("parcels", "zones", "message"),<br>    [<br>        (_parcels(crs=None), _zones(), "CRS"),<br>        (_parcels(), _zones(crs=None), "CRS"),<br>        (_parcels(), _zones(crs=LOCAL_ENGINEERING_CRS), "CRS"),<br>    ],<br>) | pytest.raises(PlanningZoningError, match=message) | 0 | Proves missing or unusable crs is rejected using the exact source reproduced in section 7. |
| `test_invalid_or_non_polygonal_parcel_geometry_is_rejected` | pytest.mark.parametrize(<br>    "geometry",<br>    [<br>        None,<br>        Polygon(),<br>        Polygon([(0, 0), (10, 10), (10, 0), (0, 10), (0, 0)]),<br>        Point(0, 0),<br>        LineString([(0, 0), (10, 10)]),<br>    ],<br>) | pytest.raises(PlanningZoningError, match="geometry\|Polygon") | 0 | Proves invalid or non polygonal parcel geometry is rejected using the exact source reproduced in section 7. |
| `test_invalid_or_non_polygonal_zone_geometry_is_rejected` | pytest.mark.parametrize(<br>    "geometry",<br>    [<br>        None,<br>        Polygon(),<br>        Polygon([(0, 0), (10, 10), (10, 0), (0, 10), (0, 0)]),<br>        Point(0, 0),<br>        LineString([(0, 0), (10, 10)]),<br>    ],<br>) | pytest.raises(PlanningZoningError, match="geometry\|Polygon") | 0 | Proves invalid or non polygonal zone geometry is rejected using the exact source reproduced in section 7. |
| `test_invalid_parcel_id_is_rejected` | pytest.mark.parametrize(<br>    "identifier",<br>    [None, "", "   ", " PARCEL", "PARCEL ", 123],<br>) | pytest.raises(PlanningZoningError, match="parcel_id") | 0 | Proves invalid parcel id is rejected using the exact source reproduced in section 7. |
| `test_duplicate_parcel_id_is_rejected` | none | pytest.raises(PlanningZoningError, match="parcel_id.*unique\|duplicate") | 0 | Proves duplicate parcel id is rejected using the exact source reproduced in section 7. |
| `test_missing_parcel_id_is_rejected` | none | pytest.raises(PlanningZoningError, match="parcel_id") | 0 | Proves missing parcel id is rejected using the exact source reproduced in section 7. |
| `test_geometry_must_be_the_active_parcel_geometry_column` | none | pytest.raises(PlanningZoningError, match="active") | 0 | Proves geometry must be the active parcel geometry column using the exact source reproduced in section 7. |
| `test_invalid_source_zone_id_is_rejected` | pytest.mark.parametrize(<br>    "identifier",<br>    [None, "", "   ", " ZONE", "ZONE ", 123],<br>) | pytest.raises(PlanningZoningError, match="LIB_IDZONE\|zone") | 0 | Proves invalid source zone id is rejected using the exact source reproduced in section 7. |
| `test_duplicate_source_zone_id_is_rejected` | none | pytest.raises(PlanningZoningError, match="LIB_IDZONE.*unique\|duplicate") | 0 | Proves duplicate source zone id is rejected using the exact source reproduced in section 7. |
| `test_zoning_document_reference_must_match_loaded_archive` | none | pytest.raises(PlanningZoningError, match="IDURBA\|document") | 0 | Proves zoning document reference must match loaded archive using the exact source reproduced in section 7. |
| `test_zoning_summary_lineage_and_count_must_match_bundle` | pytest.mark.parametrize(<br>    ("summary_field", "bad_value", "message"),<br>    [<br>        ("source_document_id", "different-document", "document lineage"),<br>        ("source_archive_sha256", "b" * 64, "archive lineage"),<br>        ("source_layer", "different_layer", "source layer"),<br>        ("feature_count", 999, "feature count"),<br>    ],<br>) | pytest.raises(PlanningZoningError, match=message) | 0 | Proves zoning summary lineage and count must match bundle using the exact source reproduced in section 7. |
| `test_existing_parcel_output_field_collision_is_rejected` | pytest.mark.parametrize(<br>    "reserved_column",<br>    [<br>        "zoning_coverage_pct",<br>        "dominant_zone_label_raw",<br>        "planning_document_id",<br>    ],<br>) | pytest.raises(PlanningZoningError, match="column\|output\|reserved\|collision") | 0 | Proves existing parcel output field collision is rejected using the exact source reproduced in section 7. |
| `test_every_source_zoning_field_is_required` | pytest.mark.parametrize("field", SOURCE_FIELDS) | pytest.raises(PlanningZoningError, match=field) | 0 | Proves every source zoning field is required using the exact source reproduced in section 7. |
| `test_input_frames_are_not_mutated` | none | none | 0 | Proves input frames are not mutated using the exact source reproduced in section 7. |
| `test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved` | none | none | 8 | Proves parcel count order geometry crs and existing columns are preserved using the exact source reproduced in section 7. |
| `test_raw_zoning_values_are_preserved_exactly` | none | none | 10 | Proves raw zoning values are preserved exactly using the exact source reproduced in section 7. |
| `test_intersection_table_references_only_known_parcels_and_zones` | none | none | 5 | Proves intersection table references only known parcels and zones using the exact source reproduced in section 7. |
| `test_result_frames_are_independent_from_inputs` | none | none | 0 | Proves result frames are independent from inputs using the exact source reproduced in section 7. |
| `test_source_complete_zoning_validation_accepts_physical_fixture` | none | none | 0 | Proves source complete zoning validation accepts physical fixture using the exact source reproduced in section 7. |
| `test_source_complete_zoning_validation_requires_every_parcel_summary_column` | pytest.mark.parametrize("missing_column", sorted(PARCEL_ZONING_OUTPUT_COLUMNS)) | pytest.raises(PlanningZoningError, match="parcel zoning.*column") | 0 | Proves source complete zoning validation requires every parcel summary column using the exact source reproduced in section 7. |
| `test_source_complete_zoning_validation_rejects_all_missing_parcel_summaries` | none | pytest.raises(PlanningZoningError, match="parcel zoning.*column") | 0 | Proves source complete zoning validation rejects all missing parcel summaries using the exact source reproduced in section 7. |
| `test_source_complete_zoning_validation_rejects_coordinated_mutations` | pytest.mark.parametrize(<br>    "mutation",<br>    [<br>        "label",<br>        "source_id",<br>        "source_layer",<br>        "reorder",<br>        "missing_zone",<br>        "extra_zone",<br>        "missing_relation",<br>        "extra_relation",<br>        "coherent_metric",<br>        "dominant_zone",<br>    ],<br>) | pytest.raises(PlanningZoningError, match="source\|reconstruction\|differs") | 0 | Proves source complete zoning validation rejects coordinated mutations using the exact source reproduced in section 7. |
| `test_source_complete_zoning_validation_rejects_physical_tamper` | none | pytest.raises(PlanningZoningError, match="Physical\|source") | 0 | Proves source complete zoning validation rejects physical tamper using the exact source reproduced in section 7. |
| `test_source_complete_zoning_validation_revalidates_physical_source_once` | none | none | 1 | Proves source complete zoning validation revalidates physical source once using the exact source reproduced in section 7. |

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

import importlib
import json
from copy import deepcopy
from dataclasses import FrozenInstanceError, replace
from hashlib import sha256
from pathlib import Path
from unittest.mock import patch

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd
import pytest
from geopandas.testing import assert_geodataframe_equal
from pandas.api.types import is_float_dtype, is_integer_dtype
from pandas.testing import assert_frame_equal
from shapely.geometry import (
    LineString,
    MultiPolygon,
    Point,
    Polygon,
)

from landscout import stages
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
    GpuSpatialLayerReference,
    load_gpu_source_config,
)
from landscout.stages.enrich_planning_zoning import (
    PARCEL_ZONING_OUTPUT_COLUMNS,
    ParcelZoningResult,
    PlanningZoningError,
    _stabilize_area_relationships,
    intersect_parcels_with_gpu_zoning,
    validate_normalized_planning_zoning_inputs,
)
from landscout.stages.planning_overlay import technical_overlay_tolerance

ARCHIVE_SHA256 = "a" * 64
ARCHIVE_NAME = "31395_PLU_20240215"
DOCUMENT_ID = "doc-1"
SOURCE_LAYER = "31395_ZONE_URBA_20240215"
STANDARD_MODEL = "CNIG PLU v2017"
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
LOCAL_ENGINEERING_CRS = (
    'ENGCRS["Local",EDATUM["Unknown"],CS[Cartesian,2],'
    'AXIS["x",east,LENGTHUNIT["metre",1]],'
    'AXIS["y",north,LENGTHUNIT["metre",1]]]'
)


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


def _planning_document(
    zoning: gpd.GeoDataFrame | None = None,
    *,
    archive_name: str = ARCHIVE_NAME,
    document_id: str = DOCUMENT_ID,
    source_layer: str = SOURCE_LAYER,
) -> GpuPlanningDocument:
    data = zoning if zoning is not None else _zones()
    source_config = load_gpu_source_config(Path("configs/sources/gpu_fr.yaml"))
    document = GpuDocumentMetadata(
        provider=source_config.provider,
        portal=source_config.portal,
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
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in data.dtypes.items()
        ),
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
        source_config=source_config,
        source_config_sha256=gpu_source_module._source_config_sha256(source_config),
        extraction=extraction,
        all_spatial_layers=(reference,),
        zoning=inspected,
        related_layers=(),
    )


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


def _run(
    parcels: gpd.GeoDataFrame | None = None,
    zones: gpd.GeoDataFrame | None = None,
) -> ParcelZoningResult:
    return intersect_parcels_with_gpu_zoning(
        parcels if parcels is not None else _parcels(),
        _planning_document(zones),
    )


def _row_for_source_zone(result: ParcelZoningResult, source_id: str) -> pd.Series:
    return result.zones.loc[result.zones["source_zone_id"] == source_id].iloc[0]


def test_clean_high_level_api_is_exported() -> None:
    module = importlib.import_module("landscout.stages.enrich_planning_zoning")
    expected = {
        "ParcelZoningResult",
        "PlanningZoningError",
        "intersect_parcels_with_gpu_zoning",
        "validate_normalized_planning_zoning_inputs",
    }
    assert stages.intersect_parcels_with_gpu_zoning is intersect_parcels_with_gpu_zoning
    assert "intersect_parcels_with_gpu_zoning" in stages.__all__
    assert stages.PlanningZoningError is PlanningZoningError
    assert stages.ParcelZoningResult is ParcelZoningResult
    assert "PlanningZoningError" in stages.__all__
    assert "ParcelZoningResult" in stages.__all__
    assert "PlanningZoningError" in module.__all__
    assert "ParcelZoningResult" in module.__all__
    assert set(module.__all__) == expected
    for name in expected:
        assert getattr(stages, name) is getattr(module, name)
        assert name in stages.__all__


def test_result_container_is_frozen() -> None:
    result = _run()

    with pytest.raises(FrozenInstanceError):
        result.parcels = result.parcels.copy()  # type: ignore[misc]


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
    assert (
        zone["source_portal"]
        == load_gpu_source_config(Path("configs/sources/gpu_fr.yaml")).portal
    )
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


@pytest.mark.parametrize(
    "parcel_geometry",
    [
        _rectangle(0, 0, 10, 10),
        MultiPolygon([_rectangle(0, 0, 5, 10), _rectangle(10, 0, 15, 10)]),
    ],
)
def test_polygon_and_multipolygon_parcels_are_supported(
    parcel_geometry: object,
) -> None:
    result = _run(
        _parcels([parcel_geometry]),
        _zones([_rectangle(-5, -5, 20, 15)]),
    )

    assert result.parcels.iloc[0]["zoning_coverage_pct"] == pytest.approx(100.0)


@pytest.mark.parametrize(
    ("zone_geometry", "expected_area", "expected_coverage"),
    [
        (_rectangle(0, 0, 10, 10), 100.0, 100.0),
        (
            MultiPolygon([_rectangle(0, 0, 4, 10), _rectangle(6, 0, 10, 10)]),
            80.0,
            80.0,
        ),
    ],
)
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


@pytest.mark.parametrize("parcel_crs", ["EPSG:2154", "EPSG:4326"])
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


def test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154() -> None:
    source = _zones([_rectangle(0, 0, 10, 10)], crs="IGNF:LAMB93")
    result = _run(_parcels(), source)

    assert source.crs.to_string() == "IGNF:LAMB93"
    assert result.zones.crs.to_epsg() == 2154
    assert result.zones.iloc[0].geometry.area == pytest.approx(100.0)


@pytest.mark.parametrize(
    ("parcels", "zones", "message"),
    [
        (_parcels(crs=None), _zones(), "CRS"),
        (_parcels(), _zones(crs=None), "CRS"),
        (_parcels(), _zones(crs=LOCAL_ENGINEERING_CRS), "CRS"),
    ],
)
def test_missing_or_unusable_crs_is_rejected(
    parcels: gpd.GeoDataFrame,
    zones: gpd.GeoDataFrame,
    message: str,
) -> None:
    with pytest.raises(PlanningZoningError, match=message):
        _run(parcels, zones)


@pytest.mark.parametrize(
    "geometry",
    [
        None,
        Polygon(),
        Polygon([(0, 0), (10, 10), (10, 0), (0, 10), (0, 0)]),
        Point(0, 0),
        LineString([(0, 0), (10, 10)]),
    ],
)
def test_invalid_or_non_polygonal_parcel_geometry_is_rejected(
    geometry: object,
) -> None:
    with pytest.raises(PlanningZoningError, match="geometry|Polygon"):
        _run(_parcels([geometry]), _zones())


@pytest.mark.parametrize(
    "geometry",
    [
        None,
        Polygon(),
        Polygon([(0, 0), (10, 10), (10, 0), (0, 10), (0, 0)]),
        Point(0, 0),
        LineString([(0, 0), (10, 10)]),
    ],
)
def test_invalid_or_non_polygonal_zone_geometry_is_rejected(
    geometry: object,
) -> None:
    with pytest.raises(PlanningZoningError, match="geometry|Polygon"):
        _run(_parcels(), _zones([geometry]))


@pytest.mark.parametrize(
    "identifier",
    [None, "", "   ", " PARCEL", "PARCEL ", 123],
)
def test_invalid_parcel_id_is_rejected(identifier: object) -> None:
    with pytest.raises(PlanningZoningError, match="parcel_id"):
        _run(_parcels(identifiers=[identifier]), _zones())


def test_duplicate_parcel_id_is_rejected() -> None:
    with pytest.raises(PlanningZoningError, match="parcel_id.*unique|duplicate"):
        _run(
            _parcels(
                [_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)],
                identifiers=["DUPLICATE", "DUPLICATE"],
            ),
            _zones(),
        )


def test_missing_parcel_id_is_rejected() -> None:
    parcels = _parcels().drop(columns=["parcel_id"])

    with pytest.raises(PlanningZoningError, match="parcel_id"):
        _run(parcels, _zones())


def test_geometry_must_be_the_active_parcel_geometry_column() -> None:
    parcels = _parcels().rename_geometry("shape")
    parcels["geometry"] = parcels["shape"]

    with pytest.raises(PlanningZoningError, match="active"):
        _run(parcels, _zones())


@pytest.mark.parametrize(
    "identifier",
    [None, "", "   ", " ZONE", "ZONE ", 123],
)
def test_invalid_source_zone_id_is_rejected(identifier: object) -> None:
    with pytest.raises(PlanningZoningError, match="LIB_IDZONE|zone"):
        _run(_parcels(), _zones(identifiers=[identifier]))


def test_duplicate_source_zone_id_is_rejected() -> None:
    with pytest.raises(PlanningZoningError, match="LIB_IDZONE.*unique|duplicate"):
        _run(
            _parcels(),
            _zones(
                [_rectangle(0, 0, 5, 10), _rectangle(5, 0, 10, 10)],
                identifiers=["DUPLICATE", "DUPLICATE"],
            ),
        )


def test_zoning_document_reference_must_match_loaded_archive() -> None:
    zones = _zones(document_references=["31395_PLU_WRONG"])

    with pytest.raises(PlanningZoningError, match="IDURBA|document"):
        _run(_parcels(), zones)


@pytest.mark.parametrize(
    ("summary_field", "bad_value", "message"),
    [
        ("source_document_id", "different-document", "document lineage"),
        ("source_archive_sha256", "b" * 64, "archive lineage"),
        ("source_layer", "different_layer", "source layer"),
        ("feature_count", 999, "feature count"),
    ],
)
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


@pytest.mark.parametrize(
    "reserved_column",
    [
        "zoning_coverage_pct",
        "dominant_zone_label_raw",
        "planning_document_id",
    ],
)
def test_existing_parcel_output_field_collision_is_rejected(
    reserved_column: str,
) -> None:
    parcels = _parcels()
    parcels[reserved_column] = "pre-existing-value"

    with pytest.raises(PlanningZoningError, match="column|output|reserved|collision"):
        _run(parcels, _zones())


@pytest.mark.parametrize("field", SOURCE_FIELDS)
def test_every_source_zoning_field_is_required(field: str) -> None:
    zones = _zones().drop(columns=[field])

    with pytest.raises(PlanningZoningError, match=field):
        _run(_parcels(), zones)


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
    assert (
        result.parcels["existing_grid_value"].tolist()
        == parcels["existing_grid_value"].tolist()
    )
    assert result.parcels.crs == parcels.crs
    assert result.parcels.geometry.reset_index(drop=True).equals(
        parcels.geometry.reset_index(drop=True)
    )
    assert not result.parcels["parcel_id"].duplicated().any()
    assert set(result.intersections["parcel_id"]).issubset(set(parcels["parcel_id"]))
    assert not result.intersections.duplicated(
        subset=["parcel_id", "planning_zone_id"]
    ).any()


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


@pytest.mark.parametrize("missing_column", sorted(PARCEL_ZONING_OUTPUT_COLUMNS))
def test_source_complete_zoning_validation_requires_every_parcel_summary_column(
    tmp_path: Path,
    missing_column: str,
) -> None:
    parcels = _parcels()
    document = _physical_planning_document(tmp_path)
    factual = intersect_parcels_with_gpu_zoning(parcels, document)

    with pytest.raises(PlanningZoningError, match="parcel zoning.*column"):
        validate_normalized_planning_zoning_inputs(
            document,
            factual.parcels.drop(columns=[missing_column]),
            factual.zones,
            factual.intersections,
        )


def test_source_complete_zoning_validation_rejects_all_missing_parcel_summaries(
    tmp_path: Path,
) -> None:
    parcels = _parcels()
    document = _physical_planning_document(tmp_path)
    factual = intersect_parcels_with_gpu_zoning(parcels, document)

    with pytest.raises(PlanningZoningError, match="parcel zoning.*column"):
        validate_normalized_planning_zoning_inputs(
            document,
            factual.parcels.drop(columns=list(PARCEL_ZONING_OUTPUT_COLUMNS)),
            factual.zones,
            factual.intersections,
        )


@pytest.mark.parametrize(
    "mutation",
    [
        "label",
        "source_id",
        "source_layer",
        "reorder",
        "missing_zone",
        "extra_zone",
        "missing_relation",
        "extra_relation",
        "coherent_metric",
        "dominant_zone",
    ],
)
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

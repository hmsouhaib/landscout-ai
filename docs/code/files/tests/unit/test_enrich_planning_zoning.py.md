# `tests/unit/test_enrich_planning_zoning.py`

## File identity

- Repository path: `tests/unit/test_enrich_planning_zoning.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Tests factual zoning geometry/summary preservation and the independent physical-layer reconstruction boundary using deterministic synthetic frames and temporary GeoPackages.
- Source SHA256: `0a5dfb7650061c6492f0d298c9dbd43d011a715c12fd6eb135347e5e6185b821`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for enrich planning zoning; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Tests factual zoning geometry/summary preservation and the independent physical-layer reconstruction boundary using deterministic synthetic frames and temporary GeoPackages.

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
- Function-local import inside `test_source_complete_zoning_validation_revalidates_physical_source_once`: `import landscout.stages.enrich_planning_zoning as module`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `ARCHIVE_SHA256`

- Category: module constant or closed domain.
- Exact declaration:

```python
ARCHIVE_SHA256 = "a" * 64
```

- Verified fixture consumers and meaning: Fabricated lowercase archive lineage ('a' repeated64), used by _planning_document, _physical_planning_document manifest and assertions; it is not a real ZIP digest.

### `ARCHIVE_NAME`

- Category: module constant or closed domain.
- Exact declaration:

```python
ARCHIVE_NAME = "31395_PLU_20240215"
```

- Verified fixture consumers and meaning: Synthetic logical31395_PLU_20240215 identity used for raw IDURBA, metadata and expected lineage.

### `DOCUMENT_ID`

- Category: module constant or closed domain.
- Exact declaration:

```python
DOCUMENT_ID = "doc-1"
```

- Verified fixture consumers and meaning: Synthetic doc-1 API identity used for source summaries/generated IDs and forged-ID assertions.

### `SOURCE_LAYER`

- Category: module constant or closed domain.
- Exact declaration:

```python
SOURCE_LAYER = "31395_ZONE_URBA_20240215"
```

- Verified fixture consumers and meaning: Synthetic physical zoning layer name used for reference/summary identity and the actual temporary GPKG layer.

### `STANDARD_MODEL`

- Category: module constant or closed domain.
- Exact declaration:

```python
STANDARD_MODEL = "CNIG PLU v2017"
```

- Verified fixture consumers and meaning: Synthetic CNIG PLU v2017 document/XML declaration, copied into expected normalized and parcel lineage.

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

- Verified fixture consumers and meaning: Exact eight raw-field names consumed by the missing-source-field parametrization; its eight cases require presence, not non-null raw semantics for every field.
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

- Verified fixture consumers and meaning: Parseable local Cartesian WKT used by _zones to relabel a fixture and by the unusable-transformation regression; no usable national transform is assumed.


### Executable module-import-time statements

No separate module-level expression statement is declared. Function decorators do execute at import: parametrization constructs the listed synthetic Shapely/GeoPandas fixtures, and the missing-summary decorator sorts the production column set.

## 5. Classes, models, dataclasses, and fields

No top-level class/model/dataclass is declared.

## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `test_shared_overlay_tolerance_preserves_zoning_numerical_behavior`

**Purpose, setup and observed assertion scope:** Assert a 100 m² reference has 1e-6 m² tolerance. A 5e-7 over-union is clamped to 100 with gap zero and excess retained; a 2e-6 excess raises PlanningZoningError matching 'materially exceeds'. This directly exercises the shared scalar guard, not a spatial overlay or policy threshold.

**Exact signature**

```python
def test_shared_overlay_tolerance_preserves_zoning_numerical_behavior() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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
| `technical_overlay_tolerance` | `landscout.common.planning_overlay.technical_overlay_tolerance`, reached through the stage compatibility re-export |
| `pytest.approx` | `pytest.approx` |
| `_stabilize_area_relationships` | `landscout.stages.enrich_planning_zoning._stabilize_area_relationships` |
| `pytest.raises` | `pytest.raises` |

**Effects and isolation:** The paragraph above states the helper's actual I/O, allocation, geometry and mutation scope; constructing a Path or copying a retained SHA string is not physical I/O or hashing.

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


### `_rectangle`

**Purpose, setup and observed assertion scope:** Construct and return a closed XY Shapely Polygon from the four supplied rectangle bounds in explicit corner order. No CRS is attached and no argument validation or I/O is performed.

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
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.

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

**Effects and isolation:** The paragraph above states the helper's actual I/O, allocation, geometry and mutation scope; constructing a Path or copying a retained SHA string is not physical I/O or hashing.

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


### `_parcels`

**Purpose, setup and observed assertion scope:** Build a new synthetic GeoDataFrame from the supplied geometry/ID lists, defaulting on either None or an empty list because `or` is used. Default geometry is a 100 m² square, IDs are PARCEL-1..., prior `existing_grid_value` starts at100, and index starts at50. Create in EPSG:2154, then clear CRS for None, return unchanged for2154, or actually transform via `to_crs`. This constructs test data only and never loads Cadastre.

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
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.

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

**Effects and isolation:** The paragraph above states the helper's actual I/O, allocation, geometry and mutation scope; constructing a Path or copying a retained SHA string is not physical I/O or hashing.

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


### `_zones`

**Purpose, setup and observed assertion scope:** Build a new synthetic zoning GeoDataFrame with all eight physical source fields, index starting200, generated IDs/labels, raw PDF names/URLs/date and document reference. Falsy optional lists use defaults, so an empty list does not construct an empty layer. Create EPSG:2154 geometry; clear CRS for None, relabel without coordinate conversion for IGNF:LAMB93 or local engineering CRS, otherwise transform. Deliberately supports null/invalid scalar fixtures within nonempty lists; URLs are never fetched.

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
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.

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

**Effects and isolation:** The paragraph above states the helper's actual I/O, allocation, geometry and mutation scope; constructing a Path or copying a retained SHA string is not physical I/O or hashing.

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


### `_planning_document`

**Purpose, setup and observed assertion scope:** Load the checked-in GPU YAML and canonical config SHA, then construct synthetic metadata/archive/extraction/reference/summary records around the supplied frame (or default zones only when None). Build summary schema/dtypes/null/type/quality counts from the frame and return a GpuPlanningDocument. ZIP size1234/hash'a'*64/cache paths are fabricated and no ZIP or extraction tree is created; the frame is retained by alias. This fixture exercises loaded-object calculation, not producer acquisition or archive-byte verification.

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
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.

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

**Effects and isolation:** The paragraph above states the helper's actual I/O, allocation, geometry and mutation scope; constructing a Path or copying a retained SHA string is not physical I/O or hashing.

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


### `_physical_planning_document`

**Purpose, setup and observed assertion scope:** Create `tmp_path/extraction/zoning.gpkg`, write the source via Pyogrio without pandas index, reread the actual layer, and use that freshly read frame for the synthetic planning bundle. Calculate actual GPKG size/SHA and write a schema2 extraction manifest, then replace the local reference/inventory/extraction fields. The ZIP metadata/path remains fabricated from `_planning_document`; no archive is created or extracted. The helper proves a physical layer/manifest fixture suitable for the existing spatial revalidator, not an end-to-end download trust chain.

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
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.

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

**Effects and isolation:** The paragraph above states the helper's actual I/O, allocation, geometry and mutation scope; constructing a Path or copying a retained SHA string is not physical I/O or hashing.

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


### `_run`

**Purpose, setup and observed assertion scope:** Invoke the real factual `intersect_parcels_with_gpu_zoning` with supplied parcels (default only for None) and `_planning_document(zones)`. The helper loads GPU YAML and calculates real in-memory geometry; it neither calls the separate source-complete validator nor accesses the fabricated source paths.

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
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.

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

**Effects and isolation:** The paragraph above states the helper's actual I/O, allocation, geometry and mutation scope; constructing a Path or copying a retained SHA string is not physical I/O or hashing.

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


### `_row_for_source_zone`

**Purpose, setup and observed assertion scope:** Return the first normalized catalog row whose exact `source_zone_id` equals the requested string. Intended only for a known unique test fixture; no explicit missing/duplicate check exists, and no frame is mutated.

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
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_planning_zoning::test_raw_zoning_values_are_preserved_exactly` via `_row_for_source_zone`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_raw_zoning_values_are_preserved_exactly` via `_row_for_source_zone`

Outbound call expressions and conservative ownership:
- No calls.

**Effects and isolation:** The paragraph above states the helper's actual I/O, allocation, geometry and mutation scope; constructing a Path or copying a retained SHA string is not physical I/O or hashing.

**Complete source-ordered implementation**

```python
def _row_for_source_zone(result: ParcelZoningResult, source_id: str) -> pd.Series:
    return result.zones.loc[result.zones["source_zone_id"] == source_id].iloc[0]
```


### `test_clean_high_level_api_is_exported`

**Purpose, setup and observed assertion scope:** Import the stage module and assert its exact four-name __all__, identical package re-export bindings, and membership of all four in stages.__all__. This checks object/export identity, not source validation or geometry behavior.

**Exact signature**

```python
def test_clean_high_level_api_is_exported() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The paragraph above states the helper's actual I/O, allocation, geometry and mutation scope; constructing a Path or copying a retained SHA string is not physical I/O or hashing.

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


### `test_result_container_is_frozen`

**Purpose, setup and observed assertion scope:** Build a result and attempt assigning a copied frame to result.parcels, expecting immediate FrozenInstanceError. The attempted assignment must not complete; this test does not claim nested GeoDataFrame contents are immutable.

**Exact signature**

```python
def test_result_container_is_frozen() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

**Complete source-ordered implementation**

```python
def test_result_container_is_frozen() -> None:
    result = _run()

    with pytest.raises(FrozenInstanceError):
        result.parcels = result.parcels.copy()  # type: ignore[misc]
```


### `test_one_parcel_fully_inside_one_zone`

**Purpose, setup and observed assertion scope:** Use equal100m² parcel/zone squares with explicit SOURCE-ZONE/UAa/U raw facts. Assert one row in every output, generated/source IDs and all catalog lineage/raw columns, EPSG2154 geometry/area, required relation-column membership, positive relation and100m²/100% metrics, complete zero-gap/zero-excess parcel summaries and single dominant zone. Provider/portal expectations come from official-identity config strings, not a live source; 57 AST assert statements inspect the synthetic case.

**Exact signature**

```python
def test_one_parcel_fully_inside_one_zone() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

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


### `test_parcel_split_across_two_zones`

**Purpose, setup and observed assertion scope:** Split a100m² parcel into adjacent40m²LEFT and60m²RIGHT zones. Assert two positive relations, exact expected areas, full union/coverage, RIGHT dominance with60% share and one maximum. Demonstrates area-based dominance rather than input-first selection.

**Exact signature**

```python
def test_parcel_split_across_two_zones() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

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


### `test_dominant_zone_tie_is_deterministic`

**Purpose, setup and observed assertion scope:** Provide equal50m² zones in Z-ZONE then A-ZONE order. Assert A-ZONE/generated A ID wins lexically, maximum/share are50, and tie count2; this is an exact-area tie, not a near-equality tolerance test.

**Exact signature**

```python
def test_dominant_zone_tie_is_deterministic() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

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


### `test_touch_only_relation_is_preserved_but_never_dominant`

**Purpose, setup and observed assertion scope:** Pair one coincident positive zone with a second zone touching the parcel edge. Assert AREA_OVERLAP versus TOUCH_ONLY, zero touch area/share, one positive plus one touch count and AREA as dominant. Both relations remain present.

**Exact signature**

```python
def test_touch_only_relation_is_preserved_but_never_dominant() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

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


### `test_parcel_with_no_positive_area_zone_is_preserved`

**Purpose, setup and observed assertion scope:** Use only an edge-touching zone. Assert the retained single TOUCH_ONLY relation, positive count/sum/union/coverage0, touch count1, full100m² gap and null dominant ID/source/area/share/tie. It does not reject a parcel lacking positive coverage.

**Exact signature**

```python
def test_parcel_with_no_positive_area_zone_is_preserved() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

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


### `test_parcel_with_no_intersecting_zone_has_zero_coverage`

**Purpose, setup and observed assertion scope:** Use a disjoint zone. Assert empty relation table in the exact17-column order, five float metric dtypes, integer counts and nullableInt64 tie count. Parcel count summaries and coverage are0 with100m²gap; schema remains usable when no relationships exist.

**Exact signature**

```python
def test_parcel_with_no_intersecting_zone_has_zero_coverage() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

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


### `test_overlapping_source_zones_expose_raw_sum_union_and_excess`

**Purpose, setup and observed assertion scope:** Overlay full100m² and half50m² zones on the same100m² parcel. Assert raw sum150, union100, excess50, coverage100% and gap0, distinguishing double-counted pairwise area from covered area.

**Exact signature**

```python
def test_overlapping_source_zones_expose_raw_sum_union_and_excess() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

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


### `test_polygon_and_multipolygon_parcels_are_supported`

**Purpose, setup and observed assertion scope:** Two declared cases cover a100m² Polygon and disjoint two-part100m² MultiPolygon inside a larger zone. Assert coverage100% in each; no Z/M or invalid geometry is supplied.

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

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

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


### `test_polygon_and_multipolygon_zones_are_supported`

**Purpose, setup and observed assertion scope:** Two declared cases provide a full100m² Polygon or two separated parts totaling80m². Assert catalog zone area and parcel coverage respectively100/100% and80/80%; the gap is geometric, not inferred from zone labels.

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

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

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


### `test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93`

**Purpose, setup and observed assertion scope:** Two cases start with the same100m² parcel stored as EPSG2154 or transformed EPSG4326. Assert output storage CRS unchanged and reconstructed metric parcel/intersection areas100 within1e-5m² absolute tolerance.

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

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

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


### `test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154`

**Purpose, setup and observed assertion scope:** Relabel the synthetic100m² zoning fixture IGNF:LAMB93, run the calculator, and assert source CRS remains that label while normalized CRS is EPSG2154 and area100. This tests equivalent-CRS normalization without altering the source frame.

**Exact signature**

```python
def test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

**Complete source-ordered implementation**

```python
def test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154() -> None:
    source = _zones([_rectangle(0, 0, 10, 10)], crs="IGNF:LAMB93")
    result = _run(_parcels(), source)

    assert source.crs.to_string() == "IGNF:LAMB93"
    assert result.zones.crs.to_epsg() == 2154
    assert result.zones.iloc[0].geometry.area == pytest.approx(100.0)
```


### `test_missing_or_unusable_crs_is_rejected`

**Purpose, setup and observed assertion scope:** Three parametrized frame pairs omit parcel CRS, omit zone CRS, or assign local engineering CRS to zones. `_run` must raise PlanningZoningError matching CRS; the third description is parseable but lacks a usable transformation to Lambert93.

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

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

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


### `test_invalid_or_non_polygonal_parcel_geometry_is_rejected`

**Purpose, setup and observed assertion scope:** Five parcel cases supply None, empty Polygon, self-crossing Polygon, Point, or LineString, with otherwise normal zones. Expect controlled PlanningZoningError matching geometry or Polygon; no repair is accepted.

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

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

**Complete source-ordered implementation**

```python
def test_invalid_or_non_polygonal_parcel_geometry_is_rejected(
    geometry: object,
) -> None:
    with pytest.raises(PlanningZoningError, match="geometry|Polygon"):
        _run(_parcels([geometry]), _zones())
```


### `test_invalid_or_non_polygonal_zone_geometry_is_rejected`

**Purpose, setup and observed assertion scope:** Five zone cases supply None, empty Polygon, self-crossing Polygon, Point, or LineString, with normal parcels. Expect controlled PlanningZoningError matching geometry or Polygon; quality/type rejection occurs in the calculator.

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

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

**Complete source-ordered implementation**

```python
def test_invalid_or_non_polygonal_zone_geometry_is_rejected(
    geometry: object,
) -> None:
    with pytest.raises(PlanningZoningError, match="geometry|Polygon"):
        _run(_parcels(), _zones([geometry]))
```


### `test_invalid_parcel_id_is_rejected`

**Purpose, setup and observed assertion scope:** Six cases supply None, empty text, whitespace-only text, leading space, trailing space or integer123 as the sole parcel ID. Expect PlanningZoningError matching parcel_id; identifiers are not trimmed or stringified into acceptance.

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

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

**Complete source-ordered implementation**

```python
def test_invalid_parcel_id_is_rejected(identifier: object) -> None:
    with pytest.raises(PlanningZoningError, match="parcel_id"):
        _run(_parcels(identifiers=[identifier]), _zones())
```


### `test_duplicate_parcel_id_is_rejected`

**Purpose, setup and observed assertion scope:** Construct two distinct parcel geometries sharing DUPLICATE ID. Expect PlanningZoningError matching parcel_id uniqueness/duplicate wording before producing ambiguous relations.

**Exact signature**

```python
def test_duplicate_parcel_id_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

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


### `test_missing_parcel_id_is_rejected`

**Purpose, setup and observed assertion scope:** Create a new parcel frame with parcel_id dropped (not in-place mutation) and expect `_run` to raise PlanningZoningError naming parcel_id.

**Exact signature**

```python
def test_missing_parcel_id_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

**Complete source-ordered implementation**

```python
def test_missing_parcel_id_is_rejected() -> None:
    parcels = _parcels().drop(columns=["parcel_id"])

    with pytest.raises(PlanningZoningError, match="parcel_id"):
        _run(parcels, _zones())
```


### `test_geometry_must_be_the_active_parcel_geometry_column`

**Purpose, setup and observed assertion scope:** Rename the active geometry to shape, then add a separate column literally named geometry. Expect an active-geometry error: mere geometry-column presence must not bypass the required active name.

**Exact signature**

```python
def test_geometry_must_be_the_active_parcel_geometry_column() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

**Complete source-ordered implementation**

```python
def test_geometry_must_be_the_active_parcel_geometry_column() -> None:
    parcels = _parcels().rename_geometry("shape")
    parcels["geometry"] = parcels["shape"]

    with pytest.raises(PlanningZoningError, match="active"):
        _run(parcels, _zones())
```


### `test_invalid_source_zone_id_is_rejected`

**Purpose, setup and observed assertion scope:** Six cases set raw LIB_IDZONE to None, empty/blank text, surrounding-space variants or integer123. Expect controlled PlanningZoningError matching LIB_IDZONE or zone, not silent ID coercion.

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

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

**Complete source-ordered implementation**

```python
def test_invalid_source_zone_id_is_rejected(identifier: object) -> None:
    with pytest.raises(PlanningZoningError, match="LIB_IDZONE|zone"):
        _run(_parcels(), _zones(identifiers=[identifier]))
```


### `test_duplicate_source_zone_id_is_rejected`

**Purpose, setup and observed assertion scope:** Create adjacent source polygons sharing DUPLICATE LIB_IDZONE. Expect PlanningZoningError matching the source ID uniqueness/duplicate requirement.

**Exact signature**

```python
def test_duplicate_source_zone_id_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

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


### `test_zoning_document_reference_must_match_loaded_archive`

**Purpose, setup and observed assertion scope:** Set source IDURBA to31395_PLU_WRONG while keeping loaded archive identity unchanged. Expect a controlled IDURBA/document error; this checks textual source identity consistency, not ZIP content.

**Exact signature**

```python
def test_zoning_document_reference_must_match_loaded_archive() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

**Complete source-ordered implementation**

```python
def test_zoning_document_reference_must_match_loaded_archive() -> None:
    zones = _zones(document_references=["31395_PLU_WRONG"])

    with pytest.raises(PlanningZoningError, match="IDURBA|document"):
        _run(_parcels(), zones)
```


### `test_zoning_summary_lineage_and_count_must_match_bundle`

**Purpose, setup and observed assertion scope:** Four cases replace the frozen retained summary's document ID, archive hash, layer name or feature count, then replace its outer layer/document records. The real calculator must raise the corresponding lineage/count error. Replacement constructs forged objects without modifying the original dataclasses.

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

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

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


### `test_existing_parcel_output_field_collision_is_rejected`

**Purpose, setup and observed assertion scope:** Three cases prepopulate zoning_coverage_pct, dominant_zone_label_raw or planning_document_id on a local input frame. Expect a collision/output-column PlanningZoningError; these are representative collisions, not enumeration of all21output names.

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

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

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


### `test_every_source_zoning_field_is_required`

**Purpose, setup and observed assertion scope:** Eight cases drop one SOURCE_FIELDS raw column from a new zone frame. Expect a controlled error containing that exact missing field; even nullable raw-value columns must exist.

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

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

**Complete source-ordered implementation**

```python
def test_every_source_zoning_field_is_required(field: str) -> None:
    zones = _zones().drop(columns=[field])

    with pytest.raises(PlanningZoningError, match=field):
        _run(_parcels(), zones)
```


### `test_input_frames_are_not_mutated`

**Purpose, setup and observed assertion scope:** Snapshot two EPSG4326 parcels and two source zones with deepcopy, run the calculator, then use two assert_geodataframe_equal calls to compare inputs against their snapshots. These assertion-helper calls matter even though the AST contains no `assert` statement in this test.

**Exact signature**

```python
def test_input_frames_are_not_mutated() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.

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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

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


### `test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved`

**Purpose, setup and observed assertion scope:** Calculate for deliberately reversed P-2/P-1 parcels in EPSG4326. Assert same count/ID order/prior grid values/storage CRS/geometries, unique output IDs, known relation parcel references and unique parcel-zone pairs. Geometry comparison resets indexes, while broader index preservation is a production postcondition and other equality tests.

**Exact signature**

```python
def test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

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


### `test_raw_zoning_values_are_preserved_exactly`

**Purpose, setup and observed assertion scope:** Supply accented/case-sensitive IDs and labels, a null long label, then mutate the local second source row's filename/URL to None. Assert exact raw strings and nulls in the normalized catalog; no uppercase normalization, fuzzy label mapping or URL fetch occurs.

**Exact signature**

```python
def test_raw_zoning_values_are_preserved_exactly() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

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


### `test_intersection_table_references_only_known_parcels_and_zones`

**Purpose, setup and observed assertion scope:** Use two separated parcel/zone pairs. Assert the exact expected parcel-ID set, relation zone IDs equal the catalog set, pair uniqueness, and all five relation metrics non-null and nonnegative. These assertions do not independently reconstruct every metric.

**Exact signature**

```python
def test_intersection_table_references_only_known_parcels_and_zones() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

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


### `test_result_frames_are_independent_from_inputs`

**Purpose, setup and observed assertion scope:** Snapshot all three result frames, then mutate a prior scalar attribute in the original parcels and raw LIBELLE in original zones. Three assert_frame_equal calls must show the result snapshots unchanged. This tests absence of these mutable-frame aliases, not complete deep immutability of every possible object-valued cell.

**Exact signature**

```python
def test_result_frames_are_independent_from_inputs() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.

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

**Effects and isolation:** The fixture helpers load checked-in GPU YAML and execute real in-memory geometry operations; their fabricated archive paths are not read. Only local fixture/result objects are used or intentionally changed as described above. No live network, production cache, subprocess or policy interpretation is exercised.

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


### `test_source_complete_zoning_validation_accepts_physical_fixture`

**Purpose, setup and observed assertion scope:** Create the real temporary GPKG/manifest fixture, calculate factual outputs, and call the real source-complete public validator expecting normal completion. No explicit assert is needed for this acceptance control; fixture ZIP identity remains synthetic.

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

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.

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

**Effects and isolation:** This test delegates actual temporary GPKG creation, byte hashing, manifest writing, physical validation and in-memory XY reconstruction to the reviewed helpers. It uses no live network or production cache; any additional mutation/counting behavior is described above.

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


### `test_source_complete_zoning_validation_requires_every_parcel_summary_column`

**Purpose, setup and observed assertion scope:** Enumerate all21 production PARCEL_ZONING_OUTPUT_COLUMNS in sorted order. For each physical fixture, calculate valid facts then pass a new parcel frame missing that single column; expect PlanningZoningError matching parcel zoning.*column before reconstruction can accept an amputated subset.

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

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** This test delegates actual temporary GPKG creation, byte hashing, manifest writing, physical validation and in-memory XY reconstruction to the reviewed helpers. It uses no live network or production cache; any additional mutation/counting behavior is described above.

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


### `test_source_complete_zoning_validation_rejects_all_missing_parcel_summaries`

**Purpose, setup and observed assertion scope:** Drop all21summary columns into a new parcel frame after calculating from the physical fixture, and require the same controlled missing-column failure. Unrelated pass-through fields remain present.

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

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** This test delegates actual temporary GPKG creation, byte hashing, manifest writing, physical validation and in-memory XY reconstruction to the reviewed helpers. It uses no live network or production cache; any additional mutation/counting behavior is described above.

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


### `test_source_complete_zoning_validation_rejects_coordinated_mutations`

**Purpose, setup and observed assertion scope:** Ten cases copy valid physical-fixture results then forge: aligned raw label; aligned source/generated ID; aligned source layer; catalog order; missing zone; extra unique-ID zone; missing relation; duplicated relation; coherently halved area and both shares; or dominant zone ID. The public validator must raise a source/reconstruction/differs error despite selected cross-table consistency. Physical source bytes are unchanged; no result hash is used as the authority.

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

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** This test delegates actual temporary GPKG creation, byte hashing, manifest writing, physical validation and in-memory XY reconstruction to the reviewed helpers. It uses no live network or production cache; any additional mutation/counting behavior is described above.

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


### `test_source_complete_zoning_validation_rejects_physical_tamper`

**Purpose, setup and observed assertion scope:** After calculating from the physical fixture, append literal tamper bytes to its GPKG in binary append mode. The unchanged facts must then fail public validation with a Physical/source error. This is an actual temporary-file write followed by physical integrity checking, not a read-only operation or a network attack.

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

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** This test delegates actual temporary GPKG creation, byte hashing, manifest writing, physical validation and in-memory XY reconstruction to the reviewed helpers. It uses no live network or production cache; any additional mutation/counting behavior is described above.

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


### `test_source_complete_zoning_validation_revalidates_physical_source_once`

**Purpose, setup and observed assertion scope:** Wrap the actual module-bound GPU batch revalidator using patch.object(wraps=original), run public validation, and assert exactly one call. The wrapper counts but does not bypass real physical checks; restoration occurs when the patch context exits. It does not count every lower-level filesystem read.

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

- Normal completion returns `None`.
- No explicit `raise` statement is declared here; assertion helpers, expected-exception contexts and delegated production calls have the behavior described above.
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

**Effects and isolation:** This test delegates actual temporary GPKG creation, byte hashing, manifest writing, physical validation and in-memory XY reconstruction to the reviewed helpers. It uses no live network or production cache; any additional mutation/counting behavior is described above.

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



## 7. Test-specific regression contract

- Test definitions: **38**, with **102 statically declared parametrized cases** (not a collected or executed result for this documentation audit).
- Pytest fixture functions declared in this file: **0**; `tmp_path` is supplied by pytest to physical-fixture tests, and seven ordinary helpers construct the inputs.
- All geometry operations use synthetic coordinates. `_planning_document` retains fabricated ZIP metadata/path. `_physical_planning_document` additionally writes a real temporary GPKG and manifest, but does not create a real ZIP. The full archive/PDF planning chain belongs to the separate integration suite.
- Assertion counts below count lexical `assert` statements only; they do not count `assert_frame_equal`, `assert_geodataframe_equal`, successful validator completion or `pytest.raises` as zero evidence. Every test's actual setup/attack/assertion scope is explained in section6.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | AST assert count | Declared cases / verified detail |
|---|---|---|---:|---|
| `test_shared_overlay_tolerance_preserves_zoning_numerical_behavior` | none | pytest.raises(PlanningZoningError, match="materially exceeds") | 4 | 1 declared case; manual invariant and exact assertions in section6. |
| `test_clean_high_level_api_is_exported` | none | none | 11 | 1 declared case; manual invariant and exact assertions in section6. |
| `test_result_container_is_frozen` | none | pytest.raises(FrozenInstanceError) | 0 | 1 declared case; manual invariant and exact assertions in section6. |
| `test_one_parcel_fully_inside_one_zone` | none | none | 57 | 1 declared case; manual invariant and exact assertions in section6. |
| `test_parcel_split_across_two_zones` | none | none | 9 | 1 declared case; manual invariant and exact assertions in section6. |
| `test_dominant_zone_tie_is_deterministic` | none | none | 5 | 1 declared case; manual invariant and exact assertions in section6. |
| `test_touch_only_relation_is_preserved_but_never_dominant` | none | none | 7 | 1 declared case; manual invariant and exact assertions in section6. |
| `test_parcel_with_no_positive_area_zone_is_preserved` | none | none | 13 | 1 declared case; manual invariant and exact assertions in section6. |
| `test_parcel_with_no_intersecting_zone_has_zero_coverage` | none | none | 10 | 1 declared case; manual invariant and exact assertions in section6. |
| `test_overlapping_source_zones_expose_raw_sum_union_and_excess` | none | none | 5 | 1 declared case; manual invariant and exact assertions in section6. |
| `test_polygon_and_multipolygon_parcels_are_supported` | pytest.mark.parametrize(<br>    "parcel_geometry",<br>    [<br>        _rectangle(0, 0, 10, 10),<br>        MultiPolygon([_rectangle(0, 0, 5, 10), _rectangle(10, 0, 15, 10)]),<br>    ],<br>) | none | 1 | 2 declared cases; manual invariant and exact assertions in section6. |
| `test_polygon_and_multipolygon_zones_are_supported` | pytest.mark.parametrize(<br>    ("zone_geometry", "expected_area", "expected_coverage"),<br>    [<br>        (_rectangle(0, 0, 10, 10), 100.0, 100.0),<br>        (<br>            MultiPolygon([_rectangle(0, 0, 4, 10), _rectangle(6, 0, 10, 10)]),<br>            80.0,<br>            80.0,<br>        ),<br>    ],<br>) | none | 2 | 2 declared cases; manual invariant and exact assertions in section6. |
| `test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93` | pytest.mark.parametrize("parcel_crs", ["EPSG:2154", "EPSG:4326"]) | none | 3 | 2 declared cases; manual invariant and exact assertions in section6. |
| `test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154` | none | none | 3 | 1 declared case; manual invariant and exact assertions in section6. |
| `test_missing_or_unusable_crs_is_rejected` | pytest.mark.parametrize(<br>    ("parcels", "zones", "message"),<br>    [<br>        (_parcels(crs=None), _zones(), "CRS"),<br>        (_parcels(), _zones(crs=None), "CRS"),<br>        (_parcels(), _zones(crs=LOCAL_ENGINEERING_CRS), "CRS"),<br>    ],<br>) | pytest.raises(PlanningZoningError, match=message) | 0 | 3 declared cases; manual invariant and exact assertions in section6. |
| `test_invalid_or_non_polygonal_parcel_geometry_is_rejected` | pytest.mark.parametrize(<br>    "geometry",<br>    [<br>        None,<br>        Polygon(),<br>        Polygon([(0, 0), (10, 10), (10, 0), (0, 10), (0, 0)]),<br>        Point(0, 0),<br>        LineString([(0, 0), (10, 10)]),<br>    ],<br>) | pytest.raises(PlanningZoningError, match="geometry\|Polygon") | 0 | 5 declared cases; manual invariant and exact assertions in section6. |
| `test_invalid_or_non_polygonal_zone_geometry_is_rejected` | pytest.mark.parametrize(<br>    "geometry",<br>    [<br>        None,<br>        Polygon(),<br>        Polygon([(0, 0), (10, 10), (10, 0), (0, 10), (0, 0)]),<br>        Point(0, 0),<br>        LineString([(0, 0), (10, 10)]),<br>    ],<br>) | pytest.raises(PlanningZoningError, match="geometry\|Polygon") | 0 | 5 declared cases; manual invariant and exact assertions in section6. |
| `test_invalid_parcel_id_is_rejected` | pytest.mark.parametrize(<br>    "identifier",<br>    [None, "", "   ", " PARCEL", "PARCEL ", 123],<br>) | pytest.raises(PlanningZoningError, match="parcel_id") | 0 | 6 declared cases; manual invariant and exact assertions in section6. |
| `test_duplicate_parcel_id_is_rejected` | none | pytest.raises(PlanningZoningError, match="parcel_id.*unique\|duplicate") | 0 | 1 declared case; manual invariant and exact assertions in section6. |
| `test_missing_parcel_id_is_rejected` | none | pytest.raises(PlanningZoningError, match="parcel_id") | 0 | 1 declared case; manual invariant and exact assertions in section6. |
| `test_geometry_must_be_the_active_parcel_geometry_column` | none | pytest.raises(PlanningZoningError, match="active") | 0 | 1 declared case; manual invariant and exact assertions in section6. |
| `test_invalid_source_zone_id_is_rejected` | pytest.mark.parametrize(<br>    "identifier",<br>    [None, "", "   ", " ZONE", "ZONE ", 123],<br>) | pytest.raises(PlanningZoningError, match="LIB_IDZONE\|zone") | 0 | 6 declared cases; manual invariant and exact assertions in section6. |
| `test_duplicate_source_zone_id_is_rejected` | none | pytest.raises(PlanningZoningError, match="LIB_IDZONE.*unique\|duplicate") | 0 | 1 declared case; manual invariant and exact assertions in section6. |
| `test_zoning_document_reference_must_match_loaded_archive` | none | pytest.raises(PlanningZoningError, match="IDURBA\|document") | 0 | 1 declared case; manual invariant and exact assertions in section6. |
| `test_zoning_summary_lineage_and_count_must_match_bundle` | pytest.mark.parametrize(<br>    ("summary_field", "bad_value", "message"),<br>    [<br>        ("source_document_id", "different-document", "document lineage"),<br>        ("source_archive_sha256", "b" * 64, "archive lineage"),<br>        ("source_layer", "different_layer", "source layer"),<br>        ("feature_count", 999, "feature count"),<br>    ],<br>) | pytest.raises(PlanningZoningError, match=message) | 0 | 4 declared cases; manual invariant and exact assertions in section6. |
| `test_existing_parcel_output_field_collision_is_rejected` | pytest.mark.parametrize(<br>    "reserved_column",<br>    [<br>        "zoning_coverage_pct",<br>        "dominant_zone_label_raw",<br>        "planning_document_id",<br>    ],<br>) | pytest.raises(PlanningZoningError, match="column\|output\|reserved\|collision") | 0 | 3 declared cases; manual invariant and exact assertions in section6. |
| `test_every_source_zoning_field_is_required` | pytest.mark.parametrize("field", SOURCE_FIELDS) | pytest.raises(PlanningZoningError, match=field) | 0 | 8 declared cases; manual invariant and exact assertions in section6. |
| `test_input_frames_are_not_mutated` | none | none | 0 | 1 declared case; manual invariant and exact assertions in section6. |
| `test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved` | none | none | 8 | 1 declared case; manual invariant and exact assertions in section6. |
| `test_raw_zoning_values_are_preserved_exactly` | none | none | 10 | 1 declared case; manual invariant and exact assertions in section6. |
| `test_intersection_table_references_only_known_parcels_and_zones` | none | none | 5 | 1 declared case; manual invariant and exact assertions in section6. |
| `test_result_frames_are_independent_from_inputs` | none | none | 0 | 1 declared case; manual invariant and exact assertions in section6. |
| `test_source_complete_zoning_validation_accepts_physical_fixture` | none | none | 0 | 1 declared case; manual invariant and exact assertions in section6. |
| `test_source_complete_zoning_validation_requires_every_parcel_summary_column` | pytest.mark.parametrize("missing_column", sorted(PARCEL_ZONING_OUTPUT_COLUMNS)) | pytest.raises(PlanningZoningError, match="parcel zoning.*column") | 0 | 21 declared cases; manual invariant and exact assertions in section6. |
| `test_source_complete_zoning_validation_rejects_all_missing_parcel_summaries` | none | pytest.raises(PlanningZoningError, match="parcel zoning.*column") | 0 | 1 declared case; manual invariant and exact assertions in section6. |
| `test_source_complete_zoning_validation_rejects_coordinated_mutations` | pytest.mark.parametrize(<br>    "mutation",<br>    [<br>        "label",<br>        "source_id",<br>        "source_layer",<br>        "reorder",<br>        "missing_zone",<br>        "extra_zone",<br>        "missing_relation",<br>        "extra_relation",<br>        "coherent_metric",<br>        "dominant_zone",<br>    ],<br>) | pytest.raises(PlanningZoningError, match="source\|reconstruction\|differs") | 0 | 10 declared cases; manual invariant and exact assertions in section6. |
| `test_source_complete_zoning_validation_rejects_physical_tamper` | none | pytest.raises(PlanningZoningError, match="Physical\|source") | 0 | 1 declared case; manual invariant and exact assertions in section6. |
| `test_source_complete_zoning_validation_revalidates_physical_source_once` | none | none | 1 | 1 declared case; manual invariant and exact assertions in section6. |

## 8. Public exports and package ownership

This module declares no `__all__`; no package-level public guarantee is inferred from direct importability alone.

## 9. Trust, provenance, side effects, and business boundary

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Effects and isolation are described per callable. The sole counting patch wraps the actual GPU spatial revalidator; it does not bypass it. No existing test or production behavior was modified by this documentation audit.

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

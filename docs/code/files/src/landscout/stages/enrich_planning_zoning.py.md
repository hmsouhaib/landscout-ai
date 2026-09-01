# `src/landscout/stages/enrich_planning_zoning.py`

## File identity

- Repository path: `src/landscout/stages/enrich_planning_zoning.py`
- File type: Python source
- Layer: pipeline stage
- Domain: factual transformation, evidence, or policy boundary
- Responsibility: Intersects parcels with verified GPU zoning and source-completely reconstructs every required factual parcel-summary column.
- Source SHA256: `2a4d6b9669fc091cb394b3d17f0f94effdd6a6aa74543c06ce77c2c99dabf4ec`

## 1. STEP 7F.1A.4 contract delta

- Requires the complete canonical factual zoning summary rather than accepting an amputated self-consistent subset.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Intersects parcels with verified GPU zoning and source-completely reconstructs every required factual parcel-summary column.

The file belongs to the **pipeline stage** layer and **factual transformation, evidence, or policy boundary** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `from dataclasses import dataclass, replace`
- `from math import isfinite`
- `from numbers import Real`

### Third-party packages

- `import geopandas as gpd`
- `import numpy as np`
- `import pandas as pd`
- `from pyproj import CRS`
- `from shapely import (  # type: ignore[import-untyped]
    area as shapely_area,
)`
- `from shapely import (
    force_2d,
    union_all,
)`
- `from shapely import (
    intersection as shapely_intersection,
)`

### Internal LandScout imports

- `from landscout.common.frame_integrity import deterministic_frame_schema_signature`
- `from landscout.sources.gpu_fr import (
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    revalidate_gpu_spatial_layer_sources,
)`
- `from landscout.stages.planning_overlay import technical_overlay_tolerance`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `__all__`

- Category: explicit package/module export list.
- Exact declaration:

```python
__all__ = [
    "ParcelZoningResult",
    "PlanningZoningError",
    "intersect_parcels_with_gpu_zoning",
    "validate_normalized_planning_zoning_inputs",
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `ParcelZoningResult`
  - `PlanningZoningError`
  - `intersect_parcels_with_gpu_zoning`
  - `validate_normalized_planning_zoning_inputs`

### `CALCULATION_CRS`

- Category: module constant or closed domain.
- Exact declaration:

```python
CALCULATION_CRS = "EPSG:2154"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `GPU_ZONING_SOURCE_FIELDS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
GPU_ZONING_SOURCE_FIELDS = {
    "source_zone_id": "LIB_IDZONE",
    "zone_label_raw": "LIBELLE",
    "zone_long_label_raw": "LIBELONG",
    "zone_type_raw": "TYPEZONE",
    "regulation_filename_raw": "NOMFIC",
    "regulation_url_raw": "URLFIC",
    "source_document_reference_raw": "IDURBA",
    "source_validity_date_raw": "DATVALID",
}
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact mapping keys:
  - `source_zone_id`
  - `zone_label_raw`
  - `zone_long_label_raw`
  - `zone_type_raw`
  - `regulation_filename_raw`
  - `regulation_url_raw`
  - `source_document_reference_raw`
  - `source_validity_date_raw`

### `GPU_ZONING_REQUIRED_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
GPU_ZONING_REQUIRED_COLUMNS = frozenset(
    {*GPU_ZONING_SOURCE_FIELDS.values(), "geometry"}
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `PARCEL_REQUIRED_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
PARCEL_REQUIRED_COLUMNS = frozenset({"parcel_id", "geometry"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `POLYGON_GEOMETRY_TYPES`

- Category: module constant or closed domain.
- Exact declaration:

```python
POLYGON_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `RELATION_TYPES`

- Category: module constant or closed domain.
- Exact declaration:

```python
RELATION_TYPES = frozenset({"AREA_OVERLAP", "TOUCH_ONLY"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `PARCEL_ZONING_OUTPUT_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
PARCEL_ZONING_OUTPUT_COLUMNS = frozenset(
    {
        "zoning_area_match_count",
        "zoning_touch_only_count",
        "zoning_intersection_area_sum_m2",
        "zoning_covered_union_area_m2",
        "zoning_coverage_pct",
        "zoning_gap_area_m2",
        "zoning_overlap_excess_area_m2",
        "dominant_planning_zone_id",
        "dominant_source_zone_id",
        "dominant_zone_type_raw",
        "dominant_zone_label_raw",
        "dominant_zone_long_label_raw",
        "dominant_zone_intersection_area_m2",
        "dominant_zone_share_pct",
        "dominant_zone_tie_count",
        "planning_document_id",
        "planning_document_type",
        "planning_archive_name",
        "planning_archive_sha256",
        "planning_source_layer",
        "planning_standard_model",
    }
)
```

- Qualified consumers:
  - import: `tests.unit.test_enrich_planning_zoning::<module>` via `from landscout.stages.enrich_planning_zoning import (
    PARCEL_ZONING_OUTPUT_COLUMNS,
    ParcelZoningResult,
    PlanningZoningError,
    _stabilize_area_relationships,
    intersect_parcels_with_gpu_zoning,
    validate_normalized_planning_zoning_inputs,
)`
  - value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_requires_every_parcel_summary_column` via `PARCEL_ZONING_OUTPUT_COLUMNS`
  - value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_all_missing_parcel_summaries` via `PARCEL_ZONING_OUTPUT_COLUMNS`

### `INTERSECTION_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
INTERSECTION_COLUMNS = (
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
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `parcel_id`
  - `planning_zone_id`
  - `source_zone_id`
  - `zone_type_raw`
  - `zone_label_raw`
  - `zone_long_label_raw`
  - `relation_type`
  - `parcel_metric_area_m2`
  - `zone_area_m2`
  - `intersection_area_m2`
  - `parcel_share_pct`
  - `zone_share_pct`
  - `source_document_id`
  - `source_archive_sha256`
  - `source_layer`
  - `source_validity_date_raw`
  - `regulation_filename_raw`

### `_INTERSECTION_FLOAT_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
_INTERSECTION_FLOAT_COLUMNS = frozenset(
    {
        "parcel_metric_area_m2",
        "zone_area_m2",
        "intersection_area_m2",
        "parcel_share_pct",
        "zone_share_pct",
    }
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `PlanningZoningError`

**Source purpose:** Raised when factual zoning normalization cannot be completed safely.

- Exact decorators: none.
- Exact bases: `ValueError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.enrich_planning_zoning import (
    ParcelZoningResult,
    PlanningZoningError,
    intersect_parcels_with_gpu_zoning,
    validate_normalized_planning_zoning_inputs,
)`
- constructor call: `landscout.stages.enrich_planning_zoning::_strict_nonempty_string` via `PlanningZoningError`
- value/type reference: `landscout.stages.enrich_planning_zoning::_strict_nonempty_string` via `PlanningZoningError`
- constructor call: `landscout.stages.enrich_planning_zoning::_validate_exact_string_ids` via `PlanningZoningError`
- value/type reference: `landscout.stages.enrich_planning_zoning::_validate_exact_string_ids` via `PlanningZoningError`
- constructor call: `landscout.stages.enrich_planning_zoning::_readable_crs` via `PlanningZoningError`
- value/type reference: `landscout.stages.enrich_planning_zoning::_readable_crs` via `PlanningZoningError`
- constructor call: `landscout.stages.enrich_planning_zoning::_active_geometry` via `PlanningZoningError`
- value/type reference: `landscout.stages.enrich_planning_zoning::_active_geometry` via `PlanningZoningError`
- constructor call: `landscout.stages.enrich_planning_zoning::_validate_polygon_geometries` via `PlanningZoningError`
- value/type reference: `landscout.stages.enrich_planning_zoning::_validate_polygon_geometries` via `PlanningZoningError`
- constructor call: `landscout.stages.enrich_planning_zoning::_validate_parcels` via `PlanningZoningError`
- value/type reference: `landscout.stages.enrich_planning_zoning::_validate_parcels` via `PlanningZoningError`
- constructor call: `landscout.stages.enrich_planning_zoning::_standard_model` via `PlanningZoningError`
- value/type reference: `landscout.stages.enrich_planning_zoning::_standard_model` via `PlanningZoningError`
- constructor call: `landscout.stages.enrich_planning_zoning::_validate_planning_document` via `PlanningZoningError`
- value/type reference: `landscout.stages.enrich_planning_zoning::_validate_planning_document` via `PlanningZoningError`
- constructor call: `landscout.stages.enrich_planning_zoning::_project_geometries` via `PlanningZoningError`
- value/type reference: `landscout.stages.enrich_planning_zoning::_project_geometries` via `PlanningZoningError`
- constructor call: `landscout.stages.enrich_planning_zoning::_normalize_zones` via `PlanningZoningError`
- value/type reference: `landscout.stages.enrich_planning_zoning::_normalize_zones` via `PlanningZoningError`
- constructor call: `landscout.stages.enrich_planning_zoning::_metric_parcels` via `PlanningZoningError`
- value/type reference: `landscout.stages.enrich_planning_zoning::_metric_parcels` via `PlanningZoningError`
- constructor call: `landscout.stages.enrich_planning_zoning::_candidate_intersections` via `PlanningZoningError`
- value/type reference: `landscout.stages.enrich_planning_zoning::_candidate_intersections` via `PlanningZoningError`
- constructor call: `landscout.stages.enrich_planning_zoning::_stabilize_area_relationships` via `PlanningZoningError`
- value/type reference: `landscout.stages.enrich_planning_zoning::_stabilize_area_relationships` via `PlanningZoningError`
- constructor call: `landscout.stages.enrich_planning_zoning::_parcel_summary` via `PlanningZoningError`
- value/type reference: `landscout.stages.enrich_planning_zoning::_parcel_summary` via `PlanningZoningError`
- constructor call: `landscout.stages.enrich_planning_zoning::_validate_numeric_columns` via `PlanningZoningError`
- value/type reference: `landscout.stages.enrich_planning_zoning::_validate_numeric_columns` via `PlanningZoningError`
- constructor call: `landscout.stages.enrich_planning_zoning::_validate_result` via `PlanningZoningError`
- value/type reference: `landscout.stages.enrich_planning_zoning::_validate_result` via `PlanningZoningError`
- constructor call: `landscout.stages.enrich_planning_zoning::_compare_exact_frame` via `PlanningZoningError`
- value/type reference: `landscout.stages.enrich_planning_zoning::_compare_exact_frame` via `PlanningZoningError`
- constructor call: `landscout.stages.enrich_planning_zoning::validate_normalized_planning_zoning_inputs` via `PlanningZoningError`
- value/type reference: `landscout.stages.enrich_planning_zoning::validate_normalized_planning_zoning_inputs` via `PlanningZoningError`
- import: `landscout.stages.interpret_bess_zoning::<module>` via `from landscout.stages.enrich_planning_zoning import (
    PlanningZoningError,
    validate_normalized_planning_zoning_inputs,
)`
- value/type reference: `landscout.stages.interpret_bess_zoning::validate_bess_zoning_precheck` via `PlanningZoningError`
- value/type reference: `landscout.stages.interpret_bess_zoning::interpret_bess_zoning` via `PlanningZoningError`
- import: `tests.unit.test_enrich_planning_zoning::<module>` via `from landscout.stages.enrich_planning_zoning import (
    PARCEL_ZONING_OUTPUT_COLUMNS,
    ParcelZoningResult,
    PlanningZoningError,
    _stabilize_area_relationships,
    intersect_parcels_with_gpu_zoning,
    validate_normalized_planning_zoning_inputs,
)`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_shared_overlay_tolerance_preserves_zoning_numerical_behavior` via `PlanningZoningError`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_clean_high_level_api_is_exported` via `PlanningZoningError`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_missing_or_unusable_crs_is_rejected` via `PlanningZoningError`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_invalid_or_non_polygonal_parcel_geometry_is_rejected` via `PlanningZoningError`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_invalid_or_non_polygonal_zone_geometry_is_rejected` via `PlanningZoningError`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_invalid_parcel_id_is_rejected` via `PlanningZoningError`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_duplicate_parcel_id_is_rejected` via `PlanningZoningError`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_missing_parcel_id_is_rejected` via `PlanningZoningError`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_geometry_must_be_the_active_parcel_geometry_column` via `PlanningZoningError`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_invalid_source_zone_id_is_rejected` via `PlanningZoningError`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_duplicate_source_zone_id_is_rejected` via `PlanningZoningError`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_zoning_document_reference_must_match_loaded_archive` via `PlanningZoningError`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_zoning_summary_lineage_and_count_must_match_bundle` via `PlanningZoningError`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_existing_parcel_output_field_collision_is_rejected` via `PlanningZoningError`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_every_source_zoning_field_is_required` via `PlanningZoningError`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_requires_every_parcel_summary_column` via `PlanningZoningError`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_all_missing_parcel_summaries` via `PlanningZoningError`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_coordinated_mutations` via `PlanningZoningError`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_physical_tamper` via `PlanningZoningError`

**Exact class source**

```python
class PlanningZoningError(ValueError):
    """Raised when factual zoning normalization cannot be completed safely."""
```

### `ParcelZoningResult`

**Source purpose:** Normalized zones, parcel facts, and long-form parcel/zone relations.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `parcels` | `gpd.GeoDataFrame` | `required` | `parcels: gpd.GeoDataFrame` |
| `zones` | `gpd.GeoDataFrame` | `required` | `zones: gpd.GeoDataFrame` |
| `intersections` | `pd.DataFrame` | `required` | `intersections: pd.DataFrame` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.enrich_planning_zoning import (
    ParcelZoningResult,
    PlanningZoningError,
    intersect_parcels_with_gpu_zoning,
    validate_normalized_planning_zoning_inputs,
)`
- value/type reference: `landscout.stages.enrich_planning_zoning::_validate_result` via `ParcelZoningResult`
- constructor call: `landscout.stages.enrich_planning_zoning::intersect_parcels_with_gpu_zoning` via `ParcelZoningResult`
- value/type reference: `landscout.stages.enrich_planning_zoning::intersect_parcels_with_gpu_zoning` via `ParcelZoningResult`
- import: `tests.integration.test_gpu_planning_end_to_end::<module>` via `from landscout.stages.enrich_planning_zoning import (
    ParcelZoningResult,
    intersect_parcels_with_gpu_zoning,
)`
- import: `tests.unit.test_enrich_planning_zoning::<module>` via `from landscout.stages.enrich_planning_zoning import (
    PARCEL_ZONING_OUTPUT_COLUMNS,
    ParcelZoningResult,
    PlanningZoningError,
    _stabilize_area_relationships,
    intersect_parcels_with_gpu_zoning,
    validate_normalized_planning_zoning_inputs,
)`
- value/type reference: `tests.unit.test_enrich_planning_zoning::_run` via `ParcelZoningResult`
- value/type reference: `tests.unit.test_enrich_planning_zoning::_row_for_source_zone` via `ParcelZoningResult`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_clean_high_level_api_is_exported` via `ParcelZoningResult`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_one_parcel_fully_inside_one_zone` via `ParcelZoningResult`

**Exact class source**

```python
class ParcelZoningResult:
    """Normalized zones, parcel facts, and long-form parcel/zone relations."""

    parcels: gpd.GeoDataFrame
    zones: gpd.GeoDataFrame
    intersections: pd.DataFrame
```

### `_PlanningContext`

**Source purpose:** Defines `_PlanningContext`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `provider` | `str` | `required` | `provider: str` |
| `portal` | `str` | `required` | `portal: str` |
| `commune_code` | `str` | `required` | `commune_code: str` |
| `document_id` | `str` | `required` | `document_id: str` |
| `document_type` | `str` | `required` | `document_type: str` |
| `archive_name` | `str` | `required` | `archive_name: str` |
| `archive_sha256` | `str` | `required` | `archive_sha256: str` |
| `source_layer` | `str` | `required` | `source_layer: str` |
| `standard_model` | `str \| None` | `required` | `standard_model: str \| None` |
| `source_crs` | `str` | `required` | `source_crs: str` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.stages.enrich_planning_zoning::_validate_planning_document` via `_PlanningContext`
- value/type reference: `landscout.stages.enrich_planning_zoning::_validate_planning_document` via `_PlanningContext`
- value/type reference: `landscout.stages.enrich_planning_zoning::_normalize_zones` via `_PlanningContext`
- value/type reference: `landscout.stages.enrich_planning_zoning::_parcel_summary` via `_PlanningContext`

**Exact class source**

```python
class _PlanningContext:
    provider: str
    portal: str
    commune_code: str
    document_id: str
    document_type: str
    archive_name: str
    archive_sha256: str
    source_layer: str
    standard_model: str | None
    source_crs: str
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_strict_nonempty_string`

**Purpose:** Implements `strict nonempty string` within the file role: Intersects parcels with verified GPU zoning and source-completely reconstructs every required factual parcel-summary column.

**Exact signature**

```python
def _strict_nonempty_string(value: object, label: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `value`
- Explicit raise paths:
  - `PlanningZoningError(f"{label} must be a non-empty exact string")` under lexical guard `not isinstance(value, str) or not value or value != value.strip()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_planning_zoning::_validate_exact_string_ids` via `_strict_nonempty_string`
- value/type reference: `landscout.stages.enrich_planning_zoning::_validate_exact_string_ids` via `_strict_nonempty_string`
- direct call: `landscout.stages.enrich_planning_zoning::_standard_model` via `_strict_nonempty_string`
- value/type reference: `landscout.stages.enrich_planning_zoning::_standard_model` via `_strict_nonempty_string`
- direct call: `landscout.stages.enrich_planning_zoning::_validate_planning_document` via `_strict_nonempty_string`
- value/type reference: `landscout.stages.enrich_planning_zoning::_validate_planning_document` via `_strict_nonempty_string`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningZoningError` | `landscout.stages.enrich_planning_zoning.PlanningZoningError` |

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
def _strict_nonempty_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise PlanningZoningError(f"{label} must be a non-empty exact string")
    return value
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_exact_string_ids`

**Purpose:** Implements `validate exact string ids` within the file role: Intersects parcels with verified GPU zoning and source-completely reconstructs every required factual parcel-summary column.

**Exact signature**

```python
def _validate_exact_string_ids(
    values: pd.Series,
    label: str,
    *,
    require_unique: bool,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `values` | positional-or-keyword | `pd.Series` | `required` |
| `label` | positional-or-keyword | `str` | `required` |
| `require_unique` | keyword-only | `bool` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `PlanningZoningError(f"{label} values must not be null")` under lexical guard `values.isna().any()`.
  - `PlanningZoningError(f"{label} values must be unique")` under lexical guard `require_unique and values.duplicated().any()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_planning_zoning::_validate_parcels` via `_validate_exact_string_ids`
- value/type reference: `landscout.stages.enrich_planning_zoning::_validate_parcels` via `_validate_exact_string_ids`
- direct call: `landscout.stages.enrich_planning_zoning::_validate_planning_document` via `_validate_exact_string_ids`
- value/type reference: `landscout.stages.enrich_planning_zoning::_validate_planning_document` via `_validate_exact_string_ids`
- direct call: `landscout.stages.enrich_planning_zoning::_validate_result` via `_validate_exact_string_ids`
- value/type reference: `landscout.stages.enrich_planning_zoning::_validate_result` via `_validate_exact_string_ids`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `values.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `values.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningZoningError` | `landscout.stages.enrich_planning_zoning.PlanningZoningError` |
| `values.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_nonempty_string` | `landscout.stages.enrich_planning_zoning._strict_nonempty_string` |
| `values.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `values.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _validate_exact_string_ids(
    values: pd.Series,
    label: str,
    *,
    require_unique: bool,
) -> None:
    if values.isna().any():
        raise PlanningZoningError(f"{label} values must not be null")
    for value in values.tolist():
        _strict_nonempty_string(value, label)
    if require_unique and values.duplicated().any():
        raise PlanningZoningError(f"{label} values must be unique")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_readable_crs`

**Purpose:** Implements `readable crs` within the file role: Intersects parcels with verified GPU zoning and source-completely reconstructs every required factual parcel-summary column.

**Exact signature**

```python
def _readable_crs(value: object, label: str) -> CRS:
```

- Exact decorators: none.
- Declared return annotation: `CRS`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `CRS.from_user_input(value)`
- Explicit raise paths:
  - `PlanningZoningError(f"{label} CRS is required")` under lexical guard `value is None`.
  - `PlanningZoningError(f"{label} CRS is unreadable")`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_planning_zoning::_validate_parcels` via `_readable_crs`
- value/type reference: `landscout.stages.enrich_planning_zoning::_validate_parcels` via `_readable_crs`
- direct call: `landscout.stages.enrich_planning_zoning::_validate_planning_document` via `_readable_crs`
- value/type reference: `landscout.stages.enrich_planning_zoning::_validate_planning_document` via `_readable_crs`
- direct call: `landscout.stages.enrich_planning_zoning::_project_geometries` via `_readable_crs`
- value/type reference: `landscout.stages.enrich_planning_zoning::_project_geometries` via `_readable_crs`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `PlanningZoningError` | `landscout.stages.enrich_planning_zoning.PlanningZoningError` |
| `CRS.from_user_input` | `pyproj.CRS.from_user_input` |

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
def _readable_crs(value: object, label: str) -> CRS:
    if value is None:
        raise PlanningZoningError(f"{label} CRS is required")
    try:
        return CRS.from_user_input(value)
    except Exception as error:
        raise PlanningZoningError(f"{label} CRS is unreadable") from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_active_geometry`

**Purpose:** Implements `active geometry` within the file role: Intersects parcels with verified GPU zoning and source-completely reconstructs every required factual parcel-summary column.

**Exact signature**

```python
def _active_geometry(frame: gpd.GeoDataFrame, label: str) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `PlanningZoningError(f"{label} geometry column is required")` under lexical guard `"geometry" not in frame.columns`.
  - `PlanningZoningError(f"{label} geometry column must be active")`.
  - `PlanningZoningError(f"{label} geometry column must be active")` under lexical guard `active_name != "geometry"`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_planning_zoning::_validate_parcels` via `_active_geometry`
- value/type reference: `landscout.stages.enrich_planning_zoning::_validate_parcels` via `_active_geometry`
- direct call: `landscout.stages.enrich_planning_zoning::_validate_planning_document` via `_active_geometry`
- value/type reference: `landscout.stages.enrich_planning_zoning::_validate_planning_document` via `_active_geometry`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `PlanningZoningError` | `landscout.stages.enrich_planning_zoning.PlanningZoningError` |

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
def _active_geometry(frame: gpd.GeoDataFrame, label: str) -> None:
    if "geometry" not in frame.columns:
        raise PlanningZoningError(f"{label} geometry column is required")
    try:
        active_name = frame.active_geometry_name
    except AttributeError as error:
        raise PlanningZoningError(f"{label} geometry column must be active") from error
    if active_name != "geometry":
        raise PlanningZoningError(f"{label} geometry column must be active")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_polygon_geometries`

**Purpose:** Implements `validate polygon geometries` within the file role: Intersects parcels with verified GPU zoning and source-completely reconstructs every required factual parcel-summary column.

**Exact signature**

```python
def _validate_polygon_geometries(frame: gpd.GeoDataFrame, label: str) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `PlanningZoningError(f"{label} geometry must not be null")` under lexical guard `geometry.isna().any()`.
  - `PlanningZoningError(f"{label} geometry must not be empty")` under lexical guard `geometry.is_empty.any()`.
  - `PlanningZoningError(f"{label} geometry must be valid")` under lexical guard `not geometry.is_valid.all()`.
  - `PlanningZoningError(<br>            f"{label} geometry must be Polygon or MultiPolygon; found: "<br>            + ", ".join(unexpected)<br>        )` under lexical guard `unexpected`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_planning_zoning::_validate_parcels` via `_validate_polygon_geometries`
- value/type reference: `landscout.stages.enrich_planning_zoning::_validate_parcels` via `_validate_polygon_geometries`
- direct call: `landscout.stages.enrich_planning_zoning::_validate_planning_document` via `_validate_polygon_geometries`
- value/type reference: `landscout.stages.enrich_planning_zoning::_validate_planning_document` via `_validate_polygon_geometries`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `geometry.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningZoningError` | `landscout.stages.enrich_planning_zoning.PlanningZoningError` |
| `geometry.is_empty.any` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.is_valid.all` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `geometry.isna().any`<br>`geometry.isna`<br>`geometry.is_empty.any`<br>`geometry.is_valid.all` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_polygon_geometries(frame: gpd.GeoDataFrame, label: str) -> None:
    geometry = frame.geometry
    if geometry.isna().any():
        raise PlanningZoningError(f"{label} geometry must not be null")
    if geometry.is_empty.any():
        raise PlanningZoningError(f"{label} geometry must not be empty")
    if not geometry.is_valid.all():
        raise PlanningZoningError(f"{label} geometry must be valid")
    unexpected = sorted(set(geometry.geom_type) - POLYGON_GEOMETRY_TYPES)
    if unexpected:
        raise PlanningZoningError(
            f"{label} geometry must be Polygon or MultiPolygon; found: "
            + ", ".join(unexpected)
        )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_parcels`

**Purpose:** Implements `validate parcels` within the file role: Intersects parcels with verified GPU zoning and source-completely reconstructs every required factual parcel-summary column.

**Exact signature**

```python
def _validate_parcels(parcels: gpd.GeoDataFrame) -> CRS:
```

- Exact decorators: none.
- Declared return annotation: `CRS`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `crs`
- Explicit raise paths:
  - `PlanningZoningError("Parcels must be a GeoDataFrame")` under lexical guard `not isinstance(parcels, gpd.GeoDataFrame)`.
  - `PlanningZoningError(<br>            "Parcels are missing required columns: " + ", ".join(missing)<br>        )` under lexical guard `missing`.
  - `PlanningZoningError(<br>            "Parcels already contain zoning output columns: " + ", ".join(collisions)<br>        )` under lexical guard `collisions`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_planning_zoning::intersect_parcels_with_gpu_zoning` via `_validate_parcels`
- value/type reference: `landscout.stages.enrich_planning_zoning::intersect_parcels_with_gpu_zoning` via `_validate_parcels`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningZoningError` | `landscout.stages.enrich_planning_zoning.PlanningZoningError` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `_active_geometry` | `landscout.stages.enrich_planning_zoning._active_geometry` |
| `_readable_crs` | `landscout.stages.enrich_planning_zoning._readable_crs` |
| `_validate_exact_string_ids` | `landscout.stages.enrich_planning_zoning._validate_exact_string_ids` |
| `_validate_polygon_geometries` | `landscout.stages.enrich_planning_zoning._validate_polygon_geometries` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_active_geometry` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_parcels(parcels: gpd.GeoDataFrame) -> CRS:
    if not isinstance(parcels, gpd.GeoDataFrame):
        raise PlanningZoningError("Parcels must be a GeoDataFrame")
    missing = sorted(PARCEL_REQUIRED_COLUMNS - set(parcels.columns))
    if missing:
        raise PlanningZoningError(
            "Parcels are missing required columns: " + ", ".join(missing)
        )
    collisions = sorted(PARCEL_ZONING_OUTPUT_COLUMNS & set(parcels.columns))
    if collisions:
        raise PlanningZoningError(
            "Parcels already contain zoning output columns: " + ", ".join(collisions)
        )
    _active_geometry(parcels, "Parcel")
    crs = _readable_crs(parcels.crs, "Parcel")
    _validate_exact_string_ids(parcels["parcel_id"], "parcel_id", require_unique=True)
    _validate_polygon_geometries(parcels, "Parcel")
    return crs
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_standard_model`

**Purpose:** Implements `standard model` within the file role: Intersects parcels with verified GPU zoning and source-completely reconstructs every required factual parcel-summary column.

**Exact signature**

```python
def _standard_model(planning_document: GpuPlanningDocument) -> str | None:
```

- Exact decorators: none.
- Declared return annotation: `str | None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `None`
  - `values[0]`
- Explicit raise paths:
  - `PlanningZoningError("GPU standard-model lineage is ambiguous")` under lexical guard `len(values) != 1`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_planning_zoning::_validate_planning_document` via `_standard_model`
- value/type reference: `landscout.stages.enrich_planning_zoning::_validate_planning_document` via `_standard_model`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `values.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_nonempty_string` | `landscout.stages.enrich_planning_zoning._strict_nonempty_string` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningZoningError` | `landscout.stages.enrich_planning_zoning.PlanningZoningError` |

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
| In-memory mutation | `values.append(_strict_nonempty_string(document_value, "GPU standard model"))`<br>`values.append(validated)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _standard_model(planning_document: GpuPlanningDocument) -> str | None:
    document_value = planning_document.extraction.archive.document.standard_model
    values: list[str] = []
    if document_value is not None:
        values.append(_strict_nonempty_string(document_value, "GPU standard model"))
    for value in planning_document.extraction.standard_models:
        validated = _strict_nonempty_string(value, "GPU extracted standard model")
        if validated not in values:
            values.append(validated)
    if not values:
        return None
    if len(values) != 1:
        raise PlanningZoningError("GPU standard-model lineage is ambiguous")
    return values[0]
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_planning_document`

**Purpose:** Implements `validate planning document` within the file role: Intersects parcels with verified GPU zoning and source-completely reconstructs every required factual parcel-summary column.

**Exact signature**

```python
def _validate_planning_document(
    planning_document: GpuPlanningDocument,
) -> tuple[_PlanningContext, gpd.GeoDataFrame]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[_PlanningContext, gpd.GeoDataFrame]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `context, source`
- Explicit raise paths:
  - `PlanningZoningError("planning_document must be a GpuPlanningDocument")` under lexical guard `not isinstance(planning_document, GpuPlanningDocument)`.
  - `PlanningZoningError(<br>            "GPU archive SHA256 must contain 64 hexadecimal chars"<br>        )` under lexical guard `len(archive_sha256) != 64 or any(<br>        character not in "0123456789abcdefABCDEF" for character in archive_sha256<br>    )`.
  - `PlanningZoningError("GPU planning bundle must contain its zoning layer")` under lexical guard `zoning.logical_name != "zoning"`.
  - `PlanningZoningError("GPU zoning data must be a GeoDataFrame")` under lexical guard `not isinstance(source, gpd.GeoDataFrame)`.
  - `PlanningZoningError(<br>            "GPU zoning is missing required source columns: " + ", ".join(missing)<br>        )` under lexical guard `missing`.
  - `PlanningZoningError("GPU zoning must contain at least one source zone")` under lexical guard `source.empty`.
  - `PlanningZoningError(<br>            "GPU zoning IDURBA does not match the loaded planning archive identity"<br>        )` under lexical guard `not source[source_document_column].eq(expected_document_reference).all()`.
  - `PlanningZoningError("GPU zoning summary document lineage is inconsistent")` under lexical guard `summary.source_document_id != document_id`.
  - `PlanningZoningError("GPU zoning summary archive lineage is inconsistent")` under lexical guard `summary.source_archive_sha256 != archive_sha256`.
  - `PlanningZoningError("GPU zoning summary source layer is inconsistent")` under lexical guard `summary.source_layer != source_layer`.
  - `PlanningZoningError("GPU zoning summary feature count is inconsistent")` under lexical guard `summary.feature_count != len(source)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_planning_zoning::intersect_parcels_with_gpu_zoning` via `_validate_planning_document`
- value/type reference: `landscout.stages.enrich_planning_zoning::intersect_parcels_with_gpu_zoning` via `_validate_planning_document`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningZoningError` | `landscout.stages.enrich_planning_zoning.PlanningZoningError` |
| `_strict_nonempty_string` | `landscout.stages.enrich_planning_zoning._strict_nonempty_string` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `_active_geometry` | `landscout.stages.enrich_planning_zoning._active_geometry` |
| `_readable_crs` | `landscout.stages.enrich_planning_zoning._readable_crs` |
| `_validate_polygon_geometries` | `landscout.stages.enrich_planning_zoning._validate_polygon_geometries` |
| `_validate_exact_string_ids` | `landscout.stages.enrich_planning_zoning._validate_exact_string_ids` |
| `archive_name.casefold().endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `archive_name.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `source[source_document_column].eq(expected_document_reference).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `source[source_document_column].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `_PlanningContext` | `landscout.stages.enrich_planning_zoning._PlanningContext` |
| `_standard_model` | `landscout.stages.enrich_planning_zoning._standard_model` |
| `source_crs.to_string` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_active_geometry` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_planning_document(
    planning_document: GpuPlanningDocument,
) -> tuple[_PlanningContext, gpd.GeoDataFrame]:
    if not isinstance(planning_document, GpuPlanningDocument):
        raise PlanningZoningError("planning_document must be a GpuPlanningDocument")

    archive = planning_document.extraction.archive
    document = archive.document
    provider = _strict_nonempty_string(document.provider, "GPU provider")
    portal = _strict_nonempty_string(document.portal, "GPU portal")
    commune_code = _strict_nonempty_string(document.commune_code, "GPU commune code")
    document_id = _strict_nonempty_string(document.document_id, "GPU document ID")
    document_type = _strict_nonempty_string(document.document_type, "GPU document type")
    archive_name = _strict_nonempty_string(document.archive_name, "GPU archive name")
    archive_sha256 = _strict_nonempty_string(archive.sha256, "GPU archive SHA256")
    if len(archive_sha256) != 64 or any(
        character not in "0123456789abcdefABCDEF" for character in archive_sha256
    ):
        raise PlanningZoningError(
            "GPU archive SHA256 must contain 64 hexadecimal chars"
        )

    zoning = planning_document.zoning
    if zoning.logical_name != "zoning":
        raise PlanningZoningError("GPU planning bundle must contain its zoning layer")
    source_layer = _strict_nonempty_string(
        zoning.reference.source_layer, "GPU zoning source layer"
    )
    source = zoning.data
    if not isinstance(source, gpd.GeoDataFrame):
        raise PlanningZoningError("GPU zoning data must be a GeoDataFrame")
    missing = sorted(GPU_ZONING_REQUIRED_COLUMNS - set(source.columns))
    if missing:
        raise PlanningZoningError(
            "GPU zoning is missing required source columns: " + ", ".join(missing)
        )
    _active_geometry(source, "GPU zoning")
    source_crs = _readable_crs(source.crs, "GPU zoning")
    _validate_polygon_geometries(source, "GPU zoning")
    if source.empty:
        raise PlanningZoningError("GPU zoning must contain at least one source zone")

    source_zone_column = GPU_ZONING_SOURCE_FIELDS["source_zone_id"]
    _validate_exact_string_ids(
        source[source_zone_column], source_zone_column, require_unique=True
    )
    source_document_column = GPU_ZONING_SOURCE_FIELDS["source_document_reference_raw"]
    _validate_exact_string_ids(
        source[source_document_column], source_document_column, require_unique=False
    )
    expected_document_reference = (
        archive_name[:-4] if archive_name.casefold().endswith(".zip") else archive_name
    )
    if not source[source_document_column].eq(expected_document_reference).all():
        raise PlanningZoningError(
            "GPU zoning IDURBA does not match the loaded planning archive identity"
        )

    summary = zoning.summary
    if summary.source_document_id != document_id:
        raise PlanningZoningError("GPU zoning summary document lineage is inconsistent")
    if summary.source_archive_sha256 != archive_sha256:
        raise PlanningZoningError("GPU zoning summary archive lineage is inconsistent")
    if summary.source_layer != source_layer:
        raise PlanningZoningError("GPU zoning summary source layer is inconsistent")
    if summary.feature_count != len(source):
        raise PlanningZoningError("GPU zoning summary feature count is inconsistent")

    context = _PlanningContext(
        provider=provider,
        portal=portal,
        commune_code=commune_code,
        document_id=document_id,
        document_type=document_type,
        archive_name=archive_name,
        archive_sha256=archive_sha256,
        source_layer=source_layer,
        standard_model=_standard_model(planning_document),
        source_crs=source_crs.to_string(),
    )
    return context, source
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_project_geometries`

**Purpose:** Implements `project geometries` within the file role: Intersects parcels with verified GPU zoning and source-completely reconstructs every required factual parcel-summary column.

**Exact signature**

```python
def _project_geometries(
    frame: gpd.GeoDataFrame,
    label: str,
) -> gpd.GeoSeries:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoSeries`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `projected`
- Explicit raise paths:
  - `PlanningZoningError(<br>            f"{label} CRS cannot be transformed safely to {CALCULATION_CRS}"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_planning_zoning::_normalize_zones` via `_project_geometries`
- value/type reference: `landscout.stages.enrich_planning_zoning::_normalize_zones` via `_project_geometries`
- direct call: `landscout.stages.enrich_planning_zoning::_metric_parcels` via `_project_geometries`
- value/type reference: `landscout.stages.enrich_planning_zoning::_metric_parcels` via `_project_geometries`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_readable_crs` | `landscout.stages.enrich_planning_zoning._readable_crs` |
| `CRS.from_epsg` | `pyproj.CRS.from_epsg` |
| `source_crs.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.geometry.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.geometry.to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoSeries` | `geopandas.GeoSeries` |
| `force_2d` | `shapely.force_2d` |
| `PlanningZoningError` | `landscout.stages.enrich_planning_zoning.PlanningZoningError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `frame.geometry.copy`<br>`frame.geometry.to_crs` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _project_geometries(
    frame: gpd.GeoDataFrame,
    label: str,
) -> gpd.GeoSeries:
    source_crs = _readable_crs(frame.crs, label)
    target_crs = CRS.from_epsg(2154)
    try:
        if source_crs.equals(target_crs):
            projected = frame.geometry.copy()
        else:
            projected = frame.geometry.to_crs(target_crs)
        projected = gpd.GeoSeries(
            force_2d(projected.array), index=frame.index, crs=CALCULATION_CRS
        )
    except Exception as error:
        raise PlanningZoningError(
            f"{label} CRS cannot be transformed safely to {CALCULATION_CRS}"
        ) from error
    return projected
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_normalize_zones`

**Purpose:** Implements `normalize zones` within the file role: Intersects parcels with verified GPU zoning and source-completely reconstructs every required factual parcel-summary column.

**Exact signature**

```python
def _normalize_zones(
    source: gpd.GeoDataFrame,
    context: _PlanningContext,
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `context` | positional-or-keyword | `_PlanningContext` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `zones`
- Explicit raise paths:
  - `PlanningZoningError("Normalized planning_zone_id values must be unique")` under lexical guard `planning_zone_ids.duplicated().any()`.
  - `PlanningZoningError("GPU zone areas must be finite and positive")` under lexical guard `not np.isfinite(zone_areas).all() or (zone_areas <= 0).any()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_planning_zoning::intersect_parcels_with_gpu_zoning` via `_normalize_zones`
- value/type reference: `landscout.stages.enrich_planning_zoning::intersect_parcels_with_gpu_zoning` via `_normalize_zones`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_project_geometries` | `landscout.stages.enrich_planning_zoning._project_geometries` |
| `source[GPU_ZONING_SOURCE_FIELDS["source_zone_id"]].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `source_zone_ids.map` | `unresolved local/third-party receiver; no ownership inferred` |
| `planning_zone_ids.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `planning_zone_ids.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningZoningError` | `landscout.stages.enrich_planning_zoning.PlanningZoningError` |
| `planning_zone_ids.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `source_zone_ids.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `GPU_ZONING_SOURCE_FIELDS.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `source[source_name].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `data.update` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.repeat` | `numpy.repeat` |
| `np.full` | `numpy.full` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `projected_geometry.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `zones.geometry.area.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.isfinite(zone_areas).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.isfinite` | `numpy.isfinite` |
| `(zone_areas <= 0).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `zones.reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `zones.set_crs` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `projected_geometry.to_numpy`<br>`zones.geometry.area.to_numpy`<br>`zones.set_crs` |
| External process/environment | None directly present. |
| In-memory mutation | `data[normalized_name] = source[source_name].to_numpy(copy=True)`<br>`data.update(<br>        {<br>            "source_provider": np.repeat(context.provider, count),<br>            "source_portal": np.repeat(context.portal, count),<br>            "source_commune_code": np.repeat(context.commune_code, count),<br>            "source_document_id": np.repeat(context.document_id, count),<br>            "source_document_type": np.repeat(context.document_type, count),<br>            "source_archive_name": np.repeat(context.archive_name, count),<br>            "source_archive_sha256": np.repeat(context.archive_sha256, count),<br>            "source_layer": np.repeat(context.source_layer, count),<br>            "source_standard_model": np.full(<br>                count, context.standard_model, dtype="object"<br>            ),<br>            "source_crs": np.repeat(context.source_crs, count),<br>        }<br>    )`<br>`zones["zone_area_m2"] = zone_areas`<br>`zones.set_crs(CALCULATION_CRS, allow_override=True)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _normalize_zones(
    source: gpd.GeoDataFrame,
    context: _PlanningContext,
) -> gpd.GeoDataFrame:
    projected_geometry = _project_geometries(source, "GPU zoning")
    source_zone_ids = source[GPU_ZONING_SOURCE_FIELDS["source_zone_id"]].copy()
    planning_zone_ids = source_zone_ids.map(
        lambda value: f"GPU:{context.document_id}:ZONE:{value}"
    )
    if planning_zone_ids.duplicated().any():
        raise PlanningZoningError("Normalized planning_zone_id values must be unique")

    data: dict[str, object] = {
        "planning_zone_id": planning_zone_ids.to_numpy(copy=True),
        "source_zone_id": source_zone_ids.to_numpy(copy=True),
    }
    for normalized_name, source_name in GPU_ZONING_SOURCE_FIELDS.items():
        if normalized_name == "source_zone_id":
            continue
        data[normalized_name] = source[source_name].to_numpy(copy=True)
    count = len(source)
    data.update(
        {
            "source_provider": np.repeat(context.provider, count),
            "source_portal": np.repeat(context.portal, count),
            "source_commune_code": np.repeat(context.commune_code, count),
            "source_document_id": np.repeat(context.document_id, count),
            "source_document_type": np.repeat(context.document_type, count),
            "source_archive_name": np.repeat(context.archive_name, count),
            "source_archive_sha256": np.repeat(context.archive_sha256, count),
            "source_layer": np.repeat(context.source_layer, count),
            "source_standard_model": np.full(
                count, context.standard_model, dtype="object"
            ),
            "source_crs": np.repeat(context.source_crs, count),
        }
    )
    zones = gpd.GeoDataFrame(
        data,
        geometry=projected_geometry.to_numpy(copy=True),
        crs=CALCULATION_CRS,
    )
    zone_areas = zones.geometry.area.to_numpy(dtype="float64", copy=True)
    if not np.isfinite(zone_areas).all() or (zone_areas <= 0).any():
        raise PlanningZoningError("GPU zone areas must be finite and positive")
    zones["zone_area_m2"] = zone_areas
    zones = zones.reset_index(drop=True)
    zones = zones.set_crs(CALCULATION_CRS, allow_override=True)
    return zones
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_metric_parcels`

**Purpose:** Implements `metric parcels` within the file role: Intersects parcels with verified GPU zoning and source-completely reconstructs every required factual parcel-summary column.

**Exact signature**

```python
def _metric_parcels(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `metric`
- Explicit raise paths:
  - `PlanningZoningError("Parcel metric areas must be finite and positive")` under lexical guard `not np.isfinite(areas).all() or (areas <= 0).any()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_planning_zoning::intersect_parcels_with_gpu_zoning` via `_metric_parcels`
- value/type reference: `landscout.stages.enrich_planning_zoning::intersect_parcels_with_gpu_zoning` via `_metric_parcels`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_project_geometries` | `landscout.stages.enrich_planning_zoning._project_geometries` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `np.arange` | `numpy.arange` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels["parcel_id"].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `metric.geometry.area.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.isfinite(areas).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.isfinite` | `numpy.isfinite` |
| `(areas <= 0).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningZoningError` | `landscout.stages.enrich_planning_zoning.PlanningZoningError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `geometry.to_numpy`<br>`metric.geometry.area.to_numpy` |
| External process/environment | None directly present. |
| In-memory mutation | `metric["_parcel_area_m2"] = areas` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _metric_parcels(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    geometry = _project_geometries(parcels, "Parcel")
    metric = gpd.GeoDataFrame(
        {
            "_parcel_position": np.arange(len(parcels), dtype="int64"),
            "parcel_id": parcels["parcel_id"].to_numpy(copy=True),
        },
        geometry=geometry.to_numpy(copy=True),
        crs=CALCULATION_CRS,
    )
    areas = metric.geometry.area.to_numpy(dtype="float64", copy=True)
    if not np.isfinite(areas).all() or (areas <= 0).any():
        raise PlanningZoningError("Parcel metric areas must be finite and positive")
    metric["_parcel_area_m2"] = areas
    return metric
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_empty_intersections`

**Purpose:** Implements `empty intersections` within the file role: Intersects parcels with verified GPU zoning and source-completely reconstructs every required factual parcel-summary column.

**Exact signature**

```python
def _empty_intersections() -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `pd.DataFrame(<br>        {<br>            column: pd.Series(<br>                dtype="float64" if column in _INTERSECTION_FLOAT_COLUMNS else "object"<br>            )<br>            for column in INTERSECTION_COLUMNS<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_planning_zoning::intersect_parcels_with_gpu_zoning` via `_empty_intersections`
- value/type reference: `landscout.stages.enrich_planning_zoning::intersect_parcels_with_gpu_zoning` via `_empty_intersections`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pd.DataFrame` | `pandas.DataFrame` |
| `pd.Series` | `pandas.Series` |

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
def _empty_intersections() -> pd.DataFrame:
    return pd.DataFrame(
        {
            column: pd.Series(
                dtype="float64" if column in _INTERSECTION_FLOAT_COLUMNS else "object"
            )
            for column in INTERSECTION_COLUMNS
        }
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_candidate_intersections`

**Purpose:** Implements `candidate intersections` within the file role: Intersects parcels with verified GPU zoning and source-completely reconstructs every required factual parcel-summary column.

**Exact signature**

```python
def _candidate_intersections(
    metric_parcels: gpd.GeoDataFrame,
    zones: gpd.GeoDataFrame,
) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `metric_parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `zones` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `pd.DataFrame(<br>            columns=("_parcel_position", "_zone_position", "_intersection_geometry")<br>        )`
  - `work`
- Explicit raise paths:
  - `PlanningZoningError("GPU zoning spatial-index query failed")`.
  - `PlanningZoningError("GPU zoning geometry overlay failed")`.
  - `PlanningZoningError("Intersection areas must be finite and non-negative")` under lexical guard `not np.isfinite(intersection_areas).all() or (intersection_areas < 0).any()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_planning_zoning::intersect_parcels_with_gpu_zoning` via `_candidate_intersections`
- value/type reference: `landscout.stages.enrich_planning_zoning::intersect_parcels_with_gpu_zoning` via `_candidate_intersections`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `metric_parcels[["_parcel_position", "parcel_id"]].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `metric_parcels.geometry.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.arange` | `numpy.arange` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `zones.geometry.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.sjoin` | `geopandas.sjoin` |
| `PlanningZoningError` | `landscout.stages.enrich_planning_zoning.PlanningZoningError` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `candidates["_parcel_position"].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `candidates["_zone_position"].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `shapely_intersection` | `shapely.intersection` |
| `np.asarray` | `numpy.asarray` |
| `shapely_area` | `shapely.area` |
| `np.isfinite(intersection_areas).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.isfinite` | `numpy.isfinite` |
| `(intersection_areas < 0).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `metric_parcels["_parcel_area_m2"].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `zones["zone_area_m2"].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.where` | `numpy.where` |
| `np.empty` | `numpy.empty` |
| `metric_parcels["parcel_id"].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected_zones["planning_zone_id"].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected_zones["source_zone_id"].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected_zones["zone_type_raw"].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected_zones["zone_label_raw"].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected_zones["zone_long_label_raw"].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected_zones["source_document_id"].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected_zones["source_archive_sha256"].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected_zones["source_layer"].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected_zones[<br>                "source_validity_date_raw"<br>            ].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected_zones[<br>                "regulation_filename_raw"<br>            ].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `work.sort_values(<br>        ["_parcel_position", "planning_zone_id"], kind="stable"<br>    ).reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `work.sort_values` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `selected_zones["source_archive_sha256"].to_numpy` |
| CRS/geometry/spatial calculation | `metric_parcels.geometry.to_numpy`<br>`zones.geometry.to_numpy`<br>`gpd.sjoin` |
| External process/environment | None directly present. |
| In-memory mutation | `geometry_values[:] = intersection_geometry` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _candidate_intersections(
    metric_parcels: gpd.GeoDataFrame,
    zones: gpd.GeoDataFrame,
) -> pd.DataFrame:
    parcel_candidates = gpd.GeoDataFrame(
        metric_parcels[["_parcel_position", "parcel_id"]].copy(),
        geometry=metric_parcels.geometry.to_numpy(copy=True),
        crs=CALCULATION_CRS,
    )
    zone_candidates = gpd.GeoDataFrame(
        {"_zone_position": np.arange(len(zones), dtype="int64")},
        geometry=zones.geometry.to_numpy(copy=True),
        crs=CALCULATION_CRS,
    )
    try:
        candidates = gpd.sjoin(
            parcel_candidates,
            zone_candidates,
            how="inner",
            predicate="intersects",
        )
    except Exception as error:
        raise PlanningZoningError("GPU zoning spatial-index query failed") from error
    if candidates.empty:
        return pd.DataFrame(
            columns=("_parcel_position", "_zone_position", "_intersection_geometry")
        )

    parcel_positions = candidates["_parcel_position"].to_numpy(dtype="int64", copy=True)
    zone_positions = candidates["_zone_position"].to_numpy(dtype="int64", copy=True)
    try:
        intersection_geometry = shapely_intersection(
            metric_parcels.geometry.iloc[parcel_positions].array,
            zones.geometry.iloc[zone_positions].array,
        )
        intersection_areas = np.asarray(
            shapely_area(intersection_geometry), dtype="float64"
        )
    except Exception as error:
        raise PlanningZoningError("GPU zoning geometry overlay failed") from error
    if not np.isfinite(intersection_areas).all() or (intersection_areas < 0).any():
        raise PlanningZoningError("Intersection areas must be finite and non-negative")

    parcel_areas = metric_parcels["_parcel_area_m2"].to_numpy(dtype="float64")[
        parcel_positions
    ]
    zone_areas = zones["zone_area_m2"].to_numpy(dtype="float64")[zone_positions]
    relation_types = np.where(intersection_areas > 0, "AREA_OVERLAP", "TOUCH_ONLY")
    selected_zones = zones.iloc[zone_positions]
    geometry_values = np.empty(len(intersection_geometry), dtype="object")
    geometry_values[:] = intersection_geometry

    work = pd.DataFrame(
        {
            "_parcel_position": parcel_positions,
            "_zone_position": zone_positions,
            "_intersection_geometry": geometry_values,
            "parcel_id": metric_parcels["parcel_id"].to_numpy(copy=False)[
                parcel_positions
            ],
            "planning_zone_id": selected_zones["planning_zone_id"].to_numpy(copy=True),
            "source_zone_id": selected_zones["source_zone_id"].to_numpy(copy=True),
            "zone_type_raw": selected_zones["zone_type_raw"].to_numpy(copy=True),
            "zone_label_raw": selected_zones["zone_label_raw"].to_numpy(copy=True),
            "zone_long_label_raw": selected_zones["zone_long_label_raw"].to_numpy(
                copy=True
            ),
            "relation_type": relation_types,
            "parcel_metric_area_m2": parcel_areas,
            "zone_area_m2": zone_areas,
            "intersection_area_m2": intersection_areas,
            "parcel_share_pct": 100.0 * intersection_areas / parcel_areas,
            "zone_share_pct": 100.0 * intersection_areas / zone_areas,
            "source_document_id": selected_zones["source_document_id"].to_numpy(
                copy=True
            ),
            "source_archive_sha256": selected_zones["source_archive_sha256"].to_numpy(
                copy=True
            ),
            "source_layer": selected_zones["source_layer"].to_numpy(copy=True),
            "source_validity_date_raw": selected_zones[
                "source_validity_date_raw"
            ].to_numpy(copy=True),
            "regulation_filename_raw": selected_zones[
                "regulation_filename_raw"
            ].to_numpy(copy=True),
        }
    )
    work = work.sort_values(
        ["_parcel_position", "planning_zone_id"], kind="stable"
    ).reset_index(drop=True)
    return work
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_technical_area_tolerance`

**Purpose:** Implements `technical area tolerance` within the file role: Intersects parcels with verified GPU zoning and source-completely reconstructs every required factual parcel-summary column.

**Exact signature**

```python
def _technical_area_tolerance(parcel_area_m2: float) -> float:
```

- Exact decorators: none.
- Declared return annotation: `float`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcel_area_m2` | positional-or-keyword | `float` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `technical_overlay_tolerance(parcel_area_m2)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_planning_zoning::_stabilize_area_relationships` via `_technical_area_tolerance`
- value/type reference: `landscout.stages.enrich_planning_zoning::_stabilize_area_relationships` via `_technical_area_tolerance`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `technical_overlay_tolerance` | `landscout.stages.planning_overlay.technical_overlay_tolerance` |

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
def _technical_area_tolerance(parcel_area_m2: float) -> float:
    return technical_overlay_tolerance(parcel_area_m2)
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_stabilize_area_relationships`

**Purpose:** Implements `stabilize area relationships` within the file role: Intersects parcels with verified GPU zoning and source-completely reconstructs every required factual parcel-summary column.

**Exact signature**

```python
def _stabilize_area_relationships(
    parcel_area: float,
    raw_sum: float,
    covered_union: float,
) -> tuple[float, float, float]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[float, float, float]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcel_area` | positional-or-keyword | `float` | `required` |
| `raw_sum` | positional-or-keyword | `float` | `required` |
| `covered_union` | positional-or-keyword | `float` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `covered_union, gap, overlap_excess`
- Explicit raise paths:
  - `PlanningZoningError(<br>                "Zoning covered-union area materially exceeds parcel area"<br>            )` under lexical guard `covered_union > parcel_area`.
  - `PlanningZoningError(<br>                "Zoning covered-union area materially exceeds raw intersection sum"<br>            )` under lexical guard `covered_union > raw_sum`.
  - `PlanningZoningError("Zoning area differences must not be negative")` under lexical guard `gap < 0 or overlap_excess < 0`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_planning_zoning::_parcel_summary` via `_stabilize_area_relationships`
- value/type reference: `landscout.stages.enrich_planning_zoning::_parcel_summary` via `_stabilize_area_relationships`
- import: `tests.unit.test_enrich_planning_zoning::<module>` via `from landscout.stages.enrich_planning_zoning import (
    PARCEL_ZONING_OUTPUT_COLUMNS,
    ParcelZoningResult,
    PlanningZoningError,
    _stabilize_area_relationships,
    intersect_parcels_with_gpu_zoning,
    validate_normalized_planning_zoning_inputs,
)`
- direct call: `tests.unit.test_enrich_planning_zoning::test_shared_overlay_tolerance_preserves_zoning_numerical_behavior` via `_stabilize_area_relationships`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_shared_overlay_tolerance_preserves_zoning_numerical_behavior` via `_stabilize_area_relationships`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_technical_area_tolerance` | `landscout.stages.enrich_planning_zoning._technical_area_tolerance` |
| `PlanningZoningError` | `landscout.stages.enrich_planning_zoning.PlanningZoningError` |

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
def _stabilize_area_relationships(
    parcel_area: float,
    raw_sum: float,
    covered_union: float,
) -> tuple[float, float, float]:
    tolerance = _technical_area_tolerance(parcel_area)
    if covered_union > parcel_area:
        if covered_union - parcel_area > tolerance:
            raise PlanningZoningError(
                "Zoning covered-union area materially exceeds parcel area"
            )
        covered_union = parcel_area
    if covered_union > raw_sum:
        if covered_union - raw_sum > tolerance:
            raise PlanningZoningError(
                "Zoning covered-union area materially exceeds raw intersection sum"
            )
        covered_union = raw_sum
    gap = parcel_area - covered_union
    overlap_excess = raw_sum - covered_union
    if gap < 0 or overlap_excess < 0:
        raise PlanningZoningError("Zoning area differences must not be negative")
    return covered_union, gap, overlap_excess
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_parcel_summary`

**Purpose:** Implements `parcel summary` within the file role: Intersects parcels with verified GPU zoning and source-completely reconstructs every required factual parcel-summary column.

**Exact signature**

```python
def _parcel_summary(
    parcels: gpd.GeoDataFrame,
    metric_parcels: gpd.GeoDataFrame,
    zones: gpd.GeoDataFrame,
    work: pd.DataFrame,
    context: _PlanningContext,
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `metric_parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `zones` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `work` | positional-or-keyword | `pd.DataFrame` | `required` |
| `context` | positional-or-keyword | `_PlanningContext` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `output`
- Explicit raise paths:
  - `PlanningZoningError(<br>                    "GPU zoning covered-union calculation failed"<br>                )` under lexical guard `not work.empty`.
  - `PlanningZoningError(<br>                    "GPU zoning covered-union area must be finite and non-negative"<br>                )` under lexical guard `not work.empty`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_planning_zoning::intersect_parcels_with_gpu_zoning` via `_parcel_summary`
- value/type reference: `landscout.stages.enrich_planning_zoning::intersect_parcels_with_gpu_zoning` via `_parcel_summary`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `metric_parcels["_parcel_area_m2"].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.zeros` | `numpy.zeros` |
| `parcel_areas.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.full` | `numpy.full` |
| `pd.array` | `pandas.array` |
| `touches.groupby` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `positive.groupby` | `unresolved local/third-party receiver; no ownership inferred` |
| `group["intersection_area_m2"].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `areas.sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `shapely_area` | `shapely.area` |
| `union_all` | `shapely.union_all` |
| `group["_intersection_geometry"].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningZoningError` | `landscout.stages.enrich_planning_zoning.PlanningZoningError` |
| `isfinite` | `math.isfinite` |
| `_stabilize_area_relationships` | `landscout.stages.enrich_planning_zoning._stabilize_area_relationships` |
| `areas.max` | `unresolved local/third-party receiver; no ownership inferred` |
| `tied.sort_values` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.where` | `numpy.where` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `group["_intersection_geometry"].to_numpy` |
| External process/environment | None directly present. |
| In-memory mutation | `touch_count[int(position)] = len(group)`<br>`area_match_count[position] = len(group)`<br>`raw_sum[position] = raw_area`<br>`covered_union[position] = union_area`<br>`gap[position] = parcel_gap`<br>`overlap_excess[position] = excess`<br>`dominant_planning[position] = selected["planning_zone_id"]`<br>`dominant_source[position] = selected["source_zone_id"]`<br>`dominant_type[position] = selected["zone_type_raw"]`<br>`dominant_label[position] = selected["zone_label_raw"]`<br>`dominant_long_label[position] = selected["zone_long_label_raw"]`<br>`dominant_area[position] = maximum`<br>`dominant_share[position] = 100.0 * maximum / parcel_areas[position]`<br>`dominant_ties[position] = len(tied)`<br>`output["zoning_area_match_count"] = area_match_count`<br>`output["zoning_touch_only_count"] = touch_count`<br>`output["zoning_intersection_area_sum_m2"] = raw_sum`<br>`output["zoning_covered_union_area_m2"] = covered_union`<br>`output["zoning_coverage_pct"] = np.where(<br>        gap == 0.0,<br>        100.0,<br>        100.0 * covered_union / parcel_areas,<br>    )`<br>`output["zoning_gap_area_m2"] = gap`<br>`output["zoning_overlap_excess_area_m2"] = overlap_excess`<br>`output["dominant_planning_zone_id"] = dominant_planning`<br>`output["dominant_source_zone_id"] = dominant_source`<br>`output["dominant_zone_type_raw"] = dominant_type`<br>`output["dominant_zone_label_raw"] = dominant_label`<br>`output["dominant_zone_long_label_raw"] = dominant_long_label`<br>`output["dominant_zone_intersection_area_m2"] = dominant_area`<br>`output["dominant_zone_share_pct"] = dominant_share`<br>`output["dominant_zone_tie_count"] = dominant_ties`<br>`output["planning_document_id"] = context.document_id`<br>`output["planning_document_type"] = context.document_type`<br>`output["planning_archive_name"] = context.archive_name`<br>`output["planning_archive_sha256"] = context.archive_sha256`<br>`output["planning_source_layer"] = context.source_layer`<br>`output["planning_standard_model"] = context.standard_model` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _parcel_summary(
    parcels: gpd.GeoDataFrame,
    metric_parcels: gpd.GeoDataFrame,
    zones: gpd.GeoDataFrame,
    work: pd.DataFrame,
    context: _PlanningContext,
) -> gpd.GeoDataFrame:
    count = len(parcels)
    parcel_areas = metric_parcels["_parcel_area_m2"].to_numpy(
        dtype="float64", copy=True
    )
    area_match_count = np.zeros(count, dtype="int64")
    touch_count = np.zeros(count, dtype="int64")
    raw_sum = np.zeros(count, dtype="float64")
    covered_union = np.zeros(count, dtype="float64")
    gap = parcel_areas.copy()
    overlap_excess = np.zeros(count, dtype="float64")

    dominant_planning = np.full(count, None, dtype="object")
    dominant_source = np.full(count, None, dtype="object")
    dominant_type = np.full(count, None, dtype="object")
    dominant_label = np.full(count, None, dtype="object")
    dominant_long_label = np.full(count, None, dtype="object")
    dominant_area = np.full(count, np.nan, dtype="float64")
    dominant_share = np.full(count, np.nan, dtype="float64")
    dominant_ties = pd.array([pd.NA] * count, dtype="Int64")

    if not work.empty:
        touches = work.loc[work["relation_type"] == "TOUCH_ONLY"]
        for position, group in touches.groupby("_parcel_position", sort=False):
            touch_count[int(position)] = len(group)

        positive = work.loc[work["relation_type"] == "AREA_OVERLAP"]
        for position_value, group in positive.groupby("_parcel_position", sort=False):
            position = int(position_value)
            areas = group["intersection_area_m2"].to_numpy(dtype="float64")
            area_match_count[position] = len(group)
            raw_area = float(areas.sum())
            raw_sum[position] = raw_area
            try:
                union_area = float(
                    shapely_area(union_all(group["_intersection_geometry"].to_numpy()))
                )
            except Exception as error:
                raise PlanningZoningError(
                    "GPU zoning covered-union calculation failed"
                ) from error
            if not isfinite(union_area) or union_area < 0:
                raise PlanningZoningError(
                    "GPU zoning covered-union area must be finite and non-negative"
                )
            union_area, parcel_gap, excess = _stabilize_area_relationships(
                float(parcel_areas[position]), raw_area, union_area
            )
            covered_union[position] = union_area
            gap[position] = parcel_gap
            overlap_excess[position] = excess

            maximum = float(areas.max())
            tied = group.loc[group["intersection_area_m2"] == maximum]
            selected = tied.sort_values("planning_zone_id", kind="stable").iloc[0]
            dominant_planning[position] = selected["planning_zone_id"]
            dominant_source[position] = selected["source_zone_id"]
            dominant_type[position] = selected["zone_type_raw"]
            dominant_label[position] = selected["zone_label_raw"]
            dominant_long_label[position] = selected["zone_long_label_raw"]
            dominant_area[position] = maximum
            dominant_share[position] = 100.0 * maximum / parcel_areas[position]
            dominant_ties[position] = len(tied)

    output = parcels.copy(deep=True)
    output["zoning_area_match_count"] = area_match_count
    output["zoning_touch_only_count"] = touch_count
    output["zoning_intersection_area_sum_m2"] = raw_sum
    output["zoning_covered_union_area_m2"] = covered_union
    output["zoning_coverage_pct"] = np.where(
        gap == 0.0,
        100.0,
        100.0 * covered_union / parcel_areas,
    )
    output["zoning_gap_area_m2"] = gap
    output["zoning_overlap_excess_area_m2"] = overlap_excess
    output["dominant_planning_zone_id"] = dominant_planning
    output["dominant_source_zone_id"] = dominant_source
    output["dominant_zone_type_raw"] = dominant_type
    output["dominant_zone_label_raw"] = dominant_label
    output["dominant_zone_long_label_raw"] = dominant_long_label
    output["dominant_zone_intersection_area_m2"] = dominant_area
    output["dominant_zone_share_pct"] = dominant_share
    output["dominant_zone_tie_count"] = dominant_ties
    output["planning_document_id"] = context.document_id
    output["planning_document_type"] = context.document_type
    output["planning_archive_name"] = context.archive_name
    output["planning_archive_sha256"] = context.archive_sha256
    output["planning_source_layer"] = context.source_layer
    output["planning_standard_model"] = context.standard_model
    return output
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_numeric_columns`

**Purpose:** Implements `validate numeric columns` within the file role: Intersects parcels with verified GPU zoning and source-completely reconstructs every required factual parcel-summary column.

**Exact signature**

```python
def _validate_numeric_columns(
    frame: pd.DataFrame,
    columns: tuple[str, ...] | frozenset[str],
    label: str,
    *,
    allow_null: bool,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `pd.DataFrame` | `required` |
| `columns` | positional-or-keyword | `tuple[str, ...] \| frozenset[str]` | `required` |
| `label` | positional-or-keyword | `str` | `required` |
| `allow_null` | keyword-only | `bool` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `PlanningZoningError(f"{label} is missing numeric column: {column}")` under lexical guard `column not in frame.columns`.
  - `PlanningZoningError(f"{label} {column} must not be null")` under lexical guard `pd.isna(value)`.
  - `PlanningZoningError(f"{label} {column} must be numeric")` under lexical guard `isinstance(value, bool) or not isinstance(value, Real)`.
  - `PlanningZoningError(f"{label} {column} must be finite")`.
  - `PlanningZoningError(<br>                    f"{label} {column} must be finite and non-negative"<br>                )` under lexical guard `not isfinite(numeric) or numeric < 0`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_planning_zoning::_validate_result` via `_validate_numeric_columns`
- value/type reference: `landscout.stages.enrich_planning_zoning::_validate_result` via `_validate_numeric_columns`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `PlanningZoningError` | `landscout.stages.enrich_planning_zoning.PlanningZoningError` |
| `frame[column].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.isna` | `pandas.isna` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `isfinite` | `math.isfinite` |

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
def _validate_numeric_columns(
    frame: pd.DataFrame,
    columns: tuple[str, ...] | frozenset[str],
    label: str,
    *,
    allow_null: bool,
) -> None:
    for column in columns:
        if column not in frame.columns:
            raise PlanningZoningError(f"{label} is missing numeric column: {column}")
        for value in frame[column].tolist():
            if pd.isna(value):
                if allow_null:
                    continue
                raise PlanningZoningError(f"{label} {column} must not be null")
            if isinstance(value, bool) or not isinstance(value, Real):
                raise PlanningZoningError(f"{label} {column} must be numeric")
            try:
                numeric = float(value)
            except (TypeError, ValueError, OverflowError) as error:
                raise PlanningZoningError(f"{label} {column} must be finite") from error
            if not isfinite(numeric) or numeric < 0:
                raise PlanningZoningError(
                    f"{label} {column} must be finite and non-negative"
                )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_result`

**Purpose:** Implements `validate result` within the file role: Intersects parcels with verified GPU zoning and source-completely reconstructs every required factual parcel-summary column.

**Exact signature**

```python
def _validate_result(
    input_parcels: gpd.GeoDataFrame,
    result: ParcelZoningResult,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `input_parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `result` | positional-or-keyword | `ParcelZoningResult` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `PlanningZoningError("Parcel zoning output count changed")` under lexical guard `len(output) != len(input_parcels)`.
  - `PlanningZoningError("Parcel zoning output IDs or order changed")` under lexical guard `output["parcel_id"].tolist() != input_parcels["parcel_id"].tolist()`.
  - `PlanningZoningError("Parcel zoning output index changed")` under lexical guard `not output.index.equals(input_parcels.index)`.
  - `PlanningZoningError("Parcel zoning output CRS changed")` under lexical guard `output.crs != input_parcels.crs`.
  - `PlanningZoningError("Parcel zoning output geometry changed")` under lexical guard `not np.array_equal(output.geometry.to_wkb(), input_parcels.geometry.to_wkb())`.
  - `PlanningZoningError("Normalized zones must use EPSG:2154")` under lexical guard `not CRS.from_user_input(result.zones.crs).equals(CRS.from_epsg(2154))`.
  - `PlanningZoningError(<br>            "Intersection table is missing columns: " + ", ".join(missing)<br>        )` under lexical guard `missing`.
  - `PlanningZoningError("Parcel/zone intersection pairs must be unique")` under lexical guard `intersections.duplicated(["parcel_id", "planning_zone_id"]).any()`.
  - `PlanningZoningError("Intersection table contains an unknown parcel ID")` under lexical guard `not set(intersections["parcel_id"]).issubset(set(output["parcel_id"]))`.
  - `PlanningZoningError("Intersection table contains an unknown zone ID")` under lexical guard `not set(intersections["planning_zone_id"]).issubset(<br>        set(result.zones["planning_zone_id"])<br>    )`.
  - `PlanningZoningError("Intersection table has an unknown relation type")` under lexical guard `not set(intersections["relation_type"]).issubset(RELATION_TYPES)`.
  - `PlanningZoningError("Parcel zoning coverage must not exceed 100 percent")` under lexical guard `(coverage > 100.0).any()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_planning_zoning::intersect_parcels_with_gpu_zoning` via `_validate_result`
- value/type reference: `landscout.stages.enrich_planning_zoning::intersect_parcels_with_gpu_zoning` via `_validate_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningZoningError` | `landscout.stages.enrich_planning_zoning.PlanningZoningError` |
| `output["parcel_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `input_parcels["parcel_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `output.index.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.array_equal` | `numpy.array_equal` |
| `output.geometry.to_wkb` | `unresolved local/third-party receiver; no ownership inferred` |
| `input_parcels.geometry.to_wkb` | `unresolved local/third-party receiver; no ownership inferred` |
| `CRS.from_user_input(result.zones.crs).equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `CRS.from_user_input` | `pyproj.CRS.from_user_input` |
| `CRS.from_epsg` | `pyproj.CRS.from_epsg` |
| `_validate_exact_string_ids` | `landscout.stages.enrich_planning_zoning._validate_exact_string_ids` |
| `_validate_numeric_columns` | `landscout.stages.enrich_planning_zoning._validate_numeric_columns` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `intersections.duplicated(["parcel_id", "planning_zone_id"]).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `intersections.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `set(intersections["parcel_id"]).issubset` | `unresolved local/third-party receiver; no ownership inferred` |
| `set(intersections["planning_zone_id"]).issubset` | `unresolved local/third-party receiver; no ownership inferred` |
| `set(intersections["relation_type"]).issubset` | `unresolved local/third-party receiver; no ownership inferred` |
| `output["zoning_coverage_pct"].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `(coverage > 100.0).any` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `output.geometry.to_wkb`<br>`input_parcels.geometry.to_wkb` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_result(
    input_parcels: gpd.GeoDataFrame,
    result: ParcelZoningResult,
) -> None:
    output = result.parcels
    if len(output) != len(input_parcels):
        raise PlanningZoningError("Parcel zoning output count changed")
    if output["parcel_id"].tolist() != input_parcels["parcel_id"].tolist():
        raise PlanningZoningError("Parcel zoning output IDs or order changed")
    if not output.index.equals(input_parcels.index):
        raise PlanningZoningError("Parcel zoning output index changed")
    if output.crs != input_parcels.crs:
        raise PlanningZoningError("Parcel zoning output CRS changed")
    if not np.array_equal(output.geometry.to_wkb(), input_parcels.geometry.to_wkb()):
        raise PlanningZoningError("Parcel zoning output geometry changed")

    if not CRS.from_user_input(result.zones.crs).equals(CRS.from_epsg(2154)):
        raise PlanningZoningError("Normalized zones must use EPSG:2154")
    _validate_exact_string_ids(
        result.zones["planning_zone_id"],
        "planning_zone_id",
        require_unique=True,
    )
    _validate_numeric_columns(
        result.zones, ("zone_area_m2",), "Normalized zone", allow_null=False
    )

    intersections = result.intersections
    missing = sorted(set(INTERSECTION_COLUMNS) - set(intersections.columns))
    if missing:
        raise PlanningZoningError(
            "Intersection table is missing columns: " + ", ".join(missing)
        )
    if intersections.duplicated(["parcel_id", "planning_zone_id"]).any():
        raise PlanningZoningError("Parcel/zone intersection pairs must be unique")
    if not set(intersections["parcel_id"]).issubset(set(output["parcel_id"])):
        raise PlanningZoningError("Intersection table contains an unknown parcel ID")
    if not set(intersections["planning_zone_id"]).issubset(
        set(result.zones["planning_zone_id"])
    ):
        raise PlanningZoningError("Intersection table contains an unknown zone ID")
    if not set(intersections["relation_type"]).issubset(RELATION_TYPES):
        raise PlanningZoningError("Intersection table has an unknown relation type")
    _validate_numeric_columns(
        intersections,
        _INTERSECTION_FLOAT_COLUMNS,
        "Intersection table",
        allow_null=False,
    )

    required_summary = (
        "zoning_area_match_count",
        "zoning_touch_only_count",
        "zoning_intersection_area_sum_m2",
        "zoning_covered_union_area_m2",
        "zoning_coverage_pct",
        "zoning_gap_area_m2",
        "zoning_overlap_excess_area_m2",
    )
    _validate_numeric_columns(
        output, required_summary, "Parcel zoning", allow_null=False
    )
    coverage = output["zoning_coverage_pct"].to_numpy(dtype="float64")
    if (coverage > 100.0).any():
        raise PlanningZoningError("Parcel zoning coverage must not exceed 100 percent")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_compare_exact_frame`

**Purpose:** Implements `compare exact frame` within the file role: Intersects parcels with verified GPU zoning and source-completely reconstructs every required factual parcel-summary column.

**Exact signature**

```python
def _compare_exact_frame(
    supplied: pd.DataFrame,
    expected: pd.DataFrame,
    label: str,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `supplied` | positional-or-keyword | `pd.DataFrame` | `required` |
| `expected` | positional-or-keyword | `pd.DataFrame` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `PlanningZoningError(f"{label} frame type differs from reconstruction")` under lexical guard `type(supplied) is not type(expected)`.
  - `PlanningZoningError(f"{label} schema differs from reconstruction")` under lexical guard `deterministic_frame_schema_signature(<br>            supplied<br>        ) != deterministic_frame_schema_signature(expected)`.
  - `PlanningZoningError(<br>                    f"{label} values or row order differ from reconstruction"<br>                )` under lexical guard `isinstance(expected, gpd.GeoDataFrame)`.
  - `PlanningZoningError(<br>                    f"{label} geometry or row order differs from reconstruction"<br>                )` under lexical guard `isinstance(expected, gpd.GeoDataFrame)`.
  - `PlanningZoningError(<br>                f"{label} values or row order differ from reconstruction"<br>            )` under lexical guard `isinstance(expected, gpd.GeoDataFrame)`.
  - `re-raise`.
  - `PlanningZoningError(<br>            f"{label} cannot be compared safely with its reconstruction"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_planning_zoning::validate_normalized_planning_zoning_inputs` via `_compare_exact_frame`
- value/type reference: `landscout.stages.enrich_planning_zoning::validate_normalized_planning_zoning_inputs` via `_compare_exact_frame`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningZoningError` | `landscout.stages.enrich_planning_zoning.PlanningZoningError` |
| `deterministic_frame_schema_signature` | `landscout.common.frame_integrity.deterministic_frame_schema_signature` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `supplied[attributes].equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `supplied.geometry.to_wkb().tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `supplied.geometry.to_wkb` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected.geometry.to_wkb().tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected.geometry.to_wkb` | `unresolved local/third-party receiver; no ownership inferred` |
| `supplied.equals` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `supplied.geometry.to_wkb().tolist`<br>`supplied.geometry.to_wkb`<br>`expected.geometry.to_wkb().tolist`<br>`expected.geometry.to_wkb` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _compare_exact_frame(
    supplied: pd.DataFrame,
    expected: pd.DataFrame,
    label: str,
) -> None:
    try:
        if type(supplied) is not type(expected):
            raise PlanningZoningError(f"{label} frame type differs from reconstruction")
        if deterministic_frame_schema_signature(
            supplied
        ) != deterministic_frame_schema_signature(expected):
            raise PlanningZoningError(f"{label} schema differs from reconstruction")
        if isinstance(expected, gpd.GeoDataFrame):
            geometry_column = expected.geometry.name
            attributes = [
                column for column in expected.columns if column != geometry_column
            ]
            if not supplied[attributes].equals(expected[attributes]):
                raise PlanningZoningError(
                    f"{label} values or row order differ from reconstruction"
                )
            if (
                supplied.geometry.to_wkb().tolist()
                != expected.geometry.to_wkb().tolist()
            ):
                raise PlanningZoningError(
                    f"{label} geometry or row order differs from reconstruction"
                )
        elif not supplied.equals(expected):
            raise PlanningZoningError(
                f"{label} values or row order differ from reconstruction"
            )
    except PlanningZoningError:
        raise
    except Exception as error:
        raise PlanningZoningError(
            f"{label} cannot be compared safely with its reconstruction"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `validate_normalized_planning_zoning_inputs`

**Purpose:** Prove normalized zoning facts against a freshly read physical GPU layer.

**Exact signature**

```python
def validate_normalized_planning_zoning_inputs(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    zones: gpd.GeoDataFrame,
    zoning_intersections: pd.DataFrame,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `zones` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `zoning_intersections` | positional-or-keyword | `pd.DataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `PlanningZoningError(<br>                "planning_document must be exactly a GpuPlanningDocument"<br>            )` under lexical guard `type(planning_document) is not GpuPlanningDocument`.
  - `PlanningZoningError("Zoning parcels must be a GeoDataFrame")` under lexical guard `not isinstance(parcels, gpd.GeoDataFrame)`.
  - `PlanningZoningError("Normalized zones must be a GeoDataFrame")` under lexical guard `not isinstance(zones, gpd.GeoDataFrame)`.
  - `PlanningZoningError(<br>                "Zoning intersections must be a non-geospatial DataFrame"<br>            )` under lexical guard `not isinstance(zoning_intersections, pd.DataFrame) or isinstance(<br>            zoning_intersections, gpd.GeoDataFrame<br>        )`.
  - `PlanningZoningError(<br>                "Required parcel zoning summary columns are missing: "<br>                f"{missing_summary_columns}"<br>            )` under lexical guard `missing_summary_columns`.
  - `PlanningZoningError(<br>                "Physical GPU zoning validation returned an invalid layer"<br>            )` under lexical guard `len(validated_sources) != 1 or (<br>            validated_sources[0].logical_name != "zoning"<br>        )`.
  - `PlanningZoningError(<br>                "Parcel zoning index differs from spatial reconstruction"<br>            )` under lexical guard `not parcels.index.equals(expected.parcels.index)`.
  - `PlanningZoningError(<br>                    f"Parcel zoning summary differs from reconstruction: {column}"<br>                )` under lexical guard `str(supplied.dtype) != str(rebuilt.dtype) or not supplied.equals(<br>                rebuilt<br>            )`.
  - `re-raise`.
  - `PlanningZoningError(<br>            "Physical GPU zoning source failed revalidation"<br>        )`.
  - `PlanningZoningError(<br>            "Normalized planning zoning inputs cannot be validated safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.enrich_planning_zoning import (
    ParcelZoningResult,
    PlanningZoningError,
    intersect_parcels_with_gpu_zoning,
    validate_normalized_planning_zoning_inputs,
)`
- import: `landscout.stages.interpret_bess_zoning::<module>` via `from landscout.stages.enrich_planning_zoning import (
    PlanningZoningError,
    validate_normalized_planning_zoning_inputs,
)`
- direct call: `landscout.stages.interpret_bess_zoning::validate_bess_zoning_precheck` via `validate_normalized_planning_zoning_inputs`
- value/type reference: `landscout.stages.interpret_bess_zoning::validate_bess_zoning_precheck` via `validate_normalized_planning_zoning_inputs`
- direct call: `landscout.stages.interpret_bess_zoning::interpret_bess_zoning` via `validate_normalized_planning_zoning_inputs`
- value/type reference: `landscout.stages.interpret_bess_zoning::interpret_bess_zoning` via `validate_normalized_planning_zoning_inputs`
- import: `tests.unit.test_enrich_planning_zoning::<module>` via `from landscout.stages.enrich_planning_zoning import (
    PARCEL_ZONING_OUTPUT_COLUMNS,
    ParcelZoningResult,
    PlanningZoningError,
    _stabilize_area_relationships,
    intersect_parcels_with_gpu_zoning,
    validate_normalized_planning_zoning_inputs,
)`
- direct call: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_accepts_physical_fixture` via `validate_normalized_planning_zoning_inputs`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_accepts_physical_fixture` via `validate_normalized_planning_zoning_inputs`
- direct call: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_requires_every_parcel_summary_column` via `validate_normalized_planning_zoning_inputs`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_requires_every_parcel_summary_column` via `validate_normalized_planning_zoning_inputs`
- direct call: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_all_missing_parcel_summaries` via `validate_normalized_planning_zoning_inputs`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_all_missing_parcel_summaries` via `validate_normalized_planning_zoning_inputs`
- direct call: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_coordinated_mutations` via `validate_normalized_planning_zoning_inputs`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_coordinated_mutations` via `validate_normalized_planning_zoning_inputs`
- direct call: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_physical_tamper` via `validate_normalized_planning_zoning_inputs`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_physical_tamper` via `validate_normalized_planning_zoning_inputs`
- direct call: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_revalidates_physical_source_once` via `validate_normalized_planning_zoning_inputs`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_revalidates_physical_source_once` via `validate_normalized_planning_zoning_inputs`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningZoningError` | `landscout.stages.enrich_planning_zoning.PlanningZoningError` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `PARCEL_ZONING_OUTPUT_COLUMNS.difference` | `unresolved local/third-party receiver; no ownership inferred` |
| `revalidate_gpu_spatial_layer_sources` | `landscout.sources.gpu_fr.revalidate_gpu_spatial_layer_sources` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.drop(columns=list(summary_columns)).copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `intersect_parcels_with_gpu_zoning` | `landscout.stages.enrich_planning_zoning.intersect_parcels_with_gpu_zoning` |
| `_compare_exact_frame` | `landscout.stages.enrich_planning_zoning._compare_exact_frame` |
| `parcels.index.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `supplied.equals` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `parcels.drop(columns=list(summary_columns))` |
| Direct parameter mutation | `parcels.drop(columns=list(summary_columns))` |

**Complete source-ordered implementation**

```python
def validate_normalized_planning_zoning_inputs(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    zones: gpd.GeoDataFrame,
    zoning_intersections: pd.DataFrame,
) -> None:
    """Prove normalized zoning facts against a freshly read physical GPU layer."""

    try:
        if type(planning_document) is not GpuPlanningDocument:
            raise PlanningZoningError(
                "planning_document must be exactly a GpuPlanningDocument"
            )
        if not isinstance(parcels, gpd.GeoDataFrame):
            raise PlanningZoningError("Zoning parcels must be a GeoDataFrame")
        if not isinstance(zones, gpd.GeoDataFrame):
            raise PlanningZoningError("Normalized zones must be a GeoDataFrame")
        if not isinstance(zoning_intersections, pd.DataFrame) or isinstance(
            zoning_intersections, gpd.GeoDataFrame
        ):
            raise PlanningZoningError(
                "Zoning intersections must be a non-geospatial DataFrame"
            )
        missing_summary_columns = sorted(
            PARCEL_ZONING_OUTPUT_COLUMNS.difference(parcels.columns)
        )
        if missing_summary_columns:
            raise PlanningZoningError(
                "Required parcel zoning summary columns are missing: "
                f"{missing_summary_columns}"
            )
        validated_sources = revalidate_gpu_spatial_layer_sources(
            planning_document,
            (planning_document.zoning,),
        )
        if len(validated_sources) != 1 or (
            validated_sources[0].logical_name != "zoning"
        ):
            raise PlanningZoningError(
                "Physical GPU zoning validation returned an invalid layer"
            )
        fresh_zoning = replace(
            planning_document.zoning,
            data=validated_sources[0].data,
        )
        fresh_document = replace(planning_document, zoning=fresh_zoning)
        summary_columns = tuple(
            column
            for column in parcels.columns
            if column in PARCEL_ZONING_OUTPUT_COLUMNS
        )
        source_parcels = parcels.drop(columns=list(summary_columns)).copy()
        expected = intersect_parcels_with_gpu_zoning(
            source_parcels,
            fresh_document,
        )
        _compare_exact_frame(zones, expected.zones, "Normalized zoning catalog")
        _compare_exact_frame(
            zoning_intersections,
            expected.intersections,
            "Parcel/zoning intersections",
        )
        if not parcels.index.equals(expected.parcels.index):
            raise PlanningZoningError(
                "Parcel zoning index differs from spatial reconstruction"
            )
        for column in summary_columns:
            supplied = parcels[column]
            rebuilt = expected.parcels[column]
            if str(supplied.dtype) != str(rebuilt.dtype) or not supplied.equals(
                rebuilt
            ):
                raise PlanningZoningError(
                    f"Parcel zoning summary differs from reconstruction: {column}"
                )
    except PlanningZoningError:
        raise
    except GpuSpatialInspectionError as error:
        raise PlanningZoningError(
            "Physical GPU zoning source failed revalidation"
        ) from error
    except Exception as error:
        raise PlanningZoningError(
            "Normalized planning zoning inputs cannot be validated safely"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `intersect_parcels_with_gpu_zoning`

**Purpose:** Return factual parcel/zoning intersections without policy interpretation.

    Parcel storage geometry and CRS are preserved.  Zoning normalization,
    overlay, area, and union calculations use planar XY geometry in EPSG:2154.

**Exact signature**

```python
def intersect_parcels_with_gpu_zoning(
    parcels: gpd.GeoDataFrame,
    planning_document: GpuPlanningDocument,
) -> ParcelZoningResult:
```

- Exact decorators: none.
- Declared return annotation: `ParcelZoningResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.enrich_planning_zoning import (
    ParcelZoningResult,
    PlanningZoningError,
    intersect_parcels_with_gpu_zoning,
    validate_normalized_planning_zoning_inputs,
)`
- direct call: `landscout.stages.enrich_planning_zoning::validate_normalized_planning_zoning_inputs` via `intersect_parcels_with_gpu_zoning`
- value/type reference: `landscout.stages.enrich_planning_zoning::validate_normalized_planning_zoning_inputs` via `intersect_parcels_with_gpu_zoning`
- import: `tests.integration.test_gpu_planning_end_to_end::<module>` via `from landscout.stages.enrich_planning_zoning import (
    ParcelZoningResult,
    intersect_parcels_with_gpu_zoning,
)`
- direct call: `tests.integration.test_gpu_planning_end_to_end::_build_physical_chain` via `intersect_parcels_with_gpu_zoning`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_build_physical_chain` via `intersect_parcels_with_gpu_zoning`
- import: `tests.unit.test_enrich_planning_zoning::<module>` via `from landscout.stages.enrich_planning_zoning import (
    PARCEL_ZONING_OUTPUT_COLUMNS,
    ParcelZoningResult,
    PlanningZoningError,
    _stabilize_area_relationships,
    intersect_parcels_with_gpu_zoning,
    validate_normalized_planning_zoning_inputs,
)`
- direct call: `tests.unit.test_enrich_planning_zoning::_run` via `intersect_parcels_with_gpu_zoning`
- value/type reference: `tests.unit.test_enrich_planning_zoning::_run` via `intersect_parcels_with_gpu_zoning`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_clean_high_level_api_is_exported` via `intersect_parcels_with_gpu_zoning`
- direct call: `tests.unit.test_enrich_planning_zoning::test_zoning_summary_lineage_and_count_must_match_bundle` via `intersect_parcels_with_gpu_zoning`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_zoning_summary_lineage_and_count_must_match_bundle` via `intersect_parcels_with_gpu_zoning`
- direct call: `tests.unit.test_enrich_planning_zoning::test_input_frames_are_not_mutated` via `intersect_parcels_with_gpu_zoning`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_input_frames_are_not_mutated` via `intersect_parcels_with_gpu_zoning`
- direct call: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_accepts_physical_fixture` via `intersect_parcels_with_gpu_zoning`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_accepts_physical_fixture` via `intersect_parcels_with_gpu_zoning`
- direct call: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_requires_every_parcel_summary_column` via `intersect_parcels_with_gpu_zoning`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_requires_every_parcel_summary_column` via `intersect_parcels_with_gpu_zoning`
- direct call: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_all_missing_parcel_summaries` via `intersect_parcels_with_gpu_zoning`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_all_missing_parcel_summaries` via `intersect_parcels_with_gpu_zoning`
- direct call: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_coordinated_mutations` via `intersect_parcels_with_gpu_zoning`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_coordinated_mutations` via `intersect_parcels_with_gpu_zoning`
- direct call: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_physical_tamper` via `intersect_parcels_with_gpu_zoning`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_rejects_physical_tamper` via `intersect_parcels_with_gpu_zoning`
- direct call: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_revalidates_physical_source_once` via `intersect_parcels_with_gpu_zoning`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_source_complete_zoning_validation_revalidates_physical_source_once` via `intersect_parcels_with_gpu_zoning`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_parcels` | `landscout.stages.enrich_planning_zoning._validate_parcels` |
| `_validate_planning_document` | `landscout.stages.enrich_planning_zoning._validate_planning_document` |
| `_normalize_zones` | `landscout.stages.enrich_planning_zoning._normalize_zones` |
| `_metric_parcels` | `landscout.stages.enrich_planning_zoning._metric_parcels` |
| `_candidate_intersections` | `landscout.stages.enrich_planning_zoning._candidate_intersections` |
| `_parcel_summary` | `landscout.stages.enrich_planning_zoning._parcel_summary` |
| `_empty_intersections` | `landscout.stages.enrich_planning_zoning._empty_intersections` |
| `work.loc[:, INTERSECTION_COLUMNS].reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `ParcelZoningResult` | `landscout.stages.enrich_planning_zoning.ParcelZoningResult` |
| `_validate_result` | `landscout.stages.enrich_planning_zoning._validate_result` |

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
def intersect_parcels_with_gpu_zoning(
    parcels: gpd.GeoDataFrame,
    planning_document: GpuPlanningDocument,
) -> ParcelZoningResult:
    """Return factual parcel/zoning intersections without policy interpretation.

    Parcel storage geometry and CRS are preserved.  Zoning normalization,
    overlay, area, and union calculations use planar XY geometry in EPSG:2154.
    """

    _validate_parcels(parcels)
    context, source_zones = _validate_planning_document(planning_document)
    zones = _normalize_zones(source_zones, context)
    metric_parcels = _metric_parcels(parcels)
    work = _candidate_intersections(metric_parcels, zones)
    parcel_output = _parcel_summary(parcels, metric_parcels, zones, work, context)
    intersections = (
        _empty_intersections()
        if work.empty
        else work.loc[:, INTERSECTION_COLUMNS].reset_index(drop=True)
    )
    result = ParcelZoningResult(
        parcels=parcel_output,
        zones=zones,
        intersections=intersections,
    )
    _validate_result(parcels, result)
    return result
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.


## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: `GPU_ZONING_SOURCE_FIELDS`, `GPU_ZONING_REQUIRED_COLUMNS`, `PARCEL_REQUIRED_COLUMNS`, `PARCEL_ZONING_OUTPUT_COLUMNS`, `INTERSECTION_COLUMNS`, `_INTERSECTION_FLOAT_COLUMNS`.
- Exact value/null/index/CRS/geometry/hash behavior is claimed only where the reproduced validators and operations enforce it.

## 8. Public exports and package ownership

Exact `__all__` members and local origins:

| Export | Local origin binding |
|---|---|
| `ParcelZoningResult` | `landscout.stages.enrich_planning_zoning.ParcelZoningResult` |
| `PlanningZoningError` | `landscout.stages.enrich_planning_zoning.PlanningZoningError` |
| `intersect_parcels_with_gpu_zoning` | `landscout.stages.enrich_planning_zoning.intersect_parcels_with_gpu_zoning` |
| `validate_normalized_planning_zoning_inputs` | `landscout.stages.enrich_planning_zoning.validate_normalized_planning_zoning_inputs` |

## 9. Trust, provenance, side effects, and business boundary

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
"""Normalize official GPU zoning and intersect it with LandScout parcels.

This module records source zoning facts only.  It deliberately contains no
urban-planning interpretation, BESS compatibility policy, rejection, or score.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from math import isfinite
from numbers import Real

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
from pyproj import CRS
from shapely import (  # type: ignore[import-untyped]
    area as shapely_area,
)
from shapely import (
    force_2d,
    union_all,
)
from shapely import (
    intersection as shapely_intersection,
)

from landscout.common.frame_integrity import deterministic_frame_schema_signature
from landscout.sources.gpu_fr import (
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    revalidate_gpu_spatial_layer_sources,
)
from landscout.stages.planning_overlay import technical_overlay_tolerance

__all__ = [
    "ParcelZoningResult",
    "PlanningZoningError",
    "intersect_parcels_with_gpu_zoning",
    "validate_normalized_planning_zoning_inputs",
]

CALCULATION_CRS = "EPSG:2154"

# Centralized CNIG/GPU source schema for the zoning layer currently supported by
# this factual normalization stage.  Raw values are copied without rewriting.
GPU_ZONING_SOURCE_FIELDS = {
    "source_zone_id": "LIB_IDZONE",
    "zone_label_raw": "LIBELLE",
    "zone_long_label_raw": "LIBELONG",
    "zone_type_raw": "TYPEZONE",
    "regulation_filename_raw": "NOMFIC",
    "regulation_url_raw": "URLFIC",
    "source_document_reference_raw": "IDURBA",
    "source_validity_date_raw": "DATVALID",
}
GPU_ZONING_REQUIRED_COLUMNS = frozenset(
    {*GPU_ZONING_SOURCE_FIELDS.values(), "geometry"}
)
PARCEL_REQUIRED_COLUMNS = frozenset({"parcel_id", "geometry"})
POLYGON_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})
RELATION_TYPES = frozenset({"AREA_OVERLAP", "TOUCH_ONLY"})

PARCEL_ZONING_OUTPUT_COLUMNS = frozenset(
    {
        "zoning_area_match_count",
        "zoning_touch_only_count",
        "zoning_intersection_area_sum_m2",
        "zoning_covered_union_area_m2",
        "zoning_coverage_pct",
        "zoning_gap_area_m2",
        "zoning_overlap_excess_area_m2",
        "dominant_planning_zone_id",
        "dominant_source_zone_id",
        "dominant_zone_type_raw",
        "dominant_zone_label_raw",
        "dominant_zone_long_label_raw",
        "dominant_zone_intersection_area_m2",
        "dominant_zone_share_pct",
        "dominant_zone_tie_count",
        "planning_document_id",
        "planning_document_type",
        "planning_archive_name",
        "planning_archive_sha256",
        "planning_source_layer",
        "planning_standard_model",
    }
)

INTERSECTION_COLUMNS = (
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

_INTERSECTION_FLOAT_COLUMNS = frozenset(
    {
        "parcel_metric_area_m2",
        "zone_area_m2",
        "intersection_area_m2",
        "parcel_share_pct",
        "zone_share_pct",
    }
)


class PlanningZoningError(ValueError):
    """Raised when factual zoning normalization cannot be completed safely."""


@dataclass(frozen=True)
class ParcelZoningResult:
    """Normalized zones, parcel facts, and long-form parcel/zone relations."""

    parcels: gpd.GeoDataFrame
    zones: gpd.GeoDataFrame
    intersections: pd.DataFrame


@dataclass(frozen=True)
class _PlanningContext:
    provider: str
    portal: str
    commune_code: str
    document_id: str
    document_type: str
    archive_name: str
    archive_sha256: str
    source_layer: str
    standard_model: str | None
    source_crs: str


def _strict_nonempty_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise PlanningZoningError(f"{label} must be a non-empty exact string")
    return value


def _validate_exact_string_ids(
    values: pd.Series,
    label: str,
    *,
    require_unique: bool,
) -> None:
    if values.isna().any():
        raise PlanningZoningError(f"{label} values must not be null")
    for value in values.tolist():
        _strict_nonempty_string(value, label)
    if require_unique and values.duplicated().any():
        raise PlanningZoningError(f"{label} values must be unique")


def _readable_crs(value: object, label: str) -> CRS:
    if value is None:
        raise PlanningZoningError(f"{label} CRS is required")
    try:
        return CRS.from_user_input(value)
    except Exception as error:
        raise PlanningZoningError(f"{label} CRS is unreadable") from error


def _active_geometry(frame: gpd.GeoDataFrame, label: str) -> None:
    if "geometry" not in frame.columns:
        raise PlanningZoningError(f"{label} geometry column is required")
    try:
        active_name = frame.active_geometry_name
    except AttributeError as error:
        raise PlanningZoningError(f"{label} geometry column must be active") from error
    if active_name != "geometry":
        raise PlanningZoningError(f"{label} geometry column must be active")


def _validate_polygon_geometries(frame: gpd.GeoDataFrame, label: str) -> None:
    geometry = frame.geometry
    if geometry.isna().any():
        raise PlanningZoningError(f"{label} geometry must not be null")
    if geometry.is_empty.any():
        raise PlanningZoningError(f"{label} geometry must not be empty")
    if not geometry.is_valid.all():
        raise PlanningZoningError(f"{label} geometry must be valid")
    unexpected = sorted(set(geometry.geom_type) - POLYGON_GEOMETRY_TYPES)
    if unexpected:
        raise PlanningZoningError(
            f"{label} geometry must be Polygon or MultiPolygon; found: "
            + ", ".join(unexpected)
        )


def _validate_parcels(parcels: gpd.GeoDataFrame) -> CRS:
    if not isinstance(parcels, gpd.GeoDataFrame):
        raise PlanningZoningError("Parcels must be a GeoDataFrame")
    missing = sorted(PARCEL_REQUIRED_COLUMNS - set(parcels.columns))
    if missing:
        raise PlanningZoningError(
            "Parcels are missing required columns: " + ", ".join(missing)
        )
    collisions = sorted(PARCEL_ZONING_OUTPUT_COLUMNS & set(parcels.columns))
    if collisions:
        raise PlanningZoningError(
            "Parcels already contain zoning output columns: " + ", ".join(collisions)
        )
    _active_geometry(parcels, "Parcel")
    crs = _readable_crs(parcels.crs, "Parcel")
    _validate_exact_string_ids(parcels["parcel_id"], "parcel_id", require_unique=True)
    _validate_polygon_geometries(parcels, "Parcel")
    return crs


def _standard_model(planning_document: GpuPlanningDocument) -> str | None:
    document_value = planning_document.extraction.archive.document.standard_model
    values: list[str] = []
    if document_value is not None:
        values.append(_strict_nonempty_string(document_value, "GPU standard model"))
    for value in planning_document.extraction.standard_models:
        validated = _strict_nonempty_string(value, "GPU extracted standard model")
        if validated not in values:
            values.append(validated)
    if not values:
        return None
    if len(values) != 1:
        raise PlanningZoningError("GPU standard-model lineage is ambiguous")
    return values[0]


def _validate_planning_document(
    planning_document: GpuPlanningDocument,
) -> tuple[_PlanningContext, gpd.GeoDataFrame]:
    if not isinstance(planning_document, GpuPlanningDocument):
        raise PlanningZoningError("planning_document must be a GpuPlanningDocument")

    archive = planning_document.extraction.archive
    document = archive.document
    provider = _strict_nonempty_string(document.provider, "GPU provider")
    portal = _strict_nonempty_string(document.portal, "GPU portal")
    commune_code = _strict_nonempty_string(document.commune_code, "GPU commune code")
    document_id = _strict_nonempty_string(document.document_id, "GPU document ID")
    document_type = _strict_nonempty_string(document.document_type, "GPU document type")
    archive_name = _strict_nonempty_string(document.archive_name, "GPU archive name")
    archive_sha256 = _strict_nonempty_string(archive.sha256, "GPU archive SHA256")
    if len(archive_sha256) != 64 or any(
        character not in "0123456789abcdefABCDEF" for character in archive_sha256
    ):
        raise PlanningZoningError(
            "GPU archive SHA256 must contain 64 hexadecimal chars"
        )

    zoning = planning_document.zoning
    if zoning.logical_name != "zoning":
        raise PlanningZoningError("GPU planning bundle must contain its zoning layer")
    source_layer = _strict_nonempty_string(
        zoning.reference.source_layer, "GPU zoning source layer"
    )
    source = zoning.data
    if not isinstance(source, gpd.GeoDataFrame):
        raise PlanningZoningError("GPU zoning data must be a GeoDataFrame")
    missing = sorted(GPU_ZONING_REQUIRED_COLUMNS - set(source.columns))
    if missing:
        raise PlanningZoningError(
            "GPU zoning is missing required source columns: " + ", ".join(missing)
        )
    _active_geometry(source, "GPU zoning")
    source_crs = _readable_crs(source.crs, "GPU zoning")
    _validate_polygon_geometries(source, "GPU zoning")
    if source.empty:
        raise PlanningZoningError("GPU zoning must contain at least one source zone")

    source_zone_column = GPU_ZONING_SOURCE_FIELDS["source_zone_id"]
    _validate_exact_string_ids(
        source[source_zone_column], source_zone_column, require_unique=True
    )
    source_document_column = GPU_ZONING_SOURCE_FIELDS["source_document_reference_raw"]
    _validate_exact_string_ids(
        source[source_document_column], source_document_column, require_unique=False
    )
    expected_document_reference = (
        archive_name[:-4] if archive_name.casefold().endswith(".zip") else archive_name
    )
    if not source[source_document_column].eq(expected_document_reference).all():
        raise PlanningZoningError(
            "GPU zoning IDURBA does not match the loaded planning archive identity"
        )

    summary = zoning.summary
    if summary.source_document_id != document_id:
        raise PlanningZoningError("GPU zoning summary document lineage is inconsistent")
    if summary.source_archive_sha256 != archive_sha256:
        raise PlanningZoningError("GPU zoning summary archive lineage is inconsistent")
    if summary.source_layer != source_layer:
        raise PlanningZoningError("GPU zoning summary source layer is inconsistent")
    if summary.feature_count != len(source):
        raise PlanningZoningError("GPU zoning summary feature count is inconsistent")

    context = _PlanningContext(
        provider=provider,
        portal=portal,
        commune_code=commune_code,
        document_id=document_id,
        document_type=document_type,
        archive_name=archive_name,
        archive_sha256=archive_sha256,
        source_layer=source_layer,
        standard_model=_standard_model(planning_document),
        source_crs=source_crs.to_string(),
    )
    return context, source


def _project_geometries(
    frame: gpd.GeoDataFrame,
    label: str,
) -> gpd.GeoSeries:
    source_crs = _readable_crs(frame.crs, label)
    target_crs = CRS.from_epsg(2154)
    try:
        if source_crs.equals(target_crs):
            projected = frame.geometry.copy()
        else:
            projected = frame.geometry.to_crs(target_crs)
        projected = gpd.GeoSeries(
            force_2d(projected.array), index=frame.index, crs=CALCULATION_CRS
        )
    except Exception as error:
        raise PlanningZoningError(
            f"{label} CRS cannot be transformed safely to {CALCULATION_CRS}"
        ) from error
    return projected


def _normalize_zones(
    source: gpd.GeoDataFrame,
    context: _PlanningContext,
) -> gpd.GeoDataFrame:
    projected_geometry = _project_geometries(source, "GPU zoning")
    source_zone_ids = source[GPU_ZONING_SOURCE_FIELDS["source_zone_id"]].copy()
    planning_zone_ids = source_zone_ids.map(
        lambda value: f"GPU:{context.document_id}:ZONE:{value}"
    )
    if planning_zone_ids.duplicated().any():
        raise PlanningZoningError("Normalized planning_zone_id values must be unique")

    data: dict[str, object] = {
        "planning_zone_id": planning_zone_ids.to_numpy(copy=True),
        "source_zone_id": source_zone_ids.to_numpy(copy=True),
    }
    for normalized_name, source_name in GPU_ZONING_SOURCE_FIELDS.items():
        if normalized_name == "source_zone_id":
            continue
        data[normalized_name] = source[source_name].to_numpy(copy=True)
    count = len(source)
    data.update(
        {
            "source_provider": np.repeat(context.provider, count),
            "source_portal": np.repeat(context.portal, count),
            "source_commune_code": np.repeat(context.commune_code, count),
            "source_document_id": np.repeat(context.document_id, count),
            "source_document_type": np.repeat(context.document_type, count),
            "source_archive_name": np.repeat(context.archive_name, count),
            "source_archive_sha256": np.repeat(context.archive_sha256, count),
            "source_layer": np.repeat(context.source_layer, count),
            "source_standard_model": np.full(
                count, context.standard_model, dtype="object"
            ),
            "source_crs": np.repeat(context.source_crs, count),
        }
    )
    zones = gpd.GeoDataFrame(
        data,
        geometry=projected_geometry.to_numpy(copy=True),
        crs=CALCULATION_CRS,
    )
    zone_areas = zones.geometry.area.to_numpy(dtype="float64", copy=True)
    if not np.isfinite(zone_areas).all() or (zone_areas <= 0).any():
        raise PlanningZoningError("GPU zone areas must be finite and positive")
    zones["zone_area_m2"] = zone_areas
    zones = zones.reset_index(drop=True)
    zones = zones.set_crs(CALCULATION_CRS, allow_override=True)
    return zones


def _metric_parcels(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    geometry = _project_geometries(parcels, "Parcel")
    metric = gpd.GeoDataFrame(
        {
            "_parcel_position": np.arange(len(parcels), dtype="int64"),
            "parcel_id": parcels["parcel_id"].to_numpy(copy=True),
        },
        geometry=geometry.to_numpy(copy=True),
        crs=CALCULATION_CRS,
    )
    areas = metric.geometry.area.to_numpy(dtype="float64", copy=True)
    if not np.isfinite(areas).all() or (areas <= 0).any():
        raise PlanningZoningError("Parcel metric areas must be finite and positive")
    metric["_parcel_area_m2"] = areas
    return metric


def _empty_intersections() -> pd.DataFrame:
    return pd.DataFrame(
        {
            column: pd.Series(
                dtype="float64" if column in _INTERSECTION_FLOAT_COLUMNS else "object"
            )
            for column in INTERSECTION_COLUMNS
        }
    )


def _candidate_intersections(
    metric_parcels: gpd.GeoDataFrame,
    zones: gpd.GeoDataFrame,
) -> pd.DataFrame:
    parcel_candidates = gpd.GeoDataFrame(
        metric_parcels[["_parcel_position", "parcel_id"]].copy(),
        geometry=metric_parcels.geometry.to_numpy(copy=True),
        crs=CALCULATION_CRS,
    )
    zone_candidates = gpd.GeoDataFrame(
        {"_zone_position": np.arange(len(zones), dtype="int64")},
        geometry=zones.geometry.to_numpy(copy=True),
        crs=CALCULATION_CRS,
    )
    try:
        candidates = gpd.sjoin(
            parcel_candidates,
            zone_candidates,
            how="inner",
            predicate="intersects",
        )
    except Exception as error:
        raise PlanningZoningError("GPU zoning spatial-index query failed") from error
    if candidates.empty:
        return pd.DataFrame(
            columns=("_parcel_position", "_zone_position", "_intersection_geometry")
        )

    parcel_positions = candidates["_parcel_position"].to_numpy(dtype="int64", copy=True)
    zone_positions = candidates["_zone_position"].to_numpy(dtype="int64", copy=True)
    try:
        intersection_geometry = shapely_intersection(
            metric_parcels.geometry.iloc[parcel_positions].array,
            zones.geometry.iloc[zone_positions].array,
        )
        intersection_areas = np.asarray(
            shapely_area(intersection_geometry), dtype="float64"
        )
    except Exception as error:
        raise PlanningZoningError("GPU zoning geometry overlay failed") from error
    if not np.isfinite(intersection_areas).all() or (intersection_areas < 0).any():
        raise PlanningZoningError("Intersection areas must be finite and non-negative")

    parcel_areas = metric_parcels["_parcel_area_m2"].to_numpy(dtype="float64")[
        parcel_positions
    ]
    zone_areas = zones["zone_area_m2"].to_numpy(dtype="float64")[zone_positions]
    relation_types = np.where(intersection_areas > 0, "AREA_OVERLAP", "TOUCH_ONLY")
    selected_zones = zones.iloc[zone_positions]
    geometry_values = np.empty(len(intersection_geometry), dtype="object")
    geometry_values[:] = intersection_geometry

    work = pd.DataFrame(
        {
            "_parcel_position": parcel_positions,
            "_zone_position": zone_positions,
            "_intersection_geometry": geometry_values,
            "parcel_id": metric_parcels["parcel_id"].to_numpy(copy=False)[
                parcel_positions
            ],
            "planning_zone_id": selected_zones["planning_zone_id"].to_numpy(copy=True),
            "source_zone_id": selected_zones["source_zone_id"].to_numpy(copy=True),
            "zone_type_raw": selected_zones["zone_type_raw"].to_numpy(copy=True),
            "zone_label_raw": selected_zones["zone_label_raw"].to_numpy(copy=True),
            "zone_long_label_raw": selected_zones["zone_long_label_raw"].to_numpy(
                copy=True
            ),
            "relation_type": relation_types,
            "parcel_metric_area_m2": parcel_areas,
            "zone_area_m2": zone_areas,
            "intersection_area_m2": intersection_areas,
            "parcel_share_pct": 100.0 * intersection_areas / parcel_areas,
            "zone_share_pct": 100.0 * intersection_areas / zone_areas,
            "source_document_id": selected_zones["source_document_id"].to_numpy(
                copy=True
            ),
            "source_archive_sha256": selected_zones["source_archive_sha256"].to_numpy(
                copy=True
            ),
            "source_layer": selected_zones["source_layer"].to_numpy(copy=True),
            "source_validity_date_raw": selected_zones[
                "source_validity_date_raw"
            ].to_numpy(copy=True),
            "regulation_filename_raw": selected_zones[
                "regulation_filename_raw"
            ].to_numpy(copy=True),
        }
    )
    work = work.sort_values(
        ["_parcel_position", "planning_zone_id"], kind="stable"
    ).reset_index(drop=True)
    return work


def _technical_area_tolerance(parcel_area_m2: float) -> float:
    return technical_overlay_tolerance(parcel_area_m2)


def _stabilize_area_relationships(
    parcel_area: float,
    raw_sum: float,
    covered_union: float,
) -> tuple[float, float, float]:
    tolerance = _technical_area_tolerance(parcel_area)
    if covered_union > parcel_area:
        if covered_union - parcel_area > tolerance:
            raise PlanningZoningError(
                "Zoning covered-union area materially exceeds parcel area"
            )
        covered_union = parcel_area
    if covered_union > raw_sum:
        if covered_union - raw_sum > tolerance:
            raise PlanningZoningError(
                "Zoning covered-union area materially exceeds raw intersection sum"
            )
        covered_union = raw_sum
    gap = parcel_area - covered_union
    overlap_excess = raw_sum - covered_union
    if gap < 0 or overlap_excess < 0:
        raise PlanningZoningError("Zoning area differences must not be negative")
    return covered_union, gap, overlap_excess


def _parcel_summary(
    parcels: gpd.GeoDataFrame,
    metric_parcels: gpd.GeoDataFrame,
    zones: gpd.GeoDataFrame,
    work: pd.DataFrame,
    context: _PlanningContext,
) -> gpd.GeoDataFrame:
    count = len(parcels)
    parcel_areas = metric_parcels["_parcel_area_m2"].to_numpy(
        dtype="float64", copy=True
    )
    area_match_count = np.zeros(count, dtype="int64")
    touch_count = np.zeros(count, dtype="int64")
    raw_sum = np.zeros(count, dtype="float64")
    covered_union = np.zeros(count, dtype="float64")
    gap = parcel_areas.copy()
    overlap_excess = np.zeros(count, dtype="float64")

    dominant_planning = np.full(count, None, dtype="object")
    dominant_source = np.full(count, None, dtype="object")
    dominant_type = np.full(count, None, dtype="object")
    dominant_label = np.full(count, None, dtype="object")
    dominant_long_label = np.full(count, None, dtype="object")
    dominant_area = np.full(count, np.nan, dtype="float64")
    dominant_share = np.full(count, np.nan, dtype="float64")
    dominant_ties = pd.array([pd.NA] * count, dtype="Int64")

    if not work.empty:
        touches = work.loc[work["relation_type"] == "TOUCH_ONLY"]
        for position, group in touches.groupby("_parcel_position", sort=False):
            touch_count[int(position)] = len(group)

        positive = work.loc[work["relation_type"] == "AREA_OVERLAP"]
        for position_value, group in positive.groupby("_parcel_position", sort=False):
            position = int(position_value)
            areas = group["intersection_area_m2"].to_numpy(dtype="float64")
            area_match_count[position] = len(group)
            raw_area = float(areas.sum())
            raw_sum[position] = raw_area
            try:
                union_area = float(
                    shapely_area(union_all(group["_intersection_geometry"].to_numpy()))
                )
            except Exception as error:
                raise PlanningZoningError(
                    "GPU zoning covered-union calculation failed"
                ) from error
            if not isfinite(union_area) or union_area < 0:
                raise PlanningZoningError(
                    "GPU zoning covered-union area must be finite and non-negative"
                )
            union_area, parcel_gap, excess = _stabilize_area_relationships(
                float(parcel_areas[position]), raw_area, union_area
            )
            covered_union[position] = union_area
            gap[position] = parcel_gap
            overlap_excess[position] = excess

            maximum = float(areas.max())
            tied = group.loc[group["intersection_area_m2"] == maximum]
            selected = tied.sort_values("planning_zone_id", kind="stable").iloc[0]
            dominant_planning[position] = selected["planning_zone_id"]
            dominant_source[position] = selected["source_zone_id"]
            dominant_type[position] = selected["zone_type_raw"]
            dominant_label[position] = selected["zone_label_raw"]
            dominant_long_label[position] = selected["zone_long_label_raw"]
            dominant_area[position] = maximum
            dominant_share[position] = 100.0 * maximum / parcel_areas[position]
            dominant_ties[position] = len(tied)

    output = parcels.copy(deep=True)
    output["zoning_area_match_count"] = area_match_count
    output["zoning_touch_only_count"] = touch_count
    output["zoning_intersection_area_sum_m2"] = raw_sum
    output["zoning_covered_union_area_m2"] = covered_union
    output["zoning_coverage_pct"] = np.where(
        gap == 0.0,
        100.0,
        100.0 * covered_union / parcel_areas,
    )
    output["zoning_gap_area_m2"] = gap
    output["zoning_overlap_excess_area_m2"] = overlap_excess
    output["dominant_planning_zone_id"] = dominant_planning
    output["dominant_source_zone_id"] = dominant_source
    output["dominant_zone_type_raw"] = dominant_type
    output["dominant_zone_label_raw"] = dominant_label
    output["dominant_zone_long_label_raw"] = dominant_long_label
    output["dominant_zone_intersection_area_m2"] = dominant_area
    output["dominant_zone_share_pct"] = dominant_share
    output["dominant_zone_tie_count"] = dominant_ties
    output["planning_document_id"] = context.document_id
    output["planning_document_type"] = context.document_type
    output["planning_archive_name"] = context.archive_name
    output["planning_archive_sha256"] = context.archive_sha256
    output["planning_source_layer"] = context.source_layer
    output["planning_standard_model"] = context.standard_model
    return output


def _validate_numeric_columns(
    frame: pd.DataFrame,
    columns: tuple[str, ...] | frozenset[str],
    label: str,
    *,
    allow_null: bool,
) -> None:
    for column in columns:
        if column not in frame.columns:
            raise PlanningZoningError(f"{label} is missing numeric column: {column}")
        for value in frame[column].tolist():
            if pd.isna(value):
                if allow_null:
                    continue
                raise PlanningZoningError(f"{label} {column} must not be null")
            if isinstance(value, bool) or not isinstance(value, Real):
                raise PlanningZoningError(f"{label} {column} must be numeric")
            try:
                numeric = float(value)
            except (TypeError, ValueError, OverflowError) as error:
                raise PlanningZoningError(f"{label} {column} must be finite") from error
            if not isfinite(numeric) or numeric < 0:
                raise PlanningZoningError(
                    f"{label} {column} must be finite and non-negative"
                )


def _validate_result(
    input_parcels: gpd.GeoDataFrame,
    result: ParcelZoningResult,
) -> None:
    output = result.parcels
    if len(output) != len(input_parcels):
        raise PlanningZoningError("Parcel zoning output count changed")
    if output["parcel_id"].tolist() != input_parcels["parcel_id"].tolist():
        raise PlanningZoningError("Parcel zoning output IDs or order changed")
    if not output.index.equals(input_parcels.index):
        raise PlanningZoningError("Parcel zoning output index changed")
    if output.crs != input_parcels.crs:
        raise PlanningZoningError("Parcel zoning output CRS changed")
    if not np.array_equal(output.geometry.to_wkb(), input_parcels.geometry.to_wkb()):
        raise PlanningZoningError("Parcel zoning output geometry changed")

    if not CRS.from_user_input(result.zones.crs).equals(CRS.from_epsg(2154)):
        raise PlanningZoningError("Normalized zones must use EPSG:2154")
    _validate_exact_string_ids(
        result.zones["planning_zone_id"],
        "planning_zone_id",
        require_unique=True,
    )
    _validate_numeric_columns(
        result.zones, ("zone_area_m2",), "Normalized zone", allow_null=False
    )

    intersections = result.intersections
    missing = sorted(set(INTERSECTION_COLUMNS) - set(intersections.columns))
    if missing:
        raise PlanningZoningError(
            "Intersection table is missing columns: " + ", ".join(missing)
        )
    if intersections.duplicated(["parcel_id", "planning_zone_id"]).any():
        raise PlanningZoningError("Parcel/zone intersection pairs must be unique")
    if not set(intersections["parcel_id"]).issubset(set(output["parcel_id"])):
        raise PlanningZoningError("Intersection table contains an unknown parcel ID")
    if not set(intersections["planning_zone_id"]).issubset(
        set(result.zones["planning_zone_id"])
    ):
        raise PlanningZoningError("Intersection table contains an unknown zone ID")
    if not set(intersections["relation_type"]).issubset(RELATION_TYPES):
        raise PlanningZoningError("Intersection table has an unknown relation type")
    _validate_numeric_columns(
        intersections,
        _INTERSECTION_FLOAT_COLUMNS,
        "Intersection table",
        allow_null=False,
    )

    required_summary = (
        "zoning_area_match_count",
        "zoning_touch_only_count",
        "zoning_intersection_area_sum_m2",
        "zoning_covered_union_area_m2",
        "zoning_coverage_pct",
        "zoning_gap_area_m2",
        "zoning_overlap_excess_area_m2",
    )
    _validate_numeric_columns(
        output, required_summary, "Parcel zoning", allow_null=False
    )
    coverage = output["zoning_coverage_pct"].to_numpy(dtype="float64")
    if (coverage > 100.0).any():
        raise PlanningZoningError("Parcel zoning coverage must not exceed 100 percent")


def _compare_exact_frame(
    supplied: pd.DataFrame,
    expected: pd.DataFrame,
    label: str,
) -> None:
    try:
        if type(supplied) is not type(expected):
            raise PlanningZoningError(f"{label} frame type differs from reconstruction")
        if deterministic_frame_schema_signature(
            supplied
        ) != deterministic_frame_schema_signature(expected):
            raise PlanningZoningError(f"{label} schema differs from reconstruction")
        if isinstance(expected, gpd.GeoDataFrame):
            geometry_column = expected.geometry.name
            attributes = [
                column for column in expected.columns if column != geometry_column
            ]
            if not supplied[attributes].equals(expected[attributes]):
                raise PlanningZoningError(
                    f"{label} values or row order differ from reconstruction"
                )
            if (
                supplied.geometry.to_wkb().tolist()
                != expected.geometry.to_wkb().tolist()
            ):
                raise PlanningZoningError(
                    f"{label} geometry or row order differs from reconstruction"
                )
        elif not supplied.equals(expected):
            raise PlanningZoningError(
                f"{label} values or row order differ from reconstruction"
            )
    except PlanningZoningError:
        raise
    except Exception as error:
        raise PlanningZoningError(
            f"{label} cannot be compared safely with its reconstruction"
        ) from error


def validate_normalized_planning_zoning_inputs(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    zones: gpd.GeoDataFrame,
    zoning_intersections: pd.DataFrame,
) -> None:
    """Prove normalized zoning facts against a freshly read physical GPU layer."""

    try:
        if type(planning_document) is not GpuPlanningDocument:
            raise PlanningZoningError(
                "planning_document must be exactly a GpuPlanningDocument"
            )
        if not isinstance(parcels, gpd.GeoDataFrame):
            raise PlanningZoningError("Zoning parcels must be a GeoDataFrame")
        if not isinstance(zones, gpd.GeoDataFrame):
            raise PlanningZoningError("Normalized zones must be a GeoDataFrame")
        if not isinstance(zoning_intersections, pd.DataFrame) or isinstance(
            zoning_intersections, gpd.GeoDataFrame
        ):
            raise PlanningZoningError(
                "Zoning intersections must be a non-geospatial DataFrame"
            )
        missing_summary_columns = sorted(
            PARCEL_ZONING_OUTPUT_COLUMNS.difference(parcels.columns)
        )
        if missing_summary_columns:
            raise PlanningZoningError(
                "Required parcel zoning summary columns are missing: "
                f"{missing_summary_columns}"
            )
        validated_sources = revalidate_gpu_spatial_layer_sources(
            planning_document,
            (planning_document.zoning,),
        )
        if len(validated_sources) != 1 or (
            validated_sources[0].logical_name != "zoning"
        ):
            raise PlanningZoningError(
                "Physical GPU zoning validation returned an invalid layer"
            )
        fresh_zoning = replace(
            planning_document.zoning,
            data=validated_sources[0].data,
        )
        fresh_document = replace(planning_document, zoning=fresh_zoning)
        summary_columns = tuple(
            column
            for column in parcels.columns
            if column in PARCEL_ZONING_OUTPUT_COLUMNS
        )
        source_parcels = parcels.drop(columns=list(summary_columns)).copy()
        expected = intersect_parcels_with_gpu_zoning(
            source_parcels,
            fresh_document,
        )
        _compare_exact_frame(zones, expected.zones, "Normalized zoning catalog")
        _compare_exact_frame(
            zoning_intersections,
            expected.intersections,
            "Parcel/zoning intersections",
        )
        if not parcels.index.equals(expected.parcels.index):
            raise PlanningZoningError(
                "Parcel zoning index differs from spatial reconstruction"
            )
        for column in summary_columns:
            supplied = parcels[column]
            rebuilt = expected.parcels[column]
            if str(supplied.dtype) != str(rebuilt.dtype) or not supplied.equals(
                rebuilt
            ):
                raise PlanningZoningError(
                    f"Parcel zoning summary differs from reconstruction: {column}"
                )
    except PlanningZoningError:
        raise
    except GpuSpatialInspectionError as error:
        raise PlanningZoningError(
            "Physical GPU zoning source failed revalidation"
        ) from error
    except Exception as error:
        raise PlanningZoningError(
            "Normalized planning zoning inputs cannot be validated safely"
        ) from error


def intersect_parcels_with_gpu_zoning(
    parcels: gpd.GeoDataFrame,
    planning_document: GpuPlanningDocument,
) -> ParcelZoningResult:
    """Return factual parcel/zoning intersections without policy interpretation.

    Parcel storage geometry and CRS are preserved.  Zoning normalization,
    overlay, area, and union calculations use planar XY geometry in EPSG:2154.
    """

    _validate_parcels(parcels)
    context, source_zones = _validate_planning_document(planning_document)
    zones = _normalize_zones(source_zones, context)
    metric_parcels = _metric_parcels(parcels)
    work = _candidate_intersections(metric_parcels, zones)
    parcel_output = _parcel_summary(parcels, metric_parcels, zones, work, context)
    intersections = (
        _empty_intersections()
        if work.empty
        else work.loc[:, INTERSECTION_COLUMNS].reset_index(drop=True)
    )
    result = ParcelZoningResult(
        parcels=parcel_output,
        zones=zones,
        intersections=intersections,
    )
    _validate_result(parcels, result)
    return result
```

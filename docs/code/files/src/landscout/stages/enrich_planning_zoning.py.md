# `src/landscout/stages/enrich_planning_zoning.py`

## File identity

- Repository path: `src/landscout/stages/enrich_planning_zoning.py`
- File type: Python source
- Layer: processing/policy stage
- Domain: planning
- Responsibility: Intersects parcels with source-completely verified GPU zoning polygons and retains factual overlap evidence.
- Source SHA256: `1838ea77ee7872ce8b663ecb19ffb82455abc7f4c947a847f041828808f22bf9`

## 1. Purpose

Intersects parcels with source-completely verified GPU zoning polygons and retains factual overlap evidence.

## 2. Position in LandScout architecture

This file belongs to the **processing/policy stage** layer and the **planning** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

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

### A. Python constants

#### `CALCULATION_CRS`

```python
CALCULATION_CRS = "EPSG:2154"
```

Coordinate-reference-system identity used for an explicit storage, validation, or calculation boundary. Consumers include `src/landscout/stages/assess_grid_coverage.py::_assess_grid_coverage_from_proximity` (value argument/reference), `src/landscout/stages/enrich_grid_proximity.py::_enrich_parcel_grid_proximity_from_normalized` (value argument/reference), `src/landscout/stages/enrich_planning_features.py::_normalize_layer` (value argument/reference), `src/landscout/stages/enrich_planning_features.py::_empty_catalog` (value argument/reference), `src/landscout/stages/enrich_planning_features.py::_empty_catalog` (value argument/reference), `src/landscout/stages/enrich_planning_features.py::_combine_catalogs` (value argument/reference), `src/landscout/stages/enrich_planning_features.py::_metric_parcels` (value argument/reference), `src/landscout/stages/enrich_planning_features.py::_relation_base` (value argument/reference), `src/landscout/stages/enrich_planning_zoning.py::_project_geometries` (value argument/reference), `src/landscout/stages/enrich_planning_zoning.py::_normalize_zones` (value argument/reference), `src/landscout/stages/enrich_planning_zoning.py::_normalize_zones` (value argument/reference), `src/landscout/stages/enrich_planning_zoning.py::_metric_parcels` (value argument/reference), `src/landscout/stages/enrich_planning_zoning.py::_candidate_intersections` (value argument/reference), `src/landscout/stages/enrich_planning_zoning.py::_candidate_intersections` (value argument/reference).

#### `GPU_ZONING_SOURCE_FIELDS`

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

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section.

#### `GPU_ZONING_REQUIRED_COLUMNS`

```python
GPU_ZONING_REQUIRED_COLUMNS = frozenset(
    {*GPU_ZONING_SOURCE_FIELDS.values(), "geometry"}
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section.

#### `PARCEL_REQUIRED_COLUMNS`

```python
PARCEL_REQUIRED_COLUMNS = frozenset({"parcel_id", "geometry"})
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section.

#### `POLYGON_GEOMETRY_TYPES`

```python
POLYGON_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema.

#### `RELATION_TYPES`

```python
RELATION_TYPES = frozenset({"AREA_OVERLAP", "TOUCH_ONLY"})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/enrich_planning_zoning.py::_validate_result` (value argument/reference).

#### `PARCEL_ZONING_OUTPUT_COLUMNS`

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

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section.

#### `INTERSECTION_COLUMNS`

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

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/enrich_planning_zoning.py::_validate_result` (value argument/reference).

#### `_INTERSECTION_FLOAT_COLUMNS`

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

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/enrich_planning_zoning.py::_validate_result` (value argument/reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

- `__all__` — explicit public export allow-list.
```python
__all__ = [
    "intersect_parcels_with_gpu_zoning",
    "validate_normalized_planning_zoning_inputs",
]
```


### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `PlanningZoningError`

**Purpose:** Raised when factual zoning normalization cannot be completed safely.

**Kind:** controlled exception.

**Inheritance:** `ValueError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_strict_nonempty_string` via `PlanningZoningError`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_validate_exact_string_ids` via `PlanningZoningError`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_readable_crs` via `PlanningZoningError`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_active_geometry` via `PlanningZoningError`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_validate_polygon_geometries` via `PlanningZoningError`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_validate_parcels` via `PlanningZoningError`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_standard_model` via `PlanningZoningError`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_validate_planning_document` via `PlanningZoningError`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_project_geometries` via `PlanningZoningError`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_normalize_zones` via `PlanningZoningError`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_metric_parcels` via `PlanningZoningError`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_candidate_intersections` via `PlanningZoningError`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_stabilize_area_relationships` via `PlanningZoningError`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_parcel_summary` via `PlanningZoningError`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_validate_numeric_columns` via `PlanningZoningError`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_validate_result` via `PlanningZoningError`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_compare_exact_frame` via `PlanningZoningError`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::validate_normalized_planning_zoning_inputs` via `PlanningZoningError`.
- import/re-export: `src/landscout/stages/interpret_bess_zoning.py::<module>` via `from landscout.stages.enrich_planning_zoning import (
    PlanningZoningError,
    validate_normalized_planning_zoning_inputs,
)`.
- callback/function object: `tests/unit/test_enrich_planning_zoning.py::test_shared_overlay_tolerance_preserves_zoning_numerical_behavior` via `pytest.raises(PlanningZoningError, match='materially exceeds')`.
- callback/function object: `tests/unit/test_enrich_planning_zoning.py::test_missing_or_unusable_crs_is_rejected` via `pytest.raises(PlanningZoningError, match=message)`.
- callback/function object: `tests/unit/test_enrich_planning_zoning.py::test_invalid_or_non_polygonal_parcel_geometry_is_rejected` via `pytest.raises(PlanningZoningError, match='geometry|Polygon')`.
- callback/function object: `tests/unit/test_enrich_planning_zoning.py::test_invalid_or_non_polygonal_zone_geometry_is_rejected` via `pytest.raises(PlanningZoningError, match='geometry|Polygon')`.
- callback/function object: `tests/unit/test_enrich_planning_zoning.py::test_invalid_parcel_id_is_rejected` via `pytest.raises(PlanningZoningError, match='parcel_id')`.
- callback/function object: `tests/unit/test_enrich_planning_zoning.py::test_duplicate_parcel_id_is_rejected` via `pytest.raises(PlanningZoningError, match='parcel_id.*unique|duplicate')`.
- callback/function object: `tests/unit/test_enrich_planning_zoning.py::test_missing_parcel_id_is_rejected` via `pytest.raises(PlanningZoningError, match='parcel_id')`.
- callback/function object: `tests/unit/test_enrich_planning_zoning.py::test_geometry_must_be_the_active_parcel_geometry_column` via `pytest.raises(PlanningZoningError, match='active')`.
- callback/function object: `tests/unit/test_enrich_planning_zoning.py::test_invalid_source_zone_id_is_rejected` via `pytest.raises(PlanningZoningError, match='LIB_IDZONE|zone')`.
- callback/function object: `tests/unit/test_enrich_planning_zoning.py::test_duplicate_source_zone_id_is_rejected` via `pytest.raises(PlanningZoningError, match='LIB_IDZONE.*unique|duplicate')`.
- callback/function object: `tests/unit/test_enrich_planning_zoning.py::test_zoning_document_reference_must_match_loaded_archive` via `pytest.raises(PlanningZoningError, match='IDURBA|document')`.
- callback/function object: `tests/unit/test_enrich_planning_zoning.py::test_zoning_summary_lineage_and_count_must_match_bundle` via `pytest.raises(PlanningZoningError, match=message)`.
- callback/function object: `tests/unit/test_enrich_planning_zoning.py::test_existing_parcel_output_field_collision_is_rejected` via `pytest.raises(PlanningZoningError, match='column|output|reserved|collision')`.
- callback/function object: `tests/unit/test_enrich_planning_zoning.py::test_every_source_zoning_field_is_required` via `pytest.raises(PlanningZoningError, match=field)`.
- callback/function object: `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_rejects_coordinated_mutations` via `pytest.raises(PlanningZoningError, match='source|reconstruction|differs')`.
- callback/function object: `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_rejects_physical_tamper` via `pytest.raises(PlanningZoningError, match='Physical|source')`.
- import/re-export: `tests/unit/test_enrich_planning_zoning.py::<module>` via `from landscout.stages.enrich_planning_zoning import (
    ParcelZoningResult,
    PlanningZoningError,
    _stabilize_area_relationships,
    intersect_parcels_with_gpu_zoning,
    validate_normalized_planning_zoning_inputs,
)`.
- direct call or construction: `tests/unit/test_interpret_bess_zoning.py::test_invalid_physical_zoning_fails_before_policy_interpretation.invalid_source` via `interpret_module.PlanningZoningError`.
- property/attribute access: `tests/unit/test_interpret_bess_zoning.py::test_invalid_physical_zoning_fails_before_policy_interpretation.invalid_source` via `interpret_module.PlanningZoningError`.

**Exact class source**

```python
class PlanningZoningError(ValueError):
    """Raised when factual zoning normalization cannot be completed safely."""
```

### `ParcelZoningResult`

**Purpose:** Normalized zones, parcel facts, and long-form parcel/zone relations.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `parcels` | `parcels: gpd.GeoDataFrame` | Pandas/GeoPandas result frame named by this field; its exact ordered schema, dtype, CRS/index, and preservation contract is documented by the owning result validator and schema declarations. |
| `zones` | `zones: gpd.GeoDataFrame` | Stores `ParcelZoningResult`'s `zones` value under exact annotation `gpd.GeoDataFrame`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `intersections` | `intersections: pd.DataFrame` | Stores `ParcelZoningResult`'s `intersections` value under exact annotation `pd.DataFrame`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

**Interface consumers**

- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::intersect_parcels_with_gpu_zoning` via `ParcelZoningResult`.
- callback/function object: `tests/unit/test_enrich_planning_zoning.py::test_one_parcel_fully_inside_one_zone` via `isinstance(result, ParcelZoningResult)`.
- import/re-export: `tests/unit/test_enrich_planning_zoning.py::<module>` via `from landscout.stages.enrich_planning_zoning import (
    ParcelZoningResult,
    PlanningZoningError,
    _stabilize_area_relationships,
    intersect_parcels_with_gpu_zoning,
    validate_normalized_planning_zoning_inputs,
)`.

**Exact class source**

```python
class ParcelZoningResult:
    """Normalized zones, parcel facts, and long-form parcel/zone relations."""

    parcels: gpd.GeoDataFrame
    zones: gpd.GeoDataFrame
    intersections: pd.DataFrame
```

### `_PlanningContext`

**Purpose:** Immutable result/value envelope carrying `provider`, `portal`, `commune_code`, `document_id`, `document_type`, `archive_name`, `archive_sha256`, `source_layer`, `standard_model`, `source_crs`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `provider` | `provider: str` | Stores `_PlanningContext`'s `provider` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `portal` | `portal: str` | Stores `_PlanningContext`'s `portal` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `commune_code` | `commune_code: str` | Stores `_PlanningContext`'s `commune code` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `document_id` | `document_id: str` | Exact identity for the entity named by the field; uniqueness, portability, and lineage meaning are only those explicitly validated by the owner. |
| `document_type` | `document_type: str` | Closed or validated `document type` classification on `_PlanningContext`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `archive_name` | `archive_name: str` | Stores `_PlanningContext`'s `archive name` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `archive_sha256` | `archive_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `source_layer` | `source_layer: str` | Exact source-lineage scalar named by the field; it is compared with configuration/result/row lineage but is not physical proof without source-byte revalidation. |
| `standard_model` | `standard_model: str \| None` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |
| `source_crs` | `source_crs: str` | Coordinate reference system identity; exact accepted/storage/calculation behavior is enforced by the owning CRS validator. |

**Interface consumers**

- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_planning_context` via `_PlanningContext`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_validate_planning_document` via `_PlanningContext`.

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


## 6. Functions and methods

### `_strict_nonempty_string`

**Exact signature**

```python
def _strict_nonempty_string(value: object, label: str) -> str:
```

**Purpose**

Private `planning` helper for strict nonempty string; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(value, str) or not value or value != value.strip()`.
- Explicit raise expressions: `PlanningZoningError(f'{label} must be a non-empty exact string')`.

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

- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_validate_exact_string_ids` via `_strict_nonempty_string`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_standard_model` via `_strict_nonempty_string`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_validate_planning_document` via `_strict_nonempty_string`.

**Complete source-ordered implementation**

```python
def _strict_nonempty_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise PlanningZoningError(f"{label} must be a non-empty exact string")
    return value
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_exact_string_ids`

**Exact signature**

```python
def _validate_exact_string_ids(
    values: pd.Series,
    label: str,
    *,
    require_unique: bool,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent exact string ids; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `values.isna().any()`.
- Guard with a raise path: `require_unique and values.duplicated().any()`.
- Explicit raise expressions: `PlanningZoningError(f'{label} values must be unique')`, `PlanningZoningError(f'{label} values must not be null')`.

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

- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_validate_parcels` via `_validate_exact_string_ids`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_validate_planning_document` via `_validate_exact_string_ids`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_validate_result` via `_validate_exact_string_ids`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_readable_crs`

**Exact signature**

```python
def _readable_crs(value: object, label: str) -> CRS:
```

**Purpose**

Private `planning` helper for readable crs; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `CRS`.
- Every observed return expression is reproduced without truncation:
```python
CRS.from_user_input(value)
```

**Validation and exceptions**

- Guard with a raise path: `value is None`.
- Explicit raise expressions: `PlanningZoningError(f'{label} CRS is required')`, `PlanningZoningError(f'{label} CRS is unreadable')`.

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

- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_validate_parcels` via `_readable_crs`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_validate_planning_document` via `_readable_crs`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_project_geometries` via `_readable_crs`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_active_geometry`

**Exact signature**

```python
def _active_geometry(frame: gpd.GeoDataFrame, label: str) -> None:
```

**Purpose**

Private `planning` helper for active geometry; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `'geometry' not in frame.columns`.
- Guard with a raise path: `active_name != 'geometry'`.
- Explicit raise expressions: `PlanningZoningError(f'{label} geometry column is required')`, `PlanningZoningError(f'{label} geometry column must be active')`.

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

- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_validate_parcels` via `_active_geometry`.
- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_normalize_layer` via `_active_geometry`.
- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_validate_catalog_contract` via `_active_geometry`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_validate_parcels` via `_active_geometry`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_validate_planning_document` via `_active_geometry`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_polygon_geometries`

**Exact signature**

```python
def _validate_polygon_geometries(frame: gpd.GeoDataFrame, label: str) -> None:
```

**Purpose**

Rejects malformed or inconsistent polygon geometries; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `geometry.isna().any()`.
- Guard with a raise path: `geometry.is_empty.any()`.
- Guard with a raise path: `not geometry.is_valid.all()`.
- Guard with a raise path: `unexpected`.
- Explicit raise expressions: `PlanningZoningError(f'{label} geometry must be Polygon or MultiPolygon; found: ' + ', '.join(unexpected))`, `PlanningZoningError(f'{label} geometry must be valid')`, `PlanningZoningError(f'{label} geometry must not be empty')`, `PlanningZoningError(f'{label} geometry must not be null')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `geometry.is_empty.any`, `geometry.is_valid.all`, `geometry.isna`, `geometry.isna().any`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_validate_parcels` via `_validate_polygon_geometries`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_validate_planning_document` via `_validate_polygon_geometries`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_parcels`

**Exact signature**

```python
def _validate_parcels(parcels: gpd.GeoDataFrame) -> CRS:
```

**Purpose**

Rejects malformed or inconsistent parcels; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `CRS`.
- Every observed return expression is reproduced without truncation:
```python
crs
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(parcels, gpd.GeoDataFrame)`.
- Guard with a raise path: `missing`.
- Guard with a raise path: `collisions`.
- Explicit raise expressions: `PlanningZoningError('Parcels already contain zoning output columns: ' + ', '.join(collisions))`, `PlanningZoningError('Parcels are missing required columns: ' + ', '.join(missing))`, `PlanningZoningError('Parcels must be a GeoDataFrame')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `_active_geometry`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/enrich_grid_proximity.py::_validate_result_contract` via `_validate_parcels`.
- direct call or construction: `src/landscout/stages/enrich_grid_proximity.py::_enrich_parcel_grid_proximity_from_normalized` via `_validate_parcels`.
- direct call or construction: `src/landscout/stages/enrich_grid_proximity.py::enrich_parcel_grid_proximity` via `_validate_parcels`.
- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` via `_validate_parcels`.
- direct call or construction: `src/landscout/stages/enrich_planning_features.py::intersect_parcels_with_gpu_planning_features` via `_validate_parcels`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::intersect_parcels_with_gpu_zoning` via `_validate_parcels`.
- direct call or construction: `src/landscout/stages/enrich_road_proximity.py::_enrich_parcel_road_proximity` via `_validate_parcels`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_build_result` via `_validate_parcels`.

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
            "Parcels already contain zoning output columns: "
            + ", ".join(collisions)
        )
    _active_geometry(parcels, "Parcel")
    crs = _readable_crs(parcels.crs, "Parcel")
    _validate_exact_string_ids(
        parcels["parcel_id"], "parcel_id", require_unique=True
    )
    _validate_polygon_geometries(parcels, "Parcel")
    return crs
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_standard_model`

**Exact signature**

```python
def _standard_model(planning_document: GpuPlanningDocument) -> str | None:
```

**Purpose**

Private `planning` helper for standard model; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str | None`.
- Every observed return expression is reproduced without truncation:
```python
values[0]

None
```

**Validation and exceptions**

- Guard with a raise path: `len(values) != 1`.
- Explicit raise expressions: `PlanningZoningError('GPU standard-model lineage is ambiguous')`.

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

- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_planning_context` via `_standard_model`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_validate_planning_document` via `_standard_model`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_planning_document`

**Exact signature**

```python
def _validate_planning_document(
    planning_document: GpuPlanningDocument,
) -> tuple[_PlanningContext, gpd.GeoDataFrame]:
```

**Purpose**

Rejects malformed or inconsistent planning document; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[_PlanningContext, gpd.GeoDataFrame]`.
- Every observed return expression is reproduced without truncation:
```python
(context, source)
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(planning_document, GpuPlanningDocument)`.
- Guard with a raise path: `len(archive_sha256) != 64 or any((character not in '0123456789abcdefABCDEF' for character in archive_sha256))`.
- Guard with a raise path: `zoning.logical_name != 'zoning'`.
- Guard with a raise path: `not isinstance(source, gpd.GeoDataFrame)`.
- Guard with a raise path: `missing`.
- Guard with a raise path: `source.empty`.
- Guard with a raise path: `not source[source_document_column].eq(expected_document_reference).all()`.
- Guard with a raise path: `summary.source_document_id != document_id`.
- Guard with a raise path: `summary.source_archive_sha256 != archive_sha256`.
- Guard with a raise path: `summary.source_layer != source_layer`.
- Guard with a raise path: `summary.feature_count != len(source)`.
- Explicit raise expressions: `PlanningZoningError('GPU archive SHA256 must contain 64 hexadecimal chars')`, `PlanningZoningError('GPU planning bundle must contain its zoning layer')`, `PlanningZoningError('GPU zoning IDURBA does not match the loaded planning archive identity')`, `PlanningZoningError('GPU zoning data must be a GeoDataFrame')`, `PlanningZoningError('GPU zoning is missing required source columns: ' + ', '.join(missing))`, `PlanningZoningError('GPU zoning must contain at least one source zone')`, `PlanningZoningError('GPU zoning summary archive lineage is inconsistent')`, `PlanningZoningError('GPU zoning summary document lineage is inconsistent')`, `PlanningZoningError('GPU zoning summary feature count is inconsistent')`, `PlanningZoningError('GPU zoning summary source layer is inconsistent')`, `PlanningZoningError('planning_document must be a GpuPlanningDocument')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `_active_geometry`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::intersect_parcels_with_gpu_zoning` via `_validate_planning_document`.

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
    commune_code = _strict_nonempty_string(
        document.commune_code, "GPU commune code"
    )
    document_id = _strict_nonempty_string(document.document_id, "GPU document ID")
    document_type = _strict_nonempty_string(
        document.document_type, "GPU document type"
    )
    archive_name = _strict_nonempty_string(document.archive_name, "GPU archive name")
    archive_sha256 = _strict_nonempty_string(archive.sha256, "GPU archive SHA256")
    if len(archive_sha256) != 64 or any(
        character not in "0123456789abcdefABCDEF" for character in archive_sha256
    ):
        raise PlanningZoningError("GPU archive SHA256 must contain 64 hexadecimal chars")

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
    source_document_column = GPU_ZONING_SOURCE_FIELDS[
        "source_document_reference_raw"
    ]
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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_project_geometries`

**Exact signature**

```python
def _project_geometries(
    frame: gpd.GeoDataFrame,
    label: str,
) -> gpd.GeoSeries:
```

**Purpose**

Private `planning` helper for project geometries; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoSeries`.
- Every observed return expression is reproduced without truncation:
```python
projected
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `PlanningZoningError(f'{label} CRS cannot be transformed safely to {CALCULATION_CRS}')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `force_2d`, `frame.geometry.copy`, `frame.geometry.to_crs`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_normalize_zones` via `_project_geometries`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_metric_parcels` via `_project_geometries`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_normalize_zones`

**Exact signature**

```python
def _normalize_zones(
    source: gpd.GeoDataFrame,
    context: _PlanningContext,
) -> gpd.GeoDataFrame:
```

**Purpose**

Projects validated source facts into zones; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
zones
```

**Validation and exceptions**

- Guard with a raise path: `planning_zone_ids.duplicated().any()`.
- Guard with a raise path: `not np.isfinite(zone_areas).all() or (zone_areas <= 0).any()`.
- Explicit raise expressions: `PlanningZoningError('GPU zone areas must be finite and positive')`, `PlanningZoningError('Normalized planning_zone_id values must be unique')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `(zone_areas <= 0).any`, `np.isfinite(zone_areas).all`, `projected_geometry.to_numpy`, `zones.geometry.area.to_numpy`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `data[normalized_name]`, `zones['zone_area_m2']`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::intersect_parcels_with_gpu_zoning` via `_normalize_zones`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_metric_parcels`

**Exact signature**

```python
def _metric_parcels(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
```

**Purpose**

Private `planning` helper for metric parcels; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
metric
```

**Validation and exceptions**

- Guard with a raise path: `not np.isfinite(areas).all() or (areas <= 0).any()`.
- Explicit raise expressions: `PlanningZoningError('Parcel metric areas must be finite and positive')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `(areas <= 0).any`, `geometry.to_numpy`, `metric.geometry.area.to_numpy`, `np.isfinite(areas).all`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `metric['_parcel_area_m2']`.
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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_empty_intersections`

**Exact signature**

```python
def _empty_intersections() -> pd.DataFrame:
```

**Purpose**

Private `planning` helper for empty intersections; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
pd.DataFrame({column: pd.Series(dtype='float64' if column in _INTERSECTION_FLOAT_COLUMNS else 'object') for column in INTERSECTION_COLUMNS})
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

- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::intersect_parcels_with_gpu_zoning` via `_empty_intersections`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_candidate_intersections`

**Exact signature**

```python
def _candidate_intersections(
    metric_parcels: gpd.GeoDataFrame,
    zones: gpd.GeoDataFrame,
) -> pd.DataFrame:
```

**Purpose**

Private `planning` helper for candidate intersections; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
work

pd.DataFrame(columns=('_parcel_position', '_zone_position', '_intersection_geometry'))
```

**Validation and exceptions**

- Guard with a raise path: `not np.isfinite(intersection_areas).all() or (intersection_areas < 0).any()`.
- Explicit raise expressions: `PlanningZoningError('GPU zoning geometry overlay failed')`, `PlanningZoningError('GPU zoning spatial-index query failed')`, `PlanningZoningError('Intersection areas must be finite and non-negative')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `(intersection_areas < 0).any`, `metric_parcels.geometry.to_numpy`, `metric_parcels['_parcel_area_m2'].to_numpy`, `np.isfinite(intersection_areas).all`, `shapely_area`, `shapely_intersection`, `zones.geometry.to_numpy`, `zones['zone_area_m2'].to_numpy`.
- Hashing: `selected_zones['source_archive_sha256'].to_numpy`, `shapely_area`, `shapely_intersection`.
- Environment/process effects: none directly visible.
- In-memory mutation: `geometry_values[:]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::intersect_parcels_with_gpu_zoning` via `_candidate_intersections`.

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

    parcel_positions = candidates["_parcel_position"].to_numpy(
        dtype="int64", copy=True
    )
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
            "planning_zone_id": selected_zones["planning_zone_id"].to_numpy(
                copy=True
            ),
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
            "source_archive_sha256": selected_zones[
                "source_archive_sha256"
            ].to_numpy(copy=True),
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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_technical_area_tolerance`

**Exact signature**

```python
def _technical_area_tolerance(parcel_area_m2: float) -> float:
```

**Purpose**

Private `planning` helper for technical area tolerance; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `float`.
- Every observed return expression is reproduced without truncation:
```python
technical_overlay_tolerance(parcel_area_m2)
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

- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_stabilize_area_relationships` via `_technical_area_tolerance`.

**Complete source-ordered implementation**

```python
def _technical_area_tolerance(parcel_area_m2: float) -> float:
    return technical_overlay_tolerance(parcel_area_m2)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_stabilize_area_relationships`

**Exact signature**

```python
def _stabilize_area_relationships(
    parcel_area: float,
    raw_sum: float,
    covered_union: float,
) -> tuple[float, float, float]:
```

**Purpose**

Private `planning` helper for stabilize area relationships; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[float, float, float]`.
- Every observed return expression is reproduced without truncation:
```python
(covered_union, gap, overlap_excess)
```

**Validation and exceptions**

- Guard with a raise path: `covered_union > parcel_area`.
- Guard with a raise path: `covered_union > raw_sum`.
- Guard with a raise path: `gap < 0 or overlap_excess < 0`.
- Guard with a raise path: `covered_union - parcel_area > tolerance`.
- Guard with a raise path: `covered_union - raw_sum > tolerance`.
- Explicit raise expressions: `PlanningZoningError('Zoning area differences must not be negative')`, `PlanningZoningError('Zoning covered-union area materially exceeds parcel area')`, `PlanningZoningError('Zoning covered-union area materially exceeds raw intersection sum')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `_technical_area_tolerance`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_parcel_summary` via `_stabilize_area_relationships`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_shared_overlay_tolerance_preserves_zoning_numerical_behavior` via `_stabilize_area_relationships`.
- import/re-export: `tests/unit/test_enrich_planning_zoning.py::<module>` via `from landscout.stages.enrich_planning_zoning import (
    ParcelZoningResult,
    PlanningZoningError,
    _stabilize_area_relationships,
    intersect_parcels_with_gpu_zoning,
    validate_normalized_planning_zoning_inputs,
)`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_parcel_summary`

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

**Purpose**

Private `planning` helper for parcel summary; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
output
```

**Validation and exceptions**

- Guard with a raise path: `not work.empty`.
- Guard with a raise path: `not isfinite(union_area) or union_area < 0`.
- Explicit raise expressions: `PlanningZoningError('GPU zoning covered-union area must be finite and non-negative')`, `PlanningZoningError('GPU zoning covered-union calculation failed')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `_stabilize_area_relationships`, `areas.max`, `areas.sum`, `group['_intersection_geometry'].to_numpy`, `group['intersection_area_m2'].to_numpy`, `metric_parcels['_parcel_area_m2'].to_numpy`, `parcel_areas.copy`, `shapely_area`.
- Hashing: `shapely_area`.
- Environment/process effects: none directly visible.
- In-memory mutation: `area_match_count[position]`, `covered_union[position]`, `dominant_area[position]`, `dominant_label[position]`, `dominant_long_label[position]`, `dominant_planning[position]`, `dominant_share[position]`, `dominant_source[position]`, `dominant_ties[position]`, `dominant_type[position]`, `gap[position]`, `output['dominant_planning_zone_id']`, `output['dominant_source_zone_id']`, `output['dominant_zone_intersection_area_m2']`, `output['dominant_zone_label_raw']`, `output['dominant_zone_long_label_raw']`, `output['dominant_zone_share_pct']`, `output['dominant_zone_tie_count']`, `output['dominant_zone_type_raw']`, `output['planning_archive_name']`, `output['planning_archive_sha256']`, `output['planning_document_id']`, `output['planning_document_type']`, `output['planning_source_layer']`, `output['planning_standard_model']`, `output['zoning_area_match_count']`, `output['zoning_coverage_pct']`, `output['zoning_covered_union_area_m2']`, `output['zoning_gap_area_m2']`, `output['zoning_intersection_area_sum_m2']`, `output['zoning_overlap_excess_area_m2']`, `output['zoning_touch_only_count']`, `overlap_excess[position]`, `raw_sum[position]`, `touch_count[int(position)]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_aggregate_frames` via `_parcel_summary`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::intersect_parcels_with_gpu_zoning` via `_parcel_summary`.

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
                    shapely_area(
                        union_all(group["_intersection_geometry"].to_numpy())
                    )
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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_numeric_columns`

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

**Purpose**

Rejects malformed or inconsistent numeric columns; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `column not in frame.columns`.
- Guard with a raise path: `pd.isna(value)`.
- Guard with a raise path: `isinstance(value, bool) or not isinstance(value, Real)`.
- Guard with a raise path: `not isfinite(numeric) or numeric < 0`.
- Explicit raise expressions: `PlanningZoningError(f'{label} is missing numeric column: {column}')`, `PlanningZoningError(f'{label} {column} must be finite and non-negative')`, `PlanningZoningError(f'{label} {column} must be finite')`, `PlanningZoningError(f'{label} {column} must be numeric')`, `PlanningZoningError(f'{label} {column} must not be null')`.

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

- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_validate_result` via `_validate_numeric_columns`.

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
                raise PlanningZoningError(
                    f"{label} {column} must be finite"
                ) from error
            if not isfinite(numeric) or numeric < 0:
                raise PlanningZoningError(
                    f"{label} {column} must be finite and non-negative"
                )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_result`

**Exact signature**

```python
def _validate_result(
    input_parcels: gpd.GeoDataFrame,
    result: ParcelZoningResult,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent result; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `len(output) != len(input_parcels)`.
- Guard with a raise path: `output['parcel_id'].tolist() != input_parcels['parcel_id'].tolist()`.
- Guard with a raise path: `not output.index.equals(input_parcels.index)`.
- Guard with a raise path: `output.crs != input_parcels.crs`.
- Guard with a raise path: `not np.array_equal(output.geometry.to_wkb(), input_parcels.geometry.to_wkb())`.
- Guard with a raise path: `not CRS.from_user_input(result.zones.crs).equals(CRS.from_epsg(2154))`.
- Guard with a raise path: `missing`.
- Guard with a raise path: `intersections.duplicated(['parcel_id', 'planning_zone_id']).any()`.
- Guard with a raise path: `not set(intersections['parcel_id']).issubset(set(output['parcel_id']))`.
- Guard with a raise path: `not set(intersections['planning_zone_id']).issubset(set(result.zones['planning_zone_id']))`.
- Guard with a raise path: `not set(intersections['relation_type']).issubset(RELATION_TYPES)`.
- Guard with a raise path: `(coverage > 100.0).any()`.
- Explicit raise expressions: `PlanningZoningError('Intersection table contains an unknown parcel ID')`, `PlanningZoningError('Intersection table contains an unknown zone ID')`, `PlanningZoningError('Intersection table has an unknown relation type')`, `PlanningZoningError('Intersection table is missing columns: ' + ', '.join(missing))`, `PlanningZoningError('Normalized zones must use EPSG:2154')`, `PlanningZoningError('Parcel zoning coverage must not exceed 100 percent')`, `PlanningZoningError('Parcel zoning output CRS changed')`, `PlanningZoningError('Parcel zoning output IDs or order changed')`, `PlanningZoningError('Parcel zoning output count changed')`, `PlanningZoningError('Parcel zoning output geometry changed')`, `PlanningZoningError('Parcel zoning output index changed')`, `PlanningZoningError('Parcel/zone intersection pairs must be unique')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `input_parcels.geometry.to_wkb`, `intersections.duplicated`, `intersections.duplicated(['parcel_id', 'planning_zone_id']).any`, `output.geometry.to_wkb`, `set(intersections['parcel_id']).issubset`, `set(intersections['planning_zone_id']).issubset`, `set(intersections['relation_type']).issubset`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/enrich_planning_features.py::intersect_parcels_with_gpu_planning_features` via `_validate_result`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::intersect_parcels_with_gpu_zoning` via `_validate_result`.
- direct call or construction: `src/landscout/stages/enrich_road_proximity.py::_enrich_parcel_road_proximity` via `_validate_result`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_strict_relation_integer_counts_are_enforced` via `_validate_result`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_strict_parcel_summary_integer_counts_are_enforced` via `_validate_result`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_corrupted_relation_semantics_are_rejected` via `_validate_result`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_point_member_relation_semantics_are_exact` via `_validate_result`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_relation_must_match_feature_catalog` via `_validate_result`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_feature_ids_are_globally_unique_across_catalogs` via `_validate_result`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_corrupted_parcel_summary_is_rejected` via `_validate_result`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_corrupted_surface_union_contract_is_rejected` via `_validate_result`.
- import/re-export: `tests/unit/test_enrich_planning_features.py::<module>` via `from landscout.stages.enrich_planning_features import (
    ParcelPlanningFeaturesResult,
    PlanningFeatureInputValidation,
    PlanningFeaturesError,
    _validate_result,
    intersect_parcels_with_gpu_planning_features,
    validate_normalized_planning_feature_inputs,
)`.

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
    if not np.array_equal(
        output.geometry.to_wkb(), input_parcels.geometry.to_wkb()
    ):
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
    _validate_numeric_columns(output, required_summary, "Parcel zoning", allow_null=False)
    coverage = output["zoning_coverage_pct"].to_numpy(dtype="float64")
    if (coverage > 100.0).any():
        raise PlanningZoningError("Parcel zoning coverage must not exceed 100 percent")
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_compare_exact_frame`

**Exact signature**

```python
def _compare_exact_frame(
    supplied: pd.DataFrame,
    expected: pd.DataFrame,
    label: str,
) -> None:
```

**Purpose**

Private `planning` helper for compare exact frame; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `type(supplied) is not type(expected)`.
- Guard with a raise path: `deterministic_frame_schema_signature(supplied) != deterministic_frame_schema_signature(expected)`.
- Guard with a raise path: `isinstance(expected, gpd.GeoDataFrame)`.
- Guard with a raise path: `not supplied[attributes].equals(expected[attributes])`.
- Guard with a raise path: `supplied.geometry.to_wkb().tolist() != expected.geometry.to_wkb().tolist()`.
- Guard with a raise path: `not supplied.equals(expected)`.
- Explicit raise expressions: `PlanningZoningError(f'{label} cannot be compared safely with its reconstruction')`, `PlanningZoningError(f'{label} frame type differs from reconstruction')`, `PlanningZoningError(f'{label} geometry or row order differs from reconstruction')`, `PlanningZoningError(f'{label} schema differs from reconstruction')`, `PlanningZoningError(f'{label} values or row order differ from reconstruction')`, `re-raise`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `expected.geometry.to_wkb`, `expected.geometry.to_wkb().tolist`, `supplied.geometry.to_wkb`, `supplied.geometry.to_wkb().tolist`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::validate_normalized_planning_zoning_inputs` via `_compare_exact_frame`.

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
            if supplied.geometry.to_wkb().tolist() != expected.geometry.to_wkb().tolist():
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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_normalized_planning_zoning_inputs`

**Exact signature**

```python
def validate_normalized_planning_zoning_inputs(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    zones: gpd.GeoDataFrame,
    zoning_intersections: pd.DataFrame,
) -> None:
```

**Purpose**

Prove normalized zoning facts against a freshly read physical GPU layer.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `type(planning_document) is not GpuPlanningDocument`.
- Guard with a raise path: `not isinstance(parcels, gpd.GeoDataFrame)`.
- Guard with a raise path: `not isinstance(zones, gpd.GeoDataFrame)`.
- Guard with a raise path: `not isinstance(zoning_intersections, pd.DataFrame) or isinstance(zoning_intersections, gpd.GeoDataFrame)`.
- Guard with a raise path: `len(validated_sources) != 1 or validated_sources[0].logical_name != 'zoning'`.
- Guard with a raise path: `not parcels.index.equals(expected.parcels.index)`.
- Guard with a raise path: `str(supplied.dtype) != str(rebuilt.dtype) or not supplied.equals(rebuilt)`.
- Explicit raise expressions: `PlanningZoningError('Normalized planning zoning inputs cannot be validated safely')`, `PlanningZoningError('Normalized zones must be a GeoDataFrame')`, `PlanningZoningError('Parcel zoning index differs from spatial reconstruction')`, `PlanningZoningError('Physical GPU zoning source failed revalidation')`, `PlanningZoningError('Physical GPU zoning validation returned an invalid layer')`, `PlanningZoningError('Zoning intersections must be a non-geospatial DataFrame')`, `PlanningZoningError('Zoning parcels must be a GeoDataFrame')`, `PlanningZoningError('planning_document must be exactly a GpuPlanningDocument')`, `PlanningZoningError(f'Parcel zoning summary differs from reconstruction: {column}')`, `re-raise`.

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

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.enrich_planning_zoning import (
    intersect_parcels_with_gpu_zoning,
    validate_normalized_planning_zoning_inputs,
)`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::validate_bess_zoning_precheck` via `validate_normalized_planning_zoning_inputs`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::interpret_bess_zoning` via `validate_normalized_planning_zoning_inputs`.
- import/re-export: `src/landscout/stages/interpret_bess_zoning.py::<module>` via `from landscout.stages.enrich_planning_zoning import (
    PlanningZoningError,
    validate_normalized_planning_zoning_inputs,
)`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_accepts_physical_fixture` via `validate_normalized_planning_zoning_inputs`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_rejects_coordinated_mutations` via `validate_normalized_planning_zoning_inputs`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_rejects_physical_tamper` via `validate_normalized_planning_zoning_inputs`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_revalidates_physical_source_once` via `validate_normalized_planning_zoning_inputs`.
- import/re-export: `tests/unit/test_enrich_planning_zoning.py::<module>` via `from landscout.stages.enrich_planning_zoning import (
    ParcelZoningResult,
    PlanningZoningError,
    _stabilize_area_relationships,
    intersect_parcels_with_gpu_zoning,
    validate_normalized_planning_zoning_inputs,
)`.

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
        present_summary_columns = tuple(
            column for column in PARCEL_ZONING_OUTPUT_COLUMNS if column in parcels.columns
        )
        source_parcels = parcels.drop(columns=list(present_summary_columns)).copy()
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
        for column in present_summary_columns:
            supplied = parcels[column]
            rebuilt = expected.parcels[column]
            if str(supplied.dtype) != str(rebuilt.dtype) or not supplied.equals(rebuilt):
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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `intersect_parcels_with_gpu_zoning`

**Exact signature**

```python
def intersect_parcels_with_gpu_zoning(
    parcels: gpd.GeoDataFrame,
    planning_document: GpuPlanningDocument,
) -> ParcelZoningResult:
```

**Purpose**

Return factual parcel/zoning intersections without policy interpretation. Parcel storage geometry and CRS are preserved. Zoning normalization, overlay, area, and union calculations use planar XY geometry in EPSG:2154.

**Return contract**

- Declared return annotation: `ParcelZoningResult`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `_candidate_intersections`, `_empty_intersections`, `work.loc[:, INTERSECTION_COLUMNS].reset_index`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.enrich_planning_zoning import (
    intersect_parcels_with_gpu_zoning,
    validate_normalized_planning_zoning_inputs,
)`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::validate_normalized_planning_zoning_inputs` via `intersect_parcels_with_gpu_zoning`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::_run` via `intersect_parcels_with_gpu_zoning`.
- property/attribute access: `tests/unit/test_enrich_planning_zoning.py::test_clean_high_level_api_is_exported` via `stages.intersect_parcels_with_gpu_zoning`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_zoning_summary_lineage_and_count_must_match_bundle` via `intersect_parcels_with_gpu_zoning`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_input_frames_are_not_mutated` via `intersect_parcels_with_gpu_zoning`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_accepts_physical_fixture` via `intersect_parcels_with_gpu_zoning`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_rejects_coordinated_mutations` via `intersect_parcels_with_gpu_zoning`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_rejects_physical_tamper` via `intersect_parcels_with_gpu_zoning`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_revalidates_physical_source_once` via `intersect_parcels_with_gpu_zoning`.
- import/re-export: `tests/unit/test_enrich_planning_zoning.py::<module>` via `from landscout.stages.enrich_planning_zoning import (
    ParcelZoningResult,
    PlanningZoningError,
    _stabilize_area_relationships,
    intersect_parcels_with_gpu_zoning,
    validate_normalized_planning_zoning_inputs,
)`.

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
    parcel_output = _parcel_summary(
        parcels, metric_parcels, zones, work, context
    )
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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.


## 7. Data contracts

### `GPU_ZONING_SOURCE_FIELDS` — required input frame fields (unordered when stored as a set)

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

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `source_zone_id` | LIB_IDZONE | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 2 | `zone_label_raw` | LIBELLE | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 3 | `zone_long_label_raw` | LIBELONG | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 4 | `zone_type_raw` | TYPEZONE | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 5 | `regulation_filename_raw` | NOMFIC | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 6 | `regulation_url_raw` | URLFIC | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 7 | `source_document_reference_raw` | IDURBA | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 8 | `source_validity_date_raw` | DATVALID | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |

### `GPU_ZONING_REQUIRED_COLUMNS` — required input frame fields (unordered when stored as a set)

```python
GPU_ZONING_REQUIRED_COLUMNS = frozenset(
    {*GPU_ZONING_SOURCE_FIELDS.values(), "geometry"}
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `DATVALID` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 2 | `IDURBA` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `LIBELLE` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 4 | `LIBELONG` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 5 | `LIB_IDZONE` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `NOMFIC` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 7 | `TYPEZONE` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `URLFIC` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 9 | `geometry` | GeoPandas geometry dtype | nullable only where the owning geometry-status contract permits it | source/geometry fact | Active geometry; never an authorization or suitability result. |

### `PARCEL_REQUIRED_COLUMNS` — required input frame fields (unordered when stored as a set)

```python
PARCEL_REQUIRED_COLUMNS = frozenset({"parcel_id", "geometry"})
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `geometry` | GeoPandas geometry dtype | nullable only where the owning geometry-status contract permits it | source/geometry fact | Active geometry; never an authorization or suitability result. |
| 2 | `parcel_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |

### `PARCEL_ZONING_OUTPUT_COLUMNS` — canonical or derived frame-column schema

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

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `dominant_planning_zone_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 2 | `dominant_source_zone_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 3 | `dominant_zone_intersection_area_m2` | float64 when builder initializes NaN/numeric metric; otherwise exact source numeric dtype shown by implementation | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 4 | `dominant_zone_label_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 5 | `dominant_zone_long_label_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 6 | `dominant_zone_share_pct` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 7 | `dominant_zone_tie_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 8 | `dominant_zone_type_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 9 | `planning_archive_name` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 10 | `planning_archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 11 | `planning_document_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 12 | `planning_document_type` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 13 | `planning_source_layer` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 14 | `planning_standard_model` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 15 | `zoning_area_match_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 16 | `zoning_coverage_pct` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 17 | `zoning_covered_union_area_m2` | float64 when builder initializes NaN/numeric metric; otherwise exact source numeric dtype shown by implementation | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 18 | `zoning_gap_area_m2` | float64 when builder initializes NaN/numeric metric; otherwise exact source numeric dtype shown by implementation | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 19 | `zoning_intersection_area_sum_m2` | float64 when builder initializes NaN/numeric metric; otherwise exact source numeric dtype shown by implementation | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 20 | `zoning_overlap_excess_area_m2` | float64 when builder initializes NaN/numeric metric; otherwise exact source numeric dtype shown by implementation | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 21 | `zoning_touch_only_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |

### `INTERSECTION_COLUMNS` — canonical or derived frame-column schema

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

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `parcel_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 2 | `planning_zone_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 3 | `source_zone_id` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 4 | `zone_type_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 5 | `zone_label_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 6 | `zone_long_label_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 7 | `relation_type` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `parcel_metric_area_m2` | float64 when builder initializes NaN/numeric metric; otherwise exact source numeric dtype shown by implementation | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 9 | `zone_area_m2` | float64 when builder initializes NaN/numeric metric; otherwise exact source numeric dtype shown by implementation | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 10 | `intersection_area_m2` | float64 when builder initializes NaN/numeric metric; otherwise exact source numeric dtype shown by implementation | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 11 | `parcel_share_pct` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 12 | `zone_share_pct` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 13 | `source_document_id` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 14 | `source_archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 15 | `source_layer` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 16 | `source_validity_date_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 17 | `regulation_filename_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |

### `_INTERSECTION_FLOAT_COLUMNS` — canonical or derived frame-column schema

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

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `intersection_area_m2` | float64 when builder initializes NaN/numeric metric; otherwise exact source numeric dtype shown by implementation | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 2 | `parcel_metric_area_m2` | float64 when builder initializes NaN/numeric metric; otherwise exact source numeric dtype shown by implementation | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 3 | `parcel_share_pct` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 4 | `zone_area_m2` | float64 when builder initializes NaN/numeric metric; otherwise exact source numeric dtype shown by implementation | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 5 | `zone_share_pct` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |


No enum/status/Literal value is classified as a column unless it is separately present in a canonical schema declaration. Mapping keys, JSON keys, dataclass fields, and configuration leaves remain distinct categories.

## 8. Interfaces

This module defines an exact `__all__` contract:

| Export | Kind | Origin | Included in `__all__` |
|---|---|---|---|
| `intersect_parcels_with_gpu_zoning` | re-exported/defined Python symbol | `defined in `src/landscout/stages/enrich_planning_zoning.py`` | yes |
| `validate_normalized_planning_zoning_inputs` | re-exported/defined Python symbol | `defined in `src/landscout/stages/enrich_planning_zoning.py`` | yes |

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

The module contributes to the planning flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.

# `src/landscout/stages/enrich_planning_zoning.py`

## File identity

- Repository path: `src/landscout/stages/enrich_planning_zoning.py`
- File type: Python source
- Primary responsibility: Intersects parcels with source-completely verified GPU zoning polygons and retains factual overlap evidence.
- Layer / domain: `stage` / `planning`
- Public or internal role: Contains an explicit module/package export surface; helpers prefixed with `_` remain internal unless re-exported elsewhere.
- Source SHA256: `1838ea77ee7872ce8b663ecb19ffb82455abc7f4c947a847f041828808f22bf9`

## 1. Purpose

Intersects parcels with source-completely verified GPU zoning polygons and retains factual overlap evidence.

## 2. Position in LandScout architecture

This file is a `stage` artifact in the `planning` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `from dataclasses import dataclass, replace` — required by the implementation paths and symbols documented below.
- `from math import isfinite` — required by the implementation paths and symbols documented below.
- `from numbers import Real` — required by the implementation paths and symbols documented below.

### Third-party

- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import numpy as np` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `from pyproj import CRS` — required by the implementation paths and symbols documented below.
- `from shapely import ( # type: ignore[import-untyped] area as shapely_area, )` — required by the implementation paths and symbols documented below.
- `from shapely import ( force_2d, union_all, )` — required by the implementation paths and symbols documented below.
- `from shapely import ( intersection as shapely_intersection, )` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.common.frame_integrity import deterministic_frame_schema_signature` — required by the implementation paths and symbols documented below.
- `from landscout.sources.gpu_fr import ( GpuPlanningDocument, GpuSpatialInspectionError, revalidate_gpu_spatial_layer_sources, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.planning_overlay import technical_overlay_tolerance` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `CALCULATION_CRS` | `"EPSG:2154"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `GPU_ZONING_SOURCE_FIELDS` | `{ "source_zone_id": "LIB_IDZONE", "zone_label_raw": "LIBELLE", "zone_long_label_raw": "LIBELONG", "zone_type_raw": "TYPEZONE", "regulation_filename_raw": "NOMFIC", "regulation_url_raw": "URLFIC", "source_document_reference_raw": "IDURBA", "source_validity_date_raw": "DATVALID", }` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `GPU_ZONING_REQUIRED_COLUMNS` | `frozenset( {*GPU_ZONING_SOURCE_FIELDS.values(), "geometry"} )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `PARCEL_REQUIRED_COLUMNS` | `frozenset({"parcel_id", "geometry"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `POLYGON_GEOMETRY_TYPES` | `frozenset({"Polygon", "MultiPolygon"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `RELATION_TYPES` | `frozenset({"AREA_OVERLAP", "TOUCH_ONLY"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `PARCEL_ZONING_OUTPUT_COLUMNS` | `frozenset( { "zoning_area_match_count", "zoning_touch_only_count", "zoning_intersection_area_sum_m2", "zoning_covered_union_area_m2", "zoning_coverage_pct", "zoning_gap_area_m2", "zoning_overlap_excess_area_m2", "dominant_planning_zone_id", "dominant_source_zone_id", "dominant_zone_type_raw", "dominant_zone_label_raw", "dominant_zone_long_label_raw", "dominant_zone_intersection_area_m2", "dominant_zone_share_pct", "dominant_zone_tie_count", "planning_document_id", "planning_document_type", "planning_archive_name", "planning_archive_sha256", "planning_source_layer", "planning_standard_model", } )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `INTERSECTION_COLUMNS` | `( "parcel_id", "planning_zone_id", "source_zone_id", "zone_type_raw", "zone_label_raw", "zone_long_label_raw", "relation_type", "parcel_metric_area_m2", "zone_area_m2", "intersection_area_m2", "parcel_share_pct", "zone_share_pct", "source_document_id", "source_archive_sha256", "source_layer", "source_validity_date_raw", "regulation_filename_raw", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_INTERSECTION_FLOAT_COLUMNS` | `frozenset( { "parcel_metric_area_m2", "zone_area_m2", "intersection_area_m2", "parcel_share_pct", "zone_share_pct", } )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `PlanningZoningError`

**Purpose:** Raised when factual zoning normalization cannot be completed safely.

**Inheritance:** `ValueError`.

**Model form and mutability:** class inheriting from `ValueError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `ParcelZoningResult`

**Purpose:** Normalized zones, parcel facts, and long-form parcel/zone relations.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `parcels` | `gpd.GeoDataFrame` | `required` | Tabular/spatial evidence carried with the schema, dtype, index, geometry, and preservation contract documented in this module. |
| `zones` | `gpd.GeoDataFrame` | `required` | Tabular/spatial evidence carried with the schema, dtype, index, geometry, and preservation contract documented in this module. |
| `intersections` | `pd.DataFrame` | `required` | `pd.DataFrame` state used by `src/landscout/stages/enrich_planning_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `_PlanningContext`

**Purpose:** Groups the `PlanningContext` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `provider` | `str` | `required` | `str` state used by `src/landscout/stages/enrich_planning_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `portal` | `str` | `required` | `str` state used by `src/landscout/stages/enrich_planning_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `commune_code` | `str` | `required` | Exact configured or source code whose vocabulary/format is enforced by the owning validator. |
| `document_id` | `str` | `required` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `document_type` | `str` | `required` | Categorical source, feature, or relation type constrained by the owning model or validator. |
| `archive_name` | `str` | `required` | `str` state used by `src/landscout/stages/enrich_planning_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `archive_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `source_layer` | `str` | `required` | Source lineage or source-bound object whose exact identity is checked before downstream use. |
| `standard_model` | `str | None` | `required` | `str | None` state used by `src/landscout/stages/enrich_planning_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `source_crs` | `str` | `required` | Source lineage or source-bound object whose exact identity is checked before downstream use. |

**Validators and methods:**

- None.

## 6. Functions and methods

### `_strict_nonempty_string`

**Signature**

```python
def _strict_nonempty_string(value: object, label: str) -> str:
```

**Purpose**

Implements strict nonempty string according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `value`.

**Algorithm**

1. Checks `not isinstance(value, str) or not value or value != value.strip()`. When true: Raises `PlanningZoningError(f'{label} must be a non-empty exact string')`.
2. Returns `value`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(value, str) or not value or value != value.strip()` is true.

**Exceptions**

- Explicitly raises: `PlanningZoningError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningZoningError`, `isinstance`, `value.strip`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_zoning.py` — `_standard_model`
- `src/landscout/stages/enrich_planning_zoning.py` — `_validate_exact_string_ids`
- `src/landscout/stages/enrich_planning_zoning.py` — `_validate_planning_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_exact_string_ids`

**Signature**

```python
def _validate_exact_string_ids(
    values: pd.Series,
    label: str,
    *,
    require_unique: bool,
) -> None:
```

**Purpose**

Validates and rejects malformed exact string ids according to the exact implementation and guards in this file.

**Inputs**

- `values` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `require_unique` (`bool`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `values.isna().any()`. When true: Raises `PlanningZoningError(f'{label} values must not be null')`.
2. Iterates `value` over `values.tolist()`. For each value: Calls `_strict_nonempty_string(value, label)` for its validation or side effect.
3. Checks `require_unique and values.duplicated().any()`. When true: Raises `PlanningZoningError(f'{label} values must be unique')`.

**Validation and invariants**

- Rejects or diverts the path when `values.isna().any()` is true.
- Rejects or diverts the path when `require_unique and values.duplicated().any()` is true.

**Exceptions**

- Explicitly raises: `PlanningZoningError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningZoningError`, `_strict_nonempty_string`, `values.duplicated`, `values.duplicated().any`, `values.isna`, `values.isna().any`, `values.tolist`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_zoning.py` — `_validate_parcels`
- `src/landscout/stages/enrich_planning_zoning.py` — `_validate_planning_document`
- `src/landscout/stages/enrich_planning_zoning.py` — `_validate_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_readable_crs`

**Signature**

```python
def _readable_crs(value: object, label: str) -> CRS:
```

**Purpose**

Implements readable crs according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `CRS`. Observed return expression(s): `CRS.from_user_input(value)`.

**Algorithm**

1. Checks `value is None`. When true: Raises `PlanningZoningError(f'{label} CRS is required')`.
2. Runs guarded operation: Returns `CRS.from_user_input(value)`. Handles `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `value is None` is true.

**Exceptions**

- Explicitly raises: `PlanningZoningError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `CRS.from_user_input`, `PlanningZoningError`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_zoning.py` — `_project_geometries`
- `src/landscout/stages/enrich_planning_zoning.py` — `_validate_parcels`
- `src/landscout/stages/enrich_planning_zoning.py` — `_validate_planning_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_active_geometry`

**Signature**

```python
def _active_geometry(frame: gpd.GeoDataFrame, label: str) -> None:
```

**Purpose**

Implements active geometry according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `'geometry' not in frame.columns`. When true: Raises `PlanningZoningError(f'{label} geometry column is required')`.
2. Runs guarded operation: Computes `active_name` from `frame.active_geometry_name`. Handles `AttributeError`.
3. Checks `active_name != 'geometry'`. When true: Raises `PlanningZoningError(f'{label} geometry column must be active')`.

**Validation and invariants**

- Rejects or diverts the path when `'geometry' not in frame.columns` is true.
- Rejects or diverts the path when `active_name != 'geometry'` is true.

**Exceptions**

- Explicitly raises: `PlanningZoningError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningZoningError`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_zoning.py` — `_validate_parcels`
- `src/landscout/stages/enrich_planning_zoning.py` — `_validate_planning_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_polygon_geometries`

**Signature**

```python
def _validate_polygon_geometries(frame: gpd.GeoDataFrame, label: str) -> None:
```

**Purpose**

Validates and rejects malformed polygon geometries according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `geometry` from `frame.geometry`.
2. Checks `geometry.isna().any()`. When true: Raises `PlanningZoningError(f'{label} geometry must not be null')`.
3. Checks `geometry.is_empty.any()`. When true: Raises `PlanningZoningError(f'{label} geometry must not be empty')`.
4. Checks `not geometry.is_valid.all()`. When true: Raises `PlanningZoningError(f'{label} geometry must be valid')`.
5. Computes `unexpected` from `sorted(set(geometry.geom_type) - POLYGON_GEOMETRY_TYPES)`.
6. Checks `unexpected`. When true: Raises `PlanningZoningError(f'{label} geometry must be Polygon or MultiPolygon; found: ' + ', '.join(unexpected))`.

**Validation and invariants**

- Rejects or diverts the path when `geometry.isna().any()` is true.
- Rejects or diverts the path when `geometry.is_empty.any()` is true.
- Rejects or diverts the path when `not geometry.is_valid.all()` is true.
- Rejects or diverts the path when `unexpected` is true.

**Exceptions**

- Explicitly raises: `PlanningZoningError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `', '.join`, `PlanningZoningError`, `geometry.is_empty.any`, `geometry.is_valid.all`, `geometry.isna`, `geometry.isna().any`, `set`, `sorted`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_zoning.py` — `_validate_parcels`
- `src/landscout/stages/enrich_planning_zoning.py` — `_validate_planning_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_parcels`

**Signature**

```python
def _validate_parcels(parcels: gpd.GeoDataFrame) -> CRS:
```

**Purpose**

Validates and rejects malformed parcels according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `CRS`. Observed return expression(s): `crs`.

**Algorithm**

1. Checks `not isinstance(parcels, gpd.GeoDataFrame)`. When true: Raises `PlanningZoningError('Parcels must be a GeoDataFrame')`.
2. Computes `missing` from `sorted(PARCEL_REQUIRED_COLUMNS - set(parcels.columns))`.
3. Checks `missing`. When true: Raises `PlanningZoningError('Parcels are missing required columns: ' + ', '.join(missing))`.
4. Computes `collisions` from `sorted(PARCEL_ZONING_OUTPUT_COLUMNS & set(parcels.columns))`.
5. Checks `collisions`. When true: Raises `PlanningZoningError('Parcels already contain zoning output columns: ' + ', '.join(collisions))`.
6. Calls `_active_geometry(parcels, 'Parcel')` for its validation or side effect.
7. Computes `crs` from `_readable_crs(parcels.crs, 'Parcel')`.
8. Calls `_validate_exact_string_ids(parcels['parcel_id'], 'parcel_id', require_unique=True)` for its validation or side effect.
9. Calls `_validate_polygon_geometries(parcels, 'Parcel')` for its validation or side effect.
10. Returns `crs`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(parcels, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `missing` is true.
- Rejects or diverts the path when `collisions` is true.

**Exceptions**

- Explicitly raises: `PlanningZoningError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `', '.join`, `PlanningZoningError`, `_active_geometry`, `_readable_crs`, `_validate_exact_string_ids`, `_validate_polygon_geometries`, `isinstance`, `set`, `sorted`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_zoning.py` — `intersect_parcels_with_gpu_zoning`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_standard_model`

**Signature**

```python
def _standard_model(planning_document: GpuPlanningDocument) -> str | None:
```

**Purpose**

Implements standard model according to the exact implementation and guards in this file.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str | None`. Observed return expression(s): `values[0]`; `None`.

**Algorithm**

1. Computes `document_value` from `planning_document.extraction.archive.document.standard_model`.
2. Defines `values` with annotation `list[str]` from `[]`.
3. Checks `document_value is not None`. When true: Calls `values.append(_strict_nonempty_string(document_value, 'GPU standard model'))` for its validation or side effect.
4. Iterates `value` over `planning_document.extraction.standard_models`. For each value: Computes `validated` from `_strict_nonempty_string(value, 'GPU extracted standard model')`. Checks `validated not in values`. When true: Calls `values.append(validated)` for its validation or side effect.
5. Checks `not values`. When true: Returns `None`.
6. Checks `len(values) != 1`. When true: Raises `PlanningZoningError('GPU standard-model lineage is ambiguous')`.
7. Returns `values[0]`.

**Validation and invariants**

- Rejects or diverts the path when `len(values) != 1` is true.

**Exceptions**

- Explicitly raises: `PlanningZoningError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningZoningError`, `_strict_nonempty_string`, `len`, `values.append`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_zoning.py` — `_validate_planning_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_planning_document`

**Signature**

```python
def _validate_planning_document(
    planning_document: GpuPlanningDocument,
) -> tuple[_PlanningContext, gpd.GeoDataFrame]:
```

**Purpose**

Validates and rejects malformed planning document according to the exact implementation and guards in this file.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[_PlanningContext, gpd.GeoDataFrame]`. Observed return expression(s): `(context, source)`.

**Algorithm**

1. Checks `not isinstance(planning_document, GpuPlanningDocument)`. When true: Raises `PlanningZoningError('planning_document must be a GpuPlanningDocument')`.
2. Computes `archive` from `planning_document.extraction.archive`.
3. Computes `document` from `archive.document`.
4. Computes `provider` from `_strict_nonempty_string(document.provider, 'GPU provider')`.
5. Computes `portal` from `_strict_nonempty_string(document.portal, 'GPU portal')`.
6. Computes `commune_code` from `_strict_nonempty_string(document.commune_code, 'GPU commune code')`.
7. Computes `document_id` from `_strict_nonempty_string(document.document_id, 'GPU document ID')`.
8. Computes `document_type` from `_strict_nonempty_string(document.document_type, 'GPU document type')`.
9. Computes `archive_name` from `_strict_nonempty_string(document.archive_name, 'GPU archive name')`.
10. Computes `archive_sha256` from `_strict_nonempty_string(archive.sha256, 'GPU archive SHA256')`.
11. Checks `len(archive_sha256) != 64 or any((character not in '0123456789abcdefABCDEF' for character in archive_sha256))`. When true: Raises `PlanningZoningError('GPU archive SHA256 must contain 64 hexadecimal chars')`.
12. Computes `zoning` from `planning_document.zoning`.
13. Checks `zoning.logical_name != 'zoning'`. When true: Raises `PlanningZoningError('GPU planning bundle must contain its zoning layer')`.
14. Computes `source_layer` from `_strict_nonempty_string(zoning.reference.source_layer, 'GPU zoning source layer')`.
15. Computes `source` from `zoning.data`.
16. Checks `not isinstance(source, gpd.GeoDataFrame)`. When true: Raises `PlanningZoningError('GPU zoning data must be a GeoDataFrame')`.
17. Computes `missing` from `sorted(GPU_ZONING_REQUIRED_COLUMNS - set(source.columns))`.
18. Checks `missing`. When true: Raises `PlanningZoningError('GPU zoning is missing required source columns: ' + ', '.join(missing))`.
19. Calls `_active_geometry(source, 'GPU zoning')` for its validation or side effect.
20. Computes `source_crs` from `_readable_crs(source.crs, 'GPU zoning')`.
21. Calls `_validate_polygon_geometries(source, 'GPU zoning')` for its validation or side effect.
22. Checks `source.empty`. When true: Raises `PlanningZoningError('GPU zoning must contain at least one source zone')`.
23. Computes `source_zone_column` from `GPU_ZONING_SOURCE_FIELDS['source_zone_id']`.
24. Calls `_validate_exact_string_ids(source[source_zone_column], source_zone_column, require_unique=True)` for its validation or side effect.
25. Computes `source_document_column` from `GPU_ZONING_SOURCE_FIELDS['source_document_reference_raw']`.
26. Calls `_validate_exact_string_ids(source[source_document_column], source_document_column, require_unique=False)` for its validation or side effect.
27. Computes `expected_document_reference` from `archive_name[:-4] if archive_name.casefold().endswith('.zip') else archive_name`.
28. Checks `not source[source_document_column].eq(expected_document_reference).all()`. When true: Raises `PlanningZoningError('GPU zoning IDURBA does not match the loaded planning archive identity')`.
29. Computes `summary` from `zoning.summary`.
30. Checks `summary.source_document_id != document_id`. When true: Raises `PlanningZoningError('GPU zoning summary document lineage is inconsistent')`.
31. Checks `summary.source_archive_sha256 != archive_sha256`. When true: Raises `PlanningZoningError('GPU zoning summary archive lineage is inconsistent')`.
32. Checks `summary.source_layer != source_layer`. When true: Raises `PlanningZoningError('GPU zoning summary source layer is inconsistent')`.
33. Checks `summary.feature_count != len(source)`. When true: Raises `PlanningZoningError('GPU zoning summary feature count is inconsistent')`.
34. Computes `context` from `_PlanningContext(provider=provider, portal=portal, commune_code=commune_code, document_id=document_id, document_type=document_type, archive_name=archive_name, archive_sha256=archive_sha256, source_layer=source_layer, standard_model=_standard_model(planning_document), source_crs=source_crs.to_string())`.
35. Returns `(context, source)`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(planning_document, GpuPlanningDocument)` is true.
- Rejects or diverts the path when `len(archive_sha256) != 64 or any((character not in '0123456789abcdefABCDEF' for character in archive_sha256))` is true.
- Rejects or diverts the path when `zoning.logical_name != 'zoning'` is true.
- Rejects or diverts the path when `not isinstance(source, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `missing` is true.
- Rejects or diverts the path when `source.empty` is true.
- Rejects or diverts the path when `not source[source_document_column].eq(expected_document_reference).all()` is true.
- Rejects or diverts the path when `summary.source_document_id != document_id` is true.
- Rejects or diverts the path when `summary.source_archive_sha256 != archive_sha256` is true.
- Rejects or diverts the path when `summary.source_layer != source_layer` is true.
- Rejects or diverts the path when `summary.feature_count != len(source)` is true.

**Exceptions**

- Explicitly raises: `PlanningZoningError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `', '.join`, `PlanningZoningError`, `_PlanningContext`, `_active_geometry`, `_readable_crs`, `_standard_model`, `_strict_nonempty_string`, `_validate_exact_string_ids`, `_validate_polygon_geometries`, `any`, `archive_name.casefold`, `archive_name.casefold().endswith`, `isinstance`, `len`, `set`, `sorted`, `source[source_document_column].eq`, `source[source_document_column].eq(expected_document_reference).all`, `source_crs.to_string`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_zoning.py` — `intersect_parcels_with_gpu_zoning`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_project_geometries`

**Signature**

```python
def _project_geometries(
    frame: gpd.GeoDataFrame,
    label: str,
) -> gpd.GeoSeries:
```

**Purpose**

Implements project geometries according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoSeries`. Observed return expression(s): `projected`.

**Algorithm**

1. Computes `source_crs` from `_readable_crs(frame.crs, label)`.
2. Computes `target_crs` from `CRS.from_epsg(2154)`.
3. Runs guarded operation: Checks `source_crs.equals(target_crs)`. When true: Computes `projected` from `frame.geometry.copy()`. Otherwise: Computes `projected` from `frame.geometry.to_crs(target_crs)`. Computes `projected` from `gpd.GeoSeries(force_2d(projected.array), index=frame.index, crs=CALCULATION_CRS)`. Handles `Exception`.
4. Returns `projected`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `PlanningZoningError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `frame.geometry.copy`, `frame.geometry.to_crs`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `CRS.from_epsg`, `PlanningZoningError`, `_readable_crs`, `force_2d`, `frame.geometry.copy`, `frame.geometry.to_crs`, `gpd.GeoSeries`, `source_crs.equals`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_zoning.py` — `_metric_parcels`
- `src/landscout/stages/enrich_planning_zoning.py` — `_normalize_zones`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_normalize_zones`

**Signature**

```python
def _normalize_zones(
    source: gpd.GeoDataFrame,
    context: _PlanningContext,
) -> gpd.GeoDataFrame:
```

**Purpose**

Normalizes zones according to the exact implementation and guards in this file.

**Inputs**

- `source` (`gpd.GeoDataFrame`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `context` (`_PlanningContext`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `zones`.

**Algorithm**

1. Computes `projected_geometry` from `_project_geometries(source, 'GPU zoning')`.
2. Computes `source_zone_ids` from `source[GPU_ZONING_SOURCE_FIELDS['source_zone_id']].copy()`.
3. Computes `planning_zone_ids` from `source_zone_ids.map(lambda value: f'GPU:{context.document_id}:ZONE:{value}')`.
4. Checks `planning_zone_ids.duplicated().any()`. When true: Raises `PlanningZoningError('Normalized planning_zone_id values must be unique')`.
5. Defines `data` with annotation `dict[str, object]` from `{'planning_zone_id': planning_zone_ids.to_numpy(copy=True), 'source_zone_id': source_zone_ids.to_numpy(copy=True)}`.
6. Iterates `(normalized_name, source_name)` over `GPU_ZONING_SOURCE_FIELDS.items()`. For each value: Checks `normalized_name == 'source_zone_id'`. When true: Executes `continue` control flow. Computes `data[normalized_name]` from `source[source_name].to_numpy(copy=True)`.
7. Computes `count` from `len(source)`.
8. Calls `data.update({'source_provider': np.repeat(context.provider, count), 'source_portal': np.repeat(context.portal, count), 'source_commune_code': np.repeat(context.commune_code, count), 'source_document_id': np.repeat(context.document_id, count), 'source_document_type': np.repeat(context.document_type, count), 'source_archive_name': np.repeat(context.archive_na…` for its validation or side effect.
9. Computes `zones` from `gpd.GeoDataFrame(data, geometry=projected_geometry.to_numpy(copy=True), crs=CALCULATION_CRS)`.
10. Computes `zone_areas` from `zones.geometry.area.to_numpy(dtype='float64', copy=True)`.
11. Checks `not np.isfinite(zone_areas).all() or (zone_areas <= 0).any()`. When true: Raises `PlanningZoningError('GPU zone areas must be finite and positive')`.
12. Computes `zones['zone_area_m2']` from `zone_areas`.
13. Computes `zones` from `zones.reset_index(drop=True)`.
14. Computes `zones` from `zones.set_crs(CALCULATION_CRS, allow_override=True)`.
15. Returns `zones`.

**Validation and invariants**

- Rejects or diverts the path when `planning_zone_ids.duplicated().any()` is true.
- Rejects or diverts the path when `not np.isfinite(zone_areas).all() or (zone_areas <= 0).any()` is true.

**Exceptions**

- Explicitly raises: `PlanningZoningError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `source[GPU_ZONING_SOURCE_FIELDS['source_zone_id']].copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `(zone_areas <= 0).any`, `GPU_ZONING_SOURCE_FIELDS.items`, `PlanningZoningError`, `_project_geometries`, `data.update`, `gpd.GeoDataFrame`, `len`, `np.full`, `np.isfinite`, `np.isfinite(zone_areas).all`, `np.repeat`, `planning_zone_ids.duplicated`, `planning_zone_ids.duplicated().any`, `planning_zone_ids.to_numpy`, `projected_geometry.to_numpy`, `source[GPU_ZONING_SOURCE_FIELDS['source_zone_id']].copy`, `source[source_name].to_numpy`, `source_zone_ids.map`, `source_zone_ids.to_numpy`, `zones.geometry.area.to_numpy`, `zones.reset_index`, `zones.set_crs`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_zoning.py` — `intersect_parcels_with_gpu_zoning`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_metric_parcels`

**Signature**

```python
def _metric_parcels(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
```

**Purpose**

Implements metric parcels according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `metric`.

**Algorithm**

1. Computes `geometry` from `_project_geometries(parcels, 'Parcel')`.
2. Computes `metric` from `gpd.GeoDataFrame({'_parcel_position': np.arange(len(parcels), dtype='int64'), 'parcel_id': parcels['parcel_id'].to_numpy(copy=True)}, geometry=geometry.to_numpy(copy=True), crs=CALCULATION_CRS)`.
3. Computes `areas` from `metric.geometry.area.to_numpy(dtype='float64', copy=True)`.
4. Checks `not np.isfinite(areas).all() or (areas <= 0).any()`. When true: Raises `PlanningZoningError('Parcel metric areas must be finite and positive')`.
5. Computes `metric['_parcel_area_m2']` from `areas`.
6. Returns `metric`.

**Validation and invariants**

- Rejects or diverts the path when `not np.isfinite(areas).all() or (areas <= 0).any()` is true.

**Exceptions**

- Explicitly raises: `PlanningZoningError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `(areas <= 0).any`, `PlanningZoningError`, `_project_geometries`, `geometry.to_numpy`, `gpd.GeoDataFrame`, `len`, `metric.geometry.area.to_numpy`, `np.arange`, `np.isfinite`, `np.isfinite(areas).all`, `parcels['parcel_id'].to_numpy`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_zoning.py` — `intersect_parcels_with_gpu_zoning`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_empty_intersections`

**Signature**

```python
def _empty_intersections() -> pd.DataFrame:
```

**Purpose**

Implements empty intersections according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `pd.DataFrame({column: pd.Series(dtype='float64' if column in _INTERSECTION_FLOAT_COLUMNS else 'object') for column in INTERSECTION_COLUMNS})`.

**Algorithm**

1. Returns `pd.DataFrame({column: pd.Series(dtype='float64' if column in _INTERSECTION_FLOAT_COLUMNS else 'object') for column in INTERSECTION_COLUMNS})`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `pd.DataFrame`, `pd.Series`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_zoning.py` — `intersect_parcels_with_gpu_zoning`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_candidate_intersections`

**Signature**

```python
def _candidate_intersections(
    metric_parcels: gpd.GeoDataFrame,
    zones: gpd.GeoDataFrame,
) -> pd.DataFrame:
```

**Purpose**

Implements candidate intersections according to the exact implementation and guards in this file.

**Inputs**

- `metric_parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zones` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `work`; `pd.DataFrame(columns=('_parcel_position', '_zone_position', '_intersection_geometry'))`.

**Algorithm**

1. Computes `parcel_candidates` from `gpd.GeoDataFrame(metric_parcels[['_parcel_position', 'parcel_id']].copy(), geometry=metric_parcels.geometry.to_numpy(copy=True), crs=CALCULATION_CRS)`.
2. Computes `zone_candidates` from `gpd.GeoDataFrame({'_zone_position': np.arange(len(zones), dtype='int64')}, geometry=zones.geometry.to_numpy(copy=True), crs=CALCULATION_CRS)`.
3. Runs guarded operation: Computes `candidates` from `gpd.sjoin(parcel_candidates, zone_candidates, how='inner', predicate='intersects')`. Handles `Exception`.
4. Checks `candidates.empty`. When true: Returns `pd.DataFrame(columns=('_parcel_position', '_zone_position', '_intersection_geometry'))`.
5. Computes `parcel_positions` from `candidates['_parcel_position'].to_numpy(dtype='int64', copy=True)`.
6. Computes `zone_positions` from `candidates['_zone_position'].to_numpy(dtype='int64', copy=True)`.
7. Runs guarded operation: Computes `intersection_geometry` from `shapely_intersection(metric_parcels.geometry.iloc[parcel_positions].array, zones.geometry.iloc[zone_positions].array)`. Computes `intersection_areas` from `np.asarray(shapely_area(intersection_geometry), dtype='float64')`. Handles `Exception`.
8. Checks `not np.isfinite(intersection_areas).all() or (intersection_areas < 0).any()`. When true: Raises `PlanningZoningError('Intersection areas must be finite and non-negative')`.
9. Computes `parcel_areas` from `metric_parcels['_parcel_area_m2'].to_numpy(dtype='float64')[parcel_positions]`.
10. Computes `zone_areas` from `zones['zone_area_m2'].to_numpy(dtype='float64')[zone_positions]`.
11. Computes `relation_types` from `np.where(intersection_areas > 0, 'AREA_OVERLAP', 'TOUCH_ONLY')`.
12. Computes `selected_zones` from `zones.iloc[zone_positions]`.
13. Computes `geometry_values` from `np.empty(len(intersection_geometry), dtype='object')`.
14. Computes `geometry_values[:]` from `intersection_geometry`.
15. Computes `work` from `pd.DataFrame({'_parcel_position': parcel_positions, '_zone_position': zone_positions, '_intersection_geometry': geometry_values, 'parcel_id': metric_parcels['parcel_id'].to_numpy(copy=False)[parcel_positions], 'planning_zone_id': selected_zones['planning_zone_id'].to_numpy(copy=True), 'source_zone_id': selected_zones[…`.
16. Computes `work` from `work.sort_values(['_parcel_position', 'planning_zone_id'], kind='stable').reset_index(drop=True)`.
17. Returns `work`.

**Validation and invariants**

- Rejects or diverts the path when `not np.isfinite(intersection_areas).all() or (intersection_areas < 0).any()` is true.

**Exceptions**

- Explicitly raises: `PlanningZoningError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `metric_parcels[['_parcel_position', 'parcel_id']].copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `(intersection_areas < 0).any`, `PlanningZoningError`, `candidates['_parcel_position'].to_numpy`, `candidates['_zone_position'].to_numpy`, `gpd.GeoDataFrame`, `gpd.sjoin`, `len`, `metric_parcels.geometry.to_numpy`, `metric_parcels['_parcel_area_m2'].to_numpy`, `metric_parcels['parcel_id'].to_numpy`, `metric_parcels[['_parcel_position', 'parcel_id']].copy`, `np.arange`, `np.asarray`, `np.empty`, `np.isfinite`, `np.isfinite(intersection_areas).all`, `np.where`, `pd.DataFrame`, `selected_zones['planning_zone_id'].to_numpy`, `selected_zones['regulation_filename_raw'].to_numpy`, `selected_zones['source_archive_sha256'].to_numpy`, `selected_zones['source_document_id'].to_numpy`, `selected_zones['source_layer'].to_numpy`, `selected_zones['source_validity_date_raw'].to_numpy`, `selected_zones['source_zone_id'].to_numpy`, `selected_zones['zone_label_raw'].to_numpy`, `selected_zones['zone_long_label_raw'].to_numpy`, `selected_zones['zone_type_raw'].to_numpy`, `shapely_area`, `shapely_intersection`, `work.sort_values`, `work.sort_values(['_parcel_position', 'planning_zone_id'], kind='stable').reset_index`, `zones.geometry.to_numpy`, `zones['zone_area_m2'].to_numpy`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_zoning.py` — `intersect_parcels_with_gpu_zoning`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_technical_area_tolerance`

**Signature**

```python
def _technical_area_tolerance(parcel_area_m2: float) -> float:
```

**Purpose**

Implements technical area tolerance according to the exact implementation and guards in this file.

**Inputs**

- `parcel_area_m2` (`float`; required) — area quantity, normally square metres where the name ends in `_m2`. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `float`. Observed return expression(s): `technical_overlay_tolerance(parcel_area_m2)`.

**Algorithm**

1. Returns `technical_overlay_tolerance(parcel_area_m2)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `technical_overlay_tolerance`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_zoning.py` — `_stabilize_area_relationships`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_stabilize_area_relationships`

**Signature**

```python
def _stabilize_area_relationships(
    parcel_area: float,
    raw_sum: float,
    covered_union: float,
) -> tuple[float, float, float]:
```

**Purpose**

Implements stabilize area relationships according to the exact implementation and guards in this file.

**Inputs**

- `parcel_area` (`float`; required) — area quantity, normally square metres where the name ends in `_m2`. Nullability and accepted values are exactly those enforced by the guards listed below.
- `raw_sum` (`float`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `covered_union` (`float`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[float, float, float]`. Observed return expression(s): `(covered_union, gap, overlap_excess)`.

**Algorithm**

1. Computes `tolerance` from `_technical_area_tolerance(parcel_area)`.
2. Checks `covered_union > parcel_area`. When true: Checks `covered_union - parcel_area > tolerance`. When true: Raises `PlanningZoningError('Zoning covered-union area materially exceeds parcel area')`. Computes `covered_union` from `parcel_area`.
3. Checks `covered_union > raw_sum`. When true: Checks `covered_union - raw_sum > tolerance`. When true: Raises `PlanningZoningError('Zoning covered-union area materially exceeds raw intersection sum')`. Computes `covered_union` from `raw_sum`.
4. Computes `gap` from `parcel_area - covered_union`.
5. Computes `overlap_excess` from `raw_sum - covered_union`.
6. Checks `gap < 0 or overlap_excess < 0`. When true: Raises `PlanningZoningError('Zoning area differences must not be negative')`.
7. Returns `(covered_union, gap, overlap_excess)`.

**Validation and invariants**

- Rejects or diverts the path when `covered_union > parcel_area` is true.
- Rejects or diverts the path when `covered_union > raw_sum` is true.
- Rejects or diverts the path when `gap < 0 or overlap_excess < 0` is true.
- Rejects or diverts the path when `covered_union - parcel_area > tolerance` is true.
- Rejects or diverts the path when `covered_union - raw_sum > tolerance` is true.

**Exceptions**

- Explicitly raises: `PlanningZoningError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningZoningError`, `_technical_area_tolerance`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_zoning.py` — `_parcel_summary`
- `tests/unit/test_enrich_planning_zoning.py` — `test_shared_overlay_tolerance_preserves_zoning_numerical_behavior`

**Tests**

- `tests/unit/test_enrich_planning_zoning.py::test_shared_overlay_tolerance_preserves_zoning_numerical_behavior`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_parcel_summary`

**Signature**

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

Implements parcel summary according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `metric_parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zones` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `work` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `context` (`_PlanningContext`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `output`.

**Algorithm**

1. Computes `count` from `len(parcels)`.
2. Computes `parcel_areas` from `metric_parcels['_parcel_area_m2'].to_numpy(dtype='float64', copy=True)`.
3. Computes `area_match_count` from `np.zeros(count, dtype='int64')`.
4. Computes `touch_count` from `np.zeros(count, dtype='int64')`.
5. Computes `raw_sum` from `np.zeros(count, dtype='float64')`.
6. Computes `covered_union` from `np.zeros(count, dtype='float64')`.
7. Computes `gap` from `parcel_areas.copy()`.
8. Computes `overlap_excess` from `np.zeros(count, dtype='float64')`.
9. Computes `dominant_planning` from `np.full(count, None, dtype='object')`.
10. Computes `dominant_source` from `np.full(count, None, dtype='object')`.
11. Computes `dominant_type` from `np.full(count, None, dtype='object')`.
12. Computes `dominant_label` from `np.full(count, None, dtype='object')`.
13. Computes `dominant_long_label` from `np.full(count, None, dtype='object')`.
14. Computes `dominant_area` from `np.full(count, np.nan, dtype='float64')`.
15. Computes `dominant_share` from `np.full(count, np.nan, dtype='float64')`.
16. Computes `dominant_ties` from `pd.array([pd.NA] * count, dtype='Int64')`.
17. Checks `not work.empty`. When true: Computes `touches` from `work.loc[work['relation_type'] == 'TOUCH_ONLY']`. Iterates `(position, group)` over `touches.groupby('_parcel_position', sort=False)`. For each value: Computes `touch_count[int(position)]` from `len(group)`. Computes `positive` from `work.loc[work['relation_type'] == 'AREA_OVERLAP']`. Executes 1 additional source-ordered statement(s).
18. Computes `output` from `parcels.copy(deep=True)`.
19. Computes `output['zoning_area_match_count']` from `area_match_count`.
20. Computes `output['zoning_touch_only_count']` from `touch_count`.
21. Computes `output['zoning_intersection_area_sum_m2']` from `raw_sum`.
22. Computes `output['zoning_covered_union_area_m2']` from `covered_union`.
23. Computes `output['zoning_coverage_pct']` from `np.where(gap == 0.0, 100.0, 100.0 * covered_union / parcel_areas)`.
24. Computes `output['zoning_gap_area_m2']` from `gap`.
25. Computes `output['zoning_overlap_excess_area_m2']` from `overlap_excess`.
26. Computes `output['dominant_planning_zone_id']` from `dominant_planning`.
27. Computes `output['dominant_source_zone_id']` from `dominant_source`.
28. Computes `output['dominant_zone_type_raw']` from `dominant_type`.
29. Computes `output['dominant_zone_label_raw']` from `dominant_label`.
30. Computes `output['dominant_zone_long_label_raw']` from `dominant_long_label`.
31. Computes `output['dominant_zone_intersection_area_m2']` from `dominant_area`.
32. Computes `output['dominant_zone_share_pct']` from `dominant_share`.
33. Computes `output['dominant_zone_tie_count']` from `dominant_ties`.
34. Computes `output['planning_document_id']` from `context.document_id`.
35. Computes `output['planning_document_type']` from `context.document_type`.
36. Computes `output['planning_archive_name']` from `context.archive_name`.
37. Computes `output['planning_archive_sha256']` from `context.archive_sha256`.
38. Computes `output['planning_source_layer']` from `context.source_layer`.
39. Computes `output['planning_standard_model']` from `context.standard_model`.
40. Returns `output`.

**Validation and invariants**

- Rejects or diverts the path when `not work.empty` is true.
- Rejects or diverts the path when `not isfinite(union_area) or union_area < 0` is true.

**Exceptions**

- Explicitly raises: `PlanningZoningError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `parcel_areas.copy`, `parcels.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `PlanningZoningError`, `_stabilize_area_relationships`, `areas.max`, `areas.sum`, `float`, `group['_intersection_geometry'].to_numpy`, `group['intersection_area_m2'].to_numpy`, `int`, `isfinite`, `len`, `metric_parcels['_parcel_area_m2'].to_numpy`, `np.full`, `np.where`, `np.zeros`, `parcel_areas.copy`, `parcels.copy`, `pd.array`, `positive.groupby`, `shapely_area`, `tied.sort_values`, `touches.groupby`, `union_all`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_zoning.py` — `intersect_parcels_with_gpu_zoning`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_numeric_columns`

**Signature**

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

Validates and rejects malformed numeric columns according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `columns` (`tuple[str, ...] | frozenset[str]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `allow_null` (`bool`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Iterates `column` over `columns`. For each value: Checks `column not in frame.columns`. When true: Raises `PlanningZoningError(f'{label} is missing numeric column: {column}')`. Iterates `value` over `frame[column].tolist()`. For each value: Checks `pd.isna(value)`. When true: Checks `allow_null`. When true: Executes `continue` control flow. Raises `PlanningZoningError(f'{label} {column} must not be null')`. Checks `isinstance(value, bool) or not isinstance(value, Real)`. When true: Raises `PlanningZoningError(f'{label} {column} must be numeric')`. Runs guarded operation: Computes `numeric` from `float(value)`. Handles `(TypeError, ValueError, OverflowError)`. Executes 1 additional source-ordered statement(s).

**Validation and invariants**

- Rejects or diverts the path when `column not in frame.columns` is true.
- Rejects or diverts the path when `pd.isna(value)` is true.
- Rejects or diverts the path when `isinstance(value, bool) or not isinstance(value, Real)` is true.
- Rejects or diverts the path when `not isfinite(numeric) or numeric < 0` is true.

**Exceptions**

- Explicitly raises: `PlanningZoningError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningZoningError`, `float`, `frame[column].tolist`, `isfinite`, `isinstance`, `pd.isna`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_zoning.py` — `_validate_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_result`

**Signature**

```python
def _validate_result(
    input_parcels: gpd.GeoDataFrame,
    result: ParcelZoningResult,
) -> None:
```

**Purpose**

Validates and rejects malformed result according to the exact implementation and guards in this file.

**Inputs**

- `input_parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`ParcelZoningResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `output` from `result.parcels`.
2. Checks `len(output) != len(input_parcels)`. When true: Raises `PlanningZoningError('Parcel zoning output count changed')`.
3. Checks `output['parcel_id'].tolist() != input_parcels['parcel_id'].tolist()`. When true: Raises `PlanningZoningError('Parcel zoning output IDs or order changed')`.
4. Checks `not output.index.equals(input_parcels.index)`. When true: Raises `PlanningZoningError('Parcel zoning output index changed')`.
5. Checks `output.crs != input_parcels.crs`. When true: Raises `PlanningZoningError('Parcel zoning output CRS changed')`.
6. Checks `not np.array_equal(output.geometry.to_wkb(), input_parcels.geometry.to_wkb())`. When true: Raises `PlanningZoningError('Parcel zoning output geometry changed')`.
7. Checks `not CRS.from_user_input(result.zones.crs).equals(CRS.from_epsg(2154))`. When true: Raises `PlanningZoningError('Normalized zones must use EPSG:2154')`.
8. Calls `_validate_exact_string_ids(result.zones['planning_zone_id'], 'planning_zone_id', require_unique=True)` for its validation or side effect.
9. Calls `_validate_numeric_columns(result.zones, ('zone_area_m2',), 'Normalized zone', allow_null=False)` for its validation or side effect.
10. Computes `intersections` from `result.intersections`.
11. Computes `missing` from `sorted(set(INTERSECTION_COLUMNS) - set(intersections.columns))`.
12. Checks `missing`. When true: Raises `PlanningZoningError('Intersection table is missing columns: ' + ', '.join(missing))`.
13. Checks `intersections.duplicated(['parcel_id', 'planning_zone_id']).any()`. When true: Raises `PlanningZoningError('Parcel/zone intersection pairs must be unique')`.
14. Checks `not set(intersections['parcel_id']).issubset(set(output['parcel_id']))`. When true: Raises `PlanningZoningError('Intersection table contains an unknown parcel ID')`.
15. Checks `not set(intersections['planning_zone_id']).issubset(set(result.zones['planning_zone_id']))`. When true: Raises `PlanningZoningError('Intersection table contains an unknown zone ID')`.
16. Checks `not set(intersections['relation_type']).issubset(RELATION_TYPES)`. When true: Raises `PlanningZoningError('Intersection table has an unknown relation type')`.
17. Calls `_validate_numeric_columns(intersections, _INTERSECTION_FLOAT_COLUMNS, 'Intersection table', allow_null=False)` for its validation or side effect.
18. Computes `required_summary` from `('zoning_area_match_count', 'zoning_touch_only_count', 'zoning_intersection_area_sum_m2', 'zoning_covered_union_area_m2', 'zoning_coverage_pct', 'zoning_gap_area_m2', 'zoning_overlap_excess_area_m2')`.
19. Calls `_validate_numeric_columns(output, required_summary, 'Parcel zoning', allow_null=False)` for its validation or side effect.
20. Computes `coverage` from `output['zoning_coverage_pct'].to_numpy(dtype='float64')`.
21. Checks `(coverage > 100.0).any()`. When true: Raises `PlanningZoningError('Parcel zoning coverage must not exceed 100 percent')`.

**Validation and invariants**

- Rejects or diverts the path when `len(output) != len(input_parcels)` is true.
- Rejects or diverts the path when `output['parcel_id'].tolist() != input_parcels['parcel_id'].tolist()` is true.
- Rejects or diverts the path when `not output.index.equals(input_parcels.index)` is true.
- Rejects or diverts the path when `output.crs != input_parcels.crs` is true.
- Rejects or diverts the path when `not np.array_equal(output.geometry.to_wkb(), input_parcels.geometry.to_wkb())` is true.
- Rejects or diverts the path when `not CRS.from_user_input(result.zones.crs).equals(CRS.from_epsg(2154))` is true.
- Rejects or diverts the path when `missing` is true.
- Rejects or diverts the path when `intersections.duplicated(['parcel_id', 'planning_zone_id']).any()` is true.
- Rejects or diverts the path when `not set(intersections['parcel_id']).issubset(set(output['parcel_id']))` is true.
- Rejects or diverts the path when `not set(intersections['planning_zone_id']).issubset(set(result.zones['planning_zone_id']))` is true.
- Rejects or diverts the path when `not set(intersections['relation_type']).issubset(RELATION_TYPES)` is true.
- Rejects or diverts the path when `(coverage > 100.0).any()` is true.

**Exceptions**

- Explicitly raises: `PlanningZoningError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `', '.join`, `(coverage > 100.0).any`, `CRS.from_epsg`, `CRS.from_user_input`, `CRS.from_user_input(result.zones.crs).equals`, `PlanningZoningError`, `_validate_exact_string_ids`, `_validate_numeric_columns`, `input_parcels.geometry.to_wkb`, `input_parcels['parcel_id'].tolist`, `intersections.duplicated`, `intersections.duplicated(['parcel_id', 'planning_zone_id']).any`, `len`, `np.array_equal`, `output.geometry.to_wkb`, `output.index.equals`, `output['parcel_id'].tolist`, `output['zoning_coverage_pct'].to_numpy`, `set`, `set(intersections['parcel_id']).issubset`, `set(intersections['planning_zone_id']).issubset`, `set(intersections['relation_type']).issubset`, `sorted`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_zoning.py` — `intersect_parcels_with_gpu_zoning`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_compare_exact_frame`

**Signature**

```python
def _compare_exact_frame(
    supplied: pd.DataFrame,
    expected: pd.DataFrame,
    label: str,
) -> None:
```

**Purpose**

Compares exact frame according to the exact implementation and guards in this file.

**Inputs**

- `supplied` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `expected` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Runs guarded operation: Checks `type(supplied) is not type(expected)`. When true: Raises `PlanningZoningError(f'{label} frame type differs from reconstruction')`. Checks `deterministic_frame_schema_signature(supplied) != deterministic_frame_schema_signature(expected)`. When true: Raises `PlanningZoningError(f'{label} schema differs from reconstruction')`. Checks `isinstance(expected, gpd.GeoDataFrame)`. When true: Computes `geometry_column` from `expected.geometry.name`. Computes `attributes` from `[column for column in expected.columns if column != geometry_column]`. Checks `not supplied[attributes].equals(expected[attributes])`. When true: Raises `PlanningZoningError(f'{label} values or row order differ from reconstruction')`. Executes 1 additional source-ordered statement(s). Otherwise: Checks `not supplied.equals(expected)`. When true: Raises `PlanningZoningError(f'{label} values or row order differ from reconstruction')`. Handles `PlanningZoningError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `type(supplied) is not type(expected)` is true.
- Rejects or diverts the path when `deterministic_frame_schema_signature(supplied) != deterministic_frame_schema_signature(expected)` is true.
- Rejects or diverts the path when `isinstance(expected, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `not supplied[attributes].equals(expected[attributes])` is true.
- Rejects or diverts the path when `supplied.geometry.to_wkb().tolist() != expected.geometry.to_wkb().tolist()` is true.
- Rejects or diverts the path when `not supplied.equals(expected)` is true.

**Exceptions**

- Explicitly raises: `PlanningZoningError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningZoningError`, `deterministic_frame_schema_signature`, `expected.geometry.to_wkb`, `expected.geometry.to_wkb().tolist`, `isinstance`, `supplied.equals`, `supplied.geometry.to_wkb`, `supplied.geometry.to_wkb().tolist`, `supplied[attributes].equals`, `type`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_zoning.py` — `validate_normalized_planning_zoning_inputs`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_normalized_planning_zoning_inputs`

**Signature**

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

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zones` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zoning_intersections` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Runs guarded operation: Checks `type(planning_document) is not GpuPlanningDocument`. When true: Raises `PlanningZoningError('planning_document must be exactly a GpuPlanningDocument')`. Checks `not isinstance(parcels, gpd.GeoDataFrame)`. When true: Raises `PlanningZoningError('Zoning parcels must be a GeoDataFrame')`. Checks `not isinstance(zones, gpd.GeoDataFrame)`. When true: Raises `PlanningZoningError('Normalized zones must be a GeoDataFrame')`. Checks `not isinstance(zoning_intersections, pd.DataFrame) or isinstance(zoning_intersections, gpd.GeoDataFrame)`. When true: Raises `PlanningZoningError('Zoning intersections must be a non-geospatial DataFrame')`. Executes 11 additional source-ordered statement(s). Handles `PlanningZoningError`, `GpuSpatialInspectionError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `type(planning_document) is not GpuPlanningDocument` is true.
- Rejects or diverts the path when `not isinstance(parcels, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `not isinstance(zones, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `not isinstance(zoning_intersections, pd.DataFrame) or isinstance(zoning_intersections, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `len(validated_sources) != 1 or validated_sources[0].logical_name != 'zoning'` is true.
- Rejects or diverts the path when `not parcels.index.equals(expected.parcels.index)` is true.
- Rejects or diverts the path when `str(supplied.dtype) != str(rebuilt.dtype) or not supplied.equals(rebuilt)` is true.

**Exceptions**

- Explicitly raises: `PlanningZoningError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `parcels.drop(columns=list(present_summary_columns)).copy`, `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `PlanningZoningError`, `_compare_exact_frame`, `intersect_parcels_with_gpu_zoning`, `isinstance`, `len`, `list`, `parcels.drop`, `parcels.drop(columns=list(present_summary_columns)).copy`, `parcels.index.equals`, `replace`, `revalidate_gpu_spatial_layer_sources`, `str`, `supplied.equals`, `tuple`, `type`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `interpret_bess_zoning`
- `src/landscout/stages/interpret_bess_zoning.py` — `validate_bess_zoning_precheck`
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

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `intersect_parcels_with_gpu_zoning`

**Signature**

```python
def intersect_parcels_with_gpu_zoning(
    parcels: gpd.GeoDataFrame,
    planning_document: GpuPlanningDocument,
) -> ParcelZoningResult:
```

**Purpose**

Return factual parcel/zoning intersections without policy interpretation. Parcel storage geometry and CRS are preserved. Zoning normalization, overlay, area, and union calculations use planar XY geometry in EPSG:2154.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `ParcelZoningResult`. Observed return expression(s): `result`.

**Algorithm**

1. Calls `_validate_parcels(parcels)` for its validation or side effect.
2. Computes `(context, source_zones)` from `_validate_planning_document(planning_document)`.
3. Computes `zones` from `_normalize_zones(source_zones, context)`.
4. Computes `metric_parcels` from `_metric_parcels(parcels)`.
5. Computes `work` from `_candidate_intersections(metric_parcels, zones)`.
6. Computes `parcel_output` from `_parcel_summary(parcels, metric_parcels, zones, work, context)`.
7. Computes `intersections` from `_empty_intersections() if work.empty else work.loc[:, INTERSECTION_COLUMNS].reset_index(drop=True)`.
8. Computes `result` from `ParcelZoningResult(parcels=parcel_output, zones=zones, intersections=intersections)`.
9. Calls `_validate_result(parcels, result)` for its validation or side effect.
10. Returns `result`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ParcelZoningResult`, `_candidate_intersections`, `_empty_intersections`, `_metric_parcels`, `_normalize_zones`, `_parcel_summary`, `_validate_parcels`, `_validate_planning_document`, `_validate_result`, `work.loc[:, INTERSECTION_COLUMNS].reset_index`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_zoning.py` — `validate_normalized_planning_zoning_inputs`
- `tests/unit/test_enrich_planning_zoning.py` — `_run`
- `tests/unit/test_enrich_planning_zoning.py` — `test_input_frames_are_not_mutated`
- `tests/unit/test_enrich_planning_zoning.py` — `test_source_complete_zoning_validation_accepts_physical_fixture`
- `tests/unit/test_enrich_planning_zoning.py` — `test_source_complete_zoning_validation_rejects_coordinated_mutations`
- `tests/unit/test_enrich_planning_zoning.py` — `test_source_complete_zoning_validation_rejects_physical_tamper`
- `tests/unit/test_enrich_planning_zoning.py` — `test_source_complete_zoning_validation_revalidates_physical_source_once`
- `tests/unit/test_enrich_planning_zoning.py` — `test_zoning_summary_lineage_and_count_must_match_bundle`

**Tests**

- `tests/unit/test_enrich_planning_zoning.py::test_input_frames_are_not_mutated`
- `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_accepts_physical_fixture`
- `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_rejects_coordinated_mutations`
- `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_rejects_physical_tamper`
- `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_revalidates_physical_source_once`
- `tests/unit/test_enrich_planning_zoning.py::test_zoning_summary_lineage_and_count_must_match_bundle`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `_intersection_geometry` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `_parcel_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `_parcel_position` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `_zone_position` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `columns` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `dominant_planning_zone_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `dominant_source_zone_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `dominant_zone_intersection_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `dominant_zone_label_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `dominant_zone_long_label_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `dominant_zone_share_pct` | Logical dtype: float64. Nullability: determined by the owning schema/dtype map and explicit null guards. | percentage derived from the exact numerator/denominator named by its stage. Consumers and exact calculations are the functions that reference this column above. |
| `dominant_zone_tie_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `dominant_zone_type_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `intersection_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `kind` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
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
| `relation_type` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `source_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `source_document_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_document_reference_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `source_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
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

This file contributes to LandScout's `planning` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.

# `src/landscout/stages/assess_grid_coverage.py`

## File identity

- Repository path: `src/landscout/stages/assess_grid_coverage.py`
- File type: Python source
- Primary responsibility: Diagnoses grid proxy distances against the configured IGN source-package boundary.
- Layer / domain: `stage` / `grid`
- Public or internal role: Module symbols without a package re-export are internal unless imported directly by repository code.
- Source SHA256: `2a74a08a04563372347c42bacbf53fc124a57ee3a49686586983d81fcef41057`

## 1. Purpose

Diagnoses grid proxy distances against the configured IGN source-package boundary.

## 2. Position in LandScout architecture

This file is a `stage` artifact in the `grid` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import re` — required by the implementation paths and symbols documented below.
- `import unicodedata` — required by the implementation paths and symbols documented below.
- `from dataclasses import dataclass` — required by the implementation paths and symbols documented below.
- `from math import isfinite` — required by the implementation paths and symbols documented below.
- `from numbers import Real` — required by the implementation paths and symbols documented below.
- `from typing import Literal` — required by the implementation paths and symbols documented below.

### Third-party

- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import numpy as np` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `from pyproj import CRS` — required by the implementation paths and symbols documented below.
- `from shapely import ( # type: ignore[import-untyped] boundary, covers, distance, force_2d, intersects, )` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.sources.ign_bdtopo_fr import ( IgnBdTopoCoverageLayerSummary, IgnBdTopoDepartmentCoverage, IgnBdTopoElectricityData, IgnBdTopoSourceConfig, _discover_department_coverage_layer, load_ign_bdtopo_department_coverage, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.enrich_grid_proximity import ( GridProximityResult, VoltageLevelCoverage, enrich_parcel_grid_proximity, profile_grid_proximity, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `CALCULATION_CRS` | `"EPSG:2154"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `COVERAGE_SPATIAL_ROLE` | `"SOURCE_COVERAGE_BOUNDARY"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `COVERAGE_STATUSES` | `frozenset( { "NOT_BOUNDARY_LIMITED", "BOUNDARY_LIMITED", "OUTSIDE_OR_CROSSING_COVERAGE", "NO_MATCH", } )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `COVERAGE_POSITIONS` | `frozenset( {"FULLY_COVERED", "OUTSIDE_OR_CROSSING_COVERAGE"} )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `PARCEL_DIAGNOSTIC_COLUMNS` | `( "grid_source_boundary_distance_m", "grid_source_coverage_position", "nearest_line_coverage_status", "nearest_exact_line_coverage_status", "nearest_post_coverage_status", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `VOLTAGE_DIAGNOSTIC_COLUMNS` | `( "source_boundary_distance_m", "coverage_status", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `COVERAGE_LINEAGE_COLUMNS` | `( "grid_source_coverage_provider", "grid_source_coverage_product", "grid_source_coverage_department_code", "grid_source_coverage_edition", "grid_source_coverage_product_version", "grid_source_coverage_archive_sha256", "grid_source_coverage_layer", "grid_source_coverage_spatial_role", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_SOURCE_LINEAGE_COLUMNS` | `( "source_provider", "source_product", "source_department_code", "source_edition", "source_product_version", "source_archive_sha256", "source_layer", "spatial_role", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_IGN_PROVIDER_IDENTITIES` | `frozenset( { "ign", "institutnationaldelinformationgeographiqueetforestiereign", } )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_SHA256_PATTERN` | `re.compile(r"^[0-9a-f]{64}$")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `GridCoverageAssessmentError`

**Purpose:** Raised when coverage diagnostics cannot be calculated safely.

**Inheritance:** `ValueError`.

**Model form and mutability:** class inheriting from `ValueError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `GridCoverageAssessmentResult`

**Purpose:** Coverage-annotated copies of both grid-proximity representations.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `parcels` | `gpd.GeoDataFrame` | `required` | Tabular/spatial evidence carried with the schema, dtype, index, geometry, and preservation contract documented in this module. |
| `voltage_level_proximity` | `pd.DataFrame` | `required` | `pd.DataFrame` state used by `src/landscout/stages/assess_grid_coverage.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `voltage_level_coverage` | `tuple[VoltageLevelCoverage, ...]` | `required` | `tuple[VoltageLevelCoverage, ...]` state used by `src/landscout/stages/assess_grid_coverage.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `source_coverage` | `IgnBdTopoDepartmentCoverage` | `required` | Source lineage or source-bound object whose exact identity is checked before downstream use. |

**Validators and methods:**

- None.

### `BoundaryDistanceProfile`

**Purpose:** Carries deterministic diagnostic/profile statistics without changing the underlying evidence rows.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `count` | `int` | `required` | `int` state used by `src/landscout/stages/assess_grid_coverage.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `minimum` | `float` | `required` | `float` state used by `src/landscout/stages/assess_grid_coverage.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `p01` | `float` | `required` | `float` state used by `src/landscout/stages/assess_grid_coverage.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `p05` | `float` | `required` | `float` state used by `src/landscout/stages/assess_grid_coverage.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `p10` | `float` | `required` | `float` state used by `src/landscout/stages/assess_grid_coverage.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `p25` | `float` | `required` | `float` state used by `src/landscout/stages/assess_grid_coverage.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `p50` | `float` | `required` | `float` state used by `src/landscout/stages/assess_grid_coverage.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `p75` | `float` | `required` | `float` state used by `src/landscout/stages/assess_grid_coverage.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `p90` | `float` | `required` | `float` state used by `src/landscout/stages/assess_grid_coverage.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `p95` | `float` | `required` | `float` state used by `src/landscout/stages/assess_grid_coverage.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `p99` | `float` | `required` | `float` state used by `src/landscout/stages/assess_grid_coverage.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `maximum` | `float` | `required` | `float` state used by `src/landscout/stages/assess_grid_coverage.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `CoverageStatusCounts`

**Purpose:** Carries source-coverage or diagnostic coverage evidence under the exact fields below.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `not_boundary_limited` | `int` | `required` | `int` state used by `src/landscout/stages/assess_grid_coverage.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `boundary_limited` | `int` | `required` | `int` state used by `src/landscout/stages/assess_grid_coverage.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `outside_or_crossing_coverage` | `int` | `required` | `int` state used by `src/landscout/stages/assess_grid_coverage.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `no_match` | `int` | `required` | `int` state used by `src/landscout/stages/assess_grid_coverage.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `VoltageCoverageStatusProfile`

**Purpose:** Carries deterministic diagnostic/profile statistics without changing the underlying evidence rows.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `voltage_kv` | `float` | `required` | `float` state used by `src/landscout/stages/assess_grid_coverage.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `parcel_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `statuses` | `CoverageStatusCounts` | `required` | `CoverageStatusCounts` state used by `src/landscout/stages/assess_grid_coverage.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `GridCoverageProfile`

**Purpose:** Carries deterministic diagnostic/profile statistics without changing the underlying evidence rows.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `parcel_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `fully_covered_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `outside_or_crossing_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `boundary_distance` | `BoundaryDistanceProfile` | `required` | `BoundaryDistanceProfile` state used by `src/landscout/stages/assess_grid_coverage.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `nearest_line` | `CoverageStatusCounts` | `required` | `CoverageStatusCounts` state used by `src/landscout/stages/assess_grid_coverage.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `nearest_exact_line` | `CoverageStatusCounts` | `required` | `CoverageStatusCounts` state used by `src/landscout/stages/assess_grid_coverage.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `nearest_post` | `CoverageStatusCounts` | `required` | `CoverageStatusCounts` state used by `src/landscout/stages/assess_grid_coverage.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `voltage_levels` | `tuple[VoltageCoverageStatusProfile, ...]` | `required` | `tuple[VoltageCoverageStatusProfile, ...]` state used by `src/landscout/stages/assess_grid_coverage.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

## 6. Functions and methods

### `_validated_lambert93`

**Signature**

```python
def _validated_lambert93(value: object, label: str) -> CRS:
```

**Purpose**

Validates and returns canonical lambert93 according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `CRS`. Observed return expression(s): `crs`.

**Algorithm**

1. Checks `value is None`. When true: Raises `GridCoverageAssessmentError(f'{label} CRS is required')`.
2. Runs guarded operation: Computes `crs` from `CRS.from_user_input(value)`. Handles `Exception`.
3. Computes `expected` from `CRS.from_epsg(2154)`.
4. Checks `not crs.is_projected or not crs.equals(expected)`. When true: Raises `GridCoverageAssessmentError(f'{label} must use EPSG:2154')`.
5. Returns `crs`.

**Validation and invariants**

- Rejects or diverts the path when `value is None` is true.
- Rejects or diverts the path when `not crs.is_projected or not crs.equals(expected)` is true.

**Exceptions**

- Explicitly raises: `GridCoverageAssessmentError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `CRS.from_epsg`, `CRS.from_user_input`, `GridCoverageAssessmentError`, `crs.equals`.

**Known repository callers**

- `src/landscout/stages/assess_grid_coverage.py` — `_validate_coverage_summary`
- `src/landscout/stages/assess_grid_coverage.py` — `_validate_source_coverage`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_normalized_identity`

**Signature**

```python
def _normalized_identity(value: object, label: str) -> str:
```

**Purpose**

Implements normalized identity according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `''.join((character for character in decomposed.casefold() if character.isalnum()))`.

**Algorithm**

1. Checks `not isinstance(value, str) or not value or value != value.strip()`. When true: Raises `GridCoverageAssessmentError(f'Department coverage {label} must be a non-empty exact string')`.
2. Computes `decomposed` from `unicodedata.normalize('NFKD', value)`.
3. Returns `''.join((character for character in decomposed.casefold() if character.isalnum()))`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(value, str) or not value or value != value.strip()` is true.

**Exceptions**

- Explicitly raises: `GridCoverageAssessmentError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `''.join`, `GridCoverageAssessmentError`, `character.isalnum`, `decomposed.casefold`, `isinstance`, `unicodedata.normalize`, `value.strip`.

**Known repository callers**

- `src/landscout/stages/assess_grid_coverage.py` — `_validate_configured_coverage_identity`
- `src/landscout/stages/assess_grid_coverage.py` — `_validate_source_coverage`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_strict_nonnegative_integer`

**Signature**

```python
def _strict_nonnegative_integer(value: object, label: str) -> int:
```

**Purpose**

Implements strict nonnegative integer according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `int`. Observed return expression(s): `value`.

**Algorithm**

1. Checks `type(value) is not int or value < 0`. When true: Raises `GridCoverageAssessmentError(f'Department coverage summary {label} must be a non-negative integer')`.
2. Returns `value`.

**Validation and invariants**

- Rejects or diverts the path when `type(value) is not int or value < 0` is true.

**Exceptions**

- Explicitly raises: `GridCoverageAssessmentError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GridCoverageAssessmentError`, `type`.

**Known repository callers**

- `src/landscout/stages/assess_grid_coverage.py` — `_validate_coverage_summary`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_coverage_summary`

**Signature**

```python
def _validate_coverage_summary(
    source: IgnBdTopoDepartmentCoverage,
    frame: gpd.GeoDataFrame,
) -> None:
```

**Purpose**

Validates and rejects malformed coverage summary according to the exact implementation and guards in this file.

**Inputs**

- `source` (`IgnBdTopoDepartmentCoverage`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `summary` from `source.summary`.
2. Checks `type(summary) is not IgnBdTopoCoverageLayerSummary`. When true: Raises `GridCoverageAssessmentError('Department coverage summary type is invalid')`.
3. Checks `summary.source_layer_name != source.source_layer`. When true: Raises `GridCoverageAssessmentError('Department coverage summary layer does not match source lineage')`.
4. Computes `summary_crs` from `_validated_lambert93(summary.crs, 'Department coverage summary')`.
5. Computes `frame_crs` from `_validated_lambert93(frame.crs, 'Department coverage')`.
6. Checks `not summary_crs.equals(frame_crs)`. When true: Raises `GridCoverageAssessmentError('Department coverage summary CRS does not match the selected frame')`.
7. Checks `type(summary.selected_feature_count) is not int or summary.selected_feature_count != len(frame)`. When true: Raises `GridCoverageAssessmentError('Department coverage summary selected feature count does not match frame')`.
8. Computes `source_count` from `_strict_nonnegative_integer(summary.source_feature_count, 'source_feature_count')`.
9. Checks `source_count < summary.selected_feature_count`. When true: Raises `GridCoverageAssessmentError('Department coverage summary source count is smaller than selected count')`.
10. Checks `type(summary.columns) is not tuple or not summary.columns or any((not isinstance(column, str) or not column or column != column.strip() for column in summary.columns)) or (len(set(summary.columns)) != len(summary.columns))`. When true: Raises `GridCoverageAssessmentError('Department coverage summary columns are invalid')`.
11. Computes `expected_frame_columns` from `(*summary.columns, *_SOURCE_LINEAGE_COLUMNS)`.
12. Checks `tuple((str(column) for column in frame.columns)) != expected_frame_columns`. When true: Raises `GridCoverageAssessmentError('Department coverage summary ordered columns do not match frame')`.
13. Computes `observed_dtypes` from `tuple(((column, str(frame[column].dtype)) for column in summary.columns))`.
14. Checks `type(summary.dtypes) is not tuple or summary.dtypes != observed_dtypes`. When true: Raises `GridCoverageAssessmentError('Department coverage summary ordered dtypes do not match frame')`.
15. Computes `geometry_counts` from `(_strict_nonnegative_integer(summary.null_geometry_count, 'null_geometry_count'), _strict_nonnegative_integer(summary.empty_geometry_count, 'empty_geometry_count'), _strict_nonnegative_integer(summary.invalid_geometry_count, 'invalid_geometry_count'))`.
16. Checks `any((count > source_count for count in geometry_counts))`. When true: Raises `GridCoverageAssessmentError('Department coverage summary geometry count exceeds source count')`.
17. Computes `geometry_types` from `summary.geometry_types`.
18. Checks `type(geometry_types) is not tuple or geometry_types != tuple(sorted(set(geometry_types))) or (not set(geometry_types) <= {'Polygon', 'MultiPolygon'})`. When true: Raises `GridCoverageAssessmentError('Department coverage summary geometry types are invalid')`.
19. Computes `selected_geometry` from `frame.geometry`.
20. Computes `selected_counts` from `(int(selected_geometry.isna().sum()), int((~selected_geometry.isna() & selected_geometry.is_empty).sum()), int((~selected_geometry.isna() & ~selected_geometry.is_empty & ~selected_geometry.is_valid).sum()))`.
21. Computes `selected_types` from `tuple(sorted((str(value) for value in selected_geometry.geom_type.dropna().unique())))`.
22. Checks `source_count == summary.selected_feature_count and (geometry_counts != selected_counts or geometry_types != selected_types)`. When true: Raises `GridCoverageAssessmentError('Department coverage summary geometry facts do not match frame')`.
23. Checks `any((observed > reported for observed, reported in zip(selected_counts, geometry_counts, strict=True))) or not set(selected_types) <= set(geometry_types)`. When true: Raises `GridCoverageAssessmentError('Department coverage selected geometry contradicts source summary')`.
24. Computes `department_field` from `summary.department_code_field`.
25. Checks `not isinstance(department_field, str) or not department_field or department_field != department_field.strip() or (department_field not in summary.columns)`. When true: Raises `GridCoverageAssessmentError('Department coverage summary department field is invalid')`.
26. Checks `summary.selected_department_code != source.source_department_code`. When true: Raises `GridCoverageAssessmentError('Department coverage summary selected department code is inconsistent')`.
27. Checks `not frame[department_field].eq(source.source_department_code).all()`. When true: Raises `GridCoverageAssessmentError('Department coverage selected department field is inconsistent')`.
28. Checks `summary.spatial_role != source.spatial_role`. When true: Raises `GridCoverageAssessmentError('Department coverage summary spatial role is inconsistent')`.

**Validation and invariants**

- Rejects or diverts the path when `type(summary) is not IgnBdTopoCoverageLayerSummary` is true.
- Rejects or diverts the path when `summary.source_layer_name != source.source_layer` is true.
- Rejects or diverts the path when `not summary_crs.equals(frame_crs)` is true.
- Rejects or diverts the path when `type(summary.selected_feature_count) is not int or summary.selected_feature_count != len(frame)` is true.
- Rejects or diverts the path when `source_count < summary.selected_feature_count` is true.
- Rejects or diverts the path when `type(summary.columns) is not tuple or not summary.columns or any((not isinstance(column, str) or not column or column != column.strip() for column in summary.columns)) or (len(set(summary.columns)) != len(summary.columns))` is true.
- Rejects or diverts the path when `tuple((str(column) for column in frame.columns)) != expected_frame_columns` is true.
- Rejects or diverts the path when `type(summary.dtypes) is not tuple or summary.dtypes != observed_dtypes` is true.
- Rejects or diverts the path when `any((count > source_count for count in geometry_counts))` is true.
- Rejects or diverts the path when `type(geometry_types) is not tuple or geometry_types != tuple(sorted(set(geometry_types))) or (not set(geometry_types) <= {'Polygon', 'MultiPolygon'})` is true.
- Rejects or diverts the path when `source_count == summary.selected_feature_count and (geometry_counts != selected_counts or geometry_types != selected_types)` is true.
- Rejects or diverts the path when `any((observed > reported for observed, reported in zip(selected_counts, geometry_counts, strict=True))) or not set(selected_types) <= set(geometry_types)` is true.
- Rejects or diverts the path when `not isinstance(department_field, str) or not department_field or department_field != department_field.strip() or (department_field not in summary.columns)` is true.
- Rejects or diverts the path when `summary.selected_department_code != source.source_department_code` is true.
- Rejects or diverts the path when `not frame[department_field].eq(source.source_department_code).all()` is true.
- Rejects or diverts the path when `summary.spatial_role != source.spatial_role` is true.

**Exceptions**

- Explicitly raises: `GridCoverageAssessmentError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `(~selected_geometry.isna() & selected_geometry.is_empty).sum`, `(~selected_geometry.isna() & ~selected_geometry.is_empty & ~selected_geometry.is_valid).sum`, `GridCoverageAssessmentError`, `_strict_nonnegative_integer`, `_validated_lambert93`, `any`, `column.strip`, `department_field.strip`, `frame[department_field].eq`, `frame[department_field].eq(source.source_department_code).all`, `int`, `isinstance`, `len`, `selected_geometry.geom_type.dropna`, `selected_geometry.geom_type.dropna().unique`, `selected_geometry.isna`, `selected_geometry.isna().sum`, `set`, `sorted`, `str`, `summary_crs.equals`, `tuple`, `type`, `zip`.

**Known repository callers**

- `src/landscout/stages/assess_grid_coverage.py` — `_validate_source_coverage`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_source_coverage`

**Signature**

```python
def _validate_source_coverage(
    source: IgnBdTopoDepartmentCoverage,
) -> gpd.GeoDataFrame:
```

**Purpose**

Validates and rejects malformed source coverage according to the exact implementation and guards in this file.

**Inputs**

- `source` (`IgnBdTopoDepartmentCoverage`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `frame`.

**Algorithm**

1. Checks `type(source) is not IgnBdTopoDepartmentCoverage`. When true: Raises `GridCoverageAssessmentError('Department coverage source type is invalid')`.
2. Checks `source.spatial_role != COVERAGE_SPATIAL_ROLE`. When true: Raises `GridCoverageAssessmentError('Department coverage spatial_role must be SOURCE_COVERAGE_BOUNDARY')`.
3. Iterates `(label, value)` over `(('source_provider', source.source_provider), ('source_product', source.source_product), ('source_department_code', source.source_department_code), ('source_edition', source.source_edition), ('source_archive_sha256', source.source_archive_sha256), ('source_layer', source.source_layer))`. For each value: Checks `not isinstance(value, str) or not value or value != value.strip()`. When true: Raises `GridCoverageAssessmentError(f'Department coverage {label} must be a non-empty exact string')`.
4. Computes `provider` from `_normalized_identity(source.source_provider, 'source_provider')`.
5. Computes `product` from `_normalized_identity(source.source_product, 'source_product')`.
6. Checks `provider not in _IGN_PROVIDER_IDENTITIES`. When true: Raises `GridCoverageAssessmentError('Department coverage provider is not an IGN identity')`.
7. Checks `product != 'bdtopo'`. When true: Raises `GridCoverageAssessmentError('Department coverage product is not BD TOPO')`.
8. Checks `_SHA256_PATTERN.fullmatch(source.source_archive_sha256) is None`. When true: Raises `GridCoverageAssessmentError('Department coverage archive SHA256 is invalid')`.
9. Computes `frame` from `source.coverage`.
10. Checks `not isinstance(frame, gpd.GeoDataFrame)`. When true: Raises `GridCoverageAssessmentError('Department coverage must be a GeoDataFrame')`.
11. Checks `'geometry' not in frame.columns or frame.active_geometry_name != 'geometry'`. When true: Raises `GridCoverageAssessmentError('Department coverage geometry column must exist and be active')`.
12. Calls `_validated_lambert93(frame.crs, 'Department coverage')` for its validation or side effect.
13. Checks `len(frame) != 1`. When true: Raises `GridCoverageAssessmentError('Department coverage must contain exactly one selected feature')`.
14. Computes `geometry` from `frame.geometry`.
15. Checks `geometry.isna().any()`. When true: Raises `GridCoverageAssessmentError('Department coverage geometry must not be null')`.
16. Checks `geometry.is_empty.any()`. When true: Raises `GridCoverageAssessmentError('Department coverage geometry must not be empty')`.
17. Checks `not geometry.is_valid.all()`. When true: Raises `GridCoverageAssessmentError('Department coverage geometry must be valid')`.
18. Checks `not set(geometry.geom_type.dropna()) <= {'Polygon', 'MultiPolygon'}`. When true: Raises `GridCoverageAssessmentError('Department coverage geometry must be Polygon or MultiPolygon')`.
19. Calls `_validate_coverage_summary(source, frame)` for its validation or side effect.
20. Defines `expected_lineage` with annotation `dict[str, object]` from `{'source_provider': source.source_provider, 'source_product': source.source_product, 'source_department_code': source.source_department_code, 'source_edition': source.source_edition, 'source_product_version': source.source_product_version, 'source_archive_sha256': source.source_archive_sha256, 'source_layer': source.s…`.
21. Computes `missing` from `set(expected_lineage) - set(frame.columns)`.
22. Checks `missing`. When true: Raises `GridCoverageAssessmentError('Department coverage lineage columns are missing: ' + ', '.join(sorted(missing)))`.
23. Iterates `(column, expected)` over `expected_lineage.items()`. For each value: Computes `actual` from `frame.iloc[0][column]`. Computes `both_null` from `pd.isna(actual) and expected is None`. Checks `not both_null and actual != expected`. When true: Raises `GridCoverageAssessmentError(f'Department coverage lineage is inconsistent: {column}')`.
24. Returns `frame`.

**Validation and invariants**

- Rejects or diverts the path when `type(source) is not IgnBdTopoDepartmentCoverage` is true.
- Rejects or diverts the path when `source.spatial_role != COVERAGE_SPATIAL_ROLE` is true.
- Rejects or diverts the path when `provider not in _IGN_PROVIDER_IDENTITIES` is true.
- Rejects or diverts the path when `product != 'bdtopo'` is true.
- Rejects or diverts the path when `_SHA256_PATTERN.fullmatch(source.source_archive_sha256) is None` is true.
- Rejects or diverts the path when `not isinstance(frame, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `'geometry' not in frame.columns or frame.active_geometry_name != 'geometry'` is true.
- Rejects or diverts the path when `len(frame) != 1` is true.
- Rejects or diverts the path when `geometry.isna().any()` is true.
- Rejects or diverts the path when `geometry.is_empty.any()` is true.
- Rejects or diverts the path when `not geometry.is_valid.all()` is true.
- Rejects or diverts the path when `not set(geometry.geom_type.dropna()) <= {'Polygon', 'MultiPolygon'}` is true.
- Rejects or diverts the path when `missing` is true.
- Rejects or diverts the path when `not isinstance(value, str) or not value or value != value.strip()` is true.
- Rejects or diverts the path when `not both_null and actual != expected` is true.

**Exceptions**

- Explicitly raises: `GridCoverageAssessmentError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `', '.join`, `GridCoverageAssessmentError`, `_SHA256_PATTERN.fullmatch`, `_normalized_identity`, `_validate_coverage_summary`, `_validated_lambert93`, `expected_lineage.items`, `geometry.geom_type.dropna`, `geometry.is_empty.any`, `geometry.is_valid.all`, `geometry.isna`, `geometry.isna().any`, `isinstance`, `len`, `pd.isna`, `set`, `sorted`, `type`, `value.strip`.

**Known repository callers**

- `src/landscout/stages/assess_grid_coverage.py` — `_assess_grid_coverage_from_proximity`
- `src/landscout/stages/assess_grid_coverage.py` — `_validate_assessment_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_configured_coverage_identity`

**Signature**

```python
def _validate_configured_coverage_identity(
    source: IgnBdTopoDepartmentCoverage,
    config: IgnBdTopoSourceConfig,
) -> None:
```

**Purpose**

Validates and rejects malformed configured coverage identity according to the exact implementation and guards in this file.

**Inputs**

- `source` (`IgnBdTopoDepartmentCoverage`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `archive` from `source.extraction.archive`.
2. Computes `expected_layer` from `_discover_department_coverage_layer(source.extraction.all_layer_names, config)`.
3. Checks `source.source_layer != expected_layer`. When true: Raises `GridCoverageAssessmentError('Department coverage does not use the configured physical layer')`.
4. Computes `expected_field` from `config.coverage.department_layer.department_code_field`.
5. Checks `source.summary.department_code_field != expected_field`. When true: Raises `GridCoverageAssessmentError('Department coverage does not use the configured department field')`.
6. Checks `archive.department_code != config.department_code`. When true: Raises `GridCoverageAssessmentError('Department coverage archive differs from the configured department')`.
7. Computes `archive_provider` from `_normalized_identity(archive.provider, 'archive provider')`.
8. Computes `config_provider` from `_normalized_identity(config.provider, 'config provider')`.
9. Checks `archive_provider not in _IGN_PROVIDER_IDENTITIES or config_provider not in _IGN_PROVIDER_IDENTITIES`. When true: Raises `GridCoverageAssessmentError('Department coverage archive provider differs from config')`.
10. Checks `_normalized_identity(archive.product, 'archive product') != 'bdtopo' or _normalized_identity(config.product, 'config product') != 'bdtopo'`. When true: Raises `GridCoverageAssessmentError('Department coverage archive product differs from config')`.

**Validation and invariants**

- Rejects or diverts the path when `source.source_layer != expected_layer` is true.
- Rejects or diverts the path when `source.summary.department_code_field != expected_field` is true.
- Rejects or diverts the path when `archive.department_code != config.department_code` is true.
- Rejects or diverts the path when `archive_provider not in _IGN_PROVIDER_IDENTITIES or config_provider not in _IGN_PROVIDER_IDENTITIES` is true.
- Rejects or diverts the path when `_normalized_identity(archive.product, 'archive product') != 'bdtopo' or _normalized_identity(config.product, 'config product') != 'bdtopo'` is true.

**Exceptions**

- Explicitly raises: `GridCoverageAssessmentError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GridCoverageAssessmentError`, `_discover_department_coverage_layer`, `_normalized_identity`.

**Known repository callers**

- `src/landscout/stages/assess_grid_coverage.py` — `_assess_grid_coverage_from_proximity`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_coverage_lineage_values`

**Signature**

```python
def _coverage_lineage_values(
    source: IgnBdTopoDepartmentCoverage,
) -> dict[str, object]:
```

**Purpose**

Implements coverage lineage values according to the exact implementation and guards in this file.

**Inputs**

- `source` (`IgnBdTopoDepartmentCoverage`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `{'grid_source_coverage_provider': source.source_provider, 'grid_source_coverage_product': source.source_product, 'grid_source_coverage_department_code': source.source_department_code, 'grid_source_coverage_edition': source.source_edition, 'grid_source_coverage_product_version': source.source_product_version, 'grid_source_coverage_archive_sha256': source.source_archive_sha256, 'grid_source_coverag…`.

**Algorithm**

1. Returns `{'grid_source_coverage_provider': source.source_provider, 'grid_source_coverage_product': source.source_product, 'grid_source_coverage_department_code': source.source_department_code, 'grid_source_coverage_edition': source.source_edition, 'grid_source_coverage_product_version': source.source_product_version, 'grid_source_coverage_archive_sha256': source.sou…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

- `src/landscout/stages/assess_grid_coverage.py` — `_assess_grid_coverage_from_proximity`
- `src/landscout/stages/assess_grid_coverage.py` — `_validate_assessment_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_proximity_source_identity`

**Signature**

```python
def _validate_proximity_source_identity(
    proximity: GridProximityResult,
    source: IgnBdTopoDepartmentCoverage,
) -> None:
```

**Purpose**

Validates and rejects malformed proximity source identity according to the exact implementation and guards in this file.

**Inputs**

- `proximity` (`GridProximityResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source` (`IgnBdTopoDepartmentCoverage`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `parcel_mappings` from `(('nearest_line_source_department_code', source.source_department_code), ('nearest_line_source_edition', source.source_edition), ('nearest_line_source_archive_sha256', source.source_archive_sha256), ('nearest_exact_line_source_department_code', source.source_department_code), ('nearest_exact_line_source_edition', sour…`.
2. Iterates `(column, expected)` over `parcel_mappings`. For each value: Computes `values` from `proximity.parcels[column].dropna()`. Checks `not values.eq(expected).all()`. When true: Raises `GridCoverageAssessmentError(f'Proximity lineage does not match department coverage: {column}')`.
3. Computes `table_mappings` from `(('source_department_code', source.source_department_code), ('source_edition', source.source_edition), ('source_archive_sha256', source.source_archive_sha256))`.
4. Iterates `(column, expected)` over `table_mappings`. For each value: Checks `not proximity.voltage_level_proximity[column].eq(expected).all()`. When true: Raises `GridCoverageAssessmentError(f'Voltage proximity lineage does not match coverage: {column}')`.

**Validation and invariants**

- Rejects or diverts the path when `not values.eq(expected).all()` is true.
- Rejects or diverts the path when `not proximity.voltage_level_proximity[column].eq(expected).all()` is true.

**Exceptions**

- Explicitly raises: `GridCoverageAssessmentError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GridCoverageAssessmentError`, `proximity.parcels[column].dropna`, `proximity.voltage_level_proximity[column].eq`, `proximity.voltage_level_proximity[column].eq(expected).all`, `values.eq`, `values.eq(expected).all`.

**Known repository callers**

- `src/landscout/stages/assess_grid_coverage.py` — `_assess_grid_coverage_from_proximity`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_finite_nonnegative`

**Signature**

```python
def _finite_nonnegative(values: pd.Series, label: str) -> np.ndarray:
```

**Purpose**

Implements finite nonnegative according to the exact implementation and guards in this file.

**Inputs**

- `values` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `np.ndarray`. Observed return expression(s): `np.asarray(converted, dtype='float64')`.

**Algorithm**

1. Defines `converted` with annotation `list[float]` from `[]`.
2. Iterates `value` over `values.tolist()`. For each value: Checks `not isinstance(value, Real) or isinstance(value, bool)`. When true: Raises `GridCoverageAssessmentError(f'{label} must be numeric')`. Runs guarded operation: Computes `numeric` from `float(value)`. Handles `(OverflowError, TypeError, ValueError)`. Checks `not isfinite(numeric) or numeric < 0`. When true: Raises `GridCoverageAssessmentError(f'{label} must be finite and non-negative')`. Executes 1 additional source-ordered statement(s).
3. Returns `np.asarray(converted, dtype='float64')`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(value, Real) or isinstance(value, bool)` is true.
- Rejects or diverts the path when `not isfinite(numeric) or numeric < 0` is true.

**Exceptions**

- Explicitly raises: `GridCoverageAssessmentError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GridCoverageAssessmentError`, `converted.append`, `float`, `isfinite`, `isinstance`, `np.asarray`, `values.tolist`.

**Known repository callers**

- `src/landscout/stages/assess_grid_coverage.py` — `_boundary_profile`
- `src/landscout/stages/assess_grid_coverage.py` — `_validate_assessment_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_coverage_statuses`

**Signature**

```python
def _coverage_statuses(
    distances: pd.Series,
    boundary_distances: np.ndarray,
    fully_covered: np.ndarray,
) -> pd.Series:
```

**Purpose**

Implements coverage statuses according to the exact implementation and guards in this file.

**Inputs**

- `distances` (`pd.Series`; required) — linear quantity, normally metres where the name ends in `_m`. Nullability and accepted values are exactly those enforced by the guards listed below.
- `boundary_distances` (`np.ndarray`; required) — linear quantity, normally metres where the name ends in `_m`. Nullability and accepted values are exactly those enforced by the guards listed below.
- `fully_covered` (`np.ndarray`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.Series`. Observed return expression(s): `pd.Series(statuses, index=distances.index, dtype='object')`.

**Algorithm**

1. Computes `numeric` from `distances.to_numpy(dtype='float64', na_value=np.nan)`.
2. Computes `matched` from `~np.isnan(numeric)`.
3. Computes `statuses` from `np.full(len(distances), 'NO_MATCH', dtype=object)`.
4. Computes `outside` from `matched & ~fully_covered`.
5. Computes `statuses[outside]` from `'OUTSIDE_OR_CROSSING_COVERAGE'`.
6. Computes `internal` from `matched & fully_covered`.
7. Computes `statuses[internal & (numeric < boundary_distances)]` from `'NOT_BOUNDARY_LIMITED'`.
8. Computes `statuses[internal & (numeric >= boundary_distances)]` from `'BOUNDARY_LIMITED'`.
9. Returns `pd.Series(statuses, index=distances.index, dtype='object')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `distances.to_numpy`, `len`, `np.full`, `np.isnan`, `pd.Series`.

**Known repository callers**

- `src/landscout/stages/assess_grid_coverage.py` — `_assess_grid_coverage_from_proximity`
- `src/landscout/stages/assess_grid_coverage.py` — `_validate_assessment_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_preserves_original_frame`

**Signature**

```python
def _preserves_original_frame(
    original: pd.DataFrame,
    output: pd.DataFrame,
    added_columns: set[str],
    label: str,
) -> None:
```

**Purpose**

Implements preserves original frame according to the exact implementation and guards in this file.

**Inputs**

- `original` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `output` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `added_columns` (`set[str]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `original_columns` from `tuple((str(column) for column in original.columns))`.
2. Checks `set(output.columns) != set(original_columns) | added_columns`. When true: Raises `GridCoverageAssessmentError(f'{label} output schema is inconsistent')`.
3. Iterates `column` over `original_columns`. For each value: Checks `column == 'geometry'`. When true: Executes `continue` control flow. Checks `not original[column].equals(output[column])`. When true: Raises `GridCoverageAssessmentError(f'{label} changed original proximity column: {column}')`.

**Validation and invariants**

- Rejects or diverts the path when `set(output.columns) != set(original_columns) | added_columns` is true.
- Rejects or diverts the path when `not original[column].equals(output[column])` is true.

**Exceptions**

- Explicitly raises: `GridCoverageAssessmentError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GridCoverageAssessmentError`, `original[column].equals`, `set`, `str`, `tuple`.

**Known repository callers**

- `src/landscout/stages/assess_grid_coverage.py` — `_assess_grid_coverage_from_proximity`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_assessment_result`

**Signature**

```python
def _validate_assessment_result(result: GridCoverageAssessmentResult) -> None:
```

**Purpose**

Validates and rejects malformed assessment result according to the exact implementation and guards in this file.

**Inputs**

- `result` (`GridCoverageAssessmentResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Calls `profile_grid_proximity(GridProximityResult(parcels=result.parcels, voltage_level_proximity=result.voltage_level_proximity, voltage_level_coverage=result.voltage_level_coverage))` for its validation or side effect.
2. Calls `_validate_source_coverage(result.source_coverage)` for its validation or side effect.
3. Computes `parcels` from `result.parcels`.
4. Computes `table` from `result.voltage_level_proximity`.
5. Computes `parcel_missing` from `(set(PARCEL_DIAGNOSTIC_COLUMNS) | set(COVERAGE_LINEAGE_COLUMNS)) - set(parcels.columns)`.
6. Computes `table_missing` from `(set(VOLTAGE_DIAGNOSTIC_COLUMNS) | set(COVERAGE_LINEAGE_COLUMNS)) - set(table.columns)`.
7. Checks `parcel_missing or table_missing`. When true: Raises `GridCoverageAssessmentError('Coverage diagnostic columns are missing')`.
8. Computes `boundary_distances` from `_finite_nonnegative(parcels['grid_source_boundary_distance_m'], 'Grid source boundary distance')`.
9. Computes `position` from `parcels['grid_source_coverage_position']`.
10. Checks `position.isna().any() or not set(position.unique()) <= COVERAGE_POSITIONS`. When true: Raises `GridCoverageAssessmentError('Coverage position values are invalid')`.
11. Computes `fully_covered` from `position.eq('FULLY_COVERED').to_numpy(dtype='bool')`.
12. Iterates `(distance_column, status_column)` over `(('nearest_line_proxy_distance_m', 'nearest_line_coverage_status'), ('nearest_exact_line_proxy_distance_m', 'nearest_exact_line_coverage_status'), ('nearest_post_proxy_distance_m', 'nearest_post_coverage_status'))`. For each value: Computes `expected` from `_coverage_statuses(parcels[distance_column], boundary_distances, fully_covered)`. Computes `actual_status` from `parcels[status_column].astype('object').reset_index(drop=True)`. Computes `expected_status` from `expected.astype('object').reset_index(drop=True)`. Executes 1 additional source-ordered statement(s).
13. Computes `boundary_by_id` from `dict(zip(parcels['parcel_id'], boundary_distances, strict=True))`.
14. Computes `fully_by_id` from `dict(zip(parcels['parcel_id'], fully_covered, strict=True))`.
15. Computes `table_boundary` from `table['parcel_id'].map(boundary_by_id).astype('float64')`.
16. Checks `not table['source_boundary_distance_m'].equals(table_boundary)`. When true: Raises `GridCoverageAssessmentError('Voltage boundary distances do not match parcel diagnostics')`.
17. Computes `table_fully` from `table['parcel_id'].map(fully_by_id).to_numpy(dtype='bool')`.
18. Computes `expected_table_status` from `_coverage_statuses(table['nearest_line_proxy_distance_m'], table_boundary.to_numpy(dtype='float64'), table_fully)`.
19. Computes `actual_table_status` from `table['coverage_status'].astype('object').reset_index(drop=True)`.
20. Computes `expected_table_status` from `expected_table_status.astype('object').reset_index(drop=True)`.
21. Checks `not actual_table_status.equals(expected_table_status)`. When true: Raises `GridCoverageAssessmentError('Voltage coverage statuses are inconsistent')`.
22. Computes `lineage` from `_coverage_lineage_values(result.source_coverage)`.
23. Iterates `(column, expected)` over `lineage.items()`. For each value: Iterates `frame` over `(parcels, table)`. For each value: Computes `values` from `frame[column]`. Checks `expected is None`. When true: Computes `valid` from `values.isna().all()`. Otherwise: Computes `valid` from `values.eq(expected).all()`. Checks `not valid`. When true: Raises `GridCoverageAssessmentError(f'Coverage diagnostic lineage is inconsistent: {column}')`.

**Validation and invariants**

- Rejects or diverts the path when `parcel_missing or table_missing` is true.
- Rejects or diverts the path when `position.isna().any() or not set(position.unique()) <= COVERAGE_POSITIONS` is true.
- Rejects or diverts the path when `not table['source_boundary_distance_m'].equals(table_boundary)` is true.
- Rejects or diverts the path when `not actual_table_status.equals(expected_table_status)` is true.
- Rejects or diverts the path when `not actual_status.equals(expected_status)` is true.
- Rejects or diverts the path when `not valid` is true.

**Exceptions**

- Explicitly raises: `GridCoverageAssessmentError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GridCoverageAssessmentError`, `GridProximityResult`, `_coverage_lineage_values`, `_coverage_statuses`, `_finite_nonnegative`, `_validate_source_coverage`, `actual_status.equals`, `actual_table_status.equals`, `dict`, `expected.astype`, `expected.astype('object').reset_index`, `expected_table_status.astype`, `expected_table_status.astype('object').reset_index`, `lineage.items`, `parcels[status_column].astype`, `parcels[status_column].astype('object').reset_index`, `position.eq`, `position.eq('FULLY_COVERED').to_numpy`, `position.isna`, `position.isna().any`, `position.unique`, `profile_grid_proximity`, `set`, `table['coverage_status'].astype`, `table['coverage_status'].astype('object').reset_index`, `table['parcel_id'].map`, `table['parcel_id'].map(boundary_by_id).astype`, `table['parcel_id'].map(fully_by_id).to_numpy`, `table['source_boundary_distance_m'].equals`, `table_boundary.to_numpy`, `values.eq`, `values.eq(expected).all`, `values.isna`, `values.isna().all`, `zip`.

**Known repository callers**

- `src/landscout/stages/assess_grid_coverage.py` — `_assess_grid_coverage_from_proximity`
- `src/landscout/stages/assess_grid_coverage.py` — `profile_grid_coverage`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_assess_grid_coverage_from_proximity`

**Signature**

```python
def _assess_grid_coverage_from_proximity(
    proximity_result: GridProximityResult,
    department_coverage: IgnBdTopoDepartmentCoverage,
    config: IgnBdTopoSourceConfig,
) -> GridCoverageAssessmentResult:
```

**Purpose**

Classify proximity results against one loaded department boundary. All geometry operations use planar XY copies in EPSG:2154. A parcel that touches or crosses the source boundary is handled conservatively as not fully covered. No parcel, proximity match, or source geometry is mutated.

**Inputs**

- `proximity_result` (`GridProximityResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `department_coverage` (`IgnBdTopoDepartmentCoverage`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GridCoverageAssessmentResult`. Observed return expression(s): `result`.

**Algorithm**

1. Calls `profile_grid_proximity(proximity_result)` for its validation or side effect.
2. Computes `coverage_frame` from `_validate_source_coverage(department_coverage)`.
3. Calls `_validate_configured_coverage_identity(department_coverage, config)` for its validation or side effect.
4. Calls `_validate_proximity_source_identity(proximity_result, department_coverage)` for its validation or side effect.
5. Computes `source_parcels` from `proximity_result.parcels`.
6. Computes `source_table` from `proximity_result.voltage_level_proximity`.
7. Computes `output_parcels` from `source_parcels.copy()`.
8. Computes `output_table` from `source_table.copy()`.
9. Computes `calculation_parcels` from `source_parcels.to_crs(CALCULATION_CRS)`.
10. Computes `parcel_geometries` from `np.asarray(force_2d(np.asarray(calculation_parcels.geometry.array, dtype=object)), dtype=object)`.
11. Computes `coverage_geometry` from `force_2d(coverage_frame.geometry.iloc[0])`.
12. Computes `coverage_boundary` from `boundary(coverage_geometry)`.
13. Computes `covered` from `np.asarray(covers(coverage_geometry, parcel_geometries), dtype='bool')`.
14. Computes `touches_boundary` from `np.asarray(intersects(parcel_geometries, coverage_boundary), dtype='bool')`.
15. Computes `fully_covered` from `covered & ~touches_boundary`.
16. Computes `measured_boundary` from `np.asarray(distance(parcel_geometries, coverage_boundary), dtype='float64')`.
17. Checks `not np.isfinite(measured_boundary).all() or (measured_boundary < 0).any()`. When true: Raises `GridCoverageAssessmentError('Calculated coverage boundary distances must be finite and non-negative')`.
18. Computes `boundary_distances` from `np.where(fully_covered, measured_boundary, 0.0)`.
19. Computes `output_parcels['grid_source_boundary_distance_m']` from `boundary_distances`.
20. Computes `output_parcels['grid_source_coverage_position']` from `np.where(fully_covered, 'FULLY_COVERED', 'OUTSIDE_OR_CROSSING_COVERAGE')`.
21. Computes `output_parcels['nearest_line_coverage_status']` from `_coverage_statuses(output_parcels['nearest_line_proxy_distance_m'], boundary_distances, fully_covered)`.
22. Computes `output_parcels['nearest_exact_line_coverage_status']` from `_coverage_statuses(output_parcels['nearest_exact_line_proxy_distance_m'], boundary_distances, fully_covered)`.
23. Computes `output_parcels['nearest_post_coverage_status']` from `_coverage_statuses(output_parcels['nearest_post_proxy_distance_m'], boundary_distances, fully_covered)`.
24. Computes `boundary_by_id` from `dict(zip(output_parcels['parcel_id'], boundary_distances, strict=True))`.
25. Computes `covered_by_id` from `dict(zip(output_parcels['parcel_id'], fully_covered, strict=True))`.
26. Computes `output_table['source_boundary_distance_m']` from `output_table['parcel_id'].map(boundary_by_id).astype('float64')`.
27. Computes `table_fully_covered` from `output_table['parcel_id'].map(covered_by_id).to_numpy(dtype='bool')`.
28. Computes `output_table['coverage_status']` from `_coverage_statuses(output_table['nearest_line_proxy_distance_m'], output_table['source_boundary_distance_m'].to_numpy(dtype='float64'), table_fully_covered)`.
29. Computes `lineage` from `_coverage_lineage_values(department_coverage)`.
30. Iterates `(column, value)` over `lineage.items()`. For each value: Computes `output_parcels[column]` from `value`. Computes `output_table[column]` from `value`.
31. Calls `_preserves_original_frame(source_parcels, output_parcels, set(PARCEL_DIAGNOSTIC_COLUMNS) | set(COVERAGE_LINEAGE_COLUMNS), 'Parcel proximity')` for its validation or side effect.
32. Calls `_preserves_original_frame(source_table, output_table, set(VOLTAGE_DIAGNOSTIC_COLUMNS) | set(COVERAGE_LINEAGE_COLUMNS), 'Voltage proximity')` for its validation or side effect.
33. Checks `not output_parcels.geometry.geom_equals_exact(source_parcels.geometry, tolerance=0, align=False).all()`. When true: Raises `GridCoverageAssessmentError('Coverage assessment changed parcel geometry')`.
34. Checks `output_parcels.crs is None or source_parcels.crs is None`. When true: Raises `GridCoverageAssessmentError('Parcel CRS is required')`.
35. Checks `not CRS.from_user_input(output_parcels.crs).equals(CRS.from_user_input(source_parcels.crs))`. When true: Raises `GridCoverageAssessmentError('Coverage assessment changed parcel CRS')`.
36. Computes `result` from `GridCoverageAssessmentResult(parcels=output_parcels, voltage_level_proximity=output_table, voltage_level_coverage=proximity_result.voltage_level_coverage, source_coverage=department_coverage)`.
37. Calls `_validate_assessment_result(result)` for its validation or side effect.
38. Returns `result`.

**Validation and invariants**

- Rejects or diverts the path when `not np.isfinite(measured_boundary).all() or (measured_boundary < 0).any()` is true.
- Rejects or diverts the path when `not output_parcels.geometry.geom_equals_exact(source_parcels.geometry, tolerance=0, align=False).all()` is true.
- Rejects or diverts the path when `output_parcels.crs is None or source_parcels.crs is None` is true.
- Rejects or diverts the path when `not CRS.from_user_input(output_parcels.crs).equals(CRS.from_user_input(source_parcels.crs))` is true.

**Exceptions**

- Explicitly raises: `GridCoverageAssessmentError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `source_parcels.copy`, `source_parcels.to_crs`, `source_table.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `(measured_boundary < 0).any`, `CRS.from_user_input`, `CRS.from_user_input(output_parcels.crs).equals`, `GridCoverageAssessmentError`, `GridCoverageAssessmentResult`, `_coverage_lineage_values`, `_coverage_statuses`, `_preserves_original_frame`, `_validate_assessment_result`, `_validate_configured_coverage_identity`, `_validate_proximity_source_identity`, `_validate_source_coverage`, `boundary`, `covers`, `dict`, `distance`, `force_2d`, `intersects`, `lineage.items`, `np.asarray`, `np.isfinite`, `np.isfinite(measured_boundary).all`, `np.where`, `output_parcels.geometry.geom_equals_exact`, `output_parcels.geometry.geom_equals_exact(source_parcels.geometry, tolerance=0, align=False).all`, `output_table['parcel_id'].map`, `output_table['parcel_id'].map(boundary_by_id).astype`, `output_table['parcel_id'].map(covered_by_id).to_numpy`, `output_table['source_boundary_distance_m'].to_numpy`, `profile_grid_proximity`, `set`, `source_parcels.copy`, `source_parcels.to_crs`, `source_table.copy`, `zip`.

**Known repository callers**

- `src/landscout/stages/assess_grid_coverage.py` — `assess_grid_coverage`
- `tests/unit/test_assess_grid_coverage.py` — `test_assessment_preserves_proximity_values_and_does_not_mutate_input`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_assessment_reproduces_configured_logical_layer`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_rejects_arbitrary_source_identity`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_source_layer_lineage_must_match_summary_and_frame`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_summary_crs_must_match_frame`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_summary_department_field_must_be_exact`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_summary_geometry_facts_are_validated`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_summary_schema_must_match_selected_source_columns`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_summary_selected_count_must_match_frame`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_summary_selected_department_must_match`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_summary_source_count_cannot_be_smaller_than_selection`
- `tests/unit/test_assess_grid_coverage.py` — `test_geographic_parcel_storage_crs_and_geometry_are_preserved`
- `tests/unit/test_assess_grid_coverage.py` — `test_invalid_coverage_geometry_is_rejected`
- `tests/unit/test_assess_grid_coverage.py` — `test_no_exact_match_uses_explicit_no_match_status`
- `tests/unit/test_assess_grid_coverage.py` — `test_outside_crossing_or_touching_parcel_is_conservative`
- `tests/unit/test_assess_grid_coverage.py` — `test_polygonal_coverage_geometry_is_accepted`
- `tests/unit/test_assess_grid_coverage.py` — `test_profile_reports_dynamic_voltage_and_boundary_distributions`
- `tests/unit/test_assess_grid_coverage.py` — `test_proximity_and_coverage_package_lineage_must_match`
- `tests/unit/test_assess_grid_coverage.py` — `test_strict_geometric_boundary_proof`

**Tests**

- `tests/unit/test_assess_grid_coverage.py::test_assessment_preserves_proximity_values_and_does_not_mutate_input`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_rejects_arbitrary_source_identity`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_source_layer_lineage_must_match_summary_and_frame`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_crs_must_match_frame`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_department_field_must_be_exact`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_geometry_facts_are_validated`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_schema_must_match_selected_source_columns`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_selected_count_must_match_frame`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_selected_department_must_match`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_source_count_cannot_be_smaller_than_selection`
- `tests/unit/test_assess_grid_coverage.py::test_geographic_parcel_storage_crs_and_geometry_are_preserved`
- `tests/unit/test_assess_grid_coverage.py::test_invalid_coverage_geometry_is_rejected`
- `tests/unit/test_assess_grid_coverage.py::test_no_exact_match_uses_explicit_no_match_status`
- `tests/unit/test_assess_grid_coverage.py::test_outside_crossing_or_touching_parcel_is_conservative`
- `tests/unit/test_assess_grid_coverage.py::test_polygonal_coverage_geometry_is_accepted`
- `tests/unit/test_assess_grid_coverage.py::test_profile_reports_dynamic_voltage_and_boundary_distributions`
- `tests/unit/test_assess_grid_coverage.py::test_proximity_and_coverage_package_lineage_must_match`
- `tests/unit/test_assess_grid_coverage.py::test_strict_geometric_boundary_proof`

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `assess_grid_coverage`

**Signature**

```python
def assess_grid_coverage(
    parcels: gpd.GeoDataFrame,
    electricity_source: IgnBdTopoElectricityData,
    source_config: IgnBdTopoSourceConfig,
) -> GridCoverageAssessmentResult:
```

**Purpose**

Diagnose source-complete grid proximity against configured coverage.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `electricity_source` (`IgnBdTopoElectricityData`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GridCoverageAssessmentResult`. Observed return expression(s): `_assess_grid_coverage_from_proximity(proximity, coverage, source_config)`.

**Algorithm**

1. Runs guarded operation: Checks `not isinstance(parcels, gpd.GeoDataFrame)`. When true: Raises `GridCoverageAssessmentError('parcels must be a GeoDataFrame with active geometry')`. Checks `type(electricity_source) is not IgnBdTopoElectricityData`. When true: Raises `GridCoverageAssessmentError('electricity source must be an IgnBdTopoElectricityData')`. Checks `type(source_config) is not IgnBdTopoSourceConfig`. When true: Raises `GridCoverageAssessmentError('source_config must be an IgnBdTopoSourceConfig')`. Computes `proximity` from `enrich_parcel_grid_proximity(parcels, electricity_source, source_config)`. Executes 3 additional source-ordered statement(s). Handles `GridCoverageAssessmentError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(parcels, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `type(electricity_source) is not IgnBdTopoElectricityData` is true.
- Rejects or diverts the path when `type(source_config) is not IgnBdTopoSourceConfig` is true.
- Rejects or diverts the path when `coverage.extraction is not electricity_source.extraction` is true.

**Exceptions**

- Explicitly raises: `GridCoverageAssessmentError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `load_ign_bdtopo_department_coverage`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GridCoverageAssessmentError`, `_assess_grid_coverage_from_proximity`, `enrich_parcel_grid_proximity`, `isinstance`, `load_ign_bdtopo_department_coverage`, `type`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_status_counts`

**Signature**

```python
def _status_counts(values: pd.Series) -> CoverageStatusCounts:
```

**Purpose**

Implements status counts according to the exact implementation and guards in this file.

**Inputs**

- `values` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `CoverageStatusCounts`. Observed return expression(s): `CoverageStatusCounts(not_boundary_limited=int(counts.get('NOT_BOUNDARY_LIMITED', 0)), boundary_limited=int(counts.get('BOUNDARY_LIMITED', 0)), outside_or_crossing_coverage=int(counts.get('OUTSIDE_OR_CROSSING_COVERAGE', 0)), no_match=int(counts.get('NO_MATCH', 0)))`.

**Algorithm**

1. Computes `counts` from `values.value_counts()`.
2. Returns `CoverageStatusCounts(not_boundary_limited=int(counts.get('NOT_BOUNDARY_LIMITED', 0)), boundary_limited=int(counts.get('BOUNDARY_LIMITED', 0)), outside_or_crossing_coverage=int(counts.get('OUTSIDE_OR_CROSSING_COVERAGE', 0)), no_match=int(counts.get('NO_MATCH', 0)))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `CoverageStatusCounts`, `counts.get`, `int`, `values.value_counts`.

**Known repository callers**

- `src/landscout/stages/assess_grid_coverage.py` — `profile_grid_coverage`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_boundary_profile`

**Signature**

```python
def _boundary_profile(values: pd.Series) -> BoundaryDistanceProfile:
```

**Purpose**

Implements boundary profile according to the exact implementation and guards in this file.

**Inputs**

- `values` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BoundaryDistanceProfile`. Observed return expression(s): `BoundaryDistanceProfile(count=len(series), minimum=float(series.min()), p01=float(series.quantile(0.01)), p05=float(series.quantile(0.05)), p10=float(series.quantile(0.1)), p25=float(series.quantile(0.25)), p50=float(series.quantile(0.5)), p75=float(series.quantile(0.75)), p90=float(series.quantile(0.9)), p95=float(series.quantile(0.95)), p99=float(series.quantile(0.99)), maximum=float(series.max…`.

**Algorithm**

1. Computes `numeric` from `_finite_nonnegative(values, 'Grid source boundary distance')`.
2. Checks `len(numeric) == 0`. When true: Raises `GridCoverageAssessmentError('Cannot profile an empty parcel coverage assessment')`.
3. Computes `series` from `pd.Series(numeric, dtype='float64')`.
4. Returns `BoundaryDistanceProfile(count=len(series), minimum=float(series.min()), p01=float(series.quantile(0.01)), p05=float(series.quantile(0.05)), p10=float(series.quantile(0.1)), p25=float(series.quantile(0.25)), p50=float(series.quantile(0.5)), p75=float(series.quantile(0.75)), p90=float(series.quantile(0.9)), p95=float(series.quantile(0.95)), p99=float(series.q…`.

**Validation and invariants**

- Rejects or diverts the path when `len(numeric) == 0` is true.

**Exceptions**

- Explicitly raises: `GridCoverageAssessmentError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BoundaryDistanceProfile`, `GridCoverageAssessmentError`, `_finite_nonnegative`, `float`, `len`, `pd.Series`, `series.max`, `series.min`, `series.quantile`.

**Known repository callers**

- `src/landscout/stages/assess_grid_coverage.py` — `profile_grid_coverage`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `profile_grid_coverage`

**Signature**

```python
def profile_grid_coverage(
    result: GridCoverageAssessmentResult,
) -> GridCoverageProfile:
```

**Purpose**

Summarize boundary diagnostics without suitability thresholds.

**Inputs**

- `result` (`GridCoverageAssessmentResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GridCoverageProfile`. Observed return expression(s): `GridCoverageProfile(parcel_count=len(parcels), fully_covered_count=int(position_counts.get('FULLY_COVERED', 0)), outside_or_crossing_count=int(position_counts.get('OUTSIDE_OR_CROSSING_COVERAGE', 0)), boundary_distance=_boundary_profile(parcels['grid_source_boundary_distance_m']), nearest_line=_status_counts(parcels['nearest_line_coverage_status']), nearest_exact_line=_status_counts(parcels['neare…`.

**Algorithm**

1. Calls `_validate_assessment_result(result)` for its validation or side effect.
2. Computes `parcels` from `result.parcels`.
3. Computes `position_counts` from `parcels['grid_source_coverage_position'].value_counts()`.
4. Defines `voltage_profiles` with annotation `list[VoltageCoverageStatusProfile]` from `[]`.
5. Iterates `item` over `result.voltage_level_coverage`. For each value: Computes `rows` from `result.voltage_level_proximity.loc[result.voltage_level_proximity['voltage_kv'] == item.voltage_kv]`. Calls `voltage_profiles.append(VoltageCoverageStatusProfile(voltage_kv=float(item.voltage_kv), parcel_count=len(rows), statuses=_status_counts(rows['coverage_status'])))` for its validation or side effect.
6. Returns `GridCoverageProfile(parcel_count=len(parcels), fully_covered_count=int(position_counts.get('FULLY_COVERED', 0)), outside_or_crossing_count=int(position_counts.get('OUTSIDE_OR_CROSSING_COVERAGE', 0)), boundary_distance=_boundary_profile(parcels['grid_source_boundary_distance_m']), nearest_line=_status_counts(parcels['nearest_line_coverage_status']), nearest_…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GridCoverageProfile`, `VoltageCoverageStatusProfile`, `_boundary_profile`, `_status_counts`, `_validate_assessment_result`, `float`, `int`, `len`, `parcels['grid_source_coverage_position'].value_counts`, `position_counts.get`, `tuple`, `voltage_profiles.append`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `BOUNDARY_LIMITED` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `FULLY_COVERED` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `NOT_BOUNDARY_LIMITED` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `NO_MATCH` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `OUTSIDE_OR_CROSSING_COVERAGE` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `coverage_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `grid_source_boundary_distance_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `grid_source_coverage_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `grid_source_coverage_department_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `grid_source_coverage_edition` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `grid_source_coverage_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `grid_source_coverage_position` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `grid_source_coverage_product` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `grid_source_coverage_product_version` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `grid_source_coverage_provider` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `grid_source_coverage_spatial_role` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_exact_line_coverage_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_exact_line_proxy_distance_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_line_coverage_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_line_proxy_distance_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_post_coverage_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_post_proxy_distance_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `source_boundary_distance_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `source_department_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_edition` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_product` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_product_version` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_provider` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `spatial_role` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `voltage_kv` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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

This file contributes to LandScout's `grid` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.
